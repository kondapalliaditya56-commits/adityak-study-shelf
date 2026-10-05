International Relations notebook: generator

Rebuild:  python3 src-ir/build.py OUTDIR   (then copy ir-*.html to the repo root)
Add a chapter: write chNN.py in the same shape as ch02.py (CH, SRC, PYQ, build(), MAP, TIMELINE, LINKS, RECALL, TRAPS, MCQ, CARDS, SKELETONS), import it in build.py, and add it to the chapter list. Then update library.json, the libdata block in index.html, and sw.js (FILES list and version V).
Content rule: only facts from the handouts and slides. No outside facts.

Live current-affairs layer: ca00.py (Start Here radar), ca01.py and ca02.py (cards per section, radar table, MCQs, flashcards). build.py appends each LIVE card to the section whose title matches exactly. Sources: Aug and Jul 2026 CA magazines in the UPSC Project; web items are labelled.
