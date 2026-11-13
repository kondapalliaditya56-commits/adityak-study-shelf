# -*- coding: utf-8 -*-
"""Class-note additions as textbook material, from the same cn/ DSL source as the handwritten notes.
python3 class_addendum.py html   -> writes <shelf>/pol-chNN.html 'From the class' section (idempotent)
python3 class_addendum.py pdf OUTDIR -> writes OUTDIR/cnNN.html + cnNN.pdf (A4, margin panel) for splicing into the textbook PDF"""
import sys, os, re, html as H
HERE = os.path.dirname(os.path.abspath(__file__)); sys.argv_saved = sys.argv[:]
import buildfound as bf
from dsl import r_book
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CSS_SITE = """.bk-cn{margin:28px 0 8px;border-top:3px solid var(--acc);padding-top:6px}.bk-cn>h2{font-size:1.35em}
.bk-cn .cn-sub{color:var(--muted);font:600 13px var(--sans);margin:2px 0 10px}.bk-cn h3{margin:18px 0 6px;font-size:1.05em;color:var(--acc)}
.bk-cn ul{padding-left:1.2em;margin:6px 0}.bk-cn li{margin:3px 0}
.bk-cn .cn-call{border-left:4px solid var(--saf);background:var(--saf-soft);border-radius:0 8px 8px 0;padding:8px 12px;margin:10px 0}
.bk-cn .cn-call.ye{border-color:#B8860B;background:var(--hl)}.bk-cn .cn-call.bl{border-color:var(--blue);background:var(--blue-soft)}
.bk-cn .cn-call.gr{border-color:var(--good);background:var(--good-soft)}.bk-cn .cn-call.ca{border-color:var(--c7);background:var(--surface2)}
.bk-cn .cn-call .tag{display:block;font:700 11px var(--sans);letter-spacing:.06em;text-transform:uppercase;margin-bottom:3px}
.bk-cn table{border-collapse:collapse;width:100%;font-size:.92em}.bk-cn th,.bk-cn td{border:1px solid var(--line);padding:5px 8px;text-align:left;vertical-align:top}.bk-cn th{background:var(--acc-soft)}"""
KIND = {'pk': ('Teacher stressed', ''), 'ye': ('Trap / check', 'ye'), 'bl': ('Definition', 'bl'), 'gr': ('Answer frame', 'gr'), 'ca': ('In the news', 'ca')}
def items_html(nodes):
    out = []; ul = []
    def flush():
        nonlocal ul
        if ul: out.append('<ul>' + ''.join('<li>%s</li>' % x for x in ul) + '</ul>'); ul = []
    for n in nodes:
        if n[0] in ('sw', 'stl'): continue
        if n[0] == 'bx': 
            flush(); lab, cls = KIND.get(n[1], ('Note', ''))
            out.append('<div class="cn-call %s"><span class="tag">%s</span>%s</div>' % (cls, lab, n[2])); continue
        if n[0] == 'mn':
            flush(); out.append('<div class="cn-call"><span class="tag">Memory aid · %s</span>%s</div>' % (n[1], n[2])); continue
        for it in r_book(n):
            if isinstance(it, str): ul.append(it)
            elif 'h' in it:
                flush(); t = re.sub(r'<[^>]+>', '', it['h'])
                t = re.sub(r'^CLASS\s*·\s*', '', t)
                out.append('<h3>%s</h3>' % t if it.get('sec') else '<p><b>%s</b></p>' % t)
            elif 'call' in it:
                flush(); c = it['call']; out.append('<div class="cn-call"><span class="tag">%s</span>%s</div>' % (c['tag'], ' '.join(c['body'])))
            elif 'ca' in it:
                flush(); out.append('<div class="cn-call ca"><span class="tag">In the news</span>%s</div>' % it['ca'])
            elif 'tbl' in it:
                flush(); t = it['tbl']
                out.append('<div class="tablewrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
                    ''.join('<th>%s</th>' % h for h in t['head']), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in t['rows'])))
    flush(); return ''.join(out)
def recall_html(ch):
    q = ch.get('cn_recall') or []
    if not q: return ''
    return '<h3>Quick recall from the class</h3><div class="tablewrap"><table><thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>' + ''.join('<tr><td>%s</td><td>%s</td></tr>' % (x, y) for x, y in q) + '</tbody></table></div>'
def chapter_fragment(ch):
    blocks = ch.get('cn_blocks') or []
    if not blocks: return None
    body = ''.join(items_html(b['nodes']) for b in blocks) + recall_html(ch)
    return ('<!--cn--><section id="class-additions" class="bk-cn"><h2>From the class<a class="anchor" href="#class-additions">#</a></h2>'
            '<div class="cn-sub">Taught in class, not in the handout: latest Supreme Court cases, comparisons with other constitutions, the teacher\'s examples and answer frames. Where class and handout differ, the box says so.</div>'
            + body + '</section><!--/cn-->')
def inject_site():
    chs = bf.load('polity'); n = 0
    for ch in chs:
        fr = chapter_fragment(ch)
        p = os.path.join(ROOT, 'pol-ch%02d.html' % ch['id'])
        if not fr or not os.path.exists(p): continue
        s = open(p, encoding='utf8').read()
        s = re.sub(r'<!--cn-->.*?<!--/cn-->', '', s, flags=re.S)
        if 'id="cncss"' not in s: s = s.replace('</head>', '<style id="cncss">' + CSS_SITE + '</style></head>', 1)
        else: s = re.sub(r'<style id="cncss">.*?</style>', '<style id="cncss">' + CSS_SITE.replace('\\', '\\\\') + '</style>', s, flags=re.S)
        k = s.find('<section id="recall">')
        assert k > 0, p
        s = s[:k] + fr + s[k:]
        open(p, 'w', encoding='utf8').write(s); n += 1
    print('site chapters updated:', n)
PDF_CSS = """@page{size:A4;margin:17mm 66mm 16mm 20mm;
 @top-left{content:string(ct);font:600 7.5pt 'Source Sans 3',sans-serif;letter-spacing:.14em;color:#0E6B5C;text-transform:uppercase;margin-left:0}
 @top-right{content:'POLITY · CLASS ADDITIONS';font:600 7.5pt 'Source Sans 3',sans-serif;letter-spacing:.14em;color:#B85C00;margin-right:-50mm}
 @bottom-center{content:var(--pg) counter(page,lower-alpha);font:8.5pt 'Source Sans 3',sans-serif;color:#444}}
div.panel{position:fixed;top:-17mm;bottom:-16mm;right:-62mm;width:56mm;background:#eef5f3;border-left:.3mm solid #cfe3de;font:600 7pt 'Source Sans 3',sans-serif;letter-spacing:.16em;color:#0E6B5C;text-align:center;padding-top:14mm}
body{font:10pt/1.5 Literata,Georgia,serif;color:#1F2A2A}
h1{font:700 15pt Literata,Georgia,serif;margin:0 0 2mm;string-set:ct content()} .cn-sub{font:italic 9pt Georgia,serif;color:#5D6A68;margin:0 0 4mm}
h3{font:700 8.5pt 'Source Sans 3',sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#0E6B5C;border-bottom:1px solid #0E6B5C;margin:5mm 0 2mm;break-after:avoid}
ul{margin:1mm 0 2mm;padding-left:4.5mm}li{margin:.8mm 0}p{margin:1mm 0}
.cn-call{border-left:1.2mm solid #B85C00;background:#FFF0DB;padding:1.6mm 2.5mm;margin:2.5mm 0;break-inside:avoid}.cn-call.ye{border-color:#B8860B;background:#FFE9A6}.cn-call.bl{border-color:#1F5FA8;background:#E3EEFA}.cn-call.gr{border-color:#2E7D32;background:#E3F3E4}.cn-call.ca{border-color:#37607A;background:#F3F1EA}
.cn-call .tag{display:block;font:700 6.8pt 'Source Sans 3',sans-serif;letter-spacing:.07em;text-transform:uppercase;margin-bottom:.6mm}
table{border-collapse:collapse;width:100%;font-size:8.8pt;margin:2mm 0;break-inside:auto}tr{break-inside:avoid}th,td{border:.2mm solid #DAD6C8;padding:1mm 1.6mm;text-align:left;vertical-align:top}th{background:#DDF0EA}"""
def build_pdf(outdir, ends):
    from weasyprint import HTML
    os.makedirs(outdir, exist_ok=True)
    for ch in bf.load('polity'):
        fr = chapter_fragment(ch)
        if not fr: continue
        body = ''.join(items_html(b['nodes']) for b in ch['cn_blocks']) + recall_html(ch)
        pgn = ends.get(ch['id'], '')
        doc = ('<html><head><meta charset="utf-8"><style>%s :root{--pg:"%s"}</style></head><body><div class="panel">MY NOTES</div><h1>Chapter %d · %s: from the class</h1>'
               '<div class="cn-sub">Taught in class, not in the handout: latest Supreme Court cases, comparisons with other constitutions, the teacher\'s examples and answer frames. Where class and handout differ, the box says so.</div>%s</body></html>'
               % (PDF_CSS, pgn, ch['id'], H.escape(ch['title'].title()), body))
        open(os.path.join(outdir, 'cn%02d.html' % ch['id']), 'w').write(doc)
        HTML(string=doc).write_pdf(os.path.join(outdir, 'cn%02d.pdf' % ch['id']))
if __name__ == '__main__':
    a = sys.argv_saved
    if a[1] == 'html': inject_site()
    else:
        import json; build_pdf(a[2], {int(k): v for k, v in json.load(open(a[3])).items()} if len(a) > 3 else {})
