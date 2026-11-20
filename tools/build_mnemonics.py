#!/usr/bin/env python3
"""Build mnemonics.json from the mnemonic pages, for 'Mnemonic of the day' on the home screen.
Each item keeps the whole mnemonic: the word or sentence, the hook line, every letter with its meaning, and the note."""
import re, json, html, glob, math, os
from collections import Counter
SUB = {'mnemonics.html': 'Modern India', 'gov-mnemonics.html': 'Governance', 'ir-mnemonics.html': 'International Relations', 'pg2-mnemonics.html': 'Polity GS-2'}
tx = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()
out = []
for f, sub in SUB.items():
    page = open(f, encoding='utf-8').read()
    sec = None; grp = ''
    for m in re.finditer(r'<section class="msec" id="([^"]+)"|<h2 id="g\d+">(.*?)<a class="anchor"|<div class="mnem[^"]*">(.*?)</div></div>', page, re.S):
        if m.group(1): sec = m.group(1); continue
        if m.group(2) is not None: grp = tx(m.group(2)); continue
        b = m.group(3)
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
                    'o': 1 if own else 0, 'u': f + ('#' + sec if sec else ''), 'y': 'sent' if sent else 'word', 'g': grp})
json.dump(out, open('mnemonics.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'mnemonics;', sum(1 for x in out if x['c']), 'with letter meanings;', sum(1 for x in out if not x['w'].strip()), 'without word')

# ---------- where each mnemonic comes from: chapter and topic ----------
LIB = {l['id']: l for l in json.load(open('library.json'))}
NBID = {'Modern India': ('modern-india', r'ch(\d+)\.html'), 'Governance': ('governance', r'gov-ch(\d+)\.html'),
        'International Relations': ('international-relations', r'ir-ch(\d+)\.html'), 'Polity GS-2': ('polity-gs2', r'pg2-ch(\d+)\.html')}
STOP = set('about after also and are because been between both but can does for from has have into its may more most not one only other our out over than that the their them then there these they this those through under use used uses was were what when where which while will with within would your every each any all per via'.split())
def toks(t): return [w for w in re.findall(r'[a-z0-9]{3,}', html.unescape(t).lower()) if w not in STOP]
def plain(h): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S))))
CH = {}
for sub, (nid, pat) in NBID.items():
    lib = LIB[nid]; rows = []
    for fn in sorted(os.listdir('.')):
        m = re.fullmatch(pat, fn)
        if not m: continue
        n = int(m.group(1)); c = next((c for c in lib['chapters'] if c['n'] == n), None)
        if not c or n == 0 and False: continue
        raw = open(fn, encoding='utf-8').read(); body = raw[raw.find('<main'):] if '<main' in raw else raw
        pos = []
        for sec in c['secs']:
            i = body.find('id="%s"' % sec['id'])
            if i >= 0: pos.append((i, sec['id'], sec['t']))
        pos.sort(); blocks = []
        for k, (i, sid, st) in enumerate(pos):
            j = pos[k + 1][0] if k + 1 < len(pos) else len(body)
            blocks.append((sid, st, body[i:j]))
        rows.append({'n': n, 'fn': fn, 'title': c['title'], 'body': body, 'text': plain(body), 'blocks': blocks})
    CH[sub] = rows
def idf(rows, key):
    df = Counter()
    for r in rows: df.update(set(toks(key(r))))
    return {w: math.log((len(rows) + 1) / (d + 0.5)) for w, d in df.items()}
IDF = {s: idf(r, lambda r: r['text']) for s, r in CH.items() if r}
def locate(it):
    rows = CH.get(it['s']) or []
    gm = re.match(r'(?:Module|Chapter) (\d+)', it.get('g', ''))
    if gm and it['s'] in ('Governance', 'International Relations'): rows = [r for r in rows if r['n'] == int(gm.group(1))] or rows
    if not rows: return None
    lab = it['l'] + ' ' if False else it['l']
    # exact: the chapter page itself carries this mnemonic
    for r in rows:
        if lab and lab in html.unescape(r['body']) and ('mlbl' in r['body']):
            i = html.unescape(r['body']).find(lab); cur = None
            b = html.unescape(r['body'])
            for sid, st, blk in r['blocks']:
                if html.unescape(blk).find(lab) >= 0: cur = (sid, st); break
            return r, cur, 9.0
    q = toks(it['l'] + ' ' + it['l'] + ' ' + it['w'] + ' ' + it['t'] + ' ' + ' '.join(c[1] for c in it['c']) + ' ' + it['n'])
    q = [w for w in q if w in IDF[it['s']]]
    if not q: return None
    W = IDF[it['s']]; tot = sum(W[w] for w in set(q)) or 1
    def sc(text, titlebonus=''):
        ts = set(toks(text)); tt = set(toks(titlebonus))
        return sum(W[w] * (1 + (0.8 if w in tt else 0)) for w in set(q) if w in ts or w in tt) / tot
    rows = [r for r in rows if r['n'] > 0] or rows
    best = max(rows, key=lambda r: sc(r['text'], r['title']))
    cs = sc(best['text'], best['title'])
    sec = None
    if best['blocks']:
        sb = max(best['blocks'], key=lambda b: sc(plain(b[2]), b[1])); sec = (sb[0], sb[1]); ss = sc(plain(sb[2]), sb[1])
    return best, sec, cs
nloc = 0
for it in out:
    r = locate(it)
    if not r: continue
    ch, sec, conf = r
    if conf < 0.5: continue
    it['ch'] = ch['n']; it['ct'] = ch['title']; it['cf'] = ch['fn']
    if it['s'] == 'International Relations': sec = None
    if sec and sec[0] not in ('chapter-map',): it['ci'] = sec[0]; it['cs'] = sec[1]
    it['q'] = 1 if conf >= 9 else 0; it['cf0'] = round(conf, 2) if conf < 9 else 1
    nloc += 1
print(nloc, 'of', len(out), 'linked to a chapter;', sum(1 for x in out if x.get('q') == 1), 'exact')
json.dump(out, open('mnemonics.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
