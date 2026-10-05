# -*- coding: utf-8 -*-
"""Chapter 1 live current-affairs layer. Facts come only from the Aug 2026 and Jul 2026 current-affairs
magazines in the UPSC Project (plus two web items, labelled). Nothing here is from memory."""
from lib import *

AUG = 'Aug 2026 CA'
JUL = 'Jul 2026 CA'

LIVE = {}

LIVE['Phase 5: Crisis of Liberalism (post-2008)'] = [
    live_head('the crisis of liberalism, today'),
    live(AUG, 'From a 3% average to 18%: tariffs became the sharpest tool against a partner',
         'Free trade is the liberal order’s signature. In 2025 the US put a **25% reciprocal tariff** on Indian exports, then a **further 25%** tied to India’s Russian oil purchases: **50%** in all. A **February 2026 interim framework** cut it to **18%**, still far above the historical average of about **3%**.',
         'In a “waning globalisation” answer: the target was a partner, not a rival, and trade was used to punish an energy choice. Then add the way out: diversify (Europe, Gulf, Africa, Latin America, ASEAN, Japan) and finish the Bilateral Trade Agreement.',
         '**Mission 500** = double trade to **USD 500 bn by 2030**. **Trade Policy Forum**: set up in 2005, co-chaired by India’s Commerce Minister and the US Trade Representative. PYQ (2025): “With the waning of globalization, the post-Cold War world is becoming a site of sovereign nationalism. Elucidate.”',
         'Name two signs in the news that the liberal order is weakening.',
         'Tariffs on a partner (50% cut to 18%, against a 3% norm) and the ICC walk-outs (Chad, Burkina Faso, Mali, Niger, Venezuela). Either one anchors the “sovereign nationalism” PYQ.',
         src='Aug 2026 CA §3.3 (India-US trade relations); PYQ line quoted there.'),
    live(JUL, 'Five states walk out of the International Criminal Court',
         'Chad notified the UN Secretary-General of its withdrawal. **Burkina Faso, Mali, Niger and Venezuela** have also started withdrawal. Complaints: **9 of 13 investigations** concern African states, the Court has **no enforcement arm**, and the **US, China and Russia** are outside it. India is not a member either.',
         'A clean example of “global judicial ambition without universal participation”: universal rules, selective membership. Contrast with the African-led fix that worked: **Hissène Habré** (Chad’s own ex-President) convicted in **2016** by the Extraordinary African Chambers in Senegal.',
         '**Article 127, Rome Statute**: withdrawal takes effect **one year after notification**; the Court keeps jurisdiction over crimes committed while the State was a member. **ICC** tries individuals (four crimes, 125 States Parties, seat at The Hague); **ICJ** settles disputes between States.',
         'When does Chad’s withdrawal take effect, and does it erase past cases?',
         'One year after notification (Article 127). No: the Court keeps jurisdiction over crimes committed while Chad was a member.',
         src='Jul 2026 CA §3.7 (Chad’s withdrawal from the ICC).'),
    live_quick('Jul-Aug 2026', [
        '**US visas:** the Department of Homeland Security replaced “Duration of Status” for **F** (students), **J** (exchange visitors, researchers) and **I** (foreign journalists) visas with a **fixed authorised stay**. Borders as an instrument of nationalism.',
        '**“Lake America”:** the US renamed its federal reference to **Lake Ontario**; Canada keeps the existing name. Small story, big signal: even names of shared waters become sovereignty statements.',
    ], src='Jul 2026 CA §3.9.4; Aug 2026 CA §3.9.5 (conflict areas).'),
]

LIVE['Phase 6: Geopolitical fragmentation and strategic realignment (2020 onwards)'] = [
    live_head('fragmentation in real time'),
    live(AUG, 'Saudi Arabia, Türkiye and Pakistan: an attack on one is an attack on all three',
         'The **Mecca Joint Defence Agreement (MJDA)** treats an armed attack on any member as an attack on all. Trigger: the **US-Israel war on Iran** made Gulf states doubt the US security umbrella. It builds on the **Saudi-Pakistan defence pact of September 2025**. Each adds something: Saudi finance, Türkiye’s conventional forces and industry, Pakistan’s nuclear deterrent.',
         'Textbook **strategic hedging**. But call it what it is: **not an alliance**. No integrated command, no published treaty text, no common enemy (Saudi eyes Iran, Türkiye eyes Israel, Pakistan eyes India), and Türkiye stays in NATO while Saudi Arabia stays US-aligned. The US even welcomed it as burden-sharing.',
         '**UN Charter Article 51**: right of individual or collective self-defence until the Security Council acts. **IORA**: India chairs 2025-27. **I2U2**: India, Israel, UAE, US. **IMEC**: India-Middle East-Europe corridor.',
         'Why can’t MJDA be called an alliance?',
         'No integrated command, no published treaty text, no common adversary, and its members keep older ties (NATO, US alignment). India’s concerns: Pakistan’s access to Saudi money and Turkish drones, Türkiye on Kashmir, and Bangladesh’s interest in joining.',
         src='Aug 2026 CA §3.2 (MJDA).'),
    live(AUG + ' + web', 'The Strait of Hormuz: one narrow sea lane, the world’s nerves',
         'About **20% of the world’s oil and LNG** passes through it. The Iran conflict disrupted it: **Japan** faced fuel shortages and **India** had LPG supply worries (Jul 2026 CA). The August CA reports **Iran and Oman agreeing to reopen it for 60 days**. On **13 Sep 2026** the two agreed details of **new entry and exit routes** (entry wholly in Iranian waters); Iran says this is **not a reopening** and has set seven conditions for the US.',
         'Perfect for “chokepoints” and “energy security” answers: one lane links Gulf producers, Japan’s fuel and India’s cooking gas. Write it as a design lesson: diversify suppliers and build strategic reserves (India and Japan agreed to cooperate on **Strategic Petroleum Reserves**).',
         'PYQ (2026): ships from which countries cross Hormuz to reach the Indian Ocean? (Bahrain, Syria, Qatar, Egypt.) The strait lies between the **Persian Gulf and the Gulf of Oman**: Bahrain and Qatar sit inside the Gulf, so answer **(b) 1 and 3**.',
         'Which of the five listed chokepoints sits at the mouth of the Red Sea?',
         'Bab el-Mandeb (Houthis declared a naval blockade of Saudi Arabia there, Jul 2026 CA). The set: Hormuz, Malacca, Bab el-Mandeb, Panama Canal, Turkish Straits.',
         flag='Sources differ: the August CA says a 60-day reopening was agreed; the 13 Sep web report says routes were agreed but the strait is still not open. Treat the status as moving and re-check before the exam.',
         src='Aug 2026 CA §3.9.2; Jul 2026 CA §3.2 and conflict areas; web: Newsonair, 13 Sep 2026.'),
    live(JUL, 'Three chokepoints, one India: Hormuz, Bab el-Mandeb, Chabahar',
         'The **Houthis** declared a naval blockade of Saudi Arabia at **Bab el-Mandeb**. US forces destroyed a **surveillance tower at Iran’s Chabahar port (Shahid Kalantari)**. India’s own terminal there, **Shahid Beheshti, run by India Ports Global Limited**, gives access to Afghanistan and Central Asia **bypassing Pakistan**. Chabahar lies outside Hormuz, on the Gulf of Oman.',
         'The geography determinant in action: Pakistan blocks India’s direct land route, so Chabahar matters, and a US-Iran war puts it in the crossfire. Good for “Link West” and “connectivity” answers.',
         '**Chabahar** is on the Gulf of Oman, **outside** the Strait of Hormuz. In the notes, Chabahar is the first example of the **Diamond Necklace**.',
         src='Jul 2026 CA conflict areas (Bab el-Mandeb, Chabahar).'),
    live(JUL, 'Europe builds its own shield and its own energy scars',
         'Ten European states announced an **Integrated Anti-Ballistic Missile Coalition** in Paris: **Denmark, France, Germany, Italy, Netherlands, Norway, Spain, Sweden, Ukraine, UK**. Separately, German prosecutors said the **2022 Nord Stream sabotage** was ordered by Ukrainian state authorities. A Russian missile strike on a merchant vessel at **Odesa** killed ten crew, **four of them Indian**.',
         'Fragmentation is not only West versus rest: Europe is hedging too, and energy pipelines have become targets. For India the lesson is practical: nationals at sea and in ports are caught in other people’s wars.',
         '**Nord Stream**: two pipeline systems, Russia to Germany under the Baltic Sea, the world’s longest subsea natural-gas pipeline; **Nord Stream 2** is non-operational. **Odesa** is a Ukrainian port on the north-western Black Sea coast.',
         src='Jul 2026 CA §3.8.5, §3.9.2, conflict areas.'),
    live(AUG, 'Even oil clubs are splitting: UAE leaves OPEC',
         'The **UAE exited OPEC in May 2026**. Meanwhile **seven OPEC+ countries** agreed to raise output “to support market stability”. India is not an OPEC member.',
         'A small, memorable example of blocs reshuffling: even the most disciplined cartel loses a major producer.',
         '**OPEC**: founded at the Baghdad Conference in **1960**, HQ **Vienna**. Members now: Algeria, Republic of Congo, Equatorial Guinea, Gabon, Iran, Iraq, Kuwait, Libya, Nigeria, Saudi Arabia, Venezuela. **OPEC+** (2016) adds partners incl. Russia, Oman, Kazakhstan, Mexico.',
         src='Aug 2026 CA §3.8.2 (OPEC and OPEC+).'),
]

LIVE['India’s foreign policy: goals and ten determinants'] = [
    live_head('the determinants, as they played out this summer'),
    live(JUL + ' + ' + AUG, 'Determinant 5 (energy) meets Hormuz, and a visit to Mauritius',
         'When Hormuz was disrupted, **LPG supply worries** hit India and **fuel shortages** hit Japan. India’s answer is diversification: the **Union Petroleum Minister visited Mauritius** (Aug 2026), an Indian Ocean partner where India built an **airstrip and a jetty on Agaléga** and which hosts **IORA’s headquarters**.',
         'Link a determinant to a live case in one line: “Energy security, determinant 5, is why India must diversify beyond one supplier or one sea lane, as the Hormuz disruption showed.” PYQ (2025): “Energy security constitutes the dominant kingpin of India’s foreign policy…” (the CA quotes it).',
         '**Mauritius**: Port Louis; includes Rodrigues, Agaléga, Cargados Carajos; **Aapravasi Ghat** is a UNESCO site; hosts the **Indian Ocean Rim Association** and the **Indian Ocean Commission** headquarters.',
         'Which determinant explains Chabahar, and which explains Mauritius?',
         'Chabahar: geography (Pakistan blocks the land route). Mauritius: energy and maritime security in the Indian Ocean.',
         src='Jul 2026 CA (Japan summit); Aug 2026 CA §3.10.1; PYQ quoted in Aug 2026 CA §3.2.'),
    live(JUL, 'Determinant 6 (science and technology): India’s third tech-trust pact',
         'India and Australia launched **PACTS** (Partnership for Cyber, Critical Technologies, Supply Chains): India’s **third** such framework after **TRUST (US)** and the **Technology Security Initiative (UK)**. Japan and India launched a first **AI Strategic Dialogue**.',
         'Shows the shift from buying technology to building trusted technology partnerships.',
         'Order to remember: TRUST (US), TSI (UK), PACTS (Australia).',
         src='Jul 2026 CA §3.1, §3.2.'),
]

LIVE['Continuities, changes, trade-offs and challenges'] = [
    live_head('the autonomy trade-off, three times in one month'),
    live(JUL, 'Multi-alignment in practice: three summits, three awkward partners',
         'In July 2026 India deepened ties with **Australia** (a US treaty ally inside **AUKUS**), **Japan** (which **sanctions Russia**) and **Indonesia** (which keeps **parallel defence ties with China, Russia, Turkey** and Western suppliers), while keeping its own defence and energy ties with Russia.',
         'This is the trade-off in one sentence: India gets partners on every side, and none of them fully shares its map of friends. Say it as: **“multi-alignment buys options, and the price is that every partner has a reservation.”**',
         'Australia: Cocos (Keeling) Islands is an Australian external territory in the Indian Ocean. Japan’s disputes: Senkaku/Diaoyu (China), Northern Territories/Southern Kurils (Russia), Takeshima/Dokdo (South Korea).',
         'Name the “reservation” each partner has about India.',
         'Australia: India is not an AUKUS-style ally and retains Russia defence ties. Japan: India keeps Russia ties despite sanctions. Indonesia: dependence on China far exceeds trade with India, and it balances all suppliers.',
         src='Jul 2026 CA §3.1, §3.2, §3.4 (challenge sections).'),
]

LIVE['Instruments of India’s contemporary foreign policy'] = [
    live_head('the toolbox, with this month’s examples'),
    live(JUL, 'Arms exporter: BrahMos goes to Indonesia, Sabang comes back',
         'India agreed to supply the **BrahMos** missile to **Indonesia**, the **second Southeast Asian country** after the **Philippines**. **Indonesia** will station a liaison officer at India’s **IFC-IOR**, and the two will **revive Sabang port** (Aceh), first agreed in 2018 and stalled eight years. With Japan, India agreed the technical details of **UNICORN**, its first defence-technology co-development.',
         'Use it for “defence diplomacy / net security provider”. Note both ends of the **Malacca Strait**: Indonesia’s Sabang at one end, India’s Andaman and Nicobar at the other. Add the honest caveat: contract value and delivery date are not announced; the Philippines took **two years** (2022 contract to 2024 delivery).',
         '**BrahMos**: India-Russia joint venture, supersonic cruise missile; first export customer **Philippines**. **IFC-IOR**: set up **2018**, hosted by the Indian Navy at **Gurugram**. **Sabang** is on Weh Island, Aceh. In the notes, Sabang is part of the **Diamond Necklace**.',
         'Why is the Sabang story a warning about announcements?',
         'It was agreed in 2018 and stalled for eight years over funding, feasibility and Indonesian sensitivities. Signing is not delivery.',
         src='Jul 2026 CA §3.4 (India-Indonesia); §3.2 (UNICORN).'),
    live(JUL + ' + ' + AUG, 'Trade as diplomacy: UK deal in force, NZ deal signed, Africa talks opened',
         '**India-UK CETA** is in force with the **Double Contribution Convention**: the UK removes duties on **99%** of tariff lines, India opens about **90%**, and keeps **dairy, cereals, millets, gold and lab-grown diamonds** out. **India-New Zealand FTA** was signed in **April 2026** after about nine months. **India-SACU** (Botswana, Eswatini, Lesotho, Namibia, South Africa) signed Terms of Reference to start **PTA** talks. The **India-Israel Bilateral Investment Agreement** entered into force.',
         'A single line for “economic diplomacy”: **“India is signing deals with the West, Oceania and Africa at once, which is exactly the diversification that the US tariff shock demanded.”** Flag the catch: the UK’s **CBAM (2027)** could tax Indian steel and aluminium and eat the tariff gains.',
         '**PTA** (positive list: only listed goods get concessions) versus **FTA** (negative list: most goods, except sensitive ones). **SACU** (1910) is the world’s oldest functioning customs union, secretariat at **Windhoek**. **DCC** ensures posted workers pay social security in one country only.',
         'PTA or FTA: which uses a negative list?',
         'FTA. A PTA gives concessions only on a positive list of agreed products. India-SACU is a PTA; India-UK CETA and India-NZ are FTAs.',
         src='Jul 2026 CA §3.6, §3.5, §3.9; Aug 2026 CA §3.8.3.'),
    live(JUL + ' + ' + AUG, 'Seats and summits: UNSC 2028-29, BRICS in India, ASEAN’s maritime year',
         'India launched its campaign for a **non-permanent UNSC seat for 2028-29** under the theme **SHANTI** (Securing Holistic Advancement through Norms, Trust and Integrity); it has served **8 terms** before. India-hosted **BRICS 2026** produced the **Guwahati Declaration** (against drug trafficking), **BRICS CONNECT** (labour platform) and the **Bhopal Declaration** (creative economy). **2026 is the ASEAN-India Year of Maritime Cooperation.** On **12 Sep 2026**, Modi and Xi met in New Delhi on the sidelines of the **18th BRICS Summit**.',
         'For “India and multilateralism”: India is both a reformer asking for a bigger seat and a host shaping the agenda. Cite SHANTI by name; examiners like specifics.',
         'UNSC: 15 members (5 permanent with veto, 10 non-permanent elected by UNGA for 2 years, **two-thirds majority**). **ARF** (1994, foreign ministers, 27 members) versus **EAS** (2005, leaders, 19 members). **IPOI** was announced by PM Modi at the 2019 EAS, Bangkok.',
         'ARF versus EAS: which is leaders-level, and which has security dialogue as its mandate?',
         'EAS is leaders-level (2005, 19 members); ARF is foreign-minister level (1994, 27 members) with a security-dialogue mandate. India joined ARF in 1996 and EAS at its start in 2005.',
         src='Jul 2026 CA §3.8.2, §3.8.3, §3.9.1; Aug 2026 CA §3.7; web: UNI, 12 Sep 2026.'),
    live(AUG, 'Soft power with a scheme: cultural exchanges with 98 countries',
         'India runs **Cultural Exchange Programmes with 98 countries** under the **Global Engagement Scheme** (Ministry of Culture): **ICEP**, **Project Mausam**, **Brihattar Bharat**, and safeguarding **Intangible Cultural Heritage**. The Standing Committee (2022) flagged thin funding, weak coordination, too few trained staff, an unclear **ICCR** mandate and no structured diaspora consultation.',
         'Balance in Mains: soft power helps, but **culture did not settle the India-China border** and political tensions can undercut shared heritage (Bangladesh). Fix: a single-window framework, a restructured ICCR, “Diaspora 2.0”, and the creative economy as an export sector.',
         'Heritage restoration abroad: **Angkor Wat, Ta Prohm, Prambanan**. **Prambanan** (Java, 9th century, UNESCO) is under joint restoration; **Tagore-Dewantara Year 2026-27** marks Tagore’s 1927 Indonesia visit. IIT Madras opened India’s first IIT campus outside India in **Zanzibar**. PYQ (2026): diaspora as “a living bridge… strategic leverage”.',
         'Name the four components of the Global Engagement Scheme.',
         'International Cultural Exchange Programme (ICEP), Project Mausam, Brihattar Bharat, and Safeguarding Intangible Cultural Heritage.',
         src='Aug 2026 CA §3.7 (cultural diplomacy); Jul 2026 CA §3.4, high-level visits.'),
    live(AUG, 'Science diplomacy at the poles: a parliamentary report says “move from presence to statecraft”',
         'The Parliamentary Committee on External Affairs reviewed India’s role in the **Arctic and Antarctic**. India is an **Arctic Council Observer (2013)** and an **Antarctic Treaty Consultative Party (1983)**, with stations **Himadri** (Arctic), **Maitri** and **Bharati** (Antarctica). Gaps: no Polar Ambassador, no polar research vessel, Maitri needs replacing, and observers cannot decide anything.',
         'Use for “climate-security nexus” and “science diplomacy”: poles shape the monsoon and sea level, so India’s interest is **consequence, not geography**. Fixes: a Polar Ambassador, a seventh “Geopolitics and Strategy” pillar in the **Arctic Policy 2022**, Maitri-II and an indigenous Polar Research Vessel.',
         '**Arctic Council** (Ottawa Declaration, 1996): 8 Arctic States plus 6 indigenous Permanent Participants; observers do not take final decisions. **Madrid Protocol**: Antarctica as a natural reserve, no mineral activity except science. **Indian Antarctic Act 2022**. PYQs quoted: Arctic Council members (2014); Arctic vs Antarctic melting (2021).',
         'Is Japan a member of the Arctic Council? (2014 PYQ asked about Denmark, Japan, Russia, UK, US.)',
         'No. Japan is an observer (the CA proposes an Asian observer grouping of India with Japan, South Korea and Singapore). Official answer to the PYQ is (d): Denmark, Russia, US.',
         src='Aug 2026 CA §3.1 (Arctic and Antarctic).'),
]

# ------------------------------------------------------------------ radar section
RADAR_ROWS = [
    ['Aug 2026', 'US tariffs: 50% cut to 18% (interim, Feb 2026); parliamentary report on India-US trade', 'Phase 5 · Instruments', 'Sovereign nationalism PYQ; diversification'],
    ['Aug 2026', 'Mecca Joint Defence Agreement (Saudi, Türkiye, Pakistan)', 'Phase 6', 'Strategic hedging; US umbrella doubts; Article 51'],
    ['Aug 2026', 'Hormuz: Iran-Oman reopening for 60 days (Sep: new routes, not yet open)', 'Phase 6 · Determinant 5', 'Chokepoints; energy security'],
    ['Aug 2026', 'UAE exits OPEC (May 2026); OPEC+ raises output', 'Phase 6', 'Blocs reshuffling'],
    ['Aug 2026', 'Cultural diplomacy: 98 countries; Global Engagement Scheme', 'Instruments', 'Soft power; diaspora PYQ 2026'],
    ['Aug 2026', 'Polar report: Arctic and Antarctic', 'Instruments', 'Science diplomacy; Arctic Council PYQ 2014'],
    ['Jul 2026', 'ICC withdrawals: Chad, Burkina Faso, Mali, Niger, Venezuela', 'Phase 5', 'Universal rules, selective membership'],
    ['Jul 2026', 'Australia, Japan, Indonesia summits', 'Trade-offs · Instruments', 'Multi-alignment; defence exports; economic security'],
    ['Jul 2026', 'UK CETA in force; NZ FTA; SACU PTA talks; Israel BIA', 'Instruments', 'Economic diplomacy; PTA vs FTA'],
    ['Jul 2026', 'UNSC 2028-29 campaign (SHANTI); BRICS Guwahati and Bhopal declarations', 'Instruments', 'Multilateralism'],
    ['Jul 2026', 'Odesa strike (4 Indians dead); Chabahar tower destroyed; Bab el-Mandeb blockade', 'Phase 6 · Determinants', 'Nationals abroad; connectivity under fire'],
    ['12 Sep 2026', 'Modi-Xi meeting in New Delhi (BRICS summit sidelines)', 'Instruments (see Ch. 2 India-China)', 'Border calm as a condition for ties'],
]

WATCH = [
    '**Hormuz:** does the strait actually reopen, and under whose route rules? Re-check before writing any energy answer.',
    '**India-US Bilateral Trade Agreement:** the interim framework (Feb 2026) is a stopgap; the parliamentary committee wants the BTA concluded early.',
    '**UK CBAM (2027):** will India win a carve-out for steel and aluminium?',
    '**India-Japan 2+2:** due within 2026; UNICORN technical details were agreed in principle.',
    '**ICC:** more withdrawal notices? Each takes effect one year after notification.',
    '**MJDA:** is a treaty text ever published, and does Bangladesh join?',
    '**UNSC 2028-29 election:** needs a two-thirds majority of UNGA members present and voting.',
]

CHAIN = [
    ('Trust drops', 'The US-Israel war on Iran makes Gulf states doubt the US umbrella.'),
    ('Hedging', 'Saudi Arabia, Türkiye and Pakistan sign MJDA; the UAE leaves OPEC; Europe forms its own missile-defence coalition.'),
    ('Trade turns sharp', 'The US taxes a partner’s Russian oil purchases: 25% reciprocal plus 25% penalty.'),
    ('Chokepoints bite', 'Hormuz disruption causes fuel shortages in Japan and LPG worries in India.'),
    ('India multi-aligns', 'Summits with Australia, Japan, Indonesia; UK and NZ trade deals; Modi-Xi meeting at BRICS.'),
]


def radar():
    blocks = [
        p('This section is the newsroom for Chapter 1. Every item comes from the **July and August 2026 current-affairs magazines** in your Project (two items from the web are marked). Read the table once a week, then try the chain from memory.'),
        tbl('What happened, and where it plugs into this chapter', ['When', 'News', 'Plugs into', 'Exam angle'], RADAR_ROWS),
        h3('Connect the dots: one story from the headlines'),
        flow('Five headlines, one argument', CHAIN),
        p('**Write it as a 4-line answer opener:** “The liberal order is giving way to hedging. When trust in the US umbrella fell, middle powers formed their own pacts; when trade became a weapon, India diversified; when a chokepoint closed, energy security became the first test of strategic autonomy.”'),
        h3('Watch next (status can change before your exam)'),
        '<ul class="watch-list">' + ''.join('<li>%s</li>' % inline(x) for x in WATCH) + '</ul>',
        callout('note', 'How to keep this section fresh', 'Every month, add the new magazine’s International Relations items here and file each one under the section it feeds. The test for any headline: **which phase, which determinant or which instrument does it prove?**'),
    ]
    return blocks


MCQ = [
    ('PYQ 2014 (as quoted in the Aug 2026 CA). Consider: 1. Denmark 2. Japan 3. Russian Federation 4. United Kingdom 5. United States of America. Which are members of the Arctic Council?',
     ['1, 2 and 3', '2, 3 and 4', '1, 4 and 5', '1, 3 and 5'], 3,
     'The CA prints this PYQ without a key; the official answer is (d). Members are the eight Arctic States, and Denmark, Russia and the US are among them. Observers such as India and Japan work through Working Groups but do not take final decisions.'),
    ('Under which Rome Statute article does a withdrawal from the ICC take effect one year after notification?',
     ['Article 12', 'Article 98', 'Article 127', 'Article 51'], 2,
     'Article 127. The Court keeps jurisdiction over crimes committed while the State was a member. Article 51 belongs to the UN Charter (self-defence).'),
    ('The Mecca Joint Defence Agreement cites which UN Charter provision as its legal basis?',
     ['Article 2(4)', 'Article 51', 'Article 25', 'Article 99'], 1,
     'Article 51: the right of individual or collective self-defence against armed attack, until the Security Council acts.'),
    ('PYQ 2026 (as quoted in the Aug 2026 CA). Ships from which countries must cross the Strait of Hormuz to reach the Indian Ocean? 1. Bahrain 2. Syria 3. Qatar 4. Egypt',
     ['1 and 2', '1 and 3', '2 and 3', '3 and 4'], 1,
     'The strait lies between the Persian Gulf and the Gulf of Oman. Bahrain and Qatar are inside the Gulf; Syria and Egypt are not. Answer (b).'),
    ('Which country exited OPEC in May 2026, according to the August 2026 CA?',
     ['Saudi Arabia', 'Iraq', 'United Arab Emirates', 'Nigeria'], 2,
     'The UAE exited OPEC in May 2026. India has never been an OPEC member.'),
    ('The India-Australia PACTS is India’s third technology-security framework. Which pair came before it?',
     ['TRUST (US) and Technology Security Initiative (UK)', 'IPEF and MSP', 'I2U2 and IMEC', 'COMPACT and Mission 500'], 0,
     'PACTS follows TRUST (US) and the Technology Security Initiative (UK).'),
    ('Which statement on PTA and FTA is correct?',
     ['A PTA uses a negative list', 'An FTA gives concessions only on a positive list', 'A PTA uses a positive list; an FTA uses a negative list', 'Both cover goods, services and investment equally'], 2,
     'PTA: positive list, limited, mostly goods. FTA: negative list (most goods get concessions), may include services and investment. India-SACU is a PTA.'),
    ('India’s UNSC campaign for 2028-29 uses which theme?',
     ['VASUDHA', 'SHANTI', 'SAGAR', 'MAHASAGAR'], 1,
     'SHANTI: Securing Holistic Advancement through Norms, Trust and Integrity. India has served 8 non-permanent terms before.'),
]

CARDS = [
    ('Live: how did US tariffs on India move in 2025-26?', '25% reciprocal plus 25% for Russian oil = 50%. Feb 2026 interim framework: 18%. Historical average about 3%.'),
    ('Live: what is the Mecca Joint Defence Agreement?', 'Saudi Arabia, Türkiye, Pakistan: attack on one is an attack on all. Article 51 basis. Not an alliance: no integrated command, no published text.'),
    ('Live: what triggered MJDA?', 'Doubts about the US security umbrella after the US-Israel war on Iran. It builds on the Sept 2025 Saudi-Pakistan pact.'),
    ('Live: why does Hormuz matter?', 'About 20% of world oil and LNG. Between the Persian Gulf and Gulf of Oman. Disruption caused fuel shortages in Japan and LPG worries in India.'),
    ('Live: which states are leaving the ICC?', 'Chad (notified), Burkina Faso, Mali, Niger, Venezuela. Article 127: effective one year after notification.'),
    ('Live: ICC criticism in three points?', 'African bias (9 of 13 investigations), no enforcement arm, power asymmetry (US, China, Russia outside; UNSC can refer and defer).'),
    ('Live: India’s three tech-trust pacts?', 'TRUST (US), Technology Security Initiative (UK), PACTS (Australia).'),
    ('Live: BrahMos export order?', 'Philippines first (2022 contract, 2024 delivery), Indonesia second in Southeast Asia (July 2026).'),
    ('Live: Chabahar in the news?', 'US CENTCOM destroyed a surveillance tower at the Shahid Kalantari port. India’s terminal is Shahid Beheshti (India Ports Global Limited). Outside Hormuz.'),
    ('Live: UK CETA in one breath?', 'UK removes duties on 99% of lines; India opens about 90%; dairy, cereals, millets, gold, lab-grown diamonds excluded; DCC included; UK CBAM (2027) is the risk.'),
    ('Live: UNSC 2028-29 campaign theme?', 'SHANTI. India has served 8 terms. Needs two-thirds of UNGA members present and voting.'),
    ('Live: Global Engagement Scheme components?', 'ICEP, Project Mausam, Brihattar Bharat, Safeguarding Intangible Cultural Heritage. Cultural exchange programmes with 98 countries.'),
]
