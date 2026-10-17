# -*- coding: utf-8 -*-
"""Handwritten-style print notes from the Governance book data. Usage: python3 hand.py OUT.pdf"""
import sys, os, re, json, html, base64
from weasyprint import HTML
HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(os.path.dirname(HERE), 'book')
sys.path.insert(0, BOOK); sys.path.insert(0, HERE)
import viz
from ca import CA
viz.W = 411.0
_box = viz.box
def _scaled(x, y, w, title, lines, color, size=8.1, tsize=8.9, **kw):
    return _box(x, y, w, title, lines, color, size=size * 1.22, tsize=tsize * 1.2, **kw)
viz.box = _scaled
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'Governance_handwritten.pdf')
B = json.load(open(os.path.join(BOOK, 'bookdata.json'), encoding='utf8'))
X = json.load(open(os.path.join(os.path.dirname(HERE), 'hubdata.json'), encoding='utf8'))
M = B['meta']
PYQ = {}
for q in X['PYQS']:
    for s in q['secs']: PYQ.setdefault(s, []).append(q)

def hx(t): return re.sub(r'&(?!amp;|lt;|gt;|quot;|#)', '&amp;', t)
def md(t): return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html.escape(t, quote=False))
def esc(t): return html.escape(t, quote=False)

# ---------- semicolon -> bullets (same rules as the book)
def balance(parts):
    out, open_ = [], False
    for x in parts:
        if open_: x = '<b>' + x
        o, c = x.count('<b>'), x.count('</b>')
        open_ = o > c
        if open_: x += '</b>'
        out.append(x)
    return out
def split_semi(t):
    parts, cur, dp, tag = [], '', 0, False
    for ch in t:
        if ch == '<': tag = True
        elif ch == '>': tag = False
        if not tag:
            if ch == '(': dp += 1
            elif ch == ')': dp = max(0, dp - 1)
            elif ch == ';' and dp == 0: parts.append(cur.strip()); cur = ''; continue
        cur += ch
    if cur.strip(): parts.append(cur.strip())
    return balance(parts)
def cap(s):
    s = s.strip().rstrip('.')
    m = re.match(r'^((?:<[^>]+>)*)(.)(.*)$', s, re.S)
    return m.group(1) + m.group(2).upper() + m.group(3) if m else s
def bul(x):
    ps = split_semi(x)
    if len(ps) < 2: return '<li>%s</li>' % hx(x)
    m = re.match(r'^(.{2,70}?:(?:</b>)?)\s+(.*)$', ps[0], re.S)
    if m:
        return '<li>%s<ul class="s">%s</ul></li>' % (hx(m.group(1)), ''.join('<li>%s</li>' % hx(cap(i)) for i in [m.group(2)] + ps[1:]))
    return ''.join('<li>%s</li>' % hx(cap(i)) for i in ps)

# ---------- visuals
def vis_html(v):
    if v['type'] == 'mnemonic':
        ch = ''.join('<div class="ch"><i>%s</i>%s</div>' % (esc(l[0]), esc(l[1])) for l in v['letters'])
        nt = '<div class="nt">%s</div>' % esc(v['note']) if v.get('note') else ''
        if v.get('word'):
            tiles = ''.join('<span class="tile">%s</span>' % esc(c) if c.isupper() or c.isdigit() else '<span class="sep">%s</span>' % esc(c) for c in v['word'])
            return '<div class="mn"><div class="lb">%s<small>%s</small></div><div class="tiles">%s</div><div class="hook">%s</div>%s%s</div>' % (esc(v.get('label', 'Mnemonic')), esc(v.get('title', '')), tiles, esc(v['hook']), ch, nt)
        return '<div class="mn"><div class="lb">Mnemonic<small>%s</small></div><div class="hook" style="font-size:15pt">%s</div>%s%s</div>' % (esc(v.get('title', '')), esc(v['sentence']), ch, nt)
    s = viz.render(dict(v))
    s = s.replace('Inter,sans-serif', 'HPH,cursive').replace('#14283F', '#2f5d8c').replace('#B58A3C', '#d08a1e').replace('#22405F', '#2f6f9a')
    return s

# ---------- notes -> trees
def key(it):
    t = it if isinstance(it, str) else (it.get('h') or (it['tbl']['head'][0] if 'tbl' in it else ''))
    return re.sub(r'<[^>]+>', '', t)

def table(t):
    return ('<table class="ht"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' %
            (''.join('<th>%s</th>' % hx(h) for h in t['head']), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % hx(c) for c in r) for r in t['rows'])))

def figure(f):
    return '<figure class="%s"><img src="img/%s"><figcaption><b>Fig.</b> %s <i>%s</i></figcaption></figure>' % ('sq' if f.get('sq') else 'wide', os.path.basename(f['img']), hx(f['cap']), hx(f.get('pg', '')))

def render_group(title, items):
    kids, buf = '', []
    def flush():
        nonlocal kids
        if buf: kids += '<ul class="k">' + ''.join(bul(x) for x in buf) + '</ul>'; buf.clear()
    for it in items:
        if isinstance(it, str): buf.append(it); continue
        flush()
        if 'tbl' in it: kids += table(it['tbl'])
        elif 'alert' in it: kids += '<div class="alert"><span class="lb">Watch out</span>%s</div>' % hx(it['alert'])
        elif 'fig' in it: kids += figure(it['fig'])
    flush()
    if not title: return '<div class="grp top"><div class="rt">Key points</div><div class="kids">%s</div></div>' % kids
    plain = re.sub(r'<[^>]+>', '', title)
    cls = 'side' if len(plain) <= 26 and len(items) <= 5 else 'top'
    return '<div class="grp %s"><div class="rt">%s</div><div class="kids">%s</div></div>' % (cls, hx(title), kids)

def notes_html(c):
    vis = [dict(v) for v in c.get('visuals', []) if v.get('after')]
    groups, cur = [], [None, []]
    for it in c['notes']:
        if isinstance(it, dict) and 'h' in it:
            if cur[1] or cur[0]: groups.append(cur)
            cur = [it['h'], []]
        else: cur[1].append(it)
    if cur[1] or cur[0]: groups.append(cur)
    out = ''
    for title, items in groups:
        out += render_group(title, items)
        keys = ([re.sub(r'<[^>]+>', '', title)] if title else []) + [key(i) for i in items]
        for v in vis:
            if not v.get('done') and any(v['after'] in k for k in keys):
                v['done'] = True; out += vis_html(v)
    for v in vis:
        if not v.get('done'): print('WARN unplaced', c['id'], v.get('title'))
    return out

def chapter(c, part_banner):
    h = '<section class="chapter" id="ch%d"><div class="run"></div>' % c['id']
    if part_banner: h += part_banner
    pr = {'H': 'High', 'M': 'Medium', 'L': 'Low'}[c['priority']]
    h += '<div class="opener"><div class="num">%d</div><div class="otitle"><h2>%s</h2><div class="pg"><span class="pri %s">%s priority</span>Handout %s</div></div></div>' % (c['id'], hx(c['title']), c['priority'], pr, hx(c.get('pages', '')))
    qs = sorted(PYQ.get(c['id'], []), key=lambda q: -q['yr'])
    if qs:
        h += '<div class="pyqbox"><span class="lb">PYQ tags</span>' + ''.join('<div><b>%s%s</b> %s</div>' % (q['yr'], (' · ' + esc(q['mk'])) if q['mk'] != 'not printed' else '', hx(re.sub(r'<[^>]+>', '', q['q']))) for q in qs) + '</div>'
    else:
        h += '<div class="pyqbox"><span class="lb">PYQ tags</span> none quoted in the material (still a hook for Prelims facts).</div>'
    pl = PLAIN[str(c['id'])] if False else c
    h += '<div class="sticky"><div class="lb">In simple words</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % md(x) for x in c['simple'])
    h += '<table class="terms"><thead><tr><th>Key term</th><th>In plain words</th></tr></thead><tbody>%s</tbody></table>' % ''.join('<tr><td><b>%s</b></td><td>%s</td></tr>' % (esc(a), esc(b)) for a, b in c['terms'])
    tops = [v for v in c.get('visuals', []) if v.get('pos') == 'top']
    h += ''.join(vis_html(v) for v in tops)
    if not any(v['type'] == 'mnemonic' for v in c.get('visuals', [])) and c.get('remember'):
        h += '<div class="sticky pink"><div class="lb">Remember it as</div><ul><li>%s</li></ul></div>' % md(c['remember'])
    h += notes_html(c)
    if c['id'] in CA:
        n = CA[c['id']]
        h += '<div class="news"><div class="lb">In the news<small>%s · verify dates</small></div><div class="tt">%s</div><ul>%s</ul></div>' % (esc(n['src']), esc(n['title']), ''.join('<li>%s</li>' % esc(p) for p in n['pts']))
    h += '<span class="endh">Recall &amp; drill</span>'
    if c.get('recall'):
        h += '<table class="rc"><tbody>%s</tbody></table>' % ''.join('<tr><td class="q">%s</td><td>%s</td></tr>' % (hx(q), hx(a)) for q, a in c['recall'])
    for t in c.get('traps', []):
        h += '<div class="trap"><b>%s · %s.</b> %s <i>%s</i></div>' % (esc(t['k']), hx(t['t']), hx(t['d']), hx(t['r']))
    if c.get('quiz'):
        for i, q in enumerate(c['quiz']):
            h += '<div class="mcq"><b>Q%d.</b> %s%s</div>' % (i + 1, hx(q['q']), ''.join('<span class="o">(%s) %s</span>' % ('abcd'[j], hx(o)) for j, o in enumerate(q['o'])))
        h += '<div class="key">Answers: %s</div>' % ', '.join('Q%d %s' % (i + 1, 'abcd'[q['a']]) for i, q in enumerate(c['quiz']))
    return h + '</section>'

def paper_svg():
    return ('data:image/svg+xml;utf8,' + ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 210 297" width="210mm" height="297mm">'
      '<line x1="17.4" y1="0" x2="17.4" y2="297" stroke="#f3b8b0" stroke-width=".35"/>'
      '<rect x="168" y="13" width="35" height="268" rx="2.2" fill="none" stroke="#9fb0c3" stroke-width=".4" stroke-dasharray="1.6 1.4"/>'
      '<text x="185.5" y="21" font-family="Caveat" font-size="5.6" fill="#d08a1e" text-anchor="middle">my notes</text>'
      '<text x="185.5" y="26" font-family="Patrick Hand" font-size="2.6" fill="#8da0b4" text-anchor="middle">current affairs</text><text x="185.5" y="29.4" font-family="Patrick Hand" font-size="2.6" fill="#8da0b4" text-anchor="middle">data · value add</text>'
      '</svg>')).replace('#', '%23').replace('<', '%3C').replace('>', '%3E').replace('"', "'")

def cover():
    deco = ('<svg class="deco" viewBox="0 0 210 297" width="210mm" height="297mm"><circle cx="190" cy="25" r="48" fill="#ffd9b0" opacity=".55"/><circle cx="14" cy="60" r="28" fill="#cfeadf" opacity=".7"/>'
            '<circle cx="22" cy="275" r="52" fill="#cfeadf" opacity=".6"/><circle cx="195" cy="262" r="34" fill="#ffd9b0" opacity=".6"/>'
            '<path d="M42 100 Q105 112 168 100" stroke="#e9a63c" stroke-width="1.6" fill="none"/><path d="M60 106 Q105 116 150 106" stroke="#e9a63c" stroke-width="1" fill="none"/>'
            '<g fill="#e9a63c"><path d="M22 84 l2 5 5 .5-4 3 1.5 5-4.5-3-4.5 3 1.5-5-4-3 5-.5z"/><path d="M172 70 l1.6 4 4 .4-3.2 2.4 1.2 4-3.6-2.4-3.6 2.4 1.2-4-3.2-2.4 4-.4z"/></g></svg>')
    return ('<section class="cover">%s<div class="tag">GS Paper II · Mains · handwritten-style notes</div><h1>Governance</h1>'
            '<div class="sub">Civil Services, Transparency, Accountability and the Fight against Corruption</div>'
            '<div class="note">Comprehensive first-read notes from the Sarrthi IAS GS-2 Governance Modules 1 and 2, with current affairs from the July and August 2026 magazines, mind maps, mnemonics and a blank column on every page for your own additions.</div>'
            '<div class="foot">UPSC CSE 2027 · Personal Study Edition</div></section>') % deco

def index(ids):
    h = '<section class="idx"><h1>Index</h1>'
    for p in B['parts']:
        h += '<div class="part">%s <small style="font:14pt HCav;color:#6b7c8f">%s</small></div>' % (esc(p['label']), esc(p['sub']))
        for c in p['chapters']:
            h += '<a class="il" href="#ch%d"><span class="n">%d</span>%s</a>' % (c['id'], c['id'], hx(c['title']))
    h += ('<div class="legend"><b>How to read the pens.</b><br><span class="h">Yellow highlight</span> = key term or number. '
          '<span class="r">Red box</span> = PYQ tag, trap or warning. <span class="g">Green box</span> = in the news (verify dates). '
          '<span class="p">Pink or orange card</span> = mnemonic. Blue brackets = the topic tree. The dashed column on the right is yours.</div></section>')
    return h

def build():
    body = cover() + index(None)
    for p in B['parts']:
        for i, c in enumerate(p['chapters']):
            banner = '<div class="part">%s<small>%s</small></div>' % (esc(p['label']), esc(p['sub'])) if i == 0 else ''
            body += chapter(c, banner)
    css = open(os.path.join(HERE, 'hand.css'), encoding='utf8').read().replace('%%PAPER%%', paper_svg())
    doc = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Governance (handwritten-style notes)</title><style>%s</style></head><body>%s</body></html>' % (css, body)
    open(os.path.join(HERE, 'hand.html'), 'w', encoding='utf8').write(doc)
    HTML(string=doc, base_url=HERE + '/').write_pdf(OUT)
    print('wrote', OUT)
build()
