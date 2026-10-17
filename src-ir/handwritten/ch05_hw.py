# -*- coding: utf-8 -*-
"""Chapter 5: extended neighbourhood. Source: PPT-7.2, PPT-7, merged handout pp. 78-100; CA Jul/Aug 2026."""
from dsl import *
from hwlib import P, H, R

CA = lambda t, src: bx('ca', '<span class="tag">In the news · %s</span>%s' % (src, t))
IMG = lambda src, cap, h=56: bx('figw', '<img src="../../img/%s" style="max-height:%dmm;max-width:100%%;display:block;margin:1mm auto;border:1.4px solid #1a237e;border-radius:3px"><div class="cap" style="text-align:center">%s</div>' % (src, h, cap))
PH = lambda t: bx('pk', '<b>Slide phrase:</b> ' + t)

CHS = [
dict(toc='Extended neighbourhood', id=5, title='EXTENDED NEIGHBOURHOOD', part=1, icon='globe',
 pyq='Mains 2024 · 2021 (×2) · 2018 (×2) · 2016 · 2015',
 simple='Six regions beyond South Asia feed India\'s energy, trade, minerals and security. In every one, India\'s problem is less intent than delivery.',
 pages='PPT-7.2 · PPT-7 · handout pp. 78-100', prio='H',
 nodes=[
 tb(['Direction', 'Region', 'Why it matters'],
    ['West', 'West Asia, Gulf', 'energy, investment, diaspora'], ['Northwest', 'Central Asia', 'connectivity, resources'],
    ['W/SW', 'Africa', 'markets, minerals, Global South'], ['East', 'ASEAN, East Asia', 'trade, tech, production networks'],
    ['Maritime arc', 'Indo-Pacific', 'sea lanes, blue economy'], ['Across the Atlantic', 'Latin America', 'energy, minerals, markets']),
 mn('W-C-A-A-I-L', '"<b>W</b>e <b>C</b>an <b>A</b>lways <b>A</b>sk <b>I</b>ndia <b>L</b>ater" = West Asia, Central Asia, ASEAN, Africa, Indo-Pacific, Latin America. <i>(own mnemonic)</i>'),

 sec('WEST ASIA: "STRATEGIC ENGAGEMENT WITH CAREFUL BALANCING"', 'r'),
 bx('qt', '"West Asia is part of our extended neighbourhood." — <b>Jaishankar</b>. India\'s <b>energy, diaspora, connectivity, maritime corridor</b>: Hormuz, Bab-el-Mandeb, Red Sea, Suez.'),
 tl(('to 1947', 'trade, Sufism'), ('1947-70s', 'Arab nationalism, Palestine'), ('1970s-91', 'oil shocks, Gulf migration'), ('1992-2004', '<b>Israel ties 1992</b>'), ('2005-13', 'Look West'), ('2014-19', '<b>de-hyphenation</b>'), ('2020-23', 'I2U2, IMEC, Abraham Accords'), ('2023-26', 'Gaza, Red Sea, Iran war')),
 hub('3 AXES', ['ISRAEL-PALESTINE: 1917, 1947, 1948, 1967, 2020, 2023', 'IRAN: 1979; JCPOA 2015; 2026 war', 'GULF: GCC six, diversifying']),
 bx('bl', '<b>Israel-Palestine:</b> Balfour 1917 → UN plan 1947 → Israel 1948 → 1967 occupation → Abraham Accords 2020 (UAE, Bahrain) → 7 Oct 2023 → ceasefire 2025. <b>Iran:</b> 1979 revolution; JCPOA 2015, US exit 2018; 2026 US-Israel-Iran war hits Hormuz. <b>GCC:</b> Saudi, UAE, Qatar, Kuwait, Oman, Bahrain; Saudi has not normalised with Israel.'),
 two([IMG('ir-ext-israel-palestine.jpg', 'Israel-Palestine (slide 6)', 50)], [IMG('ir-ext-west-asia.jpg', 'West Asia: India\'s interests (slide 9)', 50)]),
 bx('ye', '<b>Major powers (slide 8):</b> US = security actor, stop Iranian bomb · China = energy, BRI; brokered <b>Saudi-Iran 2023</b> · Russia = Iran ties, Syria 2015, OPEC+ · <b>India seeks relations across competing camps</b>.'),
 two([t('<b>Israel</b> ' + P('2018'), 'Recognised <b>1950</b>, full ties <b>1992</b>', '<b>Barak, Phalcon, Heron</b>; water, agri, cyber', 'Trade $3.93 bn; FTA round 2 (Jul 2026)', '<b>Special Strategic Partnership</b> (Feb 2026)', w=16)],
     [t('<b>Palestine</b>', '<b>De-hyphenated</b>', 'PM in <b>Ramallah 2018</b> (first)', '<b>Two-State solution</b>', 'Humanitarian aid continues', w=16)]),
 PH('"<b>Cooperation with Israel without abandoning support for Palestinian statehood</b>" (slide 11).'),
 two([t('<b>Iran</b>', '<b>Chabahar</b>: bypass Pak; <b>Shahid Beheshti 10-yr contract (May 2024)</b>', 'INSTC hub', 'Limits: sanctions, banking, war', '<b>Op Sindhu 2025</b>: 3,597 from Iran, 818 from Israel', w=16)],
     [t('<b>Gulf</b>', 'GCC trade <b>$178.56 bn</b> (FY25); ~<b>10 mn</b> Indians', '<b>UAE:</b> CEPA 2022; $101.25 bn; target $200 bn by 2032; rupee-dirham; IMEC', '<b>Saudi:</b> SPC 2019; defence committee 2025', '<b>Qatar</b> LNG · <b>Oman</b> Duqm; <b>CEPA 1 Jun 2026</b> · GCC FTA talks (Feb 2026)', w=16)]),
 t('<b>Challenges</b> (slide 17)', 'Balancing harder after 2026 US-Israel-Iran war', '<b>Hormuz, Red Sea</b> → freight, insurance, inflation', 'IMEC slowed; Chabahar sanctioned → need <b>multiple routes</b>', 'Workers: passport retention, recruitment abuse', '<b>OIC</b> on J&amp;K', w=22),
 bx('gr', '<b>Close (slide 18):</b> simultaneous engagement with competing actors; strategic autonomy, diversified partners, secure energy and sea routes, citizen protection <b>without rigid regional alignments</b>. Build <b>both Chabahar and IMEC</b>; more SPR; Op Sankalp.'),
 CA('Mecca Joint Defence Agreement (Saudi-Türkiye-Pak); India-Israel BIT in force (first OECD country on the 2015 model); Hormuz "reopen for 60 days", then new routes but no reopening (13 Sep 2026); Houthi blockade at Bab-el-Mandeb; UAE left OPEC (May 2026).', 'Jul-Aug 2026 CA'),

 sec('ASEAN: "CONVERGENCE, UNDER-REALISED ECONOMICS" ' + P('2016'), 'b'),
 bx('qt', '"ASEAN centrality is at the heart of India\'s Act East Policy" — PM, Vientiane 2024. ASEAN = <b>11</b> members (Timor-Leste 2025).'),
 two([IMG('ir-ext-asean.jpg', 'ASEAN (slide 20)', 50)],
     [tl(('1991', 'Look East'), ('1992 / 1995', 'Sectoral → Dialogue'), ('2002 / 2010', 'Summit; AITIGA'), ('2014', 'Act East'), ('2019', 'IPOI'), ('2022', 'CSP'), ('2025-26', 'Prabowo; Indonesia visit'))]),
 two([t('<b>Convergence</b>', 'Trade <b>$128.38 bn</b> (~10%); FDI $3.5 bn', 'Trilateral Highway, Kaladan', '<b>UPI-PayNow</b> (19 banks); 5.9 mn travellers', 'ASEAN Power Grid; Indonesia nickel', '<b>2026 Year of Maritime Cooperation</b>; AIME 2026', w=18)],
     [t('<b>Challenges</b>', 'Deficit <b>~$51.55 bn</b>', '<b>RCEP exit</b>; rules of origin', 'China: <b>ASEAN-China FTA 3.0</b> (2025)', 'Kaladan, Myanmar delays', 'mineral processing concentrated', w=18)]),
 bx('gr', '<b>Close (slide 24):</b> move from <b>strategic convergence to economic integration, connectivity, maritime cooperation</b>; "beyond ASEAN centrality as a slogan"; Viksit Bharat 2047 + ASEAN 2045.'),
 CA('<b>BrahMos for Indonesia</b> (2nd SE Asian buyer); <b>Sabang</b> revived; Indonesian officer at IFC-IOR. China\'s rules for <b>Scarborough Shoal</b> (2016 award: a rock). 55%+ of India\'s trade crosses SCS + Malacca.', 'Jul-Aug 2026 CA'),

 sec('INDO-PACIFIC ' + P('2021 AUKUS'), 'g'),
 two([IMG('ir-ext-indo-pacific.jpg', 'Indo-Pacific: E. Africa to the Americas (slide 25)', 48)],
     [t('<b>Why it matters</b>', 'Chokepoints: <b>Malacca, Hormuz, Bab-el-Mandeb</b>', 'Supply chains; Northeast gateway', 'Minerals: Australia, Indonesia', '<b>A&amp;N</b> near Malacca; IFC-IOR, Op Sankalp', w=16)]),
 tb(['Who', 'Preferred order'], ['<b>India</b>', 'free, open, inclusive, <b>multipolar</b>; ASEAN centrality; <b>no formal alliance</b>'], ['US', 'alliances, forward presence, <b>deterrence of China</b>'], ['China', 'against "containment" groupings'], ['ASEAN', 'centrality, no blocs'], ['Japan', '<b>FOIP</b>'], ['Australia', 'rules + deterrence']),
 t('<b>India\'s strategy</b> (slide 29)', 'No <b>formal anti-China bloc</b>; China = <span class="hl">dialogue + deterrence + de-risking</span>', 'Link <b>IPOI</b> with ASEAN\'s <b>AOIP</b>', 'IFC-IOR, satellites; Quad, IORA, ADMM-Plus, EAS, MILAN', 'Minerals: access + processing + refining + recycling', w=22),
 bx('ye', '<b>Thin notes:</b> AUKUS only named. Frame: AUKUS adds a military-tech layer; inclusive forums India prefers continue → "complement, not replacement". <b>Handout alert:</b> "Divzd cooperation…" line garbled.'),
 CA('Mains 2026 asked if <b>IPMDA</b> bridges <b>SAGAR</b> and the Quad. Quad FMM, New Delhi (26 May 2026, web). New Zealand joined IPOI\'s maritime pillar; Japan aligned FOIP with MAHASAGAR.', 'Jul 2026 CA + web'),

 sec('CENTRAL ASIA: "A GEOGRAPHY GAP, NOT AN INTEREST GAP" ' + P('2024 · 2018'), 'r'),
 two([IMG('ir-ext-central-asia.jpg', 'Kazakh uranium · Uzbek minerals · Turkmen gas · Kyrgyz education · Tajik security (slide 32)', 52)],
     [tl(('2012', 'Connect Central Asia'), ('2015', 'PM in all 5'), ('2017', 'SCO'), ('2018', 'Ashgabat'), ('2019', 'Dialogue'), ('2022', '1st Summit'), ('2026', 'Uzbek CSP'))]),
 two([t('<b>Convergence</b>', 'Uzbek trade $1.3 bn; Rare Earth Forum 2024; Uzbek MoU 2026', '<b>Kazakh uranium</b>; TAPI (stalled)', 'INSTC cargo to Kazakhstan (Mar 2025)', 'DUSTLIK 2026; Afghanistan, terror, drugs', '16,000 students in Kyrgyzstan; all 5 back UNSC bid', w=18)],
     [t('<b>Challenges</b>', 'No land route (Pak)', 'China trade <b>$106.3 bn</b>', '<b>Chabahar waiver lapsed (Apr 2026)</b>', 'Afghan militancy; Bishkek 2024 violence', w=18)]),
 bx('gr', '<b>Close (slide 35):</b> "<b>Connect Central Asia 2.0</b>": INSTC + Ashgabat + <b>EAEU FTA</b> (ToR Aug 2025) + SCO. Kazakhstan = largest uranium producer (Jul CA).'),

 sec('AFRICA: "FROM GOODWILL TO DELIVERY" ' + P('2021 · 2015'), 'g'),
 bx('qt', '"Africa will be at the top of our priorities." — PM, Uganda 2018. Ansari: a "<b>Two-Way street</b>".'),
 two([IMG('ir-ext-africa.jpg', 'Africa: India\'s interests (PPT-7 slide 5)', 54)],
     [tl(('to 1990s', 'anti-apartheid, NAM'), ('2004', 'Pan-African e-Network'), ('2008', 'IAFS-I'), ('2018', 'Kampala Principles'), ('2023', 'AU in G20'), ('2026', 'IAFS-IV postponed (Ebola)'))]),
 two([t('<b>Convergence</b>', 'Trade <b>$93.69 bn</b> (slide); <b>AfCFTA</b> 1.3 bn people', 'Minerals: lithium, copper, rare earths', 'Energy: Nigeria, Angola, Mozambique; ISA', '<b>e-VBAB</b>, ITEC, LoCs', 'AIKEYME 2025; IADD; UNSC reform', w=18)],
     [t('<b>Gaps</b>', 'Footprint far below <b>China</b>', 'Pharma quality; standards', 'Many rivals: US, EU, Russia, Türkiye, UAE', 'Sahel, Horn; <b>Op Kaveri 2023</b>', 'Delays; Red Sea; racial attacks in India; W. Africa neglected', w=18)]),
 bx('ye', '<b>Kampala Principles (2018), 10:</b> Africa a priority · African priorities · open markets · <b>share DPI</b> · agriculture · climate · counter-terror + UN peacekeeping · open oceans · <b>no external rivalry</b> · fairer global order.'),
 bx('gr', '<b>Close (slide 9):</b> move <b>from goodwill to delivery</b>, aligned with <b>Agenda 2063</b>; regular IAFS; local processing; Africa Growth Fund.'),
 CA('Mains 2025 asked on India-Africa <b>digital partnership</b>; NPCI-Bank of Namibia UPI licence (Jul 2025, web). India-SACU PTA terms signed; Chad leaving the ICC.', 'Jul-Aug 2026 CA + web'),

 sec('LATIN AMERICA &amp; CARIBBEAN', 'b'),
 two([IMG('ir-ext-latam.jpg', 'LAC: India\'s interests (PPT-7 slide 13)', 50)],
     [t('<b>Story</b>', 'Indentured diaspora: Guyana, T&amp;T, Suriname', 'PTAs: <b>MERCOSUR, Chile (2006)</b>; CELAC', '<b>KABIL lithium, Argentina</b>; 2nd CARICOM summit', '2025-26 visits: T&amp;T, Argentina, Brazil', w=16)]),
 two([t('<b>Convergence</b>', 'Brazil trade $15.21 bn; Chile CEPA talks', 'India-Brazil minerals MoU 2026; ethanol, <b>Global Biofuels Alliance</b>', 'G4 (India-Brazil); IBSA, BRICS', '1,000 ITEC slots for CARICOM; Hurricane Melissa relief', w=18)],
     [t('<b>Gaps</b>', 'Mexico tariffs up to 50% (2026)', 'China-LAC <b>$549 bn</b>', 'Distance, Panama Canal', 'Argentina, Mexico in <b>Uniting for Consensus</b>', 'Language; Venezuela crisis', w=18)]),
 bx('gr', '<b>Close (slide 16):</b> logistics, reliable projects, resilient chains can <b>turn distance into partnership</b>. "Commercially promising but strategically underdeveloped" (handout). Target $100 bn trade; Peru FTA, Chile CEPA.'),

 sec('SIX REGIONS IN ONE TABLE', 'r'),
 tb(['Region', 'Phrase', 'India trade', 'China comparison'],
    ['West Asia', 'careful balancing', 'GCC $178.56 bn', 'Gulf energy, BRI'], ['ASEAN', 'under-realised economics', '$128.38 bn', 'ASEAN-China FTA 3.0'],
    ['Indo-Pacific', 'inclusive, no bloc', '—', 'grey-zone, ports'], ['Central Asia', 'geography gap', 'Uzbek $1.3 bn', '$106.3 bn'],
    ['Africa', 'goodwill → delivery', '$93.69 bn', 'far ahead'], ['Latin America', 'distance → partnership', 'Brazil $15.21 bn', '$549 bn']),

 sec('PYQ ANSWER FRAMES', 'b'),
 tb(['PYQ', 'Approach', 'Body'],
    ['<b>2024</b> Central Asia (10m)', 'Component', 'diplomatic · economic · strategic · significance · critically'],
    ['<b>2021</b> India in Africa (10m*)', 'PESTEL', 'AU in G20 · trade · ITEC · DPI · ISA → China gap'],
    ['<b>2021</b> AUKUS (15m)', 'Level analysis', 'bilateral → regional → global → verdict'],
    ['<b>2018</b> Israel "rolled back" (10m)', 'Temporal', '1950 → 1992 → 2026 SSP → limits'],
    ['<b>2018</b> Ashgabat (10m)', 'Supply chain', 'port → INSTC → Central Asia, gains + risks'],
    ['<b>2016</b> Look East (12.5m)', 'Temporal', '1991-2010 · 2014-19 · 2022-26 → verdict'],
    ['<b>2015</b> Africa pros, cons', 'SWOT', 'S · W · O · T → net positive if delivered']),
 bx('pk', '<b>Handout errors:</b> 2018 Israel question says "<b>rolled back</b>" (handout: "overlooked"); 2021 Africa = <b>10 marks</b> (handout: 15).'),
 ],
 recall=[('Six regions mnemonic?', 'WCAAIL'), ('Three West Asia axes?', 'Israel-Palestine, Iran, Gulf'),
         ('Israel ties: recognised / full?', '1950 / 1992'), ('Shahid Beheshti contract?', '10 years, May 2024'),
         ('India-Oman CEPA in force?', '1 June 2026'), ('ASEAN deficit?', '~US$51.55 bn'),
         ('India on China in Indo-Pacific?', 'Dialogue + deterrence + de-risking'), ('Central Asia phrase?', 'Geography gap, not interest gap'),
         ('Kampala Principles year?', '2018 (10 principles)'), ('Africa close?', 'Goodwill → delivery, Agenda 2063'),
         ('China-LAC trade?', '~US$549 bn (2025)')]),
]
