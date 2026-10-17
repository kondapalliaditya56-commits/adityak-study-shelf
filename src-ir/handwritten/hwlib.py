from weasyprint import HTML
import os
F='file://'+os.path.abspath('node_modules/@fontsource')
CSS='''
@font-face{font-family:PH;src:url(%(F)s/patrick-hand/files/patrick-hand-latin-400-normal.woff)}
@font-face{font-family:KB;src:url(%(F)s/kalam/files/kalam-latin-700-normal.woff);font-weight:bold}
@font-face{font-family:KL;src:url(%(F)s/kalam/files/kalam-latin-400-normal.woff)}
@font-face{font-family:CB;src:url(%(F)s/caveat-brush/files/caveat-brush-latin-400-normal.woff)}
@font-face{font-family:CV;src:url(%(F)s/caveat/files/caveat-latin-700-normal.woff)}
@page{size:A4;margin:9mm 42mm 12mm 19mm;background:#fffdf5;@bottom-right{content:"International Relations · Handwritten Notes · " counter(page);font-family:PH;font-size:8pt;color:#888}}
body{font-family:PH;font-size:10.4pt;line-height:1.2;color:#1a237e;margin:0}
.pg{page-break-after:always}.pg:last-child{page-break-after:auto}
.ttl{display:block;width:fit-content;max-width:calc(100%% - 3mm);box-sizing:border-box;margin:0 auto 3.5mm;border:2.4px solid #111;border-radius:3px;box-shadow:2.2mm 2.2mm 0 #1a237e;padding:.6mm 5mm 1mm;font-family:CB;font-size:20pt;line-height:1.1;letter-spacing:.6px;color:#111;background:#fff;text-align:center}
.sub{display:inline-block;max-width:calc(100%% - 2mm);box-sizing:border-box;border:2px solid #111;border-radius:3px;box-shadow:1.2mm 1.2mm 0 currentColor;padding:0 3.2mm .4mm;font-family:CB;font-size:15pt;line-height:1.15;letter-spacing:.5px;color:#111;background:#fff;margin:2.2mm 1.4mm 2.4mm 0}
.sub.r{border-color:#c62828;color:#c62828}.sub.b{border-color:#1565c0;color:#1565c0}.sub.g{border-color:#2e7d32;color:#2e7d32}
.hl{background:#fff176;padding:0 1px;color:#111}
.rd{color:#c62828}.gn{color:#2e7d32}.bk{color:#111}.pu{color:#6a1b9a}.or{color:#e65100}
b{font-family:KB;font-weight:bold;font-size:.92em}
.br{display:table;width:100%%;table-layout:auto;margin:1.6mm 0}
.lab{display:table-cell;vertical-align:middle;width:1%%;min-width:22mm;max-width:30mm;border:1.8px solid;border-radius:5px;padding:.8mm 2mm;font-family:KB;font-size:10.5pt;line-height:1.15;background:#fff;margin-right:2mm}
.kids{display:table-cell;vertical-align:middle;overflow-wrap:break-word;border-left:3px solid;border-radius:8px 0 0 8px;padding-left:2.4mm}
.kid{margin:.7mm 0}
.kid:before{content:"\\2192  ";color:#999}
.br .br{margin:1.2mm 0}.kid.nb:before{content:""}
.c1{--c:#c62828}.c2{--c:#ef6c00}.c3{--c:#f9a825}.c4{--c:#2e7d32}.c5{--c:#1565c0}.c6{--c:#6a1b9a}.c7{--c:#00838f}
.br>.lab{border-color:var(--c);color:var(--c)}.br>.kids{border-color:var(--c)}
.pk{border:1.8px solid #c62828;background:#fde7ea;padding:1.2mm 2.4mm;margin:1.5mm 0;color:#7f0000;border-radius:3px}
.ye{border:1.8px solid #f9a825;background:#fff9c4;padding:1.2mm 2.4mm;margin:1.5mm 0;color:#333;border-radius:3px}
.gr{border:1.8px solid #2e7d32;background:#e8f5e9;padding:1.2mm 2.4mm;margin:1.5mm 0;color:#1b5e20;border-radius:3px}
.bl{border:1.8px dashed #1565c0;background:#e3f2fd;padding:1.2mm 2.4mm;margin:1.5mm 0;border-radius:3px}
.sw{font-family:CV;font-size:13.5pt;color:#00695c;margin:1mm 0;line-height:1.05}
.sw:before{content:"\\270E  "}
.pyq{font-family:KB;font-size:8.5pt;background:#c62828;color:#fff;border-radius:8px;padding:0 2mm;margin-left:2mm}
.qt{font-family:CV;font-size:14pt;color:#4a148c;border-left:3px solid #4a148c;padding-left:2mm;margin:1.5mm 0}
.row{display:flex;gap:3mm}.row>div{flex:1}
.mn{font-family:KB;font-size:12pt;color:#c62828;letter-spacing:1px}
.arrow{display:flex;align-items:stretch;margin:2mm 0}.arrow>div{flex:1;border-top:3px solid #1565c0;padding:1mm 1.5mm;font-size:10pt;position:relative}
.arrow>div:before{content:"";position:absolute;top:-4px;left:0;width:6px;height:6px;background:#1565c0;border-radius:50%%}
.arrow h4{margin:0;font-family:KB;color:#1565c0;font-size:10.5pt}
table{border-collapse:collapse;width:100%%;font-size:10.3pt}td,th{border:1.4px solid #1a237e;padding:.6mm 1.8mm;vertical-align:top}th{background:#e8eaf6;font-family:KB;text-align:left}
.story{display:flex;align-items:center;justify-content:space-between;margin:1mm 0 2mm;padding:1.5mm 2mm;border:1.8px dashed #888;border-radius:8px;background:#fff}.pn{text-align:center;width:24mm}.cap{font-family:CV;font-size:11pt;line-height:.95;color:#333}.ar2{color:#c62828;font-size:14pt}
.ye{position:relative;transform:rotate(-.35deg);box-shadow:1px 2px 3px #bbb}.ye:before{content:'';position:absolute;top:-2.2mm;left:45%%;width:16mm;height:4mm;background:rgba(244,143,177,.55);transform:rotate(-3deg)}
.pk{box-shadow:1px 2px 3px #ddd}.gr{box-shadow:1px 2px 3px #ddd}
.ca{border:2px solid #0d47a1;border-radius:3px;background:#f3f8ff;padding:1.2mm 2.4mm;margin:2mm 0;color:#0d2a5c;font-size:9.8pt}.ca .tag{display:inline-block;background:#0d47a1;color:#fff;font-family:KB;font-size:8pt;padding:0 2mm;border-radius:8px;margin-right:2mm}
.br,.pk,.ye,.gr,.bl,.ca,.story,table tr{break-inside:avoid}
.ttl,.sub,.sw,table tr:first-child{break-after:avoid}
.chap{break-before:page}
.pyqline{margin:-1mm 0 2mm;text-align:center}
.cov{text-align:center;padding-top:28mm}
.cov h1{font-family:CB;font-size:34pt;color:#1a237e;margin:0 0 4mm;letter-spacing:2px}
.cov .s{font-family:CV;font-size:20pt;color:#c62828;margin-bottom:10mm}
.cov .bx{border:2.4px solid #111;display:inline-block;padding:3mm 8mm;background:#fff;font-family:CB;font-size:15pt;margin:2mm}
.cov .t{font-family:KL;font-size:11pt;color:#444;margin-top:12mm;line-height:1.5}
.toc{text-align:left}.toc h2{font-family:CB;font-size:18pt;border-bottom:2.4px solid #111;margin:0 0 3mm}
.toc .pt{font-family:CB;font-size:15pt;margin:3mm 0 1mm;padding:.6mm 3mm;border-radius:4px;color:#111}
.toc a{display:block;text-decoration:none;color:#1a237e;font-size:10.8pt;line-height:1.35}
.toc a::after{content:leader('.') target-counter(attr(href url),page);color:#c62828;font-family:KB}
.partpg{break-before:page;text-align:center;padding-top:70mm}
.partpg h1{font-family:CB;font-size:30pt;color:#111;margin:0}
.partpg .s{font-family:CV;font-size:18pt;color:#c62828;margin-top:4mm}
.sv{display:block;margin:1mm auto}
'''%dict(F=F)
cols=['c1','c2','c3','c4','c5','c6','c7']
n=[0]
def B(label,kids,c=None,w=None):
    if c is None: c=cols[n[0]%7]; n[0]+=1
    st=' style="max-width:%smm;min-width:%smm"'%(w,w) if w else ''
    return '<div class="br %s"><div class="lab"%s>%s</div><div class="kids">%s</div></div>'%(c,st,label,''.join(k if k.startswith(('<div class="br','<div class="sw')) else '<div class="kid">%s</div>'%k for k in kids))
def S(t,c=''): return '<div class="sub %s">%s</div>'%(c,t)
def SW(t): return '<div class="sw">%s</div>'%t
def box(k,t): return '<div class="%s">%s</div>'%(k,t)
def pg(*x): return '<div class="pg">'+''.join(x)+'</div>'
P=lambda y:'<span class="pyq">PYQ %s</span>'%y
H=lambda t:'<span class="hl">%s</span>'%t
R=lambda t:'<span class="rd"><b>%s</b></span>'%t
def tbl(head,rows):
    return '<table><tr>'+''.join('<th>%s</th>'%h for h in head)+'</tr>'+''.join('<tr>'+''.join('<td>%s</td>'%c for c in r)+'</tr>' for r in rows)+'</table>'
def arrow(items): return '<div class="arrow">'+''.join('<div><h4>%s</h4>%s</div>'%(a,b) for a,b in items)+'</div>'

STAGES='''<svg class="sv" viewBox="0 0 320 150" width="100%" style="max-width:175mm"><defs><marker id="ar" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0L7,3.5L0,7z" fill="#111"/></marker></defs>
<g font-family="KL" text-anchor="middle" font-size="9">
<rect x="100" y="2" width="120" height="20" fill="#fff" stroke="#111" stroke-width="1.6"/><text x="160" y="16" font-family="KB" font-size="11">DIRTY MONEY</text>
<line x1="160" y1="22" x2="160" y2="30" stroke="#111" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="4" y="32" width="312" height="34" rx="6" fill="#fde7ea" stroke="#c62828" stroke-width="1.8"/><text x="50" y="52" font-family="KB" fill="#c62828" font-size="11">1 PLACEMENT</text><text x="205" y="45" font-size="8.5">cash enters system: offshore a/c, deposits,</text><text x="205" y="58" font-size="8.5">smurfing → <tspan font-family="KB" fill="#c62828">RISKIEST stage</tspan> (cash is visible)</text>
<line x1="160" y1="66" x2="160" y2="74" stroke="#111" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="4" y="76" width="312" height="34" rx="6" fill="#fff9c4" stroke="#f9a825" stroke-width="1.8"/><text x="50" y="96" font-family="KB" fill="#b26a00" font-size="11">2 LAYERING</text><text x="205" y="89" font-size="8.5">complex transactions, many routes: forex,</text><text x="205" y="102" font-size="8.5">shell cos, boats/diamonds, USA/Europe a/cs</text>
<line x1="160" y1="110" x2="160" y2="118" stroke="#111" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="4" y="120" width="250" height="28" rx="6" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.8"/><text x="58" y="138" font-family="KB" fill="#2e7d32" font-size="10">3 INTEGRATION</text><text x="188" y="138" font-size="8">re-introduced: business, shells, property</text>
<line x1="254" y1="134" x2="268" y2="134" stroke="#111" stroke-width="1.5" marker-end="url(#ar)"/><circle cx="292" cy="134" r="22" fill="#fff" stroke="#2e7d32" stroke-width="2"/><text x="292" y="132" font-family="KB" font-size="9" fill="#2e7d32">CLEAN</text><text x="292" y="143" font-family="KB" font-size="9" fill="#2e7d32">MONEY</text></g></svg>'''
HAW='''<svg class="sv" viewBox="0 0 320 110" width="100%" style="max-width:150mm"><defs><marker id="ah" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0L7,3.5L0,7z" fill="#1a237e"/></marker></defs><g font-family="KL" font-size="9" text-anchor="middle">
<text x="40" y="12" font-family="KB">Country A</text><text x="280" y="12" font-family="KB">Country B</text>
<rect x="5" y="20" width="70" height="22" rx="4" fill="#e3f2fd" stroke="#1565c0"/><text x="40" y="35">Sender</text>
<rect x="105" y="20" width="75" height="22" rx="4" fill="#fff9c4" stroke="#f9a825"/><text x="142" y="35">Hawaladar A</text>
<rect x="215" y="20" width="75" height="22" rx="4" fill="#fff9c4" stroke="#f9a825"/><text x="252" y="35">Hawaladar B</text>
<rect x="245" y="78" width="70" height="22" rx="4" fill="#e3f2fd" stroke="#1565c0"/><text x="280" y="93">Receiver</text>
<g stroke="#1a237e" stroke-width="1.5" marker-end="url(#ah)" fill="none"><line x1="75" y1="31" x2="105" y2="31"/><line x1="180" y1="31" x2="215" y2="31" stroke-dasharray="4"/><path d="M252 42 L252 60 L270 78"/><path d="M40 42 L40 90 L110 90" stroke-dasharray="2 3"/></g>
<text x="90" y="26" font-size="7.5">cash</text><text x="198" y="26" font-size="7.5">call/code</text><text x="262" y="58" font-size="7.5">code → cash</text><text x="75" y="102" font-size="7.5" fill="#c62828">① A gives CASH  ② A tells B a CODE  ③ B pays out</text></g></svg>'''
MIX='''<svg class="sv" viewBox="0 0 300 80" width="100%" style="max-width:120mm"><g font-family="KL" font-size="8" text-anchor="middle"><rect x="5" y="8" width="50" height="22" rx="3" fill="#e3f2fd" stroke="#1565c0"/><text x="30" y="22">Coins (A)</text><rect x="5" y="45" width="50" height="22" rx="3" fill="#e3f2fd" stroke="#1565c0"/><text x="30" y="59">Coins (B)</text>
<rect x="105" y="15" width="85" height="45" rx="8" fill="#fff9c4" stroke="#f9a825" stroke-width="2"/><text x="147" y="35" font-family="KB" font-size="10">MIXER</text><text x="147" y="48">pools &amp; shuffles</text>
<rect x="245" y="8" width="50" height="22" rx="3" fill="#e8f5e9" stroke="#2e7d32"/><text x="270" y="22">Clean (A')</text><rect x="245" y="45" width="50" height="22" rx="3" fill="#e8f5e9" stroke="#2e7d32"/><text x="270" y="59">Clean (B')</text>
<g stroke="#111" stroke-width="1.3" fill="none"><path d="M55 19 L105 32"/><path d="M55 56 L105 44"/><path d="M190 32 L245 19"/><path d="M190 44 L245 56"/></g></g></svg>'''


def ic(body,w=34): return '<svg viewBox="0 0 40 40" width="%dpx" height="%dpx" style="vertical-align:middle" fill="none" stroke="#111" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</svg>'%(w,w,body)
ICON={
'bag':ic('<path d="M14 9 Q20 3 26 9"/><path d="M12 13 Q6 22 9 31 Q10 36 20 36 Q30 36 31 31 Q34 22 28 13 Z" fill="#c8e6c9"/><text x="15" y="29" font-size="15" fill="#1b5e20" stroke="none" font-weight="bold">$</text>'),
'bank':ic('<path d="M4 15 L20 5 L36 15 Z" fill="#bbdefb"/><path d="M8 18 V30 M16 18 V30 M24 18 V30 M32 18 V30"/><path d="M4 33 H36 M6 36 H34"/>'),
'maze':ic('<rect x="4" y="4" width="32" height="32" fill="#fff9c4"/><path d="M4 12 H26 M14 20 H36 M4 28 H26 M30 4 V12 M10 20 V28"/>'),
'coin':ic('<circle cx="20" cy="20" r="14" fill="#ffe082"/><circle cx="20" cy="20" r="10"/><path d="M16 14 H23 Q26 14 26 17 Q26 20 23 20 H16 M23 20 Q27 20 27 23.500 Q27 26 23 26 H16 M19 11 V29"/>'),
'gavel':ic('<rect x="8" y="6" width="16" height="9" rx="2" transform="rotate(30 16 10)" fill="#ffccbc"/><path d="M19 17 L32 32"/><path d="M5 35 H22"/>'),
'globe':ic('<circle cx="20" cy="20" r="15" fill="#e1f5fe"/><ellipse cx="20" cy="20" rx="6" ry="15"/><path d="M5 20 H35 M8 12 H32 M8 28 H32"/>'),
'lens':ic('<circle cx="17" cy="17" r="10" fill="#e3f2fd"/><path d="M25 25 L35 35" stroke-width="3"/>'),
'shield':ic('<path d="M20 4 L34 9 V20 Q34 31 20 37 Q6 31 6 20 V9 Z" fill="#e8f5e9"/><path d="M13 20 L18 25 L28 14"/>'),
'target':ic('<circle cx="20" cy="20" r="15" fill="#ffebee"/><circle cx="20" cy="20" r="9"/><circle cx="20" cy="20" r="3" fill="#c62828"/><path d="M20 20 L34 6"/>'),
'tree':ic('<path d="M20 36 V22"/><circle cx="20" cy="15" r="10" fill="#c8e6c9"/><circle cx="14" cy="20" r="6" fill="#a5d6a7"/><circle cx="27" cy="20" r="6" fill="#a5d6a7"/>'),
}
ICON['hawala']=ICON['coin']
ICON['people']=ic('<circle cx="13" cy="12" r="5" fill="#ffe0b2"/><circle cx="27" cy="12" r="5" fill="#ffe0b2"/><path d="M4 34 Q4 20 13 20 Q22 20 22 34 Z" fill="#bbdefb"/><path d="M18 34 Q18 20 27 20 Q36 20 36 34 Z" fill="#c8e6c9"/>')
ICON['plane']=ic('<path d="M4 22 L36 10 L30 30 L20 24 L16 32 L14 24 Z" fill="#e3f2fd"/><path d="M14 24 L36 10"/>')
ICON['bridge']=ic('<path d="M3 26 H37"/><path d="M3 26 Q20 4 37 26" fill="#fff9c4"/><path d="M10 26 V18 M20 26 V14 M30 26 V18"/><path d="M3 32 Q10 29 17 32 T31 32 T37 31" stroke="#1565c0"/>')
TI={'MONEY LAUNDERING':'bag','TECHNIQUES':'lens','CRYPTO':'coin','IMPACT':'target','CHALLENGES':'maze','INITIATIVES':'globe','PMLA':'gavel','FATF':'shield','TERROR':'bag','ONE-PAGE':'tree'}
def T(t):
    k=next((v for a,v in TI.items() if t.startswith(a)),'bag')
    return '<div class="ttl">%s&nbsp;%s&nbsp;%s</div>'%(ICON[k],t,ICON[k])
STORY='<div class="story">'+''.join('<div class="pn">%s<div class="cap">%s</div></div>%s'%(ICON[i],c,'<div class="ar2">&#10140;</div>' if j<5 else '') for j,(i,c) in enumerate([('bag','1. Crime earns dirty cash'),('bank','2. PLACEMENT: deposit it'),('maze','3. LAYERING: move it around'),('coin','4. Convert: crypto, goods'),('shield','5. INTEGRATION: looks legit'),('gavel','6. Law strikes: PMLA, ED, FATF')]))+'</div>'

