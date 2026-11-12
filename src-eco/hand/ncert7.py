# -*- coding: utf-8 -*-
"""NCERT content for handout Ch 7 (Banking and NBFCs). Commercial-bank balance sheet, money creation, CRR/SLR mechanics and
RBI tools are in the Chapter 8 NCERT boxes (hand/ncert8.py) and are NOT repeated here.
Sources: XI Indian Economic Development Ch 3 and Ch 5, XI and XII glossaries, XII Macro Ch 1 and Ch 3. NCERT has no text on
Basel, CRAR, NPA classes, 4R, SARFAESI, IBC or NBFC layers: those are handout-only."""
SRC = 'NCERT'
def T(head, rows): return {'head': head, 'rows': rows}
NC = {
 '1': [dict(ref='XII Macro Ch 1 (macro decision makers), XI Ch 3 (financial sector), XI Glossary',
   why='The handout splits middlemen into those who decide (banks, NBFCs) and those who only facilitate (brokers, exchanges). NCERT does not draw that split, but it names the same institutions and who watches them. Use this box to put NCERT’s words next to the handout’s two columns.',
   link='Handout section 1: RBI regulates decision-making intermediaries; SEBI regulates decision-facilitating ones. NCERT’s “financial sector” covers both columns.',
   blocks=[
    dict(h='Step 1 · What NCERT calls the financial sector', pts=[
         'XI Ch 3: the financial sector includes financial institutions such as <b>commercial banks, investment banks, stock exchange operations and the foreign exchange market</b>. NCERT says it is regulated by the <b>Reserve Bank of India (RBI)</b>.',
         'XII Macro Ch 1: macroeconomic policies are pursued by the State itself or by statutory bodies like <b>RBI</b> and <b>SEBI</b>, each with public goals set by law, not private profit.']),
    dict(h='Step 2 · NCERT’s glossary words (XI Glossary)', tbl=T(['Term', 'NCERT’s definition'], [
         ['Financial institutions', 'Institutions that engage in mobilisation and allocation of savings. They include commercial banks, cooperative banks, developmental banks and investment institutions'],
         ['Merchant bankers', 'Banks or financial institutions, also known as investment bankers, that specialise in advising companies and managing their equity and debt requirement through floatation and sale or purchase of stocks and bonds'],
         ['Foreign Institutional Investors (FIIs)', 'Banking and non-banking financial institutions of foreign origin, such as commercial banks, investment banks, mutual funds, pension funds']])),
   ],
   d=['NCERT says “all banks and other financial institutions” are regulated by the RBI. The handout says SEBI regulates brokers and stock exchanges and RBI regulates banks and NBFCs. Handout wins.'])],
 '2': [dict(ref='XI Ch 3 (financial sector reforms; Exercise 3 and 4), XII Macro Ch 3 §3.2.2, XI and XII Glossaries',
   why='The handout says CRR and SLR are “deposit-side” rules set by RBI. NCERT says what RBI decides for banks and gives its short definitions of CRR and SLR. How these two actually limit money creation is in the <b>Chapter 8 NCERT boxes</b>, so it is not repeated here.',
   link='Handout section 2: depositor protection, reserve ratios, lending-side rules. NCERT’s “RBI controls banks” list is a short version of the same idea.',
   blocks=[
    dict(h='Step 1 · What RBI decides for banks (NCERT, XI Ch 3)', pts=['The RBI decides the <b>amount of money that the banks can keep with themselves</b>, fixes <b>interest rates</b> and the <b>nature of lending to various sectors</b>.',
         'NCERT Exercise 4 asks: “How is RBI controlling the commercial banks?” These three points are the NCERT answer.']),
    dict(h='Step 2 · CRR and SLR in NCERT’s glossaries', tbl=T(['Term', 'XII Macro Glossary', 'XI Glossary'], [
         ['Cash Reserve Ratio (CRR)', 'The fraction of their deposits which the commercial banks are required to keep with RBI', 'A proportion of the total deposits and reserves of the commercial banks to be kept with the central bank in liquid form; a measure of control of RBI over commercial banks'],
         ['Statutory Liquidity Ratio (SLR)', 'The fraction of their total demand and time deposits which banks must invest in specified liquid assets', 'A minimum proportion of the total deposits and reserves to be maintained by banks in liquid form; an obligation in addition to the CRR'],
         ['Reserve deposit ratio', 'The fraction of their total deposits which commercial banks keep as reserves', '']])),
    dict(h='Step 3 · Where the rest is', pts=['Bank balance sheet, loans and reserves, the worked money creation example, lender of last resort and Bank Rate are in the <b>Chapter 8</b> NCERT boxes (XII Macro Ch 3).'])],
   d=['The two NCERT glossaries word CRR differently (“fraction of their deposits kept with RBI” against “proportion of total deposits and reserves kept in liquid form”). The handout keeps CRR as cash with RBI. Use the handout.'])],
 '5': [dict(ref='XI Ch 5 §5.3 (Rural Banking: a Critical Appraisal; Work These Out)',
   why='The handout lists wilful default, economic reasons and poor risk assessment as the reasons for NPAs. NCERT has a short rural-lending case where the same debate appears: are loans not repaid on purpose, or because of events?',
   link='Handout section 5, table of reasons: A wilful default; B economic reasons (acts of God such as floods and droughts); C poor risk assessment.',
   blocks=[
    dict(h='NCERT’s two views on farm-loan default', tbl=T(['NCERT’s sentence', 'Which handout reason it matches'], [
         ['Agriculture loan default rates have been chronically high', 'Context for NPAs in the agriculture sector'],
         ['“It is alleged that farmers are deliberately refusing to pay back loans.”', 'A · wilful default (NCERT only reports the allegation and asks you to think of reasons)'],
         ['Farmers could not pay back “due to crop failure, insufficient income and employment opportunities”', 'B · economic reasons (crop failure is an act of God)'],
         ['Apart from commercial banks, other formal institutions “failed to develop a culture of deposit mobilisation, lending to worthwhile borrowers and effective loan recovery”', 'C · poor risk assessment and weak recovery']]))],
   d=['NCERT does not give NPA classes (SMA, sub-standard, doubtful, loss) or GNPA ratios. Those are in the handout only.'])],
 '7': [dict(ref='XI Ch 3 (Financial Sector Reforms), XI Glossary',
   why='The handout’s phase 3 says “Liberalisation (1990s): new private bank licences”. NCERT’s account of the same reform is short but adds three facts the handout does not give (the 74 per cent limit, freedom to open branches, and FIIs).',
   link='Handout section 7, phase 3: RBI issued new private bank licences in 1993; Lead Bank Scheme; branch licensing. NCERT frames the same period as a change in the RBI’s role.',
   blocks=[
    dict(h='Step 1 · The aim: RBI from regulator to facilitator', pts=['NCERT: “One of the major aims of financial sector reforms is to reduce the role of RBI from <b>regulator</b> to <b>facilitator</b> of the financial sector.” The sector may take decisions on many matters without consulting the RBI.',
         'NCERT Exercise 3: “Why did RBI have to change its role from controller to facilitator of financial sector in India?”']),
    dict(h='Step 2 · What the reforms did (NCERT)', tbl=T(['Reform', 'NCERT’s words'], [
         ['Private banks', 'The reform policies led to establishment of <b>private sector banks, Indian as well as foreign</b>'],
         ['Foreign investment in banks', 'Limit raised to around <b>74 per cent</b>'],
         ['Branches', 'Banks that fulfil certain conditions are free to set up <b>new branches without RBI approval</b> and rationalise existing branch networks'],
         ['Raising resources', 'Banks may generate resources from India and abroad; certain managerial aspects are <b>retained with the RBI</b> to safeguard the interests of account-holders and the nation'],
         ['Foreign investors', 'FIIs (merchant bankers, mutual funds, pension funds) are allowed to invest in Indian financial markets']]))],
   d=['NCERT gives no year for the new private banks. The handout says 1993. NCERT’s “around 74 per cent” foreign limit is not in the handout; treat it as an extra fact from NCERT.']),
  dict(ref='XI Ch 5 §5.3 (Credit and Marketing in Rural Areas), Box 5.1, XI Ch 3 recap',
   why='The handout’s five phases are told from the bank’s side. NCERT tells the same story from the <b>village’s</b> side: moneylenders, social banking, NABARD, self-help groups, micro-credit and Jan Dhan. It is a good picture of why inclusion was needed.',
   link='Handout section 7: 1969 nationalisation, RRBs (1975), NABARD and DFIs (1980s), 1992 SHG-Bank Linkage, PMJDY (Aug 2014). NCERT’s pieces drop into those phases.',
   blocks=[
    dict(h='Step 1 · Why farmers need credit', pts=['Time between sowing and income is long, so farmers borrow for seeds, fertilisers, implements and family expenses (marriage, death, religious ceremonies).']),
    dict(h='Step 2 · The story in order (NCERT)', tbl=T(['When', 'What NCERT says'], [
         ['At independence', 'Moneylenders and traders exploited small and marginal farmers and landless labourers by lending at <b>high interest rates</b> and manipulating accounts to keep them in a <b>debt-trap</b>'],
         ['After 1969', 'India adopted <b>social banking</b> and a <b>multi-agency approach</b> to meet rural credit needs'],
         ['1982', '<b>NABARD</b> set up as an apex body to coordinate all institutions in rural financing'],
         ['Green Revolution', 'Diversified rural credit towards production-oriented lending'],
         ['Today', 'Multi-agency set: commercial banks, regional rural banks (RRBs), cooperatives and land development banks']])),
    dict(h='Step 3 · Self-Help Groups and micro-credit (NCERT)', pts=[
         'SHGs emerged to fill the gap because formal credit has been inadequate and not integrated with rural community life. Collateral is needed, so a vast share of poor rural households were automatically out of the credit network.',
         'Members make a <b>minimum contribution</b> (thrift). From the pooled money, credit goes to needy members, repayable in small instalments at reasonable interest.',
         'By May 2019 nearly <b>6 crore women</b> were members in <b>54 lakh</b> women SHGs. A revolving fund of about ₹10-15,000 per SHG and another ₹2.5 lakhs per SHG as Community Investment Support Fund help self-employment. Such credit is called <b>micro-credit programmes</b>.',
         'NCERT’s caution: it is alleged that the borrowings are mainly for consumption purposes.',
         'Box 5.1: Kudumbashree (Kerala) started a thrift and credit society in 1995 as a small savings bank for poor women; it mobilised Rs 1 crore as thrift savings and is acclaimed as among the “largest informal banks in Asia”.']),
    dict(h='Step 4 · Jan Dhan as NCERT describes it', tbl=T(['Feature', 'NCERT’s words'], [
         ['Who', 'All adults encouraged to open bank accounts'],
         ['Benefits', 'Accidental insurance cover of Rs 1-2 lakh and overdraft facility of Rs 10,000'],
         ['Transfers', 'Wages from government-related jobs and works under MNREGA, old age pension and other social security payments go to the account'],
         ['Balance', 'No need to keep a minimum bank balance'],
         ['Result', 'More than 50 crore people opened accounts; banks mobilised more than Rs 2,00,000 crores']])),
    dict(h='Step 5 · NCERT’s critical appraisal of rural banking', pts=[
         'Positive: rapid expansion of banking helped rural farm and non-farm output, income and employment, especially after the Green Revolution. Famines became events of the past.',
         'Negative: except commercial banks, other formal institutions failed to develop a culture of deposit mobilisation, lending to worthwhile borrowers and effective loan recovery. Agriculture loan default rates have been chronically high. Expansion of rural banking “has taken a backseat after reforms”.'])],
   d=['NCERT’s Jan Dhan result is “more than 50 crore” accounts; the handout gives “over 70% of adults and 99%+ of households banked”. Different measures; quote the handout’s percentages and NCERT’s count only if the question asks for accounts.',
      'NCERT does not date RRBs, the Lead Bank Scheme or the SHG-Bank Linkage Programme, and says NABARD was set up in 1982; the handout lists NABARD with DFIs of the 1980s (consistent). Learn the handout’s years.'])],
 '9': [dict(ref='XI Ch 5 §5.3 and §5.4 (institutions; cooperatives), Box 5.1, XI Glossary, XII Macro Ch 3',
   why='The handout’s table of bank types has co-operative banks, RRBs and DFIs. NCERT adds the rural set of institutions and a short verdict on cooperatives. The commercial-bank functions (accepting deposits, lending, the spread) are in the Chapter 8 NCERT boxes.',
   link='Handout section 9: commercial banks, co-operative banks, RRBs, DFIs. NCERT’s “multi-agency” set uses the same names and adds land development banks.',
   blocks=[
    dict(h='NCERT’s multi-agency set of rural institutions', tbl=T(['Institution (NCERT)', 'Where it is in the handout'], [
         ['Commercial banks', 'Section 9: regulated solely by RBI'], ['Regional rural banks (RRBs)', 'Section 9 and section 7: 1975, 50:15:35'],
         ['Cooperatives', 'Section 9: co-operative banks, dual regulation'], ['Land development banks', 'Not in the handout; NCERT only names them'],
         ['NABARD (apex body, 1982)', 'Section 7 and 9: DFI that refinances retail banks']])),
    dict(h='Cooperatives: NCERT’s verdict (marketing side)', pts=[
         'The success of milk cooperatives in Gujarat and some other parts of the country shows the role of cooperatives.',
         'Cooperatives have had a setback because of inadequate coverage of farmer members, lack of an appropriate link between marketing and processing cooperatives, and inefficient financial management.'])],
   d=['NCERT’s cooperative verdict is about marketing cooperatives; the handout’s co-operative banks are credit bodies with dual regulation (State Registrar and RBI). Do not mix the two.'])],
}

SRCFILES = ['keec103', 'keec105', 'keec1gl', 'leec1gl', 'leec101']
NCMAP = [('XI Ch 3 Financial Sector Reforms; XII Macro Ch 1: financial sector and who regulates it', '1', 'Names of institutions; RBI and SEBI as statutory bodies; glossary terms'),
         ('XI Ch 3 (RBI controls banks); XI and XII glossaries: CRR, SLR', '2', 'What RBI decides for banks; short CRR and SLR definitions'),
         ('XI Ch 5 §5.3 Rural Banking: critical appraisal', '5', 'Farm-loan default debate: wilful or economic'),
         ('XI Ch 3 Financial Sector Reforms: regulator to facilitator', '7', 'Private banks, 74 per cent, branch freedom, FIIs'),
         ('XI Ch 5 §5.3 Credit; Box 5.1; Jan Dhan', '7', 'Moneylenders to social banking; NABARD 1982; SHGs and micro-credit; Jan Dhan features'),
         ('XI Ch 5 §5.3 and §5.4: multi-agency set; cooperatives', '9', 'Land development banks; cooperative setbacks'),
         ('Not in NCERT: Basel III, CRAR, provisioning, SMA and NPA classes, 4R, AQR, SARFAESI, IBC, PSL targets, NBFC layers', '3, 4, 6, 8, 9', 'Learn these from the handout only'),
         ('XII Macro Ch 3: banks, money creation, CRR and SLR mechanics, lender of last resort', 'Chapter 8', 'Already in the Chapter 8 NCERT boxes')]
NCQ = [('Exercise 3 (XI Ch 3): Why did RBI have to change its role from controller to facilitator of financial sector in India?', 'Section 7 NCERT box, Step 1'),
       ('Exercise 4 (XI Ch 3): How is RBI controlling the commercial banks?', 'Section 2 NCERT box, Step 1 (and section 2 of the handout)'),
       ('Exercise 2 (XI Ch 5): Discuss the importance of credit in rural development.', 'Section 7 NCERT box on rural credit, Steps 1 and 2'),
       ('Exercise 3 (XI Ch 5): Explain the role of micro-credit in meeting credit requirements of the poor.', 'Section 7 NCERT box, Step 3'),
       ('Exercise 6 (XI Ch 5): Critically evaluate the role of the rural banking system in the process of rural development in India.', 'Section 7 NCERT box, Step 5 (and section 5 box)'),
       ('Exercise 7 (XII Macro Ch 3): Explain the functions of a commercial bank.', 'Chapter 8 NCERT box (§3.2.2); not in this handout chapter')]
NCKEY = ['Financial institutions', 'Merchant bankers', 'Foreign Institutional Investors (FIIs)', 'Cash Reserve Ratio (CRR)', 'Statutory Liquidity Ratio (SLR)', 'Reserve deposit ratio',
         'Social banking', 'Multi-agency approach', 'NABARD', 'Self-Help Group (SHG)', 'Micro-credit', 'Jan Dhan Yojana']
NCONLY = [('XII Macro Ch 3 §3.2 to §3.4: commercial banks, money creation, RBI tools', 'Covered by the Chapter 8 NCERT boxes; read the chapter there'),
          ('XII Macro Ch 3 Box 3.2: Demonetisation', 'Chapter 8; not a banking-regulation topic'),
          ('XI Ch 5 §5.4: Agricultural market system, MSP, buffer stocks', 'Agriculture chapter, not banking'),
          ('XI Ch 3: tax, trade, foreign exchange, disinvestment reforms', 'Reforms chapter; only the financial-sector part is used above'),
          ('XI Ch 2 (1950-1990): bank loans at lower interest for small units', 'One line on concessions to small industry; no banking structure'),
          ('XI Ch 4: Human capital formation', 'Education and health; no banking content')]
