# -*- coding: utf-8 -*-
# Class-note additions for Polity ch13 (Local self-government) and ch14 (Judiciary: the SC).
# Source extracts: scratchpad/cn/bych/ch13.md and ch14.md. Nothing here repeats ch_11_14.py.
# Placement notes: ch14 extract entries on contempt, Art 13, High Court benches, Arts 130-146, NJPC all
# stay in ch14 (the handout chapter 15 notes cover the HC only in general, no benches/Jaswant Singh Committee).
from dsl import *
from hwlib import P
OWN = lambda w, h: mn(w, h + ' <i>(own mnemonic)</i>')

ADD = {
 13: [
  # ------------------------------------------------------------ meaning, significance, evolution
  dict(after='ORIGINAL CONSTITUTION', nodes=[
    sec('CLASS · LSG: significance and evolution', 'r'),
    bx('pk', '<b>Teacher:</b> LSG is the <b>closest and oldest</b> form of government, yet a “<b>misnomer</b>”: a 3-tier body, not a comprehensive government (State and Centre are also elected by us), so no separate “oneness” for accountability.'),
    t('<b>Significance of LSG (9)</b>',
      '<b>Grassroots democracy:</b> Nehru, “Democracy at the top cannot succeed unless it is built on a strong foundation from below”',
      '<b>School of democracy:</b> training ground for future leaders',
      'better at basic services: local interest, local knowledge',
      '<b>more economical:</b> spending is seen by locals, more vigilance',
      'relieves upper levels, who focus on broad policy',
      'two-way channel between people and higher government',
      'taps human and material resources: vital for national progress',
      'indispensable for decentralised planning',
      'real participation: direct democracy', w=24),
    tb(['Period', 'Class points'],
       ['<b>Ancient</b>', 'urban local government in Indus-Harappan cities; Vedic <b>Gramini, Granika</b> (village headman); <b>Pataliputra</b>: 30-member board in <b>6 committees of 5</b> for city administration'],
       ['<b>Cholas</b>', '<b>Uttaramerur</b> (T.N.) copper-plate inscriptions, 9th-10th c.: LSG on democratic lines; candidate age <b>35-70</b>, own house on own land, not a debtor'],
       ['<b>Medieval</b>', 'setback: invasions, heavy centralisation'],
       ['<b>British</b>', 'traces in urban LG; aims: (1) prevent disaffection among natives (2) relieve imperial finances: local problems from local resources, serve imperial interests (3) wider taste for British manufactures'],
       ['<b>Madras 1687</b>', 'first Municipal Corporation, <b>nominated members only</b> (handout dates 1688)']),
  ]),
  # ------------------------------------------------------------ CDP
  dict(after='EVOLUTION OF PANCHAYATI RAJ', nodes=[
    sec('CLASS · Community Development Programme (1952)', 'r'),
    t('<b>CDP 1952</b>', 'modelled on the USA <b>Extension Services Programme</b>; with NGO <b>Ford Foundation</b> and GoI', 'comprehensive rural development and reconstruction; <b>people’s participation</b>, not bureaucracy alone', t('<b>Block</b> = new unit of development', 'revenue units: District, Sub-division, Tehsil', 'development units: Block, Village'), w=24),
  ]),
  # ------------------------------------------------------------ committees extras
  dict(after='COMMITTEES ON PANCHAYATI RAJ', nodes=[
    sec('CLASS · Committees: extra points', 'r'),
    tb(['Committee', 'Class extras'],
       ['<b>Balwant Rai Mehta</b> (appointed by NDC, 1957)', 'local legislators nominated to ZP; Collector chairs ZP; <b>political parties debarred</b> from PR elections; “vertical representation”. <i>Impact:</i> some States went 2-tier or 4-tier, set up Nyaya Panchayats, made ZP executive'],
       ['<b>Ashok Mehta</b> (1977, Janata)', '<b>parties allowed</b> to contest for accountability: <b>West Bengal 1978</b> allowed it, some States do not; separate <b>Ministry of PR</b> in every State'],
       ['<b>G.V.K. Rao</b> (1985)', '= <b>CARD</b> (Committee to Advise on Administrative arrangements for Rural Development); ZP CEO as <b>District Development Commissioner</b>, status above DM; <b>DRDA</b> (IRDP from 1978) merged with ZP; ZP manages all rural development programmes'],
       ['<b>L.M. Singhvi</b> (1986)', 'Nyaya Panchayats for a <b>cluster of villages</b> (justice at grassroots); PR tribunals for election and dissolution disputes']),
    bx('bl', '<b>Parastatal</b> (DRDA etc.): fully or partly state-owned, autonomous or partly autonomous body set up by statute or as a cooperative society for a specific purpose.'),
  ]),
  # ------------------------------------------------------------ 243D example, OBC, 243O, significance
  dict(after='73RD AM.: ARTS 243 TO 243O', nodes=[
    sec('CLASS · Art 243D: worked example, OBC seats; Art 243O', 'r'),
    tb(['Panchayat of 9 seats', 'Split'],
       ['SC seats (by SC population), say <b>3</b>', '1/3 for women = <b>1 SC woman + 2 SC men</b>'],
       ['Women overall = 1/3 of 9 = <b>3</b>', 'includes SC/ST women: <b>1 SC woman + 2 other women</b>']),
    bx('pk', '<b>Teacher:</b> reservation share changes by level (village, block, district) with each level’s own SC population; chairperson posts <b>rotate</b>, rotation after 5 years; Backward Classes at State’s discretion, also for chairperson.'),
    bx('bl', '<b>OBC in local bodies:</b> Parts IX and IX-A mandate only SC, ST and <b>1/3 women</b>; OBC quota is the State’s option. <b>Vikas Kishanrao Gawali (2021):</b> (1) set up a <b>dedicated commission</b> on backwardness and OBC representation in local bodies; (2) fix OBC seat proportion <b>local body-wise</b> on its recommendation; (3) SC + ST + OBC seats together <b>not above 50%</b>.'),
    bx('pk', '<b>Art 243O</b> bars courts in electoral matters (cf. Art 329(a), delimitation; teacher: read “gerrymandering”). <b>Kishore Chandra Rathore (2024):</b> SC held delimitation and population balancing is open to judicial review for <b>arbitrariness and mala fide intent</b>.'),
    sec('CLASS · Significance of the 73rd Amendment (teacher: 6)', 'r'),
    t('<b>73rd CAA: why it matters</b>', 'new respectability to local bodies', '<b>regular elections</b>: suppressing Panchayats now difficult', 'independent <b>SFC and State Election Commission</b>', 'own functional domain (Sch XI, XII); earlier at State’s mercy', 'weaker sections: “silent revolution”, rise of the newly enfranchised', '“biggest democracy” gains substance: millions of new representatives; citizens per representative: <b>PRI 340</b>, <b>Municipalities 560</b>', w=24),
  ]),
  # ------------------------------------------------------------ Gram Sabha
  dict(after='GRAM SABHA AND PESA', nodes=[
    sec('CLASS · Gram Sabha: functions, issues, fixes', 'r'),
    bx('pk', '<b>Also considers</b> Panchayat budget, audit reports, annual administration report (varies by State). <b>Recall power</b> (remove or replace post-holders before term) in <b>Chhattisgarh</b> and <b>M.P.</b>'),
    two([t('<b>Issues (6)</b>', 'unwieldy size (some 10,000 people)', 'villagers lack knowledge of the body', 'prolonged meetings, endless talk', '<b>fictitious meetings</b> on paper (2 a year due)', 'poor women’s participation', 'class, caste, gender divides', w=16)],
        [t('<b>Suggestions (4)</b>', 'involve credible <b>NGOs</b>', 'mandatory provisions to hold meetings', 'information flow from GP to GS (grants, funds)', 'redesign GS-GP link: small <b>Ward Sabha</b> forms the GS, cutting its size', w=16)]),
  ]),
  # ------------------------------------------------------------ 3 types of Part IX provisions
  dict(after='COMPULSORY AND VOLUNTARY PROVISIONS', nodes=[
    sec('CLASS · Three kinds of Part IX provisions', 'r'),
    bx('pk', '<b>Teacher:</b> Part IX has <b>3 types</b> of provisions: <b>mandatory</b> · <b>with flexibility in implementation</b> · <b>optional</b> (voluntary).'),
  ]),
  # ------------------------------------------------------------ funds
  dict(after='FUNDS FOR PRIs', nodes=[
    sec('CLASS · PRI funds: extras', 'r'),
    bx('bl', '<b>Art 280(3)(bb) Panchayats</b> and <b>280(3)(c) Municipalities</b> (added by the 1992 Ams): Central Finance Commission recommends measures to augment the State Consolidated Fund so as to supplement local-body resources, <b>based on SFC recommendations</b>. Own-source: <b>Art 276</b> = professional tax.'),
    tb(['Scheme type', 'Who implements / pays', 'Examples'],
       ['<b>Centrally Sponsored (CSS)</b>', 'implemented by local bodies; Centre may fund only <b>partly</b>', 'MGNREGA, Jal Jeevan Mission'],
       ['<b>Central Sector</b>', 'implemented by Centre only, <b>100% Centre-funded</b>', 'capacity building, PM Jan Dhan Yojana']),
  ]),
  # ------------------------------------------------------------ challenges: State control, evaluation, women, PAI
  dict(after='CHALLENGES AND WAY FORWARD', nodes=[
    sec('CLASS · State control of PRIs: need and means', 'r'),
    bx('pk', '<b>Teacher:</b> “Where the spur and rein are required, the State uses a <b>sledge hammer</b>.”'),
    two([t('<b>Need (3)</b>', 'PRIs are <b>created, funded, empowered</b> by the State', 'balance regional development; avoid <b>“parish pump” attitude</b> (parochial, own needs only, harm to neighbouring villages)', 'State gives funds, administration, technical help, so it may control', w=16)],
        [t('<b>Means (10)</b>', 'key officials are State appointees: <b>Panchayat Secretary, BDO, ZP CEO</b>', '<b>supersession</b>, premature dissolution (even on Act loopholes)', 'suspends and removes elected members', 'suspends PRI resolutions', 'vertical budget approval', 'binding directions (no option to reject)', 'audit; enquiries into PRI affairs', 'State fixes max and min powers', '<b>tied grants</b>', w=16)]),
    sec('CLASS · Evaluation after 1992; Rajbala (2015); women in PRIs', 'r'),
    t('<b>No pan-India verdict possible</b>', 'unequal empowerment across States', 'PRIs not fully autonomous: power derived from State', 'many objectives (political consciousness, democratisation, development)', w=22),
    t('<b>Problems</b>', '<b>lack of politico-bureaucratic will:</b> State leaders see PRIs as a threat to their power', '<b>triangle of Patriarchy, Feudalism, Casteism:</b> landowners control local bodies; casteism blocks backward-class empowerment', t('<b>Caste still plays</b>', 'Art 243D not fully implemented', 'creamy layer gains more', '<b>proxy candidates: “Sarpanch Pati”</b>', 'violent backlash against backward classes', '5-year rotation too short to build lasting ties', 'restrictive State qualifications; recall misused'), w=22),
    bx('ye', '<b>Rajbala (2015), Haryana:</b> SC <b>upheld educational norms</b> for Panchayat candidates (men 10th pass, women 8th pass; SC norms lower, class note partly unreadable); also functional toilet at home, no arrears to cooperative bank or electricity, not accused of offence punishable with <b>10 years or more</b>. Result: about <b>half of rural women</b>, <b>68% of SC women</b>, <b>41% of SC men</b> disqualified. (Right to vote and contest as Constitutional Rights: see Ch 24.)'),
    two([t('<b>Impact on women</b>', 'in 5 years about <b>3 million</b> women contested, <b>1 million</b> elected', 'more Gram Sabha participation (women-headed GPs)', 'more spending on women welfare', 'better against social evils', '“Panchayat Pati” declined in a few States', w=16)],
        [t('<b>Problems of women (8)</b>', 'dual burden: home and Panchayat', 'lack of security', 'low information, literacy', '<b>Panchayat Pati</b>', 'little public exposure', 'restrictive qualifications, e.g. <b>2-child norm (Javed, 2003)</b>', 'rarely elected from general seats', 'rotation every 10 years, not 5 (class: T.N., Karnataka)', w=16)]),
    tb(['Developmental impact', 'Class examples'],
       ['Agriculture', 'Karnataka schemes failed (no technical help); <b>Gujarat, T.N.</b> PRIs raised output'],
       ['Weaker sections', 'committees from local bodies planned, not effective'],
       ['Education', 'primary and secondary given to PRIs in many States, uneven'],
       ['Verdict', '<b>political development</b> rose more than development']),
    sec('CLASS · Panchayat Advancement Index (PAI)', 'r'),
    bx('bl', '<b>PAI:</b> scores about <b>2.6 lakh Gram Panchayats</b>; “we localise SDGs at GP level”; <b>9</b> broad indicators in 3 groups: <b>infrastructure</b> (road, electricity, water), <b>socio-economic</b> (health, education, poverty), <b>environmental sustainability</b> (clean, green village).'),
    tb(['Category', 'Score', 'Share of GPs (class finding)'],
       ['A+ Achievers', 'above 90%', '0%'],
       ['A Front runners', '75-90%', '0.3%'],
       ['B Performers', '60-75%', '35%'],
       ['C Aspirants', '40-60%', '61%'],
       ['D Beginners', 'below 40%', '2.7%']),
    bx('ye', '<b>Class vs handout:</b> class says 9 indicators in 3 groups; handout CA says PAI covers nine SDG themes (check; same nine).'),
  ]),
  # ------------------------------------------------------------ urban background
  dict(after='URBAN LOCAL GOVERNMENT: EVOLUTION', nodes=[
    sec('CLASS · Urban LG: background', 'r'),
    bx('pk', '<b>Teacher:</b> urban areas give about <b>65% of India’s GDP</b>, yet urban space was neglected by State and Centre. <b>National Commission on Urbanisation (1985, Charles Correa)</b> was the first; its recommendations went into <b>Part IX-A</b>; <b>no 2nd Commission</b> yet. Grass-root planning: DPC and MPC.'),
  ]),
  # ------------------------------------------------------------ Part IX-A extras
  dict(after='74TH AM.: PART IX-A', nodes=[
    sec('CLASS · Part IX-A: extra points', 'r'),
    t('<b>Art 243Q: caution before labelling Nagar Panchayat</b>', 'urban <b>administration cost</b> is high', 'urban <b>tax rates</b> are high', 'ongoing rural programmes may stop', '<b>Gram Sabha stops</b> (shift from Part IX to IX-A)', t('<b>Criteria</b> (Governor notifies)', 'population, density, non-agricultural activity, economy'), '<b>no hierarchy</b> among municipalities (unlike 3-tier PRIs): each type suits a different area', w=24),
    bx('bl', '<b>Art 243Q proviso:</b> a <b>private industrial township</b> gets no LSG, it manages itself. Example: <b>Tata Nagar steel township</b> (Jamshedpur). Not in the original; 500+ such townships now. <b>Art 243R:</b> non-voting persons with special knowledge are <b>Aldermen</b>.'),
    tb(['Part IX-A', '= Part IX', 'Subject'],
       ['243T', '243D', 'reservation'], ['243U', '243E', 'duration'], ['243V', '243F', 'disqualification'], ['243W', '243G', 'powers'], ['243X', '243H', 'taxes'], ['243Y', '243I', 'Finance Commission (same FC)'], ['243Z', '243J', 'audit'], ['243ZA', '243K', 'elections (same SEC)'], ['243ZB', '243L', 'application to UTs']),
    bx('pk', '<b>Difference in 243T:</b> PRIs give women 1/3 of chairperson posts and SC/ST chairpersons by State population share; in ULBs chairperson reservation follows <b>State law</b> (bound by Art 334). <b>243W(b):</b> powers of committees (ward committees) are decided by the State.'),
    bx('ye', '<b>Art 243ZC:</b> Part IX reached Scheduled Areas by <b>PESA 1996</b>; Part IX-A has <b>not</b>: the <b>2001 MESA</b> bill (Municipalities Extension to Scheduled Areas) was not passed.'),
    bx('bl', '<b>243ZD/ZE:</b> DPC chairperson is chosen by its members (class); chairperson forwards the district development plan to the State Government. Class remark: Part IX and IX-A reflect an “<b>artificial dichotomy</b>” between rural and urban development.'),
  ]),
  # ------------------------------------------------------------ Bombay vs Howrah
  dict(after='TWELFTH SCHEDULE AND TYPES OF ULBs', nodes=[
    sec('CLASS · Bombay vs Howrah/Calcutta pattern', 'r'),
    tb(['Point', 'Bombay pattern', 'Howrah/Calcutta pattern'],
       ['Followed by', 'most States; Municipal Corporation', 'Mayor is real executive; Commissioner under Mayor'],
       ['Basis', 'executive-deliberative <b>dichotomy</b>', 'ARC-2 recommended'],
       ['Roles', 'bureaucrats/IAS implement plans and policies; Mayor = presiding officer, ceremonial, discusses and passes local needs', 'Mayor decides'],
       ['Accountability', '“<b>down</b>”: Commissioner answers to the State, citizens cannot remove him', '“<b>up</b>” (class label)']),
  ]),
  # ------------------------------------------------------------ urban problems
  dict(after='PERSONNEL, TRAINING', nodes=[
    sec('CLASS · Problems of urban administration (14)', 'r'),
    two([t('<b>Problems 1-7</b>', 'haphazard urbanisation: migration, overcrowding, slums, housing and water shortage', 'health: few clinical services, community health ignored', 'urban poor worse off than rural poor', 'traffic: pedestrianisation, congestion levy, public transport only, costly parking', 'pollution', 'power and water shortage', 'crime, especially against women', w=16)],
        [t('<b>Problems 8-14</b>', 'massive corruption', 'poor devolution of the <b>3 Fs</b> (funds, functions, functionaries)', 'weak capacity building', 'no urban way of life', 'lack of quality leadership', 'focus shifted to rural areas', '<b>institutional jungle:</b> 11 bodies at municipal level, e.g. Delhi: MCD + DDA + Centre + Delhi Govt', w=16)]),
  ]),
  # ------------------------------------------------------------ ULB finance
  dict(after='FUNDS FOR ULBs', nodes=[
    sec('CLASS · ULB finance: property tax immunity', 'r'),
    bx('bl', 'Property tax is poorly collected and <b>cannot be levied on government buildings</b>: <b>Art 285</b> (Union property exempt from State and local tax), <b>Art 289</b> (State property exempt from Union tax); allowed only <b>by law</b> (Parliament). Called <b>immunity of instrumentalities</b>.'),
  ]),
 ],

 14: [
  # ------------------------------------------------------------ composition
  dict(after='COMPOSITION (ART 124)', nodes=[
    sec('CLASS · SC strength: 18 May ordinance', 'r'),
    bx('ca', '<span class="tag">Class · 18 May ordinance</span>Strength raised <b>34 to 38</b> (CJI + <b>37 puisne</b>; puisne = junior judge) first by ordinance of 18 May; the 2026 Act (handout CA above) states the same rise as 33 to 37 excluding CJI.'),
  ]),
  # ------------------------------------------------------------ collegium
  dict(after='APPOINTMENT AND THE COLLEGIUM', nodes=[
    sec('CLASS · Collegium, NJAC, MoP, critique', 'r'),
    tb(['Appointment', 'Collegium'],
       ['<b>SC judges</b>', '<b>5</b> = CJI + 4 senior-most (Second case 1993: 3 = CJI + 2)'],
       ['<b>HC judges</b>', '<b>3</b> = CJI + 2 senior-most'],
       ['<b>Transfer</b>', 'same 5-member collegium consults the <b>2 HC Chief Justices</b> (judge’s old and new HC)']),
    bx('pk', '<b>Teacher’s order:</b> S.P. Gupta 1982 = First; Advocates-on-Record 1993 = Second (CJI primacy); the <b>Third</b> case explained how the procedure works. First case: “consultation” = effective consultation, not CJI concurrence; Government decides who becomes judge.'),
    bx('ye', '<b>Class vs handout:</b> class notes say any <b>2 judges</b> can veto and the <b>CJI alone</b> can veto; handout has only “if two judges disagree, CJI should not send the recommendation” (check).'),
    t('<b>NJAC (99th Am. 2014)</b>', 'Arts <b>124A, 124B, 124C</b> + NJAC Act', t('<b>6 members</b>', 'CJI', '2 SC judges', 'Law Minister', '2 eminent persons'), '<b>any 2 members can veto</b>', 'recommends the senior-most SC judge as CJI if fit', w=22),
    bx('bl', '<b>4th Judges Case (2015): SC AORA v. UOI</b> rejected the NJAC set-up. <b>Memorandum of Procedure (MoP)</b> (class notes: first issued 1947, verify): CJI appointed by seniority.'),
    fl(['Collegium recommends', 'Law Minister (+ IB report)', 'PM', 'President approves'], 'MoP: SC judges', 4),
    fl(['HC CJ + 3-member collegium: list of probables', 'Governor and CM', 'Law Minister (IB report)', 'SC 3-member collegium', 'PM and President'], 'MoP: HC judges (arrows partly unclear in class notes)', 3),
    bx('pk', '<b>Reforms needed in collegium:</b> <b>transparency</b>, appointment <b>criteria</b>, a <b>secretariat</b>, <b>time-bound</b> process.'),
    bx('gr', '<b>Mains frame: critique of the collegium (teacher flagged).</b> <i>Intro:</i> judges appoint judges since 1993. <i>Points:</i> (1) <b>delay</b>: 2023 HC sanctioned strength 1114, vacant 324 (2) <b>opacity</b>: procedure, criteria, reasons for rejection not public (3) “consultation” in Art 124 read to give judiciary a monopoly (4) CJI opinion was already convention till 1993: of <b>348</b> recommendations only <b>7</b> rejected, so no collegium needed (5) executive-era appointments were of the best; collegium brought “corrupt judges” (J.S. Verma noted, as the author of the 1993 judgment he is said to have called it a failure: class note ambiguous, verify) (6) federal judiciary eroded. <i>Close:</i> fix with MoP reform, secretariat, timelines.'),
  ]),
  # ------------------------------------------------------------ removal
  dict(after='TENURE AND REMOVAL', nodes=[
    sec('CLASS · Removal in practice', 'r'),
    bx('pk', '<b>No judge removed so far</b>; usually the judge <b>resigns before</b> the proceeding starts (some jurists want the inquiry completed even after resignation). Presiding officer may set up the committee; the third member may be an eminent law professor, none appointed yet.'),
  ]),
  # ------------------------------------------------------------ seat, benches, 145, 146
  dict(after='SEAT, PROCEDURE, BENCHES', nodes=[
    sec('CLASS · Art 130 regional benches; Arts 145, 146', 'r'),
    t('<b>Regional benches debate (Art 130)</b>', 'SC sits at Delhi or places the CJI picks with President’s approval', 'farther from Delhi, fewer cases filed (distance cuts access)', '<b>For:</b> physical proximity, access to justice', '<b>Against</b> (SC not convinced): hurts integrity of the court; consistency of decisions', t('<b>Suggestion</b>', 'separate <b>Constitutional Court</b> (no regular case allocation)', '<b>4 Cassation benches:</b> Mumbai, Delhi, Chennai, Kolkata'), w=24),
    tb(['Art 145 and 146', 'Class points'],
       ['<b>AOR</b>', 'only an <b>Advocate-on-Record</b> can file in the SC (rule of <b>1966</b>); anyone may argue; AOR needs an exam'],
       ['<b>Rules cover</b>', 'practitioners, appeals, FRs, Art 134 appeals, review, <b>139A</b>, costs and fees, bail and stay, <b>frivolous appeals</b> (summary decision), Art <b>317(1)</b> inquiries (PSC member removal)'],
       ['<b>Open court</b>', 'judgments and <b>Art 143</b> opinions strictly in open court'],
       ['<b>Art 146 staff</b>', '<b>CJI appoints</b> officers and servants (President may mandate an outside candidate; <b>UPSC</b> consulted); service rules by CJI subject to law; pay, leave, pension rules need <b>President’s approval</b>; all costs charged on <b>Consolidated Fund</b>, fees go to CFI']),
  ]),
  # ------------------------------------------------------------ appellate
  dict(after='APPELLATE JURISDICTION', nodes=[
    sec('CLASS · Appeals: Letters Patent, 134A, 136', 'r'),
    fl(['Single judge, HC', '2-judge bench, HC (Letters Patent Appeal)', 'Supreme Court'], 'Letters Patent route', 3),
    bx('bl', '<b>Art 134A:</b> every HC passing judgment, decree, final order or sentence under <b>132(1), 133(1), 134(2)</b> decides quickly whether to certify under 134(1)(c). Two ways: <b>suo motu</b> by the HC, or <b>oral application</b> by the aggrieved party right after the judgment.'),
    bx('pk', '<b>Art 136 (marked Imp):</b> nearly <b>80%</b> of cases pending in the SC are special leave petitions.'),
  ]),
  # ------------------------------------------------------------ Arts 139-143
  dict(after='ADVISORY JURISDICTION', nodes=[
    sec('CLASS · Arts 139-143: additions', 'r'),
    tb(['Art', 'Class meaning'],
       ['<b>139</b>', 'Parliament may confer power to issue directions, orders or writs for purposes <b>other than those in Art 32(2)</b>'],
       ['<b>139A</b>', 'SC withdraws cases from HCs with the <b>same substantial question of law</b>, or transfers a case between HCs for ends of justice'],
       ['<b>140</b>', 'Parliament may give <b>supplemental powers</b> so SC exercises original jurisdiction more completely'],
       ['<b>142</b>', 'any order or decree needed for <b>complete justice</b> in a pending matter; enforcement of decrees'],
       ['<b>143</b>', 'purpose: government wants a legal opinion <b>before acting</b>, the matter need not reach court; 143(2): dispute under proviso to Art 131, SC <b>“shall”</b> opine']),
    bx('ye', '<b>Class vs handout:</b> class defines Art 139 as above; handout table says “139: Centre-State agreements” (check).'),
  ]),
  # ------------------------------------------------------------ contempt
  dict(after='COURT OF RECORD AND CONTEMPT', nodes=[
    sec('CLASS · Contempt: law, issues, cases', 'r'),
    t('<b>Courts of Record:</b> SC <b>Art 129</b>, HC <b>Art 215</b>', 'acts and proceedings recorded as permanent memory', 'precedent for lower courts', 'punish own contempt', t('<b>Law on contempt</b>', '<b>Union List entry 77</b> (SC)', '<b>Concurrent List entry 14</b> (other courts)'), 'purpose: shield courts from motivated attacks; protect independence', w=24),
    tb(['Issue with contempt power', 'Point'],
       ['<b>Natural justice</b>', '<b>Nemo judex in causa sua</b> (judge is the injured party); <b>audi alteram partem</b> (unheard party: ex parte); no extraneous influence, even the judge’s ideology; reasons given; justice <b>seen</b> to be done. <b>Recusal</b> = judge withdraws over conflict of interest'],
       ['Vague definition', 'criminal contempt is loosely defined'],
       ['Fair criticism', 'can be punished: criticise the judgment, not the Judge'],
       ['<b>Mens rea</b>', 'real intent not considered']),
    tb(['Case or change', 'Holding'],
       ['<b>Spycatcher (UK, 1987)</b>', 'House of Lords banned the book even after the world read it; a newspaper mocked the Lords (“You old fools”); Lord Templeton did not treat opinion as contempt (as noted)'],
       ['<b>Mulgaonkar (1978)</b>', 'balance free criticism with judicial independence; press gets free play within reasonable limits; judges should not be hypersensitive'],
       ['<b>2006 amendment</b> (1971 Act)', '<b>truth</b> is a valid defence (if evidence against judges is valid)']),
    bx('pk', '<b>Who can start contempt:</b> (1) <b>suo motu</b> (2) Attorney General notice (SC) (3) Advocate General notice (HC) (4) a private person needs consent of the AG / Advocate General.'),
  ]),
  # ------------------------------------------------------------ Art 13
  dict(after='13 DOCTRINES OF INTERPRETATION', nodes=[
    sec('CLASS · Art 13: pre-constitutional laws', 'r'),
    t('<b>Pre-1950 laws</b>', '<b>Art 372</b> (class): pre-constitutional laws are void if they violate FRs', t('<b>Eclipse (Bhikaji 1955):</b> law not dead, only eclipsed', 'FRs are <b>prospective</b> (from 26 Jan 1950)', 'legal <b>continuity</b>', 'law still works for <b>foreigners</b>; some rights are for citizens only'), t('<b>Severability</b>', 'sever the offending sections, rest operates', 'if surgical separation impossible, whole law goes'), w=24),
    bx('ye', '<b>Class vs earlier notes:</b> “law” in Art 13(2): narrow = ordinary law; broad = ordinary law + Constituent Amendment Law; class prefers the <b>broader</b> meaning. Ch 5 notes: amendments are not “law” but reviewable on Basic Structure (check).'),
  ]),
  # ------------------------------------------------------------ independence
  dict(after='OTHER POWERS AND INDEPENDENCE', nodes=[
    sec('CLASS · Independence: why, extras, NJPC', 'r'),
    bx('gr', '<b>Mains frame: why independence is required.</b> <i>Intro:</i> judiciary guards the Constitution. <i>Points:</i> (1) checks and balances, separation of powers (2) <b>government is the biggest litigant</b> (3) shield the Constitution from unwarranted invasion by Parliament or executive (4) rule of law (5) citizens’ democratic rights (6) norms of federal polity (7) check the four “-feasances”. <i>Close:</i> without it, rights are unenforceable. <i>(Class notes skip point 7 of the teacher’s numbering.)</i>'),
    tb(['Feasance', 'Meaning'],
       ['<b>Mal</b>feasance', 'abuse of power'], ['<b>Mis</b>feasance', 'bona fide error'], ['<b>Over</b>feasance', 'beyond jurisdiction'], ['<b>Non</b>feasance', 'failure to act within jurisdiction']),
    bx('pk', '<b>Arts 121 and 211:</b> Parliament and State Legislature cannot discuss judges’ conduct except on a removal resolution. Teacher’s extras: contempt power, judicial primacy in appointments and transfers, independence of subordinate judiciary.'),
    bx('ye', '<b>Class vs handout:</b> class says an SC judge cannot practise after retirement, but an HC judge <b>can</b> practise in the SC and in an HC where he was not a judge; handout safeguard 6 says no practice before any court (check).'),
    tb(['National Judicial Pay Commission', 'Detail'],
       ['<b>1st NJPC</b>', '<b>1996</b>, Justice <b>Jagannatha Shetty</b>'],
       ['<b>2nd NJPC</b>', '<b>2017</b>, Justice <b>Venkatarama Reddy</b>'],
       ['<b>All India Judges Association v. UOI (2024)</b>', 'every HC to set up a body of <b>2 HC judges</b> to review implementation of the SNJPC; district judges are <b>not State employees</b> but holders of public office wielding judicial power; no equation with executive officers']),
  ]),
  # ------------------------------------------------------------ HC benches
  dict(after='COMPARISON', nodes=[
    sec('CLASS · High Court benches', 'r'),
    tb(['Type', 'Meaning', 'Examples'],
       ['<b>Regular</b> (permanent)', 'permanent set-up beyond principal seat', 'Bombay: Mumbai + Nagpur, Aurangabad · Allahabad + Lucknow · MP: Jabalpur + Gwalior, Indore · Madras + Madurai · <b>Karnataka</b>: Bangalore + Dharwad, Kalaburagi · Rajasthan: Jodhpur + Jaipur · Gauhati + Aizawl, Itanagar, Kohima'],
       ['<b>Circuit</b> (temporary)', 'judges travel from principal seat, return after disposing matters', 'Calcutta HC at Port Blair']),
    bx('pk', '<b>Why:</b> easy access in large or populous States. <b>Jaswant Singh Committee (1981)</b>: needs consent of the <b>HC Chief Justice</b> and the <b>State government</b>. <b>Criteria:</b> sizable population · features of a region · travel and communication · pendency at the principal seat.'),
  ]),
  # ------------------------------------------------------------ SC position frame
  dict(after='', nodes=[
    sec('CLASS · Mains frame: position of the SC', 'r'),
    bx('gr', '<b>Q: What is the position of the SC under the Constitution?</b> <i>Points (teacher):</i> (1) <b>federal court</b> (2) <b>highest court of appeal</b> (3) <b>final interpreter</b> of the Constitution (4) <b>protector of Fundamental Rights</b> (Art 32) (5) <b>court of record</b>.'),
  ]),
 ],
}

RECALL = {
 13: [('Vikas Kishanrao Gawali (2021): OBC local-body conditions?', 'dedicated commission; seats fixed local body-wise; SC+ST+OBC within 50%'),
      ('Rajbala (2015) result?', 'SC upheld education norms; about half of rural women, 68% SC women, 41% SC men disqualified'),
      ('PAI score bands and where most GPs fall?', 'A+ above 90, A 75-90, B 60-75, C 40-60, D below 40; C 61%, B 35%'),
      ('Why careful before labelling an area Nagar Panchayat (243Q)?', 'higher admin cost and tax, rural programmes stop, Gram Sabha ceases')],
 14: [('NJAC composition and veto?', '6: CJI, 2 SC judges, Law Minister, 2 eminent persons; any 2 can veto; Arts 124A-C'),
      ('Collegium size: SC, HC, transfers?', 'SC 5 (CJI + 4); HC 3 (CJI + 2); transfer also consults 2 HC Chief Justices'),
      ('Jaswant Singh Committee 1981?', 'HC benches: consent of HC CJ and State; population, region, travel, pendency'),
      ('Contempt: Mulgaonkar and 2006 change?', 'Mulgaonkar 1978 balances criticism and independence; 2006: truth is a valid defence')],
}
