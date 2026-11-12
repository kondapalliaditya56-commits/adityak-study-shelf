# -*- coding: utf-8 -*-
"""Economy handwritten notes, detailed edition.
Usage: python3 hand_eco.py OUT.pdf 6      (chapters, comma separated; sample cover + how-to only with --sample)
Takes the FULL chapter data (book_export.chapter), renders it in handwritten style, and adds the concept-first layer
(layerN.py: plain words, examples, hooks, graphs, extra mnemonics) and the chapter-end abbreviation column."""
import sys, os, re, json, html as H, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); SCR = os.path.dirname(HERE)
HN = '/home/claude/adityak-study-shelf/src-gov/handnotes'
sys.path[:0] = [HERE, SCR, HN]
os.chdir(SCR)
import hwlib, hwstyle, dsl
import hgraph as G
from eco_gloss import G as GL, SKIP
from weasyprint import HTML
import book_export as BE

COLS = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']
def e(t): return H.escape(t, quote=False)
def plain(t): return H.unescape(re.sub(r'<[^>]+>', ' ', t))

CSS = '''
.chap{break-before:page}
.sec{font-family:CB;font-size:15.5pt;display:block;border:2px solid #111;border-radius:3px;box-shadow:1.2mm 1.2mm 0 currentColor;padding:0 3.2mm .4mm;margin:3.5mm 0 2mm;background:#fff;break-after:avoid;color:#111}
.sec.c1{color:#c62828;border-color:#c62828}.sec.c2{color:#1565c0;border-color:#1565c0}.sec.c3{color:#2e7d32;border-color:#2e7d32}.sec.c4{color:#6a1b9a;border-color:#6a1b9a}.sec.c5{color:#e65100;border-color:#e65100}.sec.c6{color:#00838f;border-color:#00838f}
.sh{font-family:KB;font-size:11pt;color:#6a1b9a;border-bottom:1.6px solid #6a1b9a;margin:2.6mm 0 1.2mm;display:inline-block;break-after:avoid}
.und{border:2px solid #00897b;background:#e0f2f1;border-radius:4px;padding:1.2mm 2.6mm;margin:1.4mm 0;color:#004d40;break-inside:avoid}
.und .t{font-family:KB;color:#00695c;font-size:10pt}
.eg{border:1.8px dashed #ef6c00;background:#fff3e0;border-radius:4px;padding:1mm 2.6mm;margin:1.2mm 0;color:#4e2a00;break-inside:avoid}
.eg .t{font-family:KB;color:#e65100;font-size:10pt}
.hk{border:2px solid #6a1b9a;background:#f3e5f5;border-radius:12px;padding:.8mm 3mm;margin:1.4mm 0;color:#4a148c;font-family:KB;break-inside:avoid}
.ul{margin:.8mm 0}.li{position:relative;padding-left:5mm;margin:.5mm 0}.li:before{content:"\\27A4";position:absolute;left:0;color:#c62828;font-size:8.5pt;top:.4mm}
.li.s2{padding-left:10mm}.li.s2:before{content:"\\2192";left:5mm;color:#777}
.cb{break-inside:avoid;margin:1.5mm 0;padding:1mm 2.4mm 1.1mm;border-radius:3px}
.cb .t{font-family:KB;margin-right:1.5mm}
.cb.alert{border:1.8px solid #c62828;background:#fde7ea;color:#6a0000}.cb.alert .t{color:#c62828}
.cb.key{border:1.8px solid #2e7d32;background:#e8f5e9;color:#1b5e20}.cb.key .t{color:#2e7d32}
.cb.teacher{border:1.8px solid #f9a825;background:#fff9c4;color:#333}.cb.teacher .t{color:#b26a00}
.cb.note{border:1.8px dashed #1565c0;background:#e3f2fd;color:#0d2a5c}.cb.note .t{color:#1565c0}
.cb.quote{border-left:4px solid #4a148c;background:#f6edf9;color:#4a148c}
.cb p{margin:.6mm 0}
.tcap{font-family:KB;font-size:10pt;color:#1565c0;margin:2mm 0 .6mm;break-after:avoid}
table{font-size:9.6pt;margin:.8mm 0 1.4mm}tr{break-inside:avoid}
.fig{margin:2mm 0;text-align:center;break-inside:avoid}.fig img{max-width:100%;max-height:78mm;border:1.4px solid #888;background:#fff}
.fig .fc{font-family:CV;font-size:10.5pt;color:#555;line-height:1.05;margin-top:.6mm}
.sv{display:block;margin:1mm auto;break-inside:avoid}
.gtitle{font-family:KB;font-size:10pt;color:#1565c0;text-align:center;margin-top:2mm;break-after:avoid}
.gp2{display:flex;gap:2mm;margin:1.4mm 0;break-inside:avoid}.gp2>div{flex:1;border:1.6px solid #90a4ae;border-radius:5px;background:#fff;padding:.6mm}
.gbox{border:1.6px solid #90a4ae;border-radius:5px;background:#fff;padding:.3mm 1mm;margin:1mm 0;break-inside:avoid}
.mnc{border:2px solid #c62828;background:#fffde7;border-radius:5px;padding:1mm 2.4mm 1.4mm;margin:1.6mm 0;break-inside:avoid}
.mnc .mh{font-family:KB;color:#c62828;font-size:10pt}
.mnc .tiles{display:flex;flex-wrap:wrap;gap:1.4mm;margin:1mm 0}
.mnc .tile{border:1.6px solid #111;background:#fff;border-radius:3px;padding:.2mm 1.6mm;font-size:9.2pt;line-height:1.1;flex:1 1 40%}
.mnc .tile b{font-family:CB;font-size:15pt;color:#c62828;margin-right:1.2mm;vertical-align:-1pt}
.mnc .big{font-family:CB;font-size:19pt;letter-spacing:3px;color:#111}
.mnc .hook{font-family:CV;font-size:12pt;color:#4a148c}
.mnc .note{font-size:8.4pt;color:#777;font-style:italic}
.num{border:2px dotted #00838f;background:#e0f7fa;border-radius:5px;padding:1mm 2.4mm;margin:1.6mm 0;break-inside:avoid}
.num .nh{font-family:KB;color:#00838f}.num .nl{display:inline-block;border:1.4px solid #00838f;background:#fff;border-radius:10px;padding:0 2.2mm;margin:.5mm 1mm .5mm 0;font-size:9.4pt}
.mq{margin:1mm 0;break-inside:avoid;font-size:9.6pt}.mq .qn{font-family:KB;color:#1565c0}.mq .opts{display:flex;flex-wrap:wrap}.mq .op{display:block;width:50%;padding-left:3mm;box-sizing:border-box}.mq .ok{color:#2e7d32;font-family:KB}
.pq{margin:.9mm 0;break-inside:avoid;font-size:9.6pt;line-height:1.1}.pq .yr{font-family:KB;color:#fff;background:#c62828;border-radius:8px;padding:0 1.6mm;font-size:8.6pt;margin-right:1mm}
.pq .op{display:block;padding-left:5mm}.pq .ok{color:#2e7d32;font-family:KB}
.glo{border:1.6px dashed #6a1b9a;border-radius:4px;background:#faf5ff;padding:1mm 2.2mm 1.4mm;font-size:8.8pt;line-height:1.16;color:#311b92;margin:3mm 0 1mm}
.glo .gh{font-family:CB;font-size:12pt;color:#6a1b9a}.glo .gh i{font-family:PH;font-size:7.6pt;color:#7b1fa2;font-style:normal}
.glo .gc{column-count:2;column-gap:4mm}.glo .ge{break-inside:avoid;margin:0 0 .8mm}.glo b{color:#c62828}.glo u{text-decoration:none;color:#00695c}
.howto{font-size:10.4pt}.howto td:first-child{width:34mm}
.pyqline{margin:-1mm 0 2mm;text-align:center}
.sv text{font-family:KL}
'''


# ---------------- small renderers ----------------
def li_list(items):
    out = '<div class="ul">'
    for it in items:
        sub = it.startswith('› ')
        out += '<div class="li%s">%s</div>' % (' s2' if sub else '', it[2:] if sub else it)
    return out + '</div>'


def call(c):
    k = c['kind']; body = ''.join('<p>%s</p>' % b for b in c['body'])
    ic = {'alert': '⚠ ', 'key': '⭐ ', 'teacher': '✎ ', 'note': 'ⓘ ', 'quote': ''}.get(k, '')
    return '<div class="cb %s"><span class="t">%s%s</span>%s</div>' % (k, ic, c['tag'], body)


def table(t, cap=None):
    cap = cap or t.get('cap')
    h = '<div class="tcap">%s</div>' % e(cap) if cap else ''
    h += '<table><tr>' + ''.join('<th>%s</th>' % x for x in t['head']) + '</tr>'
    for r in t['rows']: h += '<tr>' + ''.join('<td>%s</td>' % x for x in r) + '</tr>'
    return h + '</table>'


def fig(f):
    return '<div class="fig"><img src="%s"><div class="fc">%s</div></div>' % (f['img'], e(f.get('cap', '')))


def mnemonic(v):
    L = v['letters']
    if v.get('word') or v.get('kind') == 'word':
        big = v['word']
        tiles = ''.join('<div class="tile"><b>%s</b>%s</div>' % (e(a), e(b)) for a, b in L)
        h = '<div class="mnc"><div class="mh">🧠 Memory aid · %s</div><div class="big">%s</div>' % (e(v.get('title', '')), e(big))
        if v.get('hook'): h += '<div class="hook">%s</div>' % e(v['hook'])
        h += '<div class="tiles">%s</div>' % tiles
    else:
        s = v['sentence']; words = s.replace(',', '').split()
        tiles = ''.join('<div class="tile"><b>%s</b>%s</div>' % (e(a), e(b)) for a, b in L)
        h = '<div class="mnc"><div class="mh">🧠 Memory aid (order matters) · %s</div><div class="big" style="font-size:14pt;letter-spacing:.5px">%s</div><div class="tiles">%s</div>' % (e(v.get('title', '')), e(s), tiles)
    if v.get('note'): h += '<div class="note">%s</div>' % e(v['note'])
    return h + '</div>'


def viz(v):
    t = v['type']
    if t == 'mnemonic': return mnemonic(v)
    if t == 'flow':
        steps = ['%s: %s' % (a, b) if b else a for a, b in v['steps']]
        return '<div class="gbox"><div class="gtitle">%s</div>%s</div>' % (e(v.get('title', '')), dsl.svg_flow(steps, v.get('per_row', 4)).replace('max-width:150mm', 'max-width:118mm'))
    if t == 'fork':
        h = '<div class="cb note"><span class="t">%s</span> ' % e(v['title'])
        h += '<table><tr>' + ''.join('<th>%s</th>' % e(b['t']) for b in v['branches']) + '</tr><tr>'
        for b in v['branches']: h += '<td>%s<br><b>→ %s</b></td>' % ('<br>'.join('• ' + e(x) for x in b['c']), e(b.get('verdict', '')))
        return h + '</tr></table></div>'
    if t == 'mindmap': return mindmap_tree(v)
    return ''


def mindmap_tree(v):
    kids = []
    for i, b in enumerate(v['branches']):
        kids.append(hwlib.B(e(b['t']), [e(x) for x in b['c']], COLS[i % 7], 26))
    return '<div class="gbox"><div class="gtitle">Chapter map: %s</div>%s</div>' % (e(v['center']), ''.join(kids))


GW = {'adas_equilibrium': 115, 'index_bars': 100, 'weights_bars': 112, 'phillips': 118, 'engel_curve': 112, 'price_paths': 112, 'fiscal_drag_bars': 100, 'real_rate_bar': 100, 'gain_lose': 100, 'stag_boxes': 90, 'spiral_loop': 95, 'measure_ladder': 100}


def graph(name):
    f = getattr(G, name)(); return f if isinstance(f, str) and f.startswith('<div class="gp2"') else '<div class="gbox">%s</div>' % f.svg(GW.get(name, 112))


def pyq_block(py):
    h = '<div class="sec c1">PYQs on this chapter (every one from your sheets)</div>'
    h += '<div class="cb note"><span class="t">%s</span> ★ marks the answer.</div>' % e(py['intro'])
    for g in py['groups']:
        h += '<div class="sh">%s · %s</div>' % (e(g['title']), e(g['count']))
        for q in g['prelims']:
            txt = ''.join(('<div>%s</div>' % b[1]) if b[0] == 'p' else ('<div class="li">%s</div>' % b[1]) for b in q['blocks'])
            ops = ''.join('<span class="op%s">(%s) %s%s</span>' % ('', 'abcd'[i], o, ' ★' if 'abcd'[i] == q['ans'] else '') for i, o in enumerate(q['opts']))
            h += '<div class="pq"><span class="yr">Prelims %s</span>%s%s</div>' % (q['year'], txt, ops.replace('class="op"', 'class="op"'))
        for m in g['mains']:
            h += '<div class="pq"><span class="yr">Mains %s · %s marks</span><b>%s</b> %s</div>' % (m['year'], m['marks'], e(m.get('topic', '')), e(m['q']))
    return h


def recall(rc):
    h = '<div class="sec c2">Recall drill: cover the right side and answer</div><table>'
    for i in range(0, len(rc), 2):
        row = rc[i:i + 2]
        h += '<tr>' + ''.join('<td style="width:23%%"><b>%s</b></td><td style="width:27%%">%s</td>' % (e(q), e(a)) for q, a in row) + ('<td></td><td></td>' if len(row) == 1 else '') + '</tr>'
    return h + '</table>'


def traps(tr):
    h = '<div class="sec c1">Traps to avoid in the exam hall</div>'
    for t in tr:
        h += '<div class="cb alert"><span class="t">⚠ %s: %s</span><p>%s <b>%s</b></p></div>' % (e(t['k']), e(t['t']), e(t['d']), e(t['r']))
    return h


def quiz(qz):
    h = '<div class="sec c3">Self-test (answers in the last line)</div>'; key = []
    for i, q in enumerate(qz, 1):
        h += '<div class="mq"><span class="qn">Q%d.</span> %s' % (i, e(q['q'])) + '<div class="opts">' + ''.join('<span class="op">(%s) %s</span>' % ('abcd'[j], e(o)) for j, o in enumerate(q['o'])) + '</div></div>'
        key.append('%d-%s' % (i, 'abcd'[q['a']]))
    return h + '<div class="cb key"><span class="t">Answer key:</span> %s</div>' % ' · '.join(key)


# ---------------- abbreviations ----------------
TOK = re.compile(r'(?<![A-Za-z0-9])(?:Y-o-Y|[A-Z][A-Za-z]?[A-Z0-9&\-]+[A-Za-z0-9]|[A-Z]{2,}[0-9]?|[A-Z]&[A-Z])(?![A-Za-z0-9])')
def abbreviations(text, own_defs):
    found = {}; missing = []
    for m in TOK.finditer(text):
        a = m.group(0)
        if a in SKIP: continue
        found[a] = found.get(a, 0) + 1
    ents = []
    for a in sorted(found, key=lambda x: (-found[x], x)):
        if a in GL: ents.append((a, GL[a][0], GL[a][1]))
        elif a in own_defs: ents.append((a, own_defs[a], ''))
        else: missing.append(a)
    return ents, missing


def gloss_box(ents):
    h = '<div class="glo"><div class="gh">🔤 Abbreviation column: every short form in this chapter, expanded <i>(meanings are plain-language aids, verify before quoting)</i></div><div class="gc">'
    for a, full, brief in ents:
        h += '<div class="ge"><b>%s</b> = <u>%s</u>%s</div>' % (e(a), e(full), (' — ' + e(brief)) if brief else '')
    return h + '</div></div>'


# ---------------- chapter ----------------
def chapter_html(ch, layer):
    SEC, TOP = layer.SEC, layer.TOP
    n = [0]
    h = '<div class="chap" id="c%s"><div class="ttl">%s&nbsp;%s&nbsp;%s</div>' % (ch['id'], hwlib.ICON['coin'], e(ch['title'].split(':')[0].upper()), hwlib.ICON['coin'])
    pr = {'H': 'High priority', 'M': 'Medium priority', 'L': 'Light priority'}[ch['priority']]
    h += '<div class="pyqline">%s %s · PYQs mapped: Prelims %s · Mains %s</div>' % (hwlib.P(pr), '', e(ch['prelims_pyqs']), e(ch['pyqs']))
    h += hwlib.SW(' '.join(ch['simple'][:1]).replace('**', ''))
    # 60-second route
    h += '<div class="cb key"><span class="t">The whole chapter in 60 seconds</span>' + li_list(['<b>%s</b>: %s' % (e(a), e(b)) for a, b in TOP['sixty']]) + '</div>'
    h += '<div class="und"><span class="t">🧠 In simple words</span>' + li_list([re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s) for s in ch['simple']]) + '</div>'
    h += '<div class="sh">Words you need first</div>' + table({'head': ['Word', 'Meaning'], 'rows': [['<b>%s</b>' % e(a), e(b)] for a, b in TOP['words']]})
    h += '<div class="cb key"><span class="t">⭐ One line to carry:</span> %s</div>' % e(ch['remember'])
    L = ch['lens']
    h += '<div class="row"><div class="cb note"><span class="t">Prelims hooks</span>%s</div><div class="cb note"><span class="t">Mains hooks</span>%s</div></div>' % (li_list([e(x) for x in L['prelims']]), li_list([e(x) for x in L['mains']]))
    first_viz = [x for x in ch['visuals'] if x.get('type') == 'mindmap']
    if first_viz: h += mindmap_tree(first_viz[0])

    notes = ch['notes']; buf = []; cur = None
    def flush():
        nonlocal buf
        if buf and buf[0][0] == 'ul': pass
        buf = []
    out = []; lis = []
    def endul():
        nonlocal lis
        if lis: out.append(li_list(lis)); lis = []
    cur_sec = None
    def end_section():
        nonlocal cur_sec
        endul()
        if cur_sec and cur_sec in SEC and SEC[cur_sec].get('hook'):
            out.append('<div class="hk">⭐ Remember: %s</div>' % e(SEC[cur_sec]['hook']))
        for mn in (SEC.get(cur_sec, {}).get('mn', []) if cur_sec else []):
            out.append(mnemonic(mn))
        cur_sec = None
    for it in notes:
        if isinstance(it, str):
            lis.append(it); continue
        k = list(it)[0]; v = it[k]
        endul()
        if k == 'h':
            m = re.match(r'^(\d+) · (.*)', v)
            if m:
                end_section(); cur_sec = m.group(1); n[0] += 1
                out.append('<div class="sec c%d">%s</div>' % (n[0] % 6 + 1, e(v)))
                S_ = SEC.get(cur_sec)
                if S_:
                    out.append('<div class="und"><span class="t">🧠 Understand it first</span> %s</div>' % e(S_['plain']))
                    out.append('<div class="eg"><span class="t">✏ Example</span> %s</div>' % e(S_['eg']))
            elif v.startswith(('Exam lens', 'Current affairs', 'Timeline', 'Connects', 'Mains answer')):
                end_section(); out.append('<div class="sec c%d">%s</div>' % (n[0] % 6 + 1, e(v))); n[0] += 1
            else: out.append('<div class="sh">%s</div>' % e(v))
        elif k == 'p': out.append('<p style="margin:1mm 0">%s</p>' % v)
        elif k == 'call': out.append(call(v))
        elif k == 'tbl': out.append(table(v))
        elif k == 'fig': out.append(fig(v))
        elif k == 'viz': out.append(viz(v))
    end_section()
    h += ''.join(out)
    # numbers card
    if getattr(layer, 'NUMBERS', None):
        h += '<div class="num"><span class="nh">🔢 Number card: figures to hold</span><br>' + ''.join('<span class="nl"><b>%s</b> %s</span>' % (e(a), e(b)) for a, b in layer.NUMBERS) + '</div>'
    if getattr(layer, 'DRAW', None):
        h += '<div class="cb teacher"><span class="t">✏ Blank-page drill: draw these from memory, then check</span>' + li_list([e(x) for x in layer.DRAW]) + '</div>'
    h += pyq_block(ch['pyq']) if ch.get('pyq') else ''
    h += traps(ch['traps']) if ch.get('traps') else ''
    h += recall(ch['recall']) if ch.get('recall') else ''
    h += quiz(ch['quiz']) if ch.get('quiz') else ''
    own = {}
    ents, miss = abbreviations(plain(re.sub(r'<svg.*?</svg>', ' ', h, flags=re.S)), own)
    if miss: print('UNEXPANDED ABBREVIATIONS:', miss)
    h += gloss_box(ents)
    return h + '</div>', ents, miss


COVER = ('<div class="cov"><div class="s">UPSC CSE 2027 · GS Foundation</div><h1>ECONOMY</h1><div class="s">Detailed handwritten notes · concept first</div>'
         '<div><span class="bx">SAMPLE · Chapter 6 · Inflation</span></div><div class="t">Built from the Sarrthi IAS Economy handout (Aditya Kalia) with PYQs from your sheets.<br>'
         'Every fact of the handout is kept. New: plain-words explanations, graphs, examples, memory aids and an abbreviation column.<br>'
         'Right column and left binding margin are kept blank for your own use.<br><br>Personal study edition · for printing</div></div>')
HOWTO = ('<div class="chap"><div class="ttl">HOW TO READ THESE NOTES</div><table class="howto"><tr><th>Box</th><th>What it gives you</th></tr>'
         '<tr><td><b>🧠 Understand it first</b></td><td>The idea in everyday words, before the technical notes. Read this first, then the handout notes.</td></tr>'
         '<tr><td><b>✏ Example</b></td><td>The handout’s own worked numbers, or a labelled practice picture.</td></tr>'
         '<tr><td><b>📊 Graphs and drawings</b></td><td>Curves, bars, loops and ladders you can redraw from memory on a blank page.</td></tr>'
         '<tr><td><b>Notes, tables, boxes</b></td><td>Every fact, number, name and example of the handout, in the handout’s order. Red box = trap or handout alert; green = rule; yellow = teacher/formula; blue = note.</td></tr>'
         '<tr><td><b>⭐ Remember</b></td><td>One line to hold the section. Purple pills are memory hooks.</td></tr>'
         '<tr><td><b>🧠 Memory aid</b></td><td>Word or sentence mnemonics. Unordered lists are rearranged into a real word; ordered lists keep their order. Labelled “own memory aid” when not from the handout.</td></tr>'
         '<tr><td><b>PYQs, traps, recall, self-test</b></td><td>Every PYQ from your sheets; traps with an exam-hall rule; cover-and-answer drill; MCQs with key.</td></tr>'
         '<tr><td><b>🔤 Abbreviation column</b></td><td>At the end of every chapter: every short form used in that chapter, expanded.</td></tr></table></div>')


def build(chs, out, sample=True):
    body = [COVER, HOWTO] if sample else []
    allmiss = []
    for cid in chs:
        ch = BE.chapter(importlib.import_module('ch%d' % cid).c)
        layer = importlib.import_module('layer%d' % cid)
        hch, ents, miss = chapter_html(ch, layer); body.append(hch); allmiss += miss
    css = hwlib.CSS + hwstyle.css('handlee', '') + CSS
    html = '<html><head><style>%s@page{@bottom-right{content:"Economy · Detailed Handwritten Notes · " counter(page);font-family:PH;font-size:8pt;color:#888}}</style></head><body>%s</body></html>' % (css, ''.join(body))
    html = hwstyle.decorate(html)
    d = HTML(string=html, base_url=SCR + '/').render()
    print('pages', len(d.pages)); d.write_pdf(out)
    open(out.replace('.pdf', '.html'), 'w').write(html)
    return allmiss


if __name__ == '__main__':
    build([int(x) for x in sys.argv[2].split(',')], sys.argv[1])
