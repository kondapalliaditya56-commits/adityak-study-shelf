# -*- coding: utf-8 -*-
"""Chapter 5 live current-affairs layer (Jul and Aug 2026 CA magazines; web items labelled)."""
from lib import *

AUG = 'Aug 2026 CA'
JUL = 'Jul 2026 CA'
LIVE = {}

LIVE['West Asia: three axes and the major powers'] = [
    live_head('the Gulf hedges'),
    live(AUG, 'Saudi Arabia, Türkiye and Pakistan sign a mutual-defence pact',
         'The **Mecca Joint Defence Agreement** treats an attack on one as an attack on all three. Trigger: the **US-Israel war on Iran** raised Gulf doubts about the US security umbrella. Washington **welcomed it as burden-sharing**. But there is no integrated command, no published text and no common enemy (Saudi Arabia looks at Iran, Türkiye at Israel, Pakistan at India).',
         'A live example of the handout’s line that Gulf states are “diversifying both their economies and foreign relations”, and of the US-as-security-actor row in the major-powers table. For India it touches the Pakistan factor in West Asia.',
         'Legal basis: **UN Charter Article 51**. Builds on the **Saudi-Pakistan Strategic Mutual Defence Agreement (September 2025)**.',
         src='Aug 2026 CA §3.2 (MJDA).'),
]

LIVE['India-Israel and the Palestine question'] = [
    live_head('the economic track with Israel'),
    live(JUL, 'The India-Israel investment treaty enters into force',
         'The **India-Israel Bilateral Investment Agreement**, signed in **September 2025**, entered into force. Israel is the **first OECD country** to sign India’s new-generation investment model (the **2015 Model BIT**).',
         'Pairs with the handout’s February 2026 Special Strategic Partnership and the July 2026 FTA round: the relationship is gaining an economic spine to match defence and technology. Useful for the “depth and diversity” in the 2018 PYQ.',
         'BITs are sources of international law under **Article 38(1)(a) of the ICJ Statute**. Other recent Indian BITs: Uzbekistan, UAE, Brazil, Kyrgyzstan, Belarus.',
         src='Jul 2026 CA §3.8.4.'),
]

LIVE['India-Iran and India-Gulf'] = [
    live_head('Iran, Hormuz and the Gulf in the news'),
    live(AUG + ' + web', 'Hormuz: “reopen for 60 days”, then new routes but no reopening',
         'The August magazine reports **Iran and Oman agreeing to reopen the Strait of Hormuz for 60 days** (about **20% of world oil and LNG** passes through it). On **13 September 2026** the two agreed details of **new entry and exit routes**, entry wholly in Iranian waters; Iran said this was **not a reopening** and set conditions for the US.',
         'This is the handout’s 2026 concern (“freedom of navigation through Hormuz”) as it unfolded. Note the handout’s Oman row: Oman matters for “maritime access near the Strait of Hormuz”.',
         'PYQ (2026, Prelims, quoted in the magazine): Bahrain and Qatar ships must cross Hormuz; Syria and Egypt’s need not.',
         flag='The two reports differ on whether the strait reopened. Check the latest status before the exam.',
         src='Aug 2026 CA §3.9.2; web: Newsonair, 13 Sep 2026.'),
    live_quick('Jul-Aug 2026', [
        '**Chabahar:** US forces destroyed a surveillance tower at the **Shahid Kalantari** port; India’s **Shahid Beheshti** terminal (India Ports Global Limited) is beside it (July magazine).',
        '**OPEC:** the **UAE exited OPEC in May 2026**; seven OPEC+ countries raised output (August magazine).',
        '**US-Saudi 123 Agreement:** a 30-year civil nuclear framework under Section 123 of the US Atomic Energy Act (India’s own 123 Agreement: 2008) (July magazine).',
    ], src='Jul 2026 CA conflict areas, §3.9.5; Aug 2026 CA §3.8.2.'),
]

LIVE['West Asia: stakes, challenges and way forward'] = [
    live_head('the second chokepoint'),
    live(JUL, 'The Houthis declare a naval blockade at Bab-el-Mandeb',
         'Yemen’s Iran-backed **Houthis declared a naval blockade against Saudi Arabia**. **Bab-el-Mandeb** joins the Red Sea to the Gulf of Aden and is one of five major chokepoints (with Hormuz, Malacca, the Panama Canal and the Turkish Straits).',
         'The handout’s challenge row “Disruption of Bab-el-Mandeb and the Red Sea can force ships towards longer routes around Africa” in the news. Way forward: diversify suppliers, maritime domain awareness, **Operation Sankalp**.',
         'Five chokepoints: Hormuz, Malacca, Bab-el-Mandeb, Panama Canal, Turkish Straits.',
         src='Jul 2026 CA (conflict areas).'),
]

LIVE['India-ASEAN: nature, evolution and convergence'] = [
    live_head('Act East in July 2026'),
    live(JUL, 'BrahMos for Indonesia, Sabang revived, ASEAN forums in Manila',
         'In **Jakarta**, India agreed to supply **BrahMos** (Indonesia is the second Southeast Asian buyer after the Philippines), to revive **Sabang** port, and Indonesia will post a liaison officer at **IFC-IOR**; **local currency transaction** guidelines; an **IIM Bangalore** campus in Indonesia. The External Affairs Minister attended the **ASEAN-India, EAS and ARF** foreign ministers’ meetings in **Manila**; **2026 is the ASEAN-India Year of Maritime Cooperation**.',
         'Matches the handout’s 2026 row (“PM Modi’s Indonesia visit advanced defence, critical minerals, agriculture, industry and maritime cooperation”). Use it as evidence that Act East is gaining a security edge.',
         '**ARF** (1994, foreign ministers, 27 members) versus **EAS** (2005, leaders, 19 members); India joined ARF in 1996 and was a founding EAS member. **IPOI** was announced at the 2019 EAS, Bangkok.',
         src='Jul 2026 CA §3.4, §3.8.2.', why_label='What happened'),
]

LIVE['India-ASEAN: challenges and way forward'] = [
    live_head('the South China Sea factor'),
    live(AUG, 'China writes rules for Scarborough Shoal',
         'China issued rules for a **Huangyan Dao National Nature Reserve** at **Scarborough Shoal**; the **Philippines** had deposited its chart of the shoal with the UN. The **2016 UNCLOS award** found no basis for China’s historic rights and held the shoal a **rock** under Article 121(3).',
         'The handout says India wants an Indo-Pacific order “without being drawn into... the South China Sea disputes”, and that ASEAN’s interdependence with China limits convergence. This is why: ASEAN members are divided on how hard to push.',
         'Over **55%** of India’s trade passes through the South China Sea and Malacca (MEA, quoted in the magazine).',
         src='Aug 2026 CA §3.5.'),
]

LIVE['The Indo-Pacific: significance and competing visions'] = [
    live_head('the Indo-Pacific in the 2026 paper'),
    live('Mains 2026 + web', 'IPMDA: a 2026 question on SAGAR and the Quad',
         'GS-II Q9 (10 marks) asked for a critical assessment of whether **IPMDA** (Indo-Pacific Partnership for Maritime Domain Awareness) “bridges the gap between India’s SAGAR vision and the Quad’s collective Indo-Pacific strategy”. Three months earlier, the **Quad foreign ministers met in New Delhi (26 May 2026)** and noted IPMDA’s Indian Ocean programme run through **IFC-IOR, Gurugram**.',
         'The material only names IPMDA, but this chapter gives the parts: India’s inclusive vision versus the US deterrence model, IFC-IOR, and maritime domain awareness in the strategy table. Write it as “bridge, partly”.',
         'SAGAR = Security and Growth for All in the Region; extended as MAHASAGAR.',
         src='Chapter 1 handout PYQ list; web: Quad joint statement, 26 May 2026 (collected for the PYQ Lab).', why_label='What was asked'),
]

LIVE['The Indo-Pacific: challenges and India’s strategy'] = [
    live_head('partners joining India’s initiatives'),
    live_quick('Jul 2026', [
        '**New Zealand joined the maritime-security pillar of India’s IPOI** and signed a Mutual Logistics Support Arrangement during the first Indian PM visit in 40 years.',
        '**Australia:** a temporary space-tracking terminal on the **Cocos (Keeling) Islands** for Gaganyaan; a Maritime Security Collaboration Roadmap; the **Critical Minerals Corridor**.',
        '**Japan:** an Economic Security declaration (semiconductors, critical minerals) and alignment of India’s MAHASAGAR with Japan’s updated **FOIP**.',
    ], src='Jul 2026 CA §3.5, §3.1, §3.2.'),
]

LIVE['India-Central Asia'] = [
    live_head('Central Asia in the magazines'),
    live_quick('Jul 2026', [
        '**Uranium:** Australia has the largest uranium resources, but **Kazakhstan is the largest producer** (July magazine). This is why Kazakhstan is India’s Central Asian energy partner in the handout.',
        '**Investment treaties:** Uzbekistan and Kyrgyzstan are among India’s recent BIT partners (with the UAE, Brazil and Belarus).',
        '**Chabahar under fire:** the July US strike near India’s terminal and the lapse of the US waiver (April 2026, handout) both weaken the route the handout calls India’s answer to the Pakistan barrier.',
        '**Check:** the two magazines carry no India-Central Asia headline of their own.',
    ], src='Jul 2026 CA §3.1 (Prelims fodder), §3.8.4, conflict areas.'),
]

LIVE['India-Africa'] = [
    live_head('Africa in the 2025 paper and the news'),
    live('Mains 2025 + web', 'The exam asked about India-Africa digital partnership',
         'GS-II 2025 Q9: “India-Africa digital partnership is achieving mutual respect, co-development and long-term institutional partnerships. Elaborate.” Six weeks earlier, on the PM’s **Namibia** visit (9 July 2025), NPCI and the Bank of Namibia signed a **UPI licensing agreement**.',
         'Not in this handout’s PYQ box, but the material covers it: the Kampala Principle on **sharing DPI**, the **Pan-African e-Network** and **e-VBAB**, and the handout’s line on Namibia and digital payments.',
         'UPI is live across 11 jurisdictions (August magazine). The **2021** question on Africa’s growth story is the other recent Africa PYQ.',
         src='PYQ Lab (published 2025 papers); web: The Tribune, July 2025.', why_label='What was asked'),
    live_quick('Jul-Aug 2026', [
        '**SACU:** India and the Southern African Customs Union (Botswana, Eswatini, Lesotho, Namibia, South Africa; est. 1910, secretariat Windhoek) signed Terms of Reference for a **Preferential Trade Agreement**.',
        '**South Sudan:** India condemned an attack on **UNMISS** peacekeepers in Jonglei State. **Sudan:** RSF crimes in **El Fasher** (Amnesty).',
        '**ICC:** **Chad** notified withdrawal, citing a concentration of investigations on Africa (9 of 13 investigations concern African states).',
        '**Zanzibar:** **IIT Madras** opened the first IIT campus outside India.',
    ], src='Aug 2026 CA §3.8.3, §3.9.4; Jul 2026 CA §3.7, conflict areas, high-level visits.'),
]

LIVE['India-Latin America and the Caribbean'] = [
    live_head('Latin America in the magazines'),
    live_quick('Jul-Aug 2026', [
        '**PTA examples:** the August magazine uses **India-MERCOSUR** and **India-Chile** as its examples of Preferential Trade Agreements (positive list), against FTAs (negative list).',
        '**Lithium:** **KABIL** has secured lithium exploration rights in **Argentina** (August magazine, mineral-sector reforms).',
        '**Venezuela:** has started withdrawal from the **ICC** (July magazine); it remains an **OPEC** member (August magazine). The handout lists “crises in countries such as Venezuela” as a risk to energy supplies.',
        '**Check:** neither magazine carries an India-Brazil or India-CARICOM headline.',
    ], src='Aug 2026 CA §3.8.3, mineral-sector reform, §3.8.2; Jul 2026 CA §3.7.'),
]

RADAR_ROWS = [
    ['Aug 2026', 'Mecca pact (Saudi, Türkiye, Pakistan)', 'West Asia axes', 'Gulf hedging'],
    ['Aug-Sep 2026', 'Hormuz: 60-day reopening reported; new routes agreed (Sep), strait not reopened', 'Iran and the Gulf', 'Energy, navigation'],
    ['Jul 2026', 'Houthi blockade at Bab-el-Mandeb; Chabahar strike', 'West Asia stakes', 'Chokepoints; routes'],
    ['Jul 2026', 'India-Israel BIT in force', 'India-Israel', 'Economic depth'],
    ['Aug 2026', 'UAE exits OPEC', 'Gulf', 'Diversifying Gulf'],
    ['Jul 2026', 'Indonesia: BrahMos, Sabang; ASEAN forums in Manila', 'ASEAN', 'Act East with security'],
    ['Aug 2026', 'Scarborough Shoal reserve rules', 'ASEAN challenges', 'South China Sea'],
    ['May-Aug 2026', 'Quad FMM in Delhi; IPMDA asked in Mains', 'Indo-Pacific', 'SAGAR and the Quad'],
    ['Jul 2026', 'NZ joins IPOI pillar; Australia, Japan summits', 'Indo-Pacific strategy', 'Partnerships'],
    ['Aug 2026', 'SACU PTA talks; UNMISS attack; Chad leaves ICC', 'Africa', 'Trade; security; governance'],
    ['Aug 2026', 'KABIL lithium in Argentina; MERCOSUR and Chile PTAs as examples', 'Latin America', 'Minerals; trade'],
]
WATCH = [
    '**Hormuz:** does the strait reopen, and on whose terms?',
    '**India-GCC FTA** (talks since February 2026) and the **India-Israel FTA** rounds.',
    '**Chabahar:** sanctions after the April 2026 waiver lapse.',
    '**AITIGA review (2026)** outcome; the ASEAN-India Year of Maritime Cooperation.',
    '**India-EAEU FTA** talks (ToR August 2025).',
    '**IAFS-IV:** a new date after the Ebola postponement.',
    '**Mexico’s tariffs** and the India-MERCOSUR protocol; Chile CEPA; Peru FTA.',
]
CHAIN = [
    ('One region at war', 'The US-Israel-Iran conflict: Hormuz, Bab-el-Mandeb, Chabahar.'),
    ('Partners hedge', 'Gulf pacts, UAE leaves OPEC, ASEAN balances China.'),
    ('India diversifies', 'Oman CEPA, GCC FTA talks, Indonesia deals, SACU PTA, MERCOSUR.'),
    ('China outscales India', 'ASEAN FTA 3.0; US$106 bn Central Asia; US$549 bn Latin America.'),
    ('The test is delivery', 'Chabahar, IMEC, Kaladan, INSTC, IAFS.'),
]


def radar():
    return [
        p('The newsroom for Chapter 5. Items come from the July and August 2026 current-affairs magazines; web items are marked. The handout itself runs to September 2026, so many “latest” facts are already in the notes.'),
        tbl('What happened, and where it plugs into this chapter', ['When', 'News', 'Plugs into', 'Exam angle'], RADAR_ROWS),
        h3('Connect the dots'),
        flow('Five steps, one argument', CHAIN),
        p('**4-line opener:** “India’s extended neighbourhood is being reshaped by a war in West Asia and by China’s scale everywhere else. India’s answer is diversification: new trade deals from Oman to the Southern Cone, defence ties from Jakarta to Abu Dhabi. Its weakness is delivery on corridors.”'),
        h3('Watch next'),
        '<ul class="watch-list">' + ''.join('<li>%s</li>' % inline(x) for x in WATCH) + '</ul>',
    ]


MCQ = [
    ('In 2026, which Southeast Asian country agreed to acquire BrahMos as the second buyer in the region?', ['Vietnam', 'Indonesia', 'Malaysia', 'Thailand'], 1, 'Indonesia, after the Philippines (July 2026 magazine).'),
    ('Which country joined the maritime-security pillar of India’s Indo-Pacific Oceans Initiative in 2026?', ['New Zealand', 'Canada', 'South Korea', 'Chile'], 0, 'New Zealand, during the first Indian PM visit in 40 years.'),
    ('SACU, with which India began PTA talks, has its secretariat at:', ['Pretoria', 'Gaborone', 'Windhoek', 'Maseru'], 2, 'Windhoek, Namibia. Members: Botswana, Eswatini, Lesotho, Namibia, South Africa.'),
]
CARDS = [
    ('Live: Mecca pact and West Asia?', 'Saudi-Türkiye-Pakistan collective defence after the US-Israel war on Iran; the US welcomed it; no integrated command.'),
    ('Live: India-Israel BIT?', 'Signed Sept 2025, in force 2026; Israel is the first OECD country on India’s 2015 Model BIT.'),
    ('Live: Bab-el-Mandeb?', 'Houthis declared a naval blockade against Saudi Arabia; Red Sea to Gulf of Aden.'),
    ('Live: Indonesia deals (July 2026)?', 'BrahMos, Sabang revival, IFC-IOR liaison officer, local-currency guidelines, IIM Bangalore campus.'),
    ('Live: Mains 2025 Africa question?', 'India-Africa digital partnership (Q9); Namibia UPI licensing agreement (July 2025).'),
    ('Live: KABIL?', 'Lithium exploration rights in Argentina.'),
]
