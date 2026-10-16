# -*- coding: utf-8 -*-
"""Notes book builder: bookdata.json -> print-ready A4 PDF with a right-hand notes column (WeasyPrint).
Usage: python3 book.py BOOKDATA.json OUT.pdf [sample|full] [sample_chapter_ids e.g. 4]
Schema: see README.md."""
import sys, os, json, re, html, base64
from weasyprint import HTML
import viz

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'bookdata.json')
OUT = sys.argv[2] if len(sys.argv) > 2 else 'book.pdf'
MODE = sys.argv[3] if len(sys.argv) > 3 else 'full'
SAMPLE_IDS = [int(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else None
BASE = os.path.dirname(os.path.abspath(DATA))
B = json.load(open(DATA, encoding='utf8'))
M = B['meta']
PRI = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
PRI.update(M.get('pri', {}))
ALL = {c['id']: c for p in B['parts'] for c in p['chapters']}

def md(t): return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html.escape(t, quote=False))
def hx(t): return re.sub(r'&(?!amp;|lt;|gt;|quot;|#)', '&amp;', t)


def split_semi(t):
    parts, cur, dp, tag = [], '', 0, False
    for ch in t:
        if ch == '<': tag = True
        elif ch == '>': tag = False
        if not tag:
            if ch == '(': dp += 1
            elif ch == ')': dp = max(0, dp - 1)
            elif ch == ';' and dp == 0:
                parts.append(cur.strip()); cur = ''; continue
        cur += ch
    if cur.strip(): parts.append(cur.strip())
    return balance(parts, '<b>', '</b>')

def balance(parts, op, cl):
    out, open_ = [], False
    for x in parts:
        if open_: x = op + x
        o, c = x.count(op), x.count(cl)
        if op == cl:
            open_ = o % 2 == 1
            if open_: x += cl
        else:
            open_ = o > c
            if open_: x += cl
        out.append(x)
    return out

def cap(s): 
    s = s.strip().rstrip('.')
    m = re.match(r'^((?:<[^>]+>)*)(.)(.*)$', s, re.S)
    return m.group(1) + m.group(2).upper() + m.group(3) if m else s

def bul(x, f=hx):
    """one bullet -> <li>, splitting semicolon lists into sub-bullets"""
    ps = split_semi(x)
    if len(ps) < 2: return '<li>%s</li>' % f(x)
    m = re.match(r'^(.{2,70}?:(?:</b>)?)\s+(.*)$', ps[0], re.S)
    if m:
        lab, first = m.group(1), m.group(2)
        items = [first] + ps[1:]
        return '<li>%s<ul class="sub">%s</ul></li>' % (f(lab), ''.join('<li>%s</li>' % f(cap(i)) for i in items))
    return ''.join('<li>%s</li>' % f(cap(i)) for i in ps)

def trim_img(path):
    from PIL import Image, ImageChops
    import io
    im = Image.open(os.path.join(BASE, path)).convert('RGB')
    bg = Image.new('RGB', im.size, (255, 255, 255))
    bb = ImageChops.difference(im, bg).point(lambda v: 255 if v > 14 else 0).getbbox()
    if bb:
        p = 18; im = im.crop((max(0, bb[0]-p), max(0, bb[1]-p), min(im.width, bb[2]+p), min(im.height, bb[3]+p)))
    o = io.BytesIO(); im.save(o, 'JPEG', quality=84)
    return base64.b64encode(o.getvalue()).decode()

def fig(f):
    return ('<figure class="%s"><img src="data:image/jpeg;base64,%s"><figcaption><b>Figure.</b> %s <span class="pg">%s</span></figcaption></figure>'
            % ('sq' if f.get('sq') else 'wide', trim_img(f['img']), hx(f['cap']), hx(f.get('pg', ''))))

def notes_html(notes, vis=()):
    out, buf = [], []
    def flush():
        if buf: out.append('<ul class="b">' + ''.join(bul(x) for x in buf) + '</ul>'); buf.clear()
    def key(it):
        t = it if isinstance(it, str) else (it.get('h') or (it['tbl']['head'][0] if 'tbl' in it else '') or it.get('p', ''))
        return re.sub(r'<[^>]+>', '', t)
    def after(it):
        k = key(it)
        for v in vis:
            if v.get('after') and v['after'] in k and not v.get('done'):
                v['done'] = True; flush(); out.append(viz.render(v))
    for it in notes:
        if isinstance(it, str):
            buf.append(it)
            if any(v.get('after') and v['after'] in key(it) and not v.get('done') for v in vis): flush(); after(it)
            continue
        flush()
        if 'h' in it: out.append('<h4>%s</h4>' % hx(it['h']))
        elif 'p' in it: out.append('<p class="np">%s</p>' % hx(it['p']))
        elif 'call' in it:
            k = it['call']
            out.append('<div class="callout %s"><span>%s</span>%s</div>' % (k.get('kind', 'note'), hx(k['tag']), ''.join('<p>%s</p>' % hx(b) for b in k['body'])))
        elif 'viz' in it: out.append(viz.render(it['viz']))
        elif 'tbl' in it:
            t = it['tbl']
            if t.get('cap'): out.append('<div class="tcap">%s</div>' % hx(t['cap']))
            out.append('<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (''.join('<th>%s</th>' % hx(h) for h in t['head']),
                ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % hx(c) for c in r) for r in t['rows'])))
        elif 'alert' in it: out.append('<div class="alert"><span>Handout alert</span>%s</div>' % hx(it['alert']))
        elif 'fig' in it: out.append(fig(it['fig']))
        after(it)
    flush()
    return ''.join(out)

def pyq_block(P):
    if not P: return ''
    h = '<div class="pyqblk"><div class="lbl">Past-year questions &middot; %s</div>' % hx(P['intro'])
    h += '<p class="kwkey"><span class="kc n">solid chip</span> keyword that appears in this chapter\'s notes &nbsp; <span class="kc q">outline chip</span> keyword taken from the question</p>'
    for g in P['groups']:
        h += '<h4>%s <span class="gc">%s</span></h4>' % (hx(g['title']), hx(g['count']))
        for q in g.get('prelims', []):
            h += '<div class="pq"><div class="pqh"><span class="yr">Prelims %s</span></div>' % hx(q['year'])
            inl = False
            for k, t in q['blocks']:
                if k == 's':
                    if not inl: h += '<ol class="pqst">'; inl = True
                    h += '<li>%s</li>' % hx(t)
                else:
                    if inl: h += '</ol>'; inl = False
                    h += '<p class="pqs">%s</p>' % hx(t)
            if inl: h += '</ol>'
            h += '<div class="opts">%s</div><p class="pqa">Answer: <b>(%s)</b> %s</p></div>' % (''.join('<div><b>(%s)</b> %s</div>' % ('abcd'[i], hx(o)) for i, o in enumerate(q['opts'])), hx(q['ans']), hx(q['anstext']))
        for m in g.get('mains', []):
            h += '<div class="mq"><div class="mqh"><span class="yr">Mains %s</span><span class="mk">%s marks</span><span class="tp">%s</span></div><p class="mqt">%s</p>' % (hx(m['year']), hx(m['marks']), hx(m['topic']), hx(m['q']))
            if m['chips']: h += '<div class="kw"><span class="kwl">Keywords</span>%s</div>' % ''.join('<span class="kc %s">%s</span>' % (c_, hx(k)) for c_, k in m['chips'])
            h += '</div>'
    return h + '</div>'

def chapter(c):
    h = '<section class="chapter" id="ch%d">' % c['id']
    h += '<div class="opener"><div class="cnum">%02d</div><div class="ctitle"><div class="ceyebrow">Chapter %d &middot; %s</div><h2>%s</h2></div></div>' % (c['id'], c['id'], hx(c.get('pages', '')), hx(c['title']))
    h += '<div class="meta"><span class="pri %s">%s priority</span><span>Mains PYQs quoted: <b>%s</b></span><span>Prelims PYQs: <b>%s</b></span></div>' % (c['priority'], PRI[c['priority']], hx(c.get('pyqs', '')), hx(c.get('prelims_pyqs', 'none quoted')))
    L = c['lens']
    h += '<div class="lens"><div class="lbl">Exam lens</div><div class="two"><div><h5>Prelims hooks</h5><ul class="b">%s</ul></div><div><h5>Mains hooks</h5><ul class="b">%s</ul></div></div><p class="close">%s</p></div>' % (
        ''.join('<li>%s</li>' % hx(x) for x in L['prelims']), ''.join('<li>%s</li>' % hx(x) for x in L['mains']), hx(L['close']))
    h += '<div class="simple"><div class="lbl">In simple words</div><ul class="b">%s</ul></div>' % ''.join(bul(x, md) for x in c['simple'])
    h += '<table class="terms"><thead><tr><th>Key term</th><th>In plain words</th></tr></thead><tbody>%s</tbody></table>' % ''.join('<tr><td><b>%s</b></td><td>%s</td></tr>' % (html.escape(a), html.escape(b)) for a, b in c['terms'])
    vis = [dict(v) for v in c.get('visuals', [])]
    h += ''.join(viz.render(v) for v in vis if v.get('pos') == 'top')
    if not any(v['type'] == 'mnemonic' for v in vis) and c.get('remember'):
        h += '<div class="remember2"><span>Remember it as</span> %s</div>' % md(c['remember'])
    h += notes_html(c['notes'], [v for v in vis if v.get('after')])
    h += pyq_block(c.get('pyq'))
    h += '<div class="endblk"><div class="lbl">End of chapter &middot; recall and drill</div>'
    if c.get('recall'):
        h += '<h4>Recall sheet: cover the right column and answer</h4><table class="recall"><tbody>%s</tbody></table>' % ''.join('<tr><td class="q">%s</td><td class="a">%s</td></tr>' % (hx(q), hx(a)) for q, a in c['recall'])
    for t in c.get('traps', []):
        h += '<div class="trap"><b>%s &middot; %s</b> %s <i>%s</i></div>' % (html.escape(t['k']), hx(t['t']), hx(t['d']), hx(t['r']))
    qs = c.get('quiz', [])
    if qs:
        h += '<h4>Quick quiz</h4>' + ''.join('<div class="mcq"><p><b>Q%d.</b> %s</p><ol type="a">%s</ol></div>' % (i + 1, hx(q['q']), ''.join('<li>%s</li>' % hx(o) for o in q['o'])) for i, q in enumerate(qs))
        h += '<p class="key">Answers: %s</p>' % ', '.join('Q%d %s' % (i + 1, 'abcd'[q['a']]) for i, q in enumerate(qs))
    return h + '</div></section>'

CSS = open(os.path.join(HERE, 'book.css'), encoding='utf8').read()

def notes_svg():
    lines = ''.join('<line x1="148" x2="196" y1="%s" y2="%s" stroke="#D9D0BC" stroke-width="0.18" stroke-dasharray="0.6 0.9"/>' % (y, y) for y in [32 + 8 * i for i in range(30)])
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">'
           '<rect x="144" y="18" width="56" height="261" rx="1.2" fill="#FBF8F0" stroke="#E4DCC8" stroke-width="0.25"/>'
           '<rect x="144" y="18" width="56" height="9" rx="1.2" fill="#CFE6DF"/>'
           '<text x="172" y="24" font-family="Inter, sans-serif" font-size="2.7" fill="#1F4E5F" text-anchor="middle" letter-spacing="0.35">MY NOTES</text>' + lines +
           '<text x="172" y="284.6" font-family="Inter, sans-serif" font-size="2.05" fill="#8B8168" text-anchor="middle" letter-spacing="0.12">CURRENT AFFAIRS  ·  DATA  ·  VALUE ADDITION</text></svg>')
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()

DECO='<svg class="deco" viewBox="0 0 210 297"><circle cx="190" cy="22" r="46" fill="#CBE7E0" opacity=".6"/><circle cx="12" cy="40" r="26" fill="#F8DDB8" opacity=".6"/><circle cx="20" cy="282" r="48" fill="#CBE7E0" opacity=".55"/><circle cx="198" cy="270" r="30" fill="#F8DDB8" opacity=".65"/></svg>'
def cover():
    return ('<section class="cover">%s<div class="cin"><div class="top">%s</div><div class="rule"></div><h1>%s</h1><div class="sub">%s</div>'
            '<svg class="mark" viewBox="0 0 120 80" width="46mm"><g fill="none" stroke="#C9A24D" stroke-width="1.8"><path d="M10 70h100M16 64h88M22 22h76M60 6l44 16H16z"/><path d="M28 28v34M44 28v34M60 28v34M76 28v34M92 28v34"/></g></svg>'
            '<div class="rule"></div><div class="mid">%s</div><div class="foot">%s</div></div></section>') % (DECO, hx(M['cover_top']), hx(M['title']), hx(M['subtitle']), hx(M['cover_mid']), hx(M['cover_foot']))

def front():
    return ('<section class="front"><div class="halftitle"><h1>%s</h1><div class="s">%s</div></div><div class="imprint">%s</div></section>'
            % (hx(M['title']), hx(M['subtitle']), ''.join('<p>%s</p>' % x for x in M['imprint'])))

PYQROW = ''
def how_to():
    global PYQROW
    PYQROW = ('<tr><td><b>Past-year questions</b></td><td>Every Prelims and Mains PYQ mapped to the chapter, grouped by topic. Mains questions carry keyword chips: solid = the keyword is in this chapter\'s notes, outline = taken from the question.</td></tr>' if any(c.get('pyq') for c in ALL.values()) else '')
    return ('<section class="howto"><h2 class="plain">How to use this book</h2><table class="terms"><thead><tr><th>Block</th><th>What it gives you</th></tr></thead><tbody>'
            '<tr><td><b>Exam lens</b></td><td>Priority (High, Medium, Low), the PYQs quoted for the chapter, and the Prelims and Mains hooks.</td></tr>'
            '<tr><td><b>In simple words</b></td><td>The chapter in a few plain lines, with the key terms explained.</td></tr>'
            '<tr><td><b>Memory visuals</b></td><td>A mnemonic, mind map, decision fork or flow chain that fixes the chapter in your head.</td></tr>'
            '<tr><td><b>Chapter notes</b></td><td>The complete content in source order: bullets, tables, figures.</td></tr>'
            '%s'
            '<tr><td><b>Recall and drill</b></td><td>Cover-and-answer questions, exam traps and a short quiz to close each chapter.</td></tr>'
            '<tr><td><b>My notes column</b></td><td>The ruled panel on the right of every page is yours: current affairs, data, value additions.</td></tr></tbody></table>'
            '<div class="legend">%s</div></section>') % (PYQROW, M.get('legend', '<span class="pri H">High</span> two or more PYQs map to the chapter &nbsp; <span class="pri M">Medium</span> one PYQ or a partial fit &nbsp; <span class="pri L">Low</span> none quoted'))

def toc(built):
    h = '<section class="toc"><h2 class="plain">Contents</h2>'
    for p in B['parts']:
        h += '<div class="tpart"><span>%s</span> %s</div>' % (hx(p['label']), hx(p['sub']))
        for c in p['chapters']:
            t = hx(c['title'])
            if c['id'] in built: h += '<a class="tl" href="#ch%d"><span class="n">%02d</span>%s</a>' % (c['id'], c['id'], t)
            else: h += '<div class="tl off"><span class="n">%02d</span>%s</div>' % (c['id'], t)
    if MODE=='full': h += '<div class="tpart"><span>Back matter</span></div><a class="tl" href="#back"><span class="n"></span>Priority and PYQ index</a>'
    return h + '</section>'

def back():
    h='<section class="back" id="back"><h2 class="plain">Priority and PYQ index</h2><p>Quick revision order. High: two or more PYQs map; Medium: one or partial; Low: none quoted in the handout.</p><table class="terms"><thead><tr><th>Ch</th><th>Chapter</th><th>Priority</th><th>Mains PYQs quoted</th></tr></thead><tbody>'
    for p in B['parts']:
        for c in p['chapters']:
            h+='<tr><td>%02d</td><td>%s</td><td><span class="pri %s">%s</span></td><td>%s</td></tr>'%(c['id'],hx(c['title']),c['priority'],PRI[c['priority']],hx(c.get('pyqs','')))
    return h+'</tbody></table></section>'

def build():
    ids = SAMPLE_IDS if MODE == 'sample' and SAMPLE_IDS else list(ALL)
    body = cover() + front() + how_to() + toc(set(ids))
    for p in B['parts']:
        chs = [c for c in p['chapters'] if c['id'] in ids]
        if not chs: continue
        pi = B['parts'].index(p)%2+1
        body += ('<section class="partop p%d"><svg class="deco" viewBox="0 0 210 297"><circle cx="195" cy="30" r="55" fill="%s" opacity=".55"/><circle cx="10" cy="270" r="60" fill="%s" opacity=".5"/><path d="M0 210 Q105 170 210 210 V297 H0Z" fill="%s" opacity=".35"/></svg><div class="pn">%s</div><h1>%s</h1><div class="rule"></div><p>%s</p></section>') % (pi, *(('#BFE3DA','#F8DDB8','#CBE7E0') if pi==1 else ('#F9D5BD','#CFE0F3','#F8DDB8')), hx(p['label']), hx(p['title']), hx(p['sub']))
        body += ''.join(chapter(c) for c in chs)
    if MODE=='full': body += back()
    css = CSS.replace('%%NOTES%%', notes_svg()).replace('%%RUNHEAD%%', M.get('running_head', M['title']))
    doc = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body>%s</body></html>' % (hx(M['title']), css, body)
    HTML(string=doc, base_url=BASE).write_pdf(OUT)
    print('wrote', OUT)

build()
