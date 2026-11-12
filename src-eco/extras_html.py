# -*- coding: utf-8 -*-
"""HTML renderers for the extras layer (plain-words boxes, formula cards, NCERT boxes, mnemonic cards, sheets)
used by the textbook and the Study Shelf. Same data as the handwritten notes (hand/layerN.py, hand/ncertN.py)."""
import html, re

def e(t): return html.escape(str(t), quote=False)
def tx(t): return html.unescape(re.sub(r'<[^>]+>', ' ', str(t)))

STYLE = '''<style>
.xb{border-radius:6px;padding:.55em .9em .6em;margin:.9em 0;border-left:5px solid #00897b;background:rgba(0,137,123,.10);color:inherit;break-inside:avoid-page}
.xb>.xt{display:block;font-weight:700;font-size:.82em;letter-spacing:.05em;text-transform:uppercase;color:#00796b;margin-bottom:.15em}
.xb.xe{border-left:5px dashed #ef6c00;background:rgba(239,108,0,.09)}.xb.xe>.xt{color:#e65100}
.xb.xh{border-left-color:#6a1b9a;background:rgba(106,27,154,.10);font-weight:600}.xb.xh>.xt{color:#7b1fa2}
.xb.xn{border:2px solid #c77b30;border-left-width:6px;background:rgba(199,123,48,.10);break-inside:auto}.xb.xn>.xt{color:#a8551a;font-size:.9em;border-bottom:1.4px dashed #c77b30;padding-bottom:.15em}
.xb.xn .xw{border-left:4px solid #00897b;background:rgba(0,137,123,.10);padding:.25em .6em;margin:.4em 0}
.xb.xn .xk{border-left:4px solid #6a1b9a;background:rgba(106,27,154,.09);padding:.25em .6em;margin:.4em 0;font-size:.94em}
.xb.xn .xs{font-weight:700;color:#a8551a;margin:.8em 0 .15em;border-bottom:1px solid rgba(199,123,48,.5);break-after:avoid}
.xb.xn .xd{border:1.6px solid #c62828;background:rgba(198,40,40,.09);border-radius:4px;padding:.25em .6em;margin:.5em 0}.xb.xn .xd b{color:#c62828}
.xl{margin:.3em 0;padding-left:1.2em}.xl li{margin:.2em 0}
.xtw{overflow-x:auto;margin:.45em 0}
table.xt{border-collapse:collapse;font-size:.92em;width:100%%}table.xt th{background:rgba(21,101,192,.18);text-align:left}table.xt th,table.xt td{border:1px solid rgba(120,120,120,.45);padding:.2em .5em;vertical-align:top}
.xfr{display:flex;flex-wrap:wrap;gap:.6em;margin:.6em 0}
.xf{flex:1 1 44%%;border:2.4px solid #0d47a1;background:rgba(255,235,59,.20);box-shadow:2px 2px 0 #0d47a1;border-radius:3px;padding:.2em .7em .35em;break-inside:avoid}
.xf.w{flex:1 1 100%%}.xf.xnc{border-color:#a8551a;box-shadow:2px 2px 0 #a8551a;background:rgba(199,123,48,.10)}
.xf .xfn{font-size:.72em;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#0d47a1}.xf.xnc .xfn{color:#a8551a}
.xf .xff{font-size:1.12em;font-weight:700;line-height:1.3}.xf .xfx{font-size:.8em;opacity:.78;line-height:1.2}
.xfh{font-weight:700;color:#0d47a1;margin:.7em 0 0;break-after:avoid}
.xb.xm{border:2px solid #c62828;border-left-width:5px;background:rgba(255,235,59,.18)}.xb.xm>.xt{color:#c62828}
.xm .xmw{font-size:1.6em;font-weight:800;letter-spacing:.18em}
.xtiles{display:flex;flex-wrap:wrap;gap:.35em;margin:.3em 0}.xtile{border:1.6px solid currentColor;border-radius:4px;padding:.05em .5em;flex:1 1 40%%;background:rgba(255,255,255,.35)}.xtile b{color:#c62828;font-size:1.25em;margin-right:.3em}
.xnote{font-size:.82em;opacity:.7;font-style:italic}
.xnum{display:flex;flex-wrap:wrap;gap:.4em;margin:.4em 0}.xnum span{border:1.6px solid #1565c0;border-radius:6px;padding:.05em .6em;background:rgba(21,101,192,.09)}.xnum b{color:#1565c0;margin-right:.3em}
.xchip{display:inline-block;border:1.4px solid #a8551a;border-radius:10px;padding:0 .6em;margin:.15em .2em 0 0;font-size:.9em}
.xg{border:1.6px dashed #6a1b9a;border-radius:4px;background:rgba(106,27,154,.07);padding:.4em .8em;margin:.8em 0;column-count:2;column-gap:1.4em;font-size:.9em}
.xg div{break-inside:avoid;margin:0 0 .3em}.xg b{color:#c62828}.xg u{text-decoration:none;color:#00796b}
@media(max-width:640px){.xg{column-count:1}.xf{flex-basis:100%%}}
</style>'''

def ul(items): return '<ul class="xl">' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
def table(t):
    return '<div class="xtw"><table class="xt"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
        ''.join('<th>%s</th>' % h for h in t['head']), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in t['rows']))
def fm(items, ncert=False, head=None):
    h = ('<div class="xfh">%s</div>' % head) if head else ''
    h += '<div class="xfr">'
    for it in items:
        w = len(it) > 3 and it[3] == 'wide'
        h += '<div class="xf%s%s"><div class="xfn">%s</div><div class="xff">%s</div>%s</div>' % (' w' if w else '', ' xnc' if ncert else '', it[0], it[1], ('<div class="xfx">%s</div>' % it[2]) if it[2] else '')
    return h + '</div>'
def understand(S):
    return ('<div class="xb"><span class="xt">🧠 Understand it first</span>%s</div><div class="xb xe"><span class="xt">✏ Example</span>%s</div>' % (e(S['plain']), e(S['eg'])))
def hook(S): return '<div class="xb xh"><span class="xt">⭐ Remember</span>%s</div>' % e(S['hook'])
def mnemonic(v):
    L = v['letters']; word = v.get('word') or v.get('sentence')
    big = word
    return '<div class="xb xm"><span class="xt">🧠 Memory aid · %s</span><div class="xmw">%s</div><div class="xtiles">%s</div>%s</div>' % (
        e(v.get('title', '')), e(big), ''.join('<span class="xtile"><b>%s</b>%s</span>' % (e(a), e(b)) for a, b in L), ('<div class="xnote">%s</div>' % e(v['note'])) if v.get('note') else '')
def nc_box(src, b):
    h = '<div class="xb xn"><span class="xt">📘 From %s · %s</span>' % (e(src if src.startswith('NCERT') else 'NCERT · ' + src), e(b['ref']))
    if b.get('why'): h += '<div class="xw"><b>In plain words:</b> %s</div>' % b['why']
    if b.get('link'): h += '<div class="xk"><b>Link to the handout:</b> %s</div>' % b['link']
    for k in b.get('blocks', []):
        if k.get('h'): h += '<div class="xs">%s</div>' % k['h']
        if k.get('pts'): h += ul(k['pts'])
        if k.get('fm'): h += fm(k['fm'], True)
        if k.get('tbl'): h += table(k['tbl'])
        if k.get('fig'): h += '<figure class="xfig"><img src="%s" alt="" style="max-width:100%%;max-height:90mm"><figcaption style="font-size:.85em;opacity:.75">%s</figcaption></figure>' % (k['fig'][0], e(k['fig'][1]))
    for d in b.get('d', []):
        h += '<div class="xd"><b>NCERT differs:</b> %s <i>(handout/teacher wins in class)</i></div>' % d
    return h + '</div>'
def gloss(ents):
    return '<div class="xg">' + ''.join('<div><b>%s</b> = <u>%s</u>%s</div>' % (e(a), e(f), (' — ' + e(br)) if br else '') for a, f, br in ents) + '</div><p class="xnote">Meanings are plain-language aids; verify before quoting in an answer.</p>'
