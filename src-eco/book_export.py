# -*- coding: utf-8 -*-
"""Economy chapter data (Ch objects) + layers.json + PYQ data -> bookdata.json for src-gov/book/book.py.
Single source for the PDF book and the shelf notebook."""
import sys, os, re, json, html, shutil, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pyqlib import lens_note, PYQ, chapter_pyqs, counts_by_section, _secs_for, _blocks, mains_html, _norm

LAYERS = {}
import glob
for f in sorted(glob.glob(os.path.join(HERE, 'layers*.json'))): LAYERS.update(json.load(open(f, encoding='utf8')))
PARTS = [('Part 1', 'Poverty, inequality and employment', [1, 2, 3]), ('Part 2', 'Concepts and national income', [4, 5]),
         ('Part 3', 'Prices, money and finance', [6, 7, 8, 9]), ('Part 4', 'External sector, GST and the budget', [10, 11, 12]),
         ('Part 5', 'Rural and climate finance', [13])]

PSUB = {'Part 1': 'Poverty, inequality and unemployment: how well-being is measured and shared', 'Part 2': 'Basic concepts and how national income is counted', 'Part 3': 'Inflation, banking, money, monetary policy and capital markets', 'Part 4': 'The external sector, GST and the Union budget', 'Part 5': 'Rural credit and climate finance'}

def h(s):
    s = html.escape(str(s), quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', s)
    return s

def plain(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'\*\*', '', str(s)))).strip()

def sec_notes(ch, skip_lens=True):
    """returns list of (note, text_for_anchor)"""
    out = []
    for s in ch.secs:
        is_lens = s['title'].startswith('Exam lens')
        if is_lens:
            out.append(({'h': 'Exam lens: what the handout stresses'}, 'lens'))
        else:
            out.append(({'h': plain(s['title'])}, plain(s['title'])))
        for it in s['items']:
            k = it[0]
            if k == 'p':
                out.append(({'p': h(it[1])}, plain(it[1])))
            elif k == 'ul':
                items = []
                for x in it[1]:
                    if x.startswith('> ') and items: items[-1] += '; ' + x[2:]
                    else: items.append(x)
                for x in items: out.append((h(x), plain(x)))
            elif k == 'ol':
                for i, x in enumerate(it[1], 1): out.append(('<b>%d.</b> %s' % (i, h(x)), plain(x)))
            elif k == 'h3':
                out.append(({'h': plain(it[1])}, plain(it[1])))
            elif k == 'call':
                _, kind, tag, body = it
                if is_lens and kind == 'key': continue            # goes into the Exam lens block
                out.append(({'call': {'kind': kind, 'tag': plain(tag), 'body': [h(b) for b in body]}}, plain(tag) + ' ' + ' '.join(plain(b) for b in body)))
            elif k == 'table':
                _, cap, hd, rows = it
                t = {'head': [h(x) or ' ' for x in hd], 'rows': [[h(c) for c in r] for r in rows]}
                if cap: t['cap'] = plain(cap)
                out.append(({'tbl': t}, plain(cap or '') + ' ' + ' '.join(plain(x) for x in hd) + ' ' + ' '.join(plain(c) for r in rows for c in r)))
            elif k == 'fig':
                out.append(({'fig': {'img': 'img/' + it[1], 'cap': plain(it[2]), 'pg': '', 'sq': False}}, plain(it[2])))
            elif k == 'flow':
                _, cap, steps = it
                out.append(({'viz': {'type': 'flow', 'title': plain(cap or ''), 'steps': [[plain(a), plain(b)] if b else [plain(a)] for a, b in steps], 'per_row': 3}}, plain(cap or '') + ' ' + ' '.join(a for a, b in steps)))
            elif k == 'lanes':
                _, cap, lanes = it
                for hd, st in lanes:
                    out.append(({'viz': {'type': 'flow', 'title': plain(hd), 'steps': [[plain(a), plain(b)] if b else [plain(a)] for a, b in st], 'per_row': 3}}, plain(hd)))
        if is_lens and lens_note(ch):
            ln = lens_note(ch)
            out.append(({'call': {'kind': 'note', 'tag': 'PYQ sheets', 'body': [h(x) for x in ln]}}, 'PYQ sheets'))
    return out

def place(notes, visuals):
    last = {}
    for v in visuals:
        a = v.get('after')
        if v.get('pos') == 'top' or not a: continue
        idx = None
        for i, (n, t) in enumerate(notes):
            if a in t: idx = i; break
        if idx is None: raise SystemExit('ANCHOR NOT FOUND: %r' % a)
        idx = max(idx, last.get(a, -1))
        vv = {k: x for k, x in v.items() if k != 'after'}
        notes.insert(idx + 1, ({'viz': vv}, ''))
        last[a] = idx + 1
    return notes

def lens_of(ch):
    for s in ch.secs:
        if s['title'].startswith('Exam lens'):
            for it in s['items']:
                if it[0] == 'call' and it[1] == 'key':
                    P = M = C = None
                    for b in it[3]:
                        m = re.match(r'\*\*(Prelims hooks|Mains hooks|Closing idea):\*\*\s*(.*)$', b, re.S)
                        if not m: continue
                        txt = m.group(2).rstrip('.')
                        if m.group(1) == 'Prelims hooks': P = [x.strip() for x in re.split(r';\s*', txt) if x.strip()]
                        elif m.group(1) == 'Mains hooks': M = [x.strip() for x in re.split(r';\s*', txt) if x.strip()]
                        else: C = txt + '.'
                    if P and M and C: return {'prelims': [h(x) for x in P], 'mains': [h(x) for x in M], 'close': h(C)}
    raise SystemExit('no lens for ch%d' % ch.n)

def pyq_block(ch):
    pre, mn = chapter_pyqs(ch)
    if not pre and not mn: return None
    secs = _secs_for(ch)
    chtext = _norm(' '.join(' '.join(s['plain']) for s in ch.secs))
    groups = []
    for g in sorted(set(r['sec'] for r in pre) | set(m['sec'] for m in mn)):
        title = plain(secs.get(g, ('', str(g)))[1])
        p = sorted([r for r in pre if r['sec'] == g], key=lambda r: r['year'] or '0', reverse=True)
        m = sorted([x for x in mn if x['sec'] == g], key=lambda x: x['year'], reverse=True)
        pl = []
        for r in p:
            pl.append({'year': r['year'] or 'year not stated', 'blocks': _blocks(r['stem']), 'opts': [r['opts'][k] for k in 'abcd' if k in r['opts']],
                       'ans': r['ans'], 'anstext': r['opts'].get(r['ans'], '')})
        ml = [{'year': x['year'], 'marks': x['marks'], 'topic': x['topic'], 'q': x['q'], 'chips': mains_html(x, chtext)[1]} for x in m]
        groups.append({'title': title, 'count': '%d Prelims · %d Mains' % (len(p), len(m)), 'prelims': pl, 'mains': ml})
    return {'intro': '%d Prelims and %d Mains questions from the Saarthi subject-wise sheets' % (len(pre), len(mn)), 'groups': groups}

def priority(ch):
    pre, mn = chapter_pyqs(ch); t = len(pre) + len(mn)
    return 'H' if t >= 15 else ('M' if t >= 6 else 'L')

REPO = '/home/claude/adityak-study-shelf'
def ca_items(n):
    cwd = os.getcwd(); os.chdir(REPO); sys.path.insert(0, os.path.join(REPO, 'tools'))
    try:
        import ca_integrate as ci
        out = []
        for code in ('sep26', 'oct26'):
            m = ci.load_month(code)
            for it in m['items']:
                if 'eco' in it['nb'] and ('eco-ch%02d' % n) in it['ch']: out.append((m['label'], it))
        return out
    finally: os.chdir(cwd)

def chapter(ch):
    L = LAYERS[str(ch.n)]
    pre, mn = chapter_pyqs(ch)
    notes = sec_notes(ch)
    vis = L['visuals']
    notes = [n for n, t in place(notes, vis)]
    # mind map (same data as the shelf Chapter map) goes first
    top = []
    if ch.mm:
        root, br = ch.mm
        top.append({'type': 'mindmap', 'pos': 'top', 'title': 'Chapter map', 'center': root,
                    'branches': [{'t': b, 'c': [(l + ' (' + n + ')') if n else l for l, n in leaves]} for b, leaves in br]})
    # tail: timeline, connections, mains skeletons
    cai = ca_items(ch.n)
    if cai:
        notes.append({'h': 'Current affairs'})
        for lab, it in cai:
            body = ['<b>' + h(lab) + ' · ' + {'P': 'Prelims', 'M': 'Mains', 'PM': 'Prelims + Mains'}[it['tag']] + '.</b> ' + h(it['ctx'])]
            body += ['• ' + h(x) for x in it['pts']]
            if it.get('kw'): body.append('<b>Keywords:</b> ' + h(it['kw']))
            notes.append({'call': {'kind': 'teacher', 'tag': plain(it['t']), 'body': body}})
    if ch.timeline:
        notes.append({'h': 'Timeline and numbers'})
        notes.append({'tbl': {'head': ['When', 'What'], 'rows': [[h(a), h(b) + (' ★' if s else '')] for a, b, s in ch.timeline]}})
    if ch.connects:
        notes.append({'h': 'Connects to other chapters'})
        notes.append({'tbl': {'head': ['Where', 'Why'], 'rows': [[h(a), h(b)] for a, b in ch.connects]}})
    if ch.mains:
        notes.append({'h': 'Mains answer skeletons'})
        for q, intro, pts, close in ch.mains:
            notes.append({'call': {'kind': 'key', 'tag': plain(q), 'body': ['<b>Intro:</b> ' + h(intro)] + ['• ' + h(x) for x in pts] + ['<b>Close:</b> ' + h(close)]}})
    cards = list(ch.cards)
    step = max(1, len(cards) // 16)
    recall = [[plain(q), plain(a)] for q, a in cards[::step][:14]]
    quiz = [{'q': plain(q['q']), 'o': [plain(o) for o in q['options']], 'a': q['answer']} for q in ch.mcq[:8]]
    pr = priority(ch)
    py = sorted({r['year'] for r in pre if r['year']}); my = sorted({x['year'] for x in mn})
    c = {'id': ch.n, 'title': ch.title, 'pages': L.get('pages', ''), 'priority': pr,
         'pyqs': ', '.join(my) if my else 'none in the sheets',
         'prelims_pyqs': ', '.join(py) if py else 'none in the sheets',
         'lens': lens_of(ch), 'simple': L['simple'], 'terms': L['terms'], 'remember': L['remember'],
         'notes': notes, 'recall': recall, 'traps': L['traps'], 'quiz': quiz,
         'visuals': top + [v for v in vis if v.get('pos') == 'top']}
    pb = pyq_block(ch)
    if pb: c['pyq'] = pb
    return c

def export(ids, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    chs = {}
    for n in ids:
        chs[n] = chapter(importlib.import_module('ch%d' % n).c)
    ALLT = {1:'Poverty',2:'Inequality',3:'Unemployment',4:'Basic Concepts of Economics',5:'National Income Accounting',6:'Inflation',7:'Banking and NBFCs',8:'Money and Monetary Policy',9:'Capital Markets',10:'External Sector',11:'GST',12:'Budget and Fiscal Policy',13:'Rural and Climate Finance'}
    parts = []
    for lab, title, ns in PARTS:
        parts.append({'label': lab, 'title': title, 'sub': PSUB[lab], 'chapters': [chs[n] if n in chs else {'id': n, 'title': ALLT[n], 'priority': 'L'} for n in ns]})
    meta = {'title': 'ECONOMY', 'subtitle': 'Poverty, Money, Prices, External Sector and the Budget',
            'cover_top': 'GS FOUNDATION  ·  ECONOMY', 'cover_mid': 'A study companion built from the Sarrthi IAS Economy handouts, with every Prelims and Mains PYQ from the Saarthi subject-wise sheets',
            'cover_foot': 'UPSC Civil Services Examination 2027  ·  Personal Study Edition', 'running_head': 'ECONOMY',
            'imprint': ['<b>Personal Study Edition, 2026</b>', 'Prepared for the UPSC Civil Services Examination 2027 and APPSC Group 1, General Studies Economy.',
                        'Source material: Sarrthi IAS Economy handouts (14 chapters) and the Saarthi subject-wise Prelims and Mains PYQ sheets. The facts printed here are the source documents’ own; no outside facts have been added. Copyright in the source material belongs to Sarrthi IAS and Saarthi IAS.',
                        'The wide margin on every page is left blank on purpose: use it for current affairs, related data and value-addition points.'],
            'legend': '<span class="pri H">High</span> 15 or more PYQs map to the chapter &nbsp; <span class="pri M">Medium</span> 6 to 14 &nbsp; <span class="pri L">Light</span> fewer than 6',
            'back_matter': 'Priority and PYQ index', 'pri': {'L': 'Light'}}
    json.dump({'meta': meta, 'parts': parts}, open(os.path.join(out_dir, 'bookdata.json'), 'w'), ensure_ascii=False, indent=1)
    os.makedirs(os.path.join(out_dir, 'img'), exist_ok=True)
    for f in os.listdir(os.path.join(HERE, 'img')):
        if f.startswith('eco-'): shutil.copy(os.path.join(HERE, 'img', f), os.path.join(out_dir, 'img', f))

if __name__ == '__main__':
    ids = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [6]
    export(ids, sys.argv[1])
    print('exported', ids)
