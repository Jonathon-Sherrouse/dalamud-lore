# NDL-012: A Realm Reborn 2.0 before the Black Wolf (MSQ #102–#154)

> **Status: researched and authored; awaiting your content review.** Every new record in `atlas.json` is `pending` until you accept it. The review sheet ([content-review.md](content-review.md)) shows every record exactly as the Atlas will display it, with its evidence. The claims table ([content-claims.md](content-claims.md)) lists every locator.

## Scope (user decision, 2026-11-17)

You asked for "a lot more story research to populate the Atlas" and picked **the rest of ARR 2.0**: work backward from the accepted Black Wolf arc (#155–161) through the raid on the Waking Sands, Coerthas and the *Enterprise*, Garuda, and the rescue preparations. You accepted that this needs the 16-step bound raised.

Result:

| | Before | After |
|---|---|---|
| Story points | 9 (#154–160 + 2 milestones) | **61** (#102–160 + 2 milestones) |
| Arcs | 1 | **6** |
| Entities | 19 | **44** |
| Relationships | 33 | **105** |
| Claims (verbatim locators) | 103 | **285** |
| `atlas.json` | 114 KB | about 360 KB (cap 1 MiB) |

## Method

- **Six parallel research lanes** (Claude Haiku 5.5, one per run of about 10 quests) fetched the raw Console Games Wiki wikitext for every main-scenario quest from MSQ #100 to #155, both parallel #150 paths included, and saved each page. Each lane reported every quest in a fixed format: who is present, the beat, 4–10 facts with a verbatim quote and its section, open threads, spoiler notes, and the optional or conditional lines it deliberately left out.
- **Lead verification.** A script checked all **410 lane quotes** against the saved pages: all matched verbatim. The lead then wrote the content from those reports, drafting 182 new claims in its own words, each with a locator. The same script checked all **182 locators**: every fragment matches its page exactly.
- **Only journal, steps and main dialogue are evidence.** Optional NPC dialogue and conditional branches (`> If …`) were flagged by the lanes and left out.
- **No memory of the game was used.** Where a page doesn't say something, the Atlas doesn't either (for example, nothing says where Thancred is between #106 and #154, so his entry adds nothing there).

The raw pages and lane reports were working files, not committed (they are wiki text).

## Quest inventory added

Each step means "after this quest". The `id-gt` game quest IDs come from each page's infobox, for Follow (deferred).

| Step | MSQ # | Quest | id-gt | Arc |
|---|---|---|---|---|
| `cp-msq-102` | 102 | It Was a Very Good Year | 66386 | baseline (first step) |
| `cp-msq-103`–`105` | 103–105 | In the Company of Heroes · As You Wish · Lord of Crags | 66391 · 66392 · 66393 | B1 |
| `cp-msq-106`–`110` | 106–110 | All Good Things · You Can't Take It with You · Bringing out the Dead · Bury Me Not on the Lone Prairie · Eyes on Me | 66053 · 69403 · 66412 · 66414 · 66054 | B2 (#110 shared with B3) |
| `cp-msq-111`–`129` | 111–129 | He Who Waited Behind … In Pursuit of the Past | see `atlas.json` | B3 |
| `cp-msq-130`–`141` | 130–141 | Into the Eye of the Storm … Lady of the Vortex | see `atlas.json` | B4 |
| `cp-msq-142`–`149` | 142–149 | Reclamation … Getting Even with Garlemald | see `atlas.json` | B5 |
| `cp-msq-150` | 150 | Drowning Out the Voices (path 1) | 66537 | B5 |
| `cp-msq-150b` | 150 | Acting the Part (path 2) | 66538 | B5 |
| `cp-msq-151` | 151 | Dressed for Conquest (path 2) | 69407 | B5 |
| `cp-msq-153` | 153 | Fool Me Twice (paths rejoin; there is no #152) | 66540 | B5 |
| `cp-msq-154`… | 154–161 | unchanged (A4 and the 2.0 milestone) | | B5 ends at #154; A4 |

The full list, with labels and IDs, is pinned in `RealDataTests.Real_HasExactlyTheApprovedCheckpoints`.

**Parallel paths.** *Fool Me Twice* lists both *Drowning Out the Voices* and *Dressed for Conquest* as its prerequisites, so both paths are required, in either order. The timeline orders them by MSQ index, then authored order: Drowning Out the Voices, then Acting the Part, then Dressed for Conquest. Acting the Part is marked not contiguous with the step before it, so Changes labels it "Changes since …" rather than "What this quest changed". A player who did Acting the Part first and picks "After Acting the Part" also sees Drowning Out the Voices' small beat (Cid's jamming device). That's the known cost of a linear timeline.

## Arc map

Arcs are editorial, backed by the threads the lanes reported. They must not hide each other: the Arc lens picks the earliest-started arc that contains the view, so a long "umbrella" arc (the captives' thread, #106–155) would swallow every arc inside it. That thread is carried by relationships instead (Minfilia *prisoner of* Livia from #106, *held at* Castrum Centri from #142).

| Arc | Steps | Why these boundaries | Cast (at most 10) |
|---|---|---|---|
| **B1 The Road to Titan** | #103–105 | Opens when the Company of Heroes judges you worthy (E103b) and ends with Titan's fall and the first sight of Lahabrea (E105c, E105e). The Titan storyline starts before #102, which the Atlas doesn't cover. | Y'shtola, the Company of Heroes, Titan, Rhitahtyn, Lahabrea, the Garlean Empire (6) |
| **B2 The Fall of the Waking Sands** | #106–110 | The raid (E106b) through the church's sanctuary, ending when Alphinaud names Marques as Cid (E110c). | Minfilia, the Scions, the Waking Sands, Livia, the Empire, Noraxia, Iliud, Marques, then Alphinaud and Cid at #110 (10) |
| **B3 The Search for the Enterprise** | #110–129 | Opens when the Scions need Cid's airship to reach Garuda (E110e), through Ishgard's heresy crisis, ending when the ship is found (E129d). **Shares #110 with B2**, which proves overlapping arcs in real content. | Alphinaud, Cid, Garuda, the Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont, Lahabrea (10) |
| **B4 Garuda's Barrier** | #130–141 | The corrupted-crystal hunt (E130b) through Garuda's fall and the Empire's weapon (K11), ending as the Scions resolve to re-form (E141f). | Cid, Alphinaud, Garuda, then the Ixal, Titan, Gaius, the Empire and the Scions at #141 (8) |
| **B5 The Road to Castrum Centri** | #142–154 | Rebuilding the Scions and finding the captives (E142d), Biggs and Wedge, and the infiltration preparations, ending when the armor works (K09). | Alphinaud, Cid, Yda, Y'shtola, Minfilia, the Scions, Castrum Centri, Biggs, Wedge, Glaumunt (10) |

Default arc by step: none at #102; B1 at #103–105; B2 at #106–110; B3 at #111–129; B4 at #130–141; B5 at #142–154; A4 from #155, unchanged. Pinned in `ArcArr20Tests.TheDefaultArcFollowsTheStory`.

## Worked examples

Each is pinned in `ArcArr20Tests.NewAndEndedMatchTheWorkedExamples`.

- **WE-4: captivity begins (B2 at #106).** "New" shows Minfilia *prisoner of* Livia, Livia *member of* the Empire, and Iliud *aids* the Scions. Minfilia *leads* the Scions and the Scions' headquarters were already known at the baseline, so they are not new (baseline rule).
- **WE-5: a reveal as a relationship (B2 at #110).** "New" shows Marques *revealed as* Cid, and Alphinaud *member of* the Scions.
- **WE-6: an antagonist's opposition ends inside an arc (B3).** The false Guillaime *opposes* Alphinaud from #122 and ends at #128, when you defeat him. "Ended so far" lists it from #128. Changes at #128 shows it with its end evidence (*The Heretic among Us*).
- **WE-7: the rescue ends five relationships at once (A4 at #155).** Minfilia *prisoner of* Livia (accepted) and four NDL-012 *held at* Castrum Centri edges all end at #155, with the same end evidence. The four aren't in A4's cast, so the accepted Arc lens rows are unchanged.

## Decisions to review

These are lead decisions. Each is in the review sheet; flag any you want changed.

1. **The step bound rises from 16 to 128** (`AtlasLoader.MaxCheckpoints`). Coverage needs 61 steps; 128 leaves room for the 2.x patches. Entities (44/64) and relationships (105/256) stay under their bounds, and the file is about a third of the 1 MiB cap.
2. **Marques is his own entry.** Cid's approved portrait shows his later look, so showing it on "Marques" (#106–109) would give away who he is. Marques has no portrait. From #110 he is *revealed as* Cid, and Cid carries "Marques" as an alias.
3. **B5 stops at #154**, so the accepted Black Wolf's Challenge stays the default arc at #155. The alternative, ending B5 at #155 where the rescue happens, would make the rescue arc the default there and change an accepted behavior.
4. **Arc names avoid later quest titles**, which may not appear before their step (spoiler rule): B1 is not "Lord of Crags", and B4 is not "Lady of the Vortex". Garuda gains the alias "the Lady of the Vortex" only from #141.
5. **"Feast", not "banquet"**, for the Company of Heroes' test (#102–103). "Banquet" is reserved for the 2.55 story by the existing leak test.
6. **Left out of displayed text:** Nero (NDL-009 decision 9; he appears at #105 and #143, so the text says "imperial officers"), and every surname, as before.
7. **The false Guillaime** is named "Guillaime" until #126, when the corpse proves him an impostor, then "The false Guillaime", with "Guillaime" kept as an alias.
8. **Six new relationship types:** *aids*, *opposes*, *summoned by*, *allied with* (symmetric), *revealed as* / *formerly known as*, and *held at* / *holds*.
9. **Pilot entries visible earlier.** Y'shtola, Urianger, Tataru, the Waking Sands, and Minfilia, Thancred, Alphinaud and the Scions now start at #102 (Cid, Gaius, Livia and Lahabrea from their first appearance), with fresh text for each era. Their accepted records are unchanged; the new records end where the accepted ones begin. Where nothing changes before #154, the new text repeats the accepted #154 text, so Changes shows no false "description updated" at #154. Alisaie and Louisoix still start at 2.0: they don't appear in #102–154.
10. **New entries keep their last text through the milestones** (v2 plan, baseline rule). For example, Titan's entry at 2.55 still describes the Howling Eye. It is out of date, but it never adds later knowledge.
11. **No portraits for the 25 new entries yet.** They keep their category shapes. Picking portraits is a separate step, like `NDL-011`.

## What this changes for players

- The "Viewing as of" picker now lists 61 points. A fresh install starts at the earliest one, "After It Was a Very Good Year", which shows nothing past the Company of Heroes' invitation.
- Saved settings survive: every existing checkpoint ID is unchanged.
- The milestone snapshots (2.0, 2.55) gain the new entries in the Story point lens. The accepted A4 Arc lens and its rows are unchanged, except that its Changes rows at #155 and #160 now also list the new held-at and membership endings.
