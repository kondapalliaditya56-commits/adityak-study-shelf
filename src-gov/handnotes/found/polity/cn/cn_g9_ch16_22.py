# -*- coding: utf-8 -*-
from dsl import *
from hwlib import P
OWN = lambda w, h: mn(w, h + ' <i>(own mnemonic)</i>')

ADD = {
# ================================================================== CH 16 PARLIAMENTARY COMMITTEES
16: [
  dict(after='WHY COMMITTEES', nodes=[
    sec('CLASS · Origin and appointment of committees', 'r'),
    t('<b>Committees began</b>', 'Montford reforms, <b>GoI Act 1919</b>',
      t('<b>Five sources</b>', 'Rules of the House (PAC, Estimates)', '<b>Art 344</b>: Official Language Commission, Joint, <b>30</b> = 20 LS + 10 RS, PR + STV', 'Law: <b>Salaries and Allowances of MPs Act 1954</b>, Joint, 10 LS + 5 RS', 'Motion or resolution: usually ad hoc', 'Inherent power of the presiding officer: temporary committees; a joint one by communication between the two presiding officers'), w=22),
    tb(['Appointment', 'Which committees'],
       ['<b>Election</b> (PR + STV)', 'Estimates, PAC, COPU, Welfare of SCs/STs, Official Language'],
       ['<b>Nomination</b>', 'by presiding officer after consulting Leader of the House and Leader of Opposition'],
       ['<b>Motion</b>', 'ad hoc committee; names sometimes already in the motion']),
    bx('pk', '<b>Quorum of a committee = 1/3 of its total members.</b>'),
  ]),
  dict(after='AD HOC COMMITTEES', nodes=[
    sec('CLASS · JPC examples (corruption and scams)', 'g'),
    tb(['Year', 'Joint Parliamentary Committee on'],
       ['<b>1987</b>', 'Bofors scandal'], ['<b>1992</b>', 'Harshad Mehta scam'], ['<b>2001</b>', 'Ketan Parekh scam'],
       ['<b>2004</b>', 'Pesticides in colas (after Centre for Science and Environment report)'], ['<b>2011</b>', '2G scam'], ['<b>2013</b>', 'AgustaWestland helicopter purchase (year as written)']),
  ]),
  dict(after='PUBLIC ACCOUNTS COMMITTEE', nodes=[
    sec('CLASS · PAC: powers, merits, weakness', 'r'),
    t('<b>PAC extras</b>', 'first headed by the <b>Finance Minister</b>; ministers barred after reconstitution; Opposition chair since <b>1967</b>, British convention', 'if RS does not send its 7, PAC still functions (treated as an <b>LS committee</b>)', '<b>Powers</b>: scrutinise CAG report, rule compliance, excess demands, authority for expenditure; <b>enforce production</b> of documents and records; <b>question civil servants</b>', w=22),
    two([t('<b>Merits</b>', 'deterrent on financial misconduct', 'reports shape public opinion', 'Action Taken Report (ATR) shows govt view', '<b>about 3/4</b> of recommendations accepted since independence')],
        [t('<b>Weaknesses</b>', 'deterrent feeble (scams)', 'only a <b>post-mortem</b>', 'huge gap between scam and scrutiny: thousands of CAG audit paras, overburdened 22-member PAC')]),
  ]),
  dict(after='ESTIMATES COMMITTEE', nodes=[
    sec('CLASS · Estimates Committee: extras', 'r'),
    t('<b>Estimates</b>', 'also called <b>twin sister of PAC</b>, continuous economy committee, standing committee on administrative reports', 'reviews <b>5-6 ministries</b> a year; analyses expenditure trends; proposes administrative and efficiency reforms', 'no question on policy unless wasteful: then <b>suggests alternative policy</b>', 'govt acceptance about <b>97%</b>', w=22),
  ]),
  dict(after='COMMITTEE ON PUBLIC UNDERTAKINGS', nodes=[
    sec('CLASS · COPU: report types and weakness', 'r'),
    t('<b>COPU</b>', 'last of the three financial committees (<b>1964</b>); annually elected; PR + STV; written as a committee of the House of the People', t('<b>Two report types</b>', '<b>Vertical</b>: through a report on one PSU', '<b>Horizontal</b>: a specific issue across the whole public sector'), 'tests whether PSUs followed sound business and commercial principles', '<b>Weakness</b>: each PSU gets its turn only after <b>7-8 years</b>; cannot probe all thoroughly', w=22),
  ]),
  dict(after='DEPARTMENT-RELATED STANDING', nodes=[
    sec('CLASS · DRSC: accountability and limit', 'r'),
    t('<b>DRSC extras</b>', '1993, Narasimha Rao govt; 17 at first; <b>nominated</b>, not elected', 'budget role: <b>3rd stage of budgeting</b>; scrutiny of estimates, annual reports, long-term policy documents', '<b>Accountability</b>: minister must present a <b>6-month statement</b> on implementing DRSC recommendations', '<b>Limit</b>: less expert help than PAC (backed by CAG)', w=22),
  ]),
  dict(after='INQUIRY COMMITTEES', nodes=[
    sec('CLASS · Ethics Committee: history', 'r'),
    tl(('1996', 'idea mooted: AIPOC'), ('1997', 'RS sets up'), ('2000', 'LS: ad hoc'), ('2015', 'LS: permanent')),
    bx('bl', '<b>Role:</b> code of conduct of MPs; investigates indiscipline or violation of decorum; suggests action. <b>Complaint</b> by members, or by outsiders with evidence.'),
  ]),
  dict(after='SCRUTINY AND CONTROL', nodes=[
    sec('CLASS · Scrutiny committees: one-liners', 'g'),
    bx('bl', '<b>Papers Laid on the Table:</b> also checks <b>undue delay</b> by govt in tabling reports. <b>Subordinate Legislation:</b> instruments must fit the <b>letter and spirit</b> of the parent law Parliament made.'),
  ]),
  dict(after='PARLIAMENTARY FORUMS', nodes=[
    sec('CLASS · The eight Parliamentary Forums', 'r'),
    tb(['#', 'Forum on', '#', 'Forum on'],
       ['1', 'Water conservation and management', '5', 'Global warming and climate change'],
       ['2', 'Children', '6', 'Disaster management'],
       ['3', 'Youth', '7', 'Artisans and craftspeople'],
       ['4', 'Population and public health', '8', 'MDG to SDG']),
    bx('pk', '<b>Presiding:</b> LS Speaker presides over <b>7</b>; RS Chairman only over <b>Population and Public Health</b> (class list of 8; fills the blank list in the handout).'),
  ]),
  dict(after='ADVANTAGES AND CRITICAL', nodes=[
    sec('CLASS · Bills to committees; trends in working of Parliament', 'g'),
    tl(('15th LS', '71% of Bills to committees'), ('16th LS', '27%'), ('17th LS', '16%')),
    bx('ye', '<b>Class vs handout:</b> class reads 71% / 27% / 16% all as share of tabled Bills sent to committees (handout words 16% as examined); 27% for the 16th LS is the extra. Check wording.'),
    tb(['Trend', 'Class points'],
       ['<b>Committees</b>', 'large majorities dominate nominations; coalition era (<b>1989-2014</b>) gave balance; after <b>2014</b> single-party dominance cut referrals'],
       ['<b>Private Members\' Bills</b>', 'only <b>14</b> passed since 1970, none recently (as written); 1952 Muslim Wakf Bill (Syed Md. Kasmi, as written); <b>1970</b> SC (Enlargement of Criminal Appellate Jurisdiction) Act. Introductions <b>372</b> (15th LS) to about <b>900</b> (16th); under <b>4%</b> debated; used for political statements or to embarrass govt'],
       ['<b>Chair\'s rulings</b>', 'coalition era: Speaker checked govt, protected Opposition; post-2014 adverse rulings reversed by strong majority'],
       ['<b>Meetings behind the chair</b>', 'informal leaders\' meetings in Speaker\'s chamber to break deadlock; rise with disruptions'],
       ['<b>Many parties</b>', '<b>37</b> parties in 17th LS, <b>41</b> in 18th; fragmentation hinders consensus; govt leans on <b>ordinances</b>']),
  ]),
  dict(after='CONSULTATIVE COMMITTEES AND INDIAN', nodes=[
    sec('CLASS · IPG, IPU and CPA', 'r'),
    tb(['Body', 'Class facts'],
       ['<b>Indian Parliamentary Group</b>', 'set up <b>1949</b> by <b>Constituent Assembly resolution</b>; Speaker is President; open to MPs and all ex-MPs. Does: contact between MPs and ex-MPs; debates, seminars; foreign visits of MPs'],
       ['<b>IPU</b>', 'Inter-Parliamentary Union; HQ <b>Geneva</b>; IPG = its national group'],
       ['<b>CPA</b>', 'Commonwealth Parliamentary Association; HQ <b>London</b>']),
    bx('ca', '<span class="tag">Class · Jan 2026</span><b>28th CPA Conference of Presiding Officers:</b> New Delhi, chaired by Om Birla (name partly illegible in class note, verify); <b>61</b> presiding officers attended.'),
  ]),
],

# ================================================================== CH 17 STATE LEGISLATURE
17: [
  dict(after='LEGISLATIVE ASSEMBLY', nodes=[
    sec('CLASS · Art 170: small-State exceptions and readjustment', 'r'),
    tb(['State', 'Minimum', 'Article', 'Seats now'],
       ['<b>Nagaland</b>', '46', '371A (clause 1(h))', '60'],
       ['<b>Mizoram</b>', '40', '371G', '40'],
       ['<b>Sikkim</b>', '30', '371F', '32'],
       ['<b>Arunachal Pradesh</b>', '30', '371H', '60'],
       ['<b>Goa</b>', '30', '371I', '40']),
    bx('ye', '<b>Class vs handout:</b> class note writes Mizoram 371F / 32 seats and Sikkim 371G / 40 seats (columns swapped); table here is corrected (check). Sub-clause letters unclear in class, so omitted.'),
    t('<b>Readjustment rules</b>', 'after <b>every census</b>; Parliament fixes the authority', 'effective only on <b>dissolution</b> of the Assembly; President names the date', 'boundaries on <b>2001 census</b>; total seats on <b>1971 census</b> (frozen, 84th Am)', w=22),
  ]),
  dict(after='LEGISLATIVE COUNCIL', nodes=[
    sec('CLASS · Council: who elects, who presides, utility', 'b'),
    t('<b>Constituencies</b>', 'local bodies, graduates and teachers (3 years\' standing each) elect through <b>territorial constituencies</b>', 'MLA quota (1/3) has no territorial constituency', 'Governor nominates <b>1/6</b>: arts, literature, science, cooperative movement, social service', 'Parliament may provide composition by law', w=22),
    tb(['', 'Rajya Sabha', 'Legislative Council'],
       ['Chair', 'Vice-President, ex officio, not a member', 'Chairman chosen by the Council from its own members (<b>Art 182</b>); no Governor role']),
    bx('ye', '<b>Class vs handout:</b> class bicameral list also names <b>Madhya Pradesh</b> (Council on paper since 1956, 7th Am, not active) and <b>Tamil Nadu</b> (DMK for a 2nd chamber, AIADMK against; 2010 move countered). Handout counts <b>six</b>; use six.'),
    bx('pk', '<b>Art 169 resolutions pending in Parliament:</b> <b>West Bengal (2021)</b>; <b>Odisha, Assam, Rajasthan (2018)</b>. <b>J&amp;K:</b> LA + LC as a State; as a UT only LA.'),
    t('<b>Council: nature and merit</b>', '<b>dilatory chamber</b>: advisory or delaying, no veto; RS is the federal chamber, Council structurally weak', t('<b>2nd ARC</b>', 'every State should have a Council', 'members wholly elected by local bodies (to voice institutions)'),
      t('<b>Utility (6)</b>', 'senior politicians and statesmen', 'stops hasty legislation', 'useful suggestions', 'experts (nominated)', 'special interests represented', 'shares burden of holding govt accountable'), w=22),
    t('<b>Criticism (3)</b>', 'delays legislation', 'very expensive', 'parking ground for defeated politicians and colleagues of the ruling party', w=22),
  ]),
  dict(after='KEY ARTICLES 168', nodes=[
    sec('CLASS · Articles 177, 189, 210: one-liners', 'r'),
    tb(['Art', 'Class point'],
       ['<b>177</b>', 'minister and Advocate-General may speak, attend, take part in <b>any House or legislative committee</b>; <b>no vote</b> except in the House where a member'],
       ['<b>189</b>', 'Houses act despite vacancies; quorum <b>10 or 1/10</b>'],
       ['<b>210</b>', 'language in State legislature: State\'s official language(s), Hindi or English; <b>mother-tongue</b> exception; same as <b>Art 120</b> for Parliament']),
  ]),
],

# ================================================================== CH 18 PARLIAMENTARY SYSTEM
# (Separation of Powers has no chapter of its own; placed beside the presidential system and the Montesquieu note.)
18: [
  dict(after='PRESIDENTIAL SYSTEM', nodes=[
    sec('CLASS · Separation of Powers (SOP)', 'r'),
    bx('bl', '<b>SOP:</b> <b>Montesquieu</b> (18th c., French): <b>L</b>aw-making, <b>E</b>xecution, <b>J</b>udging by separate bodies = checks and balances. <b>Benefits:</b> no absolute power; protects democracy and rights; division of labour and specialisation; public trust; constructive friction, better decisions.'),
    bx('pk', '<b>India overlaps (class):</b> judges appointed by President, removed by Parliament (2/3, impeachment); judicial review of govt; Parliament questions executive (Question Hour).'),
    sec('CLASS · Ten exceptions to SOP in India', 'r'),
    tb(['#', 'Exception', 'Class point'],
       ['1', '<b>Fusion of L and E</b>', 'ministers sit in Parliament; must be MPs; political executive (PM-CoM) above permanent executive (bureaucracy)'],
       ['2', '<b>Delegated legislation</b>', 'Parliament gives skeleton or broad policy (the "helmet"); executive fills shape and size by rules, regulations, bye-laws'],
       ['3', '<b>Administrative adjudication</b>', 'tribunal = judicial + administrative experts; e.g. income tax (technical); CAT, SAT'],
       ['4', '<b>Judicial law-making</b>', '<b>Vishaka 1997</b> guidelines till Parliament legislates; fills gaps, protects FRs'],
       ['5', '<b>Independent regulators</b>', 'TRAI: makes rules (legislative), enforces (executive), penalises (judicial)'],
       ['6', '<b>Ordinances</b>', 'President (on PM) and Governor (on CM) when House not sitting'],
       ['7', '<b>Clemency</b>', '<b>Art 72</b> President, <b>Art 161</b> Governor: pardon = acts as judge'],
       ['8', '<b>Art 143</b>', 'only the President seeks SC advisory opinion on public importance or law'],
       ['9', '<b>President, VP, CJI</b>', 'VP acts in vacancy of President; both vacant: CJI acts (article number unclear in class note)'],
       ['10', '<b>MPLADS</b>', '<b>Rs 5 cr</b> per MP per year (25 cr in 5 years); MPs act as executives; <b>Narasimha Rao 1993</b>']),
    t('<b>Why rigid SOP is impossible</b>', 'administration grows technical', 'speed and efficiency', 'power is a means to public welfare, not property (B.M. Bakshi, class note unclear)', t('<b>Articles showing some separation</b>', '<b>50</b>: separate judiciary from executive in public services', '<b>121</b>: no discussion in Parliament on conduct of SC/HC judges', '<b>211</b>: same in State Legislature', '<b>361</b>: no criminal proceeding against President/Governor in term'), w=24),
  ]),
],

# ================================================================== CH 20 CENTRE-STATE RELATIONS
20: [
  dict(after='LEGISLATIVE RELATIONS: TERRITORY', nodes=[
    sec('CLASS · Art 245-254: extra-territorial law, doctrines, reading the Lists', 'r'),
    bx('bl', '<b>Extra-territorial law:</b> operates beyond India (e.g. laws for NRIs); <b>Maritime Zones Act 1976</b> covers territorial waters, continental shelf, EEZ. <b>Residuary:</b> subject in no list = <b>Entry 97</b>, Union List. <b>Art 246:</b> Union List to Union; Concurrent to both; State List to State.'),
    tb(['Doctrine / rule', 'Case', 'Point'],
       ['<b>Territorial nexus</b>', '<b>State of Bombay v. RMDC, 1957</b>', 'State law may reach outside only with sufficient nexus'],
       ['<b>Pith and substance</b>', '<b>F.N. Balsara, 1951</b>', 'State law valid if in essence on a State subject; trespass on Union List incidental, and Union power unaffected'],
       ['<b>Colourable legislation</b>', '<b>Gajapati Narayan Deo</b>', '"wrong use" of power'],
       ['<b>Same in substance (Art 254)</b>', '<b>Bharat Shanti Lal, 2008</b>', 'Concurrent subject: same content and result, only layout of sections differs: State law valid, no repugnancy; SC raised the threshold of repugnancy']),
    bx('ye', '<b>Class vs handout:</b> class note writes Gajapati Narayan Deo as "1993"; handout gives <b>1953</b> (check).'),
    t('<b>Limits on legislative power (class list of 8)</b>', 'Art 246', 'Art 13(2)', 'Art 245', 'prior sanction', 'Art 240', 'Schedules V and VI', 'colourable legislation', 'delegated legislation: basic policy must be passed and debated by <b>Parliament</b>; an essential function, so not for the bureaucracy', w=26),
    t('<b>Interpreting the Lists</b>', 'SC reads each entry <b>liberally</b>; a general word covers all reasonable subsidiary matters', 'similar subjects sit in different Lists: Union <i>arms and ammunition</i>; State <i>police, public order, prisons</i>; Concurrent <i>criminal law and procedure</i>', 'overlap: <b>harmonise</b> entries first; if not, <b>Union List &gt; Concurrent List</b>, and (Union + Concurrent) &gt; State List', w=26),
  ]),
  dict(after='PARLIAMENT IN THE STATE FIELD', nodes=[
    sec('CLASS · Arts 252, 253 examples; Punchhi on treaties', 'g'),
    tb(['Art', 'Class example'],
       ['<b>252</b>', '<b>Clinical Establishments (Registration and Regulation) Act, 2010</b>: adopted at the request of <b>Sikkim, Himachal Pradesh, Mizoram</b> (class note also shows "2001")'],
       ['<b>253</b>', '<b>2011 Lokpal Bill</b> (UPA-2): Lokpal at Union and State level, from India\'s ratification of the <b>UN Convention against Corruption</b>; later withdrawn']),
    bx('pk', '<b>Punchhi:</b> treaties that touch State List subjects should be negotiated <b>with the States involved</b>.'),
  ]),
  dict(after='ADMINISTRATIVE RELATIONS (Arts', nodes=[
    sec('CLASS · Administrative relations: outline and Union ministries', 'b'),
    t('<b>Six aspects of administrative relations</b> (class outline)', '<b>Central Administrative Directions (CADs)</b>: normal and emergency', 'mutual delegation: <b>Arts 258, 258A</b>', '<b>Art 261</b> full faith and credit', 'position of the Governor', 'All India Services', 'coordinating mechanisms', w=24),
    bx('bl', '<b>Normal-time directions:</b> Arts <b>256, 257, 339(2), 347, 350A</b> (class list). <b>Emergency:</b> 352, 356, 360; disobedience: Art 365.'),
    t('<b>Union ministries on State List subjects</b> (MHA, Agriculture and Farmers\' Welfare, Health and Family Welfare)', '<b>Not a breach of federalism</b>: only basic functions', t('<b>Nine functions</b>', 'initiative and leadership', 'share best practice', 'national policy framework', 'research (ICAR, NDRI: State funds not enough)', 'foundational training (training of trainers)', 'financial support: <b>CSS</b>', 'evaluate CSS impact', 'inter-state coordination platform', 'liaison with international bodies'), w=26),
  ]),
  dict(after='DISTRIBUTION OF TAX RECEIPTS', nodes=[
    sec('CLASS · Taxes: cess, State duties, CST vs IGST, FRBM', 'g'),
    tb(['Tax', 'Art', 'Applies to', 'Basis'],
       ['<b>CST</b> (Central Sales Tax)', '269', 'inter-state goods <b>outside GST</b>', '<b>origin-based</b>'],
       ['<b>IGST</b>', '269A', 'inter-state goods and services under GST', '<b>destination-based</b>']),
    t('<b>Class additions</b>', '<b>Cesses and surcharges</b> (Arts 270, 271): about <b>20%</b> of Centre\'s tax revenue', '<b>Divisible pool (Art 270)</b>: all taxes except cess and surcharge (and 268, 269, 269A), shared on FC percentage', 'States still levy duties <b>outside GST</b> on: crude petroleum, petrol, high speed diesel, natural gas, ATF, alcohol for human consumption', 'grants-in-aid on FC advice; <b>plan grants</b> for five-year plans', '<b>FRBM Act 2003</b>: caps fiscal deficit; States have own FRBM laws', w=26),
  ]),
  dict(after='SARKARIA AND PUNCHHI', nodes=[
    sec('CLASS · Sarkaria and Punchhi on legislative relations', 'g'),
    tb(['Commission', 'Class point'],
       ['<b>Sarkaria</b>', 'Centre has <b>monopolised the Concurrent List</b>; over-centralised. Residuary power on <b>taxation</b> with Centre, other residuary subjects to Concurrent List'],
       ['<b>Punchhi</b>', 'on Concurrent List Parliament should pass only a <b>skeletal (broad) law</b>; use <b>Art 254(2)</b> liberally']),
  ]),
],
# ================================================================== CH 21 INTER-STATE RELATIONS
21: [
  dict(after='ZONAL COUNCILS AND NORTH-EASTERN', nodes=[
    sec('CLASS · Councils: extra facts', 'r'),
    tb(['Body', 'Class facts'],
       ['<b>North-Eastern Council</b>', 'statutory, NEC Act <b>1971</b>; members: <b>CMs and Governors</b> of the 8 States; chairperson + <b>3</b> members nominated by President'],
       ['<b>National Integration Council</b>', '<b>1962</b>'],
       ['<b>GST Council</b>', '<b>Art 279A</b>'],
       ['<b>NDC</b>', 'no longer exists; replaced by the <b>Governing Council of CMs</b>, part of NITI Aayog']),
    bx('ye', '<b>Class vs handout:</b> class writes Zonal Councils as "1958, SRA Act"; handout: <b>1956</b> (check).'),
  ]),
],

# ================================================================== CH 22 EMERGENCY PROVISIONS
22: [
  dict(after='NATIONAL EMERGENCY: GROUNDS', nodes=[
    sec('CLASS · Many National Emergencies at once', 'r'),
    bx('pk', '<b>Art 352(9) (as cited in class):</b> several National Emergencies may run together, each with its own 6-month clock and renewals, and each may rest on a <b>different ground</b>.'),
  ]),
  dict(after='EFFECTS OF NATIONAL EMERGENCY', nodes=[
    sec('CLASS · Neighbouring States and Art 172', 'r'),
    t('<b>Extra effects</b>', '<b>Art 353</b>: if one State is under NE and <b>neighbouring States are affected</b>, Union executive power reaches them too, though not under NE', '<b>Art 83</b> (LS term): one year at a time, never beyond <b>6 months</b> after the Emergency ends', '<b>Art 172</b>: same rule for the State Assembly, by Parliament\'s law', w=22),
    bx('ye', '<b>Class vs handout:</b> class cites "Art 252" for Parliament\'s full power on State List during NE; handout cites <b>353(b)</b> and <b>250</b> (check).'),
  ]),
  dict(after='HISTORICAL USE AND REFORMS', nodes=[
    sec('CLASS · Counts and a 2020 petition', 'b'),
    bx('pk', '<b>Class tally:</b> National Emergency <b>3</b> times (1962, 1971, 1975); Art 356 <b>130+</b>; Art 360 <b>never</b>. <b>1962-68</b> = longest; the 1965 Indo-Pak war needed no new proclamation. NE: Parliament approves imposition, but <b>revocation needs no approval</b> (President acts alone).'),
    bx('ca', '<span class="tag">Class · 2020</span><b>1975 Emergency in the SC:</b> petition (petitioner written as "94 ..." in class note, unclear) asked the Court to declare the 1975 Emergency unconstitutional; noted next to Minerva Mills 1980 (NE is reviewable).'),
  ]),
  dict(after='USE, MISUSE AND REVIEW OF ART 356', nodes=[
    sec('CLASS · Art 356: numbers and Sarkaria on abuse', 'r'),
    tl(('1951', 'Punjab: first'), ('1950-65', '10 times'), ('1965-80', '60 times'), ('1987', 'Punjab: 5 years'), ('1990 on', 'sharp decline')),
    bx('bl', '<b>State-wise:</b> Manipur <b>11</b> times; UP <b>10</b>. Use and abuse tracked the rise of political divides in India.'),
    t('<b>Sarkaria: observations</b>', 'dozens of cases where a ruling party with <b>clear majority</b> was dismissed', 'examples: <b>1977</b> nine Congress States after LS defeat; <b>1976</b> Tamil Nadu and <b>1979</b> Manipur: "poor administration"', 'only <b>26</b> uses found justified (mostly State reorganisation)', w=24),
    OWN('ROAD', '<b>R</b>eport dictated by Centre (Governor\'s adverse report at Centre\'s behest) · <b>O</b>pposition not allowed to try forming govt · <b>A</b>ssembly suspended or dissolved for ruling-party convenience · <b>D</b>efinition missing for "breakdown of constitutional machinery". The four problems with Art 356.'),
    fl(['Warn the State', 'Exhaust other means', 'State-specific NE (Art 352) if armed rebellion or public disorder', 'Then President\'s Rule'], 'Sarkaria: ladder before Art 356', 4),
    bx('pk', '<b>Also Sarkaria:</b> dead letter, rarely used; be patient when a State loses majority; imposition must rest on a <b>speaking, public, evidence-based</b> report.'),
    sec('CLASS · Bommai 1994: more guidelines; why 356 stays', 'b'),
    t('<b>S.R. Bommai (1994) extras</b>', 'two basic features: <b>federalism and democracy</b>; 356 must strengthen both', 'strong evidence needed; courts examine it; if irrelevant, <b>revive dissolved govt</b>', '<b>no wholesale dismissal</b> of State govts', 'Assembly not dissolved until Parliament approves; if refused, <b>revived</b> and govt restored', 'majority test in the <b>House</b>, not Governor\'s house; CM gets chance to prove it; then explore alternative govt', 'breakdown of <b>constitutional</b> machinery (State works against the Constitution) is not breakdown of <b>administrative</b> machinery (poor administration)', w=26),
    tb(['Art 356 cannot rest on', 'Can be used when'],
       ['poor administration; corruption allegation; no prior warning; Governor recommending without exploring alternatives; poor <b>finances</b> of the State', 'no govt formed even after fresh election and all options; State not following the Constitution (against secularism)']),
    bx('bl', '<b>Why 356 is still needed (teacher):</b> <b>Indian Independence Act 1947</b> ended GoI Act 1935 as working Constitution; the <b>India (Provisional Constitution) Order</b> (class writes 1977, read as 1947, check) copied the 1935 Act minus <b>Sec 93</b> (provincial emergency). Leaders held India together without it. Answer: the system is now used to the Article; removing it would leave a dangerous vacuum.'),
    bx('gr', '<b>PYQ frame: explain suspension and dissolution with reasons.</b> <b>Intro:</b> Art 356 and Bommai 1994 (federalism, democracy basic). <b>Points:</b> (1) suspension: Assembly kept alive till Parliament approves, revived if refused (2) dissolution only after approval (3) test majority on the floor (4) misuse fell after 1990: <b>coalition culture</b> (Centre needs regional parties), <b>Bommai</b>, <b>presidential checks</b>, <b>public awareness</b>, <b>media</b> (5) <b>NCRWC</b> repeats Sarkaria and Bommai. <b>Close:</b> last resort, reasoned, reviewable.'),
  ]),
],
}

RECALL = {
 16: [('Ethics Committee history?', 'idea AIPOC 1996; RS 1997; LS 2000 ad hoc; permanent 2015'),
      ('Share of recommendations accepted: PAC and Estimates?', 'PAC about 3/4; Estimates about 97%'),
      ('Which forum does RS Chairman preside over; how many does Speaker?', 'Population and Public Health; 7 of 8'),
      ('Parties in 17th and 18th LS?', '37 and 41')],
 20: [('Pith and substance; colourable legislation cases?', 'F.N. Balsara 1951; Gajapati Narayan Deo (handout 1953)'),
      ('CST vs IGST?', 'CST Art 269, origin-based, outside GST; IGST Art 269A, destination-based'),
      ('Duties States keep outside GST?', 'crude petroleum, petrol, HSD, natural gas, ATF, alcohol for human consumption'),
      ('Union List vs Concurrent vs State overlap rule?', 'harmonise; else Union > Concurrent; (Union + Concurrent) > State')],
 22: [('Emergency tally?', 'NE 3 (1962, 1971, 1975); Art 356 130+, Punjab 1951 first, Manipur 11, UP 10; Art 360 never'),
      ('Sarkaria four problems of Art 356 (ROAD)?', 'Report at Centre\'s behest; Opposition not allowed; Assembly for convenience; Definition missing'),
      ('Bommai: constitutional vs administrative breakdown?', 'Only the first (State against the Constitution) justifies 356'),
      ('Why Art 356 misuse fell after 1990?', 'Coalitions, Bommai, presidential checks, awareness, media')],
 18: [('Exceptions to separation of powers: name six?', 'Fusion, delegated legislation, adjudication, judicial law-making (Vishaka 1997), regulators (TRAI), ordinances'),
      ('Articles showing some separation?', '50, 121, 211, 361')],
}
