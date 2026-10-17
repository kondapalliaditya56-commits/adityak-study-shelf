from hwlib import *
pages=[]
# P1
pages.append(pg(T('MONEY LAUNDERING'),STORY,
 B('What is it ?',['The process of '+H('concealing or disguising')+' the true <b>nature, source, location, disposition, movement, rights, or ownership</b> of the <b>proceeds of crime</b> — and includes '+H('acquiring, possessing, using')+' such proceeds, directly or indirectly, <b>knowingly</b>. <span class="bk">(PMLA 2002, S.3)</span>',
   SW('Simple: crime earns "dirty" cash; laundering makes it look like salary/business income so it can be spent openly.')],'c1',28)+
 B('Why is it done ?',['① <b>Concealment</b> of illegal activities','② <b>Integration</b> into legitimate economy','③ <b>Terror</b> &amp; organised-crime financing','④ <b>Evasion</b> of tax',
   '<span class="mn">C · I · T · E</span> <span class="gn">→ <b>CITE</b>: cite these 4 reasons — Concealment · Integration · Terror-finance · Evasion</span>'],'c4',28)+
 box('pk','<b>Scale:</b> UNODC estimates <b>2–5% of global GDP</b> ($800 bn – 2 tn) is laundered every year. '+P('2013 · 2018 · 2021 · 2023')),
 S('STAGES OF MONEY LAUNDERING','r'),STAGES,
 box('bl','<b>Remember:</b> <b class="rd">P</b>lacement → <b class="rd">L</b>ayering → <b class="rd">I</b>ntegration = <span class="mn">PLI</span> <span class="rd">(think PLI scheme: money goes IN, comes out "incentivised")</span><br>'
   '<b>Placement</b> = riskiest, because large cash is first exposed to banks &amp; regulators.<br><b>Layering</b> = the "maze": many transfers so the trail is lost.<br><b>Integration</b> = money re-enters as legitimate wealth (shell firms, real estate, business).'),
 B('Key words',['<span class="rd"><b>smurfing</b></span> (splitting cash into small deposits) · <span class="rd"><b>shell company</b></span> · <b>offshore account</b> · <b>predicate offence</b> (the original crime that produced the money) · <b>proceeds of crime</b>'],'c5',22)+
 box('ye','<b>Value addition:</b> Money laundering is the <span class="rd">oxygen of organised crime &amp; terrorism</span> — cut the money, cut the group.')))
# P2
pages.append(pg(T('TECHNIQUES OF MONEY LAUNDERING'),
 B('① Oldest',['<b>Hawala system</b>','<b>Physical smuggling / cash couriers</b>'],'c1',24)+
 B('② Older',['<b>Shell companies</b> (no real business, only paper)','<b>Over / under-stating of values</b> — invoices inflated or deflated to move value (<span class="rd">trade-based ML, TBML</span>)'],'c2',24)+
 B('③ Latest',['<b>Cyber-crime</b> → identity theft, hedge funds','<b>Cryptocurrencies</b>','<b>NFTs</b> — Non-Fungible Tokens','<b>Insurance sector</b> (buy policy → surrender → "clean" refund)','<b>White hawala</b> transfer'],'c5',24)+
 SW('Easy recall: <b>O</b>ld→cash &amp; hawala · <b>O</b>lder→papers (shells, invoices) · <b>L</b>atest→digital (crypto, NFT, cyber)'),
 S('HAWALA SYSTEM','b'),
 '<div class="row"><div>'+B('Features',['<b>Money transfer without movement of money</b>','<b>No regulatory oversight</b> of RBI','<b>Instant</b> in nature','Runs on <b>trust + code words</b>; no paper trail'],'c4',20)+
 B('White vs Black',['<b>White hawala</b> – legal purpose (family remittance) but outside banking channel','<b>Black hawala</b> – funds crime, terror, tax evasion'],'c1',20)+'</div><div>'+HAW+'</div></div>',
 box('gr','<b>Why hawala is hard to stop:</b> no records, no KYC, instant, across borders, runs on community trust. <span class="rd">FATF Special Recommendation → "Alternative Remittance"</span> targets exactly this.'),
 S('SHELL COMPANIES &amp; TBML — in simple words','g'),
 box('bl','<b>Shell company:</b> registered firm with no real operations, used to pass money through.<br><b>Over-invoicing:</b> importer pays more than goods are worth → extra money leaves India legally "as payment".<br><b>Under-invoicing:</b> goods declared cheaper → difference settled in black money abroad; customs duty also evaded.'),
 box('pk','<b>Exam angle:</b> Techniques are not static — as banks tighten KYC, launderers move to <b>crypto, NFTs, gaming, insurance</b>. Always end an answer with this "cat-and-mouse" line.')))
# P3 crypto
pages.append(pg(T('CRYPTOCURRENCIES IN MONEY LAUNDERING'),
 box('bl','<b>Cryptocurrencies have become a tool for money laundering.</b> '+SW('Simple: digital money, no bank in the middle, accounts are just long codes — not names.')),
 S('Reasons for use','r'),
 B('Decentralised ledgers',['No central authority → <b>difficult to track</b>'],'c1',34)+
 B('No central issuing authority',['No intermediaries → <b>reduces detection</b>'],'c2',34)+
 B('Immune from govt regulation',['<b>Beyond traditional financial regulations</b>'],'c3',34)+
 B('Pseudonymous nature',['<b>Transactions harder to trace</b>'],'c4',34),
 S('Mechanism involved','b'),
 '<div class="row"><div>'+box('pk','<b>Crypto-mixers</b><br>Services that <b>mix identifiable tokens with others</b> to obscure their origin.')+MIX+'</div><div>'+box('pk','<b>Chain-hopping</b><br>Moving cryptocurrencies <b>between different blockchains</b> to obscure trails.')+box('bl','<span class="rd"><b>Example:</b></span> swap Bitcoin → Monero (privacy coin) → another chain → cash out through an exchange with weak KYC.')+'</div></div>',
 B('Prevention mechanisms',['<b>Regulation of crypto services</b>','<b>Monitoring by exchange systems</b> (KYC, suspicious-transaction reports)','<b>Use of blockchain technology</b> itself — public ledger lets analytics firms trace flows'],'c5',30),
 box('ye','<b>GLOBAL COOPERATION</b><br>• International initiatives → <b>unifying standards</b> → <span class="rd">UNGPML</span> programme<br>• <b>Pressure on tax havens</b> → diluting secrecy laws'),
 S('India – value addition','g'),
 box('gr','• <b>VDA tax:</b> 30% on gains + <b>1% TDS</b> (Virtual Digital Assets).<br>• <b>PMLA 2023 amendment</b> brought VDA service providers under PMLA as reporting entities.<br>• FATF recommends <b>travel rule</b> for crypto transfers (sender/receiver info travels with the transaction).'),
 box('ca','<span class="tag">CURRENT AFFAIRS</span><b>FATF, June 2026:</b> seventh targeted update on <b>virtual-asset / VASP standards</b> and a new report on <b>DeFi</b> risks (ML/TF/proliferation financing) — answer hook for "regulating crypto".'),
 box('pk','<b>Way forward line:</b> Legalise <b>and</b> regulate crypto (not ban) + tracking and reporting mechanisms + international standards — the faculty\'s <b>"L"</b> in MONEY LAUNDER.')))
# P4 impact
pages.append(pg(T('IMPACT OF MONEY LAUNDERING'),
 box('bl','<b>Memory word:</b> <span class="mn">SEEPS</span> — dirty money <b>seeps</b> into every layer: <b>S</b>ocial · <b>E</b>conomic · <b>E</b>nvironmental · <b>P</b>olitical · <b>S</b>ecurity (the 5 headings below are in the faculty\'s order)'),
 B('① Social',['<b>Illegal businesses strengthened</b> (drugs, prostitution)','<b>Decreasing social capital</b>, loss of morality &amp; ethics','<b>Transfer of economic power to criminals</b>','Damage to legitimate businesses'],'c1',24)+
 B('② Economic',['<span class="rd"><b>Micro</b></span> → damage to reputation of financial institutions · cost of doing business ↑ · legitimate business loses · <b>increase in organised crime</b> · <b>policy distortion due to measurement error</b>',
   '<span class="rd"><b>Macro</b></span> → <b>tax evasion</b> · <b>Ease of Doing Business (EoDB) discourages foreign investors</b> · <b>volatile exchange rates</b> due to unanticipated problems · <b>decreasing market confidence</b> · <b>increase in cost of insurance premiums</b>','Artificial inflation + jobless growth → radicalisation &amp; security challenges'],'c2',24)+
 B('③ Political',['<b>Government deprived of taxes</b>','<b>Increased spending on fighting crime</b>'],'c3',24)+
 B('④ Security',['<b>Terror funding</b>','Increase in crimes','Illegal activities'],'c4',24)+
 B('⑤ Environmental',['<b>Illegal wildlife trade</b>','Increased chance of <b>zoonotic disease</b> outbreak (animal → human diseases, e.g. COVID-type)'],'c5',24),
 box('pk','<b>FATF report "Money Laundering and the Illegal Wildlife Trade" (2020)</b><br>Impact of illegal wildlife trade → <b>Corruption</b> · <b>Threatens biodiversity</b> · <b>Threat of zoonotic diseases</b><br><b>India:</b> a source of <span class="rd"><b>rhino horns, pangolins, tusks</b></span>. Wildlife trade is estimated at <b>$7–23 bn</b> a year.'),
 B('Drivers (India)',['<b>Rich biodiversity and bad law enforcement</b>','Role of <b>private zoos</b>','<b>New communication technology</b>','<b>e-banking</b>'],'c6',28),
 box('ye','<b>Answer tip:</b> A social effect → a security effect → an environmental effect — the "environmental" and "political" points are what most students miss; add them for extra marks.')))
# P5 challenges + WF
pages.append(pg(T('CHALLENGES IN FIGHTING MONEY LAUNDERING'),
 box('bl','<span class="mn">STAMP + CBT</span> — <b>STAMP</b> out money laundering: <b>S</b>muggling · <b>T</b>ech evolution · <b>A</b>wareness lacking · <b>M</b>ultiple agencies · <b>P</b>redicate-offence law. Then the <b>CBT</b> gaps: <b>C</b>onviction low · <b>B</b>anks skip KYC · <b>T</b>ax havens.'),
 B('Challenges',['<b class="gn">C</b> – <b>Low rate of conviction</b> <span class="rd">(≈4.6%)</span>. ED: 5,892 cases since 2015, only 15 convictions (RS report 2025). <span class="gn">Counter-point: ED claims 93.33% conviction on cases tried (56 of 60).</span> → Use both: "high success on a tiny base".',
   '<b class="rd">T</b> – <b>Fast-paced tech evolution</b> (crypto, NFTs, gaming)','<b class="rd">P</b> – <b>Predicate-offence-oriented law</b> → <span class="rd">corrected by the 2019 amendment</span> (ML is now an independent offence)','<b class="rd">A</b> – <b>Lack of awareness</b> among common people (they become money mules)','<b class="rd">S</b> – <b>Widespread smuggling</b> of goods in India','<b class="gn">B</b> – <b>Banks fail to enforce KYC norms</b>','<b class="rd">M</b> – <b>Multiplicity of agencies and lack of convergence</b> (ED, FIU, CBDT, CBI, SEBI…)','<b class="gn">T</b> – <b>Tax-haven countries</b>'],'c1',22),
 box('pk','<b>Black-money linkage:</b> Tax havens + shell companies + cash economy are the "supply route" of laundering.'),
 S('WAY FORWARD FOR MONEY LAUNDERING','g'),
 arrow([('Organised crime funds','Cut the source'),('Placement','• tighten <b>e-KYC</b> norms<br>• <b>e-anti money laundering</b><br>• harm reduction'),('Layering','• <b>info sharing</b> b/w agencies (<b>ED, FIU-IND, CERT-In</b>)'),('International co-operation','• pressure <b>tax havens</b> for info sharing<br>• <b>UN GPML</b>')]),
 S('MONEY LAUNDER — the faculty\'s mnemonic','r'),
 tbl(['','Meaning','Action'],[
  ['<b class="rd">M</b>','<b>M</b>onitoring transactions','Continuous monitoring; AI to detect suspicious patterns'],
  ['<b class="rd">O</b>','<b>O</b>rganisational policy of acceptance','Clear client-acceptance policy; risk-based onboarding'],
  ['<b class="rd">N</b>','<b>N</b>otifying suspicious transactions','Report STRs promptly; train staff'],
  ['<b class="rd">E</b>','<b>E</b>nforcement of KYC','Tighter KYC; update data regularly'],
  ['<b class="rd">Y</b>','<b>Y</b>ielding to regulatory compliance','Follow AML laws; regular audits'],
  ['<b class="rd">L</b>','<b>L</b>egalising &amp; regulating crypto','Tax it; robust tracking and reporting'],
  ['<b class="rd">A</b>','<b>A</b>dvanced e-AML tools','Better software for monitoring'],
  ['<b class="rd">U</b>','<b>U</b>nified coordination among agencies','Central hub for information sharing'],
  ['<b class="rd">N</b>','<b>N</b>PA management','Coordinate when accounts turn NPA; mitigate risks'],
  ['<b class="rd">D</b>','<b>D</b>ue diligence procedures','Client identification; regular risk assessment'],
  ['<b class="rd">E</b>','<b>E</b>nhanced information sharing','Timely, accurate data exchange between agencies'],
  ['<b class="rd">R</b>','<b>R</b>egulation of international wire transfers','Follow FATF; prohibit anonymous cross-border wires']]),
 box('gr','<b>Conclusion lines:</b> Govt set up an <b>inter-ministerial coordination committee</b>; India proposed a <b>permanent secretariat</b> for countering terror financing — guiding principle <b>"Beyond-Border Cooperation"</b>.')))
# P6 initiatives
pages.append(pg(T('INITIATIVES'),S('INDIAN','b'),
 B('Legal framework',['<b>Prevention of Money Laundering Act (PMLA), 2002</b>','<b>Foreign Exchange Management Act (FEMA), 1999</b>','<b>Benami Transactions (Prohibition) Act, 1988</b> <span class="gn">(amended 2016)</span>'],'c1',30)+
 B('Regulatory measures',['<b>FATF</b> compliance','<b>RBI</b> guidelines','<b>SEBI</b> regulations','<b>IRDAI</b> guidelines'],'c2',30)+
 B('Enforcement &amp; monitoring agencies',['<b>Enforcement Directorate (ED)</b> – investigates &amp; prosecutes under PMLA','<b>Financial Intelligence Unit – India (FIU-IND)</b> – receives suspicious-transaction reports','<b>Central Board of Direct Taxes (CBDT)</b>'],'c3',30)+
 B('International cooperation',['Bilateral and multilateral agreements','Participation in international forums'],'c4',30)+
 B('Technological measures',['<b>Project Insight</b> (tax-data analytics)','<b>Central KYC Registry (CKYCR)</b> – one KYC for all institutions'],'c5',30),
 S('GLOBAL','g'),
 tbl(['Mechanism','What it does'],[
  ['<b>Vienna Convention 1988</b>','Criminalised ML from drug trafficking; cooperation &amp; extradition'],
  ['<b>Basel Committee Statement 1988</b>','Banks must not be used for ML'],
  ['<b>FATF (G7, 1989)</b>','Sets international standards (40 + 9 recommendations)'],
  ['<b>Council of Europe Convention 1990</b>','Common definition / policy; technical assistance'],
  ['<b>UN GPML 1997</b>','UN programme against ML; also UN conventions on terror financing, transnational organised crime (UNTOC), corruption (UNCAC)'],
  ['<b>Asia Pacific Group (APG)</b>','Implements FATF 40+9; 41 members + observers (WB, UN, IMF); India is a member'],
  ['<b>Wolfsberg AML Principles</b>','11 principles by a group of global banks'],
  ['<b>IMoLIN</b>','International ML Information Network by UNODC — database'],
  ['<b>Egmont Group</b>','Network of Financial Intelligence Units sharing information']]),
 box('ye','<b>Memory:</b> <b>V</b>ienna &amp; <b>B</b>asel (1988) → <b>F</b>ATF (1989) → <b>C</b>oE (1990) → <b>U</b>N-GPML (1997): <span class="mn">"Very Big Fish Catch Unwary"</span>'),
 box('bl','<b>Note:</b> The Wolfsberg Group is a bank-led association (the handout credits Transparency International for the principles) — if asked, write "Wolfsberg Group / TI" and move on.')))
# P7 PMLA
pages.append(pg(T('PMLA 2002'),S('Features','r'),
 B('Features',['<b>Confiscation of property</b> (attachment of proceeds of crime)','<b>List of crimes:</b> Schedule Part A / Part B gives crimes for ML','<b>Criminal conspiracy</b> — concealment, acquisition, possession and use of proceeds, e.g. buying property in name of family','<b>ML as a standalone crime</b>','Covers <b>Politically Exposed Persons (PEPs)</b>, <b>Virtual Digital Assets</b>, <b>NPOs</b>','<b>International jurisdiction</b> for ED'],'c1',24),
 S('Issues associated','b'),
 B('Issues',['<b>Low conviction rate</b>','<b>Dilution of laws</b>','<b>Alternate criminal law system</b> — ED works outside CrPC','<b>Admissibility of statements</b> (made to ED officers)','<b>Section 45</b> of PMLA (twin bail test)','<b>Procedural issues</b> · <b>burden to prove innocence</b> (reverse burden on accused)'],'c2',24),
 S('2023 AMENDMENT — Key changes','g'),
 B('PEN-D',['<b>P</b> – <b>Politically Exposed Persons</b> covered','<b>E</b> – b<b>E</b>neficial owner threshold <b>25% → 10%</b>','<b>N</b> – <b>NGOs / NPOs</b> brought in (registered on NGO Darpan portal)','<b>D</b> – extension of <b>due diligence</b> (records kept 5 years); VDAs covered'],'c4',22),
 S('PMLA VERDICT REVIEW — Vijay Madanlal Choudhary Case (2022)','r'),
 B('Supreme Court held',['<b>Amendment as Money Bill</b> — upheld','<b>Interpretation of S.3</b> (defines ML): <i>directly or indirectly · actually involved · connected with proceeds of crime · untainted property</i> → <span class="rd"><b>very broad</b></span>','<b>Retrospective application</b> → <b>ML is a continuous crime</b>','<b>ED need not supply copy of ECIR</b> (it is an internal document, not an FIR)','<b>Twin bail test:</b> prosecutor must be heard; court must believe (i) accused is <b>not guilty</b> (ii) <b>unlikely to reoffend</b> if released'],'c5',24),
 box('ye','<b>Way forward (faculty): <span class="mn">P · M · L · A</span></b> → <b>P</b>rocedural reforms · <b>M</b>aintaining operational efficiency · <b>L</b>ist of scheduled offences (review) · <b>A</b>dding clarification on terms<br><b>Keywords:</b> standalone offence · continuous crime · twin bail · reverse burden · ECIR≠FIR · Money Bill · PEP · beneficial owner'),
 box('ca','<span class="tag">CURRENT AFFAIRS</span><b>Directorate of Enforcement v. Bhupesh Arora (SC, 29 Sep 2026):</b> quashing the predicate-offence FIR by <b>compromise</b> does <b>not obliterate proceeds of crime</b>; HC bail set aside; ED told to finish probe in <b>5 months</b>. <span class="gn">Link: ML is an independent offence (Vijay Madanlal) — but proceeds survive a compromise.</span><br><b>Sanjay Sureka v. ED (2026 INSC 1124, SC, Oct 2026):</b> <b>S.19</b> — arrest order &amp; material must go to the Adjudicating Authority <b>"immediately"</b> = <b>expeditiously and simultaneously</b>; no fixed hours/days (5-day delay held fine).')))
# P8 FATF
pages.append(pg(T('FATF'),
 box('bl','<b>Financial Action Task Force</b> — set up by the <b>G7 in 1989</b>; sets global standards on money laundering &amp; terror financing. It issues the <b>FATF Recommendations</b>; countries are peer-reviewed through <b>Mutual Evaluation</b>; poor performers go on the <b>Grey list</b> (increased monitoring) or <b>Black list</b> (call for action).'),
 '<div class="row"><div>'+S('FATF\'s Recommendations (40)','b')+
 tbl(['No.','Subject'],[['1','Assessing risks &amp; applying a <b>risk-based approach</b>'],['2','National cooperation &amp; coordination'],['3','<b>Money laundering offence</b>'],['4','Confiscation &amp; provisional measures'],['9','Financial institution <b>secrecy laws</b>'],['10','<b>Customer due diligence</b> &amp; record'],['11','<b>Record keeping</b>'],['12','Additional measures for specific customers'],['14','<b>Politically exposed persons</b>'],['15','<b>Correspondent banking</b>'],['24','Transparency &amp; <b>beneficial ownership</b> of legal persons'],['29','<b>Financial intelligence units</b>'],['39','<b>Extradition</b>']])+
 '</div><div>'+S('FATF\'s Special Recommendations (TF)','r')+
 tbl(['#','Subject'],[['1','Ratify &amp; implement <b>UN instruments</b>'],['2','<b>Criminalise financing of terrorism</b> &amp; associated ML'],['3','<b>Freeze &amp; confiscate</b> terrorist assets'],['4','<b>Report suspicious</b> transactions related to terrorism'],['5','<b>International co-operation</b>'],['6','<b>Alternative remittance</b> (hawala)'],['7','<b>Wire transfers</b>'],['8','<b>Non-profit organisations</b>'],['9','<b>Cash couriers</b>']])+
 box('ye','<span class="mn">UNFAIR + CCW</span> — terror finance is <b>unfair</b> play:<br><b>U</b>N instruments · <b>N</b>PO · <b>F</b>reeze · <b>A</b>lternative remittance · <b>I</b>nternational co-op · <b>R</b>eport STRs<br>then <b>CCW</b>: <b>C</b>riminalise · <b>C</b>ash couriers · <b>W</b>ire transfers')+
 '</div></div>',
 box('al' if False else 'pk','<b>Note:</b> The handout earlier says 8 Special Recommendations (2001); a 9th (cash couriers) was added in 2004 → <b>40 + 9</b>. The slide list shows 10 lines; learn the 9 above.'),
 S('FATF\'S REVIEW OF INDIA','g'),
 B('Recognised India\'s efforts',['<b>Mitigating risks</b> arising from ML/TF','<b>Effective measures</b> implemented','<b>JAM Trinity</b> (Jan Dhan, Aadhaar, Mobile)'],'c4',30)+
 B('Placed India in',['<b>"Regular follow-up"</b> category — India achieved <b>highest level of technical compliance</b>','Other G-20 in regular follow-up: UK, Italy, France','Other categories: <b>Enhanced follow-up</b>, <b>Grey list</b>, <b>Black list</b>'],'c5',30)+
 box('ca','<span class="tag">CURRENT AFFAIRS</span><b>India&#39;s Mutual Evaluation (FATF):</b> on-site Nov 2023 → adopted at <b>June 2024 plenary (Singapore)</b> → 368-page report released <b>19 Sep 2024</b>. India in <b>"regular follow-up"</b> (only 4 other G20 members share it); previous review 2010; <b>next evaluation 2031</b>. FATF asked for <b>stronger prosecution</b> in ML/TF cases and better protection of the <b>NPO sector</b>.<br><b>June 2026 plenary:</b> grey list <b>+ Bosnia &amp; Herzegovina, Iraq</b>; <b>− Algeria, Namibia</b> (22 on list); black list unchanged (<b>N. Korea, Iran, Myanmar</b>). UK presidency (Giles Thomson) from <b>1 Jul 2026</b>; India&#39;s <b>Vivek Aggarwal</b> is incoming <b>Vice-President</b>. Consultation on <b>Rec. 16</b> (payment transparency).'),
 B('Mutual Evaluation Report',['<b>Peer review</b> of a country\'s measures against ML. Two components → <b>① Effectiveness rating</b> · <b>② Technical compliance rating</b>'],'c6',30)))
# P9 MER concerns + implementation
pages.append(pg(T('FATF — CONCERNS &amp; IMPLEMENTATION IN INDIA'),S('Concerns highlighted by M.E.R. in India','r'),
 B('① Illegal activities',['<b>Cyber-enabled fraud</b>, corruption, drug trafficking'],'c1',30)+
 B('② Security threats',['<b>ISIL &amp; Al-Qaeda</b> presence in Jammu &amp; Kashmir','Regional insurgencies, <b>Left-Wing Extremist</b> groups'],'c2',30)+
 B('③ Legal &amp; operational',['<b>Low ML conviction rate</b> (28 in last 5 years)','<b>Backlog of pending trials</b>','<b>Saturated court system</b>'],'c3',30)+
 B('④ Supervision deficiencies',['Weak or no supervision of <b>DNFBPs</b> (Designated Non-Financial Businesses &amp; Professions)','High-risk sectors e.g. <b>DPMS</b> (Dealers in Precious Metals &amp; Stones) lack effective controls','<b>Cash-transaction prohibitions</b> under tax laws not sufficient'],'c4',30)+
 B('⑤ PEPs',['No clear provisions under PMLA or regulatory frameworks (RBI, SEBI, IRDAI, PFRDA)'],'c5',30),
 box('pk','<b>Memory word:</b> <span class="mn">SLIPS</span> — the <b>slips</b> FATF found in India: <b>S</b>upervision gaps · <b>L</b>egal/operational · <b>I</b>llegal activities · <b>P</b>EPs · <b>S</b>ecurity threats'),
 B('FATF Mutual Evaluation — criticism',['<b>No formal rules</b>','<b>Weak listing regime</b> (wilful / non-wilful)','<b>Absentees</b> (e.g. Pakistan)','<b>Global-South representation</b> low','Emerging tech not covered'],'c6',30),
 S('Implementation of FATF recommendations in India','g'),
 B('① Reporting entities',['<b>Formation agent</b> of companies &amp; LLPs','<b>Director, secretary, partner</b> in companies &amp; LLPs','Providing <b>registered office / business address</b>','<b>Trustees</b>','<b>Nominee shareholder</b> for another person'],'c4',28)+
 B('② Responsibilities',['<b>Verify identity</b> of clients before specified transactions','Examine <b>ownership &amp; financial position</b>','Record <b>purpose</b> behind the transaction','<b>Disallow</b> specified transactions'],'c5',28)+
 B('③ Exemptions',['<b>Lawyers</b>'],'c1',28)))
# P10 NMFT + TF + black money
pages.append(pg(T('TERROR FINANCING &amp; BLACK MONEY'),
 box('bl','<b>Terror financing</b> (UN Convention): any person who <b>provides or collects funds</b>, directly or indirectly, unlawfully and wilfully, <b>intending or knowing</b> they will be used to carry out a terror offence. <b>Why money?</b> recruit &amp; support members · maintain logistics hubs · conduct operations.'),
 B('<b>N·O·M·S</b> methods',['<b class="rd">N</b>ew tech → crypto (IS-K asked <b>Monero</b> donations via <i>Voice of Khorasan</i>), digital assets/gaming/prepaid cards, dark web','<b class="rd">O</b>rganised crime → kidnapping for ransom, narcotics, illicit trade (oil, charcoal, diamonds, gold), organ &amp; human trafficking','<b class="rd">M</b>oney laundering → banks, <b>SWIFT</b>, <b>hawala</b>','<b class="rd">S</b>ponsors → <b>state sponsorship</b>, <b>crowdfunding</b> (misuse of Zakat), <b>misuse of NPOs</b> (e.g. Global Relief Foundation)'],'c1',26)+
 box('ye','<span class="mn">NOMS = "No Money for Terror"</span> — also the name of the <b>New Delhi Conference 2022</b>.'),
 S('"No Money for Terror" Conference, New Delhi 2022','b'),
 B('Takeaways',['~<b>450 delegates</b>; reviewed global counter-terror-financing regime','<b>No "good" and "bad" terrorism</b> — zero tolerance','Fight <b>terrorism as a network</b>, not just a terrorist','Impose <b>costs on state sponsors</b>; isolate sympathisers','<b>Organised crime–terror links</b>: global collaboration','Role of <b>UNSC, FATF, FIUs, Egmont</b>; joint ops, intelligence, extradition','<b>Tech:</b> dark net &amp; private currencies — involve private sector, don\'t demonise tech','<b>Delhi Declaration</b> (UNSC CTC): countering new tech for terror'],'c5',24),
 S('BLACK MONEY — quick map','r'),
 '<div class="row"><div>'+B('Sources',['tax evasion · IPO/insider trading · shell cos · <b>gold</b> · corruption · tax havens · <b>cash economy</b> · hawala · illegal gambling'],'c2',18)+B('Effects',['↓ FDI · parallel economy · policy distortion · inequality · <b>national security</b> · inflated real-estate · vicious cycle'],'c1',18)+'</div><div>'+B('Govt steps',['<b>Black Money Act 2015</b> · Benami Act 2016 · <b>TIEAs</b> · GST · IDS &amp; PMGKY 2016 · RERA · PAN · UPI · demonetisation'],'c4',18)+B('Data',['₹9.41–14.71 lakh cr (2015) · GFI $38.7 bn/yr outflow (2002-11) · Swiss deposits CHF 3.83 bn (2021) · ~90% lies <b>inside</b> India'],'c5',18)+'</div></div>',
 box('gr','<b>Way forward — BLACK:</b> <b>B</b>etter regulatory framework · <b>L</b>everage technology · <b>A</b>wareness · <b>C</b>ooperation among agencies · <b>K</b>YC enforcement.')))
# P11 recap
pages.append(pg(T('ONE-PAGE RECAP &amp; SELF-TEST'),
 '<div class="row"><div>'+S('Mnemonic sheet','r')+
 tbl(['Topic','Mnemonic'],[['Why ML','<b>CITE</b> – Concealment · Integration · Terror finance · Evasion of tax'],['Stages','<b>PLI</b> – Placement · Layering · Integration'],['Techniques','<b>O-O-L</b> – Oldest · Older · Latest'],['Impact','<b>SEEPS</b> – Social · Economic · Environmental · Political · Security'],['Challenges','<b>STAMP</b> (Smuggling·Tech·Awareness·Multiple agencies·Predicate law) + <b>CBT</b> (Conviction·Banks·Tax havens)'],['Way forward','<b>MONEY LAUNDER</b>'],['PMLA 2023','<b>PEN-D</b>'],['Verdict WF','<b>PMLA</b> – Procedural · Maintaining efficiency · List of offences · Adding clarity'],['FATF special','<b>UNFAIR + CCW</b>'],['MER concerns','<b>SLIPS</b> – Supervision · Legal · Illegal activities · PEPs · Security'],['TF methods','<b>NOMS</b>'],['Black money WF','<b>BLACK</b>'],['Global','<b>"Very Big Fish Catch Unwary"</b>']])+
 '</div><div>'+S('Self-test (cover &amp; answer)','b')+
 box('bl','1. Define ML under PMLA S.3.<br>2. Which stage is riskiest, and why?<br>3. White vs black hawala?<br>4. Name 3 reasons crypto suits launderers.<br>5. Mixer vs chain-hopping?<br>6. Five impacts of ML (SEEPS).<br>7. 2019 amendment fixed which challenge?<br>8. PEN-D — expand.<br>9. Twin bail test — two limbs?<br>10. Why did SC say ECIR need not be shared?<br>11. FATF year, founder; grey vs black list?<br>12. India\'s FATF category and why?<br>13. 3 MER concerns about India.<br>14. NOMS conference year/place?<br>15. Reconcile 93.33% vs 15 of 5,892.')+'</div></div>',
 S('Answer frame — 15 marks','g'),
 B('Structure',['<b>Intro:</b> definition + UNODC 2–5% GDP (or Peña Nieto: "oxygen to organised crime")','<b>Body:</b> stages → techniques (old→latest) → impact (SEEPS) → legal framework (PMLA, FEMA, FIU, ED) → challenges','<b>Way forward:</b> MONEY LAUNDER + FATF + <b>Beyond-Border Cooperation</b>','<b>Conclusion:</b> balance enforcement with tech + international cooperation'],'c4',22),
 box('pk','<b>PYQs:</b> 2013 (10) · 2018 (15) · 2021 (10) · 2023 (15) — all ask <b>techniques/challenges/measures</b>; keep the <span class="rd">three-layer</span> structure: <b>legal – institutional – technological</b>.'),
 box('bl','<b>Current-affairs sources:</b> Business Standard (19 Sep 2024, FATF MER India) · ComplyAdvantage (FATF June 2026 plenary outcomes) · LawBeat (DoE v. Bhupesh Arora) · Verdictum (Sanjay Sureka v. ED). Verify exact dates before quoting in mains.'),
 box('ye','<b>Source note:</b> notes inspired by the faculty\'s hand-written Sarthi IAS notes + handout; conflicting figures flagged in the text (ED conviction data, FATF special recommendations count).')))
