# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 2 (Inequality). Facts come only from the handout text."""
TOP = {
 'sixty': [('Meaning', 'inequality = differences in attainment of well-being; poverty is the floor, inequality is the gaps above it'),
           ('Two curves', 'Kuznets = theory (inverted U); Lorenz = data-based picture'),
           ('One number', 'Gini = A ÷ (A + B), from 0 (equal) to 1 (unequal), with four shortcomings'),
           ('Why it exists', 'natural advantages, Marx (capital versus labour), modern view (survival, rule of law)'),
           ('Growth', 'growth by design concentrates resources, so it causes inequality'),
           ('Two models', 'trickle-down (four conditions) versus inclusive growth (capability + opportunity)')],
 'words': [('Inequality', 'differences in how well people are doing, measured mostly through consumption'),
           ('Lorenz curve', 'a data-based curve of cumulative income shares against cumulative population'),
           ('Gini coefficient', 'one number from the Lorenz curve: the share of the triangle between equality and the curve'),
           ('Kuznets curve', 'a theoretical inverted U: inequality rises, stabilises, then corrects as incomes rise'),
           ('Survivorship bias', 'judging only by the winners that remain and ignoring those that vanished'),
           ('Rule of law', 'a whole environment of competent, fair institutions that frame, execute and judge laws'),
           ('Trickle-down', 'focus growth on a few sectors and hope or arrange for benefits to flow down'),
           ('Inclusive growth', 'broad-based growth where the bottom contributes and so has a rightful claim')],
}
SEC = {
 '1': dict(
   plain='Poverty is a floor; inequality is the staircase above it. Two people can both be well clear of deprivation and still differ in how well they are doing. Inequality can be economic, social or political, but we measure the economic kind. Wealth would show the biggest gaps, yet wealth and income are less truthfully revealed and jumpy, so consumption expenditure (CE) is the steadier, more objective yardstick even though it shows a lower gap.',
   eg='The handout’s example: one person lives where there is one hospital per 5 km² and another where there are two. Neither is probably facing pronounced deprivation, but the second’s attainment is better. That is inequality.',
   hook='Inequality = differences above the floor. Measured by CE: lower than wealth inequality but most objective.'),
 '2': dict(
   plain='Kuznets drew a story, not a photograph. As a society gets richer, some people’s incomes race ahead, so inequality first climbs; then it levels off; and eventually it corrects, giving an upside-down U. Nobody measured this curve. It is a theoretical expectation, and the three phases need not be equal in length.',
   eg='The handout’s sketch: inequality on the vertical axis, income on the horizontal, an inverted U with phases A, B and C marked. It does not define each phase separately.',
   hook='Kuznets = theory, inverted U: rises, stabilises, corrects. Phases A, B, C unequal.'),
 '3': dict(
   plain='Line up everyone from the poorest to the richest, cut them into equal-sized groups and add up the income of each group from the bottom. Plot the running totals and join the dots: that is the Lorenz curve, a photograph of inequality. If everyone had equal shares it would be a straight diagonal. If one person had everything it would hug the floor and shoot up at the very end. Real countries lie in between.',
   eg='The handout’s example: bottom 20% have 3%, the next 20% have 7%, so the bottom 40% have a cumulative 10%. The two pictures in the handout use different illustrations (50% versus 40% for the bottom 80%), so do not quote them; explain the method and the two extreme lines.',
   hook='Lorenz = data-based. Equality line OP; perfect inequality OQP (QP). The farther from OP, the less equal.'),
 '4': dict(
   plain='The Gini squeezes the Lorenz picture into one number: how big is the gap area A between the equality line and the curve, compared with the whole triangle A + B. Zero gap means perfect equality (0); no area under the curve means perfect inequality (1). It is handy, but a single number hides the shape of a society and the people in it. That is the four shortcomings: like a thermometer, not a diagnosis.',
   eg='The handout’s examples: States A and B with Ginis 0.3 and 0.4 do not combine to 0.35. Two societies can both score 0.40 (one with a starving lower class and a wealthy middle, one with a comfortable middle and a few trillionaires). A ₹10,000 gift between two middle-class people moves the Gini; a multi-billionaire taking ₹10,000 from a beggar barely does.',
   hook='Gini = A ÷ (A + B), 0 to 1. Higher = more unequal. HATS: four shortcomings.'),
 '5': dict(
   plain='Three layers of explanation. First, accidents of birth and place: family, status, networks, geography. They explain most inequality but not why siblings differ, which comparative advantages explain. Second, Marx: capital is scarce and concentrated, labour is abundant, so labour bargains badly and profit’s share compounds. Third, the modern view: Marx only sees the surviving firms; most new firms close, so what matters is survival and market share, and the means firms choose (fair or unfair) set the nature of inequality. A strong rule of law pushes firms to fair means.',
   eg='The handout’s examples: an elder sibling given responsibility earlier is better prepared for such roles; a younger sibling may lean to art. Most firms that start today shut down within 10 years. The Competition Act, 2002 is only one part of the rule of law; how it is applied decides whether the rule of law exists.',
   hook='Natural → Marx → Modern. Modern asks about the nature of inequality; rule of law decides it.'),
 '6': dict(
   plain='Growth works by sending scarce resources where they will be used best. That is exactly what makes it unequal: the favoured sectors, regions and industries grow faster and their incomes pull ahead. Growth also brings jobs and a faster fall in poverty, so we want it. The policy models that follow try to get fast growth with less inequality, and the handout stresses they are policy approaches, not mathematical models.',
   eg='The handout’s reasoning: faster growth means more employment and a faster fall in poverty. But if resources focus on certain sectors, regions or industries, their incomes grow faster, so inequality rises. Growth is not without its costs.',
   hook='Growth by design causes inequality, but also jobs and poverty fall. Two models follow: trickle-down, inclusive.'),
 '7': dict(
   plain='Trickle-down is a water-pipe plan: pour resources into a high-potential sector, let it pull the economy up, and move some of the gains down to people left out. For the water to reach the bottom four things must all work: the sector grows, the government collects tax from that growth, it chooses to spend on those left out, and the spending reaches them. If any link breaks, the inequality becomes permanent. It is not anti-poor, but a well-meant pursuit of growth creates inequality.',
   eg='The handout’s contrast: evenly spread resources give only an average growth rate, while focus aims at a multiplier effect where one sector grows and pulls the whole economy up. Benefits may trickle down naturally but it may take a long time, so the government speeds it by redistributing.',
   hook='Four conditions: sector grows; tax efficiency; decision to redistribute; efficiency of redistribution. Any one fails, inequality stays.',
   ),
 '8': dict(
   plain='Trickle-down makes the poor wait for the government’s gift. Inclusive growth turns them into contributors with a rightful claim. It stands on two pillars: capability (find who is poor and why, then give skills, health and education that fit changing industry) and opportunity (jobs, entrepreneurship, easier business, shared risk, access to capital). Interventions must also recognise behaviour: asking why children are not in school matters more than just building a school.',
   eg='The handout’s behavioural example: not just build more schools; ask whether teachers are skilled and qualified, whether there are separate girls’ washrooms and whether poor families can afford incidental costs. Reading named: National Skill Development Programme, PMKVY, Jan Dhan, Mudra, Economic Survey 2025-26.',
   hook='Inclusive = capability + opportunity; poor become active contributors with a rightful claim. Same family as trickle-down, different emphasis.',
   mn=[dict(kind='sentence', title='Pillar 1 · Capability, in order', sentence='Identify Individuals, Find Fixes, Skill-up',
            letters=[('I', 'Identify the poor and vulnerable'), ('I', 'Identify backward regions'), ('F', 'Find key reasons for backwardness'), ('F', 'Focused interventions based on those reasons'), ('S', 'Skills, basic healthcare, quality education')],
            note='Own memory aid (not from the handout): the sentence initials follow the five capability steps in the handout’s order.')]),
}
NUMBERS = [('0 to 1', 'Gini range: 0 perfect equality, 1 perfect inequality'), ('A ÷ (A + B)', 'Gini formula'),
           ('4', 'shortcomings of the Gini; four conditions of trickle-down'), ('0.3 and 0.4', 'two States’ Ginis, not combinable to 0.35'),
           ('0.40', 'two different societies can share this Gini'), ('₹10,000', 'transfer in the handout’s tails-versus-middle example'),
           ('10 years', 'most new firms shut down within this time'), ('2002', 'Competition Act, one part of the rule of law'),
           ('3% and 10%', 'bottom 20% and bottom 40% cumulative shares in the handout’s example'), ('2 pillars', 'capability and opportunity'),
           ('28.8 → 25.5', 'consumption Gini 2011-12 to 2022-23'), ('13 times', 'top 10% median earnings versus bottom 10% (2023-24)')]
DRAW = ['Redraw the handout’s Kuznets sketch (inverted U with phases A, B, C) and write “theory, not data” beside it (section 2).',
        'Redraw the handout’s Lorenz sketch with OP, the curve and OQP, shade A and B, and write Gini = A ÷ (A + B) (sections 3 and 4).',
        'Write the four trickle-down conditions, the four Gini shortcomings and the two inclusive-growth pillars with five steps each.']

FM = {
 '4': [('Gini coefficient', 'Gini = A ÷ (A + B)', 'A = area between equality line and Lorenz curve; B = area below the curve'),
       ('Range', '0 (A = 0) ≤ Gini ≤ 1 (B = 0)', 'higher Gini = more inequality')],
 '3': [('Perfect equality', 'Lorenz curve = line OP (x = y)', 'every group has the same share as any group of the same size'),
       ('Perfect inequality', 'Lorenz curve = OQP', 'one person has all the income, the rest zero')],
 '7': [('Trickle-down works if', 'sector grows AND tax efficiency AND decision to redistribute AND redistribution efficiency', 'any one fails → inequality becomes permanent', 'wide')],
}
