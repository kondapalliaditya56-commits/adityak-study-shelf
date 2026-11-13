# -*- coding: utf-8 -*-
from dsl import *
from hwlib import P
OWN = lambda w, h: mn(w, h + ' <i>(own mnemonic)</i>')
ADD = {
 # ------------------------------------------------------------------ CH 27 SCHEDULED AND TRIBAL AREAS
 27: [
   dict(after='FIFTH SCHEDULE', nodes=[
     sec('CLASS · Tribal policy, PVTGs, amending Schedules', 'r'),
     tb(['Class point', 'Detail'],
        ['<b>Tribal policy</b>', 'NE tribes (Arunachal, Mizoram, Meghalaya, Tripura): <b>“anthropological specimen”</b> approach (isolation, preservation). Rest of India: <b>assimilation</b> into larger society'],
        ['<b>PVTG</b>', 'Particularly Vulnerable Tribal Groups: <b>Dhebar Commission 1960</b>; <b>Bhuria Commission 2002</b> (class wrote “Vulnerable”, verify)'],
        ['<b>Simple majority</b>', 'Schedules <b>I, II, V, VI</b> can be amended without Art 368 (Art 4, Art 244; Fifth para 7, Sixth para 21)'],
        ['<b>Art 339</b>', '“Notwithstanding” = in spite of']),
   ]),
   dict(after='SIXTH SCHEDULE', nodes=[
     sec('CLASS · Sixth Schedule: origin, BTC, powers, Ladakh', 'r'),
     bx('pk', '<b>Origin:</b> added on the recommendation of the <b>Gopinath Bordoloi sub-committee</b> of the Constituent Assembly (tribal areas). Governor is the key authority.'),
     fl(['Tribal Area', 'Autonomous District (ADC)', 'Several tribes inside: Autonomous Regions', 'Autonomous Region Councils (same as ADC)'], 'Teacher diagram: area to councils', 4),
     tb(['Council', 'Strength'],
        ['<b>Each ADC</b>', '<b>30</b> = 26 elected (5 years) + 4 nominated'],
        ['<b>Bodoland Territorial Council</b> (exception)', '<b>46</b> = <b>40</b> elected + <b>6</b> nominated']),
     t('<b>ADC powers: 4 kinds</b>',
       t('<b>Legislative</b> (Governor’s assent)', 'land allotment, forests, water bodies, <b>shifting cultivation</b>', 'village and town committees; village and town administration incl. <b>police, public health, sanitation, education</b>', 'appointment and <b>succession of chiefs</b>; personal laws (marriage etc.)'),
       t('<b>Judicial</b>', 'village councils and courts for intra-tribal disputes', 'appeal route (class): ADC to Sub-court (as noted) to <b>HC</b> to <b>SC</b>'),
       t('<b>Financial</b>', 'collect certain taxes', 'licences for <b>prospecting and extraction of minerals</b> or a <b>share of royalty</b>', 'rules on money-lending'),
       '<b>Executive</b> (4th kind named in class)', w=22),
     t('<b>Ladakh wants Sixth Schedule status</b> (teacher’s current example)',
       t('<b>Two Hill Councils</b>', 'Leh', 'Kargil'),
       t('<b>Reasons</b>', 'industrial exploitation', 'minerals found', 'tourist conduct', '<b>reservation for locals</b> in local governments'),
       '<b>1 Lok Sabha seat</b>; also demanding <b>2 Rajya Sabha</b> seats', w=24),
   ]),
 ],
 # ------------------------------------------------------------------ CH 28 UNION AND ITS TERRITORY
 28: [
   dict(after='LANGUAGE AS BASIS', nodes=[
     sec('CLASS · Basis of States; border adjustment', 'r'),
     bx('pk', '<b>States were created mostly on:</b> language · tribal ethnicity · development deficit.'),
     bx('ye', '<b>Class vs handout:</b> class says first linguistic State after Independence = <b>Andhra Pradesh (1956)</b>; handout says <b>Andhra State, 1953</b> (check). Before Independence: Odisha, 1936.'),
     bx('gr', '<b>Cession vs adjustment (class):</b> an agreement ceding territory to another country needs a <b>special-majority amendment</b> (9th Am. 1960); a minor border adjustment can be done by <b>executive order</b>.'),
   ]),
 ],
 # ------------------------------------------------------------------ CH 31 UPSC
 31: [
   dict(after='ART 315', nodes=[
     sec('CLASS · PSC history and firsts', 'r'),
     tl(('1919', 'GoI Act'), ('1924', 'Lee Commission recommends'), ('1926', 'Federal PSC set up'), ('1929', 'Madras: first State PSC'), ('1935', 'GoI Act: FPSC, PPSC, JPSC'), ('1947', 'first Indian chair'), ('1992', 'first woman chair')),
     tb(['First', 'Name (class)'],
        ['<b>FPSC chairperson</b>', 'Sir <b>Ross Baker</b>'],
        ['<b>First Indian chair</b>', '<b>H.K. Kripalani</b>, 1947 (class wrote “H.B. Kriplani”, verify)'],
        ['<b>First woman chair</b>', '<b>Rose Bathew</b>, 1992'],
        ['<b>Present chair</b>', 'Dr. <b>Ajay Kumar</b>']),
     bx('pk', '<b>GoI Act 1935:</b> Federal PSC (now UPSC), Provincial PSC (State PSC) and <b>Joint PSC under Art 315</b>; Punjab and Haryana had a Joint PSC for a brief period. Part XIV = Public Service (Arts 308-323).'),
   ]),
   dict(after='ARTS 318, 319', nodes=[
     sec('CLASS · Movement between posts; Art 320 split', 'r'),
     tb(['Now', 'Can become'],
        ['<b>UPSC member</b>', 'UPSC Chairperson; SPSC Chairperson (class also: member of another State PSC, as written)'],
        ['<b>SPSC Chairperson</b>', 'UPSC member or Chairperson; Chairperson of another State PSC']),
     bx('pk', '<b>Art 320:</b> clauses <b>(1), (2)</b> = mandatory functions, common to all PSCs; clause <b>(3)</b> = advisory consultation. A UPSC committee (Chairperson or member) recommends elevating State civil service officers to the IAS, up to <b>1/3</b> of cadre strength (as written).'),
   ]),
 ],
 # ------------------------------------------------------------------ CH 33 FINANCE COMMISSION
 33: [
   dict(after='FOUR DUTIES', nodes=[
     sec('CLASS · ToR, vertical and horizontal, Art 281', 'r'),
     tb(['Term', 'Class note'],
        ['<b>ToR</b>', 'Terms of Reference = areas on which the FC recommends'],
        ['<b>Vertical</b>', 'Union to States share'],
        ['<b>Horizontal</b>', 'among States; FC develops a <b>formula</b>; also recommends several kinds of <b>grants</b>']),
     bx('ye', '<b>Class vs handout:</b> class says under Art 281 the report is “subject to modification by Parliament”; handout: laid before Parliament with a memorandum on action taken, advice <b>not binding</b> (check).'),
   ]),
   dict(after='COMPOSITION', nodes=[
     sec('CLASS · FC: disqualification, timing, status', 'r'),
     t('<b>Cannot be appointed to FC</b>', 'unsound mind', 'undischarged insolvent', 'convicted of an offence', 'financial interest conflicting with duties as member', w=22),
     tb(['Point', 'Class note'],
        ['<b>New FC</b>', 'constituted <b>18-24 months before</b> the 5-year award expires'],
        ['<b>Tenure</b>', 'as specified in presidential order; re-appointable; full-time or part-time; salary decided by Govt'],
        ['<b>Powers</b>', 'power of a <b>civil court</b> (quasi-judicial)']),
     OWN('SIFT', 'Disqualified: <b>S</b>ound mind lacking · <b>I</b>nsolvent · <b>F</b>inancial interest · convic<b>T</b>ed.'),
   ]),
 ],
 # ------------------------------------------------------------------ CH 34 GST COUNCIL
 34: [
   dict(after='', nodes=[
     sec('CLASS · GST framework, compensation, Mohit Minerals', 'r'),
     tb(['Provision', 'Detail'],
        ['<b>Art 246A</b>', 'Union <b>and</b> States both make GST laws'],
        ['<b>Art 269A</b>', 'GST on inter-State supply (class lists with 246A)'],
        ['<b>Art 279A</b>', 'GST Council recommends on taxes, surcharges, goods and services']),
     bx('bl', '<b>Empowered Committee of State Finance Ministers (2000):</b> worked on <b>VAT</b>, later GST.'),
     fl(['Base year 2015-16 for every State', 'Revenue assumed to grow 14% a year', 'Shortfall: Centre compensates', 'GST (Compensation to States) Cess Act, 2017: 5 years, due to end 2022', 'Covid: Centre borrowed to pay; cess ran to 2026'], 'Compensation (class)', 5),
     bx('pk', '<b>Mohit Minerals case, 2024</b> (year as written, check): GST Council recommendations are <b>not binding</b> on States.'),
     t('<b>Centre-State issues (teacher’s list, 6)</b>', 'abuse of <b>Art 356</b>', 'States unhappy with conduct of <b>Governors</b>', 'management of <b>All India Services</b>', 'States unhappy with central administrative directions', 'binding central directions in a federal polity', 'no proper special body for Centre-State coordination; existing bodies not used well', w=24),
     bx('bl', '<b>Conferences (class):</b> Chief Secretaries’ · DGPs’ · Governance · All India District Collectors’.'),
   ]),
 ],
 # ------------------------------------------------------------------ CH 37 NCBC
 37: [
   dict(after='ORIGIN AND STATUS', nodes=[
     sec('CLASS · NCBC Act 1993 body; evolution of commissions', 'r'),
     tl(('Art 338', 'Special Officer for SC/ST'), ('1990', '65th Am: National Commission for SC/ST'), ('2003', '89th Am: Art 338 NCSC, Art 338A NCST'), ('2018', '102nd Am: Art 338B NCBC')),
     tb(['NCBC Act 1993 members', 'Who'],
        ['1', 'Chairman: serving or retired <b>SC/HC judge</b>'],
        ['2', 'a <b>social scientist</b>'],
        ['3', '<b>2</b> persons with special knowledge on OBC matters'],
        ['4', '<b>Member-Secretary</b> (Govt)']),
     t('<b>1993 functions</b>', 'examine requests for inclusion in the Centre’s <b>OBC list</b>', 'advise which communities to include and <b>exclude</b> (castes ceased, or freshly identified)', w=22),
   ]),
 ],
 # ------------------------------------------------------------------ CH 39 CAG
 39: [
   dict(after='HISTORY OF IA', nodes=[
     sec('CLASS · First CAG; Departmentalisation 1976', 'r'),
     bx('pk', '<b>First CAG of India:</b> V. Narhari Rao (class: “Narhari Rao”); 15th CAG: <b>K. Sanjay Murthy</b>.'),
     fl(['Before: CAG kept and audited accounts of Centre, States, UTs (absurd)', 'Departmentalisation of Accounts Scheme 1976 (DoAS)', 'Indian Civil Accounts Service created', 'Controller General of Accounts (CGA), Finance Ministry, takes over accounts'], 'DoAS 1976', 4),
   ]),
   dict(after='POWERS AND DUTIES', nodes=[
     sec('CLASS · CAG: more functions and areas', 'r'),
     tb(['Class point', 'Detail'],
        ['<b>UTs with assemblies</b>', 'Puducherry, J&amp;K, Delhi'],
        ['<b>Sixth Schedule</b>', 'Autonomous District Councils audited by CAG'],
        ['<b>Art 279</b>', 'certifies net proceeds; assists the <b>Finance Commission</b>'],
        ['<b>Budgets</b>', 'helps Govt, States, UTs with annual budget setting (as written)']),
   ]),
   dict(after='CORPORATIONS AND AUDIT BOARD', nodes=[
     sec('CLASS · Corporations and companies: who audits', 'r'),
     tb(['Body', 'Class note'],
        ['<b>Public corporation</b> (by law, 100% Govt)', 'audit as the setup law says: full, partial or none. <b>RBI</b> (RBI Act 1934, first corporation), <b>LIC</b>, <b>FCI</b> outside CAG'],
        ['<b>Govt company</b> (joint stock)', 'min <b>51%</b> Govt-owned; auditor (chartered accountant) appointed by Govt on <b>CAG advice</b>; then CAG <b>supplementary</b> audit'],
        ['<b>All PSUs</b>', 'comprehensive performance review through <b>Audit Boards</b> from <b>1968</b>']),
   ]),
 ],
 # ------------------------------------------------------------------ CH 47 LAW COMMISSION AND BAR COUNCIL
 47: [
   dict(after='1 · LAW COMMISSION', nodes=[
     sec('CLASS · Law Commission: first, 23rd, status', 'r'),
     bx('pk', '<b>1st LC 1834</b> under the <b>Charter Act 1833</b>, Lord Macaulay (four colonial LCs: 1834, 1853, 1861, 1879). <b>23rd LC (2024): Justice Dinesh Maheshwari.</b>'),
     bx('ye', '<b>Class vs handout:</b> class calls today’s LC a “statutory body”; handout: <b>non-statutory</b>, advisory, by Govt notification. Follow the handout.'),
   ]),
   dict(after='2 · COMPOSITION', nodes=[
     sec('CLASS · LC composition (class version)', 'r'),
     t('<b>Law Commission</b>', '<b>1</b> Chairman (serving or retired SC/HC judge)', '<b>4</b> full-time members', 'ex-officio: Secretary, <b>Dept of Legal Affairs</b>; Secretary, <b>Legislative Dept</b>', 'not more than <b>5</b> part-time members', w=20),
   ]),
   dict(after='4 · MAJOR REPORTS', nodes=[
     sec('CLASS · Sedition: Sec 124A to BNS 152 ' + P('2023'), 'r'),
     tl(('1860/1870', 'IPC; 124A added 1870'), ('1962', 'Kedarnath: upheld, read down'), ('1995', 'Balwant Singh'), ('2022', 'Vombatkere: stay'), ('2023', 'BNS Sec 152 replaces 124A')),
     bx('bl', '<b>124A:</b> words, signs or visible representation bringing or attempting to bring <b>hatred or contempt</b> / exciting disaffection towards Govt; non-bailable (class: up to 3 years, verify). Gandhi: “prince among IPC sections” made to suppress Indians. Demand to add sedition to <b>Art 19(2)</b> in the Constituent Assembly was <b>not accepted</b>.'),
     t('<b>Criticism (5)</b>', 'medieval, archaic idea of loving the Govt', 'vague, politically misused', '<b>3%</b> conviction rate', 'relic of monarchy', 'racist: Indians treated as inferiors', w=22),
     tb(['Case', 'Holding'],
        ['<b>Kedarnath, 1962</b>', 'upheld 124A but <b>read down</b>: not violating Art 19(1)(a); reasonable restriction under <b>19(2)</b> for public order'],
        ['<b>Balwant Singh, 1995</b>', 'needs clear intent or actual <b>incitement to violence</b>; slogans causing no disturbance = no sedition'],
        ['<b>S.G. Vombatkere, 2022</b>', 'SC <b>stayed</b> 124A; no new case until law is declared unconstitutional; pending proceedings in abeyance; accused may seek bail']),
     bx('bl', '<b>Read down</b> = scope restricted; <b>read into</b> = scope expanded.'),
     bx('pk', '<b>BNS Sec 152:</b> purposely or knowingly, by words, signs, visible representation, <b>e-communication or financial means</b>, exciting <b>secession, armed rebellion, subversive activities, separatist feelings</b> or endangering sovereignty, unity, integrity; class: 7 years + fine (verify, BNS also provides life). <b>Explanation: criticism of Govt act or policy is not covered.</b>'),
   ]),
   dict(after='9 · TYPES OF ADVOCATES', nodes=[
     sec('CLASS · Senior Advocate, pre-audience, Rule 49, terms', 'r'),
     bx('pk', '<b>Sec 16, Advocates Act 1961:</b> SC/HC may designate a <b>Senior Advocate</b> for ability, standing, experience. <b>Limits:</b> cannot appear in the SC without a junior who is an <b>AOR</b>; cannot accept briefs directly.'),
     t('<b>Right of pre-audience (heard first)</b>', '<b>Attorney General</b> over all advocates', '<b>Solicitor General</b> over all except AG', '<b>Advocate General</b> (in the State)', '<b>Senior Advocate</b> over other advocates (order of last two partly unclear)', w=24),
     bx('ye', '<b>BCI Rule 49:</b> an advocate who becomes a <b>permanent salaried employee</b> of any person, Govt, corporation or company loses status as advocate.'),
     tb(['Legal term', 'Meaning (class)'],
        ['<b>Lawyer / Barrister</b>', 'law graduate / the same in the UK'],
        ['<b>Advocate (attorney)</b>', 'enrolled on a Bar Council'],
        ['<b>Public Prosecutor / Govt Pleader</b>', 'Govt advocate in criminal / civil cases'],
        ['<b>Res judicata</b>', 'final judgement between same parties on same question by competent court: cannot be raised again'],
        ['<b>Decree / Judgement / Order</b>', 'formal declaration of civil decision / decision with reasons / final or interlocutory order'],
        ['<b>Sources of law</b>', 'Constitution, statutes, case law, customary law']),
   ]),
   dict(after='10 · REFORMS', nodes=[
     sec('CLASS · Bar and Bench reform points (teacher)', 'r'),
     bx('bl', '<b>Aim:</b> better laws for justice and good governance under rule of law; improve quality of <b>Bar</b> (lawyers) and <b>Bench</b> (judges).'),
     t('<b>Teacher’s 5 points</b>', 'justice delivery not seen in India as part of development', 'operationalise <b>All India Judicial Service (AIJS)</b>', '<b>2010 All India Bar Exam</b>; upheld in the Bonnie Law College case, <b>2023</b> (name as written)', 'root out fake lawyers: <b>2017</b>, 14 lakh+ asked to submit degrees; only <b>6.5 lakh</b> received', '<b>2023</b> foreign law firms allowed: register with BCI, reciprocity, non-litigation (corporate: JVs, contracts, foreign law)', w=24),
   ]),
 ],
 # ------------------------------------------------------------------ CH 48 DELIMITATION
 48: [
   dict(after='4 · FOUR COMMISSIONS', nodes=[
     sec('CLASS · Chairs, the freeze and why a 4th in 2002', 'r'),
     tb(['DC', 'Chair (class, verify)'],
        ['<b>1952</b>', 'Justice J.C. Aiyar'],
        ['<b>1963</b>', 'Justice K.V. Sundaram (written “Sundaran”)'],
        ['<b>1973</b>', 'Justice J.L. Kapur'],
        ['<b>2002</b>', 'Justice Kuldeep Singh (notebook reads “Desai”)']),
     bx('ye', '<b>Class vs handout:</b> notebook gives “Desai” for the 2002 chair; handout: <b>Kuldip Singh</b> (2002), <b>Ranjana Prakash Desai</b> = 2020 Commission. Handout names no chairs for 1952-73.'),
     tl(('1976', '42nd Am: delimitation postponed to 2000'), ('2001', '84th Am: postponed to 2026'), ('2002', '4th DC: intra-State redrawing only'), ('2020', 'DC for exempt States, continues the 2002 work')),
     bx('pk', '<b>Why a 4th DC in 2002?</b> It only redrew boundaries <b>within States</b>; seat numbers stayed frozen. Exempt: Assam, Manipur, Arunachal, Nagaland, J&amp;K; the <b>2020</b> DC took up these pending States (later J&amp;K).'),
   ]),
 ],
 # ------------------------------------------------------------------ CH 52 EIGHTH SCHEDULE / OFFICIAL LANGUAGES
 52: [
   dict(after='EIGHTH SCHEDULE', nodes=[
     sec('CLASS · Inclusion committees; why Schedule 8 matters', 'r'),
     tb(['Class point', 'Detail'],
        ['<b>Committees</b>', '<b>Pahwa 1996</b>, <b>Mahapatra 2003</b>: neither produced firm criteria for inclusion (languages added on political demand)'],
        ['<b>Art 344</b>', 'official language commission, based on Schedule 8 languages'],
        ['<b>Art 351</b>', 'Union duty to spread and develop <b>Hindi</b> as composite-culture language, drawing on Hindustani and the Schedule 8 languages (mainly Sanskrit)'],
        ['<b>Count</b>', '22 scheduled languages; 11 classical (teacher’s totals)']),
   ]),
   dict(after='SIGNIFICANCE AND CLASSICAL', nodes=[
     sec('CLASS · Classical language criteria and 2024 change', 'r'),
     bx('bl', 'Classical languages = custodians of India’s rich and ancient heritage. <b>Sahitya Akademi</b> linguistic experts committee advises GoI.'),
     tb(['Criterion', 'Original', '2024'],
        ['<b>1</b>', 'high antiquity of early texts, <b>1500-2000 years</b>', 'same'],
        ['<b>2</b>', 'large body of ancient literature valued by generations of speakers', 'same'],
        ['<b>3</b>', 'original literary tradition, not borrowed', '<b>changed:</b> knowledge texts, esp. <b>prose</b>, in addition to poetry; epigraphical and inscriptional text'],
        ['<b>4</b>', 'classical literature distinct from modern and its later forms', 'same']),
     bx('ye', '<b>Class vs handout (benefits):</b> class: Centre of Excellence; <b>UGC awards</b> for writers; UGC chairs in Central Universities. Handout: <b>two international awards</b> (check).'),
   ]),
 ],
}

RECALL = {
 27: [('Bodoland Territorial Council strength?', '46 = 40 elected + 6 nominated'),
      ('Schedules amended by simple majority?', 'I, II, V, VI')],
 34: [('GST compensation base year and growth rate?', '2015-16; 14% a year'),
      ('Mohit Minerals case holding?', 'GST Council recommendations not binding on States')],
 47: [('Kedarnath 1962 on sedition?', 'Upheld 124A but read down: incitement to violence or public disorder'),
      ('Which BNS section replaced 124A?', 'Sec 152'),
      ('Who has right of pre-audience first?', 'Attorney General, then Solicitor General')],
 52: [('Which classical language criterion changed in 2024?', 'No. 3: knowledge texts, esp. prose, added to poetry')],
}
