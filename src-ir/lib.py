# -*- coding: utf-8 -*-
"""Generator library for the Study Shelf IR notebook.
Reuses the shelf's own CSS and reader JS (extracted verbatim from pol-ch04.html)."""
import html, json, re, os

HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, 'shared_css.html'), encoding='utf8').read()
JS = open(os.path.join(HERE, 'shared_js.js'), encoding='utf8').read()
STORE_ONLY = open(os.path.join(HERE, 'store_only.js'), encoding='utf8').read()
SEARCH_LOGIC = open(os.path.join(HERE, 'search_logic.js'), encoding='utf8').read()

NB_ID = 'international-relations'
BASE = 'ir-'
NB_TITLE = 'International Relations (GS-2)'

# ---------------------------------------------------------------- inline markup
def inline(t):
    """**bold**, ==mark==, [text](url), `art` -> span.art. Escapes HTML first."""
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'==(.+?)==', r'<mark>\1</mark>', t)
    t = re.sub(r'`(.+?)`', r'<span class="art">\1</span>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    return t

def plain(t):
    t = re.sub(r'\*\*|==|`', '', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', t)
    return t

def slug(t, n=40):
    s = re.sub(r'[^a-z0-9]+', '-', plain(t).lower()).strip('-')
    return s[:n].strip('-')

# ---------------------------------------------------------------- blocks
def p(t):
    return '<p>' + inline(t) + '</p>'

def h3(t):
    return '<h3>' + inline(t) + '</h3>'

def ul(items):
    out = '<ul class="lst">'
    for it in items:
        if it.startswith('> '):
            out += '<li class="sub">' + inline(it[2:]) + '</li>'
        else:
            out += '<li>' + inline(it) + '</li>'
    return out + '</ul>'

def tbl(cap, head, rows, desc=None):
    h = '<div class="tblock">'
    if cap:
        h += '<div class="tcap">' + inline(cap) + '</div>'
    h += '<div class="tablewrap"><table><thead><tr>' + ''.join('<th>%s</th>' % inline(x) for x in head) + '</tr></thead><tbody>'
    for r in rows:
        h += '<tr>'
        for i, c in enumerate(r):
            if i == 0:
                h += "<th scope='row'>%s</th>" % inline(c)
            else:
                h += '<td>%s</td>' % inline(c)
        h += '</tr>'
    h += '</tbody></table></div>'
    if desc:
        h += '<p class="gdesc">' + inline(desc) + '</p>'
    return h + '</div>'

CALL_CLASS = {'teacher': 'teacher', 'alert': 'alert', 'note': 'note', 'example': 'example',
              'source': 'source', 'key': 'key', 'mnemo': 'mnemo', 'shortcut': 'shortcut'}

def callout(kind, tag, body):
    paras = [x for x in body.split('\n\n') if x.strip()]
    inner = ''
    for x in paras:
        if x.startswith('- '):
            inner += ul([y[2:] for y in x.split('\n') if y.startswith('- ')])
        else:
            inner += p(x)
    return '<aside class="callout %s"><span class="tag">%s</span>%s</aside>' % (CALL_CLASS.get(kind, kind), inline(tag), inner)

def teacher(tag, body):   # slide stress (typed slides, no handwriting)
    return callout('teacher', tag, body)

def alert(tag, body):
    return callout('alert', tag, body)

def note(tag, body):
    return callout('note', tag, body)

def example(tag, body):
    return callout('example', tag, body)

def mnemo(tag, letters, body):
    return '<aside class="callout mnemo"><span class="tag">%s</span><div class="mn">%s</div>%s</aside>' % (
        inline(tag), ''.join('<b>%s</b>' % html.escape(c) for c in letters), p(body))

def two(cols):
    h = '<div class="two">'
    for title, items in cols:
        h += '<div class="col"><h4>%s</h4>%s</div>' % (inline(title), ul(items))
    return h + '</div>'

def flow(title, steps, lanes=None):
    """steps: list of (label, sub, cls). cls in '', 'good','warn','bad'"""
    h = '<section class="flow"><h4>%s</h4><div class="chain">' % inline(title)
    parts = []
    for s in steps:
        lab, sub = s[0], s[1]
        cls = s[2] if len(s) > 2 else ''
        parts.append('<div class="step %s"><div><div class="sl">%s</div><div class="ss">%s</div></div></div>' % (cls, inline(lab), inline(sub)))
    h += '<div class="arr" aria-hidden="true"></div>'.join(parts)
    return h + '</div></section>'

def lanes(title, lane_list):
    """lane_list: [(header, [(label, sub, cls), ...]), ...]"""
    h = '<section class="flow"><h4>%s</h4><div class="lanes">' % inline(title)
    for hd, steps in lane_list:
        h += '<div class="lane"><div class="lane-h">%s</div><div class="chain">' % inline(hd)
        parts = []
        for s in steps:
            cls = s[2] if len(s) > 2 else ''
            parts.append('<div class="step %s"><div><div class="sl">%s</div><div class="ss">%s</div></div></div>' % (cls, inline(s[0]), inline(s[1])))
        h += '<div class="arr" aria-hidden="true"></div>'.join(parts)
        h += '</div></div>'
    return h + '</div></section>'

def fig(src, caption, label='Class slide', alt=None):
    alt = alt or plain(caption)
    return ('<figure><a class="zoom" href="%s"><img src="%s" alt="%s" loading="lazy"></a>'
            '<figcaption><span class="figsrc">%s</span> %s</figcaption></figure>') % (
        src, src, html.escape(alt, quote=True), html.escape(label), inline(caption))

def details(summary, body_html):
    return '<details class="skel"><summary><strong>%s</strong></summary>%s</details>' % (inline(summary), body_html)

# ---------------------------------------------------------------- mind map
COLS = 8

def mindmap(root, branches, aria):
    """branches: [(label, [(leaf_title, leaf_note), ...]), ...]  -> (svg, outline_html)"""
    LH, STEP, GAP = 40, 48, 14
    rootw = round(9.4 * len(root) + 20, 1)
    maxbr = max(len(b[0]) for b in branches)
    brw = max(120, round(8.4 * maxbr + 26, 1))
    rx, rh = 8, 28
    bx = rx + rootw + 64
    lx = bx + brw + 164
    # leaf widths
    leafw = {}
    y = 8
    layout = []
    for bi, (bl, leaves) in enumerate(branches):
        top = y
        ls = []
        for (lt, ln) in leaves:
            w = round(max(7.6 * len(lt), 6.9 * len(ln)) + 24, 1)
            ls.append((lt, ln, y, w))
            y += STEP
        bottom = y - STEP + LH
        layout.append((bl, ls, (top + bottom) / 2))
        y += GAP
    total_h = y - GAP + 8
    maxleaf = max(l[3] for _, ls, _ in layout for l in ls)
    W = round(lx + maxleaf + 8, 1)
    rcy = total_h / 2
    svg = '<svg class="mm" viewBox="0 0 %s %s" width="%s" height="%s" role="img" aria-label="%s">' % (W, total_h, W, total_h, html.escape(aria, quote=True))
    svg += '<rect class="mm-root" x="%s" y="%s" width="%s" height="%s" rx="6"/>' % (rx, round(rcy - rh / 2, 1), rootw, rh)
    svg += '<text class="mm-root-t" x="%s" y="%s" text-anchor="middle">%s</text>' % (round(rx + rootw / 2, 1), round(rcy + 5, 1), html.escape(root))
    for bi, (bl, ls, cy) in enumerate(layout):
        c = 'c%d' % (bi % COLS)
        x0 = rx + rootw
        svg += '<path class="mm-link %s" d="M%s,%s C%s,%s %s,%s %s,%s"/>' % (c, x0, round(rcy, 1), round(x0 + 32, 1), round(rcy, 1), round(x0 + 32, 1), round(cy, 1), bx, round(cy, 1))
        svg += '<rect class="mm-branch %s" x="%s" y="%s" width="%s" height="28" rx="5"/>' % (c, bx, round(cy - 14, 1), brw)
        svg += '<text class="mm-branch-t" x="%s" y="%s" text-anchor="middle">%s</text>' % (round(bx + brw / 2, 1), round(cy + 4.5, 1), html.escape(bl))
        for (lt, ln, ly, w) in ls:
            lcy = ly + LH / 2
            ex = bx + brw
            svg += '<path class="mm-link %s" d="M%s,%s C%s,%s %s,%s %s,%s"/>' % (c, ex, round(cy, 1), round(ex + 28, 1), round(cy, 1), round(lx - 28, 1), round(lcy, 1), lx, round(lcy, 1))
            svg += '<rect class="mm-leaf %s" x="%s" y="%s" width="%s" height="%s" rx="4"/>' % (c, lx, ly, w, LH)
            svg += '<text class="mm-leaf-t" x="%s" y="%s">%s</text>' % (lx + 10, ly + 15.5, html.escape(lt))
            svg += '<text class="mm-leaf-n" x="%s" y="%s">%s</text>' % (lx + 10, ly + 30.5, html.escape(ln))
    svg += '</svg>'
    ol = '<ul class="outline"><li><strong>%s</strong><ul>' % html.escape(root)
    for bi, (bl, leaves) in enumerate(branches):
        ol += '<li class="c%d"><details open><summary>%s</summary><ul>' % (bi % COLS, html.escape(bl))
        for lt, ln in leaves:
            ol += '<li>%s <span class="ol-note">%s</span></li>' % (html.escape(lt), html.escape(ln))
        ol += '</ul></details></li>'
    ol += '</ul></li></ul>'
    return svg, ol

# ---------------------------------------------------------------- timeline, links, recall
def timeline(entries):
    """entries: [(year, text, high_bool)]"""
    h = '<ol class="timeline">'
    for y, t, hi in entries:
        h += '<li class="tl %s"><time class="yr">%s</time><span class="pin"></span><div class="tlbody">%s%s</div></li>' % (
            'high' if hi else '', html.escape(y), inline(t), '<span class="star" title="High-yield">★</span>' if hi else '')
    return h + '</ol>'

def links(items):
    h = '<div class="lkgrid">'
    for line, txt in items:
        h += '<article class="link"><div class="lk-line">%s</div><p>%s</p></article>' % (inline(line), inline(txt))
    return h + '</div>'

def recall(items):
    return '<p class="gdesc">Read once, hide it, then rebuild the chapter from memory.</p><ol class="recall">' + ''.join('<li>%s</li>' % inline(x) for x in items) + '</ol>'

# ---------------------------------------------------------------- sections
class Sec:
    def __init__(self, title, blocks, label=None, sid=None):
        self.title, self.blocks, self.label, self.sid = title, blocks, label, sid

def render_sections(secs, start=1, numbered=True):
    out, idx = [], []
    n = start
    for s in secs:
        if s.sid:
            sid = s.sid
            t = s.title
        else:
            sid = '%d-%s' % (n, slug(s.title))
            t = '%d · %s' % (n, s.title)
            n += 1
        idx.append((sid, t))
        body = ''
        if s.label:
            cls = 'cls' if s.label.startswith('Class') else 'hb'
            body += '<div class="pills"><span class="pill %s">%s</span></div>' % (cls, html.escape(s.label))
        body += ''.join(s.blocks)
        out.append('<h2 id="%s">%s<a class="anchor" href="#%s" aria-label="Link to this section">#</a></h2>%s' % (sid, inline(t), sid, body))
    return out, idx

# ---------------------------------------------------------------- page assembly
def head(title, extra_css=''):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<title>%s</title>%s%s</head>' % (html.escape(title), CSS, extra_css))

EXTRA_CSS = '<style>details.skel{border:1px solid var(--line);border-radius:10px;background:var(--surface);padding:8px 14px;margin:10px 0;font:15px/1.5 var(--sans)}details.skel summary{cursor:pointer}details.skel p,details.skel li{font-family:var(--sans)}.ptag.vhigh{background:var(--red-soft);color:var(--red)}</style>'

def json_script(obj, sid):
    return '<script type="application/json" id="%s">%s</script>' % (sid, json.dumps(obj, ensure_ascii=False).replace('</', '<\\/'))

def chapter_page(ch, prev_ch, next_ch, secs_sections, toc_idx, map_svg, map_outline, data, chead_html, footer_text, root_title):
    """ch: dict(n,title) ; prev/next: dict(n,title) or None"""
    n = ch['n']
    fn = lambda c: '%sch%02d.html' % (BASE, c['n'])
    bar = '<header class="bar"><div class="barin"><a class="home" href="index.html">Library</a><a class="home" href="%shome.html">Contents</a>' % BASE
    if prev_ch:
        bar += '<a class="nbtn" href="%s" title="%s" aria-label="Previous chapter">‹</a>' % (fn(prev_ch), html.escape(prev_ch['title'], quote=True))
    else:
        bar += '<span class="nbtn off" aria-hidden="true">‹</span>'
    label = ('Ch %d' % n) if n > 0 else 'Start'
    bar += '<span class="bartitle"><b>%s</b> %s</span>' % (label, html.escape(ch['title']))
    if next_ch:
        bar += '<a class="nbtn" href="%s" title="%s" aria-label="Next chapter">›</a>' % (fn(next_ch), html.escape(next_ch['title'], quote=True))
    else:
        bar += '<span class="nbtn off" aria-hidden="true">›</span>'
    bar += '<a class="home" href="%ssearch.html">Search</a>' % BASE
    bar += '<label class="done"><input type="checkbox" id="donebox" data-ch="%d"><span>Done</span></label><button class="aabtn" id="aabtn" type="button" aria-label="Reading settings">Aa</button></div></header>' % n
    side = '<aside class="sidetoc"><div class="sth">In this chapter</div><ol>' + ''.join('<li><a href="#%s">%s</a></li>' % (i, inline(t)) for i, t in toc_idx) + '</ol></aside>'
    pager = '<nav class="pager">'
    pager += ('<a href="%s"><small>Previous</small>%s</a>' % (fn(prev_ch), html.escape(prev_ch['title']))) if prev_ch else '<span></span>'
    pager += ('<a class="nx" href="%s"><small>Next</small>%s</a>' % (fn(next_ch), html.escape(next_ch['title']))) if next_ch else '<span></span>'
    pager += '</nav>'
    mapblock = ''
    if map_svg:
        mapblock = ('<section class="mapblock"><h2 id="chapter-map">Chapter map<a class="anchor" href="#chapter-map">#</a></h2>'
                    '<div class="seg" role="group" aria-label="Map view"><button type="button" data-v="map" aria-pressed="true">Map</button><button type="button" data-v="outline" aria-pressed="false">Outline</button></div>'
                    '<div id="mm-map" class="mmframe">%s</div><div id="mm-outline" hidden>%s</div></section>' % (map_svg, map_outline))
    else:
        # keep JS happy when there is no map
        mapblock = '<div id="mm-map" hidden></div><div id="mm-outline" hidden></div>'
    body = '<body>' + bar + '<div class="layout">' + side + '<main class="page">' + chead_html + mapblock
    body += '<div class="notes">' + ''.join(secs_sections) + '</div>'
    body += pager + '<footer>' + inline(footer_text) + '</footer></main></div><div id="lightbox" hidden><img alt=""></div>'
    body += json_script(data, 'data')
    nb = {'id': NB_ID, 'ch': n, 'title': ch['title']}
    body += '<script>window.__NB=%s;%s</script><script src="hl.js" defer></script></body></html>' % (json.dumps(nb, ensure_ascii=False), JS)
    return head('Ch %d · %s' % (n, ch['title']) if n > 0 else ch['title'], EXTRA_CSS) + body

def chead(eyebrow, title, ptag, pills, lede):
    h = '<div class="chead"><div class="eyebrow">%s</div><h1>%s' % (html.escape(eyebrow), inline(title))
    if ptag:
        cls = {'Very high': 'vhigh', 'High': 'high', 'Medium': 'med', 'Low': 'low'}.get(ptag.replace(' priority', ''), 'high')
        h += '<span class="ptag %s">%s</span>' % (cls, html.escape(ptag))
    h += '</h1><div class="pills">'
    for txt, k in pills:
        h += '<span class="pill %s">%s</span>' % (k, html.escape(txt))
    h += '</div><p class="lede">%s</p></div>' % inline(lede)
    return h

def home_page(chapters, intro_lede, footer):
    fn = lambda c: '%sch%02d.html' % (BASE, c['n'])
    bar = ('<header class="bar"><div class="barin"><a class="home" href="index.html">Library</a><a class="home" href="%shome.html">Contents</a>'
           '<span class="bartitle"><b></b> International Relations notebook</span><a class="home" href="%ssearch.html">Search</a>'
           '<button class="themebtn" id="themebtn" type="button" aria-label="Change theme">Theme</button></div></header>') % (BASE, BASE)
    built = [c for c in chapters if not c.get('pending')]
    cnt = len([c for c in built if c['n'] > 0])
    body = '<body>' + bar + '<main class="page home-page"><div class="chead"><div class="eyebrow">Sarrthi IAS · GS Mains Module · GS-2</div><h1>International Relations</h1>'
    body += '<p class="lede">%s</p>' % inline(intro_lede)
    body += '<p class="prog"><span id="progress"></span> of %d chapters marked done. More chapters will be added as the classes finish.</p>' % cnt
    body += '<div class="row"><a class="btn pri" href="%sch00.html">Start here</a><a class="btn" href="%sch01.html">Chapter 1</a><a class="btn" href="%ssearch.html">Search</a></div></div>' % (BASE, BASE, BASE)
    body += '<section class="part"><h2>Chapters so far</h2><div class="chlist">'
    for c in chapters:
        body += '<a class="chcard%s" href="%s" data-ch="%d" data-secs="%d"><span class="chn">%s</span><span class="cht"><b>%s</b><small>%s</small><span class="cbar"><i></i></span></span><span class="chb"><i class="tick" hidden>Done</i><em>%s</em></span></a>' % (
            ' pending' if c.get('pending') else '', fn(c), c['n'], len(c['secs']), c['n'] if c['n'] else '★', html.escape(c['title']), html.escape(c.get('sub', '')), html.escape(c.get('badge', '')))
    body += '</div></section>'
    body += '<footer>%s</footer></main>' % inline(footer)
    upd = ("(function(){var S=NBS;function upd(){var done=0;document.querySelectorAll('a.chcard[data-ch]').forEach(function(a){var n=+a.dataset.ch,t=+a.dataset.secs,p=S.pct('%s',n,t),rec=(S.get().nb['%s']||{})[n],d=rec&&rec.dt?!!rec.done:p>=.999;var bar=a.querySelector('.cbar i');if(bar)bar.style.width=Math.round(p*100)+'%%';var tk=a.querySelector('.tick');if(tk)tk.hidden=!d;if(d&&n>0)done++});var el=document.getElementById('progress');if(el)el.textContent=done}upd();S.onChange(upd);setTimeout(upd,2500)})();" % (NB_ID, NB_ID))
    body += '<script>%s\n%s</script></body></html>' % (STORE_ONLY, upd)
    return head('International Relations Contents', EXTRA_CSS) + body

def search_page(entries):
    bar = ('<header class="bar"><div class="barin"><a class="home" href="index.html">Library</a><a class="home" href="%shome.html">Contents</a>'
           '<span class="bartitle"><b></b> Search International Relations</span><button class="themebtn" id="themebtn" type="button" aria-label="Change theme">Theme</button></div></header>') % BASE
    body = '<body>' + bar + '<main class="page home-page"><div class="chead"><div class="eyebrow">Find anything</div><h1>Search</h1></div>'
    body += '<input class="sbox" id="q" type="search" placeholder="Type a word, e.g. Quad, Galwan, CAATSA, Westphalia" autofocus><p class="prog" id="cnt"></p><div class="results" id="res"></div></main>'
    body += json_script(entries, 'sdata')
    logic = SEARCH_LOGIC.replace("'geo-ch'", "'%sch'" % BASE).replace('Tables are images and are not searchable.', 'Tables and diagrams are included as text where possible.')
    body += '<script>%s</script><script>%s</script></body></html>' % (logic, STORE_ONLY)
    return head('Search International Relations', EXTRA_CSS) + body

def strip_tags(h):
    t = re.sub(r'<svg.*?</svg>', ' ', h, flags=re.S)
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
    t = re.sub(r'</(p|li|tr|div|h3|h4|summary|aside)>', ' ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()
