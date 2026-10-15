# -*- coding: utf-8 -*-
"""Generate the Governance notebook pages. Usage: python3 build.py OUTDIR"""
import sys, os, json, re, html, base64
from lib import *
import lib
sys.path.insert(0, os.path.join(HERE, 'book'))
import viz

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), 'out')
os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)
X = json.load(open(os.path.join(HERE, 'hubdata.json'), encoding='utf8'))
SECS = {s['id']: s for s in X['SECS']}
PRI = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
PYQ = {p['id']: p for p in X['PYQS']}
FOOT = ('Personal study notes built from the Sarrthi IAS GS-2 Governance modules (Module 1: Civil Services, Transparency, Accountability, Citizen’s Charter, RTI; '
        'Module 2: Corruption, Social Audit, CBI, CVC, Lokpal, Whistleblower, PCA). Only the handouts’ own facts are used; no class slides or board notes were supplied. '
        'Copyright belongs to the teacher; keep this private.')

# ---------------------------------------------------------------- helpers
def conv(s):
    s = re.sub(r'<b>(.*?)</b>', r'**\1**', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s)

for k, b64 in X['IMG'].items():
    open(os.path.join(OUT, 'img', 'gov-%s.jpg' % k), 'wb').write(base64.b64decode(b64))

def figs_html(keys):
    out = ''
    for k in keys:
        f = X['FIGDEF'][k]
        out += fig('img/gov-%s.jpg' % k, f['cap'], label='Handout figure, %s' % f['pg'])
    return out

def notes_html(notes):
    out, buf = [], []
    def flush():
        if buf:
            out.append(ul([conv(x) for x in buf])); buf.clear()
    for it in notes:
        if isinstance(it, str):
            buf.append(it); continue
        flush()
        if 'h' in it: out.append(h3(conv(it['h'])))
        elif 'tbl' in it:
            t = it['tbl']
            out.append(tbl(None, [conv(x) for x in t['head']], [[conv(c) for c in r] for r in t['rows']]))
        elif 'alert' in it: out.append(alert('Handout alert', conv(it['alert'])))
        elif 'figs' in it: out.append(figs_html(it['figs']))
    flush()
    return ''.join(out)

def lens_block(s):
    ys = ', '.join('%s%s' % (PYQ[i]['yr'], '*' if PYQ[i].get('partial') else '') for i in s['pyqs'])
    body = '**Priority:** %s. **Mains PYQs quoted:** %s. **Prelims PYQs quoted:** none quoted in the material.' % (PRI[s['pri']], ys or 'none quoted in the material')
    body += '\n\n**Prelims hooks**\n\n' + '\n'.join('- ' + conv(x) for x in s['lens']['prelims'])
    body += '\n\n**Mains hooks**\n\n' + '\n'.join('- ' + conv(x) for x in s['lens']['mains'])
    body += '\n\n' + conv(s['lens']['close'])
    return callout('key', 'Exam lens', body)

PLAIN = json.load(open(os.path.join(HERE, 'plain.json'), encoding='utf8'))

def plain_block(i):
    d = PLAIN[str(i)]
    out = callout('note', 'In simple words', '\n'.join('- ' + x for x in d['simple']))
    out += tbl(None, ['Term', 'In plain words'], [['**%s**' % a, b] for a, b in d['terms']])
    out += callout('shortcut', 'Remember it as', d['remember'])
    return out



# ---------------------------------------------------------------- book edition content (bullets, visuals, mnemonics)
BOOK = {c['id']: c for p_ in json.load(open(os.path.join(HERE, 'book', 'bookdata.json'), encoding='utf8'))['parts'] for c in p_['chapters']}

def split_semi(t):
    parts, cur, dp = [], '', 0
    for ch in t:
        if ch == '(': dp += 1
        elif ch == ')': dp = max(0, dp - 1)
        elif ch == ';' and dp == 0:
            parts.append(cur.strip()); cur = ''; continue
        cur += ch
    if cur.strip(): parts.append(cur.strip())
    out, open_ = [], False
    for x in parts:
        if open_: x = '**' + x
        open_ = x.count('**') % 2 == 1
        if open_: x += '**'
        out.append(x)
    return out

def capf(x):
    x = x.strip().rstrip('.')
    m = re.match(r'^(\**)(.)(.*)$', x, re.S)
    return m.group(1) + m.group(2).upper() + m.group(3) if m else x

def bul(md):
    ps = split_semi(md)
    if len(ps) < 2: return '<li>%s</li>' % inline(md)
    m = re.match(r'^(.{2,70}?:(?:\*\*)?)\s+(.*)$', ps[0], re.S)
    if m:
        lab = m.group(1)
        first = m.group(2)
        if lab.count('**') % 2: lab += '**'; first = '**' + first
        return '<li>%s<ul class="lst subl">%s</ul></li>' % (inline(lab), ''.join('<li>%s</li>' % inline(capf(i)) for i in [first] + ps[1:]))
    return ''.join('<li>%s</li>' % inline(capf(i)) for i in ps)

def vis_html(v):
    return '<div class="vwrap">%s</div>' % viz.render(dict(v))

def book_notes(c):
    vis = [dict(v) for v in c.get('visuals', []) if v.get('after')]
    out, buf = [], []
    def flush():
        if buf: out.append('<ul class="lst">' + ''.join(bul(conv(x)) for x in buf) + '</ul>'); buf.clear()
    def key(it):
        t = it if isinstance(it, str) else (it.get('h') or (it['tbl']['head'][0] if 'tbl' in it else ''))
        return re.sub(r'<[^>]+>', '', t)
    def after(it):
        k = key(it)
        for v in vis:
            if v['after'] in k and not v.get('done'):
                v['done'] = True; flush(); out.append(vis_html(v))
    for it in c['notes']:
        if isinstance(it, str):
            buf.append(it)
            if any(v['after'] in key(it) and not v.get('done') for v in vis): flush(); after(it)
            continue
        flush()
        if 'h' in it: out.append(h3(conv(it['h'])))
        elif 'tbl' in it:
            t = it['tbl']
            out.append(tbl(None, [conv(x) for x in t['head']], [[conv(cc) for cc in r] for r in t['rows']]))
        elif 'alert' in it: out.append(alert('Handout alert', conv(it['alert'])))
        elif 'fig' in it:
            f = it['fig']; k_ = os.path.splitext(os.path.basename(f['img']))[0]
            out.append(fig('img/gov-%s.jpg' % k_, f['cap'], label='Handout figure, %s' % f.get('pg', '')))
        after(it)
    flush()
    for v in vis:
        if not v.get('done'): print('WARN unplaced visual', c['id'], v.get('title'))
    return ''.join(out)

def book_top(c):
    d = PLAIN[str(c['id'])]
    out = callout('note', 'In simple words', '\n'.join('- ' + x for x in d['simple']))
    out += tbl(None, ['Term', 'In plain words'], [['**%s**' % a, b] for a, b in d['terms']])
    top = [v for v in c.get('visuals', []) if v.get('pos') == 'top']
    if not any(v['type'] == 'mnemonic' for v in c.get('visuals', [])):
        out += callout('shortcut', 'Remember it as', d['remember'])
    out += ''.join(vis_html(v) for v in top)
    return out

def section(s):
    c = BOOK[s['id']]
    blocks = [lens_block(s), book_top(c), p(conv(s['story'])), book_notes(c)]
    return Sec(s['title'], blocks, label='Handout only · %s' % s['pages'])

lib.EXTRA_CSS = lib.EXTRA_CSS.replace('</style>', """
.lst li{margin:6px 0}.lst ul.subl{margin:4px 0 6px;padding-left:20px;list-style:none}
.lst ul.subl>li{position:relative;padding-left:14px;margin:3px 0}
.lst ul.subl>li::before{content:"";position:absolute;left:0;top:.62em;width:6px;height:6px;border-radius:50%;background:var(--acc)}
.vwrap{margin:16px 0}
.vwrap .viz{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 12px;overflow-x:auto}
.vwrap .viz svg{min-width:460px;display:block}
.vwrap .vtitle{font:700 13px/1.3 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#1F4E5F;margin:0 0 8px;padding-bottom:6px;border-bottom:1px solid #E2C98A}
.vwrap .mnem{background:var(--acc-soft);border:1px solid var(--line);border-radius:12px;padding:14px 16px;color:var(--ink)}
.vwrap .mlbl{font:700 12px var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--saf);margin-bottom:8px}
.vwrap .tiles{margin:4px 0 8px}
.vwrap .tile{display:inline-block;min-width:38px;padding:6px 6px;margin:0 6px 6px 0;text-align:center;font:700 26px/1 var(--serif);color:var(--acc);background:var(--surface);border:1.5px solid var(--saf);border-radius:8px}
.vwrap .tsep{display:inline-block;font:600 16px var(--sans);color:var(--saf);margin:0 8px 0 2px;vertical-align:middle}
.vwrap .mhook{font:italic 600 17px/1.45 var(--serif);margin:2px 0 10px}
.vwrap .mchips .chip{display:flex;gap:8px;align-items:baseline;font:15px/1.45 var(--sans);padding:3px 0;margin:0;background:none;border:0;border-radius:0;box-shadow:none;color:var(--ink);white-space:normal;height:auto}
.vwrap .mchips .chip i{flex:0 0 44px;font-style:normal;font-weight:700;color:var(--saf)}
.vwrap .msent{font:600 20px/1.4 var(--serif)}.vwrap .msent b{color:var(--saf);font-size:26px}.vwrap .msent .w{margin-right:6px}
.vwrap .mnote{font:13px/1.4 var(--sans);color:var(--muted);margin-top:8px}
@media (max-width:560px){.vwrap .tile{min-width:30px;font-size:21px}}
</style>""")

def first_ref_mod(ref):
    return 2 if ref.strip().startswith('M2') else 1

def ch_of_secs(secs):
    return 1 if (not secs or min(secs) <= 14) else 2

END = {int(k): v for k, v in X['ENDMAP'].items()}
XC = {int(k): v for k, v in X['XCARDS'].items()}
XQ = {int(k): v for k, v in X['XMCQ'].items()}
rng = {1: range(1, 15), 2: range(15, 20)}

def chapter_items(n):
    cards, mcq, traps = [], [], []
    for sid in rng[n]:
        m = END.get(sid, {'c': [], 't': [], 'q': []})
        cards += [X['CARDS'][i] for i in m['c']] + XC.get(sid, [])
        mcq += [X['MCQ'][i] for i in m['q']] + XQ.get(sid, [])
        traps += [X['TRAPS'][i] for i in m['t']]
    return cards, mcq, traps

def skeleton(title, sk, partial=None):
    intro = sk['i']
    body = [conv(x) for x in sk['b']]
    closing = '**Close.** ' + conv(sk['c'])
    if partial: closing += ' (' + partial + ')'
    return (title, conv(intro), body, closing)

def secname(i): return '%d. %s' % (i, SECS[i]['title'])

REVISE = [['Day 0', 'Read the Exam lens and the notes; mark the chapter done'], ['Day +1', 'Recall sheet: read once, hide, rebuild'],
          ['Day +3', 'Flashcards: missed ones only'], ['Day +7', 'Quick quiz; fix each miss against the Traps'],
          ['Day +21', 'Write two Mains answers from memory using the skeletons'], ['Day +45', 'Blank-page test (prompts in Start Here)']]

def tail(n):
    out = []
    cards, mcq, traps = chapter_items(n)
    tl = sorted([t for t in X['TL'] if first_ref_mod(t['ref']) == n], key=lambda t: (t['t'], 0))
    out.append(Sec('Timeline', [timeline([(t['y'], conv(t['e']) + ' (%s)' % t['ref'], False) for t in tl])], sid='chapter-timeline'))
    cmp_ = [c for c in X['CMP'] if (2 if 'M2' in c['src'] else 1) == n]
    if cmp_:
        out.append(Sec('Side by side', [tbl('%s (%s)' % (conv(c['t']), c['src']), [conv(x) or ' ' for x in c['h']], [[conv(x) for x in r] for r in c['r']]) for c in cmp_], sid='side-by-side'))
    fl = [f for f in X['FLOWS'] if ch_of_secs([int(x) for x in re.findall(r'\d+', f['n'])][:1]) == n]
    if fl:
        out.append(Sec('Flow charts', [flow('%s (%s)' % (conv(f['t']), f['n']), [(conv(s), '') for s in f['s']]) for f in fl], sid='flows'))
    if traps:
        out.append(Sec('Traps', [tbl('Common mix-ups and the rule for the exam hall', ['Trap', 'What goes wrong, and the rule'],
                   [['**%s**' % conv(t['t']), conv(t['d']) + ' ' + conv(t['r'])] for t in traps])], sid='traps'))
    lk = [l for l in X['LINKS'] if ch_of_secs([l[0]]) == n]
    out.append(Sec('Connects to', [links([('§%d %s → §%d %s' % (a, SECS[a]['title'], b, SECS[b]['title']), conv(t)) for a, b, t in lk])], sid='connects'))
    out.append(Sec('Recall sheet', [recall(['**%s** %s' % (conv(q), conv(a)) for q, a in cards])], sid='recall'))
    out.append(Sec('Revise', [tbl('Spaced schedule (count from the day you finish the chapter)', ['Day', 'What to do'], REVISE)], sid='revise'))
    pr = ['<h3>Quick quiz</h3><div class="count" id="score">0 / 0 correct</div><div id="quiz"></div>',
          '<h3>Flashcards</h3><p class="gdesc">Tap the card to flip.</p><div class="deck"><div class="fc" id="fc" tabindex="0" role="button" aria-label="Flashcard, press to flip"></div><div class="count" id="fccount"></div><div class="row"><button class="btn" id="fcprev" type="button">Back</button><button class="btn pri" id="fcnext" type="button">Next</button><button class="btn" id="fcmiss" type="button">Missed it</button><button class="btn" id="fcshuf" type="button">Shuffle</button><button class="btn" id="fconlymiss" type="button">Only missed</button><button class="btn" id="fcall" type="button">All cards</button></div></div>',
          '<h3>Mains answer skeletons</h3><p class="gdesc">One for each Mains PYQ quoted in the material that the notes can support, then practice questions. Tap to open; try the answer first.</p>']
    for pq in sorted(X['PYQS'], key=lambda p: -p['yr']):
        if pq['sk'] and ch_of_secs(pq['secs']) == n:
            t = '%s · %s marks · %s' % (pq['yr'], pq['mk'], conv(pq['q'])[:110] + ('…' if len(pq['q']) > 110 else ''))
            title, intro, body, closing = skeleton(t, pq['sk'], pq.get('partial'))
            pr.append(details(title, p('**Question.** ' + conv(pq['q'])) + p(intro) + ul(body) + p(closing)))
    for mq in X['MAINSQ']:
        if ch_of_secs(mq['secs']) == n:
            title, intro, body, closing = skeleton('Practice · ' + conv(mq['q']), mq['sk'])
            pr.append(details(title, p(intro) + ul(body) + p(closing)))
    out.append(Sec('Test yourself', pr, sid='practice'))
    data = {'mcq': [{'q': q['q'], 'options': q['o'], 'answer': q['a'], 'explain': q['e']} for q in mcq],
            'cards': [{'q': q, 'a': a} for q, a in cards]}
    return out, data

def mapdata(branches):
    res = []
    for b in branches:
        leaves = []
        for c in b['c']:
            if ': ' in c: t, nn = c.split(': ', 1)
            else: t, nn = c, ''
            leaves.append((t, nn))
        res.append((b['t'], leaves))
    return res

CHS = {
 1: dict(n=1, title='Civil Services, Transparency, Accountability, Citizen’s Charter and RTI',
         sub='Module 1: PSCs, lateral entry, AIS, roles, bureaucracy, pay, reforms, Karmayogi, transparency, accountability, charters, RTI Act and CIC', badge='High · Mains'),
 2: dict(n=2, title='Corruption, Social Audit, CBI, CVC, Lokpal, Whistleblowers and PCA',
         sub='Module 2: types and causes of corruption, social audit, CBI and CVC, Lokpal, Whistleblowers Act, Prevention of Corruption Act', badge='High · Mains'),
}
CH0 = dict(n=0, title='Start Here: How to Use This Notebook',
           sub='What the notebook is, the priority and PYQ map, the mind map, numbers to know, blank-page prompts', badge='Read first')

def make_chapter(n, prev_ch, next_ch, pills, lede):
    secs = [section(SECS[i]) for i in rng[n]]
    tl, data = tail(n)
    secs += tl
    rendered, idx = render_sections(secs)
    br = X['MAP']['branches'][:6] if n == 1 else X['MAP']['branches'][6:]
    svg, outline = mindmap('Module %d' % n, mapdata(br), 'Module %d map' % n)
    toc = [('chapter-map', 'Chapter map')] + idx
    head_html = chead('Governance · GS-2 · Chapter %d' % n, CHS[n]['title'], 'High priority', pills, lede)
    page = chapter_page(CHS[n], prev_ch, next_ch, rendered, toc, svg, outline, data, head_html, FOOT, 'Governance')
    open(os.path.join(OUT, 'gov-ch%02d.html' % n), 'w', encoding='utf8').write(page)
    return toc, rendered

def make_start(next_ch):
    s = []
    s.append(Sec('What this notebook is', [
        p('Two Sarrthi IAS GS-2 Governance modules, rebuilt as one notebook you can read on the tablet: **Chapter 1** covers Module 1 (sections 1-14, civil services to RTI) and **Chapter 2** covers Module 2 (sections 15-19, corruption to the Prevention of Corruption Act).'),
        p('Every section opens with an **Exam lens** (priority, PYQs quoted, Prelims and Mains hooks). Page references such as M1 p.5 are the printed page numbers of each module. Only facts printed in the handouts are used. **No class slides or teacher board notes were supplied**, so there is no teacher-ink forecast; priority comes from where the handouts quote PYQs.'),
        alert('Source conflict', 'Module 1 says India appointed a central ombudsman in 2013; Module 2 says the Lokpal was constituted in 2019. The notes use “Act 2013, constituted 2019”.'),
        note('Counts', '**19 Mains PYQ entries quoted (2013-2024) and no Prelims PYQ.** Priority rule: High = 2 or more PYQs map to the section; Medium = 1 PYQ or a partial fit (*); Low = none quoted.'),
    ]))
    s.append(Sec('Priority and PYQ map for all 19 sections', [tbl('Sections in handout order', ['Section', 'Pages', 'Priority', 'Mains PYQs quoted'],
        [['%d · %s' % (i, SECS[i]['title']), SECS[i]['pages'], PRI[SECS[i]['pri']],
          ', '.join('%s%s' % (PYQ[q]['yr'], '*' if PYQ[q].get('partial') else '') for q in SECS[i]['pyqs']) or 'none quoted in the material'] for i in range(1, 20)])]))
    s.append(Sec('All 19 Mains PYQs', [tbl('Quoted in the modules', ['Year', 'Marks', 'Question', 'Covered in'],
        [[str(q['yr']), conv(q['mk']), conv(q['q']), ', '.join(secname(i) for i in q['secs']) or 'no matching section in these modules'] for q in sorted(X['PYQS'], key=lambda q: (-q['yr'], q['id']))])]))
    s.append(Sec('Numbers to know', [recall(['**%s** %s' % (a, conv(b)) for a, b in X['RECALL']])], sid='numbers'))
    s.append(Sec('Chains to remember', [tbl(None, ['Topic', 'Chain'], [['**%s**' % a, conv(b)] for a, b in X['TL_ORDER']])], sid='chains'))
    s.append(Sec('Blank-page prompts', [ul(X['PROMPTS'])], sid='prompts'))
    s.append(Sec('Limits of the material', [ul([conv(X['TRAPS'][19]['d']) + ' ' + conv(X['TRAPS'][19]['r']), conv(X['TRAPS'][20]['d']) + ' ' + conv(X['TRAPS'][20]['r'])])], sid='limits'))
    rendered, idx = render_sections(s)
    svg, outline = mindmap(X['MAP']['root'], mapdata(X['MAP']['branches']), 'GS-2 Governance map')
    toc = [('chapter-map', 'Chapter map')] + idx
    lede = 'How to use the notebook, the priority and PYQ map across all 19 sections, and the numbers and chains to keep in your head.'
    head_html = chead('Governance · GS-2 · Start here', CH0['title'], '', [('Read first', 'cls'), ('2 chapters, 19 sections', ''), ('No class slides supplied', '')], lede)
    page = chapter_page(CH0, None, next_ch, rendered, toc, svg, outline, {'mcq': [], 'cards': []}, head_html, FOOT, 'Governance')
    open(os.path.join(OUT, 'gov-ch00.html'), 'w', encoding='utf8').write(page)
    return toc, rendered

c0, c1, c2 = CH0, CHS[1], CHS[2]
idx0, r0 = make_start(c1)
idx1, r1 = make_chapter(1, c0, c2, [('Handout only', 'cls'), ('Module 1 · pp. 3-38', ''), ('Mains PYQs 2013-2024 · no Prelims', ''), ('6 handout figures', '')],
    'From the Public Service Commissions to the Right to Information: who the civil servants are, the six roles they play, how bureaucracy relates to democracy and development, pay and reform, and the transparency and accountability tools, ending with the RTI Act and its Commissions.')
idx2, r2 = make_chapter(2, c1, None, [('Handout only', 'cls'), ('Module 2 · pp. 3-20', ''), ('Mains PYQs 2014-2024 · no Prelims', '')],
    'What corruption is and how it is produced, social audit and the other checks, then the machinery: CBI, CVC, Lokpal, the Whistle Blowers Protection Act and the Prevention of Corruption Act 1988 as amended in 2018.')

def sf(idx, with_map): return ([{'id': 'chapter-map', 't': 'Chapter map'}] if with_map else []) + [{'id': i, 't': t} for i, t in idx if i != 'chapter-map']
chs = [dict(n=0, title=c0['title'], sub=c0['sub'], badge=c0['badge'], slides=False, pending=False, secs=sf(idx0, True)),
       dict(n=1, title=c1['title'], sub=c1['sub'], badge=c1['badge'], slides=False, pending=False, secs=sf(idx1, True)),
       dict(n=2, title=c2['title'], sub=c2['sub'], badge=c2['badge'], slides=False, pending=False, secs=sf(idx2, True))]
home = home_page(chs, 'Study notebook for the two GS-2 Governance modules: civil services, transparency, accountability, Citizen’s Charter and RTI, then corruption, social audit, CBI, CVC, Lokpal, whistleblowers and the Prevention of Corruption Act. Built from the handouts only.', FOOT)
open(os.path.join(OUT, 'gov-home.html'), 'w', encoding='utf8').write(home)
entries = []
for c, rendered in ((c0, r0), (c1, r1), (c2, r2)):
    for h in rendered:
        m = re.match(r'<h2 id="([^"]+)">(.*?)<a class="anchor"', h, re.S)
        entries.append({'c': str(c['n']), 'n': c['title'], 'id': m.group(1), 't': strip_tags(m.group(2)), 'x': strip_tags(h)})
open(os.path.join(OUT, 'gov-search.html'), 'w', encoding='utf8').write(search_page(entries))
json.dump({'id': NB_ID, 'title': NB_TITLE, 'sub': 'Sarrthi IAS GS-2 Governance modules: civil services, RTI, corruption, Lokpal', 'base': BASE,
           'home': 'home.html', 'search': 'search.html', 'chapters': chs}, open(os.path.join(OUT, 'gov-chapters.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('built', len(entries), 'search entries;', {c['n']: len(c['secs']) for c in chs})
