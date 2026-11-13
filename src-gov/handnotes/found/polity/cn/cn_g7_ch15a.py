# -*- coding: utf-8 -*-
from dsl import *
from hwlib import P
OWN = lambda w, h: mn(w, h + ' <i>(own mnemonic)</i>')
# Class-note additions for chapter 15 (Parliament and courts below the SC), first half:
# HC set-up, subordinate courts, tribunals, Lok Adalat, consumer protection, Houses, members, presiding officers,
# Bills, Budget. Courts entries belong to ch 15 (the handout keeps HCs, tribunals, Lok Adalats, consumer commissions there).
ADD = {
 15: [
  # ------------------------------------------------------------ HC set-up
  dict(after='HIGH COURTS: ORGANISATION', nodes=[
    sec('CLASS · HC set-up, strength, age', 'r'),
    tb(['Article (class bare-act list)', 'Subject'],
       ['<b>214</b>', 'a High Court for each State'],
       ['<b>230</b>', 'extends HC jurisdiction to a UT <i>(not in handout; general knowledge, verify)</i>'],
       ['<b>231</b>', 'common HC for two or more States / State + UT'],
       ['<b>241(1)</b>', 'Parliament may constitute a HC for a UT <i>(not in handout; general knowledge, verify)</i>']),
    bx('bl', '<b>Delhi HC 1966</b>; before that Delhi came under the <b>Punjab and Haryana HC</b>. J&amp;K and Ladakh share one HC.'),
    tb(['Strength fixed by', 'How'],
       ['<b>High Court</b> (Arts 215, 216 in class note)', '<b>executive order</b> of Govt of India is enough'],
       ['<b>Supreme Court</b>', 'only <b>Parliament by law</b>']),
    tb(['Retirement age', 'Age'], ['Supreme Court', '<b>65</b>'], ['High Court (Art 217)', '<b>62</b>: raised by <b>15th Am 1963</b> from <b>60</b>']),
    bx('pk', '<b>Additional judges (Art 224):</b> 2 years as additional judge is the experience route to a <b>permanent</b> HC judgeship. Class lists <b>Arts 219, 222, 223, 224, 224A</b> together.'),
    bx('ye', '<b>Date check:</b> class writes "before 99th AA, 2015" beside the Art 217 consultation list; the 99th Am / NJAC Act is dated <b>2014</b>, struck down <b>2015</b>.'),
  ]),
  # ------------------------------------------------------------ HC powers
  dict(after='HIGH COURTS: POWERS', nodes=[
    sec('CLASS · HC jurisdiction: extras', 'r'),
    bx('pk', '<b>Original (class list):</b> electoral disputes · <b>contempt matters</b> · FR cases (Art 226) · <b>admiralty</b> (maritime law, law of the seas) · revenue. New against the notes: <b>contempt</b> and <b>admiralty</b>. Bombay, Calcutta, Madras + Delhi: original civil jurisdiction in higher-value cases.'),
    t('<b>Appellate (most of HC work)</b>', '<b>1st appeal</b> (from district and sub-courts): on <b>law or fact</b>', '<b>2nd appeal</b>: only <b>question of law</b>, not fact', 'state tribunals: HC appellate jurisdiction after <b>L. Chandra Kumar (1997)</b>', w=22),
    bx('bl', '<b>Supervisory Art 227</b>; class also notes <b>Arts 228, 229</b> (228: constitutional-question cases withdrawn to HC; 229: HC officers and expenses; general knowledge, verify). <b>Sheriff</b> = nominal position only (class).'),
  ]),
  # ------------------------------------------------------------ subordinate courts, tribunals
  dict(after='SUBORDINATE COURTS AND TRIBUNALS', nodes=[
    sec('CLASS · District judiciary and quasi-judicial bodies', 'r'),
    bx('bl', '<b>Criminal ladder:</b> Magistrate courts try the <b>majority</b> of criminal cases; <b>Sessions Court</b> = highest criminal court in the district; cases go <b>Magistrate to Sessions</b>. HC = main authority over district courts. Class bare-act list: <b>Arts 233, 236, 234, 233A</b>.'),
    bx('pk', '<b>All India Judges Association case, 2025:</b> minimum <b>3 years\' practice as advocate</b> needed to appear for the state judicial service examination.'),
    t('<b>Quasi-judicial bodies (QJP)</b>', 'outside ordinary courts; given powers, duties like SC, HC, district courts', t('<b>With adjudicatory power</b> (decide like courts)', 'Consumer Commission', 'Information Commission', 'Administrative Tribunals'), t('<b>Without adjudicatory power</b>', 'NHRC, NCST, NCBC', 'judicial, administrative or expert members'), w=24),
    tl(('1941', '<b>Income Tax Tribunal</b>: first administrative tribunal'), ('1976', '<b>42nd Am</b>: Part XIV-A, Arts 323A, 323B'), ('1997', '<b>Chandra Kumar</b>: clause (d) of both struck; HC Division Bench (2 judges) hears')),
    bx('bl', '<b>Under 323A (class):</b> authorities outside the ordinary court system that interpret and apply laws when govt acts are challenged in formal suits or other established methods. <b>R. Gandhi case:</b> tribunals may be set up in areas beyond those in Art 323B (year not noted in class).'),
    tb(['Why tribunals (class)', 'Point'], ['a', 'growing <b>technicality</b> of govt functions'], ['b', 'relief to ordinary courts'], ['c', '<b>speedy</b> judgement'], ['also', 'faster procedures · laws applied in a socially relevant manner']),
  ]),
  # ------------------------------------------------------------ Lok Adalat
  dict(after='LOK ADALATS AND LEGAL SERVICES', nodes=[
    sec('CLASS · Legal aid: extras', 'r'),
    bx('pk', '<b>LSA Act 1987 core functions</b> also include undertaking <b>social-justice litigation</b>. Structure: NALSA, SLSAs, DLSAs, Taluk committee; <b>Sec 19</b> = organisation of Lok Adalats (usually civil, compoundable cases).'),
    bx('ye', '<b>Class vs handout (income limit):</b> class says <b>Rs 3 lakh</b> for district and HC level (State govt) and <b>Rs 5 lakh</b> for the SC (Central govt); handout says Rs 1,00,000 general, Rs 5,00,000 for the SC committee (check).'),
  ]),
  # ------------------------------------------------------------ consumer (end of sec 7)
  dict(after='GRAM NYAYALAYAS', nodes=[
    sec('CLASS · Consumer protection: rights, CCPA, councils', 'r'),
    tb(['Six consumer rights (class order)', 'Keyword'],
       ['1', 'protection against goods and services <b>hazardous</b> to life and property'],
       ['2', '<b>information</b> on quality, quantity, purity, standard, price'],
       ['3', '<b>access</b> to a variety of goods and services at competitive prices'],
       ['4', '<b>redressal</b> against unfair and restrictive trade practices'],
       ['5', 'to be <b>heard</b>; interests considered at appropriate fora'],
       ['6', 'consumer <b>awareness</b>']),
    bx('bl', '<b>Tiers:</b> <b>DCDRC</b> (District), <b>SCDRC</b> (State), <b>NCDRC</b> (National) Consumer Disputes Redressal Commission; each can <b>review</b>; <b>mediation</b> option; complaint can be filed <b>from anywhere</b> (e-commerce).'),
    t('<b>Product liability and e-commerce</b>', '<b>product liability:</b> compensation for injury or property loss from faulty products; the three tiers can order it', t('<b>E-commerce duties</b>', 'give information: return, refund, exchange, warranty, <b>grievance redress mechanism</b>, country of origin', 'acknowledge complaint in <b>48 hours</b>, redress in <b>30 days</b>'), w=24),
    t('<b>CCPA powers</b> (Central Consumer Protection Authority)', '<b>recall</b> goods', 'recall <b>misleading ads</b> (penalties, also on endorsers)', '<b>class action</b> suits', '<b>investigate</b> large-scale violations', 'appeal against CCPA goes to the <b>National Commission</b>', w=24),
    bx('bl', '<b>Parens patriae:</b> govt files the case where many affected persons cannot come together; e.g. govt case against <b>Nestle</b>.'),
    fl(['NCPC: Minister of Consumer Affairs', 'SCPC: State Minister', 'DCPC: headed by the DM', 'Advise govt on promotion and protection of consumer rights'], 'Consumer Protection Councils (advisory, 3 tiers)', 4),
    tb(['Procedure number', 'Value'], ['Limitation to file complaint', '<b>2 years</b>'], ['Online complaint', '<b>Jago Grahak Jago</b>'], ['Jail for offences', '<b>1 month to 3 years</b> (with or without fine)'], ['Disposal time', '<b>3 months</b> (no testing) · <b>5 months</b> (testing involved)']),
    tb(['Consumer case', 'Holding'], ['<b>IMA v. V.P. Shantha, 1995</b>', 'doctors and medical professionals covered by the Consumer Protection Act'], ['<b>Bar of Indian Lawyers v. D.K. Gandhi, 2024</b>', 'about lawyers; class note says relief lies in regular courts (civil/criminal); note partly unclear']),
  ]),
  # ------------------------------------------------------------ houses
  dict(after='PARLIAMENT AND COMPOSITION', nodes=[
    sec('CLASS · Rajya Sabha and Lok Sabha seats', 'r'),
    bx('bl', '<b>RS original basis (1941 census):</b> 1 seat per <b>1 million</b> up to the first <b>5 million</b>; then 1 more per <b>2 million</b>. <b>UT seats:</b> Sec 27 RoPA 1950 (electoral college); <b>7th Am 1956</b>: UTs also send members to the Council of States.'),
    tb(['House', 'Class split', 'Total'], ['RS', '225 States + <b>8 UTs</b> (J&amp;K 4, Delhi 3, Puducherry 1) = 233 elected + 12 nominated', '<b>245</b>'], ['LS max', '530 States + 20 UTs', '<b>550</b>'], ['LS now', '524 States + 19 UTs, all elected (UT seats: UT Direct Election Act 1965)', '<b>543</b>']),
    tb(['UT', 'LS seats'], ['J&amp;K', '5'], ['Delhi', '7'], ['Chandigarh, A&amp;N, Lakshadweep, Puducherry, Ladakh', '1 each (5)'], ['Daman &amp; Diu + Dadra &amp; Nagar Haveli', '2'], ['<b>Total</b>', '<b>19</b>']),
    bx('ye', '<b>Class vs handout:</b> class uses RS 225 + 8 UTs and LS 550 max (524 + 19 UT); handout main text says RS 229 + 4, LS max 552, 530 + 13 (check). UP has the most RS seats: <b>31</b>.'),
  ]),
  dict(after='ELECTORAL SYSTEM OF THE LOK SABHA', nodes=[
    sec('CLASS · Art 81 balances; Delimitation Commission', 'r'),
    tb(['Art 81(2)', 'Balance'], ['<b>(a)</b>', '<b>inter-state</b>: LS seats per population'], ['<b>(b)</b>', '<b>intra-state</b>: population per constituency']),
    bx('bl', 'Both rebalanced after each census by delimitation. <b>Delimitation Commission:</b> statutory body; headed by a <b>retired SC judge</b>; members <b>Chief Election Commissioner</b> and <b>State Election Commissioner</b> (class).'),
  ]),
  # ------------------------------------------------------------ terms
  dict(after='DURATION AND CONTINUITY', nodes=[
    sec('CLASS · Terms of the Houses: extras', 'r'),
    tl(('1976', '<b>42nd Am</b>: LS term 5 to <b>6</b> years'), ('1978', '<b>44th Am</b>: back to <b>5</b> years')),
    bx('bl', '<b>RS term 6 years: Sec 154 RoPA 1951</b>; one-third retire every 2nd year; first RS by <b>draw of lots</b>. "Proclamation of Emergency" = national emergency (<b>Art 366(18)</b>); LS extended <b>1 year at a time</b>, never beyond <b>6 months</b> after it ends. LS dissolves automatically after 5 years or sooner by the President.'),
  ]),
  # ------------------------------------------------------------ disqualifications
  dict(after='DISQUALIFICATIONS FOR MEMBERSHIP', nodes=[
    sec('CLASS · Office of profit and RoPA sections', 'r'),
    t('<b>Why office of profit bars</b>', 'MP/MLA as chairperson of a PSU may hamper work as member', 'compromises duty to <b>question govt</b> on public issues', '<b>ministers exempt</b>; Parliament and States may list exempt posts by law', w=22),
    bx('ca', '<span class="tag">Class · 2005-06</span><b>Jaya Bachchan disqualified (2005)</b> as chairperson of UP Film Development Corporation (UPFDC), not on the exempt list; class also cites Speaker Somnath Chatterjee as holding an office of profit. <b>2006:</b> Office of Profit (Amendment) Bill to cover all MPs\' posts retrospectively; <b>Joint Committee on Offices of Profit: 10 LS + 5 RS</b>; Kalam used the suspensive veto. Teacher: if <b>even one norm</b> is met it is an office of profit.'),
    bx('ye', '<b>Class vs handout:</b> class says Prevention of Disqualification Act <b>1956</b>; handout says <b>1959</b> (check).'),
    tb(['RoPA section', 'Class detail'],
       ['<b>8(1)</b>', 'very heinous offence (untouchability, <b>NDPS Act</b>, rape): <b>instant</b> disqualification, even on a fine'],
       ['<b>8(2)</b>', 'dowry, food adulteration'],
       ['<b>8(3)</b>', 'other offences, <b>2+ years</b> jail: instant removal + <b>6 years</b> ban'],
       ['<b>8A</b>', 'corrupt practices: up to 6 years; decided by <b>President on EC opinion</b> (Governor for States)'],
       ['<b>8(4)</b>', 'appeal within 3 months saved sitting member: <b>Lily Thomas 2013</b> struck it (discrimination)']),
  ]),
  # ------------------------------------------------------------ presiding officers
  dict(after='SPEAKER AND DEPUTY SPEAKER', nodes=[
    sec('CLASS · Speaker: removal history, powers, "once a Speaker"', 'r'),
    tl(('1954', '<b>G.V. Mavalankar</b>'), ('1966', '<b>Hukam Singh</b>'), ('1987', '<b>Balram Jakhar</b>'), ('2026', '<b>Om Birla</b> (as written in class)')),
    bx('pk', '<b>Removal motions against Speakers: all defeated.</b> Speaker action to maintain order cannot be questioned in any court (<b>Art 122</b>).'),
    t('<b>Speaker: more powers (class)</b>', 'orders <b>Marshals</b> to evict members', 'final say on Money Bills and all <b>anti-defection</b> cases', '<b>expunges</b> unparliamentary remarks; decides who holds the floor', 'schedules agenda via <b>Business Advisory Committee</b>; decides <b>points of order</b>', 'admits motions, resolutions, questions; custodian of rights and privileges', 'chairs conference of presiding officers', w=24),
    bx('bl', '<b>AIPOC</b> (All India Presiding Officers\' Conference): 1st at <b>Shimla, 1921</b>; <b>2026 Lucknow</b> = 86th.'),
    tb(['Speaker\'s independence (class list)', 'Note'], ['Speaks only for opinion', 'casting vote only in a deadlock'], ['ADL exemption', 'may <b>resign from party</b> after election as Speaker'], ['Salary', 'charged expenditure'], ['Conduct', 'discussed only on removal motion'], ['Precedence', '<b>7th</b> rank, Table of Precedence']),
    t('<b>Still not fully secure: next steps</b>', 'withdraw Speaker\'s <b>ADL</b> powers', 'convention <b>"once a Speaker always a Speaker"</b>', '<b>UK:</b> Speaker may serve a 2nd term and no rival candidate is fielded against him in the next Commons election', '<b>1925 Vithalbhai Patel</b> (first Indian Speaker); <b>V.S. Page Committee 1967</b> recommended the same convention for India', 'even after a 2nd term Speakers get Governor-type posts: so <b>no political appointment</b> of a former Speaker', w=26),
    bx('ye', '<b>Class vs handout (Art 97 pay):</b> class follows <b>Lakshmikanth</b>: RS Chairman Rs 4 lakh; Speaker = MP salary + Cabinet Minister allowances; Dy Chairman and Dy Speaker = MP salary + MoS allowances. Handout gives Rs 4 lakh to the Speaker too (check).'),
  ]),
  dict(after='CHAIRMAN, DEPUTY CHAIRMAN', nodes=[
    sec('CLASS · Arts 92 and 96: voting while removal is pending', 'r'),
    tb(['Officer', 'While his removal resolution is considered'],
       ['<b>RS Chairman</b> (Art 92)', 'cannot preside; can speak and take part but <b>cannot vote</b>'],
       ['<b>RS Deputy Chairman</b>', 'speaks, takes part and votes as an ordinary member (first instance only); <b>no casting vote</b>'],
       ['<b>LS Speaker</b> (Art 96)', 'cannot preside; can speak and vote in first instance; <b>no casting vote</b> in these proceedings']),
    bx('pk', '<b>Marked "Imp" in class:</b> Arts <b>88, 89, 93, 94</b>. Art 88: ministers and AG speak in both Houses; non-member ministers and the AG have <b>no vote</b>.'),
  ]),
  dict(after='SESSIONS, QUORUM', nodes=[
    sec('CLASS · Voting by division', 'r'),
    bx('bl', '<b>Voice vote</b> (informal): Ayes and Noes. <b>Division</b> (formal, when close): <b>AVRE</b> buttons (Y, N, Abstain), or <b>slips</b>, or <b>head count</b>: Ayes to the <b>right</b> lobby, Noes to the <b>left</b>. More democratic since citizens get to know each vote. Third mode: <b>secret ballot</b>. Quorum = <b>1/10</b>.'),
  ]),
  # ------------------------------------------------------------ bills
  dict(after='BILLS: ORDINARY', nodes=[
    sec('CLASS · Notice, readings, joint sitting, Art 110 clauses', 'r'),
    bx('bl', '<b>Notice:</b> Govt (public) Bill 7 days, only <b>1 day</b> if already published in the Gazette; Private Member Bill <b>1 month</b>. <b>2nd reading:</b> general and detailed discussion <b>mandatory</b>; select committee, joint committee, circulation for opinion <b>optional</b>.'),
    tb(['Joint sitting: class point', 'Detail'],
       ['<b>Art 118</b>', 'each House makes its own rules; for a joint sitting the <b>President</b>, after consulting RS Chairman and Speaker, makes rules (118(4))'],
       ['RS rejected / 6 months idle', 'only amendments that <b>necessarily</b> caused the delay'],
       ['Passed with amendments the first House rejected', 'those amendments + the <b>disagreed provisions</b> may be amended again'],
       ['Chairman of RS', '<b>never</b> presides; no joint sitting for Constitution Amendment Bills']),
    bx('ye', '<b>Class vs handout (joint sitting years):</b> class gives Dowry Prohibition <b>1961</b>, Banking Service Commission <b>1978</b>, POTA <b>2002</b>; handout gives 1960, 1977, 2002 (the Bill years; sittings were 1961, 1978: general knowledge, verify).'),
    t('<b>MONEY BILLS: Art 110 (Union) · Art 199 (State Assembly)</b>', '<b>Clause 1 Criteria:</b> (a) tax changes (b) borrowing (c) Consolidated / Contingency Fund custody (d) appropriation (e) charged expenditure (f) public accounts, audit (g) incidental matters', '<b>Clause 2 Exclusions:</b> only fines or penalties, licence/service fees, local-body taxes', '<b>Clause 3 Decider:</b> LS Speaker, final', '<b>Clause 4 Proof:</b> Speaker\'s signed certificate when moved', w=26),
    bx('ye', '<b>Class vs handout:</b> class reads decider = 110(3), certificate = 110(4); handout cites 110(3) for the certificate (check). Money Bill: only Art 110, only LS, President\'s recommendation, RS no power.'),
    tb(['Financial Bill', 'Class example'], ['<b>Class 1</b> (Art 117(1)): Art 110 matters + more; LS only, President\'s recommendation; RS ordinary-bill-like power', '<b>Central Road Fund Bill</b> (road cess + road works)'], ['<b>Class 2</b>: expenditure from Consolidated Fund; either House; recommendation needed at <b>2nd reading</b>, not at introduction', '<b>Supreme Court (Number of Judges) Act 1956</b>: more judges, higher salary bill']),
  ]),
  # ------------------------------------------------------------ budget
  dict(after='UNION BUDGET', nodes=[
    sec('CLASS · Funds and charged expenditure: extras', 'r'),
    tb(['', 'Union', 'State'],
       ['<b>Contingency Fund</b>', 'created by Parliament; Finance Secretary holds for the President (Act 1950)', 'created by State Legislature; <b>Governor</b> operates'],
       ['Use', 'urgent unforeseen events: disasters, wars; advance <b>before</b> approval', 'unforeseen State crisis'],
       ['Refill', '<b>ex-post-facto</b> approval, then recoupment from Consolidated Fund (Art 266)', 'same']),
    bx('bl', '<b>Public Account:</b> govt acts as a <b>banker</b> (small savings, PF, deposits); repaid to citizens; moved by executive action, no vote. <b>Consolidated Fund:</b> every withdrawal needs prior legal approval (Appropriation Act).'),
    bx('pk', '<b>Charged expenditure:</b> extra example <b>CVC Act 2003</b> (CVC + 2 VCs). Three reasons: preserve <b>independence</b> of posts; preserve <b>fiscal credibility</b>; (third reason unreadable in class note). Charged = not votable, automatic withdrawal; proposed = votable, needs Appropriation Bill.'),
    tb(['The Budget', 'Branch'], ['By purpose', '<b>Revenue Budget</b> (running costs) · <b>Capital Budget</b> (asset building)'], ['By approval', '<b>Charged</b> (non-votable, guaranteed) · <b>Proposed</b> (votable, demands for grants)']),
    sec('CLASS · Financial year and railway budget', 'r'),
    tb(['Fact', 'Class note'],
       ['Indian FY', '1 Apr to 31 Mar: 3/4 in one calendar year, 1/4 in the next'],
       ['World', '~150 countries use calendar year; <b>USA 1 Oct to 30 Sep</b>'],
       ['History', 'annual budgets from <b>1860</b>; FY began 1 May till 1866; <b>1 April from 1867-68</b>'],
       ['Why April FY is poor (ARC-1)', 'kharif output unknown; capital works cannot start after May-June (monsoon)'],
       ['Reform', '<b>2016 Shankar Acharya committee</b>: calendar year (not adopted); ARC: FY from <b>November</b>'],
       ['Railway budget', 'until 1924 combined, separated on <b>Acworth Committee</b>; 1924-2017 presented 3-4 days earlier (railways = commercial, revenue-earning); <b>Bibek Debroy 2016</b>: merge']),
    sec('CLASS · Budget stages, cuts, closures', 'r'),
    bx('bl', '<b>Stages Arts 112-117, 6 or more.</b> General discussion = <b>"hangover of the past"</b>: British-era chambers could only discuss; today whole budget is voted in LS except charged items (discussed only). <b>Committee stage:</b> ministry budgets to departmental committees ~<b>1 month</b>, House not sitting; <b>24 committees, 31 members (10 RS + 21 LS)</b> (class note partly unclear).'),
    tb(['Cut motion', 'Class example'], ['<b>Economy</b>', 'demand far above actual need'], ['<b>Token</b>', 'grievance on record: no leprosy provision in Health Ministry, <b>Rs 100</b> cut'], ['<b>Policy</b>', 'amounts to no-confidence; if passed demand cut to <b>Re 1</b>']),
    bx('ye', '<b>Guillotine:</b> ~<b>26 days</b> to discuss; Speaker cuts debate at the set time and all remaining demands are voted undiscussed (device from the French Revolution): accountability suffers. A demand once passed becomes a <b>grant</b>.'),
    tb(['Closure', 'Class note'], ['Simple', 'sufficiently discussed: <b>most democratic</b>'], ['Kangaroo', 'only important clauses discussed'], ['Compartments', 'similar sections grouped'], ['Guillotine', 'all, even undiscussed, put to vote: <b>most undemocratic</b>; used in Budget']),
    bx('bl', '<b>USA filibuster:</b> unlimited debate (Senate).'),
    sec('CLASS · Appropriation, Finance Bill, special grants', 'r'),
    t('<b>Appropriation and Finance Bills</b>', '<b>Appropriation Bill:</b> all grants + charged items = total outlay; LS accepts or rejects, <b>cannot amend</b>; becomes Act; legal authority to withdraw from CFI', '<b>Finance Bill:</b> tax proposals; becomes Finance Act; the two Acts = financial law for the year', 'Parliament cannot raise a tax on its own: executive proposes (direct: income tax; indirect: GST, customs), Parliament approves', 'indirect-tax change on 1 Feb applies from <b>midnight</b> so dealers cannot pocket stock profit', '<b>Provisional Collection of Taxes Act 1931</b> (class adds "renewed 2023", verify): collect at new rate for <b>75 days</b>; refund if Parliament does not approve', w=26),
    tb(['Grant', 'Class addition'],
       ['<b>Vote on Account</b>', 'after limited discussion; ~<b>1/6</b> of outlay, <b>2 months</b>; govt not "penniless" (typically by May)'],
       ['<b>Vote of Credit</b>', '"blank cheque" for unforeseen demands (e.g. war); approval after spending'],
       ['<b>Excess</b>', 'end of FY; <b>PAC</b> approves, LS votes; frequent excess = weak financial control'],
       ['<b>Exceptional</b>', 'one-off: e.g. hosting foreign dignitaries after a major leader\'s death'],
       ['<b>Token</b>', 'authorises <b>re-appropriation</b> beyond executive competence']),
  ]),
 ],
}

RECALL = {
 15: [
  ('HC strength vs SC strength: who changes it?', 'HC: executive order of GoI (class); SC: only Parliament by law'),
  ('Speaker removal motions so far?', 'Mavalankar 1954, Hukam Singh 1966, Balram Jakhar 1987, Om Birla 2026 (class); all defeated'),
  ('CCPA powers and appeal?', 'Recall goods, recall misleading ads, class action, investigations; appeal to NCDRC'),
  ('Consumer complaint: limitation, jail, disposal time?', '2 years; 1 month to 3 years; 3 months (no testing) / 5 months (testing)'),
 ],
}
