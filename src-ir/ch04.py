# -*- coding: utf-8 -*-
from lib import *

CH = {'n': 4, 'title': 'Indian Diaspora',
      'sub': 'Size, segments and motives; why the diaspora matters and where it stops mattering; challenges, gaps and how to strengthen policy',
      'badge': 'High · Mains', 'slides': True}

SRC = ('Class slides PPT-6 “Indian Diaspora” (13 slides) and the Indian Diaspora chapter of the merged handout, pages 72-77 '
       '(uploaded as “International Relations - Merged File”)')

PYQ = [
    ('Mains 2026 · 15 marks · 250 words', '“India’s global diaspora acts as a living bridge, as a critical economic factor and knowledge network in transforming cultural heritage into geopolitical influence and strategic leverage worldwide.” Critically examine this statement.', '“Critically”: give the bridge, then its limits (section 4). See the skeleton in Practice.', 'Sections 3 and 4', 'handout p. 77'),
    ('Mains 2023 · 10 marks · 150 words', '“Indian diaspora has scaled new heights in the West. Describe its economic and political benefits for India.”', 'Benefits for India, not for the host country. See the skeleton in Practice.', 'Section 3', 'handout p. 77'),
    ('Mains 2020 · 10 marks · 150 words (handout prints 15 and 250)', '“‘Indian diaspora has a decisive role to play in the politics and economy of America and European Countries’. Comment with examples.”', 'Test “decisive”. See the skeleton in Practice.', 'Sections 3 and 4', 'handout p. 77'),
    ('Mains 2017 · 15 marks · 250 words', '“Indian Diaspora has an important role to play in South-East Asian countries’ economy and society. Appraise the role of Indian Diaspora in South-East Asia in this context.”', '**Thin notes:** the chapter has no South-East Asia section. See the skeleton in Practice.', 'Sections 1-3 (general)', 'handout p. 77'),
]


def build():
    secs = []
    exam = []
    exam.append(callout('source', 'Source note',
        '**This chapter has class slides and a handout.** ' + SRC + '. The slides are typed with **no handwriting or board ink**; slides 1 and 13 carry no text. The slides summarise the handout in tables; the handout adds the figures, the Standing Committee’s findings and the evacuation operations (handout only). The material quotes **no Prelims PYQs**; its PYQ box lists four Mains questions.'))
    exam.append(tbl('What the slides stress', ['Signal in the material', 'Where', 'Why it matters'], [
        ['“**India has the world’s largest diaspora.**” About **37 million** overseas Indians', 'Slide 2', 'The opening line of any diaspora answer.'],
        ['“**Different groups require different forms of engagement.**”', 'Slide 4', 'The reason for a differentiated policy (section 7).'],
        ['Seven limitations in leveraging the diaspora', 'Slide 8', 'The “critically” half of the 2026 question.'],
        ['PM’s word for the diaspora: “**Rashtradoot**”; the **4 Cs** (Care, Connect, Celebrate, Contribute)', 'Slide 12', 'A ready conclusion.'],
        ['“India’s diaspora policy should move from simple engagement towards **protection, partnership and productive global networks**.”', 'Slide 12', 'The closing line.'],
    ]))
    exam.append(tbl('PYQs quoted in the material (Mains only)', ['Year, marks, words', 'What was asked', 'Answer or trap', 'Where in this chapter', 'Source'],
        [[a, b, c, d, e] for (a, b, c, d, e) in PYQ],
        desc='Mains years quoted: 2026, 2023, 2020, 2017. Prelims years quoted: none quoted in the material. The four years are exactly three apart.'))
    exam.append(alert('Handout alert: the 2020 marks', 'The handout prints the 2020 question as “15 Marks, 250 Words”. The published 2020 papers place it at **Q10, 10 marks, 150 words** (checked across several compilations for the PYQ Lab). Rule: plan a 150-word answer.'))
    exam.append(callout('key', 'What to prepare',
        '**Prelims hooks:** NRI, PIO, OCI; about 37 million overseas Indians (2026); top five destinations (US 6.07 mn, UAE 4.34 mn, Canada 3.24 mn, Saudi Arabia 2.75 mn, UK 1.28 mn); remittances US$135.4 bn (FY25), about 3.8% of GDP; Resurgent India Bonds (1998, about US$4.2 bn); Emigration Act 1983 and the Protector General of Emigrants; the Overseas Mobility (Facilitation and Welfare) Bill, 2024; Operations Raahat (2015, Yemen), Ganga (2022, Ukraine), Kaveri (2023, Sudan), Ajay (2023, Israel-Gaza), Sindhu (2025, Iran); VAIBHAV, VAJRA, GIAN.\n\n'
        '**Mains hooks:** the diaspora as a bridge (remittances, investment, lobbying, soft power, knowledge) and its limits (consumption remittances, host-country loyalties, culture without votes, security risks); one diaspora or four segments; brain drain versus brain circulation; evacuation diplomacy; the Standing Committee’s 2025 gaps.\n\n'
        '**Closing idea:** move from engagement to **protection, partnership and productive global networks**, under the 4 Cs.'))
    secs.append(Sec('Exam lens: priority and PYQs', exam, sid='exam-lens-priority-and-pyqs'))

    secs.append(Sec('Who the diaspora is', [
        p('The **Indian diaspora** is people whose origins can be traced to India, or Indian citizens settled abroad. It includes **Overseas Citizens of India (OCIs)**, **Persons of Indian Origin (PIOs)** and **Non-Resident Indians (NRIs)**. India has the **world’s largest diaspora**; it links India with the global community, economically and strategically.'),
        callout('key', 'Key concept: diaspora diplomacy (handout)', 'Building strong ties with citizens and communities living abroad and using their **networks, knowledge and influence** to support national interests.'),
        tbl('Major destinations (slide 2; handout: January 2026)', ['Country', 'Approximate diaspora'], [
            ['United States', '6.07 million'], ['UAE', '4.34 million'], ['Canada', '3.24 million'], ['Saudi Arabia', '2.75 million'], ['United Kingdom', '1.28 million'],
        ], desc='**About 37 million overseas Indians** as of 2026 (MEA). The community includes workers, students, professionals, entrepreneurs and historic groups: large, but not uniform.'),
        mnemo('Memory aid: the top five in order', 'UUCSU', 'US, UAE, Canada, Saudi Arabia, UK. Two “U”s first, a “U” last.'),
    ], label='Class + handout'))

    secs.append(Sec('Why Indians migrate, and four kinds of diaspora', [
        tbl('Why Indians migrate (slide 3, handout pp. 72-73)', ['Reason', 'Explanation and example'], [
            ['Economic opportunities', 'The strongest pull. West Asia draws workers in construction, healthcare and services; the **UAE alone hosts over 4.3 million** overseas Indians'],
            ['Higher education', 'About **12.5 lakh Indian students abroad (January 2025)**: over **4.27 lakh in Canada**, about **1.96 lakh in Australia**; also the US and UK'],
            ['Quality of life', 'Public services, healthcare, education, social security and predictable institutions, especially for skilled long-term settlers'],
            ['Family and diaspora networks', 'Information, housing, job contacts and support; family reunification sustains migration to the US, Canada, UK and Australia'],
            ['Global exposure and mobility', 'International careers and innovation ecosystems: not only higher wages'],
            ['Foreign labour demand', 'Ageing societies such as **Germany and Japan** need workers'],
        ]),
        tbl('Diversity within the diaspora (slide 4, handout p. 73)', ['Segment', 'Major locations', 'Key interests'], [
            ['Migrant workers', 'UAE, Saudi Arabia, Qatar, Kuwait, Oman; Southeast Asia', 'Job security, fair wages, labour rights, social security, legal protection, safe work'],
            ['Professionals and entrepreneurs', 'US, UK, Europe, Canada, Australia', 'Careers, investment, business facilitation, taxation, innovation, mobility'],
            ['Students and researchers', 'US, UK, Canada, Australia, Europe', 'Quality education, scholarships, research, internships, careers'],
            ['Historic diaspora', 'Mauritius, Fiji, Guyana, Suriname, South Africa, Caribbean', 'Cultural preservation, heritage, identity, educational links'],
        ]),
        teacher('Class slide stress (slide 4)', '**Different groups require different forms of engagement.** The handout: a Gulf worker, a Silicon Valley entrepreneur and a fourth-generation PIO in Mauritius have different interests and concerns.'),
    ], label='Class + handout'))

    secs.append(Sec('Why the diaspora matters for India', [
        tbl('Six dimensions (slides 5-6, handout pp. 73-74)', ['Dimension', 'Importance and examples'], [
            ['Remittances', 'India received **US$135.4 billion (FY25)**, the **world’s highest**, about **3.8% of GDP**. Shares (2023-24): **US 27.7%, UAE 19.2%, UK 10.8%**. They support households, especially in **Kerala and Punjab**'],
            ['Crisis finance', 'Diaspora savings through **India Development Bonds, Resurgent India Bonds, India Millennium Deposits**. **Resurgent India Bonds raised about US$4.2 billion in 1998**, when India faced sanctions'],
            ['Investment and business networks', 'Venture capital, mentorship, market knowledge, contacts, distributors and customers. **Silicon Valley-India** networks support SaaS, fintech and deep-tech'],
            ['Political influence and connectivity', 'Diaspora groups explain Indian concerns to host governments; Indian-origin legislators raise India’s visibility. The **Indian-American community supported the India-US Civil Nuclear Agreement (2008)**; events such as **Howdy Modi**. It keeps India informed about global trends, which aids foreign-policy making'],
            ['Culture and soft power', 'Diwali, Holi, yoga, cuisine, cinema, Ayurveda, Indian languages. **Girmitiya** communities link India with Mauritius, Fiji, Guyana, Suriname, Trinidad and Tobago, South Africa and the Caribbean'],
            ['Knowledge, skills, technology', 'Indian-origin professionals in technology, medicine, engineering, academia, research and entrepreneurship'],
        ]),
        tbl('Indian-origin leaders (slide 7, handout p. 74)', ['Name', 'Country', 'Position'], [
            ['Rishi Sunak', 'UK', 'Former Prime Minister (2022-24)'],
            ['Kamala Harris', 'US', 'Former Vice-President (2021-25)'],
            ['Sundar Pichai', 'US', 'CEO, Alphabet and Google'],
            ['Satya Nadella', 'US', 'Chairman and CEO, Microsoft'],
            ['Ajay Banga', 'US', 'President, World Bank Group (formerly President and CEO, Mastercard)'],
            ['Sunita Williams', 'US', 'NASA astronaut; retired Captain, US Navy'],
        ]),
        two([('Brain drain (handout)', ['Skilled and educated people migrate to places with better opportunities, reducing human capital at the origin.']),
             ('Brain circulation (handout)', ['Skilled migrants return with technology, capital, managerial skills and institutional knowledge.'])]),
    ], label='Class + handout'))

    secs.append(Sec('Where the diaspora stops helping', [
        tbl('Seven limitations in leveraging the diaspora (slide 8, handout p. 74)', ['Limitation', 'Concern'], [
            ['Remittance use', 'Mostly consumption, housing, health and education; they do not automatically become productive investment'],
            ['Institutional trust', 'Bonds and investment depend on trust in Indian institutions, stability, regulation and research capacity'],
            ['Unequal network access', 'Networks may stay informal; smaller Indian firms find them hard to use'],
            ['Political limits', 'Indian-origin legislators **primarily serve host-country constituencies**; their positions cannot be assumed to favour India'],
            ['Soft-power limits', 'Cultural popularity does not automatically translate into diplomatic support'],
            ['Welfare as a bilateral issue', 'Workers’ and students’ welfare becomes a bilateral issue during visa changes, discrimination, conflicts or restrictions'],
            ['Security risks', 'Most mobilisation is peaceful, but small sections may finance **separatism**, spread violent propaganda, intimidate diplomats or attack missions'],
        ]),
        callout('example', 'Use in the 2026 question', 'The question asks you to “critically examine” the diaspora as a living bridge. Section 3 is the bridge; this table is the “critically”. A balanced answer gives three of each.'),
    ], label='Class + handout'))

    secs.append(Sec('Challenges the diaspora faces, and evacuation diplomacy', [
        tbl('Challenges (slide 9, handout pp. 74-75)', ['Challenge', 'Key concern'], [
            ['Outdated migration framework', 'The **Emigration Act, 1983** regulates migration for overseas work (registration of recruiting agents; the **Protector General of Emigrants**), but is considered outdated'],
            ['Immigration restrictions', '**H-1B** and other visa rules affect IT professionals, students and workers; they can affect bilateral perceptions'],
            ['Consular problems', 'Complex visa rules, consular access and grievance delays, especially in emergencies'],
            ['Worker protection', 'Limited access to pensions, social security and labour protection in some **GCC** states'],
            ['Conflict risks', 'West Asian instability; welfare and evacuation depend partly on host-country cooperation'],
            ['Discrimination', 'Racist attacks; **over 400 Indian student deaths between 2018 and 2024**; anti-immigrant sentiment'],
            ['Identity', 'Balancing ties with India and the host country, especially in diplomatic tension; second-generation identity'],
        ]),
        callout('key', 'Key concept: mobility agreements (handout)', 'Bilateral or multilateral arrangements that facilitate the legal movement of people for employment, education, training, research or professional activity.'),
        tbl('Evacuation diplomacy (handout p. 75; not on the slides)', ['Operation', 'Crisis', 'Key feature'], [
            ['Raahat, 2015', 'Yemen', 'Naval-air coordination; Indians and foreign nationals evacuated'],
            ['Ganga, 2022', 'Ukraine', 'Transit diplomacy through neighbouring countries'],
            ['Kaveri, 2023', 'Sudan', 'Naval, air and diplomatic assets coordinated'],
            ['Ajay, 2023', 'Israel-Gaza conflict', 'Rapid registration and organised return flights'],
            ['Sindhu, 2025', 'Iran', 'Special evacuation flights and diplomatic coordination'],
        ], desc='The handout calls protecting Indians in wars and crises “an important part of India’s consular and humanitarian diplomacy”.'),
        mnemo('Memory aid: evacuations in date order', 'RGKAS', 'Raahat (Yemen 2015), Ganga (Ukraine 2022), Kaveri (Sudan 2023), Ajay (Israel 2023), Sindhu (Iran 2025): “Really Good Kind And Swift”.'),
    ], label='Class + handout'))

    secs.append(Sec('Gaps in India’s approach', [
        tbl('Gaps (slide 10 lists nine; the handout adds two)', ['Gap', 'Concern'], [
            ['No single diaspora policy', 'Fragmented engagement (**Standing Committee on External Affairs, 2025**); **no authentic data** on the diaspora'],
            ['Recruitment malpractice', '**Over 3,000 unregistered agents** notified (October 2024); penalties are insufficient'],
            ['Contract enforcement', 'Hard to enforce contracts and labour rights abroad'],
            ['Low mission registration', 'Hard to contact and help people in emergencies'],
            ['Limited consular capacity', 'Heavy caseloads in high-migration countries'],
            ['Institutional coordination', 'Weak links among the MEA, state governments and recruiters'],
            ['Student verification', 'Some students choose weak or unverified institutions'],
            ['Host-country dependence (handout)', 'Welfare and evacuation depend on host and transit countries'],
            ['Labour demand versus migration policy (handout)', 'Countries short of labour still tighten immigration'],
            ['Emigration reform delay', 'The **Emigration [Overseas Mobility (Facilitation and Welfare)] Bill, 2024** is still pending'],
        ]),
    ], label='Class + handout'))

    secs.append(Sec('Strengthening diaspora policy', [
        tbl('Way forward (slide 11, handout p. 76)', ['Priority', 'Way forward'], [
            ['Differentiated policy', 'Separate approaches for workers, students, professionals, entrepreneurs and researchers'],
            ['Centralised database', 'A **real-time national migration database** of migrants and returnees (Standing Committee, 2025)'],
            ['Worker protection and crisis response', 'Labour agreements, recruitment regulation, contract enforcement, legal aid; pre-departure training, mission registration, evacuation capacity. **Recruitment agents must register with the Protector General of Emigrants**'],
            ['Consular and digital capacity', 'Diaspora liaison offices in major missions; digital platforms linking MEA, states, recruiters and employers'],
            ['Talent networks', 'Strengthen **VAIBHAV, VAJRA and GIAN**; joint research and visiting faculty; collaborate without requiring permanent return'],
            ['Diaspora capital', 'Cheaper transfers, investment options (mutual funds, stocks), taxation concerns; start-up partnerships'],
            ['Security', 'Intelligence-sharing and legal action against illegal financing and violent networks, **distinguishing unlawful individuals from the wider diaspora**'],
        ]),
        tbl('The 4 Cs (slide 12, handout p. 76)', ['C', 'Focus'], [
            ['Care', 'Protect diaspora welfare'], ['Connect', 'Build institutional and societal links'],
            ['Celebrate', 'Strengthen cultural identity'], ['Contribute', 'Channel skills, capital and knowledge towards India'],
        ]),
        teacher('Class slide stress: “Conclusion” (slide 12)', 'The PM has described the diaspora as “**Rashtradoot**”, India’s global brand ambassador. **India’s diaspora policy should move from simple engagement towards protection, partnership and productive global networks.**'),
    ], label='Class + handout'))
    return secs


MAP = ('Indian diaspora', [
    ('Who', [('Types', 'NRI, PIO, OCI'), ('Size', 'about 37 million'), ('Top five', 'US, UAE, Canada, Saudi, UK')]),
    ('Why migrate', [('Pull', 'jobs, education, life'), ('Networks', 'family, community'), ('Demand', 'ageing Germany, Japan')]),
    ('Four segments', [('Workers', 'Gulf: rights, wages'), ('Professionals', 'West: careers'), ('Students', '12.5 lakh abroad'), ('Historic', 'Girmitiya')]),
    ('Why it matters', [('Money', 'US$135.4 bn; RIB 1998'), ('Influence', '2008 nuclear deal'), ('Soft power', 'yoga, cinema'), ('Knowledge', 'brain circulation')]),
    ('Limits', [('Remittances', 'consumption'), ('Politics', 'host-country loyalty'), ('Culture', 'no automatic votes'), ('Security', 'small separatist sections')]),
    ('Challenges', [('Law', 'Emigration Act 1983'), ('Visas', 'H-1B'), ('Safety', '400+ student deaths'), ('Evacuations', 'Raahat to Sindhu')]),
    ('Fix', [('Policy', 'differentiated; database'), ('Bill', 'Overseas Mobility 2024'), ('4 Cs', 'Care Connect Celebrate Contribute')]),
])

TIMELINE = [
    ('1983', 'Emigration Act: registration of recruiting agents; Protector General of Emigrants', True),
    ('1998', 'Resurgent India Bonds raise about US$4.2 billion amid sanctions', True),
    ('2008', 'Indian-American community supports the India-US Civil Nuclear Agreement', False),
    ('2015', 'Operation Raahat, Yemen', True),
    ('2022', 'Operation Ganga, Ukraine', True),
    ('2022-24', 'Rishi Sunak UK Prime Minister', False),
    ('2023', 'Operation Kaveri (Sudan); Operation Ajay (Israel-Gaza)', True),
    ('2018-24', 'Over 400 Indian student deaths abroad', False),
    ('2024', 'Overseas Mobility (Facilitation and Welfare) Bill, 2024 (still pending); over 3,000 unregistered agents notified (October)', False),
    ('2025', 'Operation Sindhu, Iran; Standing Committee report on the diaspora; 12.5 lakh students abroad (January)', True),
    ('FY25', 'Remittances US$135.4 billion, world’s highest', True),
    ('2026', 'About 37 million overseas Indians (January figures)', False),
]

LINKS = [
    ('Chapter 1: determinants', 'The diaspora is one of the determinants of India’s foreign policy; this chapter is its full treatment.'),
    ('Chapter 2: India-US', 'H-1B and visa frictions, the 2008 nuclear deal lobby and the 2020 and 2023 PYQs sit across both chapters.'),
    ('Chapter 5: West Asia', 'Nearly ten million Indians live in GCC states; Operation Sindhu and labour protection appear there too.'),
    ('Chapter 5: Africa and Latin America', 'Girmitiya communities in Mauritius, South Africa, Guyana, Suriname and Trinidad and Tobago.'),
    ('Chapter 3: Maldives', 'About 60,000 Indians live in the Maldives: diaspora as part of neighbourhood policy.'),
]

RECALL = [
    '**Who:** NRI (citizen abroad), PIO, OCI. About 37 million. Top five: US 6.07, UAE 4.34, Canada 3.24, Saudi 2.75, UK 1.28 (million).',
    '**Why migrate:** jobs, education (12.5 lakh students; Canada 4.27 lakh, Australia 1.96 lakh), quality of life, networks, exposure, labour demand (Germany, Japan).',
    '**Four segments:** workers (Gulf), professionals (West), students, historic (Girmitiya).',
    '**Why it matters:** remittances US$135.4 bn (FY25; 3.8% of GDP; US 27.7%, UAE 19.2%, UK 10.8%); RIB 1998 US$4.2 bn; Silicon Valley; 2008 nuclear deal; soft power; brain circulation.',
    '**Limits:** consumption remittances; trust; unequal network access; host-country loyalty; culture without votes; welfare disputes; security risks.',
    '**Challenges:** Emigration Act 1983; H-1B; consular delays; GCC labour protection; conflict; 400+ student deaths (2018-24); identity.',
    '**Evacuations:** Raahat 2015 Yemen; Ganga 2022 Ukraine; Kaveri 2023 Sudan; Ajay 2023 Israel; Sindhu 2025 Iran.',
    '**Gaps:** no single policy, no data, 3,000+ unregistered agents, weak contracts, low registration, thin consulates, coordination, verification, Bill 2024 pending.',
    '**Fix:** differentiated policy, database, worker protection, liaison offices, VAIBHAV-VAJRA-GIAN, diaspora capital, security; 4 Cs; “Rashtradoot”.',
]

TRAPS = [
    ('NRI is a citizen; OCI is not', 'An NRI is an Indian citizen abroad; an OCI is a foreign citizen of Indian origin. Rule: citizenship decides.'),
    ('Largest diaspora, largest remittances', 'Both are world records for India: about 37 million people; US$135.4 billion (FY25). Rule: do not swap the numbers.'),
    ('US remits most, UAE hosts most workers', 'US 27.7% of remittances (2023-24); the UAE hosts over 4.3 million Indians, mostly workers. Rule: money share versus headcount.'),
    ('Resurgent India Bonds', '1998, about US$4.2 billion, during sanctions. Rule: 1998 = Pokhran year = bonds.'),
    ('Brain drain versus brain circulation', 'Drain loses skills; circulation brings them back with capital and know-how. Rule: circulation is the policy goal.'),
    ('Indian-origin is not pro-India', 'Indian-origin legislators serve host-country voters first (slide 8). Rule: say “can support”, never “will support”.'),
    ('Operation names', 'Raahat (Yemen), Ganga (Ukraine), Kaveri (Sudan), Ajay (Israel), Sindhu (Iran). Do not mix with Devi Shakti (Afghanistan, Chapter 3).'),
    ('Handout marks for 2020', 'Printed as 15 marks; the paper had it at Q10, 10 marks. Rule: 150 words.'),
]

MCQ = [
    ('As of 2026 (MEA), the number of overseas Indians is about:', ['13 million', '25 million', '37 million', '52 million'], 2, 'About 37 million, the world’s largest diaspora.'),
    ('Which country hosts the largest Indian diaspora (January 2026)?', ['UAE', 'United States', 'Canada', 'Saudi Arabia'], 1, 'US 6.07 million, then UAE 4.34, Canada 3.24, Saudi Arabia 2.75, UK 1.28.'),
    ('India’s remittances in FY25 were about:', ['US$83 billion, 2% of GDP', 'US$135.4 billion, about 3.8% of GDP', 'US$200 billion, 6% of GDP', 'US$54 billion, 1.5% of GDP'], 1, 'US$135.4 billion, the world’s highest.'),
    ('Resurgent India Bonds (1998) raised about:', ['US$1 billion', 'US$4.2 billion', 'US$10 billion', 'US$15 billion'], 1, 'About US$4.2 billion when India faced sanctions.'),
    ('Which law regulates migration of Indian workers for overseas employment and set up the Protector General of Emigrants?', ['Passports Act, 1967', 'Emigration Act, 1983', 'Foreigners Act, 1946', 'Citizenship Act, 1955'], 1, 'Emigration Act, 1983. Its replacement, the Overseas Mobility Bill 2024, is pending.'),
    ('Operation Kaveri (2023) evacuated Indians from:', ['Yemen', 'Ukraine', 'Sudan', 'Iran'], 2, 'Sudan. Raahat: Yemen. Ganga: Ukraine. Ajay: Israel-Gaza. Sindhu: Iran.'),
    ('Brain circulation means:', ['Permanent loss of skilled workers', 'Return of skilled migrants with capital, technology and know-how', 'Students switching courses abroad', 'Rotation of diplomats'], 1, 'Handout definition; contrast with brain drain.'),
    ('VAIBHAV, VAJRA and GIAN are:', ['Evacuation operations', 'Talent and knowledge-mobility programmes linking global Indian experts with Indian institutions', 'Remittance bonds', 'Visa categories'], 1, 'The way forward says strengthen them.'),
    ('Which is NOT one of the 4 Cs of diaspora policy?', ['Care', 'Connect', 'Celebrate', 'Control'], 3, 'Care, Connect, Celebrate, Contribute.'),
]

CARDS = [
    ('Define the Indian diaspora.', 'People of Indian origin or Indian citizens settled abroad: NRIs, PIOs, OCIs.'),
    ('Diaspora diplomacy?', 'Building ties with communities abroad and using their networks, knowledge and influence for national interests.'),
    ('Size and top five?', 'About 37 million. US 6.07 mn, UAE 4.34, Canada 3.24, Saudi 2.75, UK 1.28.'),
    ('Six reasons Indians migrate?', 'Jobs, education, quality of life, family networks, global exposure, foreign labour demand.'),
    ('Students abroad (January 2025)?', 'About 12.5 lakh; Canada over 4.27 lakh; Australia about 1.96 lakh.'),
    ('Four diaspora segments?', 'Migrant workers (Gulf), professionals (West), students and researchers, historic diaspora (Girmitiya).'),
    ('Remittance facts?', 'US$135.4 bn (FY25), world’s highest, about 3.8% of GDP; US 27.7%, UAE 19.2%, UK 10.8%.'),
    ('Crisis finance from the diaspora?', 'India Development Bonds, Resurgent India Bonds (1998, US$4.2 bn), India Millennium Deposits.'),
    ('Diaspora and the nuclear deal?', 'The Indian-American community supported the 2008 India-US Civil Nuclear Agreement.'),
    ('Girmitiya countries?', 'Mauritius, Fiji, Guyana, Suriname, Trinidad and Tobago, South Africa, the Caribbean.'),
    ('Six Indian-origin leaders on the slide?', 'Sunak, Harris, Pichai, Nadella, Banga, Sunita Williams.'),
    ('Seven limits of leveraging the diaspora?', 'Consumption remittances, institutional trust, unequal access, host-country loyalty, soft-power limits, welfare disputes, security risks.'),
    ('Challenges the diaspora faces?', 'Outdated 1983 Act, visas (H-1B), consular delays, GCC labour protection, conflict, discrimination (400+ student deaths 2018-24), identity.'),
    ('Five evacuations?', 'Raahat 2015 Yemen; Ganga 2022 Ukraine; Kaveri 2023 Sudan; Ajay 2023 Israel-Gaza; Sindhu 2025 Iran.'),
    ('Gaps found by the Standing Committee (2025)?', 'No single diaspora policy, no authentic data, weak penalties for recruitment malpractice; wants a real-time database and agent registration.'),
    ('Unregistered recruiting agents?', 'Over 3,000 notified as of October 2024.'),
    ('The pending emigration law?', 'Emigration [Overseas Mobility (Facilitation and Welfare)] Bill, 2024.'),
    ('Mobility agreements?', 'Arrangements for legal movement of people for work, study, training, research or professional activity.'),
    ('Talent programmes?', 'VAIBHAV, VAJRA, GIAN.'),
    ('The 4 Cs and the PM’s word?', 'Care, Connect, Celebrate, Contribute. “Rashtradoot”.'),
]

SKELETONS = [
    ('Mains 2026 (15m, 250w): diaspora as a living bridge, critically examined',
     'Intro: about 37 million overseas Indians, the world’s largest diaspora; the PM calls them “Rashtradoot”.',
     ['Economic factor: US$135.4 bn remittances (FY25); Resurgent India Bonds (1998); investment and Silicon Valley networks.',
      'Knowledge network: professionals and leaders (Pichai, Nadella, Banga); brain circulation; VAIBHAV, VAJRA, GIAN.',
      'Cultural heritage into influence: yoga, Diwali, cinema; Girmitiya links; lobbying for the 2008 nuclear deal; Howdy Modi.',
      'Critically: remittances go to consumption; Indian-origin leaders serve host voters; culture does not guarantee votes; small sections finance separatism; welfare crises (visas, 400+ student deaths) become bilateral issues.',
      'Way forward: differentiated policy, database, worker protection, the Overseas Mobility Bill.'],
     'Closing: a living bridge carries traffic both ways; under the 4 Cs it can become strategic leverage, not just goodwill.'),
    ('Mains 2023 (10m, 150w): economic and political benefits of the diaspora in the West',
     'Intro: the US (6.07 mn), Canada (3.24 mn) and UK (1.28 mn) host large, high-skill Indian communities.',
     ['Economic: the US alone sends 27.7% of remittances; investment, venture capital, Silicon Valley-India networks; knowledge and technology.',
      'Political: Indian-origin legislators and leaders (Sunak, Harris); the 2008 nuclear deal; visibility for Indian concerns.',
      'Caveat in one line: they serve host-country voters first.'],
     'Closing: benefits grow when India protects and connects (Care, Connect).'),
    ('Mains 2020 (10m, 150w as printed in the paper): a “decisive” role in American and European politics and economy?',
     'Intro: the diaspora is influential in the West; “decisive” overstates it.',
     ['For: leaders and legislators; the 2008 nuclear deal lobby; tech leadership (Pichai, Nadella); remittance and investment flows.',
      'Against: host-country loyalties; a minority in electorates; culture does not translate into diplomatic votes; visa rules (H-1B) still tighten.'],
     'Closing: important and growing, but not decisive.'),
    ('Mains 2017 (15m, 250w): the diaspora’s role in South-East Asian economies and societies',
     'Intro: **thin notes:** the chapter does not cover South-East Asia specifically. Use the general frame and add class notes.',
     ['Segments present: migrant workers and the historic diaspora (handout: “migrant workers: Southeast Asia”).',
      'Economy: business networks, trade links; society: culture, festivals, shared Buddhist and Ramayana heritage (Chapter 5, ASEAN).',
      'Limits: identity and integration issues; host-country priorities.'],
     'Closing: a cultural and commercial bridge that supports Act East.'),
]
