# -*- coding: utf-8 -*-
"""Final sync check for Polity class additions: every added heading, table row label, box and recall question must appear in the
handwritten PDF, the textbook PDF and the Shelf chapter page. usage: python3 sync_audit.py HANDWRITTEN.pdf TEXTBOOK.pdf"""
import sys, re, subprocess, html as H, os
import buildfound as bf
from dsl import r_book
hw, tb = sys.argv[1:3]
def pdftext(p): return re.sub(r'\s+', ' ', subprocess.run(['pdftotext', p, '-'], capture_output=True, text=True).stdout)
norm = lambda s: re.sub(r'[^a-z0-9]+', '', H.unescape(re.sub(r'<[^>]+>', '', s)).lower())
HWt, TBt = pdftext(hw), pdftext(tb)
HW, TB = norm(HWt), norm(TBt)
WHW = set(re.findall(r'[a-z0-9]{3,}', HWt.lower())); WTB = set(re.findall(r'[a-z0-9]{3,}', TBt.lower()))
root = os.path.abspath(os.path.join(bf.HERE, '..', '..', '..'))
miss = {'hw': [], 'tb': [], 'shelf': []}; total = 0
for ch in bf.load('polity'):
    if not ch.get('cn_blocks'): continue
    SH = norm(open(os.path.join(root, 'pol-ch%02d.html' % ch['id']), encoding='utf8').read())
    probes = []
    for b in ch['cn_blocks']:
        for n in b['nodes']:
            for it in r_book(n) if n[0] not in ('sw', 'stl') else []:
                if isinstance(it, str): probes.append(it)
                elif 'h' in it: probes.append(it['h'])
                elif 'call' in it: probes.append(' '.join(it['call']['body']))
                elif 'ca' in it: probes.append(it['ca'])
                elif 'tbl' in it: probes += [r[0] for r in it['tbl']['rows'] if r]
    probes += [q for q, a in ch.get('cn_recall', [])]
    for p in probes:
        p2 = re.sub(r'^\s*CLASS\s*·\s*', '', H.unescape(re.sub(r'<[^>]+>', '', p)).strip())
        if p2 in ('Timeline / way forward', 'Flow') : continue
        k = norm(p2)[:16]
        if len(k) < 7: continue
        total += 1
        ws = re.findall(r'[a-z0-9]{3,}', H.unescape(re.sub(r'<[^>]+>', '', p2)).lower())[:6]
        def seen(full, words, Wset): return k in full or all(w in Wset for w in ws)
        if not seen(HW, ws, WHW): miss['hw'].append((ch['id'], p[:60]))
        if not seen(TB, ws, WTB): miss['tb'].append((ch['id'], p[:60]))
        if k not in SH: miss['shelf'].append((ch['id'], p[:60]))
print('probes', total, {k: len(v) for k, v in miss.items()})
for k, v in miss.items():
    for x in v[:15]: print(k, x)
