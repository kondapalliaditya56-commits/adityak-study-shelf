# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 5 (National Income Accounting). Facts come only from the handout text.
plain = idea in everyday words (memory aid); eg = the handout's own example; hook = one-line handle."""
TOP = {
 'sixty': [('One loop', 'income A = production B = expenditure C, in a year'),
           ('Three views', 'income R+P+W+Int; expenditure C+G+I+X−M; production ΣVA = GVA'),
           ('GDP', 'final goods only, produced this year, inside the territory, at a price'),
           ('Prices', 'nominal vs real; MP = BP + product taxes − subsidies; FC = BP − production taxes'),
           ('India', 'eight GVA sectors, three methods by sector; base 2022-23, double deflation'),
           ('Beyond GDP', 'six limits; HDI, IHDI, GDI, GII, GPI, GNH, Green GDP, GHI')],
 'words': [('Factors of production', 'land, labour, capital, enterprise; paid rent, wages, interest, profit'),
           ('Leakage', 'money pulled out of the loop: savings, taxes, imports'),
           ('Injection', 'money pumped into the loop: investment, government spending, exports'),
           ('Value added', 'what a producer adds: its output value minus the inputs it bought'),
           ('Double counting', 'counting the same value twice, once as input and again inside the final good'),
           ('Nominal GDP', 'output valued at current prices'),
           ('Real GDP', 'output valued at constant base-year prices, so only quantities change'),
           ('Economic territory', 'the area whose production counts as ours, which is not always the map')],
}
SEC = {
 '1': dict(
   plain='Imagine a country with no dashboard: no speedometer, no fuel gauge. The government, the central bank and citizens would be driving blind. National income accounting is that dashboard. We cannot build it by asking everyone what they earn, because people forget, lie, and much of the economy is informal. So the handout builds it in three steps: a simple model, an advanced model, then the methods used in India today.',
   eg='The handout’s two meanings of “national”: income earned in the nation whoever earns it, or income earned by the nationals wherever they are. Income itself means the reward for the factors of production: rent, wages, interest, profit.',
   hook='NIA = the economy’s dashboard. Income = rent (land) + wages (labour) + interest (capital) + profit (enterprise).'),
 '2': dict(
   plain='Picture two parties passing money around a ring. Households own the factors of production and hand them to firms. Firms pay incomes (A), households spend that money (C) on the goods firms make (B). With no saving, no stock-piling and no outside world, whatever goes out comes straight back, so the three flows are the same size.',
   eg='A = wages + rent + interest + profit paid by firms; B = value of all goods and services produced; C = money households spend on them. Households spend all they earn; firms keep no inventory; firms pay out everything received, and the leftover is profit.',
   hook='CFIM: two sectors, no saving, no government, no trade ⇒ A = B = C.'),
 '3': dict(
   plain='Now open the ring up. Money can leak out (savings, taxes, imports) and be pumped in (investment, government spending, exports). If households save, they spend less, firms build up stock and produce less, and income falls. If the government spends or exports rise, the loop speeds up. The three flows are always adjusting towards each other: A chases C and B chases A. Over a year they settle.',
   eg='The handout’s two stories. Saving: C falls, then B, then A. Government hiring teachers and soldiers raises A, then C, then B. The economy grows only if injections exceed leakages.',
   hook='Leakages S, T, M pull out. Injections I, G, X push in. “A chases C, B chases A.”'),
 '4': dict(
   plain='One tree, three ways to measure its shadow. Add up what is paid to the factors (income). Add up what is spent on the goods that domestic firms receive (expenditure): total spending C + G + I + X includes foreign parts, so subtract imports M. Or add up the value added by every producer (production). All three give the same total. Then read “GDP” word by word: total, value, final, produced, territory, period.',
   eg='The handout’s word-by-word list: a parent cooking for a child has no price, so it is excluded; second-hand sales are not counted again but new services such as brokerage, registration and repair are. The ₹10 crore Delhi land question is left open: by the handout’s own rule the purchase adds nothing.',
   hook='Income R+P+W+Int · Expenditure C+G+I+X−M · Production ΣVA. GDP = total value of FINAL goods and services produced in a year inside the territory.'),
 '5': dict(
   plain='Draw the economic map of India. It mostly matches the political map, with exceptions. Indian embassies abroad and Indian ships in international waters count as ours; foreign embassies in India and the UN offices do not. GNP changes the question from where to who: add what Indians earn abroad and subtract what foreigners earn here. That gap is NFIA.',
   eg='Counts as India’s: the Indian embassy in Washington, a consulate in Dubai, research bases in Antarctica (Bharati, Maitri), an Air India flight over the Atlantic. Does not count: the American embassy in Chanakyapuri, UN, WHO and IMF offices in India.',
   hook='GNP = GDP + NFIA = GDP + (income of Indians abroad − income of foreigners in India). Write it in words, not B and C.'),
 '6': dict(
   plain='Counting only final goods needs someone to sort final from intermediate, and every producer thinks its own output is final. So we skip the sorting. Each producer adds up only what it added: output minus the inputs it bought. Add these up across the chain and the total equals the value of the final good. Picture a relay race: each runner is credited only for the distance they ran, not for the distance already run.',
   eg='The handout’s wheat-atta-bread-sandwich chain: farmers 1,00,000 (inputs 0); each of the next three makers sells 1,00,000 and bought 60,000, so adds 40,000. GDP = GVA = 1,00,000 + 40,000 + 40,000 + 40,000 = ₹2,20,000, the same as the final-goods check: 40k + 40k + 40k + 1 lakh.',
   hook='VA = output − inputs. ΣVA = GVA = GDP. No double counting.'),
 '7': dict(
   plain='If GDP doubles, did we make twice as much or did prices double? Nominal GDP uses today’s prices, so it mixes both. Real GDP values every year at the same fixed prices, so only quantities can change. The year that supplies the fixed prices is the base year. It should look like today (so we can price a smartphone) and be a boring, shock-free year (so growth is not distorted).',
   eg='The handout’s two traps: using 1980 would make telecom impossible to price; using Covid year 2020 as base would make 2021’s recovery look like 20-25% growth. Base years are updated every 5 to 10 years.',
   hook='Nominal = P × Q (current). Real = Q × P (base). Growth = % change in real GDP. Base year: recent and boring.'),
 '8': dict(
   plain='The buyer pays one price, the seller keeps a smaller one, and the factors of production take home a smaller one still. The gaps are taxes and subsidies. Product taxes are charged per unit (GST); production taxes are lump sums unrelated to volume (land revenue, stamp duty). Start from the price at the factory gate (basic price): add product taxes to get the market price, subtract production taxes to get factor cost.',
   eg='The handout’s GST case: a ₹100 good plus 18% GST = ₹118 market price; the seller keeps ₹100. Headline form: GDP = GVA + net product taxes.',
   hook='MP = BP + product T − product S. FC = BP − production T + production S. BP in the middle.'),
 '9': dict(
   plain='India cannot survey every shop, so each part of the economy gets a different tool. Farming: sown area × yield × mandi price. Registered companies: their audited accounts (value added = revenue − intermediate expenses). The informal part: headcount × value added per worker. Where only a sample is known, the sample’s share of the market blows it up to the whole.',
   eg='The handout’s numbers: 10 lakh e-rickshaw drivers × ₹1.8 lakh = ₹18,000 crore. Blow-up: two firms with ₹100 crore value added hold 40% of the market (400 of 1,000 students surveyed), so the total is 100 crore ÷ 40% = ₹250 crore (10% would give ₹1,000 crore; 50% gives ₹200 crore).',
   hook='Agriculture = production method; corporate = MCA-21 value added; unorganised = labour input; sample ÷ share = total.'),
 '10': dict(
   plain='GDP is a thermometer, not a diagnosis. It adds up rupees, so it does not know whether they went to schools or to casinos, whether one person holds nearly all of it, whether unpaid work happened, or whether a factory polluted a river. Prices alone can also lift it when no one is better off.',
   eg='The handout’s illustrations: Country A and B both ₹1,000 crore but of different things; 10 people, GDP ₹100, per capita ₹10, yet one holds ₹99 and nine share ₹1; hire a maid and GDP rises; cut a forest and GDP rises, and so do the inhalers bought later.',
   hook='Six limits: composition, inequality, unpriced work, externalities, informality, price effects.'),
 '11': dict(
   plain='Since GDP cannot measure well-being, economists build other scorecards. Some correct for inequality (IHDI), some for gender (GDI, GII), some for the environment and unpaid work (Green GDP, GPI), some measure happiness (GNH) or hunger (GHI). HDI is the best known, with three ingredients: a long healthy life, knowledge, and a decent standard of living. GDP still remains king because it is standard, objective and available every quarter.',
   eg='The handout’s HDI ingredients: life expectancy at birth; expected and mean years of schooling (age 25+); GNI per capita in PPP dollars. India is in the medium group. GHI is on a 100-point scale: 0 best, 100 worst.',
   hook='HDI = health + knowledge + income. IHDI adjusts for inequality. GDI and GII for gender. GPI and Green GDP for environment. GNH Bhutan. GHI hunger.'),
 '12': dict(
   plain='National income is a family of totals, each one step from the next. Start at GDP, add what nationals earn abroad (GNP), take away wear and tear and indirect taxes to get National Income, then strip out what firms and government keep (PI), and finally the taxes households pay (PDI). Divide by people to get per capita income.',
   eg='The handout’s chain: NI = GNP(MP) − indirect taxes + subsidies − depreciation; PI = NI − corporate taxes − undistributed profits − net interest paid by households + transfers; PDI = PI − personal taxes = consumption + savings. A brother’s money from Dubai is a transfer, not income.',
   hook='GDP → +NFIA → GNP → −dep → NNP → −net indirect taxes → NI → PI → PDI.'),
}
NUMBERS = [('A = B = C', 'income = production = expenditure over a year'),
           ('C + G + I + X − M', 'expenditure approach (AD)'),
           ('₹2,20,000', 'wheat-atta-bread-sandwich GVA = GDP'), ('1,00,000 / 40,000', 'farmer value added / each later maker'),
           ('₹118', 'market price of a ₹100 good with 18% GST'),
           ('5 to 10 years', 'how often the base year is updated'), ('20-25%', 'fake 2021 growth if Covid 2020 were the base'),
           ('60-90%', 'handout’s range for the informal share'), ('₹18,000 crore', '10 lakh e-rickshaws × ₹1.8 lakh'),
           ('₹250 crore', 'blow-up: ₹100 crore ÷ 40%'), ('2008', 'SNA 2008'), ('2015', 'GDP methodology overhaul; MCA-21'),
           ('2022-23', 'new base year (replaces 2011-12); double deflation, SUT'), ('8', 'GVA sectors; also 8 alternatives to GDP'),
           ('7.8% / 10.3% / 2.3%', 'Q1 FY27 real GDP, nominal GDP, implicit deflator')]
DRAW = ['Redraw the handout’s circular flow figure (CFIM): firms and households, A = incomes, B = production, C = expenditure, assumptions below it (section 2).',
        'Redraw the handout’s multi-sectoral figure: dotted leakages (S, T, M) and solid injections (I, G, X) (section 3).',
        'Write the value-added table of the wheat economy, then the chain GDP → GNP → NNP → NI → PI → PDI with the operation between each step (sections 6 and 12).']
FM = {
 '2': [('Circular flow', 'A = B = C', 'income = production = expenditure; A = wages + rent + interest + profit')],
 '3': [('Leakages', 'S, T, M ⇒ A, B or C shrinks', 'savings, taxes, imports'),
       ('Injections', 'I, G, X ⇒ A, B or C expands', 'investment, government expenditure, exports'),
       ('Growth rule', 'economy grows only if injections > leakages', 'dynamic equilibrium: A chases C, B chases A')],
 '4': [('Income approach', 'TI = R + P + W + Int', 'all payments to factors in the domestic territory'),
       ('Expenditure approach', 'TI = AD = C + G + I + X − M', 'subtract the foreign part of C, G, I (total imports M)'),
       ('Production approach', 'TI = GDP = Σ VA<sub>i</sub> = GVA', 'total value of final goods and services in a year')],
 '5': [('GNP', 'GNP = GDP + NFIA', 'NFIA = income earned by Indians abroad − income earned by foreigners in India')],
 '6': [('Value added', 'VA<sub>i</sub> = output value − input value', 'wheat chain: 1,00,000 + 40,000 + 40,000 + 40,000 = 2,20,000'),
       ('GDP by value added', 'GDP = Σ VA<sub>i</sub> = GVA', 'equals the sum of final goods: 40k + 40k + 40k + 1 lakh')],
 '7': [('Nominal GDP', 'P(current) × Q(current)', 'current prices'),
       ('Real GDP', 'Q(current) × P(base year)', 'constant prices'),
       ('Growth', 'economic growth = % change in real GDP', '')],
 '8': [('Market price', 'MP = BP + product taxes − product subsidies', 'what the buyer pays'),
       ('Basic price', 'BP = MP − product taxes + product subsidies', 'factory-gate price'),
       ('Factor cost', 'FC = BP − production taxes + production subsidies', 'what the factors take home'),
       ('Headline form', 'GDP (MP) = GVA (BP) + net product taxes', 'GDP = GVA + net indirect taxes', 'wide')],
 '9': [('Labour input method', 'headcount × value added per worker', '10 lakh × ₹1.8 lakh = ₹18,000 crore'),
       ('Corporate value added', 'VA = revenue − intermediate expenses', 'MCA-21 balance sheets and P&amp;L'),
       ('Blow-up factor', 'total = sample value added ÷ sample’s market share', '₹100 crore ÷ 40% = ₹250 crore')],
 '12': [('GNP', 'GNP = GDP + NFIA', ''),
        ('National Income', 'NI = NNP at factor cost = GNP(MP) − indirect taxes + subsidies − depreciation', '', 'wide'),
        ('Personal income', 'PI = NI − incomes not paid to households + other transfers to households', 'subtract CT, UP and net interest paid by households; add transfers', 'wide'),
        ('Personal disposable income', 'PDI = PI − personal taxes = consumption + savings', ''),
        ('Per capita income', 'PCI = GDP ÷ mid-year population', ''),
        ('Use side', 'TI = C + S + T', 'consumption, savings, taxes')],
}
