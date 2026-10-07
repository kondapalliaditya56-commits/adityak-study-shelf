# -*- coding: utf-8 -*-
from lib import *
from ch03b import *

CH = {'n': 3, 'title': 'India and its Neighbourhood',
      'sub': 'Neighbourhood policy, then Pakistan, Afghanistan, Bangladesh, Nepal, Bhutan, Myanmar, Sri Lanka and the Maldives',
      'badge': 'High · Mains', 'slides': True}

SRC = ('Class slides “India’s Neighbourhood” PPT-4 (43 slides) and handout Chapter 3, pages 1-27 '
       '(uploaded as “GS-2 International Relations - 4”)')

# (year/marks/words, question, answer or trap, where covered, source)
PYQ = [
    ('Mains 2024 · 15 marks · 250 words', 'Discuss the geopolitical and geostrategic importance of Maldives for India with a focus on global trade and energy flows. Further also discuss how this relationship affects India’s maritime security and regional stability amidst international competition?', 'Two parts: importance (location, sea lanes), then effect on India’s security. See the skeleton in Practice.', 'Section 13', 'handout p. 27'),
    ('Mains 2022 · 10 marks · 150 words', 'India is an age-old friend of Sri Lanka. Discuss India’s role in the recent crisis in Sri Lanka in the light of the preceding statement.', 'First responder: about US$4 bn in 2022. See the skeleton in Practice.', 'Section 12', 'handout p. 27'),
    ('Mains 2015 · 12.5 marks · 200 words', '“Project ‘Mausam’ is considered a unique foreign policy initiative of the Indian Government to improve relationships with its neighbours. Does the project have a strategic dimension? Discuss.”', '**Thin notes:** Project Mausam is only named (Maldives way forward). See the skeleton in Practice.', 'Section 13 (one line)', 'handout p. 27'),
    ('Mains 2015 · 12.5 marks · 200 words', '“Terrorist activities and mutual distrust have clouded India-Pakistan relations. To what extent the use of soft power like sports and cultural exchange could help generate goodwill between the two countries? Discuss with suitable examples.”', '“To what extent”: soft power helps people, not the core dispute. See the skeleton in Practice.', 'Sections 5 and 6', 'handout p. 27'),
]


def build():
    secs = []

    # ---------------------------------------------------------------- exam lens
    exam = []
    exam.append(callout('source', 'Source note',
        '**This chapter has class slides and a handout.** ' + SRC + '. The slides are typed with **no handwriting or board ink**, so the teacher’s stress is read from the slides’ “Core idea” and “Conclusion” lines. Slides 1 and 43 carry no text (title and closing). Each country gets the same five slides or fewer: nature, evolution, convergence and divergence, a map where there is one, and way forward. The handout adds the detail: figures, dates, project names and the reasoning. The material quotes **no Prelims PYQs**; its PYQ box lists four Mains questions.'))
    exam.append(tbl('What the slides stress', ['Signal in the material', 'Where', 'Why it matters'], [
        ['“**Core idea: Neighbourhood First prioritises physical, digital and people-to-people connectivity, trade and commerce.**”', 'Slide 4', 'The one-line definition of the policy.'],
        ['“**Core idea: Geography creates permanent interdependence, but politics and security determine whether it produces cooperation or friction.**”', 'Slide 5', 'An opening line for any neighbourhood answer.'],
        ['“**Core idea: Combine the Gujral Doctrine and non-reciprocity with Neighbourhood First’s focus on connectivity, security and development to build trust rather than dependence.**”', 'Slide 6', 'A ready closing line.'],
        ['Pakistan: “**Core idea: Credible deterrence + escalation control + limited functional engagement.**”', 'Slide 8', 'The three-part frame for any Pakistan answer.'],
        ['Afghanistan: “**engagement without endorsement**”; conclusion “engagement without recognition, people-level goodwill, counter-terrorism and connectivity”', 'Slides 13 and 17', 'The phrase to use for India’s Taliban policy.'],
        ['Bangladesh: “a **strategic reset** amid political transition, water issues and China’s growing role”', 'Slide 18', 'The current state in four words.'],
        ['Nepal: “civilisational and people-centred partnership rooted in religion, open border and **Roti-Beti** relations”', 'Slide 22', 'Why closeness also creates mistrust.'],
        ['Bhutan: “**Core idea: Bharat for Bhutan, Bhutan for Bharat**”', 'Slide 26', 'India’s most stable partnership.'],
        ['Myanmar: “tests India’s ability to **balance values, security and connectivity**. The best approach is **calibrated engagement**.”', 'Slide 33', 'The dilemma and the answer.'],
        ['Maldives: “vital because of its **strategic location, not size**”', 'Slide 42', 'The first line of the 2024 PYQ answer.'],
    ]))
    exam.append(tbl('PYQs quoted in the material (Mains only)', ['Year, marks, words', 'What was asked', 'Answer or trap', 'Where in this chapter', 'Source'],
        [[a, b, c, d, e] for (a, b, c, d, e) in PYQ],
        desc='Mains years quoted: 2015 (two), 2022, 2024. Prelims years quoted: none quoted in the material. The Mains 2026 question on the BRI in South Asia is quoted in the Chapter 1 and 2 handouts and is answered in Chapter 2; this chapter gives it its neighbour-by-neighbour evidence.'))
    exam.append(tbl('Priority by neighbour (from the material)', ['Neighbour', 'PYQ quoted in the handout', 'What the material stresses'], [
        ['Maldives', 'Mains 2024 (15 marks)', 'Location, first responder, “India Out” to reset'],
        ['Sri Lanka', 'Mains 2022 (10 marks)', 'Crisis partnership, Tamil issue, fisheries'],
        ['Pakistan', 'Mains 2015 (soft power)', 'Deterrence, escalation control, limited engagement; 2025 escalation'],
        ['All neighbours', 'Mains 2015 (Project Mausam)', 'Neighbourhood First, Gujral Doctrine'],
        ['Bangladesh, Nepal, Bhutan, Myanmar, Afghanistan', 'none quoted in the material', 'Each has a one-phrase frame on the slides (see the table above)'],
    ], desc='The slides carry no stars or “important” marks. The handout’s PYQ box is the only priority signal.'))
    exam.append(callout('note', 'From the PYQ Lab (outside the class material)', 'In the ten GS-II papers of 2017-2026, only **4 of 40** International Relations questions were about a named neighbour or South Asia (China 2017, Sri Lanka 2022, Maldives 2024, BRI in South Asia 2026). Pakistan, Bangladesh, Nepal, Bhutan, Myanmar and Afghanistan were not asked by name. Each neighbourhood question followed a crisis or shift next door. So prepare this chapter as **themes** (crisis response, connectivity, water, the China factor), with each country as the example.'))
    exam.append(callout('key', 'What to prepare',
        '**Prelims hooks:** Gujral Doctrine (1996); SAARC (1985); BIMSTEC and IORA (1997); Indus Waters Treaty (1960), western and eastern rivers; Shimla Agreement (1972); Operation Meghdoot (1984); 1988 nuclear-installations agreement; Kartarpur Corridor (2019); Sir Creek; Operation Devi Shakti; Shahid Beheshti Terminal; UNSC Resolution 2593; 4,096 km border; Land Boundary Agreement (2015): 111 and 51 enclaves; Ganga Treaty (1996, expires December 2026); Kushiyara (153 cusecs); 1950 Treaty; Kalapani, Lipulekh, Limpiyadhura; Koshi (1954), Gandak (1959), Mahakali (1996); Arun-III (900 MW); 2007 Treaty with Bhutan; Operation All Clear (2003); Punatsangchhu-I and II; Gelephu Mindfulness City; 1,643 km border; Kaladan; Kyaukphyu; Operation Brahma; Sirimavo-Shastri Pact; 13th Amendment; Katchatheevu (1974, 1976); Operation Sagar Bandhu; Operation Cactus (1988); Operation Neer (2014); Ekuverin, Ekatha, Dosti; Greater Malé Connectivity Project.\n\n'
        '**Mains hooks:** “Big Brother” perception and how to reduce it; China’s footprint in each neighbour; rivers as cooperation and conflict; first-responder diplomacy; domestic politics next door (Bangladesh 2024, Maldives 2023, Nepal 2025-26) and inside India (Teesta, Katchatheevu); delivery gaps (Kaladan, Trilateral Highway, Pancheshwar, Punatsangchhu-I); engagement without recognition (Taliban, Myanmar’s military).\n\n'
        '**Closing idea:** India should combine the Gujral Doctrine’s non-reciprocity with Neighbourhood First’s connectivity, security and development, to build a neighbourhood based on **trust rather than dependence**.'))
    secs.append(Sec('Exam lens: priority and PYQs', exam, sid='exam-lens-priority-and-pyqs'))

    # ---------------------------------------------------------------- 1 overview
    secs.append(Sec('India’s neighbourhood: overview and India’s interests', [
        p('India and its neighbourhood is a **civilisational region** shaped by shared history, culture, geography and socio-economic links. **Colonial rule, Partition and modern state formation** drew political borders across these older connections. Today, interdependence in trade, connectivity, energy and security makes India central to the region’s economic and security dynamics.'),
        tbl('The neighbourhood in five lines (slide 2)', ['Aspect', 'Meaning'], [
            ['Civilisational links', 'Shared history, culture, religion and communities'],
            ['Colonial legacy', 'Partition and modern borders divided older connections'],
            ['Regional interdependence', 'Trade, rivers, energy, migration and security'],
            ['India’s centrality', 'India shapes regional economic and security dynamics'],
            ['Geographical spread', 'South Asia plus the wider Indian Ocean Region: land and maritime neighbourhoods'],
        ], desc='**Countries:** Pakistan, Afghanistan, Bangladesh, Nepal, Bhutan, Myanmar, Sri Lanka, Maldives and China. (China is covered in Chapter 2.)'),
        fig('img/ir-nb-map.jpg', 'India and its neighbours (handout p. 1; the same map is on slide 3). The map is marked “not to scale”.', 'Handout map'),
        p('India’s neighbourhood directly affects its **security, economy, connectivity and regional influence**. Stable relations with neighbours are a basic requirement of India’s foreign policy.'),
        tbl('India’s interests in its neighbourhood (slide 4, handout p. 1)', ['Interest', 'Why it matters', 'Examples'], [
            ['National security', 'Instability next door reaches India’s border and internal security through terrorism, insurgency and cross-border threats', 'Terrorism from **Pakistan**, insurgent movements from **Myanmar**, instability in **Afghanistan**'],
            ['Trade and connectivity', 'Links India’s frontier and landlocked regions with wider markets', '**Bangladesh** gives access to the Northeast; **Myanmar** connects India to Southeast Asia through **Kaladan** and the **India-Myanmar-Thailand Trilateral Highway**'],
            ['Energy security', 'Regional electricity trade and pipelines', 'Hydropower from **Bhutan and Nepal**; power trade among India, Nepal and Bangladesh'],
            ['Managing external influence', 'India wants a neighbourhood open to all, but not a source of security pressure', '**China’s** infrastructure, economic and defence presence'],
            ['People-to-people ties', 'Family, religion, language and migration cross borders, so relations are more than state-to-state diplomacy', 'India-Nepal **open border**; Buddhist links with Bhutan and Sri Lanka; ethnic ties across the India-Myanmar border'],
            ['Regional stability', 'Cooperation is essential', 'Border management, maritime security, disaster response and sea-lane security'],
        ]),
        teacher('Class slide stress: “Core idea” (slide 4)', '**Neighbourhood First prioritises physical, digital and people-to-people connectivity, trade and commerce.** The handout says the same of India’s official Neighbourhood First Policy.'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 2 challenges
    secs.append(Sec('Challenges in the neighbourhood', [
        p('Geographical closeness creates opportunities. It also means that political or security problems next door can quickly affect India.'),
        tbl('Eight challenges (slide 5, handout p. 2)', ['Challenge', 'Key concern', 'Example in the material'], [
            ['Political instability', 'Frequent political change disrupts established partnerships', 'Transitions in **Bangladesh**, instability in **Myanmar**, repeated political shifts in **Nepal**'],
            ['Security threats', 'Terrorism, insurgency, drug trafficking, cross-border crime', 'India-Pakistan tensions affect the wider region; Myanmar’s conflict brings arms trafficking, refugees and insurgent activity'],
            ['China’s growing presence', 'Infrastructure, trade, defence cooperation and BRI projects', '**CPEC** (Pakistan), **Hambantota** (Sri Lanka), **Kyaukpyu** (Myanmar), infrastructure in Nepal and Maldives'],
            ['Trust deficit', 'India’s size can create fear of dominance: the “**Big Brother**” perception', 'The “**India Out**” campaign in the Maldives: even security cooperation can become politically sensitive'],
            ['Weak regional integration', 'South Asia is poorly integrated compared with many other regions', 'India-Pakistan tensions have weakened **SAARC**; incomplete sections of **Kaladan** and the **Trilateral Highway**'],
            ['Domestic politics', 'Bilateral relations become part of domestic political competition', '**Teesta**: Indian state-level concerns can affect an international agreement'],
            ['Migration and refugees', 'Conflict produces large cross-border movements', 'Refugee flows from Myanmar into the Northeast'],
            ['Climate and environment', 'Shared rivers, floods, glacial risks, sea-level rise', 'India and Bangladesh manage **54 shared rivers**; Nepal and Bhutan matter for Himalayan flood and hydropower cooperation'],
        ]),
        teacher('Class slide stress: “Core idea” (slide 5)', '**Geography creates permanent interdependence, but politics and security determine whether it produces cooperation or friction.**'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 3 way forward
    secs.append(Sec('Way forward for neighbourhood policy', [
        p('India’s neighbourhood policy should focus **less on announcements and more on trust, delivery and long-term interdependence**.'),
        tbl('Eight priorities (slide 6, handout p. 2)', ['Priority', 'Way forward'], [
            ['Respect sovereignty', 'Deal with smaller neighbours as **equal sovereign partners**; this reduces fears of interference and the old “Big Brother” perception'],
            ['Security cooperation', 'Intelligence sharing, joint border management, maritime surveillance, action against trafficking and terrorism'],
            ['Border communities', 'Better roads, livelihoods and services in frontier areas. The **Vibrant Villages Programme** treats border communities as part of national security and connectivity'],
            ['Project delivery', 'Timely completion of roads, railways, ports, power lines and development projects builds **credibility**'],
            ['Economic integration', 'Easier customs, **border haats**, energy trade and investment. **Nepal-Bangladesh power trade through India** is a useful model. Strengthen BBIN, BIMSTEC, coastal shipping, rail links, energy grids, digital connectivity'],
            ['Subregional platforms', 'Where SAARC is blocked, use **BIMSTEC, BBIN and Indian Ocean platforms**'],
            ['Climate cooperation', 'Early-warning systems, disaster response and regular data-sharing on rivers, floods, cyclones and glacial risks'],
            ['People-centric diplomacy', 'Scholarships, healthcare, tourism, cultural exchanges and easier mobility create goodwill that **survives political change**'],
        ]),
        teacher('Class slide stress: “Core idea” (slide 6)', '**Combine the Gujral Doctrine and non-reciprocity with Neighbourhood First’s focus on connectivity, security and development to build trust rather than dependence.**'),
        callout('key', 'Gujral Doctrine (1996), as the handout defines it', '**Non-reciprocity, non-interference, respect for sovereignty and peaceful dispute resolution** with neighbours. The handout pairs its “accommodation and non-reciprocity” with Neighbourhood First.'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 4 evolution of policy
    secs.append(Sec('Evolution of India’s neighbourhood policy', [
        tbl('Eight phases (slide 7, handout p. 3)', ['Phase', 'Keyword', 'Key developments'], [
            ['Pre-1947', 'Imperial security', 'British India’s external policy was shaped by London’s imperial interests. **Nepal, Bhutan, Afghanistan and Tibet** were viewed as **strategic buffers**; **Myanmar was annexed into British India in 1885**'],
            ['1947-49', 'Partition and new borders', 'Independence and Partition created new boundaries and the India-Pakistan conflict (Kashmir). **Sri Lanka (1948) and Myanmar (1948)** became independent neighbours'],
            ['1950s-60s', 'Idealism and non-alignment', '**NAM, Panchsheel**, sovereignty, non-interference and peaceful coexistence; cooperative relations with neighbours without aligning with major blocs'],
            ['1962-65', 'Security recalibration', 'The **India-China War (1962)** and **India-Pakistan War (1965)** exposed vulnerabilities; greater emphasis on border security and preparedness'],
            ['1970s-80s', 'Regional assertiveness', '**Bangladesh Liberation War (1971)**, **India-Sri Lanka Accord (1987)**, **Operation Cactus in Maldives (1988)**. **SAARC (1985)** institutionalised regional cooperation'],
            ['1991-96', 'Economic regionalism', '**Look East Policy (1991)** expanded engagement eastward. **Gujral Doctrine (1996)**'],
            ['1997-2013', 'Multilateral regionalism', '**BIMSTEC and IORA, both established in 1997**, broadened engagement beyond SAARC, with focus on the Bay of Bengal and Indian Ocean'],
            ['2014-present', 'Proactive regional diplomacy', '**Neighbourhood First** put immediate neighbours and the Indian Ocean Region at the centre: connectivity, development, security, trade, people-to-people ties. **Act East** builds on Look East, with more stress on regional connectivity'],
        ]),
        mnemo('Memory aid: the eight keywords in order', 'IPISREMP', 'Imperial security, Partition, Idealism, Security recalibration, Regional assertiveness, Economic regionalism, Multilateral regionalism, Proactive diplomacy. Built from the handout’s own keywords.'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 5 Pakistan nature, evolution, convergence
    secs.append(Sec('India-Pakistan: nature, evolution and convergence', [
        p('India-Pakistan relations are South Asia’s **most persistent structural rivalry**, shaped by territorial disputes, cross-border terrorism, nuclear deterrence, water tensions and the China-Pakistan nexus. The **Pahalgam attack, Operation Sindoor and IWT abeyance in 2025** hardened the relationship further. Humanitarian and religious channels continue because complete disengagement between two nuclear-armed neighbours is difficult.'),
        tbl('Nature of the relationship (slide 8, handout p. 4)', ['Nature', 'Meaning'], [
            ['Security-driven rivalry', 'Cross-border terrorism and low political trust'],
            ['Territorial dispute', 'Jammu and Kashmir, Siachen and Sir Creek'],
            ['Nuclear deterrence', 'Discourages full-scale war but makes every crisis more dangerous'],
            ['China-Pakistan nexus', 'CPEC, Gwadar and the two-front challenge'],
            ['Limited engagement', 'Humanitarian, religious and consular channels continue'],
            ['Civil-military imbalance (handout)', 'The Pakistan Army’s dominant role in security and India policy limits civilian-led peace initiatives'],
        ]),
        teacher('Class slide stress: “Core idea” (slide 8)', '**Credible deterrence + escalation control + limited functional engagement.** The handout repeats the three as the frame of the relationship.'),
        tbl('Evolution (handout p. 4; slide 9 uses shorter rows)', ['Phase', 'Keyword', 'Key developments'], [
            ['1947-65', 'Partition and territorial conflict', 'Partition, the J&K dispute and the wars of **1947-48 and 1965** set the core rivalry. The **1960 Indus Waters Treaty** remained an important area of cooperation. Slide: **Tashkent Agreement** after 1965'],
            ['1971-84', 'Regional restructuring', 'The **1971 Bangladesh War** altered the regional balance. The **Shimla Agreement (1972)** emphasised **bilateralism**. **Operation Meghdoot (1984)** brought **Siachen** into the conflict'],
            ['1998-2007', 'Nuclearisation and peace efforts', '**1998 nuclear tests** made escalation control central. **Lahore, Kargil, the 2003 LoC ceasefire and the Composite Dialogue** showed alternating conflict and engagement'],
            ['2008-14', 'Terrorism and stalled dialogue', 'The **Mumbai attacks (2008)** disrupted the peace process and made cross-border terrorism the central obstacle'],
            ['2014-19', 'Engagement to punitive deterrence', 'Early outreach was followed by **Pathankot, Uri and Pulwama**. India responded with **surgical strikes (2016)** and **Balakot airstrikes (2019)**'],
            ['2021', 'Ceasefire restoration', 'The **DGMOs reaffirmed the 2003 LoC ceasefire**, reducing firing and restoring limited stability'],
            ['2025-26', 'Escalation and freeze', '**Pahalgam attack, Operation Sindoor, IWT abeyance** and diplomatic restrictions'],
        ]),
        tbl('Areas of convergence (slide 10, handout pp. 4-5)', ['Area', 'Key points'], [
            ['Ceasefire and nuclear risk reduction', 'The **2003 LoC ceasefire**, backed by the **DGMO channel**. In **May 2025** both sides agreed to stop firing and military action after the confrontation: direct crisis communication matters. Under the **1988 Agreement** both sides **annually exchange lists of nuclear installations**'],
            ['Humanitarian and consular', 'The **2008 Consular Access Agreement**: prisoner lists exchanged **twice a year**. Civilian prisoners and fishermen are among the few routine humanitarian channels'],
            ['Religious and cultural', 'The **1974 Shrines Protocol** facilitates pilgrimages. The **Kartarpur Corridor (opened 2019)** gives visa-free Sikh pilgrimage (**suspended amid the 2025 tensions**). Shared Punjabi, Sindhi and Sufi traditions'],
            ['Multilateral and regional', 'The **SCO** is a platform for both; India took part in the **SCO CHG (heads of government) meeting in Islamabad in 2024**. **SAARC** remains the institutional framework, severely constrained by bilateral tensions'],
        ]),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 6 Pakistan divergence, way forward
    secs.append(Sec('India-Pakistan: divergence and way forward', [
        tbl('Areas of divergence (slide 10, handout pp. 5-6)', ['Area', 'Key points'], [
            ['Cross-border terrorism', 'Pakistan-based networks (**LeT, JeM**) and Pakistan’s support to non-state actors are India’s primary security concern. Major attacks (**Mumbai, Pathankot, Uri, Pulwama, Pahalgam**) repeatedly disrupted dialogue. **Drones, cyber operations, missile exchanges and disinformation** add new crisis risks'],
            ['Territorial disputes', '**Jammu and Kashmir and Ladakh are integral and inalienable parts of India**; Pakistan disputes this and raises it internationally. India **rejects third-party mediation** and stresses bilateral resolution under the **Shimla Agreement**. **Siachen**: India seeks authentication of the **Actual Ground Position Line (AGPL)** before demilitarisation. **Sir Creek** is unresolved, affecting the maritime boundary, EEZ, fishing rights and offshore resources'],
            ['China-Pakistan nexus', 'India objects to **CPEC passing through Pakistan-occupied Kashmir** on sovereignty grounds. **Gwadar** adds a maritime dimension. Chinese weapons, drones and military technology feed India’s **two-front** concern'],
            ['Indus waters', 'The **1960 IWT** was one of the most durable bilateral agreements. India placed it **in abeyance after the April 2025 Pahalgam attack**; Pakistan rejects that position. Disputes over **Kishanganga, Ratle** and other hydropower projects add technical and political tension'],
            ['Trade and connectivity', 'Formal trade has been very limited **since 2019**. After Pahalgam India **closed the Attari Integrated Check Post** and further restricted Pakistan-origin imports. Pakistan’s geography limits India’s overland access to Afghanistan and Central Asia. India increasingly uses **BIMSTEC, BBIN and Indian Ocean platforms**'],
            ['Nuclear and escalation risks', 'Nuclear weapons limit full-scale war but create a **stability-instability paradox**: lower-level conflict can continue below the nuclear threshold. Terrorism, drones, cyber and missiles raise the risk of rapid escalation and miscalculation'],
        ]),
        '<div class="two">' + fig('img/ir-nb-sir-creek.jpg', 'Sir Creek between Sindh and Kutch, with the international border, the “Green Line”, Kajhar Creek and Kori Creek (handout p. 5, slide 11).', 'Handout map') + fig('img/ir-nb-iwt.jpg', 'The Indus Waters Treaty graphic (handout p. 5). The slide version marks the western rivers “Pakistan’s control” and the eastern rivers “India’s control”.', 'Handout graphic') + '</div>',
        tbl('Indus Waters Treaty: what the handout’s graphic says', ['Point', 'Detail'], [
            ['Signed', '**19 September 1960**, between India, Pakistan and a representative of the **World Bank**, after **eight years of negotiations**'],
            ['Why', 'Partition cut across the Indus basin: the Indus plus **five main tributaries**'],
            ['Western rivers', '**Chenab, Jhelum, Indus.** India’s rights are **limited**: certain irrigation, **run-of-the-river** power plants, very limited storage, domestic and non-consumptive use, all subject to conditions'],
            ['Eastern rivers', '**Sutlej, Beas, Ravi.** All **exclusive rights lie with India**'],
            ['Indus Waters Commission', 'A general inspection of all rivers in parts **once every five years**; meets **once a year**. The graphic counts over 100 inspection tours and over 100 meetings'],
            ['On the map', 'Kishenganga/Neelum; **Baglihar dam on the Chenab** (photo)'],
        ], desc='Memory aid from the graphic: **western = Indus, Jhelum, Chenab; eastern = Ravi, Beas, Sutlej.**'),
        tbl('Way forward (slide 12, handout p. 6)', ['Area', 'Way forward'], [
            ['Security and counter-terrorism', 'Link wider diplomatic reopening to **verifiable action** against terrorist groups, financing and infrastructure. Strengthen intelligence-sharing, counter-infiltration and counter-drone capabilities. Use **FATF standards, UN mechanisms** and bilateral channels against terror financing'],
            ['Nuclear risk and crisis management', 'Keep **DGMO hotlines and diplomatic backchannels** working for air, land or maritime incidents. Continue the annual nuclear-installation exchange; strengthen **missile-test notifications**'],
            ['Humanitarian', 'Insulate **fishermen, prisoners, pilgrims and urgent medical cases** from political tension; faster repatriation after nationality verification'],
            ['Water', 'Maintain essential **hydrological and flood-information channels** even while the IWT is in abeyance. Any future water framework should account for climate change, hydropower needs and changing river conditions'],
            ['Connectivity', 'Reduce dependence on Pakistan-controlled transit routes; expand connectivity with Afghanistan and Central Asia'],
        ]),
        callout('key', 'Conclusion', 'Relations remain constrained by terrorism, territorial disputes, water tensions and nuclear risks. The immediate priority is **credible deterrence with escalation control**, with humanitarian channels kept open. **Durable normalisation requires a terror-free environment, strategic restraint and sustained bilateral engagement.**'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 7 Afghanistan
    secs.append(Sec('India-Afghanistan', [
        p('Relations have shifted from a **development partnership with the Islamic Republic** to **pragmatic engagement with the Taliban authorities**. India’s approach is shaped by humanitarian interests, counter-terrorism, regional connectivity and people-to-people goodwill. Afghanistan also matters for access to **Central Asia**, the **Pakistan factor** and the regional balance involving **China, Iran and Russia**. India has expanded working engagement with Kabul but has **not formally recognised** the Taliban government.'),
        tbl('Nature of the relationship (slide 13, handout p. 7)', ['Nature', 'Meaning'], [
            ['People-centred goodwill', 'Education, healthcare, culture and development projects; friendly relations with the Afghan people'],
            ['Engagement without endorsement', 'Contact without formal recognition, so India keeps contact without accepting policies that conflict with its security and humanitarian concerns'],
            ['Counter-terror priority', 'Afghan soil should not be used against India'],
            ['Connectivity interest', 'Chabahar and access to Central Asia'],
            ['Regional balance', 'The China, Pakistan, Iran and Russia factor'],
        ]),
        tbl('Evolution (slide 14, handout p. 7)', ['Phase', 'Keyword', 'Key developments'], [
            ['Ancient-1950', 'Civilisational and diplomatic foundation', '**Gandhara, Buddhism** and trade links; the **1950 Treaty of Friendship** set up the modern relationship'],
            ['1979-2001', 'Conflict and Taliban phase', 'India kept ties with Kabul in the Soviet period, **did not recognise the first Taliban regime** and supported the **Northern Alliance**'],
            ['2001-14', 'Development partnership', 'Major partner in infrastructure, health, education, capacity-building; the **2011 Strategic Partnership Agreement** widened cooperation'],
            ['2015-16', 'Flagship projects', 'The **Afghan Parliament Building** and the **Afghan-India Friendship Dam** (the slide calls it **Salma Dam**); slide adds the **Zaranj-Delaram Road**'],
            ['2021', 'Taliban takeover', 'India evacuated citizens through **Operation Devi Shakti** and reduced its diplomatic presence'],
            ['2022-25', 'Pragmatic re-engagement', 'India reopened a **Technical Mission in Kabul**; humanitarian and working-level engagement expanded'],
            ['Current phase', 'Engagement without recognition', 'Practical engagement, formal recognition kept separate; focus on counter-terrorism, humanitarian support and connectivity'],
        ]),
        tbl('Areas of convergence (slide 15, handout pp. 7-8)', ['Area', 'Key points'], [
            ['Development and humanitarian', '**High Impact Community Development Projects** in agriculture, education, health, rural development. Major projects: Parliament Building, Friendship Dam, Zaranj-Delaram Road. Food, medicines, healthcare and disaster relief continue; Afghan patients use Indian healthcare. A **people-centric rather than regime-centric** approach'],
            ['Trade and connectivity', 'Merchandise trade about **US$907.85 million (FY 2025-26)**: India exports **US$253.63 million**, imports **US$654.22 million**. The **2026 Joint Working Group** discussed customs, trader visas, pharmaceuticals, agriculture, banking and cargo. **Chabahar** gives Afghanistan sea access and India a route that **bypasses Pakistan** (used for wheat shipments). The **2024 long-term arrangement for the Shahid Beheshti Terminal** strengthens access to Afghanistan, Central Asia and Eurasia'],
            ['Security and stability', 'A stable Afghanistan **free from terrorism, war and drugs** (also stressed by the **2025 India-Central Asia Dialogue**). **UNSC Resolution 2593**: Afghan territory must not be used to threaten or attack other countries'],
            ['People-to-people', 'Shared language, cuisine, music and cinema (the **Kabuliwala** story). Scholarships and training. **Cricket** as a soft-power link: Afghanistan uses Indian venues for home matches'],
        ]),
        tbl('Areas of divergence (slide 15, handout pp. 8-9)', ['Area', 'Key points'], [
            ['Recognition, governance, rights', 'India engages the **de facto** authorities without recognition. Taliban restrictions on **women’s education, employment and public participation**; security and rights of **Afghan Sikhs, Hindus** and other minorities'],
            ['Terrorism, extremism, narcotics', 'Afghan territory must not be used against India. **ISIL-K** is an active regional threat; UN monitoring flags **Al-Qaeda**; concern about **LeT and JeM** links. Afghanistan’s role in the **Death Crescent** and the opiate trade'],
            ['Pakistan and connectivity', 'No direct land route because of unreliable Pakistani transit, so **Chabahar** matters. Afghanistan-Pakistan tensions and border closures disrupt trade. **US sanctions on Iran and conflicts in West Asia** complicate Chabahar. Landlocked position plus banking, insurance and onward-transport limits'],
            ['Economic fragility', 'Weak investment, unreliable electricity, limited finance, high informality; hard to maintain and expand Indian-supported projects'],
            ['Regional uncertainty', 'Instability limits Afghanistan as a bridge between South and Central Asia. **China** has expanded diplomacy, infrastructure, mining and security contacts (the **Mes Aynak copper mine**). India wants to prevent an **exclusive China-Pakistan strategic space**'],
        ]),
        fig('img/ir-nb-afghan-routes.jpg', 'Afghanistan connectivity routes: Chabahar Port, the Zaranj-Delaram highway, the Ring Road (Herat, Kandahar, Ghazni, Kabul, Mazar-e-Sharif) and Salma Dam (handout p. 8, slide 16).', 'Handout map'),
        tbl('Way forward (slide 17, handout p. 9)', ['Area', 'Way forward'], [
            ['Diplomatic engagement', 'Continue **functional engagement** with the de facto authorities, keeping recognition separate from day-to-day contact; no unconditional political legitimacy. Coordinate with **Iran, Russia, Central Asian and Gulf states and the UN**'],
            ['Counter-terrorism', 'A firm red line; credible assurances against **LeT, JeM, Al-Qaeda and ISIL-K**; coordination through the UN, SCO and the India-Central Asia Dialogue'],
            ['Humanitarian and human capital', 'Food, medicines, healthcare, disaster assistance, reaching **women and vulnerable groups**; scholarships, training and digital education'],
            ['Connectivity and economy', 'Strengthen the **Chabahar-Zaranj-Delaram** route; customs, cargo and payment mechanisms; link to Central Asian and Eurasian routes. **Prioritise small, locally maintainable projects** over large ones vulnerable to instability. Trade in pharmaceuticals, agriculture and food; trader visas and banking'],
        ]),
        callout('key', 'Conclusion', 'From a strategic development partnership to pragmatic engagement. India’s approach should rest on **engagement without recognition, people-level goodwill, counter-terrorism and connectivity**.'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 8 Bangladesh
    secs.append(Sec('India-Bangladesh', [
        p('Once described by PM Modi as a “**Sonali Adhyay**”, India-Bangladesh ties are now in a **strategic reset**: Bangladesh’s political transition, Teesta and Ganga Treaty issues, migration concerns and China’s growing role. Sharing India’s **longest land border (4,096 km)**, Bangladesh is a vital link to the Northeast, an anchor of Bay of Bengal security and an important test for Neighbourhood First.'),
        tbl('Nature of the relationship (slide 18, handout p. 10)', ['Nature', 'Meaning'], [
            ['Geographical interdependence', 'Permanent; India’s longest land border'],
            ['Northeast connectivity', 'Bangladesh is vital for integrating India’s Northeast'],
            ['Bay of Bengal security', 'Maritime and regional cooperation'],
            ['Sovereignty sensitivity', 'Bangladesh values cooperation but is sensitive about sovereignty and **unequal dependence**'],
            ['Institutional need', 'Stable mechanisms beyond changing political equations'],
        ]),
        tbl('Evolution (slide 19, handout p. 10)', ['Phase', 'Keyword', 'Key developments'], [
            ['Pre-1971 to 1972', 'Historical ties and liberation', 'Shared language and culture. India’s support in the **1971 Liberation War** and the **1972 Friendship Treaty**'],
            ['1975-2008', 'Distrust and selective cooperation', 'Political changes created mistrust (slide: anti-India politics and military rule, 1975-90); the **1996 Ganga Water Treaty** was a cooperative milestone'],
            ['2009-14', 'Strategic convergence', '**Sheikh Hasina’s** return brought stronger security cooperation, especially against **Northeast insurgent groups**'],
            ['2014-15', 'Boundary settlement', 'The **2014 maritime boundary settlement** (slide: maritime arbitration) and the **2015 Land Boundary Agreement**'],
            ['2021-23', 'Connectivity and integration', '**Kushiyara MoU**, CEPA discussions, **Akhaura-Agartala rail link**, **Friendship Pipeline**'],
            ['2024', 'Political transition', 'Sheikh Hasina’s exit disrupted established channels'],
            ['2025-26', 'Strategic reset', 'China outreach, Teesta, Ganga Treaty renewal, trade and political issues'],
        ]),
        tbl('Areas of convergence (slide 20, handout pp. 10-11)', ['Area', 'Key points'], [
            ['Economic partnership', 'Bangladesh is India’s **biggest trade partner in South Asia**; India is Bangladesh’s **second biggest trade partner in Asia**. Total trade **US$14.01 billion (FY 2023-24)**; Bangladesh exported **US$1.97 billion** to India'],
            ['Connectivity and energy', '**Akhaura-Agartala rail** links Bangladesh with **Tripura**. **Chattogram and Mongla port** arrangements give transit to the Northeast. **40 MW of Nepalese hydropower** began reaching Bangladesh through India in **November 2024**. The **Friendship Pipeline** can carry **1 million metric tonnes of diesel a year**. **2024 Digital Partnership Shared Vision**'],
            ['Water and disaster', '**1996 Ganga Waters Treaty**: dry-season sharing. **Kushiyara (2022)**: each side may withdraw **153 cusecs** in the dry season. **Joint Rivers Commission**: the **54 shared rivers**. Bangladesh agreed in 2024 to co-lead the **disaster-risk pillar of the Indo-Pacific Oceans Initiative**'],
            ['Defence, border, maritime', '**SAMPRITI** exercises and coordinated naval patrols. **Coordinated Border Management Plan**. The **2015 Land Boundary Agreement** exchanged **111 Indian and 51 Bangladeshi enclaves**'],
            ['People and regional', '**Indira Gandhi Cultural Centre, Dhaka**. **BIMSTEC and BBIN**. Foreign ministers met in **April 2026**'],
        ]),
        tbl('Areas of divergence (slide 20, handout pp. 11-12)', ['Area', 'Key points'], [
            ['Political and humanitarian', 'Sheikh Hasina’s departure in **August 2024**. Bangladesh **renewed its extradition request in August 2026**; India is examining it under its legal procedures. Reported attacks on **Hindus and other minorities**. **Rohingya** refugee movements from Bangladesh'],
            ['Water', '**Teesta** is unresolved despite a draft understanding dating to **2011**. The **1996 Ganga Treaty expires in December 2026**. Arrangements exist for Kushiyara and Feni, but not for most shared rivers'],
            ['Border and security', 'A **4,096.7 km** border with **864.482 km unfenced (February 2025)**; objections from **Border Guard Bangladesh** delay fencing. Drug and gold smuggling, human trafficking. **Border deaths** in incidents involving the BSF are a recurring concern'],
            ['Trade and transit', 'India’s **2025 restrictions** on selected Bangladeshi imports (ready-made garments, some food and plastic products). **Land-port restrictions** at several Northeastern land customs stations. India withdrew the **third-country trans-shipment facility (April 2025)**'],
            ['Strategic', 'China’s infrastructure and defence cooperation, including its role in Bangladesh’s **submarine facilities**'],
        ]),
        tbl('Way forward (slide 21, handout p. 12)', ['Area', 'Way forward'], [
            ['Political engagement', 'Keep foreign-minister and official dialogue going despite differences over transition, extradition and minority safety; people-to-people ties'],
            ['Water', 'A **time-bound Teesta dialogue** involving India, Bangladesh **and West Bengal**, on shared flow data, ecological needs and dry-season requirements. Negotiate the **post-2026** Ganga arrangement with measured flows and transparent review'],
            ['Border', 'Joint mechanisms on border deaths, trafficking and smuggling; fencing and patrolling through agreed protocols'],
            ['Trade and connectivity', 'Take forward **CEPA**; reduce non-tariff barriers; **advance notice and clear criteria** for trade and port restrictions; keep rail, passenger and Northeast transit links running, insulated from unrelated disputes'],
            ['Digital and energy', 'Turn the 2024 Digital Partnership into digital payments, cybersecurity and data protection. Expand **Nepal-Bangladesh electricity trade through India**: **BBIN energy integration**'],
        ]),
        callout('key', 'Conclusion', 'Political transitions may change the trajectory, but **shared geography, rivers, security and economic interdependence remain permanent**. A pragmatic Neighbourhood First approach based on mutual respect and shared prosperity can turn present tensions into a more resilient partnership.'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 9 Nepal
    secs.append(Sec('India-Nepal', [
        p('A **civilisational partnership** rooted in cultural, religious and historical ties, especially Hinduism and Buddhism, strengthened by the **open border**, economic mobility and **Roti-Beti** relations. It is becoming a more development-oriented partnership around the **HIT formula (Highways, I-ways, Trans-ways)**, cross-border power trade and regional integration.'),
        tbl('Nature of the relationship (slide 22, handout p. 13)', ['Nature', 'Meaning'], [
            ['Civilisational closeness', 'Hindu-Buddhist links, pilgrimage and family ties'],
            ['Open border', 'Labour, trade, mobility and daily interaction'],
            ['High expectations', 'Closeness also creates misunderstandings and political mistrust'],
            ['Strategic balancing', 'Nepal seeks foreign-policy **diversification**; India seeks a stable, friendly Nepal and watches external strategic influence'],
            ['Development focus', 'HIT formula, power trade and regional integration'],
        ]),
        tbl('Evolution (slide 23, handout p. 13)', ['Phase', 'Keyword', 'Key developments'], [
            ['Ancient-1950', 'Civilisational and institutional ties', 'Slide: **Lumbini, Pashupatinath, Janakpur, Kashi, Ayodhya**; the **Treaty of Sugauli (1816)** as the boundary framework. The **1950 Treaty of Peace and Friendship** institutionalised the open-border relationship'],
            ['1989-2008', 'Trust deficit and strategic change', 'The **1989 trade-transit crisis** left lasting mistrust. The **1996 Mahakali Treaty** expanded water cooperation. Nepal’s transition to a **republic** increased strategic balancing'],
            ['2015', 'Madhesi crisis and trust deficit', '**Operation Maitri** (earthquake) showed humanitarian cooperation, but border disruptions during the **Madhesi protests** created a strong **anti-blockade perception**'],
            ['2020', 'Boundary tensions', 'Nepal’s **new map** covering **Kalapani, Lipulekh and Limpiyadhura**'],
            ['2024-25', 'Energy integration', 'The **10,000 MW power-export framework**; Nepal-Bangladesh electricity trade through India'],
            ['2025-26', 'Political transition', '**Youth-led** political change: focus on governance, jobs and delivery'],
        ]),
        tbl('Areas of convergence (slide 24, handout pp. 13-14)', ['Area', 'Key points'], [
            ['Trade and investment', 'India is Nepal’s **largest trading partner**: goods trade **US$9.39 billion (2025-26)**. India took **over 82%** of Nepal’s goods exports; Nepal has **unilateral duty-free access**. India holds about **one-third of Nepal’s FDI stock** (around 150 ventures). **UPI-NPI linkage** for digital remittances'],
            ['Connectivity', '**Jaynagar-Bijalpura rail**; Integrated Check Posts at **Birgunj, Biratnagar and Nepalgunj**; the **Motihari-Amlekhgunj** petroleum pipeline'],
            ['Energy', 'The **2024 power-trade agreement**: Nepal to export up to **10,000 MW** to India. **SJVN** is developing **900 MW Arun-III** and **669 MW Lower Arun**'],
            ['Water', '**Koshi (1954), Gandak (1959), Mahakali (1996)** agreements: irrigation, flood control, hydropower (the **Pancheshwar Multipurpose Project**). India-supported river works on the **Kamala, Bagmati and Lalbakeya**'],
            ['Defence and security', '**Surya Kiran** exercises; **Gorkha regiments**; exchange of **Honorary General** ranks. **Agreement on Mutual Legal Assistance in Criminal Matters (February 2026)**. **ITEC** training; the **National Police Academy, Panauti**'],
            ['People and culture', 'Open border; **Janakpur-Ayodhya** and **Lumbini-Bodh Gaya** links. **BHASHINI** and Kathmandu University’s Centre for DPI and AI signed an MoU on language technology'],
            ['Humanitarian and regional', '**Operation Maitri (2015)** and a **US$1 billion** reconstruction commitment. In the recent **GLOF**, India sent **over 130 tonnes** of relief (as of September 2026). **BBIN, BIMSTEC**; the **Joint Commission** reviews relations'],
        ]),
        tbl('Areas of divergence (slide 24, handout p. 14)', ['Area', 'Key points'], [
            ['Boundary', 'Competing claims over **Kalapani, Lipulekh and Limpiyadhura**; Nepal’s 2020 map includes them, India contests it. **Three-party sensitivity: India-China activity at Lipulekh** affects Nepal’s claim. Encroachments, boundary pillars, misuse of the open border'],
            ['1950 Treaty', 'Calls in Nepal to revise it over “unequal provisions”. The **Eminent Persons Group’s** recommendations (2018) remain unimplemented'],
            ['Gorkha recruitment', 'Nepal opposed the **Agnipath Scheme**, saying it violated the **1947 Tripartite Agreement**'],
            ['BRI', 'Nepal and China signed a **Framework for Belt and Road Cooperation (December 2024)**'],
            ['Projects and transit', '**Pancheshwar** (agreed under the 1996 Mahakali Treaty) still lacks a mutually finalised **Detailed Project Report**. Nepal’s dependence on routes through India makes disruptions politically sensitive'],
        ]),
        tbl('Way forward (slide 25, handout p. 15)', ['Area', 'Way forward'], [
            ['Treaty reform', 'Jointly review the 1950 Treaty through **negotiated reciprocity**; use the 2018 EPG recommendations as an input'],
            ['Boundary talks', 'Resume **evidence-based** talks on Kalapani-Lipulekh with historical maps and survey records. The **India-Bangladesh border settlement** is a possible model'],
            ['Energy and connectivity', 'Nepal-Bangladesh power trade through the Indian grid; common scheduling, transmission and settlement rules; clear timelines for roads, railways, ICPs and pipelines'],
            ['Defence and border', 'A mutually acceptable framework for **Gorkha recruitment** (Agnipath and post-service employment). A **smart open border**: keep legitimate movement, target trafficking and crime'],
            ['Disaster management', 'Real-time sharing of **glacial-lake, rainfall and river-level** data'],
            ['People-to-people', 'Cultural, tourism and youth exchanges; **Track-II diplomacy**'],
            ['Balanced engagement', 'Respect Nepal’s ability to balance India and China, while keeping it out of regional rivalries; use BBIN, BIMSTEC and SAARC'],
        ], desc='**Track-II diplomacy** (handout definition): informal, non-governmental dialogue among academics, religious leaders, retired officials and civil society to build understanding, relationships and trust.'),
        callout('key', 'Conclusion', 'India-Nepal ties span border, family, pilgrimage, labour and security. **Dialogue, safer open borders and hydropower trade** can deepen trust and strengthen South Asian integration.'),
    ], label='Class + handout'))

    return build_rest(secs)
