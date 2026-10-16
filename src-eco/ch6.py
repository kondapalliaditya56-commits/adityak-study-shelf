from lib import Ch

c = Ch(6, 'Inflation: Causes, Measurement, Effects and Control',
       'Economy · GS Foundation · Chapter 6',
       [('hb', 'Handout only: no class slides'), ('', 'Handout pages 1-16'), ('', 'No PYQs quoted')],
       'Price versus price level, AD and AS, demand-pull and cost-push causes, how inflation is measured and indexed, CPI and WPI, the 2024 base-year CPI, headline, core and skewflation, hyperinflation, stagflation and the Phillips curve, who gains and loses, fiscal drag, and why control works through the cost of money.')

c.sec('Exam lens: priority and PYQs', 'exam-lens-priority-and-pyqs')
c.call('alert', 'Source note', ['**Handout only.** No class slides and no teacher ink. **No Prelims or Mains PYQ is quoted** in this handout: none quoted in the material. The priority below is the handout’s own emphasis (definitions, worked examples, and the recent changes in measurement).'])
c.table('What the handout stresses', ['Signal in the handout', 'Where', 'Why it matters'], [
    ['Inflation is a rise in the **price level,** not in one price. Prices rise when **AD exceeds AS**', 'Sections 1-2', 'The base of every cause and every cure'],
    ['Index = (100 ÷ base-year basket price) × current basket price. Inflation = % change over the **same month** of the previous year', 'Section 4', 'Worked numbers (₹10,000 → ₹15,000 → ₹16,500)'],
    ['The new **2024 = 100** CPI series (released Feb 2026): 12 divisions, COICOP 2018, food weight 36.75%, 358 items, e-commerce data', 'Section 5', 'Recent changes; a likely current-affairs hook'],
    ['**Headline = CPI-C,** target **4% ± 2%,** adopted for inflation targeting in **2015;** Urjit Patel Committee **2014**', 'Section 6', 'Facts and dates'],
    ['Core inflation: headline minus **food and fuel;** petrol and diesel stay **inside** core', 'Section 6', 'A classic trap'],
    ['Stagflation breaks the **Phillips Curve** (A.W. Phillips, UK 1861-1957)', 'Section 7', 'Concept plus author'],
    ['Fiscal drag: inflation pushes workers into higher tax brackets; an **automatic stabiliser**', 'Section 9', 'Worked table (₹9 L → ₹10.8 L)'],
    ['Real interest = nominal interest − inflation (RIR = NIR − Inflation)', 'Section 8', 'Borrowers gain, lenders and depositors lose'],
])
c.call('key', 'What to prepare', [
    '**Prelims hooks:** price versus prices; AD and AS factors; demand-pull versus cost-push; CPI versus WPI (who releases which); the 2024 base and 12 divisions; headline, core, super core, skewflation, structural inflation; deflation versus disinflation; recession versus depression; shrinkflation; stagflation and the Phillips Curve; Engel’s Law; fiscal drag.',
    '**Mains hooks:** why inflation hurts the poor most (Engel’s Law); who gains and loses; why a cause-agnostic cure is needed; why cheaper-money policy fuels demand-pull; fiscal drag as an automatic cooling effect; why a lower food weight changes how the RBI reads inflation.',
    '**Closing idea:** inflation is AD chasing AS; since you cannot fix every cause in time, make money expensive and AD falls.'])

c.sec('1 · What inflation is, and what it is not')
c.p('**Inflation is a general rise in prices or the price level.** A rise in the price of one good may cause inflation but is **not** inflation by itself. People feel inflation when the **overall value of the basket** they buy goes up. Each person has a different basket, so the experience differs (the handout asks how an agricultural labourer in Odisha feels it versus a new joiner in a Bengaluru startup).')
c.ul(['**Price** is the value at which a single good is exchanged, set by that good’s demand and supply.',
      '**Prices (the price level)** are set by **Aggregate Demand (AD)** and **Aggregate Supply (AS).**',
      'We cannot measure inflation for each person. We track a **normative basket** reflecting the consumption pattern of a specific group.'])

c.sec('2 · AD, AS and the price level')
c.table('Aggregate Demand versus Aggregate Supply', ['', 'Aggregate Demand (AD)', 'Aggregate Supply (AS)'], [
    ['**Meaning**', 'Total demand for all goods and services in the economy, which domestic producers are required to meet', 'Total supply of all goods and services, what all producers produce combined'],
    ['**Depends on**', 'General price level; incomes; spending habits (culture of spending); availability of money (easy loans); size of population', 'General price level; availability of basic raw materials (coal, iron, oil); skill level of the population; investment in infrastructure, capital goods and R&D'],
    ['**Link to price level**', 'Inversely related: if things become expensive, people demand less', 'Rises with price level: producers have an incentive to produce more (but inputs eventually run out)'],
], rowhead=True)
c.fig('eco-adas-sketch.jpg', 'The teacher’s sketches in the handout. Top left: equilibrium price level at a given level of GDP (AD meets AS). Top right: increase in price due to AD up, so higher price and higher demand (AD0 to AD1, Y0 to Y1). Bottom: prices rise due to a fall in AS, so higher price and lower production (AS0 to AS1, Y1 below Y0).')
c.fig('eco-adas-shift.jpg', 'Demand-side inflation: AD shifts right (demand-pull). Supply-side inflation: AS shifts left (cost-push).')
c.call('key', 'Rule', '**Prices rise when AD exceeds AS:** either AD rises for some reason, or AS falls for some reason.')

c.sec('3 · Causes of inflation')
c.p('Demand and supply factors of any good split into **specific** factors (taste for ice cream) and **general** factors (size of population, income levels, availability of money). Causes of inflation are the **general** factors that shift AD or AS, not the factors of one good.')
c.table('Demand-side versus supply-side inflation', ['', 'Demand-pull (AD shifts right)', 'Cost-push (AS shifts left)'], [
    ['**Trigger**', 'Anything that raises AD', 'Anything that lowers AS or restricts production'],
    ['**Examples**', 'Rising income levels; easy money (lower interest rates, cheaper credit); more government spending; rising population; changing spending habits (less saving, more consumption, usually a secondary effect of higher incomes)', 'Rising cost or non-availability of basic raw materials (crude, metals, coal); higher cost of factors of production (wages, interest on capital); low investment (poor infrastructure, no capital goods, poor R&D); falling productivity or failure to adopt new skills; poor Ease of Doing Business (compliance, contract enforcement, weak entrepreneurship culture); frequent disasters disrupting supply chains'],
], rowhead=True)
c.p('**Other factors** named in the handout:')
c.ul(['**Legal and market distortions:** cartelisation (producers collude to act as a monopoly), hoarding (artificial scarcity), widespread black money (untracked cash).',
      '**International shocks:** geopolitical tension, war, trade sanctions, disasters, especially in countries we import heavily from (oil producers).'])

c.sec('4 · Measuring inflation and the idea of an index')
c.p('Inflation is the **percentage change in prices** in the current period over the previous period. It is usually reported **year-on-year (Y-o-Y):** the current month against the **same month** of the previous year.')
c.ol(['Identify the **target group.**',
      'Construct a **normative basket** of goods and services for an average person in that group.',
      'Choose a **base year.** The basket is built separately for each month to account for seasonality. The importance of each item is its **weight** (% of total expenditure). Most items stay, some enter and exit, and some weights change.',
      'Collect the prices of the items for each month of the base year to get the basket’s total price.',
      'Collect the prices for the corresponding months of later years to get the new basket price.',
      'Inflation = **% change** in the basket price in a month of this year over the same month of last year.',
      'Communicate the **index value** along with the % change over the year.'])
c.sec('5 · Indexing: why, and a worked example')
c.p('If the government only said “prices are 4.3% higher than last year”, last year would become a moving benchmark. People need a **fixed** base. Also, the raw basket price (like ₹11,345 and ₹18,967) is a meaningless number for a normative basket. So the base-year basket price is set to a clean value, **usually 100.**')
c.table('The handout’s example', ['Period', 'Basket price', 'Index value'], [
    ['Base year (March 2015)', '₹10,000', '100'],
    ['March 2025', '₹15,000', '(100 ÷ 10,000) × 15,000 = **150**'],
    ['March 2026', '₹16,500', '(100 ÷ 10,000) × 16,500 = **165**'],
], rowhead=True)
c.ul(['**Inflation (March 2026 over March 2025)** = (16,500 − 15,000) ÷ 15,000 × 100 = **10%.**',
      'An index of **165** means prices are **65% higher** than in the 2015 base year.',
      'The base year here gives a **constant basket** to compare the cost of living; in Real GDP the base year gives **constant prices** to value output.'])

c.sec('6 · Indices in India and the 2024 base-year CPI')
c.table('Common inflation indices', ['Index', 'Variants', 'Released by'], [
    ['**CPI**', 'CPI-Rural, CPI-Urban, CPI-Combined (CPI-C)', 'National Statistical Office (NSO) under MoSPI'],
    ['**CPI-AL and CPI-IW**', 'Agricultural Labourers; Industrial Workers', 'Labour Bureau (Ministry of Labour and Employment)'],
    ['**WPI**', 'Wholesale Price Index', 'Office of the Economic Adviser (OEA), Department for Promotion of Industry and Internal Trade (DPIIT), Ministry of Commerce and Industry'],
], rowhead=True)
c.ul(['A working group chaired by **Prof. Ramesh Chand** was constituted to revise the **WPI base year from 2011-12 to 2022-23,** and to recommend a roadmap to switch from **WPI to a Producer Price Index (PPI).**',
      'India has **no official PPI.** So in **2017** WPI was adjusted to sit closer to **basic prices / factor cost** by **removing indirect taxes,** bringing it nearer to producers’ realised prices.'])
c.p('**In Feb 2026 MoSPI released the new 2024 = 100 base-year series,** a structural overhaul, not a routine weight change:')
c.table('2012 series versus 2024 series (as given in the handout)', ['Change', '2012 series', '2024 series'], [
    ['**Breakup of “Miscellaneous”**', '6 groups; a giant “Miscellaneous” bucket (doctor visits, bus fares, school fees) with **28.32%** weight', '**12 divisions** under the UN **COICOP 2018** framework; Transport, Health, Education and Communications tracked separately'],
    ['**Engel’s Law (food loses its crown)**', 'Food and Beverages weight **45.86%**', '**36.75%.** Food is volatile (onion, tomato spikes), so headline inflation should be less volatile and give the RBI a clearer demand signal'],
    ['**Digital and service economy**', '**299** items', '**358** items. Removed: VCRs, tape recorders, CDs. Added: OTT subscriptions, pen drives, attendant/babysitter services, pet products. For the first time, prices scraped from **12 major e-commerce platforms;** **Rural House Rent** introduced'],
], rowhead=True)

c.sec('7 · Key terminology')
c.h3('Headline, skewflation, core, structural')
c.table('Types of inflation measure', ['Term', 'Meaning in the handout', 'Notes and trap'], [
    ['**Headline inflation**', 'Overall inflation = **CPI-C.** What the news reports', 'Adopted as the **primary anchor of Inflation Targeting in 2015.** Shift from WPI to CPI-C recommended by the **Urjit Patel Committee, 2014.** Target set by the **Monetary Policy Framework Agreement at 4%, tolerance ±2%**'],
    ['**Skewflation**', 'Inflation driven by a few items rising fast while most stay stable. “Skew” means bent or asymmetrical', 'Gained prominence in India around **2009-2010** (Economic Survey): onions and pulses spiked while manufactured goods stayed cheap'],
    ['**Core inflation**', 'Headline minus highly volatile items (**food and fuel**) that authorities cannot immediately control. Also **non-food, non-fuel** inflation', 'NSO calculates headline; food and fuel are removed to reach core; **RBI calculates the value.** **Petrol and diesel for vehicles are inside core** (under Transport and Communication within Miscellaneous), not in “Fuel and Light”; their prices are controlled through taxation'],
    ['**Super core / refined core**', 'Headline minus food, fuel, petrol, diesel and precious metals', 'Truest picture of underlying demand'],
    ['**Structural inflation**', 'Caused by structural features (poor infrastructure, bad EODB, skill deficits, supply-chain bottlenecks) that take long to fix', 'Handout example: political complexity blocks agriculture supply-chain reform, so the current system stays inherently inflationary'],
], rowhead=True)
c.call('alert', 'Handout alert: where petrol sits', 'Many people assume petrol and diesel are in “Fuel and Light”. **The handout puts vehicle petrol and diesel under Transport and Communication, so they are inside core.** Exam-hall rule: core = headline minus food and fuel (Fuel and Light) only; petrol and diesel come out only in **super core.**')
c.h3('Hyperinflation, deflation, disinflation')
c.ul(['**Hyperinflation:** runaway, exceptionally high inflation (galloping, trotting). Costs: **shoe-leather costs** (running to the bank before money loses value) and **menu costs** (constantly updating prices).',
      '> There is **no consensus** on the criteria separating high from hyper. **Phillip Cagan:** more than **50% per month.** Examples: **Weimar Germany (1923), Zimbabwe (2008).** It is commonly understood as the rate beyond people’s normal capacity to bear: the US normal is 1-2%, so 6% looks “hyper” there; India’s normal over two decades is 5-6%, so even 9% is “high”, not “hyper”; Turkey has had 80-100%.',
      '**Deflation:** a fall in prices (negative inflation). **Disinflation:** a fall in the **rate** of inflation; prices still rise, but slower, largely a result of **base effect.** Continued disinflation may become deflation.',
      '**Japan** is the famous modern deflation example: “Lost Decades” since the 1990s; consumers delayed purchases expecting cheaper goods tomorrow.'])
c.h3('Recession, depression, shrinkflation')
c.table('Contraction terms', ['Term', 'Meaning', 'Note'], [
    ['**Recession**', 'Contraction in output for **two consecutive quarters**', 'A rule of thumb. The US **NBER** looks at broader metrics (employment, industrial production, wholesale-retail sales) to declare one'],
    ['**Depression**', 'Severe, prolonged contraction; the economy cannot get back to its original output', 'No objective criterion. **Great Depression (1929):** US GDP fell by nearly **30%,** unemployment hit **25%.** “A recession is a speed bump; a depression is a crater”'],
    ['**Shrinkflation**', 'Size or quantity of a good shrinks while the packet price stays the same', 'Rampant in FMCG. Handout examples: **Parle-G, Maggi** cutting grammage to hold the ₹5 or ₹10 price point'],
], rowhead=True)

c.sec('8 · Spirals, stagflation and the Phillips Curve')
c.ul(['**Price-wage spiral:** prices rise, workers demand higher wages, firms pass the wage cost to consumers, a continuous positive feedback loop.',
      '**Inflation expectations:** a **self-fulfilling prophecy.** If people expect prices to rise, panic-buying today creates shortages and prices actually rise.',
      '**Reflation:** the government induces inflation (stimulus cheques, tax cuts, lower interest rates) to boost AD and reduce unemployment after a recession or deflation.'])
c.call('key', 'Stagflation', '**Stagflation = stagnation of output (low growth, high unemployment) + high inflation, together.** Merely a contraction is recession; merely high inflation is hyperinflation. Stagflation needs **both** to be adverse at once.')
c.p('Normally there is a **trade-off:** fast growth (low unemployment) comes with high inflation, and slow growth (high unemployment) comes with low inflation. This comes from the **Phillips Curve:** **A.W. Phillips** studied the **UK from 1861 to 1957** and found an **inverse relation between inflation (wage growth) and unemployment.** Points where both were low, or both high, were outliers; the both-high points are the periods of stagflation.')
c.ul(['If inflation is very high, unemployment is probably low, so the policy maker will pay the price of a slight rise in UE to cut inflation. If UE is very high, prices are probably low, so a rise in prices is a bearable cost to cut UE.',
      '**Stagflation breaks the Phillips Curve:** pursuing either goal worsens the other, which creates **policy uncertainty and paralysis.**'])

c.sec('9 · Effects of inflation')
c.h3('Time value of money and real return')
c.p('Inflation erodes money’s value. If ₹100 bought 1 kg of apples and apples now cost ₹110, ₹1 has gone from 1/100 kg to 1/110 kg. With 10% inflation, **₹110 this year buys what ₹100 bought last year.** Someone with ₹105 is nominally richer but **poorer in real terms.** You need **exactly inflation% extra** to keep your worth.')
c.call('teacher', 'Formula', '**Real Interest Rate (RIR) = Nominal Interest Rate (NIR) − Inflation.** Handout example: lent at 10% with 7% inflation, the lender is richer by only **10% − 7% = 3%** in real terms.')
c.table('Who gains and who loses', ['Group', 'Effect', 'Why'], [
    ['**Borrowers**', 'Benefit', 'Inflation eats into the lender’s return and helps shoulder the borrower’s burden'],
    ['**Lenders (banks)**', 'Lose, unless protected', 'Banks protect themselves by (a) charging a high NIR that stays above inflation, or (b) using a **floating rate:** RIR fixed, NIR = RIR + inflation'],
    ['**Depositors**', 'Lose', 'They are lenders to banks with no bargaining power. Deposit rates (the handout says a meagre 2-3%) do not beat inflation, so the real return is generally **negative.** Even fixed deposits hardly beat inflation. This does **not** mean keep cash at home: cash loses value at the rate of inflation'],
    ['**Consumers**', 'Lose', 'Money loses purchasing power'],
    ['**Producers**', 'Generally benefit', 'Depends on pricing power: necessities have inelastic demand but more competition; luxuries have elastic demand but less competition. Most producers can pass on the rise, so profit margins expand'],
], rowhead=True)
c.sec('10 · Is inflation desirable? Engel’s Law and the poor')
c.p('As a consumer you might prefer deflation, but a healthy economy needs **low and stable** inflation. Low inflation within people’s tolerance **keeps producers profitable** so they invest, expand capacity, pay higher wages and create jobs. Stability brings predictability and stops people **delaying** decisions.')
c.call('teacher', 'Engel’s Law (asterisked in the handout)', '**Ernst Engel:** as family income rises, the **% of income spent on food falls,** even if absolute spending on food rises. Corollary: a poor household spends most of its money on necessities like food, whose prices are volatile and whose producers can pass on price rises. So **the poor are disproportionately hit by inflation:** no buffer or luxury spending to cut.')

c.sec('11 · Fiscal drag: how inflation cools itself')
c.p('In inflation the government collects more **direct and indirect** taxes. Indirect taxes are mostly **ad valorem** (on the value of goods), so the same rate collects more. Direct taxes: a worker who negotiates a raise equal to inflation is pushed into a **higher bracket** under progressive taxation.')
c.table('The handout’s hypothetical (inflation 20%)', ['', 'Income ₹9 L', 'Income ₹10.8 L (+20%)'], [
    ['Slabs (hypothetical)', '0-5 L at 10%; 5-10 L at 15%; 10-30 L at 20%; 30 L+ at 25%', 'Same slabs'],
    ['Tax', '₹50,000 on first 5 L + ₹60,000 on next 4 L = **₹1.1 L**', '₹50,000 + ₹75,000 on next 5 L + ₹16,000 on next 80k = **₹1.41 L**'],
    ['Disposable income', '9 − 1.1 = **₹7.9 L**', '10.8 − 1.41 = **₹9.39 L**'],
    ['Change', 'Post-tax income up **18.8%**', 'Tax outgo up **28.2%**'],
], rowhead=True)
c.p('Nominal income rose by the full inflation rate (20%), but real disposable income rose only about 18-19%. People pay a larger share of their **increment** as tax. No new tax was imposed; the system does it automatically. People realise they are poorer, cut spending, **AD falls** and prices cool without the government acting. This automatic cooling is **fiscal drag,** acting as an **automatic stabiliser.**')
c.call('alert', 'Handout alert: 18% or 18.8%', 'The table gives **18.8%** for the rise in post-tax income, but the text beneath says “grew by a lesser rate (18%)”. Use **about 18.8%** if asked for a number; the point (smaller than 20%) is what the exam wants.')

c.sec('12 · Controlling inflation: why “make money expensive”')
c.ul(['**Two problems:** (1) identifying the cause (price is the collective outcome of many intertwined factors); (2) the ability to fix it (you cannot build roads and ports, or attract capital, in a year). Structural fixes (infrastructure, import resilience, EODB) are necessary but come too late. The solution must be **effective and agnostic of the cause.**',
      'Inflation is a consequence of **AD exceeding AS.** Bring down AD and prices cool. AD is expenditure using **money.** If money becomes **expensive,** people hold on to it and spend less.',
      '**The cost of money is the interest rate** (a loan of ₹1 lakh at 8%). Raise it from 8% to 10%: those with money save it for the higher interest, those without cannot afford to borrow. **Both reduce demand,** AD cools and prices fall.',
      'The price of money, like any price, depends on its **demand and supply.** Reduce the supply of money and its cost rises. **Who does this and how** is the next chapter: money, its demand and supply, and monetary policy.'])
c.flow([
    ('AD exceeds AS', 'Prices rise', ''),
    ('Raise the cost of money', 'Interest rate up (8% → 10%)', ''),
    ('Savers save, borrowers borrow less', 'Spending falls', ''),
    ('AD falls', 'Prices cool', ''),
], 'The handout’s logic for controlling inflation')

c.mm = ('Inflation', [
    ('What it is', [('General rise in price level', None), ('Price vs prices', 'AD and AS'), ('Normative basket', None)]),
    ('Causes', [('Demand-pull: AD right', 'income, easy money, spending, population'), ('Cost-push: AS left', 'raw materials, wages, EODB, disasters'), ('Cartels, hoarding, black money', None), ('International shocks', None)]),
    ('Measurement', [('Base year 100', 'index'), ('Y-o-Y, same month', None), ('Example 10%; index 165 = 65% up', None)]),
    ('Indices', [('CPI (NSO, MoSPI)', None), ('CPI-AL, CPI-IW (Labour Bureau)', None), ('WPI (OEA, DPIIT)', None), ('2024=100: 12 divisions, 358 items', None)]),
    ('Terms', [('Headline = CPI-C, 4% ± 2%', None), ('Core = minus food and fuel', None), ('Skewflation', None), ('Structural', None), ('Disinflation vs deflation', None)]),
    ('Stagnation side', [('Recession: 2 quarters', None), ('Depression', None), ('Stagflation', 'breaks Phillips Curve'), ('Reflation', None)]),
    ('Effects', [('RIR = NIR − inflation', None), ('Borrowers gain; depositors lose', None), ('Engel’s Law: poor hit most', None), ('Fiscal drag', None)]),
    ('Control', [('Make money expensive', None), ('Interest rate up', None), ('AD falls', None)]),
])

c.timeline = [
    ('1861-1957', 'A.W. Phillips studies UK data for the Phillips Curve (inverse relation between inflation (wage growth) and unemployment).', False),
    ('1923', 'Weimar Germany: the handout’s hyperinflation example.', False),
    ('1929', 'Great Depression: US GDP fell by nearly 30%, unemployment 25%.', False),
    ('2008', 'Zimbabwe: hyperinflation example.', False),
    ('2009-2010', 'Skewflation prominent in India (onions, pulses).', False),
    ('2014', 'Urjit Patel Committee recommends CPI-C as headline instead of WPI.', True),
    ('2015', 'CPI-C adopted as the primary anchor for the Inflation Targeting framework.', True),
    ('2017', 'WPI adjusted: indirect taxes removed so it sits closer to basic prices / factor cost.', False),
    ('Feb 2026', 'MoSPI releases the new 2024 = 100 CPI base-year series.', True),
]

c.connects = [
    ('[Chapter 5: National Income Accounting](eco-ch05.html)', 'The handout says the base year in inflation gives a constant basket, as in the Real GDP chapter it gives constant prices.'),
    ('[Chapter 3: Unemployment](eco-ch03.html)', 'The Phillips Curve and stagflation link inflation to unemployment; ch3 covers NAIRU and cyclical unemployment.'),
    ('[Chapter 4: Basic Concepts](eco-ch04.html)', 'Necessary versus luxury goods (elasticity) decide the producer’s pricing power; normal versus inferior goods connect to Engel’s Law.'),
    ('[Chapter 8: Money and Monetary Policy](eco-ch08.html)', 'The handout ends by turning to money, its demand, supply and monetary policy: the cure for inflation.'),
    ('Budget and Fiscal Policy handout', 'Government spending drives AD; fiscal drag works through tax brackets.'),
]

c.recall = [
    'Inflation = rise in price level (not one price). Prices rise when AD exceeds AS. Demand-pull: AD right. Cost-push: AS left.',
    'Index = 100 ÷ base price × current price. Example: 10,000 → 15,000 → 16,500: index 150, 165; inflation 10%.',
    'CPI by NSO (MoSPI); CPI-AL, CPI-IW by Labour Bureau; WPI by OEA (DPIIT). 2024=100 series: 12 divisions, 358 items, food 36.75% (was 45.86%), Miscellaneous was 28.32%.',
    'Headline = CPI-C; target 4% ± 2%; adopted 2015; Urjit Patel Committee 2014. Core = minus food and fuel; petrol and diesel stay in core.',
    'Disinflation: rate falls, prices still rise. Deflation: prices fall. Recession: 2 quarters. Depression: severe and prolonged.',
    'Stagflation: low growth + high inflation; breaks the Phillips Curve (Phillips, UK 1861-1957).',
    'RIR = NIR − inflation. Borrowers gain; lenders and depositors lose. Engel’s Law: the poor are hit hardest.',
    'Fiscal drag: higher bracket, more tax, AD falls: an automatic stabiliser.',
    'Control: raise the cost of money (interest rate), AD falls, prices cool.',
    'Blank page: draw AD-AS with AD shifting right, then AS shifting left, and label the new price level.',
]

c.mcq = [
    {'q': 'Inflation in the macroeconomic sense means…', 'options': ['a rise in the price of any one good', 'a general rise in the price level', 'a rise in the price of food only', 'a rise in wages'], 'answer': 1, 'explain': 'A rise in one price may cause inflation but is not inflation by itself.'},
    {'q': 'Which of the following causes demand-pull inflation?', 'options': ['Rising crude oil prices', 'Rising wages of workers', 'Easy availability of money through cheaper credit', 'Frequent disasters in supply chains'], 'answer': 2, 'explain': 'Demand-pull comes from a rise in AD (income, easy money, government spending). The others shift AS left.'},
    {'q': 'In the handout’s example the base-year basket costs ₹10,000 (index 100) and later costs ₹16,500. The index is…', 'options': ['150', '165', '116.5', '16.5'], 'answer': 1, 'explain': '(100 ÷ 10,000) × 16,500 = 165, meaning prices are 65% higher than in the base year.'},
    {'q': 'The Consumer Price Index (CPI-Combined) is compiled by…', 'options': ['Labour Bureau', 'Office of the Economic Adviser, DPIIT', 'National Statistical Office under MoSPI', 'Reserve Bank of India'], 'answer': 2, 'explain': 'NSO releases CPI-R, CPI-U and CPI-C. Labour Bureau handles CPI-AL and CPI-IW; OEA handles WPI.'},
    {'q': 'The inflation target set by the Monetary Policy Framework Agreement, per the handout, is…', 'options': ['2% ± 4%', '4% ± 2%', '6% ± 2%', '5% ± 1%'], 'answer': 1, 'explain': '4% with a tolerance band of ±2%, anchored on headline CPI-C.'},
    {'q': 'Which was the share of Food and Beverages in the new 2024 = 100 CPI basket, per the handout?', 'options': ['45.86%', '36.75%', '28.32%', '12%'], 'answer': 1, 'explain': '36.75%, down from 45.86% in 2012. 28.32% was the old Miscellaneous weight.'},
    {'q': 'Core inflation is headline inflation excluding…', 'options': ['food and fuel', 'petrol and diesel only', 'housing', 'imports'], 'answer': 0, 'explain': 'Per the handout, petrol and diesel for vehicles remain inside core; they come out only in super core.'},
    {'q': 'A fall in the rate of inflation, with prices still rising, is called…', 'options': ['deflation', 'disinflation', 'reflation', 'stagflation'], 'answer': 1, 'explain': 'Deflation is a fall in prices. Disinflation is a slower rise.'},
    {'q': 'Stagflation is a situation of…', 'options': ['low growth and low inflation', 'high growth and high inflation', 'low growth, high unemployment and high inflation together', 'high growth and low inflation'], 'answer': 2, 'explain': 'It breaks the Phillips Curve trade-off.'},
    {'q': 'The Phillips Curve showed an inverse relation between…', 'options': ['inflation and interest rate', 'inflation (wage growth) and unemployment', 'GDP and money supply', 'prices and exports'], 'answer': 1, 'explain': 'A.W. Phillips studied the UK from 1861 to 1957.'},
    {'q': 'A lender lends at 10% when inflation is 7%. The real return is…', 'options': ['17%', '10%', '3%', '7%'], 'answer': 2, 'explain': 'RIR = NIR − inflation = 10 − 7 = 3%.'},
    {'q': 'Why does the handout say the poor are hit hardest by inflation?', 'options': ['They hold more cash', 'Engel’s Law: most of their spending is on volatile necessities with no buffer', 'They pay higher taxes', 'They borrow more'], 'answer': 1, 'explain': 'A poor household’s spending is mostly food and necessities, and producers of these can pass on prices.'},
    {'q': 'Fiscal drag arises because…', 'options': ['new taxes are imposed in inflation', 'rising nominal incomes push people into higher tax brackets, cooling demand automatically', 'the government cuts spending', 'banks raise interest rates'], 'answer': 1, 'explain': 'No new tax is imposed; the progressive system takes a larger share of the increment, which acts as an automatic stabiliser.'},
    {'q': 'Why does raising interest rates control inflation, per the handout?', 'options': ['It raises AS directly', 'Money becomes expensive, so both savers and borrowers spend less and AD falls', 'It lowers wages', 'It reduces the import bill'], 'answer': 1, 'explain': 'The interest rate is the cost of money; dearer money cools AD.'},
]
for q in c.mcq:
    q.pop('explanation', None)

c.mains = [
    ('Distinguish between a rise in a price and inflation. What causes inflation?',
     'Inflation is a general rise in the price level, not a rise in one good’s price.',
     ['Prices rise when AD exceeds AS.', 'Demand-pull: rising incomes, easy money, government spending, population, spending habits.', 'Cost-push: raw material costs, wages, low investment, poor EODB, disasters.', 'Other: cartels, hoarding, black money, international shocks.'],
     'The causes to look for are the general factors that shift AD or AS.'),
    ('How is inflation measured in India? Discuss the recent changes in measurement.',
     'A normative basket is tracked against a base year and converted to an index.',
     ['Steps: target group, basket and weights, base year, prices, year-on-year change.', 'CPI (NSO), CPI-AL and CPI-IW (Labour Bureau), WPI (OEA).', 'Headline = CPI-C, target 4% ± 2%, Urjit Patel Committee 2014.', '2024 = 100 series: 12 divisions (COICOP 2018), food weight 36.75%, 358 items, e-commerce data, rural house rent.'],
     'A lower food weight should give a less volatile and clearer signal for monetary policy.'),
    ('Why does inflation hurt the poor more? Explain with Engel’s Law.',
     'Engel’s Law says the share of income spent on food falls as income rises.',
     ['A poor household spends most of its budget on necessities like food.', 'Food prices are volatile and producers can pass them on.', 'No buffer or luxury spending to cut.', 'Deposit returns of the poor are generally negative in real terms.'],
     'Inflation is a regressive burden.'),
    ('Explain stagflation and why it creates a policy dilemma.',
     'Stagflation is low growth, high unemployment and high inflation together.',
     ['Normally the Phillips Curve gives a trade-off.', 'Policy maker normally pays a small price in one to fix the other.', 'In stagflation both are adverse; fighting one worsens the other.', 'Result is policy uncertainty and paralysis.'],
     'Stagflation breaks the trade-off that policy relies on.'),
    ('What is fiscal drag? How does it act as an automatic stabiliser?',
     'In inflation nominal incomes rise, pushing people into higher tax brackets.',
     ['Worked example: ₹9 L to ₹10.8 L; tax up 28.2%, post-tax income up 18.8%.', 'Indirect taxes are ad valorem, so collections rise.', 'People feel poorer, cut spending, AD falls.', 'No new tax and no government action needed.'],
     'The tax system cools inflation automatically.'),
]

c.cards = [
    ('Inflation?', 'A general rise in the price level.'),
    ('Is a rise in one price inflation?', 'No. It may cause inflation but is not inflation itself.'),
    ('What sets the price level?', 'Aggregate Demand and Aggregate Supply.'),
    ('When do prices rise?', 'When AD exceeds AS.'),
    ('Demand-pull inflation?', 'AD shifts right.'),
    ('Cost-push inflation?', 'AS shifts left.'),
    ('Four demand-pull examples?', 'Rising incomes, easy money, more government spending, rising population.'),
    ('Four cost-push examples?', 'Raw material costs, wage costs, low investment, poor EODB.'),
    ('Non-AD/AS factors?', 'Cartels, hoarding, black money, international shocks.'),
    ('How is inflation reported?', 'Year-on-year: same month, previous year.'),
    ('Index of base year?', 'Usually 100.'),
    ('Index 165 means?', 'Prices are 65% higher than in the base year.'),
    ('Who releases CPI?', 'NSO under MoSPI.'),
    ('Who releases CPI-AL and CPI-IW?', 'Labour Bureau.'),
    ('Who releases WPI?', 'Office of the Economic Adviser, DPIIT.'),
    ('Who chairs the WPI base revision group?', 'Prof. Ramesh Chand (2011-12 to 2022-23; roadmap to PPI).'),
    ('Why was WPI adjusted in 2017?', 'No official PPI; indirect taxes removed to sit closer to basic prices.'),
    ('2024 CPI: groups to divisions?', 'From 6 groups to 12 divisions under COICOP 2018.'),
    ('2024 CPI: items?', '358 (from 299).'),
    ('Food weight 2012 versus 2024?', '45.86% versus 36.75%.'),
    ('Old Miscellaneous weight?', '28.32%.'),
    ('New data source in 2024 CPI?', '12 major e-commerce platforms; rural house rent introduced.'),
    ('Headline inflation?', 'CPI-C; the RBI’s anchor (2015). Target 4% ± 2%.'),
    ('Who recommended CPI-C as headline?', 'Urjit Patel Committee, 2014.'),
    ('Skewflation?', 'A few items rising fast make the whole basket costly (onions, pulses around 2009-2010).'),
    ('Core inflation?', 'Headline minus food and fuel.'),
    ('Where are petrol and diesel placed?', 'Inside core (Transport and Communication); out only in super core.'),
    ('Structural inflation?', 'Caused by long-to-fix structural features (infrastructure, EODB, skills, supply chains).'),
    ('Hyperinflation (Cagan)?', 'Over 50% per month. Weimar 1923, Zimbabwe 2008.'),
    ('Shoe-leather and menu costs?', 'Running to the bank; constantly updating prices.'),
    ('Deflation versus disinflation?', 'Prices fall versus the rate of inflation falls (prices still rise).'),
    ('Recession?', 'Contraction in output for two consecutive quarters.'),
    ('Shrinkflation?', 'Pack size shrinks, price stays (Parle-G, Maggi).'),
    ('Price-wage spiral?', 'Prices up, wages up, prices up again.'),
    ('Reflation?', 'Government induces inflation to lift AD after a recession or deflation.'),
    ('Stagflation?', 'Low growth, high unemployment and high inflation together.'),
    ('Phillips Curve?', 'Inverse relation between inflation (wage growth) and unemployment; UK 1861-1957.'),
    ('Real interest rate?', 'RIR = NIR − inflation.'),
    ('Engel’s Law?', 'As income rises, the share spent on food falls.'),
    ('Fiscal drag?', 'Inflation pushes people into higher tax brackets; an automatic stabiliser.'),
]
c.summary = 'Price versus price level, AD-AS causes, indexing with the worked example, CPI and WPI, the 2024=100 CPI, headline, core and skewflation, stagflation and the Phillips Curve, who gains and loses, Engel’s Law, fiscal drag and the cure. No PYQs quoted.'
