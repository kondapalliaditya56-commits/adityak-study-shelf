# -*- coding: utf-8 -*-
"""Chapter 3: India's neighbourhood. Source: PPT-4 Neighbourhood, handout Ch 3 pp. 1-27 (+ merged handout); CA Jul/Aug 2026."""
from dsl import *
from hwlib import P, H, R

CA = lambda t, src: bx('ca', '<span class="tag">In the news · %s</span>%s' % (src, t))
IMG = lambda src, cap, h=58: bx('figw', '<img src="../../img/%s" style="max-height:%dmm;max-width:100%%;display:block;margin:1mm auto;border:1.4px solid #1a237e;border-radius:3px"><div class="cap" style="text-align:center">%s</div>' % (src, h, cap))
PH = lambda t: bx('pk', '<b>Slide phrase:</b> ' + t)

CHS = [
dict(toc='India’s neighbourhood', id=3, title='INDIA\'S NEIGHBOURHOOD', part=1, icon='shield',
 pyq='Mains 2024 Maldives · 2022 Sri Lanka · 2015 Mausam · 2015 India-Pak soft power',
 simple='Geography ties India to its neighbours for ever. Politics and security decide whether that closeness brings cooperation or friction.',
 pages='PPT-4 Neighbourhood · handout pp. 1-27', prio='H',
 nodes=[
 two([IMG('ir-nb-map.jpg', 'India and its neighbours (handout p. 1, slide 3)', 62)],
     [t('<b>India\'s interests</b> (slide 4)', '<b>Security:</b> terror (Pak), insurgency (Myanmar), Afghan instability', '<b>Trade, connectivity:</b> B\'desh → NE; Myanmar → SE Asia (Kaladan, Trilateral Highway)', '<b>Energy:</b> Bhutan, Nepal hydropower', '<b>External influence:</b> China', '<b>People:</b> open border, Buddhism', '<b>Stability:</b> disasters, sea lanes', w=20)]),
 bx('pk', '<b>Slide 4:</b> "Neighbourhood First prioritises <b>physical, digital and people-to-people connectivity, trade and commerce</b>." &nbsp;<b>Slide 5:</b> "<b>Geography creates permanent interdependence, but politics and security determine whether it produces cooperation or friction.</b>"'),
 hub('8 CHALLENGES (slide 5)', ['Political instability', 'Security threats', 'China\'s presence: CPEC, Hambantota, Kyaukpyu', 'Trust deficit: "Big Brother", India Out', 'Weak integration: SAARC stuck', 'Domestic politics: Teesta', 'Refugees from Myanmar', 'Climate: 54 shared rivers']),
 t('<b>Way forward</b> (slide 6)', 'Respect sovereignty: <b>equal partners</b>', 'Security cooperation; <b>Vibrant Villages</b> for border communities', '<b>Project delivery</b> = credibility', 'Economic integration: border haats, Nepal-B\'desh power via India; BBIN, BIMSTEC', 'Climate data-sharing; <b>people-centric diplomacy</b> that survives regime change', w=22),
 bx('gr', '<b>Closing line (slide 6):</b> combine the <b>Gujral Doctrine (1996)</b> (non-reciprocity, non-interference, sovereignty, peaceful settlement) with Neighbourhood First → <b>trust rather than dependence</b>.'),
 tl(('Pre-1947', 'imperial buffers'), ('1947-49', 'Partition'), ('1950s-60s', 'NAM, Panchsheel'), ('1962-65', 'security recalibration'), ('1970s-80s', '1971, SAARC 1985, Cactus 1988'), ('1991-96', 'Look East, Gujral'), ('1997-2013', 'BIMSTEC, IORA 1997'), ('2014-', 'Neighbourhood First')),
 bx('ye', '<b>PYQ Lab note:</b> only 4 of 40 IR questions (2017-26) named a neighbour, each after a crisis next door. Prepare <b>themes</b> (crisis response, connectivity, water, China factor) with countries as examples.'),

 sec('PAKISTAN: "STRUCTURAL RIVALRY" ' + P('2015 soft power'), 'r'),
 PH('<b>Credible deterrence + escalation control + limited functional engagement</b> (slide 8).'),
 tl(('1947-65', 'Kashmir wars; IWT 1960; Tashkent'), ('1971-84', 'Shimla 1972; Meghdoot 1984'), ('1998-2007', 'nukes; Lahore, Kargil, 2003 ceasefire'), ('2008-14', 'Mumbai'), ('2014-19', 'Uri → surgical strikes; Pulwama → Balakot'), ('2021', 'ceasefire renewed'), ('2025-26', 'Pahalgam, Op Sindoor, IWT abeyance')),
 two([t('<b>Still open</b>', '2003 ceasefire, <b>DGMO</b> line; May 2025 stop-firing', '<b>1988 pact:</b> nuclear-site lists every year', '2008 consular pact: prisoner lists twice a year', '<b>1974 Shrines Protocol</b>; <b>Kartarpur 2019</b> (suspended 2025)', 'SCO (Islamabad CHG 2024); SAARC stuck', w=18)],
     [t('<b>Divergence</b>', 'Terror: LeT, JeM; drones, cyber', 'J&amp;K integral; <b>no third-party mediation</b> (Shimla)', 'Siachen: authenticate <b>AGPL</b>; <b>Sir Creek</b>', 'CPEC via PoK; two-front', 'IWT in abeyance (Apr 2025); Attari ICP closed', '<b>Stability-instability paradox</b>', w=18)]),
 two([IMG('ir-nb-sir-creek.jpg', 'Sir Creek (handout p. 5)', 48)], [IMG('ir-nb-iwt.jpg', 'IWT 1960 graphic (handout p. 5)', 48)]),
 bx('ye', '<b>IWT (19 Sep 1960, World Bank):</b> <b>Western</b> = Indus, Jhelum, Chenab → Pakistan; India limited use (run-of-river). <b>Eastern</b> = Ravi, Beas, Sutlej → India. Commission meets once a year. Disputes: Kishanganga, Ratle.'),
 bx('gr', '<b>Close:</b> deterrence with escalation control now; humanitarian channels (fishermen, prisoners, pilgrims) insulated; <b>durable peace needs a terror-free environment</b>.'),

 sec('AFGHANISTAN: "ENGAGEMENT WITHOUT ENDORSEMENT"', 'b'),
 tl(('to 1950', 'Gandhara; 1950 Treaty'), ('1979-2001', 'no Taliban recognition; Northern Alliance'), ('2001-14', 'development; 2011 SPA'), ('2015-16', 'Parliament, Salma Dam, Zaranj-Delaram'), ('2021', 'Op Devi Shakti'), ('2022-25', 'Technical Mission, Kabul')),
 two([t('<b>Convergence</b>', 'High Impact Community Projects; people-centric not regime-centric', 'Trade ~$907.85 mn (FY26); <b>Chabahar</b> bypasses Pak; Shahid Beheshti 2024 deal', '<b>UNSC Res 2593</b>: Afghan soil not against others', 'Cricket, Kabuliwala, scholarships', w=18)],
     [t('<b>Divergence</b>', 'No recognition; women\'s rights; minorities', 'ISIL-K, Al-Qaeda, LeT/JeM; <b>Death Crescent</b> opiates', 'No land route; Iran sanctions hit Chabahar', 'China: <b>Mes Aynak</b> copper', w=18)]),
 IMG('ir-nb-afghan-routes.jpg', 'Chabahar → Zaranj-Delaram → Ring Road (handout p. 8)', 46),
 bx('gr', '<b>Close (slide 17):</b> <b>engagement without recognition, people-level goodwill, counter-terrorism and connectivity</b>; small, locally maintainable projects.'),

 sec('BANGLADESH: "STRATEGIC RESET"', 'g'),
 bx('bl', 'From "<b>Sonali Adhyay</b>" to reset. <b>Longest land border 4,096 km</b>; link to the Northeast; Bay of Bengal security.'),
 tl(('1971-72', 'Liberation; Friendship Treaty'), ('1975-2008', 'distrust; <b>Ganga Treaty 1996</b>'), ('2009-14', 'Hasina: anti-insurgency'), ('2014-15', 'maritime award; <b>LBA 2015</b>'), ('2021-23', 'Kushiyara; Akhaura-Agartala; pipeline'), ('2024', 'Hasina exits'), ('2025-26', 'reset')),
 two([t('<b>Convergence</b>', 'Biggest S. Asian trade partner: <b>$14.01 bn</b> (FY24)', 'Chattogram, Mongla transit; <b>40 MW Nepal power</b> via India (Nov 2024); diesel pipeline 1 MMT/yr', 'Ganga 1996; <b>Kushiyara 153 cusecs</b>; 54 rivers (JRC)', '<b>LBA: 111 + 51 enclaves</b>; SAMPRITI', w=18)],
     [t('<b>Divergence</b>', 'Hasina extradition request renewed (Aug 2026); minorities; Rohingya', '<b>Teesta</b> unsettled (draft 2011); <b>Ganga Treaty expires Dec 2026</b>', '864 km unfenced; border deaths', '2025 import, land-port curbs; trans-shipment withdrawn (Apr 2025)', 'China: submarine facility', w=18)]),
 bx('gr', '<b>Fix:</b> time-bound Teesta talks <b>with West Bengal</b>; post-2026 Ganga deal; CEPA; clear notice before trade curbs; BBIN energy. <b>Geography, rivers, security stay permanent.</b>'),

 sec('NEPAL: "ROTI-BETI &amp; OPEN BORDER"', 'b'),
 PH('civilisational, people-centred; <b>HIT formula</b> = Highways, I-ways, Trans-ways. Closeness also breeds mistrust.'),
 tl(('1816 / 1950', 'Sugauli; 1950 Treaty'), ('1989', 'trade-transit crisis'), ('1996', 'Mahakali'), ('2015', 'Op Maitri; Madhesi "blockade"'), ('2020', 'new map'), ('2024-25', '10,000 MW pact'), ('2025-26', 'youth-led change')),
 two([t('<b>Convergence</b>', 'Largest partner: <b>$9.39 bn</b>; 82%+ of Nepal\'s exports; UPI-NPI', 'Jaynagar-Bijalpura rail; ICPs; <b>Motihari-Amlekhgunj</b> pipeline', '<b>10,000 MW</b> export deal; <b>Arun-III 900 MW</b>', 'Koshi 1954, Gandak 1959, Mahakali 1996', 'Surya Kiran; Gorkha regiments; GLOF relief 130 t+', w=18)],
     [t('<b>Divergence</b>', '<b>Kalapani, Lipulekh, Limpiyadhura</b> (2020 map)', '1950 Treaty "unequal"; EPG 2018 report pending', '<b>Agnipath</b> vs 1947 Tripartite pact', 'BRI framework (Dec 2024)', 'Pancheshwar DPR stuck', w=18)]),
 bx('gr', '<b>Fix:</b> review 1950 Treaty; evidence-based boundary talks (B\'desh LBA as model); <b>smart open border</b>; <b>Track-II</b>; respect Nepal\'s balancing.'),

 sec('BHUTAN: "BHARAT FOR BHUTAN, BHUTAN FOR BHARAT"', 'g'),
 two([t('<b>Story</b>', '1949 Treaty → <b>Op All Clear 2003</b> → <b>2007 Treaty</b> (more autonomy) → <b>Doklam 2017</b> (Siliguri) → diversification', 'Trade ₹12,669 cr (2024); 55%+ of FDI; 2016 trade-transit pact', '<b>₹10,000 cr</b> for 13th Plan (2024-29)', '5 hydro projects <b>3,156 MW</b>; Punatsangchhu-II 1,020 MW (2025); ₹4,000-cr LoC (Jul 2026)', 'IMTRAT; RuPay, UPI QR; India-Bhutan satellite 2022; first <b>Vaccine Maitri</b> country', w=18)],
     [IMG('ir-nb-gelephu.jpg', 'Gelephu Mindfulness City, near Assam', 52),
      t('<b>Issues</b>', 'Bhutan-China talks near Doklam', 'BBIN MVA not ratified', 'Punatsangchhu-I delays; 60-70% loans', 'India ~80% of trade', '2013 LPG subsidy row', w=16)]),
 bx('gr', '<b>Close:</b> move <b>beyond hydropower</b>; Kokrajhar-Gelephu &amp; Banarhat-Samtse rail; sovereignty-first consultation on Doklam.'),

 sec('MYANMAR: "CALIBRATED ENGAGEMENT"', 'r'),
 PH('Myanmar tests India\'s ability to <b>balance values, security and connectivity</b> (slide 33). Not whether to engage, but with whom.'),
 two([t('<b>Convergence</b>', 'Trade <b>$2.15 bn</b> (2024-25); Rupee-Kyat (May 2024)', '<b>Kaladan</b>: Kolkata-Sittwe-Mizoram; Trilateral Highway; BIMSTEC, MGC', '<b>Op Brahma</b> (Mar 2025 quake)', 'Ananda Temple, Bagan; 2 mn of Indian origin', w=18)],
     [t('<b>Divergence</b>', '<b>1,643 km</b> border; Death Triangle; FMR curbs opposed in Mizoram, Naga areas', 'Post-2021 refugees; Rakhine, Rohingya', 'China: <b>Kyaukphyu</b> port', 'Sittwe got first cargo 2023, corridor unfinished', 'values vs national interest', w=18)]),

 sec('SRI LANKA ' + P('2022'), 'b'),
 two([t('<b>Story</b>', 'Sirimavo-Shastri Pact → 1987 Accord, IPKF → post-2009 reconciliation', '<b>2022 crisis: ~US$4 bn</b>; co-chaired Official Creditor Committee', '2024-25: grid, LNG, UPI, ferries (Dissanayake)', 'Cyclone Ditwah → <b>Op Sagar Bandhu</b> (1,058 t+); $450 mn package', w=18)],
     [IMG('ir-nb-palk.jpg', 'Palk Strait, Gulf of Mannar', 46)]),
 two([t('<b>Convergence</b>', 'Trade <b>$7.18 bn</b> (FY26); ETCA talks', '60,000 houses; Kankesanthurai $65 mn; Nagapattinam ferry; UPI 2024', '<b>Sampur solar</b>; HVDC MoU; <b>Trincomalee energy hub</b> (with UAE)', 'Defence MoU 2025; Mitra Shakti, SLINEX; MRCC; CSC', w=18)],
     [t('<b>Divergence</b>', '<b>13th Amendment</b>; Provincial Council polls', '<b>Katchatheevu</b> (1974, 1976); bottom trawling; Delft firing 2025', 'Adani left Mannar wind', '<b>Hambantota</b>', w=18)]),
 bx('ye', '<b>Handout alert:</b> ISFTA dated 2000 (handout) vs 1998 (slide 35). Write "ISFTA" and check class notes.'),

 sec('MALDIVES: "LOCATION, NOT SIZE" ' + P('2024'), 'r'),
 tl(('1976', 'maritime boundary (slide: 1979)'), ('1988', 'Op Cactus'), ('2004-14', 'tsunami; Op Neer'), ('2016-23', 'India First'), ('2023', 'India Out'), ('2024', 'civilians; CEMSP'), ('2025-26', 'reset')),
 two([t('<b>Convergence</b>', '<b>CEMSP</b> Oct 2024; Ekuverin, Ekatha, Dosti; CSC', 'Trade $771.76 mn; FTA round 1 (Jul 2026)', 'Swap US$400 mn + ₹30 bn; RuPay; <b>Favara-UPI</b>', '<b>GMCP US$500 mn</b>; Hanimaadhoo runway', '60,000 Indians; 1,000 civil servants trained', w=18)],
     [t('<b>Divergence</b>', '"India Out" 2023-24; hydrographic pact not renewed', 'Chinese research vessel 2024; UTF Harbour suspicion', 'China-Maldives FTA (Jan 2025)', 'Lakshadweep row (Jan 2024): tourist boycott; 2 lakh+ tourists before', w=18)]),
 bx('gr', '<b>Close (slide 42):</b> combine <b>security cooperation with respect for sovereignty</b> under MAHASAGAR; clear rules for Indian assets; Project Mausam.'),
 CA('MAHASAGAR: India as "preferred security partner and first responder" (Aug CA). Favara-UPI corridor live (Jul CA). ₹4,000-cr LoC to Bhutan; Hasina extradition request renewed (handout, 2026).', 'Jul-Aug 2026'),

 sec('EIGHT NEIGHBOURS IN ONE TABLE', 'b'),
 tb(['Neighbour', 'Slide phrase', 'China footprint', 'One fix'],
    ['Pakistan', 'Structural rivalry', 'CPEC, Gwadar', 'Deterrence + humanitarian channels'],
    ['Afghanistan', 'Engagement without endorsement', 'Mes Aynak', 'Chabahar; small projects'],
    ['Bangladesh', 'Strategic reset', 'Submarine facility', 'Teesta + Ganga 2026'],
    ['Nepal', 'Roti-Beti, open border', 'BRI framework 2024', '1950 Treaty review'],
    ['Bhutan', 'B4B', 'Boundary talks', 'Beyond hydropower'],
    ['Myanmar', 'Calibrated engagement', 'Kyaukphyu', 'Finish Kaladan'],
    ['Sri Lanka', 'Crisis → connectivity', 'Hambantota', 'Fisheries framework'],
    ['Maldives', 'Location, not size', 'FTA, research vessel', 'Sovereignty-sensitive rules']),

 sec('PYQ ANSWER FRAMES', 'b'),
 tb(['PYQ', 'Approach', 'Body'],
    ['<b>2024</b> Maldives (15m)', 'Component + SWOT', 'Part 1 importance · Part 2 S/W/O/T'],
    ['<b>2022</b> Sri Lanka crisis (10m)', 'Temporal', 'old ties → 2022 $4 bn → connectivity → limits'],
    ['<b>2015</b> Project Mausam (12.5m)', 'Level analysis', 'cultural → bilateral → Indian Ocean strategy (thin notes)'],
    ['<b>2015</b> India-Pak soft power (12.5m)', 'Stakeholder', 'people, pilgrims · govts · army, terror → "goodwill follows peace"']),
 ],
 recall=[('Gujral Doctrine 4 parts?', 'Non-reciprocity, non-interference, sovereignty, peaceful settlement'), ('Pakistan frame?', 'Deterrence + escalation control + limited engagement'),
         ('IWT western rivers?', 'Indus, Jhelum, Chenab'), ('Afghan phrase?', 'Engagement without endorsement/recognition'),
         ('LBA 2015 enclaves?', '111 Indian, 51 Bangladeshi'), ('Ganga Treaty expires?', 'December 2026'),
         ('Nepal disputed areas?', 'Kalapani, Lipulekh, Limpiyadhura'), ('Bhutan core idea?', 'Bharat for Bhutan, Bhutan for Bharat'),
         ('Myanmar border length / project?', '1,643 km; Kaladan (Kolkata-Sittwe-Mizoram)'), ('Sri Lanka 2022 aid?', '~US$4 bn; creditor committee co-chair'),
         ('Maldives partnership 2024?', 'CEMSP (October 2024)')]),
]
