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
FULL = {int(k): v for k, v in json.load(open(os.path.join(HERE, 'book', 'fullnotes_pol2.json'), encoding='utf8')).items()}
for _id, _c in BOOK.items():
    if int(_id) in FULL: _c['notes'] = FULL[int(_id)]['notes']   # full detailed notes (same content as the handwritten source, uncondensed)

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

# Each visual sits right after the note item it explains (index into the full notes of that chapter)
PLACE = {
 1: {'Issues in the working of UPSC': 20, 'UPSC story in four steps': 50},
 2: {'Consequences of a closed': 21, 'Generalist or specialist': 31, 'Lateral entry at a glance': 48},
 3: {'Service articles': 24, 'AIS: from British': 13, 'AIS debate': 17},
 4: {'Six roles of civil services': 1, 'Bhaskar Ghose': 15, 'Civil services activism': 48},
 5: {'Causes of poor performance': 17, '21st-century challenges': 21},
 6: {'Bureaucracy as a threat': 16, 'Features and paradoxes': 51},
 7: {'8th CPC': 2, 'Right to strike': 21},
 8: {'Nolan principles': 26},
 9: {'Challenges to civil service reform': 6, 'Aarambh': 32, 'Reform challenges and the way out': 14},
 10: {'Three metaphors': 2, 'Objectives of transparency': 10, 'NDSAP 2012': 27},
 11: {'Components of accountability': 1, 'Dimensions of accountability': 7, 'Types of accountability': 37, 'Horizontal, vertical': 28},
 12: {'Sevottam: seven steps': 48, 'ARC-II recommendations': 33, 'Charter to Sevottam': 46, "Citizen's Charter: what it holds": 44},
 13: {'RTI numbers': 32, 'Criteria for a sound': 14, 'How an RTI request': 32, 'RTI 2005: map': 49},
 14: {'CIC numbers': 10, 'Removal without': 13, 'CIC: appointment': 13, 'RTI: problems and cures': 35},
 15: {'Factors behind corruption': 39, 'Psycho-social factors': 21, 'Implications of corruption': 18, 'Causes of corruption': 39, 'Sanction chain': 36},
 16: {'Anti-corruption toolbox': 2, 'Issues with social audit': 52, 'Strengthening social audit': 58, 'Stick, carrot, radical': 31},
 17: {'CBI and CVC in date order': 22, 'CBI and CVC compared': 23, 'Vineet Narain': 20},
 18: {'Lokpal selection committee': 23, 'PM decisions the Lokpal': 37, 'Should the Prime Minister': 34},
 19: {'Where a whistleblower': 2, 'PCA 2018': 17},
}
def _place_for(c, v):
    for t, i in PLACE.get(c['id'], {}).items():
        if v.get('title', '').startswith(t): return i
    return None

def book_notes(c):
    vis = [dict(v) for v in c.get('visuals', []) if v.get('after') or _place_for(c, v) is not None]
    for v in vis:
        v['at'] = _place_for(c, v)
    out, buf = [], []
    def flush():
        if buf: out.append('<ul class="lst">' + ''.join(bul(conv(x)) for x in buf) + '</ul>'); buf.clear()
    def key(it):
        t = it if isinstance(it, str) else (it.get('h') or (it['tbl']['head'][0] if 'tbl' in it else ''))
        return re.sub(r'<[^>]+>', '', t)
    def after(it, i=None):
        k = key(it)
        for v in vis:
            if v.get('done'): continue
            if (v.get('at') is not None and v['at'] == i) or (v.get('at') is None and v.get('after') and v['after'] in k):
                v['done'] = True; flush(); out.append(vis_html(v))
    for i, it in enumerate(c['notes']):
        if isinstance(it, str):
            buf.append(it)
            if any(not v.get('done') and ((v.get('at') is not None and v['at'] == i) or (v.get('at') is None and v.get('after') and v['after'] in key(it))) for v in vis): flush(); after(it, i)
            continue
        flush()
        if 'h' in it: out.append(h3(conv(it['h'])))
        elif 'tbl' in it:
            t = it['tbl']
            out.append(tbl(None, [conv(x) for x in t['head']], [[conv(cc) for cc in r] for r in t['rows']]))
        elif 'alert' in it: out.append(alert('Handout alert', conv(it['alert'])))
        elif 'call' in it:
            cl = it['call']; kd = {'teacher': 'teacher', 'alert': 'alert', 'note': 'note', 'shortcut': 'shortcut', 'quote': 'note'}.get(cl['kind'], 'note')
            out.append(callout(kd, cl['tag'], '\n\n'.join(conv(b) for b in cl['body'])))
        elif 'ca' in it: out.append(callout('source', 'In the news (Saarthi IAS CA; verify dates)', conv(re.sub(r'<span class="tag">.*?</span>', '', it['ca']))))
        elif 'flow' in it:
            fw = it['flow']; out.append(flow(fw['title'], [(conv(s), '') for s in fw['steps']]))
        elif 'timeline' in it: out.append(timeline([(conv(a), conv(b), False) for a, b in it['timeline']]))
        elif 'fig' in it:
            f = it['fig']; k_ = os.path.splitext(os.path.basename(f['img']))[0]
            out.append(fig('img/gov-%s.jpg' % k_, f['cap'], label='Handout figure, %s' % f.get('pg', '')))
        after(it, i)
    flush()
    rest = [v for v in vis if not v.get('done')]
    if rest:
        out.append(h3('Memory visuals for this section'))
        out += [vis_html(v) for v in rest]
    return ''.join(out)

def book_top(c):
    d = PLAIN[str(c['id'])]
    out = callout('note', 'In simple words', '\n'.join('- ' + x for x in d['simple']))
    out += tbl(None, ['Term', 'In plain words'], [['**%s**' % a, b] for a, b in d['terms']])
    top = [v for v in c.get('visuals', []) if v.get('pos') == 'top' and _place_for(c, v) is None]
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


CHS = {1: dict(n=1, title='Constitutionalism, Rule of Law, Separation of Powers and Checks and Balances', sub='Constitutionalism and its features, Dicey and exceptions to legal equality, separation of powers, functional overlap, checks and balances, India-USA-UK comparison', badge='Low · Mains (no PYQ quoted)'),
 2: dict(n=2, title='Critique of the Constitution, Constitutionalism in Practice and Interpretation', sub='Five criticisms and replies, Ambedkar warnings, political-administrative-social culture, methods of interpretation, conventions', badge='Low · Mains (no PYQ quoted)'),
 3: dict(n=3, title='Constitutional Morality and the Living Constitution', sub='Meaning, Ambedkar, Navtej and Sabarimala, the debate, features of a living Constitution and the journey of Article 21', badge='Low · Mains (no PYQ quoted)'),
 4: dict(n=4, title='Union and Its Territory: Small States, Second SRC, Delhi and Ladakh', sub='Linguistic reorganisation, small states, Uttar Pradesh, Second SRC, Delhi statehood, Ladakh statehood and Sixth Schedule', badge='Low · Mains (no PYQ quoted)')}
CH0 = dict(n=0, title='Start Here: GS-2 Polity (Constitution, Union and Its Territory)', sub='What this notebook is and the priority map', badge='Read first')
EXTRA_IDS = {1: range(40, 42), 2: range(42, 44), 3: range(44, 46), 4: range(46, 49)}
SHORT = {40: 'Constitutionalism, Rule of Law', 41: 'Separation, checks', 42: 'Critique, Ambedkar', 43: 'Practice, interpretation', 44: 'Constitutional morality', 45: 'Living Constitution, Art 21', 46: 'Small states, 2nd SRC', 47: 'Delhi statehood', 48: 'Ladakh'}
EXTRA_FOOT = ('Built from the Sarrthi IAS GS-2 Polity handout "Introduction to Constitution, Union and Its Territory". Only the handout\u2019s own facts are used; mnemonics marked \u201cown mnemonic\u201d are mine. The handout quotes no PYQs, so every section is tagged Low by the rule. Items marked \u201cverify\u201d are current-affairs lines to check. Copyright belongs to the teacher; keep this private.')
PRI_FULL = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
def sec_lens(meta):
    yrs = meta['pyq'].split(' · Handout')[0].strip() or 'none quoted in the handout'
    body = '**Priority:** %s. **Mains PYQs quoted:** %s. **Prelims PYQs quoted:** none quoted in the material.' % (PRI_FULL.get(meta['prio'], 'Medium'), conv(yrs))
    return callout('key', 'Exam lens', body)

def auto_mcq(pairs_by_ch, ch_ids):
    allp = [(q, a) for i in ch_ids for q, a in pairs_by_ch[i]]
    mcq = []
    for k, (q, a) in enumerate(allp):
        pool = []
        for _, x in allp:
            if x != a and x not in pool: pool.append(x)
        off = (k * 7 + 3) % len(pool)
        dis = [pool[(off + t * 5) % len(pool)] for t in range(len(pool))]
        d3 = []
        for x in dis:
            if x not in d3: d3.append(x)
            if len(d3) == 3: break
        pos = k % (len(d3) + 1)
        opts = d3[:pos] + [a] + d3[pos:]
        mcq.append({'q': '%s: which is correct?' % conv(q), 'options': [conv(x) for x in opts], 'answer': pos, 'explain': 'From the handout: **%s** → %s.' % (conv(q), conv(a))})
    return mcq

def make_extra(n, prev_ch, next_ch, pills, lede):
    ids = list(EXTRA_IDS[n])
    secs = []
    for i in ids:
        f = FULL[i]; m = f['meta']
        blocks = [sec_lens(m), callout('note', 'In simple words', '- ' + m['simple']), book_notes({'id': i, 'notes': f['notes'], 'visuals': []})]
        secs.append(Sec(m['title'], blocks, label='Handout only · ' + (m['pyq'].split('Handout ')[-1] if 'Handout ' in m['pyq'] else 'Saarthi IAS')))
    pairs = {i: FULL[i]['meta']['recall'] for i in ids}
    cards = [(q, a) for i in ids for q, a in pairs[i]]
    pr = ['<h3>Quick quiz</h3><div class="count" id="score">0 / 0 correct</div><div id="quiz"></div>',
          '<h3>Flashcards</h3><p class="gdesc">Tap the card to flip.</p><div class="deck"><div class="fc" id="fc" tabindex="0" role="button" aria-label="Flashcard, press to flip"></div><div class="count" id="fccount"></div><div class="row"><button class="btn" id="fcprev" type="button">Back</button><button class="btn pri" id="fcnext" type="button">Next</button><button class="btn" id="fcmiss" type="button">Missed it</button><button class="btn" id="fcshuf" type="button">Shuffle</button><button class="btn" id="fconlymiss" type="button">Only missed</button><button class="btn" id="fcall" type="button">All cards</button></div></div>']
    secs.append(Sec('Recall sheet', [recall(['**%s** %s' % (conv(q), conv(a)) for q, a in cards])], sid='recall'))
    secs.append(Sec('Revise', [tbl('Spaced schedule (count from the day you finish the chapter)', ['Day', 'What to do'], REVISE)], sid='revise'))
    secs.append(Sec('Test yourself', pr, sid='practice'))
    rendered, idx = render_sections(secs)
    branches = []
    for i in ids:
        heads = [it['h'] for it in FULL[i]['notes'] if isinstance(it, dict) and it.get('h')]
        seen, leaves = set(), []
        for h in heads:
            hh = re.sub(r'<[^>]+>', ' ', h)
            hh = re.sub(r'\s*PYQ.*$', '', hh).strip().capitalize() if hh.isupper() or 'PYQ' in hh else re.sub(r'\s+', ' ', hh).strip()
            hh = re.sub(r'\s+', ' ', hh)
            hh = re.sub(r'\b(AND|THE|OF|IN|TO|FOR|ON|ARE|VS)\b', lambda m: m.group(1).lower(), hh); hh = hh[:1].upper() + hh[1:]
            if len(hh) < 3: continue
            hh = hh if len(hh) <= 26 else hh[:26].rsplit(' ', 1)[0] + '…'
            if hh.lower() not in seen and len(leaves) < 6: seen.add(hh.lower()); leaves.append((hh, ''))
        branches.append((SHORT[i], leaves))
    svg, outline = mindmap('Chapter %d' % n, branches, 'Chapter %d map' % n)
    toc = [('chapter-map', 'Chapter map')] + idx
    head_html = chead('Polity · GS-2 · Chapter %d' % n, CHS[n]['title'], 'Low priority', pills, lede)
    data = {'mcq': auto_mcq(pairs, ids), 'cards': [{'q': q, 'a': a} for q, a in cards]}
    page = chapter_page(CHS[n], prev_ch, next_ch, rendered, toc, svg, outline, data, head_html, EXTRA_FOOT, 'Polity (GS-2)')
    open(os.path.join(OUT, BASE + 'ch%02d.html' % n), 'w', encoding='utf8').write(page)
    return toc, rendered

def sf(idx, with_map): return ([{'id': 'chapter-map', 't': 'Chapter map'}] if with_map else []) + [{'id': i, 't': t} for i, t in idx if i != 'chapter-map']
def make_start(next_ch):
    s = [Sec('What this notebook is', [p('The Sarrthi IAS GS-2 Polity handout **Introduction to Constitution, Union and Its Territory**, rebuilt as a notebook: **Chapter 1** (constitutionalism, Rule of Law, separation of powers), **Chapter 2** (critique, constitutionalism in practice, interpretation), **Chapter 3** (constitutional morality, living Constitution), **Chapter 4** (Union and its territory: small states, Delhi, Ladakh).'),
        p('Every section opens with an **Exam lens**. The handout quotes **no PYQs**, so by the rule (High = 2 or more, Medium = 1 or partial, Low = none quoted) each section is Low; check your PYQ priority files for topics like constitutional morality and Article 21, which are often asked. Mnemonics marked own mnemonic are mine.')]),
        Sec('Priority map', [tbl('Sections in handout order', ['Section', 'Priority', 'Mains PYQs quoted'], [['%d \u00b7 %s' % (i, FULL[i]['meta']['title']), PRI[FULL[i]['meta']['prio']], 'none quoted in the handout'] for i in range(40, 49)])])]
    rendered, idx = render_sections(s)
    toc = [('chapter-map', 'Chapter map')] + idx
    branches = [(CHS[k]['title'].split(',')[0][:26], [(SHORT[i], '') for i in EXTRA_IDS[k]]) for k in CHS]
    svg, outline = mindmap('Polity GS-2', branches, 'GS-2 Polity map')
    head_html = chead('Polity \u00b7 GS-2 \u00b7 Start here', CH0['title'], '', [('Read first', 'cls'), ('4 chapters, 9 sections', '')], 'How to use the notebook and the priority map.')
    page = chapter_page(CH0, None, next_ch, rendered, toc, svg, outline, {'mcq': [], 'cards': []}, head_html, EXTRA_FOOT, 'Polity (GS-2)')
    open(os.path.join(OUT, BASE + 'ch00.html'), 'w', encoding='utf8').write(page)
    return toc, rendered
c0 = CH0; idx0, r0 = make_start(CHS[1])
ledes = {1: 'What limits government power, how powers are separated and balanced, and where India sits between the USA and the UK.',
 2: 'Five charges against the Constitution and their replies, why culture decides whether constitutionalism lives, and how courts interpret the text.',
 3: 'Constitutional morality against public morality, and the Constitution as a living document through the journey of Article 21.',
 4: 'Linguistic states, the small-states debate, a Second SRC, and the live cases of Delhi and Ladakh.'}
res = {}; prev = c0
order = [1, 2, 3, 4]
for k in order:
    nxt = CHS[k + 1] if k + 1 in CHS else None
    res[k] = make_extra(k, prev, nxt, [('Handout only', 'cls'), ('GS-2 Polity', ''), ('No PYQ quoted', '')], ledes[k]); prev = CHS[k]
chs = [dict(n=0, title=c0['title'], sub=c0['sub'], badge=c0['badge'], slides=False, pending=False, secs=sf(idx0, True))]
for k in order: chs.append(dict(n=k, title=CHS[k]['title'], sub=CHS[k]['sub'], badge=CHS[k]['badge'], slides=False, pending=False, secs=sf(res[k][0], True)))
home = home_page(chs, 'Study notebook for the GS-2 Polity handout: constitutionalism, Rule of Law, separation of powers, constitutional morality, the living Constitution, and Union and its territory (small states, Delhi, Ladakh). Built from the handout only.', EXTRA_FOOT)
open(os.path.join(OUT, BASE + 'home.html'), 'w', encoding='utf8').write(home)
entries = []
for c, rendered in [(c0, r0)] + [(CHS[k], res[k][1]) for k in order]:
    for h in rendered:
        m = re.match(r'<h2 id="([^"]+)">(.*?)<a class="anchor"', h, re.S)
        entries.append({'c': str(c['n']), 'n': c['title'], 'id': m.group(1), 't': strip_tags(m.group(2)), 'x': strip_tags(h)})
open(os.path.join(OUT, BASE + 'search.html'), 'w', encoding='utf8').write(search_page(entries))
json.dump({'id': NB_ID, 'title': NB_TITLE, 'sub': 'Sarrthi IAS GS-2 Polity: constitutionalism, constitutional morality, living Constitution, Union and its territory', 'base': BASE, 'home': 'home.html', 'search': 'search.html', 'chapters': chs}, open(os.path.join(OUT, 'pg2-chapters.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('built', len(entries))
