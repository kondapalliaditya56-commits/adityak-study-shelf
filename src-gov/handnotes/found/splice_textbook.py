# -*- coding: utf-8 -*-
"""Rebuild the Polity textbook PDF with class-note pages after each chapter, from the ORIGINAL textbook PDF kept in git history at
the commit given (default: the committed version before class additions: rev 'ef7425b:Polity-Book-Personal-Study-Edition.pdf').
usage: python3 splice_textbook.py ORIGINAL_PDF ADDENDA_DIR OUT_PDF   (ADDENDA_DIR holds cnNN.pdf; ends.json = {chapter: first-page-index-after-chapter})"""
import sys, os, glob, json
from pypdf import PdfReader, PdfWriter
orig, D, out = sys.argv[1:4]
ends = {int(k): v for k, v in json.load(open(os.path.join(D, 'ends_only.json'))).items()}
w = PdfWriter(clone_from=orig)
ids = sorted(int(os.path.basename(f)[2:4]) for f in glob.glob(D + '/cnpdf/cn*.pdf'))
n = {c: len(PdfReader(D + '/cnpdf/cn%02d.pdf' % c).pages) for c in ids}
for cid in reversed(ids):
    for k, pg in enumerate(PdfReader(D + '/cnpdf/cn%02d.pdf' % cid).pages): w.insert_page(pg, ends[cid] + k)
tot = 0; final = {}
for cid in ids: final[cid] = ends[cid] + tot; tot += n[cid]
root = w.add_outline_item('Class additions (from the class notes)', final[ids[0]])
for cid in ids: w.add_outline_item('Chapter %d: from the class' % cid, final[cid], parent=root)
w.add_metadata({'/Title': 'Polity: Personal Study Edition (with class additions)'})
w.write(out); print(len(w.pages))
