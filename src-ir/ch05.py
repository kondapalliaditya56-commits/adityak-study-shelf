# -*- coding: utf-8 -*-
from lib import *
from ch05b import *

CH = {'n': 5, 'title': 'India’s Extended Neighbourhood',
      'sub': 'West Asia, ASEAN, the Indo-Pacific, Central Asia, Africa and Latin America: what India wants, what it has built and what holds it back',
      'badge': 'High · Mains', 'slides': True}

SRC = ('Class slides PPT-7.2 (36 slides: overview, West Asia, ASEAN, Indo-Pacific, Central Asia) and PPT-7 (17 slides: Africa, Latin America), '
       'and the Extended Neighbourhood chapter of the merged handout, pages 78-100')

PYQ = [
    ('Mains 2024 · 10 marks · 150 words', 'Critically analyse India’s evolving diplomatic, economic and strategic relations with the Central Asian Republics (CARs) highlighting their increasing significance in regional and global geopolitics.', 'Three dimensions, then limits. See the skeleton in Practice.', 'Section 11', 'handout p. 100'),
    ('Mains 2021 · 10 marks · 150 words (handout prints 15 and 250)', '“If the last few decades were of Asia’s growth story, the next few are expected to be of Africa’s.” In the light of this statement, examine India’s influence in Africa in recent years.', 'Influence with examples, then the China gap. See the skeleton in Practice.', 'Section 12', 'handout p. 100'),
    ('Mains 2021 · 15 marks · 250 words', 'The newly tri-nation partnership AUKUS is aimed at countering China’s ambitions in the Indo-Pacific region. Is it going to supersede the existing partnerships in the region? Discuss the strength and impact of AUKUS in the present scenario.', '**Thin notes:** AUKUS is only named in the material. See the skeleton in Practice.', 'Sections 9 and 10', 'handout p. 100'),
    ('Mains 2018 · 10 marks · 150 words', '“India’s relations with Israel have, of late, acquired a depth and diversity, which cannot be rolled back.” Discuss. (The handout prints “cannot be overlooked”.)', 'Depth (defence, tech, water), then the limits (Palestine, Iran, Gulf). See the skeleton in Practice.', 'Section 4', 'handout p. 100'),
    ('Mains 2018 · 10 marks · 150 words', 'A number of outside powers have entrenched themselves in Central Asia, which is a zone of interest to India. Discuss the implications, in this context, of India’s joining the Ashgabat Agreement.', 'Connectivity without Pakistan; Russia and China already there. See the skeleton in Practice.', 'Section 11', 'handout p. 100'),
    ('Mains 2016 · 12.5 marks · 200 words', 'Evaluate the economic and strategic dimensions of India’s Look East Policy in the context of the post-Cold War international scenario.', 'Look East (1991) to Act East (2014). See the skeleton in Practice.', 'Section 7', 'handout p. 100'),
    ('Mains 2015 · 12.5 marks · 200 words', '“Increasing interest of India in Africa has its pros and cons.” Critically examine.', 'Pros (markets, minerals, Global South), cons (China gap, delivery, security). See the skeleton in Practice.', 'Section 12', 'handout p. 100'),
]


def build():
    secs = []
    exam = []
    exam.append(callout('source', 'Source note',
        '**This chapter has class slides and a handout.** ' + SRC + '. The slides are typed with **no handwriting or board ink**; they carry seven maps (Israel-Palestine, West Asia, ASEAN, Indo-Pacific, Central Asia, Africa, Latin America). Each region has the same shape: nature, evolution, convergence, challenges, way forward. The handout adds figures and dates; a few handout lines are garbled in print, and the slides fill those gaps (flagged where they occur). The material quotes **no Prelims PYQs**; its PYQ box lists seven Mains questions.'))
    exam.append(tbl('What the slides stress', ['Signal in the material', 'Where', 'Why it matters'], [
        ['West Asia: “**Present character: Strategic engagement with careful regional balancing**”; India seeks relations “across competing camps”', 'PPT-7.2, slides 3 and 8', 'The frame for any West Asia answer.'],
        ['Palestine: “**Cooperation with Israel without abandoning support for Palestinian statehood**” (de-hyphenation)', 'Slide 11', 'The one line examiners look for.'],
        ['West Asia close: success depends on “strategic autonomy, diversified partnerships, secure energy and maritime routes, and strong citizen protection **without entering rigid regional alignments**”', 'Slide 18', 'A ready conclusion.'],
        ['ASEAN: “**Strategic convergence with under-realised economic potential**”; direction: move to economic integration, connectivity and maritime cooperation', 'Slides 19 and 24', 'The ASEAN gap in one phrase.'],
        ['Indo-Pacific: manage China by “**Dialogue + deterrence + de-risking**”; avoid “a formal anti-China bloc”', 'Slide 29', 'India’s position against the US model.'],
        ['Central Asia: “**Strategic interest constrained by geography and connectivity**”; “a **geography gap, not an interest gap**”; “**Connect Central Asia 2.0**”', 'Slides 30, 34-35', 'A full answer frame in three phrases.'],
        ['Africa: move “**from goodwill to delivery**”, aligned with **Agenda 2063**', 'PPT-7, slide 9', 'The Africa conclusion.'],
        ['Latin America: turn “**geographical distance into a more meaningful strategic partnership**”', 'PPT-7, slide 16', 'The Latin America conclusion.'],
    ]))
    exam.append(tbl('PYQs quoted in the material (Mains only)', ['Year, marks, words', 'What was asked', 'Answer or trap', 'Where in this chapter', 'Source'],
        [[a, b, c, d, e] for (a, b, c, d, e) in PYQ],
        desc='Mains years quoted: 2024, 2021 (two), 2018 (two), 2016, 2015. Prelims years quoted: none quoted in the material. West Asia’s energy questions (2017, 2025) are not in this handout’s box; they are in the PYQ Lab.'))
    exam.append(alert('Handout alert: two PYQ details', 'The handout prints the 2018 Israel question as “…which cannot be **overlooked**”; the published paper reads “cannot be **rolled back**”. It prints the 2021 Africa question as 15 marks; the paper had it at **Q9, 10 marks, 150 words**. Both checked across several compilations for the PYQ Lab. Rule: “rolled back” is the bait word; plan 150 words for Africa.'))
    exam.append(callout('key', 'What to prepare',
        '**Prelims hooks:** Balfour Declaration (1917); UN partition plan (1947); Israel 1948; 1967 war; Abraham Accords (2020); JCPOA (2015; US exit 2018); GCC members; India recognised Israel 1950, full ties 1992; Ramallah visit 2018; Shahid Beheshti 10-year contract (May 2024); Operation Sindhu; India-UAE CEPA (2022); India-Oman CEPA (1 June 2026); India-GCC FTA talks (February 2026); Strategic Partnership Council (2019); ASEAN 11 members (Timor-Leste 2025); Sectoral partner 1992, Dialogue Partner 1995, first summit 2002, AITIGA 2010, Act East 2014, IPOI 2019, CSP 2022; IPOI and AOIP; IFC-IOR; Connect Central Asia (2012); SCO (2017); Ashgabat (2018); India-Central Asia Dialogue (2019) and Summit (2022); TAPI; INSTC; DUSTLIK; Pan-African e-Network (2004); IAFS-I (2008); Kampala Principles (2018); AU in the G20; AIKEYME; KABIL in Argentina; MERCOSUR and Chile PTAs; CELAC; CARICOM; G4.\n\n'
        '**Mains hooks:** de-hyphenation and balancing three axes; energy and chokepoints; Chabahar versus IMEC; ASEAN trade deficit and RCEP; competing Indo-Pacific visions; Central Asia’s connectivity deficit; Africa and Latin America against China’s scale; diaspora protection.\n\n'
        '**Closing idea:** across all six regions, India’s problem is less intent than **delivery**: connectivity, trade integration and project completion.'))
    secs.append(Sec('Exam lens: priority and PYQs', exam, sid='exam-lens-priority-and-pyqs'))

    # 1 overview
    secs.append(Sec('The extended neighbourhood at a glance', [
        p('India’s extended neighbourhood is a **strategic and civilisational space** linking West Asia, Central Asia, Southeast Asia and the wider Indian Ocean-Indo-Pacific. These regions shape India’s **trade, energy, connectivity, security and global influence**.'),
        tbl('Six regions and why each matters (PPT-7.2 slide 2, handout p. 78)', ['Direction', 'Region', 'Importance for India'], [
            ['West', 'West Asia and the Gulf', 'Energy, investment and diaspora'],
            ['Northwest', 'Central Asia', 'Connectivity and strategic resources'],
            ['West/Southwest', 'Africa', 'Markets, critical minerals, Global South cooperation'],
            ['East', 'ASEAN and East Asia', 'Trade, technology and production networks'],
            ['Maritime arc', 'Indian Ocean-Indo-Pacific', 'Sea-lane security, blue economy and regional public goods'],
            ['West across the Atlantic', 'Latin America and the Caribbean', 'Energy, minerals and markets'],
        ]),
        mnemo('Memory aid: the six regions', 'WCAAIL', 'West Asia, Central Asia, ASEAN, Africa, Indo-Pacific, Latin America: “We Can Always Ask India Later”.'),
    ], label='Class + handout'))

    # 2 West Asia nature & evolution
    secs.append(Sec('West Asia: nature and evolution', [
        p('“**West Asia is part of our extended neighbourhood.**” (S. Jaishankar, quoted.) West Asia is India’s **energy, diaspora, connectivity and maritime-security corridor**: it supplies oil, LNG and fertilisers, hosts millions of Indians and controls the chokepoints of **Hormuz, Bab-el-Mandeb, the Red Sea and the Suez route**.'),
        tbl('Nature of the relationship (slide 3, handout p. 78)', ['Nature', 'Meaning'], [
            ['Multi-aligned', 'Simultaneous engagement with competing regional actors: Israel, Iran and the Gulf at once'],
            ['Interest-driven', 'Energy, security, trade and connectivity shape policy, not a single partner'],
            ['Strategic balancing', 'Ties are kept despite intra-regional rivalries'],
            ['Crisis-sensitive', 'Regional wars hit India’s energy, shipping and diaspora directly'],
            ['Expanding agenda', 'Oil-centric ties → defence, technology, investment and connectivity'],
        ]),
        teacher('Class slide stress (slide 3)', '**Present character: Strategic engagement with careful regional balancing.**'),
        tbl('Evolution (slide 4, handout p. 78)', ['Phase', 'Keyword', 'Key developments'], [
            ['Ancient-1947', 'Civilisational and maritime links', 'Trade, Islam, Sufism, Indian Ocean routes, spices and textiles'],
            ['1947-1970s', 'Nehruvian diplomacy', 'Support for **Arab nationalism, Palestine and non-alignment**; distance from Israel'],
            ['1970s-1991', 'Energy and diaspora', '**Oil shocks** made Gulf energy central; Gulf migration made worker welfare, remittances and evacuation key concerns'],
            ['1992-2004', 'Normalisation and diversification', '**Full diplomatic ties with Israel (1992)**: defence, agriculture, water, technology; ties with the Arab world and Iran continued'],
            ['2005-2013', 'Look West Policy', 'Wider economic, energy, diaspora and strategic engagement'],
            ['2014-2019', 'De-hyphenation', 'Israel, Iran and the Gulf engaged simultaneously; Israel separated from Palestine, Iran from Gulf rivalries'],
            ['2020-23', 'Geo-economic integration', '**I2U2, IMEC and the Abraham Accords**: connectivity, food security, clean energy, investment, technology: beyond oil'],
            ['2023-26', 'Crisis resilience', 'The **Gaza war, Red Sea attacks and Iran-Israel war**: focus on energy security, maritime security, diaspora protection, crisis management'],
        ]),
    ], label='Class + handout'))

    # 3 Three axes & major powers
    secs.append(Sec('West Asia: three axes and the major powers', [
        p('The region is easiest to read through **three axes: Israel (and the Palestine question), Iran, and the Gulf states**, plus the competing interests of the US, China and Russia.'),
        tbl('The three axes (slides 5 and 7, handout p. 79)', ['Axis', 'Background and present character'], [
            ['Israel and the Palestine question', 'After the First World War Palestine came under the **British Mandate**; the **Balfour Declaration (1917)** supported a Jewish national home. The **UN proposed separate Arab and Jewish states in 1947**; Israel declared independence in **1948**, followed by the first Arab-Israeli war. The **1967 war** brought the West Bank, East Jerusalem and Gaza under Israeli occupation. Unresolved: statehood, Jerusalem, settlements, refugees, Israeli security. The widely supported framework is a **two-State solution**. Israel has a close strategic relationship with the US. The **Abraham Accords (2020)** normalised ties with the **UAE and Bahrain** but did not resolve Palestine. The latest conflict began with the **Hamas-led attack of 7 October 2023**; despite a **2025 ceasefire**, violence and the humanitarian crisis continued into 2026'],
            ['Iran', 'A US partner under the **Shah**; the **1979 Islamic Revolution** transformed its relations with the US and Israel. A major Shia power with influence through partners and armed groups in **Iraq, Lebanon, Syria and Yemen**. Its nuclear programme brought sanctions. The **JCPOA (2015)** limited it; the **US withdrew in 2018**. In **2026**, direct conflict involving the **US, Israel and Iran** became the region’s most serious crisis and disrupted energy through **Hormuz**'],
            ['Gulf states', 'The **GCC**: Saudi Arabia, UAE, Qatar, Kuwait, Oman, Bahrain. Mostly Sunni-ruled monarchies with different foreign policies; major oil and gas; historically dependent on the US for security. With Iran: rivalry and selective engagement (Saudi-Iran competition; **Oman and Qatar** keep broader channels). On Israel: the UAE and Bahrain normalised in 2020; **Saudi Arabia has not**. Now diversifying towards India, China, Europe and others'],
        ]),
        '<div class="two">' + fig('img/ir-ext-israel-palestine.jpg', 'Israel-Palestine: Gaza Strip, West Bank and Jerusalem, with control as of October 2026. The map notes: West Bank occupied since 1967, the Palestinian Authority administers parts of Areas A and B, Israel controls settlements and Area C; Israel controls Jerusalem, East Jerusalem’s annexation is not internationally recognised and Palestinians claim it as a future capital; Gaza is fragmented, Israel controls about two-thirds (slide 6; also in the handout).', 'Class slide map') + fig('img/ir-ext-west-asia.jpg', 'West Asia and India’s key interests: Israel (defence technology, agriculture, water), Iran (Chabahar, access to Central Asia), Saudi Arabia (energy, defence), UAE (energy, investment, logistics), Oman (maritime security, Gulf connectivity), Qatar (LNG) (slide 9).', 'Class slide map') + '</div>',
        tbl('What the major powers want (slide 8, handout pp. 79-80)', ['Power', 'Interests in West Asia'], [
            ['United States and Europe', 'The most important external security actor: Israel’s security, Gulf bases and partnerships, **preventing an Iranian nuclear weapon**, energy and sea routes, supported the Abraham Accords; the 2026 conflict reinforced its military role. Several **European** states take stronger positions for Palestinian statehood and against settlements'],
            ['China', 'Economics, energy and diplomacy: oil and gas, trade and infrastructure with both Iran and the Gulf, BRI sea routes; relations with all camps; brokered the **Saudi-Iran rapprochement (2023)**; supports a two-State solution while trading with Israel'],
            ['Russia', 'Strategic influence, energy and security: close ties with Iran; **military intervention in Syria from 2015**; relations with Israel and the Gulf; **OPEC+** with Gulf producers; supports Palestinian statehood'],
            ['India', 'Energy, diaspora, connectivity, defence, trade and maritime stability'],
        ], desc='Slide 8: “India’s approach differs: it seeks relations **across competing camps** while preserving strategic autonomy and freedom of navigation.”'),
    ], label='Class + handout'))

    # 4 Israel and Palestine
    secs.append(Sec('India-Israel and the Palestine question', [
        p('India no longer treats West Asia mainly as a source of oil. With **Israel** the relationship is a **high-technology strategic partnership**, while India keeps an **independent position on Palestine**.'),
        tbl('India-Israel (slide 10, handout p. 80)', ['Area', 'Key cooperation'], [
            ['Diplomatic', 'India **recognised Israel in 1950**; **full diplomatic relations in 1992**'],
            ['Defence', '**Barak** missiles, **Phalcon** airborne warning systems, **Heron** drones'],
            ['Technology', 'Cybersecurity, AI, space, critical technologies'],
            ['Agriculture and water', 'Irrigation, water management, agricultural innovation'],
            ['Economic', 'Merchandise trade about **US$3.93 billion (FY 2025-26)**; the **second round of FTA negotiations** concluded in **July 2026**'],
            ['Strategic upgrade', '**February 2026**: a **Special Strategic Partnership for Peace, Innovation and Prosperity**'],
        ]),
        tbl('India and Palestine (slide 11, handout p. 80)', ['Point', 'Detail'], [
            ['Approach', '**De-hyphenated**: Israel and Palestine are separate, independent relationships'],
            ['Support for Palestine', 'Longstanding political and development support; continued humanitarian aid'],
            ['Landmark', 'The PM’s **2018 visit to Ramallah**: the first by an Indian Prime Minister'],
            ['Position', 'A **negotiated two-State solution**: Israel and Palestine side by side in peace and security'],
        ]),
        teacher('Class slide stress (slide 11)', '**Approach: Cooperation with Israel without abandoning support for Palestinian statehood.**'),
    ], label='Class + handout'))

    # 5 Iran and the Gulf
    secs.append(Sec('India-Iran and India-Gulf', [
        tbl('India-Iran: strategically important, externally constrained (slide 12, handout pp. 80-81)', ['Dimension', 'Key point'], [
            ['Connectivity', '**Chabahar** gives access to Afghanistan and Central Asia without Pakistan'],
            ['2024 agreement', '**May 2024: 10-year contract** to equip and operate the **Shahid Beheshti Terminal**'],
            ['INSTC', 'Iran is central to the **International North South Transport Corridor** and India’s Persian Gulf interests'],
            ['Constraints', 'Sanctions, banking restrictions and regional conflict limit trade and investment'],
            ['Maritime interest', 'The 2026 conflict made **freedom of navigation through Hormuz** an immediate concern'],
            ['Diplomacy (handout)', 'PM Modi and President **Pezeshkian** met at the **SCO Summit (August 2026)** and the **BRICS Summit (September 2026)**; India stressed dialogue, peace and protection of shipping'],
            ['Citizen protection', '**Operation Sindhu (2025)** evacuated **3,597 Indians from Iran** and **818 from Israel**'],
        ]),
        tbl('India and the Gulf: the economic and people-centred core (slide 13, handout p. 81)', ['Dimension', 'Importance'], [
            ['Trade', 'India-GCC trade **US$178.56 billion (FY 2024-25)**'],
            ['Energy', 'Crude oil, LNG, LPG and petrochemicals'],
            ['Diaspora', '**Nearly 10 million** Indians across GCC states'],
            ['Investment', 'Sovereign wealth funds and infrastructure'],
            ['Security and new sectors', 'Defence, counter-terrorism, maritime cooperation; digital, renewables, food security, logistics'],
            ['Trade architecture', '**India-GCC FTA negotiations formally launched in February 2026**'],
        ]),
        tbl('Key Gulf partners (slides 14-15, handout pp. 81-82)', ['Country', 'What stands out'], [
            ['UAE', 'India’s **most diversified Gulf partnership**. **CEPA (2022)**. Trade **US$101.25 billion (FY 2025-26)**, over US$100 billion for the first time; target **US$200 billion by 2032**. **Local Currency Settlement** (rupee-dirham). A **Letter of Intent for a Strategic Defence Partnership** (UAE President’s **January 2026** visit) and a broader framework (PM’s **May 2026** visit). Central to **IMEC**. A proposed **US$11.5 billion** UAE-linked aluminium investment in **Odisha** (September 2026)'],
            ['Saudi Arabia', 'Crude oil and Indian workers. The **India-Saudi Strategic Partnership Council (2019)**; a **Ministerial Committee on Defence Cooperation (April 2025)**. The **first India Pavilion at the World Defence Show, Riyadh (February 2026)**. Direct high-level engagement on the community during the 2026 conflict'],
            ['Qatar', 'LNG security and long-term gas supplies'],
            ['Oman', 'Maritime access near Hormuz; **Duqm Port**. The **India-Oman CEPA** came into force on **1 June 2026**: duty-free access to **98.08%** of Oman’s tariff lines, covering **99.38%** of India’s exports by value'],
            ['Kuwait and Bahrain', 'Energy, diaspora, investment, wider GCC engagement'],
        ]),
    ], label='Class + handout'))

    # 6 West Asia matters, challenges, way forward
    secs.append(Sec('West Asia: stakes, challenges and way forward', [
        tbl('Why West Asia matters (slide 16, handout p. 82)', ['Interest', 'Significance'], [
            ['Energy security', 'A substantial share of India’s crude, LNG and LPG; **Hormuz**: the 2026 Iran conflict hit oil prices, shipping, insurance and inflation; India stressed safe navigation with both Iran and the UAE'],
            ['Trade and investment', 'GCC trade US$178.56 bn; UAE US$101.25 bn; **Gulf sovereign wealth funds** in Indian infrastructure, energy, finance, logistics, manufacturing'],
            ['Diaspora', 'Nearly 10 million Indians in the GCC make stability a **domestic** concern; Operation Sindhu'],
            ['Connectivity', '**Chabahar** (Afghanistan, Central Asia) and **IMEC** (Europe via the Gulf and Mediterranean); conflict delays both'],
            ['Maritime security', 'Hormuz (energy); **Bab-el-Mandeb and the Red Sea** (India-Europe trade). **Operation Sankalp** protects merchant shipping and seafarers'],
        ]),
        tbl('Challenges (slide 17, handout pp. 82-83)', ['Challenge', 'Concern'], [
            ['Regional conflicts', 'India keeps ties with opposing sides; the 2026 US-Israel-Iran conflict made balancing harder; Israel-Palestine; Yemen and the Houthis'],
            ['Energy and chokepoints', 'Hormuz disruption hits crude, LNG, LPG; Red Sea disruption forces ships round Africa; freight, insurance and fuel costs feed inflation'],
            ['Connectivity under pressure', 'Conflict involving Israel can slow **IMEC**; sanctions on Iran constrain **Chabahar**: India needs **multiple routes**'],
            ['Great-power competition', 'US sanctions affect Iran ties; China’s expanding Gulf role; Russia via Iran, Syria and energy'],
            ['Diaspora and labour', 'Airspace closures and evacuations; wage disputes, recruitment abuse, **passport retention**'],
            ['Political differences', '**OIC statements on Jammu and Kashmir** differ from India’s position; Israel ties do not always align with Arab positions'],
        ]),
        tbl('Way forward (slide 18, handout p. 83)', ['Priority', 'Way forward'], [
            ['Strategic autonomy', 'Preserve **de-hyphenation**; never make one relationship conditional on another; consistent principles on terrorism, civilians, sovereignty, humanitarian access and the two-State solution'],
            ['Energy and maritime', 'Diversify crude, LNG and LPG suppliers; more **strategic petroleum reserves** and gas storage; maritime domain awareness around Hormuz, Bab-el-Mandeb and the Arabian Sea; alternative shipping and insurance'],
            ['Connectivity', 'Develop **both Chabahar and IMEC**, not one route; link ports, customs, digital platforms and logistics'],
            ['Gulf integration', 'Advance the **GCC FTA**; use the **UAE and Oman CEPAs**; renewables, green hydrogen, manufacturing, food security; the UAE and Saudi Arabia as gateways to Africa'],
            ['Defence', 'Build on the 2026 India-UAE defence framework; expand with Saudi Arabia, Oman and others; counter-terrorism, cyber, maritime intelligence'],
            ['Diaspora', 'Worker registration, emergency contacts, action against recruitment fraud, evacuation plans and funds; lessons from Operation Sindhu'],
            ['Regional stability', 'Engage all actors; support dialogue and a viable two-State solution; protect freedom of navigation and seafarers'],
        ]),
        teacher('Class slide stress: conclusion (slide 18)', '**India’s West Asia policy rests on simultaneous engagement with competing regional actors.** Success depends on strategic autonomy, diversified partnerships, secure energy and maritime routes and strong citizen protection **without entering rigid regional alignments**.'),
    ], label='Class + handout'))

    # 7 ASEAN
    secs.append(Sec('India-ASEAN: nature, evolution and convergence', [
        p('“**ASEAN centrality is at the heart of India’s Act East Policy; this is the Asian century, and India and ASEAN will shape it together.**” (PM Narendra Modi, 21st ASEAN-India Summit, Vientiane, 2024.) **ASEAN** is a regional organisation of **11** Southeast Asian countries. It is the **anchor of Act East** and a pillar of India’s Indo-Pacific strategy. India wants a free, open, inclusive Indo-Pacific built around ASEAN centrality, **without being drawn into US-China rivalry or the South China Sea disputes**.'),
        tbl('Nature of the relationship (slide 19, handout p. 85)', ['Nature', 'Meaning'], [
            ['Stable partnership', 'Little direct political friction'],
            ['Institutionally mature', 'Regular summits and ASEAN-led mechanisms'],
            ['Strategic convergence', 'Shared preference for an inclusive order without rigid blocs'],
            ['Economic gap', 'Trade and production integration lag strategic relations'],
            ['Connectivity deficit', 'Projects slower than political engagement'],
        ]),
        teacher('Class slide stress (slide 19)', '**Present character: Strategic convergence with under-realised economic potential.**'),
        fig('img/ir-ext-asean.jpg', 'ASEAN map (slide 20; also in the handout).', 'Class slide map'),
        tbl('Evolution (slide 21, handout p. 85)', ['Phase', 'Keyword', 'Key developments'], [
            ['Ancient-1991', 'Civilisational and maritime ties', 'Maritime trade, Hinduism, Buddhism, temple culture'],
            ['1991-95', 'Look East begins', 'Liberalisation led to **Look East**. India became a **Sectoral Partner (1992)** and **Dialogue Partner (1995)**'],
            ['2002-10', 'Institutional and economic integration', '**First ASEAN-India Summit (2002)**; **AITIGA in force (2010)**'],
            ['2014-19', 'Act East and strategic depth', '**Act East Policy (2014)** added strategic and security cooperation; **Indo-Pacific Oceans Initiative (2019)**'],
            ['2022', 'Comprehensive Strategic Partnership', 'Ties elevated across economic, security and connectivity areas'],
            ['2025', 'Expanded engagement', 'Indonesia’s President **Prabowo Subianto** was **Republic Day chief guest**; **Timor-Leste became ASEAN’s 11th member**'],
            ['2026', 'Strategic and economic deepening', 'PM’s **Indonesia** visit: defence, critical minerals, agriculture, industry, maritime cooperation'],
        ]),
        tbl('Areas of convergence (slide 22, handout pp. 85-86)', ['Area', 'Key points'], [
            ['Trade and value chains', 'India’s market, services and technology complement ASEAN manufacturing. Trade **US$128.38 billion (FY 2025-26)**, about **10% of India’s trade**. ASEAN received **US$3.5 billion FDI** from India (2024). The **2026 AITIGA review** covers customs, market access and rules of origin'],
            ['Connectivity', 'The Northeast as a gateway: the **Trilateral Highway** and **Kaladan**'],
            ['Digital and people', '**UPI-PayNow** expanded to **19 Indian banks** (July 2025). **5.9 million** Indian travellers to ASEAN (2024). Up to **1,000 doctoral fellowships at IITs** for ASEAN citizens'],
            ['Energy and minerals', 'ASEAN targets **45% renewable capacity by 2030**; India supports the **ASEAN Power Grid**. **Indonesia’s nickel refining** for minerals cooperation'],
            ['Maritime security', 'ASEAN-led mechanisms; exercises and information sharing; **2026 ASEAN-India Year of Maritime Cooperation**. Non-traditional threats: cybercrime, trafficking, online scams'],
            ['HADR and climate', 'India’s naval, medical and logistics capabilities; the **ASEAN-India Maritime Exercise 2026** included HADR training; early warning and resilient infrastructure'],
            ['Environment and culture', 'Blue and green economy (fisheries, pollution, sustainable tourism); Buddhist, Ramayana and maritime heritage; **2025 ASEAN-India Year of Tourism**'],
        ]),
    ], label='Class + handout'))

    # 8 ASEAN divergence
    secs.append(Sec('India-ASEAN: challenges and way forward', [
        tbl('Challenges (slide 23, handout pp. 86-87)', ['Challenge', 'Key concern'], [
            ['Trade imbalance', 'Imports exceed exports: FY 2025-26 deficit about **US$51.55 billion**. Weak production linkages; the **China-ASEAN FTA 3.0 (2025)** deepened China’s integration'],
            ['RCEP and rules of origin', 'India’s withdrawal from **RCEP** limits integration; third-country routing and weak verification complicate AITIGA reform'],
            ['China factor', 'ASEAN’s consensus-based, inclusive approach and economic interdependence with China limit strategic convergence'],
            ['Connectivity delays', 'Myanmar instability; **Kaladan** has problems in its port, river and road parts'],
            ['Energy and minerals', 'Fossil-fuel dependence; the **APAEC 2026-2030** flags energy-security pressure; mineral **processing** remains concentrated'],
            ['Security and climate gaps', 'Fragmented cyber enforcement; last-mile relief blocked by conflict; unequal adaptation finance; development-environment trade-offs'],
        ]),
        tbl('Way forward (slide 24, handout p. 87)', ['Priority', 'Way forward'], [
            ['ASEAN centrality', 'Measurable targets under the **2026-30 Plan of Action**, monitored by the **Joint Cooperation Committee**; ASEAN-led mechanisms, Quad and IPOI, with strategic autonomy'],
            ['Value chains and trade', 'Joint electronics, pharma and EV-component chains linking MSMEs; a balanced **AITIGA review** with simpler customs, stronger rules of origin, fewer non-tariff barriers'],
            ['Connectivity', 'Complete the Trilateral Highway and Kaladan; Northeast logistics and digital customs'],
            ['Energy and minerals', 'Renewables, storage, grid links; tie offtake to joint processing and skills'],
            ['Maritime and HADR', 'Information-sharing, coast guards, maritime domain awareness; pre-positioned relief with the **AHA Centre**; resilient ports and early warning through **CDRI**'],
            ['Sustainable growth', 'Marine spatial planning, ecosystem restoration, sustainable fisheries; inclusive development'],
        ]),
        teacher('Class slide stress (slide 24)', '**Direction: Move from strategic convergence to stronger economic integration, connectivity and maritime cooperation.** The handout ends: move “beyond ASEAN centrality as a slogan”, aligning **Act East and Viksit Bharat 2047** with **ASEAN 2045 (Our Shared Future)**.'),
    ], label='Class + handout'))

    # 9 Indo-Pacific significance and visions
    secs.append(Sec('The Indo-Pacific: significance and competing visions', [
        p('The **Indo-Pacific** links the Indian and Pacific Oceans, broadly **from the eastern coast of Africa to the western shores of the Americas**: the Indian Ocean Region, South Asia, Southeast Asia, East Asia, Oceania and the Pacific, with **ASEAN at its centre**. For India it is not only a security concept but the space through which its trade, energy, supply chains and maritime interests operate.'),
        fig('img/ir-ext-indo-pacific.jpg', 'The Indo-Pacific region, spanning the Indian and Pacific Oceans (slide 25; also in the handout).', 'Class slide map'),
        tbl('Significance for India (slide 26, handout p. 88)', ['Dimension', 'Importance'], [
            ['Trade, energy, chokepoints', 'Sea routes to West Asia, Africa, ASEAN, East Asia and the Americas; **Malacca, Hormuz and Bab-el-Mandeb**; disruption raises freight, fuel and inflation'],
            ['Markets and supply chains', 'ASEAN, China, Japan, South Korea, Australia; diversification in electronics, pharma, semiconductors, advanced manufacturing; the Northeast as a gateway'],
            ['Critical minerals', '**Australia and Indonesia**: rare earths for EVs, batteries, renewables, semiconductors, defence; India-Indonesia cooperation strengthened in 2026'],
            ['Maritime and national security', 'Piracy, trafficking, submarines, attacks on shipping. The **Andaman and Nicobar Islands** sit near the **Malacca Strait**. **IFC-IOR, Operation Sankalp**, exercises and maritime domain awareness'],
        ]),
        tbl('Competing visions (slide 27, handout p. 89)', ['Stakeholder', 'Preferred regional order'], [
            ['India', 'Free, open, inclusive and **multipolar**; ASEAN centrality, sovereignty, international law, freedom of navigation; **balancing without formal alliances**'],
            ['United States', 'A favourable balance through **alliances, forward presence** and partnerships such as the Quad; **deterrence of China**'],
            ['China', 'Opposes “containment-oriented” groupings; wants its economic weight and connectivity at the centre'],
            ['ASEAN', '**ASEAN centrality**, no bloc politics, dialogue and inclusivity'],
            ['Japan', '**Free and Open Indo-Pacific**: rule of law, navigation, connectivity, economic security'],
            ['Australia', 'Rules-based order backed by stronger deterrence and partnerships, while supporting ASEAN centrality'],
        ]),
    ], label='Class + handout'))

    # 10 Indo-Pacific challenges & strategy
    secs.append(Sec('The Indo-Pacific: challenges and India’s strategy', [
        tbl('Challenges (slide 28, handout pp. 89-90)', ['Challenge', 'Concern'], [
            ['China’s footprint', 'BRI-linked ports, dual-use facilities, naval deployments; in the South China Sea, grey-zone coercion, coast guards and maritime militias; **no ASEAN-China Code of Conduct**'],
            ['Chokepoints', 'Hormuz, Bab-el-Mandeb, Malacca: diversifying suppliers cannot remove route dependence'],
            ['Divergent visions', 'India (inclusive, non-alliance), the US (deterrence, alliances), ASEAN (non-bloc): a common security architecture is hard'],
            ['Critical-mineral dependence', 'Processing concentrated; **China’s** influence over rare-earth chains; export controls'],
            ['Maritime and undersea security', 'Submarines, piracy, drones, cyberattacks; **undersea cables, pipelines, ports**; need for seabed monitoring'],
            ['Trade and connectivity gaps', 'Weak East Asian production links; ASEAN trade imbalance; Trilateral Highway and Kaladan delays'],
        ]),
        tbl('India’s Indo-Pacific strategy (slide 29, handout p. 90)', ['Priority', 'Approach'], [
            ['Inclusive order', 'Avoid turning partnerships into a **formal anti-China bloc**'],
            ['Manage China', '**Dialogue + deterrence + de-risking** (not complete decoupling)'],
            ['ASEAN centrality', 'Link the **IPOI** with the **ASEAN Outlook on the Indo-Pacific (AOIP)**'],
            ['Maritime capability', 'Navy, anti-submarine warfare, logistics'],
            ['Maritime awareness', 'Expand **IFC-IOR**, satellites, information sharing; **AIME-2026** and the Year of Maritime Cooperation'],
            ['Regional platforms', '**Quad, IORA, ADMM-Plus, EAS and MILAN**'],
            ['Trade and connectivity', 'AITIGA review; Trilateral Highway and Kaladan; the Northeast gateway'],
            ['Critical minerals', '**Access + processing + refining + recycling**, with Australia, Indonesia, Japan and Quad partners'],
            ['HADR', 'Early warning, satellite data, disaster-response technology'],
        ]),
        alert('Handout alert: a garbled line', 'The handout’s energy-security point reads “Divzd cooperation in renewables, hydrogen, batteries and storage” (cut off in print). The sense is to diversify and expand cooperation in renewables, hydrogen, batteries and storage. Check class notes.'),
        teacher('Class slide stress: conclusion (slide 29)', 'India’s Indo-Pacific strategy should **combine credible maritime power with inclusive partnerships**, guided by **Act East, MAHASAGAR, ASEAN centrality and strategic autonomy**.'),
    ], label='Class + handout'))

    return build_rest(secs)
