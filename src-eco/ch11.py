from lib import Ch

c = Ch(11, 'Goods and Services Tax (GST)',
       'Economy · GS Foundation · Chapter 11',
       [('hb', 'Handout only: no class slides'), ('', 'Handout pages 1-13'), ('', 'No PYQs quoted')],
       'Taxes as events, the old indirect-tax system and cascading (tax on tax), VAT and Input Tax Credit, why GST completes the job, the GST definition and its three properties, CGST, SGST and IGST, the GST Council, what stays outside GST, benefits and challenges, state compensation, revenue neutral rate, anti-profiteering, the Constitution (101st Amendment) Act, registration, composition, e-way bill and GSTN.')

c.sec('Exam lens: priority and PYQs', 'exam-lens-priority-and-pyqs')
c.call('alert', 'Source note', ['**Handout only.** No class slides and no teacher ink. The handout carries the teacher’s **handwritten worked examples** (the shirt example in pink); those are part of the handout, not a forecast. **No Prelims or Mains PYQ is quoted** in this handout: none quoted in the material. Priority below is the handout’s own emphasis.'])
c.table('What the handout stresses', ['Signal in the handout', 'Where', 'Why it matters'], [
    ['**Cascading** = tax on tax and tax on value already taxed. Of ₹32 tax, only **₹5.8** was on fresh value', 'Section 2', 'Core concept; the shirt example'],
    ['**ITC** works only **tax against the same tax**. Tax is always charged on the entire value; ITC makes it effectively a tax on value added', 'Section 3', 'Two “very important points” in the handout'],
    ['GST = tax on supply of goods and services **other than alcohol for human consumption;** **one nation-one tax, destination-based, VAT-like**', 'Section 4', 'Statutory definition'],
    ['**CGST, SGST, IGST;** SGST goes to the destination state; customs is not part of GST', 'Section 4', 'Statement traps'],
    ['**GST Council (Art. 279A):** chair Union FM; quorum 50%; decision by **75%**; States **2/3** weight, Centre **1/3**', 'Section 5', 'Numbers'],
    ['**101st Amendment Act, 2016 (08.09.2016);** Art. **246A, 269A, 279A;** 5 petroleum products outside GST for now', 'Sections 5-6', 'Provisions'],
    ['**Compensation:** base on pre-2017 revenue, **14%** assumed growth, **5 years (till 2022);** only for shortfall caused by GST', 'Section 7', 'Number and condition'],
    ['**Revenue neutral rate;** **anti-profiteering;** **exports zero-rated**', 'Section 7', 'Concept questions'],
    ['**Registration ₹20 lakh** (₹10 lakh special category), **composition,** **GSTN** (2013, Section 25 company, Infosys), **e-way bill 01.04.2018**', 'Section 8', 'Numbers and dates; conflicts flagged'],
])
c.call('key', 'What to prepare', [
    '**Prelims hooks:** the three properties of GST; GST on what (not alcohol for human consumption); CGST, SGST, IGST; ITC rule; what is outside GST; GST Council composition and voting; Articles 246A, 269A, 279A; 101st Amendment; compensation (14%, 5 years); zero-rated versus exempt; RNR; anti-profiteering; GSTN; composition and registration limits.',
    '**Mains hooks:** how GST ends cascading and why compliance rose; GST and cooperative federalism (pooled sovereignty versus loss of State autonomy); challenges (multiple slabs, lobbying, petroleum outside); why compensation became a conflict; why a single flat rate would be regressive.',
    '**Closing idea:** GST is the 2005 VAT idea taken to its end: one event, one tax chain, one credit system.'])

c.sec('1 · The old system: taxes are levied on events')
c.ul(['**Taxes are levied on events:** sale of a good or service, generation of income, change of international boundary (customs), profit of a company. The person on whom tax is levied deposits it with the government.',
      '**Indirect tax:** the tax is levied on A and A pays the government, but A **collects it from B,** who bears the burden. Centre, States and local bodies all levied such taxes.',
      '**Old regime flow:** every producer pays **excise duty** to the Centre on production. On every sale the State levies **sales tax** (later VAT). Wholesaler and retailer add margins; sales tax applies at every sale. The consumer bears it all.',
      '**Central Sales Tax (CST):** a State cannot tax an inter-State sale because that would distort free movement of goods (**Art. 301-307**). The Centre levies CST and **transfers the entire amount to the selling State.**'])
c.fig('eco-gst-old-flow.jpg', 'Handout page 2 (teacher’s drawing): the old regime. Cloth and thread producers pay excise duty to the Centre and sales tax to the State; the shirt producer pays excise (C) and sales tax (S) at each stage; the note says sales tax is levied on the value of sales and excise duty on the value of production (or at a fixed rate, i.e. a specific duty).')

c.sec('2 · The problem: cascading of taxes')
c.p('The shirt example: value added at each stage is **₹366** (cloth 100, thread 100, shirt producer 58, wholesaler 48, retailer 60). The consumer pays **₹550,** so the effective tax is **₹184 on ₹550 = 33.5%.** The handout’s conclusion: with that burden nobody would ask for a bill. The problem is **compounding: double taxation of the same value and a tax on tax.** This is **cascading.**')
c.fig('eco-gst-old-numbers.jpg', 'Handout page 3 (teacher’s drawing): the shirt example with numbers. Cloth and thread ₹100 each with excise ₹10 and sales tax ₹11; shirt producer value added ₹58 and excise ₹20; wholesaler margin ₹48; retailer margin ₹60; final price paid ₹550.')
c.p('Take the sale from producer to wholesaler: sales value **₹320,** sales tax at **10% = ₹32,** so the wholesaler pays **₹352.** The ₹32 breaks down as:')
c.table('Where the ₹32 comes from', ['Part', 'Amount', 'What it is'], [
    ['Tax on the value added by the shirt producer', '**₹5.8**', 'Fresh value: the only legitimate part'],
    ['Tax on the producer’s own excise duty (₹20)', '₹2', 'Tax on tax'],
    ['Tax on value added by cloth producer and by thread producer (₹10 each)', '₹20 (10 + 10)', 'Tax on value already taxed'],
    ['Tax on the excise paid by cloth and thread producers (₹1 each)', '₹2', 'Tax on tax'],
    ['Tax on the sales tax between cloth/thread and the shirt producer (₹1.1 each)', '₹2.2', 'Tax on tax'],
], rowhead=True)
c.call('key', 'The punchline', ['Out of ₹32 levied at this stage, only **₹5.8** was on value not yet taxed. The remaining **₹26.2** was tax on tax or tax on value already taxed.'])
c.call('alert', 'Handout alert', ['In the handout’s algebra line, “121 (cost paid to cloth producer)” is written twice; the second should be the thread producer. The totals are unaffected. **Exam-hall rule:** learn the five-part split above, not the algebra.'])

c.sec('3 · The correction: VAT (2005) and Input Tax Credit')
c.ul(['**From 2005, State sales tax is levied on value added,** not the whole transaction; this was itself called **VAT.** For Central excise, the VATting system was already used in the **1980s** and was called **CENVAT / MODVAT.**',
      '**Aim:** reduce the burden by making taxation fair and so raise **compliance.** In the example, the producer-to-wholesaler tax falls to a tax on ₹58 only (₹5.8).',
      '**Input Tax Credit (ITC):** the tax already paid on inputs (the previous stage) with proof, the bill, is **offset** against the tax payable on the output. The producer had paid ₹11 each on cloth and thread, so **₹22** of ITC sits in his account.'])
c.call('key', 'Two very important points (handout)', [
    '**1. Tax is always charged on the entire value of the transaction.** The government cannot see your value added. Taxing value added is the **objective;** ITC is how it is **achieved.** The seller’s bill shows only inputs plus value added, so the customer is charged accordingly.',
    '**2. ITC and offsetting work only for a tax against the same tax.** VAT against VAT, not against excise (a Central tax) or State taxes such as entertainment, luxury and octroi.'])
c.fig('eco-gst-bills.jpg', 'Handout page 5 (teacher’s drawing): bills of transaction between producer and wholesaler. Old regime (pre-2005): value of sale 320, sales tax @10% 32, total paid 352. New regime (2005-2017): value of input 110 + 110 = 220, tax already paid 22, value added 58, excise paid 20, value of sale 220 + 58 + 20 = 298, sales tax 29.8, total paid 327.8; tax paid by the producer = 29.8 − 22 = 7.8 = 5.8 + 2.')
c.table('Old regime versus VAT: producer to wholesaler', ['', 'Old regime (pre-2005)', 'VAT (2005-2017)'], [
    ['**Tax base**', '₹320 (everything)', '₹298 (input 220 + value added 58 + excise 20)'],
    ['**Tax**', '₹32', '₹29.8, less ITC ₹22 = **₹7.8 payable**'],
    ['**Total paid by wholesaler**', '₹352', '₹327.8'],
    ['**What is left of cascading**', 'All of it', 'The **₹2 tax on excise** (VAT is still levied on excise duty)'],
], rowhead=True)
c.ul(['**Benefit of VAT:** the tax burden falls because the taxable value is far smaller.',
      '**Shortcoming:** cascading is **not eliminated,** because VAT is still levied on excise. **GST removes it completely** by removing every other event of taxation except sale, so that all taxes can be offset against each other.'])

c.sec('4 · What GST is')
c.p('**GST is the wider application of the VAT system.** It removes all other events of indirect tax **(except Customs)** and combines them into one event: **the sale of a good or a service.** There is no excise, CST or entry tax/octroi any more. A produces and sells to B: only GST. B sells to C and charges tax on the value added.')
c.fig('eco-gst-flow.jpg', 'Handout page 6 (teacher’s drawing): the GST chain. Cloth and thread producers, shirt producer, wholesaler and retailer each charge GST (Centre + State); the consumer pays at the end. Small note: “Let GST be @ 20%”.')
c.table('The same shirt under GST at an assumed 20%', ['Stage', 'Value added', 'GST on the sale', 'Net tax paid after ITC'], [
    ['**Cloth and thread producers**', '₹100 each', '₹20 each (on ₹100)', '₹20 − 0 = **₹20** each (20% of 100)'],
    ['**Shirt producer**', '₹58', '₹51.6 (on 258)', '51.6 − 40 = **₹11.6** (20% of 58)'],
    ['**Wholesaler**', '₹48', '₹61.2 (on 306)', '61.2 − 51.6 = **₹9.6** (20% of 48)'],
    ['**Retailer**', '₹60', '₹73.2 (on 366)', '73.2 − 61.2 = **₹12** (20% of 60)'],
    ['**Consumer pays**', '₹366 in total', '**₹73.2** = 20% of 366', '**Final price ₹439.2** (against ₹550 earlier)'],
], rowhead=True)
c.fig('eco-gst-net-tax.jpg', 'Handout page 7 (teacher’s drawing): “Net tax paid” at each stage, ending with the customer paying 73.2 = 20% of the entire value added (100 + 100 + 58 + 48 + 60).')
c.call('alert', 'Handout alert', ['A tiny bracket note at the bottom of the numbers diagram (page 6) is handwritten and hard to read; it appears to compare ₹439.2 with ₹550 under the earlier tax regime. **Check your notebook.** The 20% is the teacher’s assumed rate for the example, **not** an actual GST slab (the handout’s slabs are 0, 5, 12, 18 and 28).'])
c.fig('eco-gst-structure.jpg', 'Handout page 12: the pre-GST structure (Central taxes with their administrations, Acts and procedures; multiple State taxes, administrations, Acts and procedures; Customs, Excise, Electricity duty, Entertainment tax, Luxury tax, VAT, Entry tax and Octroi layered above State levies) giving way to GST: a single tax, single administration, uniform law and computerised uniform procedures, split into CGST, SGST/UTGST and IGST.')
c.h3('Statutory definition and three properties')
c.p('GST is **any tax on supply of goods and services other than on alcohol for human consumption.**')
c.table('Three properties', ['Property', 'Meaning'], [
    ['**One nation-one tax**', 'Subsumes many indirect taxes: **VAT, CST, Excise, Service tax,** etc.'],
    ['**Destination-based**', 'The taxing authority is the place where goods are **supplied to,** not where the sale originates'],
    ['**VAT-like structure**', 'Taxes paid at previous stages are available as **set-off** at the next stage'],
], rowhead=True)
c.table('CGST, SGST and IGST', ['Tax', 'When', 'Who gets the revenue'], [
    ['**CGST + SGST**', 'Sale **within a State** (the consumer sees two components)', 'CGST: the Centre. SGST: the **destination** State'],
    ['**IGST (Integrated GST)**', 'Sale **across two States**', 'Levied by the Centre on inter-State supplies and imports (Art. 269A)'],
], rowhead=True)
c.ul(['The goods and services to be taxed and the other essential design features must be **common** between the Centre and the States.',
      '**International trade:** GST is destination-based, so **exports are zero-rated.** **Zero-rated does not mean exempt:** exporters are eligible for **full duty drawback.** **Customs duty is not part of GST.** **Imports** are taxed like domestic goods: **basic customs duty** on entry, then **IGST.**'])

c.sec('5 · GST Council and the Constitution')
c.ul(['**Constitution (101st Amendment) Act, 2016,** notified on **08.09.2016.**',
      '**Art. 246A:** concurrent jurisdiction for levy and collection of GST by the Centre and the States.',
      '**Art. 269A:** the Centre levies and collects **IGST** on inter-State supplies, including imports.',
      '**Compensation** to States for loss of revenue for **five years** on the recommendation of the GST Council (the handout cites “Clause 19”).',
      '**Petroleum:** crude, high speed diesel, motor spirit (petrol), natural gas and aviation turbine fuel to be brought under GST **from a later date** on the Council’s recommendation.'])
c.table('GST Council (Article 279A)', ['Feature', 'Provision'], [
    ['**Chairperson**', 'Union Finance Minister'],
    ['**Vice Chairperson**', 'Chosen from the Ministers of State Governments'],
    ['**Members**', 'Minister of State (Finance) and all Finance/Taxation Ministers of each State'],
    ['**Quorum**', '**50%** of total members'],
    ['**Decision**', '**75% majority**'],
    ['**Weightage**', '**States 2/3, Centre 1/3**'],
    ['**Role**', 'Apex policy-making body: recommends on model GST laws, rates, place of supply rules and everything related to GST'],
], rowhead=True)
c.call('note', 'Federalism argument', ['Some commentators say GST made States **surrender financial sovereignty** (visible during Covid when States could not raise indirect tax rates). The handout rejects this: the Centre and States have **“pooled their sovereign rights”** through the Council to streamline taxation. Use both sides in Mains.'])

c.sec('6 · Outside GST, and what GST changed in administration')
c.fig('eco-gst-outside.jpg', 'Handout page 11: “Outside GST!” Alcohol for human consumption: power to tax remains with the State. Five petroleum products (crude oil, diesel, petrol, natural gas, ATF): GST Council to decide the date from which GST will be applicable. Tobacco: part of GST but the Central Government has power to levy additional excise duty. Entertainment tax levied by local bodies: power to tax remains with local bodies.')
c.ul(['**As of March 2022 (handout):** petroleum and petroleum products are **not** subject to GST; they stay under the earlier system. **VAT and other input taxes paid on them cannot be offset against GST.**',
      '**12 nautical miles:** the area up to 12 nautical miles is under **Central administration,** but States can collect tax on economic activities carried out there.',
      '**Stamp duties** on legal agreements continue to be levied separately by States.'])
c.call('note', 'Reading tip', ['The handout’s text says GST excludes “alcohol for human consumption”, and the infographic adds that **tobacco is inside GST** with an extra Central excise power. **Exam-hall rule:** alcohol, five petroleum products and local entertainment tax are outside GST; tobacco is inside.'])

c.sec('7 · Benefits, challenges, compensation, RNR and anti-profiteering')
c.h3('Benefits')
c.ul(['**Simple to administer and efficient.** A wider and growing tax base (registered users) shows higher compliance. In the old system the honest taxpayer paid his own share and the evader’s.',
      '**ITC across Centre and State taxes** is called the biggest reform: earlier Central and State taxes were isolated and administered separately, so there was no offsetting. Harmonised administration cuts duplication and red tape; automated GSTN reduces errors and eases filing.',
      '**Compliance logic:** a good tax law has **low cost of compliance and high cost of non-compliance.** Earlier, multiple events and authorities made compliance costly, and catching an evader depended on a tax officer, so the penalty was usually a bribe. Under GST the **system** catches the evader and the cost reaches the legal penalty.'])
c.fig('eco-gst-benefits.jpg', 'Handout page 13: Benefits of GST (12 items in two groups). Group one: reduction in cascading of taxes and overall price reduction (decrease in inflation); common national market and benefits to small taxpayers (ease of doing business); self-regulating and non-intrusive electronic tax system (decrease in “black” transactions). Group two: simplified tax regime and reduction in multiplicity of taxes (more informed consumer); consumption-based tax and abolition of CST (poorer States to gain); exports zero-rated and protection of domestic industry through IGST (Make in India).')
c.h3('Challenges')
c.ul(['**Multiple slabs:** **0%, 5%, 12%, 18% and 28%** (handout, 2022); raw agricultural produce is **zero-rated;** luxury goods and goods with negative externalities attract a **cess** above 28%. This is the most important challenge.',
      'Filings fell drastically (e.g. **GSTR-3B**) but are still more than the “zero” that businesses practically filed earlier.',
      '**Lobbying and politicisation:** producers (especially food processing) seek zero rating; the Centre, with its majority in the Council, is accused of cutting rates with an eye on elections.',
      '**One flat rate** may be ideal, but it would be **regressive.** The multiple rates add a **progressive** element: 0 or 5% for necessities, 18% and 28% plus cess for luxury and demerit goods. A reform of slabs is still desirable.'])
c.h3('Compensation to States')
c.ul(['States demanded compensation before pooling their rights. Each State’s **pre-2017 indirect tax revenue** was taken and an **average nominal growth of 14% a year for five years** (till **2022**) was assumed.',
      'If actual revenue under GST falls short of this path, the **Centre compensates the shortfall.** The handout stresses: only for a shortfall **on account of GST implementation.** Not for the State’s own failure or a pandemic.',
      'The **GST compensation cess** on luxury and demerit goods funds this. It was meant to end in 2022; the handout says it is not yet going away “thanks to Covid”.'])
c.h3('Revenue Neutral Rate (RNR)')
c.p('**RNR** is the average GST rate at which the government receives **the same revenue** despite the change in tax law, input credits and exemptions. Pre-GST incidence in most States was about **30%** (12% excise, 14% VAT and others). Example: at 30% effective rate, ₹10 of tax means only **₹33** of the ₹100 of output was taxed (one-third of GDP). If GST taxes **double** the value (two-thirds of GDP), a **15%** rate still gives ₹10. That 15% is the RNR.')
c.h3('Anti-profiteering')
c.p('With a lower RNR, goods should be cheaper. But the seller may keep the **tax reduction as extra profit** instead of passing it on. That is **profiteering,** and GST law makes it **illegal.** Institutions: **National Anti-Profiteering Authority,** a **Standing Committee** and **State-level Screening Committees** (all “already set up” per the handout).')

c.sec('8 · Features of the Act: registration, composition, e-way bill and GSTN')
c.table('Main features', ['Feature', 'Provision (handout)'], [
    ['**Jurisdiction**', 'Concurrent: Centre levies **CGST,** States levy **SGST;** Centre levies **IGST** on inter-State supplies and imports'],
    ['**Mode**', 'All transactions and processes **electronic:** non-intrusive administration'],
    ['**Registration**', '**PAN-based;** only if turnover is **above ₹20 lakh** (**₹10 lakh** for special category States except J&K); **voluntary registration** allowed'],
    ['**Deemed registration**', 'In **three working days**'],
    ['**Input Tax Credit**', 'On taxes paid on all procurements, except a few specified items'],
    ['**E-way bill**', 'For all inter-State movement of goods from **01.04.2018;** by **16.06.2018** all States and UTs had introduced it for intra-State movement'],
], rowhead=True)
c.h3('Composition levy')
c.ul(['An **alternative, optional** levy for small taxpayers to bring simplicity and cut compliance cost: tax at a **prescribed percentage of turnover** every quarter instead of the normal rate.',
      '**Not available** to inter-State suppliers, service providers (**except restaurant service**) and specified manufacturers.',
      '**Quarterly return in Form GSTR-4** on the GSTN portal by the **18th of the month** after the quarter (July-September 2017 return due **18 October 2017**).'])
c.call('alert', 'Handout alert', ['**Composition threshold conflict:** the “Main Features” list says **₹100 lakh;** the composition-levy paragraph says turnover up to **₹75 lakh (₹50 lakh in a few States).** The handout does not reconcile them. **Exam-hall rule:** if the options carry both, pick the one matching the wording (₹75 lakh with the composition levy paragraph); if only one is present, use it.'])
c.h3('Goods and Services Tax Network (GSTN)')
c.ul(['Incorporated in **March 2013** as a **Section 25** private limited company with paid-up capital of **₹10 crore.**',
      '**Equity holders:** earlier Centre, States **and private sector;** **now completely government owned.**',
      'A **common pass-through portal** for taxpayers to submit registration applications, file returns and pay tax. **Infosys** is the Managed Service Provider (MSP); **73 GST Suvidha Providers (GSPs)** appointed.'])

c.mm = ('GST', [
    ('Old system', [('Events taxed: excise, sales tax, CST, entry', None), ('Cascading: tax on tax', None), ('₹32: only ₹5.8 fresh', None), ('₹550 price, 33.5% effective tax', None)]),
    ('VAT and ITC', [('VAT 2005; CENVAT/MODVAT 1980s', None), ('ITC: same tax only', None), ('Tax on whole value; effective on value added', None), ('Left ₹2 tax on excise', None)]),
    ('GST', [('Tax on supply except alcohol for human consumption', None), ('One nation-one tax', None), ('Destination-based', None), ('VAT-like set-off', None)]),
    ('Taxes', [('CGST + SGST within State', None), ('IGST inter-State and imports', None), ('Exports zero-rated; full drawback', None), ('Customs outside GST', None)]),
    ('Council and law', [('101st Amendment 2016', None), ('Art. 246A, 269A, 279A', None), ('Quorum 50%, decision 75%', None), ('States 2/3, Centre 1/3', None)]),
    ('Outside GST', [('Alcohol for human consumption', None), ('Five petroleum products', None), ('Local entertainment tax', None), ('Tobacco inside + extra excise', None)]),
    ('Challenges', [('Slabs 0/5/12/18/28 + cess', None), ('Lobbying, politicisation', None), ('Compensation: 14% for 5 years', None), ('Flat rate would be regressive', None)]),
    ('Administration', [('Registration ₹20 lakh', None), ('Composition, GSTR-4', None), ('E-way bill 01.04.2018', None), ('GSTN: 2013, Section 25, Infosys', None)]),
])

c.timeline = [
    ('1980s', 'VATting of excise duty: CENVAT/MODVAT (Central).', False),
    ('2005', 'State sales tax becomes VAT (tax on value added).', True),
    ('March 2013', 'GSTN incorporated as a Section 25 company, ₹10 crore capital.', False),
    ('08.09.2016', 'Constitution (101st Amendment) Act, 2016 notified.', True),
    ('01.07.2017', 'GST comes into effect.', True),
    ('01.04.2018', 'E-way bill for all inter-State movement of goods.', False),
    ('16.06.2018', 'All States and UTs have e-way bill for intra-State movement.', False),
    ('2022', 'Five-year State compensation period ends (14% assumed growth). Compensation cess still continuing per the handout.', True),
]

c.connects = [
    ('[Chapter 12: Budget and Fiscal Policy](eco-ch12.html)', 'GST revenue, indirect versus direct tax shares and fiscal federalism feed the Budget.'),
    ('[Chapter 6: Inflation](eco-ch06.html)', 'Cascading and price effects: GST’s promise of lower prices is an inflation argument.'),
    ('[Chapter 10: External Sector](eco-ch10.html)', 'Zero-rating of exports, IGST on imports and Make in India.'),
    ('[Chapter 5: National Income Accounting](eco-ch05.html)', 'Revenue neutral rate depends on how much of GDP is taxed (tax base).'),
    ('[Chapter 2: Inequality](eco-ch02.html)', 'Progressive versus regressive elements of the multi-slab GST.'),
]

c.recall = [
    'Cascading: tax on tax and tax on already-taxed value. Shirt example: ₹550 price, 33.5% effective tax; ₹32 of which only ₹5.8 fresh.',
    'VAT 2005 (State), CENVAT/MODVAT 1980s (Centre). VAT still taxed excise: ₹2 cascading left.',
    'ITC: same tax only. Tax is charged on whole value; ITC makes it effectively on value added.',
    'GST: tax on supply except alcohol for human consumption. One nation-one tax, destination-based, VAT-like.',
    'CGST + SGST within a State; IGST inter-State and imports. SGST to destination State. Customs outside GST.',
    'Exports zero-rated (not exempt); full drawback. Imports: BCD then IGST.',
    '101st Amendment 2016 (08.09.2016). Art. 246A (concurrent), 269A (IGST), 279A (Council).',
    'Council: FM chair; quorum 50%; decision 75%; States 2/3, Centre 1/3.',
    'Outside GST: alcohol for human consumption, five petroleum products, local entertainment tax. Tobacco inside + extra excise.',
    'Slabs 0/5/12/18/28 + cess. Compensation: 14% growth for 5 years (till 2022), only for GST-caused shortfall.',
    'RNR: rate that keeps revenue same. Anti-profiteering: pass the benefit on.',
    'Registration ₹20 lakh (₹10 lakh special category). Composition ₹75 lakh vs ₹100 lakh (conflict). GSTN 2013, Section 25, Infosys, 73 GSPs. E-way bill 01.04.2018.',
]

c.mcq = [
    {'q': 'Which of the following correctly describes GST?', 'options': ['A tax on income of companies', 'A tax on supply of goods and services other than alcohol for human consumption', 'A tax on all goods including alcohol', 'A tax on imports only'], 'answer': 1, 'explain': 'The handout’s statutory definition excludes alcohol for human consumption.'},
    {'q': 'GST is a destination-based tax. This means…', 'options': ['revenue goes to the State where goods are made', 'the taxing authority is where goods are supplied to', 'only imports are taxed', 'tax is levied only at the final stage'], 'answer': 1, 'explain': 'The authority is the place of supply, not the place where the sale originates.'},
    {'q': 'In an inter-State sale, the tax levied is…', 'options': ['CGST and SGST', 'IGST', 'CST', 'VAT'], 'answer': 1, 'explain': 'IGST is levied by the Centre on inter-State supplies and imports (Art. 269A). CST was abolished.'},
    {'q': 'Input Tax Credit under VAT can be offset…', 'options': ['against any tax of the Centre', 'against any State tax', 'only against the same tax', 'against excise duty'], 'answer': 2, 'explain': 'ITC is available only for a tax against the same tax.'},
    {'q': 'Which tax is NOT part of GST in the handout?', 'options': ['Customs duty', 'Service tax', 'Central Sales Tax', 'Excise duty'], 'answer': 0, 'explain': 'GST subsumes VAT, CST, excise and service tax. Customs is the exception.'},
    {'q': 'Which of these is outside GST (power to tax remains with the State)?', 'options': ['Tobacco', 'Alcohol for human consumption', 'Services', 'Electricity transmission'], 'answer': 1, 'explain': 'Tobacco is inside GST with an extra Central excise power.'},
    {'q': 'Under the GST Council voting rules, decisions need…', 'options': ['simple majority', '2/3 majority', '75% majority', 'unanimity'], 'answer': 2, 'explain': 'Quorum is 50%; decision by 75%; States hold 2/3 weightage, Centre 1/3.'},
    {'q': 'Concurrent power of the Centre and States to levy GST comes from…', 'options': ['Article 246A', 'Article 269A', 'Article 279A', 'Article 301'], 'answer': 0, 'explain': '246A: concurrent jurisdiction; 269A: IGST; 279A: Council.'},
    {'q': 'Exports under GST are zero-rated. This means…', 'options': ['they are exempt and lose ITC', 'no tax and eligible for full duty drawback', 'taxed at 5%', 'taxed only by the State'], 'answer': 1, 'explain': 'Zero-rated does not mean exempt.'},
    {'q': 'The compensation promised to States assumed an average nominal growth of…', 'options': ['10%', '12%', '14%', '18%'], 'answer': 2, 'explain': 'On pre-2017 indirect tax revenue, for five years (till 2022).'},
    {'q': 'Compensation to States covers…', 'options': ['any revenue shortfall', 'shortfall due to a pandemic', 'shortfall on account of GST implementation', 'only petroleum losses'], 'answer': 2, 'explain': 'The handout stresses the shortfall must be due to GST implementation.'},
    {'q': 'The Revenue Neutral Rate is…', 'options': ['the highest GST slab', 'the average rate that keeps government revenue unchanged', 'the cess rate', 'the composition rate'], 'answer': 1, 'explain': 'At RNR revenue stays the same despite input credits and exemptions.'},
    {'q': 'The effective tax in the old-regime shirt example was about…', 'options': ['10%', '20%', '33.5%', '50%'], 'answer': 2, 'explain': '₹184 on ₹550.'},
    {'q': 'VAT did not completely remove cascading because…', 'options': ['VAT was levied on excise duty as well', 'ITC was not allowed', 'CST was abolished', 'there was no bill'], 'answer': 0, 'explain': 'That left the ₹2 tax on excise; GST removes it by merging the events.'},
    {'q': 'GSTN, the common GST portal, is…', 'options': ['an RBI department', 'a Section 25 company, now fully government owned', 'a private bank', 'a SEBI unit'], 'answer': 1, 'explain': 'Incorporated in March 2013 with ₹10 crore; earlier had private shareholders.'},
]
for q in c.mcq:
    q.pop('explanation', None)

c.mains = [
    ('Explain how GST addresses the problem of cascading taxes seen in the earlier indirect tax system.',
     'Under the old system the same value was taxed repeatedly: a tax on tax.',
     ['Old regime: excise, sales tax and CST at each stage; ₹550 price, 33.5% effective tax; ₹26.2 of ₹32 was tax on tax or on taxed value.', 'VAT 2005 and CENVAT taxed value added through ITC, but VAT still taxed excise.', 'GST merges all events into the sale; ITC across Central and State taxes; same example gives ₹439.2.', 'Exports zero-rated, anti-profiteering to pass on gains.'],
     'GST finished what the 2005 VAT began.'),
    ('Discuss the structure and role of the GST Council in the context of cooperative federalism.',
     'The Council is the apex body where the Centre and the States jointly decide GST.',
     ['Art. 279A: FM chair, State ministers as members, quorum 50%, decisions by 75%, States 2/3 and Centre 1/3.', 'Recommends on laws, rates, place of supply and compensation.', 'Argument that States surrendered sovereignty versus the handout’s “pooled sovereignty”.', 'Concerns: Centre accused of influencing rate cuts; Covid-time compensation tension.'],
     'A shared taxing power works only if the two sides keep trusting the Council.'),
    ('What are the challenges in the GST system? Is a single rate desirable?',
     'GST has simplified taxation but problems remain.',
     ['Multiple slabs 0/5/12/18/28 plus cess.', 'Lobbying and politicisation; classification disputes.', 'Petroleum outside GST; compensation cess continuing.', 'Single rate would be regressive; multiple slabs give a progressive element.'],
     'Fewer slabs are desirable; one slab is not.'),
    ('Explain the GST compensation mechanism and the concept of Revenue Neutral Rate.',
     'States agreed to pool powers on the promise of protection against loss.',
     ['Pre-2017 revenue base with 14% assumed growth for five years (till 2022).', 'Only for shortfall due to GST implementation; funded by the compensation cess on luxury and demerit goods.', 'RNR: average rate that leaves revenue unchanged; 30% on a third of GDP versus 15% on two-thirds.', 'Tax base widening is the reason a lower rate can work.'],
     'RNR is a promise that a broader base can replace a higher rate.'),
    ('Discuss how GST treats international trade and what lies outside its scope.',
     'GST is destination-based, so it follows the consumption of goods and services.',
     ['Exports zero-rated with full duty drawback; imports: BCD then IGST; customs outside GST.', 'Outside GST: alcohol for human consumption, five petroleum products pending Council decision, local entertainment tax; tobacco inside with extra excise.', 'IGST protects domestic industry (Make in India).', 'Stamp duties and the 12 nautical miles administration.'],
     'Where the tax falls is decided by where the goods are consumed.'),
]

c.cards = [
    ('Taxes are levied on?', 'Events: sale, income, border crossing, profit.'),
    ('Indirect tax?', 'Levied on A, collected from B who bears the burden.'),
    ('Why CST existed?', 'States cannot tax inter-State sales (Art. 301-307); Centre levied CST and gave it to the selling State.'),
    ('Cascading?', 'Tax on tax and tax on value already taxed.'),
    ('Old regime shirt price and effective tax?', '₹550; 33.5% (184/550).'),
    ('Total value added in the example?', '₹366.'),
    ('Of the ₹32 tax, how much was on fresh value?', '₹5.8 (₹26.2 was tax on tax or taxed value).'),
    ('VAT introduced?', '2005 for State sales tax.'),
    ('Central VATting in the 1980s?', 'CENVAT / MODVAT.'),
    ('ITC?', 'Tax paid on inputs offset against tax on output.'),
    ('ITC rule?', 'Same tax only: VAT against VAT.'),
    ('Is tax charged on value added?', 'No: on the entire value; ITC makes it effective on value added.'),
    ('What VAT left behind?', 'A ₹2 tax on excise (VAT on excise).'),
    ('GST definition?', 'Tax on supply of goods and services other than alcohol for human consumption.'),
    ('Three properties of GST?', 'One nation-one tax; destination-based; VAT-like.'),
    ('Event under GST?', 'Only the sale (supply) of a good or service.'),
    ('Which tax stays out of GST by design?', 'Customs.'),
    ('Within a State?', 'CGST + SGST.'),
    ('Across States?', 'IGST.'),
    ('SGST goes to?', 'The destination State.'),
    ('Exports under GST?', 'Zero-rated; full duty drawback.'),
    ('Zero-rated vs exempt?', 'Zero-rated gets credit/drawback; exempt does not.'),
    ('Imports under GST?', 'Basic customs duty, then IGST.'),
    ('101st Amendment?', 'Constitution (101st Amendment) Act, 2016, notified 08.09.2016.'),
    ('Art. 246A?', 'Concurrent power to levy GST.'),
    ('Art. 269A?', 'Centre levies IGST on inter-State supplies and imports.'),
    ('Art. 279A?', 'GST Council.'),
    ('Council chair and vice chair?', 'Union FM; a State minister.'),
    ('Quorum and decision?', '50% quorum; 75% majority.'),
    ('Voting weight?', 'States 2/3, Centre 1/3.'),
    ('Outside GST?', 'Alcohol for human consumption; 5 petroleum products; local entertainment tax.'),
    ('Five petroleum products?', 'Crude, high speed diesel, petrol, natural gas, ATF.'),
    ('Tobacco?', 'Inside GST, with extra Central excise.'),
    ('Stamp duty?', 'Levied separately by States.'),
    ('12 nautical miles?', 'Central administration; States may tax activities there.'),
    ('GST rate slabs (handout)?', '0, 5, 12, 18, 28 (+ cess).'),
    ('Raw agricultural produce?', 'Zero-rated.'),
    ('Compensation assumed growth?', '14% for 5 years (till 2022).'),
    ('Compensation condition?', 'Only for shortfall due to GST implementation.'),
    ('RNR?', 'Rate that keeps government revenue unchanged.'),
    ('Pre-GST incidence?', 'About 30% (12% excise + 14% VAT + others).'),
    ('Anti-profiteering?', 'Illegal to keep tax cuts as extra profit.'),
    ('Registration threshold?', '₹20 lakh (₹10 lakh special category except J&K).'),
    ('Deemed registration?', 'In 3 working days.'),
    ('Composition levy?', 'Optional turnover-based tax for small taxpayers; GSTR-4 quarterly.'),
    ('Composition threshold?', '₹75 lakh (₹50 lakh some States) in the paragraph; ₹100 lakh in the features list (conflict).'),
    ('E-way bill?', 'Inter-State from 01.04.2018; all intra-State by 16.06.2018.'),
    ('GSTN?', 'Section 25 company, March 2013, ₹10 crore; now fully government owned.'),
    ('GSTN service providers?', 'Infosys is MSP; 73 GSPs.'),
]
c.summary = 'Cascading and the shirt example, VAT and Input Tax Credit, the GST definition and three properties, CGST, SGST and IGST, GST Council voting, Articles 246A, 269A and 279A, outside GST, compensation, revenue neutral rate, anti-profiteering, registration, composition and GSTN.'
