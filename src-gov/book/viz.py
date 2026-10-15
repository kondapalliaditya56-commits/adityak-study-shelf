# -*- coding: utf-8 -*-
"""Remembrance visuals for the book: radial mind map, decision fork, flow chain, mnemonic card.
Each function takes a dict (see visuals.json) and returns an HTML/SVG string sized for the 122 mm text column."""
import html
from PIL import ImageFont

def _font(path):
    return ImageFont.truetype(path, 100)
F_REG = _font('/usr/share/fonts/opentype/inter/Inter-Regular.otf')
F_BOLD = _font('/usr/share/fonts/opentype/inter/Inter-SemiBold.otf')
W = 346.0  # svg units: 1 unit = 1 pt; the text column is about 346 pt wide
PAL = ['#14283F', '#2F6F73', '#B58A3C', '#9C3B2E', '#4F7A36', '#6A4C93', '#3F6E8F', '#8A5A2B']

def esc(t): return html.escape(t, quote=False)

def width(t, size, bold=False):
    return (F_BOLD if bold else F_REG).getlength(t) * size / 100.0

def wrap(text, size, maxw, bold=False):
    out, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if width(t, size, bold) <= maxw or not cur: cur = t
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out

def box(x, y, w, title, lines, color, size=8.1, tsize=8.9, fill='#FFFFFF', head=True, pad=4):
    """Rounded card with coloured title strip. Returns (svg, height)."""
    tl = wrap(title, tsize, w - 2 * pad, True)
    th = len(tl) * (tsize + 2.2) + 4 if head else 0
    body = []
    for ln in lines: body += wrap('• ' + ln if not ln.startswith('→') else ln, size, w - 2 * pad)
    bh = len(body) * (size + 2.6) + 5 if body else 0
    h = th + bh + (0 if body else 2)
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s" stroke="%s" stroke-width="0.9"/>' % (x, y, w, h, fill, color)
    if head:
        s += '<path d="M%.1f %.1fh%.1fv%.1fh-%.1fz" fill="%s" opacity="1"/>' % (x, y + 3, w, th - 3, w, color)
        s = s.replace('<path', '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s"/><path' % (x, y, w, 7, color), 1)
        for i, l in enumerate(tl):
            s += '<text x="%.1f" y="%.1f" font-size="%.1f" font-weight="600" fill="#FFFFFF">%s</text>' % (x + pad, y + 2 + (i + 1) * (tsize + 2.2) - 1.2, tsize, esc(l))
    for i, l in enumerate(body):
        s += '<text x="%.1f" y="%.1f" font-size="%.1f" fill="#1C2733">%s</text>' % (x + pad, y + th + 3 + (i + 1) * (size + 2.6) - 1.6, size, esc(l))
    return s, h

def svgwrap(inner, h, title=None):
    t = '<div class="vtitle">%s</div>' % esc(title) if title else ''
    return '<div class="viz">%s<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.0f %.1f" width="100%%" style="font-family:Inter,sans-serif">%s</svg></div>' % (t, W, h, inner)

def mindmap(d):
    br = d['branches']; n = len(br)
    left, right = br[:(n + 1) // 2], br[(n + 1) // 2:]
    bw = 122.0; gap = 7.0
    cols = []
    for side, items, x in (('L', left, 0.0), ('R', right, W - bw)):
        y = 0.0; rows = []
        for i, b in enumerate(items):
            idx = (br.index(b))
            s, h = box(x, y, bw, b['t'], b['c'], PAL[idx % len(PAL)])
            rows.append((s, y, h, idx)); y += h + gap
        cols.append((rows, y - gap))
    H = max(cols[0][1], cols[1][1] if cols[1][0] else 0) + 2
    cx, cy = W / 2, H / 2
    out = ''
    # connectors first
    for ci, (rows, tot) in enumerate(cols):
        off = (H - 2 - tot) / 2
        for s, y, h, idx in rows:
            by = y + off + h / 2
            bx = bw if ci == 0 else W - bw
            col = PAL[idx % len(PAL)]
            ex = cx - 46 if ci == 0 else cx + 46
            out += '<path d="M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" fill="none" stroke="%s" stroke-width="1.6" opacity=".85"/>' % (bx, by, bx + (ex - bx) * .5, by, bx + (ex - bx) * .5, cy, ex, cy, col)
    for ci, (rows, tot) in enumerate(cols):
        off = (H - 2 - tot) / 2
        for s, y, h, idx in rows:
            out += '<g transform="translate(0 %.1f)">%s</g>' % (off, s)
    cl = wrap(d['center'], 9.6, 78, True)
    out += '<ellipse cx="%.1f" cy="%.1f" rx="48" ry="%.1f" fill="#14283F" stroke="#B58A3C" stroke-width="1.6"/>' % (cx, cy, 14 + len(cl) * 6)
    for i, l in enumerate(cl):
        out += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="9.6" font-weight="600" fill="#FFFFFF">%s</text>' % (cx, cy + 3.4 + (i - (len(cl) - 1) / 2) * 11.5, esc(l))
    return svgwrap(out, H, d.get('title'))

def fork(d):
    root = d['root']; br = d['branches']; n = len(br)
    gapx = 6.0; bw = (W - gapx * (n - 1)) / n
    rs, rh = box((W - 190) / 2, 0, 190, root['t'], root.get('c', []), '#14283F', fill='#EEF3F7')
    top = rh + 20
    boxes = []; mh = 0
    for i, b in enumerate(br):
        lines = list(b.get('c', []))
        s, h = box(i * (bw + gapx), top, bw, b['t'], lines, PAL[(i + 1) % len(PAL)], size=7.9)
        boxes.append((s, h)); mh = max(mh, h)
    out = rs
    for i in range(n):
        x = i * (bw + gapx) + bw / 2
        out += '<path d="M%.1f %.1f V%.1f H%.1f V%.1f" fill="none" stroke="#7A8594" stroke-width="1.1"/>' % (W / 2, rh, rh + 9, x, top - 1)
        out += '<path d="M%.1f %.1f l-3 -5 h6z" fill="#7A8594"/>' % (x, top)
    for s, h in boxes: out += s
    H = top + mh + 2
    for i, b in enumerate(br):
        if b.get('verdict'):
            vl = wrap(b['verdict'], 7.2, bw - 4)
            for j, l in enumerate(vl):
                out += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="7.2" font-style="italic" fill="%s">%s</text>' % (i * (bw + gapx) + bw / 2, top + mh + 9 + j * 9, PAL[(i + 1) % len(PAL)], esc(l))
            H = max(H, top + mh + 9 + len(vl) * 9)
    return svgwrap(out, H + 2, d.get('title'))

def flow(d):
    steps = d['steps']; per = d.get('per_row', 4)
    rows = [steps[i:i + per] for i in range(0, len(steps), per)]
    out = ''; y = 0.0; centers = []
    ag = 13.0
    for r, row in enumerate(rows):
        n = len(row); bw = (W - ag * (per - 1)) / per
        rh = 0; items = []
        for i, st in enumerate(row):
            s, h = box(i * (bw + ag), y, bw, st[0], st[1:] , PAL[(r * per + i) % len(PAL)], size=7.7, tsize=8.4)
            items.append((s, h, i * (bw + ag))); rh = max(rh, h)
        for s, h, x in items: out += s
        for i in range(n - 1):
            x = (i + 1) * (bw + ag) - ag
            out += '<path d="M%.1f %.1f h%.1f" stroke="#7A8594" stroke-width="1.3" fill="none"/><path d="M%.1f %.1f l-4.5 -3.5 v7z" fill="#7A8594"/>' % (x + 1, y + rh / 2, ag - 7, x + ag - 1, y + rh / 2)
        if r < len(rows) - 1:
            lastx = (n - 1) * (bw + ag) + bw / 2
            out += '<path d="M%.1f %.1f v%.1f H%.1f v%.1f" stroke="#7A8594" stroke-width="1.3" fill="none"/><path d="M%.1f %.1f l-3.5 -5 h7z" fill="#7A8594"/>' % (lastx, y + rh, 8, bw / 2, 8, bw / 2, y + rh + 17)
            y += rh + 26
        else: y += rh
    return svgwrap(out, y + 2, d.get('title'))

def mnemonic(d):
    sent = d['sentence'].split(); letters = d['letters']
    spans = ''.join('<span class="w"><b>%s</b>%s</span>' % (esc(w[0]), esc(w[1:])) for w in sent)
    chips = ''.join('<span class="chip"><i>%s</i>%s</span>' % (esc(l[0]), esc(l[1])) for l in letters)
    return ('<div class="mnem"><div class="mlbl">Mnemonic &middot; %s</div><div class="msent">%s</div><div class="mchips">%s</div>%s</div>'
            % (esc(d.get('title', 'Remember it as')), spans, chips, '<div class="mnote">%s</div>' % esc(d['note']) if d.get('note') else ''))

RENDER = {'mindmap': mindmap, 'fork': fork, 'flow': flow, 'mnemonic': mnemonic}
def render(v): return RENDER[v['type']](v)
