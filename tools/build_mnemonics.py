#!/usr/bin/env python3
"""Build mnemonics.json from the mnemonic pages, for 'Mnemonic of the day' on the home screen."""
import re, json, html, glob
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.items=[]; s.depth=0; s.cur=None; s.cls=[]
    def handle_starttag(s, tag, a):
        c = dict(a).get('class', '')
        if tag == 'div' and re.search(r'\bmnem\b', c) and s.cur is None:
            s.cur = {'l': '', 'tiles': [], 'h': []}; s.depth = 1; s.cls = []; return
        if s.cur is not None:
            if tag == 'div': s.depth += 1
            s.cls.append((tag, c))
    def handle_endtag(s, tag):
        if s.cur is None: return
        if tag == 'div':
            s.depth -= 1
            if s.depth == 0: s.items.append(s.cur); s.cur = None; return
        if s.cls: s.cls.pop()
    def handle_data(s, d):
        if s.cur is None or not d.strip(): return
        cl = ' '.join(c for _, c in s.cls)
        if 'mlbl' in cl: s.cur['l'] += d
        elif 'tile' in cl and 'tiles' not in cl.split(): s.cur['tiles'].append(d.strip())
        elif 'mhook' in cl: s.cur['h'].append(d)
        
SUB = {'mnemonics.html': ('Modern India', 'mnemonics.html'), 'gov-mnemonics.html': ('Governance', 'gov-mnemonics.html'), 'ir-mnemonics.html': ('International Relations', 'ir-mnemonics.html'), 'pg2-mnemonics.html': ('Polity GS-2', 'pg2-mnemonics.html')}
out = []
for f, (sub, url) in SUB.items():
    p = P(); p.feed(open(f, encoding='utf-8').read())
    for it in p.items:
        lbl = re.sub(r'\s+', ' ', html.unescape(it['l'])).replace('Mnemonic ·', '').strip(' ·')
        hook = re.sub(r'\s+', ' ', html.unescape(''.join(it['h']))).strip()
        word = ''.join(it['tiles'])
        if not (word or hook): continue
        out.append({'s': sub, 'l': lbl, 'w': word, 't': hook[:420], 'u': url})
json.dump(out, open('mnemonics.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'mnemonics')
