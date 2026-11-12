# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 9 (Capital Markets). Facts come only from the handout text."""
TOP = {
 'sixty': [('Two markets', 'money market = debt under 1 year, near money; capital market = equity and debt over 1 year, fixed capital'),
           ('Instruments', 'T-bills 91/182/364 days and CMBs 7-15 days (Centre only); CP; CoD (tradable)'),
           ('Raising money', 'primary market = company gets money (IPO/FPO); secondary = investor to investor; OFS = company gets zero'),
           ('Trust architecture', 'exchange + clearing house (pre-funding, novation) + depositories (NSDL, CDSL) + broker + bank'),
           ('Yardsticks', 'Sensex 30 firms base 100 (1979); Nifty 50 base 1000 (1995); alpha = extra return, beta = volatility'),
           ('Derivatives and funds', 'futures = obligation, option = right with capped loss; mutual fund = Trust with NAV; ETF trades live')],
 'words': [('Money market', 'the place for borrowing and lending for less than a year, to keep day-to-day cash flowing'),
           ('Capital market', 'the place where money is tied up for long, to build factories and expand'),
           ('Primary market', 'where a company sells brand-new shares and receives the money'),
           ('Secondary market', 'where one investor sells to another; the company is not involved'),
           ('Clearing house', 'the middleman that stands as buyer to every seller and seller to every buyer, so nobody can default on you'),
           ('Derivative', 'a contract with no value of its own; it draws its value from something else (the underlying)'),
           ('NAV', 'the value of one mutual fund unit: (assets minus liabilities) divided by units'),
           ('Depository receipt', 'a paper traded abroad that stands for real shares kept at home')],
}
SEC = {
 '1': dict(
   plain='Think of two kinds of money jobs. One is plumbing: a shop needs cash for a few weeks to pay suppliers, so it borrows for under a year. That is the money market, low risk and almost as good as cash. The other is construction: a factory needs money for years, so the investor parts with cash for long and cannot easily get it back. That is the capital market. In both, the people with and without money decide themselves and carry the risk; the middlemen only help with information, trust and paperwork.',
   eg='The handout’s own line: equity gives rights in perpetuity, so it is long term and belongs to the capital market; only debt below 1 year is money market. Banking is different: there the bank decides (Chapter 7).',
   hook='Money market = under 1 year, debt, near money. Capital market = factories, long term. Four splits: rights, maturity, terms, settlement.'),
 '2': dict(
   plain='Four short-term IOUs. A T-bill is the Centre’s IOU sold at a discount (say you pay less today and get the full face value back later), so there is no interest coupon. A CMB is the same idea but for just days. Commercial paper is a company’s IOU, allowed only if its rating is good enough. A certificate of deposit is a bank’s IOU, and unlike an FD you can sell it on.',
   eg='The handout: States do not issue T-bills; they use Ways and Means Advances (WMA) from RBI. Five AIFIs can issue CP: NABARD, NHB, SIDBI, EXIM Bank, NaBFID.',
   hook='T-bill 91-182-364; CMB 7-15 days; only the Centre. CP = rated company paper; CoD = bank paper you can trade.'),
 '3': dict(
   plain='Some contracts are tailor-made (a loan, a debenture) and so are hard to sell to a stranger. Others come in standard sizes (a bond, an ordinary share) so many people trade them freely. Separately, you can settle at once (spot) or fix a price today for a deal later (futures or forward). A derivative is a contract whose value comes from something else, like a betting slip on rain.',
   eg='The handout’s pairs: customised (OTC) = loans, debentures, preference shares; standardised = bonds, common equity. Futures are standardised; forwards are OTC.',
   hook='Customised = OTC, hard to trade. Standard = liquid. Spot = now; futures = fixed price, later. Derivative = value borrowed from the underlying.'),
 '4': dict(
   plain='A business starts as one person’s idea, then becomes a company, a separate legal body that can sign contracts and be sued. To grow it takes money from angel investors, then funds and investment banks, and at last the public through an IPO. In an IPO the company sells new shares and gets the cash. In an OFS the early owners sell their shares and the company gets nothing. So always ask how much of the headline is fresh issue.',
   eg='The handout’s sum: a ₹10,000 Cr IPO with ₹9,000 Cr as OFS means the company raises only ₹1,000 Cr. The green shoe: the underwriter borrows extra shares from promoters, sells them, and if the price crashes on listing uses that cash to buy shares back.',
   hook='Primary = company gets money. Secondary = investor to investor. OFS = company gets ZERO. DRHP (no price) becomes RHP (price band).',
   mn=[dict(kind='sentence', title='The IPO process, six steps in order', sentence='Don’t Skip Reading Any Company Documents',
            letters=[('D', 'Decide amount and manner with advisors (lead manager, underwriter)'), ('S', 'SEBI application: DRHP becomes RHP'),
                     ('R', 'Reveal to the public by advertisement'), ('A', 'Apply through ASBA (money blocked, not debited)'),
                     ('C', 'Cut-off price; over- or under-subscription; green shoe'), ('D', 'Demat credit to successful applicants, funds unblocked for others')],
            note='Own memory aid (not from the handout): the six steps are the handout’s own list, in its order.')]),
 '5': dict(
   plain='Strangers will not hand money to strangers unless someone guarantees the deal. The exchange is the marketplace and price-finder. The clearing house checks that money and shares are locked before the order and then stands in the middle of every trade, so if one side fails the other is still safe. Depositories keep your shares safely in digital form. A broker is your gateway, and banks supply the money. Settlement, the time from trade to delivery, has shrunk from 14 days to T+1.',
   eg='The handout: before the Depositories Act, 1996 shares were paper, settlement took 14 days and brokers misused client assets, ending in the 1992 stock market scam. Brokers first met under a Banyan tree in Mumbai in 1875.',
   hook='Exchange = trust, convenience, price discovery. CH = pre-funding + novation. NSDL and CDSL = Act of 1996. T+1, moving to T+0.'),
 '6': dict(
   plain='Return can be told in several ways. Absolute return is just start to finish. Average return is the yearly compounded figure. IRR looks at every cash flow in between, like rent and repairs on a flat. Comparative return asks whether you beat the benchmark. Alpha is the extra return over the benchmark; beta is how wildly you swing compared with it. A high beta with no alpha means more risk for no reward.',
   eg='The handout’s house example: bought at ₹2 Cr, worth ₹5 Cr in 5 years, but rent and maintenance cash flows change the real return. Beta 1 moves exactly with the Nifty; beta 1.5 is 50% more volatile.',
   hook='Alpha = extra return. Beta = volatility versus the benchmark. IRR counts cash flows.'),
 '7': dict(
   plain='An index is a scoreboard for a basket of big listed companies, weighted by size. It starts at a base value (100 or 1000) and moves with the weighted average price. But the scoreboard covers only the largest, most formal firms, so it can hit a record while small businesses, farmers and the jobless suffer. Also, markets look ahead while the economy reports the past.',
   eg='The handout’s sum: if the weighted average price rises from 10,000 (index 100) to 100,000 the index is 1000, ten times in 10 years. COVID: the market hit record highs while GDP fell, because large firms survived and took the share of dying small ones.',
   hook='Sensex 30 / 100 / 1979. Nifty 50 / 1000 / 1995. Market looks forward, economy mirrors the past.'),
 '8': dict(
   plain='Picture a plot of land worth ₹10 L that becomes ₹50 L if a highway is approved and ₹5 L if cancelled. Buying now ties up all your cash. A future locks a price for one year with nothing paid now, and you must buy whatever happens, so you can lose. An option costs a small non-refundable fee for the right, not the duty, to buy, so your loss is capped at the fee. The contract itself can become valuable and tradable.',
   eg='The handout’s table: futures at ₹11 L give profit ₹39 L if approved, loss ₹6 L if cancelled. Option with ₹1 L premium gives net profit ₹38 L if approved, loss only ₹1 L if cancelled.',
   hook='Future = obligation, symmetrical. Option = right, loss capped at premium. Be right on direction AND time.'),
 '9': dict(
   plain='Trading yourself means competing against institutions that heard the news months before you. The handout’s advice is to hand your money to experts. A mutual fund pools money from many people, a fund manager invests it, and each investor holds units. An ETF is a fund that simply copies an index and trades live on the exchange like a share.',
   eg='The handout: a Nifty 50 ETF holds the exact 50 stocks in index weights. A mutual fund NAV is computed once a day (EOD); an ETF value can be computed every second.',
   hook='Fund = owner + objective + manager + contributors + corpus. NAV = (assets − liabilities) ÷ units. ETF = index, traded live.'),
 '10': dict(
   plain='An Indian company that wants dollars from abroad can keep its shares with a bank in Mumbai and let a bank overseas issue receipts against them, traded in dollars. That is an ADR (US) or GDR (global). An IDR is the mirror: a foreign company raises rupees here. P-Notes were a back door: black money went offshore, came back through a registered FII, and SEBI could not see the real owner. After 2016-2017 FIIs had to disclose the Ultimate Beneficial Owner.',
   eg='The handout’s examples: Infosys for ADR and GDR, Standard Chartered for IDR, Mauritius as the tax haven in the P-Note round trip.',
   hook='ADR = US, GDR = global, IDR = foreigner raising rupees. P-Note = hidden owner; UBO rule 2016-2017.'),
}
NUMBERS = [('91 / 182 / 364', 'T-bill maturities in days'), ('7-15 days', 'Cash Management Bills'), ('5', 'AIFIs that can issue CP'),
           ('₹10,000 Cr / ₹9,000 Cr', 'IPO with OFS: company raises only ₹1,000 Cr'), ('1875', 'Brokers under a Banyan tree (BSE)'),
           ('1992', 'Stock market scam'), ('1996', 'Depositories Act: NSDL, CDSL'), ('14 days to T+1', 'settlement cycle'),
           ('30 / 100 / 1979', 'Sensex companies, base value, base year'), ('50 / 1000 / 1995', 'Nifty companies, base value, base year'),
           ('6 months', 'index rebalancing gap'), ('₹10 L, ₹50 L, ₹5 L, ₹11 L, ₹1 L', 'highway-land example'), ('1882', 'Indian Trusts Act (mutual fund)'),
           ('2016-2017', 'SEBI UBO rule for P-Notes')]
DRAW = ['Redraw the handout’s fork on IPO or OFS (section 4): who gets the money? Write ₹10,000 Cr, ₹9,000 Cr and ₹1,000 Cr on it.',
        'Redraw the handout’s six-step IPO flow (section 4) from memory, then the five intermediaries (SHRED) of section 5.',
        'Redraw the handout’s fork of futures versus option (section 8) with the ₹50 L and ₹5 L outcomes.']
FM = {
 '4': [('OFS arithmetic', 'company raises = IPO size − OFS part', '₹10,000 Cr − ₹9,000 Cr = ₹1,000 Cr (handout)')],
 '6': [('Beta reading', 'beta 1 = moves with Nifty; beta 1.5 = 50% more volatile', 'high beta + no alpha = more risk, no extra return')],
 '7': [('Index jump', 'index = base × (WAP now ÷ WAP at base)', 'WAP 10,000 → 100,000 on base 100 gives 1000')],
 '8': [('Futures payoff', 'profit = market value − agreed price', '₹50 L − ₹11 L = ₹39 L; ₹5 L − ₹11 L = −₹6 L'),
       ('Option payoff', 'net = market value − strike − premium', '₹50 L − ₹11 L − ₹1 L = ₹38 L; loss capped at ₹1 L')],
 '9': [('NAV', 'NAV = (assets − liabilities and expenses) ÷ units', 'one unit of a mutual fund')],
}
