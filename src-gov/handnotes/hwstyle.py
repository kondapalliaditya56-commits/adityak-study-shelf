# -*- coding: utf-8 -*-
"""Visual layer for the handwritten print notes: font themes, coloured side headings, key-point highlighting,
pictograms (emoji) for memory, tighter spacing. Content is never changed, only styled."""
import os, re
F = 'file://' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
THEMES = {
 # name: (body, bold, heading, label)
 'gaegu':   ('Gaegu', 'Gaegu', 'CB', 'Gaegu', 13.2),
 'neucha':  ('Neucha', 'KB', 'CB', 'KB', 11.2),
 'handlee': ('HandleeM', 'HandleeH', 'CB', 'HandleeH', 11.2),
 'patrick': ('PH', 'KB', 'CB', 'KB', 10.8),
 'indie':   ('Indie', 'KB', 'Shadows', 'KB', 10.0),
}
FACES = '''
@font-face{font-family:Gaegu;src:url(%(F)s/gaegu-latin-400-normal.woff)}
@font-face{font-family:Gaegu;font-weight:bold;src:url(%(F)s/gaegu-latin-700-normal.woff)}
@font-face{font-family:Neucha;src:url(%(F)s/neucha-latin-400-normal.woff)}
@font-face{font-family:Handlee;src:url(%(F)s/handlee-latin-400-normal.woff)}
@font-face{font-family:HandleeM;src:url(%(F)s/handlee-medium.ttf)}
@font-face{font-family:HandleeH;src:url(%(F)s/handlee-heavy.ttf)}
@font-face{font-family:Indie;src:url(%(F)s/indie-flower-latin-400-normal.woff)}
@font-face{font-family:Shadows;src:url(%(F)s/shadows-into-light-latin-400-normal.woff)}
'''
def css(theme='gaegu', label=''):
    body, bold, head, lab, size = THEMES[theme]
    return (FACES % dict(F=F)) + '''
body{font-family:%(body)s,PH;font-size:%(size)spt;line-height:1.2;color:#0f1a5c}
b{font-family:%(bold)s,KB;font-weight:bold;font-size:1em;color:#b71c1c}
td,th{padding:.35mm 1.6mm;line-height:1.1}
td:first-child{background:#eef7f6}td:first-child b{color:#00695c}
th{background:#d9e0f7;color:#1a237e;font-family:%(bold)s,KB}
.lab{font-family:%(bold)s,KB;font-size:1em;padding:.5mm 1.8mm}
.br{margin:1.1mm 0}.kid{margin:.35mm 0}.kids{padding-left:2mm}
.sub{font-family:%(head)s,CB;margin:1.6mm 1.4mm 1.8mm 0}
.pk,.ye,.gr,.bl,.ca{margin:1.1mm 0;padding:.9mm 2.2mm 1mm}
.pk b{color:#0d47a1}.pk{color:#6a0000}
.gr b{color:#bf360c}.ca b{color:#b71c1c}.ye b{color:#b71c1c}
.k{background:linear-gradient(transparent 58%%,#fff176 58%%,#fff176 100%%);padding:0 1px;border-radius:2px}
.pk .k{background:linear-gradient(transparent 58%%,#ffe082 58%%,#ffe082 100%%)}
.pk:before,.ye:after,.gr:before,.bl:before{font-family:"Noto Color Emoji";font-size:11pt;float:right;margin:0 0 0 2mm}
.pk:before{content:"\\2B50"}.gr:before{content:"\\2705"}.bl:before{content:"\\1F4A1"}
.ye:after{content:"\\1F4CC";position:absolute;right:1.5mm;top:-3.2mm;left:auto;width:auto;height:auto;background:none;transform:none;font-size:13pt}
.ye:before{display:none}.ye{padding-top:1.6mm}
.ca:before{content:"\\1F4F0 ";font-family:"Noto Color Emoji";font-size:10pt}
.pic{font-family:"Noto Color Emoji";font-size:.95em;font-style:normal;margin-right:1.2mm;font-weight:normal;vertical-align:-1px}
.mn{font-size:1.15em;letter-spacing:1.5px}
@page{@bottom-left{content:"%(label)s";font-family:PH;font-size:7pt;color:#aaa}}
''' % dict(body=body, bold=bold, head=head, size=size, label=label)

PIC = [  # (regex on plain label, emoji) first match wins
 (r'establish|origin|born|history|why and how|background|genesis|set up|creat', '\U0001F3DB️'),
 (r'compos|structure|member|strength|size|constitut', '\U0001F465'),
 (r'select|committee|panel|appoint|nominat|elect', '\U0001F5F3️'),
 (r'eligib|qualif|who can', '\U0001F393'),
 (r'term|tenure|age limit|duration|retire', '⏳'),
 (r'remov|impeach|dismiss|suspen|disqualif', '\U0001F6AA'),
 (r'salar|allowance|pay|fund|finance|tax|fiscal|grant|budget|cess|revenue|gst|loan|borrow', '\U0001F4B0'),
 (r'power|function|role|jurisdic|authority|mandate', '⚡'),
 (r'procedure|step|process|working|how .* work|stages', '\U0001F4DD'),
 (r'complain|petition|writ|remed|redress|grievance', '\U0001F4EC'),
 (r'court|judg|supreme|high court|tribunal|verdict|case|doctrine', '⚖️'),
 (r'right|liberty|freedom|equal|dignity|protect|safeguard|security', '\U0001F6E1️'),
 (r'duty|duties|obligation|responsib', '\U0001F91D'),
 (r'law|act\b|bill|amend|statute|article|section|provision|ordinance|legislat', '\U0001F4DC'),
 (r'parliament|lok sabha|rajya sabha|speaker|house|assembly|council|session', '\U0001F3DB️'),
 (r'president|governor|prime minister|chief minister|minister|executive|commission', '\U0001F451'),
 (r'state|centre|union|federal|territor|boundar|schedule', '\U0001F5FA️'),
 (r'challeng|problem|criticism|weakness|fail|issue|concern|limitation|gap|drawback|loophole|threat', '⚠️'),
 (r'reform|way forward|suggest|recommend|solution|improve|measure|steps? to|strengthen', '\U0001F527'),
 (r'pyq|previous|asked|trend|exam|prelims|mains', '\U0001F3AF'),
 (r'minorit|women|child|tribal|scheduled|backward|disab|weaker|vulnerable|sc\b|st\b|obc', '\U0001F9D1‍\U0001F91D‍\U0001F9D1'),
 (r'educat|school|culture|religio|secular|conversion|waqf', '\U0001F4DA'),
 (r'international|global|treaty|un\b|udhr|convention|world|foreign', '\U0001F310'),
 (r'recent|current|2024|2025|2026|latest|new\b', '\U0001F195'),
 (r'meaning|definition|concept|idea|principle|feature|nature|significance|importance|purpose|objective|aim', '\U0001F4A1'),
]
PICC = [(re.compile(p, re.I), e) for p, e in PIC]
def pic(text):
    plain = re.sub(r'<[^>]+>', '', text)
    for rx, e in PICC:
        if rx.search(plain): return e
    return ''
KEYRX = re.compile(r'\d|\bArt(?:icle)?\b|\bAct\b|\bSection\b|\bSchedule\b|\bPart\b', re.I)
def _key(m):
    inner = m.group(1)
    plain = re.sub(r'<[^>]+>', '', inner)
    if len(plain) <= 70 and KEYRX.search(plain) and not re.match(r'\s*\d+\.\s', plain) and 'class="k"' not in inner:
        return '<b><span class="k">%s</span></b>' % inner
    return m.group(0)
def decorate(html):
    # key facts (numbers, articles, acts) in bold -> marker highlight
    html = re.sub(r'<b>((?:(?!</b>).)*)</b>', _key, html, flags=re.S)
    # pictograms on section headings, tree labels, table row labels
    def sub_(m):
        e = pic(m.group(3));  return '%s%s%s</div>' % (m.group(1), ('<i class="pic">%s</i>' % e) if e else '', m.group(3)) if False else m.group(0)
    def addpic(rx, grp_open=1, grp_txt=2):
        def f(m):
            e = pic(m.group(grp_txt))
            return m.group(0) if not e else m.group(grp_open) + '<i class="pic">%s</i>' % e + m.group(grp_txt) + m.group(grp_txt + 1)
        return f
    html = re.sub(r'(<div class="sub[^"]*">)((?:(?!</div>).)*)(</div>)', addpic(None), html, flags=re.S)
    html = re.sub(r'(<div class="lab"[^>]*>)((?:(?!</div>).)*)(</div>)', addpic(None), html, flags=re.S)
    html = re.sub(r'(<tr><td>)((?:(?!</td>).)*)(</td>)', addpic(None), html, flags=re.S)
    return html
