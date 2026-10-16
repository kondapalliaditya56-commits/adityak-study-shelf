from lib import Ch

c = Ch(5, 'National Income Accounting: GDP, GVA, GNP and Alternatives',
       'Economy · GS Foundation · Chapter 5',
       [('hb', 'Handout only: no class slides'), ('', 'Handout pages 1-36'), ('', '3 Prelims PYQs quoted')],
       'The circular flow of income and the multi-sectoral model, the three approaches (income, expenditure, production), what GDP means word by word, economic territory, GNP and NFIA, the GVA method, nominal versus real GDP and the base year, market price versus basic price versus factor cost, how India estimates GDP (SNA 2008, MCA-21, labour input, the 2022-23 base year), the limitations of GDP, HDI and the other alternatives, and the full family of national-income measures.')

c.sec('Exam lens: priority and PYQs', 'exam-lens-priority-and-pyqs')
c.call('alert', 'Source note', ['**Handout only.** No class slides and no teacher ink. The handout ends with **3 Prelims PYQs** (2018, 2015, 2015). **Mains PYQs: none quoted in the material.** This is the longest conceptual chapter so far and the formula chapter of the book.'])
c.table('Prelims PYQs quoted in the handout', ['Year', 'What was asked', 'Answer in handout', 'Where covered / trap'], [
    ['2018', 'Increase in absolute and per capita real GNP do not connote a higher level of development, if…', '(c) poverty and unemployment increase', 'Section 11 (limitations of GDP: inequality, well-being) and Chapters 1 and 3'],
    ['2015', 'A decrease in the tax-to-GDP ratio indicates: 1. slowing economic growth rates 2. less equitable distribution of national income', '(a) 1 only', 'Handout gives only the answer. Statement 2 is the trap'],
    ['2015', 'Real GDP growth has steadily increased in the last decade? GDP at market prices (in rupees) has steadily increased in the last decade?', '(b) 2 only', 'Section 8: nominal GDP rises with prices; real growth does not rise steadily'],
], rowhead=False)
c.table('What the handout stresses', ['Signal in the handout', 'Where', 'Why it matters'], [
    ['A = B = C: income, production and expenditure are equal over a year (dynamic equilibrium)', 'Sections 2-3', 'The base of all three approaches'],
    ['**GDP = GVA + net product taxes;** GVA is at basic price', 'Sections 7 and 9', 'Appears again as a “headline” formula'],
    ['MP, BP and FC: product taxes versus production taxes', 'Section 9', 'The handout builds this carefully: volume-based versus lump-sum'],
    ['Production approach is given primacy; “discrepancy” balances the expenditure side', 'Section 10', 'Statement-type question'],
    ['**2022-23 new base year; double deflation; SUT** (early 2026 changes)', 'Section 10', 'Current-affairs hook inside the handout'],
    ['Eight alternatives to GDP, each with one defining feature', 'Section 12', 'Match-the-pair questions'],
])
c.call('key', 'What to prepare', [
    '**Prelims hooks:** the A-B-C identity; injections (I, X, G) and leakages (S, T, M); AD = C + G + I + X − M; GDP terms (total, value, final, produced, territory, time); GNP = GDP + NFIA; GVA; nominal versus real; base-year properties; MP = BP + product taxes − product subsidies; FC = BP − production taxes + production subsidies; the eight GVA sectors; MCA-21; labour input method; HDI components; the eight alternatives; NI = NNP at factor cost; PI and PDI.',
    '**Mains hooks:** why GDP is still king despite its limits; limitations (merit versus demerit, inequality, unpriced work, externalities, informality, inflation); how the informal sector is estimated; why the base year matters; what the 2022-23 revision changes.',
    '**Closing idea:** GDP is a good thermometer of income and a poor judge of well-being, which is why we pair it with other indices.'])

c.sec('1 · What national income accounting is for')
c.p('**Accounting** is the systematic recording, classification and summarising of incomes. **National** sets the boundary: either the income earned **in** the nation (irrespective of who earns it) or the income earned **by** the nationals (irrespective of where). **Income** is strictly the reward paid for the **Factors of Production:** rent for land, wages for labour, interest for capital, profit for entrepreneurship.')
c.p('Without national accounts the government, the central bank and citizens are “driving blind”: NIA is the economy’s **dashboard.** It cannot be measured by asking 1.4 billion people what they earn (people lie, forget, and much of the economy is informal), so the handout builds the idea in three steps: a **basic model** (the “tree’s shadow”), an **advanced model** (dropping unrealistic assumptions) and the **real world** (the methods used in India today).')

c.sec('2 · Circular flow of income model (CFIM)')
c.p('Two entities only: **households** (own all factors of production and supply them) and **firms** (use them to produce and sell goods back).')
c.fig('eco-cfim.jpg', 'The Circular Flow of Income Model. Assumptions: no savings, no government, no foreign trade. Households give factors of production (land, labour, capital, enterprise) to firms (real flow); firms pay incomes (A); households spend (C) to buy goods (B). A = B = C.')
c.table('The three flows', ['Label', 'Meaning'], [
    ['**A** · total incomes', 'Total payments by firms to households for factors: wages + rent + interest + profit'],
    ['**B** · total production', 'Total value of all goods and services produced by firms'],
    ['**C** · total expenditure', 'Total money spent by households on those goods'],
], rowhead=True)
c.p('**CFIM states A = B = C.** Households spend all they earn (A = C); firms keep no inventory (B = C); firms pay out all expenditure received as factor incomes (whatever is left is profit for the entrepreneurial households).')

c.sec('3 · Multi-sectoral model (MSM): injections and leakages')
c.p('CFIM assumes no saving, no inventory, no government, no foreign trade and no spending on capital goods. The MSM drops all of these and still arrives at **A = B = C**, but as a **dynamic equilibrium:** the three are always changing, may not be equal at a point in time, but readjust towards each other. “**A will always chase C, and B will always chase A.**” They are **flow variables** measured over a period (usually a year).')
c.fig('eco-msm.jpg', 'The Multi-Sectoral Model (open economy). Households, firms, government, banks and foreigners. Leakages (dotted): savings, taxes, imports. Injections (solid): investment, government expenditure, exports.')
c.table('Leakages and injections', ['', 'Items', 'Effect'], [
    ['**Leakages** (pull money out)', 'Savings (S), taxes (T), imports (M)', 'A, B or C shrinks'],
    ['**Injections** (pump money in)', 'Investment (I), exports (X), government expenditure (G)', 'A, B or C expands'],
], rowhead=True)
c.ul([
    '**Saving example:** households save, spend less; firms build inventory, produce less next cycle, use fewer factors, pay less income: C falls, then B, then A.',
    '**Government** is both a special household and a special firm. Spending on goods raises C, then B, then A. Hiring teachers and soldiers raises A, then C, then B. Savings go through banks to firms as investment, again lifting B, C and A. Export demand does the same.',
    '**The economy grows only if injections exceed leakages.** Over an accounting year the adjustments settle and A = B = C.'])

c.sec('4 · The three approaches to measuring national income')
c.table('Three ways to measure the same total', ['Approach', 'Formula', 'What it counts'], [
    ['**Income (A)**', 'TI = R + P + W + Int', 'All payments to factors of production in the domestic territory'],
    ['**Expenditure (C)**', 'TI = AD = C + G + I + X − M', 'Expenditure **received by domestic firms.** Total spending is C + G + I + X, but each of C, G and I has a domestic and a foreign part; subtract the foreign parts (total imports M) to get what domestic firms received'],
    ['**Production (B)**', 'TI = GDP = Σ VAᵢ = GVA', 'Total value of final goods and services produced in a year'],
], rowhead=True)
c.h3('GDP word by word')
c.table('Total value of all final goods and services produced in an economy over a given time', ['Word', 'Meaning in the handout'], [
    ['**Total**', 'GDP is an aggregate: indifferent to merit versus demerit goods and to who owns the factors'],
    ['**Value**', 'Not “worth” (which varies by person) but the objectively assessed **price** (transaction value). So only goods and services that have a price count: a parent cooking dinner for a child is excluded'],
    ['**Final**', 'Only final goods. Their value already includes intermediates, so counting both is **double counting**'],
    ['**Produced**', 'Counted in the year of **production,** not when or how often sold. Second-hand sales are not counted again, but new services (brokerage, registration, repair) are'],
    ['**Economic territory**', 'Production inside the territory, **irrespective of who produces** (residents or foreigners)'],
    ['**Given period**', 'A flow variable: a quarter or a year'],
], rowhead=True)
c.call('note', 'The land question', 'The handout asks: if you buy land worth ₹10 crore in Delhi, what is the effect on GDP? It leaves the question open. By its own rules (“production matters, not the sale”) the purchase itself adds nothing; services such as brokerage and registration would.')

c.sec('5 · Economic territory and GNP')
c.p('The economic territory (ET) mostly coincides with the political territory, **except:**')
c.table('Where economic territory differs from the map', ['Counts as India’s ET', 'Does NOT count as India’s ET'], [
    ['**Enclaves abroad:** Indian embassy in Washington, consulate in Dubai, research bases in Antarctica (Bharati, Maitri). Salaries of Indian staff are Indian GDP', '**Foreign enclaves in India:** the American embassy in Chanakyapuri, a Japanese consulate in Mumbai: part of that country’s GDP'],
    ['**Ships and aircraft in international transit:** an Air India flight over the Atlantic, a Shipping Corporation of India vessel in the Mediterranean', '**International organisations in India:** UN, WHO, IMF offices are “extraterritorial”; their core production is excluded'],
    ['**Fishing vessels and oil rigs in international waters** where India has exclusive exploitation rights (the EEZ)', ''],
], rowhead=False)
c.p('**GNP** is the total value of final goods and services produced by the **nationals** of a country (residents), wherever they are. The handout writes **GNP = GDP + C − B** where C is output by Indians abroad and B is output by foreigners in India, i.e. **GNP = GDP + NFIA** (net factor income from abroad). If nationals produce more outside than foreigners produce inside, GNP exceeds GDP.')
c.call('alert', 'Handout alert: letters reused', 'In this section the handout reuses the letters B and C for “output by foreigners in India” and “output by Indians abroad”, while elsewhere B and C are the production and expenditure flows. **Rule for the exam hall:** write it as **GNP = GDP + NFIA = GDP + (income earned by Indians abroad − income earned by foreigners in India).**')

c.sec('6 · The GVA method: why GDP is counted by value added')
c.p('Using GDP = Σ Pᵢ·Qᵢ over final goods needs final goods to be separated from intermediates, which is nearly impossible: every producer sees their output as final. Instead, **each producer’s value added** is summed: **VAᵢ = output value − input value.** The total is **GVA, which equals GDP.**')
c.table('The handout’s wheat-atta-bread-sandwich economy (all in rupees)', ['Producer', 'Output', 'Inputs bought', 'Value added'], [
    ['Farmers (wheat)', '1,00,000', '0', '1,00,000'], ['Atta makers', '1,00,000', '60,000 wheat', '40,000'],
    ['Bread makers', '1,00,000', '60,000 atta', '40,000'], ['Sandwich makers', '1,00,000', '60,000 bread', '40,000'],
    ['**GDP = GVA**', '', '', '**2,20,000**']], rowhead=True)
c.p('Final goods check: wheat 40k + atta 40k + bread 40k + sandwiches 1L = **₹2.2 lakh.** The two methods agree. The proof: the value of any final good equals the total value added by all producers with respect to that good; summing over all final goods gives the total value added by all producers.')

c.sec('7 · Nominal and real GDP; the base year')
c.table('Valuing output at different prices', ['', 'Nominal GDP', 'Real GDP'], [
    ['**Formula**', 'P(current year) · Q(current year)', 'Q(current year) · P(constant base-year price)'],
    ['**Prices**', 'Current prices', 'Constant (e.g. previous year or a base year)'],
    ['**Use**', 'Size of the economy at today’s prices', 'Fair comparison of output across years, removing price changes. **Economic growth = % change in real GDP**'],
], rowhead=True)
c.p('A **base year** provides the constant prices. The handout says the choice dictates the officially measured growth rate. A good base year has two properties:')
c.ul([
    '**Structurally similar** to the present (the “time machine” problem): the basket produced and consumed should resemble today’s. Using 1980 would make telecom impossible to price (no smartphones or 5G then). So it should be as recent as possible, usually updated every **5 to 10 years.**',
    '**Stable** (avoiding the **base effect**): if 2020, a Covid year, were the base, 2021’s recovery would look like 20-25% growth. A base year must be free of droughts, floods, pandemics, wars and policy shocks such as demonetisation. “It should be a boring year.”'])

c.sec('8 · Market price, basic price and factor cost')
c.p('Because of government taxes and subsidies, what the buyer pays differs from what the seller receives. Output can be valued at three prices:')
c.table('Three prices', ['Price', 'Meaning', 'Relation'], [
    ['**Market price (MP)**', 'What the **buyer pays:** the sticker price. Closer to the consumer', 'MP = BP + product taxes − product subsidies'],
    ['**Basic price (BP)**', 'What the seller actually wants to receive and keep: the “factory gate price”', 'BP = MP − product taxes + product subsidies'],
    ['**Factor cost (FC)**', 'The cost attributable to the factors of production: what workers, landowners and capitalists take home. Closer to the producer', 'FC = BP − production taxes + production subsidies'],
], rowhead=True)
c.table('Product versus production taxes and subsidies', ['', 'Product T and S', 'Production T and S'], [
    ['**Basis**', 'Levied or given on a **quantity** basis (per unit, per kg, per litre)', 'Independent of the volume of production: **lump sum**'],
    ['**Examples**', 'GST (₹100 good + 18% GST = ₹118 market price, seller keeps ₹100); subsidies on LPG and fertilisers', 'Land revenue, stamp duties, a municipal factory licence fee; help for setting up in a backward region or for small-scale industry'],
], rowhead=True)
c.call('teacher', 'GDP at the three prices', [
    '**GDP(BP) = GDP(MP) − product taxes + product subsidies,** so **GDP(MP) = GDP(BP) + product taxes − product subsidies.**',
    '**GDP(FC) = GDP(BP) − production taxes + production subsidies.**',
    'Headline form: **GDP = GVA + net product taxes** (GDP at market prices = GVA at basic prices + product taxes − product subsidies).'])
c.call('note', 'The earlier simple version', 'The handout first introduces GDP(MP) = GDP(FC) + total indirect taxes − subsidies and says this was “nothing wrong” but incomplete: factor cost needs the production-level taxes and subsidies removed as well. **Rule for the exam hall:** use the BP step.')

c.sec('9 · How India estimates GDP')
c.flow([
    ('Step 1 · The global rulebook: SNA 2008', 'UN System of National Accounts. India overhauled its GDP methodology in **2015** to align with it, so that numbers are comparable across years and countries'),
    ('Step 2 · Slice the economy', 'NSO under MoSPI defines the economic territory and splits the economy into agriculture, industry and services, then **8 official GVA sectors**'),
    ('Step 3 · Choose the tool for each sector', 'Different methods for agriculture, organised corporate and unorganised sectors (below)'),
    ('Step 4 · Extrapolate', 'Scale the sample up to the sub-sector using secondary data and assumptions that are reasonable, standardised and replicable'),
    ('Step 5 · From GVA to headline GDP', 'Add the 8 sectors to get **GVA at basic prices,** then **GDP(MP) = GVA(BP) + product taxes − product subsidies**'),
    ('Step 6 · Reality check', 'Production-method GDP and expenditure-method AD rarely match (different data sources). The NSO gives **primacy to the production method** and adds a balancing **“discrepancy”** to the expenditure side', 'good'),
], 'How the NSO estimates GDP')
c.table('The eight GVA sectors', ['#', 'Sector'], [
    ['1', 'Agriculture, forestry and fishing'], ['2', 'Mining and quarrying'], ['3', 'Manufacturing'], ['4', 'Electricity, gas, water supply and other utility services'],
    ['5', 'Construction'], ['6', 'Trade, hotels, transport, communication and broadcasting'], ['7', 'Financial, real estate and professional services'], ['8', 'Public administration, defence and other services']], rowhead=False)
c.table('Method by sector', ['Sector', 'Method', 'Detail'], [
    ['**Agriculture**', 'Production method', 'Satellite data give **total sown area;** multiply by **yield per hectare;** multiply by mandi prices to get gross value'],
    ['**Organised corporate**', 'Value added method using **MCA-21** (Ministry of Corporate Affairs database)', 'Every registered company uploads audited balance sheets and P&L; value added = revenue − intermediate expenses. The shift to MCA-21 in **2015** replaced the old **Annual Survey of Industries (ASI) establishment approach** (counting factory output) with an **enterprise approach** that also captures R&D labs, marketing and headquarters'],
    ['**Unorganised**', '**Labour input method** (Effective Labour Input)', 'Employment surveys (e.g. PLFS) give the **headcount;** a smaller survey gives **value added per worker;** multiply. Example: 10 lakh e-rickshaw drivers × ₹1.8 lakh a year = ₹18,000 crore'],
], rowhead=True)
c.p('The informal sector is estimated at **60-90%** of the economy (the handout’s range).')
c.call('example', 'Extrapolation by “blow-up factor” (the Rajendra Nagar coaching example)', [
    'Two sample firms have a combined value added of ₹100 crore (from MCA-21). The NSO needs their share of the market. A survey of 1,000 students finds 400 study at the two firms, so they are 40% of the market.',
    '**Total output = 100 crore ÷ 40% = ₹250 crore.** If they held 10% it would be ₹1,000 crore; at 50%, ₹200 crore. The same issue arises with Airtel, Jio and Vodafone: Airtel’s rent and financial income must not be counted as telecom value added. This is why SNA 2008 rules are needed.'])
c.call('teacher', 'Recent changes (early 2026): the new base year 2022-23', [
    '**New base year 2022-23,** seen as a “normal” post-Covid, post-GST stabilisation year reflecting a service-heavy, digital economy. The older 2011-12 had become distant.',
    '**Double deflation** adopted for manufacturing and agriculture: inflation stripped separately from inputs and outputs (earlier: single deflation of output only).',
    '**High-frequency data** directly integrated: GST collections, e-Vahan vehicle registrations, digital transactions.',
    '**Supply and Use Tables (SUT)** reconcile the production and expenditure methods, reducing discrepancies.'])

c.sec('10 · Limitations of GDP')
c.table('Why GDP only approximates well-being', ['Limitation', 'Handout’s illustration'], [
    ['**Aggregate: ignores composition**', 'Country A produces ₹1,000 crore of schools, hospitals and clean energy; Country B ₹1,000 crore of assault weapons, cigarettes and casinos. Same GDP, very different well-being (merit versus demerit)'],
    ['**Ignores inequality**', '10 people, GDP ₹100, per capita ₹10 looks fine, but one holds ₹99 and nine share ₹1'],
    ['**Counts only priced goods and services**', 'Hire a maid and GDP rises; the family does it and it does not. India has large non-monetised sectors (subsistence farming, household care), so well-being is understated'],
    ['**Externalities**', 'Cutting a forest raises GDP; a polluting factory raises GDP; the inhalers bought for the resulting asthma raise GDP too'],
    ['**Hard to estimate with a large informal sector and black money**', 'Estimates less accurate; comparison unfair'],
    ['**Valued at price**', 'Prices can rise from inflation, higher taxes or lower subsidies, which do not improve well-being'],
], rowhead=True)

c.sec('11 · Alternatives to GDP')
c.table('The eight alternatives', ['Index', 'What it is'], [
    ['**1 · HDI**', 'Proposed by Amartya Sen and Mahbub-ul-Haq to UNDP (the handout says **1980**), reported in the Human Development Reports. **Composite of three dimensions:** a long and healthy life (**life expectancy at birth**), knowledge (**expected years of schooling** and **mean years of schooling** for ages 25+), decent standard of living (**GNI per capita** in PPP international dollars). Groups: low, medium, high, very high. **India is in the medium category**'],
    ['**2 · IHDI** (Inequality-adjusted HDI)', 'HDI “discounted” for inequality in health, education and income. If perfectly equal, HDI = IHDI'],
    ['**3 · GDI** (Gender Development Index)', 'Gender gap in HDI: HDI of women compared with that of men'],
    ['**4 · GII** (Gender Inequality Index)', 'Loss of achievement from gender inequality: reproductive health (maternal mortality), empowerment (women in parliament), labour-market participation'],
    ['**5 · GPI** (Genuine Progress Indicator)', 'GDP **plus** unpaid volunteer and household work, **minus** costs of pollution, crime and resource depletion'],
    ['**6 · GNH** (Gross National Happiness)', 'Pioneered by **Bhutan;** rejects pure materialism; **nine domains** including psychological well-being, cultural resilience, community vitality, ecological diversity'],
    ['**7 · Green GDP**', 'GDP minus the monetary value of environmental degradation and depletion of natural capital'],
    ['**8 · GHI** (Global Hunger Index)', '100-point severity scale (**0 best, 100 worst**). Four indicators under three dimensions: **inadequate food supply; child undernutrition** (wasting and stunting in under-fives); **child mortality**'],
], rowhead=True)
c.call('teacher', 'Why GDP is still “king”', ['**(i) Standardisation and objectivity:** built on UN SNA 2008, calculated the same way everywhere; alternatives rely on subjective assumptions (how do you value “happiness”?).', '**(ii) Data availability:** GDP is calculated regularly by almost every country, and can be done **quarterly,** a “real-time heartbeat monitor”.'])
c.call('alert', 'Handout alert: the HDI year', 'The handout says Sen and Mahbub-ul-Haq proposed the HDI to UNDP in **1980.** The handout also says the HDR has measured it “since then”. **Rule for the exam hall:** treat the year as a detail to verify against your standard reference before quoting; the question is more likely to test the three dimensions.')

c.sec('12 · The family of national income measures')
c.table('Aggregate measures', ['Measure', 'Formula'], [
    ['Income approach', 'TI = R + P + W + Int'], ['Expenditure approach', 'TI = AD = C + G + I + X − M'], ['Production approach', 'TI = GDP = Σ VAᵢ = GVA'],
    ['GNP (income of nationals)', 'GNP = GDP + NFIA'], ['Income from the use side', 'TI = C + S + T (consumption, savings, taxes)']], rowhead=True)
c.table('Average, headline and special measures', ['Group', 'Measure', 'Meaning'], [
    ['**Average**', '**Per capita income (PCI)**', 'GDP ÷ mid-year population'],
    ['', '**GNI per capita**', 'GNP ÷ population, with NFIA = income earned by Indians outside India − income earned by foreigners in India'],
    ['**Headline**', '**GDP**', 'GDP(MP), i.e. nominal GDP'],
    ['', '**GVA**', 'GVA(BP); GDP(MP) = GDP(BP) + product taxes − product subsidies; **GDP = GVA + net indirect taxes**'],
    ['', '**Economic growth**', '% change in **real** GDP'],
    ['', '**National Income (NI)**', '**NI = NNP at factor cost = GNP(MP) − indirect taxes + subsidies − depreciation**'],
    ['**Special**', '**Personal income (PI)**', 'Household income. **PI = NI − incomes not paid to households + other transfers to households.** Subtract corporate taxes (CT), undistributed profits (UP) and net interest paid by households; add transfers by firms or government to households (bonuses, welfare transfers, scholarships)'],
    ['', '**Personal disposable income (PDI)**', '**PDI = PI − personal taxes** (income, property, professional). PDI = consumption + savings'],
], rowhead=False)
c.call('note', 'Transfers', 'Transfers (for example money from a brother in Dubai) are **not income;** they are only a transfer of the right to spend income earned by someone else. Counting them in GDP would double count. But when the money is spent, it becomes consumption (C), and the circular flow lifts B and A.')

c.mm = ('National income', [
    ('Circular flow', [('CFIM: A = B = C', 'no S, G, trade'), ('MSM: dynamic equilibrium', 'A chases C, B chases A'), ('Leakages S, T, M', None), ('Injections I, X, G', None)]),
    ('Three approaches', [('Income: R + W + P + Int', None), ('Expenditure: C + G + I + X − M', None), ('Production: Σ value added', None)]),
    ('GDP and GNP', [('Final, produced, priced, in territory', None), ('Enclaves, ships, rigs', None), ('GNP = GDP + NFIA', None)]),
    ('GVA method', [('VA = output − inputs', None), ('GVA = GDP', None), ('Wheat example: ₹2.2 lakh', None)]),
    ('Prices', [('Nominal vs real', None), ('Base year: similar and stable', 'base effect'), ('MP, BP, FC', 'product vs production taxes')]),
    ('Estimating in India', [('SNA 2008, MCA-21 (2015)', None), ('8 sectors', None), ('Labour input method', 'workers × VA/worker'), ('Base 2022-23, double deflation', None)]),
    ('Limits and alternatives', [('Composition, inequality, unpriced work', None), ('Externalities, informality, inflation', None), ('HDI, IHDI, GDI, GII, GPI, GNH, Green GDP, GHI', None)]),
    ('Measures', [('PCI, GNI per capita', None), ('NI = NNP at FC', None), ('PI and PDI', None)]),
])

c.timeline = [
    ('1980', 'HDI proposed by Sen and Mahbub-ul-Haq to UNDP (the handout’s date; see alert)', False),
    ('2008', 'SNA 2008 published by the UN', False),
    ('2011-12', 'Earlier base year for GDP (replaced by 2022-23)', False),
    ('2015', 'India overhauls GDP methodology to align with SNA 2008; shift to MCA-21 and the enterprise approach', True),
    ('2015', 'PYQs on real versus nominal GDP and the tax-to-GDP ratio', False),
    ('2018', 'PYQ: real GNP growth does not mean development if poverty and unemployment increase', False),
    ('2022-23', 'New base year introduced in early 2026; double deflation and SUT', True),
]

c.connects = [
    ('[Chapter 4: Basic Concepts](eco-ch04.html)', 'The handout calls this chapter the formal start after Chapter 4: final versus intermediate goods, GCF and depreciation (CFC for NDP and NNP) are used here.'),
    ('[Chapter 3: Unemployment](eco-ch03.html)', 'The SNA production boundary decides what counts as employment; the PLFS supplies the headcount for the labour input method.'),
    ('[Chapter 2: Inequality](eco-ch02.html)', 'GDP is blind to inequality; IHDI and the Gini carry the same idea. The handout refers back to “the inequality chapter” for the meaning of income.'),
    ('[Chapter 1: Poverty](eco-ch01.html)', 'The 2018 PYQ links real GNP to poverty and unemployment; HDI and GHI are well-being measures alongside poverty measures.'),
    ('GST and Budget handouts', 'Product taxes (GST) move GDP between basic and market prices; taxes and subsidies are the fiscal side of MP, BP and FC.'),
]

c.recall = [
    'NIA = dashboard. Income is the reward to factors: rent, wages, interest, profit.',
    'CFIM: A = B = C with no saving, government or trade. MSM: dynamic equilibrium; A chases C, B chases A.',
    'Leakages: S, T, M. Injections: I, X, G. Growth when injections exceed leakages.',
    'Income: R + W + P + Int. Expenditure: C + G + I + X − M. Production: GDP = Σ VA = GVA.',
    'GDP: total, value (price, priced only), final, produced, in territory, in a period.',
    'Territory: embassies abroad, ships and aircraft in transit, rigs in EEZ count; foreign embassies and UN offices in India do not.',
    'GNP = GDP + NFIA.',
    'GVA method: wheat economy gives ₹2.2 lakh either way.',
    'Nominal = current prices. Real = constant prices. Growth = change in real GDP. Base year: structurally similar and stable (avoid base effect).',
    'MP = BP + product taxes − product subsidies. FC = BP − production taxes + production subsidies. GDP = GVA + net product taxes.',
    'India: SNA 2008 (2015), 8 sectors, agriculture by area × yield × price, corporate by MCA-21, unorganised by labour input; production method has primacy; discrepancy balances.',
    '2022-23 base year, double deflation, GST and e-Vahan data, SUT.',
    'Limits: composition, inequality, unpriced work, externalities, informality, inflation. Alternatives: HDI, IHDI, GDI, GII, GPI, GNH, Green GDP, GHI.',
    'NI = NNP at FC = GNP(MP) − indirect taxes + subsidies − depreciation. PI = NI − CT − UP − net interest + transfers. PDI = PI − personal taxes.',
]

c.mcq = [
    {'q': 'Increase in absolute and per capita real GNP do not connote a higher level of economic development, if (2018)', 'options': ['industrial output fails to keep pace with agricultural output', 'agricultural output fails to keep pace with industrial output', 'poverty and unemployment increase', 'imports grow faster than exports'], 'answer': 2, 'explain': 'Handout answer: (c). Output measures ignore inequality and well-being.'},
    {'q': 'A decrease in the tax to GDP ratio of a country indicates which of the following? 1. Slowing economic growth rates 2. Less equitable distribution of national income (2015)', 'options': ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 'answer': 0, 'explain': 'Handout answer: (a). The handout prints only the answer.'},
    {'q': 'With reference to India economy: 1. The rate of growth of real GDP has steadily increased in the last decade. 2. The GDP at market prices (in rupees) has steadily increased in the last decade. (2015)', 'options': ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 'answer': 1, 'explain': 'Handout answer: (b). Nominal GDP rises with prices; real growth does not rise steadily.'},
    {'q': 'In the circular flow model, which of the following is a leakage?', 'options': ['Government expenditure', 'Exports', 'Imports', 'Business investment'], 'answer': 2, 'explanation': '', 'explain': 'Leakages are savings, taxes and imports. Injections are investment, exports and government expenditure.'},
    {'q': 'Total expenditure received by domestic firms equals…', 'options': ['C + G + I + X', 'C + G + I + X − M', 'C + S + T', 'GDP − NFIA'], 'answer': 1, 'explain': 'Remove the foreign part of C, G and I (total imports M).'},
    {'q': 'The embassy of India in Washington D.C. is, for GDP purposes, part of…', 'options': ['the USA’s economic territory', 'India’s economic territory', 'no country’s', 'the UN’s'], 'answer': 1, 'explain': 'Embassies and consulates abroad are the home country’s economic territory.'},
    {'q': 'UN office in India: its production is…', 'options': ['counted in India’s GDP', 'counted in the UN’s home country GDP', 'excluded from India’s GDP (extraterritorial)', 'counted in GNP only'], 'answer': 2, 'explain': 'International organisations do not belong to any single country’s territory.'},
    {'q': 'GNP equals…', 'options': ['GDP − NFIA', 'GDP + NFIA', 'GDP + net product taxes', 'GVA − depreciation'], 'answer': 1, 'explain': 'NFIA is income earned by Indians abroad minus income earned by foreigners in India.'},
    {'q': 'In the wheat-atta-bread-sandwich example, the GDP is…', 'options': ['₹1 lakh', '₹2.2 lakh', '₹4 lakh', '₹3.4 lakh'], 'answer': 1, 'explain': 'Value added 1L + 40k + 40k + 40k = 2.2L, matching the final goods sum.'},
    {'q': 'A base year should be…', 'options': ['as old as possible', 'structurally similar to today and stable', 'a year of high growth', 'a year of a recession'], 'answer': 1, 'explain': 'A shock year gives a misleading base effect.'},
    {'q': 'Basic price equals…', 'options': ['MP − product taxes + product subsidies', 'MP + product taxes − product subsidies', 'FC + production taxes', 'MP − production taxes'], 'answer': 0, 'explanation': '', 'explain': 'BP is what the seller keeps: strip product taxes, add back product subsidies.'},
    {'q': 'Land revenue and stamp duty paid by a factory are examples of…', 'options': ['product taxes', 'production taxes', 'subsidies', 'transfers'], 'answer': 1, 'explain': 'They are lump-sum, independent of the volume produced.'},
    {'q': 'For the unorganised sector, the NSO estimates GVA by…', 'options': ['MCA-21 balance sheets', 'satellite sown area × yield', 'total workers × value added per worker', 'GST collections only'], 'answer': 2, 'explain': 'The labour input method.'},
    {'q': 'The three dimensions of HDI are…', 'options': ['health, education and standard of living', 'income, inequality and gender', 'GDP, GNP and GNI', 'hunger, mortality and schooling'], 'answer': 0, 'explanation': '', 'explain': 'Long and healthy life, knowledge, decent standard of living.'},
]
for q in c.mcq:
    q.pop('explanation', None)

c.mains = [
    ('Explain the circular flow of income and show why income, production and expenditure are equal.',
     'The economy is a loop in which one party’s expenditure is another’s income.',
     ['CFIM: two sectors, A (incomes) = B (production) = C (expenditure) under no saving, inventory, government or trade.', 'MSM: drop the assumptions; leakages S, T, M and injections I, X, G; dynamic equilibrium.', 'Adjustment: C falls, then B, then A; government spending lifts C, B, A.', 'Over a year they settle: A = B = C.'],
     'The three ways of measuring national income are three views of one loop.'),
    ('Why is GDP calculated by the value-added method? Illustrate.',
     'Final and intermediate goods cannot be told apart at the point of production.',
     ['Every producer sees its output as final.', 'VA = output − inputs; GDP = Σ VA = GVA.', 'Wheat-atta-bread-sandwich: 1L + 40k + 40k + 40k = 2.2L.', 'Avoids double counting.'],
     'Add the value each producer adds, and the final total takes care of itself.'),
    ('Distinguish between market price, basic price and factor cost. How do they link GDP and GVA?',
     'The same output looks different to buyer, seller and the factors.',
     ['MP = BP + product taxes − product subsidies.', 'FC = BP − production taxes + production subsidies.', 'Product versus production: per-unit versus lump-sum.', 'GDP(MP) = GVA(BP) + net product taxes.'],
     'Taxes and subsidies sit between what you pay and what factors earn.'),
    ('How does India estimate GDP, including the informal sector? What has changed with the 2022-23 base year?',
     'India follows SNA 2008 and uses a different tool for each part of the economy.',
     ['8 GVA sectors; agriculture by sown area × yield × price.', 'Corporate sector by MCA-21; the 2015 switch to the enterprise approach.', 'Unorganised by labour input: headcount × value added per worker.', 'Extrapolation with a blow-up factor; production method primacy and a discrepancy.', '2022-23 base, double deflation, GST and e-Vahan data, SUT.'],
     'GDP in India is an estimate, made reliable by standard rules.'),
    ('Why do economists propose alternatives to GDP, and why does GDP still dominate?',
     'GDP measures income, which only approximates well-being.',
     ['Limitations: merit versus demerit, inequality, unpriced work, externalities, informality, inflation.', 'Alternatives: HDI, IHDI, GDI, GII, GPI, GNH, Green GDP, GHI.', 'GDP wins on standardisation and objectivity, and on regular data (quarterly).', 'Use GDP with the others.'],
     'GDP is the thermometer: indispensable but not a diagnosis.'),
]

c.cards = [
    ('What does “income” mean in national accounts?', 'Reward to factors of production: rent, wages, interest, profit.'),
    ('A, B, C in CFIM?', 'A incomes, B production, C expenditure; A = B = C.'),
    ('CFIM assumptions?', 'No saving, no inventory, no government, no foreign trade, no capital-goods spending.'),
    ('MSM equilibrium?', 'Dynamic: A chases C, B chases A.'),
    ('Leakages?', 'Savings, taxes, imports.'),
    ('Injections?', 'Investment, exports, government expenditure.'),
    ('When does the economy grow?', 'When injections exceed leakages.'),
    ('Expenditure approach formula?', 'AD = C + G + I + X − M.'),
    ('Income approach formula?', 'R + W + P + Int.'),
    ('Why “value” and not “worth”?', 'Value is the objective price; unpriced goods are excluded.'),
    ('Why only final goods?', 'To avoid double counting.'),
    ('Are second-hand goods counted again?', 'No; but brokerage, registration and repair services are.'),
    ('Indian embassy in Washington: whose GDP?', 'India’s.'),
    ('US embassy in Delhi: whose GDP?', 'The USA’s.'),
    ('UN office in India?', 'Extraterritorial; excluded from India’s GDP.'),
    ('GNP formula?', 'GDP + NFIA.'),
    ('NFIA?', 'Income earned by Indians abroad minus income earned by foreigners in India.'),
    ('VA of a producer?', 'Output value minus input value.'),
    ('GDP and GVA?', 'GDP = GVA = sum of value added by all producers.'),
    ('Nominal GDP?', 'Current-year output at current prices.'),
    ('Real GDP?', 'Current-year output at constant (base) prices.'),
    ('Economic growth?', '% change in real GDP.'),
    ('Base effect?', 'A depressed base year makes the next year’s growth look huge.'),
    ('Market price?', 'What the buyer pays.'),
    ('Basic price?', 'What the seller keeps: MP − product taxes + product subsidies.'),
    ('Factor cost?', 'BP − production taxes + production subsidies.'),
    ('Product versus production taxes?', 'Per-unit (GST) versus lump sum (land revenue, stamp duty).'),
    ('Headline GDP formula?', 'GDP(MP) = GVA(BP) + product taxes − product subsidies.'),
    ('Global rulebook for GDP?', 'SNA 2008 (UN); adopted in India in 2015.'),
    ('MCA-21?', 'Ministry of Corporate Affairs database of audited balance sheets; used for the corporate sector.'),
    ('Labour input method?', 'Total workers × value added per worker (unorganised sector).'),
    ('Which method has primacy in India?', 'The production method; a discrepancy is added to the expenditure side.'),
    ('New base year?', '2022-23 (early 2026), replacing 2011-12.'),
    ('Double deflation?', 'Strip inflation separately from inputs and outputs.'),
    ('HDI dimensions?', 'Long and healthy life, knowledge, decent standard of living.'),
    ('IHDI?', 'HDI discounted for inequality.'),
    ('GII looks at?', 'Maternal mortality, women in parliament, labour participation.'),
    ('GPI?', 'GDP plus unpaid work minus costs of pollution, crime and depletion.'),
    ('GNH domains?', 'Nine; pioneered by Bhutan.'),
    ('GHI scale?', '0 best, 100 worst; undernutrition, child mortality, food supply.'),
    ('National Income formula?', 'NNP at factor cost = GNP(MP) − indirect taxes + subsidies − depreciation.'),
    ('PI to PDI?', 'PDI = PI − personal taxes.'),
]
c.summary = 'Circular flow, the three approaches, GDP word by word, economic territory, GNP, the GVA method, nominal and real GDP, MP-BP-FC, how India estimates GDP (new 2022-23 base), limits of GDP, HDI and seven other alternatives, and PI/PDI. Three Prelims PYQs.'
