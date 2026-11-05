# -*- coding: utf-8 -*-
"""Governance mnemonic wall sheet: every mnemonic in Governance chapters 1-33, large type, with recall drills. Usage: python3 gov_mnemonic_sheet.py out.pdf"""
import importlib, sys, os, re
from weasyprint import HTML
F = 'file://' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
MODS = [('Module 1', 'Civil Services, Transparency, Accountability, Citizen\'s Charter, RTI', range(1, 15), '#00796b'),
        ('Module 2', 'Corruption, Social Audit, CBI, CVC, Lokpal, Whistleblower, PCA', range(15, 20), '#ef6c00'),
        ('Module 3', 'Governance, E-Governance, Data Protection, Emerging Tech', range(20, 25), '#5e35b1'),
        ('Module 4', 'Civil Society, NGOs, SHGs, Pressure Groups, CAG', range(25, 30), '#c2185b'),
        ('Module 5', 'Regulatory Bodies, FSSAI, CCI', range(30, 34), '#2e7d32')]
def walk(x, out):
    if isinstance(x, tuple):
        if len(x) >= 3 and x[0] == 'mn': out.append((x[1], x[2]))
        for y in x: walk(y, out)
    elif isinstance(x, list):
        for y in x: walk(y, out)
chs = {}
for m in 'abcdefg':
    for c in importlib.import_module('ch_' + m).CHS:
        if 1 <= c['id'] < 40:
            o = []; walk(c['nodes'], o); chs[c['id']] = (c['toc'], o)
CSS = '''
@font-face{font-family:KB;src:url(%(F)s/kalam-latin-700-normal.woff);font-weight:bold}
@font-face{font-family:KL;src:url(%(F)s/kalam-latin-400-normal.woff)}
@font-face{font-family:CB;src:url(%(F)s/caveat-brush-latin-400-normal.woff)}
@page{size:A4;margin:11mm 12mm 14mm 12mm;@bottom-center{content:"Governance mnemonic sheet · " counter(page);font:10pt KL;color:#666}}
b{font-family:KB;color:#000}body{font-family:KL;font-size:13.5pt;color:#222;line-height:1.35}
.cover{height:255mm;text-align:center;padding-top:60mm;page-break-after:always}
.cover h1{font:56pt CB;margin:0;color:#00796b}.cover p{font-size:16pt;margin:8mm 20mm}
.mod{page-break-before:always;font:30pt CB;padding:3mm 5mm;color:#fff;border-radius:6px;margin-bottom:5mm}
.mod small{display:block;font:13pt KL}
.card{border:2.5px solid;border-radius:10px;padding:3mm 5mm;margin:0 0 4.5mm;page-break-inside:avoid}
.w{font:34pt CB;line-height:1.05}.tag{font:10pt KL;color:#777;float:right;text-align:right;max-width:55mm}
.h{font-size:13.5pt}.own{font-size:10pt;color:#8d6e00}
.drill h2{font:26pt CB;margin:0 0 3mm}.dr{border-bottom:1.5px dashed #bbb;padding:2.2mm 0;page-break-inside:avoid}
.dr b{font:22pt CB;display:inline-block;width:62mm}.dr span{font-size:11pt;color:#666}
'''%{'F':F}
h = ['<html><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS]
n = sum(len(chs[i][1]) for i in chs)
h.append('<div class="cover"><h1>Governance<br>Mnemonic Sheet</h1><p>%d mnemonics from all five GS-2 Governance modules, in large type for the wall.</p><p>Teacher\'s and handout mnemonics are kept exactly as given. Mnemonics marked <b>own</b> were added where the material had none.</p><p>Last pages: cover-and-recall drills.</p></div>' % n)
drill = []
for lab, desc, rng, col in MODS:
    h.append('<div class="mod" style="background:%s">%s<small>%s</small></div>' % (col, lab, desc))
    for i in rng:
        toc, o = chs[i]
        for w, html in o:
            own = 'own mnemonic' in html or 'Own anchor' in html
            body = html.replace(' <i>(own mnemonic)</i>', '')
            h.append('<div class="card" style="border-color:%s"><span class="tag">%s%s</span><div class="w" style="color:%s">%s</div><div class="h">%s</div></div>' % (col, toc, '<br><span class="own">own mnemonic</span>' if own else '', col, w, body))
            drill.append((w, toc, col))
h.append('<div class="drill" style="page-break-before:always"><h2>Cover-and-recall drill</h2><p>Hide the right side. Say what each letter stands for, then check against the cards.</p>')
for k, (w, toc, col) in enumerate(drill):
    if k and k % 14 == 0: h.append('<div style="page-break-before:always"></div>')
    h.append('<div class="dr"><b style="color:%s">%s</b><span>%s</span></div>' % (col, w, toc))
h.append('</div></body></html>')
HTML(string=''.join(h)).write_pdf(sys.argv[1] if len(sys.argv) > 1 else 'Governance-Mnemonic-Sheet.pdf')
print(n, 'mnemonics')
