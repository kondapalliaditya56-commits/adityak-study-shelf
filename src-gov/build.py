# -*- coding: utf-8 -*-
"""Generate the Governance notebook pages. Usage: python3 build.py OUTDIR"""
import sys, os, json, re, html, base64
from lib import *

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

def section(s):
    blocks = [lens_block(s), p(conv(s['story'])), notes_html(s['notes'])]
    return Sec(s['title'], blocks, label='Handout only · %s' % s['pages'])

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
