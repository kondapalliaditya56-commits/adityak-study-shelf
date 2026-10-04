# -*- coding: utf-8 -*-
"""Generate the International Relations notebook pages.
Usage: python3 build.py OUTDIR
Writes ir-ch00.html, ir-ch01.html, ir-ch02.html, ir-home.html, ir-search.html, ir-chapters.json
"""
import sys, os, json, html
from lib import *
import ch00, ch01, ch02

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), 'out')
os.makedirs(OUT, exist_ok=True)

FOOT = ('Personal study notes built from the Sarrthi IAS GS Mains Module (International Relations) handouts and class slides. '
        'The class slides are typed: no handwriting or board ink. Memory aids are built from the material’s own facts. '
        'Copyright belongs to the teacher; keep this private.')

BLANK = {
    1: ['Draw the six phases with one date each and the defining character of each.',
        'Write the Realism flow from memory, then the Phase 6 “Essence” chain.',
        'List the ten determinants, the six periods, five trade-offs and seven challenges.',
        'Write a 5-line opening for “Has India given up idealism?” using strategic autonomy.'],
    2: ['Fill a 3 x 4 grid: US, China, Russia against their four ambitions and one example each.',
        'Draw the India-China border with its three sectors, lengths and key points.',
        'Write the “India seeks / India avoids” table for the US from memory.',
        'Write one line each on the EU, France, Japan and Australia: what grows, what lags.'],
}


def tail(mod, n):
    out = []
    out.append(Sec('Timeline', [timeline(mod.TIMELINE)], sid='chapter-timeline'))
    out.append(Sec('Traps', [tbl('Common mix-ups and the rule for the exam hall', ['Trap', 'What goes wrong, and the rule'],
                                 [['**%s**' % a, b] for a, b in mod.TRAPS])], sid='traps'))
    out.append(Sec('Connects to', [links(mod.LINKS)], sid='connects'))
    out.append(Sec('Recall sheet', [recall(mod.RECALL)], sid='recall'))
    out.append(Sec('Revise', [
        tbl('Spaced schedule (count from the day you finish the chapter)', ['Day', 'What to do'], [
            ['Day 0', 'Read the Exam lens and the notes; mark the chapter done'],
            ['Day +1', 'Recall sheet: read once, hide, rebuild'],
            ['Day +3', 'Flashcards: missed ones only'],
            ['Day +7', 'Quick quiz; fix each miss against the Traps'],
            ['Day +21', 'Write two Mains answers from memory using the skeletons'],
            ['Day +45', 'Blank-page test (prompts below)'],
        ]),
        h3('Blank-page prompts'),
        ul(BLANK[n]),
    ], sid='revise'))
    # practice
    pr = []
    pr.append('<h3>Quick quiz</h3><div class="count" id="score">0 / 0 correct</div><div id="quiz"></div>')
    pr.append('<h3>Flashcards</h3><p class="gdesc">Tap the card to flip.</p><div class="deck"><div class="fc" id="fc" tabindex="0" role="button" aria-label="Flashcard, press to flip"></div><div class="count" id="fccount"></div><div class="row"><button class="btn" id="fcprev" type="button">Back</button><button class="btn pri" id="fcnext" type="button">Next</button><button class="btn" id="fcmiss" type="button">Missed it</button><button class="btn" id="fcshuf" type="button">Shuffle</button><button class="btn" id="fconlymiss" type="button">Only missed</button><button class="btn" id="fcall" type="button">All cards</button></div></div>')
    pr.append('<h3>Mains answer skeletons</h3><p class="gdesc">One for each Mains PYQ quoted in the material. Tap to open; try the answer first.</p>')
    for title, intro, body, closing in mod.SKELETONS:
        pr.append(details(title, p(intro) + ul(body) + p(closing)))
    out.append(Sec('Test yourself', pr, sid='practice'))
    return out


def make_chapter(mod, n, prev_ch, next_ch, pills, lede, ptag):
    secs = mod.build() + tail(mod, n)
    rendered, idx = render_sections(secs)
    svg, outline = mindmap(mod.MAP[0], mod.MAP[1], 'Chapter %d map' % n)
    toc = [('chapter-map', 'Chapter map')] + idx
    data = {'mcq': [{'q': q, 'options': o, 'answer': a, 'explain': e} for (q, o, a, e) in mod.MCQ],
            'cards': [{'q': q, 'a': a} for (q, a) in mod.CARDS]}
    head_html = chead('International Relations · GS-2 · Chapter %d' % n, mod.CH['title'], ptag, pills, lede)
    page = chapter_page(mod.CH, prev_ch, next_ch, rendered, toc, svg, outline, data, head_html, FOOT, 'International Relations')
    fn = '%sch%02d.html' % (BASE, n)
    open(os.path.join(OUT, fn), 'w', encoding='utf8').write(page)
    return toc, rendered


def make_start(prev_ch, next_ch):
    secs = ch00.build()
    rendered, idx = render_sections(secs)
    data = {'mcq': [], 'cards': []}
    lede = ('How the International Relations paper is asked, how this notebook is built, the priority and PYQ map, and which lecture feeds which chapter. '
            'Chapters 1 and 2 are ready; more will be added as the classes finish.')
    head_html = chead('International Relations · GS-2 · Start here', ch00.CH['title'], '', [('Read first', 'cls'), ('Chapters 1 and 2 built', ''), ('No handwriting in the decks', '')], lede)
    page = chapter_page(ch00.CH, None, next_ch, rendered, idx, None, None, data, head_html, FOOT, 'International Relations')
    open(os.path.join(OUT, '%sch00.html' % BASE), 'w', encoding='utf8').write(page)
    return idx, rendered


c0, c1, c2 = ch00.CH, ch01.CH, ch02.CH
idx0, r0 = make_start(None, c1)
idx1, r1 = make_chapter(ch01, 1, c0, c2,
    [('Class + handout', 'cls'), ('PPT-1 and PPT-2 · handout pp. 1-21', ''), ('7 Mains PYQs quoted · no Prelims', '')],
    'How the world order moved through six phases, from Westphalia to today’s multipolar churn, and how India’s foreign policy answers it: goals, ten determinants, six periods, five trade-offs and seven challenges.',
    'High priority')
idx2, r2 = make_chapter(ch02, 2, c1, None,
    [('Class + handout', 'cls'), ('PPT-3 · handout pp. 1-24', ''), ('10 Mains PYQs quoted · no Prelims', ''), ('EU, France, Japan, Australia: handout only', 'hb')],
    'What the US, China and Russia want and how they act, how their rivalries land on India, and India’s ties with China, the US, Russia, the EU, France, Japan and Australia.',
    'High priority')

chapters = []
for c, idx in ((c0, idx0), (c1, [('chapter-map', 'Chapter map')] + idx1[0:0]), (c2, None)):
    pass

def secs_for(idx, with_map):
    s = [{'id': i, 't': t} for i, t in idx]
    return ([{'id': 'chapter-map', 't': 'Chapter map'}] + s) if with_map else s

chs = [
    dict(n=0, title=c0['title'], sub=c0['sub'], badge=c0['badge'], slides=True, pending=False, secs=secs_for(idx0, False)),
    dict(n=1, title=c1['title'], sub=c1['sub'], badge=c1['badge'], slides=True, pending=False, secs=secs_for(idx1, True)),
    dict(n=2, title=c2['title'], sub=c2['sub'], badge=c2['badge'], slides=True, pending=False, secs=secs_for(idx2, True)),
]

home = home_page(chs, 'Study notebook for the GS-2 International Relations module: how the world order evolved, the major powers, and India’s foreign policy and bilateral ties. Built from your class slides and handouts only. Chapters are added as classes finish.', FOOT)
open(os.path.join(OUT, '%shome.html' % BASE), 'w', encoding='utf8').write(home)

# search
entries = []
for c, rendered in ((c0, r0), (c1, r1), (c2, r2)):
    import re
    for i, h in enumerate(rendered):
        m = re.match(r'<h2 id="([^"]+)">(.*?)<a class="anchor"', h, re.S)
        sid, title = m.group(1), strip_tags(m.group(2))
        entries.append({'c': str(c['n']), 'n': c['title'], 'id': sid, 't': title, 'x': strip_tags(h)})
open(os.path.join(OUT, '%ssearch.html' % BASE), 'w', encoding='utf8').write(search_page(entries))

json.dump({'id': NB_ID, 'title': NB_TITLE, 'sub': 'Sarrthi IAS GS Mains Module handouts and class slides', 'base': BASE,
           'home': BASE + 'home.html', 'search': BASE + 'search.html', 'timeline': '', 'chapters': chs},
          open(os.path.join(OUT, 'ir-chapters.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('built', len(entries), 'search entries;', {c['n']: len(c['secs']) for c in chs})
