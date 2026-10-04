# -*- coding: utf-8 -*-
from lib import *
import ch01, ch02

CH = {'n': 0, 'title': 'Start Here: How to Use This Notebook',
      'sub': 'What the notebook is, how IR is asked, the box colours, the lecture map, the PYQ and priority map, and how to revise',
      'badge': 'Read first', 'slides': True}

MASTER = [
    # chapter, teacher's marking, Prelims years quoted, Mains years quoted, where to spend time
    ['**1 · Introduction to World Geopolitics and India’s Foreign Policy**', 'Slide 3 (PPT-1) puts four 2026 questions on screen; the slides’ “Core idea”, “Key lesson”, “Essence of the phase” and “Central thread: strategic autonomy” lines', 'none quoted in the material', '2026 (four questions on slide 3: IPMDA, BRICS, diaspora, BRI), 2025, 2020, 2019', '**First.** The six-phase story, ten determinants, six periods, five trade-offs'],
    ['**2 · Major Powers and Their Relationship with India**', 'Slides’ “Core idea” lines on the US, US-China, Russia-West and India’s approach; “India seeks / India avoids”; Three Mutuals', 'none quoted in the material', '2026, 2024, 2023, 2021, 2020 (two), 2019 (two), 2018, 2017', '**Second.** All ten PYQs on the handout’s last page; China, US and Russia first, EU, France, Japan, Australia afterwards'],
    ['3 onwards', 'Pending: classes still going on', 'pending', 'pending', 'Add each chapter as the class finishes'],
]

ALLPYQ = [
    ('2026', 'Q9 · 10m · 150w', 'IPMDA, SAGAR and the Quad', 'Chapter 1 (slide 3)'),
    ('2026', 'Q10 · 10m · 150w', 'BRICS as a counterweight; alternative to other groupings', 'Chapter 1 (slide 3)'),
    ('2026', 'Q19 · 15m · 250w', 'Diaspora as a living bridge and strategic leverage', 'Chapter 1 (slide 3)'),
    ('2026', 'Q20 · 15m · 250w', 'BRI and South Asia as a theatre of great-power competition', 'Chapters 1 and 2'),
    ('2025', '10m · 150w', 'Sovereign nationalism after the waning of globalisation', 'Chapter 1'),
    ('2024', '10m · 150w', 'The West fostering India as an alternative to China', 'Chapter 2'),
    ('2023', '15m · 250w', 'NATO expansion and US-Europe partnership: good for India?', 'Chapter 2'),
    ('2021', '15m · 250w', 'AUKUS and existing Indo-Pacific partnerships', 'Chapter 2 (thin notes)'),
    ('2020', '15m · 250w', 'Indo-US versus Indo-Russian defence deals', 'Chapter 2'),
    ('2020', '15m · 250w', 'Quad: military alliance to trade bloc?', 'Chapters 1 and 2'),
    ('2019', '15m · 250w', 'Friction in India-US ties', 'Chapter 2'),
    ('2019', '15m · 250w', 'India as a leader of the oppressed and marginalised', 'Chapter 1'),
    ('2019', '10m · 150w', 'India-Japan global and strategic partnership', 'Chapter 2'),
    ('2018', '15m · 250w', 'US-Iran nuclear pact and India', 'Chapter 2 (thin notes)'),
    ('2017', '10m · 150w', 'China’s trade surplus and military power', 'Chapter 2'),
]


def build():
    secs = []
    secs.append(Sec('What this notebook is', [
        p('This is a **private study notebook for GS-2 International Relations**, built **only** from the Sarrthi IAS GS Mains Module material you gave: the class slides (PPT-1, PPT-2, PPT-3) and the handouts (Chapter 1 and Chapter 2). Every fact, date, name and number comes from those files. No outside facts are added.'),
        p('Each chapter has the same shape: an **Exam lens** (priority, PYQs quoted in the material, what to prepare), the notes in the handout’s order with the slides’ stress beside the facts, a **mind map**, a **timeline**, **traps**, **connects to**, a **recall sheet**, a **revision schedule**, and a **practice** section (quiz, flashcards and Mains answer skeletons).'),
        callout('key', 'Built so you can keep adding', 'Classes are still going on. Chapters 1 and 2 are done. When a new chapter finishes, send the handout and slides and it will be added as Chapter 3 with the same layout. This page and the Contents page will update.'),
        callout('source', 'Copyright', 'Notes are personal study notes. Copyright for the material belongs to the teacher and institute. Keep this notebook private.'),
    ], label='Notebook'))

    secs.append(Sec('IR in the GS-2 paper and how it is asked', [
        tbl('Syllabus lines (slide 2, PPT-1)', ['Syllabus line'], [
            ['India and its neighbourhood: relations'],
            ['Bilateral, regional and global groupings and agreements involving India and/or affecting India’s interests'],
            ['Effect of policies and politics of developed and developing countries on India’s interests'],
            ['Indian diaspora'],
            ['Important international institutions, agencies and fora: their structure, mandate'],
        ]),
        tbl('Weightage (slide 3, PPT-1)', ['Question', 'Marks', 'Words'], [
            ['Q9 and Q10', '10 each', '150'],
            ['Q19 and Q20', '15 each', '250'],
        ], desc='Every year, **4 questions carrying 50 marks** come from IR. The slide says this placement and marks distribution have been consistent over the years.'),
        tbl('The four 2026 questions on slide 3', ['No.', 'Statement, in short', 'Where it is covered'], [
            ['Q9 · 10m', 'IPMDA bridges the gap between India’s SAGAR vision and the Quad’s collective Indo-Pacific strategy. Critically assess, focusing on IPMDA', 'Chapter 1 (partial); IPMDA itself is not in the notes'],
            ['Q10 · 10m', 'BRICS as a powerful counterweight, amplifying the Global South. Role of BRICS in projecting itself as an alternative to other groupings', 'Chapters 1 and 2'],
            ['Q19 · 15m', 'India’s diaspora as a living bridge, economic factor and knowledge network, turning cultural heritage into strategic leverage. Critically examine', 'Chapter 1 (determinant 9) and Chapter 2 (US diaspora)'],
            ['Q20 · 15m', 'BRI has turned South Asia into a theatre of great-power competition. Strategic implications for India’s security and regional influence', 'Chapter 2'],
        ]),
        teacher('Class slide stress: how the nature of IR questions has changed (slide 4)', '**From bilateral relations to India’s place in the global order:** questions now start from the global context, not from single-country relations. **Statement-based questions that require critical evaluation:** they open with an assertive claim that must be **tested, not endorsed**. Examples on the slide, 2026: BRI turning South Asia into a theatre; BRICS as a “powerful counterweight”; the diaspora as “strategic leverage”.'),
        flow('The teacher’s approach to IR (slide 5)', [
            ('1 · Questions are broader now', 'themes asked in a wider context', ''),
            ('2 · Big picture first', 'how the world order evolved (Chapter 1)', ''),
            ('3 · Major powers before bilaterals', 'what US, China and Russia want (Chapter 2)', ''),
            ('4 · Bilaterals follow', 'within the bigger picture', ''),
            ('5 · The outcome', 'place any theme in its wider context', 'good')]),
        callout('example', 'A repeatable answer shape (built from slides 4 and 5)', '- Open with the **global setting** (one sentence from Chapter 1).\n- **Test the claim**: where it holds, where it does not.\n- Give **examples** (the notes give one for most points).\n- Close with India’s frame: **strategic autonomy, multi-alignment, issue-based partnerships**.'),
    ], label='Class slides'))

    secs.append(Sec('The box colours', [
        p('The same boxes are used in every chapter.'),
        callout('teacher', 'Class slide stress (orange)', 'What the teacher’s slides stress: “Core idea”, “Key lesson”, “Essence”, the PYQs on the screen. **The IR decks are typed: there is no handwriting, underlining or board ink**, so “teacher stressed” here means what the slide itself highlights.'),
        callout('alert', 'Handout alert (red)', 'A date or fact where the slides and the handout differ, or a thing the handout names without explaining. Each ends with a rule for the exam hall.'),
        callout('key', 'Key idea (green)', 'The line to remember: a definition, a conclusion or a closing idea.'),
        callout('example', 'Example (blue)', 'A quote, example or ready-made shape for an answer.'),
        callout('source', 'Source note (grey)', 'Where the section comes from: Class + handout, or **Handout only** (no slides yet).'),
        callout('mnemo', 'Memory aid', 'A memory aid built from the material’s own words, never from outside facts.'),
    ], label='Notebook'))

    secs.append(Sec('Priority and PYQ map', [
        callout('source', 'How this table was built', 'From the material only: the handouts’ PYQ pages and the slides’ own PYQ and “core idea” markings. The material quotes **no Prelims PYQs** for IR (this is the Mains module). The Mains years are “years quoted”, not a count of distinct questions. Chapters that are not built yet show “pending”.'),
        tbl('Priority map', ['Chapter', 'Teacher’s marking', 'Prelims years quoted', 'Mains years quoted', 'Where to spend time'], MASTER),
        tbl('All Mains PYQs quoted so far (15 questions)', ['Year', 'Marks and words', 'Topic', 'Notes in'], [list(x) for x in ALLPYQ],
            desc='Every question in the table is a statement or “discuss” type. Chapter pages give each one a skeleton in their Practice section.'),
        alert('Handout alert: three gaps flagged', '**IPMDA** (2026 Q9), **AUKUS** (2021) and the **US-Iran nuclear pact** (2018) are asked in PYQs but have **thin or no notes** in the material. Their skeletons say so. Add details from your class notes.'),
    ], label='Notebook'))

    secs.append(Sec('Which lecture covers which chapter', [
        tbl('Lecture-to-chapter map', ['Upload', 'Material', 'Goes to', 'Notes'], [
            ['PPT-1 (24 slides)', 'Class slides: syllabus, weightage, 2026 questions, six phases of the global order', 'Chapter 1, sections 1-7', 'Slide 1 is a title slide'],
            ['PPT-2 (23 slides)', 'Class slides: India’s foreign policy: goals, determinants, six periods, trade-offs, challenges, key ideas', 'Chapter 1, sections 8-10', 'Slides stop before the instruments section'],
            ['Handout “GS-2 IR - 12” (24 pages)', 'Chapter 1 handout', 'Chapter 1', 'The upload label “12” is the handout for Chapter 1'],
            ['PPT-3 (37 slides)', 'Class slides: major powers, US-China, Russia-West, India with China, US, Russia', 'Chapter 2, sections 1-17', 'Slides 1 and 37 carry no text'],
            ['Handout “GS-2 IR - 3” (28 pages)', 'Chapter 2 handout', 'Chapter 2', 'The upload label “3” is Chapter 2. Includes the EU, France, Japan, Australia'],
        ]),
        callout('source', 'Handout only (no class slides yet)', '- Chapter 1, section 11: Instruments of India’s contemporary foreign policy.\n- Chapter 2, sections 18-21: the EU, France, Japan, Australia.\n- Parts of earlier tables (a few phases of India-US and India-Russia) that the handout adds beyond the slides are marked “handout only”.'),
        callout('source', 'Missing lectures', 'No lecture is missing between PPT-1, PPT-2 and PPT-3. Later chapters are not uploaded yet: they will follow as the classes finish.'),
    ], label='Notebook'))

    secs.append(Sec('Tools inside the notebook and a revision plan', [
        tbl('Tools in every chapter', ['Tool', 'What it does'], [
            ['Exam lens', 'Priority, PYQs quoted, what to prepare'],
            ['Mind map and Outline', 'One-screen view of the chapter; use Outline on a phone'],
            ['Timeline', 'Dates, with high-yield dates starred'],
            ['Traps', 'Common mix-ups, each with a rule for the exam hall'],
            ['Recall sheet and Revise', 'Read once, hide, rebuild; spaced schedule and blank-page prompts'],
            ['Practice', 'Quick quiz, flashcards (tap to flip) and Mains answer skeletons'],
            ['Search', 'Finds any word across chapters; links to the exact section'],
            ['Done box and Aa', 'Mark a chapter done; change text size, width and theme'],
        ]),
        tbl('Spaced revision plan (counted from the day you finish a chapter)', ['Day', 'What to do', 'Time'], [
            ['Day 0', 'Read the Exam lens and the notes once; mark the chapter done', 'As needed'],
            ['Day +1', 'Recall sheet: read once, hide, rebuild', '15 min'],
            ['Day +3', 'Flashcards (missed ones only)', '15 min'],
            ['Day +7', 'Quick quiz; fix every miss against the Traps', '20 min'],
            ['Day +21', 'Write two Mains answers from the skeletons, from memory', '40 min'],
            ['Day +45', 'Blank-page test: draw the chapter map and the timeline from memory', '30 min'],
        ]),
        callout('key', 'One line for the whole notebook', 'India’s central thread is **strategic autonomy**: partnering widely, aligning selectively and depending permanently on none.'),
    ], label='Notebook'))
    return secs
