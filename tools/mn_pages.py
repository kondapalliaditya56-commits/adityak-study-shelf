"""Build <prefix>-mnemonics.html (Study Shelf mnemonic page + recall drill) and a large-type wall-sheet PDF per notebook.
Usage: python3 tools/mn_collect.py <nb> ; python3 tools/mn_pages.py <nb>   (nb = gov | pg2 | ir). Idempotent."""
import sys, os, re, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ca_integrate as ci
ROOT = ci.ROOT
nb = sys.argv[1]
TITLE = {'gov': 'Governance', 'pg2': 'Polity (GS-2)', 'ir': 'International Relations'}[nb]
PDFN = {'gov': 'Governance-Mnemonic-Sheet.pdf', 'pg2': 'Polity-GS2-Mnemonic-Sheet.pdf', 'ir': 'IR-Mnemonic-Sheet.pdf'}[nb]
nbid, base, home, search, tplf, nbt = ci.NB[nb]
G = json.load(open('/tmp/mn_%s.json' % nb))
e = ci.e
strip = lambda s: html.unescape(re.sub(r'<[^>]+>', '', s)).strip()
def card(it, col):
    w = it['w']; lab = 'Mnemonic &middot; ' + e(it['toc']) + (' &middot; own mnemonic' if it['own'] else '')
    if re.fullmatch(r'[A-Za-z][A-Za-z \-]*', w):
        tiles = '<div class="tiles">%s</div>' % ''.join('<span class="tile">%s</span>' % c for c in w if c.isalpha())
    else:
        tiles = '<div class="mhook"><b>%s</b></div>' % e(w)
    return '<div class="mnem mword"><div class="mlbl">%s</div>%s<div class="mhook">%s</div></div>' % (lab, tiles, it['h'].replace(' <i>(own mnemonic)</i>', ''))
body = []; secs = []; cards = []; n = 0
for gi, g in enumerate(G):
    sid = 'g%d' % gi
    body.append('<h2 id="%s">%s<a class="anchor" href="#%s" aria-label="Link to this section">#</a></h2>' % (sid, e(g['label'] + (' · ' + g['desc'] if g['desc'] else '')), sid))
    secs.append((sid, g['label']))
    for it in g['items']:
        body.append(card(it, g['col'])); n += 1
        cards.append({'q': 'What does %s stand for? (%s)' % (it['w'], it['toc']), 'a': strip(it['h'])})
fn = '%s-mnemonics.html' % nb
secs.append(('recall', 'Recall drill'))
page = ci.build_page(tplf, nbid, nbt, 901, '%s: mnemonics' % TITLE, 'Mnemonics · %s' % TITLE,
    '%d mnemonics from the handwritten notes, grouped by topic. Teacher\'s and handout mnemonics are kept as given; ones marked own were added where the material had none. Use the recall drill at the end, and the large-type PDF sheet for the wall.' % n,
    secs, ''.join(body), cards, home, search, 'Mnemonics collected from the handwritten notes of this notebook. Keep private.')
open(fn, 'w', encoding='utf-8').write(page)
# home card
hp = open(home, encoding='utf-8').read()
hp = re.sub(r'<!--mn-card-->.*?<!--/mn-card-->', '', hp, flags=re.S)
cd = ('<!--mn-card--><a class="hwcard" href="%s" style="display:flex;align-items:center;gap:12px;margin:10px 0 4px;padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--surface);text-decoration:none;color:inherit;font-family:var(--sans)">'
      '<span style="font-size:24px" aria-hidden="true">&#129504;</span><span style="flex:1"><b style="display:block;font-size:16px">Mnemonics and recall drill</b><small style="color:var(--muted)">%d mnemonics in one place</small></span><span style="font-weight:700;color:var(--accent)">Open &rsaquo;</span></a><!--/mn-card-->') % (fn, n)
hp = hp.replace('<p class="prog">', cd + '<p class="prog">', 1) if '<p class="prog">' in hp else hp.replace('</h1>', '</h1>' + cd, 1)
open(home, 'w', encoding='utf-8').write(hp)
# sw.js
sw = open('sw.js', encoding='utf-8').read()
m = re.search(r'const FILES=(\[.*?\]);', sw, re.S); files = json.loads(m.group(1))
if fn not in files: files.append(fn)
open('sw.js', 'w', encoding='utf-8').write(sw.replace(m.group(0), 'const FILES=' + json.dumps(sorted(files)) + ';', 1))
# PDF wall sheet
from weasyprint import HTML
F = 'file://' + os.path.join(ROOT, 'src-gov', 'handnotes', 'fonts')
CSS = ('@font-face{font-family:KB;src:url(%(F)s/kalam-latin-700-normal.woff);font-weight:bold}@font-face{font-family:KL;src:url(%(F)s/kalam-latin-400-normal.woff)}@font-face{font-family:CB;src:url(%(F)s/caveat-brush-latin-400-normal.woff)}'
       '@page{size:A4;margin:11mm 12mm 14mm 12mm;@bottom-center{content:"%(T)s mnemonic sheet · " counter(page);font:10pt KL;color:#666}}b{font-family:KB;color:#000}body{font-family:KL;font-size:13.5pt;color:#222;line-height:1.35}'
       '.cover{height:255mm;text-align:center;padding-top:60mm;page-break-after:always}.cover h1{font:56pt CB;margin:0;color:#00796b}.cover p{font-size:16pt;margin:8mm 20mm}'
       '.mod{page-break-before:always;font:28pt CB;padding:3mm 5mm;color:#fff;border-radius:6px;margin-bottom:5mm}.mod small{display:block;font:13pt KL}'
       '.card{border:2.5px solid;border-radius:10px;padding:3mm 5mm;margin:0 0 4.5mm;page-break-inside:avoid}.w{font:34pt CB;line-height:1.05}.tag{font:10pt KL;color:#777;float:right;text-align:right;max-width:55mm}.own{font-size:10pt;color:#8d6e00}'
       '.drill h2{font:26pt CB;margin:0 0 3mm}.dr{border-bottom:1.5px dashed #bbb;padding:2.2mm 0;page-break-inside:avoid}.dr b{font:22pt CB;display:inline-block;width:62mm}.dr span{font-size:11pt;color:#666}') % {'F': F, 'T': TITLE}
h = ['<html><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS,
     '<div class="cover"><h1>%s<br>Mnemonic Sheet</h1><p>%d mnemonics from the handwritten notes, in large type for the wall.</p><p>Teacher\'s and handout mnemonics are kept exactly as given. Mnemonics marked <b>own</b> were added where the material had none.</p><p>Last pages: cover-and-recall drills.</p></div>' % (TITLE, n)]
dr = []
for g in G:
    h.append('<div class="mod" style="background:%s">%s<small>%s</small></div>' % (g['col'], g['label'], g['desc']))
    for it in g['items']:
        h.append('<div class="card" style="border-color:%s"><span class="tag">%s%s</span><div class="w" style="color:%s">%s</div><div>%s</div></div>' % (g['col'], e(it['toc']), '<br><span class="own">own mnemonic</span>' if it['own'] else '', g['col'], it['w'], it['h'].replace(' <i>(own mnemonic)</i>', '')))
        dr.append((it['w'], it['toc'], g['col']))
h.append('<div class="drill" style="page-break-before:always"><h2>Cover-and-recall drill</h2><p>Hide the right side. Say what each letter or number stands for, then check against the cards.</p>')
for k, (w, toc, col) in enumerate(dr):
    if k and k % 14 == 0: h.append('<div style="page-break-before:always"></div>')
    h.append('<div class="dr"><b style="color:%s">%s</b><span>%s</span></div>' % (col, w, e(toc)))
h.append('</div></body></html>')
HTML(string=''.join(h)).write_pdf(PDFN)
print(nb, n, 'mnemonics ->', fn, PDFN)
