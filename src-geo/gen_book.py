# -*- coding: utf-8 -*-
"""Geography textbook data in the Economy-book pattern. Chapter notes come from the Study Shelf chapter (the handout in order); the exam lens, plain-words layer, terms, memory visuals, recall, traps and quiz are authored per chapter in chap/chN.py."""
import re, sys, os, json, html as H, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'src-gov', 'handnotes', 'found', 'geography')); sys.path.insert(0, HERE)
import cover
def clean(s): return re.sub(r'\s+', ' ', s).strip()
def _main(n):
    t = open(os.path.join(ROOT, 'geo-ch%02d.html' % n), encoding='utf8').read()
    m = t[t.index('<main'):t.index('<nav class="pager"')]
    return re.sub(r'^<main[^>]*>', '', m)
def fig_html(h, cap):
    m = re.search(r'class="([^"]*)" style="--w:([\d.]+)px"><img[^>]*src="([^"]+)"', h)
    if not m: return ''
    cls, w, src = m.group(1), float(m.group(2)), m.group(3)
    k = 'sq' if (w < 200 and 'tbl' not in cls) else 'wide'
    return '<figure class="%s"><img src="%s"><figcaption><b>Handout figure.</b> %s</figcaption></figure>' % (k, src, H.escape(cap))
def nest(items):
    out = []; cur = -1; open_li = False
    for d, h in items:
        h = clean(h)
        if cur < 0: out.append('<ul class="b">'); cur = 0; d = 0
        else: d = min(d, cur + 1)
        while cur > d:
            out.append('</li></ul>'); cur -= 1
        if d > cur:
            out.append('<ul class="sub">'); cur = d
        elif open_li: out.append('</li>')
        out.append('<li>%s' % h); open_li = True
    while cur >= 0: out.append('</li></ul>' if cur else '</li></ul>'); cur -= 1
    return ''.join(out)
def convert(bl, skip_h=()):
    """handout blocks -> book notes items (bullets nested, headings, tables, figures in place)"""
    out = []; run = []; hd = ''
    def flush():
        nonlocal run
        if run: out.append({'raw': nest(run)}); run = []
    for k, d, t, h in bl:
        if k == 'h':
            flush(); hd = re.sub(r'^\d+\s*·\s*', '', t).strip(': ')
            if clean(t) in skip_h: continue
            out.append({'h': (hd.title() if hd.isupper() else hd)})
        elif k == 'li':
            if not clean(t): continue
            run.append((d, h))
        elif k == 'p':
            flush()
            if not clean(t) or t.startswith('Understand it first'): continue
            out.append({'raw': '<p class="np">%s</p>' % clean(h)})
        elif k == 'tbl': flush(); out.append({'raw': '<div class="tblx">%s</div>' % h})
        elif k == 'fig':
            flush(); f = fig_html(h, (hd.title() if hd.isupper() else hd)); 
            if f: out.append({'raw': f})
    flush(); return out
GCSS = ('<style>.gsec{font:700 13.2pt Lora;color:#1F4E5F;border-bottom:1.6pt solid #C9A24D;margin:6mm 0 2.4mm;padding-bottom:.8mm;break-after:avoid;letter-spacing:.02em}'
        '.gsec b{color:#B07F1E;margin-right:2mm}.gsec .py{font:700 7pt Inter;background:#F4E7C5;color:#7a5a12;border-radius:2mm;padding:.4mm 2mm;margin-left:2mm;vertical-align:middle}'
        '.und{background:#E4F3F1;border-left:2.2pt solid #1F7A74;border-radius:1mm;padding:2mm 3.2mm;margin:1.6mm 0 2.4mm;font:9.4pt/1.45 Lora;break-inside:avoid}'
        '.und span,.hk span{font:700 7pt Inter;letter-spacing:.14em;text-transform:uppercase;color:#1F7A74;display:block;margin-bottom:.6mm}'
        '.hk{background:#EFE9F6;border-left:2.2pt solid #7A55A8;border-radius:1mm;padding:1.8mm 3.2mm;margin:2.4mm 0 1mm;font:9.4pt/1.4 Lora;break-inside:avoid}.hk span{color:#7A55A8}'
        '.np{margin:1mm 0}.tblx img{max-width:100%}.tblx table{font:8.6pt Inter;width:100%;border-collapse:collapse}.tblx td,.tblx th{border:.4pt solid #aaa;padding:.6mm 1.2mm}'
        '.tblx{overflow:hidden}</style>')
def build_chapter(n, spec):
    """spec = chap/chN module"""
    m = _main(n); bl = cover.blocks(m); notes = [{'raw': GCSS}]
    SECS = spec.sections(bl); DROP = spec.drop(bl)
    for k, (title, rngs, und, hook) in enumerate(SECS):
        pyq = spec.SEC_PYQ.get(k, '')
        notes.append({'raw': '<h3 class="gsec"><b>%d</b>%s%s</h3>' % (k + 1, H.escape(title), ('<span class="py">PYQ %s</span>' % pyq) if pyq else '')})
        if und: notes.append({'raw': '<div class="und"><span>Understand it first</span>%s</div>' % und})
        seg = [x for a, b in rngs for i, x in enumerate(bl) if a <= i < b and i not in DROP]
        notes += convert(seg, skip_h=spec.SKIP_H)
        notes += spec.EXTRA.get(k, [])
        if hook: notes.append({'raw': '<div class="hk"><span>Remember</span>%s</div>' % hook})
    ch = dict(id=n, title=spec.TITLE, pages=spec.PAGES, priority=spec.PRIORITY, pyqs=spec.PYQS, prelims_pyqs=spec.PRELIMS,
              lens=spec.LENS, simple=spec.SIMPLE, terms=spec.TERMS, remember=spec.REMEMBER, notes=notes, pyq=spec.PYQBLOCK,
              recall=spec.RECALL, traps=spec.TRAPS, quiz=spec.QUIZ, visuals=spec.VISUALS)
    return ch
