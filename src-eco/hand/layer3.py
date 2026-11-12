# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 3 (Unemployment). Facts come only from the handout text.
plain = idea in everyday words (memory aid); eg = the handout's own example; hook = one-line handle."""
TOP = {
 'sixty': [('Unemployed', 'able, willing and actively looking: a subset of “not working”'),
           ('Measured by', 'PLFS: Usual Status (one year, 183 days) and Current Weekly Status (7 days)'),
           ('Headline rate', 'UR (PS+SS) = unemployed ÷ labour force; 3.2% in 2023-24'),
           ('Types', 'structural, seasonal, frictional, voluntary, wage-rate, cyclical; disguised and under-employment sit inside “employed”'),
           ('India story', 'UR 6.0% to 3.2% and LFPR 49.8% to 60.1%, but the fall came from agriculture and self-employment'),
           ('Cure', 'skills plus formal, decent jobs: Labour Codes, PMKVY, ELI, PLI, MGNREGA')],
 'words': [('Labour force', 'everyone who is working or looking for work: employed plus unemployed'),
           ('Working age population', 'people in the age group fit for economic activity (15+ for PLFS, 15-64 for demography)'),
           ('LFPR', 'what share of a group is in the labour force'),
           ('Marginal product of labour', 'the extra output the next worker adds'),
           ('Disguised unemployment', 'extra hands on a job who add no output, yet are counted as employed'),
           ('Natural rate (NRU)', 'the unemployment left when wages are at equilibrium and the cycle is neutral'),
           ('Employment elasticity', 'how many per cent jobs grow for each 1% growth in output'),
           ('Informal worker', 'a worker with no written contract and no social security from the employer')],
}
SEC = {
 '1': dict(
   plain='Picture the whole population as a crowd. Take out the children and the elderly dependents and you have the working-age crowd. Inside it, only those who are working or hunting for work form the labour force. A grandparent, a student or a homemaker who is not looking is “not working” but is not unemployed either. The unemployed are only those who are able, willing and have actively searched for work.',
   eg='The handout’s own building blocks: UR = UE ÷ LF and LF = Emp + UE, so it is a share of the labour force, not of the population. Which working age? Demography (dependency ratio, demographic dividend) uses 15-64; PLFS measures (LFPR, UR, WPR) use 15 years and above.',
   hook='UR = UE ÷ (Emp + UE). Demography: 15-64. PLFS: 15+.'),
 '2': dict(
   plain='Employment is anything that adds to national output inside the national-accounts boundary, whether or not a salary arrives. A child helping in a parent’s shop counts; the same child’s mother cooking for her own family does not, because that is not market activity; but a paid cook in someone else’s home does. Pay can come in food, shares, or swapped labour.',
   eg='The handout’s table: running a business for profit Yes; unpaid work in a family shop Yes; farming for own consumption Yes; domestic work for own family No; paid domestic work for others Yes; NGO volunteering No. A 13-year-old at a tea stall is counted as employed in the raw data.',
   hook='Employed = inside the SNA boundary. A salary is not mandatory.'),
 '3': dict(
   plain='There are two ways to ask the same person what they were doing. Usual Status looks back a whole year and asks what you did most of the time. Current Weekly Status looks only at last week and gives priority to working over seeking over staying out. A year smooths the seasons; a week catches shocks, so the weekly rate usually reads higher. In Usual Status the first test is the labour-force test: 183 days or more working or seeking. Then Principal Status asks if you worked the majority of those days, and Subsidiary Status rescues anyone with at least 30 days of work. Merge both and you get UPSS.',
   eg='The handout’s population-1000 example: Not in LF = 200; LF = 800. Principal status: employed 600, unemployed 200. Of those 200, subsidiary status: employed 150, unemployed 50. UR (PS) = 200 ÷ 800 = 25% and UR (PS+SS) = 50 ÷ 800 = 6.25%, the headline rate. Also the four-person table (persons A to D).',
   hook='Test order: LF (≥ 183 days) → PS → SS. UPSS = PS + SS = the headline UR.'),
 '4': dict(
   plain='Each type is a different reason a person is without work or under-used. Structural: the skills do not fit the new jobs. Seasonal: the work itself comes and goes with the calendar. Frictional: the short search time between jobs. Voluntary: the job is on offer but the person says no. Wage-rate: the wage is stuck too high, so more people want work than firms want to hire. Cyclical: the economy is in a slowdown. Underemployment and disguised unemployment are different again: those people are counted as employed, but their work is not fully used or adds nothing.',
   eg='The handout’s farm picture: a 2-acre family farm needs 2 people but has 5 brothers; output stays 100 quintals, so the 3rd, 4th and 5th brothers have MPL zero. 3 hours of work in an 8-hour day is underemployment (the old CDS test). PhD holders applying for peon posts are invisible underemployment.',
   hook='Disguised: MPL = 0 and counted employed. Underemployment is employment, not unemployment.'),
 '5': dict(
   plain='Wage-rate unemployment needs one idea: a wage is a price. Demand slopes down (dearer, fewer wanted); supply slopes up (dearer, more offered). The price settles where the two meet. For labour, firms demand it and workers supply it. If the wage sits above the meeting point and cannot fall, a permanent crowd of workers has no job.',
   eg='The handout: DL ∝ 1 ÷ wages and SL ∝ wages. If wages above equilibrium cannot adjust downwards, there is a permanent excess supply of labour: wage-rate unemployment. Examples: minimum wages fixed above equilibrium by law; strong unions bargaining wages up.',
   hook='DL ∝ 1/w, SL ∝ w. Wage stuck above equilibrium = permanent excess supply = wage-rate unemployment.'),
 '6': dict(
   plain='Four wage yardsticks climb like steps: the floor wage (the nationwide bottom), the minimum wage (survival, set mostly by States), the fair wage (what the industry can afford) and the living wage (what a family needs for dignity, whatever the employer can pay). The second half is about growth. Firms hire when they expect demand, so unemployment rises in a slowdown. Even in good times some unemployment stays: that is the natural rate, the rate at full employment (which is not zero). NAIRU is the line below which pushing unemployment makes inflation speed up.',
   eg='The handout’s sum: LF 100 (80 employed, 20 unemployed, UR 20%). LF rises 10% to 110 and employment rises 5% to 84. Unemployed = 26 and UR = 26 ÷ 110 = 23.6%, higher than 20%, even though jobs rose. Economist A says NRU is 5% so cyclical UE is 3%; Economist B says 7% so 1% (UR is 8%).',
   hook='Floor ≤ Minimum ≤ Fair ≤ Living. NRU = frictional + structural + seasonal + voluntary.',
   mn=[dict(kind='sentence', title='The wage ladder (order matters)', sentence='Floors Mean Fair Living',
            letters=[('F', 'Floor wage (Union baseline, Code on Wages 2019)'), ('M', 'Minimum wage (States, survival)'), ('F', 'Fair wage (what industry can afford)'), ('L', 'Living wage (decent life, ignores affordability)')],
            note='Own memory aid (not from the handout): a floor under the ladder, then fair pay, then a living.')]),
 '7': dict(
   plain='The headline looks great: unemployment falls from 6.0% to 3.2% while more people join the labour force and more people work. But a low UR is only good if the jobs behind it are good. Almost the whole fall came from more agricultural jobs and more self-employment, where productivity is low or workers are vulnerable. Education shows the odd pattern: the more educated, the higher the unemployment.',
   eg='The handout’s productivity table: agriculture 18 (share of GDP) against 46 (share of workers), ₹0.39 per worker; industry 28 and 25, ₹1.12; services 54 and 29, ₹1.86. Graduates: UR 12.9% (2024); at age 20-24 it is 37%.',
   hook='UR 6.0 → 3.2 and LFPR 49.8 → 60.1: a falling UR is not automatically good news.'),
 '8': dict(
   plain='Three suspects. Is growth too low? No: about 6.5% since the 1990s beats the world. Is growth jobless? The employment elasticity fell to about 0.01 in 2004-09, but unemployment did not rise because jobs still grew faster than the labour force. So the handout’s real culprit is a mismatch between what the educated young aspire to and the skills they have. If the job fits your skill but not your aspiration, that is voluntary. If it fits your aspiration but you lack the skill, it is structural and the job stays vacant.',
   eg='The handout’s sum: output grows 10% and employment 6%, so ε = 0.6: 60% of growth from more workers and 40% from higher productivity. Three periods: LF about 1.8% vs jobs about 1.5-1.6%; LF about 1.3% vs jobs about 1.2%; LF about 4.5% vs jobs about 5.0%.',
   hook='ε = % change in employment ÷ % change in output. “Jobless” is too harsh; the mismatch is voluntary plus structural.'),
 '9': dict(
   plain='Two different splits. Organised versus unorganised sorts the enterprise (registered and bigger, or not). Formal versus informal sorts the worker by contract and social security, ignoring firm size. So a contract security guard at a big IT park sits in an organised firm but is an informal worker. Complying with over 40 central and over 100 state laws was costly, so firms hired indirectly. The four Labour Codes merge 29 central laws, and fixed-term employment gives formal-job benefits with informal-job flexibility.',
   eg='The handout’s four boxes: software engineer at Infosys (organised, formal); contract guard at an IT park (organised, informal); farm labourer or street vendor (unorganised, informal); about 80%+ of India’s workforce is informal. Gratuity: 5 years of continuous service for a permanent employee, 1 year for a fixed-term employee.',
   hook='Organised = the firm; formal = the worker. Four Codes replace 29 laws. Gratuity: permanent 5 years, fixed-term 1 year.',
   mn=[dict(kind='sentence', title='The pre-2020 labour laws by year (order matters)', sentence='Tired Plant Inspectors Meet Frightened Employers, Many Complain',
            letters=[('T', 'Trade Unions Act 1926'), ('P', 'Payment of Wages Act 1936'), ('I', 'Industrial Disputes Act 1947'), ('M', 'Minimum Wages Act 1948'),
                     ('F', 'Factories Act 1948'), ('E', 'Employees’ Provident Funds Act 1952'), ('M', 'Maternity Benefit Act 1961'), ('C', 'Contract Labour Act 1970')],
            note='Own memory aid (not from the handout): the sentence is about the “Inspector Raj” compliance burden the handout describes.')]),
 '10': dict(
   plain='Think of each scheme as a patch for one hole. Employers drowning in paperwork: Shram Suvidha. Unorganised workers with no safety net: e-Shram and PM-SYM. Skills that do not match jobs: PMKVY. Too few formal jobs: PLI and ELI. Rural distress and shocks: MGNREGA.',
   eg='PM-SYM: a worker pays e.g. ₹55-200 a month, the government matches it, and the pension is ₹3,000 a month after age 60 (for earners under ₹15,000 a month). e-Shram (2021) gives a Universal Account Number. MGNREGA guarantees 100 days of wage employment.',
   hook='Compliance → Shram Suvidha; vulnerability → e-Shram, PM-SYM; skills → PMKVY; jobs → PLI, ELI; rural shock → MGNREGA (write the full Act name in the exam).'),
}
NUMBERS = [('6.0% → 3.2%', 'UR, 2017-18 to 2023-24'), ('49.8% → 60.1%', 'LFPR (first time above 60%)'), ('46.8% → 58.2%', 'WPR'), ('23.3% → 41.7%', 'female LFPR'),
           ('183 days / 30 days', 'labour-force test / subsidiary-status work test'), ('25% and 6.25%', 'UR (PS) and UR (PS+SS), handout’s 1000-person example'),
           ('0.01', 'employment elasticity in 2004-09 (“jobless growth”)'), ('46 / 18 / ₹0.39', 'agriculture: % of workers / % of GDP / productivity per worker'),
           ('about 13%', 'graduate UR (12.9% in 2024); 37% at age 20-24'), ('80%+', 'informal share of India’s workforce'), ('29 → 4', 'central labour laws merged into Labour Codes'),
           ('5 yr / 1 yr', 'gratuity: permanent / fixed-term employee'), ('100 days', 'MGNREGA guarantee'), ('₹3,000', 'PM-SYM monthly pension after 60'),
           ('1948', 'Minimum Wages Act, Factories Act and Committee on Fair Wages')]
DRAW = ['Redraw the handout’s flow of the Usual Status tests (section 3): labour-force test (≥ 183 days) → PS → SS, then do the four-person table.',
        'Redraw the handout’s flow of how a market reaches equilibrium (section 5) and mark where a wage stuck above equilibrium leaves excess supply of labour.',
        'Write from memory: the wage ladder, the four Labour Codes, and the problem → scheme list (section 10).']
FM = {
 '1': [('Dependency ratio', 'DR = [Pop(0-14) + Pop(65+)] ÷ Pop(15-64) × 100', 'DR uses 15-64'),
       ('Labour force', 'LF = Emp + UE', 'employed plus unemployed'),
       ('Unemployment rate', 'UR = UE ÷ LF = UE ÷ (Emp + UE)', 'a share of the labour force, not of the population'),
       ('LFPR', 'LFPR = labour force of a cohort ÷ total population of the cohort × 100', 'PLFS reports it for age 15+'),
       ('WPR', 'WPR = employed persons ÷ total population', 'handout: expressed per 1000 persons')],
 '3': [('Labour-force test (US)', 'in LF if working or seeking for ≥ 183 days', 'Principal Status'),
       ('Principal status', 'employed if work found for the majority of the LF days', 'LF 200 days, work 120 days → employed'),
       ('Subsidiary status', 'employed if work for ≥ 30 days in the year', 'not even 30 days → unemployed on SS'),
       ('CWS rule', 'working if worked ≥ 1 hour on any 1 day in the 7 days', 'priority: Working beats Unemployed beats Not in LF'),
       ('UR (PS)', '200 ÷ 800 = 25%', 'handout, population-1000 example'),
       ('UR (PS+SS)', '50 ÷ 800 = 6.25%', 'the headline rate')],
 '4': [('Marginal product', 'MPL of the (n+1)th worker = output(n+1) − output(n)', 'n workers make x, n+1 make x + y → marginal output y; disguised UE: y = 0')],
 '5': [('Demand for labour', 'DL ∝ 1 ÷ wages', 'high wages, fewer workers wanted'),
       ('Supply of labour', 'SL ∝ wages', 'high wages, more people willing to work'),
       ('Law of demand', 'QD varies inversely with price', 'ceteris paribus'),
       ('Law of supply', 'QS varies directly with price', 'ceteris paribus')],
 '6': [('Wage ladder', 'Floor ≤ Minimum ≤ Fair ≤ Living wage', ''),
       ('Natural rate', 'NRU = frictional + structural + seasonal + voluntary UE', 'wage-rate and cyclical UE are both zero at NRU; full employment is not zero unemployment'),
       ('Cyclical UE', 'cyclical UE = actual UR − NRU', 'UR 8%: NRU 5% → 3%; NRU 7% → 1% (handout)'),
       ('UR falls only if', 'employment growth &gt; labour-force growth', 'LF +10%, jobs +5%: UR 20% → 23.6%')],
 '7': [('Relative productivity', 'GDP share ÷ employment share', 'agriculture 18 ÷ 46 → ₹0.39 per worker (handout)')],
 '8': [('Employment elasticity', 'ε = % change in employment ÷ % change in output', 'output +10%, jobs +6% → ε = 0.6'),
       ('Rule', 'UR falls only if employment growth &gt; labour-force growth', 'sluggish decade: LF 1.8% vs jobs 1.5-1.6% → rising UE')],
 '9': [('Formal worker test', 'written contract + paid leave + social security from the employer', 'above all PF, ESIC, pension, maternity'),
       ('Organised (private firm)', '10+ workers (with power) or 20+ (without)', 'unorganised: unincorporated, under ten workers'),
       ('Gratuity', 'permanent: 5 years; fixed-term: 1 year', 'Code on Social Security, 2020'),
       ('Labour Codes', '29 central laws → 4 Codes', '2019-2020')],
 '10': [('PM-SYM', 'worker pays ₹55-200 a month + government matches → pension ₹3,000 a month after 60', 'for earners under ₹15,000 a month'),
        ('MGNREGA', '100 days of wage employment per rural household demanding unskilled manual work', 'shock absorber and floor for rural wages')],
}
