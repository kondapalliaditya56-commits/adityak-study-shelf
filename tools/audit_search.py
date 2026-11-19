#!/usr/bin/env python3
"""Check every search result of every notebook: target file exists, anchor id exists, chapter matches."""
import re, json, os, sys
def ids(f, cache={}):
    if f not in cache:
        cache[f] = set(re.findall(r'\bid="([^"]+)"', open(f, encoding='utf-8').read())) if os.path.exists(f) else None
    return cache[f]
def data(f, sid):
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<script type="application/json" id="%s">(.*?)</script>' % sid, s, re.S)
    return json.loads(m.group(1))
bad = 0
def check(page, target, n):
    global bad
    f, _, a = target.partition('#')
    i = ids(f)
    if i is None: bad += 1; print(page, 'MISSING FILE', target) if bad < 40 else 0
    elif a and a not in i: bad += 1; print(page, 'MISSING ANCHOR', target) if bad < 40 else 0
tot = {}
# prefix pages: discovered from the file names (x-search.html -> x-ch01.html)
import glob
PAGES = []
for f in sorted(glob.glob('*-search.html')):
    pre = f[:-len('-search.html')]
    if pre == 'ca': continue
    src = open(f, encoding='utf-8').read()
    m = re.search(r'id="(sdata|idx)"', src)
    if not m: continue
    D0 = data(f, m.group(1))
    ck = 'ch' if 'ch' in D0[0] else 'c'; tk = 'cht' if 'cht' in D0[0] else 'n'
    PAGES.append((f, m.group(1), pre + '-ch', ck, tk))
    used = set(re.findall(r"""<a href=\\?["']?([a-z0-9]+)-ch['"]""", src)) | set(re.findall(r"""href="([a-z0-9]+)-ch'\+""", src))
    if used and used != {pre}:
        bad += 1; print(f, 'LINKS TO WRONG NOTEBOOK PREFIX', used, 'expected', pre)
for page, sid, pre, ck, tk in PAGES:
    D = data(page, sid); tot[page] = len(D)
    for d in D:
        if d.get('href'): check(page, d['href'], 1); continue
        c = int(d[ck]); check(page, '%s%02d.html#%s' % (pre, c, d['id']), 1)
# modern india
D = json.load(open('search.json')); tot['search.html'] = len(D['items'] if 'items' in D else D)
for it in (D.get('items') or []): check('search.html', 'ch%02d.html#%s' % (it['c'], it['s']), 1)
print(tot); print('broken links:', bad)

# chapter title check: the title stored in the index must match the page it opens
def norm(t): return re.sub(r'[^a-z0-9]+', '', re.sub(r'<[^>]+>', '', t).lower())
def h1(f):
    s = open(f, encoding='utf-8').read(); m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S); return norm(m.group(1)) if m else ''
mm = 0
for page, sid, pre, ck, tk in PAGES:
    seen = {}
    for d in data(page, sid):
        if d.get('href') or not d.get(ck): continue
        c = int(d[ck]); f = '%s%02d.html' % (pre, c)
        if (f, d[tk]) in seen: continue
        seen[(f, d[tk])] = 1
        a, b = norm(d[tk]), h1(f)
        if a and b and a not in b and b not in a:
            mm += 1
            if mm < 25: print('TITLE MISMATCH', page, f, '| index:', d[tk][:40], '| page:', b[:40])
print('title mismatches:', mm)
