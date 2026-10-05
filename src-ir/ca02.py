# -*- coding: utf-8 -*-
"""Chapter 2 live current-affairs layer. Facts come only from the Aug 2026 and Jul 2026 current-affairs
magazines in the UPSC Project (plus web items, labelled)."""
from lib import *

AUG = 'Aug 2026 CA'
JUL = 'Jul 2026 CA'

LIVE = {}

# ------------------------------------------------------------------ major powers
LIVE['Ambitions and instruments: the United States'] = [
    live_head('US instruments, caught on camera'),
    live(AUG, 'Tariffs as foreign policy: 25% + 25% became 18%',
         'The US used **economic statecraft** against India: a **25% reciprocal tariff** (2025), a further **25%** citing Russian oil, then a **February 2026 interim framework** bringing the total to **18%**. India’s baseline moved from about **3% to 18%**.',
         'In a “US ambitions and instruments” answer, this is your instrument example: tariffs punished an energy choice by a partner. Pair it with the **friend-shoring** idea the US now offers (semiconductors, electronics).',
         '**Friend-shoring**: relocating supply chains to trusted countries with shared interests. **Minerals Security Partnership**: India joined in **2023**. **IPEF** (2022, 14 members): India is in the Supply Chains, Clean Economy and Fair Economy pillars, but an **observer in the Trade pillar**.',
         src='Aug 2026 CA §3.3.'),
    live_quick('Jul-Aug 2026', [
        '**US-Saudi civil nuclear deal:** a **123 Agreement** (Section 123, US Atomic Energy Act 1954) giving a **30-year** framework for civil nuclear cooperation. A 123 Agreement is required before the US can transfer nuclear material, reactors, technology or fuel. **India-US 123 Agreement: 2008.**',
        '**Visa rules:** “Duration of Status” replaced by a fixed stay for F, J and I visas.',
        '**CENTCOM at Chabahar:** US forces destroyed a surveillance tower at Iran’s Shahid Kalantari port, near India’s own terminal.',
        '**“Lake America”:** the US federal reference to Lake Ontario was renamed; Canada keeps the old name.',
    ], src='Jul 2026 CA §3.9.4, §3.9.5, conflict areas; Aug 2026 CA §3.9.5.'),
]

LIVE['Ambitions and instruments: China'] = [
    live_head('China’s instruments, this summer'),
    live(AUG, 'Writing a nature reserve into a disputed shoal',
         'China issued rules to manage the **Huangyan Dao National Nature Reserve** around **Scarborough Shoal**: no one may enter except as law allows, and fishing, mining and coral extraction that harm rare species are banned without approval. The **Philippines** had just deposited its official chart of the shoal with the UN.',
         'A neat example of **lawfare**: environmental protection used to assert control. Contrast the instruments: China writes a domestic rule; the Philippines files an international chart; the 2016 arbitral award says China has no historic-rights basis.',
         'Scarborough = **Huangyan Dao** (China) = **Panatag** (Philippines). The 2016 UNCLOS tribunal held it a **rock under Article 121(3)**: no EEZ, no continental shelf. See the full card under US-China rivalry.',
         src='Aug 2026 CA §3.5 (South China Sea).'),
    live_quick('Aug 2026', [
        '**Polar Silk Road:** China pushes it in the Arctic; Russia holds over **40%** of the Arctic; Marine Protected Areas in Antarctica’s Southern Ocean (which India co-sponsors) are **blocked by Russia and China**.',
        '**Brahmaputra:** China is building **one of the largest hydropower projects** on the river; India has raised concern about flows. China controls the **upstream** Brahmaputra, Sutlej and Indus.',
        '**CPEC**, China’s flagship BRI project, passes through **PoK**. India has **not joined the BRI** (launched 2013).',
    ], src='Aug 2026 CA §3.1, §3.4, §3.6.'),
]

LIVE['Ambitions and instruments: Russia'] = [
    live_head('Russia’s instruments, this summer'),
    live_quick('Jul-Aug 2026', [
        '**Kuril Islands:** Japan condemned President Putin’s visit. Japan claims **Etorofu** as part of its **Northern Territories**. The chain stretches from **Kamchatka** to Japan’s **Hokkaido** and separates the **Sea of Okhotsk** from the North Pacific; rich in fish and minerals, strategic.',
        '**OPEC+:** Russia is a partner in the 2016 grouping; seven OPEC+ countries agreed to raise output in Aug 2026. The **UAE left OPEC in May 2026**.',
        '**Arctic:** Russia holds over **40%** of the Arctic, with extensive strategic and energy assets; it limits data availability.',
        '**Nord Stream:** German prosecutors said the 2022 sabotage was ordered by Ukrainian state authorities. Nord Stream 2 remains non-operational.',
    ], src='Aug 2026 CA §3.9.3, §3.8.2, §3.1; Jul 2026 CA §3.8.5.'),
]

LIVE['US-China rivalry'] = [
    live_head('the rivalry, on a map'),
    live(AUG, 'Scarborough Shoal: the 2016 award, a rock, and a chart at the UN',
         'China claims nearly **90%** of the South China Sea under the **Nine-Dash Line**, overlapping ASEAN states’ EEZs. The **2016 UNCLOS tribunal** said there is **no legal basis for China’s historic rights**; it held **Scarborough Shoal is a “rock” (Article 121(3))** with no EEZ or shelf, and affirmed **traditional Filipino fishing rights**. China calls the award null and void. In 2026 the **Philippines deposited its nautical chart with the UN** (UNCLOS Article 16) and **China issued reserve rules**.',
         'Frame the rivalry as **rules versus facts on the water**: law (award, charts at the UN) against construction (artificial islands, reserve rules). The US is not the claimant here; the rivalry runs through its Philippine ally and India’s own interests.',
         '**UNCLOS Art. 16** (charts to the UN Secretary-General), **Art. 121(3)** (rocks), **Art. 123** (cooperation in semi-enclosed seas). **Spratlys**: claimed in full by China, Taiwan, Vietnam; parts by Malaysia, Philippines. **Paracels**: held by China, claimed by Vietnam and Taiwan. PYQs quoted: SCS significance (2016); India-China bilateral issues with SCS (2014).',
         'Which article denies a “rock” an EEZ, and which one sends charts to the UN?',
         'Article 121(3) denies a rock an EEZ or continental shelf. Article 16 requires charts to be deposited with the UN Secretary-General.',
         src='Aug 2026 CA §3.5 (South China Sea).'),
    live(AUG, 'Why India has skin in this game: 55% of its trade',
         'Over **55% of India’s trade** passes through the **South China Sea and Malacca Strait** (MEA). The sea carries about **22% of global trade** and **60% of maritime trade**, holds about **12% of the world fish catch**, and its deep basin hides submarines. **ONGC Videsh** holds exploration **Block 128** off Vietnam. India’s **first BrahMos export** went to the **Philippines**.',
         'Link the US-China contest to India’s interests: trade, energy, defence exports. India’s answer in policy words: **Act East, Neighbourhood First, MAHASAGAR**. Add the way out: a **binding ASEAN-China Code of Conduct** and UNCLOS-aligned claims.',
         '**MAHASAGAR**: extends SAGAR from maritime security to economic and geopolitical concerns; India as “Preferred Security Partner and First Responder” rather than only “net security provider”. SCS oil and gas: 11 billion barrels of oil, 190 trillion cubic feet of gas.',
         src='Aug 2026 CA §3.5.'),
    live(AUG, 'The rivalry reaches the poles',
         'India sits between two blocs at the poles: **Seven of the eight Arctic States are NATO members**, Russia holds **over 40%** of the Arctic, and China pushes a **Polar Silk Road**. India is only an **Arctic Council observer (2013)**, without a decision-making vote.',
         'Use it in a “rivalry beyond the Indo-Pacific” answer. India’s lever is science (Himadri, IndARC) and the **three-pole advantage** (Arctic, Antarctica, Himalaya).',
         '**Arctic Council** (1996 Ottawa Declaration): 8 States, 6 Permanent Participants. **India’s Arctic Policy (2022)**: six pillars.',
         src='Aug 2026 CA §3.1.'),
]

LIVE['Russia-West confrontation'] = [
    live_head('confrontation, July-August 2026'),
    live(JUL, 'Europe forms a ten-nation missile shield; Ukraine is a member',
         'Ten countries announced the **Integrated Anti-Ballistic Missile Coalition** in **Paris**: Denmark, France, Germany, Italy, Netherlands, Norway, Spain, Sweden, **Ukraine** and the UK. Its aim is a shared integrated ballistic-missile defence that **complements existing European systems**.',
         'Evidence for the “Russia-West confrontation” sections: Europe is now building air-defence architecture around Ukraine itself, not only sanctioning Russia.',
         'Note the membership is **not the same as NATO or the EU**: it includes Ukraine and excludes some EU states. Ukraine joining this coalition is the news hook.',
         src='Jul 2026 CA §3.9.2.'),
    live(JUL, 'Nord Stream, Odesa, Kuril: three fronts, one pattern',
         '**Nord Stream:** German prosecutors said the 2022 sabotage was ordered by **Ukrainian state authorities**. **Odesa:** a Russian missile strike on a merchant ship killed **ten crew, four of them Indian**. **Kurils:** Japan condemned Putin’s visit to islands it calls its Northern Territories.',
         'Three fronts, one pattern: energy lifelines, shipping and disputed territory are all now arenas of the same confrontation. Add the India angle: Indian seafarers die in the crossfire.',
         '**Odesa**: Ukrainian port, north-western Black Sea. **Kuril/Etorofu**: Japan’s Northern Territories claim; **Sea of Okhotsk** separated from the North Pacific.',
         'Which of the three events killed Indians, and where is the port?',
         'The Odesa ship strike (four Indian crew among ten dead); Odesa is a Ukrainian port on the north-western Black Sea.',
         src='Jul 2026 CA §3.8.5, conflict areas; Aug 2026 CA §3.9.3.'),
]

LIVE['India’s approach to major-power competition'] = [
    live_head('India’s balancing act, with evidence'),
    live(JUL + ' + ' + AUG, 'Hedging by others, balancing by India: MJDA and three summits',
         'While **Saudi Arabia, Türkiye and Pakistan** hedged with MJDA, India signed with **Australia** (inside AUKUS), **Japan** (sanctions Russia) and **Indonesia** (parallel ties with China, Russia, Turkey). The MEA said it is **examining MJDA’s implications** for national security and regional stability and will safeguard national interests.',
         'India’s approach in one line: **partners on every side, alliances with none**. MJDA shows the world hedging; the summits show India hedging back. Add the **Kautilya mandala**: a neighbouring rival (Pakistan) may gain strength through its allies, so befriend the rival’s rivals (Greece, Cyprus, Armenia; UAE, Israel, Oman).',
         '**Link and Act West**; **IMEC**, **I2U2**, **IORA** (India chair 2025-27), **MAHASAGAR**. **IPEF** observer in the trade pillar shows India picks the pillars it joins.',
         'In what sense is India’s response to MJDA “mandala” thinking?',
         'It treats Pakistan’s new allies as a neighbour-rival strengthened by friends, and answers by befriending the encircling states: Greece, Cyprus, Armenia, and UAE, Israel, Oman.',
         src='Aug 2026 CA §3.2; Jul 2026 CA §3.1, §3.2, §3.4.'),
]

# ------------------------------------------------------------------ India-China
LIVE['India-China: nature, evolution and convergence'] = [
    live_head('the thaw, step by step'),
    live('Web, 12 Sep 2026', 'Modi and Xi meet in New Delhi on the BRICS sidelines',
         'On **12 September 2026** the two leaders met on the sidelines of the **18th BRICS Summit** in New Delhi. They reviewed a **“steady improvement”** in ties, urged a **long-term strategic approach**, and stressed that **peace and tranquillity along the border remain essential**. Their previous meeting was at **Tianjin in August 2025**.',
         'Use it for “nature of relations”: **competition with managed cooperation**. The border stays the hinge on which the rest of the relationship swings.',
         '**BRICS** gives a venue where India and China meet without bilateral formality. India has **not joined the BRI** (2013).',
         flag='Only the intro of this report was readable (paywall). Verify details in a full news report before quoting beyond the three lines above.',
         src='web: United News of India, 12 Sep 2026.'),
]

LIVE['India-China: areas of divergence and the border'] = [
    live_head('the border, as of August 2026'),
    live(AUG, '25th Special Representatives talks: an eight-point consensus',
         'The 25th round of **SR talks** on the boundary question produced **eight points**: **two additional military meeting points and two hotlines**; an **Expert Group on Boundary Delimitation** and a **Working Group on Border Management**, both under the **WMCC**; **reopening of Lipulekh, Shipki La and Nathu La** border trade points and **more Kailash Mansarovar Yatra batches**; and a pledge to advance settlement talks on the **2005 Agreement on Political Parameters and Guiding Principles**.',
         'The word to use is **“architecture”**: hotlines, groups and trade points are confidence-building, but they do not draw a line. Still unresolved: **no mutually agreed LAC**, **Arunachal** (renaming of places, stapled visas), **CPEC through PoK**, and tri-junctions like **Doklam** near the **Siliguri Corridor**.',
         '**SR mechanism**: 2003. **WMCC**: 2012. **2005** Political Parameters. **1993** Peace and Tranquillity Agreement; **2020 Moscow 5-Point Statement**; **October 2024 Patrolling Agreement**. Passes: **Shipki La** (HP); **Mana, Niti, Lipulekh** (Uttarakhand); **Nathu La, Jelep La** (Sikkim); **Bum La** (Arunachal).',
         'Which two new bodies sit under the WMCC, and what does each do?',
         'An Expert Group on Boundary Delimitation (works on the line) and a Working Group on Border Management (works on the ground: patrols, contact, protocols).',
         why_label='What was agreed', src='Aug 2026 CA §3.4 (India-China boundary).'),
]

LIVE['India-China: four issue boxes'] = [
    live_head('water, rare earths and the Necklace in today’s news'),
    live(AUG, 'Rivers: the Brahmaputra dam, expired MoUs, and a treaty ticking down',
         'China controls the **upstream Brahmaputra, Sutlej and Indus** and is building **one of the largest hydropower projects** on the Brahmaputra. India and China have **no water-sharing treaty**: past MoUs **expired**. In **2017, during Doklam, China halted hydrological data sharing**. Closer to home, the **1996 Ganges (Farakka) Treaty** with Bangladesh **expires in December 2026**; the **Indus Waters Treaty** is **in abeyance** after the Pahalgam attack.',
         'The 2026 PYQ (“Water resources are both an asset and a source of conflict in South Asia”) is the template: upstream dominance, data as a weapon, treaties that lapse. Fix: updated agreements, joint data platforms, and **basin-wide management**.',
         '**Farakka**: sharing in the lean season, measured at Farakka (West Bengal), **Joint Rivers Commission**. **Teesta** talks blocked in 2011 by West Bengal. **Pancheshwar** (Mahakali Treaty 1996) unsettled. **UN Water Convention (1992)**: India not a signatory; **Bangladesh acceded in 2025**.',
         'Why is the December 2026 date important for India-Bangladesh ties?',
         'The 30-year Ganges Water Sharing (Farakka) Treaty of 1996 expires then, so renewal or replacement talks are due. Teesta remains the unresolved sister file.',
         src='Aug 2026 CA §3.6 (transboundary water).'),
    live(JUL, 'Diversifying from one supplier: the rare-earth and critical-minerals map',
         'India signed a **critical minerals and rare earth magnets** MoU in **Indonesia**, announced an **India-Australia Critical Minerals Corridor** and agreed with Japan to work on **semiconductors and critical minerals** under an economic-security declaration.',
         'Answer the “rare-earth magnets” box with the response, not only the problem: **three corridors away from China** (Australia, Japan, Indonesia). Honest caveat: Australia’s corridor has **no mine-to-market projects yet**.',
         'Australia holds the world’s **largest uranium resources** (Kazakhstan produces the most) and is the **largest lithium producer**.',
         src='Jul 2026 CA §3.1, §3.2, §3.4.'),
    live(JUL, 'String of Pearls versus Diamond Necklace: Sabang is back',
         'India and Indonesia agreed to **revive the joint development of Sabang port (Aceh)**, and Indonesia will post a liaison officer at India’s **IFC-IOR**. India now has partners at **both ends of the Malacca Strait**. The agreement was first reached in **2018** and stalled for eight years.',
         'The Necklace in real time: Chabahar, Duqm, **Sabang**. The Pearls keep growing too; the difference is in the rules. Keep one line ready: **“announcements are cheap, delivery is the proof.”**',
         '**Sabang** on Weh Island, Aceh. Malacca: the world’s busiest trade route by cargo volume (CA).',
         src='Jul 2026 CA §3.4.'),
]

LIVE['India-China: way forward and the Three Mutuals'] = [
    live_head('functional cooperation, restarted'),
    live_quick('Aug 2026', [
        '**Kailash Mansarovar Yatra:** more pilgrim batches agreed at the 25th SR talks.',
        '**Border trade:** Lipulekh, Shipki La and Nathu La trade points to reopen.',
        '**Rivers:** an Expert-Level Mechanism on vital resources (rivers) is part of the way forward the CA lists, alongside pilgrimages and trade.',
        '**Border management:** keep up the **Vibrant Villages Programme**, border roads and **ITBP** capacity while talking.',
    ], src='Aug 2026 CA §3.4 (way forward).'),
]

# ------------------------------------------------------------------ India-US
LIVE['India-US: nature and evolution'] = [
    live_head('the relationship by the numbers'),
    live(AUG, 'A US$239 billion relationship with a tariff problem',
         'Bilateral trade was **US$239 bn in FY25**, with an **Indian surplus**. The US is India’s **first export destination** and **fourth import source**, and the **third largest investor** (cumulative FDI **US$77.27 bn**, 2000-2025). Then came the tariff chain: **25% + 25% = 50%**, an **interim framework in February 2026**, **18%** today.',
         'Use the numbers to open an “India-US relations” answer: a big, balanced-looking relationship that is **politically more fragile than its trade figures**. The Parliamentary Standing Committee on Commerce has now reported on it.',
         '**Mission 500**: double trade to US$500 bn by 2030. **Trade Policy Forum**: 2005. Modi quote used in the CA: India “had successfully overcome its hesitations of history to forge a resilient partnership with the United States”.',
         src='Aug 2026 CA §3.3.'),
]

LIVE['India-US: areas of convergence'] = [
    live_head('convergence, still alive'),
    live(AUG + ' + ' + JUL, 'Friend-shoring, minerals and technology keep the partnership moving',
         'The committee wants India to use **friend-shoring** to slot into US supply chains in **semiconductors and electronics**. India is in the **Minerals Security Partnership (2023)** and three **IPEF** pillars (Supply Chains, Clean Economy, Fair Economy), with **TRUST** one of India’s three technology-trust frameworks (PACTS is the third).',
         'Convergence is now **supply chains and technology**, not only defence. Mention that the same technology-trust template was then repeated with the UK and Australia.',
         '**IPEF**: 14 members, launched 2022. India is an **observer in the Trade pillar**.',
         src='Aug 2026 CA §3.3; Jul 2026 CA §3.1.'),
]

LIVE['India-US: areas of divergence'] = [
    live_head('divergence, as the parliamentary committee lists it'),
    live(AUG, 'Where it hurts: the committee’s list of frictions',
         '**Rising and unpredictable tariffs** (18% against a 3% norm; frequent changes, earlier penalties). **Non-tariff barriers:** strict **SPS** standards and **MRL** limits on farm exports; heavy customs paperwork and audits. **Macro limits:** rupee volatility; **MSMEs** with thin buffers. The visa change (fixed stay for F, J, I visas) adds a people-to-people friction.',
         'Group frictions as **price (tariffs), paperwork (NTBs), people (visas)** and then add the **Russia factor** (the 25% oil penalty) from the notes. This gives a clean three-plus-one structure.',
         '**SPS**: sanitary and phytosanitary. **MRL**: Maximum Residue Limit. **Rules of origin** and **MRAs** (mutual recognition agreements) are the usual remedies.',
         'Name the three kinds of friction (price, paperwork, people) with one live example each.',
         'Price: 18% tariffs. Paperwork: SPS/MRL and customs audits. People: the new fixed-stay rule for F, J, I visas.',
         src='Aug 2026 CA §3.3; Jul 2026 CA §3.9.4.'),
]

LIVE['India-US: how India manages the relationship'] = [
    live_head('the committee’s recipe, and India’s wider answer'),
    live(AUG + ' + ' + JUL, 'Manage the US by diversifying around it',
         'The committee’s fixes: conclude the **Bilateral Trade Agreement**, a time-bound **Mission 500 roadmap**, **mutual recognition agreements**, a **US pre-clearance protocol** for farm exports, MSME support, and **diversifying** towards Europe, the Gulf, Africa, Latin America, ASEAN and Japan. India has been doing exactly that: **UK CETA** in force, **New Zealand FTA** (April 2026), **SACU PTA** talks, **Israel BIA** in force.',
         'The strongest management line: **“India’s answer to a tariff shock is more trade partners, not fewer.”** Pair the committee’s “trade partners” list with the deals actually signed.',
         '**PTA vs FTA**: PTA positive list, FTA negative list. **UK CETA**: UK removes duty on 99% of lines; India opens ~90%.',
         src='Aug 2026 CA §3.3; Jul 2026 CA §3.5, §3.6; Aug 2026 CA §3.8.3.'),
]

# ------------------------------------------------------------------ India-Russia
LIVE['India-Russia: nature, evolution and convergence'] = [
    live_head('the oldest partnership, still at work'),
    live(JUL + ' + ' + AUG, 'BrahMos, the Arctic and the Chennai-Vladivostok route',
         '**BrahMos**, an India-Russia joint venture, has now won a **second Southeast Asian customer** (Indonesia, after the Philippines). In the Arctic, the **Northern Sea Route can complement the Chennai-Vladivostok corridor** and Russia holds over 40% of the Arctic.',
         'Show that the partnership has **moved from buying Russian arms to making and exporting jointly**. That is a better Mains point than repeating “defence dependence”.',
         '**BrahMos**: supersonic cruise missile; JV; first export Philippines.',
         src='Jul 2026 CA §3.4; Aug 2026 CA §3.1.'),
]

LIVE['India-Russia: divergence, the triangle and way forward'] = [
    live_head('the triangle, tested'),
    live(AUG + ' + ' + JUL, 'The Russian-oil penalty and a table of awkward friends',
         'The extra **25% US tariff** was imposed **citing India’s Russian oil purchases**. Meanwhile **Japan sanctions Russia while India keeps defence and energy ties**, and **Australia** (AUKUS) notes the same divergence. An Odesa strike on a merchant ship killed **four Indians**.',
         'Triangle in one sentence: **India pays a price in Washington for ties with Moscow, and a price in Moscow-adjacent places (Odesa) for being in the same neighbourhood as the war.** Close with the fix: diversify oil and arms sources, keep the relationship transparent, and sell the logic as **strategic autonomy**.',
         '**OPEC+** includes Russia (and Oman, Kazakhstan, Mexico); India is not an OPEC member. **UAE left OPEC in May 2026.**',
         'Which US measure was explicitly tied to India’s Russian oil purchases?',
         'The additional 25% tariff that took the total additional duty to 50% (later cut to 18% by the February 2026 interim framework).',
         src='Aug 2026 CA §3.3, §3.8.2; Jul 2026 CA §3.1, §3.2, conflict areas.'),
]

# ------------------------------------------------------------------ others
LIVE['India-European Union'] = [
    live_head('Europe in the news'),
    live(AUG, 'Iceland says no to restarting EU talks, and a refresher on how one joins',
         'Icelandic voters **rejected restarting negotiations** to join the EU. The EU has **27 members**; the **latest member is Croatia (2013)**; the **only exit was the UK (Brexit, 2020)**. Joining runs through **Article 49** (TEU), the **Copenhagen Criteria** (stable democracy, functioning market economy, capacity to apply EU law) and an **accession treaty** needing unanimity and ratification by all.',
         'Use it for “EU as a partner”: an EU that is **hard to join, hard to leave, but wide in influence**. For India that means negotiating with a bloc that moves by consensus, which explains why FTA talks take years.',
         '**Schengen**: 25 of the 27 EU states; **Ireland and Cyprus** are EU but not Schengen. PYQ (2026): which of Belarus, Poland, Germany, Switzerland are EU members? (Answer: **Poland and Germany**, option c.)',
         'Name the Treaty article and the criteria for joining the EU.',
         'Article 49 of the Treaty on European Union; Copenhagen Criteria: stable democratic institutions, a functioning market economy, capacity to implement EU law.',
         src='Aug 2026 CA §3.8.1.'),
    live_quick('Jul-Aug 2026', [
        '**Ceuta:** migrants crossed from Morocco into the Spanish enclave of Ceuta; Spain deployed troops; at least **18 deaths**. Ceuta and Melilla are the **EU’s only land borders with Africa**.',
        '**President’s visit (July):** first visits by an Indian President to **North Macedonia** (NATO’s 30th member, March 2020; EU candidate) and **Moldova** (EU candidate; joined the ISA as its 107th member), plus **Romania** (EU and NATO member; Danube Delta UNESCO site).',
        '**Trade levers:** the Aug 2026 CA names the **India-EU FTA** alongside the **India-UK CETA** as tools to diversify exports (textiles, among others). It does not state the FTA’s current status.',
        '**UK CETA** (not the EU): the **UK’s CBAM, from 2027**, could tax Indian steel and aluminium and offset tariff gains.',
    ], src='Aug 2026 CA §3.9.1; Jul 2026 CA high-level visits, §3.6.'),
]

LIVE['India-France'] = [
    live_head('France in the news'),
    live_quick('Jul-Aug 2026', [
        '**UPI in France:** UPI is live across **11 jurisdictions** including the UAE, Singapore, **France**, Nepal, Bhutan, Cambodia, Greece and the Maldives. PYQ (2025): of UAE, France, Germany, Singapore and Bangladesh, in how many does UPI work for merchant payments? The CA’s own list shows **three** (UAE, France, Singapore): option **(b)**.',
        '**Paris, July:** the **Integrated Anti-Ballistic Missile Coalition** of ten European states was announced in Paris, with France a member.',
        '**P5:** France holds a UNSC veto; the UK also backs India’s permanent seat (CA).',
        '**Check:** the two CA issues carry no direct India-France summit item this quarter. Add one when it appears.',
    ], src='Aug 2026 CA UPI section (PYQ 2025); Jul 2026 CA §3.9.2, §3.8.3, §3.6.'),
]

LIVE['India-Japan'] = [
    live_head('Japan, July 2026'),
    live(JUL, '16th India-Japan Annual Summit: from strategic to economic security',
         'Joint Statement: **Advancing a Partnership of Strategic Convergence and Trust**. Deliverables: **Joint Declaration on Economic Security** (semiconductors, critical minerals), cooperation on **payments and local-currency transactions**, a **Joint Statement on Energy Resilience** (including **Strategic Petroleum Reserves**), the **UNICORN** defence co-development (agreement in principle), a first **AI Strategic Dialogue**, and a **human-resource action plan**: **5 lakh exchanges in 5 years**, including **50,000 skilled Indians to Japan**.',
         'Why now: both faced **US tariffs** and the **Iran conflict disrupted the Strait of Hormuz** (fuel shortages in Japan, LPG worries in India). Say it as: **“crisis converted a partnership of convenience into a partnership of resilience.”** Delivery is the test: the Indian community in Japan is about **59,000** against a target of 5 lakh.',
         '**Exercises:** Dharma Guardian (army), JIMEX (navy), Veer Guardian (air force), Malabar (multilateral). **Japan’s disputes:** Senkaku/Diaoyu (China), Northern Territories/Southern Kurils (Russia), Takeshima/Dokdo (South Korea). **2+2 dialogue due within 2026.** PYQ quoted: India-Japan “global and strategic partnership” (2019).',
         'Name three summit deliverables that respond directly to the Hormuz crisis.',
         'The Joint Statement on Energy Resilience, cooperation on Strategic Petroleum Reserves, and the Economic Security declaration (supply chains for critical minerals and semiconductors).',
         why_label='What was agreed', src='Jul 2026 CA §3.2 (16th India-Japan summit).'),
    live(AUG, 'The Kurils: Japan protests Putin’s visit',
         'Japan condemned Putin’s visit to the **Kuril Islands**. Japan claims **Etorofu** as one of its **Northern Territories**.',
         'A one-liner for “divergence on Russia”: Japan **sanctions Russia and has an unresolved territorial dispute with it**, while India keeps defence and energy ties.',
         'The Kuril chain runs from **Kamchatka** to **Hokkaido**.',
         src='Aug 2026 CA §3.9.3.'),
]

LIVE['India-Australia'] = [
    live_head('Australia, July 2026'),
    live(JUL, '3rd India-Australia Annual Summit: uranium, defence, cyber, space, minerals',
         'Outcomes: an **Administrative Arrangement** under the 2014 Civil Nuclear Cooperation Agreement (enables long-term **Australian uranium exports under IAEA safeguards**); a **Joint Declaration on Defence and Security Cooperation** upgrading the 2009 declaration plus a **Maritime Security Collaboration Roadmap**; **PACTS** (cyber, critical technologies, supply chains); a temporary **space tracking terminal on the Cocos (Keeling) Islands** for **Gaganyaan**; the **India-Australia Critical Minerals Corridor**; a skills MoU for mining in Bhubaneswar.',
         'The sentence that scores: **“the relationship is moving from the 3Cs (Commonwealth, cricket, curry) and 3Ds (democracy, diaspora, dosti) to the 3Es (energy, economy, education).”** Then name the gap: **trade is only US$24.1 bn** against China-Australia **US$212 bn**, and **CECA** is still unfinished four years after ECTA.',
         '**Quad partner**: Australia hosted **Malabar** for the first time in **2023**. **AUKUS** versus India’s multi-alignment is the strategic mismatch. **Australia**: largest uranium **resources**, but Kazakhstan the largest **producer**; **largest lithium producer**. **Deakin and Wollongong** opened India’s first foreign university campuses at **GIFT City**.',
         'Why does India need the Cocos (Keeling) terminal?',
         'To track and receive telemetry from India’s Gaganyaan human spaceflight mission. It is also a trust signal: Indian space infrastructure on Australian territory.',
         why_label='What was agreed', src='Jul 2026 CA §3.1 (3rd India-Australia Annual Summit).'),
]

# ------------------------------------------------------------------ radar section
RADAR_ROWS = [
    ['Aug 2026', '25th SR talks: eight-point consensus (hotlines, expert group, trade points, Kailash Yatra)', 'India-China', 'Border architecture without a line'],
    ['12 Sep 2026', 'Modi-Xi meeting in New Delhi (BRICS sidelines)', 'India-China', 'Managed cooperation'],
    ['Aug 2026', 'Scarborough Shoal: China reserve rules; Philippines chart at the UN', 'US-China · India-China', 'UNCLOS 121(3), 16; 2016 award'],
    ['Aug 2026', 'Transboundary water: Farakka treaty expires Dec 2026; IWT in abeyance; Brahmaputra dam', 'India-China · neighbours', 'Water PYQ 2026'],
    ['Aug 2026', 'India-US: committee report; 50% to 18%; Mission 500', 'India-US', 'Tariffs, NTBs, BTA, friend-shoring'],
    ['Aug 2026', 'MJDA (Saudi, Türkiye, Pakistan)', 'India’s approach', 'Hedging vs balancing; mandala'],
    ['Aug 2026', 'Kurils, OPEC+, UAE leaves OPEC', 'Russia', 'Disputed land; energy blocs'],
    ['Aug 2026', 'Iceland rejects EU talks; Ceuta crisis; Schengen refresher', 'EU', 'Article 49; Copenhagen; 25 of 27'],
    ['Jul 2026', 'Europe’s ten-nation missile coalition; Nord Stream; Odesa strike', 'Russia-West', 'Confrontation, energy, seafarers'],
    ['Jul 2026', '16th India-Japan summit', 'India-Japan', 'Economic security; UNICORN; 2+2'],
    ['Jul 2026', '3rd India-Australia summit', 'India-Australia', 'Uranium; PACTS; Cocos terminal; CECA gap'],
    ['Jul 2026', 'India-Indonesia (BrahMos, Sabang), India-NZ, India-UK CETA', 'Instruments · India-China (Necklace)', 'Defence exports; trade diversification'],
]

WATCH = [
    '**Farakka Treaty (Dec 2026):** renewal, or a new India-Bangladesh water framework?',
    '**India-US BTA:** does the interim 18% framework become a full agreement?',
    '**Hormuz:** does the strait reopen, and under what route rules (Sep 2026: routes agreed, strait not yet open)?',
    '**India-China:** do the new expert group, working group and hotlines start working; do the border trade points reopen?',
    '**Scarborough Shoal:** more rules, more charts, more patrols; an ASEAN-China Code of Conduct remains the real fix.',
    '**India-Japan 2+2 (within 2026)** and **UNICORN** details.',
    '**MJDA:** does Bangladesh join; does a text appear?',
    '**UK CBAM (2027)** on Indian steel and aluminium.',
]

CHAIN = [
    ('The US raises the price of partnership', 'Tariffs on India: 50%, then 18% (Feb 2026).'),
    ('India widens its table', 'Summits with Japan, Australia, Indonesia; UK and NZ deals; SACU talks; Modi-Xi meeting.'),
    ('China tests the edges', 'Reserve rules at Scarborough; a Brahmaputra mega-dam; but also an eight-point border consensus.'),
    ('Russia’s war keeps spilling over', 'Odesa strike kills four Indians; Nord Stream blame; Kuril visit angers Japan.'),
    ('Rivals hedge too', 'MJDA, Europe’s missile coalition, UAE leaves OPEC.'),
]


def radar():
    return [
        p('The newsroom for Chapter 2. Every item comes from the **July and August 2026 current-affairs magazines** in your Project (web items are marked). Read the table once a week, then retell the chain from memory.'),
        tbl('What happened, and where it plugs into this chapter', ['When', 'News', 'Plugs into', 'Exam angle'], RADAR_ROWS),
        h3('Connect the dots: one story from the headlines'),
        flow('Five headlines, one argument', CHAIN),
        p('**Write it as a 4-line answer opener:** “India is being priced by one great power, probed by another and caught in the spillover of a third’s war. Its answer is not a camp but a wider table: new trade partners, new technology pacts, a thawing but guarded border, and a seat for itself wherever rules are written.”'),
        h3('Watch next (status can change before your exam)'),
        '<ul class="watch-list">' + ''.join('<li>%s</li>' % inline(x) for x in WATCH) + '</ul>',
        callout('note', 'How to keep this section fresh', 'Every month, add the new magazine’s International Relations items here and file each one under the section it feeds. The test for any headline: **which bilateral relationship, which rivalry, which instrument does it prove?**'),
    ]


MCQ = [
    ('The 2016 UNCLOS arbitral tribunal held Scarborough Shoal to be a “rock” under which Article?',
     ['Article 16', 'Article 121(3)', 'Article 123', 'Article 76'], 1,
     'Article 121(3): rocks that cannot sustain human habitation or economic life of their own have no EEZ or continental shelf. Article 16 is about depositing charts with the UN; Article 123 is cooperation in enclosed or semi-enclosed seas.'),
    ('The Philippines deposited its Scarborough Shoal chart with the UN under which UNCLOS provision?',
     ['Article 16', 'Article 121(3)', 'Article 123', 'Article 15'], 0,
     'Article 16 requires due publicity and deposit of baseline charts with the UN Secretary-General.'),
    ('The 25th round of India-China Special Representatives talks produced which of these?',
     ['A final boundary treaty', 'An Expert Group on Boundary Delimitation and a Working Group on Border Management under the WMCC', 'India joining the BRI', 'Withdrawal of China’s claim on Arunachal'],
     1,
     'Eight-point consensus: two more military meeting points and hotlines, the two WMCC bodies, reopening of Lipulekh, Shipki La and Nathu La trade points, more Kailash Mansarovar batches, and a reaffirmed 2005 Agreement.'),
    ('The India-Bangladesh Ganges Water Sharing (Farakka) Treaty, signed in 1996 for 30 years, expires in:',
     ['December 2025', 'December 2026', 'June 2027', 'It has no expiry date'], 1,
     'It was signed in 1996 for 30 years and expires in December 2026 (Aug 2026 CA). Sharing is measured at Farakka; the Joint Rivers Commission handles issues.'),
    ('PYQ 2016 (quoted in the Aug 2026 CA): “Belt and Road Initiative” is sometimes in the news in the context of the affairs of:',
     ['African Union', 'Brazil', 'European Union', 'China'], 3,
     'BRI is China’s flagship global infrastructure and connectivity initiative, launched in 2013. India has not joined it; CPEC, its flagship project, passes through PoK.'),
    ('PYQ 2026 (quoted in the Aug 2026 CA). Which of Belarus, Poland, Germany, Switzerland are members of the EU? Select: (a) 1, 2, 4 (b) 1, 4 only (c) 2 and 3 (d) 2 and 4 only',
     ['1, 2 and 4', '1 and 4 only', '2 and 3', '2 and 4 only'], 2,
     'The EU has 27 members; Poland and Germany are members. Belarus and Switzerland are not. Answer (c). For the Schengen area, 25 of 27 members take part (not Ireland, Cyprus).'),
    ('The additional 25% US tariff on India in 2025 was linked to:',
     ['India’s rice exports', 'India’s Russian oil purchases', 'India’s digital taxes', 'India’s BRICS membership'], 1,
     'It raised the total additional duty to 50%. The February 2026 interim framework cut it to 18%.'),
    ('PYQ 2015 (quoted in the Jul 2026 CA). India is a member of which among APEC, ASEAN and East Asia Summit?',
     ['APEC and ASEAN only', 'East Asia Summit only', 'All three', 'None of them'], 1,
     'India is in the EAS (since 2005, 19 members). It is not a member of ASEAN (the ASEAN-India CSP dates from 2022) or APEC. Answer (b).'),
    ('India-Australia: which statement is correct?',
     ['Australia is the world’s largest uranium producer', 'Australia is the largest uranium resource holder; Kazakhstan is the largest producer', 'India-Australia trade exceeds China-Australia trade', 'CECA was signed in 2022'], 1,
     'Australia holds the world’s largest uranium resources, but Kazakhstan produces the most. India-Australia trade is US$24.1 bn against China-Australia US$212 bn; CECA is still unconcluded.'),
    ('The 16th India-Japan summit’s human-resource plan envisages exchange of how many people over five years?',
     ['50,000', '1 lakh', '5 lakh', '10 lakh'], 2,
     '5 lakh personnel in 5 years, including 50,000 skilled workers from India to Japan. The Indian community in Japan is about 59,000.'),
]

CARDS = [
    ('Live: what did the 25th India-China SR talks agree?', 'Eight-point consensus: two military meeting points + two hotlines; Expert Group on Boundary Delimitation and Working Group on Border Management (under WMCC); reopen Lipulekh, Shipki La, Nathu La trade; more Kailash Yatra batches; 2005 Agreement reaffirmed.'),
    ('Live: when did Modi and Xi last meet?', '12 Sep 2026 in New Delhi on the BRICS summit sidelines; before that, Tianjin, Aug 2025. Both stressed peace and tranquillity on the border.'),
    ('Live: three things to say about Scarborough Shoal.', '2016 award: it is a rock (Art. 121(3)), no EEZ, no historic rights. Philippines chart at UN (Art. 16). China’s 2026 nature-reserve rules (Huangyan Dao).'),
    ('Live: why is the SCS vital to India?', 'Over 55% of India’s trade passes SCS and Malacca; ONGC Videsh Block 128 off Vietnam; BrahMos to the Philippines.'),
    ('Live: which water deadlines matter in 2026?', 'Farakka treaty (1996, 30 years) expires Dec 2026. Indus Waters Treaty in abeyance. India-China water MoUs expired; China building a mega-dam on the Brahmaputra.'),
    ('Live: India-US trade facts?', 'US$239 bn FY25, Indian surplus. US: 1st export market, 4th import source, 3rd investor (US$77.27 bn FDI 2000-2025). Mission 500 by 2030.'),
    ('Live: list the committee’s India-US frictions.', 'Tariffs (18% vs 3%), NTBs (SPS, MRL, customs), currency volatility, MSME vulnerability.'),
    ('Live: how does the committee want India to respond?', 'BTA, Mission 500 roadmap, MRAs, pre-clearance protocol, MSME support, diversify (Europe, Gulf, Africa, Latin America, ASEAN, Japan), friend-shoring.'),
    ('Live: Japan summit, five deliverables?', 'Economic Security declaration, energy resilience (SPR), UNICORN, AI Strategic Dialogue, 5 lakh HR exchange (50,000 skilled Indians).'),
    ('Live: Australia summit, five deliverables?', 'Civil nuclear arrangement (uranium), defence declaration + MSCR, PACTS, Cocos tracking terminal for Gaganyaan, Critical Minerals Corridor.'),
    ('Live: how is Iceland-EU news useful?', 'Iceland voters rejected restarting EU talks. Article 49; Copenhagen Criteria; accession needs unanimity + ratification. Schengen: 25 of 27 (not Ireland, Cyprus).'),
    ('Live: three Russia-linked incidents of summer 2026?', 'Nord Stream blame (Ukrainian state authorities per German prosecutors), Odesa strike (4 Indians dead), Putin’s Kuril visit (Japan protested).'),
]
