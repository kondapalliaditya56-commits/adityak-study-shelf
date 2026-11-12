# -*- coding: utf-8 -*-
"""NCERT content for handout Ch 6 (Inflation), placed after the matching handout section.
Sources: XII Macroeconomics Ch 1, 2, 3, 4, 5, 6; XII Microeconomics Ch 1, 5; XI Indian Economic Development Ch 2, 3; glossaries.
Only NCERT-only points or differences. Every number is as printed in NCERT or the handout."""
SRC = 'NCERT'
def T(head, rows): return {'head': head, 'rows': rows}
NC = {
 '1': [dict(ref='XII Macro Ch 1 (Introduction), XII Micro Ch 1 §1.5, XI Ch 2 (price as a signal), XI Glossary',
   why='The handout says one dearer good is not inflation. NCERT explains <b>why economists talk about “the price level” at all</b>, and how one price differs from it. Read the three small steps; each is two or three lines.',
   link='Handout section 1: “Price = one good; price level = AD and AS”. NCERT’s “price of one good” is the handout’s “price”; NCERT’s “general price level” is the handout’s “price level”.',
   blocks=[
    dict(h='Step 1 · Prices of different goods tend to move together', pts=[
         'NCERT (XII Macro Ch 1): “prices of different goods and services generally have a tendency to rise or fall simultaneously”. So macroeconomics can think of <b>one imaginary representative good</b> whose price stands for the general price level.',
         'When prices are going up fast “in what is called an inflation”, the direction of movement is usually the same for all the individual commodities as for the economy as a whole.']),
    dict(h='Step 2 · Micro looks at one price; macro asks “why do prices rise?”', pts=[
         'XII Micro Ch 1: in microeconomics we study how price and quantity are fixed in <b>one market</b>. In macroeconomics we study aggregate measures: total output, employment and the <b>aggregate price level</b>. One of its questions: “Why do prices rise?”',
         'XII Macro Ch 1: for microeconomics, inflation or unemployment were either not mentioned or taken as given. They are not variables that individual buyers or sellers can change.',
         'Who can act on them? NCERT: macroeconomic policies are pursued by the State itself or by statutory bodies like the <b>RBI</b> and <b>SEBI</b>, each with public goals set by law, not private profit.']),
    dict(h='Step 3 · A single price is a signal (XI Ch 2)', pts=[
         'If a good becomes scarce, its price rises. The rise is a <b>signal</b> that less is available, and gives users an incentive to use it with greater care.',
         'NCERT’s example: the price of water goes up because of lower supply, so people stop watering the garden. Likewise a petrol price rise reflects greater scarcity and encourages using less petrol or looking for alternate fuels.']),
    dict(h='NCERT’s glossary definition (XI Glossary)', pts=['<b>Inflation</b>: “A sustained rise in the general price level.”'])],
   d=['NCERT’s glossary says a <b>sustained</b> rise in the general price level; the handout says a general rise in prices or the price level. Same idea. Use the handout’s words and add “sustained” if you wish.'])],
 '2': [dict(ref='XII Macro Ch 4 §4.3 and §4.4 (price level fixed first; excess and deficient demand)',
   why='The handout rule is “prices rise when AD exceeds AS”. NCERT says the same thing in its own words (<b>excess demand</b>) and explains why its first model keeps the price level fixed, so you do not get confused when a NCERT diagram shows no price at all.',
   link='Handout: AD &gt; AS ⇒ prices rise. NCERT: excess demand ⇒ rise in prices. “Full employment output” is the output when all factors are fully employed.',
   blocks=[
    dict(h='Step 1 · Why NCERT first keeps the price level fixed', pts=[
         'NCERT builds the theory in two steps: (1) find the macroeconomic equilibrium taking the <b>price level as fixed</b>; (2) then let the price level vary.',
         'Reason (i): at the first stage the economy has unused resources: machineries, buildings and labours. The law of diminishing returns does not apply, so extra output can be produced without increasing marginal cost, and the price level does not change when the quantity changes. Reason (ii): it is a simplifying assumption that will be changed later.']),
    dict(h='Step 2 · Equilibrium output against full-employment output', tbl=T(['Where equilibrium output stands', 'NCERT’s name', 'What it does to prices “in the long run”'], [
         ['Less than full-employment output (demand not enough to employ all factors)', '<b>Deficient demand</b>', 'Leads to a <b>decline</b> in prices'],
         ['More than full-employment output (demand more than the output produced at full employment)', '<b>Excess demand</b>', 'Leads to a <b>rise</b> in prices']]),
         pts=['NCERT’s caution: equilibrium (Y = AD) by itself does not mean full employment. It only means income will not change if left to itself, even with unemployment.'])],
   d=['NCERT says excess demand raises prices “in the long run”. The handout (teacher) says prices rise when AD exceeds AS. Same direction; use the handout rule in the answer.'])],
 '3': [dict(ref='XII Micro Ch 5 §5.1 (Market Equilibrium), Figs 5.2 and 5.3',
   why='The handout’s AD shift and AS shift pictures copy a simpler picture NCERT draws for <b>one market</b>. Understand it here once: a demand shift and a supply shift move price in the way the handout’s “pull” and “push” do.',
   link='Handout section 3: demand-pull = AD shifts right (price up, output up). Cost-push = AS shifts left (price up, output down). NCERT’s single-market result is the same pattern.',
   blocks=[
    dict(h='Step 1 · The four shifts in one table (NCERT)', tbl=T(['What shifts', 'Equilibrium price', 'Equilibrium quantity', 'NCERT’s example'], [
         ['Demand curve to the <b>right</b>', 'Rises', 'Rises', 'Higher consumer income for a normal good like clothes; more consumers'],
         ['Demand curve to the left', 'Falls', 'Falls', 'The opposite shift'],
         ['Supply curve to the <b>left</b>', 'Rises', 'Falls', 'Rise in the price of an input: marginal cost goes up, so supply at each price is less'],
         ['Supply curve to the right', 'Falls', 'Rises', 'Increase in the number of firms']]),
         pts=['NCERT’s rule: the direction of change of price and quantity is the <b>same</b> whenever demand shifts, and <b>opposite</b> whenever supply shifts.']),
    dict(h='Step 2 · Why price rises after a right shift of demand', pts=[
         'At the old price p<sub>0</sub> there is <b>excess demand</b>. Some individuals are willing to pay a higher price, so the price tends to rise until the new equilibrium G (price p<sub>2</sub>).',
         'After a left shift of supply there is also excess demand at p<sub>0</sub>: consumers who cannot get the good are willing to pay more, so the price rises.'],
         fig=('img/ncert-c6-demshift.png', 'NCERT Fig. 5.2, original: shift in demand. Panel (a) is the right shift (E to G, price and quantity up).')),
    dict(h='Step 3 · The supply side, in NCERT’s own figure', fig=('img/ncert-c6-supshift.png', 'NCERT Fig. 5.3, original: shift in supply. Panel (a) is the left shift (E to G, price up, quantity down).'))],
   d=['NCERT’s curves are for <b>one good</b> (microeconomics). The handout’s AD and AS are for the <b>whole economy</b>; the logic is the same, but they are different curves and should not be mixed in one diagram.']),
  dict(ref='XII Macro Ch 5 §5.3 (deficits and debt), XII Macro Glossary, XI Ch 3 (1991 crisis)',
   why='The handout lists “more government spending” and “easy money” as demand-pull causes. NCERT adds <b>when</b> a deficit pushes prices up and when it does not, and shows a real case.',
   link='Handout section 3: demand-pull causes (government spending, easy money) and the international-shock list. NCERT gives the condition that decides whether spending turns into inflation.',
   blocks=[
    dict(h='Step 1 · Are fiscal deficits inflationary? (NCERT’s answer)', pts=[
         'One of the main criticisms of deficits is that they are inflationary: when the government increases spending or cuts taxes, aggregate demand increases.'],
         tbl=T(['Condition in the economy', 'What NCERT says happens'], [
         ['Firms cannot produce the higher quantity demanded at the going prices', 'Prices will have to <b>rise</b>'],
         ['There are unutilised resources; output is held back by lack of demand', 'A high fiscal deficit comes with higher demand and greater output, so it <b>need not be inflationary</b>']])),
    dict(h='Step 2 · Borrowing from the central bank', pts=['NCERT Glossary: financing a budget deficit by borrowing money from the central bank “leads to increase in money supply in an economy and may result in inflation”.']),
    dict(h='Step 3 · A real case: India before 1991 (XI Ch 3)', pts=[
         'In the late 1980s government expenditure began to exceed its revenue by such large margins that meeting it through borrowings became unsustainable.',
         'Prices of many essential goods rose sharply. Imports grew at a very high rate without matching growth of exports, and foreign exchange reserves fell to a level not adequate to finance imports for more than two weeks.',
         'NCERT lists “rising prices of essential goods” among the reasons for the financial crisis that led to the 1991 reforms.'])],
   d=['The handout names government spending as a cause of demand-pull without any condition. NCERT adds the condition: it raises prices when output cannot rise to meet it.'])],
 '5': [dict(ref='XII Macro Ch 2 §2.4 (Nominal and real GDP; CPI; GDP deflator)',
   why='The handout’s index rule is “(100 ÷ base basket price) × current basket price”. NCERT shows the <b>same ratio</b> with a tiny two-item basket, so you can see every step. It also introduces a second price index, the GDP deflator, which uses the base year in the way the handout’s last bullet mentions.',
   link='Handout section 5: index = (100 ÷ base-year price) × current price; base year = constant basket. NCERT calls this ratio the <b>Consumer Price Index (CPI)</b>. The handout’s last bullet: in Real GDP the base year gives constant prices. NCERT shows that now.',
   blocks=[
    dict(h='Step 1 · NCERT’s CPI recipe', pts=['Work out the cost of buying a given basket of commodities in the <b>base year</b>.', 'Work out the cost of buying the <b>same basket</b> in the current year.', 'Express the second as a percentage of the first.'],
         fm=[('CPI (NCERT)', 'CPI = cost of basket in current year ÷ cost of basket in base year × 100', 'the same ratio as the handout’s index', 'wide')]),
    dict(h='Step 2 · NCERT’s worked example (representative consumer buys 90 kg rice and 5 pieces of cloth a year)', tbl=T(['Item', 'Quantity', 'Price 2000', 'Price 2005', 'Spend 2000', 'Spend 2005'], [
         ['Rice', '90 kg', '₹10', '₹15', '₹900', '₹1,350'], ['Cloth', '5 pieces', '₹100', '₹120', '₹500', '₹600'], ['<b>Total</b>', '', '', '', '<b>₹1,400</b>', '<b>₹1,950</b>']]),
         pts=['CPI = 1,950 ÷ 1,400 × 100 = <b>139.29</b> (approximately), as printed in NCERT. Read it exactly as the handout reads 165: prices are about 39% above the base year (arithmetic: 139.29 − 100).']),
    dict(h='Step 3 · Why real GDP is needed (nominal against real)', pts=[
         'If GDP doubles, production may have doubled, or only prices may have doubled. So NCERT compares GDP at <b>constant prices</b> (real GDP). Nominal GDP is GDP at current prevailing prices.',
         'The base year is the year whose prices are used to work out real GDP.'],
         tbl=T(['NCERT’s bread economy', 'Units of bread', 'Price per bread', 'Nominal GDP', 'Real GDP (at year 2000 prices)'], [
         ['Year 2000 (base year)', '100', '₹10', '₹1,000', '₹1,000 (same as nominal in the base year; worked out here)'], ['Year 2001', '110', '₹15', '₹1,650 (110 × ₹15)', '₹1,100 (110 × ₹10)']])),
    dict(h='Step 4 · GDP deflator: a price index from the same two numbers', fm=[('GDP deflator', 'GDP deflator = nominal GDP ÷ real GDP (× 100 for per cent)', 'NCERT: 1,650 ÷ 1,100 = 1.50 = 150 per cent')],
         pts=['The ratio of nominal to real GDP shows how prices moved from the base year to the current year. NCERT: 150 per cent means the price of bread in 2001 was 1.5 times the price in 2000, which is true (₹10 to ₹15).',
              'Practice (NCERT Exercise 11): nominal GNP ₹2,500 crore; GNP at base-year prices ₹3,000 crore. GNP deflator = 2,500 ÷ 3,000 × 100 = 83.33 per cent (worked out here). It is below 100, so the price level has not risen since the base year; it has fallen.'])],
   d=['NCERT’s glossary defines CPI as the “Percentage change in the weighted average price level”, but NCERT’s own chapter text defines CPI as an <b>index</b> (139.29). That is an internal mismatch in NCERT. Use the handout: the index is the level; <b>inflation is the % change of the index</b> over the same month last year.',
      'NCERT’s example compares year 2000 with year 2005 with one yearly basket. The handout builds a basket for each month (for seasons) and quotes Y-o-Y inflation. Handout wins for method.'])],
 '6': [dict(ref='XII Macro Ch 2 §2.4 (retail and wholesale price; CPI, WPI, PPI; why they differ from the deflator), XII Macro Glossary',
   why='The handout lists the Indian indices and who releases them. NCERT explains the <b>idea</b> behind CPI and WPI (retail against wholesale) and gives three reasons why a CPI is not the same as the GDP deflator.',
   link='Handout section 6: CPI, CPI-AL and CPI-IW, WPI, and “India has no official PPI”. NCERT does not name the release bodies, CPI-AL, CPI-IW or the 2024 series: learn those from the handout only.',
   blocks=[
    dict(h='Step 1 · Retail price against wholesale price', pts=[
         'Many commodities have two sets of prices: the <b>retail price</b> the consumer actually pays, and the <b>wholesale price</b> at which goods are traded in bulk. They can differ because of the margin kept by traders.',
         'Goods traded in bulk (such as raw materials or semi-finished goods) are not purchased by ordinary consumers.',
         'Like CPI, the index for wholesale prices is the <b>Wholesale Price Index (WPI)</b>. NCERT: in countries like the USA it is called the <b>Producer Price Index (PPI)</b>.'],
         tbl=T(['Index', 'Basket, in NCERT’s glossary'], [['Consumer Price Index (CPI)', 'A given basket of consumption goods'], ['Wholesale Price Index (WPI)', 'A given basket of goods traded in bulk'], ['GDP deflator', 'Ratio of nominal to real GDP']])),
    dict(h='Step 2 · Why CPI (or WPI) differs from the GDP deflator', tbl=T(['#', 'Reason (NCERT)', 'In plain words'], [
         ['1', 'Goods bought by consumers are not all the goods produced; the deflator takes all goods and services', 'CPI covers a shopping bag; the deflator covers everything the country produces'],
         ['2', 'CPI includes prices of imported goods consumers buy; the deflator does not include prices of imported goods', 'A dearer imported phone shows in CPI, not in the deflator'],
         ['3', 'Weights are constant in CPI; in the deflator they differ with the production level of each good', 'CPI keeps one fixed basket; the deflator’s mix follows what is produced']]))],
   d=['NCERT says CPI weights are constant. The handout shows weights and items being revised when a new base-year series starts (food 45.86% to 36.75%, 299 to 358 items). Read NCERT’s “constant” as “fixed for one base-year series” (this is a reading, not an NCERT sentence).',
      'NCERT’s glossary again says CPI and WPI are “Percentage change in the weighted average price level”; the chapter text calls them indices. Use the index meaning.'])],
 '9': [dict(ref='XII Macro Ch 3 §3.1 (value of money), XII Macro Ch 6 §6.3 (PPP, Example 6.1, Exercise 15)',
   why='The handout shows inflation shrinking what money buys, with apples. NCERT gives the same idea as a one-line formula, and adds an effect the handout skips: what inflation does to the <b>exchange rate</b> in the long run.',
   link='Handout section 9: ₹100 bought 1 kg of apples, now ₹110. NCERT’s “purchasing power of money” is the same thing.',
   blocks=[
    dict(h='Step 1 · The value of money falls when the price level rises', fm=[('Value of ₹1 in terms of a good', '1 ÷ price of the good', 'pencil ₹2 → ₹1 = 0.5 pencil; pen ₹10 → ₹1 = 0.1 pen')],
         pts=['If prices of all commodities increase in terms of money (a general increase in the price level), the value of money in terms of any commodity has decreased: a unit of money now buys less. NCERT calls this a <b>deterioration in the purchasing power of money</b>.',
              'Money can store value only if its own value is sufficiently stable. “A rising price level may erode the purchasing power of money.”']),
    dict(h='Step 2 · Inflation and the exchange rate in the long run (PPP theory)', pts=[
         'NCERT: over the long run, exchange rates between two currencies adjust to reflect differences in the <b>price levels</b> of the two countries, so the same product costs the same in rupees in India or dollars in the US (ignoring transport, and with no tariffs or quotas).'],
         tbl=T(['NCERT Example 6.1: a shirt', 'Price in the US', 'Price in India', 'Exchange rate that equalises them'], [
         ['Start', '$8', '₹400', '₹50 per dollar'], ['After prices rise 20 per cent in India and 50 per cent in the US', '$12', '₹480', '$12 must be worth ₹480, so ₹40 per dollar: the dollar has <b>depreciated</b>']])),
    dict(h='Step 3 · NCERT’s practice question (Exercise 15)', pts=['Rate ₹30 = $1 in 2010. Prices double in India over 20 years and stay fixed in the USA. By the PPP idea the rate in 2030 is 30 × 2 = ₹60 per dollar (worked out here): the rupee is weaker because India’s prices rose.'])],
   d=['The handout’s effects of inflation are all domestic (borrowers, lenders, depositors, consumers, producers). The exchange-rate effect is NCERT-only; add it as an extra point in a Mains answer.'])],
 '11': [dict(ref='XII Macro Ch 5 §5.1.2 and §5.3 (progressive tax; automatic stabilisers), Key Concepts',
   why='The handout calls fiscal drag an “automatic stabiliser”. NCERT defines that term. It uses a different tax example, so first see NCERT’s idea, then match it to the handout’s slabs.',
   link='Handout section 11: higher slabs mean more tax on the extra income, so spending is cut automatically. NCERT: a tax that takes a part of every rupee of extra income acts as a shock absorber.',
   blocks=[
    dict(h='Step 1 · What an automatic stabiliser is (NCERT)', pts=['NCERT: a proportional income tax acts as an automatic stabiliser, a <b>shock absorber</b>, because it makes disposable income, and thus consumer spending, less sensitive to fluctuations in GDP.'],
         tbl=T(['Phase', 'What happens'], [
         ['GDP rises', 'Disposable income also rises but by <b>less</b> than GDP, because a part is siphoned off as taxes. This limits the upward fluctuation in consumption spending'],
         ['Recession (GDP falls)', 'Disposable income falls <b>less sharply</b>, so consumption does not drop as much and the fall in aggregate demand is reduced']])),
    dict(h='Step 2 · Automatic against deliberate', pts=[
         'Built-in stabilisers work “without the need for any decision-maker to take action”; they work automatically. <b>Welfare transfers</b> also help stabilise income.',
         'Deliberate action to stabilise the economy (changing government spending or taxes) is called <b>discretionary fiscal policy</b>.',
         'NCERT’s caution: built-in stabilisers reduce only <b>part</b> of the fluctuation; the rest must be taken care of by deliberate policy.']),
    dict(h='Step 3 · Progressive tax (the handout’s slabs)', pts=['NCERT: redistribution is sought through <b>progressive</b> income taxation, in which the higher the income, the higher the tax rate. Firms are taxed on a proportional basis, a particular proportion of profits.'])],
   d=['NCERT’s example of a stabiliser is a <b>proportional</b> tax, and it explains the effect on a recession as well. The handout’s fiscal drag works through <b>progressive</b> slabs in an inflation. NCERT does not use the term “fiscal drag”. Use the handout’s term and quote NCERT’s “automatic stabiliser”.'])],
 '12': [dict(ref='XII Macro Ch 5 §5.1.1 (stabilisation function), XI Ch 3 (stabilisation measures), XI Glossary',
   why='The handout’s cure is one idea: make money expensive. NCERT shows two more pieces of the picture: the <b>government’s</b> stabilisation job, and India’s own short-term measures in 1991. The tools of the RBI itself are in the Chapter 8 NCERT boxes.',
   link='Handout section 12: bring AD down, whatever the cause; structural fixes come too late. NCERT’s “stabilisation” (short term) and “structural” (long term) are the same split.',
   blocks=[
    dict(h='Step 1 · The stabilisation function of the budget (NCERT)', pts=[
         'If demand is not enough to use labour and other resources fully, the government needs to intervene to <b>raise</b> aggregate demand.',
         'There may also be times when demand exceeds available output under conditions of high employment and gives rise to inflation. Then “restrictive conditions may be needed to <b>reduce</b> demand”.',
         'The government’s intervention, whether to expand demand or to reduce it, is the <b>stabilisation function</b>.']),
    dict(h='Step 2 · India 1991: two kinds of measures (XI Ch 3)', tbl=T(['', 'Stabilisation measures', 'Structural reform policies'], [
         ['Time frame', 'Short-term', 'Long-term'],
         ['Aim', 'Correct weaknesses in the balance of payments and bring inflation under control; keep enough foreign exchange reserves and keep rising prices under control', 'Improve the efficiency of the economy and increase its international competitiveness']]),
         pts=['XI Glossary: <b>Stabilisation measures</b> are “fiscal and monetary measures adopted to control fluctuations in the balance of payments and high rate of inflation”.']),
    dict(h='Step 3 · Where the RBI’s own tools are', pts=['CRR, Bank Rate, open market operations and the repo rate are covered in the NCERT boxes of <b>Chapter 8</b> (Money and Monetary Policy), so they are not repeated here.'])],
   d=['NCERT presents controlling inflation as a job for both fiscal and monetary measures. The handout puts the weight on money becoming expensive (monetary) and promises that story in Chapter 8.'])],
}

SRCFILES = ['leec101', 'leec102', 'leec103', 'leec104', 'leec105', 'leec106', 'leec201', 'leec205', 'keec102', 'keec103', 'leec1gl', 'keec1gl']
NCMAP = [('XII Macro Ch 1 and XII Micro Ch 1, XI Ch 2: price level, one price as a signal', '1', 'Why macro talks about the price level; inflation in NCERT’s glossary'),
         ('XII Macro Ch 4 §4.3 and §4.4: price level fixed first; excess and deficient demand', '2', 'Why NCERT shows no price at first; excess demand raises prices'),
         ('XII Micro Ch 5, Figs 5.2 and 5.3: demand and supply shifts in one market', '3', 'Price and quantity after each shift: the single-market version of pull and push'),
         ('XII Macro Ch 5 §5.3, Glossary, XI Ch 3: deficits and prices; the 1991 crisis', '3', 'When a deficit becomes inflation; central bank borrowing; real case'),
         ('XII Macro Ch 2 §2.4: CPI example; nominal and real GDP; GDP deflator', '5', 'Worked CPI of 139.29; deflator; Exercise 11 answered'),
         ('XII Macro Ch 2 §2.4: retail, wholesale, WPI, PPI; why CPI differs from the deflator', '6', 'Three reasons; the idea behind CPI and WPI'),
         ('XII Macro Ch 3 §3.1 and Ch 6 §6.3: value of money; PPP', '9', 'Value of ₹1; inflation and the exchange rate (Example 6.1)'),
         ('XII Macro Ch 5: automatic stabilisers, progressive tax', '11', 'NCERT’s meaning of automatic stabiliser; built-in against discretionary'),
         ('XII Macro Ch 5 §5.1.1; XI Ch 3: stabilisation function and measures', '12', 'Government’s side of inflation control; short against long term')]
NCQ = [('Exercise 11 (XII Macro Ch 2): nominal GNP ₹2,500 crore, GNP at base-year prices ₹3,000 crore: find the GNP deflator; has the price level risen?', 'Section 5 NCERT box, Step 4 (83.33 per cent: no, it has fallen)'),
       ('Exercise 13 (XII Macro Ch 5): Are fiscal deficits inflationary?', 'Section 3 NCERT box on deficits'),
       ('Exercise 15 (XII Macro Ch 6): prices double in India, fixed in the USA; what is the PPP exchange rate in 2030?', 'Section 9 NCERT box, Step 3'),
       ('Exercise 1 (XI Ch 3): Why were reforms introduced in India? (the price part)', 'Section 3 NCERT box, Step 3 (rising prices of essential goods)')]
NCKEY = ['Nominal GDP', 'Real GDP', 'Base year', 'GDP Deflator', 'Consumer Price Index (CPI)', 'Wholesale Price Index (WPI)', 'Inflation', 'Stabilisation measures',
         'Automatic stabiliser', 'Discretionary fiscal policy', 'Purchasing power parity']
NCONLY = [('XII Macro Ch 2 §2.5: GDP and welfare', 'Limits of GDP as a measure of well-being: not part of this inflation chapter'),
          ('XII Macro Ch 4 (rest): effective demand, MPC, multiplier', 'Income determination with the price level fixed; read from NCERT'),
          ('XII Macro Ch 6: exchange rate determination, balance of payments', 'Foreign exchange demand and supply; belongs to the external sector chapter'),
          ('XII Macro Ch 5: budget receipts, expenditure, deficits, FRBM Act', 'Budget chapter; only the inflation points are used above'),
          ('XI Ch 3: other reforms (industry, trade, privatisation)', 'Reforms chapter; only price and stabilisation points are used above')]
