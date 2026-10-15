# -*- coding: utf-8 -*-
"""Reference converter: Governance hubdata.json + plain.json + visuals.json -> bookdata.json (the neutral schema book.py reads).
For a new subject, write a similar converter (or write bookdata.json directly). Run from this folder."""
import json, os, base64
SG = '..'
X = json.load(open(SG + '/hubdata.json')); P = json.load(open(SG + '/plain.json')); VIS = json.load(open('visuals.json'))
os.makedirs('img', exist_ok=True)
END = {int(k): v for k, v in X['ENDMAP'].items()}; XC = {int(k): v for k, v in X['XCARDS'].items()}; XQ = {int(k): v for k, v in X['XMCQ'].items()}
PYQ = {p['id']: p for p in X['PYQS']}
for k, b in X['IMG'].items(): open('img/%s.jpg' % k, 'wb').write(base64.b64decode(b))
def chap(s):
    m = END.get(s['id'], {'c': [], 't': [], 'q': []}); notes = []
    for it in s['notes']:
        if isinstance(it, dict) and 'figs' in it:
            for k in it['figs']:
                f = X['FIGDEF'][k]; notes.append({'fig': {'img': 'img/%s.jpg' % k, 'cap': f['cap'], 'pg': f['pg'], 'sq': bool(f.get('sq'))}})
        else: notes.append(it)
    d = P[str(s['id'])]
    return {'id': s['id'], 'title': s['title'], 'pages': s['pages'], 'priority': s['pri'],
            'pyqs': ', '.join('%s%s' % (PYQ[i]['yr'], '*' if PYQ[i].get('partial') else '') for i in s['pyqs']) or 'none quoted in the material',
            'lens': s['lens'], 'simple': d['simple'], 'terms': d['terms'], 'remember': d['remember'], 'notes': notes,
            'recall': [[q, a] for q, a in [X['CARDS'][i] for i in m['c']] + XC.get(s['id'], [])],
            'traps': [X['TRAPS'][i] for i in m['t']],
            'quiz': [{'q': q['q'], 'o': q['o'], 'a': q['a']} for q in [X['MCQ'][i] for i in m['q']] + XQ.get(s['id'], [])],
            'visuals': VIS.get(str(s['id']), [])}
S = {s['id']: s for s in X['SECS']}
book = json.load(open('bookdata.json'))['meta'] if os.path.exists('bookdata.json') else None
meta = book or {}
json.dump({'meta': meta, 'parts': [
    {'label': 'Part I', 'title': 'Module 1', 'sub': 'Civil Services, Transparency, Accountability, Citizen’s Charter and RTI', 'chapters': [chap(S[i]) for i in range(1, 15)]},
    {'label': 'Part II', 'title': 'Module 2', 'sub': 'Corruption, Social Audit, CBI, CVC, Lokpal, Whistleblower and PCA', 'chapters': [chap(S[i]) for i in range(15, 20)]}]},
    open('bookdata.json', 'w'), ensure_ascii=False, indent=1)
