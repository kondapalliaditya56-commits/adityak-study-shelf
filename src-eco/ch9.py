from lib import Ch

c = Ch(9, 'Capital Markets: Money Market, Stock Market, Derivatives and Funds',
       'Economy · GS Foundation · Chapter 9',
       [('hb', 'Handout only: no class slides'), ('', 'Handout pages 1-18'), ('', 'No PYQs quoted')],
       'Classes of contracts, the money market (T-bills, CMBs, CP, CoD), how a company raises capital, the IPO process and OFS, stock market intermediaries (exchange, clearing house, depositories, brokers), returns, alpha and beta, Nifty and Sensex, market versus economy, derivatives (futures and options), mutual funds, ETFs, depository receipts and P-Notes.')

c.sec('Exam lens: priority and PYQs', 'exam-lens-priority-and-pyqs')
c.call('alert', 'Source note', ['**Handout only.** No class slides, no teacher ink. **No Prelims or Mains PYQ is quoted** in this handout: none quoted in the material. Priority below is the handout’s own emphasis (explicit numbers, definitions and its “starred” points).'])
c.table('What the handout stresses', ['Signal in the handout', 'Where', 'Why it matters'], [
    ['Money market = under **1 year,** debt only, “near money”; capital market = long term (fixed capital formation)', 'Section 1', 'Basic classification'],
    ['**T-bills 91, 182, 364 days; CMBs 7-15 days;** only the Centre issues them; zero-coupon, sold at a discount', 'Section 2', 'Numbers'],
    ['**CP:** investment-grade rating (SEBI); **5 AIFIs** can issue (NABARD, NHB, SIDBI, EXIM, NaBFID). **CoD** tradable', 'Section 2', 'Lists'],
    ['**Primary versus secondary;** IPO/FPO versus **OFS** (company gets zero); **DRHP → RHP; ASBA; green shoe**', 'Sections 3-4', 'Process terms'],
    ['**Clearing house:** pre-funding and **novation;** **Depositories Act 1996:** NSDL, CDSL; **T+1,** moving to T+0', 'Section 5', 'Institutions and dates'],
    ['**Alpha and beta;** **Sensex 30 companies, base 100, 1979;** **Nifty 50, base 1000, 1995;** rebalanced about every 6 months', 'Sections 6-7', 'Numbers'],
    ['Futures (obligation) versus options (right); **strike, expiry, premium**', 'Section 8', 'Highway-and-land example'],
    ['**Mutual fund as a Trust (Indian Trusts Act 1882);** AMC; NAV; TER; ETF; **ADR, GDR, IDR;** **P-Notes (ODIs),** UBO rules 2016-2017', 'Sections 9-10', 'Definitions'],
])
c.call('key', 'What to prepare', [
    '**Prelims hooks:** T-bill and CMB maturities; who can issue CP and CoD; primary versus secondary market; IPO versus OFS; DRHP/RHP; ASBA; green shoe; novation; NSDL and CDSL; Sensex and Nifty facts; alpha and beta; futures versus options; NAV and TER; ETF; ADR, GDR, IDR; P-Notes.',
    '**Mains hooks:** what stock exchanges, clearing houses and depositories do for trust; why the stock market is not the economy and why it can rise when the economy falls; why derivatives are risk-management tools; why retail investors lose; regulation of P-Notes.',
    '**Closing idea:** a market works because strangers can trust each other; every institution in it exists to manufacture that trust.'])

c.sec('1 · Capital markets: the four ways to classify contracts')
c.p('In capital markets the **demanders and suppliers themselves decide,** so they **bear the risks** and enjoy most of the reward. Intermediaries give information, build trust and do back-end work. (In banking, by contrast, the bank decides: see Chapter 7.) Contracts are classified by:')
c.ol(['**Rights and obligations:** debt versus equity.',
      '**Maturity:** less than 1 year is **short term;** more than 1 year is **long term.**',
      '**Terms and conditions:** standardised versus customised.',
      '**Settlement:** spot versus futures (derivatives).'])
c.table('Money market versus capital market', ['', 'Money market', 'Capital market'], [
    ['**Contracts**', 'Short-term (**below 1 year**) **debt** contracts (equity gives rights in perpetuity, so it is long term)', 'Equity, and debt of **more than 1 year** (loans, bonds)'],
    ['**Purpose**', 'Manage **working capital** and short-term liquidity mismatches', '**Fixed capital formation** (factories, expansion)'],
    ['**Features**', 'Less risky, usually **unsecured,** low interest, extremely liquid: **“near money”**', 'Money turns into an asset for long: money loses liquidity (the asset itself may be liquid)'],
], rowhead=True)

c.sec('2 · Money market instruments')
c.table('T-bills, CMBs, CP and CoD', ['Instrument', 'Issuer', 'Key facts (from the handout)'], [
    ['**Treasury Bills (T-bills)**', '**Only the Centre**', 'Unsecured short-term government debt; maturity **91, 182, 364 days;** **zero coupon:** sold by **auction at a discount** and redeemed at par (face value)'],
    ['**Cash Management Bills (CMBs)**', '**Only the Centre**', 'Maturity **7 to 15 days.** **State governments** manage short-term mismatches through **Ways and Means Advances (WMA) from RBI,** not T-bills'],
    ['**Commercial Paper (CP)**', 'Corporations, several NBFCs, **InvITs, DFIs**', 'Unsecured; issuer needs a rating **above a SEBI-prescribed minimum investment grade.** Five **AIFIs** (All India Financial Institutions) can issue: **NABARD, NHB, SIDBI, EXIM Bank, NaBFID** (National Bank for Financing Infrastructure Development)'],
    ['**Certificate of Deposit (CoD)**', 'Banks', 'Short-term deposits raised by issuing certificates, used when banks face a liquidity crunch. Unlike FDs, **CoDs are tradable**'],
], rowhead=True)

c.sec('3 · Customised versus standardised, spot versus futures')
c.table('Two more splits', ['', 'Customised (OTC)', 'Standardised'], [
    ['**Liquidity**', 'Market not well developed, not easily tradable except via specific counters: **Over The Counter (OTC)**', 'Many buyers and sellers, easily tradable on markets'],
    ['**Examples**', 'Loans, debentures, preference shares', 'Bonds, common equity'],
], rowhead=True)
c.ul(['**Spot contracts:** settled on the spot (buyer pays, seller delivers); also called **CNC (Cash and Carry).**',
      '**Futures (standardised) / Forwards (OTC):** signed today, exchange at a **future date** at a **predetermined price.** The **underlying** is the commodity or contract; the agreed price is the **strike price** (the biggest factor is the **current market price, CMP**); the time limit is **maturity.**',
      '**Derivatives:** contracts with no value of their own; they **derive** value from the underlying (futures, options, swaps, securitised loans). The handout likens one to a **betting slip** on rain.'])

c.sec('4 · From a business idea to a public company')
c.ul(['A **company** exists independently of the entrepreneur, so it can enter enforceable contracts, sue and be sued. **Authorised capital** is the total shares of some face value it may issue; the part issued is **paid-up capital.** Promoters bring the initial capital. Shares can be given without money, e.g. **sweat equity** for employees.',
      'Growth stages: **angel investors** (money plus experience, network, mentoring; a valuation is negotiated and equity given); then **venture capital funds, private equity funds, investment banks** (who raise from firms and HNIs); finally the **public.**',
      '**Primary market:** the company issues **new shares** from its authorised capital. **Secondary market:** an existing investor sells to a new one; **the company is nowhere involved.**',
      '**Preference shares:** customised shares with **priority rights** (fixed dividend first and capital back first on bankruptcy). Only beyond a point are standardised shares issued for liquidity.'])
c.table('Public issue', ['Term', 'Meaning'], [
    ['**IPO / FPO**', 'Initial / Follow-on Public Offer: the company issues shares and **raises capital**'],
    ['**OFS (Offer for Sale)**', 'Existing owners sell to the public: a **secondary market** sale. **The company receives ZERO.** Example in the handout: a ₹10,000 Cr IPO with ₹9,000 Cr as OFS means the company raises only ₹1,000 Cr'],
], rowhead=True)
c.h3('The IPO process (SEBI-prescribed)')
c.ol(['The company decides the amount (e.g. ₹10,000 Cr) and manner (fresh issue or OFS, capital structure, valuation) with advisors: **investment banks (lead manager, underwriter).** An **underwriter** promises to buy all unsold shares.',
      '**Application to SEBI:** documents (balance sheet, promoter records, risks). The **DRHP (Draft Red Herring Prospectus)** has **no valuation;** after approval and once the price band is final it becomes the **RHP.** (“Red herring”: intentionally lacks final price and quantity.)',
      '**Revealing to the public** by advertisement.',
      '**Application and allotment** through **ASBA (Application Supported by Blocked Amount):** the money is **blocked, not debited,** so you keep earning savings interest and refunds are not delayed.',
      '**Cut-off price.** **Over-subscription:** demand exceeds supply (fair allocation); **under-subscription:** demand below supply (the underwriter steps in). The **green shoe option** is an over-allotment option for price stabilisation: the underwriter borrows extra shares from promoters and sells them; if the price crashes on listing, the cash is used to buy back shares from the market.',
      'Successful applicants get shares in their **demat** accounts; others get funds unblocked.'])
c.p('Public issues and trading both take place on **NSE and BSE;** exchanges serve the **primary** as well as the secondary market (commonly forgotten).')

c.sec('5 · Stock market intermediaries')
c.table('Five main intermediaries', ['Intermediary', 'Role (from the handout)'], [
    ['**Stock exchanges (NSE, BSE)**', 'Background tasks, **trust** between strangers, information on demand, supply and price, for **rational price discovery.** Brokers first met under a **Banyan tree in Mumbai in 1875** (today’s BSE). Three functions: **trust** (the market is the guarantor; the “Amazon” function), **convenience** (transfer of title via the Registrar), **rationality / price discovery** (participation gives depth, so no one can manipulate the price)'],
    ['**Clearing house (CH)**', 'The **trust architect.** **Pre-funding:** buyer’s money is blocked in the trading account and the seller’s shares are blocked in the demat account before the order. **Novation:** the CH becomes buyer to every seller and seller to every buyer, so **counterparty risk is annihilated**'],
    ['**Depositories and DPs**', 'Safe storage of digital assets (shares, bonds, MF units, T-bills). The **Depositories Act, 1996** created **NSDL and CDSL** and mandated **dematerialisation.** Before, shares were paper, settlement took **14 days,** and brokers misused client assets, culminating in the **1992 stock market scam**'],
    ['**Brokers**', 'The gateway: citizens cannot trade directly. A **SEBI-registered broker** opens a **trading account** (holds funds); a **demat** account is opened with NSDL or CDSL'],
    ['**Banks**', 'Provide money to investors, own or borrowed'],
], rowhead=True)
c.p('**The flow:** open trading and demat accounts, place a buy order via the broker, the CH makes sure obligations are met first, orders form **bids and asks,** a matched order is **executed.** The time from execution to credit of shares and money is the **settlement cycle.** Settlement is now **T+1** (T = transaction day) with a **migration to same-day (T+0)** started.')
c.call('alert', 'Handout alert: demat date and settlement', 'The handout says the **Depositories Act was passed in 1996** and, later, that SEBI required **dematerialisation in 1995.** The 1996 Act is the statutory date; **1995** is given for the SEBI requirement. Also, settlement was **14 days** earlier and is **T+1** now. Exam-hall rule: quote **Depositories Act 1996 (NSDL, CDSL)**; mention 1995 only if a question uses it.')

c.sec('6 · Returns: absolute, IRR, alpha and beta')
c.table('Ways to look at returns', ['Kind', 'Meaning'], [
    ['**Absolute returns**', 'Point to point over a period'],
    ['**Average returns**', 'Per year, as a **compounded** average'],
    ['**IRR / XIRR**', 'Internal rate of return on **cash flows** (regular or irregular investments, dividends, rent, maintenance). The handout’s house example: bought at ₹2 Cr, worth ₹5 Cr in 5 years, but rent and maintenance cash flows change the real return'],
    ['**Comparative returns**', 'Against a **benchmark** (Nifty 50, Sensex or a relevant index)'],
    ['**Alpha**', 'The **additional** return a portfolio earns over the benchmark'],
    ['**Beta**', 'The portfolio’s **volatility relative to the benchmark.** Beta 1 moves exactly with the Nifty; **beta 1.5 is 50% more volatile (riskier).** High beta with no alpha means more risk without better returns'],
], rowhead=True)

c.sec('7 · Benchmarks and indices: Nifty, Sensex and market versus economy')
c.ul(['A **benchmark** is a basket of listed companies with **weights** by relative importance (assessed mainly by **free-float market capitalisation**). Its **weighted average price (WAP)** at the base date is **indexed** to 100 or 1000. If WAP goes from 10,000 (index 100) to 100,000 the index is **1000:** the sector gave **10 times** over 10 years. A relevant benchmark for an IT-heavy portfolio is an IT index.',
      'Indices are **rebalanced about every 6 months** (firms exit and enter, weights change).'])
c.table('Sensex versus Nifty', ['', 'BSE Sensex', 'Nifty 50'], [
    ['**Companies**', '30', '50'],
    ['**Base value**', '100', '1000'],
    ['**Base year**', '1979', '1995'],
], rowhead=True)
c.h3('Market versus economy')
c.ul(['Broad indices are used as a **proxy** for economic health, which can mislead. They reflect only the WAP of **50 largest, most formal, cash-rich corporations,** not unorganised MSMEs, agricultural distress, poverty, unemployment, inflation or trade.',
      'In **systemic shocks (COVID-19)** the market can hit **record highs** while GDP falls and unemployment rises, because large firms survive and capture the share of dying small businesses.',
      '**Forward-discounting mechanism:** the economy is a mirror of the past and present, but the stock market **discounts the future** (about 18 months ahead in the handout’s words). A stock price is the aggregate of what millions expect a company to earn.'])

c.sec('8 · Derivatives: the highway-and-land example')
c.p('The handout uses land worth ₹10 L that could be worth ₹50 L if a highway is approved or ₹5 L if cancelled, with the decision in one year.')
c.table('Spot versus futures versus option', ['Contract', 'What you do', 'If approved (₹50 L)', 'If cancelled (₹5 L)', 'Risk'], [
    ['**Spot (cash and carry)**', 'Pay ₹10 L now, take the papers', 'You own it', 'You own it', '100% risk, all capital tied up'],
    ['**Futures / forward**', 'Agree to buy for **₹11 L** in one year; no money now', 'Profit **₹39 L**', 'Loss **₹6 L** (bound to buy a worthless plot)', '**Symmetrical,** an obligation for both'],
    ['**Option**', 'Pay a non-refundable **₹1 L premium** for the **right, not the obligation,** to buy at ₹11 L', 'Net profit **₹38 L** (cost ₹12 L)', 'Loss **only ₹1 L:** tear up the contract', '**Asymmetrical:** upside large, downside capped at the premium'],
], rowhead=True)
c.table('Mapping to market terms', ['In the example', 'Term'], [
    ['The barren land', '**Underlying asset** (shares, gold, wheat)'],
    ['The 1-year deadline', '**Expiry date**'],
    ['The agreed ₹11 L', '**Strike price**'],
    ['The ₹1 L token', '**Option premium**'],
], rowhead=True)
c.ul(['The option itself becomes tradable and valuable (others may offer ₹15 L for it): that is why derivatives are traded.',
      '**Philosophy:** derivatives are **risk-management (hedging)** vehicles; institutions buy options as insurance. Retail traders use the **leverage** (₹1 L premium controls ₹50 L of exposure) for gambling; the handout says **99% of retail derivative traders lose money.**',
      '**The ticking clock:** in spot markets you need to be right on **direction;** in derivatives you must be right on **direction AND time.** A call option expiring March 31 is worthless if the highway is announced April 1.'])

c.sec('9 · Expert handling of money: mutual funds and ETFs')
c.ul(['**Retail trap:** slogans like “Yeh market sabka hai” and FOMO; by the time news reaches retail traders, institutions have known for months. The handout says **9 out of 10 retail traders lose money** and advises handing capital to experts, i.e. **mutual funds.**',
      'Every “fund” has: an **owner,** a **designated objective,** a **fund manager,** **voluntary contributors** and a **corpus.**'])
c.table('Mutual fund versus ETF', ['', 'Mutual fund', 'ETF (Exchange Traded Fund)'], [
    ['**Structure**', 'A **Trust** under the **Indian Trusts Act, 1882;** investors are beneficiaries; a board of **Trustees** oversees. An **AMC** (Asset Management Company) launches schemes and hires fund managers', 'Passively managed: e.g. a Nifty 50 ETF holds the exact 50 stocks in index weights'],
    ['**Unit value**', 'Investors get **Units;** value of one unit is **NAV = (assets − liabilities and expenses) ÷ units.** **TER (Total Expense Ratio)** is capped by SEBI', 'Value computable every second'],
    ['**Trading**', 'NAV computed **once a day (EOD);** buy and sell **with the AMC,** not on the exchange', 'Units **listed on the stock exchange** and traded live like shares'],
], rowhead=True)

c.sec('10 · Crossing borders: depository receipts and P-Notes')
c.table('Depository receipts', ['Instrument', 'Meaning'], [
    ['**Mechanism**', 'An Indian company (the handout uses Infosys) deposits shares with a **local custodian bank** in Mumbai; an **overseas depository bank** issues **receipts** against them, traded in dollars abroad. Avoids conforming the whole accounting system to US standards'],
    ['**ADR**', 'American Depository Receipt: traded in the US'],
    ['**GDR**', 'Global Depository Receipt: Europe or other global markets'],
    ['**IDR**', 'Indian Depository Receipt: the reverse; a **foreign** company raises rupees from Indian investors by issuing IDRs on BSE/NSE (the handout’s example: Standard Chartered)'],
], rowhead=True)
c.p('**Participatory Notes (P-Notes)** are officially **Offshore Derivative Instruments (ODIs).** They were used as a “washing mechanism” (round-tripping) for black money: illegal wealth goes to a tax haven (Mauritius), is handed to a SEBI-registered **FII** which invests in its own name; the FII issues a P-Note to the owner, passing on the profits. SEBI could not see the real owner. In **2016-2017** SEBI required FIIs to disclose the **Ultimate Beneficial Owner (UBO)** of every P-Note on request; issuance then fell sharply.')

c.mm = ('Capital markets', [
    ('Classification', [('Debt vs equity', None), ('Short vs long term (1 year)', None), ('Standardised vs OTC', None), ('Spot vs futures', None)]),
    ('Money market', [('T-bills 91/182/364; CMB 7-15 days', None), ('CP: 5 AIFIs', None), ('CoD tradable', None), ('WMA for states', None)]),
    ('Raising capital', [('Angel → VC/PE → public', None), ('Primary vs secondary', None), ('IPO/FPO vs OFS', None), ('Preference shares', None)]),
    ('IPO process', [('DRHP → RHP', None), ('ASBA', None), ('Underwriter, green shoe', None), ('Demat allotment', None)]),
    ('Intermediaries', [('Exchange: trust, convenience, price discovery', None), ('Clearing house: pre-funding, novation', None), ('NSDL, CDSL: Depositories Act 1996', None), ('Brokers, banks', None)]),
    ('Returns', [('Absolute, IRR', None), ('Alpha, beta', None), ('Sensex 30/100/1979', None), ('Nifty 50/1000/1995', None)]),
    ('Derivatives', [('Futures: obligation', None), ('Options: right, premium', None), ('Underlying, strike, expiry', None), ('Hedging vs speculation', None)]),
    ('Funds and cross-border', [('Mutual fund: Trust, AMC, NAV, TER', None), ('ETF', None), ('ADR, GDR, IDR', None), ('P-Notes (ODIs), UBO', None)]),
])

c.timeline = [
    ('1875', 'Brokers gather under a Banyan tree in Mumbai (today’s BSE).', True),
    ('1882', 'Indian Trusts Act (legal form of a mutual fund).', False),
    ('1979', 'Sensex base year (base value 100).', True),
    ('1992', 'Stock market scam (broker misuse of client assets).', True),
    ('1995', 'Nifty base year (base value 1000); demat requirement by SEBI.', True),
    ('1996', 'Depositories Act: NSDL and CDSL.', True),
    ('2016-2017', 'SEBI UBO disclosure rules for P-Notes.', True),
]

c.connects = [
    ('[Chapter 7: Banking and NBFCs](eco-ch07.html)', 'The previous handout’s section 1 on contracts and intermediaries leads here: banks are decision-making intermediaries (RBI), exchanges are decision-facilitating (SEBI).'),
    ('[Chapter 8: Money and Monetary Policy](eco-ch08.html)', 'T-bills, MIBOR, CoD and G-secs are the market instruments RBI uses; T-bills appear as EBLR benchmarks.'),
    ('[Chapter 5: National Income Accounting](eco-ch05.html)', 'The market-versus-economy section contrasts index levels with GDP, unemployment and poverty.'),
    ('[Chapter 10: External Sector](eco-ch10.html)', 'ADR, GDR, IDR, FII and P-Notes link to capital account flows.'),
    ('[Chapter 12: Budget and Fiscal Policy](eco-ch12.html)', 'T-bills and CMBs fund the Centre’s short-term needs; States use WMA.'),
]

c.recall = [
    'Money market: debt under 1 year, near money, working capital. Capital market: equity and debt over 1 year, fixed capital.',
    'T-bills 91/182/364 days, zero coupon at discount; CMBs 7-15 days; only the Centre; States use WMA. CP: investment-grade, 5 AIFIs. CoD: tradable bank deposit.',
    'Primary: company issues. Secondary: investors trade; company uninvolved. OFS: company gets zero.',
    'IPO: lead manager and underwriter; DRHP (no price) → RHP; ASBA blocks money; green shoe over-allotment.',
    'Exchange = trust, convenience, price discovery. Clearing house = pre-funding, novation. Depositories Act 1996: NSDL, CDSL. T+1, moving to T+0.',
    'Alpha = excess return over benchmark. Beta = relative volatility (1.5 = 50% more).',
    'Sensex: 30, base 100, 1979. Nifty: 50, base 1000, 1995. Rebalanced about every 6 months. Index ≠ economy (forward-discounting).',
    'Futures: symmetrical obligation. Option: right with premium, capped loss. Underlying, strike, expiry. Need direction and time.',
    'Mutual fund: Trust (1882), AMC, units, NAV once a day, TER capped by SEBI. ETF: passive, listed, live price.',
    'ADR (US), GDR (global), IDR (foreign firm in India). P-Notes = ODIs; UBO disclosure 2016-2017.',
]

c.mcq = [
    {'q': 'Which of these is a money market instrument?', 'options': ['Equity share', 'Debenture of 5 years', 'Treasury Bill', 'Preference share'], 'answer': 2, 'explain': 'Money market contracts are short-term debt (under 1 year). Equity is long-term by nature.'},
    {'q': 'Cash Management Bills have a maturity of…', 'options': ['7 to 15 days', '91 days', '182 days', '364 days'], 'answer': 0, 'explain': 'T-bills are 91, 182 and 364 days; CMBs 7 to 15 days. Only the Centre issues them.'},
    {'q': 'State governments meet short-term mismatches through…', 'options': ['T-bills', 'CMBs', 'Ways and Means Advances from RBI', 'Commercial paper'], 'answer': 2, 'explain': 'Only the Centre issues T-bills and CMBs.'},
    {'q': 'Which of the following is NOT an AIFI that can issue Commercial Paper per the handout?', 'options': ['NABARD', 'SIDBI', 'EXIM Bank', 'RBI'], 'answer': 3, 'explain': 'The five are NABARD, NHB, SIDBI, EXIM Bank and NaBFID.'},
    {'q': 'In an Offer for Sale (OFS), the company receives…', 'options': ['the full amount', 'half of the amount', 'nothing', 'only the premium'], 'answer': 2, 'explain': 'Existing owners sell to the public; it is a secondary market sale.'},
    {'q': 'A Draft Red Herring Prospectus differs from the RHP because it…', 'options': ['has no valuation or final price', 'has final price band', 'is filed with RBI', 'is only for FPO'], 'answer': 0, 'explain': 'Once approved and the price band finalised it becomes the RHP.'},
    {'q': 'ASBA means…', 'options': ['a bank debits your money at application', 'the amount is blocked in your account, not debited, until allotment', 'cheques are sent physically', 'shares are issued free'], 'answer': 1, 'explain': 'You keep earning savings interest; refunds are unblocked if not allotted.'},
    {'q': 'The mechanism by which the clearing house becomes buyer to every seller and seller to every buyer is…', 'options': ['Novation', 'Green shoe', 'Rebalancing', 'Hedging'], 'answer': 0, 'explain': 'Novation removes counterparty risk. Pre-funding is the other pillar.'},
    {'q': 'NSDL and CDSL were created under the…', 'options': ['SEBI Act 1992', 'Companies Act 2013', 'Depositories Act, 1996', 'Securities Contracts Act 1956'], 'answer': 2, 'explain': 'Per the handout: the Depositories Act of 1996 followed the 1992 scam.'},
    {'q': 'A portfolio with beta 1.5 is…', 'options': ['50% less volatile than the benchmark', '50% more volatile than the benchmark', 'equal to the benchmark', 'giving 50% alpha'], 'answer': 1, 'explain': 'Beta 1 moves exactly with the benchmark.'},
    {'q': 'The Nifty 50 has a base value and base year of…', 'options': ['100 and 1979', '1000 and 1995', '1000 and 1979', '100 and 1995'], 'answer': 1, 'explain': 'Sensex: 30 companies, 100, 1979.'},
    {'q': 'In an options contract, the buyer’s maximum loss is…', 'options': ['unlimited', 'the strike price', 'the premium paid', 'zero'], 'answer': 2, 'explain': 'The buyer has the right, not the obligation. Futures have symmetrical risk.'},
    {'q': 'The NAV of a mutual fund is…', 'options': ['updated every second', 'computed once a day at the end of the day', 'decided by the stock exchange', 'fixed at ₹10'], 'answer': 1, 'explain': 'Mutual fund units are bought from and sold to the AMC; ETFs trade live on exchanges.'},
    {'q': 'An IDR is issued by…', 'options': ['an Indian company in the US', 'a foreign company to raise rupees in India', 'an Indian company in Europe', 'RBI'], 'answer': 1, 'explain': 'ADR and GDR are Indian shares abroad; IDR is the reverse.'},
    {'q': 'SEBI’s 2016-2017 rule for P-Notes required FIIs to disclose…', 'options': ['their profits', 'the Ultimate Beneficial Owner on request', 'their tax returns', 'the underlying price'], 'answer': 1, 'explain': 'P-Notes (ODIs) were used to round-trip black money; UBO disclosure ended the anonymity.'},
]
for q in c.mcq:
    q.pop('explanation', None)

c.mains = [
    ('Distinguish the money market from the capital market. Explain the instruments of the money market.',
     'The money market is short-term debt for working capital; the capital market is long-term for fixed capital.',
     ['Under 1 year, debt, near money, usually unsecured.', 'T-bills (91/182/364 days), CMBs (7-15 days): only the Centre; WMA for States.', 'CP: investment-grade, 5 AIFIs. CoD: tradable bank deposit.', 'Capital market: equity and debt over 1 year.'],
     'The money market keeps the economy’s plumbing liquid.'),
    ('Explain how a company raises capital and the process of an IPO. Why should investors read an OFS differently?',
     'Companies raise capital through equity and debt at successive stages of growth.',
     ['Angel, VC/PE, investment banks, public issue.', 'IPO process: lead manager and underwriter, DRHP to RHP, ASBA, cut-off, green shoe, demat allotment.', 'Primary versus secondary market.', 'In an OFS the company receives zero: it is early investors cashing out.'],
     'Read the size of the fresh issue, not the headline.'),
    ('Discuss the role of the stock exchange, clearing house and depositories in building trust in the market.',
     'A stock market is an institutional solution to anonymous strangers trusting each other with money.',
     ['Exchange: trust, convenience and price discovery.', 'Clearing house: pre-funding and novation remove counterparty risk.', 'Depositories Act 1996, NSDL and CDSL ended physical fraud after the 1992 scam.', 'Settlement shortened to T+1 and moving to T+0.'],
     'Trust is the product that markets sell.'),
    ('Why is the stock market not a reliable indicator of the health of the economy?',
     'Indices reflect a weighted average of a few large listed firms.',
     ['Nifty 50 excludes MSMEs, agriculture, unemployment, poverty.', 'COVID: record highs while GDP fell, as large firms captured share.', 'Forward-discounting: prices reflect expectations about the future.', 'Constituents tend to do well when the economy does, but there is no guarantee.'],
     'The economy mirrors the past; the market bets on the future.'),
    ('Differentiate futures and options. Why were derivatives designed, and why do retail traders lose?',
     'Both derive their value from an underlying asset.',
     ['Futures: symmetrical obligation; options: right with a capped loss (premium).', 'Underlying, strike, expiry, premium.', 'Designed for hedging by institutions.', 'Retail: leverage, need to be right on direction and time; 99% lose per the handout.'],
     'Derivatives are insurance in the hands of institutions and lottery tickets for retail.'),
]

c.cards = [
    ('Money market maturity?', 'Under 1 year; debt contracts only.'),
    ('Why “near money”?', 'Very liquid, low risk, low interest.'),
    ('Money market purpose?', 'Working capital and short-term liquidity.'),
    ('Capital market purpose?', 'Fixed capital formation.'),
    ('T-bill maturities?', '91, 182 and 364 days.'),
    ('CMB maturity?', '7 to 15 days.'),
    ('T-bill pricing?', 'Zero coupon; sold at discount, redeemed at par.'),
    ('Who issues T-bills and CMBs?', 'Only the Centre.'),
    ('How do States cover short-term gaps?', 'Ways and Means Advances from RBI.'),
    ('CP eligibility?', 'Rating above SEBI’s minimum investment grade.'),
    ('Five AIFIs allowed to issue CP?', 'NABARD, NHB, SIDBI, EXIM Bank, NaBFID.'),
    ('CoD?', 'Tradable short-term bank deposit certificate.'),
    ('OTC contract examples?', 'Loans, debentures, preference shares.'),
    ('Standardised contract examples?', 'Bonds, common equity.'),
    ('Spot (CNC) contract?', 'Settled on the spot: cash and carry.'),
    ('Underlying, strike, maturity?', 'The asset; the agreed price; the delivery date.'),
    ('Derivative?', 'A contract whose value derives from an underlying (a betting slip).'),
    ('Authorised vs paid-up capital?', 'Total shares allowed vs shares actually issued.'),
    ('Sweat equity?', 'Shares given to employees for contribution.'),
    ('Primary market?', 'Company issues new shares.'),
    ('Secondary market?', 'Investors trade among themselves; company uninvolved.'),
    ('Preference shares?', 'Fixed dividend first; capital first on bankruptcy.'),
    ('IPO/FPO vs OFS?', 'Company raises capital vs existing owners sell (company gets zero).'),
    ('Underwriter?', 'Promises to buy unsold shares.'),
    ('DRHP vs RHP?', 'Draft with no valuation vs final with price band.'),
    ('ASBA?', 'Application Supported by Blocked Amount.'),
    ('Green shoe option?', 'Over-allotment to stabilise price after listing.'),
    ('Oversubscription?', 'Demand exceeds supply.'),
    ('BSE origin?', 'Banyan tree gathering, Mumbai, 1875.'),
    ('Exchange’s three functions?', 'Trust, convenience, price discovery.'),
    ('Clearing house tools?', 'Pre-funding and novation.'),
    ('Novation?', 'CH becomes buyer to every seller and seller to every buyer.'),
    ('NSDL and CDSL?', 'Depositories created after the Depositories Act 1996.'),
    ('Why demat?', 'Physical paper fraud: 14-day settlement, 1992 scam.'),
    ('Settlement cycle now?', 'T+1, moving to T+0.'),
    ('IRR / XIRR?', 'Return on cash flows over time.'),
    ('Alpha?', 'Excess return over the benchmark.'),
    ('Beta?', 'Volatility relative to the benchmark.'),
    ('Sensex facts?', '30 companies, base 100, 1979.'),
    ('Nifty facts?', '50 companies, base 1000, 1995.'),
    ('Index rebalancing?', 'About every 6 months.'),
    ('Index weights based on?', 'Free-float market capitalisation.'),
    ('Forward-discounting?', 'Stock market prices expected future earnings.'),
    ('Futures risk?', 'Symmetrical; obligation for both.'),
    ('Option premium?', 'Price paid for the right; maximum loss for the buyer.'),
    ('Derivatives need what to win?', 'Direction and time.'),
    ('Mutual fund legal form?', 'Trust under Indian Trusts Act, 1882.'),
    ('AMC?', 'Asset Management Company that runs the schemes.'),
    ('NAV formula?', '(Assets − liabilities and expenses) ÷ units.'),
    ('TER?', 'Total Expense Ratio, capped by SEBI.'),
    ('ETF vs MF?', 'ETF is passive and listed (live price); MF NAV once a day via AMC.'),
    ('ADR, GDR, IDR?', 'Indian shares in the US; in global markets; foreign shares in India.'),
    ('P-Notes?', 'Offshore Derivative Instruments (ODIs); used for round-tripping.'),
    ('UBO rule?', 'SEBI 2016-2017: disclose the Ultimate Beneficial Owner.'),
]
c.summary = 'Money market versus capital market, T-bills, CMBs, CP and CoD, primary and secondary markets, IPO and OFS, clearing house and depositories, alpha and beta, Nifty and Sensex, market versus economy, futures versus options, mutual funds and ETFs, ADR, GDR, IDR and P-Notes. No PYQs quoted.'
