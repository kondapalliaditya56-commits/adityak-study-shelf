# usage: python3 check_layer.py N   (validates layers_N.json against chN.py)
import sys, json, re, importlib
sys.path.insert(0, '.')
n = int(sys.argv[1])
L = json.load(open('layers_%d.json' % n, encoding='utf8'))[str(n)]
ch = importlib.import_module('ch%d' % n).c
import book_export as be
ok = True
for k in ('simple', 'terms', 'remember', 'traps', 'visuals'):
    if k not in L: print('MISSING', k); ok = False
if not 3 <= len(L['simple']) <= 6: print('simple should be 3-6 lines'); ok = False
if not 8 <= len(L['terms']) <= 16: print('terms should be 8-16'); ok = False
if not 3 <= len(L['traps']) <= 6: print('traps 3-6'); ok = False
words = 0
for v in L['visuals']:
    if v['type'] == 'mnemonic':
        if v.get('word'):
            words += 1
            w = re.sub(r'[^A-Z]', '', v['word'])
            ls = ''.join(l[0] for l in v['letters'])
            if w != ls: print('BAD WORD', v['word'], ls); ok = False
        else:
            ini = ''.join(x[0].upper() for x in v['sentence'].split())
            ls = ''.join(l[0].upper() for l in v['letters'])
            if ini != ls: print('BAD SENTENCE', ini, ls); ok = False
        for l in v['letters']:
            if not l[1].upper().startswith(l[0].upper()): print('CHIP DOES NOT START WITH LETTER', l); ok = False
    if v.get('pos') != 'top' and not v.get('after'): print('no anchor', v.get('title')); ok = False
if not 2 <= len(L['visuals']) <= 5: print('2-5 visuals'); ok = False
if words < 1: print('need at least one word mnemonic'); ok = False
try:
    notes = be.sec_notes(ch); be.place(notes, L['visuals'])
except SystemExit as e: print(e); ok = False
print('OK' if ok else 'FIX ABOVE')
