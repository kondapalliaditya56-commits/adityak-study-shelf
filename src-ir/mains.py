# -*- coding: utf-8 -*-
"""Mains-ready notes: PYQ answers built on the teacher's APPROACHES sheet.
Facts come only from the chapter material and the CA layers already in the notebook (labelled)."""
import html, re
import lib
from lib import *

# ---------------------------------------------------------------- CSS
lib.EXTRA_CSS += ('<style>'
'.mr{border:1.5px solid var(--line);border-radius:14px;background:var(--surface);margin:18px 0 26px;overflow:hidden}'
'.mr-h{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center;justify-content:space-between;padding:10px 14px;background:var(--acc-soft);border-bottom:1px solid var(--line);font:600 13px/1.3 var(--sans)}'
'.mr-yr{color:var(--ink)}.mr-ap{background:var(--acc);color:var(--acc-ink);border-radius:99px;padding:3px 10px;font-size:12.5px}'
'.mr-b{padding:4px 14px 12px}.mr-q{font:italic 17px/1.5 var(--serif);margin:12px 0}'
'.mr-dec{font:14.5px/1.5 var(--sans);border-left:3px solid var(--saf);background:var(--saf-soft);padding:8px 12px;border-radius:0 8px 8px 0;margin:10px 0}'
'.mr-dec p{margin:3px 0}'
'.mr-part{margin:16px 0 6px;font:700 13px/1.2 var(--sans);letter-spacing:.06em;text-transform:uppercase;display:flex;align-items:center;gap:8px}'
'.mr-part i{font-style:normal;font-weight:500;letter-spacing:0;text-transform:none;color:var(--muted)}'
'.mr-part b{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:6px;color:var(--bg);font-size:12px}'
'.mr-part.i b{background:var(--blue)}.mr-part.bd b{background:var(--acc)}.mr-part.v b{background:var(--saf)}.mr-part.c b{background:var(--good)}'
'.mr-opt{border:1px dashed var(--line);border-radius:10px;padding:8px 12px;margin:6px 0;font:15px/1.5 var(--sans)}'
'.mr-opt span{display:block;font:600 11.5px/1.2 var(--sans);color:var(--blue);text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}'
'.mr-bh{font:700 15px/1.3 var(--sans);margin:12px 0 4px;color:var(--acc)}'
'.mr-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:10px;margin:12px 0}'
'.mr-box{border-radius:10px;padding:10px 12px;font:14.5px/1.45 var(--sans)}'
'.mr-box h5{margin:0 0 6px;font:700 12px/1.2 var(--sans);text-transform:uppercase;letter-spacing:.05em}'
'.mr-box ul{margin:0;padding-left:18px}.mr-box li{margin:3px 0}'
'.mr-data{background:var(--blue-soft)}.mr-data h5{color:var(--blue)}'
'.mr-ca{background:var(--saf-soft)}.mr-ca h5{color:var(--saf)}'
'.mr-src{display:inline-block;font:600 11px/1 var(--sans);color:var(--muted);border:1px solid var(--line);border-radius:99px;padding:2px 6px;margin-left:4px;white-space:nowrap}'
'.kw{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}.kw span{font:600 13px/1.2 var(--sans);background:var(--acc-soft);color:var(--ink);border:1px solid var(--acc);border-radius:99px;padding:5px 10px}'
'.mr-bud{font:13px/1.4 var(--sans);color:var(--muted);margin:6px 0}'
'.lvl{display:grid;gap:6px;margin:12px 0}.lvl-r{display:grid;grid-template-columns:120px 1fr 1fr;gap:6px}'
'.lvl-r>div{border-radius:8px;padding:8px 10px;font:14px/1.4 var(--sans)}'
'.lvl-r .lv-n{background:var(--acc);color:var(--acc-ink);font-weight:700;display:flex;align-items:center}'
'.lvl-r .lv-p{background:var(--good-soft)}.lvl-r .lv-m{background:var(--red-soft)}'
'.lvl-hd>div{background:none!important;color:var(--muted)!important;font:700 11.5px/1.2 var(--sans)!important;text-transform:uppercase;letter-spacing:.05em;padding:0 10px!important}'
'@media(max-width:640px){.lvl-r{grid-template-columns:1fr 1fr}.lvl-r .lv-n{grid-column:1/-1}.lvl-hd .lv-n{display:none}}'
'.swot{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0}@media(max-width:560px){.swot{grid-template-columns:1fr}}'
'.swot>div{border-radius:10px;padding:10px 12px;font:14px/1.45 var(--sans)}.swot h5{margin:0 0 4px;font:800 14px/1.2 var(--sans)}'
'.swot ul{margin:0;padding-left:18px}.sw-s{background:var(--good-soft)}.sw-w{background:var(--red-soft)}.sw-o{background:var(--blue-soft)}.sw-t{background:var(--saf-soft)}'
'.mr-model{border-top:1px solid var(--line);margin-top:14px}.mr-model>summary{cursor:pointer;padding:12px 0;font:700 15px/1.3 var(--sans);color:var(--acc)}'
'.mr-model .ma{font:16px/1.65 var(--serif);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin-bottom:10px}'
'.mr-model .ma h6{font:700 13px/1.2 var(--sans);margin:12px 0 2px;color:var(--acc)}.mr-model .ma p{margin:6px 0}.mr-model .ma ul{margin:4px 0;padding-left:20px}'
'.apx td:first-child,.apx th:first-child{white-space:nowrap}'
'</style>')


# ---------------------------------------------------------------- the teacher's sheet
APPROACHES = [
    ('1', 'Stakeholder', 'Impact, limitations / way forward', 'Who gains and who loses: India, the partner, communities, workers, investors. Good for “to what extent” and policy questions.'),
    ('2', 'Supply chain', 'Process', 'A chain from start to end: a trade corridor, energy route, or migration cycle (recruit → travel → work → return).'),
    ('3', 'GS Paper-wise', 'PESTEL (replacement)', 'Political, Economic, Social, Technological, Environmental, Legal or security. Good for “examine the relationship / influence”.'),
    ('4', 'Level analysis', 'Different points of view: personal, national, international', 'Household → national → bilateral → global. Good for diaspora, soft power and “global significance” questions.'),
    ('5', 'Component-based', 'Already read components only', 'When the question names its parts (“diplomatic, economic and strategic”), use those parts as headings, in that order.'),
    ('6', 'SDGs-based', '“Sustainable” word; significance', 'When the question says sustainable or development: climate, health, food, energy cooperation (Africa, island states).'),
    ('7', 'Syllabus-based', 'Broad question', 'A very broad question: use the syllabus line itself (bilateral, regional, global groupings; effect of policies of developed and developing countries; diaspora).'),
    ('8', 'Demand / Supply', '', 'What India wants versus what the partner offers: minerals, energy, markets, labour demand (Gulf, Germany, Japan).'),
    ('9', 'P3I', 'People, Powers, Processes, Infra (evaluate / body)', 'For IR, read “Powers” as the outside powers in play. Good for connectivity and regional-engagement questions.'),
    ('10', 'Life cycle', 'Living things / history', 'The arc of a relationship: birth, growth, crisis, reset (Maldives: First Responder → India Out → reset).'),
    ('11', 'Temporal (timeline)', '', 'Phases with dates. Good for “evolution”, “of late”, “post-Cold War” questions.'),
    ('12', 'SWOT', '', 'Strengths, weaknesses, opportunities, threats. Good for “importance and challenges” or “pros and cons”.'),
]

QUICK = 'Stakeholder → Supply Chain → GS Paper-wise → Level → Component → SDG → Syllabus → Demand/Supply → P3I → Life Cycle → Temporal → SWOT'


def approach_sheet():
    out = []
    out.append(callout('teacher', 'Your teacher’s APPROACHES sheet',
        'Every Mains answer here follows one shape: **Intro** (2-3 lines: a definition, a number or a current hook) → **Body** built on one approach from the sheet → **Way forward** → **Conclusion** (one line, ideally the slide’s own closing phrase). Pick the approach from the question’s **directive word** and the **parts it names**.\n\n'
        '**Quick recall:** ' + QUICK + '.'))
    out.append(details('Open the sheet: twelve approaches and where each fits in IR',
        '<div class="apx">' + tbl(None, ['No.', 'Approach', 'How to use / key words (sheet)', 'Where it fits in IR'],
            [[a, '**%s**' % b, c or '—', d] for a, b, c, d in APPROACHES]) + '</div>'))
    return out


# ---------------------------------------------------------------- visual helpers
def levels(rows, head=('Level', 'The bridge works (+)', 'Where it breaks (−)')):
    h = '<div class="lvl"><div class="lvl-r lvl-hd"><div class="lv-n">%s</div><div>%s</div><div>%s</div></div>' % tuple(html.escape(x) for x in head)
    for n, pl, mi in rows:
        h += '<div class="lvl-r"><div class="lv-n">%s</div><div class="lv-p">%s</div><div class="lv-m">%s</div></div>' % (inline(n), inline(pl), inline(mi))
    return h + '</div>'


def swot(s, w, o, t):
    cell = lambda cls, title, items: '<div class="%s"><h5>%s</h5><ul>%s</ul></div>' % (cls, title, ''.join('<li>%s</li>' % inline(x) for x in items))
    return '<div class="swot">' + cell('sw-s', 'S · Strengths', s) + cell('sw-w', 'W · Weaknesses', w) + cell('sw-o', 'O · Opportunities', o) + cell('sw-t', 'T · Threats', t) + '</div>'


def words(paras):
    txt = ' '.join(plain(re.sub(r'^#+\s*|^- ', '', x)) for x in paras)
    return len(re.findall(r"[A-Za-z0-9₹$][\w’'.,%$₹-]*", txt))


def model_html(paras):
    h, in_ul = '', False
    for x in paras:
        if x.startswith('- '):
            if not in_ul:
                h += '<ul>'; in_ul = True
            h += '<li>%s</li>' % inline(x[2:])
            continue
        if in_ul:
            h += '</ul>'; in_ul = False
        if x.startswith('## '):
            h += '<h6>%s</h6>' % inline(x[3:])
        else:
            h += p(x)
    if in_ul:
        h += '</ul>'
    return h


def answer(d):
    """d keys: meta, approach, q, decode[list], why, intros[(label,text)], body[(head,[pts])], visual[html],
    data[(text,src)], ca[(text,src)], wf[list], concl, kw[list], budget, model[list], limit"""
    h = '<article class="mr" id="%s">' % d['id']
    h += '<header class="mr-h"><span class="mr-yr">%s</span><span class="mr-ap">Approach: %s</span></header><div class="mr-b">' % (inline(d['meta']), inline(d['approach']))
    h += '<p class="mr-q">“%s”</p>' % inline(d['q'])
    h += '<div class="mr-dec">' + ''.join(p(x) for x in d['decode']) + p('**Why this approach:** ' + d['why']) + '</div>'
    h += '<p class="mr-bud">' + inline(d['budget']) + '</p>'
    # intro
    h += '<div class="mr-part i"><b>I</b>Introduction <i>pick one opener</i></div>'
    for lab, t in d['intros']:
        h += '<div class="mr-opt"><span>%s</span>%s</div>' % (html.escape(lab), inline(t))
    # body
    h += '<div class="mr-part bd"><b>B</b>Body <i>%s</i></div>' % inline(d['approach'])
    for head, pts in d['body']:
        h += '<div class="mr-bh">%s</div>%s' % (inline(head), ul(pts))
    # visual
    h += '<div class="mr-part v"><b>V</b>Draw this in the answer <i>30 seconds</i></div>' + ''.join(d['visual'])
    # data + CA
    srcs = lambda s: ('<span class="mr-src">%s</span>' % html.escape(s)) if s else ''
    h += '<div class="mr-grid"><div class="mr-box mr-data"><h5>Numbers to drop in</h5><ul>%s</ul></div>' % ''.join('<li>%s%s</li>' % (inline(t), srcs(s)) for t, s in d['data'])
    h += '<div class="mr-box mr-ca"><h5>Current affairs to cite</h5><ul>%s</ul></div></div>' % ''.join('<li>%s%s</li>' % (inline(t), srcs(s)) for t, s in d['ca'])
    # way forward + conclusion
    h += '<div class="mr-part c"><b>C</b>Way forward and conclusion</div>' + ul(d['wf'])
    h += callout('key', 'Closing line', d['concl'])
    h += '<div class="mr-bh">Keywords to underline</div><div class="kw">' + ''.join('<span>%s</span>' % html.escape(k) for k in d['kw']) + '</div>'
    n = words(d['model'])
    assert n <= d['limit'], (d['id'], n, d['limit'])
    h += '<details class="mr-model"><summary>Model answer to compare (%d words; limit %d). Write yours first.</summary><div class="ma">%s</div></details>' % (n, d['limit'], model_html(d['model']))
    return h + '</div></article>'


def pyq_map(rows):
    return tbl('Approach for every PYQ in this chapter', ['PYQ', 'Directive and parts', 'Best approach', 'Body headings'], rows,
               desc='★ = worked sample below. The others follow the same shape; their outlines are in “Test yourself”.')


# ================================================================= CHAPTER 3
CH3 = [
    dict(id='mr-2024-maldives', limit=250,
         meta='Mains 2024 · 15 marks · 250 words', approach='Component (two parts) + SWOT',
         q='Discuss the geopolitical and geostrategic importance of Maldives for India with a focus on global trade and energy flows. Further also discuss how this relationship affects India’s maritime security and regional stability amidst international competition?',
         decode=['**Directive:** “Discuss” twice, so two clearly labelled parts.',
                 '**Part 1:** importance, with a focus on **trade and energy flows**. **Part 2:** effect on **maritime security and regional stability**, with **international competition** (China) built in.'],
         why='The question names its own parts (Component). Part 2 asks for an effect amid competition, which a SWOT shows in one glance: what works, what is fragile, what can grow, what threatens.',
         budget='Budget: intro 30 words · part 1 ≈ 70 · part 2 (SWOT) ≈ 100 · way forward and conclusion ≈ 50. Time: 11 minutes.',
         intros=[('Slide opener', 'The Maldives matter for **location, not size**: they sit in the **Central Indian Ocean** beside the sea lanes that carry India’s trade and energy.'),
                 ('Current hook', 'From the “India Out” campaign (2023-24) to the **Favara-UPI** link (2026), India-Maldives ties show how a small island state shapes India’s maritime security.')],
         body=[('Part 1 · Importance for trade and energy', [
                   '**Sea lanes:** close to India’s sea lanes and maritime approaches; trade and energy pass near the archipelago.',
                   '**First Responder record:** Operation **Cactus (1988)**, the **2004 tsunami**, Operation **Neer (2014)**: proof that India is the nearest reliable partner.',
                   '**Economic stake:** **Greater Malé Connectivity Project (US$500 mn)**, **Hanimaadhoo** runway (2024), RBI swap **US$400 mn and ₹30 bn**; trade **US$771.76 mn (FY 2025-26)**.']),
               ('Part 2 · Effect on maritime security and regional stability (SWOT)', [
                   'Draw the SWOT grid below; write two points in each box.',
                   '**Competition:** name it inside “Threats”: the Chinese research vessel (2024), the **China-Maldives FTA (January 2025)**.'])],
         visual=[swot(['**CEMSP (October 2024)**', 'Exercises **Ekuverin, Ekatha, Dosti**', '**Colombo Security Conclave**'],
                      ['**Sovereignty sensitivity**: “India Out” (2023-24)', 'Military personnel replaced by civilians (2024)', 'Hydrographic survey not renewed (2024)'],
                      ['**FTA**: first round concluded (July 2026)', '**Favara-UPI** live (July 2026)', 'Climate-resilient ports, airports, water', '**MAHASAGAR**'],
                      ['**Chinese research vessel** docked (2024)', '**China-Maldives FTA** (January 2025)', 'Suspicion over the **UTF Harbour**', 'Tourism boycott after the **January 2024 Lakshadweep** row']),
                 fig('img/ir-nb-map.jpg', 'Sketch tip: mark India, Sri Lanka and the Maldives and draw the sea lane past them (map: handout p. 1).', 'Handout map')],
         data=[('Trade US$771.76 million (FY 2025-26)', 'handout'), ('Currency swap: US$400 million and ₹30 billion (2024)', 'handout'),
               ('About 60,000 Indians live in the Maldives', 'handout'), ('Indian tourists over 2 lakh a year (2021-23)', 'merged handout'),
               ('1,000 civil servants trained (2019-24), another 1,000 in 2024-29', 'handout')],
         ca=[('**Favara-UPI corridor** live: rufiyaa settled in rupees; less dependence on the dollar', 'Jul 2026 CA'),
             ('**FTA round one** ended in July 2026; China’s FTA in force since January 2025', 'handout'),
             ('**MAHASAGAR**: India as “preferred security partner and first responder”', 'Aug 2026 CA')],
         wf=['**Sovereignty-sensitive engagement:** clearly define ownership, personnel and operating rules for Indian-supported assets.',
             '**Maritime security:** information sharing, search and rescue; keep **operational decisions with Maldivian authorities**.',
             '**Economy:** faster FTA talks; transparent, debt-sustainable finance.',
             '**Climate and people:** climate-resilient infrastructure; **Project Mausam** and shared heritage.'],
         concl='“Maldives is vital because of its strategic location, not size.” India should **combine security cooperation with respect for sovereignty** (slide 42), under MAHASAGAR.',
         kw=['Location not size', 'First Responder', 'CEMSP 2024', 'India Out', 'Sovereignty-sensitive', 'Favara-UPI', 'China-Maldives FTA', 'Colombo Security Conclave', 'MAHASAGAR'],
         model=['The Maldives matter for location, not size: they sit in the Central Indian Ocean beside the sea lanes that carry India’s trade and energy.',
                '## Part 1: Importance',
                '- **Trade and energy:** the archipelago lies close to India’s sea lanes and maritime approaches.',
                '- **First Responder:** Operation Cactus (1988), the 2004 tsunami and Operation Neer (2014) built deep trust.',
                '- **Economic stake:** the Greater Malé Connectivity Project (US$500 million), the Hanimaadhoo runway and a US$400 million and ₹30 billion currency swap.',
                '## Part 2: Effect on maritime security',
                '- **Strengths:** the Comprehensive Economic and Maritime Security Partnership (2024); exercises Ekuverin, Ekatha and Dosti; the Colombo Security Conclave.',
                '- **Weaknesses:** sovereignty sensitivity. The “India Out” campaign (2023-24) forced Indian personnel to be replaced by civilians, and the hydrographic survey was not renewed.',
                '- **Opportunities:** FTA talks (first round, July 2026), the Favara-UPI link and climate-resilient infrastructure.',
                '- **Threats:** a Chinese research vessel (2024), the China-Maldives FTA (2025), suspicion over the UTF Harbour, and tourism boycotts after the Lakshadweep row.',
                '## Way forward',
                'India should define clear rules for the assets it supports, leave operational decisions with Maldivian authorities, speed up the FTA and invest in climate resilience and shared heritage through Project Mausam.',
                'Combining security cooperation with respect for sovereignty, under MAHASAGAR, will keep India the Maldives’ preferred security partner and first responder.']),
]
MAP3 = [
    ['★ 2024 · Maldives (15m)', 'Discuss + discuss: importance; effect on security amid competition', '**Component + SWOT**', 'Part 1 importance · Part 2 S/W/O/T'],
    ['2022 · Sri Lanka crisis (10m)', 'Discuss India’s role “in the light of” age-old friendship', '**Temporal**', 'Old ties → 2022 crisis response → post-crisis connectivity → limits'],
    ['2015 · Project Mausam (12.5m)', 'Does it have a strategic dimension? Discuss', '**Level analysis**', 'Cultural → bilateral → Indian Ocean (strategic) → limits'],
    ['2015 · India-Pakistan soft power (12.5m)', '“To what extent”', '**Stakeholder**', 'People and pilgrims · governments · army and terror groups → verdict'],
]

# ================================================================= CHAPTER 4
CH4 = [
    dict(id='mr-2026-diaspora', limit=250,
         meta='Mains 2026 · 15 marks · 250 words', approach='Level analysis',
         q='India’s global diaspora acts as a living bridge, as a critical economic factor and knowledge network in transforming cultural heritage into geopolitical influence and strategic leverage worldwide. Critically examine this statement.',
         decode=['**Directive:** “Critically examine”: show the bridge **and** where it breaks; end with a balanced verdict.',
                 '**Parts named:** economic factor · knowledge network · culture into influence and leverage.'],
         why='“Worldwide” and “from cultural heritage to geopolitical influence” describe a climb through levels: household, national, bilateral, global. Putting a “+” and a “−” at each level gives the “critically” half without a separate essay.',
         budget='Budget: intro 30 words · four levels ≈ 130 · limits ≈ 50 · way forward and conclusion ≈ 40. Time: 11 minutes.',
         intros=[('Data opener', 'With about **37 million** overseas Indians, India has the **world’s largest diaspora**; the PM calls them “**Rashtradoot**”.'),
                 ('Current hook', 'On Pravasi Bharatiya Divas (9 January 2026) the MEA called the diaspora “**a living bridge** connecting India and the world”.')],
         body=[('Level 1 · Household and state: the economic factor', [
                   '**Remittances US$135.4 bn (FY25)**, world’s highest, about **3.8% of GDP**; they sustain households in **Kerala and Punjab**.']),
               ('Level 2 · National: crisis finance and the knowledge network', [
                   '**Resurgent India Bonds (1998)** raised about **US$4.2 bn** during sanctions.',
                   'Leaders such as **Pichai, Nadella, Banga**; **Silicon Valley-India** start-up links; **brain circulation** through **VAIBHAV, VAJRA, GIAN**.']),
               ('Level 3 · Bilateral: strategic leverage', [
                   'The Indian-American community backed the **2008 India-US civil nuclear agreement**; events such as Howdy Modi.']),
               ('Level 4 · Global: heritage into influence', [
                   'Yoga, Diwali, cinema, Ayurveda; **Girmitiya** links with Mauritius, Fiji, Guyana, Suriname and the Caribbean.']),
               ('“Critically”: where the bridge breaks (slide 8)', [
                   'Remittances go mostly to **consumption**, not productive investment.',
                   'Indian-origin legislators **serve host-country voters**; culture does not guarantee diplomatic votes.',
                   'Small sections **finance separatism** and target missions.',
                   'Welfare crises become **bilateral issues**: 400+ student deaths (2018-24), H-1B rules.'])],
         visual=[levels([('Household', 'Remittances to Kerala, Punjab', 'Spent on consumption, housing'),
                         ('National', 'RIB 1998 US$4.2 bn; brain circulation', 'Depends on trust in institutions'),
                         ('Bilateral', '2008 nuclear deal lobby', 'Legislators answer to host voters'),
                         ('Global', 'Yoga, Diwali, Girmitiya; “Rashtradoot”', 'Soft power ≠ diplomatic votes; separatist fringe')]),
                 flow('The chain the question describes', [('Cultural heritage', 'yoga, festivals, Girmitiya', ''), ('Soft power', 'visibility, goodwill', ''),
                      ('Influence', 'lobbying, leaders', ''), ('Strategic leverage', '2008 deal; crisis finance', 'good')])],
         data=[('About 37 million overseas Indians; US 6.07 mn, UAE 4.34 mn', 'handout, 2026'), ('Remittances US$135.4 bn (FY25), about 3.8% of GDP', 'handout'),
               ('Remittance shares 2023-24: US 27.7%, UAE 19.2%, UK 10.8%', 'handout'), ('About 12.5 lakh Indian students abroad (January 2025)', 'handout'),
               ('Over 3,000 unregistered recruiting agents (October 2024)', 'handout')],
         ca=[('MEA: diaspora is “a living bridge” (9 January 2026), the phrase the question borrowed', 'web'),
             ('**e-OCI card** launched: digital OCI services', 'Jul 2026 CA'),
             ('Four Indian sailors killed in a strike at **Odesa**; US fixes stay limits for F, J, I visas', 'Jul 2026 CA'),
             ('“**Diaspora 2.0**”: from ceremony to structured partnership', 'Aug 2026 CA')],
         wf=['**Differentiated policy** for workers, students, professionals and the historic diaspora (slide 4: “different groups require different forms of engagement”).',
             '**Real-time migration database** (Standing Committee, 2025); pass the **Overseas Mobility (Facilitation and Welfare) Bill, 2024**.',
             '**Diaspora capital:** cheaper transfers and investment options; **security:** act on unlawful individuals while separating them from the wider diaspora.'],
         concl='Under the **4 Cs** (Care, Connect, Celebrate, Contribute), policy should move “from simple engagement towards **protection, partnership and productive global networks**” (slide 12).',
         kw=['Living bridge', 'Rashtradoot', 'US$135.4 bn', 'Brain circulation', 'Girmitiya', '2008 nuclear deal', 'Host-country loyalty', 'Diaspora 2.0', '4 Cs'],
         model=['With about 37 million overseas Indians, India has the world’s largest diaspora. The MEA calls it “a living bridge”; the PM calls its members “Rashtradoot”.',
                '## How the bridge works, level by level',
                '- **Household:** remittances of US$135.4 billion (FY25), the world’s highest and about 3.8% of GDP, sustain families in Kerala and Punjab.',
                '- **National:** Resurgent India Bonds raised US$4.2 billion during the 1998 sanctions; leaders such as Pichai, Nadella and Banga, Silicon Valley start-up links and VAIBHAV, VAJRA and GIAN turn brain drain into brain circulation.',
                '- **Bilateral:** the Indian-American community backed the 2008 India-US civil nuclear agreement.',
                '- **Global:** yoga, Diwali, cinema and Girmitiya ties with Mauritius, Fiji and the Caribbean convert heritage into soft power.',
                '## Where the bridge breaks',
                '- Remittances fund consumption more than investment.',
                '- Indian-origin legislators serve host-country voters, and cultural appeal does not guarantee diplomatic votes.',
                '- Small sections finance separatism and target Indian missions.',
                '- Welfare crises become bilateral issues: over 400 student deaths (2018-24), H-1B curbs and sailors killed at Odesa (2026).',
                '## Way forward',
                'India needs a differentiated policy for workers, students and professionals, a real-time migration database, the pending Overseas Mobility Bill, 2024, and a “Diaspora 2.0” partnership on skills and investment.',
                'Guided by the 4 Cs, India must move from engagement to protection, partnership and productive global networks. Only then will goodwill become lasting strategic leverage.']),
]
MAP4 = [
    ['★ 2026 · living bridge (15m)', 'Critically examine: economic, knowledge, culture → influence', '**Level analysis**', 'Household → national → bilateral → global, each with + and −'],
    ['2023 · benefits in the West (10m)', 'Describe economic and political benefits', '**Component**', 'Economic · political · one-line caveat'],
    ['2020 · “decisive” role (10m)', 'Comment with examples', '**Stakeholder**', 'Host governments · voters · Indian state → “important, not decisive”'],
    ['2017 · role in South-East Asia (15m)', 'Appraise role in economy and society', '**GS Paper-wise (PESTEL)**', 'Economic · social and cultural · political → limits'],
]

# ================================================================= CHAPTER 5
CH5 = [
    dict(id='mr-2016-look-east', limit=200,
         meta='Mains 2016 · 12.5 marks · 200 words', approach='Temporal (timeline)',
         q='Evaluate the economic and strategic dimensions of India’s Look East Policy in the context of the post-Cold War international scenario.',
         decode=['**Directive:** “Evaluate”: give the record, then a verdict (what worked, what did not).',
                 '**Parts named:** economic · strategic · post-Cold War context.'],
         why='“Post-Cold War” asks you to show change over time. Three dated phases show the policy moving from economics (Look East) to strategy (Act East); a verdict line closes the “evaluate”.',
         budget='Budget: intro 25 words · three phases ≈ 90 · results and limits ≈ 50 · verdict and conclusion ≈ 35. Time: 9 minutes.',
         intros=[('Context opener', 'After the Cold War, the **1991 liberalisation** led India to **Look East** towards Southeast Asia; in **2014** it became **Act East**.'),
                 ('Slide opener', 'India-ASEAN ties are “**strategic convergence with under-realised economic potential**” (slide 19): the two halves of this question.')],
         body=[('Phase 1 · 1991-2010: the economic phase', [
                   '**Sectoral Partner (1992)**, **Dialogue Partner (1995)**, first **ASEAN-India Summit (2002)**, **AITIGA (2010)**.']),
               ('Phase 2 · 2014-19: Act East adds strategy', [
                   'Security and maritime cooperation; the **Indo-Pacific Oceans Initiative (2019)** with **ASEAN centrality**.']),
               ('Phase 3 · 2022-26: comprehensive partnership', [
                   '**Comprehensive Strategic Partnership (2022)**; Indonesia’s President **Prabowo** Republic Day chief guest (2025); **2026 Year of Maritime Cooperation**.']),
               ('Evaluate: results versus limits', [
                   '**Results:** trade **US$128.38 bn** (about **10%** of India’s trade); **UPI-PayNow**; 5.9 million Indian travellers (2024).',
                   '**Limits:** deficit about **US$51.55 bn**; **RCEP exit**; China’s **ASEAN FTA 3.0 (2025)**; **Kaladan** and Trilateral Highway delays.'])],
         visual=[flow('Timeline to draw', [('1991', 'Look East begins', ''), ('1992 · 1995', 'Sectoral → Dialogue Partner', ''), ('2002 · 2010', 'Summit · AITIGA', ''),
                      ('2014', 'Act East', 'good'), ('2019', 'IPOI', 'good'), ('2022', 'CSP', 'good'), ('2026', 'Maritime year · BrahMos', 'good')]),
                 fig('img/ir-ext-asean.jpg', 'Sketch tip: outline ASEAN, mark the Malacca Strait, the Andamans and Kaladan (slide 20).', 'Class slide map')],
         data=[('Trade US$128.38 bn (FY 2025-26), about 10% of India’s trade', 'handout'), ('Trade deficit about US$51.55 bn (FY 2025-26)', 'handout'),
               ('India’s FDI into ASEAN US$3.5 bn (2024)', 'handout'), ('UPI-PayNow: 19 Indian banks (July 2025)', 'handout'), ('5.9 million Indian travellers to ASEAN (2024)', 'handout')],
         ca=[('**BrahMos** for Indonesia; **Sabang** port revived; Indonesian liaison officer at **IFC-IOR**', 'Jul 2026 CA'),
             ('China’s rules for **Scarborough Shoal**: why ASEAN is divided on China', 'Aug 2026 CA'),
             ('ASEAN-India, EAS and ARF foreign ministers met in Manila', 'Jul 2026 CA')],
         wf=['A balanced **AITIGA review** (customs, rules of origin, non-tariff barriers); joint electronics, pharma and EV value chains.',
             'Complete the **Trilateral Highway and Kaladan**; maritime domain awareness; HADR with the **AHA Centre**.',
             'Align **Act East and Viksit Bharat 2047** with **ASEAN 2045**.'],
         concl='“Move from **strategic convergence** to stronger **economic integration, connectivity and maritime cooperation**” (slide 24): beyond ASEAN centrality as a slogan.',
         kw=['Look East 1991', 'Act East 2014', 'ASEAN centrality', 'AITIGA', 'IPOI', 'CSP 2022', 'Trade deficit', 'RCEP', 'Kaladan'],
         model=['After the Cold War, the 1991 liberalisation led India to look east towards Southeast Asia. In 2014 the Look East Policy became the Act East Policy.',
                '## Three phases',
                '- **1991-2010, economic:** India became ASEAN’s Sectoral Partner (1992) and Dialogue Partner (1995); the first summit followed in 2002 and the goods agreement (AITIGA) in 2010.',
                '- **2014-19, strategic:** Act East added security and maritime cooperation; the Indo-Pacific Oceans Initiative (2019) placed ASEAN centrality at its core.',
                '- **2022-26, comprehensive:** a Comprehensive Strategic Partnership (2022), a Year of Maritime Cooperation (2026) and BrahMos for Indonesia.',
                '## Evaluation',
                'Trade has reached US$128.38 billion, about 10% of India’s trade, and UPI-PayNow links people. But the deficit is about US$51.55 billion, India left RCEP, China deepened its ASEAN FTA, and Kaladan is delayed. Strategically the policy has matured; economically it is under-realised.',
                'A balanced AITIGA review, joint value chains and finished corridors can move India from strategic convergence to real economic integration.']),
    dict(id='mr-2024-central-asia', limit=150,
         meta='Mains 2024 · 10 marks · 150 words', approach='Component-based',
         q='Critically analyse India’s evolving diplomatic, economic and strategic relations with the Central Asian Republics (CARs) highlighting their increasing significance in regional and global geopolitics.',
         decode=['**Directive:** “Critically analyse”: break it into parts and add limits.',
                 '**Parts named:** diplomatic · economic · strategic · significance in regional and global geopolitics.'],
         why='The question lists its own components; use them as headings in the same order. The examiner ticks each heading. Add one “critically” block and a one-line verdict.',
         budget='Budget: intro 20 words · three components ≈ 75 · significance ≈ 15 · limits ≈ 25 · conclusion ≈ 15. Time: 7 minutes.',
         intros=[('Slide opener', 'Central Asia is India’s **Eurasian gateway without direct land access**: “**civilisational depth but a connectivity deficit**”.'),
                 ('Quote opener', '“**Central Asia is central to India’s vision of an integrated and stable extended neighbourhood**” (PM, quoted in the handout).')],
         body=[('Diplomatic', ['**Connect Central Asia (2012)**; PM in **all five** (2015); **SCO (2017)**; Dialogue (2019); **first Summit (2022)**; all five back India’s **UNSC** bid.']),
               ('Economic', ['**Uranium** (Kazakhstan); **Rare Earth Forum (2024)**, Uzbek mineral MoU (2026); **US$1 bn LoC (2020)**; **EAEU FTA** terms (August 2025).']),
               ('Strategic', ['Afghanistan, terrorism, narcotics; **DUSTLIK 2026**; cargo to Kazakhstan via **INSTC (March 2025)**.']),
               ('Significance', ['A balancing presence in a region shaped by **Russia and China**; support in the **SCO** (slide 30: “competitive environment”).']),
               ('Critically', ['No land route (**Pakistan transit blocked**); China’s trade **US$106.3 bn** dwarfs India’s; **Chabahar waiver lapsed (April 2026)**; **TAPI** stalled.'])],
         visual=[lanes('Three columns to draw', [('Diplomatic', [('2012', 'Connect Central Asia', ''), ('2017', 'SCO', ''), ('2022', 'First Summit', 'good')]),
                                                 ('Economic', [('Uranium', 'Kazakhstan', ''), ('Rare earths', 'Forum 2024', ''), ('EAEU FTA', 'ToR 2025', 'good')]),
                                                 ('Strategic', [('Afghanistan', 'terror, drugs', ''), ('INSTC', 'cargo 2025', ''), ('Chabahar', 'waiver lapsed', 'bad')])]),
                 fig('img/ir-ext-central-asia.jpg', 'Sketch tip: five republics with one interest each: Kazakhstan uranium, Uzbekistan minerals, Turkmenistan gas, Kyrgyzstan education, Tajikistan security (slide 32).', 'Class slide map')],
         data=[('China-Central Asia trade US$106.3 bn (2025)', 'handout'), ('India-Uzbekistan trade US$1.3 bn (2025)', 'handout'),
               ('About 16,000 Indian students in Kyrgyzstan', 'handout'), ('US$1 bn Line of Credit (2020)', 'handout')],
         ca=[('**Kazakhstan is the largest uranium producer** (Australia has the largest resources)', 'Jul 2026 CA'),
             ('US strike near **Shahid Beheshti**, Chabahar, where India runs the terminal', 'Jul 2026 CA'),
             ('Uzbekistan and Kyrgyzstan among India’s recent **BIT** partners', 'Jul 2026 CA')],
         wf=['Run **Chabahar-INSTC-Ashgabat** as a regular commercial corridor; finish the **EAEU FTA**.',
             'Long-term uranium, gas and mineral deals with joint processing; student safety and quality medical education.'],
         concl='“A **geography gap, not an interest gap**” (slide 35): a stronger **Connect Central Asia 2.0** can turn civilisational ties into sustained engagement.',
         kw=['Eurasian gateway', 'Connect Central Asia 2012', 'SCO 2017', 'India-Central Asia Summit', 'Uranium', 'Rare earths', 'INSTC', 'Geography gap', 'Connect Central Asia 2.0'],
         model=['Central Asia is India’s Eurasian gateway, linked by the Silk Routes but cut off by geography.',
                '- **Diplomatic:** Connect Central Asia (2012), the PM’s visit to all five republics (2015), SCO membership (2017) and the first Summit (2022); all five back India’s UNSC bid.',
                '- **Economic:** uranium from Kazakhstan, rare-earth cooperation (2024, 2026), a US$1 billion credit line and EAEU FTA talks.',
                '- **Strategic:** Afghanistan, terrorism and drugs; exercise DUSTLIK; Indian cargo reached Kazakhstan via the INSTC (2025).',
                '- **Significance:** a balancing presence where Russia and China dominate.',
                '- **Critically:** Pakistan blocks land access, China’s US$106.3 billion trade dwarfs India’s, the Chabahar waiver has lapsed and TAPI is stalled.',
                'The gap is of geography, not interest; a “Connect Central Asia 2.0” through Chabahar, the INSTC and Ashgabat can close it.']),
]
MAP5 = [
    ['★ 2024 · Central Asia (10m)', 'Critically analyse: diplomatic, economic, strategic; significance', '**Component**', 'The three named parts · significance · critically'],
    ['2021 · influence in Africa (10m)', 'Examine India’s influence', '**GS Paper-wise (PESTEL)**', 'Political (AU in G20) · economic · social (ITEC, e-VBAB) · tech (DPI) · environment (ISA) → China gap'],
    ['2021 · AUKUS (15m)', 'Supersede existing partnerships? Strength and impact', '**Level analysis**', 'Bilateral (Australia) → regional (ASEAN, Quad) → global (US-China) → verdict'],
    ['2018 · Israel “cannot be rolled back” (10m)', 'Discuss', '**Temporal**', '1950 → 1992 → 2026 SSP; then limits (Palestine, Iran, Gulf)'],
    ['2018 · Ashgabat Agreement (10m)', 'Implications amid outside powers', '**Supply chain**', 'Port → INSTC → Central Asia, each link with gains and risks'],
    ['★ 2016 · Look East (12.5m)', 'Evaluate economic and strategic dimensions', '**Temporal**', '1991-2010 · 2014-19 · 2022-26 → results and limits'],
    ['2015 · Africa pros and cons (12.5m)', 'Critically examine', '**SWOT**', 'Strengths · weaknesses · opportunities · threats → verdict'],
]

DATA = {3: (CH3, MAP3), 4: (CH4, MAP4), 5: (CH5, MAP5)}


def section(n):
    if n not in DATA:
        return None
    items, rows = DATA[n]
    blocks = approach_sheet() + [pyq_map(rows)]
    blocks.append(callout('source', 'How these are built',
        'Facts and numbers come from this chapter’s slides and handout; current-affairs points come from the Jul and Aug 2026 magazines in your Project (web items are labelled). Each sample has a **model answer** inside the word limit. Write yours first, then compare.'))
    for d in items:
        blocks.append(answer(d))
    return Sec('Mains-ready notes', blocks, sid='mains-ready')
