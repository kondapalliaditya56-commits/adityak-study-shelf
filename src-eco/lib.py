import re, json, html

SH = '/tmp/claude-0/-home-claude/72cbe3e5-542c-596f-8ef0-06a8d705bf8d/scratchpad/shelf/'
_ch8 = open(SH + 'ch08.html').read()
_styles = re.findall(r'<style>.*?</style>', _ch8, flags=re.S)
STYLE = ''.join(_styles)
_si = _ch8.find('<script>', _ch8.find('id="data"') + 10)
_script = _ch8[_si + 8:_ch8.find('</script>', _si)]
_script = _script[_script.find(';') + 1:]            # drop window.__NB=...;
_k = _script.find('(function(){\nvar D=JSON.parse')
STORE_JS = _script[:_k]
CHAP_JS = _script[_k:]

import sys
sys.path.insert(0,'/tmp/claude-0/-home-claude/72cbe3e5-542c-596f-8ef0-06a8d705bf8d/scratchpad')
from pyqlib import *
from pyqlib import _secs_for
import book_export as BE
sys.path.insert(0, '/home/claude/adityak-study-shelf/src-gov/book')
import viz as BV
NB_ID = 'economy'
PFX = 'eco-'


def esc(s):
    return html.escape(str(s), quote=False)


def md(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a class="xref" href="%s">%s</a>' % (m.group(2), m.group(1)), s)
    return s


def slug(t):
    t = re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
    return t[:48].rstrip('-')


class Ch:
    def __init__(self, n, title, eyebrow, pills, lede):
        self.n, self.title, self.eyebrow, self.pills, self.lede = n, title, eyebrow, pills, lede
        self.secs = []       # (id, title, html, plain)
        self.cur = None
        self.timeline = []   # (label, text, star)
        self.connects = []
        self.recall = []
        self.mcq = []
        self.cards = []
        self.mains = []
        self.mm = None

    # ---- block builders (append to current section)
    def sec(self, title, sid=None):
        sid = sid or slug(title)
        self.cur = {'id': sid, 'title': title, 'html': [], 'plain': [], 'items': []}
        self.secs.append(self.cur)

    def _add(self, h, plain='', item=None):
        if item is not None: self.cur['items'].append(item)
        self.cur['html'].append(h)
        self.cur['plain'].append(re.sub(r'<[^>]+>', ' ', plain or h))

    def p(self, t):
        self._add('<p>%s</p>' % md(t), t, ('p', t))

    def ul(self, items):
        out = ["<ul class='lst'>"]
        for it in items:
            if it.startswith('> '):
                out.append("<li class='sub'>%s</li>" % md(it[2:]))
            else:
                out.append('<li>%s</li>' % md(it))
        out.append('</ul>')
        self._add('\n'.join(out), ' '.join(items), ('ul', list(items)))

    def ol(self, items):
        self._add('<div class="stepsblock"><ol>%s</ol></div>' % ''.join('<li>%s</li>' % md(i) for i in items), ' '.join(items), ('ol', list(items)))

    def h3(self, t):
        self._add('<h3>%s</h3>' % md(t), t, ('h3', t))

    def call(self, kind, tag, body):
        if isinstance(body, str):
            body = [body]
        inner = ''.join('<p>%s</p>' % md(b) for b in body)
        self._add('<aside class="callout %s"><span class="tag">%s</span>%s</aside>' % (kind, esc(tag), inner), ' '.join(body), ('call', kind, tag, list(body)))

    def table(self, cap, headers, rows, rowhead=True):
        h = '<div class="tblock">'
        if cap:
            h += '<div class="tcap">%s</div>' % md(cap)
        h += '<div class="tablewrap"><table><thead><tr>%s</tr></thead><tbody>' % ''.join('<th>%s</th>' % md(x) for x in headers)
        for r in rows:
            cells = []
            for i, c in enumerate(r):
                if i == 0 and rowhead:
                    cells.append("<th scope='row'>%s</th>" % md(c))
                else:
                    cells.append('<td>%s</td>' % md(c))
            h += '<tr>%s</tr>' % ''.join(cells)
        h += '</tbody></table></div></div>'
        self._add(h, (cap or '') + ' ' + ' '.join(headers) + ' ' + ' '.join(' '.join(r) for r in rows), ('table', cap, list(headers), [list(r) for r in rows]))

    def fig(self, img, cap, alt=None):
        alt = alt or cap
        h = '<figure><a class="zoom" href="img/%s"><img src="img/%s" alt="%s" loading="lazy"></a><figcaption><span class="figsrc">Handout figure</span> %s</figcaption></figure>' % (img, img, esc(alt), md(cap))
        self._add(h, cap, ('fig', img, cap))

    def flow(self, steps, cap=None):
        h = '<div class="flow">'
        if cap:
            h += '<div class="tcap">%s</div>' % md(cap)
        h += '<div class="chain">'
        for i, s in enumerate(steps):
            kind = ''
            lab = s[0]; sub = s[1] if len(s) > 1 else ''
            if len(s) > 2:
                kind = ' ' + s[2]
            if i:
                h += '<div class="arr"></div>'
            h += '<div class="step%s"><div class="sl">%s</div>%s</div>' % (kind, md(lab), ('<div class="ss">%s</div>' % md(sub)) if sub else '')
        h += '</div></div>'
        self._add(h, ' '.join(' '.join(s[:2]) for s in steps), ('flow', cap, [list(x[:2]) for x in steps]))

    def lanes(self, lanes, cap=None):
        """lanes: list of (heading, [ (label, sub, kind) ... ])"""
        h = '<div class="flow">'
        if cap:
            h += '<div class="tcap">%s</div>' % md(cap)
        h += '<div class="lanes">'
        plain = []
        for head, steps in lanes:
            h += '<div class="lane"><div class="lane-h">%s</div><div class="chain">' % esc(head)
            for i, s in enumerate(steps):
                kind = (' ' + s[2]) if len(s) > 2 else ''
                if i:
                    h += '<div class="arr"></div>'
                h += '<div class="step%s"><div class="sl">%s</div>%s</div>' % (kind, md(s[0]), ('<div class="ss">%s</div>' % md(s[1])) if len(s) > 1 and s[1] else '')
                plain.append(' '.join(s[:2]))
            h += '</div></div>'
        h += '</div></div>'
        self._add(h, ' '.join(plain), ('lanes', cap, [(hd, [list(x[:2]) for x in st]) for hd, st in lanes]))


# ---------------------------------------------------------------- mind map
def wrap(t, n=34):
    if len(t) <= n:
        return [t]
    words = t.split(); a = ''; lines = []
    for w in words:
        if len((a + ' ' + w).strip()) > n and a:
            lines.append(a); a = w
        else:
            a = (a + ' ' + w).strip()
    lines.append(a)
    return lines[:2] if len(lines) > 1 else lines


def mindmap(root, branches, title):
    """branches: [(label, [(leaf, note|None), ...])]"""
    RW = 7.0
    leaf_items = []
    # layout
    y = 8
    cols = []
    for bi, (bl, leaves) in enumerate(branches):
        ls = []
        for leaf, note in leaves:
            lines = wrap(leaf)
            if note:
                lines = lines[:1] + [note]
            h = 28 if len(lines) == 1 else 40
            w = max(len(l) for l in lines) * 7.0 + 20
            ls.append({'lines': lines, 'h': h, 'w': w, 'note': bool(note), 'y': y})
            y += h + 8
        y += 10
        cols.append(ls)
    total_h = y
    rootlines = wrap(root, 14)
    rw = max(len(l) for l in rootlines) * 8.4 + 20
    rh = 22 * len(rootlines) + 6
    bx = 8 + rw + 64
    maxbw = max(len(b[0]) for b in branches) * 7.6 + 24
    lx = bx + maxbw + 56
    maxlw = max(l['w'] for ls in cols for l in ls)
    W = lx + maxlw + 10
    ry = total_h / 2 - rh / 2
    svg = ['<svg class="mm" viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-label="Mind map: %s">' % (W, total_h, W, total_h, esc(title))]
    svg.append('<rect class="mm-root" x="8" y="%.1f" width="%.1f" height="%.1f" rx="6"/>' % (ry, rw, rh))
    for i, l in enumerate(rootlines):
        svg.append('<text class="mm-root-t" x="%.1f" y="%.1f" text-anchor="middle">%s</text>' % (8 + rw / 2, ry + 20 + i * 18, esc(l)))
    for bi, (bl, leaves) in enumerate(branches):
        c = 'c%d' % (bi % 8)
        ls = cols[bi]
        top = ls[0]['y']; bot = ls[-1]['y'] + ls[-1]['h']
        by = (top + bot) / 2
        bw = len(bl) * 7.6 + 24
        svg.append('<path class="mm-link %s" d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>' % (c, 8 + rw, total_h / 2, 8 + rw + 32, total_h / 2, bx - 32, by, bx, by))
        svg.append('<rect class="mm-branch %s" x="%.1f" y="%.1f" width="%.1f" height="28" rx="5"/>' % (c, bx, by - 14, bw))
        svg.append('<text class="mm-branch-t" x="%.1f" y="%.1f" text-anchor="middle">%s</text>' % (bx + bw / 2, by + 4.5, esc(bl)))
        for l in ls:
            cy = l['y'] + l['h'] / 2
            svg.append('<path class="mm-link %s" d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>' % (c, bx + bw, by, bx + bw + 28, by, lx - 28, cy, lx, cy))
            svg.append('<rect class="mm-leaf %s" x="%.1f" y="%.1f" width="%.1f" height="%d" rx="4"/>' % (c, lx, l['y'], l['w'], l['h']))
            for j, t in enumerate(l['lines']):
                cls = 'mm-leaf-n' if (l['note'] and j == len(l['lines']) - 1) else 'mm-leaf-t'
                ty = l['y'] + (19 if len(l['lines']) == 1 else 15 + j * 15)
                svg.append('<text class="%s" x="%.1f" y="%.1f">%s</text>' % (cls, lx + 10, ty, esc(t)))
    svg.append('</svg>')
    outline = ['<ul class="outline"><li><strong>%s</strong><ul>' % esc(root)]
    for bi, (bl, leaves) in enumerate(branches):
        outline.append('<li class="c%d"><details open><summary>%s</summary><ul>' % (bi % 8, esc(bl)))
        for leaf, note in leaves:
            outline.append('<li>%s%s</li>' % (esc(leaf), (' <span class="ol-note">%s</span>' % esc(note)) if note else ''))
        outline.append('</ul></details></li>')
    outline.append('</ul></li></ul>')
    return ''.join(svg), ''.join(outline)


SHELF_VIZ_CSS = """<style>
.lst li{margin:6px 0}
.vwrap{margin:16px 0}
.vwrap .viz{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 12px;overflow-x:auto}
.vwrap .viz svg{min-width:460px;display:block}
.vwrap .vtitle{font:700 13px/1.3 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#1F4E5F;margin:0 0 8px;padding-bottom:6px;border-bottom:1px solid #E2C98A}
.vwrap .mnem{background:var(--acc-soft);border:1px solid var(--line);border-radius:12px;padding:14px 16px;color:var(--ink)}
.vwrap .mlbl{font:700 12px var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--saf);margin-bottom:8px}
.vwrap .tiles{margin:4px 0 8px}
.vwrap .tile{display:inline-block;min-width:38px;padding:6px 6px;margin:0 6px 6px 0;text-align:center;font:700 26px/1 var(--serif);color:var(--acc);background:var(--surface);border:1.5px solid var(--saf);border-radius:8px}
.vwrap .tsep{display:inline-block;font:600 16px var(--sans);color:var(--saf);margin:0 8px 0 2px;vertical-align:middle}
.vwrap .mhook{font:italic 600 17px/1.45 var(--serif);margin:2px 0 10px}
.vwrap .mchips .chip{display:flex;gap:8px;align-items:baseline;font:15px/1.45 var(--sans);padding:3px 0;margin:0;background:none;border:0;border-radius:0;box-shadow:none;color:var(--ink);white-space:normal;height:auto}
.vwrap .mchips .chip i{flex:0 0 44px;font-style:normal;font-weight:700;color:var(--saf)}
.vwrap .msent{font:600 20px/1.4 var(--serif)}.vwrap .msent b{color:var(--saf);font-size:26px}.vwrap .msent .w{margin-right:6px}
.vwrap .mnote{font:13px/1.4 var(--sans);color:var(--muted);margin-top:8px}
@media (max-width:560px){.vwrap .tile{min-width:30px;font-size:21px}}
</style>"""


def layer(ch):
    return BE.LAYERS.get(str(ch.n))


def vhtml(v):
    return '<div class="vwrap">%s</div>' % BV.render({k: x for k, x in v.items() if k != 'after'})


def _item_texts(it, is_lens):
    k = it[0]
    if k == 'p': return [BE.plain(it[1])]
    if k == 'ul':
        items = []
        for x in it[1]:
            if x.startswith('> ') and items: items[-1] += '; ' + x[2:]
            else: items.append(x)
        return [BE.plain(x) for x in items]
    if k == 'ol': return [BE.plain(x) for x in it[1]]
    if k == 'h3': return [BE.plain(it[1])]
    if k == 'call':
        if is_lens and it[2] == 'key': return []
        return [BE.plain(it[2]) + ' ' + ' '.join(BE.plain(b) for b in it[3])]
    if k == 'table':
        _, cap, hd, rows = it
        return [BE.plain(cap or '') + ' ' + ' '.join(BE.plain(x) for x in hd) + ' ' + ' '.join(BE.plain(c) for r in rows for c in r)]
    if k == 'fig': return [BE.plain(it[2])]
    if k == 'flow': return [BE.plain(it[1] or '') + ' ' + ' '.join(a for a, b in it[2])]
    if k == 'lanes': return [BE.plain(hd) for hd, st in it[2]]
    return []


def placements(ch):
    """{(sec_index, html_index): [viz dict]}; html_index -1 = directly under the heading. Same first-match rule as the book exporter."""
    L = layer(ch)
    out = {}
    if not L: return out
    last = {}
    for v in L['visuals']:
        a = v.get('after')
        if v.get('pos') == 'top' or not a: continue
        hit = None
        for si, s in enumerate(ch.secs):
            is_lens = s['title'].startswith('Exam lens')
            if a in ('lens' if is_lens else BE.plain(s['title'])): hit = (si, -1); break
            for hi, it in enumerate(s['items']):
                if any(a in t for t in _item_texts(it, is_lens)): hit = (si, hi); break
            if hit: break
        if hit is None: raise SystemExit('shelf anchor not found: %r' % a)
        if hit in last: out[hit].append(v)
        else: out[hit] = [v]; last[hit] = 1
    return out


def top_blocks(ch):
    L = layer(ch)
    if not L: return ''
    h = '<section class="simple"><h2 id="in-simple-words">In simple words<a class="anchor" href="#in-simple-words">#</a></h2><aside class="callout"><span class="tag">In simple words</span><ul class="lst">%s</ul></aside>' % ''.join('<li>%s</li>' % md(x) for x in L['simple'])
    rows = ''.join('<tr><th scope="row">%s</th><td>%s</td></tr>' % (md(a), md(b)) for a, b in L['terms'])
    h += '<div class="tblock"><div class="tcap">Key terms in plain words</div><div class="tablewrap"><table><thead><tr><th>Key term</th><th>In plain words</th></tr></thead><tbody>%s</tbody></table></div></div>' % rows
    if not any(v['type'] == 'mnemonic' and v.get('word') for v in L['visuals']):
        h += '<aside class="callout key"><span class="tag">Remember it as</span><p>%s</p></aside>' % md(L['remember'])
    h += ''.join(vhtml(v) for v in L['visuals'] if v.get('pos') == 'top')
    return h + '</section>'


def traps_section(ch):
    L = layer(ch)
    if not L or not L.get('traps'): return ''
    h = '<section><h2 id="exam-traps">Exam traps<a class="anchor" href="#exam-traps">#</a></h2><p class="gdesc">Each trap ends with a rule for the exam hall.</p>'
    for t in L['traps']:
        h += '<aside class="callout alert"><span class="tag">%s: %s</span><p>%s</p><p><strong>%s</strong></p></aside>' % (esc(t['k']), md(t['t']), md(t['d']), md(t['r']))
    return h + '</section>'


# ---------------------------------------------------------------- page assembly
HEAD = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>@@T@@</title>' + STYLE + CSS_PYQ + SHELF_VIZ_CSS + '</head>'


def chap_page(ch, prev, nxt, total_chapters):
    def fn(n):
        return '%sch%02d.html' % (PFX, n)
    toc = ''.join('<li><a href="#%s">%s</a></li>' % (s['id'], md(s['title'])) for s in all_sections(ch))
    bar = '<header class="bar"><div class="barin"><a class="home" href="index.html">Library</a><a class="home" href="%shome.html">Contents</a>' % PFX
    if prev is not None:
        bar += '<a class="nbtn" href="%s" title="%s" aria-label="Previous chapter">‹</a>' % (fn(prev[0]), esc(prev[1]))
    else:
        bar += '<span class="nbtn off">‹</span>'
    bar += '<span class="bartitle"><b>Ch %d</b> %s</span>' % (ch.n, esc(ch.title))
    if nxt is not None:
        bar += '<a class="nbtn" href="%s" title="%s" aria-label="Next chapter">›</a>' % (fn(nxt[0]), esc(nxt[1]))
    else:
        bar += '<span class="nbtn off">›</span>'
    bar += '<a class="home" href="%ssearch.html">Search</a><a class="home" href="%stimeline.html">Timeline</a><label class="done"><input type="checkbox" id="donebox" data-ch="%d"><span>Done</span></label><button class="aabtn" id="aabtn" type="button" aria-label="Reading settings">Aa</button></div></header>' % (PFX, PFX, ch.n)
    _pre, _mn = chapter_pyqs(ch)
    _pl = [(c, ('Handout quotes no PYQs' if t == 'No PYQs quoted' else t)) for c, t in ch.pills]
    _tot = len(_pre) + len(_mn)
    _pl.append(('', 'PYQ sheets: %d Prelims · %d Mains · %s' % (len(_pre), len(_mn), BE.priority(ch) and {'H': 'High', 'M': 'Medium', 'L': 'Light'}[BE.priority(ch)])))
    pills = ''.join('<span class="pill %s">%s</span>' % (c, esc(t)) for c, t in _pl)
    body = '<main class="page"><div class="chead"><div class="eyebrow">%s</div><h1>%s</h1><div class="pills">%s</div><p class="lede">%s</p></div>' % (esc(ch.eyebrow), esc(ch.title), pills, md(ch.lede))
    if ch.mm:
      svg, outline = mindmap(ch.mm[0], ch.mm[1], ch.title)
      body += '<section class="mapblock"><h2 id="chapter-map">Chapter map<a class="anchor" href="#chapter-map">#</a></h2><div class="seg" role="group" aria-label="Map view"><button type="button" data-v="map" aria-pressed="true">Map</button><button type="button" data-v="outline" aria-pressed="false">Outline</button></div><div id="mm-map" class="mmframe">%s</div><div id="mm-outline" hidden>%s</div></section>' % (svg, outline)
    body += top_blocks(ch)
    body += '<div class="notes">'
    _PL = placements(ch)
    _sec = _secs_for(ch); _cs = counts_by_section(ch); _PC = {}
    for _n, (_id, _t) in _sec.items():
        if _n in _cs: _PC[_id] = _cs[_n]
    for _si, s in enumerate(ch.secs):
        body += '<h2 id="%s">%s<a class="anchor" href="#%s" aria-label="Link to this section">#</a></h2>\n' % (s['id'], md(s['title']), s['id'])
        _pc = _PC.get(s['id'])
        if _pc: body += '<a class="pyqlink" href="#pyq-%s">PYQs for this topic: %d Prelims · %d Mains</a>\n' % (s['id'], _pc[0], _pc[1])
        for _v in _PL.get((_si, -1), []): body += vhtml(_v) + '\n'
        for _hi, _h in enumerate(s['html']):
            body += _h + '\n'
            for _v in _PL.get((_si, _hi), []): body += vhtml(_v) + '\n'
        if s['title'].startswith('Exam lens') and lens_note(ch):
            _ln = lens_note(ch)
            body += '<aside class="callout note"><span class="tag">PYQ sheets</span>' + ''.join('<p>%s</p>' % md(x) for x in _ln) + '</aside>\n'
    body += '</div>'
    body += traps_section(ch)
    body += pyq_section(ch)
    # timeline
    if ch.timeline:
        body += '<section><h2 id="chapter-timeline">Timeline and numbers<a class="anchor" href="#chapter-timeline">#</a></h2><ol class="timeline">'
        for lab, txt, star in ch.timeline:
            body += '<li class="tl %s"><time class="yr">%s</time><span class="pin"></span><div class="tlbody">%s%s</div></li>' % ('high' if star else '', esc(lab), md(txt), '<span class="star" title="High-yield">★</span>' if star else '')
        body += '</ol></section>'
    if ch.connects:
      body += '<section><h2 id="connects">Connects to<a class="anchor" href="#connects">#</a></h2><div class="lkgrid">'
      for line, reason in ch.connects:
        body += '<article class="link"><div class="lk-line">%s</div><p>%s</p></article>' % (md(line), md(reason))
      body += '</div></section>'
    if ch.recall:
     body += '<section><h2 id="recall">Recall sheet<a class="anchor" href="#recall">#</a></h2><p class="gdesc">Read once, hide it, then rebuild the chapter from memory.</p><ol class="recall">%s</ol></section>' % ''.join('<li>%s</li>' % md(r) for r in ch.recall)
    if ch.mcq:
        body += '<section><h2 id="practice">Test yourself<a class="anchor" href="#practice">#</a></h2>'
        body += '<p class="gdesc">Practice questions below are written from the handout. They are not past-year questions.</p>'
        body += '<h3>Quick quiz</h3><div class="count" id="score">0 / 0 correct</div><div id="quiz"></div>'
        body += '<h3>Mains practice: answer skeletons</h3><p class="gdesc">Try the answer on a blank page first, then open the skeleton.</p>'
        for q, intro, pts, close in ch.mains:
            body += '<details class="q"><summary class="qt">%s</summary><p><strong>Intro:</strong> %s</p><ul class="lst">%s</ul><p><strong>Closing line:</strong> %s</p></details>' % (md(q), md(intro), ''.join('<li>%s</li>' % md(x) for x in pts), md(close))
        body += '<h3>Flashcards</h3><p class="gdesc">Tap the card to flip.</p><div class="deck"><div class="fc" id="fc" tabindex="0" role="button" aria-label="Flashcard, press to flip"></div><div class="count" id="fccount"></div><div class="row"><button class="btn" id="fcprev" type="button">Back</button><button class="btn pri" id="fcnext" type="button">Next</button><button class="btn" id="fcmiss" type="button">Missed it</button><button class="btn" id="fcshuf" type="button">Shuffle</button><button class="btn" id="fconlymiss" type="button">Only missed</button><button class="btn" id="fcall" type="button">All cards</button></div></div></section>'
    body += '<nav class="pager">'
    body += ('<a href="%s"><small>Previous</small>%s</a>' % (fn(prev[0]), esc(prev[1]))) if prev else '<span></span>'
    body += ('<a class="nx" href="%s"><small>Next</small>%s</a>' % (fn(nxt[0]), esc(nxt[1]))) if nxt else '<span></span>'
    body += '</nav><footer>Personal study notes built from the Sarrthi IAS GS Foundation Economy handout (Aditya Kalia). ' + getattr(ch,'footer_note','Handout only: no class slides or teacher ink for this chapter.') + ' Copyright belongs to the teacher; keep this private.</footer></main>'
    layout = '<div class="layout"><aside class="sidetoc"><div class="sth">In this chapter</div><ol>%s</ol></aside>%s</div>' % (toc, body[body.find('<main'):])
    data = json.dumps({'mcq': ch.mcq, 'cards': [{'q': q, 'a': a} for q, a in ch.cards]}, ensure_ascii=False).replace('</', '<\\/')
    nb = 'window.__NB=%s;' % json.dumps({'id': NB_ID, 'ch': ch.n, 'title': ch.title})
    return HEAD.replace('@@T@@', esc('Ch %d · %s' % (ch.n, ch.title))) + '<body>' + bar + layout + '<div id="lightbox" hidden><img alt=""></div><script type="application/json" id="data">' + data + '</script><script>' + nb + STORE_JS + CHAP_JS + '</script><script src="hl.js" defer></script></body></html>'


def all_sections(ch):
    out = [{'id': 'chapter-map', 'title': 'Chapter map'}]
    if layer(ch): out.append({'id': 'in-simple-words', 'title': 'In simple words'})
    out += [{'id': s['id'], 'title': s['title']} for s in ch.secs]
    if layer(ch) and layer(ch).get('traps'): out.append({'id': 'exam-traps', 'title': 'Exam traps'})
    if chapter_pyqs(ch)[0] or chapter_pyqs(ch)[1]:
        out.append({'id': 'pyq', 'title': 'Past-year questions'})
    if ch.timeline:
        out.append({'id': 'chapter-timeline', 'title': 'Timeline and numbers'})
    out += [{'id': 'connects', 'title': 'Connects to'}, {'id': 'recall', 'title': 'Recall sheet'}, {'id': 'practice', 'title': 'Test yourself'}]
    return out
