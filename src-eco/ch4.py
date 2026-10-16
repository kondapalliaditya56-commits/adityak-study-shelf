from lib import Ch

c = Ch(4, 'Basic Concepts of Economics: PPF, Goods and Capital',
       'Economy · GS Foundation · Chapter 4',
       [('hb', 'Handout only: no class slides'), ('', 'Handout pages 1-20'), ('', '1 Prelims PYQ quoted')],
       'The economist’s job, the production possibilities frontier, marginal cost and opportunity cost, free-market versus command systems, the types of goods (necessary, luxury, normal, inferior, substitute, complement, merit, demerit, Giffen, Veblen, private, public, intermediate, final, consumer, capital), fixed and working capital, investment and gross capital formation, and depreciation versus CFC versus CCA.')

c.sec('Exam lens: priority and PYQs', 'exam-lens-priority-and-pyqs')
c.call('alert', 'Source note', ['**Handout only.** No class slides and no teacher ink. The handout ends with **one** Prelims PYQ (2021). **Mains PYQs: none quoted in the material.** The chapter is the foundation for National Income Accounting (the handout ends with “Now we are ready to formally begin: National Income Accounting”).'])
c.table('Prelims PYQ quoted in the handout', ['Year', 'What was asked', 'Answer in handout', 'Where covered'], [
    ['2021', 'Other things unchanged, market demand for a good might increase if: 1) price of its substitute increases 2) price of its complement increases 3) it is an inferior good and income rises 4) its price falls', '(a) 1 and 4 only', 'Section 4: substitutes (positive cross-price effect), complements (negative), inferior goods (demand falls as income rises), law of demand']], rowhead=False)
c.table('What the handout stresses', ['Signal in the handout', 'Where', 'Why it matters'], [
    ['Production boundary: a good is final or intermediate by **economic modification,** not by its physical form. Salt for a household is final; salt for a hotel is intermediate', 'Section 6', 'A classic Prelims trap; the base of GDP counting'],
    ['“Investment” in economics is **spending on capital goods** (a flow), not buying shares or gold. Capital is a stock', 'Section 8', 'Asterisked statement; flow versus stock'],
    ['Depreciation (historical cost) versus CFC (current replacement cost) versus CCA (tax rule)', 'Section 9', 'Three similar terms with three different owners'],
    ['Giffen goods are inferior goods under special circumstances; Veblen goods are ultra-luxury', 'Section 4', 'Both break the law of demand'],
    ['Public goods: non-excludable and non-rival, so free-rider problem and market failure', 'Section 5', 'Marked with a star in the handout'],
])
c.call('key', 'What to prepare', [
    '**Prelims hooks:** PPF is normative and dynamic; MC versus OC; elasticity-based and income-based classes of goods; cross-price sign for substitutes and complements; merit versus demerit (externalities); Giffen versus Veblen; excludability and rivalry grid; intermediate versus final; capital versus working capital; GFCF, change in inventory and valuables; net investment; depreciation, CFC, CCA.',
    '**Mains hooks:** why decentralised and command systems both fail in some way (inequality, information problem, rent-seeking); why governments provide public goods; opportunity cost in public spending.',
    '**Closing idea:** economics does not say what to choose; it shows what you give up by choosing.'])

c.sec('1 · The economist’s task: budget, technology and the PPF')
c.p('The economic problem is **limited resources and unlimited wants.** The economist cannot create more resources or reduce desires, and is not the decision-maker. The **decision-maker** (a person, family, firm, community or government) chooses; the economist’s main task is to **advise** whether the current use of resources is optimal. He first assesses two things:')
c.ul(['**(a) Budget constraints:** the resources that actually **limit** output. All resources are limited, but only some are limiting (for a farmer it may be water or fertiliser, not seeds).',
      '**(b) The prevailing technology:** the current manner of using resources (stone tools, iron tools, tractors and harvesters).'])
c.p('Given these, the decision-maker has many options (chairs or tables, tobacco or mango or wheat). The economist estimates the **maximum sustainable output** for each possibility. That is the **Production Possibilities Frontier (PPF).**')
c.table('The handout’s hunter-gatherer PPF (8 hours of daylight)', ['Scenario', 'Deer hunted', 'Berries gathered'], [
    ['A', '10', '0'], ['B', '8', '200'], ['C', '6', '380'], ['D', '4', '530'], ['E', '2', '630'], ['F', '0', '700']], rowhead=True)
c.p('Reading the table (simple arithmetic on the handout’s figures): every 2 fewer deer buys 200, 180, 150, 100 and then 70 more berries. Each sacrifice buys less than the one before.')
c.ul([
    'The **PPF is a normative concept:** every economist has an assessment. Actual output is a **fact;** the PPF is a “sustainable-potential” benchmark.',
    '**Below the PPF:** possible but not desirable. **Beyond the PPF:** desirable but not sustainably possible (working 15 hours a day).',
    'It is **not cast in stone:** better technology pushes it out. Today there are “less deer but more bullets”: time is no longer the constraint, the number of deer is.',
    'The economist’s key role: help society reach the PPF, an output both **desirable and sustainably possible.**'])

c.sec('2 · The two tools: marginal cost and opportunity cost')
c.table('Marginal cost versus opportunity cost', ['', 'Marginal cost (MC)', 'Opportunity cost (OC)'], [
    ['**Meaning**', 'The actual, tangible cost of producing **one more unit** at the current level of output', 'The **benefit foregone** when a choice is made: the value of the **next best alternative** given up'],
    ['**Nature**', 'Resources actually spent', 'A **conceptual** cost, not necessarily financial'],
    ['**Use**', 'Prevents overreach: the best resources are used first, so more output becomes harder and dearer. A high MC is justified only if the marginal benefit is equally high', 'Forces the decision-maker to look past visible results to what was sacrificed'],
    ['**Handout example**', 'Stadium: cement, steel and labour bought', 'Stadium: the rural hospital or school that the same resources could have built'],
], rowhead=True)
c.call('teacher', 'Handout stress', 'The handout calls opportunity cost “arguably the most powerful concept in all of economics” and “the ultimate reality check on human intentions.” Economics “has no morals”: it does not say hospitals are better than stadiums, only that choosing the stadium means choosing **not** to have the hospital.')

c.sec('3 · Systems of resource allocation: decentralised versus centralised')
c.table('Two extremes (seen as systems of information and incentives)', ['', 'Decentralised (libertarian, free market)', 'Centralised (authoritarian, command)'], [
    ['**Core mechanism**', 'Individuals have liberty to own, trade and allocate. Millions of consumers and producers use **prices** as signals', 'An **authority** (king, dictator, politburo, feudal lord, even an elected government with such powers) directs the use of resources. Central planning replaces the market'],
    ['**Role of the state**', '**Laissez-faire.** Only the “invisible infrastructure”: rule of law, private property, contract enforcement, truthful information, preventing fraud and violence, minimal regulation (car safety standards)', 'Controls or directs resources; intent is “deeply moral”: equitable, socialist distribution and protecting the vulnerable'],
    ['**Incentive**', 'Self-interest (Adam Smith): to profit, a producer must offer what society values. Self-interest gives collective well-being: the **invisible hand.** Market punishes waste and rewards competence', 'The state cannot meet all demands, so it appoints private entities as **state-created monopolies** (licences, quotas). The incentive shifts from serving consumers to **being connected:** **rent-seeking** (cronyism)'],
    ['**Critique**', 'People differ in capabilities, capital and luck, so the capitalists come to dominate. Raises absolute wealth but produces **high inequality** from natural advantages', '**Information problem:** no planner can know the subjective wants and opportunity costs of millions. Designed to reduce inequality, it creates a **rigid, worse kind** (wealth goes to the politically connected, and even a more competent producer is denied)'],
], rowhead=True)
c.call('teacher', 'The trade-off', 'A state that enforces equality must use authoritarian force to confiscate and redistribute, crushing incentives. The handout quotes Milton Friedman: “A society that puts equality before freedom will get neither. A society that puts freedom before equality will get a high degree of both.” And George Bernard Shaw on communism at 20 and capitalism at 30. **None of the systems is perfect.**')

c.sec('4 · Types of goods: applying demand and supply')
c.table('Goods classified by how demand behaves', ['Pair', 'Defining behaviour', 'Curve', 'Examples'], [
    ['**Necessary** vs **Luxury** (price elasticity)', 'Necessary: high utility, **inelastic**; a big price change barely moves Qd. Luxury: lower utility, **elastic**; demand rises a lot when price falls slightly', 'Necessary: steep (near vertical). Luxury: flat (near horizontal)', 'Staples, life-saving drugs, salt vs high-end home décor, premium electronics, vacation packages'],
    ['**Normal** vs **Inferior** (income elasticity)', 'Normal: demand rises with income, curve shifts **right.** Inferior: demand actively **falls** as income rises, curve shifts **left**', 'Shift right / shift left', 'Cars instead of bicycles, nutritious food vs coarse grains, public transport, second-hand clothing'],
    ['**Substitute** vs **Complementary** (cross-price)', 'Substitutes: demand for A **rises** when price of B rises (positive cross-price elasticity). Complements: demand for A **falls** when price of B rises (negative cross-price elasticity). In complements one good leads and the other complements it', '-', 'Coffee and tea; cars and petrol, bread and butter, printers and ink cartridges'],
    ['**Merit** vs **Demerit** (effect on society)', 'Merit: positive externalities, **under-consumed** by the free market. Demerit: negative externalities, **over-consumed**', '-', 'Education, healthcare, vaccines, libraries vs alcohol, tobacco, recreational drugs'],
], rowhead=True)
c.call('note', 'Relativity of goods', 'Very few goods are universally normal or inferior. A basic motorcycle is a **normal** good in a low-income nation (richer people buy more bikes) but **inferior** in a high-income one (they buy cars instead). It depends on the society’s baseline income.')
c.h3('Exceptions to the law of demand: Veblen and Giffen')
c.table('Upward-sloping demand', ['', 'Veblen goods', 'Giffen goods'], [
    ['**What they are**', 'Ultra-luxury goods; almost nil marginal utility over cheaper luxury versions; they give **social status**', '**Inferior** goods that, in special circumstances, show demand rising with price'],
    ['**Why price up means demand up**', 'Status comes at a price. If the price falls, those who could afford it no longer find the unique status, so demand falls (and those who could not afford it still cannot)', 'Must take a **massive share of a poor consumer’s income** and have **no cheaper substitutes.** A price rise makes him so much poorer he drops the costlier normal good and buys even more of the staple'],
    ['**Handout example**', 'Luxury sports cars, designer jewellery, heritage items, rare animal breeds', 'Worker spends 90% of income on coarse grain and 10% on meat. Grain price rises, meat becomes unaffordable, the worker buys more grain. The negative **income effect** overpowers the **substitution effect**'],
    ['**Reality**', '-', 'Mostly **theoretical**, rarely observed'],
], rowhead=True)

c.sec('5 · Private goods versus public goods')
c.p('The classification uses two characteristics: **excludability** (can you stop someone using it if they do not pay?) and **rivalry** (does one person’s use reduce what is left for others?).')
c.fig('eco-goods-matrix.jpg', 'Classification of goods by consumption mechanics. Rows: excludable yes or no. Columns: rivalrous yes or no. Private goods (food, clothing, cars, electronics): the market works, non-payers are denied. Club goods (cable TV, private parks). Common resources (ocean fisheries, public roads). Public goods (national defence, law and order, clean air): market failure, the free-rider problem, no one pays voluntarily, so government and taxes are needed.')
c.table('Private versus public', ['', 'Private goods', 'Public goods'], [
    ['**Characteristics**', 'Excludable **and** rivalrous. Consumers bid through prices for limited supply: “market efficiency”', '**Non-excludable** and **non-rival**'],
    ['**Result**', 'Provided by the market', '**Free Rider Problem (FRP):** everyone expects someone else to pay, so no private business will produce it. A permanent unmet desire: **market failure**'],
    ['**Who provides**', 'Producers', 'Government: society gives someone authority to collect taxes and the responsibility to provide. “This is how a government comes into existence”'],
    ['**Examples**', 'Food, clothing, cars, electronics', 'Law and order (police), defence, administration, licensing and regulatory services, streetlights and lighthouses'],
], rowhead=True)
c.p('Because government resources are limited, it provides only the most vital ones, prioritised by necessity (police presence may be higher in one area than another). Because there is no rivalry, one person’s use does not reduce availability to others.')

c.sec('6 · Intermediate versus final goods: the production boundary')
c.p('This classification is crucial for calculating **National Income (GDP).** A good is not inherently intermediate or final; it depends on **end-use.**')
c.fig('eco-prod-boundary.jpg', 'The production boundary. Scenario A: a household buys salt to cook dinner; economic identity retained, result is a final good. Scenario B: a hotel buys salt as an ingredient of a meal for sale; economic identity modified, salt becomes an intermediate good and the meal the final good.')
c.ul([
    '**Intermediate goods (IG):** used as inputs for other goods **for resale;** their economic identity is **lost** (modified into a new good meant for sale).',
    '**Final goods (FG):** economic identity **retained;** no further **economic** modification, even if physically or chemically changed.',
    '**Crucial:** the new good may or may not be physically or chemically different. What matters is only whether it was **economically** modified.'])
c.table('The handout’s examples', ['Case', 'Classification', 'Reason'], [
    ['Salt bought by a household (cooked at home)', '**Final**', 'Home-cooked food is not sold; no new commercial identity'],
    ['Salt bought by a hotel', '**Intermediate**', 'The meal is sold; the salt’s value merges into the price of the dish'],
    ['Mobile phone, screen guard and cover used together', 'All **final**', 'Physical assembly by the consumer is only a way of using final goods; no commercial value added for resale'],
    ['Phone sold second-hand after 3 years', 'Still **final**', 'Identity was finalised at first purchase; resale is only a transfer of ownership of an existing final good, no new production'],
], rowhead=True)

c.sec('7 · Consumer goods versus capital goods; fixed versus working capital')
c.p('Both consumer goods and capital goods are **sub-categories of final goods:** neither is transformed and resold.')
c.ul([
    '**Consumer goods:** final goods for household consumption (non-producers). By replacement frequency: **durables** and **non-durables.**',
    '**Capital goods:** machines and tools that **assist** production; bought by **producers.** Unlike raw materials (used up in one cycle) they last for **many** production cycles. They are still **final goods.**',
    'In the System of National Accounts (SNA) capital goods are **produced assets** “used repeatedly or continuously in production processes for **more than one year**”: factory buildings, heavy machinery, blast furnaces, delivery trucks, tractors, and intangibles such as commercial software and R&D.'])
c.table('Fixed capital versus working capital', ['', 'Fixed capital', 'Working (circulating) capital'], [
    ['**What**', 'Assets retained and used repeatedly over **more than one accounting year**', 'Capital used up in day-to-day operations; identity modified or liquidated within a production cycle or **under a year**'],
    ['**Role**', 'The rigid “infrastructure” of capacity; not for immediate resale', 'The “blood” through the infrastructure'],
    ['**Examples**', 'Plants, machinery, equipment, buildings', 'Raw-material inventory, work-in-progress, cash for wages and utilities'],
], rowhead=True)
c.call('alert', 'Handout alert: financial capital', '**Financial capital (money, stocks, bonds) is NOT economic capital in this context,** because a stock certificate cannot manufacture a product. The handout says: “Do not make this mistake in the exam.”')

c.sec('8 · Investment and gross capital formation')
c.p('In everyday language investment means mutual funds or gold. In macroeconomics that is merely a **transfer of financial assets: not investment.** **Investment is the expenditure by firms on capital goods in a period (usually a year).**')
c.table('Stock versus flow', ['', 'Capital', 'Investment'], [
    ['**Type**', '**Stock** variable', '**Flow** variable'],
    ['**Meaning**', 'Total value of machines a firm currently owns', 'Money spent buying **new** capital goods over a period'],
], rowhead=True)
c.p('Institutions such as the IMF, OECD and India’s National Accounts Statistics call it **Gross Capital Formation (GCF):** “the total value of the gross fixed capital formation, changes in inventories, and acquisitions less disposals of valuables for a unit or sector.”')
c.flow([
    ('Total investment (GCF)', '= GFCF + Δ Inventory + Valuables'),
    ('1 · GFCF (Gross Fixed Capital Formation)', 'Addition to the stock of fixed capital before depreciation: machines, tools, software, buildings, new roads, factories, intellectual property. The **most important** component. A high GFCF share of GDP signals a rapidly industrialising, future-focused economy'),
    ('GFCF has three parts', 'a) business fixed investment (machinery), b) public investment (roads, bridges), c) residential construction investment (houses)'),
    ('2 · Δ Inventory', 'Unsold or unused stock, treated by convention as capital. A factory makes 100 cars and sells 90: the 10 unsold are added to inventory, as if the firm invested in its own unsold goods'),
    ('3 · Acquisition of valuables', 'Non-financial assets held as a store of value, not for production or consumption: monetary gold, diamonds, antiques'),
], 'Components of investment')
c.call('note', 'Why housing is investment', 'Households “produce” labour services, and dwelling units are the infrastructure that sustains that. So an addition to the number of dwellings in a year is **investment,** not consumption.')

c.sec('9 · Depreciation, CFC, CCA and maintenance')
c.p('**Depreciation** is the loss in value of capital goods from an actual or perceived loss of ability to assist production, commonly wear and tear. It is **neither an actual loss nor an actual expenditure.** Gross spending on capital goods is partly only replacement, so:')
c.call('teacher', 'Formula', '**Net Investment = Gross Investment − Depreciation.**')
c.table('Three scenarios', ['Case', 'Meaning', 'Effect'], [
    ['Net investment > 0', 'More new machines than worn-out ones', 'Productive capacity expands (PPF shifts outward)'],
    ['Net investment = 0', 'Just enough to replace the broken ones', 'Economy is stagnant'],
    ['Net investment < 0', 'Not enough even to cover depreciation', 'Capital stock shrinks; capacity collapses'],
], rowhead=True)
c.table('Depreciation versus CFC versus CCA', ['Term', 'Whose tool', 'Basis', 'Handout example (machine bought for ₹10 lakh in 2015)'], [
    ['**Depreciation**', 'Corporate accountant (financial accounting)', '**Historical cost** (original price)', 'Lasts 10 years, so ₹1 lakh deducted each year, even if a new machine now costs ₹25 lakh'],
    ['**Consumption of Fixed Capital (CFC)**', 'National statistician and the RBI (SNA); used for **NDP and NNP**', '**Current replacement cost** (today’s market price)', 'Replacing 10% of its capacity costs ₹2.5 lakh today, so CFC is recorded as ₹2.5 lakh, not ₹1 lakh'],
    ['**Capital Consumption Allowance (CCA)**', 'Income Tax Department (tax lawyer’s tool)', '**Statutory rate** set by the government; a “legal fiction”; applied on historical cost', 'Accelerated depreciation: writing off 40% of a solar plant in year one to encourage green energy, though it did not lose 40% of capacity'],
], rowhead=True)
c.call('note', 'Maintenance is different', '**Maintenance** is routine expenditure to keep an asset working (oiling a machine, fixing a belt). It is an **intermediate cost.** It does **not** stop depreciation: a perfectly oiled 1990s loom still becomes useless because a 2024 automated loom is 10 times faster (obsolescence).')

c.mm = ('Basic concepts', [
    ('Economist’s task', [('Budget constraint + technology', None), ('PPF: normative, dynamic', 'sustainable maximum'), ('Advise, not decide', None)]),
    ('Two tools', [('Marginal cost: one more unit', None), ('Opportunity cost: next best foregone', 'stadium vs hospital')]),
    ('Systems', [('Free market: invisible hand', 'inequality'), ('Command: rent-seeking', 'information problem'), ('Friedman trade-off', None)]),
    ('Goods by demand', [('Necessary vs luxury', 'steep vs flat'), ('Normal vs inferior', 'income'), ('Substitute vs complement', 'cross-price'), ('Merit vs demerit', 'externalities'), ('Giffen and Veblen', None)]),
    ('Public vs private', [('Excludable and rivalrous', None), ('Public: free-rider problem', None), ('Government provides', None)]),
    ('Production boundary', [('Intermediate vs final', 'economic modification'), ('Salt: household vs hotel', None), ('Second-hand = still final', None)]),
    ('Capital', [('Consumer vs capital goods', None), ('Fixed vs working capital', None), ('Financial capital is not capital', None)]),
    ('Investment', [('GCF = GFCF + Δinventory + valuables', None), ('Stock vs flow', None), ('Net = gross − depreciation', None), ('Depreciation vs CFC vs CCA', None)]),
])

c.timeline = []

c.connects = [
    ('[Chapter 2: Inequality](eco-ch02.html)', 'The handout asks “remember reasons for inequality?” when it says a pure free-market system creates inequality through natural advantages; the rule-of-law and rent-seeking points reappear.'),
    ('[Chapter 3: Unemployment](eco-ch03.html)', 'The demand-and-supply and market-clearance ideas used for wage-rate unemployment are the same ones applied to goods here; Chapter 3 also refers to the SNA production boundary.'),
    ('National Income Accounting handout (next in your PDF)', 'The handout says this chapter prepares you for it: final versus intermediate goods, GCF, depreciation, CFC and NDP/NNP are the building blocks of GDP.'),
    ('Budget and Fiscal Policy handout', 'Public goods and merit goods explain why governments tax and spend; opportunity cost frames public spending choices.'),
]

c.recall = [
    'Economist advises: budget constraint + technology give the PPF. PPF is normative, dynamic, “sustainable and desirable”.',
    'MC = cost of one more unit. OC = value of next best alternative foregone (stadium versus hospital).',
    'Free market: invisible hand, inequality. Command: information problem, rent-seeking, rigid inequality. Friedman: equality before freedom gets neither.',
    'Necessary = steep, inelastic. Luxury = flat, elastic. Normal: income up, demand up. Inferior: income up, demand down. Substitute: positive cross-price. Complement: negative.',
    'Merit: positive externality, under-consumed. Demerit: negative externality, over-consumed.',
    'Giffen: inferior, big share of poor income, no substitutes. Veblen: ultra-luxury status good. Both: price up, demand up (in theory / status).',
    'Private = excludable + rivalrous. Public = neither; free-rider problem; government provides.',
    'Intermediate versus final is about economic modification: household salt final, hotel salt intermediate; second-hand phone is still final.',
    'Capital goods: final goods used repeatedly for more than one year. Fixed versus working capital. Financial capital is not capital.',
    'Investment = spending on capital goods (flow). GCF = GFCF + Δ inventory + valuables. Net investment = gross − depreciation.',
    'Depreciation (historical cost, accountant) versus CFC (replacement cost, statistician, NDP/NNP) versus CCA (tax rule).',
    'Blank page: draw the excludable-rivalrous 2×2 and place private, club, common and public goods.',
]

c.mcq = [
    {'q': 'Other things remaining unchanged, market demand for a good might increase if 1) price of its substitute increases 2) price of its complement increases 3) the good is an inferior good and income of the consumers increases 4) its price falls. Which are correct? (2021)', 'options': ['1 and 4 only', '2, 3 and 4', '1, 3 and 4', '1, 2 and 3'], 'answer': 0, 'explain': 'Handout answer: (a). Substitute price up raises demand (positive cross-price); complement price up lowers it; inferior-good demand falls as income rises; a price fall raises quantity demanded.'},
    {'q': 'A good that shows rising demand as its price rises because it takes a huge share of a poor consumer’s income and has no cheaper substitute is a…', 'options': ['Veblen good', 'Giffen good', 'Merit good', 'Capital good'], 'answer': 1, 'explain': 'Giffen: negative income effect overpowers the substitution effect.'},
    {'q': 'Veblen goods are bought mainly for…', 'options': ['their nutritional value', 'social status', 'their low price', 'their use in production'], 'answer': 1, 'explain': 'They give almost no extra utility over cheaper luxuries; the status comes at a price.'},
    {'q': 'A good that is non-excludable and non-rival is a…', 'options': ['private good', 'public good', 'club good', 'inferior good'], 'answer': 1, 'explain': 'Public goods suffer the free-rider problem and are provided by government.'},
    {'q': 'Salt bought by a household for cooking at home is…', 'options': ['an intermediate good', 'a final good', 'a capital good', 'a merit good'], 'answer': 1, 'explain': 'Home-cooked food is not sold, so the salt retains its economic identity.'},
    {'q': 'A second-hand mobile phone sold after three years is…', 'options': ['an intermediate good', 'still a final good', 'working capital', 'a new production'], 'answer': 1, 'explain': 'Its identity was finalised at first purchase; resale is a transfer of ownership.'},
    {'q': 'Which of these is investment in the macroeconomic sense?', 'options': ['Buying shares', 'Buying mutual funds', 'A firm buying new machinery', 'Buying gold bars to hold'], 'answer': 2, 'explain': 'Investment is expenditure on capital goods. Shares and funds are transfers of financial assets. (Gold held as a store of value is the separate “valuables” item inside GCF, not business fixed investment.)'},
    {'q': 'Gross Capital Formation equals…', 'options': ['GFCF + change in inventories + acquisitions less disposals of valuables', 'GFCF − depreciation', 'Capital stock + working capital', 'Savings − consumption'], 'answer': 0, 'explain': 'That is the handout’s definition of GCF.'},
    {'q': 'Net investment is zero. This means…', 'options': ['capital stock is growing', 'the firm bought just enough to replace worn-out machines', 'capital stock is shrinking', 'the firm has no machines'], 'answer': 1, 'explain': 'The economy is stagnant: capacity neither grows nor shrinks.'},
    {'q': 'Consumption of Fixed Capital (CFC) is valued at…', 'options': ['historical cost', 'current replacement cost', 'a statutory tax rate', 'zero'], 'answer': 1, 'explain': 'CFC is the macroeconomist’s tool, used for NDP and NNP. Historical cost is accounting depreciation; the statutory rate is CCA.'},
    {'q': 'Accelerated depreciation allowed under the Income Tax Act is an example of…', 'options': ['CFC', 'CCA', 'maintenance', 'GFCF'], 'answer': 1, 'explain': 'CCA is a statutory allowance used as a policy tool, not a measure of wear and tear.'},
    {'q': 'Maintenance expenditure is treated as…', 'options': ['an intermediate cost that does not stop depreciation', 'investment', 'consumption of fixed capital', 'a capital good'], 'answer': 0, 'explain': 'Oiling a loom does not stop obsolescence.'},
    {'q': 'Which one is NOT a component of GFCF according to the handout?', 'options': ['Business fixed investment', 'Public investment', 'Residential construction investment', 'Purchase of corporate bonds'], 'answer': 3, 'explain': 'Financial assets are not capital. The three parts are business, public and residential.'},
]

c.mains = [
    ('What is the PPF? Why does the handout call it normative and dynamic?',
     'The PPF is the sustainable, desirable maximum output given budget constraints and technology.',
     ['Economist assesses limiting resources and technology, then each possible product mix.', 'Hunter-gatherer example: 8 hours of daylight; deer versus berries.', 'Below PPF possible but not desirable; beyond it not sustainable.', 'Normative: each economist’s assessment; dynamic: technology and information change it.'],
     'The PPF is a target to reach, not a fact to observe.'),
    ('Distinguish marginal cost from opportunity cost. Why does the handout call opportunity cost the most powerful concept?',
     'One is what you pay, the other is what you give up.',
     ['MC: cost of one more unit at the current output; rises as best resources are used first.', 'OC: next best alternative foregone; conceptual, not financial.', 'Stadium versus rural hospital or school.', 'Economics has no morals: it only shows the trade-off.'],
     'Every choice is also a refusal.'),
    ('Compare the decentralised and centralised systems of resource allocation. Why does each produce inequality?',
     'Both are mechanisms of information and incentives, and both fail in a way.',
     ['Free market: price signals, invisible hand, but those with capital dominate.', 'Command: central planner’s information problem; rent-seeking; state-created monopolies.', 'Command inequality is rigid and worse: connections, not competence.', 'Friedman: equality before freedom gets neither.'],
     'No system is perfect; each trades freedom against equality.'),
    ('What are public goods? Why must government provide them?',
     'Public goods are non-excludable and non-rival, so the market fails to supply them.',
     ['Free-rider problem: no one pays voluntarily.', 'Society creates government with the authority to tax and the duty to provide.', 'Examples: law and order, defence, streetlights, lighthouses.', 'Limited resources: only the most vital are provided, prioritised by necessity.'],
     'Government exists because some goods cannot be sold.'),
    ('Explain investment in the macroeconomic sense and distinguish depreciation, CFC and CCA.',
     'Investment is spending on capital goods, a flow that adds to the stock of capital.',
     ['GCF = GFCF + change in inventories + valuables; GFCF has business, public and residential parts.', 'Net investment = gross investment − depreciation; the three scenarios.', 'Depreciation: historical cost (accountant). CFC: replacement cost (national accounts). CCA: tax allowance (policy tool).', 'Maintenance does not stop depreciation.'],
     'Capital is what you own; investment is what you add to it in a year.'),
]

c.cards = [
    ('What are the two things an economist assesses first?', 'The budget constraints (limiting resources) and the prevailing technology.'),
    ('What is the PPF?', 'The maximum sustainable output possible from given resources and technology; normative and dynamic.'),
    ('Output below the PPF?', 'Possible but not desirable.'),
    ('Output beyond the PPF?', 'Desirable but not sustainably possible.'),
    ('Marginal cost?', 'Actual cost of producing exactly one more unit.'),
    ('Opportunity cost?', 'Value of the next best alternative foregone.'),
    ('Stadium example?', 'MC is cement, steel, labour. OC is the rural hospital or school not built.'),
    ('Invisible hand?', 'Individual self-interest mechanically maximises collective well-being in a free market.'),
    ('What is rent-seeking?', 'Pleasing the planner (being connected) instead of competing; under a command system.'),
    ('Friedman’s quote?', 'Equality before freedom gets neither; freedom before equality gets a high degree of both.'),
    ('Necessary goods: demand curve?', 'Steep, inelastic.'),
    ('Luxury goods: demand curve?', 'Flat, elastic.'),
    ('Normal vs inferior?', 'Normal: demand rises with income. Inferior: demand falls with income.'),
    ('Substitute: sign of cross-price elasticity?', 'Positive.'),
    ('Complement: sign of cross-price elasticity?', 'Negative.'),
    ('Merit goods?', 'Positive externalities; under-consumed by markets (education, vaccines).'),
    ('Demerit goods?', 'Negative externalities; over-consumed (alcohol, tobacco).'),
    ('Veblen goods?', 'Ultra-luxury status goods: demand falls when price falls.'),
    ('Giffen goods?', 'Inferior goods with huge income share and no substitutes: price up, demand up. Mostly theoretical.'),
    ('Excludable and rivalrous?', 'Private goods.'),
    ('Non-excludable and non-rival?', 'Public goods.'),
    ('Free-rider problem?', 'Everyone expects someone else to pay, so no one does and the market fails.'),
    ('How is a good final or intermediate?', 'By retention or loss of economic identity (economic modification), not physical form.'),
    ('Hotel salt vs household salt?', 'Intermediate vs final.'),
    ('Are capital goods final goods?', 'Yes; used repeatedly for more than one year.'),
    ('Fixed vs working capital?', 'More than one year (plant, machines) vs used up within a cycle (raw materials, cash).'),
    ('Is financial capital economic capital?', 'No.'),
    ('Is capital a stock or flow? Investment?', 'Capital: stock. Investment: flow.'),
    ('GCF components?', 'GFCF + change in inventories + acquisitions less disposals of valuables.'),
    ('Three parts of GFCF?', 'Business fixed, public, residential.'),
    ('Net investment?', 'Gross investment minus depreciation.'),
    ('Depreciation basis?', 'Historical cost (financial accounting).'),
    ('CFC basis and use?', 'Current replacement cost; NDP and NNP.'),
    ('CCA?', 'Statutory tax allowance, a legal fiction and policy tool.'),
    ('Does maintenance stop depreciation?', 'No: obsolescence continues.'),
]
c.summary = 'PPF, marginal and opportunity cost, free-market versus command systems, every type of good (including Giffen, Veblen, public, intermediate and capital), investment and GCF, depreciation versus CFC versus CCA. One Prelims PYQ.'
