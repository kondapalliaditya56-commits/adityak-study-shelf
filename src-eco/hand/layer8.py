# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 8 (Money and Monetary Policy). Facts come only from the handout text.
plain = idea in everyday words (memory aid); eg = the handout's own example; hook = one-line handle."""
TOP = {
 'sixty': [('Money', 'a generally acceptable medium of exchange; trust beats law'),
           ('Supply', 'RBI makes base money (M0); banks multiply it: MS = m × M0'),
           ('Demand', 'transaction (with GDP) + speculative (against r)'),
           ('Price of money', 'the interest rate, where vertical MS meets falling MD'),
           ('Tools', 'qualitative nudges, quantitative levers, corridor MSF-Repo-SDF'),
           ('Goal', 'adequate and trustworthy money: growth vs inflation (FIT 4% ± 2%)')],
 'words': [('Medium of exchange', 'the thing everyone accepts in a sale so that you need not find a perfect swap partner'),
           ('Base money (M0)', 'the money the RBI itself creates (currency plus bank balances with it)'),
           ('Money multiplier (m)', 'how many rupees of money the banking system builds on each rupee of M0'),
           ('Reserve', 'the slice of deposits a bank keeps back and does not lend'),
           ('Interest rate (r)', 'the price of holding or borrowing money'),
           ('Liquidity', 'how quickly and cheaply something turns into spendable cash')],
}
SEC = {
 '1': dict(
   plain='Imagine a village with no money. You have rice and want cloth, so you must find a weaver who wants rice at that same moment: a double coincidence. As the crowd grows this becomes hopeless. So the village agrees on one thing everybody will take in a sale. That thing is money. It only works if it is valuable, keeps its value, can be trusted as genuine, and can be split or added up to any price.',
   eg='The handout’s own pictures: you cannot offer 10 L of water for 1 kg of wheat every time (value needs general demand and limited supply); an apple rots (so it cannot preserve value); tea is divisible, a house needs aggregation (denomination).',
   hook='Money = acceptance. Four tests: Value, Preservation, Authenticity, Denomination.',
   mn=[dict(kind='word', title='NCERT’s three functions of money (order is free)', word='SUM',
            letters=[('S', 'Store of value'), ('U', 'Unit of account'), ('M', 'Medium of exchange')],
            note='Own memory aid (not from NCERT or the handout): money lets you SUM up value. See the NCERT box above.')]),
 '2': dict(
   plain='Money began as gold you could hold. Today it is a promise: the central bank prints a note, and we accept it for two reasons, we trust the issuer and the law says a debt can be settled with it. Government bonds can stand in for gold because they are safe and liquid. The chain of promises runs: note ← central bank ← government ← its power to tax.',
   eg='The handout compares: gold and sovereign bonds are safe; one gram of gold and one share of a company are identical (liquid); land and diamonds are unique units (not replicable, thin market).',
   hook='Legal tender forces acceptance for debt; it does not create value. Trust always overrides law.'),
 '3': dict(
   plain='Read the RBI’s balance sheet like a shop’s ledger with a very lucky owner. Its liabilities (notes, bank balances) cost almost nothing, while its assets (gold, bonds, foreign assets) earn or appreciate. So it makes big profits, but profit is a by-product. Its real duty is to hold only the safest assets, because if its assets ever fall below its promises, people stop trusting the money.',
   eg='Handout’s example: RBI earns 7% on government bonds, pays 0% on a ₹500 note, printing costs about ₹1.2-1.3 a note. The bitcoin case: bought for ₹10 L, falls to ₹5 L, liabilities stay ₹10 L, so liabilities exceed assets and trust is lost.',
   hook='Seigniorage = interest on assets that back a zero-cost promise. RBI buys only the safest assets.'),
 '4': dict(
   plain='Money is not one number. M0 is what the RBI creates. Then we widen the net step by step: M1 is the most spendable money (cash plus demand deposits), M2 adds post-office savings, M3 adds time deposits with banks, M4 adds all post-office deposits. As you go down the ladder, money becomes less liquid. The supply curve is vertical because a monopoly central bank prints for adequacy and trust, not for the interest it could earn.',
   eg='The handout’s reason for the new aggregates: a 14-day FD and a 10-year FD were both “time deposits” in M3 although the first is nearly cash. So the Reddy Committee (1998) moved to maturity: NM1, NM2 (up to 1 year), NM3 (also over 1 year).',
   hook='M1/M2 narrow, M3/M4 broad. Down the ladder: less liquid, wider net. MS is vertical.'),
 '5': dict(
   plain='The RBI puts base money into the system. A seller keeps some as cash and deposits the rest; the bank keeps a reserve and lends the rest; the borrower spends it and the receiver again keeps some cash and deposits the rest. Each round is smaller, so the chain stops. A higher cash habit (cdr) or a higher reserve (rdr) means a shorter chain and a smaller multiplier.',
   eg='The handout’s story: depositors may withdraw everything but banks reserve only for “normal” demand; left alone, banks push the reserve towards zero (reserves give 100% liquidity and 0% profit), so RBI fixes a minimum, the CRR: “the legal enforcement of trust”.',
   hook='MS = m × M0. m falls when cdr rises or rdr rises: m, MS ∝ 1/cdr and 1/rdr.'),
 '6': dict(
   plain='People hold money for three reasons: to spend now and in emergencies (transaction), and to protect wealth when they expect assets to lose value (speculative). Transaction demand grows with the size of the economy (P·Q) and falls if money circulates faster. Speculative demand depends on what you expect interest rates to do. When rates are very low everyone expects them to rise, so everyone hoards cash: the liquidity trap.',
   eg='Handout: a ₹100 note changing hands 10 times a month carries ₹1,000 of transactions (v = 10). With v = 5 you need ₹200 for the same ₹1,000. Bond case: hold a 5% bond, RBI lifts market rates to 8%, nobody wants your 5% bond, so its price must fall.',
   hook='MD = MDT + MDS. MDT ∝ P·Q ÷ v. MDS ∝ 1/r. Bond price and interest rate move opposite. r-min = liquidity trap.'),
 '7': dict(
   plain='Supply is a fixed vertical line set by the RBI; demand slopes down with cost. Where they cross is the interest rate. So the RBI can steer the interest rate by moving supply. Too little money chokes growth; too much money makes people doubt the money itself. Every move has a good and a bad side: that is the dual mandate.',
   eg='Handout: if growth falls, increase supply, r falls, spending and AD rise. If money is too plentiful, cut supply, r rises, AD falls, prices cool.',
   hook='Supply (RBI) × Demand = interest rate. Dual mandate = growth vs inflation, each tool has two sides.'),
 '8': dict(
   plain='The RBI has two kinds of lever. Qualitative tools are nudges and rules about behaviour: they steer direction but the exact effect is hard to predict. Quantitative tools are precise levers: the RBI can calculate the liquidity added or drained. The modern interest-rate framework is a corridor with the MSF rate as ceiling, the repo rate in the middle as anchor, and the SDF rate as floor.',
   eg='Handout’s LTV example: a ₹60 loan against ₹100 of gold instead of ₹80 is tighter credit with no change in interest rates. Moral suasion example: asking banks to restrict lending for speculative stock-market buying in a bubble.',
   hook='Qualitative = CLAMP the behaviour. Quantitative = OMO, CRR, SLR, LAF, MSF, Bank Rate, SDF. Corridor: MSF > Repo > SDF.'),
 '9': dict(
   plain='Two limits shape policy. First, the RBI can supply money but cannot make people borrow: weak roads, high taxes and a poor business climate keep growth stuck even at 0% interest. Second, raising the price of money cuts spending whatever caused inflation, so central banks are better at crushing inflation than at lifting growth. Rules (FIT) replace the Governor’s mood.',
   eg='Handout: governments facing elections press for cheap money to create a temporary boom that later brings long-term inflation (time inconsistency). So the 2015 framework fixes the target: 4% with a band of ±2%.',
   hook='Inside 2-6%: RBI may help growth. Above 6%: must hike. MPC = 3 RBI + 3 external, Governor casts only in a tie.'),
 '10': dict(
   plain='The RBI lends only to banks, not to you. Its decision matters only if banks pass it on. For years they did not. So the way loans are priced was changed four times, each time tying it more tightly to something outside the bank’s control until a repo cut reaches your home-loan EMI automatically.',
   eg='Handout example: home loan = repo 6.5% + 3% spread = 9.5%. Repo cut by 50 basis points to 6.0%, the EMI resets to 9.0% at the next reset date; the bank cannot block it.',
   hook='PLR (after 1993) → Base Rate 2010 → MCLR 2016 → EBLR 2019. Only EBLR is external.'),
 '11': dict(
   plain='Each recent tool answers a specific problem: banks hoarding cash in COVID (LTRO/TLTRO), surplus parked at the RBI (VRRR, SDF), small investors locked out of G-secs (Retail Direct), and foreign inflows that print rupees (sterilisation via MSS).',
   eg='Handout: VRRR announces an amount (say ₹2 Lakh Crore) and banks bid the rate; SDF takes overnight funds with no G-Sec collateral, because selling G-Secs to absorb money would crash prices and raise government borrowing costs.',
   hook='LTRO = long cheap loans. VRRR = auction to absorb. SDF = floor, no collateral. MSS 2004 = lock the rupees.'),
}
NUMBERS = [('4% ± 2%', 'FIT target band (2015)'), ('6', 'members in the MPC (3 RBI + 3 external)'), ('0% to 100%', 'CRR range after the 2006 Amendment (earlier floor 3%, ceiling 40%)'),
           ('1998', 'Y.V. Reddy Committee: NM1-NM3'), ('2004', 'MSS introduced'), ('2010 / 2016 / 2019', 'Base Rate / MCLR / EBLR'),
           ('2020', 'LTRO / TLTRO'), ('2021', 'Retail Direct Scheme'), ('Apr 2022', 'SDF becomes the floor'), ('14 days', 'maximum repo tenor in the handout'),
           ('₹1.2-1.3', 'printing cost per note (handout)'), ('6.5% + 3% = 9.5%', 'EBLR home-loan example')]
DRAW = ['Redraw the handout’s figure of the ladder of money measures (M0 to M4) from section 4, and mark narrow and broad money.',
        'Redraw the handout’s figure with the vertical money supply curve crossing the falling money demand curve at r0 (section 7).',
        'Write the corridor: MSF (ceiling) > Repo (anchor) > SDF (floor), and the four loan-pricing phases in order.']

# ---- handout formulas, shown as boxed cards at the top of the section and again on the formula sheet
FM = {
 '3': [('Base money (M0)', 'M0 = RBI’s total liabilities', 'currency in circulation + bank deposits + government deposits + provisions'),
       ('Seigniorage', 'interest earned on assets − printing cost', 'example: 7% on bonds − 0% on a ₹500 note, minus ≈ ₹1.2-1.3 printing cost')],
 '4': [('M1 (narrow)', 'M1 = CC + DD + “Other” deposits with RBI', 'cash with the public + demand deposits'),
       ('M2 (narrow)', 'M2 = M1 + P.O. demand deposits', ''),
       ('M3 (broad)', 'M3 = M1 + TD with banks', 'the handout’s most important metric for RBI'),
       ('M4 (broad)', 'M4 = M3 + post-office deposits (DD, TD, other)', ''),
       ('NM1', 'NM1 = CC + DD + other deposits with RBI', 'practically the old M1'),
       ('NM2', 'NM2 = NM1 + short-term TD (up to 1 year)', ''),
       ('NM3', 'NM3 = NM2 + long-term TD (over 1 year) + call/term funding', 'Y.V. Reddy Committee, 1998', 'wide')],
 '5': [('Money supply', 'MS = m × M0', 'M0 = high-powered money; m = money multiplier'),
       ('cdr', 'cdr = cash ÷ deposits', 'm, MS ∝ 1 ÷ cdr'),
       ('rdr', 'rdr = reserves ÷ deposits', 'm, MS ∝ 1 ÷ rdr')],
 '6': [('Total money demand', 'MD = MD<sub>T</sub> + MD<sub>S</sub>', 'transaction + speculative'),
       ('Transaction demand', 'MD<sub>T</sub> ∝ V<sub>T</sub> ∝ P·Q', 'V<sub>T</sub> = value of transactions; P·Q = nominal GDP'),
       ('With velocity', 'MD<sub>T</sub> ∝ P·Q ÷ v', 'v = ₹1,000 ÷ ₹100 = 10 per month (handout)'),
       ('Speculative demand', 'MD<sub>S</sub> ∝ 1 ÷ r', 'r high → MDS falls; r = r-min → ∞')],
 '7': [('Interest rate', 'r0 is where vertical MS = falling MD', 'handout figure, section 7')],
 '8': [('NDTL (base of CRR/SLR)', 'NDTL = demand + time deposits − inter-bank deposits', ''),
       ('Policy corridor', 'SDF rate &lt; Repo rate &lt; MSF rate', 'floor, anchor, ceiling'),
       ('Tightening chain', 'CRR or SLR ↑ ⇒ m ↓ ⇒ MS ↓', 'handout, quantitative tools table')],
 '9': [('FIT band', 'CPI target 4% ± 2% = 2% to 6%', 'inside: may help growth; above 6%: must hike')],
 '10': [('EBLR loan rate', 'loan rate = repo + spread', '6.5% + 3% = 9.5%; repo −50 bps → 6.0% → 9.0%')],
}
