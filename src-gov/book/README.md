# Notes book builder (print-ready A4 PDF with a notes column)

Build: `python3 book.py bookdata.json OUT.pdf full` (or `sample 4` for a front-matter + chapter 4 sample). Needs `pip install weasyprint pillow`; fonts Inter and Lora.

## bookdata.json
```
{ "meta": {title, subtitle, cover_top, cover_mid, cover_foot, running_head, imprint:[html lines], back_matter},
  "parts": [ {label, title, sub, chapters:[ chapter, ... ]} ] }
chapter = { id, title, pages, priority "H|M|L", pyqs "2017, 2020*", prelims_pyqs?,
  lens:{prelims:[], mains:[], close}, simple:["**bold** plain-language lines"], terms:[[term, plain meaning]], remember,
  notes:[ "bullet html" | {h:"subheading"} | {tbl:{head:[],rows:[[]]}} | {alert:"..."} | {fig:{img,cap,pg,sq}} ],
  recall:[[q,a]], traps:[{k,t,d,r}], quiz:[{q,o:[],a:index}], visuals:[ ... ] }
```
Visual blocks (`visuals`, rendered by viz.py; `pos:"top"` or `after:"text of a note/heading/table-head"`):
- `{type:"mnemonic", sentence, letters:[[initial, word]], title, note}`: a real-meaning sentence whose initials spell the list.
- `{type:"mindmap", center, branches:[{t, c:[short lines]}], title}`: 3 to 8 branches around a centre.
- `{type:"fork", root:{t,c}, branches:[{t, c, verdict}], title}`: one situation, 2 to 3 outcomes.
- `{type:"flow", steps:[[title, line, line...]], per_row:4, title}`: process, chain or timeline in boxes.
`to_bookdata.py` shows the Governance conversion. The notes panel is drawn on every interior page; the cover, title page and part openers are clean.
