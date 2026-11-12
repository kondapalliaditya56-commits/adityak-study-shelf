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
    if lab is None: return '<div class="cax-r k-def"><span class="cax-l">●</span><span class="cax-x">%s</span></div>' % hl(body)
    k, ic = kind_of(lab)
    return '<div class="cax-r k-%s"><span class="cax-l">%s %s</span><span class="cax-x">%s</span></div>' % (k, ic, e(lab), hl(body))

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
.cax{border:2px solid #1565c0;border-radius:8px;margin:3mm 0 4mm;padding:0 0 1.2mm;overflow:hidden;background:rgba(21,101,192,.05);color:inherit}
.cax-h{display:flex;flex-wrap:wrap;align-items:center;gap:1.6mm;background:#1565c0;color:#fff;padding:1.2mm 3mm;border-radius:5px 5px 0 0}
.cax-t{font-family:%(lab)s;font-weight:700;font-size:1.06em;flex:1 1 60%%}
.cax-m{font-size:.78em;background:rgba(255,255,255,.2);border-radius:9px;padding:0 2.4mm}
.cax-p{font-size:.78em;font-weight:700;border-radius:9px;padding:0 2.4mm;color:#fff}
.cax-p.P{background:#c62828}.cax-p.M{background:#2e7d32}
.cax-ctx{margin:1.4mm 3mm;font-style:italic}
.cax-nums{display:flex;flex-wrap:wrap;gap:1.6mm;margin:1.2mm 3mm}
.cax-n{display:inline-flex;flex-direction:column;align-items:center;border:1.6px solid #e65100;background:rgba(255,193,7,.22);border-radius:7px;padding:0 2.4mm;line-height:1.15}
.cax-n b{font-family:%(lab)s;font-size:1.05em;color:#bf360c}
.cax-n i{font-style:normal;font-size:.68em;opacity:.8}
.cax-r{display:flex;gap:2mm;align-items:flex-start;margin:1mm 3mm;padding:.6mm 0;border-bottom:1px dotted rgba(120,120,120,.35)}
.cax-l{flex:0 0 27mm;font-family:%(lab)s;font-weight:700;font-size:.82em;color:#fff;border-radius:4px;padding:.3mm 1.6mm;text-align:left;line-height:1.2;background:#6a1b9a}
.cax-r.k-ok .cax-l{background:#2e7d32}.cax-r.k-bad .cax-l{background:#c62828}.cax-r.k-go .cax-l{background:#1565c0}.cax-r.k-why .cax-l{background:#00838f}.cax-r.k-def .cax-l{background:#6a1b9a;flex-basis:5mm;text-align:center}
.cax-x{flex:1 1 auto}
mark.cax-f{background:linear-gradient(transparent 52%%,rgba(255,193,7,.75) 52%%);color:inherit;font-weight:700;padding:0 .4mm}
.cax-box{margin:1.6mm 3mm;border-radius:5px;padding:.8mm 2.6mm;border-left:5px solid #c62828;background:rgba(198,40,40,.07)}
.cax-box.mains{border-color:#2e7d32;background:rgba(46,125,50,.08)}
.cax-box.pyq{border-color:#6a1b9a;background:rgba(106,27,154,.08)}
.cax-box>b{font-family:%(lab)s;font-size:.82em;letter-spacing:.06em;text-transform:uppercase;display:block}
.cax-box .cax-r{margin:.4mm 0;border:0;padding:0}
.cax-kw{margin:1.6mm 3mm 0}.cax-kw .cax-k{display:inline-block;border:1.6px solid #1565c0;border-radius:11px;padding:0 2.4mm;margin:.6mm .8mm 0 0;font-size:.84em;background:rgba(21,101,192,.1)}
.cax-kw>b{font-family:%(lab)s;font-size:.8em;margin-right:1.4mm}
</style>'''
FONT = {'shelf': 'Inter,system-ui,sans-serif', 'book': 'Inter,sans-serif', 'hand': 'KB,Handlee,cursive'}

def card(it, label=None, mode='shelf', first=True, with_extra=True, header=True):
    tagn = {'P': ['Prelims'], 'M': ['Mains'], 'PM': ['Prelims', 'Mains']}[it['tag']]
    h = (STYLE % {'lab': FONT[mode]}) if first else ''
    h += '<div class="cax">'
    if header: h += '<div class="cax-h"><span class="cax-t">%s</span>%s%s</div>' % (
        e(it['t']), ('<span class="cax-m">%s</span>' % e(label)) if label else '',
        ''.join('<span class="cax-p %s">%s</span>' % (x[0], x) for x in tagn))
    if it.get('ctx'): h += '<div class="cax-ctx">%s</div>' % hl(it['ctx'])
    nums = numbers(it.get('pts', []))
    if nums: h += '<div class="cax-nums">%s</div>' % ''.join('<span class="cax-n"><b>%s</b><i>%s</i></span>' % (e(f), e(l)) for f, l in nums)
    for p in it.get('pts', []): h += row(p)
    if with_extra:
        if it.get('pro'): h += '<div class="cax-box"><b>Prelims fodder</b>%s</div>' % ''.join(row(p) for p in it['pro'])
        if it.get('mains'): h += '<div class="cax-box mains"><b>Mains fodder</b>%s</div>' % ''.join(row(p) for p in it['mains'] if not p.startswith('Keywords'))
    if it.get('kw'):
        h += '<div class="cax-kw"><b>🔑 Keywords</b>%s</div>' % ''.join('<span class="cax-k">%s</span>' % e(k.strip()) for k in re.split(r';', it['kw']) if k.strip())
    if with_extra and it.get('pyq'): h += '<div class="cax-box pyq"><b>PYQ connect</b>%s</div>' % hl(it['pyq'])
    return h + '</div>'
