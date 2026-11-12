# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 13 (NABARD, NBFCs, Chit Funds and Ponzi Schemes). Facts come only from the handout text.
plain = idea in everyday words (memory aid); eg = the handout's own example; hook = one-line handle."""
TOP = {
 'sixty': [('NABARD', 'rural development bank: CRAFICARD 1979, Act 61 of 1981, born 12 July 1982; now fully owned by the Government'),
           ('Three heads', 'financial (refinance, RIDF, LTIF), developmental (cooperatives, SHGs, RSETIs), supervision (StCBs, DCCBs, RRBs)'),
           ('Climate', 'National Implementing Entity for the Adaptation Fund (July 2012) and for NAFCC; own Climate Change Fund'),
           ('NBFC', 'lends like a bank but takes no demand deposits, issues no cheques, has no DICGC cover'),
           ('Regulators', 'RBI for NBFCs; SEBI, IRDA, NHB, MCA and State Governments for the exempt ones'),
           ('Frauds', 'chit funds: States; MLM and Ponzi: banned by the 1978 Act; CIS: SEBI')],
 'words': [('Refinance', 'NABARD’s money to banks and other institutions so that they can lend onward'),
           ('Net Owned Funds (NOF)', 'the owner’s own money in an NBFC; ₹2 crore is the minimum since April 1999'),
           ('Certificate of Registration (CoR)', 'RBI’s licence without which an NBFC may not do business'),
           ('Systemically important NBFC', 'an NBFC big enough (₹500 crore of assets) to matter for the stability of the economy'),
           ('DICGC cover', 'insurance on bank deposits if the bank fails; NBFC depositors do not get it'),
           ('Chit fund', 'a group in which everyone pays a sum each period and one member takes the whole pot in turn'),
           ('Pyramid / MLM', 'income comes from enrolling more members who pay fees, not from selling a product'),
           ('Ponzi scheme', 'one depositor’s money is paid out as another’s return, with no asset created')],
}
SEC = {
 '1': dict(
   plain='Picture rural credit before 1982 as many small taps run by different bodies. The Government asked RBI to review the arrangements, and the Sivaraman committee said rural credit needed one institution giving it “undivided attention”. Parliament passed an Act, and the new bank took over RBI’s farm-credit work and the refinance work of an older corporation. Today the Government owns it fully.',
   eg='The handout’s dates: CRAFICARD constituted 30 March 1979 (chair B. Sivaraman); interim report 28 November 1979; Act 61 of 1981; NABARD comes into existence 12 July 1982 by transferring RBI’s agricultural credit functions and the refinance functions of ARDC.',
   hook='Committee 1979 → Act 61 of 1981 → NABARD 12 July 1982. Now fully owned by the Government of India.',
   mn=[dict(kind='sentence', title='The four dates, in order', sentence='Credit Always Needs Support',
            letters=[('C', 'CRAFICARD, 30 March 1979'), ('A', 'Act 61 of 1981'), ('N', 'NABARD born, 12 July 1982'), ('S', 'SHG Bank Linkage Project, 1992')],
            note='Own memory aid (not from the handout): the sentence is about rural credit, the reason NABARD exists.')]),
 '2': dict(
   plain='NABARD wears three hats. As financier it supplies money (refinance and rural infrastructure) and guides district credit plans. As developer it designs and runs schemes and trains artisans. As supervisor it watches cooperative banks and Regional Rural Banks and helps them adopt sound practice and core banking.',
   eg='The handout’s claims: the SHG Bank Linkage Project (1992) “has blossomed into the world’s largest microfinance project”; the Kisan Credit Card was designed by NABARD; it has financed one-fifth of India’s rural infrastructure and pioneered watershed development as climate proofing.',
   hook='Financial, Developmental, Supervision. SHG Bank Linkage 1992; KCC designed by NABARD.'),
 '3': dict(
   plain='Money flows in two ways. Direct finance goes to the borrowing body itself (food parks, cold chains, marketing federations, cooperative banks, Producer Organisations). Indirect finance goes through funds or schemes (Alternative Investment Funds, the Long Term Irrigation Fund, PMAY-G). Refinance is NABARD lending to banks and institutions that then lend to farmers and others; the type depends on the purpose and the time.',
   eg='PMAY-G: one crore houses over 3 years needed ₹81,975 crore: ₹60,000 crore from the budget and ₹21,975 crore borrowed from NABARD. LTIF: set up in 2016 with ₹20,000 crore; priorities: 23 projects by 2016-17, 31 by 2017-18, the balance 45 by 2019-20.',
   hook='Direct vs indirect. Refinance: off-farm, short-term, long-term (up to 15 years). LTIF 2016, ₹20,000 crore. These figures are history.'),
 '4': dict(
   plain='More than half of rural credit goes out through cooperative banks and RRBs, so NABARD’s developmental job is to strengthen them: the whole ladder from the village society to the state apex bank. It also runs farm-sector and off-farm departments, promotes women’s SHGs and Joint Liability Groups, and backs rural training institutes.',
   eg='The handout’s ladder under Institutional Development: Rural Credit Cooperatives; State Cooperative Banks (StCBs); Central Cooperative Banks (CCBs); Primary Agricultural Credit Societies (PACS); SCARDBs; PCARDBs. Training: RUDSETI and RSETIs for rural youth and women.',
   hook='More than 50% of rural credit: cooperative banks + RRBs. NABARD builds them (ID); SHG-BLP; RSETIs train.'),
 '5': dict(
   plain='Climate money has four pots. Two are international (Adaptation Fund and Green Climate Fund) and two are Indian (NAFCC and NABARD’s own Climate Change Fund). NABARD is the national channel: it is the accredited National Implementing Entity, which means it carries full responsibility for managing, financing, monitoring and reporting the projects, while the Environment Ministry is the National Designated Authority that endorses proposals.',
   eg='The handout’s facts: Adaptation Fund under the Kyoto Protocol, established 2001, launched 2007 at Marrakech, funded partly by 2% of CER proceeds, HQ Washington. Green Climate Fund: decision at COP 16 Cancun (December 2010), operational at COP 17 Durban (2011), HQ Songdo. NAFCC: August 2015, ₹350 crore for 2015-16 and 2016-17.',
   hook='NIE for the Adaptation Fund July 2012 (only NIE for India) and for NAFCC. NDA = MoEFCC. Climate Change Fund from 2016-17 profit.'),
 '6': dict(
   plain='Supervision means inspection to protect depositors. The law gives NABARD the power to inspect StCBs, DCCBs and RRBs, and it inspects voluntarily the state-level institutions such as SCARDBs, apex weavers societies and marketing federations. The five objectives run from protecting depositors to making institutions strong enough to lend more efficiently.',
   eg='The handout: Section 35(6) of the Banking Regulation Act, 1949 empowers NABARD to inspect State Cooperative Banks, Central Cooperative Banks (DCCBs) and Regional Rural Banks.',
   hook='Sec 35(6) BR Act 1949: StCBs, DCCBs, RRBs. Voluntary: SCARDBs, apex weavers, marketing federations.'),
 '7': dict(
   plain='An NBFC looks like a bank because it lends and invests, but it lacks three banking features: it cannot take demand deposits, it is not part of the payment system so it cannot issue cheques on itself, and its depositors have no deposit insurance. NBFCs must hold an RBI registration certificate and a minimum of owned funds. Some finance companies are exempt from RBI registration because another regulator already watches them.',
   eg='The handout’s regulator table: Housing Finance Companies - National Housing Bank; merchant bankers, VCFs, stock exchanges, brokers - SEBI; insurance companies - IRDA; chit funds - State Governments; Nidhi companies - Ministry of Corporate Affairs; deposit acceptance - RBI.',
   hook='NBFC vs bank: no demand deposits, no cheques, no DICGC. Systemically important: ₹500 crore. NOF ₹2 crore since April 1999 (was ₹25 lakh).'),
 '8': dict(
   plain='An NBFC’s label tells you what it does and which rule it follows. Asset Finance Companies finance machines like tractors. Investment Companies hold securities. Infrastructure Finance Companies must put most of their assets into infrastructure loans. Microfinance, factoring and mortgage-guarantee companies each have a percentage test. NOFHC is the holding vehicle through which a promoter group sets up a new bank.',
   eg='The handout’s tests: IFC at least 75% of assets in infrastructure loans, minimum NOF ₹300 crore, rating A, CRAR 15%; NBFC-MFI at least 85% in qualifying assets; Factors at least 50% of assets and 50% of income; MGC at least 90% of turnover or income, NOF ₹100 crore.',
   hook='AFC: physical assets. IC: securities. IFC 75%. MFI 85%. Factors 50/50. MGC 90%. NOFHC: holding vehicle for a new bank.'),
 '9': dict(
   plain='RBI wants only banks to take public deposits, because depositors put money on trust and expect it back, unlike an investor who shares the risk. So since 1997 no new deposit-taking registration has been issued to NBFCs, and the old ones are tightly boxed in: rated, capped, fixed terms. Residuary NBFCs, whose main business is deposits, must keep the whole deposit liability in very safe, liquid instruments.',
   eg='The handout’s terms: maximum interest 12.5%; minimum 12 months, maximum 60 months; no deposits repayable on demand; deposit limit 1.5 times NOF. Banks’ depositors: DICGC pays insurance on deposits up to ₹1 lakh if a bank fails (handout figure, may be dated).',
   hook='Since 1997 no new deposit CoR. Deposits: rated, ≤ 1.5 × NOF, 12-60 months, ≤ 12.5%, none on demand.'),
 '10': dict(
   plain='A chit fund is a savings circle written into law. Members pay in every period; each period the pot goes to one member chosen by bid, lot, auction or tender; everyone gets a turn before the next round. The Central Act is run by State Governments, so there is no single national rulebook. RBI’s only hook is that chit funds may not accept public deposits. A chit subscription is not a deposit.',
   eg='The handout’s name rule: a company whose main business is a chit fund must carry “Chit Fund” in its name (Rule 8(2)(b)(iii), Companies (Incorporation) Rules, 2014). Fraud by a chit company is an offence under the Prize Chits and Money Circulation Schemes (Banning) Act, 1978.',
   hook='Chit Funds Act 1982: Central Act, State administration. RBI deposit ban from August 2009. Cheating: 1978 Act.',
   mn=[dict(kind='sentence', title='The legal milestones in order (1978, 1982, 1997, 1999, 2009)', sentence='Protect Chit Savers, Never Betray',
            letters=[('P', 'Prize Chits and Money Circulation Schemes (Banning) Act, 1978'), ('C', 'Chit Funds Act, 1982'), ('S', 'Stop: no new deposit CoR to NBFCs, 1997'),
                     ('N', 'NOF raised from ₹25 lakh to ₹2 crore, April 1999'), ('B', 'Ban: chit funds barred from deposits, August 2009')],
            note='Own memory aid (not from the handout): the order follows the years; the sentence is about protecting small savers.')]),
 '11': dict(
   plain='Three kinds of money-collecting scheme, three owners. Collective Investment Schemes (money for units such as time-share or plots) belong to SEBI. Multi-level marketing and direct selling belong to the State Government. Money circulation, pyramid and Ponzi schemes are banned outright by the 1978 Act, and States deal with them. A pyramid pays from new members’ fees; a Ponzi pays old investors from new investors’ money, so both collapse when new money stops.',
   eg='The handout’s Ponzi picture: high-return promises, no asset creation, one depositor’s money is paid as another’s return, the scheme cannot return even the principal and the perpetrators disappear. In a pyramid, the lowest members suffer most.',
   hook='CIS → SEBI. MLM and direct selling → State. Pyramid and Ponzi → banned by the 1978 Act, States enforce.'),
}
NUMBERS = [('30 Mar 1979', 'CRAFICARD (B. Sivaraman) constituted'), ('Act 61 of 1981', 'NABARD Act'), ('12 July 1982', 'NABARD comes into existence'), ('1992', 'SHG Bank Linkage Project'),
           ('₹20,000 crore', 'LTIF corpus, 2016'), ('₹81,975 crore', 'PMAY-G need = ₹60,000 crore budget + ₹21,975 crore NABARD'), ('July 2012', 'NABARD accredited NIE for the Adaptation Fund'),
           ('₹500 crore', 'systemically important NBFC'), ('₹25 lakh → ₹2 crore', 'NOF, April 1999'), ('1997', 'no new deposit CoR to NBFCs'), ('1.5 × NOF', 'deposit limit of a deposit-accepting NBFC'),
           ('12.5%, 12-60 months', 'maximum interest and deposit term'), ('75 / 85 / 90%', 'IFC / MFI / MGC asset or income tests'), ('₹1 lakh', 'DICGC cover (handout figure)'),
           ('1978 / 1982', 'Prize Chits Act / Chit Funds Act'), ('August 2009', 'RBI bars chit funds from deposits')]
DRAW = ['Redraw the handout’s flow “How NABARD came to be” (section 1) with the three dates.',
        'Redraw the handout’s fork “Bank or NBFC?” (section 7) and write the three differences under it.',
        'Redraw the handout’s fork “Who handles which money-collecting scheme?” (section 11): CIS, MLM, Ponzi and their owners.']
FM = {
 '3': [('PMAY-G funding', '₹81,975 crore = ₹60,000 crore (budget) + ₹21,975 crore (NABARD borrowings)', 'one crore houses, 2016-17 to 2018-19'),
       ('Long-term refinance', 'loan period up to a maximum of 15 years', 'investment credit that creates assets and capital formation')],
 '5': [('Adaptation Fund money', 'government and private donors + 2% of CER proceeds under the CDM', 'Adaptation Fund Board: 16 members, 16 alternates')],
 '7': [('Systemically important NBFC', 'asset size ≥ ₹500 crore', 'last audited balance sheet'),
       ('Registration', 'Certificate of Registration + NOF ₹2 crore (earlier ₹25 lakh)', 'Section 45-IA of the RBI Act, 1934; ₹2 crore since April 1999'),
       ('NBFC vs bank', 'no demand deposits, no cheques on itself, no DICGC cover', 'the three differences')],
 '8': [('IFC', '≥ 75% of assets in infrastructure loans; NOF ≥ ₹300 crore; rating “A”; CRAR 15%', ''),
       ('NBFC-MFI', '≥ 85% of assets in qualifying assets', 'non-deposit taking'),
       ('NBFC-Factors', 'factoring assets ≥ 50% of total assets and income ≥ 50% of gross income', 'non-deposit taking'),
       ('MGC', '≥ 90% of turnover or gross income from mortgage guarantee; NOF ₹100 crore', '')],
 '9': [('Deposit limit', 'deposits ≤ 1.5 × NOF', 'only NBFCs with a specific authorisation and an investment-grade rating'),
       ('Deposit terms', '12 months ≤ term ≤ 60 months; interest ≤ 12.5%; none repayable on demand', 'handout'),
       ('RNBC safety', '100% of deposit liability in highly liquid, secure instruments', 'G-secs, FDs with scheduled banks, CoDs, mutual fund units')],
}
