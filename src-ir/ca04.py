# -*- coding: utf-8 -*-
"""Chapter 4 live current-affairs layer (Jul and Aug 2026 CA magazines; web items labelled)."""
from lib import *

AUG = 'Aug 2026 CA'
JUL = 'Jul 2026 CA'
LIVE = {}

LIVE['Who the diaspora is'] = [
    live_head('the diaspora in the news'),
    live(JUL, 'OCI goes fully digital: the e-OCI card',
         'The Union Home Minister launched an **e-Overseas Citizen of India (e-OCI) card** for fully digital OCI services, alongside the FCRA 2.0 portal. The magazine restates the difference: an **NRI is an Indian citizen living abroad**; an **OCI is a foreign citizen of Indian origin** with a lifelong visa who can live, work and study in India indefinitely.',
         'A small but concrete “Connect” step under the 4 Cs: easier paperwork for the 37-million community. Use it in the way-forward paragraph on digital and consular capacity.',
         '**OCI** = foreign citizen of Indian origin; **NRI** = Indian citizen abroad. FCRA = Foreign Contribution (Regulation) Act, 2010.',
         'NRI or OCI: which one is an Indian citizen?',
         'The NRI. An OCI holds a foreign passport with a lifelong visa for India.',
         src='Jul 2026 CA (quick updates: FCRA portal and e-OCI card).', why_label='What happened'),
]

LIVE['Why the diaspora matters for India'] = [
    live_head('2026: the exam used the government’s own phrase'),
    live('Mains 2026 + web', '“A living bridge”: from a ministry statement to a 15-mark question',
         'On **Pravasi Bharatiya Divas (9 January 2026)** the MEA called the diaspora “**a living bridge** connecting India and the world”. Seven months later GS-II Q19 opened with the same words. The August magazine’s cultural-diplomacy chapter quotes the question as its PYQ and lists **Pravasi Bharatiya Divas and the Know India Programme** as diaspora programmes.',
         'Pattern worth knowing: UPSC borrows official phrases. Read MEA statements for vocabulary. The magazine also gives the soft-power example the handout uses: the diaspora **helped push the 2008 India-US civil nuclear agreement in the US Congress**.',
         'Cultural diplomacy runs through the **Global Engagement Scheme** (Ministry of Culture) and the **ICCR** (under the MEA).',
         src='web: Newsonair, 9 Jan 2026 (collected for the PYQ Lab); Aug 2026 CA §3.7.', why_label='What happened'),
    live(AUG, 'Mauritius and the Girmitiya memory',
         'The Union Petroleum Minister visited **Mauritius**, whose **Aapravasi Ghat** (a UNESCO World Heritage Site) was the immigration depot for the British “great experiment” in **indentured labour** to replace slave labour.',
         'The historic diaspora in one place: the Girmitiya link the handout names is a living asset in Indian Ocean diplomacy (Mauritius also hosts the IORA headquarters).',
         '**Aapravasi Ghat**, Port Louis: UNESCO site; the first site of the indentured-labour experiment.',
         src='Aug 2026 CA §3.10.1 (high-level visits).'),
]

LIVE['Where the diaspora stops helping'] = [
    live_head('limits, as the magazine sees them'),
    live(AUG, '“Diaspora 2.0”: from ceremony to structured partnership',
         'The Standing Committee on External Affairs (2022 report, as quoted) found that **Indian missions lack a structured mechanism for regular consultation with overseas Indians**. The magazine’s fix is “**Diaspora 2.0**”: move from ceremonial engagement to structured partnership on **skills, investment and second-generation cultural retention**.',
         'It matches this chapter’s limits table: networks stay informal, and remittances do not become investment by themselves. Quote “Diaspora 2.0” as a one-phrase way forward.',
         'Two committee reports: **2022** (cultural diplomacy, as quoted in the magazine) and **2025** (Indian Diaspora Overseas, as quoted in the handout).',
         src='Aug 2026 CA §3.7 (cultural diplomacy).'),
]

LIVE['Challenges the diaspora faces, and evacuation diplomacy'] = [
    live_head('the risks, in real headlines'),
    live(JUL, 'Indian sailors killed at Odesa; US visa rules tighten',
         'A Russian missile strike on a merchant vessel at **Odesa** killed **ten crew, four of them Indian**. The US Department of Homeland Security replaced “Duration of Status” with a **fixed authorised stay** for **F (students), J (exchange visitors and researchers) and I (journalists)** visas.',
         'Two rows of the challenges table in the news: **conflict risk** (seafarers caught in wars far from West Asia) and **immigration restrictions** (students and researchers). A third headline from the same month: India’s **Global Passport Index** rank fell to **125th**.',
         'Global Passport Index (Global Citizen Solutions) differs from the Henley index (visa-free destinations).',
         src='Jul 2026 CA (conflict areas; §3.9.4; §3.9.3).', why_label='What happened'),
    live_quick('2025-26', [
        '**Operation Sindhu (2025):** the extended-neighbourhood handout gives the numbers: **3,597 Indians evacuated from Iran and 818 from Israel**.',
        '**Hormuz and the Gulf (Aug magazine):** the Iran conflict disrupted the Strait of Hormuz; nearly ten million Indians live in GCC states (handout), so West Asian instability is the largest single diaspora risk.',
        '**H-1B fee (web):** a US$100,000 H-1B fee was announced in September 2025.',
    ], src='Merged handout (West Asia, p. 81); Aug 2026 CA §3.9.2; web: collected for the PYQ Lab.'),
]

RADAR_ROWS = [
    ['Jan 2026', 'MEA: the diaspora is “a living bridge” (Pravasi Bharatiya Divas)', 'Why it matters', 'Became Mains 2026 Q19'],
    ['Jul 2026', 'e-OCI card launched', 'Who the diaspora is · way forward', 'Connect; digital consular capacity'],
    ['Jul 2026', 'Odesa strike kills four Indian sailors', 'Challenges', 'Conflict risk beyond West Asia'],
    ['Jul 2026', 'US fixed-stay rule for F, J, I visas; Passport Index rank 125', 'Challenges', 'Immigration restrictions'],
    ['Aug 2026', '“Diaspora 2.0”; missions lack consultation mechanisms', 'Limits · way forward', 'Structured partnership'],
    ['Aug 2026', 'Mauritius visit; Aapravasi Ghat', 'Why it matters', 'Girmitiya soft power'],
    ['2025', 'Operation Sindhu: 3,597 from Iran, 818 from Israel', 'Evacuation diplomacy', 'Consular preparedness'],
]
WATCH = [
    '**Overseas Mobility (Facilitation and Welfare) Bill, 2024:** passed or still pending?',
    '**A national migration database** (Standing Committee, 2025): any start?',
    '**West Asia:** any new evacuation, and Gulf labour reforms.',
    '**US, UK, Canada, Australia visa and student rules.**',
    '**Remittance figures** for FY26 (compare with US$135.4 bn in FY25).',
]
CHAIN = [
    ('A huge, mixed community', '37 million: workers, professionals, students, Girmitiya.'),
    ('Real value to India', 'US$135.4 bn remittances, lobbying, soft power, knowledge.'),
    ('Real limits', 'Consumption remittances, host-country loyalties, culture without votes.'),
    ('Real risks', 'Wars (Iran, Odesa), visa rules, discrimination, separatist fringes.'),
    ('The answer', 'Care, Connect, Celebrate, Contribute; a law and a database to match.'),
]


def radar():
    return [
        p('The newsroom for Chapter 4. Items come from the July and August 2026 current-affairs magazines and the merged handout; web items are marked.'),
        tbl('What happened, and where it plugs into this chapter', ['When', 'News', 'Plugs into', 'Exam angle'], RADAR_ROWS),
        h3('Connect the dots'),
        flow('Five steps, one argument', CHAIN),
        p('**4-line opener:** “India’s diaspora is the world’s largest and its remittances the world’s highest. It lobbies, teaches and carries Indian culture abroad, but it votes as citizens of other countries. Wars and visa rules turn its welfare into foreign policy. The 4 Cs need a modern law and real data behind them.”'),
        h3('Watch next'),
        '<ul class="watch-list">' + ''.join('<li>%s</li>' % inline(x) for x in WATCH) + '</ul>',
    ]


MCQ = [
    ('The e-OCI card launched in 2026 provides:', ['Voting rights to OCIs', 'Fully digital OCI services', 'Dual citizenship', 'An Indian passport to PIOs'], 1, 'Fully digital OCI services (July 2026 magazine). An OCI is a foreign citizen of Indian origin with a lifelong visa.'),
    ('Aapravasi Ghat, a UNESCO World Heritage Site, is in:', ['Fiji', 'Guyana', 'Mauritius', 'Trinidad and Tobago'], 2, 'Port Louis, Mauritius: the immigration depot of the indentured-labour “great experiment”.'),
]
CARDS = [
    ('Live: where did “living bridge” come from?', 'The MEA’s Pravasi Bharatiya Divas statement (9 Jan 2026); it became the wording of Mains 2026 GS-II Q19.'),
    ('Live: e-OCI card?', 'Fully digital OCI services (July 2026); launched with the FCRA 2.0 portal.'),
    ('Live: “Diaspora 2.0”?', 'From ceremonial engagement to structured partnership on skills, investment and second-generation culture (Aug 2026 magazine).'),
    ('Live: Operation Sindhu numbers?', '3,597 Indians from Iran and 818 from Israel (2025).'),
]
