# -*- coding: utf-8 -*-
"""NCERT Class XII Introductory Macroeconomics Ch 3 (Money and Banking) integrated into handout Ch 8, by section.
Each box: why (plain words) + link (to handout notation) + blocks (h, pts, tbl, fm, fig, ex) + d (NCERT differs).
Only NCERT-only points or differences. Every number is as printed in NCERT."""
SRC = 'NCERT Class XII Macroeconomics, Ch 3'
def T(head, rows): return {'head': head, 'rows': rows}
NC = {
 '1': [dict(ref='§3.1 Functions of money',
   why='The handout told you what makes something money. NCERT tells you what money <b>does</b>: three jobs. Read this box first; the handout then reads faster.',
   link='Handout “Denomination of values” = unit of account; “Preservation of value” = store of value; money as medium of exchange = GA-MOE.',
   blocks=[
    dict(h='When is money needed at all?', pts=['One person alone, or a family on an isolated island that does not trade, has no use for money. Money matters once two or more people trade through the market.',
         'Without money (barter) you need a <b>double coincidence of wants</b>. Example: a person with surplus rice wants clothing; she must find someone with surplus clothing who wants rice. Search costs “may become prohibitive” as the crowd grows. So an intermediate good acceptable to both sides is needed: money.']),
    dict(h='The three functions, each with NCERT’s own example', tbl=T(['Function', 'What it means', 'NCERT’s example'], [
         ['<b>Medium of exchange</b> (principal role)', 'Sell for money, buy with money; no double coincidence needed', 'Sell rice for money, then buy cloth with it'],
         ['<b>Unit of account</b>', 'All values expressed in one unit, so relative prices are easy to compute', 'Watch = ₹500; pencil ₹2, pen ₹10, so a pen = 10 ÷ 2 = 5 pencils'],
         ['<b>Store of value</b>', 'Wealth carried forward to a future date', 'Rice is perishable and bulky; money is not perishable, cheap to store, accepted by anyone. Needs a stable price level; a rising price level erodes it']])),
    dict(h='Purchasing power: the value of money itself', fm=[('Value of ₹1 in terms of a good', '1 ÷ price of the good', 'pencil ₹2 → ₹1 = 0.5 pencil; pen ₹10 → ₹1 = 0.1 pen')],
         pts=['If the price level rises, one rupee buys less of every commodity: the <b>purchasing power</b> of money has deteriorated.',
              'Other assets (gold, land, houses, bonds) also store value, but they are not easily convertible and lack universal acceptability.']),
    dict(h='Cashless society (NCERT’s current-issue note)', pts=['Transactions by transfer of digital information, not physical notes and coins.',
         'India’s push for financial inclusion: Jan Dhan accounts, Aadhaar-enabled payment systems, e-wallets, National Financial Switch (NFS); mobile and smartphone spread makes inclusion “a realistic dream”.'])],
   d=[])],
 '2': [dict(ref='§3.2.2 and Measures of money supply',
   why='Why do we accept a ₹100 note when the paper is worth almost nothing? NCERT’s answer is the same as the handout’s: trust in the issuer. It also adds a clean test for what is and is not legal tender.',
   link='Handout: “modern money is a promise issued by the central bank”; legal tender = a creditor cannot lawfully refuse it.',
   blocks=[
    dict(h='Where a note gets its value', pts=['The paper in a ₹100 note, or the metal in a ₹5 coin, is worth far less than its face value. Value comes from the <b>guarantee of the issuing authority</b>.',
         'Every note carries the Governor’s promise: the RBI will be responsible for giving purchasing power equal to the value printed.']),
    dict(h='Fiat money and legal tender: the test', tbl=T(['Item', 'Fiat money?', 'Legal tender? (cannot be refused)'], [
         ['Currency notes (issued by the RBI)', 'Yes', 'Yes'], ['Coins (issued by the Government of India)', 'Yes', 'Yes'],
         ['Cheque on a savings or current account (demand deposit)', 'No (it is a bank liability)', '<b>No</b>: anyone may refuse a cheque']]),
         pts=['Fiat = no intrinsic value (unlike a gold or silver coin). Legal tender = no citizen can refuse it to settle any transaction.']),
   ],
   d=['NCERT’s legal tender covers notes and coins only. The handout adds CBDC. Use the handout list (notes, coins, CBDC) in the exam.'])],
 '3': [dict(ref='§3.2.2 Central bank',
   why='Before the RBI’s balance sheet, know what the RBI does for a living. NCERT lists the jobs; the handout then explains the money-making side of one of them (issuing currency).',
   link='The currency the RBI issues is its liability (handout, “zero-cost liabilities”); NCERT calls this base “high-powered money”.',
   blocks=[
    dict(h='NCERT’s list of central bank functions (India: RBI, set up 1935)', tbl=T(['#', 'Function', 'In one line'], [
         ['1', 'Issues the currency', 'Notes held by the public or by commercial banks'], ['2', 'Controls money supply', 'Bank rate, open market operations, variations in reserve ratios'],
         ['3', 'Banker to the government', ''], ['4', 'Custodian of foreign-exchange reserves', ''], ['5', 'Bank to the banking system', 'Including <b>lender of last resort</b> (section 8)']])),
    dict(h='High-powered money, three names', pts=['Currency issued by the central bank (held by the public or banks) = <b>high-powered money</b> = <b>reserve money</b> = <b>monetary base</b>, because it is the basis for credit creation.',
         'From the money-supply point of view, the function to focus on is the issue of currency. RBI is “the only institution which can issue currency”.'])],
   d=[])],
 '4': [dict(ref='Measures of money supply (end of chapter) and Appendix 3.2, 3.3',
   why='M1 to M4 is a ladder: start at money you can spend instantly and keep widening the net. NCERT gives its own version of each rung; the handout’s ladder wins in class, so read NCERT’s version only to recognise it if a question quotes it.',
   link='Handout formulas are in the card above. Money supply (MS) is a <b>stock</b>: how much the public holds at one moment.',
   blocks=[
    dict(h='NCERT’s legal definitions (use for recognition)', fm=[('M1 (narrow)', 'CU + DD', ''), ('M2 (narrow)', 'M1 + savings deposits with Post Office savings banks', ''),
         ('M3 (broad)', 'M1 + net time deposits of commercial banks', 'most commonly used; “aggregate monetary resources”'), ('M4 (broad)', 'M3 + total deposits with Post Office savings organisations (excl. NSC)', '')],
         pts=['CU = currency (notes plus coins) held by the public. DD = net demand deposits held by commercial banks.',
              '“Net” means only the public’s deposits count. Interbank deposits (one bank’s deposit in another) are <b>not</b> part of money supply.',
              'Demand deposits (savings, current) are payable on demand; time deposits (e.g. fixed deposits) have a fixed maturity.',
              'M1, M2 = narrow money. M3, M4 = broad money. Decreasing order of liquidity: M1 most liquid, M4 least.']),
    dict(h='What the data show (Appendix 3.2, RBI Handbook 2024-25), in ₹ crore', tbl=T(['Year', 'M1 (narrow)', 'M3 (broad)', 'M3 − M1 = time deposits (worked out here)'], [
         ['1999-00', '3,41,796', '11,24,174', '7,82,378'], ['2009-10', '14,89,268', '56,02,698', '41,13,430'], ['2019-20', '41,25,948', '1,67,99,963', '1,26,74,015'], ['2024-25', '65,84,081', '2,72,86,589', '2,07,02,508']]),
         pts=['NCERT’s note: the difference between the two columns is the time deposits held by commercial banks. Broad money has grown much faster than narrow money.']),
    dict(h='What the base (M0) is made of: Appendix 3.3, 2023-24, ₹ crore', tbl=T(['Component', '₹ crore'], [
         ['Currency in circulation', '35,11,461'], ['− Cash with banks', '1,01,185'], ['= Currency with the public', '34,10,276'], ['+ Other deposits with RBI', '94,536'], ['+ Bankers’ deposit with the RBI', '10,25,449']]),
         pts=['Reading the table: currency with the public = currency in circulation minus cash that banks themselves hold. NCERT’s 2024-25 row does not add up as printed (3,724,448 − 9,396 ≠ 3,630,751), so use the 2023-24 row.'])],
   d=['NCERT M1 = CU + DD only. The handout’s M1 also includes “Other” deposits with RBI. Handout wins for class.',
      'NCERT M2 adds “savings deposits with Post Office savings banks”; the handout says post-office demand deposits. NCERT M4 adds total post-office deposits; the handout lists DD, TD and other. Learn the handout ladder.'])],
 '5': [dict(ref='§3.2.2 and §3.3 Banks and money creation',
   why='This is the one chapter section where the teacher said “read NCERT”. The idea: a bank lends out most of what you deposit, the borrower deposits it again, and the chain multiplies money. NCERT shows it with a story, a balance sheet and a table. Read in this order: bank job → Lala’s story → balance sheet → the table → the formula.',
   link='NCERT assumes no cash is kept by the public (M1 = 0 + deposits), so only the reserve ratio matters. That is the handout’s m ∝ 1/rdr case (cdr = 0).',
   blocks=[
    dict(h='1 · What a commercial bank does (NCERT Q7)', pts=['Accepts deposits from the public; lends part of the funds to those who want to borrow (home loans, crop loans).',
         'Earns the <b>spread</b>: interest paid to depositors is lower than interest charged to borrowers.',
         'Depositors come for interest and safety; a demand deposit with cheques and debit cards makes big payments convenient.',
         'Survival rule: a bank must lend as much as it can for profit, but keep enough to repay any depositor on demand. Depositors stay only if fully confident of getting money back.']),
    dict(h='2 · Lala the goldsmith: money out of thin air', tbl=T(['Step', 'What happens', 'Receipts (money) outstanding'], [
         ['1', 'Villagers keep 100 kg of gold with Lala and get paper receipts; receipts start circulating as money', '100 kg'],
         ['2', 'Ramu asks for a loan of 25 kg. Lala bets not everyone will withdraw at once, and lends', '100 kg (+25 kg lent)'],
         ['3', 'Ramu pays Ali with the 25 kg; Ali deposits it with Lala for a receipt', '<b>125 kg</b>']]),
         pts=['Lala has “created money out of thin air”. A modern bank works the same way: <b>when a bank lends, a new deposit is opened in the borrower’s name</b>, so money supply rises by the new deposit.']),
    dict(h='3 · The bank’s balance sheet', fm=[('Assets', 'Reserves + Loans', 'Reserves = deposits with RBI + the bank’s cash'), ('Liabilities', 'Deposits', 'what the bank owes to depositors'), ('Net worth', 'Assets − Liabilities', 'both sides must balance')],
         tbl=T(['Table 3.1 (start)', 'Assets', 'Liabilities'], [['', 'Reserves ₹100', 'Deposits ₹100'], ['', 'Net worth ₹0 (balance)', ''], ['Total', '₹100', '₹100']])),
    dict(h='4 · CRR and SLR in NCERT’s words', pts=['<b>CRR</b>: the percentage of deposits a bank must keep as cash reserves. Fixed by the RBI so that no bank is “over lending”; legally binding.',
         '<b>SLR</b>: apart from CRR, banks must keep some reserves in liquid form in the short term.',
         'At CRR 20%, deposits of ₹100 force the bank to keep ₹20 and lend only ₹80: the reserve requirement is the limit to credit creation.']),
    dict(h='5 · The multiplier, round by round (CRR = 20%, one bank, no cash with the public)', tbl=T(['Round', 'Deposits at start', 'Required reserve (20%)', 'Loan made'], [
         ['1', '100', '20', '80'], ['2', '180 (100 + 80 re-deposited)', '36', '64'], ['3, 4, …', 'keeps rising', 'keeps rising', 'keeps shrinking'], ['Last', '<b>500</b>', '<b>100</b>', '<b>400</b>']]),
         pts=['Why 180 in round 2: the ₹80 loan comes back as a deposit (100 + 80). Reserve needed is 20% of 180 = ₹36, so the bank can lend ₹64 (the original ₹100 of cash minus ₹36).',
              'The chain stops when required reserves reach ₹100, the cash the bank actually has: that is at deposits of ₹500 (20% of 500 = 100).',
              'Final balance sheet (Table 3.3): Reserves ₹100; Loans ₹400 | Deposits ₹500. M1 = 0 + 500 = ₹500, up from ₹100.'],
         fm=[('Money multiplier', '1 ÷ CRR', 'NCERT: 1 ÷ 20% = 1 ÷ 0.2 = 5 (arithmetic)'), ('Deposits created', 'multiplier × reserves', '5 × ₹100 = ₹500')]),
    dict(h='Sum of the chain (NCERT Appendix 3.1)', fm=[('Infinite geometric series', 'S = a ÷ (1 − r)', 'for 0 &lt; r &lt; 1; derived by S − rS = a')], pts=[])],
   d=['NCERT says reserves are kept partly as cash and partly in bonds and treasury bills issued by the RBI. The handout keeps CRR as cash with the RBI and SLR as gold and G-secs. Handout wins.',
      'NCERT Appendix 3.1 proves S = a ÷ (1 − r), but its printed numbers (r = 0.4, answer 5/3) do not match the chapter’s 20% case (multiplier 5). Use 5 for the example; take only the formula from the appendix.'])],
 '6': [dict(ref='§3.2.1 and Box 3.1 Demand for money',
   why='Why does anyone hold money when a bank pays interest? Two reasons: you need cash to spend (transaction), and you may wait in cash when you fear bonds will lose value (speculative). Read the four small steps below in order: each has a tiny story and one formula.',
   link='Handout MDT ∝ P·Q ÷ v is NCERT’s MDT = k·P·Y with v = 1/k (same thing). Handout MDS ∝ 1/r is NCERT’s MDS formula below. NCERT counts two motives; the handout folds “precautionary” into transaction.',
   blocks=[
    dict(h='Step 1 · Liquidity preference and its price', pts=['Demand for money balances = <b>liquidity preference</b>. Money is the most liquid asset: universally acceptable, easy to swap for goods.',
         'But money has an <b>opportunity cost</b>: the interest you could earn (say, in a fixed deposit). You trade liquidity against forgone interest.',
         'Plain rule (§3.2.1): higher income → more transactions → more money demanded. Higher interest rate → people hold less money → money demand falls.']),
    dict(h='Step 2 · Transaction demand: the salary story', tbl=T(['', 'Day 1 of month', 'Last day', 'Average balance'], [
         ['Worker (earns ₹100, spends evenly)', '₹100', '₹0', '(100 + 0) ÷ 2 = <b>₹50</b>'], ['Firm (receives ₹100 back)', '₹0', '₹100', '₹50']]),
         pts=['One person: average cash held = half the monthly income; transactions made = ₹100. Two-person economy: money used = ₹100 but transactions = ₹200 (firm sells ₹100 of output; worker sells ₹100 of services).',
              'Each rupee changes hands <b>twice</b>: the number of times a unit of money changes hands in a period is the <b>velocity of circulation</b>.',
              'MDT is a <b>stock</b> (money people wish to hold); T is a <b>flow</b>; v has the time dimension.'],
         fm=[('Transaction demand', 'MD<sub>T</sub> = k · T', 'T = nominal value of transactions; k a positive fraction'), ('Velocity', 'v = 1 ÷ k', 'example: k = ½, v = 2'),
             ('Velocity form', 'v · MD<sub>T</sub> = T', 'money × turns = transactions'), ('Link to GDP', 'MD<sub>T</sub> = k · P · Y', 'P = price level (GDP deflator); Y = real GDP')]),
    dict(h='Step 3 · Bond price story: why interest rate and bond price move opposite', pts=['“Bond” = any paper promising future money, issued by governments or firms. Example bond: face value ₹100, 2 years, coupon 10% (pays ₹10 after year 1, ₹10 + ₹100 after year 2).',
         'Compare with a savings account at 5%: how much money in the bank gives ₹10 after one year, and ₹110 after two? Add the two = <b>present value (PV)</b>.'],
         tbl=T(['Market interest rate', 'PV of the bond (its fair price)', 'Compared with face value ₹100', 'What happens'], [
         ['5%', '<b>₹109.29</b> (approx.)', 'Higher', 'Bond looks attractive; people rush; bidding raises its price until price = PV'],
         ['6%', '<b>₹107.33</b> (approx.)', 'Still higher, but lower than at 5%', 'Rate up ⇒ bond price down: inverse relation']]),
         fm=[('Present value of the bond', '10 ÷ (1 + r) + 110 ÷ (1 + r)²', 'r = market rate as a fraction (values worked out here): r = 0.05 → 109.29; r = 0.06 → 107.33', 'wide')]),
    dict(h='Step 4 · From bond fears to cash hoarding (speculative demand)', pts=['If you expect the rate to rise (say settle at 8% when it is 5%), you expect bond prices to fall: a <b>capital loss</b>. So you sell bonds and hold money.',
         '<b>High r</b>: everyone expects it to fall, so expects capital gains, so holds bonds: speculative demand for money is <b>low</b>. <b>Low r</b>: everyone expects a rise, expects capital loss, holds money: demand is <b>high</b>.'],
         fm=[('Speculative demand', 'MD<sub>S</sub> = (r<sub>max</sub> − r) ÷ (r − r<sub>min</sub>)', 'r<sub>max</sub>, r<sub>min</sub> = upper and lower limits of r (positive constants)', 'wide'),
             ('Total money demand', 'MD = k·P·Y + (r<sub>max</sub> − r) ÷ (r − r<sub>min</sub>)', 'transaction part ∝ real GDP and price level; speculative part falls as r rises', 'wide')],
         tbl=T(['Where r stands', 'MDS value', 'Meaning'], [['r = r-max', '0', 'Everyone has put speculative money into bonds'], ['r falls from r-max towards r-min', 'rises from 0', 'More and more people expect capital loss'], ['r = r-min', '∞', 'Liquidity trap: everyone holds money; speculative demand infinitely elastic']]),
         fig=('img/ncert-fig3-1-speculative.png', 'NCERT Fig. 3.1, original: speculative demand for money. r on the vertical axis; the curve falls from r-max and flattens towards r-min, where MDS goes to ∞ (the arrow). How to read: lower r, more money held for speculation.'))],
   d=['The handout lists three purposes (transaction, precautionary, speculative); NCERT has two. For the exam, write the handout’s three.'])],
 '7': [dict(ref='Box 3.1 (last part)',
   why='This is the link between the money you see (supply) and the interest rate. NCERT adds the actual chain of events behind “more money lowers the interest rate”.',
   link='Handout section 7 figure: vertical MS meets falling MD at r0. NCERT explains the arrow of cause behind it.',
   blocks=[dict(h='Why extra money pushes the interest rate down', tbl=T(['Step', 'Event'], [['1', 'Money supply increases'], ['2', 'People use the extra money to buy bonds'], ['3', 'Demand for bonds goes up, so bond prices rise'], ['4', 'Bond price up ⇒ interest rate falls (inverse relation)'], ['5', 'The fall stops at r-min: everyone then expects a rise, so extra money just piles up as cash (liquidity trap)']]),
         pts=['The interest rate is the “price” of holding money balances, so it comes down as supply rises.',
              'NCERT’s chapter summary: RBI regulates money supply by controlling high-powered money, the bank rate and reserve requirements; it also “sterilises” money supply against external shocks (see section 11).'])],
   d=[])],
 '8': [dict(ref='§3.4 Policy tools to control money supply',
   why='NCERT’s tool list is short; its value is the worked cases. Use the tables to see what each tool does to reserves, loans and money supply.',
   link='Handout classification wins: repo and reverse repo are filed under LAF, separate from OMO.',
   blocks=[
    dict(h='Lender of last resort', pts=['When banks need more funds for credit they go to the market, or to the central bank. The RBI being ready to lend to banks at all times is the <b>lender of last resort</b> role.']),
    dict(h='NCERT’s two families of tools', tbl=T(['Quantitative (changes the extent of money supply)', 'Qualitative (persuasion to encourage or discourage lending)'], [['CRR, Bank Rate, Open Market Operations', 'Moral suasion, margin requirement, etc.']])),
    dict(h='Reserve ratio at work: the 20% to 25% case', tbl=T(['Reserve ratio', '₹100 of reserves supports deposits of', 'Loans possible', 'Result'], [
         ['20%', '₹500', '₹400', 'Starting position'], ['25%', '₹400 (₹100 ÷ 0.25, arithmetic)', '₹300', 'Banks must call back some loans; money supply falls']]),
         pts=['Higher reserve ratio ⇒ less lending ⇒ fewer deposits ⇒ lower money supply.', 'NCERT’s sentence says “₹400” for the earlier case; its own table shows ₹500 at 20%. Rule: ₹500 at 20%, ₹400 at 25%.']),
    dict(h='Open market operations: four cases in one table', tbl=T(['Operation', 'What RBI does', 'Promise to reverse?', 'Effect on reserves and money'], [
         ['Outright purchase', 'Buys government bonds, pays by <b>cheque</b>', 'No: permanent', 'Reserves up; money supply up'],
         ['Outright sale', 'Sells bonds to private persons or institutions', 'No: permanent', 'Reserves down; money supply down'],
         ['Repo (repurchase agreement)', 'Buys with a date and price of resale; the rate = <b>repo rate</b>', 'Yes', 'Money injected, then returned'],
         ['Reverse repo', 'Sells with a date and price of repurchase; the rate = <b>reverse repo rate</b>', 'Yes', 'Money withdrawn, then returned']]),
         pts=['Purchase and sale are entrusted to the RBI on behalf of the Government.', 'RBI runs repo and reverse repo at overnight, 7-day, 14-day and other maturities; NCERT calls this now the <b>main tool</b> of monetary policy.']),
    dict(h='Bank Rate (NCERT’s version)', pts=['The rate at which RBI gives loans to commercial banks. Raise it: loans costlier, banks’ reserves fall, money supply decreases. Cut it: money supply can rise.'])],
   d=['NCERT treats the Bank Rate as a live lever. The handout says it is operationally dormant, aligned with the MSF rate and used mainly as the baseline for penalties. Handout wins.',
      'NCERT treats repo and reverse repo as types of OMO; the handout files them under LAF. Use the handout’s classification in answers.'])],
 '11': [dict(ref='Box 3.2 Demonetisation',
   why='A real-life use of the “legal tender” idea: the state declared old notes no longer legal tender. NCERT records the dates, limits and the debate.',
   link='Legal tender (section 2) · cdr and cash habit (section 5) · formal payments shift (cashless society, NCERT §3.1).',
   blocks=[
    dict(h='What happened and when', tbl=T(['When', 'What'], [['Nov 2016', 'Old ₹500 and ₹1000 notes stop being legal tender; new ₹500 and ₹2000 notes launched'], ['Till 12 Dec 2016', 'Old notes still accepted at petrol pumps, government hospitals, and for government dues (taxes, power bills)'],
         ['Till 31 Dec 2016', 'Deposit old notes in a bank account without declaration'], ['Up to 31 Mar 2017', 'Deposit with the RBI, with declaration'], ['Per person per day', 'Exchange of old notes worth ₹4,000 for new (as printed in NCERT)']])),
    dict(h='The aims and the debate', tbl=T(['Aims', 'Costs', 'Gains cited'], [['Corruption, black money, terrorism, fake currency', 'Long queues at banks and ATMs; currency shortage hurt economic activity; normalcy returned with time',
         'Better tax compliance; savings channelised into the formal system (banks lend more at lower rates); signal against tax evasion; shift from cash to electronic payment']]))],
   d=[])],
}

SRCFILES = ["leec103"]
# reading map shown on the chapter opening page
NCMAP = [('3.1 Functions of money; cashless society', '1, 2', 'Three functions of money; barter’s three weaknesses; price level and purchasing power'),
         ('3.2 Demand and supply of money; central bank; commercial banks', '3, 4, 6', 'Central bank functions; HPM; spread; the goldsmith story'),
         ('3.3 Money creation by the banking system', '5', 'Bank balance sheet; CRR and SLR; the ₹100 → ₹500 worked example'),
         ('3.4 Policy tools to control money supply', '8', 'Lender of last resort; outright vs repo OMO; Bank Rate; the 25% example'),
         ('Box 3.1 Demand and supply for money in detail', '6, 7', 'k·T, velocity, bond price, MDS formula, liquidity trap'),
         ('Measures of money supply (M1-M4)', '4', 'NCERT’s legal definitions, narrow vs broad'),
         ('Box 3.2 Demonetisation', '11', 'Nov 2016: aims, exchange limits, effects')]
NCQ = [('What is a barter system? Its drawbacks?', 'Section 1 and NCERT 3.1'),
       ('Main functions of money; how does it overcome barter’s shortcomings?', 'NCERT 3.1 (handout: section 1)'),
       ('What is transaction demand for money; how is it related to the value of transactions?', 'Section 6 + NCERT Box 3.1'),
       ('Alternative definitions of money supply in India?', 'Section 4 (handout ladder) + NCERT definitions'),
       ('What is a legal tender? What is fiat money?', 'Section 2 + NCERT 3.2'),
       ('What is High Powered Money?', 'Sections 3-4 + NCERT 3.2.2'),
       ('Explain the functions of a commercial bank.', 'NCERT 3.2.2 (not in the handout)'),
       ('What is the money multiplier? What determines its value?', 'Section 5 + NCERT 3.3'),
       ('What are the instruments of monetary policy of RBI?', 'Section 8 + NCERT 3.4'),
       ('Is a commercial bank a creator of money?', 'Section 5 + NCERT 3.3'),
       ('Which role of RBI is “lender of last resort”?', 'NCERT 3.4 (handout: sections 8, 11)')]


NCKEY = ['Barter exchange', 'Double coincidence of wants', 'Money', 'Medium of exchange', 'Unit of account', 'Store of value', 'Bonds', 'Rate of interest', 'Liquidity trap', 'Fiat money', 'Legal tender',
         'Narrow money', 'Broad money', 'Currency deposit ratio', 'Reserve deposit ratio', 'High powered money', 'Money multiplier', 'Lender of last resort', 'Open market operation',
         'Bank Rate', 'Cash Reserve Ratio (CRR)', 'Repo Rate', 'Reverse Repo Rate']

NCONLY = []
