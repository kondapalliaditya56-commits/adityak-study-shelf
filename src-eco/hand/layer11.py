# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 11 (Goods and Services Tax). Facts come only from the handout text.
plain = idea in everyday words (memory aid); eg = the handout's own example; hook = one-line handle."""
TOP = {
 'sixty': [('Old system', 'taxes on many events (production, sale, entry), levied by Centre and States separately'),
           ('Problem', 'cascading: tax on tax; of ₹32 only ₹5.8 was on fresh value'),
           ('Cure 1', 'VAT (2005) and Input Tax Credit: tax only on value added, same tax against same tax'),
           ('Cure 2', 'GST: one event (the sale), one nation-one tax, destination-based, CGST + SGST or IGST'),
           ('Rulebook', '101st Amendment (08.09.2016), GST Council (Art. 279A): FM chair, 75% to decide, States 2/3 weight'),
           ('Fine print', 'benefits, slabs, compensation (14% for 5 years), RNR, anti-profiteering, registration ₹20 lakh')],
 'words': [('Indirect tax', 'tax put on A, paid to government by A, but collected from B who bears the burden'),
           ('Cascading', 'tax on tax, and tax again on value that was already taxed'),
           ('Value added', 'what a producer adds to the inputs he bought: the only fresh value at his stage'),
           ('Input Tax Credit (ITC)', 'the tax you already paid on inputs, subtracted from the tax you owe on your sale'),
           ('Destination-based', 'the tax belongs to the place where the goods are supplied to, not where they were sold from'),
           ('Zero-rated', 'exports carry no GST and the exporter can claim full duty drawback; not the same as exempt'),
           ('Revenue Neutral Rate (RNR)', 'the average GST rate that leaves government revenue unchanged'),
           ('Profiteering', 'a seller keeping a tax cut as extra profit instead of lowering the price')],
}
SEC = {
 '1': dict(
   plain='Picture a toll road. A tax is a toll on an event: a sale, earning income, a crossing of the border, a company making profit. The person on whom the toll is put hands it to the government. In an indirect tax that person (A) simply adds it to his price and collects it back from B, who bears the burden. In the old system there were many toll booths, Centre and States each with their own, and a State could not tax a sale that crossed its border, so the Centre took Central Sales Tax and gave it to the selling State.',
   eg='The handout’s old regime: every producer pays excise duty to the Centre on production; on every sale the State levies sales tax; wholesaler and retailer add margins; the consumer bears it all.',
   hook='Tax is on an event. Indirect: A pays the government, B bears it.'),
 '2': dict(
   plain='Picture paying a toll, and then the next booth charging a toll on a price that already contains the first toll. That is a tax on tax. The same rupee of value is taxed again at every stage, so by the time a shirt reaches you, a large part of the price is tax on tax. With such a burden nobody would ask for a bill.',
   eg='The handout’s shirt: price ₹550, effective tax ₹184 on ₹550 = 33.5%. Of the ₹32 sales tax from producer to wholesaler: ₹5.8 fresh value, ₹2 tax on the excise, ₹20 on value already taxed, ₹2 and ₹2.2 more tax on tax.',
   hook='Of ₹32 levied, only ₹5.8 was on fresh value. ₹26.2 was tax on tax.'),
 '3': dict(
   plain='Think of a bill with a credit note. When you bought inputs you already paid tax on them. When you sell, the tax is charged on the whole sale, but you subtract what you paid earlier (proof: the bill) and hand over only the difference. So the government really gets tax on your value added. The rule: credit works only for the same tax, VAT with VAT, never VAT against excise or other levies. VAT still taxed the excise, so some cascading stayed.',
   eg='The handout’s bills: old regime ₹320 + ₹32 = ₹352. VAT regime: inputs 220 + value added 58 + excise 20 = ₹298, tax ₹29.8, less ITC ₹22 = ₹7.8 payable, wholesaler pays ₹327.8. The ₹7.8 is ₹5.8 + ₹2.',
   hook='Charge tax on the whole, ITC trims it to value added. Same tax against same tax only.'),
 '4': dict(
   plain='GST is VAT stretched over everything. All the other events of indirect tax (excise, CST, entry tax, octroi) are removed and only one is left: the sale. Because every tax is now the same family, credit flows all the way down the chain, and each stage ends up paying tax only on its own value added. Inside a State you see two parts (Centre and State); across States there is one tax, IGST, collected by the Centre.',
   eg='The handout’s shirt at an assumed 20%: shirt producer 51.6 − 40 = ₹11.6 (20% of 58); wholesaler 61.2 − 51.6 = ₹9.6; retailer 73.2 − 61.2 = ₹12; consumer pays ₹73.2 = 20% of 366; final price ₹439.2 against ₹550 earlier.',
   hook='One event (sale), one tax, credit all the way. Net tax at each stage = rate × value added.'),
 '5': dict(
   plain='Imagine a joint committee that both the Centre and the States sit on, so neither can change the tax alone. The Union Finance Minister chairs it; State ministers fill the seats. At least half the members must be present and a decision needs a 75% majority. Votes are weighted: States hold two-thirds, the Centre one-third. The handout reads this as sovereignty pooled, not surrendered; critics say States gave up control of their own tax rates.',
   eg='The handout’s three articles: Art. 246A (both levy), Art. 269A (Centre levies IGST on inter-State supply and imports), Art. 279A (the Council). Five petroleum products are to come in later on the Council’s word.',
   hook='Council: FM chairs, quorum 50%, decision 75%, States 2/3 and Centre 1/3.'),
 '6': dict(
   plain='Think of a fence around GST with a few things left outside. Alcohol for human consumption stays with the State, five petroleum products wait for the Council to fix a date, and the entertainment tax of local bodies stays local. Tobacco is inside, but the Centre can add excise. Stamp duties stay with States. Because petroleum is outside, the VAT paid on it cannot be offset against GST.',
   eg='The handout’s infographic “Outside GST!”: alcohol (State), crude oil, diesel, petrol, natural gas and ATF (Council to decide the date), tobacco (inside, extra Central excise), entertainment tax (local bodies).',
   hook='Outside: alcohol, five petroleum products, local entertainment tax. Tobacco is inside.',
   mn=[{'kind': 'word', 'title': 'What stays outside GST (order is free)', 'word': 'APE',
        'letters': [('A', 'Alcohol for human consumption'), ('P', 'Petroleum (five products)'), ('E', 'Entertainment tax of local bodies')],
        'note': 'Own memory aid (not from the handout): the APE stays outside the GST fence. Tobacco is inside.'}]),
 '7': dict(
   plain='Benefits: fewer layers, one market, credit across Centre and State taxes (the biggest reform), and a system that catches the evader instead of a tax officer who may be bribed. Problems: many slabs, lobbying to get rates cut, politics in the Council. A single flat rate would be regressive, so slabs add a progressive touch. States were promised compensation for five years. RNR is the break-even rate: widen the base and a lower rate collects the same money. Anti-profiteering makes sure the cut reaches the buyer.',
   eg='The handout’s RNR: at 30% effective rate, ₹10 of tax means only ₹33 of the ₹100 of output was taxed (one-third of GDP). If GST taxes double the value (two-thirds of GDP), a 15% rate still gives ₹10. Compensation: pre-2017 revenue grown at 14% a year for five years (till 2022).',
   hook='Broader base, lower rate: RNR 30% to 15%. Compensation only for GST-caused shortfall.'),
 '8': dict(
   plain='Think of the paperwork of a small shop. It need not register unless turnover is above ₹20 lakh. A small taxpayer may choose the composition levy: a fixed percentage of turnover each quarter instead of the normal rate. Everything runs online through the GST Network (GSTN), a company incorporated in 2013 and now completely government owned. The e-way bill tracks goods that move.',
   eg='The handout’s numbers: registration above ₹20 lakh (₹10 lakh special category States except J&K); deemed registration in three working days; e-way bill from 01.04.2018; GSTN: Section 25 company, ₹10 crore capital, Infosys as managed service provider, 73 GSPs.',
   hook='Register above ₹20 lakh. GSTN 2013, e-way bill 01.04.2018, GST 01.07.2017.',
   mn=[{'kind': 'sentence', 'title': 'The road to GST, in order (VAT, GSTN, Amendment, GST)', 'sentence': 'Value Gets Added Gradually',
        'letters': [('V', 'VAT 2005'), ('G', 'GSTN 2013'), ('A', 'Amendment 08.09.2016'), ('G', 'GST 01.07.2017')],
        'note': 'Own memory aid (not from the handout): keep the order.'}]),
}
FM = {
 '3': [('Tax payable after ITC', 'output tax − ITC (tax already paid on inputs)', 'old VAT example: 29.8 − 22 = 7.8'),
       ('VAT tax base (2005-2017)', 'input + value added + excise = 220 + 58 + 20 = 298', 'tax 29.8; wholesaler pays 327.8'),
       ('Cascading test', 'tax on value added = fresh; the rest = tax on tax', 'of ₹32: 5.8 fresh, 26.2 not'),
       ('ITC rule', 'tax against the same tax only', 'VAT against VAT, not excise or State levies', 'wide')],
 '4': [('Net tax at a stage', 'GST on sale − ITC = rate × value added', 'shirt producer: 51.6 − 40 = 11.6 = 20% of 58'),
       ('Final burden', 'rate × total value added', '20% of 366 = 73.2; price ₹439.2'),
       ('Within a State', 'CGST + SGST', 'CGST to the Centre, SGST to the destination State'),
       ('Across States', 'IGST', 'levied by the Centre (Art. 269A); imports: basic customs duty then IGST')],
 '5': [('Council rule', 'quorum 50%; decision 75%; weight States 2/3, Centre 1/3', 'chair: Union Finance Minister (Art. 279A)')],
 '7': [('Compensation due', 'pre-2017 revenue grown at 14% a year for 5 years − actual revenue', 'only if the shortfall is because of GST', 'wide'),
       ('Revenue neutral rate', 'rate × share of GDP taxed = revenue', '30% on one-third = ₹10; 15% on two-thirds = ₹10'),
       ('Good tax law', 'low cost of compliance + high cost of non-compliance', 'GST: the system catches the evader')],
 '8': [('Registration', 'turnover above ₹20 lakh (₹10 lakh special category except J&K)', 'voluntary registration allowed; deemed in 3 working days'),
       ('Composition return', 'Form GSTR-4 by the 18th after the quarter', 'July-September 2017 due 18 October 2017')],
}
NUMBERS = [('₹32 → ₹5.8', 'sales tax producer to wholesaler; fresh part (rest ₹26.2)'),
           ('33.5%', 'effective tax on the ₹550 shirt (₹184)'),
           ('₹7.8', 'VAT payable after ITC ₹22 on ₹29.8'),
           ('₹439.2 vs ₹550', 'shirt price under GST at 20% against the old regime'),
           ('2005', 'State VAT starts'),
           ('08.09.2016', '101st Amendment Act notified'),
           ('01.07.2017', 'GST comes into effect'),
           ('50% / 75%', 'Council quorum / decision majority'),
           ('2/3 : 1/3', 'weight of States : Centre in the Council'),
           ('₹20 lakh / ₹10 lakh', 'registration limit / special category States'),
           ('14% for 5 years', 'assumed growth for compensation, till 2022'),
           ('30% → 15%', 'RNR example: one-third versus two-thirds of GDP'),
           ('March 2013', 'GSTN incorporated, ₹10 crore capital'),
           ('01.04.2018', 'e-way bill for inter-State movement'),
           ('0, 5, 12, 18, 28', 'slabs in the handout (2022)')]
DRAW = ['Redraw the handout’s shirt diagram (page 3) with the five value-added figures (100, 100, 58, 48, 60) and the final price ₹550.',
        'Redraw the handout’s bills of transaction (page 5): old regime 320 + 32 and VAT regime 298 with ITC 22, then the GST chain at 20% (page 6).',
        'Write from memory: Council features (chair, quorum, decision, weights), the “Outside GST” list, and the order VAT, GSTN, Amendment, GST.']
