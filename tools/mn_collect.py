"""Collect mnemonics from handwritten-notes sources into /tmp/mn_<nb>.json. Usage: python3 tools/mn_collect.py gov|pg2|ir"""
import sys, os, json, importlib, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
nb = sys.argv[1]
def walk(x, out):
    if isinstance(x, tuple):
        if len(x) >= 3 and x[0] == 'mn': out.append((x[1], x[2]))
        for y in x: walk(y, out)
    elif isinstance(x, list):
        for y in x: walk(y, out)
if nb == 'ir':
    sys.path.insert(0, os.path.join(ROOT, 'src-ir', 'handwritten')); os.chdir(os.path.join(ROOT, 'src-ir', 'handwritten'))
    mods = ['ch0%d_hw' % i for i in range(1, 6)]
    GROUPS = [('Chapter %d' % i, '', range(i, i + 1), c) for i, c in zip(range(1, 6), ['#0277bd', '#00838f', '#5e35b1', '#c2185b', '#2e7d32'])]
else:
    sys.path.insert(0, os.path.join(ROOT, 'src-gov', 'handnotes')); os.chdir(os.path.join(ROOT, 'src-gov', 'handnotes'))
    if nb == 'gov':
        mods = ['ch_' + c for c in 'abcdefg']; lo, hi = 1, 40
        GROUPS = [('Module 1', "Civil Services, Transparency, Accountability, Citizen's Charter, RTI", range(1, 15), '#00796b'), ('Module 2', 'Corruption, Social Audit, CBI, CVC, Lokpal, Whistleblower, PCA', range(15, 20), '#ef6c00'),
                  ('Module 3', 'Governance, E-Governance, Data Protection, Emerging Tech', range(20, 25), '#5e35b1'), ('Module 4', 'Civil Society, NGOs, SHGs, Pressure Groups, CAG', range(25, 30), '#c2185b'), ('Module 5', 'Regulatory Bodies, FSSAI, CCI', range(30, 34), '#2e7d32')]
    else:
        mods = ['ch_' + c for c in 'hijklmnopqrs']; lo, hi = 40, 108
        GROUPS = [('Constitution and Union', 'Constitutionalism, living Constitution, Union and its territory', range(40, 49), '#1565c0'), ('Fundamental Rights 1', 'Art 12, reservation, Art 19, contempt, media, protest', range(49, 60), '#ef6c00'),
                  ('Fundamental Rights 2', 'Arts 19(1)(g) to 30, Article 21, secularism, Waqf', range(60, 76), '#00796b'), ('DPSP and Duties', 'DPSP, Article 39(b), UCC, Fundamental Duties', range(76, 80), '#c2185b'),
                  ('Bodies and Commissions', 'NCSC, NCST, NCBC, NHRC, NCW, NCPCR, minorities, NIA', range(80, 88), '#00838f'), ('Executive and Legislature', 'President, ordinance, Cabinet, Speaker, privileges, Parliament', range(88, 99), '#6a1b9a'),
                  ('Centre-State Relations', 'Federalism, legislative, administrative, Governor, fiscal, inter-State', range(99, 108), '#e65100')]
out = []
for m in mods:
    for c in importlib.import_module(m).CHS:
        if nb == 'ir' or lo <= c['id'] < hi:
            o = []; walk(c['nodes'], o); out.append({'id': c['id'], 'toc': c['toc'], 'mn': o})
res = []
for lab, desc, rng, col in GROUPS:
    items = []
    for c in out:
        if c['id'] in rng:
            for w, h in c['mn']: items.append({'toc': c['toc'], 'w': w, 'h': h, 'own': ('own mnemonic' in h or 'Own anchor' in h)})
    if items: res.append({'label': lab, 'desc': desc, 'col': col, 'items': items})
json.dump(res, open('/tmp/mn_%s.json' % nb, 'w'), ensure_ascii=False)
print(nb, sum(len(g['items']) for g in res), 'mnemonics in', len(res), 'groups')
