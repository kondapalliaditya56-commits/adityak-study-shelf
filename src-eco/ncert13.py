# -*- coding: utf-8 -*-
"""NCERT content integrated into handout Ch 13 (NABARD, NBFCs, chit funds, Ponzi schemes). NCERT is thin here: most content is Class XI Ch 5 (Rural Development,
credit), plus Class XI Ch 3 (financial sector reforms), Class XII Macro Ch 3 (banks) and Class XI Ch 7 (Kyoto). Handout sections 6, 8, 10, 11 have no NCERT passage."""
SRC = 'NCERT'
def T(head, rows): return {'head': head, 'rows': rows}
NC = {
 '1': [dict(ref='Class XI Indian Economic Development, Ch 5 §5.3 (Credit)',
   why='The handout tells you how NABARD came to be. NCERT tells you <b>why rural India needed it</b>: who lent to farmers before, and how the system was reshaped.',
   link='Handout section 1: CRAFICARD, Act 61 of 1981, 12 July 1982; section 4: the list of rural credit institutions.',
   blocks=[
    dict(h='Step 1 · Why farmers need credit', pts=['The time between sowing and getting income after production (the gestation period) is long, so farmers borrow for seeds, fertilisers, implements and also for family expenses such as marriage, death and religious ceremonies. Growth of the rural economy depends on infusion of capital from time to time.']),
    dict(h='Step 2 · The story in order (NCERT)', tbl=T(['When', 'What happened'], [
         ['At independence', 'Moneylenders and traders exploited small and marginal farmers and landless labourers: high interest rates, manipulated accounts, a <b>debt-trap</b>'],
         ['After 1969', 'India adopted <b>social banking</b> and a <b>multi-agency approach</b> to meet the needs of rural credit'],
         ['1982', 'NABARD set up as an apex body to coordinate the activities of all institutions in the rural financing system'],
         ['Green Revolution', 'Led to a change in the credit system: rural credit shifted towards production-oriented lending']])),
    dict(h='Step 3 · Today’s structure (NCERT’s list)', pts=['Multi-agency institutions: commercial banks, regional rural banks (RRBs), cooperatives and land development banks. They are expected to dispense adequate credit at cheaper rates.'])],
   d=['NCERT does not mention CRAFICARD or the Act number. Take those from the handout.',
      'NCERT’s list says “land development banks”; the handout’s list names SCARDBs and PCARDBs. NCERT does not say they are the same, so learn both names and do not equate them unless a question does.'])],
 '2': [dict(ref='Class XI Indian Economic Development, Ch 5 §5.3 (SHGs, micro-credit), Box 5.1 Kudumbashree, Box 5.2 TANWA',
   why='The handout says the SHG Bank Linkage Project is the world’s largest microfinance project. NCERT explains <b>what an SHG is and why it exists</b>, in five small steps.',
   link='Handout section 2 (SHG Bank Linkage Project, 1992) and section 4 (women SHGs, Joint Liability Groups, microfinance).',
   blocks=[
    dict(h='Step 1 · The gap SHGs fill', pts=['The formal credit delivery mechanism proved inadequate and was not fully integrated into rural social and community development. Since some kind of <b>collateral</b> is required, a vast proportion of poor rural households were automatically out of the credit network.']),
    dict(h='Step 2 · How an SHG works', tbl=T(['Step', 'What happens'], [['1', 'Members promote thrift by a small minimum contribution from each member'], ['2', 'The contributions form a pooled sum'], ['3', 'From the pool, credit is given to needy members'], ['4', 'The loan is repaid in small instalments at reasonable interest rates']])),
    dict(h='Step 3 · The numbers NCERT gives', pts=['By May 2019 nearly 6 crore women in India had become members in 54 lakh women SHGs.',
         'In recent years about ₹10-15,000 per SHG and another ₹2.5 lakhs per SHG as a Community Investment Support Fund (CISF) are provided as part of a fund for self-employment and income generation. Such credit provisions are called <b>micro-credit programmes</b>.',
         'NCERT’s points: SHGs have helped the empowerment of women; it is alleged that the borrowings are mainly confined to consumption purposes.']),
    dict(h='Step 4 · Two examples', tbl=T(['Example', 'NCERT’s facts'], [
         ['Kudumbashree (Box 5.1, Kerala)', 'Women-oriented community-based poverty reduction programme. In 1995 a thrift and credit society was started as a small savings bank for poor women; it mobilised ₹1 crore as thrift savings. Acclaimed as the largest informal banks in Asia in terms of participation and savings mobilised'],
         ['TANWA (Box 5.2, Tamil Nadu)', 'Tamil Nadu Women in Agriculture: project of the late 1980s to train women in the latest agricultural techniques and organic farming. Farm Women’s Groups work like mini banks through a micro-credit system and use the savings for small household activities']]))],
   d=['NCERT prints the CISF as part of a “renovating fund”; from the context (money given to the SHG for lending on) this is probably a misprint for a revolving fund. Do not quote the phrase.',
      'Two different “largest” claims: the handout calls the SHG Bank Linkage Project the world’s largest microfinance project; NCERT calls the Kudumbashree societies the largest informal banks in Asia. Keep them apart in an answer.',
      'NCERT gives no year for the SHG Bank Linkage Project. Use the handout’s 1992.'])],
 '4': [dict(ref='Class XI Indian Economic Development, Ch 5 §5.3 (Rural Banking, a critical appraisal) and Ch 5 §5.4',
   why='The handout lists what NABARD supports. NCERT asks a harder question that often appears in Mains: <b>how well has rural banking worked?</b> Read it as a scorecard with one column for credit and one for cooperatives.',
   link='Handout section 4: more than 50% of rural credit is disbursed by cooperative banks and RRBs; financial inclusion.',
   blocks=[
    dict(h='Scorecard 1 · Rural banking', tbl=T(['What worked', 'What did not'], [[
         'Rapid expansion of the banking system raised rural farm and non-farm output, income and employment, especially after the Green Revolution. Farmers got services and credit; famines became events of the past; food security and buffer stocks followed',
         'With the possible exception of commercial banks, other formal institutions failed to develop a culture of deposit mobilisation, lending to worthwhile borrowers and effective loan recovery. Agriculture loan default rates have been chronically high. After the reforms, expansion of rural banking took a backseat']])),
    dict(h='Scorecard 2 · Cooperatives in marketing', pts=['The success of milk cooperatives in transforming Gujarat and some other parts of the country shows the role of cooperatives. In the Operation Flood system, farmers pool milk, which is graded, processed and marketed to urban centres through cooperatives, and they are assured of a fair price.',
         'But cooperatives have received a setback: inadequate coverage of farmer members, lack of a link between marketing and processing cooperatives, and inefficient financial management.']),
    dict(h='The fix NCERT names: Jan-Dhan Yojana (financial inclusion)', pts=['All adults are encouraged to open bank accounts. Holders can get ₹1-2 lakh accidental insurance cover and an overdraft facility of ₹10,000. Wages for government work (including the rural job guarantee), old age pension and other social security payments go straight to bank accounts, with no need to keep a minimum balance.',
         'More than 50 crore people opened accounts; banks mobilised more than ₹2,00,000 crores through them. NCERT says this indirectly promoted the thrift habit and efficient allocation of financial resources, particularly in rural areas.'])],
   d=['The handout says cooperative banks and RRBs give more than half of rural credit and NABARD supervises them; NCERT’s scorecard says formal institutions other than commercial banks have weak deposit mobilisation and recovery. Use the handout’s figure for facts and NCERT’s scorecard for the evaluation part of a Mains answer.'])],
 '5': [dict(ref='Class XI Indian Economic Development, Ch 7 Box 7.1 (Global Warming)',
   why='NCERT never mentions the climate funds of this section, but it gives the background that explains why they exist: the Kyoto agreement and the idea of fighting global warming.',
   link='Handout section 5: the Adaptation Fund is under the Kyoto Protocol of the UNFCCC.',
   blocks=[dict(h='What NCERT says', pts=['Global warming: a gradual increase in the average temperature of the earth’s lower atmosphere from the increase in greenhouse gases since the Industrial Revolution; much of it is human-induced (burning of fossil fuels, deforestation).',
         'A UN Conference on Climate Change, held in Kyoto, Japan, in 1997, resulted in an international agreement to fight global warming, which called for <b>reductions in emissions of greenhouse gases by industrialised nations</b>.',
         'Longer-term results listed by NCERT: melting of polar ice and rising sea level with coastal flooding; disrupted drinking water supplies; extinction of species; more frequent tropical storms; more tropical diseases.'])],
   d=['NCERT says nothing about the Adaptation Fund, the Green Climate Fund, NAFCC or NABARD’s role as an implementing entity. All of those are handout-only.'])],
 '7': [dict(ref='Class XI Indian Economic Development, Ch 3 §3.3 (Financial sector reforms) and Glossary',
   why='The handout shows who regulates which finance company. NCERT gives the big picture: RBI is the regulator of the whole financial sector, and the 1991 reforms changed its role.',
   link='Handout section 7: who regulates what; RBI as the regulator of deposit acceptance.',
   blocks=[
    dict(h='Step 1 · What the financial sector is (NCERT)', pts=['The financial sector includes financial institutions such as commercial banks, investment banks, stock exchange operations and the foreign exchange market. It is regulated by the Reserve Bank of India.',
         'Glossary: <b>financial institutions</b> engage in mobilisation and allocation of savings; they include commercial banks, cooperative banks, developmental banks and investment institutions.']),
    dict(h='Step 2 · RBI’s role before and after the reforms', tbl=T(['Before', 'After the reforms'], [['All banks and other financial institutions regulated through RBI norms; RBI decided the amount of money banks keep with themselves, fixed interest rates and the nature of lending to various sectors',
         'One major aim: to reduce the role of RBI from <b>regulator to facilitator</b> of the financial sector, so it may take decisions on many matters without consulting RBI. Private sector banks, Indian and foreign, were established; banks meeting conditions were free to open branches without RBI approval']]),
         pts=['Foreign Institutional Investors (FII), such as merchant bankers, mutual funds and pension funds, are now allowed to invest in Indian financial markets. Glossary: FIIs are banking and non-banking financial institutions of foreign origin. Certain managerial aspects were kept with RBI to safeguard account-holders and the nation.'])],
   d=['NCERT says RBI “fixes interest rates”. That is the pre-reform picture. The handout says RBI has deregulated interest on loans of financial institutions (except NBFC-MFIs), so loan rates depend on the loan agreement and must be disclosed. Handout wins for NBFC questions.',
      'NCERT mentions only that the sector is regulated by RBI. The split among SEBI, IRDA, NHB, the Ministry of Corporate Affairs and States is handout-only.'])],
 '9': [dict(ref='Class XII Macroeconomics, Ch 3 §3.2.2, §3.3 and Glossary',
   why='The handout says depositors place money on trust, so protection is supreme. NCERT shows <b>why</b>: a bank lends out most of what it holds and survives only while depositors are confident.',
   link='Handout section 9: “Why so restrictive”; DICGC cover for bank depositors; RBI as lender to banks.',
   blocks=[
    dict(h='Step 1 · A bank’s balancing act (NCERT)', pts=['A bank accepts deposits from the public and lends part of them. It keeps a portion to repay depositors whenever they demand their funds. The interest paid to depositors is lower than the interest charged to borrowers; the difference is the <b>spread</b>, the bank’s profit.',
         'Any bank would like to lend the maximum possible, but being able to repay depositors on demand is crucial to its survival. Depositors keep funds in a bank only if they are fully confident of getting them back on demand. So a bank must balance lending so that sufficient funds are available to repay any depositor.',
         'Banks can lend because they do not expect all depositors to withdraw at the same time.']),
    dict(h='Step 2 · The rule that limits lending (NCERT)', pts=['The RBI fixes a percentage of deposits which every bank must keep as reserves, so that no bank is “over lending”. This is a legal requirement: the Cash Reserve Ratio (CRR). Banks must also keep some reserves in liquid form in the short term: the Statutory Liquidity Ratio (SLR).']),
    dict(h='Step 3 · Lender of last resort (Glossary)', pts=['The function of the monetary authority in which it provides a guarantee of solvency to commercial banks in a situation of liquidity crisis or bank runs.'])],
   d=['NCERT says nothing about NBFCs, deposit insurance or why NBFCs are restricted. The comparison with NBFCs is handout-only.'])],
}

SRCFILES = ['keec105', 'keec103', 'keec107', 'keec1gl', 'leec103', 'leec1gl']
NCMAP = [('XI Ch 5 §5.3 Credit and marketing in rural areas', '1, 2, 4', 'Moneylenders, social banking after 1969, multi-agency structure, SHGs and micro-credit, Kudumbashree, Jan-Dhan'),
         ('XI Ch 5 §5.4 Agricultural market system (cooperative marketing)', '4', 'Milk cooperatives and their setback'),
         ('XI Ch 3 §3.3 Financial sector reforms', '7', 'RBI from regulator to facilitator; FIIs; financial institutions'),
         ('XII Macro Ch 3 §3.2.2-3.3 Commercial banks', '9', 'Spread, repay-on-demand rule, CRR and SLR, lender of last resort'),
         ('XI Ch 7 Box 7.1 Global warming', '5', 'Kyoto 1997 and the background to climate finance'),
         ('(No NCERT passage)', '3, 6, 8, 10, 11', 'Refinance and LTIF/PMAY-G detail, supervision, NBFC categories, chit funds, MLM and Ponzi schemes are handout-only')]
NCQ = [('Discuss the importance of credit in rural development.', 'Sections 1-4 + NCERT XI Ch 5 §5.3'),
       ('Explain the role of micro-credit in meeting the credit requirements of the poor.', 'Section 2/4 (SHG-BLP) + NCERT XI Ch 5 §5.3'),
       ('Critically evaluate the role of the rural banking system in rural development.', 'Section 4 + NCERT scorecard (§5.3)'),
       ('“Jan-Dhan-Yojna helps in rural development.” Do you agree?', 'NCERT XI Ch 5 §5.3 (not in the handout)'),
       ('Why did RBI have to change its role from controller to facilitator of the financial sector? How is RBI controlling commercial banks?', 'Section 7 + NCERT XI Ch 3 §3.3'),
       ('Explain the functions of a commercial bank.', 'Section 9 + NCERT XII Macro Ch 3 §3.2.2')]
NCKEY = ['Moneylenders (debt-trap)', 'Social banking', 'Multi-agency approach', 'NABARD (apex body)', 'Regional rural banks', 'Cooperatives', 'Land development banks', 'Self-Help Groups',
         'Micro-credit programmes', 'Community Investment Support Fund', 'Jan-Dhan Yojana', 'Financial institutions', 'Foreign Institutional Investors', 'Merchant bankers',
         'Spread', 'Cash Reserve Ratio (CRR)', 'Statutory Liquidity Ratio (SLR)', 'Lender of last resort']
NCONLY = [('Class XI Ch 5 §5.4 Agricultural marketing', 'regulated markets, infrastructure, MSP, buffer stocks, PDS, e-NAM, alternate channels: read from NCERT'),
          ('Class XI Ch 5 §5.5-5.6 Diversification and organic farming', 'allied activities, non-farm jobs, sustainable farming: not part of this handout chapter')]
