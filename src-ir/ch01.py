# -*- coding: utf-8 -*-
from lib import *

CH = {'n': 1, 'title': 'Introduction to World Geopolitics and India’s Foreign Policy',
      'sub': 'Six phases of the global order, then India’s foreign policy: determinants, evolution, trade-offs, instruments',
      'badge': 'High · Mains', 'slides': True}

SRC = ('Class slides PPT-1 (24 slides) and PPT-2 (23 slides); handout Chapter 1, pages 1-21 '
       '(uploaded as “GS-2 International Relations - 12”)')

# ------------------------------------------------------------------ PYQs quoted in the material
PYQ = [
    ('Mains 2026 · Q9 · 10 marks · 150 words', 'IPMDA (Indo-Pacific Partnership for Maritime Domain Awareness) “bridges the gap between India’s SAGAR vision and the Quad’s collective Indo-Pacific strategy.” Critically assess, focusing on IPMDA.', 'Open-ended. See the skeleton in Practice.', 'Partial: SAGAR/MAHASAGAR and Quad in section 11 and Chapter 2. IPMDA itself is not in these notes.', 'slides 3'),
    ('Mains 2026 · Q10 · 10 marks · 150 words', 'BRICS “acts as a powerful counterweight in global governance, actively amplifying the voice and influence of the Global South.” Explain the role of BRICS in projecting itself as an alternative to other groupings.', 'Open-ended. See the skeleton in Practice.', 'BRICS in sections 5, 6, 7 and 11', 'slides 3'),
    ('Mains 2026 · Q19 · 15 marks · 250 words', 'India’s global diaspora “acts as a living bridge, as a critical economic factor and knowledge network in transforming cultural heritage into geopolitical influence and strategic leverage.” Critically examine.', 'Open-ended. See the skeleton in Practice.', 'Determinant 9 in section 8; evacuations in sections 8 and 11; US diaspora in Chapter 2', 'slides 3'),
    ('Mains 2026 · Q20 · 15 marks · 250 words', 'China’s BRI “has transformed South Asia from a regional space into a theatre of great power competition.” Analyse the strategic implications for India’s security and regional influence in South Asia.', 'Open-ended. Answered in Chapter 2.', 'Chapter 2 (also BRI 2013 in section 6 here)', 'slides 3'),
    ('Mains 2025 · 10 marks · 150 words', '“With the waning of globalization, post-Cold War world is becoming a site of sovereign nationalism.” Elucidate.', 'Open-ended. See the skeleton in Practice.', 'Sections 6 and 7', 'handout p. 21'),
    ('Mains 2020 · 15 marks · 250 words', '“Quadrilateral Security Dialogue (Quad)” is transforming itself into a trade bloc from a military alliance, in present times: discuss.', 'Open-ended. See the skeleton in Practice.', 'Sections 6, 7, 9 and 11', 'handout p. 21 (also quoted in Chapter 2)'),
    ('Mains 2019 · 15 marks · 250 words', '“The long-sustained image of India as a leader of the oppressed and marginalised nations has disappeared on account of its new found role in the emerging global order.” Elaborate.', 'Open-ended. See the skeleton in Practice.', 'Sections 9 and 10', 'handout p. 21'),
]


def build():
    secs = []

    # ---------------------------------------------------------------- exam lens
    exam = []
    exam.append(callout('source', 'Source note',
        '**This chapter has class slides and a handout.** ' + SRC + '. The slides are typed. **There is no handwriting, underlining or board ink in these decks**, so the “teacher’s stress” in this notebook comes from what the slides themselves put in headings, “Core idea”, “Key lesson”, “Essence” and “Key ideas” lines. Priority below is read from the slides and the handout’s PYQ page. The material quotes **no Prelims PYQs** for IR (this is the GS Mains module). Mains years quoted are listed below; a “years quoted” count is not a count of distinct questions.'))
    exam.append(tbl('What the teacher and handout stress', ['Signal in the material', 'Where', 'Why it matters'], [
        ['IR carries **4 questions and 50 marks every year**: Q9 and Q10 (10 marks, 150 words) and Q19 and Q20 (15 marks, 250 words)', 'Slide 3 (PPT-1)', 'Fixes your time per answer. The slide says the placement has stayed consistent over the years.'],
        ['“Questions are broader now”: themes asked in a **wider context**, not as direct bilateral questions', 'Slides 4 and 5 (PPT-1)', 'Open every answer with the global setting, then narrow to India.'],
        ['**Statement-based questions that must be tested, not endorsed**', 'Slide 4 (PPT-1)', 'Use “agree in part, but…”. Every 2026 question opened with a strong claim.'],
        ['Order of study: **big picture first, major powers before bilaterals**', 'Slide 5 (PPT-1)', 'Chapter 1 is the big picture; Chapter 2 gives the powers; bilaterals follow.'],
        ['Phase 6 “**Essence of the phase**”: Rivalry → Strategic Realignment → Economic and Tech Fragmentation → Multipolarity → Institutional Paralysis', 'Slide 21 (PPT-1)', 'A ready-made one-line introduction for any current-affairs IR answer.'],
        ['“**Where does the global order stand today?**”: six features, with a US-led versus China-backed table', 'Slides 22-23 (PPT-1)', 'The six features are a checklist for the “context” paragraph.'],
        ['India’s “**Central thread: strategic autonomy**” and the “Key ideas” keyword table', 'Slides 21-22 (PPT-2)', 'Strategic autonomy is the answer to “why does India do X?”.'],
        ['“Not a shift from values to interests”: India still follows its values but has more capability', 'Handout p. 17', 'Answers “Has India given up idealism?” type questions.'],
    ]))
    exam.append(tbl('PYQs quoted in the material (Mains only)', ['Year, marks, words', 'What was asked', 'Answer or trap', 'Where in this chapter', 'Source'],
        [[a, b, c, d, e] for (a, b, c, d, e) in PYQ],
        desc='Mains years quoted: 2026 (four questions, quoted on slide 3), 2025, 2020 and 2019. Prelims years quoted: none quoted in the material. Question 20 of 2026 and the Quad question of 2020 are also quoted in Chapter 2.'))
    exam.append(callout('key', 'What to prepare',
        '**Prelims hooks:** the six phases and their years; Westphalia 1648; Wilson’s 14 Points 1918; League 1920; NATO 1949 and Warsaw Pact 1955; NAM 1961 (Belgrade); NPT 1968; Stockholm 1972; Schengen 1985; WTO 1995 and China’s entry 2001; BRICS NDB 2014; BRI 2013; Brexit 2016; Gujral Doctrine; String of Pearls versus Diamond Necklace; Operations Ganga, Kaveri and Sindhu.\n\n'
        '**Mains hooks:** why each phase gave way to the next (cause and effect); what “multipolar churn” means; economic nationalism and weaponised interdependence; the Global South and institutional reform; India’s determinants and the six periods of its policy; five trade-offs and seven structural challenges; India’s “bridge power” role.\n\n'
        '**Closing idea:** India’s central thread is strategic autonomy, now pursued with more economic, military, technological and diplomatic capability.'))
    secs.append(Sec('Exam lens: priority and PYQs', exam, sid='exam-lens-priority-and-pyqs'))

    # ---------------------------------------------------------------- 1 basics
    secs.append(Sec('Basics first: IR, foreign policy and the six-phase story', [
        p('**International Relations (IR)** is the study of how countries interact with one another and with other actors across borders: international organisations, companies, social movements and individuals. Its core question is: **why do countries behave the way they do?** Behaviour is shaped by power, security, economic interests, ideas and institutions. IR is wider than war and diplomacy: it includes trade, technology, energy, climate change, migration and global institutions.'),
        tbl('Key terms', ['Term', 'Meaning', 'Main question'], [
            ['Foreign policy', 'What a country wants from the outside world and how it pursues those goals', 'What does a country want to achieve abroad?'],
            ['Geopolitics', 'How geography, location and resources affect power and strategy', 'Why does location matter?'],
            ['Global order', 'How power, rules and institutions are arranged in the world', 'Who has influence, and how is the system organised?'],
        ]),
        tbl('How the global order evolved: six phases at a glance', ['Phase', 'Period', 'Defining character'], [
            ['Phase 1', 'Until 1914', 'Sovereign states, empires and the balance of power'],
            ['Phase 2', '1919 to 1945', 'Liberal experiment, its failure and a second world war'],
            ['Phase 3', '1945 to 1991', 'Two superpowers, nuclear deterrence and new institutions'],
            ['Phase 4', '1991 to 2008', 'American primacy, globalisation and the Washington Consensus'],
            ['Phase 5', '2008 to 2019', 'Crisis of the liberal order and the rise of new powers'],
            ['Phase 6', '2020 onwards', 'Post-COVID fragmentation, economic nationalism and multipolar churn'],
        ]),
        p('The handout’s warning: the world did not move in a straight line from war to peace. Every phase mixed power politics, cooperation and competing ideas, and each new phase carried features of the older one.'),
        teacher('Class slide stress: the teacher’s approach (slide 5)',
            'Questions are broader now. **Big picture first**: the course opens with how the world order evolved. **Major powers before bilaterals**: what the US, China and Russia want comes before India’s ties with them. **Bilaterals follow**, inside the bigger picture. **Outcome:** any specific theme can be placed in its wider context.'),
        flow('Teacher’s order of study', [
            ('1 · The world order', 'Six phases (this chapter)', ''),
            ('2 · Major powers', 'US, China, Russia: ambitions and instruments (Chapter 2)', ''),
            ('3 · Bilaterals', 'India with China, US, Russia and others (Chapter 2 onwards)', ''),
            ('4 · The outcome', 'Place any theme in its wider context', 'good'),
        ]),
        alert('Handout alert: where Phase 5 ends',
            'The slide table and handout table say Phase 5 is **2008 to 2019**. The Phase 5 slide headings say “**Post-2008 till 2020**”. Phase 6 begins in **2020**. **Rule for the exam hall:** Phase 5 = 2008 to 2019/20; Phase 6 starts in 2020 (post-COVID).'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 2 phase 1
    secs.append(Sec('Phase 1: Dominance of Realism (until World War I)', [
        p('“A country that demands moral perfection in its foreign policy will achieve neither perfection nor security.” (Henry Kissinger, quoted in the handout.)'),
        h3('The sovereign state system'),
        ul(['Before **1648**, Europe was divided by **religious and dynastic conflicts**. People were loyal to rulers and churches, not to nation-states.',
            'The **Thirty Years’ War (1618-1648)** was fought largely along Protestant-Catholic and dynastic lines. It showed how fragmented authority and competing loyalties lead to widespread violence.',
            'The **Peace of Westphalia (1648)** ended the war and laid the foundation of **modern international law and the sovereign state system**. It set the principles of **state sovereignty and non-interference** in internal affairs. Centralised states such as **France and Sweden** grew stronger after it.']),
        tbl('Key concepts', ['Concept', 'Meaning'], [
            ['Sovereignty', 'Supreme authority inside its territory; accepts no outside authority over it'],
            ['International anarchy', 'Not chaos. There is **no world government** above states, so no one but the state itself can guarantee its safety'],
            ['Nation-state', 'A state (fixed territory, population, government) where state and nation (a people who feel they belong together by language, culture or history) broadly match'],
            ['Security dilemma', 'One state arms for defence, others feel threatened and arm too. Both end up **less secure**, though neither wanted war'],
            ['Balance of Power (BoP)', 'States act to prevent any one power becoming dominant'],
        ]),
        h3('Realism and its flow'),
        p('**Realism** sees international politics as a struggle for **security, survival and sovereignty**. With no authority above states, countries rely on **self-help** and build their own power. This creates mistrust: one state’s build-up makes others feel threatened.'),
        flow('The Realism flow (slide 7)', [
            ('International anarchy', 'no central authority', ''),
            ('Self-help', 'every state builds its own power', ''),
            ('Mistrust', '', 'warn'),
            ('Security dilemma', 'defensive arming looks like a threat', 'warn'),
            ('Arms race', '', 'bad'),
            ('Balance of Power', 'the attempt to stop any one state dominating', ''),
        ]),
        h3('The road to World War I'),
        ul(['Many states believed that **attacking first** could give an advantage. Germany’s **Schlieffen Plan** reflected this thinking.',
            'The **Balance of Power could not prevent conflict**. Military build-up and rival alliances increased tensions.',
            'The assassination of **Archduke Franz Ferdinand** triggered World War I, but deeper rivalries had already made war likely.',
            'The peace after the war stayed weak. **Nehru** called it a “**nervous state of peace**”.']),
        callout('key', 'The Realist problem in one line', 'A state may increase its power to become safer, but this can make other states feel threatened. The cycle: fear → self-help → military build-up → arms race → balancing.'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 3 phase 2
    secs.append(Sec('Phase 2: Liberal thought enters, but Realism dominates (inter-war)', [
        p('After World War I, ideas of **collective security, cooperation and economic interdependence** gained ground. Many proposals were not fully realised because of geopolitical resistance and continuing power politics.'),
        h3('Rise of liberal ideas'),
        ul(['**Wilson’s 14 Points (1918)**: self-determination, free trade, international cooperation and an association of nations.',
            '**League of Nations (1920)**: Wilson’s “association of nations”; collective security, “one for all, all for one”; tried to mediate disputes through diplomacy.',
            '**Trade and movement of people** were seen as tools to reduce the risk of war by linking countries more closely.']),
        tbl('Two key concepts', ['Concept', 'Meaning'], [
            ['Liberalism', 'War is not inevitable. Institutions, trade, democracy and international law can build cooperation **without a world government**'],
            ['Collective security', 'All members act together against any aggressor. It works **only when major powers are willing to enforce it**'],
        ]),
        h3('Return of Realism after the Great Depression (1929)'),
        ul(['**Protectionism:** trade barriers rose.', '**Authoritarian regimes** rose in **Germany, Italy and Japan**.',
            '**Expansionism:** aggressive foreign policies. The League **could not stop Japan in Manchuria (1931) or Italy in Abyssinia (1935)**.',
            'These developments led to **World War II**, whose devastation exposed the limits of the inter-war order.']),
        h3('The Nuclear Age'),
        ul(['The atomic bombing of **Hiroshima and Nagasaki (1945)** changed international security.',
            '**Nuclear deterrence** became central. **Mutually Assured Destruction (MAD)** discouraged direct nuclear war because any exchange would destroy both sides.',
            '**Deterrence** prevents an attack by convincing the enemy that the cost will exceed the gain. It depends on **capability, credibility and clear communication**.']),
        flow('Phase 2 cause chain', [
            ('Liberal hope', '14 Points 1918 → League 1920', 'good'),
            ('Great Depression 1929', 'protectionism, authoritarian regimes, expansionism', 'warn'),
            ('League fails', 'Manchuria 1931, Abyssinia 1935', 'bad'),
            ('World War II', 'then the nuclear age: Hiroshima and Nagasaki 1945', 'bad'),
        ]),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 4 phase 3
    secs.append(Sec('Phase 3: Liberalism, Realism and Idealism together (Cold War, 1945-1991)', [
        p('Liberal institutions promoted cooperation and collective security, while US-USSR rivalry drove military blocs, proxy wars and the arms race. A third strand, **Idealism**, appeared as the Non-Aligned Movement.'),
        tbl('Liberalism: cooperation and collective security', ['Institution or agreement', 'Purpose'], [
            ['United Nations (1945)', 'Peace, diplomacy, collective security. Superpower rivalry often limited it'],
            ['IMF and World Bank', 'Economic stability and reconstruction'],
            ['Marshall Plan', 'About **13 billion dollars** for rebuilding Europe; also aimed to **contain communism**'],
            ['NPT (1968)', 'Prevent spread of nuclear weapons; laid the ground for **SALT** (Strategic Arms Limitation Talks)'],
            ['Stockholm Conference (1972)', 'Early global cooperation on environmental protection'],
            ['Schengen Agreement (1985)', 'Free movement and economic integration in Europe'],
        ]),
        p('**Cooperation and great-power interests:** liberal institutions did not work apart from power politics. The Marshall Plan helped rebuild Western Europe and served containment. The USSR created **COMECON** to deepen economic cooperation and keep influence over Eastern Europe.'),
        tbl('Realism: rivalry and arms race', ['Feature', 'Detail'], [
            ['Blocs', '**NATO (1949)** versus **Warsaw Pact (1955)**'],
            ['Proxy wars', '**Korean War** and **Vietnam War**'],
            ['Nuclear arms race', 'Huge arsenals; **Cuban Missile Crisis (1962)** brought the world close to nuclear war'],
            ['Middle East', '**Yom Kippur War (1973)**: US backed Israel; USSR backed Arab states'],
            ['Result', '**Bipolarity**: a world dominated by two powers, with smaller states pressed to align'],
        ]),
        h3('Idealism: NAM and strategic autonomy'),
        ul(['The **Non-Aligned Movement** was formally launched at the **Belgrade Summit (1961)**: peace, sovereignty, anti-colonialism and independent foreign policy. New countries stayed outside the US and USSR blocs.',
            'Under **Nehru**, India promoted **strategic autonomy** and independent judgement. **Strategic autonomy** = the ability to take foreign-policy decisions on one’s own national interest, without being bound to any bloc.',
            'Security needs sometimes pushed NAM countries towards one bloc. India signed the **1971 Treaty of Peace, Friendship and Cooperation with the USSR** during the Bangladesh crisis.',
            'India-US relations were strained when the US sent the **USS Enterprise** into the Bay of Bengal in support of Pakistan.']),
        tbl('Three strands side by side (slides 11-12)', ['Strand', 'Core idea', 'Examples'], [
            ['Liberalism', 'Institutions bring cooperation', 'UN 1945, IMF-World Bank, NPT 1968, Stockholm 1972, Schengen 1985, Marshall Plan, COMECON'],
            ['Realism', 'Rivalry and power balance', 'NATO 1949, Warsaw Pact 1955, Korea, Vietnam, Cuban Missile Crisis 1962'],
            ['Idealism', 'Peace and independence from blocs', 'NAM 1961, Nehru’s strategic autonomy, with India-USSR Treaty 1971 as a security exception'],
        ]),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 5 phase 4
    secs.append(Sec('Phase 4: Victory of Liberalism (the unipolar moment, 1991-2008)', [
        p('The high point of the liberal order: democracy, capitalism, free trade, globalisation and multilateral institutions under strong US leadership. At the same time climate change, terrorism and cybersecurity raised the need for global cooperation, and emerging powers pushed the world towards multipolarity.'),
        h3('Fall of the USSR (1991)'),
        ul(['The collapse of the Soviet Union **ended the Cold War** and left the US as the sole superpower: the **unipolar moment**.',
            'Former Soviet and Eastern European states moved towards democracy and market economies. **Poland and the Baltic states** moved closer to **NATO and the EU**.',
            'Under **Boris Yeltsin**, Russia adopted privatisation and deregulation, though the transition created serious economic problems.']),
        h3('Globalisation and US hegemony'),
        ul(['**WTO (1995)** institutionalised free trade. **China’s WTO accession (2001)** accelerated its integration. India and Brazil also gained from expanding trade.',
            'The US acted through institutions, and **unilaterally** when it thought necessary. **Afghanistan (2001)** and **Iraq (2003)** showed its military reach; the Iraq War also exposed the risks of unchallenged hegemony and **strategic overreach**.',
            'US-led globalisation provided markets, capital and stability that helped emerging economies such as **China and India**.']),
        tbl('Global issues needing cooperation', ['Issue', 'Marker'], [
            ['Climate change', '**Kyoto Protocol (1997)**, later the **Paris Agreement (2015)**'],
            ['Terrorism', '**9/11** strengthened counter-terrorism cooperation'],
            ['Cybersecurity', 'Digital dependence created cross-border vulnerability'],
        ]),
        p('**Rise of multipolarity:** the economic rise of **China, India, Brazil and Russia** shifted power away from a purely US-dominated system. **BRICS** reflected emerging economies’ demand for a greater voice in global governance.'),
        h3('India’s LPG reforms (1991)'),
        ul(['The **1991 balance-of-payments crisis** led to **Liberalisation** (fewer industrial controls and licences), **Privatisation** (bigger role for private sector) and **Globalisation** (more trade, FDI, technology).',
            'India’s nominal GDP rose from about **$270 billion (1991)** to nearly **$1.2 trillion (2008)**.',
            '**Economic interests became more important in India’s foreign policy.**']),
        callout('key', 'Concept: unipolarity and hegemony', '**Unipolarity** is a world with one dominant power. **Hegemony** is leadership strong enough to write the rules for others. It can give stability but can also lead to overreach.'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 6 phase 5 (sid number auto)
    secs.append(Sec('Phase 5: Crisis of Liberalism (post-2008)', [
        p('The **Global Financial Crisis (2008)** weakened Western economies and confidence in the Western-led liberal order. China and India gained weight. The phase saw **multipolarity, protectionism, nationalism and strategic competition**.'),
        tbl('Major trends of the phase', ['Trend', 'What changed'], [
            ['Shift to the Indo-Pacific', 'China and India became major growth centres. **2010: China overtook Japan** as the second-largest economy. The US answered with the **Pivot to Asia** under Obama'],
            ['Reduced US engagement', 'Focus on domestic recovery; fewer commitments in Iraq and Afghanistan. Later **America First** under Trump: national interest, tariffs, burden-sharing'],
            ['Rise of BRICS and G20', 'Emerging economies sought a bigger global role. BRICS created the **New Development Bank (2014)**. G20 became the platform for managing crises'],
            ['India as a balancing power', 'Bigger Indo-Pacific role with **strategic autonomy**, through BRICS, G20 and Quad; keeps seeking reform of global institutions, including a **permanent UNSC seat**'],
            ['Brexit and European challenges', '**Brexit (2016)**: sovereignty, immigration and integration concerns; about **52%** voted to leave the EU'],
            ['Migration, nationalism, populism', 'The **Syrian refugee crisis** deepened divisions in Europe. **Germany took over one million refugees**; countries such as **Hungary** resisted'],
            ['Rise of protectionism', 'Tariffs and other measures; the **US-China trade war** is the main example'],
        ]),
        h3('Rise of China and the start of US-China rivalry'),
        tbl('Four dimensions of China’s rise', ['Dimension', 'Detail'], [
            ['Economic and strategic', 'Manufacturing strength, financial scale, supply-chain centrality. **BRI (2013)** gave access to chokepoints, ports and energy corridors. **Gwadar, Hambantota and CPEC** extended presence in the Indian Ocean and reduced dependence on the **Malacca Strait**'],
            ['Military and maritime', 'Naval expansion; **grey-zone tactics and salami slicing** to advance claims; South China Sea and Taiwan tensions; **A2/AD** in its near seas'],
            ['Technological', 'Self-reliance in 5G, semiconductors, EVs, batteries. **Made in China 2025 (2015)**. **Huawei’s 5G** became a symbol of US-China tech rivalry'],
            ['Institutional', 'Bigger role in **BRICS and SCO**; **AIIB** strengthened its role in development finance'],
        ]),
        flow('US-China rivalry: how it spread (slide 17)', [
            ('Pivot to Asia', 'Indo-Pacific focus', ''),
            ('2018 trade war', 'tariffs', 'warn'),
            ('Technology competition', '5G, semiconductors', 'warn'),
            ('Supply-chain competition', 'diversification', 'warn'),
            ('Indo-Pacific competition', 'strategic rivalry', 'bad'),
        ]),
        teacher('Class slide stress: “Overall” (slide 17)', 'Rivalry **expanded from trade to technology, supply chains, semiconductors and regional security.** Globalisation continued but became **more political, protectionist and security-driven**.'),
        tbl('Key terms', ['Term', 'Meaning and example'], [
            ['Salami slicing', 'Gradual change through small steps that avoid a major response. Example: incremental expansion in the South China Sea'],
            ['A2/AD', 'Anti-Access/Area-Denial: capabilities to keep an opponent’s forces out of a region. Example: China’s missiles and navy around Taiwan and the South China Sea'],
            ['Strategic chokepoints', 'Narrow sea passages carrying huge trade and energy flows. Examples: **Strait of Malacca, Strait of Hormuz**'],
            ['Pivot to Asia', 'Obama-era shift of US diplomatic, economic and military attention to the Asia-Pacific'],
            ['Made in China 2025', '2015 industrial policy for advanced manufacturing and strategic technologies (semiconductors, EVs, robotics)'],
            ['Strategic competition', 'Long-term rivalry for economic, military, technological and political influence without necessarily going to war'],
        ]),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 7 phase 6
    secs.append(Sec('Phase 6: Geopolitical fragmentation and strategic realignment (2020 onwards)', [
        p('The 2020s have more global and regional conflicts, driven by rivalry, economic shifts and nationalism. States put **sovereignty, national security and strategic interests** first. Features: strategic recalibration, **techno-nationalism**, economic nationalism, transactional diplomacy, cyber threats and weaker cooperation.'),
        h3('1 · Major conflicts and rivalries'),
        ul(['**West Asia:** the **Israel-Hamas conflict (began 2023)** created a major humanitarian crisis in Gaza. Iran, Israel, Hezbollah and the Houthis widened it beyond Gaza.',
            '> In **February 2026** joint US-Israeli strikes on Iran marked a major escalation and killed Iran’s Supreme Leader Ayatollah Ali Khamenei. Iran retaliated. The handout reads this as a shift from proxy confrontation towards **direct state-to-state conflict**.',
            '**Russia-Ukraine (2022-):** sharply raised Russia-West tension; hit European security, energy markets and food; Western military support and sanctions made it part of the wider Russia-West confrontation; no durable settlement yet. Russia vetoed a 2022 UNSC resolution on the invasion.']),
        h3('2 · Power shifts and multipolarity'),
        ul(['**US-China rivalry** dominates the Indo-Pacific. China: **BRI plus military modernisation**; US: **Quad plus AUKUS**.',
            '**Middle powers** (India, Brazil, Indonesia, Türkiye) seek strategic space. Countries form **issue-based coalitions**, not permanent blocs.',
            '**BRICS, Quad, SCO, G20** show overlapping partnerships and **competitive multilateralism**: different powers and groupings compete to shape rules and outcomes.',
            '**India:** strategic autonomy and multi-alignment; ties with both Russia and the West; Quad, BRICS, SCO and G20 together. The handout calls this “strategic patience and calibrated engagement”.']),
        h3('3 · Economic nationalism and deglobalisation'),
        ul(['COVID-19 and geopolitical tension exposed the risks of dependence on global supply chains, strengthening **deglobalisation, protectionism and economic nationalism**.',
            '**Supply-chain resilience:** diversify semiconductors, pharmaceuticals, critical minerals. **Supply Chain Resilience Initiative (SCRI)** by India, Japan and Australia.',
            '**Reshoring:** the EU is raising domestic production of semiconductors and pharmaceuticals. **Friend-shoring and de-risking:** shifting supply chains to trusted partners (example given: Pax Silica). **Strategic trade:** security considerations shape trade and investment.',
            '**Alternative finance:** BRICS countries have discussed local currencies and alternative payment mechanisms.',
            '**US tariff politics:** a protectionist administration returned after the 2024 election and revived “America First” (the slide says since 2025). The **Lindsey O. Graham Sanctioning Russia and Iran Act of 2026** lets the US President impose **tariffs up to 100%** on countries importing large amounts of Russian oil and gas. In **2025** fresh US tariffs hit Chinese goods; China answered with tariffs on US farm exports and curbs on critical materials, including **rare earths**.',
            '**Sovereignty-first** policy: national security now outranks market efficiency. India’s own parallel is **Atmanirbhar Bharat**.']),
        tbl('Key concepts', ['Concept', 'Meaning and example'], [
            ['Geoeconomics', 'Use of trade, tariffs, sanctions, investment or finance to reach strategic goals'],
            ['Weaponised interdependence', 'Using control over financial, trade or technology networks to pressure another country. Examples: curbs on Russian banks’ access to **SWIFT**; US **chip export controls** on China'],
            ['Transactional diplomacy', 'Foreign policy based on immediate benefits and bargaining, not long-term commitments or shared values'],
            ['Techno-nationalism', 'Links technology to national security and economic power; states control critical technologies and may deny them to rivals'],
        ]),
        h3('4 · Technology and cyber geopolitics'),
        ul(['The US and China compete in **AI, semiconductors, advanced computing and telecom** (example: US ban on Huawei).',
            '**Export controls** and technology restrictions are used for security. **Cyberattacks** on critical infrastructure and **military AI** raise new risks.',
            'India stresses an **inclusive, human-centric approach to AI** and wider democratisation. The handout quotes PM Modi: “India does not see fear in AI. India sees fortune in AI. India sees the future in AI.”']),
        h3('5 · Rise of the Global South'),
        ul(['Developing countries want more voice in **agenda-setting, development finance and institutional reform**.',
            'G20 presidencies: **Indonesia (2022), India (2023), Brazil (2024), South Africa (2025)**, bringing development, debt, food security and Global South concerns forward.',
            '**African Union became a permanent member of the G20 (2023).** **Global Alliance Against Hunger and Poverty** came under Brazil’s G20 presidency.',
            'Reform demands: **G4** seeks more permanent UNSC seats; **Ezulwini Consensus** is the AU’s demand for African representation in the Security Council; developing countries seek more say in the **IMF and World Bank**.']),
        h3('6 · Nationalism and populist politics'),
        ul(['Themes: national sovereignty, stricter migration controls, protection of domestic industry, doubt about deeper globalisation.',
            'Examples named: Trump’s “America First”, Giorgia Meloni’s **Brothers of Italy**, Marine Le Pen’s **National Rally** (France), the **AfD** (Germany).']),
        h3('7 · Climate and humanitarian stress'),
        ul(['Climate change is a **threat multiplier**: food insecurity, displacement, livelihood stress, pressure on resources. It usually **intensifies existing vulnerabilities** rather than directly causing conflict.',
            '**Nepal:** a 2026 glacier collapse and floods showed Himalayan vulnerability and revived calls for climate justice and loss-and-damage support. **South Asia:** heatwaves, floods, extreme rain.',
            '**Myanmar:** Cyclone Mocha (2023) worsened a crisis after the 2021 military takeover; conflict pushed refugees into India and Thailand. **Sahel and Horn of Africa:** conflict, instability and climate shocks worsen hunger and migration.']),
        h3('8 · Institutional paralysis'),
        ul(['**UNSC veto:** the P5 veto can block action in major conflicts (Russia’s 2022 veto).',
            '**WTO Appellate Body paralysis:** the US blocked judicial appointments, leaving no quorum for appeals.',
            'The handout calls the result **selective multilateralism and institutional paralysis**.']),
        flow('Essence of the phase (slide 21)', [
            ('Rivalry', '', 'bad'), ('Strategic realignment', '', ''), ('Economic and tech fragmentation', '', 'warn'),
            ('Multipolarity', '', ''), ('Institutional paralysis', '', 'bad')]),
        h3('Where does the global order stand today? (slides 22-23)'),
        fig('img/ir-global-order-1.jpg', 'Features 1 to 3: great-power rivalry and multipolarity; economics has become strategic; institutions are under stress.', 'Class slide 22'),
        fig('img/ir-global-order-2.jpg', 'Features 4 to 6: rise of minilateralism; sovereign nationalism and a changing globalisation; US-led order versus China-backed alternatives (table below).', 'Class slide 23'),
        tbl('Feature 6: US-led system versus China-backed alternatives (slide 23)', ['Area', 'US-led system', 'China-backed alternatives'], [
            ['Development finance', 'IMF / World Bank', 'AIIB / NDB'],
            ['Connectivity', 'PGII / IMEC', 'BRI / CPEC'],
            ['Finance', 'Dollar and SWIFT', 'Yuan settlements and alternative payment mechanisms'],
            ['Technology', 'US-led AI and semiconductors', 'Chinese 5G and digital infrastructure'],
        ], desc='The slide’s own line: China has **not replaced** the US-led order. Competition has widened across finance, technology, connectivity, institutions and narratives. Minilateral groupings (Quad, SCO, I2U2, BRICS+, trilaterals) **supplement, not replace**, traditional institutions.'),
        alert('Handout alert: “Pax Silica” and “Operation Ajay”',
            'The handout names **Pax Silica** (as a friend-shoring example) and **Operation Ajay** (in a list of evacuation operations) without explaining them. They appear here only as the handout writes them. Check the notebook if the teacher explained them in class.'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 8 India's goals & determinants
    secs.append(Sec('India’s foreign policy: goals and ten determinants', [
        p('India’s foreign policy changes with the **global order** (Cold War bipolarity to present multipolar churn), the **security environment** (China border, Pakistan, terrorism), **economic needs** (trade, FDI, energy, technology, especially after 1991) and **national ambitions** (G20, Global South, UNSC reform). Three broad goals stay constant: **security, prosperity and an independent voice** (strategic autonomy).'),
        tbl('The ten determinants (slides 3-7 of PPT-2, with handout detail)', ['Determinant', 'Aim and content', 'Examples'], [
            ['1 · Economic development', 'Create an outside environment that supports growth: **export markets and FDI, technology and capital, energy and minerals, reliable supply chains, connectivity, opportunities for Indian business and workers**. The 1991 reforms tightened the link', 'US, EU, Japan (trade and FDI); semiconductors, defence (technology); Russian crude, West Asian oil; China+1; Chabahar, INSTC, IMEC'],
            ['2 · Security and territorial integrity', 'Boundary disputes with **China and Pakistan**; cross-border terrorism; nuclear and missile risks; maritime and cyber security; external influence in the neighbourhood; fragile supply chains. These shape border infrastructure, defence partnerships, nuclear policy, maritime cooperation and **opposition to CPEC**', 'LAC preparedness; Indian Ocean surveillance'],
            ['3 · Geography', '**Himalayan frontier** (China, Nepal, Bhutan); **Pakistan** blocks direct land access to Afghanistan and Central Asia (so Chabahar matters); **Indian Ocean** carries trade and energy; **Andaman and Nicobar** sit near the Indian-Pacific sea routes; neighbours’ instability affects migration, security, connectivity', 'Malacca Strait; Chabahar'],
            ['4 · Strategic autonomy', 'Freedom to decide on India’s own interests: **pragmatism, sovereignty, multi-alignment, avoiding rigid alliances**', 'Quad with the US while keeping ties with Russia'],
            ['5 · Energy and critical resources', 'Aim: **diversification without excessive dependence on any one supplier**. West Asia (oil, gas); Russia (crude, nuclear); US (LNG, energy technology); Australia, Africa, Latin America (critical minerals)', '**National Critical Mineral Mission (2025)**'],
            ['6 · Science and technology', 'Access to advanced technology while building domestic capability: AI and semiconductors, space and quantum, defence technology, telecom and cyber, nuclear and clean energy, digital infrastructure', 'India-US critical technology; India-France space'],
            ['7 · Political values and history', 'Sovereign equality, **anti-colonialism and opposition to racial discrimination**, non-interference, peaceful settlement, multilateralism, **reform of global institutions**. Principles combine with pragmatism', 'Demand for UNSC reform'],
            ['8 · Domestic and federal politics', 'Parliament, parties, industry, media and public opinion shape policy space', '**Tamil Nadu**: Sri Lankan Tamils and fishermen; **West Bengal**: Teesta; **Northeast**: Bangladesh and Myanmar connectivity; coastal states: ports'],
            ['9 · Diaspora and people-to-people ties', 'One of the world’s largest overseas communities: **remittances and investment, business and professional networks, technology and knowledge links, cultural influence, consular protection**', '**Operation Ganga (2022)**: Ukraine. **Operation Kaveri (2023)**: Sudan. **Operation Sindhu (2025)**: Iran and Israel'],
            ['10 · Climate and emerging issues', 'Climate change and finance, sustainable lifestyles, global health, cybersecurity and AI governance, oceans and blue economy, space and polar regions', '**ISA, CDRI, Mission LiFE**'],
        ]),
        teacher('Class slide stress: each determinant is framed as “Aim: … Eg: …” (slides 3-7)',
            'The teacher gives a one-line **Aim** and a current **example** for every determinant. Use the example in your answer: it is what turns a list into evidence. The diaspora determinant is the one the **2026 Q19** asked about.'),
        mnemo('Ten determinants (memory aid built from the list)', 'ESGSEStPDDC',
            '**E**conomy · **S**ecurity · **G**eography · **S**trategic autonomy · **E**nergy · **S**cience and tech · **P**olitical values · **D**omestic politics · **D**iaspora · **C**limate. Say: “**E**very **S**mart **G**uy **S**ees **E**nergy, **S**cience, **P**olitics, **D**omestic **D**iaspora **C**limate.”'),
        callout('key', 'Why diaspora matters twice', 'The handout calls the diaspora **both a foreign-policy asset and a consular responsibility**: assets (remittances, networks, soft power) and duties (evacuations such as Ganga, Kaveri, Sindhu).'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 9 evolution
    secs.append(Sec('Evolution of India’s foreign policy: six periods', [
        tbl('At a glance (slide 8, PPT-2)', ['Period', 'Main approach', 'Key example'], [
            ['1947-1962', 'Non-alignment and idealism', 'Panchsheel, NAM'],
            ['1962-1971', 'Security correction', '1962 China war'],
            ['1971-1991', 'Strategic assertion', 'Indo-Soviet Treaty'],
            ['1991-1998', 'Economic opening', 'LPG, Look East'],
            ['1998-2014', 'Diversified partnerships', 'India-US Nuclear Deal'],
            ['2014-present', 'Multi-alignment', 'Quad + BRICS + SCO'],
        ]),
        h3('1947-1962: Non-alignment and idealist foreign policy'),
        ul(['India became independent in the Cold War bipolar order and wanted to avoid dependence on either bloc.',
            'Idealist principles: **peace, anti-colonialism, racial equality, disarmament, cooperation**. The handout calls this emphasis on values “**normative idealism**”.',
            'Emphasis: **non-alignment, Panchsheel and peaceful coexistence, support for newly independent countries, faith in multilateralism**.']),
        h3('1962-1971: Security correction'),
        ul(['The **1962 China war** exposed weak defence preparedness; the **1965 Pakistan war** raised the importance of security further.',
            'Focus: **defence modernisation, territorial integrity, military preparedness, pragmatic engagement with major powers, hard power**. Example: more defence cooperation with the Soviet Union.',
            'Shift: **idealism continued, but Realist concerns became stronger.** India did not abandon non-alignment.']),
        h3('1971-1991: Strategic assertion'),
        ul(['More willingness to use diplomatic and military capability: **Indo-Soviet Treaty (1971)**, **creation of Bangladesh**, **Pokhran-I (1974)**, more involvement in the neighbourhood, still **no formal alliances**.',
            'Key lesson: **non-alignment did not stop India from making a strategic partnership when security required it.**']),
        h3('1991-1998: Economic opening and strategic adjustment'),
        ul(['Key idea: **autonomy through economic integration**. The Soviet collapse and India’s 1991 crisis changed the environment.',
            'Focus: liberalisation, trade and FDI, access to capital and technology, **Look East Policy**, better ties with the US, Europe and East Asia.',
            '**Gujral Doctrine:** better neighbourhood relations through **trust + non-reciprocity + respect for sovereignty**.']),
        h3('1998-2014: Diversified strategic partnerships'),
        ul(['**Pokhran-II (1998)** first drew pressure, then ties widened: **deepening India-US relations, India-US Civil Nuclear Agreement**, continued Russia partnership, Japan, ASEAN and Europe, more defence, energy and technology cooperation, bigger roles in **G20 and BRICS**.',
            'India built strong relations with several powers **without depending on any one**.']),
        h3('2014-present: Multi-alignment and strategic pragmatism'),
        ul(['Context: **multipolar churn**: US-China rivalry, conflicts, technology competition, supply-chain risk, pressure on institutions. Approach: **multi-alignment and issue-based partnerships**.',
            '**Quad:** free and open Indo-Pacific amid China’s assertiveness. **AIIB:** India joined this China-initiated bank despite differences. **BRICS:** India works with China and Russia for a multipolar order.',
            '**Russia, energy:** India keeps importing Russian oil despite Western pressure. **Russia, defence:** India bought the **S-400** despite the risk of US **CAATSA** sanctions.',
            'Instruments: **minilateralism, maritime diplomacy, technology diplomacy, geoeconomics**. Role: a **bridge power** between major powers and the Global South, supporting **reformed multilateralism**.']),
        flow('India’s overall evolution (slide 21, PPT-2)', [
            ('Non-alignment', '', ''), ('Strategic partnerships', '', ''), ('Multi-alignment', '', ''), ('Issue-based cooperation', '', 'good')]),
        teacher('Class slide stress: “Central thread: Strategic autonomy” (slide 21)',
            'Present aim: **protect national interest, maintain policy independence, build economic and military capability, expand global influence, become a stronger rule-shaper.**'),
        alert('Handout alert: Gujral Doctrine and idealism are not the same thing',
            'The **Gujral Doctrine** belongs to **1991-1998** and is about the **neighbourhood** (trust, non-reciprocity, respect for sovereignty). **Panchsheel and NAM** belong to **1947-1962**. Do not mix the periods.'),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 10 continuities etc
    secs.append(Sec('Continuities, changes, trade-offs and challenges', [
        tbl('Strategic autonomy then and now (slide 15)', ['Earlier approach', 'Present approach'], [
            ['Distance from rival blocs', 'Engage several power centres'],
            ['Non-alignment', 'Multi-alignment'],
            ['Limited partnerships', 'Issue-based partnerships'],
            ['Political autonomy', 'Economic + technology + security autonomy'],
        ], desc='Example on the slide: Russian oil + Quad cooperation + BRICS membership.'),
        tbl('Key continuities', ['Continuity', 'Meaning', 'Example (slide 16)'], [
            ['Strategic autonomy', 'Decide on national interest without permanent dependence on any bloc', 'US + Russia ties'],
            ['National interest', 'Security, development and sovereignty guide choices', 'Russian crude'],
            ['Sovereignty and territorial integrity', 'Independent decision-making; protect borders', 'Opposition to CPEC through PoK'],
            ['Global South orientation', 'Anti-colonial solidarity became development partnership, climate justice, institutional reform', 'Voice of the Global South'],
            ['Dialogue and multilateralism', 'Peaceful settlement; cooperation', 'Ukraine diplomacy'],
            ['Neighbourhood centrality', 'South Asia and the Indian Ocean stay vital', 'Neighbourhood First'],
        ]),
        tbl('Key changes (slide 17)', ['Earlier pattern', 'Emerging pattern'], [
            ['Non-alignment', 'Multi-alignment and issue-based partnerships'],
            ['Post-colonial leadership', 'Global South leadership'],
            ['Continental focus', 'Continental + maritime + technology'],
            ['Limited economic leverage', 'Geoeconomics, DPI and supply-chain partnerships'],
            ['Cautious, defensive diplomacy', 'Proactive diplomacy and minilateralism (G20, Quad, I2U2, BRICS, SCO, ISA, CDRI)'],
            ['Mainly an aid recipient', 'Development partner and capacity builder'],
            ['Limited role in shaping rules', 'Greater ambition to be a rule-shaper'],
        ], desc='The handout’s warning: the shift is **not from values to interests**. India still follows its values but now has more economic, military and diplomatic capability to protect its interests. Examples on the slide: Quad, IMEC, DPI partnerships, G20 Presidency.'),
        tbl('Five trade-offs (slides 18-19)', ['Trade-off', 'What India must balance', 'Example'], [
            ['Strategic autonomy versus deeper alignment', 'Needs US and Europe for technology, defence, investment and balancing China; wants independence and Russia ties. Sharper US-China and Russia-West rivalry makes it harder', 'Quad + Russian oil'],
            ['China competition versus continued engagement', 'Respond on LAC, Indian Ocean, neighbourhood, technology; keep trade and BRICS/SCO engagement; de-risk', 'Competition: LAC. Cooperation: BRICS, SCO'],
            ['Neighbourhood sensitivity versus security assertion', 'Protect security and answer instability and outside influence without looking overbearing to smaller neighbours', 'Maldives, Nepal, Sri Lanka'],
            ['Global South leadership versus major-power partnerships', 'Speaks for developing countries yet builds close ties with advanced economies. Credibility needs real development support, finance and capacity-building', 'US, EU, Japan ties'],
            ['Principles versus hard national interest', 'Supports peace, dialogue and sovereignty yet takes practical decisions on energy, defence and security', 'Ukraine dialogue + Russian energy'],
        ]),
        p('The handout stresses: a **trade-off** is two important interests pulling different ways and India balancing both. The challenges below are **constraints, not trade-offs**.'),
        tbl('Structural challenges (handout lists seven; slide 20 shows the first three)', ['Challenge', 'Content'], [
            ['Institutional constraints', 'UNSC, IMF and World Bank still reflect an older power structure; India seeks UNSC permanent membership'],
            ['Domestic capability', 'Manufacturing, logistics, technology, defence capacity and resilience must support global ambitions'],
            ['External shocks', 'COVID-19, Ukraine war, Red Sea disruptions (slide); wars, energy disruptions, crises, supply-chain shocks (handout)'],
            ['Disjointed neighbourhood', 'South Asia is among the **least integrated regions**: low regional trade, connectivity gaps, political tension, weak regional institutions (handout only)'],
            ['Technology dependence', 'Gaps in semiconductors, AI, advanced manufacturing and critical technologies (handout only)'],
            ['Diplomatic capacity', 'Many engagements need a larger, more specialised diplomatic network (handout only)'],
            ['Global perception and credibility', 'Growing ambition has to be balanced with development priorities and commitments on governance, climate, trade and norms (handout only)'],
        ]),
        tbl('Key ideas in India’s foreign policy (slide 22)', ['Keyword', 'Meaning (and example)'], [
            ['Strategic autonomy', 'Independent choices; US + Russia ties'],
            ['Multi-alignment', 'Engage many power centres; Quad + BRICS'],
            ['Issue-based alignment', 'Different partners for different issues'],
            ['Vishwabandhu', 'India as a reliable friend and bridge-builder'],
            ['Net security provider', 'Regional (especially Indian Ocean) security role'],
            ['First responder', 'Quick help in crises'],
            ['Neighbourhood First', 'Priority to immediate neighbours (handout)'],
            ['Act East', 'Deeper engagement with Southeast Asia and the Indo-Pacific (handout)'],
            ['Reformed multilateralism', 'Reform UNSC and other institutions'],
            ['Global South leadership', 'Represent developing-country concerns'],
        ]),
    ], label='Class + handout'))

    # ---------------------------------------------------------------- 11 instruments (handout only)
    secs.append(Sec('Instruments of India’s contemporary foreign policy', [
        callout('source', 'Source note', '**Handout only (pages 19-21): no class slides for this part yet.** The handout calls the approach **The India Way**: protecting national interests without joining a fixed bloc, and working with several powers across security, trade, technology, energy, connectivity and development.'),
        tbl('Geoeconomic and technology diplomacy', ['Area', 'India’s approach'], [
            ['Energy security', 'Diversify supply: West Asia, Russia, the US and renewable-energy partnerships'],
            ['Supply-chain resilience', 'China+1, de-risking, friend-shoring, domestic capacity in critical sectors'],
            ['Critical minerals', 'Partnerships for lithium, rare earths, strategic minerals'],
            ['Connectivity', '**Chabahar, INSTC and IMEC** as alternative trade routes'],
            ['Digital diplomacy', 'Sharing DPI, UPI and digital public infrastructure'],
            ['Development partnership', 'Lines of credit, grants, training, capacity-building'],
        ], desc='The aim: turn India’s market size, technology and development experience into diplomatic influence.'),
        h3('Security diplomacy and the China factor'),
        p('China affects India’s border security, neighbourhood, Indian Ocean strategy, supply chains and technology choices. India’s response mixes **deterrence, de-risking, competition and selective engagement**:'),
        ul(['**LAC:** stronger infrastructure and military preparedness.', '**Indo-Pacific:** support for a free, open, inclusive, rules-based order.',
            '**Maritime partnerships:** with the US, Japan, Australia, France and island states.', '**BRI and CPEC:** opposition where projects affect India’s sovereignty.',
            '**Institutions:** engage China in BRICS and SCO while also working through the Quad.']),
        tbl('Two “necklace” ideas', ['Term', 'Meaning', 'Examples'], [
            ['String of Pearls', 'China’s network of ports, infrastructure projects and access points across the Indian Ocean region', '**Gwadar** (Pakistan), **Hambantota** (Sri Lanka), military base in **Djibouti**'],
            ['Diamond Necklace', 'India’s strategy of maritime partnerships, logistics access and strategic cooperation across the Indian Ocean and Indo-Pacific', '**Chabahar** (Iran), **Duqm** (Oman), **Sabang** (Indonesia)'],
        ]),
        h3('Neighbourhood and Indian Ocean diplomacy'),
        ul(['**Neighbourhood First**, connectivity (road, rail, ports, waterways, energy, digital), **First Responder** help in disasters, managing China’s growing regional influence.',
            'In the Indian Ocean India seeks to be a **net security provider**: **Maritime Domain Awareness, anti-piracy, HADR, coastal surveillance, capacity-building**. **SAGAR and MAHASAGAR** link maritime security with shared growth.']),
        tbl('Minilateral and institutional diplomacy', ['Platform', 'Main role'], [
            ['Quad', 'Indo-Pacific, maritime security, technology, supply chains'],
            ['I2U2', 'Food, energy, investment, technology'],
            ['India-France-UAE trilateral', 'Maritime, defence, energy'],
            ['BRICS / BRICS+', 'Global South voice and multipolarity'],
            ['SCO', 'Eurasia, Central Asia, security dialogue'],
            ['G20', 'Development, debt, climate finance, DPI'],
            ['ISA / CDRI', 'Renewable energy and climate resilience'],
        ], desc='India uses minilateralism as a **supplement, not a replacement**, for multilateralism, and still backs reform in the UN, WTO and global financial institutions.'),
        h3('Humanitarian, diaspora and soft-power diplomacy'),
        ul(['**First responder** in regional disasters; **evacuation diplomacy:** Operations **Ganga, Kaveri, Ajay and Sindhu**; humanitarian aid (food, medicines, vaccines, relief); diaspora protection.',
            '**Soft power:** Yoga, Buddhism and Ayurveda; diaspora networks; democracy and pluralism; development partnerships; civilisational links. The handout adds that soft power works best **when backed by delivery, credibility and development partnerships**.',
            'Diplomatic terms to know: **Vasudhaiva Kutumbakam, Voice of the Global South, Vishwabandhu, human-centric globalisation, Mission LiFE, reformed multilateralism**.']),
    ], label='Handout only'))

    return secs


# ------------------------------------------------------------------ map, timeline, links, recall, quiz
MAP = ('World order and India’s foreign policy', [
    ('Phases 1-2', [('Realism to 1914', 'Westphalia 1648; BoP; Schlieffen'), ('Liberal try', '14 Points 1918; League 1920'), ('Realism returns', 'Depression 1929; Manchuria 1931'), ('Nuclear age', 'Hiroshima 1945; MAD')]),
    ('Phase 3 Cold War', [('Liberalism', 'UN, IMF-WB, NPT 1968'), ('Realism', 'NATO 1949; Warsaw 1955'), ('Idealism', 'NAM 1961 (Belgrade)'), ('India link', 'Treaty 1971; USS Enterprise')]),
    ('Phase 4 Unipolar', [('USSR falls', '1991; US sole superpower'), ('Globalisation', 'WTO 1995; China 2001'), ('US reach', 'Afghanistan 2001; Iraq 2003'), ('India LPG', '1991 BoP crisis')]),
    ('Phase 5 Crisis', [('GFC 2008', 'faith in liberal order falls'), ('China rises', '2010 No. 2; BRI 2013'), ('New platforms', 'BRICS; NDB 2014'), ('Backlash', 'Brexit 2016; trade war')]),
    ('Phase 6 2020-', [('Conflicts', 'West Asia; Ukraine 2022'), ('Econ nationalism', 'tariffs; friend-shoring'), ('Tech and cyber', 'AI, chips, export controls'), ('Global South', 'AU in G20; UNSC reform'), ('Paralysis', 'UNSC veto; WTO AB')]),
    ('Ten determinants', [('Economy, security', 'growth; borders; terrorism'), ('Geography', 'Himalaya; Indian Ocean'), ('Autonomy, energy, S&T', 'multi-alignment'), ('Values, federal', 'anti-colonial; TN, WB'), ('Diaspora, climate', 'Ganga, Kaveri, Sindhu; ISA')]),
    ('Six periods', [('1947-62', 'non-alignment; Panchsheel'), ('1962-91', 'security; assertion; 1971'), ('1991-2014', 'LPG; Pokhran-II; US deal'), ('2014-', 'multi-alignment')]),
    ('Limits and tools', [('Trade-offs (5)', 'autonomy; China; neighbours'), ('Challenges (7)', 'institutions; capability'), ('Instruments', 'geoeconomics; maritime'), ('Soft power', 'Yoga; diaspora; DPI')]),
])

TIMELINE = [
    ('1618-1648', 'Thirty Years’ War: shows the danger of fragmented authority', False),
    ('1648', 'Peace of Westphalia: sovereign state system, non-interference', True),
    ('Till 1914', 'Phase 1: balance of power; Schlieffen Plan; Archduke Franz Ferdinand’s assassination triggers World War I', False),
    ('1918', 'Wilson’s 14 Points', True),
    ('1920', 'League of Nations', True),
    ('1929', 'Great Depression: protectionism, authoritarian regimes', False),
    ('1931', 'League fails to stop Japan in Manchuria', False),
    ('1935', 'League fails to stop Italy in Abyssinia', False),
    ('1945', 'Hiroshima and Nagasaki; United Nations; Cold War begins', True),
    ('1949', 'NATO formed', False),
    ('1955', 'Warsaw Pact', False),
    ('1961', 'NAM formally launched, Belgrade Summit', True),
    ('1962', 'Cuban Missile Crisis; India-China war (security correction begins)', False),
    ('1965', 'India-Pakistan war', False),
    ('1968', 'NPT', False),
    ('1971', 'Indo-Soviet Treaty of Peace, Friendship and Cooperation; Bangladesh; USS Enterprise', True),
    ('1972', 'Stockholm Conference', False),
    ('1973', 'Yom Kippur War', False),
    ('1974', 'Pokhran-I', False),
    ('1985', 'Schengen Agreement', False),
    ('1991', 'USSR collapses; India’s BoP crisis and LPG reforms', True),
    ('1995', 'WTO established', False),
    ('1997', 'Kyoto Protocol', False),
    ('1998', 'Pokhran-II', False),
    ('2001', 'China joins WTO; Afghanistan invasion; 9/11', False),
    ('2003', 'Iraq invasion', False),
    ('2008', 'Global Financial Crisis: crisis of liberalism begins', True),
    ('2010', 'China overtakes Japan as the second-largest economy', False),
    ('2013', 'Belt and Road Initiative', False),
    ('2014', 'BRICS New Development Bank', False),
    ('2015', 'Made in China 2025; Paris Agreement', False),
    ('2016', 'Brexit (about 52% vote to leave)', False),
    ('2018', 'US-China trade war', False),
    ('2020', 'Phase 6 begins (post-COVID)', True),
    ('2022', 'Russia invades Ukraine; Operation Ganga', False),
    ('2023', 'Israel-Hamas conflict; AU joins G20; Operation Kaveri', False),
    ('2025', 'Fresh US tariffs; National Critical Mineral Mission; Operation Sindhu', False),
    ('Feb 2026', 'Joint US-Israeli strikes on Iran', False),
]

LINKS = [
    ('Chapter 2: Major Powers', 'Phase 5 and 6 rivalry (US-China, Russia-West) is unpacked there with each power’s ambitions and instruments.'),
    ('Chapter 2: India-China', 'Phase 5 gave BRI, CPEC, Gwadar, Hambantota; Chapter 2 gives the border, issue boxes and the way forward.'),
    ('Chapter 2: India-US', 'The 1971 USS Enterprise episode here is the “strategic mistrust” row there.'),
    ('Chapter 2: India-Russia', 'The 1971 Treaty here opens the India-Russia timeline there; Russian oil and S-400 are the trade-off examples.'),
    ('Syllabus: neighbourhood and groupings', 'Determinants 3 and 8 and the “disjointed neighbourhood” challenge lead to “India and its neighbourhood”. Quad, BRICS, SCO, G20, I2U2 lead to “bilateral, regional and global groupings”.'),
    ('Syllabus: diaspora', 'Determinant 9 and the evacuation operations lead to the syllabus line “Indian diaspora”.'),
    ('Syllabus: institutions', 'UNSC, WTO Appellate Body, IMF and World Bank reform lead to “important international institutions, agencies and fora”.'),
    ('Syllabus: policies of other countries', 'US tariffs, the 2026 sanctions Act, China’s rare-earth controls are the “effect of policies of developed and developing countries on India’s interests”.'),
]

RECALL = [
    '**Six phases:** to 1914 sovereign states and BoP; 1919-1945 liberal experiment and WWII; 1945-1991 two superpowers and deterrence; 1991-2008 US primacy; 2008-2019/20 crisis of liberalism; 2020 onwards fragmentation.',
    '**Realism flow:** anarchy → self-help → mistrust → security dilemma → arms race → balance of power. Westphalia 1648 = sovereignty and non-interference.',
    '**Inter-war:** 14 Points 1918, League 1920; Depression 1929; Manchuria 1931, Abyssinia 1935; Hiroshima 1945; MAD and deterrence.',
    '**Cold War:** UN 1945, NPT 1968, Stockholm 1972, Schengen 1985, Marshall Plan (about $13 bn) versus COMECON; NATO 1949, Warsaw Pact 1955, Cuban crisis 1962, Yom Kippur 1973; NAM Belgrade 1961; India-USSR Treaty 1971.',
    '**Unipolar:** USSR 1991; WTO 1995; China WTO 2001; Afghanistan 2001, Iraq 2003; Kyoto 1997; India LPG 1991 (GDP about $270 bn to about $1.2 tn by 2008).',
    '**Crisis:** GFC 2008; China No. 2 in 2010; Pivot to Asia; NDB 2014; BRI 2013; Made in China 2025; Brexit 2016 (52%); 2018 trade war.',
    '**Phase 6:** West Asia (Feb 2026 strikes on Iran), Ukraine 2022; competitive multilateralism; Graham Act 2026 (up to 100% tariff); weaponised interdependence; G20 Indonesia-India-Brazil-South Africa 2022-2025; AU in G20 2023; G4 and Ezulwini; UNSC veto, WTO AB.',
    '**Essence:** Rivalry → Strategic Realignment → Economic and Tech Fragmentation → Multipolarity → Institutional Paralysis.',
    '**Ten determinants:** economy, security, geography, strategic autonomy, energy, S&T, values, domestic politics, diaspora, climate.',
    '**Six periods:** 1947-62 non-alignment; 1962-71 security correction; 1971-91 assertion; 1991-98 opening (Gujral Doctrine); 1998-2014 diversified; 2014- multi-alignment.',
    '**Five trade-offs:** autonomy v alignment; China competition v engagement; neighbourhood v assertion; Global South v major powers; principles v interest. **Seven challenges:** institutions, capability, shocks, neighbourhood, technology, diplomacy, credibility.',
    '**Instruments:** geoeconomics and tech, security (String of Pearls v Diamond Necklace), neighbourhood and IOR (SAGAR, MAHASAGAR), minilateral, humanitarian (Ganga, Kaveri, Ajay, Sindhu), soft power.',
]

TRAPS = [
    ('Phase 5 end date', 'Tables say 2008-2019; slide headings say “till 2020”. Rule: answer “2008 to 2019/20” and start Phase 6 in 2020.'),
    ('Westphalia is not the League', 'Westphalia 1648 = sovereignty and non-interference. League 1920 = collective security. Rule: sovereignty links to 1648, collective security to 1920.'),
    ('Security dilemma versus balance of power', 'The dilemma is the **problem** (arming for defence frightens others); BoP is the **attempt** to stop dominance. Rule: dilemma = cause of arms race; BoP = response.'),
    ('NAM date', 'NAM was formally launched at **Belgrade in 1961**, not at independence in 1947. Rule: 1961 and Belgrade together.'),
    ('1971 is not “joining a bloc”', 'The Treaty with the USSR is read as a security exception inside non-alignment, not an alliance. Rule: say “strategic partnership without formal alliance”.'),
    ('Strategic autonomy is not neutrality', 'Multi-alignment means engaging several powers at once (Quad + BRICS + Russian oil), not staying away from all. Rule: autonomy = freedom of choice, not distance.'),
    ('Gujral Doctrine belongs to 1991-98', 'It is about neighbours: trust, non-reciprocity, respect for sovereignty. Rule: Gujral = neighbourhood, 1990s.'),
    ('Trade-off versus challenge', 'The handout separates them: a trade-off balances two interests; a challenge is a constraint. Rule: “vs” rows are trade-offs; the rest are challenges.'),
    ('String of Pearls versus Diamond Necklace', 'Pearls are China’s ports and access (Gwadar, Hambantota, Djibouti). Necklace is India’s partnerships (Chabahar, Duqm, Sabang). Rule: Pearls = China, Necklace = India.'),
    ('Pax Silica and Operation Ajay', 'Named in the handout without explanation. Rule: do not invent details; check class notes.'),
]

MCQ = [
    ('The Peace of Westphalia (1648) is important in IR because it:', ['created the League of Nations', 'laid the foundation of the sovereign state system and non-interference', 'ended the Cold War', 'created a world government'], 1, 'It ended the Thirty Years’ War and set state sovereignty and non-interference. Rule: Westphalia = sovereignty.'),
    ('Which sequence is the Realism flow taught in class?', ['Anarchy → mistrust → self-help → arms race → security dilemma → BoP', 'Anarchy → self-help → mistrust → security dilemma → arms race → balance of power', 'Self-help → anarchy → arms race → mistrust → BoP → dilemma', 'Mistrust → anarchy → BoP → self-help → arms race → dilemma'], 1, 'Slide 7: international anarchy → self-help → mistrust → security dilemma → arms race → balance of power.'),
    ('The League of Nations failed to stop which two aggressions?', ['Germany in Poland and Italy in Manchuria', 'Japan in Manchuria (1931) and Italy in Abyssinia (1935)', 'Italy in Manchuria (1935) and Japan in Abyssinia (1931)', 'Soviet Union in Cuba and USA in Vietnam'], 1, 'Japan in Manchuria (1931) and Italy in Abyssinia (1935). The Cuban crisis belongs to the Cold War.'),
    ('Which pair of institution and year is correct (Cold War phase)?', ['NPT: 1985', 'Stockholm Conference: 1972', 'Schengen Agreement: 1968', 'Warsaw Pact: 1949'], 1, 'NPT 1968, Stockholm 1972, Schengen 1985, Warsaw Pact 1955 (NATO was 1949).'),
    ('The Non-Aligned Movement was formally launched at:', ['Bandung in 1955', 'Belgrade in 1961', 'New Delhi in 1947', 'Geneva in 1971'], 1, 'The handout: Belgrade Summit, 1961.'),
    ('Which statement about the unipolar phase (1991-2008) is correct?', ['WTO was set up in 1995 and China joined it in 2001', 'WTO was set up in 2001 and China joined in 1995', 'The Marshall Plan was launched in 1991', 'BRICS was dissolved in 2003'], 0, 'WTO 1995; China’s accession 2001.'),
    ('India’s 1991 LPG reforms followed:', ['the Pokhran-I test', 'a balance-of-payments crisis', 'the Indo-Soviet Treaty', 'the 2008 financial crisis'], 1, '1991 BoP crisis led to Liberalisation, Privatisation, Globalisation.'),
    ('The US “Pivot to Asia” under Obama was a response to:', ['the 1991 Soviet collapse', 'China’s rise, including overtaking Japan as No. 2 economy in 2010', 'Brexit', 'the 2022 Ukraine war'], 1, 'China overtook Japan in 2010; the US responded with the Pivot to Asia.'),
    ('The BRICS New Development Bank was created in:', ['2008', '2010', '2014', '2016'], 2, 'NDB 2014 (Brexit was 2016; GFC 2008).'),
    ('“Weaponised interdependence” is best illustrated by:', ['an arms-control treaty', 'curbs on Russian banks’ access to SWIFT and US chip export controls on China', 'a cultural exchange programme', 'a free-trade agreement'], 1, 'Control over financial, trade or technology networks used to pressure another country.'),
    ('Which sequence of G20 presidencies is correct?', ['India, Indonesia, Brazil, South Africa', 'Indonesia, India, Brazil, South Africa', 'Brazil, India, Indonesia, South Africa', 'Indonesia, Brazil, India, South Africa'], 1, '2022 Indonesia, 2023 India, 2024 Brazil, 2025 South Africa.'),
    ('The Gujral Doctrine rests on:', ['trust, non-reciprocity and respect for sovereignty', 'reciprocity, deterrence and alliance', 'Panchsheel and non-alignment', 'Look East and Act East'], 0, 'Gujral Doctrine: better neighbourhood relations through trust, non-reciprocity, respect for sovereignty (1991-98 phase).'),
    ('Which is an example of India’s “Diamond Necklace”?', ['Gwadar', 'Hambantota', 'Chabahar', 'Djibouti'], 2, 'Diamond Necklace: Chabahar, Duqm, Sabang. The first, second and fourth are String of Pearls examples.'),
    ('Operation Kaveri (2023) evacuated Indians from:', ['Ukraine', 'Sudan', 'Iran and Israel', 'Myanmar'], 1, 'Ganga 2022 Ukraine; Kaveri 2023 Sudan; Sindhu 2025 Iran and Israel.'),
    ('Which is a TRUE statement about India’s present foreign policy?', ['It has moved from values to interests entirely', 'Its central thread remains strategic autonomy, now with more capability', 'It rejects all minilateral groupings', 'It follows a treaty alliance with the US'], 1, 'The handout: the shift is not from values to interests; the central thread remains strategic autonomy.'),
]

CARDS = [
    ('What did the Peace of Westphalia (1648) establish?', 'State sovereignty and non-interference; basis of modern international law and the sovereign state system.'),
    ('What is international anarchy?', 'No world government above states, so each state must secure itself. It is not chaos.'),
    ('Define the security dilemma.', 'One state arms for defence, others feel threatened and arm too; all end up less secure though none wanted war.'),
    ('Realism flow (slide 7)?', 'Anarchy → self-help → mistrust → security dilemma → arms race → balance of power.'),
    ('What did Nehru call the peace after World War I?', 'A “nervous state of peace”.'),
    ('Wilson’s 14 Points and League of Nations: years?', '14 Points 1918; League of Nations 1920 (collective security).'),
    ('Why did the League fail?', 'Collective security works only if major powers will enforce it; it could not stop Japan (Manchuria 1931) or Italy (Abyssinia 1935).'),
    ('What did the Great Depression (1929) do?', 'Weakened cooperation; protectionism; authoritarian regimes in Germany, Italy, Japan; expansionism; led to WWII.'),
    ('What is MAD?', 'Mutually Assured Destruction: any nuclear exchange destroys both sides, so direct nuclear war is deterred.'),
    ('Three strands of Phase 3?', 'Liberalism (UN, IMF-WB, NPT), Realism (NATO, Warsaw, proxy wars), Idealism (NAM).'),
    ('Marshall Plan versus COMECON?', 'Marshall Plan: about $13 bn to rebuild Western Europe and contain communism. COMECON: Soviet-led economic cooperation, kept influence over Eastern Europe.'),
    ('NPT, Stockholm, Schengen: years?', 'NPT 1968; Stockholm Conference 1972; Schengen 1985.'),
    ('NATO and Warsaw Pact: years?', 'NATO 1949; Warsaw Pact 1955.'),
    ('When and where was NAM formally launched?', 'Belgrade Summit, 1961.'),
    ('Why did India sign the 1971 Treaty with the USSR?', 'Security need during the Bangladesh crisis. The US sent the USS Enterprise into the Bay of Bengal in support of Pakistan.'),
    ('WTO and China’s entry: years?', 'WTO 1995; China joined 2001.'),
    ('What do Afghanistan (2001) and Iraq (2003) show?', 'US military reach; Iraq also showed the risk of strategic overreach.'),
    ('What triggered India’s LPG reforms and what did GDP do?', 'The 1991 BoP crisis. Nominal GDP rose from about $270 bn (1991) to nearly $1.2 tn (2008).'),
    ('Why did the 2008 GFC matter?', 'It weakened Western economies and confidence in the liberal order; emerging powers, especially China, gained weight.'),
    ('China overtook Japan as No. 2 economy in?', '2010; the US answered with the Pivot to Asia.'),
    ('What are salami slicing and A2/AD?', 'Salami slicing: small steps that avoid a big response. A2/AD: capabilities to keep opposing forces out of a region.'),
    ('How did US-China rivalry spread (slide 17)?', 'Pivot to Asia → 2018 trade war → technology → supply chains → Indo-Pacific rivalry.'),
    ('Essence of Phase 6?', 'Rivalry → Strategic Realignment → Economic and Tech Fragmentation → Multipolarity → Institutional Paralysis.'),
    ('What is competitive multilateralism?', 'Powers and groupings compete to shape rules and institutions (BRICS, Quad, SCO, G20).'),
    ('Name the three Phase 6 concepts: geoeconomics, weaponised interdependence, techno-nationalism.', 'Geoeconomics: trade/finance as strategic tools. Weaponised interdependence: use of control over networks (SWIFT, chips). Techno-nationalism: technology tied to national security.'),
    ('Which law allows US tariffs up to 100% on buyers of Russian oil and gas?', 'The Lindsey O. Graham Sanctioning Russia and Iran Act of 2026.'),
    ('G20 presidencies 2022-2025?', 'Indonesia, India, Brazil, South Africa. AU became a permanent member in 2023.'),
    ('G4 and Ezulwini Consensus?', 'G4 seeks more permanent UNSC seats; Ezulwini is the AU’s demand for African representation.'),
    ('What does “climate as threat multiplier” mean?', 'Climate change intensifies existing vulnerabilities (food, displacement, livelihoods); it does not usually cause conflict directly.'),
    ('Two signs of institutional paralysis?', 'UNSC veto (Russia 2022); WTO Appellate Body without quorum because the US blocked appointments.'),
    ('Name the ten determinants of Indian foreign policy.', 'Economy, security, geography, strategic autonomy, energy, S&T, values, domestic politics, diaspora, climate.'),
    ('Six periods of Indian foreign policy and one example each?', '1947-62 Panchsheel/NAM; 1962-71 1962 war; 1971-91 Indo-Soviet Treaty; 1991-98 LPG/Look East; 1998-2014 India-US nuclear deal; 2014- Quad + BRICS + SCO.'),
    ('What is the Gujral Doctrine?', 'Neighbourhood policy of trust, non-reciprocity and respect for sovereignty (1991-98).'),
    ('How does India show multi-alignment (slide 14)?', 'Quad; AIIB; BRICS; Russian oil despite pressure; S-400 despite CAATSA risk.'),
    ('Five trade-offs?', 'Autonomy v alignment; China competition v engagement; neighbourhood v assertion; Global South v major-power ties; principles v hard interest.'),
    ('Seven structural challenges?', 'Institutions, domestic capability, external shocks, disjointed neighbourhood, technology dependence, diplomatic capacity, global credibility.'),
    ('String of Pearls versus Diamond Necklace?', 'Pearls: China’s ports/access (Gwadar, Hambantota, Djibouti). Necklace: India’s partnerships (Chabahar, Duqm, Sabang).'),
    ('Operations Ganga, Kaveri, Sindhu?', 'Ganga 2022 Ukraine; Kaveri 2023 Sudan; Sindhu 2025 Iran and Israel.'),
    ('India’s “net security provider” tools?', 'Maritime Domain Awareness, anti-piracy, HADR, coastal surveillance, capacity-building; SAGAR and MAHASAGAR.'),
]

# Mains skeletons: (id, title, intro, body list, closing)
SKELETONS = [
    ('Mains 2025 (10m, 150w): sovereign nationalism after waning globalisation',
     'Intro: the post-Cold War liberal order (WTO 1995, China 2001) has given way, since 2008, to globalisation that is “more selective, more political, more security-driven”.',
     ['Waning globalisation: GFC 2008; protectionism; 2018 US-China trade war; COVID exposed supply-chain risks → reshoring, friend-shoring, de-risking.',
      'Sovereign nationalism: Brexit 2016 (sovereignty, immigration), Syrian refugee crisis, populist parties (America First, Brothers of Italy, National Rally, AfD), migration controls, techno-nationalism, security over market efficiency.',
      'Institutions weaken: UNSC veto, WTO Appellate Body paralysis → selective multilateralism.',
      'Counter-trend: interdependence continues; minilateral groupings and the Global South seek voice; India answers with Atmanirbhar Bharat plus multi-alignment.'],
     'Closing: globalisation is not ending; it is being rewired by sovereignty and security.'),
    ('Mains 2020 (15m, 250w): Quad, from military alliance to trade bloc?',
     'Intro: the Quad (India, US, Japan, Australia) is a minilateral grouping for a free and open Indo-Pacific, not a treaty alliance.',
     ['Test the claim: the notes give the Quad’s role as Indo-Pacific, maritime security, technology and supply chains. Trade bloc features are not named.',
      'Maritime side: Quad and Malabar strengthen maritime security and naval coordination.',
      'Economic and technology side: resilient supply chains and critical technologies (Chapter 2).',
      'India’s stance: avoids a formal anti-China military bloc; uses minilateralism as a supplement, not a replacement (Chapter 1).'],
     'Closing: the Quad is a multi-issue minilateral; calling it a trade bloc overstates the shift.'),
    ('Mains 2019 (15m, 250w): has India stopped being a leader of the oppressed?',
     'Intro: in 1947-62 India stressed anti-colonialism, racial equality and support for newly independent states, and led NAM.',
     ['What changed: post-colonial leadership → Global South leadership; aid recipient → development partner; rule-shaping ambition.',
      'Evidence of continuity: Voice of the Global South; G20 presidency 2023; AU’s permanent G20 seat (2023); CBDR and climate justice stance.',
      'Evidence of tension: the Global South v major-power trade-off (close ties with US, EU, Japan); credibility needs real finance and capacity-building; security turn after 1962.',
      'Verdict: the image has changed form (from moral leader to bridge power), not vanished.'],
     'Closing: India now leads by delivery and by bridging, not by moral claim alone.'),
    ('Mains 2026 Q10 (10m, 150w): BRICS as counterweight and alternative',
     'Intro: BRICS grew from emerging economies’ demand for a bigger voice in global governance.',
     ['Alternative finance: NDB (2014) alongside AIIB versus IMF/World Bank; talk of local currencies and alternative payments; Russia’s “BRICS Bridge” idea (Chapter 2).',
      'Voice and multipolarity: BRICS and BRICS+ project Global South voice; China uses BRICS, SCO, AIIB, BRI to expand influence.',
      'India’s use: works with China and Russia for a multipolar order; the 2026 New Delhi Declaration backed a Task Force on Growth and Development and a bigger NDB role (Chapter 2).',
      'Limits: groupings supplement, not replace, existing institutions; India-China divergences; Chinese influence may shape the platform.'],
     'Closing: a counterweight in voice, not yet a replacement for the US-led system.'),
    ('Mains 2026 Q19 (15m, 250w): diaspora as living bridge and strategic leverage',
     'Intro: India has one of the world’s largest overseas communities, treated as a foreign-policy asset and a consular responsibility.',
     ['Economic: remittances, investment, business and professional networks.',
      'Knowledge and technology links; in the US, Indians are about 1.5% of the population, pay over $300 bn in federal taxes, and Indian students are 82% STEM (Chapter 2).',
      'Cultural and soft power: Yoga, Buddhism, Ayurveda, diaspora networks, civilisational links.',
      'Critical view: leverage is limited by host-country politics (H-1B, student safety, extremism in some places); consular burden (Ganga 2022, Kaveri 2023, Sindhu 2025); soft power works only when backed by delivery and credibility.'],
     'Closing: a bridge and an asset, but leverage depends on host-country goodwill and Indian delivery.'),
    ('Mains 2026 Q9 (10m, 150w): IPMDA between SAGAR and the Quad',
     'Intro: SAGAR/MAHASAGAR links maritime security with shared growth; the Quad is the collective Indo-Pacific strategy. (IPMDA is not covered in these notes; add its details after class.)',
     ['SAGAR/MAHASAGAR: India as net security provider through Maritime Domain Awareness, anti-piracy, HADR, coastal surveillance, capacity-building.',
      'Quad: Indo-Pacific, maritime security, technology and supply chains.',
      'Bridge logic: Maritime Domain Awareness is the shared capability: it answers Chinese presence (ports, research vessels, naval reach) in the Indian Ocean.',
      'Critical angle: depends on partners’ capacity and on island states’ comfort (neighbourhood sensitivity v security assertion).'],
     'Closing: IPMDA-type cooperation connects India’s regional role to the Quad, but delivery is the test.'),
]

PRIORITY = 'High'
