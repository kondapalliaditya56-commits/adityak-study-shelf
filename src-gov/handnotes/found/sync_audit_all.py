# -*- coding: utf-8 -*-
"""Cross-format sync audit for ANY subject: Study Shelf chapter pages vs textbook PDF vs handwritten PDF.
usage: python3 sync_audit_all.py [subject ...]   (default: polity economy geography modern-india)
For each Shelf chapter page it extracts the fact tokens (numbers, Articles/Sections, acronyms, case names) and reports how many appear in the textbook
PDF and in the handwritten PDF (searched across the whole PDF). Textbook vs Shelf should be ~100%; handwritten may be lower by design (condensed),
so the report lists the chapters with the lowest coverage and the missing facts to check. For Polity class additions also run sync_audit.py."""
import sys, os, re, html, subprocess, glob
sys.argv_saved = sys.argv[:]
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
import check
CFG = {'polity': ('pol-ch', 'Polity-Book-Personal-Study-Edition.pdf', 'Polity-Foundation-Handwritten-Revision-Notes.pdf'),
       'economy': ('eco-ch', 'Economy-Textbook-Personal-Study-Edition.pdf', 'Economy-Handwritten-Revision-Notes.pdf'),
       'geography': ('geo-ch', 'Geography-Textbook-Personal-Study-Edition.pdf', 'Geography-Handwritten-Revision-Notes.pdf'),
       'modern-india': ('ch', 'Modern-India-Textbook-Personal-Study-Edition.pdf', 'Modern-India-Handwritten-Revision-Notes.pdf')}
def ptxt(p):
    t = check.norm(subprocess.run(['pdftotext', os.path.join(ROOT, p), '-'], capture_output=True, text=True).stdout)
    t = re.sub(r'(?<=\d),(?=\d)', '', t)
    t = re.sub(r'\barticles?\.?\s*', 'art ', t); t = re.sub(r'\bart\.\s*', 'art ', t); t = re.sub(r'\bsections?\.?\s*|\bsec\.\s*', 'sec ', t)
    return t
def present(f, T):
    return f in T or f.replace(' ', '') in T.replace(' ', '')
def run(subj):
    pre, tbp, hwp = CFG[subj]
    pages = sorted(glob.glob(os.path.join(ROOT, pre + '[0-9][0-9].html')))
    if not pages: print(subj, 'no Shelf pages found for prefix', pre); return
    TB, HW = ptxt(tbp), ptxt(hwp); rows = []
    for p in pages:
        s = open(p, encoding='utf8').read()
        s = re.sub(r'<(style|script)[^>]*>.*?</\1>', ' ', s, flags=re.S)
        s = re.sub(r'<!--ca:.*?-->.*?</aside>', ' ', s, flags=re.S)
        F = check.facts(check.plain(s)); 
        if not F: continue
        mt = [f for f in F if not present(f, TB)]; mh = [f for f in F if not present(f, HW)]
        rows.append((os.path.basename(p), len(F), 100 - 100 * len(mt) // len(F), 100 - 100 * len(mh) // len(F), mt[:6], mh[:6]))
    print('== %s: %d chapters. Textbook-vs-Shelf min %d%%, avg %d%%. Handwritten-vs-Shelf min %d%%, avg %d%%' % (subj, len(rows),
        min(r[2] for r in rows), sum(r[2] for r in rows) // len(rows), min(r[3] for r in rows), sum(r[3] for r in rows) // len(rows)))
    for r in sorted(rows, key=lambda r: r[2])[:4]: print('  textbook low:', r[0], '%d%%' % r[2], 'missing e.g.', r[4])
    for r in sorted(rows, key=lambda r: r[3])[:4]: print('  handwritten low:', r[0], '%d%%' % r[3], 'missing e.g.', r[5])
if __name__ == '__main__':
    for s in (sys.argv_saved[1:] or CFG): run(s)
