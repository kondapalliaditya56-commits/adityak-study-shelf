from lib import Ch

c = Ch(2, 'Inequality: Measures, Causes and Growth Models',
       'Economy · GS Foundation · Chapter 2',
       [('hb', 'Handout only: no class slides'), ('', 'Handout pages 27-35'), ('', 'No PYQs quoted')],
       'What inequality is and why consumption is used, the Kuznets curve, the Lorenz curve and Gini coefficient (with four shortcomings), the reasons for inequality (natural advantages, Marx, modern reasoning and the rule of law), why growth causes inequality, and the two policy approaches: trickle-down and inclusive growth.')

c.sec('Exam lens: priority and PYQs', 'exam-lens-priority-and-pyqs')
c.call('alert', 'Source note', [
    '**This chapter comes from the handout only.** No class slides, no teacher ink and no PYQ section came with it. PYQs quoted in the material: **none quoted in the material.**'])
c.table('What the handout itself stresses', ['Signal in the handout', 'Where', 'Why it matters'], [
    ['Kuznets curve is "**not a data-based curve,** merely a theoretical expectation"; Lorenz curve **is** data-based', 'Section 2', 'A clean statement trap: theory versus data.'],
    ['Gini ranges 0 (perfect equality) to 1 (perfect inequality); a higher Gini means more inequality. **Four shortcomings** listed', 'Section 4', 'The handout gives each with "The Concept" and "The Explanation".'],
    ['Modern reasoning: it is about the **nature** of inequality, and the **rule of law** decides it', 'Section 5', 'A Mains theme. The handout stresses that rule of law is more than a law.'],
    ['**Trickle-down works only if four conditions hold;** inclusive growth rests on **capability and opportunity**', 'Sections 7-8', 'A compare-and-contrast Mains question. The handout says the two are "essentially the same" with different emphasis.'],
    ['Skill and inclusion readings named: National Skill Development Programme, PMKVY, Jan Dhan, Mudra, Economic Survey 2025-26', 'Section 8', 'The handout points to these for further reading.'],
])
c.call('key', 'What to prepare', [
    '**Prelims hooks:** Kuznets versus Lorenz; the Lorenz plotting steps and what the equality line OP and the line QP mean; the Gini formula and range; the four Gini shortcomings; the four conditions for trickle-down; the two pillars of inclusive growth.',
    '**Mains hooks:** causes of inequality (natural, Marxist, modern); why growth causes inequality; why trickle-down fails; why inclusive growth is about claim, not charity; the rule-of-law argument.',
    '**Closing idea:** some inequality comes with growth, but its kind decides the outcome. Good inequality (earned by fair means under rule of law) is tolerable; bad inequality (from connections and weak law) hurts everyone.'])

c.sec('1 · What is inequality?')
c.p('**Inequality is differences in the degree of attainment on various aspects of well-being.** Example: one person lives where there is one hospital per 5 km² and another where there are two. Neither is probably facing pronounced deprivation, but the second\'s attainment is better than the first\'s. That is inequality. (Poverty is about a floor; inequality is about differences above it.)')
c.ul([
    'It can be economic, social or political, but it is generally **measured through economic differences:** income, expenditure and wealth.',
    'Like poverty, the preferred method is **consumption expenditure (CE).**',
    'Inequality measured through **wealth** is generally higher. But wealth and income are less truthfully revealed and highly volatile, so **CE-based inequality, even though lower, is generally the most objective.**',
    'The government generally measures **consumption inequality** because it lacks verifiable, regularly collected data on other measures.'])

c.sec('2 · Kuznets curve: a theory')
c.p('The Kuznets curve is a **theoretical prediction** about how inequality relates to incomes in a society over time. Kuznets predicts that **as incomes rise, inequality first rises** (incomes of some grow faster than others), then **stabilises,** and eventually **corrects.**')
c.fig('eco-kuznets.jpg', 'Hand-drawn Kuznets curve: inequality on the vertical axis, income on the horizontal axis. An inverted U with three phases marked A, B and C.')
c.ul(['It is **not a data-based curve,** only a theoretical expectation.', 'The phases **A, B, C are not necessarily of equal or proportional lengths.**'])
c.call('alert', 'Handout alert: what the curve shows', 'The handout gives the shape as rise, stabilise, correct. It labels the phases A, B, C on the sketch but does not define each one separately. **Rule for the exam hall:** call it a theoretical, inverted-U expectation, never a measured curve.')

c.sec('3 · Lorenz curve: a data-based picture')
c.p('The Lorenz curve (LC) is a **data-based representation** of existing inequality in income, CE or wealth.')
c.flow([
    ('1 · Collect data', 'Income, CE or wealth, from the population or a sample'),
    ('2 · Sort it', 'Generally in descending order (the handout\'s wording)'),
    ('3 · Divide into equal-sized groups', 'For example 5 groups of 20% of the population'),
    ('4 · Find each group\'s share', 'Total income of the group, hence its share in total income'),
    ('5 · Plot cumulative shares', 'Example: bottom 20% have 3%, next 20% have 7%, so bottom 40% have a cumulative 10%. Join the points', 'good'),
], 'How to plot the Lorenz curve')
c.fig('eco-lorenz-chart.jpg', 'Lorenz curve of income distribution. The diagonal is the line of perfect equality. Points: bottom 20% earn 3% cumulative, bottom 40% earn 10%, bottom 60% earn 25%, bottom 80% earn 50% (in this chart the last point shown is 50%).')
c.fig('eco-lorenz-sketch.jpg', 'Hand-drawn sketch from the handout: the equality line OP, the Lorenz curve, and the right-angle line OQP for perfect inequality. Example: the bottom 80% have a share of 40% of total income.')
c.call('alert', 'Handout alert: two examples, different numbers', 'The text example says bottom 20% have 3%, bottom 40% have 10%. The chart printed beside it labels bottom 80% as 50% cumulative, while the written example beneath the sketch says bottom 80% have **40%.** They are two different illustrations. **Rule for the exam hall:** do not quote a number from these pictures; explain the method and the two extreme lines.')
c.table('Reading the curve', ['Case', 'What the LC looks like'], [
    ['**Perfect equality**', 'Every group has the same share as any other group of the same size. The LC is the **x = y line, OP:** the **line of perfect equality**'],
    ['**Perfect inequality**', 'One person has all the income, so the rest have zero. The LC runs along the **x-axis** until the very last point, then rises vertically: **OQP, or simply QP**'],
    ['**A real country**', 'Lies between the two. **The closer to the equality line, the more equal;** the farther away, the less equal'],
], rowhead=True)

c.sec('4 · Gini coefficient and its four shortcomings')
c.p('The Gini coefficient is a statistical measure of inequality calculated using the Lorenz curve. Let **A** be the area between the line of equality and the Lorenz curve, and **B** the area below the Lorenz curve.')
c.fig('eco-lorenz-gini.jpg', 'Lorenz curve with areas A (between the equality line and the curve) and B (below the curve). Gini = A / (A + B).')
c.call('teacher', 'Formula', '**Gini (GC) = Area between equality line and Lorenz curve / Area between equality line and inequality line = A / (A + B).**')
c.ul(['**Range:** 0 when A = 0 (perfect equality) to 1 when B = 0 (perfect inequality).', '**An increase in Gini means an increase in inequality.**'])
c.table('Shortcomings of the Gini (the handout\'s four)', ['Shortcoming', 'The concept', 'The handout\'s explanation'], [
    ['**1 · Not easily decomposable or additive**', 'You cannot do simple maths with Ginis to see the bigger picture', 'Average incomes of two states combine easily into one average. Ginis do not: State A at 0.3 and State B at 0.4 do **not** combine to 0.35. The maths is complex, so policymakers cannot easily say which region or sector drives overall inequality'],
    ['**2 · Different distributions can give the same Gini**', 'One number hides the **shape** of society', 'Society A: starving lower class, wealthy middle class, no billionaires. Society B: comfortable lower and middle class, but a few trillionaires hoarding half the wealth. Both could score **0.40,** yet feel completely different'],
    ['**3 · Reacts differently to transfers at the tails than in the middle**', 'Over-sensitive to the middle class, somewhat **blind to the extremes**', 'A ₹10,000 gift between two middle-class people visibly improves the Gini. A multi-billionaire taking ₹10,000 from a destitute beggar (a transfer at the tails) barely moves it. It misses rising concentration at the very top'],
    ['**4 · Hides demographic variation among subgroups**', 'Blind to **who** the rich and poor are', 'A "low" Gini cannot show whether the old hold 90% of the wealth while youth face poverty, or whether one racial group or caste earns far less. It throws everyone into one pot'],
])

c.sec('5 · Why does inequality exist?')
c.h3('(1) Natural advantages')
c.p('These are **accidents of birth or location** that give some people a better chance at well-being: birth in a family of means or higher social status, better networks, inherited wealth. A place with better geography and fewer adverse events has better access to health, education and livelihood. **Most inequalities can be explained by natural advantages or disadvantages,** and they cannot be wished away.')
c.p('But they cannot explain everything. Siblings in the same household can have very different outcomes. That is explained by **comparative advantages and disadvantages:** also natural, but not apparent at first. Example: an elder sibling is given responsibility earlier and is better prepared for such roles; a younger sibling may lean toward artistic or talent-based pursuits.')
c.h3('(2) Economic reasons: the Marxist view')
c.ul([
    'Marx: inequality results from **differences in the ability of different groups to enforce their interests.** The groups are those with **capital** and those with **labour,** and the interest is to take a larger share of revenue as **profits versus wages.**',
    'A firm gets factors of production as capital (entrepreneurship, capital, land) and labour. Revenue is split into wages and the retained profit. Both sides want a larger share.',
    '**Capital is scarce and labour abundant,** so labour\'s ability to bargain is low. Capital is concentrated in few hands, so providers keep a larger share as profit.',
    'To some extent this is fair: capital takes greater risk and deserves higher reward. But as revenue rises, **profit\'s share keeps increasing while wages rise slowly,** so initial inequalities **compound** over time. That growing inequality is the problem, according to Marx.'])
c.h3('(3) Modern reasoning')
c.p('**a. A critique of the Marxist view.** The handout says Marxist reasoning has **survivorship bias:** it uses only the information that is visible.')
c.ul([
    'Profits do rise faster than wages at a broad level. But adjust profits for the **losses of firms that shut down** and the growth rate is not very different.',
    '**Most firms that start today shut down within 10 years.** Marxist reasoning considers only profit, which belongs to the firm that survives.',
    'There are periods when profits decline but wages do not. Over a longer term, **profits and wages grow at a similar rate.**',
    'Why do profits still rise quickly? Surviving firms grow because of market growth **and** because of **larger market share after other firms close.** Wages grow only with market size, since the number of workers stays mostly stable.',
    'Marxism is "obviously not wrong" (it rightly points to unequal ability to enforce interests) but it underplays the **low survival rate of firms** versus a stable worker count.',
    'So firms see that the key to exceptional profit is **survival and market share.** The **means** they choose decide the kind of inequality a society has.'])
c.p('**b. The political-legal system: the rule of law.** Every firm wants to survive and to monopolise; when market share rises, profits rise sharply. There are two routes to more share:')
c.table(None, ['', 'Fair means', 'Unfair means'], [
    ['What firms do', 'Better goods and services through **R&D,** risk-taking, innovation, hiring skilled workers and paying them well', 'Exploit position and **connections with lawmakers and enforcers,** making it hard for others to compete'],
    ['Under a **strong** rule of law', 'Firms are pushed to this route, since connections are not exploited and violators are punished', 'Strong disincentive'],
    ['Under a **weak** rule of law', 'Fair players fall; wrongdoers get away', 'Firms lack integrity and ignore workers, consumers, minority shareholders and society'],
    ['Outcome', 'They still monopolise and inequalities emerge, but society benefits. Such inequality is tolerable and "**good**"', 'Everyone loses except the owners (and only briefly). Inequality gives **bad** outcomes'],
])
c.call('teacher', 'The modern point', '**Modern reasoning is less about why inequality exists anywhere and more about why a certain kind of inequality exists in some places that gives the worst outcomes for everyone. It is about its nature.**')
c.call('note', 'What is "rule of law"?', ['It is **not merely a law or some laws.** It is a **collective environment of institutions** that frame, execute and adjudicate the laws. The people and institutions must be competent **and** act fairly and without bias.', 'Example: the **Competition Act, 2002** aims to prevent monopolies through unfair practices. But many entities decide what a monopoly is, what is fair, and what to do about it. The Act is **one aspect** of the rule of law; how it is applied decides whether the rule of law exists.'])

c.sec('6 · Growth and inequality')
c.ul([
    '**Growth, by its design, is inequality-causing.** Faster growth happens when limited resources go where growth potential is higher, in sectors or places that can use them more efficiently.',
    'Faster growth means **more employment and a faster fall in poverty,** which is desirable.',
    'But if resources are focused on certain sectors, regions or industries, the incomes of those grow faster, so **inequality rises.** Growth is "not without its costs".',
    'To correct this, governments have tried models of growth that aim for **faster growth with less inequality.** The handout stresses these are **not mathematical models** but **general policy approaches,** and by the end you see both are **essentially the same,** differing in emphasis.'])

c.sec('7 · Trickle-down approach')
c.p('The intent is **focus:** maximum output in least time. The government focuses scarce economic, technological, human and natural resources, through policy, on sectors or regions with potential for faster growth. The expectation is a **multiplier effect:** one sector grows and pulls the whole economy up, while evenly spread resources would give only an average rate.')
c.ul(['Benefits **can trickle down** naturally to nearby areas, sectors and people, but it may take a long time, and those left out just keep waiting.', 'So the government **accelerates** it by **redistributing** benefits to those at the bottom.'])
c.table('Four conditions for trickle-down to work', ['#', 'Condition'], [
    ['1', '**The chosen sector grows**'],
    ['2', 'The government is able to collect more **taxes** from that growth (**high taxation efficiency**)'],
    ['3', 'The government **decides to redistribute,** i.e. spends on those left out instead of reinvesting in the same or a related sector'],
    ['4', '**Efficiency of redistribution is high:** benefits reach the intended beneficiaries'],
])
c.call('alert', 'Why it often fails', 'If any condition fails, trickle-down does not happen and the inequalities created **become permanent.** More often than not these assumptions fail, so inequalities persist and are even **created by the approach.** It is **not an anti-poor model,** but a well-meant pursuit of growth ends up creating more inequality. This leads to the inclusive approach.')

c.sec('8 · Inclusive growth')
c.p('The handout calls trickle-down a **pro-poor** model that relies on the government moving the benefits of growth to the bottom. Being "brutally honest": the benefits do not **rightfully** belong to the bottom, since they did not contribute to growth, which is driven largely by those at the top. The top contributes and so **keeps most of the benefits.** The bottom\'s only "sacrifice" was not getting special policy focus, and schemes for the poor are a payment for it. So the poor get benefits only at the **government\'s discretion,** transfers often fail and inequality stays.')
c.p('**Inclusive growth** is based on the premise that growth should be **broad-based:** it must include as many sections of society and the economy as possible, driven not only by the top but also by the bottom. The aim is to move those at the bottom from **passive recipients** of growth\'s benefits to **active contributors,** with a rightful claim on its fruits. It has **two pillars:**')
c.lanes([
    ('Pillar 1 · Capability', [
        ('Identify the poor and vulnerable', ''),
        ('Identify backward regions', ''),
        ('Find key reasons for backwardness or vulnerability', 'Disasters, poor health and nutrition, weak institutions including economic ones like agricultural markets, youth migration'),
        ('Focused interventions based on those reasons', ''),
        ('Skills, basic healthcare, quality education for all', 'Skills are dynamic, so link them to evolving industry needs, with incentives and hand-holding'),
    ]),
    ('Pillar 2 · Opportunity', [
        ('Job creation through industrial development', 'Especially labour-intensive industry'),
        ('Shift from job-seeking to job-creating', 'An entrepreneurship culture'),
        ('Improve ease of doing business (EoDB)', 'Contract enforcement (judicial reforms), easier registration, land acquisition'),
        ('Reduce or share entrepreneurial risk', ''),
        ('Access to capital', 'For example guarantees to banks on the borrower\'s behalf; this needs **financial inclusion**'),
    ]),
], 'The two pillars of inclusive growth')
c.call('teacher', 'Behavioural point', ['Interventions must recognise **behaviour.** "The government should build more schools" is not enough. Ask why children are not going to school. Are teachers skilled and qualified? Are there separate girls\' washrooms? Can poor families afford the incidental costs?', 'Skills are dynamic, so link them to evolving industry requirements and recognise the need for **incentives and hand-holding.**'])
c.table('Trickle-down versus inclusive growth', ['', 'Trickle-down', 'Inclusive growth'], [
    ['Idea', 'Focus resources on high-growth sectors; let benefits reach the bottom', 'Broad-based growth that includes the bottom as **contributors**'],
    ['Bottom\'s position', 'Passive recipient of benefits', 'Active contributor with a rightful claim'],
    ['Role of government', 'Redistributes benefits (at its discretion)', 'Builds **capability** and provides **opportunity**'],
    ['Weakness', 'Fails if any of four conditions fails; inequality becomes permanent', 'Takes effort on skills, institutions, credit and enterprise'],
], rowhead=True)
c.call('note', 'Reading named in the handout', ['Students may refer to the **National Skill Development Programme, PMKVY** and the **Economic Survey 2025-26** discussion on skill development, health and education.', 'For opportunities, refer to **Jan Dhan Yojana, Mudra Yojana** and Economic Survey 2025-26 on support to industry.', '**Important note:** the handout says it will return to inequality when it turns to different kinds of economies, and will discuss inclusive growth much more in later chapters. "This is just the beginning."'])

c.mm = ('Inequality', [
    ('What it is', [('Differences in attainment', 'hospital per 5 km2 example'), ('Measured by income, CE, wealth', None), ('CE is most objective', None)]),
    ('Kuznets curve', [('Theory, not data', None), ('Inequality rises, stabilises, corrects', None), ('Phases A, B, C unequal', None)]),
    ('Lorenz curve', [('Data-based', None), ('Sort, group, share, cumulate', None), ('OP = equality, QP = perfect inequality', None)]),
    ('Gini', [('A / (A + B)', None), ('0 to 1', 'higher = more unequal'), ('Four shortcomings', 'not additive, same Gini, tails, subgroups')]),
    ('Causes', [('Natural advantages', 'birth, place, comparative'), ('Marx: capital vs labour', None), ('Modern: survivorship, firm survival', None), ('Rule of law: fair vs unfair means', 'Competition Act 2002')]),
    ('Growth models', [('Growth causes inequality', None), ('Trickle-down: 4 conditions', None), ('Inclusive: capability + opportunity', None)]),
])

c.timeline = [
    ('2002', 'Competition Act: the handout\'s example of a law that is only one part of the rule of law', False),
    ('2011-12', 'Consumption-based Gini 28.8 (from the handout\'s summary in Chapter 1)', False),
    ('2022-23', 'Consumption-based Gini 25.5', False),
    ('2023-24', 'Median earnings of the top 10% are 13 times those of the bottom 10%', True),
    ('2025-26', 'Economic Survey 2025-26: the handout\'s pointer for skills, health, education and support to industry', False),
]

c.connects = [
    ('[Chapter 1: Poverty](eco-ch01.html)', 'Relative poverty reflects inequality; the PGI ignores inequality among the poor; the Gini fell from 28.8 to 25.5 (2011-12 to 2022-23) in the Chapter 1 summary.'),
    ('Unemployment handout (next in your PDF)', 'Refers back to "our discussion on inclusive growth" and to the same schemes. The capability pillar (skills) and opportunity pillar (jobs) are the structure behind youth unemployment.'),
    ('National Income Accounting handout', 'Covers the Inequality-adjusted HDI (IHDI), which discounts HDI for inequality in health, education and income: the Gini and Lorenz ideas at work in a development index.'),
    ('Banking and NBFCs handout', 'Financial inclusion (PM Jan Dhan Yojana, 2014) is the "access to capital" requirement of the opportunity pillar.'),
    ('Budget and Fiscal Policy handout', 'Redistribution, taxation and who should receive free foodgrains are the fiscal side of trickle-down conditions 2 to 4.'),
]

c.recall = [
    'Inequality = differences in attainment on aspects of well-being. Measured through consumption expenditure (most objective); wealth inequality is higher but less reliable.',
    'Kuznets curve: theory, not data. Inequality rises, stabilises, then corrects as incomes rise. Phases A, B, C unequal.',
    'Lorenz curve: data-based. Sort, group, find shares, plot cumulative. OP = equality line; QP (OQP) = perfect inequality.',
    'Gini = A/(A+B); 0 to 1; up = more inequality.',
    'Four Gini shortcomings: not decomposable; same Gini for different distributions (0.40 example); tails versus middle transfers; no demographic detail.',
    'Causes: natural advantages (birth, place, comparative); Marx (capital versus labour, compounding); modern (survivorship bias, firm survival, market share); rule of law (fair versus unfair means, Competition Act 2002, good versus bad inequality).',
    'Growth causes inequality by focusing resources; models try to keep growth with less inequality.',
    'Trickle-down: four conditions (sector grows, tax efficiency, decision to redistribute, redistribution efficiency). Fails often; inequality becomes permanent.',
    'Inclusive growth: capability (identify poor and regions, reasons, focused interventions, skills, health, education) and opportunity (jobs, entrepreneurship, EoDB, risk sharing, capital with financial inclusion).',
    'Blank page: draw Lorenz with OP and QP, shade A and B, then write the four shortcomings.',
]

c.mcq = [
    {'q': 'Which statement about the Kuznets curve is correct, according to the handout?', 'options': ['It is plotted from survey data', 'It is a theoretical expectation, not a data-based curve', 'It shows the share of income of each population group', 'It is a measure of the gap between the rich and the poor'], 'answer': 1, 'explain': 'Kuznets predicts rising, then stabilising, then falling inequality as incomes rise. It is theory.'},
    {'q': 'The Lorenz curve is...', 'options': ['a theoretical prediction', 'a data-based representation of existing inequality', 'a measure of poverty depth', 'a price index'], 'answer': 1, 'explain': 'It is built from data on income, CE or wealth.'},
    {'q': 'In a Lorenz diagram, perfect equality is shown by...', 'options': ['the x-axis', 'the x = y line OP', 'the vertical line at 100%', 'any curve below OP'], 'answer': 1, 'explain': 'Every group has the same share as any other group of the same size.'},
    {'q': 'Perfect inequality (one person has everything) makes the Lorenz curve...', 'options': ['run along the x-axis and then rise vertically (QP)', 'coincide with the diagonal', 'run along the y-axis', 'become a straight line with slope 2'], 'answer': 0, 'explain': 'The remaining population has zero share, so the curve stays at zero until the very last point.'},
    {'q': 'Gini coefficient is calculated as...', 'options': ['B / (A + B)', 'A / (A + B)', 'A x B', 'A - B'], 'answer': 1, 'explain': 'A is the area between the equality line and the Lorenz curve; A + B is the area under the equality line.'},
    {'q': 'The Gini coefficient varies between...', 'options': ['-1 and 1', '0 and 100', '0 (perfect equality) and 1 (perfect inequality)', '1 and 10'], 'answer': 2, 'explain': '0 when A = 0; 1 when B = 0.'},
    {'q': 'State A has Gini 0.3 and State B has 0.4. Combined, the Gini is...', 'options': ['exactly 0.35', 'not simply an average: Gini is not easily decomposable', 'always 0.4', 'always 0.3'], 'answer': 1, 'explain': 'The handout\'s first shortcoming: Gini is not additive.'},
    {'q': 'A multi-billionaire takes ₹10,000 from a destitute person. The Gini will...', 'options': ['rise sharply', 'fall sharply', 'barely change', 'become zero'], 'answer': 2, 'explain': 'Gini is sensitive to the middle of the distribution and nearly blind to the tails.'},
    {'q': 'Which is NOT one of the handout\'s Gini shortcomings?', 'options': ['It is not easily decomposable', 'Different distributions can give the same value', 'It cannot be computed from a Lorenz curve', 'It hides demographic variation among subgroups'], 'answer': 2, 'explain': 'Gini is calculated from the Lorenz curve. The other three are listed shortcomings.'},
    {'q': 'Why does the government generally measure consumption inequality?', 'options': ['Consumption is more equal than wealth and verifiable data exists', 'Wealth data is published every month', 'The law forbids measuring wealth', 'Consumption is always higher'], 'answer': 0, 'explain': 'Wealth and income are less truthfully revealed and volatile; CE-based inequality is the most objective.'},
    {'q': 'According to Marx, inequality arises from...', 'options': ['differences in ability to enforce interests between capital and labour', 'differences in climate', 'government subsidies', 'inflation'], 'answer': 0, 'explain': 'Capital is scarce and concentrated; labour is abundant, so labour bargains poorly and profit share compounds.'},
    {'q': 'The handout\'s critique of Marxist reasoning is that it suffers from...', 'options': ['sampling error', 'survivorship bias', 'inflation bias', 'selection of wrong currency'], 'answer': 1, 'explain': 'It counts only profits of surviving firms; most firms shut down within 10 years.'},
    {'q': 'In the modern reasoning, what decides whether firms use fair or unfair means?', 'options': ['Strength of the rule of law', 'The size of the labour force', 'The exchange rate', 'The tax rate alone'], 'answer': 0, 'explain': 'Strong rule of law discourages unfair means; weak rule of law rewards connections.'},
    {'q': 'Which of the following is NOT a condition for trickle-down to succeed?', 'options': ['The chosen sector grows', 'The government collects more tax from the growth', 'Benefits are kept within the same sector', 'Redistribution efficiency is high'], 'answer': 2, 'explain': 'The government must decide to redistribute, not reinvest in the same or a related sector.'},
    {'q': 'The two pillars of inclusive growth are...', 'options': ['Taxation and subsidy', 'Capability and opportunity', 'Savings and investment', 'Trade and aid'], 'answer': 1, 'explain': 'Give people capability to contribute and opportunities in which to contribute.'},
    {'q': 'In inclusive growth the bottom of society moves from...', 'options': ['active contributor to passive recipient', 'passive recipient to active contributor', 'employer to employee', 'saver to borrower'], 'answer': 1, 'explain': 'The aim is a rightful claim on the fruits of growth, not discretionary transfers.'},
]

c.mains = [
    ('Distinguish the Kuznets curve from the Lorenz curve. How is the Gini coefficient derived from the latter?',
     'One is a theory about how inequality moves with income, the other is a picture of inequality at a point in time.',
     ['Kuznets: theoretical, not data-based; inequality rises, stabilises, corrects; phases unequal.', 'Lorenz: data-based; sort, group, find shares, plot cumulative shares.', 'Equality line OP; perfect inequality QP.', 'Gini = A/(A+B), range 0 to 1.'],
     'Kuznets tells a story, Lorenz shows the facts, and Gini compresses the facts into a number.'),
    ('"The Gini coefficient alone cannot describe inequality." Discuss.',
     'A single number can hide the shape and the people behind it.',
     ['Not decomposable: states\' Ginis cannot be simply averaged.', 'Same Gini, different societies (0.40 example).', 'Insensitive to transfers at the tails; sensitive in the middle.', 'Blind to age, race, caste and other subgroups.', 'So use Lorenz, subgroup data and wealth concentration along with it.'],
     'Use Gini as a thermometer, not a diagnosis.'),
    ('Why does inequality exist? Compare the Marxist and modern explanations.',
     'Inequality has natural, economic and institutional roots.',
     ['Natural advantages: birth, place, comparative advantages between siblings.', 'Marx: capital versus labour bargaining; profits compound.', 'Modern: survivorship bias; firms seek survival and market share.', 'Means chosen decide the nature of inequality: fair versus unfair, set by rule of law (Competition Act 2002 is one part only).'],
     'The question is not whether inequality exists but what kind.'),
    ('Why does growth cause inequality? Why does trickle-down often fail?',
     'Growth concentrates scarce resources where returns are highest.',
     ['Focus on high-potential sectors raises their incomes faster.', 'Trickle-down needs four conditions: sector grows, tax efficiency, decision to redistribute, redistribution efficiency.', 'When one fails, inequality becomes permanent.', 'Benefits reach the poor only at government discretion.'],
     'Trickle-down hopes the benefit flows down; it has no way to make it.'),
    ('Explain inclusive growth. How does it improve on the trickle-down approach?',
     'Inclusive growth makes the poor contributors to growth, not recipients of charity.',
     ['Premise: broad-based growth with a rightful claim for all.', 'Capability: identify poor and regions, causes, focused interventions, skills, health, education, recognising behaviour.', 'Opportunity: labour-intensive jobs, entrepreneurship, EoDB, risk sharing, access to capital (financial inclusion).', 'Both approaches are essentially the same with different emphasis.'],
     'Growth is inclusive when the bottom helps make it and so rightfully shares it.'),
]

c.cards = [
    ('Define inequality.', 'Differences in the degree of attainment on various aspects of well-being.'),
    ('Why is CE used to measure inequality?', 'Wealth and income are less truthfully revealed and volatile; CE is the most objective and verifiable.'),
    ('Is inequality higher on wealth or consumption?', 'Higher on wealth; CE-based inequality is lower but most objective.'),
    ('Kuznets curve in one line?', 'Theory: as incomes rise, inequality rises, stabilises, then corrects. Not data-based.'),
    ('Kuznets phases A, B, C?', 'Not necessarily equal or proportional in length.'),
    ('Lorenz curve: data or theory?', 'Data-based.'),
    ('Steps to plot a Lorenz curve?', 'Collect data, sort, divide into equal groups, find each group\'s share, plot cumulative shares.'),
    ('Line OP in the Lorenz diagram?', 'Line of perfect equality (x = y).'),
    ('Line QP (OQP)?', 'Perfect inequality: zero share until the last point, then vertical.'),
    ('Gini formula?', 'A / (A + B): area between equality line and Lorenz curve over area under the equality line.'),
    ('Gini range and direction?', '0 (perfect equality) to 1 (perfect inequality); higher means more inequality.'),
    ('Gini shortcoming 1?', 'Not easily decomposable or additive.'),
    ('Gini shortcoming 2?', 'Different distributions can have the same Gini (0.40 example).'),
    ('Gini shortcoming 3?', 'Responds differently to transfers in the middle than at the tails.'),
    ('Gini shortcoming 4?', 'Does not show demographic variations among subgroups.'),
    ('Natural advantages?', 'Accidents of birth or location giving better outcomes; comparative advantages explain sibling differences.'),
    ('Marxist explanation?', 'Capital versus labour ability to enforce interests; scarce concentrated capital keeps profit; inequality compounds.'),
    ('Survivorship bias in the Marx critique?', 'Uses only profits of surviving firms; most firms shut in 10 years; adjusted for losses, growth is similar.'),
    ('Why do profits rise fast?', 'Market growth plus more market share after rivals close; wages grow only with market size.'),
    ('Two routes to market share?', 'Fair means (R&D, risk, skilled pay) and unfair means (connections with lawmakers and enforcers).'),
    ('What decides which route firms take?', 'The strength of the rule of law.'),
    ('Good versus bad inequality?', 'Good: society benefits (fair means, strong rule of law). Bad: weak rule of law, everyone loses except owners briefly.'),
    ('Is rule of law just a law?', 'No: a collective environment of institutions that frame, execute and adjudicate laws, acting fairly and without bias.'),
    ('Competition Act 2002 in this chapter?', 'Example of one aspect of rule of law; application decides whether rule of law exists.'),
    ('Why does growth cause inequality?', 'Resources focus on high-potential sectors or regions, whose incomes rise faster.'),
    ('Trickle-down: the intent?', 'Focus resources for maximum output in least time; multiplier effect.'),
    ('Four conditions for trickle-down?', 'Sector grows; tax efficiency high; government decides to redistribute; redistribution efficient.'),
    ('Why does inclusive growth reject discretionary benefits?', 'The bottom did not contribute, so benefits depend on government discretion and often fail.'),
    ('Inclusive growth premise?', 'Broad-based growth; move the bottom from passive recipients to active contributors with a rightful claim.'),
    ('Two pillars of inclusive growth?', 'Capability and opportunity.'),
    ('Capability includes?', 'Identify poor and regions, find reasons, focused interventions, skills, healthcare, education.'),
    ('Opportunity includes?', 'Labour-intensive jobs, job creators not job seekers, EoDB, risk sharing, access to capital (financial inclusion).'),
    ('Readings named for inclusive growth?', 'National Skill Development Programme, PMKVY, Jan Dhan, Mudra, Economic Survey 2025-26.'),
]
