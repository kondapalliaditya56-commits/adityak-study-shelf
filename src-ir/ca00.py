# -*- coding: utf-8 -*-
"""Start-here live layer: where the current-affairs items live, plus items that have no chapter yet."""
from lib import *

AUG = 'Aug 2026 CA'
JUL = 'Jul 2026 CA'

MAP_ROWS = [
    ['US tariffs (50% to 18%), India-US trade report', 'Ch. 1 Phase 5 and Instruments; Ch. 2 US, India-US sections'],
    ['MJDA (Saudi-Türkiye-Pakistan)', 'Ch. 1 Phase 6; Ch. 2 India’s approach'],
    ['Hormuz, Bab el-Mandeb, Chabahar', 'Ch. 1 Phase 6 and determinants'],
    ['ICC withdrawals, UAE exits OPEC', 'Ch. 1 Phase 5 and 6'],
    ['Cultural diplomacy, polar report, UNSC campaign, BRICS', 'Ch. 1 Instruments'],
    ['Australia, Japan, Indonesia summits', 'Ch. 1 Trade-offs and Instruments; Ch. 2 Japan and Australia'],
    ['UK CETA, NZ FTA, SACU PTA, Israel BIA', 'Ch. 1 Instruments; Ch. 2 India-US management'],
    ['25th SR talks, Modi-Xi (12 Sep), water disputes, Scarborough', 'Ch. 2 India-China, US-China'],
    ['Nord Stream, Odesa, Kurils, Europe’s missile coalition', 'Ch. 2 Russia sections'],
    ['Iceland and the EU, Ceuta, North Macedonia and Moldova visits', 'Ch. 2 India-EU'],
    ['Farakka treaty, Mecca pact and Bangladesh, Lipulekh, Nepal flood, cross-border trains, Chabahar strike, Favara-UPI', 'Ch. 3, under each neighbour'],
    ['New Zealand, UNCITRAL, Sudan and South Sudan, Passport Index', 'Parked below until their chapters arrive'],
]


def radar():
    return [
        p('International Relations changes every month. Each chapter has a **Live radar** section and a red **In the news** card inside the sections it feeds. All items come from the **July and August 2026 current-affairs magazines** in your Project; two web items (the 12 Sep 2026 Modi-Xi meeting and the 13 Sep 2026 Hormuz routes) are marked.'),
        tbl('Where each current-affairs item lives', ['Item', 'Where to read it'], MAP_ROWS),
        h3('Parking lot: news with no chapter yet'),
        live(JUL, 'New Zealand: first Indian PM visit in 40 years, FTA and a Strategic Partnership',
             'An **India-NZ FTA** was signed in **April 2026** (about nine months of talks). In July the ties became a **Strategic Partnership with a Roadmap to 2030**; trade target **NZ$7 billion by 2030**. **NZ joined the maritime-security pillar of India’s IPOI**; the two signed a **Mutual Logistics Support Arrangement** and a hydrography arrangement.',
             'A “trade first, strategy second” case. Honest caveats for Mains: the Roadmap is **non-binding**, NZ’s **dairy** exports clash with India’s smallholders, and NZ’s military scale is small.',
             '**Realm of New Zealand**: NZ, Cook Islands, Niue, Tokelau, Ross Dependency. **Zealandia**: submerged landmass in the south-west Pacific. NZ is a **Five Eyes** member.',
             why_label='What happened', src='Jul 2026 CA §3.5.'),
        live(JUL, 'UNCITRAL at 60, hosted in New Delhi',
             'India hosted the conference marking the **60th anniversary of UNCITRAL** (founded **1966**). India has been a **member since 1966**, one of only **eight countries with uninterrupted membership**.',
             'A soft-power and rule-making example: India as a host of international trade-law reform.',
             '**UNCITRAL**: UNGA body, 70 members elected for six-year terms, secretariat in **Vienna**. Instruments: 1985 arbitration model law → India’s Arbitration and Conciliation Act 1996; 1996 e-commerce model law → IT Act 2000; **Singapore Convention (2019)** → India signed; Mediation Act 2023. India is **not a party** to the Vienna Sales Convention (1980).',
             src='Jul 2026 CA §3.8.1.'),
        live_quick('Jul-Aug 2026', [
            '**South Sudan:** India condemned an attack on **UNMISS** peacekeepers in Jonglei State. Landlocked; capital **Juba**; civil conflict since **2013**; the **Sudd** is one of the world’s largest wetlands.',
            '**Sudan:** the RSF committed crimes against humanity and ethnic cleansing in **El Fasher** (capital of North Darfur), per Amnesty International.',
            '**Global Passport Index:** India fell to **125th**; top is **Sweden**. Different from the **Henley** index (visa-free destinations). Published by Global Citizen Solutions.',
            '**Zanzibar:** first-ever **IIT campus outside India** (IIT Madras).',
        ], src='Aug 2026 CA §3.9.4; Jul 2026 CA conflict areas, §3.9.3, high-level visits.'),
        callout('note', 'How to use the radar', 'Once a week: open the chapter’s **Live radar**, read the table, then retell the five-headline chain without looking. When a new magazine arrives, send it and the new items get filed under the section they prove.'),
    ]
