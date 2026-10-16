from lib import Ch

c = Ch(13, 'NABARD, NBFCs, Chit Funds and Ponzi Schemes',
       'Economy · GS Foundation · Chapter 13',
       [('hb', 'Handout only: no class slides'), ('', 'Handout pages 1-13'), ('', 'No PYQs quoted')],
       'NABARD’s origin (CRAFICARD), mission and three kinds of functions (financial, developmental, supervision), LTIF and PMAY-G funding, climate finance (Adaptation Fund, Green Climate Fund, NAFCC, Climate Change Fund), what an NBFC is and how it differs from a bank, NBFC categories and regulators, deposit rules, residuary NBFCs, chit funds, collective investment schemes, and Ponzi and multi-level marketing schemes.')

c.sec('Exam lens: priority and PYQs', 'exam-lens-priority-and-pyqs')
c.call('alert', 'Source note', ['**Handout only.** No class slides, no teacher ink. **No Prelims or Mains PYQ is quoted:** none quoted in the material. Priority below is the handout’s own emphasis (its numbered facts and question-and-answer boxes). Several figures here come from an older RBI FAQ and are **dated** (see the alerts); Chapter 7 carries the newer NBFC scale-based regulation.'])
c.table('What the handout stresses', ['Signal in the handout', 'Where', 'Why it matters'], [
    ['**CRAFICARD** (30 March 1979, B. Sivaraman) → **NABARD Act 61 of 1981** → NABARD on **12 July 1982;** now fully owned by the Government of India', 'Section 1', 'Origin and dates'],
    ['NABARD’s **three function heads:** financial, developmental, supervision', 'Section 2', 'Classification'],
    ['**SHG Bank Linkage 1992;** **KCC;** **LTIF 2016, ₹20,000 crore;** **PMAY-G**', 'Sections 2-3', 'Schemes'],
    ['**NABARD = National Implementing Entity** for the Adaptation Fund (**July 2012,** only NIE for India) and NAFCC', 'Section 5', 'Climate finance'],
    ['**Section 35(6) Banking Regulation Act 1949:** inspection of StCBs, DCCBs, RRBs', 'Section 6', 'Provision'],
    ['**NBFC versus bank:** no demand deposits, no cheques, no DICGC cover', 'Section 7', 'Three differences'],
    ['**Systemically important NBFC:** ₹500 crore; registration **Sec. 45-IA RBI Act 1934,** NOF **₹2 crore** since 1999', 'Section 7', 'Numbers (dated)'],
    ['NBFC categories: **AFC, IC, IFC, IDF-NBFC, CIC, MFI, Factors, MGC, NOFHC**', 'Section 8', 'List with numbers'],
    ['**Chit Funds Act 1982;** **Prize Chits and Money Circulation Schemes (Banning) Act 1978;** CIS regulated by **SEBI**', 'Sections 10-11', 'Regulators'],
])
c.call('key', 'What to prepare', [
    '**Prelims hooks:** NABARD’s origin and committee; SHG-BLP, KCC, LTIF, RIDF, PMAY-G funding; Adaptation Fund versus Green Climate Fund (founding, HQ); NAFCC; NABARD’s supervisory powers; NBFC versus bank; which NBFCs RBI does not regulate and who does; NBFC categories and their thresholds; deposit rules; chit funds versus deposits; CIS regulator; Ponzi and MLM legality.',
    '**Mains hooks:** why a separate rural credit institution was needed; NABARD’s role in microfinance and climate adaptation; why NBFCs are important but regulated differently; why RBI restricts NBFC deposits (depositor protection); the fraud pattern of Ponzi schemes and the multiple-regulator gap.',
    '**Closing idea:** rural credit needs an institution with an unfair focus on the village, and depositor money needs a regulator with an unfair suspicion of everyone else.'])

c.sec('1 · How NABARD came to be')
c.ul(['The importance of **institutional credit for the rural economy** was clear early in planning. At the Government’s insistence RBI constituted the **Committee to Review the Arrangements for Institutional Credit for Agriculture and Rural Development (CRAFICARD)** on **30 March 1979,** chaired by **B. Sivaraman,** former member of the Planning Commission.',
      'Its **interim report (28 November 1979)** asked for a new organisational device giving “undivided attention, forceful direction and pointed focus” to rural credit: a unique **development financial institution.**',
      '**NABARD** was approved by Parliament through **Act 61 of 1981** and came into existence on **12 July 1982,** by **transferring RBI’s agricultural credit functions** and the refinance functions of the **Agricultural Refinance and Development Corporation (ARDC).**',
      'After the share capital of the Government and RBI was revised, **NABARD is today fully owned by the Government of India.**'])
c.call('note', 'Mission (handout)', ['“Promote sustainable and equitable agriculture and rural development through participative financial and non-financial interventions, innovations, technology and institutional development for securing prosperity.”'])

c.sec('2 · Functions at a glance')
c.p('Three heads, touching almost every aspect of the rural economy: **Financial, Developmental, Supervision.**')
c.ul(['Refinance support and rural infrastructure; **district-level credit plans** and guiding banks to meet targets.',
      '**Supervising Cooperative Banks and Regional Rural Banks (RRBs),** helping them adopt sound practices and the **CBS** (core banking) platform.',
      'Designing new development schemes and implementing the Government of India’s schemes; **training handicraft artisans** and giving them a marketing platform.'])
c.call('key', 'Claims to remember (handout)', ['The **SHG Bank Linkage Project (1992)** “has blossomed into the **world’s largest microfinance project**”. **Kisan Credit Card** was designed by NABARD. It has **financed one-fifth of India’s total rural infrastructure** and was a **pioneer in watershed development** as a tool for climate proofing.'])

c.sec('3 · Financial functions')
c.table('Direct and indirect finance', ['Type', 'What it covers'], [
    ['**Direct finance**', 'Loans for **food parks, warehouses, cold storage and cold chain;** credit to **marketing federations;** **Rural Infrastructure Development Fund (RIDF)** and **NABARD Infrastructure Development Assistance;** direct refinance to **cooperative banks;** support to **Producer Organisations**'],
    ['**Indirect finance**', 'Contributions to **Alternative Investment Funds** invested in rural sectors; **Long Term Irrigation Fund;** **PMAY-G** funding'],
], rowhead=True)
c.h3('Long Term Irrigation Fund (LTIF)')
c.ul(['Set up in **2016** within NABARD with an initial corpus of **₹20,000 crore** to fund and fast-track **incomplete major and medium irrigation projects.** A Mission was set up in the Ministry of Water Resources, River Development and Ganga Rejuvenation.',
      'Aim: bridge the resource gap and finish the projects during **2016-2020.** Priority I: **23 projects by 2016-17;** Priority II: **31 projects by 2017-18;** Priority III: **balance 45 projects by 2019-20.**'])
c.h3('PMAY-Grameen (PMAY-G)')
c.ul(['A **pucca house with basic amenities** for all houseless households and those in kutcha or dilapidated houses **by 2022;** implemented by the **Ministry of Rural Development.** About **2.95 crore** houses by 2022; **one crore by March 2019.**',
      'For one crore houses over 3 years (2016-17 to 2018-19) the requirement was **₹81,975 crore:** **₹60,000 crore** from budgetary sources and **₹21,975 crore** through **borrowings from NABARD.** In **2017-18** NABARD sanctioned **₹9,000 crore** to NRIDA for the central share.'])
c.h3('Refinance')
c.table('Refinance types', ['Type', 'Features (handout)'], [
    ['**Off-farm refinance**', 'E.g. rural housing, renewable energy, rural MSMEs'],
    ['**Short-term refinance**', 'Linked to production and productivity, marketing, and raising surplus and savings'],
    ['**Long-term refinance (LTF)**', 'Investment credit that creates **assets and capital formation,** induces technological upgradation. **Long and medium term refinance to banks;** loan period **up to a maximum of 15 years.** For agriculture and allied activities (minor irrigation, farm mechanisation, land development, soil conservation, dairy, sheep/goat), artisans, SSI, non-farm sector, handicrafts, handlooms, powerlooms, and voluntary agencies and **self-help groups**'],
], rowhead=True)
c.p('Eligible to access refinance: **State Cooperative Agricultural and Rural Development Banks, RRBs, commercial banks, NBFCs** and others.')
c.call('alert', 'Handout alert', ['The LTIF, PMAY-G and refinance figures are from **2016-2019** and use targets that have now passed (2020, 2022, March 2019). Treat them as **history of the scheme design,** not as current status. **Exam-hall rule:** a question on “current” status needs the latest budget or ministry data, which is not in this material.'])

c.sec('4 · Developmental functions')
c.ul(['**More than 50% of rural credit** is disbursed by **cooperative banks and RRBs,** and NABARD regulates and supervises them. Under **Institutional Development (ID)** it supports: **Rural Credit Cooperatives; State Cooperative Banks (StCBs); Central Cooperative Banks (CCBs); Primary Agricultural Credit Societies (PACS); State Cooperative Agriculture and Rural Development Banks (SCARDBs); Primary Cooperative Agriculture and Rural Development Banks (PCARDBs).**',
      '**Farm sector:** Farm Sector Development Department (FSDD) and Farm Sector Policy Department (FSPD).',
      '**Off-farm sector:** financial inclusion; micro credit innovation; **women Self-Help Groups, Joint Liability Groups and the SHG-Bank Linkage programme;** microfinance to various bodies.',
      '**RUDSETI / RUDSETI-type institutions / RSETIs:** specialised institutions giving entrepreneurship and skill training to rural youth and women; NABARD assists those meeting its criteria.'])

c.sec('5 · Climate finance: the funds NABARD works with')
c.table('Four climate funds', ['Fund', 'Set up', 'Key facts (handout)'], [
    ['**Adaptation Fund (AF)**', 'Under the **Kyoto Protocol** of the **UNFCCC;** established **2001,** officially launched **2007 at CoP 7, Marrakech**', 'Finances **concrete adaptation projects** for vulnerable communities in developing countries that are Kyoto Parties. Funded by government and private donors **and a 2% share of proceeds of Certified Emission Reductions (CERs)** under the **CDM.** **HQ Washington, USA.** Managed by the **Adaptation Fund Board** (16 members, 16 alternates); **World Bank is interim trustee**'],
    ['**Green Climate Fund (GCF)**', 'Decision at **COP 16, Cancun (December 2010);** operationalised at **COP 17, Durban (2011)**', 'An **operating entity of the financial mechanism of the UNFCCC.** **HQ Songdo, Incheon City, Republic of Korea.** Aims at a **paradigm shift to low-emission, climate-resilient development** by helping developing countries limit emissions and adapt'],
    ['**National Adaptation Fund for Climate Change (NAFCC)**', '**August 2015**', 'Meets adaptation costs for **vulnerable States and UTs.** Budget provision **₹350 crore** for 2015-16 and 2016-17; estimated need **₹181.5 crore** for 2017-18. Prioritises needs under the **State Action Plan on Climate Change (SAPCC)** and missions under the **National Action Plan on Climate Change (NAPCC)**'],
    ['**NABARD Climate Change Fund**', 'Created from NABARD’s profit in **2016-17**', 'NABARD contributes **annually from its profit.** For climate impacts, adaptation and mitigation, awareness, knowledge sharing and sustainable development. A “unique initiative” by a DFI'],
], rowhead=True)
c.ul(['**National Designated Authority (NDA)** for the Adaptation Fund: the **Ministry of Environment, Forest and Climate Change;** proposals go with the NDA’s endorsement.',
      '**NABARD is accredited as National Implementing Entity (NIE)** for the Adaptation Fund in **July 2012** and is **the only NIE for India.** An NIE is a national legal entity nominated by a Party and recognised by the Board as meeting its **fiduciary standards;** it bears **full responsibility** for management, finance, monitoring and reporting.',
      'NABARD is also designated **NIE for NAFCC** by the Government of India: it facilitates identification of project ideas from SAPCCs, formulation, appraisal, sanction, disbursement, monitoring and evaluation, and capacity building. Under the GCF heading the handout also notes **“NABARD is accredited as National Implementing Entity.”**'])
c.call('alert', 'Handout alert', ['The Adaptation Fund line says it was “officially launched in **2007** at **CoP 7** in Marrakech”, and the Green Climate Fund line numbers its COPs (16 in Cancun, 17 in Durban). The year and the COP number for the launch **do not obviously match.** **Exam-hall rule:** remember “established 2001, launched 2007, Marrakech” only if an option uses the same wording; check the COP numbering in your notebook.'])

c.sec('6 · Supervision functions')
c.ul(['**Section 35(6) of the Banking Regulation Act, 1949** empowers NABARD to inspect **State Cooperative Banks, Central Cooperative Banks (DCCBs) and Regional Rural Banks.**',
      'NABARD also inspects, **on a voluntary basis,** state-level cooperative institutions such as **SCARDBs, Apex Weavers Societies and Marketing Federations.**'])
c.table('Objectives of supervision', ['#', 'Objective'], [
    ['1', 'Protect the interest of **present and future depositors**'],
    ['2', 'Ensure business conforms to the relevant **Acts, rules, regulations and bye-laws**'],
    ['3', 'Ensure observance of rules and guidelines of **NABARD, RBI and the Government**'],
    ['4', 'Examine the **financial soundness** of the banks'],
    ['5', 'Suggest ways to strengthen institutions so they can **purvey rural credit** more efficiently'],
], rowhead=True)

c.sec('7 · NBFCs: what they are and how they differ from banks')
c.ul(['A **Non-Banking Financial Company (NBFC)** is a company registered under the **Companies Act, 1956** engaged in **loans and advances; acquisition of shares, stocks, bonds, debentures, securities; leasing; hire-purchase; insurance business; chit business.** It excludes institutions whose **principal business** is agriculture, industry, trading in goods (other than securities), providing services, or buying, selling or constructing immovable property.',
      'A company whose principal business is **receiving deposits** under any scheme, lump sum or instalments, is also an NBFC: the **Residuary Non-Banking Company (RNBC).**'])
c.table('NBFC versus bank (the three differences)', ['', 'Bank', 'NBFC'], [
    ['**Demand deposits**', 'Can accept', '**Cannot** accept demand deposits'],
    ['**Payment and settlement system**', 'Part of it; issues cheques drawn on itself', '**Not part of it;** cannot issue cheques drawn on itself'],
    ['**Deposit insurance (DICGC)**', 'Available', '**Not available** to NBFC depositors'],
], rowhead=True)
c.ul(['**Systemically important NBFCs:** asset size of **₹500 crore or more** (last audited balance sheet), because their activities bear on the financial stability of the economy.',
      '**Registration:** under **Section 45-IA of the RBI Act, 1934,** no NBFC may carry on business without a **Certificate of Registration** and **Net Owned Funds (NOF) of ₹25 lakh (₹2 crore since April 1999).**',
      '**Exempt from RBI registration** (to avoid dual regulation), subject to conditions: **Venture Capital Fund, Merchant Banking and Stock-broking companies** (SEBI); **insurance companies** (IRDA); **Nidhi companies** (Ministry of Corporate Affairs; Section 620A Companies Act 1956); **Chit companies** (Chit Funds Act 1982; State Governments); **Housing Finance Companies** (**National Housing Bank**); **Stock Exchanges; Mutual Benefit companies.** **Mortgage Guarantee Companies** are notified as NBFCs (Section 45-I(f)(iii)); **Core Investment Companies** under ₹100 crore, or ₹100 crore and above but not accessing public funds, are exempt.'])
c.table('Who regulates what (handout)', ['Entity', 'Regulator'], [
    ['Housing Finance Companies', 'National Housing Bank'],
    ['Merchant bankers, VCFs, stock exchanges, stock brokers and sub-brokers', 'SEBI'],
    ['Insurance companies', 'IRDA'],
    ['Chit fund companies', 'State Governments (under the Chit Funds Act 1982)'],
    ['Nidhi companies', 'Ministry of Corporate Affairs'],
    ['Deposit acceptance of banks, co-operative banks and NBFCs', 'RBI'],
], rowhead=True)
c.call('alert', 'Handout alert', ['This handout classifies systemically important NBFCs at **₹500 crore;** **Chapter 7** (the newer scale-based regulation, 2022) uses layers with the Base Layer at **non-deposit NBFCs below ₹1,000 crore.** They are different regimes. **Exam-hall rule:** pick the figure that matches the wording of the question (older “NBFC-ND-SI” language: ₹500 crore; scale-based layers: ₹1,000 crore base). The handout also quotes the **DICGC cover as ₹1 lakh,** which may be dated; check the current limit.'])

c.sec('8 · Categories of NBFCs')
c.p('NBFCs are classified by **liabilities** (deposit-accepting and non-deposit-accepting), by **size** (non-deposit taking: **systemically important, NBFC-ND-SI,** and others, **NBFC-ND**), and by **activity.**')
c.table('Types by activity', ['Type', 'Definition (handout)'], [
    ['**Asset Finance Company (AFC)**', 'Principal business is **financing physical assets** supporting productive activity, e.g. automobiles, tractors'],
    ['**Investment Company (IC)**', 'Principal business is the **acquisition of securities**'],
    ['**Infrastructure Finance Company (IFC)**', 'At least **75% of total assets in infrastructure loans;** minimum **NOF ₹300 crore;** minimum rating **“A”;** **CRAR 15%**'],
    ['**Infrastructure Debt Fund NBFC (IDF-NBFC)**', 'Facilitates **long-term debt into infrastructure;** raises rupee or dollar bonds of **minimum 5-year maturity;** **only IFCs can sponsor** IDF-NBFCs'],
    ['**Systemically Important Core Investment Company (CIC-ND-SI)**', 'NBFC acquiring shares and securities, meeting conditions'],
    ['**NBFC-Micro Finance Institution (NBFC-MFI)**', 'Non-deposit taking; **not less than 85% of assets** in qualifying assets'],
    ['**NBFC-Factors**', 'Non-deposit taking; principal business **factoring;** financial assets in factoring **at least 50% of total assets** and income from it **not less than 50% of gross income**'],
    ['**Mortgage Guarantee Company (MGC)**', '**At least 90%** of turnover or gross income from mortgage guarantee; **NOF ₹100 crore**'],
    ['**NBFC-NOFHC (Non-Operative Financial Holding Company)**', 'Wholly owned vehicle through which a promoter group sets up a **new bank,** holding the bank and other financial services companies'],
], rowhead=True)

c.sec('9 · Residuary NBFCs, prudential norms, interest and deposits')
c.ul(['**RNBC:** principal business is **receiving deposits** under any scheme, and it is **not** an Investment, Asset Financing or Loan company. It must maintain **investments as per RBI directions,** in addition to liquid assets, and prudential norms apply. **No ceiling** on deposits, but **100% of deposit liability** must be invested in highly liquid, secure instruments: **Central/State government securities, fixed deposits with scheduled commercial banks, CoDs of SCBs/FIs, units of mutual funds.**',
      '**Prudential norms:** NBFC (Deposit Accepting or Holding) Prudential Norms **Directions 2007;** Non-SI Non-Deposit NBFCs **Directions 2015;** SI Non-Deposit NBFCs **Directions 2015.** They cover income recognition, asset classification, provisioning, exposure norms, disclosures, capital adequacy, limits on investment in land and building and unquoted shares, and **LTV for gold-loan NBFCs.** Deposit-accepting NBFCs also meet **statutory liquidity** requirements.',
      '**Interest rates:** RBI has **deregulated** interest on loans by financial institutions (**except NBFC-MFIs**). The rate depends on the loan agreement but must be **transparent and disclosed** in the application form and sanction letter.'])
c.table('Who may accept public deposits', ['Entity', 'Rule'], [
    ['**Banks, including co-operative banks**', 'May accept deposits'],
    ['**NBFCs with a deposit-accepting CoR**', 'Only those with a **specific authorisation** and an **investment-grade rating,** to a limit of **1.5 times NOF**'],
    ['**Housing Finance Companies;** companies under the **Companies (Acceptance of Deposits) Rules**', 'Up to a certain limit'],
    ['**Co-operative credit societies**', 'From **members** only, not the general public'],
    ['**Unincorporated bodies** (individuals, partnerships, associations)', '**Prohibited** from deposit-taking as principal business; prohibited from even accepting deposits if they carry on financial business'],
], rowhead=True)
c.ul(['**Since 1997 RBI has issued no new CoR for deposit acceptance** to NBFCs; as a matter of policy only **banks** should accept public deposits.',
      '**Deposit terms (handout):** maximum interest **12.5%;** paid or compounded at rests not shorter than monthly; **minimum 12 months, maximum 60 months;** **no deposits repayable on demand.** Unrated AFCs had to be rated by **31 March 2016** or could not renew or accept deposits.',
      '**Why so restrictive:** depositors place money **on trust,** unlike an investor who shares risk and return; **protection of depositors’ interest is supreme.** Banks are the most regulated; **DICGC** pays insurance on deposits up to **₹1 lakh** if a bank fails (handout figure).'])

c.sec('10 · Chit funds')
c.ul(['**Chit funds / chitty / kuri** are **saving institutions** with no standard form: members make **periodic subscriptions;** each period’s collection goes to one member chosen by **bid, lot, auction or tender;** every member gets a turn before a second round. They are the Indian version of **Rotating Savings and Credit Associations (ROSCAs).**',
      '**Chit Funds Act, 1982, Section 2(b):** a “chit” is a transaction where a person agrees with a specified number of persons that each subscribes a sum (or grain) in instalments over a definite period, and **each subscriber in turn** gets the **prize amount** by lot, auction or tender. **It is not a chit** if some, but not all, subscribers get the prize without liability to pay future subscriptions, or if all get it by turns **with** a liability to pay future subscriptions.',
      '**Regulation:** the **Chit Funds Act 1982** is a **Central Act administered by State Governments;** the Centre has framed **no rules,** so **registration and regulation are by States** under their own rules. RBI counts them as NBFCs under **Miscellaneous Non-Banking Company (MNBC)** but has laid down **no separate framework.**',
      '**Fraud:** cheating by a chit company through fraudulent schemes is an offence under the **Prize Chits and Money Circulation Schemes (Banning) Act, 1978;** State Governments investigate and prosecute.',
      '**Name rule:** under **Rule 8(2)(b)(iii) of the Companies (Incorporation) Rules, 2014** a company whose main business is a chit fund cannot be incorporated unless its name indicates it (“Chit Fund”).'])
c.table('Chit subscription versus deposit', ['', 'Deposit (RBI Act 1934)', 'Chit'], [
    ['**Definition**', 'Acceptance of money **other than** share capital, money from banks and FIs, security deposits, earnest money and advances against goods or services, and **subscriptions to chits.** All other amounts received as loan or in any form are deposits', 'Instalment subscriptions with a rotating prize; **specifically excluded** from “deposit”'],
    ['**RBI position**', 'Regulated', 'Chit funds **prohibited by RBI from accepting deposits from August 2009;** RBI can prosecute a chit fund that accepts public deposits'],
], rowhead=True)
c.call('alert', 'Handout alert', ['The handout gives the date of the RBI prohibition on chit funds accepting deposits as **“August 2009”** in one place and **“2009”** in another. They agree on the year. Another small point: the section on “regulation” says RBI has **no** framework for chit funds, yet it also says RBI **can prosecute** a chit fund that takes deposits. **Exam-hall rule:** chit funds are regulated by **State Governments;** RBI’s only hook is the deposit ban.'])

c.sec('11 · Collective investment schemes, MLM and Ponzi schemes')
c.table('Who regulates what', ['Activity', 'Regulator or law'], [
    ['**Multi-Level Marketing, direct selling, online selling companies**', '**Not RBI.** The respective **State Government**'],
    ['**Collective Investment Schemes (CIS)** (money for units: time-share in resorts, profit from sale of wood, developed commercial plots)', '**SEBI.** Complaints go to SEBI and to the **EOW/Police of the State Government**'],
    ['**Money circulation, MLM / pyramid and Ponzi schemes**', 'Banned under the **Prize Chits and Money Circulation Schemes (Banning) Act, 1978;** acceptance of money is a **cognizable offence;** monitored and dealt with by **State Governments.** RBI’s role: only advising and assisting the Centre in framing rules'],
], rowhead=True)
c.ul(['**Pyramid / MLM:** income comes **not from selling a product** but from enrolling more members who pay hefty fees; a portion goes up the pyramid. **Any break in the chain collapses it,** and the lowest members suffer most.',
      '**Ponzi scheme:** collects money on promises of **high returns;** with **no asset creation,** one depositor’s money is paid as another’s return. The scheme becomes unviable, cannot return even the principal, and the perpetrators disappear.',
      'The 1978 Act prohibits any person to **promote or conduct** a prize chit or money circulation scheme, **enrol** as a member, or participate by **receiving or remitting money.**'])

c.mm = ('NABARD and NBFCs', [
    ('NABARD origin', [('CRAFICARD 30 Mar 1979, B. Sivaraman', None), ('Interim report 28 Nov 1979', None), ('Act 61 of 1981; 12 July 1982', None), ('From RBI credit + ARDC; govt owned', None)]),
    ('Financial', [('Direct: food parks, RIDF, co-op refinance', None), ('Indirect: AIFs, LTIF, PMAY-G', None), ('Refinance up to 15 years', None), ('Short, long and off-farm', None)]),
    ('Developmental', [('Cooperatives, PACS, SCARDBs', None), ('SHG-Bank Linkage 1992', None), ('RUDSETI / RSETIs', None), ('KCC; watershed', None)]),
    ('Climate finance', [('Adaptation Fund; NIE July 2012', None), ('Green Climate Fund: Cancun 2010', None), ('NAFCC Aug 2015', None), ('Climate Change Fund 2016-17', None)]),
    ('Supervision', [('Sec. 35(6) BR Act 1949', None), ('StCBs, DCCBs, RRBs', None), ('Protect depositors', None), ('Voluntary: SCARDBs, weavers', None)]),
    ('NBFCs', [('No demand deposits, cheques, DICGC', None), ('SI: ₹500 crore (older)', None), ('Sec. 45-IA; NOF ₹2 crore', None), ('Exempt: HFC, SEBI, IRDA, Nidhi, chit', None)]),
    ('NBFC types', [('AFC, IC, IFC (75%, ₹300 crore)', None), ('IDF-NBFC, CIC, MFI (85%)', None), ('Factors (50%), MGC (90%)', None), ('NOFHC for new bank', None)]),
    ('Informal finance', [('Chit Funds Act 1982: States', None), ('Prize Chits Act 1978', None), ('CIS: SEBI', None), ('Ponzi/MLM banned', None)]),
])

c.timeline = [
    ('1978', 'Prize Chits and Money Circulation Schemes (Banning) Act.', False),
    ('30 March 1979', 'CRAFICARD (B. Sivaraman Committee) constituted.', True),
    ('28 November 1979', 'CRAFICARD interim report recommends a new rural DFI.', False),
    ('1981', 'NABARD Act 61 of 1981.', True),
    ('12 July 1982', 'NABARD comes into existence (RBI agricultural credit functions + ARDC refinance).', True),
    ('1982', 'Chit Funds Act.', False),
    ('1992', 'SHG Bank Linkage Project launched.', True),
    ('1997', 'RBI stops issuing new CoRs to NBFCs for deposit acceptance.', True),
    ('April 1999', 'NOF requirement for NBFCs raised from ₹25 lakh to ₹2 crore.', False),
    ('2001 / 2007', 'Adaptation Fund established / officially launched (per handout).', False),
    ('August 2009', 'RBI prohibits chit funds from accepting deposits.', False),
    ('December 2010', 'Decision to set up the Green Climate Fund (COP 16, Cancun).', False),
    ('2011', 'GCF operationalised at COP 17, Durban.', False),
    ('July 2012', 'NABARD accredited NIE for the Adaptation Fund.', True),
    ('August 2015', 'National Adaptation Fund for Climate Change (NAFCC).', False),
    ('2016', 'Long Term Irrigation Fund, ₹20,000 crore.', True),
    ('2016-17', 'NABARD Climate Change Fund created from profit.', False),
]

c.connects = [
    ('[Chapter 7: Banking and NBFCs](eco-ch07.html)', 'The newer scale-based NBFC regulation and the banking structure; this chapter’s NBFC figures are the older RBI FAQ.'),
    ('[Chapter 9: Capital Markets](eco-ch09.html)', 'SEBI regulates CIS, merchant bankers and stock-brokers; mutual funds are approved investments for RNBC deposits.'),
    ('[Chapter 8: Money and Monetary Policy](eco-ch08.html)', 'CoDs and G-Secs appear as RNBC investments.'),
    ('[Chapter 12: Budget and Fiscal Policy](eco-ch12.html)', 'CSS and Central Sector schemes such as PMAY-G.'),
    ('[Chapter 3: Unemployment](eco-ch03.html)', 'RSETIs and SHGs link to rural livelihoods and self-employment.'),
]

c.recall = [
    'CRAFICARD (30 Mar 1979, B. Sivaraman) → NABARD Act 61 of 1981 → NABARD 12 July 1982. Took RBI’s agri credit and ARDC refinance. Now fully GoI-owned.',
    'Three functions: financial, developmental, supervision. SHG-BLP 1992 = world’s largest microfinance project. KCC designed by NABARD.',
    'LTIF 2016, ₹20,000 crore, incomplete irrigation projects (23 + 31 + 45). PMAY-G: ₹81,975 crore for one crore houses, ₹21,975 crore via NABARD.',
    'Long-term refinance up to 15 years. Eligible: StCARDBs, RRBs, commercial banks, NBFCs.',
    'More than 50% of rural credit by co-operative banks and RRBs.',
    'Adaptation Fund: Kyoto Protocol, 2% of CER proceeds, HQ Washington, NABARD NIE July 2012. GCF: Cancun 2010, Durban 2011, HQ Songdo. NAFCC Aug 2015. NABARD Climate Change Fund from 2016-17 profits.',
    'Supervision: Section 35(6) BR Act 1949 (StCBs, DCCBs, RRBs); SCARDBs voluntary.',
    'NBFC ≠ bank: no demand deposits, no cheques, no DICGC. SI NBFC ₹500 crore (older). Sec. 45-IA; NOF ₹2 crore since April 1999.',
    'RBI does not register: VCF/merchant bankers/brokers (SEBI), insurance (IRDA), Nidhi (MCA), chit (States), HFC (NHB).',
    'IFC 75%, NOF ₹300 crore, rating A, CRAR 15%. MFI 85%. Factors 50%/50%. MGC 90%, ₹100 crore. NOFHC sets up a new bank.',
    'RNBC: deposits, 100% invested in approved instruments. Deposits only with CoR + investment grade, up to 1.5 × NOF; 12-60 months; max 12.5%; no new CoR since 1997.',
    'Chit funds: Chit Funds Act 1982 (States); not deposits; banned from deposits Aug 2009. CIS: SEBI. MLM, Ponzi: banned by the 1978 Act; States enforce.',
]

c.mcq = [
    {'q': 'NABARD came into existence on…', 'options': ['30 March 1979', '28 November 1979', '12 July 1982', '1 April 1981'], 'answer': 2, 'explain': 'The Act is 61 of 1981; NABARD started 12 July 1982.'},
    {'q': 'The committee whose recommendation led to NABARD was chaired by…', 'options': ['B. Sivaraman', 'N.K. Singh', 'Y.V. Reddy', 'Narasimham'], 'answer': 0, 'explain': 'CRAFICARD, constituted 30 March 1979.'},
    {'q': 'NABARD was formed by transferring RBI’s agricultural credit functions and the refinance functions of…', 'options': ['IDBI', 'ARDC', 'NHB', 'SIDBI'], 'answer': 1, 'explain': 'The Agricultural Refinance and Development Corporation.'},
    {'q': 'The SHG Bank Linkage Project was launched in…', 'options': ['1982', '1992', '1999', '2005'], 'answer': 1, 'explain': 'The handout calls it the world’s largest microfinance project.'},
    {'q': 'Which of these is the only National Implementing Entity for the Adaptation Fund in India?', 'options': ['EXIM Bank', 'SIDBI', 'NABARD', 'IREDA'], 'answer': 2, 'explain': 'Accredited July 2012; also NIE for NAFCC.'},
    {'q': 'The Green Climate Fund is headquartered at…', 'options': ['Washington', 'Songdo, Incheon, Korea', 'Geneva', 'Bonn'], 'answer': 1, 'explain': 'The Adaptation Fund is headquartered in Washington.'},
    {'q': 'Which Act gives NABARD power to inspect StCBs, DCCBs and RRBs?', 'options': ['Section 35(6), Banking Regulation Act 1949', 'Section 45-IA, RBI Act 1934', 'NABARD Act 1981 only', 'Companies Act 2013'], 'answer': 0, 'explain': 'Section 45-IA is the NBFC registration provision.'},
    {'q': 'Which of the following is a difference between NBFCs and banks?', 'options': ['NBFCs cannot lend', 'NBFCs cannot accept demand deposits', 'NBFCs cannot hold securities', 'NBFCs are not companies'], 'answer': 1, 'explain': 'Also: not part of the payment system and no DICGC insurance.'},
    {'q': 'Housing Finance Companies are regulated by…', 'options': ['SEBI', 'IRDA', 'National Housing Bank', 'Ministry of Corporate Affairs'], 'answer': 2, 'explain': 'They are exempt from RBI registration.'},
    {'q': 'Nidhi companies are regulated by…', 'options': ['RBI', 'Ministry of Corporate Affairs', 'SEBI', 'State Governments'], 'answer': 1, 'explain': 'Chit funds are regulated by State Governments.'},
    {'q': 'An Infrastructure Finance Company must deploy at least what share of assets in infrastructure loans?', 'options': ['50%', '75%', '85%', '90%'], 'answer': 1, 'explain': 'Also NOF ₹300 crore, rating “A” and CRAR 15%. MFI is 85%.'},
    {'q': 'Only which entities can sponsor an IDF-NBFC?', 'options': ['Any NBFC', 'Infrastructure Finance Companies', 'Banks only', 'Mutual funds'], 'answer': 1, 'explain': 'IDF-NBFCs raise bonds of minimum 5-year maturity.'},
    {'q': 'RBI has not issued a new Certificate of Registration to NBFCs for deposit acceptance since…', 'options': ['1982', '1997', '2009', '2016'], 'answer': 1, 'explain': 'As a matter of public policy only banks should accept public deposits.'},
    {'q': 'Chit funds are regulated mainly by…', 'options': ['RBI', 'SEBI', 'State Governments under the Chit Funds Act 1982', 'NABARD'], 'answer': 2, 'explain': 'It is a Central Act administered by States; RBI banned chit funds from accepting deposits in 2009.'},
    {'q': 'Collective Investment Schemes are regulated by…', 'options': ['RBI', 'SEBI', 'NABARD', 'State Governments'], 'answer': 1, 'explain': 'MLM and direct-selling companies fall under State Governments.'},
]
for q in c.mcq:
    q.pop('explanation', None)

c.mains = [
    ('Discuss the genesis, functions and role of NABARD in India’s rural economy.',
     'NABARD was created as a development finance institution with “undivided attention” to rural credit.',
     ['CRAFICARD 1979, Act 61 of 1981, 12 July 1982; RBI agri credit plus ARDC refinance; now fully GoI-owned.', 'Three functions: financial (refinance, RIDF, LTIF, PMAY-G), developmental (cooperatives, SHG-BLP, RSETIs), supervision (StCBs, DCCBs, RRBs).', 'SHG-BLP the world’s largest microfinance project; KCC; one-fifth of rural infrastructure.'],
     'NABARD is the rural economy’s banker’s bank.'),
    ('How is NABARD involved in climate finance in India?',
     'India’s adaptation needs are met through international and national funds, with NABARD as the implementing agency.',
     ['NIE for the Adaptation Fund (July 2012, only NIE for India) and for NAFCC (August 2015).', 'Adaptation Fund (Kyoto, 2% of CER proceeds) and the Green Climate Fund (Cancun 2010).', 'NABARD’s own Climate Change Fund from 2016-17 profit.', 'Watershed development as climate proofing.'],
     'Rural resilience is financed one watershed at a time.'),
    ('Differentiate NBFCs from banks. Why does RBI restrict their deposit-taking?',
     'NBFCs lend and invest like banks but lack some banking features.',
     ['No demand deposits, no cheque or payment-system access, no DICGC cover.', 'Registration (Sec. 45-IA); categories by liabilities, size and activity; exempt categories regulated by SEBI, IRDA, NHB, MCA, States.', 'No new deposit CoR since 1997; rated, capped at 1.5 × NOF, 12-60 months.', 'Depositors place money on trust; protection is supreme.'],
     'Lend like a bank, but never hold the public’s trust like one.'),
    ('Examine the regulatory framework for chit funds and the 1978 Act on prize chits and money circulation schemes.',
     'Informal savings schemes sit across State and Central laws, which creates regulatory gaps.',
     ['Chit Funds Act 1982: Central Act administered by States; no Central rules; RBI deposit ban since 2009.', 'Chit subscriptions are not deposits.', 'MLM, pyramid and Ponzi schemes are banned by the 1978 Act and enforced by States.', 'CIS regulated by SEBI.'],
     'A fraud that spans three regulators is a fraud that is hard to catch.'),
    ('Explain the types of NBFCs and the conditions that define each.',
     'NBFCs are classified by what they do and how large they are.',
     ['AFC and IC by principal business; IFC (75% infrastructure loans, ₹300 crore NOF, rating A, CRAR 15%).', 'IDF-NBFC, CIC, MFI (85%), Factors (50%/50%), MGC (90%, ₹100 crore).', 'NOFHC for promoters setting up a new bank.'],
     'The label tells you the regulation.'),
]

c.cards = [
    ('CRAFICARD date and chair?', '30 March 1979; B. Sivaraman.'),
    ('NABARD Act?', 'Act 61 of 1981.'),
    ('NABARD start date?', '12 July 1982.'),
    ('NABARD took over what?', 'RBI’s agricultural credit functions and ARDC’s refinance.'),
    ('NABARD ownership?', 'Fully owned by the Government of India.'),
    ('Three NABARD functions?', 'Financial, developmental, supervision.'),
    ('SHG-BLP year?', '1992; world’s largest microfinance project.'),
    ('KCC?', 'Kisan Credit Card, designed by NABARD.'),
    ('NABARD’s infrastructure share?', 'Financed one-fifth of India’s rural infrastructure.'),
    ('LTIF?', '2016; ₹20,000 crore; incomplete irrigation projects.'),
    ('LTIF projects?', '23 (priority I) + 31 (II) + 45 (III).'),
    ('PMAY-G funding for 1 crore houses?', '₹81,975 crore: ₹60,000 budget + ₹21,975 NABARD.'),
    ('Long-term refinance period?', 'Up to 15 years.'),
    ('Who can access refinance?', 'StCARDBs, RRBs, commercial banks, NBFCs.'),
    ('Share of rural credit by co-op banks and RRBs?', 'More than 50%.'),
    ('RSETI/RUDSETI?', 'Entrepreneurship and skill training for rural youth and women.'),
    ('Adaptation Fund: set up under?', 'Kyoto Protocol (UNFCCC); 2% of CDM CER proceeds.'),
    ('Adaptation Fund HQ and trustee?', 'Washington; World Bank (interim).'),
    ('NDA for Adaptation Fund in India?', 'Ministry of Environment, Forest and Climate Change.'),
    ('NABARD NIE date?', 'July 2012; the only NIE for India.'),
    ('GCF decision and start?', 'COP 16 Cancun, Dec 2010; COP 17 Durban, 2011.'),
    ('GCF HQ?', 'Songdo, Incheon, Republic of Korea.'),
    ('NAFCC?', 'National Adaptation Fund for Climate Change, August 2015.'),
    ('NABARD Climate Change Fund?', 'From NABARD profit, 2016-17.'),
    ('Supervision provision?', 'Section 35(6), Banking Regulation Act 1949.'),
    ('Institutions NABARD inspects?', 'StCBs, DCCBs, RRBs (voluntarily SCARDBs, weavers, federations).'),
    ('NBFC definition?', 'Company engaged in loans, securities, leasing, hire-purchase, insurance, chits; not mainly agriculture, industry, trade or property.'),
    ('Three NBFC-bank differences?', 'No demand deposits; no payment system/cheques; no DICGC.'),
    ('SI NBFC threshold (this handout)?', '₹500 crore.'),
    ('NBFC registration section?', 'Section 45-IA, RBI Act 1934.'),
    ('NBFC NOF?', '₹25 lakh; ₹2 crore since April 1999.'),
    ('NBFC exemptions?', 'VCF/merchant/broker (SEBI), insurance (IRDA), Nidhi (MCA), chit (States), HFC (NHB).'),
    ('IFC conditions?', '75% infra assets, NOF ₹300 crore, rating A, CRAR 15%.'),
    ('IDF-NBFC?', 'Long-term infra bonds, min 5 years; sponsored only by IFCs.'),
    ('NBFC-MFI?', 'Non-deposit; at least 85% qualifying assets.'),
    ('NBFC-Factors?', 'Factoring assets ≥ 50% and income ≥ 50%.'),
    ('MGC?', '≥ 90% business is mortgage guarantee; NOF ₹100 crore.'),
    ('NOFHC?', 'Holding company for a promoter’s new bank.'),
    ('RNBC?', 'Deposit-taking NBFC; 100% deposits in approved investments.'),
    ('NBFC deposit conditions?', 'Specific CoR, investment grade, up to 1.5 × NOF, 12-60 months, max 12.5%.'),
    ('No new deposit CoR since?', '1997.'),
    ('Why restrict NBFC deposits?', 'Depositors trust; protection supreme.'),
    ('DICGC cover (handout)?', '₹1 lakh (may be dated).'),
    ('Chit fund?', 'ROSCA: periodic subscriptions, rotating prize by lot, auction or tender.'),
    ('Chit Funds Act year and administrator?', '1982; State Governments.'),
    ('Chit funds and deposits?', 'Subscriptions are not deposits; deposits banned Aug 2009.'),
    ('Chit company name rule?', 'Must indicate “Chit Fund” (Rule 8(2)(b)(iii), 2014).'),
    ('CIS regulator?', 'SEBI.'),
    ('MLM and direct selling regulator?', 'State Governments.'),
    ('Ponzi scheme?', 'Pays old investors from new money; no asset creation; collapses.'),
    ('Pyramid/MLM scheme?', 'Income from enrolling members, not product sales.'),
    ('Banning law?', 'Prize Chits and Money Circulation Schemes (Banning) Act, 1978; State enforcement.'),
]
c.summary = 'NABARD’s origin (CRAFICARD, Act 61 of 1981), its financial, developmental and supervisory functions, LTIF and PMAY-G, climate funds (Adaptation Fund, Green Climate Fund, NAFCC), NBFC definition, categories and regulators, deposit rules, chit funds, CIS and Ponzi schemes.'
