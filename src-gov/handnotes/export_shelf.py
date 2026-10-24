# -*- coding: utf-8 -*-
"""Export the full (uncondensed) handwritten-notes DSL chapters to shelf-ready note items.
Writes ../book/fullnotes.json  {chapter_id: {'notes': [...], 'meta': {...}}}"""
import re, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch_a, ch_b, ch_c, ch_d, ch_e, ch_f, ch_g
ALL = [c for m in (ch_a, ch_b, ch_c, ch_d, ch_e, ch_f, ch_g) for c in m.CHS]
import listify; listify.apply_all(ALL)
BOOKDATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'book', 'bookdata.json')
VISWORDS = {}
for part in json.load(open(BOOKDATA, encoding='utf8'))['parts']:
    for c in part['chapters']:
        VISWORDS[int(c['id'])] = {re.sub(r'[^A-Z0-9]', '', (v.get('word') or '').upper()) for v in c.get('visuals', []) if v.get('type') == 'mnemonic'}
def clean(s):
    s = re.sub(r'<span class="pyq">(.*?)</span>', r' (\1)', s)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = s.replace('&amp;', '&')
    s = re.sub(r'\s+', ' ', s).strip()
    return s
def nice(s):
    s = clean(re.sub(r'<[^>]+>', '', s))
    if s.isupper() or (sum(c.isupper() for c in s) > 0.8 * sum(c.isalpha() for c in s)):
        w = []
        for t in s.split(' '):
            core = re.sub(r'[^A-Za-z]', '', t)
            w.append(t if len(core) <= 4 or not core.isupper() else t.capitalize())
        s = ' '.join(w)
        s = s[:1].upper() + s[1:]
    return s
def bullet(x): return clean(x).replace(' · ', '; ')
def kid(x):
    if isinstance(x, tuple):  # sub-tree
        return '<b>%s</b>: ' % clean(re.sub(r'<[^>]+>', '', x[1])) + '; '.join(bullet(k) if not isinstance(k, tuple) else kid(k) for k in x[2])
    return bullet(x)
def items(n, cid):
    k = n[0]; out = []
    if k == 'tree':
        out.append({'h': nice(n[1])})
        out += [kid(x) for x in n[2]]
    elif k == 'sec': out.append({'h': nice(n[1]), 'sec': 1})
    elif k == 'bx':
        kind, body = n[1], clean(n[2])
        if kind == 'ca': out.append({'ca': body})
        elif kind == 'qt': out.append({'call': {'kind': 'quote', 'tag': 'Quote', 'body': [body]}})
        elif kind == 'pk': out.append({'call': {'kind': 'teacher', 'tag': 'Value addition', 'body': [body]}})
        elif kind == 'ye': out.append({'call': {'kind': 'alert', 'tag': 'Note', 'body': [body]}})
        elif kind == 'gr': out.append({'call': {'kind': 'note', 'tag': 'Way forward / key point', 'body': [body]}})
        else: out.append({'call': {'kind': 'note', 'tag': 'Key point', 'body': [body]}})
    elif k == 'tb': out.append({'tbl': {'head': [clean(h) for h in n[1]], 'rows': [[clean(c) for c in r] for r in n[2]]}})
    elif k == 'mn':
        w = re.sub(r'[^A-Z0-9]', '', n[1].upper())
        if w in VISWORDS.get(cid, set()): return []
        out.append({'call': {'kind': 'shortcut', 'tag': 'Memory aid · ' + n[1], 'body': [clean(n[2])]}})
    elif k == 'fl': out.append({'flow': {'title': nice(n[2] or 'Flow'), 'steps': [clean(s) for s in n[1]]}})
    elif k == 'hub':
        out.append({'h': nice(n[3] or n[1])}); out.append('<b>%s</b>: ' % clean(n[1]) + '; '.join(clean(s) for s in n[2]))
    elif k == 'tl': out.append({'timeline': [[clean(re.sub(r'<[^>]+>', '', a)), clean(b)] for a, b in n[1]]})
    elif k == 'two':
        for x in list(n[1]) + list(n[2]): out += items(x, cid)
    return out
res = {}
for ch in ALL:
    cid = int(ch['id']); notes = []
    for n in ch['nodes']:
        if n[0] == 'sw': continue
        notes += items(n, cid)
    res[cid] = {'notes': notes, 'meta': {'title': nice(ch['title']), 'toc': ch.get('toc', ''), 'prio': ch.get('prio', 'M'), 'pyq': clean(ch.get('pyq', '')),
        'simple': clean(ch.get('simple', '')), 'recall': [[clean(a), clean(b)] for a, b in ch.get('recall', [])], 'part': ch.get('part')}}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'book', 'fullnotes.json')
json.dump(res, open(out, 'w', encoding='utf8'), ensure_ascii=False)
print({k: len(v['notes']) for k, v in res.items()})
