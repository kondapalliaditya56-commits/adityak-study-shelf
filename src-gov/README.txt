Governance notebook: generator

Source of truth: hubdata.json (exported from the Governance Study Hub: SECS notes, PYQS, MAP, TL, FLOWS, CMP, LINKS, TRAPS, MCQ, CARDS, ...).
Rebuild:  python3 src-gov/build.py OUTDIR   (then copy gov-*.html and img/gov-*.jpg to the repo root / img)
Content rule: only facts from the two Sarrthi IAS GS-2 Governance modules. No outside facts.
Registry steps after a rebuild: library.json and the libdata block in index.html (both written by build.py from gov-chapters.json), plus sw.js (FILES and version V).
