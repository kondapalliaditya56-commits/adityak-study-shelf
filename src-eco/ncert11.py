# -*- coding: utf-8 -*-
"""NCERT content for handout Ch 11 (GST), placed by handout section. Sources: Class XII Macroeconomics Ch 5 (Box 5.3,
5.1.2, deficit reduction), Class XI Indian Economic Development Ch 3 (tax reforms) and its glossary."""
SRC = 'NCERT'
def T(head, rows): return {'head': head, 'rows': rows}
NC = {
 '1': [dict(ref='Class XII Macroeconomics Ch 5, §5.1.2 Classification of Receipts',
   why='The handout explained indirect tax by who pays and who bears. NCERT gives its own sorting of the old tax list into two families. Use it to recognise the names in a question.',
   link='Handout section 1: “indirect tax: A pays, B bears”. NCERT lists which taxes belong to each family before GST.',
   blocks=[
    dict(h='Step 1 NCERT’s two families of tax', tbl=T(['Family', 'NCERT’s list', 'NCERT’s note'], [
         ['<b>Direct</b>', 'Personal income tax (on individuals); corporation tax (on firms)', 'Income tax is progressive: higher the income, higher the rate. Firms are taxed on a proportional basis'],
         ['<b>Direct, minor</b>', 'Wealth tax, gift tax, estate duty (now abolished)', 'Never brought in large revenue, so called “paper taxes”'],
         ['<b>Indirect</b>', 'Excise taxes (duties on goods produced within the country); customs duties (goods imported into and exported out of India); service tax', 'A footnote says GST, which covers both goods and services, was implemented by the Centre, 28 states and 7 Union territories from 1 July 2017']])),
    dict(h='Step 2 How NCERT says excise was shaped (before GST)', pts=['Necessities of life: exempted or taxed at low rates.', 'Comforts and semi-luxuries: moderately taxed.', 'Luxuries, tobacco and petroleum products: taxed heavily.']),
    dict(h='Step 3 One extra idea: the Finance Bill', pts=['The Finance Bill is presented along with the Annual Financial Statement. It gives the details of imposing, abolishing, remitting, altering or regulating the taxes proposed in the Budget.'])],
   d=['NCERT’s list of indirect taxes names only excise, customs and service tax. The handout also names sales tax/VAT, CST, entry tax and octroi (State and local levies). Use the handout’s longer list.'])],
 '2': [dict(ref='Class XII Macroeconomics Ch 5, Box 5.3 GST: One Nation, One Tax, One Market',
   why='NCERT explains cascading in three sentences, with no numbers. Read it as the short definition to write in an answer; the handout’s shirt example is the proof.',
   link='Handout’s ₹32 split: the ₹26.2 that was “tax on tax” is NCERT’s “taxes paid on intermediate goods” hidden inside the total value.',
   blocks=[
    dict(h='Step 1 What the pre-GST regime did', pts=['It imposed taxes not on the value added at each stage but on the <b>total value</b> of the commodity or service.', 'There was only a minimal facility of Input Tax Credit (ITC).', 'That total value included the taxes paid on intermediate goods and services. This amounted to <b>cascading of tax</b>.']),
    dict(h='Step 2 The same point as a comparison', tbl=T(['', 'Pre-GST regime (NCERT)', 'Under GST (NCERT)'], [
         ['Tax charged on', 'Total value, including taxes paid on intermediates', 'Value addition at each stage'],
         ['Credit for earlier tax', 'Minimal', 'Credit of tax paid at the previous stage is set off at the next stage'],
         ['Result', 'Cascading', 'Effectively a tax on value addition at each stage of supply']]))],
   d=[])],
 '3': [dict(ref='Class XII Macroeconomics Ch 5, Box 5.3 and Class XI Ch 3 (Tax reforms)',
   why='VAT started the idea of taxing only value added. NCERT says GST takes that idea to every good and service, which is why the handout calls GST “the wider application of VAT”.',
   link='Handout section 3: VAT 2005 and ITC. NCERT’s phrase for the next step: extend the principles of “value-added taxation” to all goods and services.',
   blocks=[
    dict(h='Step 1 NCERT’s account of ITC under GST', pts=['Under GST, tax is discharged at every stage of supply.', 'The credit of tax paid at the previous stage is available for set-off at the next stage of supply of goods and/or services.', 'So it is effectively a tax on value addition at each stage.']),
    dict(h='Step 2 Why NCERT says GST was needed', pts=['Our economy is large and fast growing, so GST aims to establish parity in taxation across the country and extend value-added taxation to all goods and services.', 'Class XI adds a second aim: reform of the indirect taxes, taxes levied on goods and services.'])],
   d=[])],
 '4': [dict(ref='Class XII Macroeconomics Ch 5, Box 5.3; Class XI glossary: Goods and Services Tax',
   why='This is the one NCERT box on GST. It repeats the handout’s definition in its own words, lists every tax that GST swallowed, and names the laws. Read the table of taxes: it is a favourite for statement questions.',
   link='Handout section 4: “one nation-one tax, destination-based, VAT-like”. NCERT uses almost the same three ideas.',
   blocks=[
    dict(h='Step 1 What GST is (NCERT)', pts=['The single comprehensive indirect tax, operational from 1 July 2017, on supply of goods and services, from the manufacturer or service provider to the consumer.', 'A destination based consumption tax with the facility of Input Tax Credit in the supply chain.', 'Applicable throughout the country with one rate for one type of goods or service.', 'It amalgamated a large number of Central and State taxes and cesses.']),
    dict(h='Step 2 Taxes that GST replaced (NCERT)', tbl=T(['Levied by', 'Taxes subsumed'], [
         ['Centre', 'Central Excise Duty, Service Tax, Central Sales Tax, cesses like KKC and SBC'],
         ['States', 'VAT/Sales Tax, Entry Tax, Luxury Tax, Octroi, Entertainment Tax, taxes on advertisements, taxes on lottery/betting/gambling, State cesses on goods']])),
    dict(h='Step 3 The laws behind it (NCERT)', pts=['CGST Act, UTGST Act and SGST Acts were enacted for GST.', 'Laws, procedures and rates of tax across the country are standardised.']),
    dict(h='Step 4 Class XI glossary says', pts=['A single indirect tax on the supply of goods and services, introduced in July 2017 by abolishing a variety of taxes such as sales tax and excise.', 'Tax is imposed on the basis of value addition at each stage of movement of goods and services.', 'Slabs of 0, 5, 12, 18 and 28 per cent on almost all goods and services; the slab is the same throughout the country.'])],
   d=['NCERT Box 5.3 says there are <b>six</b> standard rates: 0%, 3%, 5%, 12%, 18% and 28%. The Class XI glossary and the handout list <b>five</b> (no 3%). Use the handout’s five in class; if a question quotes the NCERT box, recognise the sixth rate.',
      'NCERT’s lists of replaced taxes do not mention customs. The handout is explicit that customs duty stays outside GST.'])],
 '5': [dict(ref='Class XII Macroeconomics Ch 5, Box 5.3 and footnote 1',
   why='NCERT tells the story of how GST became law: a constitutional amendment, then three kinds of Act, then a midnight launch. It does not mention the GST Council at all, so for the Council use the handout only.',
   link='Handout section 5: 101st Amendment Act 2016, Art. 246A. NCERT adds the three Acts and the launch session.',
   blocks=[
    dict(h='Step 1 The order of events (NCERT)', tbl=T(['When', 'What'], [
         ['8 September 2016', 'The 101st Constitution Amendment Act received the assent of the President'],
         ['After that', 'CGST Act, UTGST Act and SGST Acts were enacted'],
         ['Midnight of 30 June / 1 July 2017', 'GST rolled out during a special midnight session of Parliament']])),
    dict(h='Step 2 What Art. 246A does (NCERT)', pts=['It “cross empowers” Parliament and the Legislatures of States to make laws on GST imposed by the Union and the States.']),
    dict(h='Step 3 Who started on 1 July 2017 (NCERT footnote)', pts=['The Centre, 28 states and 7 Union territories.']),
    dict(h='Step 4 What NCERT calls it', pts=['“The biggest tax reform in the country since independence.”', 'Class XI Ch 3: expected to “generate additional revenue for the government, reduce tax evasion and create one nation, one tax and one market”.'])],
   d=['NCERT says the Amendment “received assent” on 8 September 2016; the handout says “notified” on 08.09.2016. Same date, different word. NCERT also misprints “101th” for 101st.'])],
 '6': [dict(ref='Class XII Macroeconomics Ch 5, Box 5.3',
   why='A short check of the “Outside GST” list. NCERT agrees with the handout on all three items and on tobacco.',
   link='Handout section 6: alcohol, five petroleum products, local entertainment tax outside; tobacco inside with extra Central excise.',
   blocks=[
    dict(h='What NCERT says', tbl=T(['Item', 'NCERT’s statement'], [
         ['Five petroleum products', 'Kept out of GST “for the time being”; with the passage of time they will get subsumed'],
         ['Alcoholic liquor for human consumption', 'State Governments will continue to levy VAT on it'],
         ['Tobacco and tobacco products', 'Attract both GST and Central Excise Duty']]))],
   d=['NCERT says petroleum “will get subsumed”; the handout says only that the Council will decide the date, and that it remains outside as of March 2022. Use the handout’s cautious wording.'])],
 '7': [dict(ref='Class XII Macroeconomics Ch 5, Box 5.3; Class XI Ch 3 (Tax reforms)',
   why='The handout’s benefits list is long. NCERT adds a few of its own claims, including one number (a rise in GDP). Read them as the “official promise” of GST.',
   link='Handout section 7, benefits: NCERT’s list overlaps heavily; the new items are marked below.',
   blocks=[
    dict(h='Step 1 NCERT’s benefits of GST', tbl=T(['Benefit', 'NCERT’s words (short)', 'In handout?'], [
         ['Simpler tax system', 'Simplified the multiplicity of taxes; laws, procedures and rates standardised', 'Yes'],
         ['One market', 'Freedom of movement of goods and services; a common market in the country', 'Yes'],
         ['Lower business cost', 'Reduced cost of business operations and cascading on consumers; reduced overall cost of production', 'Yes (cascading)'],
         ['Competitive products', 'Indian products and services more competitive in domestic and international markets', 'Partly (Make in India)'],
         ['<b>Growth</b>', 'GDP “expected to rise by about 2%”', '<b>New</b>'],
         ['Easy compliance', 'Registration, returns, payments online through one common portal www.gst.gov.in', 'Yes (GSTN)'],
         ['Wider base, transparency', 'Expanded the tax base; higher transparency; reduced human interface between taxpayer and government; ease of doing business', 'Yes'],
         ['Class XI: revenue, evasion', 'Expected to generate additional revenue and reduce tax evasion; procedures simplified and rates substantially lowered to encourage compliance', 'Partly']])),
    dict(h='Step 2 Two NCERT clues for the “single rate” debate', pts=['Class XII (deficit reduction): indirect taxes “are regressive in nature”, they impact all income groups equally.', 'Class XII (excise): necessities exempted or taxed low, comforts moderate, luxuries, tobacco and petroleum heavy. This is the same idea as the handout’s multiple slabs adding a progressive element.'])],
   d=['NCERT’s “about 2%” rise in GDP is an expectation, not a result. The handout gives no such number; quote it only as NCERT’s expectation.'])],
 '8': [dict(ref='Class XII Macroeconomics Ch 5, Box 5.3',
   why='One small NCERT point that fits the GSTN paragraph: the portal.',
   link='Handout GSTN: “a common pass-through portal for taxpayers”.',
   blocks=[dict(h='What NCERT adds', pts=['All tax-payment-related services (registration, returns, payments) are available online through a common portal, www.gst.gov.in.', 'This has reduced human interface between taxpayer and government and is furthering ease of doing business.'])],
   d=[])],
}
SRCFILES = ['leec105', 'keec103', 'keec1gl']
NCMAP = [('Class XII Ch 5, Box 5.3 GST: One Nation, One Tax, One Market', '2, 3, 4, 5, 6, 7, 8', 'Cascading in NCERT’s words; list of taxes replaced; Acts; launch; outside-GST items; benefits; the portal'),
         ('Class XII Ch 5, §5.1.2 Classification of receipts', '1, 7', 'Direct and indirect taxes; paper taxes; how excise was shaped; Finance Bill'),
         ('Class XII Ch 5, Deficit reduction paragraph', '7', 'Indirect taxes are regressive'),
         ('Class XI Ch 3, Tax reforms and glossary', '3, 4, 5, 7', 'GST aims; glossary definition and slabs')]
NCQ = [('What do you understand by G.S.T? How good is the system of G.S.T as compared to the old tax system? State its categories.',
        'Definition: section 4. Old system and cascading: sections 1-3. Benefits: section 7. Categories: CGST, SGST, IGST in section 4 (NCERT also names the UTGST Act)')]
NCKEY = ['Goods and Services Tax (GST)', 'Destination based consumption tax', 'Input Tax Credit (ITC)', 'Cascading of tax', 'Value addition at each stage', 'Direct and indirect taxes', 'Article 246A', 'CGST, UTGST and SGST Acts', 'Finance Bill']
NCONLY = [('Class XI Ch 3 Tax reforms (direct tax half)', 'Income tax and corporation tax cuts since 1991 and why moderate rates were thought to encourage savings and disclosure. Read in the Chapter 12 NCERT box (section 9).')]
