# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 1 (Poverty). Facts come only from the handout text.
plain = idea in everyday words (picture); eg = the handout's own example; hook = one-line handle."""
TOP = {
 'sixty': [('Meaning', 'poverty = inadequacy of well-being: money, health, education, water, security, voice'),
           ('Two kinds', 'absolute (fixed expert bar) versus relative (compared with others, a mirror of inequality)'),
           ('Money line', 'price a basket of necessities: the poverty line; count the share below it: HCR'),
           ('Progress', 'slow fall before the 2000s, fast fall after; Tendulkar line is still official'),
           ('Beyond money', 'National MPI: 12 indicators, poor above a 33% score, MPI = H × A'),
           ('Depth', 'HCR says how many, PGI how far, SPG who is furthest (FGT measures)')],
 'words': [('Well-being', 'how well a person is doing: body, mind, relationships, money, surroundings'),
           ('Poverty line (PL)', 'the money value of a basket of necessities; below it means deprivation'),
           ('Headcount ratio (HCR)', 'the share of the population below the poverty line'),
           ('PPP', 'a conversion rate that counts what money buys, not what the market exchange rate says'),
           ('Deprivation score', 'the weighted share of the 12 indicators in which a household is lacking'),
           ('Headcount (H)', 'what share of people are multidimensionally poor'),
           ('Intensity (A)', 'on average, how deprived the poor are'),
           ('Poverty gap', 'how far a poor person’s income is below the line, as a share of the line')],
}
SEC = {
 '1': dict(
   plain='Picture a health report card with several rows: body, feelings, friends, money, mind, purpose and surroundings. A person doing badly on one row is not necessarily poor. Poverty, the World Bank says, is pronounced deprivation in well-being across many rows: low income, but also low health and education, no clean water or sanitation, no security and no voice. Money is one row, an important one, but not the whole card.',
   eg='The handout’s table lists seven dimensions of well-being (physical, emotional, social, financial, intellectual, spiritual, environmental) and notes the list is not exhaustive. For the financial one it says financial stress ranks as a top source of anxiety.',
   hook='Poverty = inadequacy of well-being. Many dimensions, not just income.',
   mn=[dict(kind='sentence', title='Seven dimensions of well-being (order as in the handout)', sentence='People Expect Safety, Food, Income, Schooling, Environment',
            letters=[('P', 'Physical'), ('E', 'Emotional'), ('S', 'Social'), ('F', 'Financial'), ('I', 'Intellectual'), ('S', 'Spiritual'), ('E', 'Environmental')],
            note='Own memory aid (not from the handout): the sentence initials follow the handout’s table order.')]),
 '2': dict(
   plain='Two ways to call someone poor. Absolute: experts draw a fixed finish line and anyone short of it is poor, like a height bar at a fairground. Relative: you compare people with each other, so someone is poor if they fall below the average. A person can pass the fixed bar and still be poor next to their neighbours, which is why relative poverty is a reflection of inequality.',
   eg='The handout’s examples: absolute poverty means you cannot afford the expert’s basket of goods; relative poverty means your income is below the population average.',
   hook='Absolute = normative bar (experts). Relative = comparison, mirror of inequality.'),
 '3': dict(
   plain='There are two different jobs here. Job one is delivery: a scheme needs a list of names, and every list makes two mistakes, leaving out a deserving person (exclusion) or admitting an undeserving one (inclusion). Fixing one worsens the other, so governments reduce exclusion first. Job two is judging progress: set a milestone, check a representative sample, and say what share is below it. The first is a ration queue, the second is a class pass-rate. The poor are not the beneficiaries on the lists.',
   eg='The handout’s example: if 20% of a representative sample is below the PL, the population is assumed to have around 20% below the line. It is an estimate, not a count. Poverty is assessed on consumption expenditure, not income, because income is less truthfully revealed and more volatile.',
   hook='Beneficiaries ≠ the poor. Exclusion versus inclusion error. Estimation judges progress; HCR = estimate, not a count.'),
 '4': dict(
   plain='A poverty line is an expert’s shopping list for a life of basic dignity, priced in the market. Each committee made the list longer: first only calories, then separate rural and urban lists, then state lists, then health, education, water and sanitation, and finally what poor people actually spend on. The list is normative, so experts differ and views change as living standards improve.',
   eg='The handout’s numbers: Dandekar and Rath (1971) 2250 calories a day; Alagh (1979) 2400 rural and 2100 urban; Lakdawala (1993) state-specific lines; Tendulkar (2009) adds health, education, water and sanitation; Rangarajan (2014) adds a behavioural part (alcohol, tobacco and so on) for a household of 5.',
   hook='Order: Dandekar, Alagh, Lakdawala, Tendulkar, Rangarajan. Rangarajan not accepted; Tendulkar stays official.'),
 '5': dict(
   plain='The fall in poverty ran at two speeds. Before the 2000s it was a slow walk, and because the population was growing faster the number of poor people actually rose. After the 2000s growth almost doubled and the fall tripled in pace. The handout also warns that one year can carry several poverty numbers because each uses a different yardstick, so always name the yardstick.',
   eg='The handout’s arithmetic: HCR from about 65% (1951) to about 45% (1993) is about 20 percentage points in about 45 years = 0.44 pp a year. Then about 45% to about 22% (2012) is about 23 pp in 20 years = 1.15 pp a year, thrice the earlier pace. Growth rose from 3.5% to 6.5%.',
   hook='0.44 pp a year (slow) → 1.15 pp a year (fast). Name the yardstick for every figure.'),
 '6': dict(
   plain='The World Bank draws three lines from the national lines of groups of countries: low-income, lower-middle-income (India’s group) and upper-middle-income. Money in different countries buys different amounts, so every line is converted by PPP, a price-tag translator. Think of it as asking how many rupees buy in India what one dollar buys in the US, not what the money market says.',
   eg='The handout’s PPP example: a basket costs $100 in the US and Rs 2000 in India, so the PPP conversion factor for India is 20. Apples at ₹100 a kg in India and $5 a kg in the US mean ₹100 has the same purchasing power as $5. The three lines (2021 PPP): $3.00, $4.20, $8.30 a day.',
   hook='Three lines: $3.00 (IPL), $4.20 (LMIC, India’s group), $8.30 (UMIC). PPP factor = local price ÷ dollar price.'),
 '7': dict(
   plain='Take one Indian and measure him against three lines and you get three answers: he is rarely poor by the lowest line, sometimes by the middle one and nearly always by the highest. The message is that few Indians are in extreme poverty now, but most of the rest are not far above the line and would count as poor in middle-income countries.',
   eg='The handout’s numbers: at $3.00, 5.3% (about 75 million in 2022); at $4.20, 24% (close to 350 million); at $8.30, more than 80%. World extreme poverty is 10.8% against India’s 5.3%, the first time India is below the world average.',
   hook='5.3% → 24% → over 80%: one person, three lines, three rates. Use $4.20 for India.'),
 '8': dict(
   plain='A money line asks whether you can afford the basics. The multidimensional approach asks whether you actually have them. A family may have money on paper but no clean cooking fuel, toilet or school nearby. So deprivation is checked directly, indicator by indicator. The global MPI uses three dimensions (health, education, standard of living) and 10 indicators.',
   eg='The handout’s example: a household is deprived of cooking fuel if it uses solid fuel such as tree bark or cow dung and has no modern fuel such as LPG or kerosene. A household deprived on 3 or more of the 10 indicators is poor in the global version.',
   hook='Money line = can you buy it? MPI = do you have it? Global: 10 indicators, 3 or more.'),
 '9': dict(
   plain='Give every household a score out of 100% for how many weighted things it lacks. Above 33% it counts as poor. Then ask two questions of the whole population: how many people are poor (H), and how badly off are the poor on average (A). Multiply to get one number, MPI = H × A. Only people in poor households count, so a household under the cut-off is simply left out of both questions.',
   eg='The handout’s worked example: HH1 has 7 members and score 72.8%, HH2 has 5 and 52.6%, HH3 has 4 and 21.4% (not poor). H = 12 ÷ 16 = 0.75; A = 0.64; MPI = 0.75 × 0.64 = 0.48. So 75% of individuals are poor and each is deprived in 64% of the weighted indicators on average.',
   hook='National: 12 indicators, 33%. Global: 10 indicators. MPI = H × A. Three dimensions at 1/3 each.'),
 '10': dict(
   plain='Between the two NFHS rounds India’s MPI nearly halved. Fewer people were poor (H fell) and the poor were slightly less deprived (A fell a little). The fall was fastest in rural areas, where poverty was highest, so the rural-urban gap narrowed in absolute terms, though it remains. The biggest gains came where schemes reached households directly: sanitation and cooking fuel.',
   eg='The handout’s numbers: MPI 0.117 (NFHS-4) to 0.066 (NFHS-5); H 24.85% to 14.96%; A 47.14% to 44.39%. Rural H 32.59% to 19.28%; urban 8.65% to 5.27%. 135 million escaped. Falls: sanitation 21.8 pp, cooking fuel 14.6 pp. Highest H: Bihar 33.76%.',
   hook='MPI 0.117 → 0.066. H 24.85 → 14.96. 135 million out. Sanitation and cooking fuel led.'),
 '11': dict(
   plain='The summary is a scorecard with wins and gaps. The wins are large drops in extreme poverty, multidimensional poverty and the consumption Gini. The gaps are about dignity and fairness: a line that still looks too low for a decent life, a wide earnings gap, fewer women in paid work, young people without jobs, hunger and low development scores. The handout uses different line values here, so keep the figures with their dates.',
   eg='The handout’s numbers: extreme poverty 27.1% (2011-12) to 5.3% (2022-23); rural 18.4% to 2.8%; urban 10.7% to 1.1%; rural-urban gap 7.7 pp to 1.7 pp; MPI 55.34% (2005-06) to 14.96% (2019-21); Gini 28.8 to 25.5. Dignity deficit: ₹62 a day, while one litre of Amul milk cost ₹63 in 2022.',
   hook='Wins: 27.1 → 5.3, 55.34 → 14.96, Gini 28.8 → 25.5. Gaps: dignity, jobs, hunger, inequality.'),
 '12': dict(
   plain='The headcount ratio is like counting who failed an exam: it treats someone one mark short the same as someone who scored zero. Depth asks how far below the line the poor are (PGI), and severity squares each gap so the people furthest away count most (SPG). Helping people just under the line improves the headcount but barely moves the squared gap.',
   eg='The handout’s example: HCR cannot tell someone ₹1 below the line from someone with zero income. PGI × poverty line × total population = the money needed to lift every poor person exactly to the line, with perfectly targeted transfers. FGT measures were developed in 1984.',
   hook='HCR = how many. PGI = how far. SPG = who is furthest. FGT1 and FGT2.'),
}
NUMBERS = [('65% → 45%', 'HCR 1951 to 1993 (about 0.44 pp a year)'), ('45% → 22%', 'HCR 1993 to 2012 (1.15 pp a year)'),
           ('2250; 2400/2100', 'calories: Dandekar and Rath; Alagh rural/urban'), ('$3.00 / $4.20 / $8.30', 'World Bank lines, 2021 PPP, June 2025'),
           ('20', 'PPP factor in the handout example ($100 basket = Rs 2000)'), ('5.3% / 24% / over 80%', 'India at the three lines'),
           ('10 / 12', 'indicators in the global MPI / national MPI'), ('33%', 'deprivation cut-off for the national MPI'),
           ('0.75 × 0.64 = 0.48', 'H × A = MPI in the worked example'), ('0.117 → 0.066', 'national MPI, NFHS-4 to NFHS-5'),
           ('135 million', 'escaped multidimensional poverty'), ('27.1% → 5.3%', 'extreme poverty 2011-12 to 2022-23'),
           ('28.8 → 25.5', 'consumption Gini 2011-12 to 2022-23'), ('1984', 'FGT measures (depth and severity)')]
DRAW = ['Redraw the handout’s five-step flow for measuring poverty (section 3) and add one number to each box.',
        'Redraw the handout’s worked MPI example with three households (section 9) and compute H, A and MPI from memory.',
        'Write the five poverty line committees in order with one fact each, then the three World Bank lines with India’s rate at each.']

FM = {
 '3': [('Headcount ratio (HCR)', 'HCR = people below the PL ÷ total population', 'from a representative sample; 20% of sample → about 20% of population')],
 '4': [('Rangarajan basket', 'PL basket = normative food + normative non-food + behavioural', 'household of 5; Tendulkar still official')],
 '5': [('Pace of fall', 'pp a year = fall in HCR ÷ years', 'about 20 ÷ 45 = 0.44; about 23 ÷ 20 = 1.15')],
 '6': [('PPP conversion factor', 'PPP factor = local price of basket ÷ US$ price of basket', 'Rs 2000 ÷ $100 = 20 (handout)'),
       ('Line in rupees', '₹ line ≈ PPP factor × $ line', 'about ₹62 = 20.6 × $3 (handout summary)')],
 '8': [('Global MPI poor', 'deprived on 3 or more of the 10 indicators', 'national MPI differs: score above 33% on 12 indicators')],
 '9': [('Poor household', 'deprivation score &gt; 33%', '12 indicators, weights 1/3 per dimension'),
       ('Headcount (H)', 'H = poor persons ÷ total persons', '12 ÷ 16 = 0.75'),
       ('Intensity (A)', 'A = sum of weighted scores of the poor ÷ number of poor', '(7 × 0.728 + 5 × 0.526) ÷ 12 = 0.64'),
       ('MPI', 'MPI = H × A', '0.75 × 0.64 = 0.48')],
 '12': [('Cost of ending poverty', 'PGI × poverty line × total population', 'with perfectly targeted transfers'),
        ('Squared poverty gap', 'SPG = average of (poverty gap)²', 'FGT2: more weight on larger gaps')],
}
