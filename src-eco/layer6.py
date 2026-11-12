# -*- coding: utf-8 -*-
"""Authored 'concept-first' layer for Economy Ch 6 (Inflation) in the handwritten notes.
plain = the idea in everyday words (memory aid, no new facts); eg = worked/everyday example; hook = one-line memory handle;
graphs = names of functions in hgraph.py; mn = extra mnemonic cards. Facts here come only from the handout text."""
TOP = {
 'sixty': [('Prices rise', 'when AD > AS'), ('Causes', 'pull (AD right), push (AS left)'), ('Measure', 'basket + base year = index'),
           ('Read', 'headline, core, super core'), ('Effects', 'borrowers gain; poor hit most; fiscal drag'), ('Cure', 'make money expensive')],
 'words': [('Price', 'cost of ONE good, set by that good’s own demand and supply'),
           ('Price level', 'the overall level of prices of everything; set by AD and AS'),
           ('Basket', 'a fixed bag of goods and services a typical person in a group buys'),
           ('Base year', 'the year whose basket price is fixed at 100 so later years can be compared'),
           ('Index', 'basket price rescaled to the base year = 100 (165 = 65% dearer than base)'),
           ('Y-o-Y', 'this month compared with the same month last year, so seasons do not distort it')],
}
SEC = {
 '1': dict(
   plain='Picture a crowd of people. One tall person does not make the crowd tall. Inflation means the whole crowd is growing taller: the overall cost of what people buy keeps rising. A single dearer good (say tomatoes) is not inflation by itself.',
   eg='The handout’s contrast: an agricultural labourer in Odisha and a new joiner in a Bengaluru startup buy very different baskets, so each feels inflation differently. That is why we track one fixed “normative basket” for a group.',
   hook='ONE price up ≠ inflation. Inflation = the whole basket (price level) up.'),
 '2': dict(
   plain='AD is everybody’s shopping list added up, in rupees. AS is everything farms and factories can put on the shelves. When the shopping list is longer than the shelves, shops raise prices; when shelves overflow, prices ease. The price level sits where the two meet.',
   eg='Think of a school canteen. 100 students want samosas (AD) but the kitchen makes only 60 (AS). The canteen raises the price. Same idea for a whole economy (practice picture, not from the handout).',
   hook='AD chases AS. AD > AS → prices rise. Two ways: AD up, or AS down.',
   graphs=['adas_equilibrium']),
 '3': dict(
   plain='There are only two roads to dearer goods. PULL: buyers have more money or more wish to spend, so the AD curve slides right. PUSH: it becomes costlier or harder to produce, so the AS curve slides left. Cartels, hoarding, black money and shocks from abroad ride on top of these two.',
   eg='Pull: a salary hike plus cheap loans means more car and phone buying, so prices drift up. Push: war cuts oil supply, fuel is a cost for every producer, so everything gets dearer (the handout stresses oil producers and import dependence).',
   hook='PULL = demand shifts RIGHT (price UP, output UP). PUSH = supply shifts LEFT (price UP, output DOWN).',
   graphs=['demand_cost_panels']),
 '4': dict(
   plain='We cannot measure inflation for each person, so we fix a typical shopping bag for a group, price it every month, and compare with the same month a year ago. The % change is inflation. Comparing with the same month removes seasonal swings.',
   eg='Practice sum (not from the handout): if the same basket cost ₹9,000 in March last year and ₹9,900 now, inflation = (9,900 − 9,000) ÷ 9,000 × 100 = 10%.',
   hook='Same month, fixed basket, % change = inflation.',
   mn=[dict(kind='sentence', title='Seven steps, in order (order matters, so a sentence)', sentence='To Buy Bread, Begin Looking Intently Inside',
            letters=[('T', 'Target group'), ('B', 'Basket (normative)'), ('B', 'Base year (weights, monthly basket)'), ('B', 'Base-year prices collected'),
                     ('L', 'Later-year prices collected'), ('I', 'Inflation = % change, same month'), ('I', 'Index value communicated'),],
            note='Own memory aid (not from the handout): the sentence is about a basket, which is the whole idea.')]),
 '5': dict(
   plain='A raw basket price like ₹11,345 means nothing. So we rescale the base-year basket to a clean 100. Later prices become readable at once: 150 means 50% dearer than the base year, 165 means 65% dearer. The base also gives a fixed yardstick, not a moving one.',
   eg='The handout’s numbers: base March 2015 ₹10,000 (index 100); March 2025 ₹15,000 (index 150); March 2026 ₹16,500 (index 165). Inflation in the last year = (16,500 − 15,000) ÷ 15,000 = 10%. Prices are 65% above 2015.',
   hook='Index − 100 = % rise since the base year. Inflation = % change of the index over the same month last year.',
   graphs=['index_bars']),
 '6': dict(
   plain='Different yardsticks for different questions. CPI follows what households pay in shops (retail). WPI follows prices in bulk trade between businesses. CPI-AL and CPI-IW follow farm labourers and factory workers. A PPI would follow what producers receive, but India has none yet.',
   eg='In Feb 2026 the new CPI (2024 = 100) widened the basket: 299 → 358 items, OTT subscriptions and e-commerce prices came in, VCRs and CDs went out. Food’s weight fell from 45.86% to 36.75% (Engel’s Law at work).',
   hook='CPI → NSO (MoSPI). CPI-AL, CPI-IW → Labour Bureau. WPI → OEA (DPIIT).',
   graphs=['weights_bars']),
 '7': dict(
   plain='Terms are different lenses on the same price rise. Headline shows everything. Core removes volatile food and fuel to show the underlying trend. Super core removes even more. Skewflation is one or two items spiking. “Dis-” means slower, “De-” means down. Stagnation words (recession, depression) describe output, not prices.',
   eg='Trap to remember: petrol and diesel are NOT in “Fuel and Light”; the handout puts them under Transport and Communication, so they stay inside core. They leave only at super core.',
   hook='Dis- = the RATE slows. De- = the LEVEL falls. Core = headline − food − fuel.',
   graphs=['measure_ladder', 'price_paths'],
   mn=[dict(kind='sentence', title='The ladder of measures, narrow to narrower (an order)', sentence='Hot Chai Soothes',
            letters=[('H', 'Headline (all items, CPI-C)'), ('C', 'Core (minus food and fuel)'), ('S', 'Super core (also minus petrol, diesel, precious metals)')],
            note='Own memory aid: each step peels off more volatile items.')]),
 '8': dict(
   plain='Prices and wages can chase each other in a loop: dearer goods, higher wage demands, dearer goods again. Expectations matter too: if everyone expects prices to rise, they stock up today and prices do rise. Normally a country picks between inflation and unemployment (the Phillips Curve). Stagflation is the nightmare: both are bad at once.',
   eg='Why stagflation paralyses a policy maker: boosting demand to cut unemployment worsens inflation; cooling demand to cut inflation worsens unemployment. Neither lever helps.',
   hook='Phillips Curve = inverse (low UE, high inflation). Stagflation = off the curve: both high.',
   graphs=['spiral_loop', 'phillips', 'stag_boxes']),
 '9': dict(
   plain='Inflation is a quiet tax on money: ₹110 this year buys only what ₹100 bought last year. Whoever owes money gains, because the debt is repaid with weaker rupees; whoever is owed loses. What the lender truly earns is the nominal rate minus inflation.',
   eg='Handout example: lend at 10% when inflation is 7%, so the lender is richer by only 10 − 7 = 3% in real terms. Deposits paying 2-3% do not beat inflation, so depositors’ real return is negative. Cash at home loses value at the rate of inflation.',
   hook='RIR = NIR − inflation. “LDC lose; BP gain”: Lenders, Depositors, Consumers lose; Borrowers, Producers gain.',
   graphs=['real_rate_bar', 'gain_lose'],
   mn=[dict(kind='word', title='Who loses, who gains', word='LDC + BP',
            letters=[('L', 'Lenders / banks lose (unless protected)'), ('D', 'Depositors lose (real return negative)'), ('C', 'Consumers lose (money buys less)'),
                     ('B', 'Borrowers gain'), ('P', 'Producers gain (they can pass the rise on)')],
            note='Own memory aid: the five groups from the handout table. The order is free.')]),
 '10': dict(
   plain='Zero or falling prices are not the goal. A little steady inflation keeps firms profitable, so they invest, hire and raise wages. Stability also stops people from putting off buying. But the poor suffer most: they spend most of their income on food, whose prices swing and whose sellers can pass price rises on.',
   eg='Engel’s Law: as income rises, the SHARE of income spent on food falls even if the rupee amount rises. A household with ₹10,000 a month that spends ₹7,000 on food feels a food-price jump far more than one that spends a small share on food (practice picture, not from the handout).',
   hook='Engel: richer ⇒ smaller food share ⇒ poor hit hardest.',
   graphs=['engel_curve']),
 '11': dict(
   plain='When prices rise, the government collects more tax without passing any new law. Indirect taxes are mostly a % of value, so they collect more. A worker whose pay rises with inflation moves into a higher slab and pays a bigger share as tax. Real take-home grows less than pay, spending falls, and prices cool by themselves.',
   eg='Handout table at 20% inflation: income ₹9 L → ₹10.8 L; tax ₹1.1 L → ₹1.41 L (up 28.2%); take-home ₹7.9 L → ₹9.39 L (up 18.8%, less than 20%).',
   hook='Fiscal drag = inflation pushes you into higher slabs = automatic stabiliser (AD falls, prices cool).',
   graphs=['fiscal_drag_bars']),
 '12': dict(
   plain='We cannot find the exact cause quickly, and fixing roads, ports and the business climate takes years. So the cure must work whatever the cause: cut AD. AD is spending, and spending needs money. If money becomes expensive (higher interest rate), savers save more and borrowers borrow less, so AD falls and prices cool.',
   eg='Handout: a loan of ₹1 lakh at 8%. Raise the rate to 10%: those with money save it for the higher interest, those without cannot afford to borrow. Both cut demand.',
   hook='Dearer money ⇒ less spending ⇒ AD falls ⇒ prices cool. (Who does it and how: Chapter 8.)'),
}

FM = {
 '2': [('Price rule', 'AD &gt; AS ⇒ price level ↑', 'either AD rises or AS falls (handout key rule)'),
       ('Link to price level', 'AD: price ↑ ⇒ demand ↓ · AS: price ↑ ⇒ supply ↑', 'AD inversely, AS positively related to the price level')],
 '3': [('Demand-pull', 'AD shifts right: AD0 → AD1', 'price ↑ and output ↑ (Y0 → Y1)'),
       ('Cost-push', 'AS shifts left: AS0 → AS1', 'price ↑ and output ↓')],
 '4': [('Inflation (Y-o-Y)', 'Inflation % = (basket price this month − basket price same month last year) ÷ basket price same month last year × 100', 'handout: % change in the basket price over the same month of last year', 'wide')],
 '5': [('Index', 'Index = (100 ÷ base-year basket price) × current basket price', 'base year = 100'),
       ('Handout numbers', '(100 ÷ 10,000) × 15,000 = 150 · (100 ÷ 10,000) × 16,500 = 165', 'March 2015 base ₹10,000; March 2025; March 2026'),
       ('Inflation from the baskets', '(16,500 − 15,000) ÷ 15,000 × 100 = 10%', 'March 2026 over March 2025'),
       ('Reading an index', 'index of 165 ⇒ prices 65% above the base year', 'index − 100 = % above the base')],
 '7': [('Core inflation', 'Core = Headline − food − fuel (Fuel and Light)', 'petrol and diesel stay inside core'),
       ('Super core', 'Super core = Headline − food − fuel − petrol − diesel − precious metals', 'handout: truest picture of underlying demand', 'wide'),
       ('Recession rule', 'output falls for 2 consecutive quarters', 'a rule of thumb (NBER looks at broader data)'),
       ('Hyperinflation (Cagan)', 'more than 50% per month', 'no consensus on the line between high and hyper')],
 '8': [('Stagflation', 'Stagflation = stagnation (low growth, high unemployment) + high inflation', 'both adverse at once'),
       ('Phillips Curve', 'inflation ↑ ⇔ unemployment ↓ (inverse)', 'A.W. Phillips, UK 1861-1957')],
 '9': [('Real interest rate', 'RIR = NIR − Inflation', 'handout: 10% − 7% = 3%'),
       ('Floating rate (banks)', 'NIR = RIR + Inflation', 'RIR fixed, NIR moves with inflation'),
       ('Keeping your worth', 'extra needed = inflation %', 'with 10% inflation ₹110 buys what ₹100 bought last year')],
 '10': [('Engel’s Law', 'income ↑ ⇒ % of income spent on food ↓', 'even if rupees spent on food rise')],
 '11': [('Tax at ₹9 L', '₹50,000 + ₹60,000 = ₹1.1 L', '10% on first 5 L; 15% on next 4 L (hypothetical slabs)'),
        ('Tax at ₹10.8 L', '₹50,000 + ₹75,000 + ₹16,000 = ₹1.41 L', '20% on the last 80k'),
        ('Disposable income', 'income − tax: 9 − 1.1 = ₹7.9 L; 10.8 − 1.41 = ₹9.39 L', 'handout table'),
        ('Fiscal drag', 'income +20% ⇒ tax +28.2%, post-tax income +18.8%', 'no new law; AD falls; prices cool')],
 '12': [('Cure logic', 'cost of money ↑ ⇒ spending ↓ ⇒ AD ↓ ⇒ prices cool', 'handout: loan of ₹1 lakh at 8% → 10%')],
}

NUMBERS = [('4% ± 2%', 'inflation target band'), ('2014', 'Urjit Patel Committee: CPI-C as headline'), ('2015', 'CPI-C adopted as the anchor'), ('2024 = 100', 'new CPI base (Feb 2026)'),
           ('12', 'divisions in the 2024 CPI'), ('358', 'items (was 299)'), ('36.75%', 'food weight (was 45.86%)'), ('28.32%', 'old “Miscellaneous” weight'),
           ('165', 'index = prices 65% above base'), ('2 quarters', 'recession rule of thumb'), ('50% a month', 'Cagan’s hyperinflation mark'), ('1861-1957', 'Phillips’s UK data'),
           ('~30% / 25%', 'Great Depression: US GDP fall, unemployment'), ('10 − 7 = 3', 'real interest example'), ('+20% → +28.2%', 'income vs tax (fiscal drag)')]
DRAW = ['Redraw the handout’s AD-AS sketches (equilibrium; AD shifting right; AS shifting left) from the figures in section 2, then label P0, P1, Y0, Y1.',
        'Write the seven measurement steps and the sentence “To Buy Bread, Begin Looking Intently Inside”.',
        'Write headline, core and super core, and what each leaves out.']
