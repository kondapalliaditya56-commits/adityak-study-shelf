Governance notebook: generator

Source of truth: hubdata.json (exported from the Governance Study Hub: SECS notes, PYQS, MAP, TL, FLOWS, CMP, LINKS, TRAPS, MCQ, CARDS, ...).
Rebuild:  python3 src-gov/build.py OUTDIR   (then copy gov-*.html and img/gov-*.jpg to the repo root / img)
Content rule: only facts from the two Sarrthi IAS GS-2 Governance modules. No outside facts.
Registry steps after a rebuild: library.json and the libdata block in index.html (both written by build.py from gov-chapters.json), plus sw.js (FILES and version V).

Since Oct 2026 the section bodies come from the book edition: book/bookdata.json (notes) + book/visuals.json (mnemonics, mind maps, forks, flows).
Edit visuals.json, run `python3 book/to_bookdata.py` (from book/), then build.py for the shelf and book.py for the PDF. Lens, story, timeline, quiz, flashcards and skeletons still come from hubdata.json.
