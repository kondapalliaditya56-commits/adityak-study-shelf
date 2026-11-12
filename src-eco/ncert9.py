# -*- coding: utf-8 -*-
"""NCERT content for handout Ch 9 (Capital Markets). NCERT is thin here: financial sector reforms, disinvestment,
glossary definitions, repo/OMO and the bond-price rule. Every number is as printed in NCERT or the handout."""
SRC = 'NCERT'
SRCFILES = ['keec103', 'keec1gl', 'leec103', 'leec101']
def T(head, rows): return {'head': head, 'rows': rows}
NC = {
 '1': [dict(ref='NCERT Class XI Indian Economic Development, Ch 3 (Financial Sector Reforms) and Glossary',
   why='The handout says the capital market is where demanders and suppliers decide for themselves. NCERT tells the same story from the side of the regulator: after 1991 the RBI was meant to step back from controller to helper, so that markets could decide more. Read the three small steps below.',
   link='Handout section 1: “in banking the bank decides; in capital markets the parties decide”. NCERT’s reform aim is the move from decision-making by the RBI towards decision-facilitating.',
   blocks=[
    dict(h='What the “financial sector” means in NCERT', pts=['Financial sector = financial institutions such as commercial banks, investment banks, stock exchange operations and the foreign exchange market. It is regulated by the RBI.',
         'Glossary: <b>Financial Institutions</b> = institutions that mobilise and allocate savings: commercial banks, cooperative banks, developmental banks and investment institutions.',
         'Before reforms the RBI decided the amount of money banks could keep with themselves, fixed interest rates and the nature of lending to sectors.']),
    dict(h='The reform aim and what changed', tbl=T(['Reform point (NCERT)', 'In plain words'], [
         ['RBI to move “from regulator to facilitator”', 'The financial sector may take many decisions without consulting the RBI'],
         ['Private sector banks, Indian and foreign, allowed', 'More players in banking'],
         ['Foreign investment limit in banks raised to around 74 per cent', 'Foreign money may own a large part of a bank'],
         ['Banks meeting conditions may open branches without RBI approval', 'Less permission-raj'],
         ['Foreign Institutional Investors (FII), such as merchant bankers, mutual funds and pension funds, allowed to invest in Indian financial markets', 'Foreign money into the stock market: the origin of today’s FPIs']])),
    dict(h='NCERT glossary words you will meet in this chapter', tbl=T(['Term', 'NCERT’s definition (short)'], [
         ['Stock Market', 'An institution where stocks and shares are traded'],
         ['Stock Exchange', 'A market in which the securities of governments and public companies are traded; it provides facilities for stock brokers to trade company stocks and other securities'],
         ['Merchant Bankers', 'Banks or financial institutions, also known as investment bankers, that specialise in advising companies and managing their equity and debt requirement through floatation and sale or purchase of stocks and bonds']]))],
   d=['NCERT’s Stock Exchange glossary says securities of “governments and public companies” are traded; the handout also stresses that the same exchanges (NSE, BSE) serve the primary market (IPOs) as well. Both are true; the handout adds the primary-market role.'])],
 '2': [dict(ref='NCERT Class XII Macroeconomics, Ch 3 (Open Market Operations; bank reserves)',
   why='The handout lists the instruments that the money market trades. NCERT adds two things the handout does not: how the RBI itself buys and sells government paper (OMO), and the repo, the money market’s everyday loan.',
   link='Handout section 2 (T-bills, CMBs, CP, CoD) and Chapter 8 (RBI’s tools). The repo and reverse repo are the RBI’s short-term lending and borrowing against government securities.',
   blocks=[
    dict(h='Step 1 · Open Market Operations (OMO)', pts=['OMO = buying and selling of bonds issued by the Government in the open market, entrusted to the central bank on behalf of the Government.',
         'RBI buys a bond and pays by cheque: reserves in the economy rise, so money supply rises. RBI sells a bond to private individuals or institutions: reserves fall, so money supply falls.']),
    dict(h='Step 2 · Two kinds of OMO', tbl=T(['Kind', 'What happens', 'Effect'], [
         ['Outright', 'RBI buys or sells the securities with no promise to reverse the deal later', 'Permanent injection or absorption of money'],
         ['Repo (repurchase agreement)', 'RBI buys a security and the agreement also fixes the date and price of resale', 'Money lent for a fixed time; the interest rate is the <b>repo rate</b>'],
         ['Reverse repo', 'RBI sells a security with a fixed date and price at which it will be repurchased', 'Money withdrawn for a fixed time; the rate is the <b>reverse repo rate</b>']]),
         pts=['RBI conducts repo and reverse repo operations at various maturities: overnight, 7-day, 14-day. NCERT calls these the main tool of monetary policy.']),
    dict(h='Step 3 · Treasury bills in NCERT’s bank-reserve story', pts=['NCERT says a bank’s reserves are deposits with the RBI plus its cash, “kept partly as cash and partly in the form of financial instruments (bonds and treasury bills) issued by the RBI”.'])],
   d=['NCERT says bonds and treasury bills are “issued by the RBI”. The handout says T-bills and CMBs are issued only by the Centre (the RBI runs the auction for it). Use the handout in class: only the Centre issues T-bills.',
      'NCERT’s repo and reverse repo pair is older wording; the Chapter 8 handout uses the corridor with the SDF as floor. Learn the handout corridor, recognise NCERT’s terms.'])],
 '4': [dict(ref='NCERT Class XI Indian Economic Development, Ch 3 (Privatisation, Disinvestment)',
   why='An OFS or a public sale of shares is also how the government sells part of a public company. NCERT calls this <b>disinvestment</b>. It explains why the handout’s warning “read who gets the money” matters for government sales as well.',
   link='Handout section 4: IPO, FPO, OFS. NCERT’s disinvestment is the government selling part of its equity to the public.',
   blocks=[
    dict(h='Step 1 · What disinvestment is', pts=['Privatisation of public sector enterprises by selling off part of their equity to the public is known as <b>disinvestment</b>.',
         'Glossary: disinvestment = a deliberate sale of a part of the capital stock of a company to raise resources and change the equity and/or management structure of a company.',
         'Two routes to privatisation: (i) withdrawal of the government from ownership and management of public sector companies, and/or (ii) outright sale of public sector companies.',
         'Purpose according to the government: to improve financial discipline and facilitate modernisation; private capital and managerial capabilities could improve the performance of PSUs.']),
    dict(h='Step 2 · The numbers NCERT gives', tbl=T(['Year', 'What happened'], [
         ['1991-92', 'Target: mobilise Rs 2500 crore; the government mobilised Rs 3,040 crore more than the target'],
         ['2022-23', 'Government mobilised about Rs. 46,000 crores']]),
         pts=['Every year the government fixes a target for disinvestment of PSEs.']),
    dict(h='Step 3 · The criticism NCERT records', pts=['Critics: assets of PSEs were undervalued and sold to the private sector, a substantial loss to the government.',
         'Proceeds were used to offset the shortage of government revenues, not for developing the PSEs or building social infrastructure.',
         'Navratnas, maharatnas and miniratnas: PSEs given special status and managerial autonomy (NCERT Box 3.1) to compete better.'])],
   d=['NCERT’s “strategic and minority sale” (its Exercise 6) is not explained in the text and is not in the handout; the handout only separates primary issue from OFS.'])],
 '5': [dict(ref='NCERT Class XII Macroeconomics, Ch 1 (macro players)',
   why='The handout names SEBI as the market regulator. NCERT’s one line puts it with the RBI as a macro decision maker whose goals are public goals, not private profit.',
   link='Handout section 5, exchanges and the regulator (SEBI); Chapter 7 puts the RBI as decision-maker and SEBI as decision-facilitator.',
   blocks=[
    dict(h='What NCERT says', pts=['Macroeconomic policies are pursued by the State itself or by statutory bodies like the Reserve Bank of India (RBI), the Securities and Exchange Board of India (SEBI) and similar institutions.',
         'Each such body has one or more public goals defined by law or the Constitution of India; they are not the goals of individuals maximising private profit or welfare.'])],
   d=[])],
 '10': [dict(ref='NCERT Class XI Glossary: FII, FDI',
   why='The handout’s P-Notes story is about FIIs. NCERT’s glossary gives the plain definitions of who an FII is and why “hot money” worries economists.',
   link='Handout section 10 (P-Notes and FIIs) and Chapter 10 section 4 (FDI versus FPI).',
   blocks=[
    dict(h='Definitions as printed in NCERT', tbl=T(['Term', 'NCERT’s words (short)'], [
         ['Foreign Institutional Investment', 'Foreign investments in the form of stocks, bonds or other financial assets; does not entail active management or control over the firms'],
         ['Foreign Institutional Investors (FIIs)', 'Banking and non-banking financial institutions of foreign origin, e.g. commercial banks, investment banks, mutual funds, pension funds, as distinct from domestic institutions'],
         ['Foreign Direct Investment', 'Investment of foreign assets into domestic structures, equipment and organisations; “does not include foreign investment into the stock markets”']]),
         pts=['NCERT’s hot money point: equity investments are potentially “hot money” that can leave at the first sign of trouble, whereas FDI is durable and useful whether things go well or badly.',
              'NCERT growth figure: foreign investment (FDI plus FII) rose from about US $100 million in 1990-91 to US $ 23 billion in 2022-23.'])],
   d=['NCERT uses the old term FII. The handout (Chapter 10) says SEBI merged FIIs into FPIs in 2014; the handout term wins.'])],
 'end': [dict(ref='NCERT Class XII Macroeconomics, Ch 3 (bonds, present value)',
   why='The September current affairs item on the global bond sell-off says “bond prices and yields move in opposite directions”. NCERT proves it with a small sum. Read it once and you never forget which way it goes.',
   link='Handout current affairs: global bond sell-off and rising sovereign yields. Same rule as Chapter 8 section 6 (bond price and interest rate).',
   blocks=[
    dict(h='NCERT’s bond: face value Rs 100, 2 years, coupon 10%', pts=['The bond pays Rs 10 after year 1 and Rs 10 plus the Rs 100 principal after year 2.',
         'Compare it with a savings account: what sum today would give you the same? That sum is the <b>present value (PV)</b>. Competitive bidding pushes the bond’s price to its PV.'],
         fm=[('Present value', '10 ÷ (1 + r) + 110 ÷ (1 + r)²', 'r = market interest rate as a fraction', 'wide')],
         tbl=T(['Market rate', 'Price of the bond (PV)'], [['5 per cent', '109.29 (approx.)'], ['6 per cent', '107.33 (approx.)']])),
    dict(h='The rule', pts=['Interest rate up, bond price down; interest rate down, bond price up. A falling bond price is a capital loss to the holder.'])],
   d=[])],
}
NCMAP = [('Class XI Ch 3: financial sector reforms, FII, glossary', '1, 5, 10', 'RBI from regulator to facilitator; FII allowed; stock market and exchange definitions'),
         ('Class XI Ch 3: privatisation and disinvestment', '4', 'Disinvestment, targets and criticism'),
         ('Class XII Ch 3: OMO, repo, reverse repo, reserves', '2', 'Outright versus repo operations; maturities'),
         ('Class XII Ch 3: bonds and present value', 'Current affairs', 'Why bond prices and yields move opposite'),
         ('Class XII Ch 1: macro decision makers', '5', 'RBI and SEBI as public-goal bodies')]
NCQ = [('Why did RBI have to change its role from controller to facilitator of the financial sector in India? (Class XI Ch 3, Q3)', 'NCERT box in section 1'),
       ('Distinguish between strategic and minority sale (Class XI Ch 3, Q6 i)', 'Not explained in NCERT text or the handout; see NCONLY'),
       ('Those PSUs which are making profits should be privatised. Do you agree? (Class XI Ch 3, Q9)', 'NCERT box in section 4 (disinvestment arguments)')]
NCKEY = ['Financial Institutions', 'Stock Market', 'Stock Exchange', 'Merchant Bankers', 'Foreign Institutional Investors (FIIs)', 'Foreign Direct Investment', 'Disinvestment',
         'Bonds', 'Present value', 'Open Market Operations', 'Repo and reverse repo']
NCONLY = [('Class XI Ch 3, strategic versus minority sale (Exercise 6)', 'Asked in the chapter’s exercises but not explained in the NCERT text; no home in this handout'),
          ('Class XI Ch 3, Navratna policy (Box 3.1)', 'Public enterprise status and autonomy; read it in NCERT, only touched in section 4 here')]
