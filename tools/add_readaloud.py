#!/usr/bin/env python3
"""Add the read-aloud script to every notebook page (idempotent). Run after generating new pages."""
import glob, re
SKIP = {'index.html', 'pdfview.html'}
tag = '<script src="readaloud.js" defer></script>'
n = 0
for f in sorted(glob.glob('*.html')):
    if f in SKIP: continue
    s = open(f, encoding='utf-8').read()
    if 'readaloud.js' in s or '</body>' not in s: continue
    i = s.rindex('</body>')
    open(f, 'w', encoding='utf-8').write(s[:i] + tag + s[i:]); n += 1
print('added to', n, 'pages')
