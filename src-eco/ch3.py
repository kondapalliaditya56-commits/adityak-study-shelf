from lib import Ch

c = Ch(3, 'Unemployment: Measures, Types, Causes and Labour Market',
       'Economy · GS Foundation · Chapter 3',
       [('hb', 'Handout only: no class slides'), ('', 'Handout pages 1-34'), ('', '10 Prelims PYQs quoted')],
       'Who counts as unemployed, the PLFS and its two approaches (usual status and current weekly status), the types of unemployment, how demand and supply explain wage-rate unemployment, India’s PLFS numbers and what hides behind them, jobless growth, the skill mismatch, labour laws, formal and informal work, the four Labour Codes, fixed-term employment and the schemes.')

c.sec('Exam lens: priority and PYQs', 'exam-lens-priority-and-pyqs')
c.call('alert', 'Source note', [
    '**This chapter comes from the handout only.** No class slides and no teacher ink came with it. The handout ends with a **UPSC Prelims PYQs** section of **10 questions** (years quoted: 2011, 2012, 2013 twice, 2017, 2018 twice, 2020, 2021, 2022). **Mains PYQs: none quoted in the material.**',
    'Priority here comes from the handout’s own signals: the 10 PYQs, the “Crucial Prelims Fact” on gratuity, and the “do not memorise, just understand” note on NSSO definitions.'])
c.table('Prelims PYQs quoted in the handout (answers as printed in the handout)', ['Year', 'What was asked', 'Answer in handout', 'Trap / where covered'], [
    ['2022', 'Which body compiles information on industrial disputes, closures, retrenchments and layoffs in factories?', '(c) Labour Bureau', 'Handout gives only the answer. The body is not discussed in the chapter text'],
    ['2021', 'Casual workers: EPF for all, regular hours and overtime for all, wages through bank account by notification', '(b) 2 and 3 only', 'Word “all” in statements 1 and 2. Handout gives only the answer. Related: Section 8 (labour laws, Code on Wages)'],
    ['2020', 'Post-1991: worker productivity, rural share of workforce, non-farm economy, rural employment growth', '(b) 3 and 4 only', 'Handout gives only the answer. Related: Section 6 (employment share of agriculture)'],
    ['2018', 'Rise in real GNP does not mean higher development if…', '(c) poverty and unemployment increase', 'Links Chapter 1 and this chapter'],
    ['2018', 'PM Kaushal Vikas Yojana: flagship of Ministry of Labour and Employment? soft skills, entrepreneurship, digital literacy? align the unregulated workforce to the NSQF?', '(c) 2 and 3 only', 'Statement 1 is the trap. Related: Section 9 (PMKVY)'],
    ['2017', 'National Career Services: initiative of DoPT? launched in mission mode for uneducated youth?', '(d) Neither 1 nor 2', 'Handout gives only the answer. Not in the chapter text'],
    ['2013', 'Disguised unemployment generally means…', '(c) marginal productivity of labour is zero', '**Direct hit:** Section 4, disguised UE'],
    ['2013', 'Economic growth in country X will necessarily occur if…', '(c) there is capital formation in X', 'Handout gives only the answer. Not discussed in the chapter text'],
    ['2012', 'How does the National Rural Livelihood Mission seek to improve livelihoods of the rural poor?', '(b) 2 only (strengthening SHGs and skill development)', 'Not in the chapter text. Statement 3 (free inputs) is the trap'],
    ['2011', 'Who is eligible for MGNREGA?', '(d) Adult members of any household', 'Section 9 says it guarantees 100 days to rural households that demand unskilled manual work'],
], rowhead=False)
c.call('note', 'How the years were counted', 'The list above is the ten questions printed in the handout. The years are “years quoted”: 2013 and 2018 each appear twice. Only 2013 (disguised UE), 2018 (PMKVY) and the schemes sit squarely inside the chapter text. Several PYQs (Labour Bureau, NCS, NRLM, capital formation) are quoted **without any explanation** in this handout, so their answers are carried from the handout and not explained.')
c.call('key', 'What to prepare', [
    '**Prelims hooks:** the definition set (WAP, dependents, dependency ratio, labour force, LFPR, UR, WPR); working age 15-64 versus 15+; US (PS+SS) versus CWS and which gives the higher rate; PS 183 days, SS 30 days, CWS 1 hour in 7 days; the types of unemployment (above all disguised UE with MPL zero); floor, minimum, fair and living wage order; NRU and NAIRU; employment elasticity; organised versus unorganised and formal versus informal; the four Labour Codes; fixed-term employment and gratuity after 1 year; the schemes and their problems.',
    '**Mains hooks:** why UR is falling but not for the right reasons; jobless growth versus the numbers; skill mismatch and the youth-education paradox; informalisation and the compliance burden; productivity versus employment as a false choice; gig workers and the new codes.',
    '**Closing idea:** India’s problem is not too little growth or too few jobs. It is a mismatch between aspirations and skills, and a labour market split between protected and unprotected workers.'])

c.sec('1 · Who is unemployed? The demographic divisions')
c.p('The standard definition: **unemployment is “a situation where someone who is able as well as willing to work, is unable to find work”.** The handout quotes Mankiw, Samuelson-Nordhaus and Blanchard: the unemployed have no job, are available for work and have actively looked for work in the previous four weeks. “Not working” is a large set; “unemployed” is a **subset** of it, because the grandparent, the young child or the homemaker who is not looking is not unemployed.')
c.p('The main source for Indian definitions is the **Periodic Labour Force Survey (PLFS)** of the NSSO. The RBI and the Ministry of Labour generally align with it; the **ILO** sets the global standard.')
c.table('The building blocks', ['Term', 'Meaning in the handout'], [
    ['**Working Age Population (WAP)**', 'People in the age group considered fit for economic activity. In India (NSSO/PLFS) this is typically **15 years and above**. The ILO often uses **15-64**'],
    ['**Dependents**', 'Those not in the WAP: **children (0-14)** and, in many contexts, **senior citizens (65+)**. The word is reserved for the non-working-age population'],
    ['**Dependency Ratio (DR)**', 'Dependents ÷ people of working age × 100. DR = [Population (0-14) + Population (65+)] ÷ Population (15-64) × 100'],
    ['**Labour Force (LF)**', 'People who are **working or looking for work**: both able and willing. Splits into the employed and the unemployed'],
    ['**Not in Labour Force**', 'Unable or unwilling to work: students, rentiers, the disabled, those in domestic duties'],
    ['**Able to work**', 'Physical and mental capacity. Age is only a filter applied later'],
    ['**Willing to work**', 'A genuine effort: the **active search** criterion (applying for jobs, registering at exchanges) in the reference period'],
    ['**LFPR**', 'Labour force in a cohort ÷ total population of the cohort × 100. Can be crude (whole population), 15+ (the commonly reported one) or for a specific group such as married women aged 21-30'],
    ['**Unemployment rate (UR)**', '**n(UE) ÷ n(LF)**, and n(LF) = n(Emp) + n(UE). So UR = UE ÷ (Emp + UE). It is a share of the labour force, **not** of the population'],
    ['**Worker Population Ratio (WPR)**', 'Employed persons ÷ total population. Expressed per 1000 persons'],
], rowhead=True)
c.call('teacher', 'Handout stress: which working age?', [
    'The handout spends a page on one exam trap: the **working age.** If the question is about **demographics** (demographic dividend, population pyramids, dependency ratio) the answer is **15-64**, because at 65 people are globally classified as elderly dependents.',
    'If the question is about **India’s NSSO/PLFS metrics** (LFPR, UR, WPR) the answer is **15 years and above**, because India’s informal sector lacks universal social security and a 70-year-old farmer cannot afford to retire. The handout says the first reading is “not wrong”; the second “becomes more right” in this context.'])
c.call('alert', 'Handout alert: formula wording', 'The handout writes the dependency ratio’s denominator as “people in the working age” and then as 15-64 in the formula, while its PLFS tables use 15+. **Rule for the exam hall:** DR uses 15-64; LFPR, UR and WPR as reported by the PLFS use 15+.')

c.sec('2 · What counts as employment')
c.p('Employment is **not just a 9-to-5 job.** The NSSO defines it through **economic activities**, using the System of National Accounts (SNA) boundary (SNA is covered in the National Income Accounting handout). A salary is not mandatory.')
c.ul([
    '**Self-employment:** own-account workers (a street vendor, a consultant) and employers.',
    '**Unpaid family helpers:** a child helping in a parent’s kirana store counts as employed even without cash.',
    '**Casual labour:** daily-wage work in construction or agriculture.',
    '**Regular salaried:** employees with a contract and monthly pay.',
    '**Remuneration can be in kind** (food, clothing, a place to stay), **in assets** (shares or equity), or **exchange labour** (two farmers working each other’s fields).'])
c.table('Economic or not?', ['Activity', 'Employed?', 'Why'], [
    ['Running a business for profit', 'Yes', 'Economic activity for profit'],
    ['Working in a family shop (unpaid)', 'Yes', 'Contributing to a family economic enterprise'],
    ['Farming for own consumption', 'Yes', 'Production of goods for self-consumption (inside the SNA boundary)'],
    ['Domestic work for own family', 'No', 'Non-economic, non-market activity'],
    ['Paid domestic work for others', 'Yes', 'Market activity for remuneration'],
    ['Volunteer work for an NGO', 'No', 'Usually excluded: no remuneration or profit intent'],
], rowhead=True)
c.p('**NSSO wording (the handout says understand, do not memorise).** Workers: persons engaged in any economic activity, or who despite attachment to it abstained for illness, injury, disability, bad weather, festivals or other contingencies. Unemployed: persons who, owing to lack of work, had not worked but sought work (exchanges, intermediaries, friends or relatives, applications) or expressed willingness or availability for work. “Able to work” is purely physical and mental capacity: the NSSO has a code (**Code 95**) for those not able to work owing to disability and does not use age. A 13-year-old working at a tea stall is counted as employed in the raw data.')

c.sec('3 · Measuring unemployment: PLFS, US and CWS')
c.p('The NSSO measures unemployment through the **PLFS.** Earlier it used the **EUS** (Employment-Unemployment Survey), carried out about once in 5 years. The PLFS has a larger sample, higher frequency and better technology: an **annual** survey where sampled households are **visited once every month**. Field investigators ask how household members spent their time over set reference periods, and each person is classified into one of three statuses: **Working, Seeking/Available for work, Not in labour force.**')
c.flow([
    ('1 · Lay down two standards', 'One to decide whether a person is in the LF; one to decide, if in LF, whether working'),
    ('2 · Take a representative sample', 'Collect data relevant to the standards'),
    ('3 · Apply the standards', 'Status A: neither working nor looking (not in LF). Status B: working (employed). Status C: not working (unemployed)'),
    ('4 · Compute UR', 'n(status = UE) ÷ [n(status = Emp) + n(status = UE)]', 'good'),
], 'How the PLFS arrives at the unemployment rate (same logic as poverty: standard, sample, information, application)')
c.p('An “approach” is simply a standard. As with poverty, a person can be “working” on one approach and not even in the LF on the other. The PLFS uses two.')
c.table('Usual Status (US) versus Current Weekly Status (CWS)', ['Point', 'Usual Status (US)', 'Current Weekly Status (CWS)'], [
    ['**Reference period**', 'One year (365 days)', 'The 7 days before the survey'],
    ['**Criterion**', '**Majority time**: what was the person doing for most of the period', '**Priority**: Working beats Unemployed beats Not in LF'],
    ['**In LF if**', 'Working or seeking work for the majority of the year (**≥ 183 days**) = Principal Status (PS)', 'Worked or was available for work at any point in the 7 days'],
    ['**Working if**', 'PS: worked the majority of the days in the LF. SS: worked at least **30 days** in the year', 'Worked for **at least 1 hour on any 1 day** in the week'],
    ['**Unemployed if**', 'In LF but did not work for the majority of LF days (PS); and on SS, did not work even 30 days', 'Did not work even an hour but was seeking or available for work for at least 1 hour on any day'],
    ['**What it captures**', 'Chronic or long-term (structural) picture; smooths seasonal bumps', 'Short-term fluctuations and underemployment; closer to ILO standards; reacts quickly to shocks'],
    ['**Which UR is higher?**', 'Generally lower', '**Generally higher.** Short recall makes answers accurate and captures seasonality'],
], rowhead=True)
c.h3('Principal and Subsidiary status in detail')
c.ul([
    '**PS (Principal Status):** in the LF if working or seeking for ≥ 183 days. Then “employed” if work was found for the majority of the days in the LF. Example: LF for 200 days and work for 120 days gives employed.',
    '**SS (Subsidiary Status):** a person who is principally unemployed but found work for at least 30 days is **employed on SS.** Anyone with work for at least 30 days in the year is employed on SS basis. Unemployed on both PS and SS means not even 30 days of work.',
    '**UPSS** (Usual Principal and Subsidiary Status) merges both: a person is employed if a worker in either capacity. This deliberately captures invisible labour, for example millions of women whose principal status is domestic duties but who spend about 40 harvest days in farm labour.'])
c.table('The handout’s four-person example', ['Person', 'Days working', 'Days looking', 'Total LF days', 'In LF (≥ 183)', 'PS employed', 'SS employed'], [
    ['A', '150', '0', '150', 'No (not in LF)', '-', 'Yes (≥ 30 days)'],
    ['B', '110', '90', '200', 'Yes', 'Yes (110 ≥ 100)', 'Yes'],
    ['C', '140', '160', '300', 'Yes', 'No (140 < 150)', 'Yes'],
    ['D', '25', '275', '300', 'Yes', 'No', 'No (25 < 30)'],
], rowhead=True)
c.call('example', 'Worked example from the handout (population 1000)', [
    'Not in LF = 200; LF = 800. Principal status: employed 600, unemployed 200. Of the 200 principally unemployed, subsidiary status: employed 150, unemployed 50.',
    '**UR (PS) = 200 ÷ 800 = 25%** and **UR (PS+SS) = 50 ÷ 800 = 6.25%.** The handout calls **UR (PS+SS) the headline rate**: the one the government uses and quotes without naming the approach, because those with no work even for 30 days are the chronically unemployed and the priority.'])
c.call('note', 'Reading the table', 'Person A (150 working days, none spent looking) is **not in the LF** on the principal-status test (150 < 183) but is still counted as **employed on subsidiary status**, because the work was at least 30 days. This is exactly why UPSS merges the two. **Rule for the exam hall:** first the LF test (≥ 183 days), then PS, then SS.')
c.call('note', 'CDS dropped', 'Up to 2012 the EUS also used the **Current Daily Status (CDS)** approach, which measured underemployment by the time worked on each day of the last week. It was dropped in the PLFS because the data now come far more frequently, from a larger sample and with monthly visits.')

c.sec('4 · Types of unemployment')
c.table('The types at a glance', ['Type', 'What it is', 'Handout’s example or cause'], [
    ['**Structural**', 'Joblessness from a fundamental **mismatch** between skills workers have and skills employers demand, or between worker and job location. Long-term and dangerous: workers are “immobile” from the old structure to the new', 'Agriculture to industry; new technology; automation displaces low-skilled factory labour while AI developers are scarce'],
    ['**Seasonal**', 'Predictable drops in labour demand at specific times of year', 'Agriculture outside harvest; tourism off-season; construction in the rains'],
    ['**Frictional**', 'The “search time” to match worker and job under imperfect information. A certain level is healthy. Job portals have reduced it', 'Quitting one job and not yet finding another; fresh graduates entering the workforce'],
    ['**Voluntary**', 'In the LF, offered a job, but chooses not to accept it, and so counted as unemployed', 'Below one’s dignity; skills higher than required; unacceptable terms (timing, location, wages); lucrative unemployment benefits'],
    ['**Underemployment** (*employment*, not unemployment)', 'Officially employed but the job does not use skills, education or hours on offer. **Invisible:** over-qualified, over-skilled. **Visible:** wants longer hours', 'PhD holders applying for peon or sweeper posts; 3 hours of work in an 8-hour day (the old CDS test)'],
    ['**Disguised**', 'More workers than needed; the extra workers add **no output.** Their **marginal product of labour (MPL) is zero** (or negative). Recorded as employed, so the reality is hidden', 'A 2-acre family farm that needs 2 people but has 5 brothers: output stays 100 quintals, so the 3rd, 4th and 5th brother have MPL zero. A hallmark of Indian agriculture'],
    ['**Wage-rate (classical)**', 'Wages stay **above equilibrium** and cannot fall, so labour supply exceeds demand permanently', 'Minimum wages fixed above equilibrium by law; strong unions bargaining wages up'],
    ['**Cyclical (Keynesian)**', 'Extra unemployment above the natural rate because growth is slower than expected (a downturn in the business cycle)', 'Falls when aggregate demand grows fast; rises when it slows'],
], rowhead=True)
c.call('teacher', 'Handout stress: marginal product', 'Marginal product of the (n+1)th worker = output with n+1 workers minus output with n workers. If n workers produce x and n+1 produce x + y, the marginal output is y. Disguised unemployment is where y = 0. This is the 2013 PYQ.')
c.call('alert', 'Handout alert: underemployment is not unemployment', 'The handout flags the word: it is **employment**, not unemployment. An underemployed person’s working status remains **employed.** **Rule for the exam hall:** underemployment and disguised unemployment both sit inside “employed” in the statistics.')

c.sec('5 · Demand, supply and the market (needed for wage-rate unemployment)')
c.p('The handout inserts the basics of markets here so that wage-rate unemployment can be understood.')
c.ul([
    '**Demand** exists only when there is both **ability** and **willingness.** Quantity demanded (QD) is what is actually asked for. Factors: price, income, taste, culture, geography (season), population size, substitutes.',
    '**Law of demand** (ceteris paribus): QD varies **inversely** with price. If another factor changes, the curve **shifts**.',
    '**Supply** needs both ability and willingness. Quantity supplied is what **is being** produced. Factors: price, profitability, raw materials, labour, capital, ease of doing business and policy, investment (especially R&D), infrastructure.',
    '**Law of supply** (ceteris paribus): quantity supplied varies **directly** with price.',
    '**Price takers.** Producers and consumers take the price the market offers. Under perfect competition (identical goods, no entry or exit barriers) no one can set a price. In real markets competition is imperfect and producers have limited pricing power. **Only in a monopoly are producers price setters.**',
    '**A market is a place of exchange of information** and so of rationalising expectations, not merely a place.'])
c.flow([
    ('Start: some random price P1', 'At P1, quantity supplied is greater than quantity demanded: **excess supply**'),
    ('Sellers fear unsold stock', 'They cut prices: downward pressure. New buyers enter (QD rises), some sellers exit (QS falls)', 'warn'),
    ('Price adjusts to P0', 'QS = QD. No excess supply, no downward pressure', 'good'),
    ('If the start price was P2 (below P0)', 'QD > QS: **excess demand.** Buyers bid prices up until QS = QD at P0'),
    ('Equilibrium price and market clearance', 'At P0 everyone who came to sell has sold and everyone who came to buy has bought. Equilibrium is rarely seen because factors keep changing; the price is always adjusting towards it', 'good'),
], 'How a market reaches equilibrium (as the handout explains it)')
c.p('**The labour market works the same way.** Firms demand labour; the labour force supplies it. **Demand for labour (DL) ∝ 1 ÷ wages** (high wages, fewer workers wanted); **supply of labour (SL) ∝ wages** (high wages, more people willing to work). Factors for DL: wages, price of substitutes such as machines, skill, number of firms, willingness to hire given complex laws. Factors for SL: wages, terms and conditions, education and skill level of the population. If wages above equilibrium cannot adjust downwards, there is permanent excess supply: **wage-rate unemployment.**')

c.sec('6 · Four kinds of wage, and cyclical unemployment')
c.table('Types of wages', ['Wage', 'What it is', 'Focus'], [
    ['**Floor wage**', 'A **central baseline** set by the Union Government (Code on Wages, 2019). States cannot set minimum wages lower than it, which prevents a race to the bottom', 'Absolute national bottom'],
    ['**Minimum wage**', 'The lowest legal pay for a category of work. **State governments** primarily set it, so a factory worker in Haryana may have a different one from Bihar. Designed to prevent extreme exploitation', 'Survival'],
    ['**Fair wage**', 'Between the minimum and the living wage; capped by what the industry can afford. Formalised by the **Committee on Fair Wages (1948).** Depends on prevailing area rates, productivity and profitability', 'Industry capacity to pay and worker’s willingness'],
    ['**Living wage**', 'A **normative** wage for a decent standard of living: nutrition, housing, healthcare, children’s education, transport, savings. Ignores whether the employer can afford it. Almost always above the statutory minimum', 'Decent life and dignity'],
], rowhead=True)
c.call('key', 'Order to remember', '**Floor wage ≤ Minimum wage ≤ Fair wage ≤ Living wage.**')
c.h3('Cyclical (Keynesian) unemployment')
c.ul([
    'A firm hires because it **needs** workers, and that depends on the demand for the goods it expects to sell. At the economy level, demand for workers is **derived from aggregate demand (AD).**',
    '**UR falls only when employment growth is faster than labour-force growth.** Example: LF 100 (80 employed, 20 unemployed, UR 20%). LF rises 10% to 110 and employment rises 5% to 84. Unemployed = 26 and UR = 26 ÷ 110 = 23.6%, higher than 20%, even though jobs rose.',
    'Growth is **cyclical** (booms and recessions) and unemployment moves inversely. If growth is slower than an economist expected, the extra UR is **cyclical.**'])
c.h3('Natural rate of unemployment (NRU) and NAIRU')
c.ul([
    '**NRU:** the UR when wages are at equilibrium (zero wage-rate UE) and the cycle is neutral (zero cyclical UE). **NRU = frictional + structural + seasonal + voluntary UE.** At the NRU the economy is at **full employment** (which is **not** zero unemployment) and producing at **potential GDP.**',
    '**NAIRU** (Non-Accelerating Inflation Rate of Unemployment): comes from the Phillips Curve (covered in the Inflation chapter). If UR is pushed below it by printing money or heavy deficit spending, the labour market tightens, wages are bid up, a **wage-price spiral** starts and inflation accelerates.',
    'The actual UR can be counted. **NRU and potential GDP cannot be measured; they are estimated** and depend on the model. Example: UR is 8%. Economist A says NRU is 5% so cyclical UE is 3%; Economist B says NRU is 7% so cyclical UE is 1%.'])

c.sec('7 · Unemployment in India: the PLFS numbers')
c.p('India’s UR is measured by the PLFS, carried out every year since **2017.** It gives both US (PS+SS) and CWS rates; the CWS numbers are now released **monthly** for rural and urban areas. The survey period was July-June and has now changed to the **calendar year (Jan-Dec).**')
c.table('PLFS (usual status, age 15+)', ['Survey (July-June)', 'UR', 'LFPR (overall)', 'Female LFPR'], [
    ['2017-18', '6.0%', '49.8%', '23.3%'], ['2018-19', '5.8%', '50.2%', '24.5%'], ['2019-20', '4.8%', '53.5%', '30.0%'],
    ['2020-21', '4.2%', '54.9%', '32.5%'], ['2021-22', '4.1%', '55.2%', '32.8%'], ['2022-23', '3.2%', '57.9%', '37.0%'], ['2023-24', '3.2%', '60.1%', '41.7%'],
], rowhead=True)
c.table('Then and now', ['Indicator', '2017-18', '2023-24', 'Trend'], [
    ['LFPR', '49.8%', '60.1%', 'Rising'], ['WPR', '46.8%', '58.2%', 'Rising'], ['UR', '6.0%', '3.2%', 'Falling']], rowhead=True)
c.p('The handout calls this “outstanding”: a falling UR **with** a rising LFPR. Then it asks what is behind the numbers.')
c.h3('Critical analysis of the trends')
c.ul([
    '**LFPR is still low.** Handout comparators: Vietnam ~68.5%, China ~66.5%, South Korea ~63.5%, Japan ~63.2%, United States ~62.5%, Bangladesh ~61.9%. India crossed 60% for the first time in 2023-24.',
    '**The UR decline is not entirely desirable.** Between PLFS rounds 2 to 3 and 3 to 4 almost the whole fall came from (a) more **agricultural jobs** and (b) more **self-employment.**',
    '**Agriculture** already has disguised UE and underemployment and the lowest productivity, so a net rise in agricultural jobs is undesirable for a country wanting the demographic dividend.',
    '**Self-employment** is generally more productive and remunerative, but leaves workers vulnerable to shocks without safety nets, and much of it is **distress employment.**'])
c.table('Sector productivity (the handout’s table)', ['Sector', 'Share in GDP (₹)', 'Share in employment (workers)', 'Relative productivity (GDP ÷ employment)'], [
    ['Agriculture', '18', '46', '₹0.39 per worker'], ['Industry', '28', '25', '₹1.12 per worker'], ['Services', '54', '29', '₹1.86 per worker']], rowhead=True)
c.p('**Context.** Agriculture’s employment share was about **75% at independence,** fell below 50% around **2012,** reached about **44% before Covid,** and rose to about **46% by PLFS round 5** because only agriculture could absorb the laid-off. The last two surveys show it declining again. Self-employment has risen continuously and Covid only accelerated it. Firms prefer contractual workers (no compliance burden, flexible size), and a growing proportion of workers prefer self-employment for quicker earnings. The handout calls it “a low-income country with first world problems” and says the focus should be on reducing vulnerability and building skills.')
c.fig('eco-ur-education.jpg', 'Unemployment rate by education level (2024): illiterate close to nil, primary 1.1%, secondary 3.5%, higher education 12.9%. Among graduates in the labour force one in eight is unemployed. Source printed: PLFS 2023-24.')
c.fig('eco-ur-age.jpg', 'Unemployment rate among graduates by age group (2024): 20-24 years 37%, 25-29 years 19%, 30-34 years 8%, 35-39 years 2%, 40-44 years under 1%. Highest among recent graduates.')
c.fig('eco-ur-reasons.jpg', 'Graduates outside the labour force, by reason, gender and age (2024). Women: care and home commitments dominate (about 58% in the twenties, 91% in the thirties, 88% in the forties). Men in their twenties: education (96%).')
c.fig('eco-ur-situation.jpg', 'India’s unemployment situation (all-India, age 15+ and youth 15-29), Apr-Jun and Jul-Sep: all-India 5.4% and 5.2%; rural 4.8% and 4.4%; urban 6.8% and 6.9%; youth 14.6% and 14.8%; rural youth 13.1% and 13.1%; urban youth 17.9% and 18.4%. Source printed: MoSPI.')
c.call('alert', 'Handout alert: reading the chart numbers', 'The last figure is a newspaper-style graphic reproduced in the handout with small print. The quarter labels (Apr-Jun, Jul-Sep) and the values above are read from the picture. **Rule for the exam hall:** use the trend (youth and urban youth are far higher than the all-India rate), not the decimal points.')

c.sec('8 · Why is there unemployment in India? Low growth, jobless growth, or skills?')
c.h3('1 · Is our growth “low”?')
c.p('Post-1990s average growth is about **6.5%**, faster than the world average (**3.5%**) and the developing-country average (**~4.5%**). A plain “low growth” argument does not hold for most of the post-2000s.')
c.h3('2 · Jobless growth?')
c.p('**Employment elasticity (ε) = % change in employment ÷ % change in output.** If output grows 10% and employment 6%, ε = 0.6: **60% of growth comes from more workers and 40% from higher productivity.** Falling ε means growth is attributed more to productivity. Between **2004-09,** the fastest-growth period, ε fell to **about 0.01**; economists called this “jobless growth.”')
c.call('teacher', 'Handout’s critique of “jobless”', [
    'A falling elasticity should push UR up, but long-term UR (ILO data) has not risen. The reason: **employment growth, though falling, is still faster than labour-force growth.**',
    'So “jobless” is “misleading or at least too harsh”.'])
c.table('Three periods (handout figures)', ['Period', 'Labour force growth', 'Employment growth', 'Reading'], [
    ['**Sluggish decade** 2000-01 to 2011-12', '~1.8%', '~1.5-1.6%', 'LF faster than jobs: rising UE. 2004-2010 employment growth near 0%'],
    ['**Lost and found** 2011-12 to 2020-21', '~1.3% (volatile)', '~1.2%', 'Workforce stagnated or shrank to 2017 as women left the LF (female LFPR ~23%); 2017-21 distress pulled women back as unpaid agricultural helpers'],
    ['**Surge** 2017-18 to 2023-24', '~4.5%', '~5.0%', 'WPR 46.8% to 58.2%; workforce up ~36%, about **170 million jobs** in 7 years; UR falls to 3.2%'],
], rowhead=True)
c.call('alert', 'Handout alert: the “surge” and the data', 'The handout says the surge appears “as soon as we start collecting data in a better manner” (the PLFS captures the informal sector better). Part of the surge is therefore better counting and, as Section 7 shows, much of it is agriculture and self-employment. **Rule for the exam hall:** quote the surge together with its quality caveat.')
c.h3('Productivity versus employment: a false choice')
c.ul([
    '**Cannot be inefficient:** if Indian firms avoid technology to save jobs, China or Vietnam will undercut them, the firm may go bankrupt and everyone loses their job.',
    '**The goal is decent jobs, not just more jobs.** (Hire a million people to dig holes with spoons and another million to fill them in: 0% UE, but poor.) A high wage needs a highly productive worker.',
    '**Falling elasticity is not always bad:** one skilled worker may produce what ten once did. It is bad only if total jobs do not absorb new entrants.',
    'The answer is “to skill our youth so they can run the machines”, not to break them.'])
c.h3('3 · The key reason: aspirations and skills do not match')
c.ul([
    'The handout’s conclusion: not lack of growth or jobs, but a mismatch between **aspirations and skills** versus the jobs. That is **voluntary and structural unemployment.**',
    '**Voluntary:** the job matching the worker’s skill exists but fails the worker’s aspiration. **Structural:** the aspired job exists but the worker lacks the skill; the job stays vacant.',
    '**Youth-education paradox:** as education rises, wage and status expectations rise. The young, educated and non-poor can afford the “luxury of unemployment”. **Unemployment is a luxury only the non-poor can afford; the poor are too poor to be unemployed.** With age the buffer runs out: they accept lower-skilled work or drop out of the LF (**hidden unemployment**).',
    '**India Skills Report** (Wheebox with CII, AICTE and AIU; the WNET test): graduate employability hovers around **50% to 55%** (ISR 2024/2025).',
    'Graduate UR is estimated at **13%**, close to nil for those with no education. The LFPR of women with diplomas/certificates is about **55%** versus about **89%** for men. Youth (15-29) urban UR stays high while older groups collapse to near zero.',
    'The remedy: **skills and vocational training,** plus better wages in lower-skilled jobs.'])
c.call('alert', 'Handout alert: two UR numbers for graduates', 'The text says graduate UR is “estimated at 13 percent”; the chart in Section 7 prints **12.9%** for higher education (2024). They are the same estimate, rounded. **Rule for the exam hall:** write “about 13%”.')

c.sec('9 · Nature of employment: labour laws, formal and informal work')
c.p('**Labour laws** govern the employer-employee relationship (who is a worker, leave, safety, misconduct, night shifts for women). The pre-2020 laws the handout lists:')
c.table('Key pre-2020 labour laws', ['Year', 'Act', 'What it does'], [
    ['1926', 'Trade Unions Act', 'Registration, rights and regulation of trade unions for collective bargaining'],
    ['1936', 'Payment of Wages Act', 'Wages on time; no arbitrary deductions'],
    ['1947', 'Industrial Disputes Act', 'Employer-union relations: strikes, lockouts, layoffs, retrenchment'],
    ['1948', 'Minimum Wages Act', 'Government fixes minimum wages for scheduled occupations'],
    ['1948', 'Factories Act', 'Safety, health and welfare in factories (hours, ventilation, hazardous work)'],
    ['1952', 'Employees’ Provident Funds and Miscellaneous Provisions Act', 'Compulsory employer and employee contributions: retirement corpus, pension, insurance'],
    ['1961', 'Maternity Benefit Act', 'Paid maternity leave (currently 26 weeks); no firing for pregnancy'],
    ['1970', 'Contract Labour (Regulation and Abolition) Act', 'Conditions of contract labour; can abolish it in certain core industries'],
], rowhead=False)
c.p('Till 2019 India had **over 40 central and over 100 state labour laws.** Compliance was costly (“Inspector Raj”). A small firm stays off the radar and risks non-compliance; as it grows, its compliance cost rises exponentially. So it hires **indirectly** (for example security guards through a contractor). Law makes no distinction between workers: **the formal/informal split is an artificial distinction created by firms** to cut compliance cost. Ways to formalise: PF contributions, tax deducted at source, a formal contract.')
c.table('Two different classifications (NCEUS or Arjun Sengupta Committee)', ['', 'Organised vs unorganised', 'Formal vs informal'], [
    ['**Looks at**', 'The **enterprise** (ignores the workers)', 'The **worker’s** contract and benefits (ignores firm size)'],
    ['**Organised / formal**', 'Registered, incorporated, bound by formal accounting and labour laws; government, registered bodies, private firms with 10+ workers (with power) or 20+ (without)', 'Written contract, paid leave and above all **social security** (PF, ESIC, pension, maternity) paid by the employer'],
    ['**Unorganised / informal**', '“All unincorporated private enterprises owned by individuals or households…on a proprietary or partnership basis and with **less than ten** total workers”', 'Workers in unorganised enterprises or households, excluding regular workers with social security, **and** workers in the formal sector without employment and social security benefits from employers'],
], rowhead=True)
c.table('Four boxes', ['', 'Formal worker', 'Informal worker'], [
    ['**Organised enterprise**', 'Software engineer at Infosys; government bank manager', '**Informalisation of the formal sector:** a contract guard or cleaner at a big IT park or factory, hired through a contractor (no PF, leave or job security)'],
    ['**Unorganised enterprise**', 'Statistically almost non-existent', 'Farm labourer, street vendor, assistant at a tiny bakery. About **80%+** of India’s workforce'],
], rowhead=True)
c.ul([
    '**Gig and platform workers** (defined in the NITI Aayog report “India’s Booming Gig and Platform Economy”): treated as “independent contractors” or “partners” by platforms (Uber, Swiggy, Urban Company), outside the employer-employee relationship, with no social security.',
    '**Contractual employment** is the bridge between the organised sector and informal labour: hired for a period or task, often through a third-party agency. NITI Aayog points out that rigid laws (hard to fire permanent staff) pushed the organised sector towards contract workers.'])
c.h3('The solution: four Labour Codes (2019-2020)')
c.p('The government amalgamated **29 central labour laws into four codes:**')
c.table('The four Labour Codes', ['Code', 'Main point in the handout'], [
    ['**Code on Wages, 2019**', 'Universalises minimum wages and timely payment, including the unorganised sector'],
    ['**Code on Social Security, 2020**', 'First legal framework for social security funds for gig, platform and unorganised workers. Gratuity after **1 year** for fixed-term employees'],
    ['**Occupational Safety, Health and Working Conditions Code, 2020**', 'Streamlines safety rules; heavily regulates the use of contract labour'],
    ['**Industrial Relations Code, 2020**', 'Simplifies dispute resolution and gives firms somewhat more hiring and firing flexibility'],
], rowhead=True)
c.h3('Fixed-term employment (FTE)')
c.ul([
    'Direct hiring for a **pre-determined period** on a written contract; it ends automatically unless renewed. Introduced across all sectors to fix the exploitation of contract workers hired through agencies.',
    '**Parity with permanent workers:** same working hours, wages, allowances and statutory benefits (EPF, ESIC).',
    '**Gratuity (crucial Prelims fact):** a permanent employee needs **5 years** of continuous service, a fixed-term employee becomes eligible after **1 year** under the Code on Social Security, 2020.',
    '**What they lack:** long-term job security. Expiry is **not retrenchment,** so no notice and no retrenchment compensation.',
    '**Superior to contract workers:** on the principal employer’s direct payroll, no middleman cut, social security guaranteed, cannot be paid less for the same work.',
    'In the handout’s words, FTE gives the worker the **social security of a formal job** and the employer the **hiring flexibility of an informal job.**'])

c.sec('10 · Schemes: the problem each one fixes')
c.table('Problem and fix (the handout’s summary)', ['Problem', 'Fix'], [
    ['Employer compliance burden', 'Shram Suvidha'], ['Unorganised worker vulnerability', 'e-Shram and PM-SYM'], ['Structural skill mismatch', 'PMKVY (Skill India)'],
    ['Lack of formal jobs (jobless growth)', 'PLI and ELI schemes'], ['Rural distress and cyclical shocks', 'MGNREGA'],
], rowhead=True)
c.table('The schemes in detail', ['Scheme', 'What the handout says'], [
    ['**e-Shram portal** (2021)', 'First **National Database of Unorganised Workers.** Gives a **Universal Account Number (UAN)**. Lets the government transfer cash or food to vulnerable workers in a shock'],
    ['**PM Shram Yogi Maan-dhan (PM-SYM)**', 'Voluntary, contributory **pension** for unorganised workers earning **under ₹15,000 a month.** Worker pays e.g. ₹55-200 a month, the government **matches** it, pension **₹3,000 a month after age 60**'],
    ['**Shram Suvidha portal**', 'Employer side: a **Labour Identification Number (LIN),** single consolidated online returns, **randomly assigned inspectors** by computer (removes bribery and bias). Cuts compliance cost so firms hire formally'],
    ['**PMKVY / Skill India**', 'Flagship for the skill mismatch: short-term, industry-relevant training for dropouts and unemployed youth. **Recognition of Prior Learning (RPL)** certifies existing skills (a traditional carpenter) so workers can bargain for better wages'],
    ['**PLI scheme**', 'Subsidies to companies **only if** they meet domestic production targets. Drives derived demand for semi-skilled and skilled labour'],
    ['**ELI scheme** (Budget 2024-25)', 'Subsidises **job creation:** the government pays a portion of **EPFO contributions for first-time employees** entering the formal workforce, lowering the employer’s cost of hiring'],
    ['**MGNREGA / VB-GRAM(G)**', 'Guarantees **100 days** of wage employment to rural households demanding unskilled manual work. Acts as a shock absorber and a legal floor for rural wages'],
], rowhead=True)
c.call('alert', 'Handout alert: the scheme name', 'The handout writes “MGNREGA/VB-GRAM(G)” for the rural job guarantee and does not explain the second name. **Rule for the exam hall:** the 2011 PYQ uses “Mahatma Gandhi National Rural Employment Guarantee Act”; write that.')

c.mm = ('Unemployment', [
    ('Who is unemployed', [('Able and willing, not finding work', None), ('WAP, dependents, DR', '15-64 vs 15+'), ('LF, LFPR, UR, WPR', 'UR = UE / LF')]),
    ('What counts as work', [('Economic activity', 'incl. unpaid helpers'), ('Domestic chores: no', None), ('Own-consumption farming: yes', None)]),
    ('Measuring (PLFS)', [('US: PS 183 days, SS 30 days', 'headline PS+SS'), ('CWS: 1 hour in 7 days', 'higher rate'), ('CDS dropped', None)]),
    ('Types', [('Structural, seasonal, frictional', None), ('Voluntary, underemployment', None), ('Disguised: MPL zero', None), ('Wage-rate and cyclical', None), ('NRU and NAIRU', None)]),
    ('India: the numbers', [('UR 6.0 to 3.2', 'LFPR 49.8 to 60.1'), ('Fall = agriculture + self-employment', None), ('Graduate UR about 13%', None)]),
    ('Why', [('Not low growth', '6.5% vs 3.5%'), ('Jobless growth? ε about 0.01', None), ('Key: skills vs aspirations', 'voluntary + structural')]),
    ('Labour market', [('29 laws into 4 Codes', None), ('Organised vs formal', None), ('Fixed-term: gratuity at 1 year', None), ('Gig and contract', None)]),
    ('Schemes', [('e-Shram, PM-SYM, Shram Suvidha', None), ('PMKVY, RPL', None), ('PLI, ELI', None), ('MGNREGA 100 days', None)]),
])

c.timeline = [
    ('1926', 'Trade Unions Act', False),
    ('1936', 'Payment of Wages Act', False),
    ('1947', 'Industrial Disputes Act', False),
    ('1948', 'Minimum Wages Act, Factories Act and the Committee on Fair Wages', False),
    ('1952', 'Employees’ Provident Funds and Miscellaneous Provisions Act', False),
    ('1961', 'Maternity Benefit Act (26 weeks today)', False),
    ('1970', 'Contract Labour (Regulation and Abolition) Act', False),
    ('2004-09', 'Employment elasticity falls to about 0.01: the “jobless growth” period', True),
    ('2012', 'Last year of the CDS approach in the EUS', False),
    ('2017', 'PLFS starts as an annual survey', True),
    ('2017-18', 'UR 6.0%, LFPR 49.8%, WPR 46.8%, female LFPR 23.3%', True),
    ('2019', 'Code on Wages (floor wage, universal minimum wage)', False),
    ('2020', 'Codes on Social Security, OSH and Industrial Relations', False),
    ('2021', 'e-Shram portal launched', False),
    ('2023-24', 'UR 3.2%, LFPR 60.1% (first time above 60%), WPR 58.2%, female LFPR 41.7%', True),
    ('2024-25', 'Employment Linked Incentive scheme announced in the Budget', False),
]

c.connects = [
    ('[Chapter 1: Poverty](eco-ch01.html)', 'The 2018 PYQ ties poverty and unemployment to development. The poor are “too poor to be unemployed”, so UR is not a poverty measure.'),
    ('[Chapter 2: Inequality](eco-ch02.html)', 'The handout asks the reader to see the skills and jobs schemes through “our discussion on inclusive growth”: capability (skills) and opportunity (jobs).'),
    ('National Income Accounting handout', 'The handout says the System of National Accounts, which draws the production boundary used to decide what counts as employment, is covered there.'),
    ('Inflation handout', 'NAIRU comes from the Phillips Curve, which the handout says is studied in the inflation chapter.'),
    ('Money, Banking and Budget handouts', 'The Budget announced the ELI scheme (2024-25); the handout points to PLI and the schemes in the same breath as manufacturing growth.'),
]

c.recall = [
    'Unemployed = able and willing, in the labour force, not finding work. UR = UE ÷ LF (not ÷ population). LF = Emp + UE.',
    'Working age: 15-64 for demographics and dependency ratio; 15+ for PLFS (LFPR, UR, WPR).',
    'Employment includes unpaid family helpers, own-consumption farming and pay in kind; domestic chores and volunteering are excluded.',
    'US: PS needs ≥ 183 days in LF; SS needs ≥ 30 days of work; headline = PS+SS. CWS: 1 hour in 7 days; priority rule; higher UR. CDS dropped.',
    'Example: pop 1000, LF 800, UR(PS) 25%, UR(PS+SS) 6.25%.',
    'Types: structural (skills mismatch), seasonal, frictional (search time), voluntary, underemployment (employed!), disguised (MPL zero), wage-rate (wages stuck high), cyclical (below-potential growth).',
    'Wage order: floor ≤ minimum ≤ fair ≤ living. Floor: Centre; minimum: states; fair: 1948 committee.',
    'NRU = frictional + structural + seasonal + voluntary. Full employment ≠ zero UE. NAIRU: below it, inflation accelerates. Both are estimates.',
    'PLFS: UR 6.0 to 3.2, LFPR 49.8 to 60.1, WPR 46.8 to 58.2, female LFPR 23.3 to 41.7 (2017-18 to 2023-24).',
    'UR fell because of agriculture and self-employment; agriculture is 46% of workers but 18% of GDP.',
    'Not low growth (6.5% vs 3.5%). Jobless growth: ε about 0.01 in 2004-09, but employment growth still beats LF growth. Real cause: skills versus aspirations.',
    '29 laws into 4 codes. Organised versus unorganised is about the firm; formal versus informal is about the worker. Gratuity: 5 years permanent, 1 year fixed-term.',
    'Schemes: e-Shram (2021, UAN), PM-SYM (₹3,000 after 60), Shram Suvidha (LIN), PMKVY and RPL, PLI, ELI (EPFO for first jobs), MGNREGA (100 days).',
    'Blank page: draw the PS/SS/CWS comparison, then list the eight types with one example each.',
]

c.mcq = [
    {'q': 'In India, which one of the following compiles information on industrial disputes, closures, retrenchments and layoffs in factories employing workers? (2022)', 'options': ['Central Statistics Office', 'Department for Promotion of Industry and Internal Trade', 'Labour Bureau', 'National Technical Manpower Information System'], 'answer': 2, 'explain': 'Handout answer: (c) Labour Bureau. The handout prints only the answer.'},
    {'q': 'With reference to casual workers employed in India, consider: 1. All casual workers are entitled for Employees Provident Fund coverage. 2. All casual workers are entitled for regular working hours and overtime payment. 3. The government can by a notification specify that an establishment or industry shall pay wages only through its bank account. Which are correct? (2021)', 'options': ['1 and 2 only', '2 and 3 only', '1 and 3 only', '1, 2 and 3'], 'answer': 1, 'explain': 'Handout answer: (b). Statements 1 and 2 use “all”, which is the trap. The handout gives only the answer.'},
    {'q': 'With reference to the Indian economy after the 1991 liberalisation, consider: 1. Worker productivity (Rs per worker at 2004-05 prices) increased in urban areas while it decreased in rural areas. 2. The percentage share of rural areas in the workforce steadily increased. 3. In rural areas, the growth in non-farm economy increased. 4. The growth rate in rural employment decreased. Which are correct? (2020)', 'options': ['1 and 2 only', '3 and 4 only', '3 only', '1, 2 and 4 only'], 'answer': 1, 'explain': 'Handout answer: (b) 3 and 4 only. The handout prints only the answer.'},
    {'q': 'Increase in absolute and per capita real GNP do not connote a higher level of economic development, if (2018)', 'options': ['industrial output fails to keep pace with agricultural output', 'agricultural output fails to keep pace with industrial output', 'poverty and unemployment increase', 'imports grow faster than exports'], 'answer': 2, 'explain': 'Handout answer: (c). Growth without falling poverty and unemployment is not development.'},
    {'q': 'With reference to Pradhan Mantri Kaushal Vikas Yojana, consider: 1. It is the flagship scheme of the Ministry of Labour and Employment. 2. It will also impart training in soft skills, entrepreneurship, financial and digital literacy. 3. It aims to align the competencies of the unregulated workforce to the National Skill Qualification Framework. (2018)', 'options': ['1 and 3 only', '2 only', '2 and 3 only', '1, 2 and 3'], 'answer': 2, 'explain': 'Handout answer: (c) 2 and 3 only, so statement 1 is the incorrect one. The handout treats PMKVY as the flagship to cure the skills mismatch, with Recognition of Prior Learning.'},
    {'q': 'Consider the following in respect of ‘National Career Services’: 1. It is an initiative of the Department of Personnel and Training. 2. It has been launched in Mission Mode to improve employment opportunities to uneducated youth. (2017)', 'options': ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 'answer': 3, 'explain': 'Handout answer: (d). The handout prints only the answer.'},
    {'q': 'Disguised unemployment generally means (2013)', 'options': ['large number of people remain unemployed', 'alternative employment is not available', 'marginal productivity of labour is zero', 'productivity of workers is low'], 'answer': 2, 'explain': 'Handout answer: (c). Extra workers add no output, so MPL is zero or negative, yet they are recorded as employed.'},
    {'q': 'Economic growth in country X will necessarily have to occur if (2013)', 'options': ['there is a technical progress in the world economy', 'there is population growth in X', 'there is capital formation in X', 'the volume of trade grows in the world economy'], 'answer': 2, 'explain': 'Handout answer: (c). The handout prints only the answer.'},
    {'q': 'How does the National Rural Livelihood Mission seek to improve livelihood options of the rural poor? 1. Setting up a large number of new manufacturing industries and agri-business centres in rural areas 2. Strengthening Self-Help Groups and providing skill development 3. Supplying seeds, fertilizers, diesel pumpsets and micro-irrigation equipment free of cost to farmers (2012)', 'options': ['1 and 2 only', '2 only', '1 and 3 only', '1, 2 and 3'], 'answer': 1, 'explain': 'Handout answer: (b). Only statement 2 is correct.'},
    {'q': 'Among the following who are eligible to benefit from the Mahatma Gandhi National Rural Employment Guarantee Act? (2011)', 'options': ['Adult members of only the SC and ST households', 'Adult members of below poverty line households', 'Adult members of households of all backward communities', 'Adult members of any household'], 'answer': 3, 'explain': 'Handout answer: (d). The Act guarantees 100 days to rural households demanding unskilled manual work.'},
    {'q': 'A person was in the labour force for 200 days of the year and worked for 120 days of them. Under the usual status approach (principal status) the person is...', 'options': ['employed', 'unemployed', 'not in the labour force', 'underemployed'], 'answer': 0, 'explain': '200 days is at least 183, so the person is in the LF; 120 is more than half of 200, so employed on principal status. This is the handout’s own example.'},
    {'q': 'Which statement about current weekly status (CWS) is correct?', 'options': ['It uses a one-year reference period', 'A person is employed if they worked at least one hour on any one day in the week', 'It generally gives a lower unemployment rate than usual status', 'It was introduced in the PLFS to replace UPSS'], 'answer': 1, 'explain': 'CWS uses 7 days, the priority criterion, and generally reports a higher UR than US. It does not replace UPSS.'},
    {'q': 'Which of these is correct about the natural rate of unemployment (NRU)?', 'options': ['It equals zero at full employment', 'It is the sum of frictional, structural, seasonal and voluntary unemployment', 'It includes cyclical unemployment', 'It can be counted directly by the NSSO'], 'answer': 1, 'explain': 'At the NRU wage-rate and cyclical UE are zero. Full employment is not zero unemployment, and the NRU is estimated, not counted.'},
    {'q': 'Under the Code on Social Security, 2020, a fixed-term employee becomes eligible for gratuity after...', 'options': ['6 months', '1 year', '3 years', '5 years'], 'answer': 1, 'explain': 'The handout’s “crucial Prelims fact”: 1 year for fixed-term versus 5 years for permanent employees.'},
    {'q': 'A security guard at a large IT park is hired through a contractor and gets no PF. In the handout’s classification he is...', 'options': ['formal worker in the organised sector', 'informal worker in the organised sector', 'informal worker in the unorganised sector', 'formal worker in the unorganised sector'], 'answer': 1, 'explain': 'The enterprise is organised but the employment is informal: the informalisation of the formal sector.'},
]

c.mains = [
    ('“India’s unemployment rate is falling, yet the fall is not entirely desirable.” Examine.',
     'The PLFS shows UR down from 6.0% to 3.2% with LFPR up from 49.8% to 60.1%, but the composition of the fall matters.',
     ['Numbers: UR 6.0 to 3.2, LFPR 49.8 to 60.1, WPR 46.8 to 58.2 (2017-18 to 2023-24).', 'Almost the whole fall came from agricultural jobs and self-employment.', 'Agriculture: 46% of workers, 18% of GDP, ₹0.39 per worker; disguised UE and underemployment.', 'Self-employment: more productive but vulnerable, much of it distress employment.', 'Context: Covid pushed workers into agriculture; the last two surveys show agriculture declining again.', 'LFPR is still below Vietnam, China, South Korea and others.'],
     'A low unemployment rate is a good number only if the jobs behind it are productive.'),
    ('Is Indian growth “jobless”? Discuss with reference to employment elasticity.',
     'Elasticity is employment growth divided by output growth, and in India it has fallen.',
     ['ε fell to about 0.01 in 2004-09: almost all growth credited to productivity.', 'But UR has not risen, because employment growth still exceeds labour-force growth.', 'Three phases: sluggish (LF 1.8% vs jobs 1.5-1.6%), lost and found, surge (LF 4.5% vs jobs 5.0%).', 'Falling elasticity is not always bad: skilled workers produce more.', 'Productivity versus employment is a false choice: we need adequate and decent jobs.'],
     '“Jobless” is too harsh a word; “not enough good jobs” is the right one.'),
    ('Why does unemployment persist among educated youth in India? Suggest measures.',
     'The handout’s answer is a mismatch between skills and aspirations, not a lack of growth.',
     ['Voluntary UE: the available job fails the aspiration. Structural UE: the aspired job needs skills the degree did not give.', 'Youth-education paradox: only the non-poor can afford the luxury of unemployment.', 'Evidence: employability about 50-55% (ISR); graduate UR about 13%; age 20-24 graduates 37%.', 'Hidden unemployment as the buffer runs out.', 'Measures: PMKVY with RPL, better wages in lower-skilled jobs, ELI, vocational preference.'],
     'The cure for unemployment is skills, not breaking the machines.'),
    ('Distinguish between organised and unorganised sector and between formal and informal employment. How have the Labour Codes addressed the problem?',
     'One classifies the enterprise, the other classifies the worker.',
     ['Organised versus unorganised: registered, 10+/20+ workers versus unincorporated, under ten workers (NCEUS).', 'Formal versus informal: written contract and social security versus none.', 'Four boxes, including the informal worker in the organised sector (the contractual trap).', 'Root cause: the compliance burden of 40+ central and 100+ state laws; firms hire indirectly.', 'Codes: 29 laws into four; Code on Social Security covers gig and unorganised workers; FTE gives parity and gratuity after 1 year.'],
     'Formalisation will work when complying becomes cheaper than avoiding.'),
    ('Explain the different types of unemployment with Indian examples. Why is disguised unemployment a hallmark of Indian agriculture?',
     'Unemployment is not one thing: each type has a different cause and a different cure.',
     ['Structural, seasonal, frictional, voluntary, wage-rate, cyclical, with one example each.', 'Underemployment: employed but under-used, invisible versus visible.', 'Disguised: MPL zero; the 5 brothers on a 2-acre farm producing 100 quintals.', 'Agriculture holds 46% of workers for 18% of GDP.', 'Shift workers to higher-productivity sectors through skills and manufacturing (PLI, ELI).'],
     'Match the cure to the type: skills for structural, demand for cyclical, jobs outside the farm for disguised.'),
]

c.cards = [
    ('Standard definition of unemployment?', 'Someone able as well as willing to work is unable to find work.'),
    ('Is “not working” the same as “unemployed”?', 'No. Unemployed is a subset of not working: only those in the labour force.'),
    ('Labour force?', 'People working or looking for work (able and willing).'),
    ('Formula for UR?', 'n(UE) ÷ n(LF) = UE ÷ (Emp + UE). A share of the labour force, not of population.'),
    ('WPR?', 'Employed persons ÷ total population, per 1000.'),
    ('Dependency ratio?', '(Population 0-14 + 65+) ÷ population 15-64 × 100.'),
    ('Working age for LFPR and UR in India?', '15 years and above (PLFS). For demographics and DR: 15-64.'),
    ('Is farming for own consumption employment?', 'Yes (inside the SNA production boundary). Domestic chores for own family: no.'),
    ('What is Code 95?', 'NSSO activity code for those not able to work owing to disability. Age is not used.'),
    ('PLFS frequency?', 'Annual survey; households visited monthly. Replaced the 5-yearly EUS.'),
    ('Principal status test?', 'In LF if working or seeking for ≥ 183 days; employed if work for the majority of LF days.'),
    ('Subsidiary status test?', 'At least 30 days of work in the year.'),
    ('Which approach gives the headline UR?', 'UPSS: PS+SS.'),
    ('CWS rule?', 'Reference week; at least 1 hour of work on any day means employed. Priority: working over unemployed over not in LF.'),
    ('Which UR is higher, US or CWS?', 'CWS generally higher.'),
    ('Why was CDS dropped?', 'The PLFS has more frequency, a larger sample and monthly visits.'),
    ('Structural unemployment?', 'Skills or location mismatch between workers and jobs.'),
    ('Frictional unemployment?', 'Search time between jobs under imperfect information; partly healthy.'),
    ('Voluntary unemployment?', 'In the LF, offered a job, refuses it.'),
    ('Underemployment: employed or unemployed?', 'Employed, but under-used (visible: hours; invisible: skills).'),
    ('Disguised unemployment?', 'Extra workers whose marginal product is zero; recorded as employed.'),
    ('Wage-rate unemployment: two classical reasons?', 'Minimum wages above equilibrium; strong unions.'),
    ('Order of the four wages?', 'Floor ≤ minimum ≤ fair ≤ living.'),
    ('Who set up the fair wage concept?', 'The Committee on Fair Wages (1948).'),
    ('NRU formula?', 'Frictional + structural + seasonal + voluntary UE.'),
    ('NAIRU?', 'The UR below which inflation accelerates (wage-price spiral). Linked to the Phillips Curve.'),
    ('PLFS 2023-24: UR, LFPR, WPR?', '3.2%, 60.1%, 58.2%.'),
    ('Female LFPR 2017-18 and 2023-24?', '23.3% and 41.7%.'),
    ('Employment elasticity?', '% change in employment ÷ % change in output. About 0.01 in 2004-09.'),
    ('The handout’s key cause of Indian unemployment?', 'Mismatch of aspirations and skills: voluntary and structural.'),
    ('Organised vs formal?', 'Organised looks at the enterprise; formal looks at the worker’s contract and social security.'),
    ('How many central laws became four Labour Codes?', '29.'),
    ('Gratuity eligibility: permanent versus fixed-term?', '5 years versus 1 year (Code on Social Security, 2020).'),
    ('e-Shram?', 'National database of unorganised workers with a UAN (launched 2021).'),
    ('PM-SYM pension?', '₹3,000 a month after age 60; for workers earning under ₹15,000; government matches contribution.'),
    ('ELI scheme?', 'Budget 2024-25: government pays part of EPFO contributions for first-time formal employees.'),
    ('PLI scheme?', 'Subsidy tied to domestic production targets; drives demand for labour.'),
    ('MGNREGA guarantee?', '100 days of wage employment to rural households demanding unskilled manual work.'),
]

c.summary = 'Who is unemployed, PLFS and the US and CWS approaches, the types of unemployment, India\u2019s PLFS numbers, jobless growth versus the skills mismatch, labour laws, the four Labour Codes, fixed-term employment and the schemes. Ten Prelims PYQs quoted.'
