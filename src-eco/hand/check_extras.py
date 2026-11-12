# usage: python3 hand/check_extras.py N   (run from scratchpad). Validates layerN.py and ncertN.py for Economy chapter N.
import sys, re, importlib, html, os
SC = '/tmp/claude-0/-home-claude/72cbe3e5-542c-596f-8ef0-06a8d705bf8d/scratchpad'
sys.path.insert(0, SC); sys.path.insert(0, SC + '/hand')
n = int(sys.argv[1])
H = open('%s/ncert/h%d.txt' % (SC, n)).read()
secs = re.findall(r'^## (\d+) · ', H, flags=re.M)
ok = True
def strip(t): return html.unescape(re.sub(r'<[^>]+>', ' ', str(t)))
def toks(t):
    out = set()
    for m in re.finditer(r'\d[\d,]*(?:\.\d+)?', t):
        x = m.group(0).replace(',', '').rstrip('.')
        out.add(x)
    return out
def big(x): return len(x) >= 2 or '.' in x
Hn = toks(H)
layer = importlib.import_module('layer%d' % n)
print('sections in handout:', secs)
# ---- layer
for k in secs:
    S = layer.SEC.get(k)
    if not S: print('LAYER: no SEC for section', k); ok = False; continue
    for f in ('plain', 'eg', 'hook'):
        if not S.get(f): print('LAYER: section', k, 'missing', f); ok = False
    for f in ('plain', 'eg', 'hook'):
        t = strip(S.get(f, ''))
        if 'not from the handout' in t or 'practice' in t.lower(): continue
        miss = [x for x in toks(t) if big(x) and x not in Hn]
        if miss: print('LAYER: sec', k, f, 'numbers not in handout text:', miss); ok = False
    for mn in S.get('mn', []):
        L = mn['letters']
        if mn.get('word') or mn.get('kind') == 'word':
            w = re.sub(r'[^A-Z]', '', mn['word'])
            if w != ''.join(l[0] for l in L): print('BAD WORD MNEMONIC', mn['word']); ok = False
        else:
            ini = ''.join(x[0].upper() for x in mn['sentence'].split())
            if ini != ''.join(l[0].upper() for l in L): print('BAD SENTENCE MNEMONIC', mn['sentence']); ok = False
        for l in L:
            if not l[1].upper().startswith(l[0].upper()): print('CHIP DOES NOT START WITH LETTER', l); ok = False
for k in layer.SEC:
    if k not in secs: print('LAYER: SEC key', k, 'is not a numbered section'); ok = False
for k, items in getattr(layer, 'FM', {}).items():
    if k not in secs: print('FM key not a section', k); ok = False
    for it in items:
        if len(it) < 3: print('FM tuple needs (name, formula, note)', it); ok = False
if not getattr(layer, 'TOP', None) or len(layer.TOP.get('sixty', [])) < 5 or len(layer.TOP.get('words', [])) < 5: print('TOP needs >=5 sixty and >=5 words'); ok = False
if not getattr(layer, 'NUMBERS', None): print('NUMBERS missing'); ok = False
if not getattr(layer, 'DRAW', None): print('DRAW missing'); ok = False
# ---- ncert
try:
    nm = importlib.import_module('ncert%d' % n)
except ImportError:
    print('no ncert%d.py yet' % n); print('OK' if ok else 'FIX ABOVE'); sys.exit()
src = ''
for f in nm.SRCFILES:
    src += open('%s/ncert/txt/%s.txt' % (SC, f)).read() + '\n'
Sn = toks(src) | Hn
def walk(b):
    for f in ('why', 'link'): yield b.get(f, '')
    for k in b.get('blocks', []):
        yield k.get('h', '')
        for p in k.get('pts', []): yield p
        for it in k.get('fm', []): yield ' '.join(str(x) for x in it)
        if k.get('tbl'):
            yield ' '.join(k['tbl']['head'])
            for r in k['tbl']['rows']: yield ' '.join(r)
        if k.get('fig'):
            yield k['fig'][1]
            if not os.path.exists(SC + '/' + k['fig'][0]): print('FIG FILE MISSING', k['fig'][0]); globals()['ok'] = False
    for d in b.get('d', []): yield d
for sec, boxes in nm.NC.items():
    if sec != 'end' and sec not in secs: print('NC key not a numbered section:', sec); ok = False
    for b in boxes:
        for f in ('ref', 'why', 'link', 'blocks'):
            if f not in b: print('NC box missing', f, 'in', sec, b.get('ref')); ok = False
        for t in walk(b):
            t = strip(t)
            if 'worked out' in t.lower() or 'arithmetic' in t.lower(): continue
            miss = [x for x in toks(t) if big(x) and x not in Sn]
            if miss: print('NCERT sec', sec, b.get('ref'), '| numbers not found in NCERT source or handout:', miss, '|', t[:70]); ok = False
for a in ('SRC', 'SRCFILES', 'NC', 'NCMAP', 'NCQ', 'NCKEY', 'NCONLY'):
    if not hasattr(nm, a): print('ncert module missing', a); ok = False
print('OK' if ok else 'FIX ABOVE (numbers flagged may be legitimately derived: say "worked out here" in that text, or fix)')
