#!/usr/bin/env python3
"""Build search-all.json: one lightweight index (section titles + a short snippet) over every notebook,
used by the search box on the Study Shelf home screen. Re-run after notebooks change."""
import re, json, html
def idx(f, sid):
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<script type="application/json" id="%s">(.*?)</script>' % sid, s, re.S)
    return json.loads(m.group(1))
def snip(x, t):
    x = re.sub(r'\s+', ' ', x or '').strip()
    if x.lower().startswith(t.lower()): x = x[len(t):].lstrip(' .#-:')
    return x[:150]
NB = [  # id, title, file prefix, search page, data id, chapter key, chapter-title key
 ('modern-india', 'Modern India', 'ch', None, None, None, None),
 ('polity', 'Polity', 'pol-ch', 'pol-search.html', 'idx', 'ch', 'cht'),
 ('economy', 'Economy', 'eco-ch', 'eco-search.html', 'idx', 'ch', 'cht'),
 ('geography', 'Geography', 'geo-ch', 'geo-search.html', 'sdata', 'c', 'n'),
 ('sociology', 'Sociology I', 'soc-ch', 'soc-search.html', 'sdata', 'c', 'n'),
 ('sociology2', 'Sociology II', 'soc2-ch', 'soc2-search.html', 'sdata', 'c', 'n'),
 ('polity-gs2', 'Polity GS-2', 'pg2-ch', 'pg2-search.html', 'sdata', 'c', 'n'),
 ('governance', 'Governance', 'gov-ch', 'gov-search.html', 'sdata', 'c', 'n'),
 ('international-relations', 'International Relations', 'ir-ch', 'ir-search.html', 'sdata', 'c', 'n'),
 ('gs3', 'GS3', 'gs3-ch', 'gs3-search.html', 'sdata', 'c', 'n'),
 ('social-justice-gs2', 'Social Justice GS-2', 'sj-ch', 'sj-search.html', 'sdata', 'c', 'n'),
 ('world-mapping', 'World Mapping', 'wm-ch', 'wm-search.html', 'sdata', 'c', 'n'),
 ('current-affairs', 'Current Affairs', '', None, None, None, None)]
out = {'nb': [[n[0], n[1], n[2]] for n in NB], 'r': []}
for i, (nid, title, pre, page, sid, ck, tk) in enumerate(NB):
    if nid == 'modern-india':
        j = json.load(open('search.json'))
        ch = j['chapters']
        for it in j['items']:
            out['r'].append([i, int(it['c']), re.sub(r'<[^>]+>', '', ch.get(str(it['c']), '')), it['t'], it['s'], snip(it.get('x'), it['t'])])
    elif nid == 'current-affairs':
        s = open('ca-search.html', encoding='utf-8').read(); a = s.index('var D=['); b = s.index('];', a)
        for d in json.loads(s[a + 6:b + 1]):
            out['r'].append([i, 0, d.get('sub', '') + ' · ' + d.get('m', ''), d['t'], d['u'], snip(d.get('x'), d['t'])])
    else:
        for d in idx(page, sid):
            if d.get('href'):
                out['r'].append([i, int(d.get(ck) or 0), re.sub(r'<[^>]+>', '', d.get(tk, '')), d['t'], d['href'], snip(d.get('x'), d['t'])]); continue
            out['r'].append([i, int(d[ck]), re.sub(r'<[^>]+>|(High|Medium|Low) priority$', '', d.get(tk, '')), d['t'], d['id'], snip(d.get('x'), d['t'])])
json.dump(out, open('search-all.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
import os; print(len(out['r']), 'sections,', os.path.getsize('search-all.json') // 1024, 'KB')
