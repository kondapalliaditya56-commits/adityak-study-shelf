# Economy generator (shelf notebook + book edition)
One data source feeds both outputs: chN.py (chapter content), layers_N.json (simple words, key terms, traps, mnemonics, diagrams) and pyq_final.json (PYQs + Mains keywords).
- Shelf pages: `python3 build.py` (writes out/eco-*.html).
- Book: `python3 book_export.py OUTDIR 1,2,...,13`, then `python3 ../src-gov/book/book.py OUTDIR/bookdata.json economy_book.pdf full`.
Rule: change content or layers in one place and rebuild both, so the shelf and the book never drift.
Paths inside the scripts point at the original working directory; adjust them when running elsewhere.
