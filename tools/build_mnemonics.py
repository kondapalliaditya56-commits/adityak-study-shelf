#!/usr/bin/env python3
"""Build mnemonics.json from the mnemonic pages, for 'Mnemonic of the day' on the home screen.
Each item keeps the whole mnemonic: the word or sentence, the hook line, every letter with its meaning, and the note."""
import re, json, html
SUB = {'mnemonics.html': 'Modern India', 'gov-mnemonics.html': 'Governance', 'ir-mnemonics.html': 'International Relations', 'pg2-mnemonics.html': 'Polity GS-2'}
tx = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()
out = []
for f, sub in SUB.items():
    page = open(f, encoding='utf-8').read()
    sec = None
    for m in re.finditer(r'<section class="msec" id="([^"]+)"|<div class="mnem[^"]*">(.*?)</div></div>', page, re.S):
        if m.group(1): sec = m.group(1); continue
        b = m.group(2)
        lbl = re.search(r'<div class="mlbl">(.*?)</div>', b, re.S)
        lbl = tx(lbl.group(1)) if lbl else ''
        kind = re.match(r'(Mnemonic|Number card|[A-Za-z ]+?)\s*·\s*(.*)', lbl)
        kindw, title = (kind.group(1), kind.group(2)) if kind else ('', lbl)
        own = title.endswith(' · own mnemonic'); title = title.replace(' · own mnemonic', '')
        tiles = ''.join(tx(x) if tx(x) else ' ' for x in re.findall(r'<span class="(?:tile|tsep)">(.*?)</span>', b, re.S))
        sent = re.findall(r'<span class="w"><b>(.*?)</b>(.*?)</span>', b, re.S)
        hook = re.search(r'<div class="mhook">(.*?)</div>', b, re.S)
        hook = tx(hook.group(1)) if hook else ''
        if sent:
            tiles = tiles or ''.join(tx(a) for a, _ in sent)
            hook = hook or ' '.join(tx(a) + tx(r) for a, r in sent)
        chips = [[tx(a), tx(r)] for a, r in re.findall(r'<span class="chip"><i>(.*?)</i>(.*?)</span>', b, re.S)]
        note = re.search(r'<div class="mnote">(.*?)</div>', b, re.S)
        note = tx(note.group(1)) if note else ''
        if not (tiles.strip() or hook): continue
        out.append({'s': sub, 'k': kindw, 'l': title, 'w': tiles, 't': hook, 'c': chips, 'n': note,
                    'o': 1 if own else 0, 'u': f + ('#' + sec if sec else ''), 'y': 'sent' if sent else 'word'})
json.dump(out, open('mnemonics.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'mnemonics;', sum(1 for x in out if x['c']), 'with letter meanings;', sum(1 for x in out if not x['w'].strip()), 'without word')
