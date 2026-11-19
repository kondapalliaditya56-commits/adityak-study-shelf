#!/usr/bin/env python3
"""Add the read-aloud script to every notebook page (idempotent). Run after generating new pages."""
import glob, re
SKIP = {'index.html', 'pdfview.html'}
TAGS = ['<script src="readaloud.js" defer></script>', '<script src="anchorfix.js" defer></script>']
n = 0
for f in sorted(glob.glob('*.html')):
    if f in SKIP: continue
    s = open(f, encoding='utf-8').read()
    if '</body>' not in s: continue
    add = ''.join(t for t in TAGS if t.split('"')[1] not in s)
    if not add: continue
    i = s.rindex('</body>')
    open(f, 'w', encoding='utf-8').write(s[:i] + add + s[i:]); n += 1
print('added to', n, 'pages')
