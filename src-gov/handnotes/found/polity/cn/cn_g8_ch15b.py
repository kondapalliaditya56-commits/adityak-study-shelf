# -*- coding: utf-8 -*-
from dsl import *
from hwlib import P
OWN = lambda w, h: mn(w, h + ' <i>(own mnemonic)</i>')
# Class-note additions for chapter 15 (Parliament), second half of the extract (file A10 pages a-238 to a-258).
# All entries belong to ch15 (Parliament); courts are not involved in this half.
ADD = {
 15: [
  # ---------------- women: after the existing 106th Am block (section 11) ----------------
  dict(after='QUALIFICATIONS FOR MEMBERSHIP', nodes=[
    sec('CLASS · Women in Parliament: data, quota history, 106th Am', 'r'),
    tb(['Women MPs', 'Figure'], ['18th LS', '74 (14%)'], ['17th LS', '78 (15%)'], ['Rajya Sabha', 'about 10%'], ['State Assemblies', 'average 9-10%'], ['Global average (apex houses)', '26%']),
    t('<b>Women MPs: who and issues</b>', 'mostly from <b>political families</b>; some student politics; upper-class professionals (lawyers)', 'few grassroots activists (e.g. Brinda Karat)', 'women\'s movement <b>divided</b>: outside groups (atrocities, violations) vs MPs who put <b>party</b> interest first'),
    t('<b>Quota history</b>', 'Constituent Assembly: most women members <b>opposed</b> quota (stigma, hope, party sensitivity, clean politics)', 'expectations unmet: debate revived <b>1990s</b>; Bills <b>1996, 1998, 1999</b> lapsed', t('<b>108th Am Bill 2008</b>', 'passed by <b>RS 2010</b>, lapsed with 15th LS', '1/3 seats; 1/3 sub-quota SC/ST; rotation')),
    t('<b>106th Am (Nari Shakti Vandan Adhiniyam) 2023: class adds</b>', '<b>1/3 of SC/ST reserved seats</b> go to women; applies to LS, State Assemblies, Delhi', 'effective only after <b>census + delimitation</b>; rotation after each delimitation', '<b>15 years</b>, Parliament can extend by law', t('<b>Articles</b>', '<b>330A</b> LS 1/3', '<b>332A</b> State Assemblies', '<b>334A</b> commencement, after delimitation, up to 15 years', '<b>239AA</b> NCT Delhi 1/3'), '<b>Puducherry:</b> Govt of UTs Act 1963 amended 2023; <b>J&amp;K:</b> J&amp;K (Reorganisation) Second Amendment Act 2023: 1/3 each', 'class reform demand: implement <b>without waiting for delimitation</b> (not 2029 otherwise)'),
    t('<b>Issues with women\'s quota</b>', 'perpetuates unequal status; <b>proxy candidates</b>; resistance to women on general seats', 'restricts voter choice (popular men barred)', 'palliative, short-term; ignores socio-economic roots', 'rotation cuts incentive to nurture a constituency', 'Bill silent on <b>Upper House</b> quota'),
    bx('gr', '<b>Teacher\'s writing task (frame built from class points):</b> (1) <i>Quality of Opposition:</i> intro = role (accountability, alternatives, agenda); 3-5 problems (composition, reactive, short-term pay-offs, disunity, weak parties); close = shadow-cabinet-like specialisation. (2) <i>Women\'s representation:</i> intro = 14% vs 26% global; measures = quota with rotation fixes, party tickets, grassroots training, curb proxies; close = Rwanda-style norm.'),
  ]),
  # ---------------- size of the House (section 8: composition) ----------------
  dict(after='PARLIAMENT AND COMPOSITION', nodes=[
    sec('CLASS · Size of the House: inadequate representation', 'r'),
    tb(['Year / country', 'Population : MPs'], ['1971', '54 crore : 543'], ['2011', '121 crore : 543'], ['2026', '140+ crore : 543 (about <b>1 MP per 25 lakh</b>)'], ['UK Commons', '6.5 crore : 650']),
    bx('ye', '<b>Unequal representation:</b> Malkajgiri (Telangana) about <b>30 lakh</b> vs Lakshadweep about <b>49,000</b>. <b>Against enlarging:</b> harder to manage, less time to speak, more constituencies, more expenditure.'),
  ]),
  # ---------------- leaders: LoO, whips, secretary-general ----------------
  dict(after='CHAIRMAN, DEPUTY CHAIRMAN, LEADERS', nodes=[
    sec('CLASS · Leader of Opposition: the 10% rule', 'r'),
    bx('pk', '<b>10% criterion:</b> <b>Direction 121</b> by first Speaker <b>G.V. Mavalankar</b>. Why 10%: equals <b>quorum</b>, so opposition can hold a sitting if ruling party is absent. UK = Shadow PM.'),
    tl(('1952-69', 'no LoO'), ('1969', 'Ram Subhag Singh (Cong-O), LS'), ('1971-77', 'none'), ('1980-89', 'none'), ('1989-2014', '9th-15th LS: LoO'), ('16th, 17th LS', 'none qualified')),
    bx('ye', '<b>Issue:</b> a Speaker\'s direction cannot override a <b>law of Parliament</b> (1977 Act). Law-made bodies (<b>NHRC, CVC, CBI Director, CIC, Lokpal, ECI</b>) need LoO on selection panels: if none, <b>leader of single largest opposition party</b> sits. LoO presents lapses and alternatives but cannot enforce; answerable to the whole nation.'),
    sec('CLASS · Role of opposition and its problems', 'r'),
    t('<b>Role (5)</b>', 'hold govt accountable', 'question, sometimes confront', 'shape public opinion', 'alternative views', 'shape govt agenda'),
    t('<b>Problems securing effective opposition</b>', 'party composition of LS', '<b>reactive</b>, depends on media for information', 'short-term pay-off issues; governance neglected', 'lack of unity', '<b>flimsy parties</b>: no shadow cabinet (UK), no ideological filters, unstable affiliation'),
    sec('CLASS · Secretary-General, recognised party, whips', 'r'),
    bx('bl', '<b>Art 98:</b> each House has its own secretariat. <b>Secretary-General</b> = rank of Cabinet Secretary; appointed by presiding officer after consulting <b>Leader of House + LoO</b>; all notices addressed to S-G; custodian of papers and records.'),
    tb(['Leaders and Chief Whips Act 1998', 'RS', 'LS'], ['Recognised <b>group</b>', '15 to 24 members', '30 to 54'], ['Recognised <b>party</b> (not the EC test)', '25 or more', '55 or more']),
    tb(['Whip', 'Binding?'], ['One-line', 'non-binding notice; may abstain'], ['Two-line', 'attendance compulsory; vote optional'], ['Three-line', 'binding: attend and vote as directed']),
    bx('bl', '<b>All India Conference of Chief Whips:</b> Ministry of Parliamentary Affairs; 1st <b>Indore 1952</b>; 18th <b>Udaipur 2018</b>.'),
  ]),
  # ---------------- sessions: suspension, expunging, secret sitting, prorogation extras ----------------
  dict(after='SESSIONS, QUORUM, VOTING', nodes=[
    sec('CLASS · Suspension of MPs, expunging, secret sitting', 'r'),
    t('<b>Disciplining a member</b>', '<b>Naming:</b> PO draws House\'s attention to unruly member', '<b>Rule 373 (LS):</b> Speaker directs withdrawal for the day; <b>Rule 255 (RS)</b> similar', t('<b>Long suspension</b>', 'before <b>2001</b>: House collectively suspended', 'after 2001: <b>Rule 374-A (LS)</b> (digits unclear, verify): named member auto-suspended <b>5 sittings or rest of session</b>', 'revoked only by <b>House resolution</b>, not Speaker', '<b>RS Chairman has no power to suspend</b>')),
    tb(['Period', 'MPs suspended'], ['2006-2014', '51'], ['2015-2022', '139'], ['Winter Session 2023', '143']),
    bx('pk', '<b>Ashish Shelar case, 2022:</b> Maharashtra Assembly (MVA govt) suspended <b>12 BJP MLAs for 1 year</b> (2021); SC held it <b>unconstitutional</b>: suspension cannot exceed <b>the remainder of the session</b>.'),
    bx('ye', '<b>Effects:</b> cannot enter House, loses minister\'s reply to his question, cannot give notice. <b>Problems:</b> Bills passed without debate; constituency unrepresented; chills free speech.'),
    tb(['Device', 'Rule and detail'], ['<b>Expunging</b> remarks', 'LS <b>Rule 380</b>, RS <b>Rule 261</b>; Speakers publish lists of unparliamentary words (list recently issued)'], ['<b>Secret sitting</b>', 'LS <b>Rule 248</b> (RS rule unclear); outsiders, media, gallery barred; first in <b>1948</b> (class page names M.S. Aney, verify); Chhattisgarh Assembly <b>2007</b>']),
    sec('CLASS · Prorogation and dissolution: what survives', 'r'),
    bx('pk', '<b>Prorogation:</b> pending business <b>shifts to next session</b>. <b>Dissolution:</b> all pending LS business lapses, including LS-passed Bill pending in RS. <b>Do not lapse:</b> assurances pending with <b>Committee on Government Assurances</b>; Bills passed by both Houses awaiting assent; Bills returned by President; Bills where <b>joint sitting</b> was already called.'),
  ]),
  # ---------------- Question Hour, motions ----------------
  dict(after='QUESTION HOUR, ZERO HOUR, MOTIONS', nodes=[
    sec('CLASS · Question Hour: origin, colours, utility, problems', 'r'),
    bx('pk', '<b>Interpellation</b> via Question Hour: <b>Indian Councils Act 1892</b>. First hour, about 11 to 12. <b>No Question Hour:</b> President\'s address; Budget day; (holiday/extended sitting, class wording unclear). <b>First suspension ever: Monsoon Session 2020.</b>'),
    tb(['Question', 'Class detail'], ['<b>Starred</b>', 'oral answer, supplementaries; list on <b>GREEN</b> paper'], ['<b>Unstarred</b>', 'written reply, no supplementaries; <b>WHITE</b> paper'], ['<b>Short notice</b>', 'urgent public importance; notice under 10 days'], ['<b>To private members</b>', 'only on their own Bill, resolution or motion; if evaded, petition to presiding officer, whose decision is final']),
    t('<b>Utility</b>', 'deterrent on govt', 'accountability of ministers and civil servants', 'exposes lapses; shapes opinion', 'tool to know govt stand', 'tool to embarrass govt'),
    t('<b>Problems</b>', 'only <b>30-45%</b> answered; 15th LS about 10% (class figure, verify)', '"cash for query" scams; absenteeism', 'first casualty of disruption (well, slogans)', 'about <b>70%</b> of questions obtainable via RTI', 'fix: <b>Hamid Ansari</b> suggested shifting to <b>3 PM</b>'),
    sec('CLASS · Zero Hour: class details', 'r'),
    bx('bl', '<b>Unwritten, not in rules</b>, convention only; no point of order allowed. Regular since the <b>1960s</b>, fills gap before 1 PM lunch. Matter needs no notice but <b>notice by 10 AM</b> to presiding officer for time management. Minister replies if present. 15 min to 1 hour, timing by Speaker/Chairman.'),
    bx('ye', '<b>Class vs handout:</b> class writes RS rule as <b>"180AA"</b> (special mention); handout says RS <b>Rule 180-E</b> (check). LS Rule 377 agrees.'),
    sec('CLASS · Motions: classification, admission, no-confidence, trust', 'r'),
    tb(['Motion', 'Class meaning and example'], ['Substantive', 'self-contained: no-confidence, adjournment'], ['Subsidiary', 'arises from an earlier motion: referring a Bill to committee'], ['Substitute', 'replaces an existing motion with an alternative'], ['Closure', 'ends debate, immediate vote: simple, kangaroo, compartments, guillotine'], ['Privilege', 'against a minister giving misleading or false information'], ['Dilatory', 'to delay or postpone House business'], ['No Day Yet Named', 'admitted, but no date appointed'], ['Censure', 'LS only; specific reasons; individual minister or whole govt']),
    t('<b>Adjournment motion (Rule 56): 7 conditions</b>', 'urgent, national importance', 'govt responsibility', 'no privilege question', 'specific', 'no revival of same-session debate', 'not sub-judice', 'support of <b>50 LS MPs</b>', 'then admission by Speaker; min <b>2.5 hrs</b>; if passed = <b>censure</b> of govt'),
    t('<b>No-confidence motion</b>', 'not named in Constitution: <b>Art 75(3)</b> + <b>Rule 198</b>', t('<b>Conditions</b>', 'LS only; once per session', 'against <b>whole</b> government', '<b>50 members</b> support; no grounds needed'), 'if admitted: debate and vote within <b>10 days</b>'),
    bx('pk', '<b>History:</b> first <b>1963</b> by <b>Acharya Kripalani</b> vs Nehru; <b>27</b> since independence (15 vs Indira Gandhi); <b>none succeeded</b>. Vajpayee, Deve Gowda, V.P. Singh fell on the <b>trust vote</b>, not a no-confidence motion.'),
    t('<b>Trust vote (confidence motion)</b>', 'sought by govt/PM to prove LS majority', 'under <b>Rule 184</b> (debate with vote); <b>Rule 193</b> = debate without vote', t('<b>PMs</b>', 'Charan Singh: resigned unfaced <b>1979</b>', 'V.P. Singh: lost <b>1990</b>', 'Vajpayee: resigned <b>1996</b>; lost by one vote <b>1999</b>', 'Deve Gowda: lost <b>1997</b>')),
    sec('CLASS · Resolutions and short devices', 'r'),
    bx('bl', '<b>Resolution</b> states House opinion; all resolutions are <b>voted</b> (some motions pass without a vote). <b>Statutory resolutions:</b> removal of judges, CAG. <b>Half-hour:</b> 3 days a week, clarifies a minister\'s answer. <b>Short duration:</b> 2 days a week, 1-2 hours. <b>Calling attention:</b> Indian innovation.'),
  ]),
  # ---------------- budget ----------------
  dict(after='UNION BUDGET, GRANTS', nodes=[
    sec('CLASS · Budget sectors and six-tier accounts', 'r'),
    t('<b>Budget: 4 sectors</b>', 'General services (defence, fiscal)', 'Social/community (health, education)', 'Economic (industry, transport)', 'Grants-in-aid and others'),
    tb(['Tier', 'Head', 'Example'], ['1', '<b>Major head</b> = function', 'Education'], ['2', '<b>Sub-major</b> = sub-function', 'Primary education'], ['3', '<b>Minor</b> = programme', 'Govt primary school'], ['4', '<b>Sub head</b> = scheme', 'scheme'], ['5', '<b>Detailed sub head</b> = sub-scheme', 'Salary and allowances'], ['6', '<b>Object head</b> = object of spending', 'TA, DA']),
    bx('pk', '<b>Re-appropriation:</b> shifting money from a head with surplus to one with deficit. Higher tier: <b>Parliament</b> approval through a <b>token demand of Re 1</b>; lower tier: executive via Finance Ministry. Class example: Rs 100 cr = A 50 + B 50; B = C 30 + D 20; D = E 10 + F 5 + G 5.'),
    bx('ye', '<b>FRBM Act 2003:</b> class lists <b>4</b> statements with the budget: Medium-term Fiscal Policy, <b>Medium-term Expenditure Framework</b> (extra), Fiscal Policy Strategy, Macro-economic Framework. Handout lists three.'),
  ]),
  # ---------------- functions and control inadequacies (section 20) ----------------
  dict(after='ROLE OF PARLIAMENT', nodes=[
    sec('CLASS · Functions, control means, inadequacies', 'r'),
    bx('bl', '<b>Extra functions (class):</b> <b>national unity</b> (microcosm), link people-govt, <b>quasi-judicial</b>, electoral, <b>organ of information</b> (RTI Act gives citizens authentic information). <b>Control means:</b> QH, Zero Hour, President\'s speech, debates, budget, committees, privileges.'),
    t('<b>10 inadequacies of control (* = new in class)</b>', '*technical govt, layman Parliament', '*committee problems', 'delegated legislation', '*falling debate quality', '*QH: absenteeism, cash-for-query, disruption', '*few sittings', '*fragmented opposition', '*majority and leadership shifted to executive (creation dominates creator)', 'ordinances', 'guillotine'),
  ]),
  # ---------------- RS (section 22) ----------------
  dict(after='RAJYA SABHA: PARITY', nodes=[
    sec('CLASS · LS and RS special features; second chamber; RS critique', 'r'),
    two([t('<b>LS special</b>', 'Council responsible to LS (<b>Art 75(3)</b>)', 'Money Bills', 'joint sitting: Speaker presides, numbers favour LS', 'predominates in joint committees', 'can revoke National Emergency (Art 352, class)')], [t('<b>RS special</b>', 'no dissolution; <b>1/3 retire every 2 years</b>', 'RPA 1951: <b>Sec 154</b> (RS) and <b>Sec 156</b> (Council) fix 6-year term', 'continuity: composition does not change overnight')]),
    t('<b>Why a second chamber</b>', 'tradition (House of Lords)', 'federalism (RS, US Senate)', 'review: calm, stops hurried law', '<b>functional representation</b>: LS territorial; RS class/occupation; <b>12 nominated</b> experts', 'groups otherwise unrepresented'),
    bx('pk', '<b>Utility:</b> senior statesmen; "<b>House of Correction</b>" vs LS "<b>House of Passions</b>"; guards Constitution from being a plaything of ruling party; Council of States in union decisions; intellectuals.'),
    t('<b>Critique of RS</b>', 'not as weak as Lords, not as strong as US Senate', '<b>non-federal</b>: domicile rule removed <b>2003</b>; nominees; weak money powers; unequal state seats; UTs represented', 'party representation replaced states\' voice', 'revisory role: only <b>3 deadlocks</b> in 75 years', '"pale shadow of LS"; Hamid Ansari: "Federation of Anarchists" (as noted)', 'could not stop <b>42nd Am</b> ("mini Constitution")', 'ordinary Bills passed as <b>Money Bills</b> bypass RS'),
  ]),
  # ---------------- limits / problems (section 24) ----------------
  dict(after='LIMITS ON PARLIAMENT', nodes=[
    sec('CLASS · Sovereignty vs supremacy; problems of Parliament', 'r'),
    bx('pk', '<b>Teacher\'s line:</b> India practises <b>parliamentary supremacy</b>, not parliamentary sovereignty. Sovereignty = uncontrolled law-making, courts cannot strike laws; UK: no constitutional/ordinary distinction, yet a "myth" given conventions and public opinion. India adds a <b>5th limit: Basic Structure</b> (Art 13(2) is the 4th).'),
    tb(['Sitting days', 'Class data'], ['1950s', '127 days'], ['last 10 years', '67 days'], ['Recommended', '<b>120</b> LS, <b>100</b> RS']),
    bx('bl', '<b>Calendar:</b> UK/USA have a pre-set, pre-announced calendar; India\'s ruling party controls timing. Suggestion: Parliament convened on written notice of a set % of MPs (class figure unclear, 30%?).'),
    t('<b>Disruption</b>', 'Nehru era: tolerance for debate; later brute majorities', 'methods: storming the well, slogans, walkouts', '<b>15th LS:</b> most disrupted, <b>40%</b> time wasted, <b>179</b> Bills', 'opposition complains: no role in House agenda or rules (Rules 184, 193)'),
    t('<b>Instability and fixes</b>', 'stable to <b>1989</b>; unstable <b>1989-99</b> (5 elections: 1989, 91, 96, 98, 99)', '<b>1999-2014</b> NDA vs UPA bipolar; 2014 single-party majority', 'fix 1: <b>Rule 198</b> change, no-confidence once a <b>year</b>', 'fix 2: <b>constructive no-confidence</b> (Germany, Art 67 Basic Law): replacement must be agreed first'),
    sec('CLASS · Expenses on Parliament', 'r'),
    t('<b>Salaries: Arts 106 and 195</b>', '<b>Art 106:</b> Parliament fixes by law; till then Constituent Assembly rates', '<b>Art 195:</b> State legislatures fix; till then Provincial Assembly rates', 'Salary, Allowances and Pension of MPs <b>Act 1954</b>; Joint Committee (<b>10 LS + 5 RS</b>)', '<b>2018:</b> revision every <b>5 years</b> by Cost Inflation Index'),
    tb(['2025 (class)', 'Old', 'New'], ['Constituency allowance', '70K', '87,000'], ['Office allowance', '60K', '75,000'], ['Daily allowance', '2K', '2,500'], ['Pension (after 5 yrs)', '25K', '31K; plus 2.5K per extra year (was 2K)']),
    tb(['Country', 'Parliament cost (class)'], ['India', 'Rs 1,000-1,500 cr a year'], ['Japan', 'USD 1.71 bn'], ['USA', 'USD 5-12 bn; Senate salary USD 174,000'], ['UK', '<b>IPSA</b> recommends pay and allowances']),
    bx('bl', '<b>LARRDIS</b> (Library, Reference, Research, Documentation and Information Service): helps MPs; <b>231</b> staffers. Basic salary Rs 1.24 lakh/month.'),
  ]),
 ],
}
RECALL = {
 15: [
  ('Adjournment motion: rule, supporters, minimum debate?', 'Rule 56; 50 LS MPs; 2.5 hours; LS only'),
  ('First no-confidence motion, and how many succeeded?', '1963 Kripalani vs Nehru; 27 so far, none succeeded'),
  ('Recognised party vs group (Act 1998)?', 'Party: 55 LS / 25 RS; group: 30-54 LS / 15-24 RS'),
  ('Ashish Shelar case 2022 held?', 'One-year suspension of 12 BJP MLAs unconstitutional; limit = rest of session'),
 ],
}
