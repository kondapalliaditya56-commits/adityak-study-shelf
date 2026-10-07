# -*- coding: utf-8 -*-
"""Chapter 3 live current-affairs layer. Facts come only from the Aug 2026 and Jul 2026 current-affairs
magazines in the UPSC Project (web items are labelled)."""
from lib import *

AUG = 'Aug 2026 CA'
JUL = 'Jul 2026 CA'

LIVE = {}

LIVE['India’s neighbourhood: overview and India’s interests'] = [
    live_head('the neighbourhood in the 2026 papers'),
    live('Mains 2026', 'Two 2026 questions came from this chapter’s ground',
         '**GS-II Q20 (15 marks):** China’s BRI “has transformed South Asia from a regional space into a theatre of great power competition”: strategic implications for India’s security and regional influence. **GS-I Q7 (10 marks):** “Water resources are both an asset and a source of conflict in South Asia.”',
         'Neither names a single neighbour. Both ask for a **theme with examples from several neighbours**. That is how to revise this chapter: China’s footprint and rivers, country by country (section 14 has both tables).',
         'The BRI question is quoted in the Chapter 1 and 2 handouts; its skeleton is in Chapter 2. The water question is quoted in the August 2026 current-affairs magazine.',
         'Give four neighbours for a water answer, one line each.',
         'Pakistan: IWT in abeyance. Bangladesh: Ganga Treaty expires December 2026, Teesta stuck. Nepal: Pancheshwar has no agreed report. Bhutan: hydropower as shared benefit (asset side).',
         src='Chapter 1 and 2 handouts (PYQ lists); Aug 2026 CA §3.6 (PYQ quoted).', why_label='What was asked'),
    live(AUG, 'MAHASAGAR: from “net security provider” to “preferred security partner”',
         '**MAHASAGAR** extends **SAGAR** from maritime security to economic and geopolitical concerns, and across the whole Indo-Pacific. India’s self-description moves from “Net Security Provider” to “**Preferred Security Partner and First Responder**”.',
         'This is the vocabulary for Sri Lanka, Maldives and Myanmar answers: all three handout conclusions invoke MAHASAGAR.',
         'SAGAR came first; MAHASAGAR is its extension.',
         src='Aug 2026 CA §3.5 (Prelims fodder).'),
]

LIVE['Challenges in the neighbourhood'] = [
    live_head('a new outside pact on both flanks'),
    live(AUG, 'The Mecca pact reaches India’s west and may reach its east',
         'The **Mecca Joint Defence Agreement** (Saudi Arabia, Türkiye, Pakistan) treats an attack on one as an attack on all. **Bangladesh has expressed interest in joining**, which “would extend the pact to India’s eastern front”. Türkiye already backs Pakistan on Kashmir at the UN.',
         'Add it to the “China’s growing presence” challenge as a second kind of external influence: not infrastructure, but a defence pact. It also shows the “political instability” challenge: a transition in Dhaka changes the map of alignments.',
         'Legal basis: **UN Charter Article 51**. It builds on the **Saudi-Pakistan Strategic Mutual Defence Agreement (September 2025)**.',
         src='Aug 2026 CA §3.2 (MJDA).'),
]

LIVE['Way forward for neighbourhood policy'] = [
    live_head('delivery, measured in trains'),
    live(JUL, 'One new freight train, three suspended passenger trains, no rail to Bhutan',
         'Indian Railways ran the **first direct commercial container freight train from Kolkata Port to Biratnagar, Nepal**. With Bangladesh, the three passenger services (**Maitree** Kolkata-Dhaka, **Bandhan** Kolkata-Khulna, **Mitali** New Jalpaiguri-Dhaka) have been **suspended since 2024**. With Bhutan, **no rail link is operational**; the proposed Kokrajhar-Gelephu and Banarhat-Samtse lines would be its first.',
         'The handout’s way forward says “less on announcements and more on trust, delivery”. This single news item gives one success (Nepal), one reversal (Bangladesh) and one promise (Bhutan). Use it as the evidence line for “project delivery”.',
         'Nepal rail links: **Jaynagar-Kurtha-Bijalpura** (passenger), **Jogbani-Biratnagar** (freight).',
         'Which neighbour got its first direct container freight train from Kolkata Port in 2026?',
         'Nepal (Biratnagar). Bangladesh’s three passenger trains have been suspended since 2024; Bhutan has no operating rail link.',
         src='Jul 2026 CA (India’s cross-border railway connectivity).', why_label='What happened'),
]

LIVE['India-Pakistan: nature, evolution and convergence'] = [
    live_head('Pakistan’s new partners'),
    live(AUG, 'Pakistan gains a Saudi purse and a Turkish arsenal',
         'Under the Mecca pact, India’s concern is Pakistan’s **easier access to Saudi financing and Turkish defence technology (drones, naval platforms)**. Pakistan brings the pact its status as the **only nuclear-armed Muslim-majority state** and a long military-training role in Saudi Arabia. The MEA said it is **examining the implications** for national security.',
         'It widens the “China-Pakistan nexus” row of the nature table: Pakistan’s external backing is no longer only Chinese. But note the limit the magazine gives: **no common enemy** (Saudi Arabia looks at Iran, Türkiye at Israel, Pakistan at India), **no integrated command, no published text**.',
         'Kautilya’s **mandala** idea in the magazine: a neighbouring rival gains strength through allies, so India builds ties with Greece, Cyprus and Armenia, and with the UAE, Israel and Oman.',
         src='Aug 2026 CA §3.2 (MJDA).'),
]

LIVE['India-Pakistan: divergence and way forward'] = [
    live_head('water and corridors'),
    live(AUG, 'The Indus treaty in abeyance, and CPEC through PoK',
         'The magazine’s water chapter lists the **IWT (1960, World Bank-facilitated) as “in abeyance by India after the terrorist attack in Pahalgam”**, and notes Pakistan’s earlier protests over **Baglihar** and **Kishanganga**. Its boundary chapter repeats India’s objection: **CPEC, the flagship of China’s BRI, passes through PoK**.',
         'Two ready examples for the divergence table: water (treaty in abeyance) and sovereignty (CPEC). The magazine’s fix for water disputes applies here too: updated agreements, transparent data, basin-level thinking.',
         'IWT: signed **1960**, **World Bank** facilitated. BRI launched **2013**; India has not joined.',
         src='Aug 2026 CA §3.6 (transboundary water) and §3.4.'),
]

LIVE['India-Afghanistan'] = [
    live_head('Chabahar under fire'),
    live(JUL, 'A US strike at Chabahar, next to India’s terminal',
         'US Central Command **destroyed a surveillance tower at Chabahar’s Shahid Kalantari Port**. India’s terminal there, **Shahid Beheshti, operated by India Ports Global Limited**, gives access to Afghanistan and Central Asia while bypassing Pakistan. Chabahar is on the **Gulf of Oman, outside the Strait of Hormuz**.',
         'The handout says “sanctions and regional conflict complicate India’s Chabahar engagement”. This is that sentence as a headline. Pair it with the way forward: small, locally maintainable projects and alternative Central Asian routes.',
         'Two terminals at Chabahar: **Shahid Kalantari** and **Shahid Beheshti** (India’s).',
         'Why does Chabahar matter more to India than its cargo volume suggests?',
         'Pakistan blocks India’s land route, so Chabahar is the only dependable access to Afghanistan and Central Asia. It lies outside Hormuz.',
         src='Jul 2026 CA (conflict areas: Chabahar).', why_label='What happened'),
    live_quick('2025-26', [
        '**CPEC into Afghanistan (web):** China, Pakistan and Afghanistan agreed in 2025 to extend CPEC to Afghanistan. This is the “exclusive China-Pakistan strategic space” the handout warns about.',
        '**Death Crescent:** the August magazine’s drug-abuse chapter uses the same term for the opium-producing region to India’s west, and “Death Triangle” for the east.',
    ], src='web: The Tribune, May 2025 (collected for the PYQ Lab); Aug 2026 CA (drug abuse in India).'),
]

LIVE['India-Bangladesh'] = [
    live_head('the reset, issue by issue'),
    live(AUG, 'December 2026: the Ganga treaty runs out',
         'India and Bangladesh have discussed river issues including the **Ganges Water Sharing (Farakka) Treaty**: signed **1996 for 30 years**, it **expires in December 2026**. Sharing is for the **lean season**, calculated at **Farakka (West Bengal)**; the **Joint Rivers Commission** resolves issues. On **Teesta**, the two were ready to sign in **2011** but **West Bengal opposed** it. Bangladesh **acceded to the UN Water Convention in 2025**; India is not a signatory.',
         'The live test of the handout’s “strategic reset”. Write it as upstream-downstream trust: Bangladesh wants a larger dry-season share; India must balance West Bengal and Sikkim. The handout’s fix: a time-bound Teesta dialogue including West Bengal, and a post-2026 Ganga arrangement on measured flows.',
         '**UN Water Convention** (Helsinki, 1992; in force 1996). **Helsinki Rules (1966)** and **Berlin Rules (2004)** are by the International Law Association, a private body.',
         'What is measured where under the Ganga treaty, and which body handles disputes?',
         'Lean-season flow available at Farakka in West Bengal; the Joint Rivers Commission.',
         src='Aug 2026 CA §3.6 (transboundary water).'),
    live_quick('Jul-Aug 2026', [
        '**Trains:** Maitree, Bandhan and Mitali Express have been suspended since 2024 (July magazine).',
        '**Mecca pact:** Bangladesh has expressed interest in joining (August magazine).',
        '**Culture has limits:** the August magazine notes that India-Bangladesh shared heritage and people-to-people ties “have often been affected by domestic political issues”.',
        '**Trilateral (web):** China, Pakistan and Bangladesh held a first trilateral meeting in Kunming on 19 June 2025.',
    ], src='Jul 2026 CA (cross-border rail); Aug 2026 CA §3.2, §3.7; web: collected for the PYQ Lab.'),
]

LIVE['India-Nepal'] = [
    live_head('Lipulekh, a freight train and a flood'),
    live(AUG, 'India and China agree to reopen Lipulekh for trade',
         'At the **25th Special Representatives talks**, India and China agreed to **reopen the Lipulekh, Shipki La and Nathu La border trade points** and to send more Kailash Mansarovar Yatra batches.',
         'This is the handout’s “**three-party sensitivity**” in the news: India-China activity at Lipulekh touches Nepal’s claim over Kalapani, Lipulekh and Limpiyadhura. In an answer, pair the reopening with the handout’s remedy: evidence-based boundary talks with Nepal.',
         'Lipulekh Pass is in **Uttarakhand** (with Mana and Niti); Shipki La in Himachal Pradesh; Nathu La in Sikkim.',
         'Why can an India-China trade decision become an India-Nepal problem?',
         'Because Nepal’s 2020 map claims Lipulekh. India-China activity there affects Nepal’s territorial claim.',
         src='Aug 2026 CA §3.4 (India-China boundary).', why_label='What happened'),
    live(AUG + ' + ' + JUL, 'A Himalayan flood and a first freight train',
         'On **26 August 2026** a mass of glacier ice and rock collapsed into the **Lhende Khola** catchment near the Nepal-Tibet border, dammed the stream and then breached, sending a flash flood down the **Bhote Koshi-Trishuli** system. The handout records India’s relief (over 130 tonnes). In July, Indian Railways ran the **first direct container freight train from Kolkata Port to Biratnagar**.',
         'Two halves of the way forward: **real-time glacial-lake, rainfall and river-level data sharing**, and **timely connectivity**. The magazine’s ethics chapter adds a sovereignty angle: whether to accept foreign rescue teams.',
         'The magazine also lists **Pancheshwar** as unsettled over water sharing, benefit assessment and cost sharing, under the **1996 Mahakali Treaty**.',
         src='Aug 2026 CA (disaster and ethics chapters; §3.6); Jul 2026 CA (cross-border rail).', why_label='What happened'),
]

LIVE['India-Bhutan'] = [
    live_head('Bhutan in the magazines'),
    live_quick('Jul-Aug 2026', [
        '**Rail:** “No railway link is operational”; the proposed Kokrajhar-Gelephu and Banarhat-Samtse lines “would provide Bhutan its first rail connectivity” (July magazine). The handout makes the same point: planned, not operating.',
        '**Water as a shared asset:** the August magazine’s example of hydropower cooperation is India-Bhutan: **Chukha, Tala, Mangdechhu**. Use Bhutan as the “asset” half of a water answer.',
        '**UPI:** Bhutan was the **first country** to which UPI expanded internationally (August magazine).',
        '**Doklam:** the August magazine calls Doklam, near the **Siliguri Corridor (“Chicken’s Neck”)**, a sensitive tri-junction flashpoint.',
    ], src='Jul 2026 CA (cross-border rail); Aug 2026 CA §3.6, UPI chapter, §3.4.'),
]

LIVE['India-Myanmar'] = [
    live_head('Myanmar in the magazines'),
    live_quick('Jul-Aug 2026', [
        '**Kaladan** is named in the August magazine as a connectivity and navigation link built on shared waters.',
        '**Death Triangle:** the August magazine’s drug-abuse chapter links India’s Northeast to the opium-producing “Death Triangle”, and lists the North-Eastern states among the regions with concentrated substance use. This is the domestic cost of the border problem in the handout.',
        '**Check:** the two magazines carry no India-Myanmar headline of their own. Add one when it appears.',
    ], src='Aug 2026 CA §3.6 and the drug-abuse chapter.'),
]

LIVE['India-Sri Lanka'] = [
    live_head('Sri Lanka in the magazines'),
    live_quick('Jul-Aug 2026', [
        '**ISFTA as the textbook FTA:** the August magazine uses the **India-Sri Lanka FTA** as its example of a free trade agreement (negative list), against PTAs such as India-MERCOSUR.',
        '**MAHASAGAR and the island states:** the August magazine’s MAHASAGAR note fits Sri Lanka and the Maldives: India as “Preferred Security Partner and First Responder”.',
        '**Check:** the two magazines carry no India-Sri Lanka headline of their own. The handout’s latest items are Operation Sagar Bandhu (November 2025) and FY 2025-26 trade.',
    ], src='Aug 2026 CA §3.8.3, §3.5.'),
]

LIVE['India-Maldives'] = [
    live_head('the reset shows up in payments'),
    live(JUL, 'Favara-UPI: rufiyaa to rupees in real time',
         'The **Favara-UPI Payment Corridor** went live between the **Maldives Instant Payment System (Favara)** and India’s **UPI**. It allows real-time person-to-person and person-to-merchant transfers in **Maldivian Rufiyaa settled in Indian Rupees**. It lowers remittance fees, eases trade settlement and **reduces reliance on third-currency (US dollar) conversion**.',
         'A small, concrete proof of the “cautious reset”: after “India Out”, cooperation returned through low-politics tools (payments, currency swap, runway) and not through troops. Use it in the “economic and digital” paragraph of the 2024 PYQ.',
         'UPI is live across **11 jurisdictions**, including the Maldives (August magazine).',
         'Why is a payments link politically easier than a defence link in the Maldives?',
         'It delivers a visible benefit to ordinary people and involves no Indian personnel or assets, which were the target of the “India Out” campaign.',
         src='Jul 2026 CA (Favara-UPI Payment Corridor); Aug 2026 CA (UPI chapter).', why_label='What happened'),
]

RADAR_ROWS = [
    ['Aug 2026', 'Ganga (Farakka) treaty talks; expiry December 2026; Teesta', 'Bangladesh', 'Water as asset and conflict'],
    ['Aug 2026', 'Mecca pact: Pakistan’s gains; Bangladesh’s interest', 'Challenges · Pakistan · Bangladesh', 'External influence beyond China'],
    ['Aug 2026', 'Lipulekh trade point to reopen (India-China talks)', 'Nepal', 'Three-party sensitivity'],
    ['Aug 2026', 'Nepal flash flood (26 Aug), Bhote Koshi-Trishuli', 'Nepal', 'Data sharing; first responder'],
    ['Aug 2026', 'IWT listed as in abeyance; CPEC through PoK', 'Pakistan', 'Water; sovereignty'],
    ['Aug 2026', 'MAHASAGAR: preferred security partner, first responder', 'Overview · Sri Lanka · Maldives', 'Vocabulary'],
    ['Jul 2026', 'First Kolkata-Biratnagar freight train; Bangladesh trains suspended; no Bhutan rail', 'Way forward · Nepal · Bangladesh · Bhutan', 'Delivery versus announcement'],
    ['Jul 2026', 'US strike at Chabahar’s Shahid Kalantari port', 'Afghanistan', 'Connectivity under fire'],
    ['Jul 2026', 'Favara-UPI corridor live', 'Maldives', 'Low-politics reset'],
    ['Handout, 2026', 'Hasina extradition request renewed (Aug); India-Maldives FTA round one (Jul); ₹4,000-crore credit line to Bhutan (Jul)', 'Bangladesh · Maldives · Bhutan', 'The handout’s own latest facts'],
]

WATCH = [
    '**Ganga Treaty, December 2026:** renewal, replacement or lapse?',
    '**Sheikh Hasina’s extradition request:** India is examining it under its legal procedures.',
    '**Indus Waters Treaty:** does “abeyance” continue; do flood-data channels survive?',
    '**Bangladesh and the Mecca pact:** interest, or membership?',
    '**India-Maldives FTA:** round one ended in July 2026; China’s FTA has been in force since January 2025.',
    '**Nepal:** youth-led politics, the 1950 Treaty review, and any reaction to Lipulekh trade reopening.',
    '**Bhutan:** the two rail links and Punatsangchhu-I.',
    '**Myanmar:** Kaladan’s last stretch to Mizoram; the Free Movement Regime.',
    '**Chabahar:** sanctions and the West Asia conflict.',
]

CHAIN = [
    ('Politics shifts next door', 'Bangladesh after August 2024; “India Out” in the Maldives; youth-led change in Nepal.'),
    ('Outside powers step in', 'China’s ports and FTAs; a Mecca pact Bangladesh wants to join; CPEC stretching to Afghanistan.'),
    ('Old agreements strain', 'IWT in abeyance; Ganga Treaty expiring; 1950 Treaty under review calls.'),
    ('India answers with low-politics tools', 'UPI links, currency swaps, freight trains, relief operations.'),
    ('The test is delivery', 'Kaladan, the Bhutan rail links, Pancheshwar, the Sri Lanka grid link are still unfinished.'),
]


def radar():
    return [
        p('The newsroom for Chapter 3. Items come from the **July and August 2026 current-affairs magazines** in your Project; web items are marked. The handout itself is very current (it runs to September 2026), so its latest facts are listed in the last row.'),
        tbl('What happened, and where it plugs into this chapter', ['When', 'News', 'Plugs into', 'Exam angle'], RADAR_ROWS),
        h3('Connect the dots: one story from the headlines'),
        flow('Five steps, one argument', CHAIN),
        p('**Write it as a 4-line answer opener:** “India’s neighbourhood is shaped less by India’s offers than by its neighbours’ politics and by outside powers ready to step in. Old treaties are under strain. India’s best tools have been quiet ones: payments, power, trains and relief. What remains to be proved is delivery.”'),
        h3('Watch next (status can change before your exam)'),
        '<ul class="watch-list">' + ''.join('<li>%s</li>' % inline(x) for x in WATCH) + '</ul>',
        callout('note', 'How to keep this section fresh', 'Each month, file the new magazine’s neighbourhood items under the country they concern, and then ask the theme question: **is this about China’s footprint, water, crisis response, domestic politics or delivery?**'),
    ]


MCQ = [
    ('Which neighbour received the first direct commercial container freight train from Kolkata Port in 2026?',
     ['Bangladesh (Dhaka)', 'Nepal (Biratnagar)', 'Bhutan (Gelephu)', 'Myanmar (Sittwe)'], 1,
     'Nepal. Bangladesh’s three passenger trains have been suspended since 2024; Bhutan has no operating rail link (July 2026 magazine).'),
    ('The Maitree, Bandhan and Mitali Express connect India with:', ['Nepal', 'Bangladesh', 'Bhutan', 'Sri Lanka'], 1,
     'Bangladesh: Kolkata-Dhaka, Kolkata-Khulna, New Jalpaiguri-Dhaka. Suspended since 2024.'),
    ('The Favara-UPI Payment Corridor links India with:', ['Mauritius', 'Sri Lanka', 'Maldives', 'Bhutan'], 2,
     'Favara is the Maldives Instant Payment System. Transfers in rufiyaa are settled in rupees.'),
    ('At Chabahar, the terminal operated by India Ports Global Limited is:', ['Shahid Kalantari', 'Shahid Beheshti', 'Bandar Abbas', 'Gwadar'], 1,
     'Shahid Beheshti. The US strike in 2026 hit a surveillance tower at Shahid Kalantari.'),
    ('Under the 1996 Ganga Water Sharing Treaty, water sharing is calculated at:', ['Haridwar', 'Farakka', 'Patna', 'Goalundo'], 1,
     'Farakka in West Bengal, for the lean season. The Joint Rivers Commission resolves issues. The treaty expires in December 2026.'),
    ('Which border trade points did India and China agree to reopen at the 25th Special Representatives talks?',
     ['Lipulekh, Shipki La, Nathu La', 'Mana, Niti, Jelep La', 'Bum La, Nathu La, Zoji La', 'Lipulekh, Rohtang, Karakoram'], 0,
     'Lipulekh (Uttarakhand), Shipki La (Himachal Pradesh), Nathu La (Sikkim). Lipulekh is also claimed by Nepal.'),
]

CARDS = [
    ('Live: two 2026 questions from the neighbourhood?', 'GS-II Q20: BRI and South Asia as a theatre of great-power competition. GS-I Q7: water as asset and source of conflict in South Asia.'),
    ('Live: MAHASAGAR in one line?', 'Extension of SAGAR to economic and geopolitical concerns across the Indo-Pacific; India as Preferred Security Partner and First Responder.'),
    ('Live: how does the Mecca pact touch the neighbourhood?', 'Pakistan gains Saudi financing and Turkish defence technology; Bangladesh has shown interest in joining.'),
    ('Live: cross-border rail in 2026?', 'First Kolkata Port-Biratnagar freight train (Nepal); Bangladesh passenger trains suspended since 2024; no operating rail to Bhutan.'),
    ('Live: Chabahar in the news?', 'US CENTCOM destroyed a tower at Shahid Kalantari; India’s terminal is Shahid Beheshti (India Ports Global Limited).'),
    ('Live: Ganga treaty facts?', '1996, 30 years, expires December 2026; lean-season sharing at Farakka; Joint Rivers Commission.'),
    ('Live: why does Lipulekh matter twice?', 'India and China agreed to reopen it for trade; Nepal claims it. Three-party sensitivity.'),
    ('Live: Favara-UPI?', 'Maldives’ instant payment system linked to UPI: rufiyaa settled in rupees, lower remittance fees, less dollar conversion.'),
]
