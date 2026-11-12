# -*- coding: utf-8 -*-
"""Merge the extras layer (hand/layerN.py + hand/ncertN.py) into an Economy Ch object, for the textbook and the shelf.
apply(c, n) returns a deep copy with: understand/example/formula cards at each numbered section start; NCERT boxes, hook and
mnemonics at its end; new sections for 60 seconds + words + NCERT map, formula sheet + number card + drills, NCERT checklist, abbreviation column."""
import copy, importlib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.path.join(HERE, 'hand')):
    if p not in sys.path: sys.path.insert(0, p)
import extras_html as X
from eco_gloss import G as GL, SKIP

TOK = re.compile(r'(?<![A-Za-z0-9])(?:Y-o-Y|[A-Z][A-Za-z]?[A-Z0-9&\-]+[A-Za-z0-9]|[A-Z]{2,}[0-9]?|[A-Z]&[A-Z])(?![A-Za-z0-9])')

def slug(t): return re.sub(r'[^a-z0-9]+', '-', X.tx(t).lower()).strip('-')

def _load(name):
    try: return importlib.import_module(name)
    except ImportError: return None

def put(sec, html, where='end'):
    pl = X.tx(html); pl = re.sub(r'\s+', ' ', pl)
    if where == 'start':
        sec['html'].insert(0, html); sec['plain'].insert(0, pl); sec['items'].insert(0, ('raw', html, pl))
    else:
        sec['html'].append(html); sec['plain'].append(pl); sec['items'].append(('raw', html, pl))

def newsec(title):
    return {'id': slug(title), 'title': title, 'html': [], 'plain': [], 'items': []}

def apply(c, n):
    layer = _load('layer%d' % n)
    if layer is None: return c
    nm = _load('ncert%d' % n)
    c = copy.deepcopy(c)
    NCX = getattr(nm, 'NC', {}) if nm else {}
    SRC = getattr(nm, 'SRC', 'NCERT') if nm else 'NCERT'
    first = [True]
    def css():
        if first[0]: first[0] = False; return X.STYLE % {}
        return ''
    # ---- numbered sections
    for sec in c.secs:
        m = re.match(r'^(\d+) · ', sec['title'])
        if not m: continue
        k = m.group(1); S = layer.SEC.get(k)
        start = ''
        if S: start += X.understand(S)
        if k in getattr(layer, 'FM', {}): start += X.fm(layer.FM[k], False, '📐 Formulas of this section')
        if start: put(sec, start, 'start')
        for b in NCX.get(k, []): put(sec, X.nc_box(SRC, b))
        if S and S.get('hook'): put(sec, X.hook(S))
        for mn in (S or {}).get('mn', []): put(sec, X.mnemonic(mn))
    # ---- new sections
    head = newsec('Start here: 60 seconds, key words, NCERT map')
    TOP = getattr(layer, 'TOP', None)
    if TOP:
        h = '<div class="xb"><span class="xt">The whole chapter in 60 seconds</span>' + X.ul(['<b>%s</b>: %s' % (X.e(a), X.e(b)) for a, b in TOP['sixty']]) + '</div>'
        h += X.table({'head': ['Word', 'Meaning'], 'rows': [['<b>%s</b>' % X.e(a), X.e(b)] for a, b in TOP['words']]})
        put(head, css() + h)
    if nm and getattr(nm, 'NCMAP', None):
        put(head, '<div class="xb xn"><span class="xt">📘 Read NCERT first: where each NCERT part fits this chapter</span>' + X.table({'head': ['NCERT part', 'Handout section', 'What it adds'], 'rows': [[X.e(a), X.e(b), X.e(cc)] for a, b, cc in nm.NCMAP]}) + '</div>')
    idx = 1 if c.secs and c.secs[0]['title'].startswith('Exam lens') else 0
    if head['html']: c.secs.insert(idx, head)
    # NCERT end boxes, formulas, numbers
    tail = newsec('Formula sheet, number card and drills')
    if getattr(layer, 'FM', None):
        rows = []
        for sec in layer.FM:
            for it in layer.FM[sec]: rows.append(['Sec %s' % sec, it[0], '<b>%s</b>' % it[1], 'handout'])
        for sec, boxes in NCX.items():
            for b in boxes:
                for kk in b.get('blocks', []):
                    for it in kk.get('fm', []): rows.append(['Sec %s' % sec, it[0], '<b>%s</b>' % it[1], 'NCERT'])
        put(tail, '<div class="xb xe"><span class="xt">📐 Formula sheet: cover the third column, say the formula, then check</span>' + X.table({'head': ['Where', 'Name', 'Formula', 'Source'], 'rows': rows}) + '</div>')
    if getattr(layer, 'NUMBERS', None):
        put(tail, '<div class="xb"><span class="xt">🔢 Number card: figures to hold</span><div class="xnum">%s</div></div>' % ''.join('<span><b>%s</b>%s</span>' % (X.e(a), X.e(b)) for a, b in layer.NUMBERS))
    if getattr(layer, 'DRAW', None):
        put(tail, '<div class="xb xe"><span class="xt">✏ Blank-page drill: draw these from memory, then check</span>' + X.ul([X.e(x) for x in layer.DRAW]) + '</div>')
    if tail['html']: c.secs.append(tail)
    chk = newsec('NCERT checklist: end boxes, questions, key concepts')
    for b in NCX.get('end', []): put(chk, X.nc_box(SRC, b))
    if nm:
        if getattr(nm, 'NCONLY', None): put(chk, '<div class="xb xn"><span class="xt">📘 NCERT parts with no matching handout section (read them from NCERT)</span>' + X.ul(['<b>%s</b>: %s' % (X.e(a), X.e(b)) for a, b in nm.NCONLY]) + '</div>')
        if getattr(nm, 'NCKEY', None): put(chk, '<div class="xb xn"><span class="xt">📘 NCERT key concepts: tick each when you can define it</span>%s</div>' % ''.join('<span class="xchip">☐ %s</span>' % X.e(x) for x in nm.NCKEY))
        if getattr(nm, 'NCQ', None): put(chk, '<div class="xb xn"><span class="xt">📘 NCERT’s own end-of-chapter questions: can you answer each from these notes?</span>' + X.table({'head': ['NCERT question', 'Answer lives in'], 'rows': [[X.e(a), X.e(b)] for a, b in nm.NCQ]}) + '</div>')
    if chk['html']: c.secs.append(chk)
    # abbreviation column
    text = ' '.join(' '.join(s['plain']) for s in c.secs)
    found = {}
    for m in TOK.finditer(text):
        a = m.group(0)
        if a in SKIP: continue
        found[a] = found.get(a, 0) + 1
    ents = [(a, GL[a][0], GL[a][1]) for a in sorted(found, key=lambda x: (-found[x], x)) if a in GL]
    miss = [a for a in found if a not in GL]
    if miss: print('ch%d unexpanded abbreviations:' % n, miss)
    ab = newsec('Abbreviation column')
    put(ab, '<p>Every short form used in this chapter, expanded.</p>' + X.gloss(ents))
    c.secs.append(ab)
    return c
