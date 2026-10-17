# -*- coding: utf-8 -*-
"""GS Paper III notebook for the Study Shelf. Source: bookdata.json (same content as the printed textbook).
Rebuild: python3 src-gs3/build.py OUTDIR ; then copy gs3-*.html to the repo root and run the registry step (library.json, sw.js)."""
import sys, os, json, re, html
MY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(MY, '..', 'src-gov')); sys.path.insert(0, MY)
import lib
from lib import *
lib.NB_ID = 'gs3'; lib.BASE = 'gs3-'; lib.NB_TITLE = 'GS Paper III'
import viz
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(MY, '..', 'out')
os.makedirs(OUT, exist_ok=True)
B = json.load(open(os.path.join(MY, 'bookdata.json'), encoding='utf8'))
PRI = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
FOOT = 'Personal study notes built from the Sarrthi IAS MMP+ GS-3 handouts, class slides and PYQ sets. Boxes marked "verify" carry current affairs to re-check before quoting. Copyright belongs to the teacher; keep this private.'

def conv(s):
    s = re.sub(r'<b>(.*?)</b>', r'**\1**', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s).replace('&amp;', '&')

def rows(c): return [[conv(x) for x in r] for r in c]

def render_item(it, vis, key_after):
    if 'h' in it: return h3(conv(it['h']))
    if 'tbl' in it:
        t = it['tbl']; return tbl(None, [conv(x) for x in t['head']], rows(t['rows']))
    if 'ca' in it: return callout('example', 'Current affairs', conv(it['ca']))
    if 'alert' in it: return alert('Alert', conv(it['alert']))
    if 'call' in it:
        c = it['call']; body = '\n\n'.join(conv(x) for x in c['body']); tag = c['tag']
        if tag.startswith('Memory aid · '):
            word = tag.split(' · ', 1)[1]
            return mnemo('Memory aid', [ch for ch in word if ch.isalnum()], body)
        return callout({'quote': 'teacher', 'teacher': 'teacher', 'note': 'note'}.get(c['kind'], 'note'), tag, body)
    return ''

def bullets(buf):
    items = []
    for x in buf:
        x = conv(x)
        items.append('> ' + x[2:] if x.startswith('› ') else x)
    return ul(items)

ACR = {'ML','PMLA','FATF','LWE','NIA','UAPA','CAPF','MSP','PDS','DPDP','AFSPA','ARC','II','III','IV','FRA','PESA','PYQ','NSC','NSA','CIBMS','TBML','DM','UN','UNODC','ICG','BADP','VVP','BIM','FCRA','NDPS','NCB','CDS','CBI','CVC','SPG','NSAB','JIC','VDA','AI','EU','LAC','IMSS','NATGRID','MLAT','MLATS','NE','J&K','NPA','EOD','KYC','STR','SEEPS','SAMADHAN','NAXALISM','STAR','TURF','PLEDGES','DFMANC','CITE','PLI'}
SMALL = {'AND','OF','IN','THE','TO','FOR','A','AN','ON','VS','OR'}
def nice(t):
    out = []
    for i, w in enumerate(t.split()):
        core = re.sub(r'[^A-Za-z0-9&]', '', w).upper()
        if core in ACR or any(ch.isdigit() for ch in w) and w.isupper() and len(core) <= 5 and not core.isdigit():
            out.append(w)
        elif core in SMALL and i: out.append(w.lower())
        else: out.append('-'.join(x[:1].upper() + x[1:].lower() for x in w.split('-')))
    return ' '.join(out)

def split_sections(c):
    """notes -> [(title, [html blocks])]; a new section starts at an all-capitals heading."""
    secs, cur_t, blocks, buf = [], 'Overview', [], []
    vis = [dict(v) for v in c.get('visuals', []) if v.get('after')]
    def flush():
        nonlocal buf
        if buf: blocks.append(bullets(buf)); buf = []
    def place(text):
        for v in vis:
            if v['after'] in text and not v.get('done'):
                v['done'] = True; flush(); blocks.append('<div class="vwrap">%s</div>' % viz.render(dict(v)))
    for it in c['notes']:
        if isinstance(it, str):
            buf.append(it); place(re.sub(r'<[^>]+>', '', it)); continue
        flush()
        if 'h' in it:
            t = conv(it['h'])
            if it.get('sec'):
                if blocks: secs.append((cur_t, blocks))
                pq = re.findall(r'PYQ [^P]*?(?= PYQ|$)', t)
                base = t.split(' PYQ')[0].strip()
                cur_t = nice(base) if re.sub(r'\(.*?\)', '', base).isupper() else base
                blocks = []
                if ' PYQ' in t: blocks.append(note('PYQs', ' · '.join(x.strip() for x in re.findall(r'PYQ [^P]+', t))))
                place(t)
                continue
        blocks.append(render_item(it, vis, None))
        place(conv(it['h']) if 'h' in it else (conv(it['tbl']['head'][0]) if 'tbl' in it else ''))
    flush()
    if blocks: secs.append((cur_t, blocks))
    for v in vis:
        if not v.get('done'): print('WARN unplaced visual', c['id'], v.get('title'))
    return secs

def top_blocks(c):
    out = callout('note', 'In simple words', '\n'.join('- ' + conv(x) for x in c['simple']))
    if c['terms']:
        out += tbl(None, ['Key term', 'In plain words'], [['**%s**' % a, b] for a, b in c['terms']])
    top = [v for v in c.get('visuals', []) if v.get('pos') == 'top']
    out += ''.join('<div class="vwrap">%s</div>' % viz.render(dict(v)) for v in top)
    if c.get('remember') and not any(v.get('type') == 'mnemonic' for v in c.get('visuals', [])):
        out += callout('shortcut', 'Remember it as', c['remember'])
    return out

def bank_blocks(c):
    b = c.get('bank'); out = []
    if not b: return out
    if b.get('data'): out.append(tbl('Data to quote', ['Indicator', 'Figure'], rows(b['data'])))
    if b.get('quotes'): out.append(tbl('Quotes', ['Quote', 'By', 'Use in'], rows(b['quotes'])))
    if b.get('keywords'): out.append(ul([conv(k[0]) for k in b['keywords']]))
    if b.get('cases'): out.append(h3('Case studies') + ul(b['cases']))
    if b.get('reports'): out.append(h3('Reports and judgments') + ul(b['reports']))
    if b.get('lines'): out.append(h3('Intro and conclusion lines') + ul(['**%s** %s' % (a, conv(t)) for a, t in b['lines']]))
    return out

def mains_blocks(c):
    m = c.get('mains')
    if not m: return []
    out = []
    if m.get('asked'): out.append(tbl('Mains PYQs and where the answer lives', ['Year · marks', 'Question', 'Use'], rows(m['asked'])))
    if m.get('trend'): out.append(note('Trend', conv(m['trend'])))
    return out

chapters = [c for p in B['parts'] for c in p['chapters']]
part_of = {c['id']: p['title'] for p in B['parts'] for c in p['chapters']}
N = len(chapters)
CH0 = dict(n=0, title='Start Here: How to Use This Notebook')
metas = [dict(n=c['id'], title=c['title']) for c in chapters]

def make_chapter(i, c):
    prev_ch = CH0 if i == 0 else metas[i - 1]
    next_ch = metas[i + 1] if i + 1 < N else None
    secs = [Sec('Start here: simple words and key terms', [top_blocks(c)])]
    if mains_blocks(c): secs.append(Sec('Mains PYQs', mains_blocks(c)))
    for t, bl in split_sections(c): secs.append(Sec(t, bl))
    if bank_blocks(c): secs.append(Sec('Answer bank', bank_blocks(c)))
    cards = [{'q': conv(q), 'a': conv(a)} for q, a in c.get('recall', [])]
    if cards: secs.append(Sec('Recall sheet', [recall(['**%s** %s' % (x['q'], x['a']) for x in cards])], sid='recall'))
    rendered, idx = render_sections(secs)
    quiz = [{'q': q['q'], 'options': q['o'], 'answer': q['a'], 'explain': q.get('e', '')} for q in c.get('quiz', []) if isinstance(q, dict) and 'o' in q]
    data = {'mcq': quiz, 'cards': cards}
    pills = [('Handout + slides', 'cls'), (c.get('pages', ''), ''), ('PYQ: ' + (c.get('pyqs') or 'none quoted'), '')]
    head_html = chead('%s · Chapter %d' % (part_of[c['id']], c['id']), c['title'], PRI[c['priority']] + ' priority', [x for x in pills if x[0]], conv(c['simple'][0]) if c['simple'] else '')
    page = chapter_page(dict(n=c['id'], title=c['title']), prev_ch, next_ch, rendered, idx, None, '', data, head_html, FOOT, 'GS Paper III')
    open(os.path.join(OUT, 'gs3-ch%02d.html' % c['id']), 'w', encoding='utf8').write(page)
    return idx, rendered

def make_start():
    mn_rows = []
    for c in chapters:
        for it in c['notes']:
            if isinstance(it, dict) and 'call' in it and it['call']['tag'].startswith('Memory aid · '):
                mn_rows.append(['**%s**' % it['call']['tag'].split(' · ', 1)[1], c['title'], conv(it['call']['body'][0])[:140]])
        for v in c.get('visuals', []):
            if v.get('type') == 'mnemonic' and v.get('word'):
                mn_rows.append(['**%s**' % v['word'], c['title'], conv(v.get('hook', ''))[:140]])
    s = [Sec('What this notebook is', [
        p('One book for **GS Paper III** (Agriculture, Disaster Management, Internal Security), the same content as the printed textbook, built from the Sarrthi IAS MMP+ handouts, class slides and PYQ sets.'),
        p('Each chapter opens with **simple words and key terms**, then the notes (tables, mnemonics, current-affairs boxes), then a **recall sheet**. Faculty mnemonics are kept exactly as taught (MONEY LAUNDER, BLACK, P-M-L-A, NAXALISM, SAMADHAN and others); the rest are marked as memory aids.'),
        alert('Limits of the material', 'No Economy, Environment or Science and Technology source was supplied. Disaster Management static slides were handwritten and read by OCR, so only legible facts are used. Items marked "verify" are current affairs to re-check before quoting.')]),
        Sec('Priority and PYQ map', [tbl('All chapters', ['Chapter', 'Part', 'Priority', 'PYQs quoted'], [['%d · %s' % (c['id'], c['title']), part_of[c['id']], PRI[c['priority']], c.get('pyqs') or 'none quoted'] for c in chapters])]),
        Sec('Mnemonics', [tbl('Quick sheet', ['Word', 'Chapter', 'Meaning'], mn_rows)], sid='mnemonics')]
    rendered, idx = render_sections(s)
    head_html = chead('GS Paper III · Start here', CH0['title'], '', [('Read first', 'cls'), ('%d chapters' % N, '')], 'How to use the notebook, the priority and PYQ map for every chapter, and the mnemonic sheet.')
    page = chapter_page(CH0, None, metas[0], rendered, idx, None, '', {'mcq': [], 'cards': []}, head_html, FOOT, 'GS Paper III')
    open(os.path.join(OUT, 'gs3-ch00.html'), 'w', encoding='utf8').write(page)
    return idx, rendered

idx0, r0 = make_start()
allr = [(CH0, r0)]
chs = [dict(n=0, title=CH0['title'], sub='Priority map and mnemonic sheet', badge='Read first', slides=False, pending=False, secs=[{'id': i, 't': t} for i, t in idx0])]
for i, c in enumerate(chapters):
    idx, r = make_chapter(i, c)
    allr.append((dict(n=c['id'], title=c['title']), r))
    chs.append(dict(n=c['id'], title=c['title'], sub=c['simple'][0].replace('**', '')[:140] if c['simple'] else '', badge=part_of[c['id']] + ' · ' + PRI[c['priority']], slides=False, pending=False, secs=[{'id': a, 't': b} for a, b in idx]))

def fix(s):
    return (s.replace('Governance notebook', 'GS Paper III notebook').replace('<h1>Governance</h1>', '<h1>GS Paper III</h1>')
             .replace('Sarrthi IAS · GS Mains Modules · GS-2', 'Sarrthi IAS · GS Mains · GS-3').replace('Governance Contents', 'GS Paper III Contents')
             .replace('Chapters so far', 'Chapters').replace('Search Governance', 'Search GS Paper III')
             .replace('Chapter 1</a>', 'Chapter 1</a>'))
home = home_page(chs, 'GS Paper III in one notebook: Agriculture, Disaster Management and Internal Security (security, borders, terrorism, cyber, money laundering, defence), with current-affairs boxes, mnemonics and recall sheets.', FOOT)
open(os.path.join(OUT, 'gs3-home.html'), 'w', encoding='utf8').write(fix(home))
entries = []
for c, rendered in allr:
    for h in rendered:
        m = re.match(r'<h2 id="([^"]+)">(.*?)<a class="anchor"', h, re.S)
        entries.append({'c': str(c['n']), 'n': c['title'], 'id': m.group(1), 't': strip_tags(m.group(2)), 'x': strip_tags(h)})
open(os.path.join(OUT, 'gs3-search.html'), 'w', encoding='utf8').write(fix(search_page(entries)).replace('e.g. Lokpal, Vineet Narain, Sevottam, Section 8', 'e.g. PMLA, FATF, Naxalism, Agnipath'))
json.dump({'id': 'gs3', 'title': 'GS Paper III (Mains)', 'sub': 'Agriculture, Disaster Management, Internal Security: notes, mnemonics and recall sheets', 'base': 'gs3-', 'home': 'home.html', 'search': 'search.html', 'chapters': chs}, open(os.path.join(OUT, 'gs3-chapters.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('built', len(entries), 'search entries;', N, 'chapters')
