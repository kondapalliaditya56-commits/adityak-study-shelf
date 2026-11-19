#!/usr/bin/env python3
"""Modern India textbook (Personal Study Edition) from the published chapter pages.
python3 build_textbook.py REPO OUT.pdf"""
import sys, os, re, json, html, subprocess, io
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

REPO, OUT = sys.argv[1], sys.argv[2]
TMP = '/tmp/tb'
SITE = '/tmp/printsite'
os.makedirs(TMP, exist_ok=True)
lib = json.load(open(os.path.join(REPO, 'library.json')))[0]
chs = [c for c in lib['chapters'] if c['n'] >= 1 and not c.get('pending')]
PARTS = [(1, 'Part 1 · Sources and the eighteenth century'), (8, 'Part 2 · British conquest and rule'), (15, 'Part 3 · Company rule: ideology, economy, administration, society'),
         (20, 'Part 4 · Resistance and 1857'), (23, 'Part 5 · Rise of nationalism (1861–1915)'), (33, 'Part 6 · Home Rule to the Gandhian era'), (38, 'Part 7 · Mass movements to Independence')]
home = open(os.path.join(REPO, 'home.html'), encoding='utf-8').read()
m = re.findall(r'<section class="part"><h2>([^<]*)</h2><p class="gdesc">([^<]*)', home)
if m:
    PARTS = []
    for h2, d in m:
        a = re.search(r'(\d+)', d)
        PARTS.append((int(a.group(1)), html.unescape(h2)))
PARTS.sort()
# chapter 32 sits in Part 5 ("23-32"); use the ranges from home.html


def part_of(n):
    cur = PARTS[0][1]
    for s, t in PARTS:
        if n >= s:
            cur = t
    return cur


def meta(n):
    p = open(os.path.join(REPO, 'ch%02d.html' % n), encoding='utf-8').read()
    pri = 'M'
    if 'priH' in p[:20000]:
        pri = 'H'
    elif 'priL' in p[:20000]:
        pri = 'L'
    i = p.find('class="pills"')
    pills = re.findall(r'<span class="pill[^"]*">(.*?)</span>', p[i:i + 1500])
    pyq = ''
    for x in pills:
        t = html.unescape(re.sub('<[^>]+>', '', x))
        if t.startswith('Prelims PYQs'):
            pyq = t.replace('Prelims PYQs:', '').strip()
    return pri, pyq


CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter','Source Sans 3',Arial,sans-serif;color:#1F4E5F}
.cover{height:297mm;width:210mm;padding:44mm 26mm 20mm 34mm;background:linear-gradient(160deg,#EAF4F1 0%,#FFF8E8 55%,#FDF1E3 100%);position:relative;overflow:hidden}
.cover .c1{position:absolute;right:-30mm;top:-20mm;width:110mm;height:110mm;border-radius:50%;background:#DCEBE7;opacity:.7}
.cover .c2{position:absolute;left:-25mm;bottom:-25mm;width:90mm;height:90mm;border-radius:50%;background:#F7E6C4;opacity:.7}
.cover h1{font-family:'Lora',Georgia,serif;font-size:40pt;line-height:1.1;margin:0 0 6mm;position:relative}
.cover .sub{font-size:13pt;position:relative;max-width:130mm}.cover .gold{width:40mm;height:1.2mm;background:#C9A24D;margin:8mm 0;position:relative}
.cover .foot{position:absolute;left:34mm;bottom:22mm;font-size:10pt;color:#B07F1E;font-weight:600;max-width:140mm;line-height:1.5}
.toc{padding:20mm 26mm 14mm 28mm}.toc h2{font-family:'Lora',Georgia,serif;font-size:20pt;margin:0 0 5mm}
.toc .pt{font-weight:700;font-size:9.5pt;background:#EAF4F1;padding:1.2mm 3mm;margin:4mm 0 1.5mm;border-left:1.2mm solid #C9A24D}
.toc .r{display:flex;font-size:9pt;line-height:1.55}.toc .r .t{flex:1;overflow:hidden}.toc .r .d{border-bottom:1px dotted #9bb;flex:0 0 8mm;margin:0 2mm 1.4mm}.toc .r .p{flex:none;width:10mm;text-align:right}
.toc .r .k{flex:none;width:6mm;font-weight:700;color:#B07F1E}
.idx{padding:20mm 20mm 14mm 28mm}.idx h2{font-family:'Lora',Georgia,serif;font-size:20pt;margin:0 0 3mm}.idx p{font-size:9pt;margin:0 0 4mm}
.idx table{width:100%;border-collapse:collapse;font-size:8.2pt}.idx th{background:#DCEBE7;text-align:left;padding:1.2mm 2mm}.idx td{padding:1mm 2mm;border-bottom:1px solid #e3ece9;vertical-align:top}
.H{color:#B3261E;font-weight:700}.M{color:#B07F1E;font-weight:700}.L{color:#5C7A1F;font-weight:700}
.how{padding:30mm 30mm 20mm 34mm;font-size:10.5pt;line-height:1.55}.how h2{font-family:'Lora',Georgia,serif;font-size:20pt}
"""


def front(pages_map=None):
    rows = ''
    cur = None
    for c in chs:
        pt = part_of(c['n'])
        if pt != cur:
            cur = pt
            rows += '<div class="pt">%s</div>' % html.escape(pt)
        pg = pages_map.get(c['n'], 0) if pages_map else 0
        rows += '<div class="r"><span class="k">%d</span><span class="t">%s</span><span class="d"></span><span class="p">%s</span></div>' % (
            c['n'], html.escape(c['title']), pg or '')
    cover = ('<div class="cover"><div class="c1"></div><div class="c2"></div><div style="font-size:11pt;letter-spacing:.2em;color:#B07F1E;font-weight:700;position:relative">UPSC CSE 2027 · GS FOUNDATION</div>'
             '<h1>Modern Indian History</h1><div class="gold"></div><div class="sub">Eighteenth-century India · British conquest · Revolt of 1857 · Reforms · Moderates and Extremists · Gandhian era · Constitutional developments · Independence</div>'
             '<div class="foot">Personal Study Edition<br>Built from the Sarrthi IAS handout and Himanshu Khatri class slides. Copyright belongs to the teacher and institute; keep this private.</div></div>')
    how = ('<div class="how" style="break-before:page"><h2>How to use this book</h2><p>Every chapter opens with <b>Exam lens</b>, the story in one go and plain-language key terms, then the full notes in handout order with the teacher\'s board points, handout alerts, PYQ tags, mnemonics and a timeline. Each chapter ends with a recall sheet. The practice quizzes, flashcards and question banks live on the Study Shelf.</p>'
           '<p><b>Priority tags:</b> <span class="H">H</span> = two or more PYQs map to the chapter; <span class="M">M</span> = one PYQ or a partial fit; <span class="L">L</span> = none quoted in the material.</p>'
           '<p>The wide blank column on the right of every page, and the binding margin on the left, are kept free for your own current affairs, data and value additions.</p>'
           '<p>Reign-year codes (for example Babur 26-30) are kept exactly as the teacher writes them.</p></div>')
    toc = '<div class="toc" style="break-before:page"><h2>Contents</h2>%s</div>' % rows
    return '<html><head><meta charset="utf-8"><style>%s</style></head><body>%s%s%s</body></html>' % (CSS, cover, how, toc)


def back():
    rows = ''
    info = [(c['n'], c['title']) + meta(c['n']) for c in chs]
    for n, t, pri, pyq in info:
        rows += '<tr><td>%d</td><td>%s</td><td class="%s">%s</td><td>%s</td></tr>' % (n, html.escape(t), pri, pri, html.escape(pyq or 'none quoted in the material'))
    cnt = {k: sum(1 for i in info if i[2] == k) for k in 'HML'}
    return ('<html><head><meta charset="utf-8"><style>%s</style></head><body><div class="idx"><h2>Priority and PYQ index</h2>'
            '<p>H = %d chapters · M = %d · L = %d. Prelims years as quoted in the handout and class slides; a number in brackets is the count in that year.</p>'
            '<table><tr><th>Ch</th><th>Chapter</th><th>Priority</th><th>Prelims PYQs</th></tr>%s</table></div></body></html>') % (CSS, cnt['H'], cnt['M'], cnt['L'], rows)


def pw_print(jobs):
    """jobs: list of (url, outpdf, kind) ; kind chapter|plain"""
    js = r"""
const {chromium}=require('playwright');
(async()=>{const jobs=JSON.parse(process.argv[2]);const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:900,height:1200}});
for(const j of jobs){const pg=await ctx.newPage();await pg.goto(j.url,{waitUntil:'load'});await pg.waitForTimeout(500);
 await pg.emulateMedia({media:'print'});
 if(j.kind==='chapter'){await pg.addStyleTag({content:`@page{size:A4;margin:16mm 14mm 16mm 24mm}
header.bar,.dock,.rbar,.sheet,.toast,button,aside.sidetoc,nav.pager,footer,#practice,section:has(> #practice),.banklink,.themebtn,#lightbox,details.glance,.cabox .btn{display:none!important}
  .layout{display:block!important} main.page{max-width:none!important;width:120mm!important;margin:0!important;padding:0!important;overflow-wrap:anywhere}
  table{font-size:8.2pt} .bfig img{max-height:68mm;max-width:100%;object-fit:contain} img{max-width:100%} pre,code{white-space:pre-wrap}
  body{font-size:10pt;background:#fff!important} .chead{break-before:page}`});
  await pg.pdf({path:j.out,format:'A4',printBackground:true,preferCSSPageSize:true});}
 else {await pg.pdf({path:j.out,format:'A4',printBackground:true,preferCSSPageSize:true});}
 await pg.close();}
await b.close()})();
"""
    open('/tmp/tb/pw_jobs.js', 'w').write(js)
    subprocess.run(['node', '/tmp/tb/pw_jobs.js', json.dumps(jobs)], check=True)


def prep_site():
    import shutil
    from PIL import Image
    if os.path.exists(SITE): shutil.rmtree(SITE)
    os.makedirs(SITE + '/img')
    for f in os.listdir(REPO):
        if f.endswith('.html') or f.endswith('.json') or f.endswith('.css') or f.endswith('.js'):
            os.symlink(os.path.join(REPO, f), os.path.join(SITE, f))
    for f in os.listdir(REPO + '/img'):
        im = Image.open(os.path.join(REPO, 'img', f))
        if im.width > 820: im = im.resize((820, int(im.height * 820 / im.width)))
        im = im.convert('RGB')
        if f.endswith('.png'): im.save(os.path.join(SITE, 'img', f), 'PNG', optimize=True)
        else: im.save(os.path.join(SITE, 'img', f), 'JPEG', quality=58, optimize=True)


def main():
    prep_site()
    base = 'http://localhost:8766/printsite/'
    jobs = [(base + 'ch%02d.html' % c['n'], '%s/ch%02d.pdf' % (TMP, c['n'])) for c in chs]
    pw_print([{'url': u, 'out': o, 'kind': 'chapter'} for u, o in jobs])
    open(TMP + '/back.html', 'w').write(back())
    open(TMP + '/front0.html', 'w').write(front())
    pw_print([{'url': 'file://' + TMP + '/back.html', 'out': TMP + '/back.pdf', 'kind': 'plain'},
              {'url': 'file://' + TMP + '/front0.html', 'out': TMP + '/front0.pdf', 'kind': 'plain'}])
    nfront = len(PdfReader(TMP + '/front0.pdf').pages)
    counts = {c['n']: len(PdfReader('%s/ch%02d.pdf' % (TMP, c['n'])).pages) for c in chs}
    start = {}
    p = nfront + 1
    for c in chs:
        start[c['n']] = p
        p += counts[c['n']]
    open(TMP + '/front.html', 'w').write(front(start))
    pw_print([{'url': 'file://' + TMP + '/front.html', 'out': TMP + '/front.pdf', 'kind': 'plain'}])
    assert len(PdfReader(TMP + '/front.pdf').pages) == nfront
    w = PdfWriter()
    for f in [TMP + '/front.pdf'] + ['%s/ch%02d.pdf' % (TMP, c['n']) for c in chs] + [TMP + '/back.pdf']:
        for pg in PdfReader(f).pages:
            w.add_page(pg)
    # outline
    for c in chs:
        w.add_outline_item('%d  %s' % (c['n'], c['title']), start[c['n']] - 1)
    w.add_outline_item('Priority and PYQ index', p - 1)
    # stamp: notes column, footer, page number
    total = len(w.pages)
    for i, pg in enumerate(w.pages):
        if i == 0:
            continue
        is_ch = start[chs[0]['n']] - 1 <= i <= p - 2
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(210 * mm, 297 * mm))
        if is_ch:
            c.setStrokeColorRGB(.86, .92, .90)
            c.setLineWidth(.4)
            x0, x1 = 154 * mm, 199 * mm
            c.setFillColorRGB(.55, .68, .66)
            c.setFont('Helvetica-Bold', 6.5)
            c.drawString(x0 + 1 * mm, 289 * mm, 'MY NOTES')
            c.line(x0 - 3 * mm, 16 * mm, x0 - 3 * mm, 286 * mm)
            y = 280 * mm
            while y > 22 * mm:
                c.line(x0, y, x1, y)
                y -= 8 * mm
        c.setFont('Helvetica', 7.5)
        c.setFillColorRGB(.4, .45, .5)
        c.drawString(24 * mm, 9 * mm, 'Modern Indian History · Personal Study Edition')
        c.drawRightString(199 * mm, 9 * mm, str(i + 1))
        c.save()
        buf.seek(0)
        pg.merge_page(PdfReader(buf).pages[0])
    w.write(OUT)
    subprocess.run(['qpdf', '--recompress-flate', '--compression-level=9', '--object-streams=generate', OUT, OUT + '.tmp'])
    if os.path.exists(OUT + '.tmp'): os.replace(OUT + '.tmp', OUT)
    print('pages', total, 'front', nfront, 'size', os.path.getsize(OUT))


main()
