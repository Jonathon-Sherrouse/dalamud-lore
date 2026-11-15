# Atlas v2 discovery: quest inventory, threads and proposed arc map (NDL-006)

> **Arc-map decision (user, 2026-11-14): option 1, build A4 (*The Black Wolf's challenge*, #155–161) only, with an editorial cast of 10.** The cast cap counts participants, not the arc entry. A3 and the longer threads are deferred to the backlog.
>
> **Status: PROVISIONAL research, with the arc map decided.** This is `NDL-006`'s discovery step: the [v2 plan](v2-plan.md) requires it before the schema freezes. It is research input, not reviewed canon. The content story (`NDL-009`) researches and reviews the chosen arc in full.

## Method

- **Coverage.** Four parallel research lanes (Claude Haiku 5.5, high effort) read every main-scenario quest from *In the Company of Heroes* (MSQ #103) to *The Ultimate Weapon* (#161), plus the two parallel-path quests, *Acting the Part* and *Dressed for Conquest*. That is 59 quest pages, read as raw Console Games Wiki wikitext. Each lane reported every quest in a fixed format: story beat, who is present, what starts, ends or is revealed, and which story threads open, advance or resolve.
- **Quest order.** Taken from each page's `msq-index`, `prev-quest` and `next-quest` fields.
- **Lead verification:**
  - A script checked **633 quoted locators** against the saved source text: **628 match verbatim**. The 5 misses are a paraphrased item handover, a quote-style difference and link markup; none is used here.
  - Every passage cited below was re-checked by hand, including whether it sits outside optional dialogue and conditional branches. All are journal or main dialogue.
- **Optional and branch content.** Facts inside optional NPC dialogue or conditional branches (`> If …`) are flagged and kept out of the arc evidence.

## Quest inventory (A Realm Reborn 2.0, MSQ #103–161)

The `id-gt` value is the game's quest ID as the wiki records it. It is a candidate source for the Follow step's `gameQuestIds`, which `NDL-007` verifies against the client.

The second bundled milestone, `cp-arr-2-55`, uses *Before the Dawn* (MSQ index 241, level 50, patch 2.55, `id-gt` **65964**), the last 2.x main-scenario quest; its `next-quest` field lists only the 3.0 openers and side unlocks. Source: the same wiki's *Before the Dawn* page, fetched for `NDL-006`.

| # | Quest | MSQ index | Level | Game quest ID (wiki `id-gt`) | Thread notes |
|---|---|---|---|---|---|
| 1 | In the Company of Heroes | 103 | 33 | 66391 | pre-raid baseline (Titan) |
| 2 | As You Wish | 104 | 33 | 66392 |  |
| 3 | Lord of Crags | 105 | 34 | 66393 | Titan falls; Ascians and Garleans at the Navel |
| 4 | All Good Things | 106 | 34 | 66053 | **raid on the Waking Sands; Minfilia and others taken** |
| 5 | You Can't Take It with You | 107 | 35 | 69403 |  |
| 6 | Bringing out the Dead | 108 | 35 | 66412 |  |
| 7 | Bury Me Not on the Lone Prairie | 109 | 35 | 66414 |  |
| 8 | Eyes on Me | 110 | 35 | 66054 | Alphinaud returns, Cid found; Garuda thread opens |
| 9 | He Who Waited Behind | 111 | 36 | 66419 |  |
| 10 | Cold Reception | 112 | 36 | 66420 | Coerthas / Ishgard begins |
| 11 | The Unending War | 113 | 36 | 66422 |  |
| 12 | Men of Honor | 114 | 36 | 66423 |  |
| 13 | Three for Three | 115 | 36 | 66425 |  |
| 14 | The Rose and the Unicorn | 116 | 36 | 66426 |  |
| 15 | The Talk of Coerthas | 117 | 37 | 66433 |  |
| 16 | Road to Redemption | 118 | 38 | 66446 |  |
| 17 | Following the Evidence | 119 | 38 | 66447 |  |
| 18 | In the Eyes of Gods and Men | 120 | 38 | 66448 |  |
| 19 | The Final Flight of the Enterprise | 121 | 38 | 69404 |  |
| 20 | Ye of Little Faith | 122 | 39 | 66460 |  |
| 21 | Factual Folklore | 123 | 39 | 66463 |  |
| 22 | The Best Inventions | 124 | 39 | 69405 |  |
| 23 | Influencing Inquisitors | 125 | 40 | 66474 |  |
| 24 | By the Lights of Ishgard | 126 | 40 | 66475 |  |
| 25 | Blood for Blood | 127 | 40 | 66476 |  |
| 26 | The Heretic among Us | 128 | 40 | 66477 |  |
| 27 | In Pursuit of the Past | 129 | 41 | 66488 | Enterprise found; Lahabrea seen |
| 28 | Into the Eye of the Storm | 130 | 41 | 66489 |  |
| 29 | Sealed with Science | 131 | 41 | 66491 |  |
| 30 | With the Utmost Care | 132 | 41 | 66492 |  |
| 31 | A Promising Prospect | 133 | 41 | 66495 |  |
| 32 | It's Probably Not Pirates | 134 | 42 | 66496 |  |
| 33 | Representing the Representative | 135 | 42 | 66497 |  |
| 34 | The Reluctant Researcher | 136 | 42 | 66498 |  |
| 35 | Sweet Somethings | 137 | 42 | 66499 |  |
| 36 | History Repeating | 138 | 42 | 66503 |  |
| 37 | The Curious Case of Giggity | 139 | 43 | 69406 |  |
| 38 | Better Late than Never | 140 | 43 | 66511 |  |
| 39 | Lady of the Vortex | 141 | 44 | 66055 | **Garuda falls; the weapon absorbs the primals; Scions to reform** |
| 40 | Reclamation | 142 | 44 | 66056 | **captives' location revealed (Castrum Centri); rescue arc opens** |
| 41 | Casing the Castrum | 143 | 44 | 66514 | four prisoners sighted; Biggs and Wedge thread |
| 42 | Eyes on the Empire | 144 | 44 | 66516 |  |
| 43 | Footprints in the Snow | 145 | 44 | 66517 |  |
| 44 | Monumental Hopes | 146 | 44 | 66518 |  |
| 45 | Notorious Biggs | 147 | 44 | 66519 | Biggs and Wedge rejoin |
| 46 | Come-Into-My-Castrum | 148 | 44 | 66520 |  |
| 47 | Getting Even with Garlemald | 149 | 44 | 66522 | rescue plan set; the main story splits into two paths |
| 48 | Drowning Out the Voices | 150 | 46 | 66537 | path 1 of 2 (rejoins at 153) |
| 49 | Fool Me Twice (Quest) | 153 | 46 | 66540 | paths rejoin |
| 50 | Every Little Thing She Does Is Magitek | 154 | 46 | 66541 | last quest before the rescue |
| 51 | Escape from Castrum Centri | 155 | 46 | 66057 | **captives freed; Thancred's possession revealed; ultimatum** |
| 52 | The Black Wolf's Ultimatum | 156 | 46 | 66058 | leaders refuse; replica-crystal plan |
| 53 | Operation Archon | 157 | 49 | 70057 | counteroffensive opens; Rhitahtyn falls |
| 54 | A Hero in Need | 158 | 49 | 66573 |  |
| 55 | Hearts on Fire | 159 | 49 | 69408 |  |
| 56 | Rock the Castrum | 160 | 50 | 69409 | assault on Castrum Meridianum; Livia falls |
| 57 | The Ultimate Weapon | 161 | 50 | 70058 | **Thancred freed; Gaius and Ultima ended; milestone `cp-arr-2-0`** |
| — | Acting the Part | 150 | 46 | 66538 | path 2 of 2 (effectively required) |
| — | Dressed for Conquest | 151 | 46 | 69407 | path 2, continued (effectively required) |


**Parallel paths.**
- After *Getting Even with Garlemald* (#149), the main story offers two paths: *Drowning Out the Voices* (#150), and *Acting the Part* (#150) → *Dressed for Conquest* (#151). They rejoin at *Fool Me Twice* (#153). No quest has index #152.
- *Acting the Part* and *Dressed for Conquest* are effectively required: their emote and items are used in #153 and #155. The source doesn't say whether *Drowning Out the Voices* can be skipped.
- There is no other parallel main-scenario quest in the range; every other extra `next-quest` entry is a side or feature quest.

## Story threads

| Thread | Opens | Status along the way | Resolves | Span |
|---|---|---|---|---|
| **Captured Scions** | *All Good Things* (#106): the Waking Sands is raided and "Minfilia is among them" (journal) | Silent from #107 to #141. Ishgard even presumes the Scions dead. *Reclamation* (#142) reveals "your comrades are being held at Castrum Centri"; *Casing the Castrum* (#143) reports four prisoners "observed being led into Castrum Centri"; the rescue plan is set at #149 | *Escape from Castrum Centri* (#155): "Though the rescue mission was a success" (journal) | about 50 quests |
| **Coerthas, the *Enterprise* and Garuda** | *Eyes on Me* (#110): Alphinaud finds Cid and needs his airship; Garuda torments Coerthas | Ishgard and the heresy hunt (#112–128); the *Enterprise* is found (#129); the ice-crystal hunt (#133–140) | *Lady of the Vortex* (#141): Garuda falls, and the imperial weapon "dispatches and seemingly absorbs all three primals" (journal) | 32 quests |
| **Biggs and Wedge** | *Casing the Castrum* (#143) | Their trail (#144–146) | *Notorious Biggs* (#147) | 5 quests |
| **Thancred possessed by Lahabrea** | *Escape from Castrum Centri* (#155): "the shocking revelation that Thancred has been possessed by Lahabrea" (journal) | The replica-crystal plan (#156) | *The Ultimate Weapon* (#161): "free your comrade Thancred from his enthrallment" (journal) | 7 quests |
| **The Empire's weapon / Ultima** | *Lady of the Vortex* (#141) | Shown at #155; targeted by Operation Archon (#157–160) | *The Ultimate Weapon* (#161): "With Gaius van Baelsar slain, and the Ultima Weapon destroyed" (journal) | 21 quests |
| **Operation Archon** | *Operation Archon* (#157): "the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace" | Rhitahtyn falls (#157); Livia falls (#160) | #161 | 5 quests |
| Titan (pre-raid) | #103 | — | *Lord of Crags* (#105) | 3 quests, before the arcs |

## Proposed arc map

Arcs are editorial decisions backed by the threads above. They may overlap.

| Arc (working name; neutral names are an `NDL-009` content decision) | First quest | Last quest | Length | Overlaps | Fits the v2 caps? |
|---|---|---|---|---|---|
| **A1. After the raid** (the captives thread) | #106 *All Good Things* | #155 *Escape from Castrum Centri* | about 50 | Contains A2 and A3 | No. It also goes silent for 35 quests, so it reads as a long thread more than an arc. |
| **A2. Coerthas and the *Enterprise*** | #110 *Eyes on Me* | #141 *Lady of the Vortex* | 32 | Inside A1 | No |
| **A3. The rescue at Castrum Centri** | #142 *Reclamation* | #155 *Escape from Castrum Centri* | 14, including both parallel paths | Inside A1; shares #155 with A4 | No; just over (14 steps plus a baseline, against a cap of 10) |
| **A4. The Black Wolf's challenge** | #155 *Escape from Castrum Centri* | #161 *The Ultimate Weapon* | **7** | Shares #155 with A3 | **Yes**: a baseline (#154) plus 6 slice steps, with the arc ending at the `cp-arr-2-0` milestone |

### Options for the user (the plan says discovery stops here and the user decides)

1. **Recommended: build A4 only.**
   - **Fit:** 7 consecutive quests with no parallel paths. It fits every cap without raising anything.
   - **What it exercises:** a multi-quest relationship that starts and ends inside the arc (the possession), captives freed at the arc's first step ("Ended so far"), event participation (Operation Archon), and an arc that ends at a milestone, which is the trickiest boundary rule.
   - **Overlap** is proven with synthetic fixtures, as the plan allows.
   - **Cost:** the lowest. About 7 recaps plus baseline coverage.
2. **A3 + A4, overlapping in real content.**
   - **Fit:** about 20 slice steps (baseline #141, then #142–160 including both parallel paths). The plan's step cap would rise from 10 to about 20, and the schema's 16-checkpoint bound would need raising, for example to 32.
   - **What it adds:** it proves overlap in real content, and both arcs build quest by quest.
   - **Cost:** about 2.5× the content work. It also needs an ordering rule for the parallel paths, and Follow evidence that every player completes both (`NDL-007`).
3. **A3 + A4 using only the quests that change the chart.** It stays within 10 steps (for example #141, 142, 143, 149, 155–160), but A3 would jump instead of building quest by quest. It is cheaper than option 2, but weaker on the user's vision.

A1 and A2 are not proposed for v2. They become candidates for the later breadth stories.

### Cast-cap flag (a decision either way)

The real cast of A4 is larger than the 10-member cap. It includes Minfilia, Thancred, Alphinaud, Y'shtola, Yda, Papalymo, Urianger, Tataru, Cid, Gaius, Lahabrea, Livia, Nero, Rhitahtyn, the three Alliance leaders, Biggs and Wedge.

The plan says to flag this, never to trim silently. The proposal is an **editorial cast** that groups minor figures into organizations. An example of 10: Minfilia, Thancred, Alphinaud, Cid, the Scions (organization), Gaius, Lahabrea, Livia, the Eorzean Alliance (organization), and Operation Archon (event).

The alternative is a justified raise, for example to 14. Also to settle at the freeze: whether the cap counts the arc entry itself. The proposal is that it counts participants only.

## Worked examples (for the schema freeze)

Passages are short locators from the wiki's transcription of the journal or main dialogue, all outside optional dialogue and branches.

### WE-1: A relationship that starts and ends inside the arc, ending at a milestone
- **Relationship:** Thancred → *possessed by* → Lahabrea, `[#155, #161)`.
- **Start:** *Escape from Castrum Centri* (journal): "the shocking revelation that Thancred has been possessed by Lahabrea".
- **Context:** *The Black Wolf's Ultimatum*, in Minfilia's dialogue: Ascians "entrap and possess mortal men by means of malign artifacts known as Crystals of Darkness".
- **End:** *The Ultimate Weapon* (journal): "free your comrade Thancred from his enthrallment". Alphinaud also says "the Crystal that bound Thancred is no more". These become this relationship's `endCitations`, available at `cp-arr-2-0`.
- **Behavior:**
  - At #155–160, the Arc lens shows the edge as active. Per rule 2, it carries no "temporary" badge.
  - At #161 (the milestone), the Arc lens's "Ended so far" lists it, with no sources. The Changes lens does not, because it never compares across a slice → milestone boundary.
  - The recap at #160 must not hint at the ending; the recap at #161 must not read as a conclusion of the arc (rule 7).

### WE-2: Captives freed at the arc's first step (the baseline rule and "Ended so far")
- **Relationship:** Minfilia, Urianger, Papalymo and Tataru → *held captive at* → Castrum Centri, or by the Empire.
- **Known since #142:** *Reclamation* (journal) "the Scions taken prisoner by the Empire"; *Casing the Castrum* (journal) "were observed being led into Castrum Centri"; *Getting Even with Garlemald*, in Alphinaud's dialogue, "So Minfilia and the others are indeed at Castrum Centri!"
- **End:** *Escape from Castrum Centri* (journal) "Enter the tower via the steel gate, and set your friends free"; and "Though the rescue mission was a success".
- **Behavior:**
  - The baseline rule means the captivity is authored at the baseline step (#154), because the player already knows it.
  - At #155, the arc's first step, the Arc lens's "Ended so far" shows the captivity ending (from the step pair #154 → #155), and the recap explains the rescue.
  - This needs A4's `firstStep` to be #155 with #154 as the baseline. That's consistent with the rule that an arc never starts on the first timeline step.

### WE-3: Event participation and cast growth
- **Event:** *Operation Archon* (#157), "the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace" (journal).
- **Participants:** the Alliance, the Scions and the player's side. Each gets a `participant-in` edge from #157, which never ends.
- **Within it:**
  - Rhitahtyn falls at #157 ("you deal Rhitahtyn his death-blow"); his relationships end, but he stays in the cast.
  - Livia falls at #160 ("defeated Livia sas Junius into the bargain").
  - At #161, "With Gaius van Baelsar slain, and the Ultima Weapon destroyed".
- **Behavior:**
  - A mid-arc joiner whose existing relationships with the cast are already authored shows no false "New" rows.
  - #161 shows endings in the Arc lens only.

## What this confirms for the schema freeze

- **The model fits.** For the recommended option, one "after this quest" step per quest and a linear main-scenario timeline are enough. Option 2 would also need an **ordering rule for the parallel paths**: by MSQ index, then authored order, with every path required, subject to `NDL-007`.
- **Relationship vocabulary.** The likely new types are `participant-in`, *held captive at/by* and *possessed by*. That is three, at the cap. An *opposes* or *at war with* type for the Alliance and the Empire would be a fourth; `NDL-009` decides whether to raise the cap by one or express it another way.
- **Spoiler notes for content:**
  - **Surnames:** first names only. Cid's surname appears in source lines and in the company name "Garlond Ironworks", so `NDL-009` decides whether the company name is shown.
  - **Fine to use:** "Warrior of Light", used in game from #156, is not a spoiler.
  - **Not to use in recaps:** the post-battle cutscene at #161 names further Ascians and says "Bahamut stirs". Those set up later content.
- **Game quest IDs** are available for every step from the wiki (`id-gt`), for `NDL-007` to verify.

## Decisions (user, 2026-11-14)

1. **The arc:** option 1, A4 only (#155–161). Overlap is proven with synthetic fixtures.
2. **The cast:** editorial, at most 10 participants, with organizations grouping minor figures. The arc entry doesn't count toward the cap. The exact 10 are an `NDL-009` content decision; the example above is the starting point.
3. **"Garlond Ironworks":** left to `NDL-009`.
