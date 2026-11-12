# -*- coding: utf-8 -*-
"""Styled current-affairs card (shared by the shelf, the book and the handwritten notes).
card(it, label=None, mode='shelf'|'book'|'hand', first=True) -> HTML.
it = a current-affairs item dict from ca/*.py (t, tag, ctx, pts, pro, mains, kw, pyq).
Pictographic memory aids: coloured side-heading chips with icons, highlighted figures (money, %, years),
a strip of key figures, Prelims/Mains pills, keyword chips. Uses its own scoped <style>; works in light and dark."""
import re, html

def e(t): return html.escape(str(t), quote=False)

FIG = re.compile(
    r'(?:(?:\+/-|±)\s?\d+(?:\.\d+)?\s?%)'
    r'|(?:(?:₹|Rs\.?\s?|US\$|\$)\s?\d[\d,]*(?:\.\d+)?(?:\s?(?:lakh crore|crore|billion|million|trillion|lakh|thousand))?)'
    r'|(?:\d[\d,]*(?:\.\d+)?\s?(?:lakh crore|crore|billion|million|trillion|lakh|per cent|%|bps|basis points|quarters?|years?|days?|months?))'
    r'|(?:\b(?:19|20)\d\d(?:\s?[-–]\s?\d{2,4})?\b)')
MONEYLIKE = re.compile(r'₹|Rs|\$|%|crore|lakh|billion|million|trillion|bps|basis|quarter|per cent')

KINDS = [  # (keywords in label, css kind, icon, title colour class)
    (('result', 'outcome', 'impact', 'achievement', 'performance', 'progress', 'gain', 'benefit'), 'ok', '✔'),
    (('concern', 'challenge', 'issue', 'criticism', 'risk', 'problem', 'limitation', 'drawback', 'gap'), 'bad', '⚠'),
    (('way forward', 'solution', 'step', 'recommend', 'suggest', 'reform', 'measure', 'other rbi'), 'go', '➜'),
    (('why', 'significance', 'importance', 'relevance', 'rationale', 'need'), 'why', '★'),
]
def kind_of(label):
    l = label.lower()
    for keys, k, ic in KINDS:
        if any(x in l for x in keys): return k, ic
    return 'def', '●'

def hl(t):
    """escape + highlight figures"""
    s = e(t); out = []; pos = 0
    for m in FIG.finditer(s):
        out.append(s[pos:m.start()]); out.append('<mark class="cax-f">%s</mark>' % m.group(0)); pos = m.end()
    out.append(s[pos:])
    return ''.join(out)

def split_label(t):
    m = re.match(r'^([^:]{2,42}):\s(.*)$', t, flags=re.S)
    return (m.group(1), m.group(2)) if m else (None, t)

def row(t):
    lab, body = split_label(t)
    if lab is None: return '<div class="cax-r k-def">%s</div>' % hl(body)
    k, ic = kind_of(lab)
    return '<div class="cax-r k-%s"><span class="cax-l">%s:</span><span class="cax-x">%s</span></div>' % (k, e(lab), hl(body))

def numbers(pts):
    out = []
    for p in pts:
        lab, body = split_label(p)
        if lab is None: continue
        n = 0
        for m in FIG.finditer(body):
            f = m.group(0)
            if not MONEYLIKE.search(f): continue
            out.append((f.strip(), lab)); n += 1
            if n == 2: break
    seen = set(); res = []
    for f, l in out:
        if f in seen: continue
        seen.add(f); res.append((f, l))
    return res[:6]

STYLE = '''<style>
.cax{border-left:3px solid rgba(21,101,192,.55);margin:3mm 0 4mm;padding:.4mm 0 .4mm 3mm;color:inherit}
.cax-h{display:flex;flex-wrap:wrap;align-items:baseline;gap:2mm}
.cax-t{font-family:%(lab)s;font-weight:700;font-size:1.05em;color:#1565c0;flex:1 1 60%%}
.cax-m,.cax-p{font-size:.76em;opacity:.65}
.cax-ctx{margin:1mm 0;font-style:italic;opacity:.9}
.cax-r{margin:.8mm 0}
.cax-l{font-weight:700;color:#455a64;margin-right:1.2mm}
.cax-r.k-ok .cax-l{color:#2e7d32}.cax-r.k-bad .cax-l{color:#b23b2e}.cax-r.k-go .cax-l{color:#1565c0}.cax-r.k-why .cax-l{color:#00838f}
.cax-x{display:inline}
mark.cax-f{background:linear-gradient(transparent 62%%,rgba(255,193,7,.45) 62%%);color:inherit;font-weight:600;padding:0}
.cax-box{margin:1.4mm 0;padding-left:2.4mm;border-left:2px solid rgba(120,120,120,.4)}
.cax-box>b{font-size:.8em;letter-spacing:.05em;text-transform:uppercase;opacity:.65;display:block}
.cax-kw{margin:1.2mm 0 0;font-size:.88em;opacity:.85}.cax-kw>b{margin-right:1.4mm}
</style>'''
FONT = {'shelf': 'Inter,system-ui,sans-serif', 'book': 'Inter,sans-serif', 'hand': 'KB,Handlee,cursive'}

def card(it, label=None, mode='shelf', first=True, with_extra=True, header=True):
    tagn = {'P': 'Prelims', 'M': 'Mains', 'PM': 'Prelims · Mains'}[it['tag']]
    h = (STYLE % {'lab': FONT[mode]}) if first else ''
    h += '<div class="cax">'
    if header: h += '<div class="cax-h"><span class="cax-t">%s</span>%s<span class="cax-p">%s</span></div>' % (
        e(it['t']), ('<span class="cax-m">%s</span>' % e(label)) if label else '', tagn)
    if it.get('ctx'): h += '<div class="cax-ctx">%s</div>' % hl(it['ctx'])
    for p in it.get('pts', []): h += row(p)
    if with_extra:
        if it.get('pro'): h += '<div class="cax-box"><b>Prelims fodder</b>%s</div>' % ''.join(row(p) for p in it['pro'])
        if it.get('mains'): h += '<div class="cax-box"><b>Mains fodder</b>%s</div>' % ''.join(row(p) for p in it['mains'] if not p.startswith('Keywords'))
    if it.get('kw'):
        h += '<div class="cax-kw"><b>Keywords</b>%s</div>' % ' · '.join(e(k.strip()) for k in re.split(r';', it['kw']) if k.strip())
    if with_extra and it.get('pyq'): h += '<div class="cax-box"><b>PYQ connect</b>%s</div>' % hl(it['pyq'])
    return h + '</div>'
