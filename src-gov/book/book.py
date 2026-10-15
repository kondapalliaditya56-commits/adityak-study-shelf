# -*- coding: utf-8 -*-
"""Governance book: HTML -> PDF via WeasyPrint. Usage: python3 book.py OUT.pdf [sample|full]"""
import sys, os, json, re, html, base64
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
SG = os.path.dirname(HERE)
IMG = os.path.join(os.path.dirname(SG), 'img')
X = json.load(open(os.path.join(SG, 'hubdata.json'), encoding='utf8'))
P = json.load(open(os.path.join(SG, 'plain.json'), encoding='utf8'))
SECS = {s['id']: s for s in X['SECS']}
PYQ = {p['id']: p for p in X['PYQS']}
PRI = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
END = {int(k): v for k, v in X['ENDMAP'].items()}
XC = {int(k): v for k, v in X['XCARDS'].items()}
XQ = {int(k): v for k, v in X['XMCQ'].items()}
MODE = sys.argv[2] if len(sys.argv) > 2 else 'sample'
OUT = sys.argv[1] if len(sys.argv) > 1 else 'book.pdf'

NAVY, GOLD, IVORY, INK = '#14283F', '#B58A3C', '#FBF9F4', '#1C2733'

def md(t):  # **bold** -> <b>
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html.escape(t, quote=False))

def hx(t):  # trusted html snippet from the notes (already has <b>); escape stray ampersands only
    return re.sub(r'&(?!amp;|lt;|gt;|quot;|#)', '&amp;', t)

def trim(b64):
    from PIL import Image, ImageChops
    import io
    im = Image.open(io.BytesIO(base64.b64decode(b64))).convert('RGB')
    bg = Image.new('RGB', im.size, (255, 255, 255))
    bbox = ImageChops.difference(im, bg).point(lambda v: 255 if v > 14 else 0).getbbox()
    if bbox:
        pad = 18
        bbox = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(im.width, bbox[2]+pad), min(im.height, bbox[3]+pad))
        im = im.crop(bbox)
    o = io.BytesIO(); im.save(o, 'JPEG', quality=84); return base64.b64encode(o.getvalue()).decode()

def fig(k):
    f = X['FIGDEF'][k]
    b64 = trim(X['IMG'][k])
    cls = 'sq' if f.get('sq') else 'wide'
    return ('<figure class="%s"><img src="data:image/jpeg;base64,%s"><figcaption><b>Figure.</b> %s <span class="pg">Handout %s</span></figcaption></figure>'
            % (cls, b64, hx(f['cap']), f['pg']))

def notes_html(notes):
    out, buf = [], []
    def flush():
        if buf:
            out.append('<ul class="b">' + ''.join('<li>%s</li>' % hx(x) for x in buf) + '</ul>'); buf.clear()
    for it in notes:
        if isinstance(it, str): buf.append(it); continue
        flush()
        if 'h' in it: out.append('<h4>%s</h4>' % hx(it['h']))
        elif 'tbl' in it:
            t = it['tbl']
            out.append('<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (
                ''.join('<th>%s</th>' % hx(h) for h in t['head']),
                ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % hx(c) for c in r) for r in t['rows'])))
        elif 'alert' in it: out.append('<div class="alert"><span>Handout alert</span>%s</div>' % hx(it['alert']))
        elif 'figs' in it: out.append(''.join(fig(k) for k in it['figs']))
    flush()
    return ''.join(out)

def chapter(num, s):
    d = P[str(s['id'])]
    ys = ', '.join('%s%s' % (PYQ[i]['yr'], '*' if PYQ[i].get('partial') else '') for i in s['pyqs']) or 'none quoted in the material'
    h = '<section class="chapter" id="ch%d">' % s['id']
    h += '<div class="opener"><div class="cnum">%02d</div><div class="ctitle"><div class="ceyebrow">Chapter %d &middot; %s</div><h2>%s</h2></div></div>' % (
        s['id'], s['id'], hx(s['pages']), hx(s['title']))
    h += '<div class="meta"><span class="pri %s">%s priority</span><span>Mains PYQs quoted: <b>%s</b></span><span>Prelims PYQs: <b>none quoted</b></span></div>' % (s['pri'], PRI[s['pri']], hx(ys))
    h += '<div class="lens"><div class="lbl">Exam lens</div><div class="two"><div><h5>Prelims hooks</h5><ul class="b">%s</ul></div><div><h5>Mains hooks</h5><ul class="b">%s</ul></div></div><p class="close">%s</p></div>' % (
        ''.join('<li>%s</li>' % hx(x) for x in s['lens']['prelims']), ''.join('<li>%s</li>' % hx(x) for x in s['lens']['mains']), hx(s['lens']['close']))
    h += '<div class="simple"><div class="lbl">In simple words</div><ul class="b">%s</ul></div>' % ''.join('<li>%s</li>' % md(x) for x in d['simple'])
    h += '<table class="terms"><thead><tr><th>Key term</th><th>In plain words</th></tr></thead><tbody>%s</tbody></table>' % ''.join(
        '<tr><td><b>%s</b></td><td>%s</td></tr>' % (html.escape(a), html.escape(b)) for a, b in d['terms'])
    h += '<div class="remember"><span>Remember it as</span> %s</div>' % md(d['remember'])
    h += '<p class="story">%s</p>' % hx(s['story'])
    h += notes_html(s['notes'])
    # end of chapter
    m = END.get(s['id'], {'c': [], 't': [], 'q': []})
    cards = [X['CARDS'][i] for i in m['c']] + XC.get(s['id'], [])
    traps = [X['TRAPS'][i] for i in m['t']]
    qs = [X['MCQ'][i] for i in m['q']] + XQ.get(s['id'], [])
    h += '<div class="endblk"><div class="lbl">End of chapter &middot; recall and drill</div>'
    if cards:
        h += '<h4>Recall sheet: cover the right column and answer</h4><table class="recall"><tbody>%s</tbody></table>' % ''.join(
            '<tr><td class="q">%s</td><td class="a">%s</td></tr>' % (hx(q), hx(a)) for q, a in cards)
    for t in traps:
        h += '<div class="trap"><b>%s &middot; %s</b> %s <i>%s</i></div>' % (html.escape(t['k']), hx(t['t']), hx(t['d']), hx(t['r']))
    if qs:
        h += '<h4>Quick quiz</h4>' + ''.join('<div class="mcq"><p><b>Q%d.</b> %s</p><ol type="a">%s</ol></div>' % (
            i + 1, hx(q['q']), ''.join('<li>%s</li>' % hx(o) for o in q['o'])) for i, q in enumerate(qs))
        h += '<p class="key">Answers: %s</p>' % ', '.join('Q%d %s' % (i + 1, 'abcd'[q['a']]) for i, q in enumerate(qs))
    h += '</div></section>'
    return h

CSS = open(os.path.join(HERE, 'book.css'), encoding='utf8').read()

def notes_svg():
    lines = ''.join('<line x1="148" x2="196" y1="%s" y2="%s" stroke="#D9D0BC" stroke-width="0.18" stroke-dasharray="0.6 0.9"/>' % (y, y) for y in [32 + 8 * i for i in range(30)])
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">'
           '<rect x="144" y="18" width="56" height="261" rx="1.2" fill="#FBF8F0" stroke="#E4DCC8" stroke-width="0.25"/>'
           '<rect x="144" y="18" width="56" height="9" rx="1.2" fill="#14283F"/>'
           '<text x="172" y="24" font-family="Inter, sans-serif" font-size="2.7" fill="#E9D9B0" text-anchor="middle" letter-spacing="0.35">MY NOTES</text>'
           + lines +
           '<text x="172" y="284.6" font-family="Inter, sans-serif" font-size="2.05" fill="#8B8168" text-anchor="middle" letter-spacing="0.12">CURRENT AFFAIRS  ·  DATA  ·  VALUE ADDITION</text>'
           '</svg>')
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()

def cover():
    return ('<section class="cover"><div class="cin"><div class="top">GS PAPER II &nbsp;·&nbsp; MAINS</div>'
            '<div class="rule"></div><h1>GOVERNANCE</h1><div class="sub">Civil Services, Transparency, Accountability<br>and the Fight against Corruption</div>'
            '<svg class="mark" viewBox="0 0 120 80" width="46mm"><g fill="none" stroke="#B58A3C" stroke-width="1.6"><path d="M10 70h100M16 64h88M22 22h76M60 6l44 16H16z"/><path d="M28 28v34M44 28v34M60 28v34M76 28v34M92 28v34"/></g></svg>'
            '<div class="rule"></div><div class="mid">A complete study companion built from the Sarrthi IAS GS-2 Governance Modules 1 and 2</div>'
            '<div class="foot">UPSC Civil Services Examination 2027 &nbsp;·&nbsp; Personal Study Edition</div></div></section>')

def front():
    return ('<section class="front"><div class="halftitle"><h1>GOVERNANCE</h1><div class="s">Civil Services, Transparency, Accountability and the Fight against Corruption</div></div>'
            '<div class="imprint"><p><b>Personal Study Edition, 2026</b></p>'
            '<p>Prepared for the UPSC Civil Services Examination 2027, General Studies Paper II.</p>'
            '<p>Source material: Sarrthi IAS GS-2 Governance Module 1 (Civil Services, Role, Transparency, Accountability, RTI, Citizen&rsquo;s Charter) and Module 2 (Corruption, Social Audit, CBI, CVC, Lokpal, Whistleblower, PCA). The facts printed here are the handouts&rsquo; own; no outside facts have been added. Copyright in the source material belongs to Sarrthi IAS and its teacher.</p>'
            '<p>The wide margin on every page is left blank on purpose: use it for current affairs, related data and value-addition points.</p></div></section>')

def how_to():
    return ('<section class="howto"><h2 class="plain">How to use this book</h2>'
            '<table class="terms"><thead><tr><th>Block</th><th>What it gives you</th></tr></thead><tbody>'
            '<tr><td><b>Exam lens</b></td><td>Priority (High, Medium, Low), the Mains PYQs quoted for the chapter, and the Prelims and Mains hooks.</td></tr>'
            '<tr><td><b>In simple words</b></td><td>The chapter in a few plain lines, with the key terms explained.</td></tr>'
            '<tr><td><b>Chapter notes</b></td><td>The complete handout content in handout order: bullets, tables, redrawn figures.</td></tr>'
            '<tr><td><b>Recall and drill</b></td><td>Cover-and-answer questions, exam traps and a short quiz to close each chapter.</td></tr>'
            '<tr><td><b>My notes column</b></td><td>The ruled panel on the right of every page is yours. Add current affairs, data and value additions.</td></tr></tbody></table>'
            '<div class="legend"><span class="pri H">High</span> two or more PYQs map to the chapter &nbsp; <span class="pri M">Medium</span> one PYQ or a partial fit &nbsp; <span class="pri L">Low</span> none quoted</div></section>')

PARTS = [('Part I', 'Module 1', 'Civil Services, Transparency, Accountability, Citizen&rsquo;s Charter and RTI', range(1, 15)),
         ('Part II', 'Module 2', 'Corruption, Social Audit, CBI, CVC, Lokpal, Whistleblower and PCA', range(15, 20))]

def toc(built):
    h = '<section class="toc"><h2 class="plain">Contents</h2>'
    for pn, mod, title, rng in PARTS:
        h += '<div class="tpart"><span>%s</span> %s</div>' % (pn, title)
        for i in rng:
            t = hx(SECS[i]['title'])
            if i in built: h += '<a class="tl" href="#ch%d"><span class="n">%02d</span><span class="t">%s</span></a>' % (i, i, t)
            else: h += '<div class="tl off"><span class="n">%02d</span><span class="t">%s</span><span class="dots"></span></div>' % (i, t)
    h += '<div class="tpart"><span>Back matter</span> Mind maps, timeline, PYQ index and drills</div></section>'
    return h

def part_opener(pn, mod, title):
    return ('<section class="partop"><div class="pn">%s</div><h1>%s</h1><div class="rule"></div><p>%s</p></section>' % (pn, mod, title))

def build():
    ids = [4] if MODE == 'sample' else list(range(1, 20))
    body = cover() + front() + how_to() + toc(set(ids))
    for pn, mod, title, rng in PARTS:
        if MODE == 'sample' and pn != 'Part I': continue
        body += part_opener(pn, mod, title)
        for i in rng:
            if i in ids: body += chapter(i, SECS[i])
    css = CSS.replace('%%NOTES%%', notes_svg())
    doc = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Governance</title><style>%s</style></head><body>%s</body></html>' % (css, body)
    open(os.path.join(HERE, 'book.html'), 'w', encoding='utf8').write(doc)
    HTML(string=doc, base_url=HERE).write_pdf(OUT)
    print('wrote', OUT)

build()
