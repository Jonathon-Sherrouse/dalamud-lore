# Atlas discovery evidence matrix (NDL-002)

> **Status: PROVISIONAL / UNREVIEWED.** Discovery research input for the [Lore Relationship Atlas](../lore-relationship-atlas.md) pilot. This is not accepted canon, it is never packaged, and nothing here is human-reviewed. `NDL-003` completes and reviews the dataset; this file only shows that the fixed pilot can be sourced and gives the schema freeze something to work from.

Researched 2026-11-14. Four parallel research lanes covered the checkpoint anchors, the roster, relationships, and citation safety. The lead reconciled their reports and checked every claim marked **V** against wikitext fetched from the Console Games Wiki MediaWiki API. Rows marked **R** are lane-reported and not yet lead-verified. All passages are fan transcriptions of in-game text. No official Square Enix source could be verified (see [Open questions](#open-questions)).

Worked examples: [worked-examples.md](worked-examples.md).

## Evidence rules adopted in discovery

1. **Available-content rule** (user decision, 2026-11-14). A fact counts as player knowledge at a checkpoint when it is shown in either of these:
   - required main-scenario content through that checkpoint's terminal quest; or
   - optional content (wiki `type = feature`, e.g. the Binding Coil quests) that is **both** doable at that story point, because its whole unlock chain is satisfiable by main-scenario progress through the checkpoint plus other eligible optional content, **and** released in or before the checkpoint's patch.

   Optional content released later is not counted early, even if today's game lets the player reach it sooner. The Binding Coil story is the deciding case: the whole chain through 2.4 is gated only by *The Ultimate Weapon*, so without the release-patch condition it would all land at 2.0. Every optional source must record its verified unlock chain; see WE-3.
2. **Occurred vs. learned.** Every claim records the patch in which the player is shown it, not when it happened in-universe.
3. **Intervals snap to checkpoints.** Relationship bounds are checkpoint IDs. A fact that begins *and* ends between two checkpoints (for example the 2.1–2.55 Rising Stones headquarters) cannot be an edge. It appears only in the later snapshot's description.
4. **First names only.** No surname (Warde, Waters, Rhul, Augurelt, Leveilleur, Taru, Totolymo, Hext) or birth name (Ascilia) appears in display text or citation URLs. None was verified in displayed 2.0 text, and the wiki's surname sources (Encyclopaedia Eorzea, The Unending Codex 6.1) are not per-checkpoint evidence. Leveilleur does appear plainly at 2.4 ("Commander Leveilleur"), but the pilot gains nothing from it.
5. **Cite the quest, not the character page.** Character pages carry post-2.55 content. Quest pages are the citation of record. Outbound URLs follow the [citation safety table](#citation-safety).

## Checkpoint anchors

| ID | Player-facing label | Terminal MSQ | Evidence | Grade |
|---|---|---|---|---|
| `cp-arr-2-0` | A Realm Reborn — Patch 2.0 complete | **The Ultimate Weapon** (Lv 50, Raubahn, Northern Thanalan) | Infobox `patch = 2.0`, `type = main scenario`. Next quest *The Price of Principles* is 2.1. There is no separate 2.0 epilogue quest. | V |
| `cp-arr-2-55` | A Realm Reborn — Patch 2.55 complete | **Before the Dawn** (Lv 50, Haurchefant, Coerthas Central Highlands) | Infobox `patch = 2.55`. Previous quest *The Parting Glass* (2.55); next quest *Coming to Ishgard* (Heavensward). | V |

- Labels carry patch numbers only. Avoid quest names and the "Before the Fall" subtitle, which signals a downfall.
- Thonky files *Before the Dawn* under 2.5 rather than 2.55. It is the same quest either way, so the anchor is unaffected.

## Claims

Source quests are on `ffxiv.consolegameswiki.com/wiki/<Title>`. Quotes are short locators, not content to copy.

| ID | Claim (own words) | Source quest · patch · locator | Player learns | Grade |
|---|---|---|---|---|
| C01 | Minfilia leads the Scions. | *The Scions of the Seventh Dawn (Quest)* · 2.0 · journal: "the leader of the Scions of the Seventh Dawn" | 2.0 | V |
| C02 | The Scions are based at the Waking Sands. | Same quest · 2.0 · "headquartered … the Waking Sands"; *The Black Wolf's Ultimatum* · 2.0 · "retire to the Waking Sands" | 2.0 | V |
| C03 | The Scions formed from the Circle of Knowing and the Path of the Twelve. | *A Wild Rose by Any Other Name* · 2.0 · Y'shtola's explanation | 2.0 | V |
| C04 | Tataru greets visitors at the Waking Sands. | *The Scions of the Seventh Dawn (Quest)* · 2.0 · journal: "a singing Lalafell by the name of Tataru" | 2.0 | V |
| C05 | Thancred introduces Y'shtola as a fellow Scion. | *A Wild Rose by Any Other Name* · 2.0 · "the lovely maiden beside me is named Y'shtola" | 2.0 | V |
| C06 | Imperial forces raid the Waking Sands and take prisoners. | *All Good Things* · 2.0 · journal: "the Waking Sands was raided by imperial forces" | 2.0 | V |
| C07 | Urianger and Papalymo are among the captives freed. | *Escape from Castrum Centri* · 2.0 · "Unbind Papalymo and Urianger!" | 2.0 | V |
| C08 | Thancred was revealed to have been possessed by Lahabrea. | *Escape from Castrum Centri* · 2.0 · journal: "Thancred has been possessed by Lahabrea" | 2.0 | V |
| C09 | Thancred is freed from his enthrallment. | *The Ultimate Weapon* · 2.0 · journal: "free your comrade Thancred from his enthrallment" | 2.0 | R |
| C10 | Alphinaud and Alisaie are twins. | *A Hero in the Making* · 2.0 · journal: "the traveling twins, Alphinaud and Alisaie"; Alphinaud: "my sister, Alisaie" | 2.0 | V |
| C11 | Alisaie has gone her own way, apart from her brother and the Scions. | *Back from the Wood (Quest)* · 2.0 · Alphinaud: "Alisaie has chosen to walk her own path" | 2.0 | V |
| C12 | Alphinaud addresses an unnamed "Grandfather" whose dream cost his life. | *The Ultimate Weapon* · 2.0 · "Do you see, Grandfather?" | 2.0 (implied only) | V. Not used: names no one; C13/C26 carry the fact. |
| C13 | Louisoix was Alisaie's grandfather. | *Alisaie's Pledge* · 2.0 feature · Urianger: "Master Louisoix was my lady's grandsire" | 2.0 (optional; chain U1) | V |
| C26 | Louisoix is the twins' shared grandfather. | *Another Turn in the Coil* · 2.2 feature · Alphinaud: "my sister's admiration and affection for our grandsire" | 2.55 (optional, released 2.2; chain U1) | V |
| C27 | Louisoix sealed Bahamut during the Calamity and is presumed dead. | *Alisaie's Pledge* · 2.0 feature · journal: "seemingly by Louisoix, who was presumed dead" | 2.0 (optional; chain U1) | V |
| C28 | The player freed Louisoix's soul from Bahamut. | *Alisaie's Path* · 2.4 feature · Alisaie: "You are the one who freed Grandfather's soul" | 2.55 (optional, released 2.4; chain U1) | V |
| C29 | Louisoix's power is why no one remembers the Warrior of Light. | *A Wild Rose by Any Other Name* · 2.0 MSQ · "the power that Louisoix invoked to save your life" | 2.0 | V |
| C30 | Urianger asks the player to join "the young Scion", Alisaie. | *Alisaie's Pledge* · 2.0 feature · journal: "join the young Scion" | 2.0 (optional; chain U1) | V |
| C14 | The Scions' new home will be the Rising Stones in Mor Dhona. | *Laying the Foundation* · 2.1 · "a new home in Mor Dhona: the Rising Stones" | 2.1 (snapshot 2.55) | V |
| C15 | The Rising Stones is inaugurated as the new headquarters. | *Build on the Stone* · 2.1 · journal: "inauguration of their new headquarters" | 2.1 (snapshot 2.55) | V |
| C16 | Alphinaud commands the newly formed Crystal Braves. | *Traitor in the Midst* · 2.4 · journal: "his new station as commander of the Crystal Braves" | 2.4 (snapshot 2.55) | V |
| C17 | Minfilia stays behind during the flight and says Hydaelyn is speaking to her. | *The Parting Glass* · 2.55 · "I must remain behind"; "Hydaelyn... She speaks to me." | 2.55 | V |
| C18 | Y'shtola and Thancred stay to hold off the pursuit. | *The Parting Glass* · 2.55 · "Thancred and I will deal with this." | 2.55 | V |
| C19 | Crystal Braves control the Rising Stones. | *The Parting Glass* · 2.55 · "The Rising Stones is also under our control."; *Before the Dawn* · Yugiri: "Only Crystal Braves await you there." | 2.55 | V |
| C20 | The Crystal Braves turned on the Scions. | *Before the Dawn* · 2.55 · Tataru: "Crystal Braves─our own people!─turned on us" | 2.55 | V |
| C21 | After the banquet, Urianger glamoured the Waking Sands, the "old headquarters", into a hidden refuge. | *Before the Dawn* · 2.55 · Tataru: "he used his magicks to weave a glamour … our old headquarters" | 2.55 | V |
| C22 | Every other Scion who attended the banquet is unaccounted for. | *Before the Dawn* · 2.55 · journal: "remains unaccounted for" | 2.55 | V |
| C23 | Alisaie was not with the others; Alphinaud believes she was watching over him. | *The Parting Glass* · 2.55 · "she was the one watching over me" | 2.55 | V |
| C24 | The survivors regroup in an intercessory in Coerthas. | *Before the Dawn* · 2.55 · journal: "join your companions in the intercessory" | 2.55 | V |
| C25 | Alphinaud is a Scion in the 2.0 main scenario. | *Escape from Castrum Centri* · 2.0 · Alphinaud: "the Scions of the Seventh Dawn are returned!" | 2.0 | R |

Excluded because a lane found them only in secondary summaries, or because they are spoiler-heavy without adding pilot value: the Lifestream fate of Y'shtola and Thancred, Yda and Papalymo going into hiding, Nanamo's survival, and Urianger's final-cutscene meeting with an Ascian in *Before the Dawn* (R; deliberately left out of the pilot).

### Optional-content unlock chains

Each step's prerequisite was verified from wiki infobox fields (`prev-quest`, `req-quest`, `requirements`). Story steps are listed; the raid clears that gate them sit between.

| Chain | Steps (patch) | Main-scenario gate | Eligible at |
|---|---|---|---|
| U1 Binding Coil story | *The Ultimate Weapon* (2.0 MSQ) → *A Recurring Problem* → Hard-mode Ifrit, Garuda, Titan trials → *Primal Awakening* → Binding Coil Turns 1–5 → *Alisaie's Pledge* (2.0) → *Another Turn in the Coil* (2.2) → Second Coil Turn 4 → *Alisaie's Resolve* (2.2) → *Fragments of Truth* (2.4) → Final Coil Turn 4 → *Alisaie's Path* (2.4) | *The Ultimate Weapon* only | 2.0 steps at `cp-arr-2-0`; 2.2 and 2.4 steps at `cp-arr-2-55` (release-patch condition) |

Patch 5.3 removed some ARR quests, so the lead also checked every cited quest against the wiki's removal lists. None of them was removed.

## Provisional roster (12)

All 12 entities are sourceable; 12 is the pilot's upper bound. The roster fixes membership and visibility only; NDL-003 writes the reviewed presentations.

| ID | Category | Visible @2.0 | Visible @2.55 | Changes? | Key claims |
|---|---|---|---|---|---|
| `char-minfilia` | character | yes | yes | description | C01, C17 |
| `char-thancred` | character | yes | yes | description | C05, C08, C09, C18 |
| `char-yshtola` | character | yes | yes | description | C03, C05, C18 |
| `char-urianger` | character | yes | yes | description + new edge | C07, C21 |
| `char-alphinaud` | character | yes | yes | description | C10, C16, C25 |
| `char-alisaie` | character | yes | yes | description | C10, C11, C23, C30 |
| `char-louisoix` | character | yes | yes | description + new edge | C13, C26–C29 |
| `char-tataru` | character | yes | yes | description | C04, C21 |
| `org-scions` | organization | yes | yes | description + edges | C01–C03, C20, C22 |
| `org-crystal-braves` | organization | **no** | yes | appears at 2.55 | C16, C19, C20 |
| `loc-waking-sands` | location | yes | yes | description + edges | C02, C06, C21 |
| `loc-rising-stones` | location | **no** | yes | appears at 2.55 | C14, C15, C19 |

Considered and cut:
- **Yda:** name trap. Her Heavensward identity reveal makes her the pilot's highest leak risk, and she has no needed change.
- **Papalymo:** valid, but redundant. Swap him in if Alisaie fails review.
- **Path of the Twelve / Circle of Knowing:** defunct predecessors with no change between checkpoints.
- **G'raha Tia, Estinien, Lahabrea:** not Scions at 2.55, or carry later-reveal traps.

## Provisional relationships (14)

Intervals are `[validFrom, validUntil)` over checkpoint IDs. `—` means ongoing.

| ID | Source → type → target | validFrom | validUntil | Claims | Notes |
|---|---|---|---|---|---|
| R01 | `char-minfilia` → leads → `org-scions` | `cp-arr-2-0` | — | C01 | Ongoing (user decision, 2026-11-14). Her 2.55 description says her whereabouts are unknown. |
| R02 | `char-thancred` → member-of → `org-scions` | `cp-arr-2-0` | — | C05, C08 | |
| R03 | `char-yshtola` → member-of → `org-scions` | `cp-arr-2-0` | — | C05 | |
| R04 | `char-urianger` → member-of → `org-scions` | `cp-arr-2-0` | — | C07 | NDL-003 needs an explicit membership passage. |
| R05 | `char-alphinaud` → member-of → `org-scions` | `cp-arr-2-0` | — | C25 | Verify C25. |
| R06 | `char-tataru` → member-of → `org-scions` | `cp-arr-2-0` | — | C04 | |
| R07 | `char-alphinaud` → twin-of → `char-alisaie` | `cp-arr-2-0` | — | C10 | Symmetric: stored once; a reversed duplicate is rejected (user decision, 2026-11-14). |
| R08 | `org-scions` → headquartered-at → `loc-waking-sands` | `cp-arr-2-0` | `cp-arr-2-55` | C02 | Ends; the move happened at 2.1. Cite only C02: the end evidence (C15, C21) is from later quests and belongs on the 2.55 Rising Stones and Waking Sands presentations (schema citation timing rule). |
| R09 | `org-crystal-braves` → controls → `loc-rising-stones` | `cp-arr-2-55` | — | C19 | Begins. |
| R10 | `org-crystal-braves` → turned-against → `org-scions` | `cp-arr-2-55` | — | C20 | Begins. |
| R11 | `char-urianger` → conceals → `loc-waking-sands` | `cp-arr-2-55` | — | C21 | Begins. |
| R12 | `char-alisaie` → grandchild-of → `char-louisoix` | `cp-arr-2-0` | — | C13 | Optional, chain U1 (2.0). |
| R13 | `char-alphinaud` → grandchild-of → `char-louisoix` | `cp-arr-2-55` | — | C26 | Begins. Optional, chain U1, released 2.2. At 2.0 it is only inferable through R07 + R12, and inference is not shown. |
| R14 | `char-alisaie` → member-of → `org-scions` | `cp-arr-2-0` | — | C30 | Optional, chain U1 (2.0). |

Not encodable as edges (rule 3), so carried in 2.55 descriptions instead: the Scions headquartered at the Rising Stones (2.1 until the 2.55 seizure), and Alphinaud commanding the Crystal Braves (2.4 until their betrayal).

Pilot change requirements:
- **Relationship change:** satisfied by R08 ending and R09–R11 beginning.
- **Description change:** satisfied by the Waking Sands, Minfilia, the Scions, and Louisoix (presumed dead → soul freed), among others.

At 2.0, two entities and four edges (R09–R11, R13) are hidden. That exercises hidden-count and leak tests.

## Citation safety

Lane D findings, reconciled. "URL" means showing an outbound wiki link at that checkpoint; the plain-text citation title can still be shown.

| Entity | URL @2.0 | URL @2.55 | Rule |
|---|---|---|---|
| Minfilia | no | no | `Minfilia` is a disambiguation page naming a 5.0 character. `Minfilia_Warde` carries an unverified surname. Cite quest pages only. |
| Thancred, Y'shtola, Urianger, Tataru, Alphinaud, Alisaie | yes | yes | Use the canonical first-name page, never a surname redirect. |
| The Scions of the Seventh Dawn | prefer quest | yes | The page title is safe; prefer the 2.0 quest page for 2.0 claims. |
| The Waking Sands | yes | yes | |
| Louisoix | **no** | yes | Canonical page `Louisoix_Leveilleur` carries the surname. First plain-text use is 2.1 (*The Gifted*). Show the citation title only at 2.0. |
| The Rising Stones | **no** (hidden) | yes | 2.1 location. |
| Crystal Braves | **no** (hidden) | yes | Formed in 2.3. |
| Quest pages from 2.1–2.55 | **no** | yes | Never cite a quest the player has not completed. |
| Always unsafe | — | — | `Minfilia_(The_First)`, `Ryne`, `Oracle_of_Light`, `The_First`, `Lyse`, `Lyse_Hext`, `The_Unending_Codex`, `Ascilla`, and `#anchors` that name later titles. |

Banned display terms for the pilot: Lyse, Exarch, Crystal Exarch, Emet-Selch, Hythlodaeus, Hades, Ryne, Oracle of Light, Word of the Mother, Wyrmblood, Lightwarden, Minfilia (The First), Warrior of Darkness, and every surname under rule 4.

## Inputs to the schema freeze

These are not decisions; the freeze in NDL-002 step 2 decides them.

- **Checkpoint-ID bounds.** An interval that falls entirely between checkpoints is invalid, not hidden (rule 3).
- **Evidence eligibility belongs to the research process, not the runtime model.** The dataset carries only reviewed citation display metadata. The available-content rule is enforced in review, and the evidence matrix records each optional source's unlock chain.
- **Relationship types are a closed vocabulary.** The pilot needs: `leads`, `member-of`, `twin-of` (symmetric), `grandchild-of`, `headquartered-at`, `controls`, `turned-against`, `conceals`. Each type needs labels for both directions so incoming edges render.
- **Symmetric types** (`twin-of`) are declared symmetric in the type vocabulary and stored as one edge. A reversed duplicate is a validation error, not normalized (user decision, 2026-11-14).
- **Content scope tags** (user request, 2026-11-14). The user wants a main-story view and a main-plus-optional view, because optional content can change what is known. Every edge and presentation carries `scope: main | optional`. A main-story view hides optional edges and uses the main presentation. The full view may use an optional presentation that replaces the main one at the same checkpoint. An entity whose only evidence is optional is hidden in the main view. In the pilot, the optional-scope records are R12–R14 and Louisoix's descriptions (C27, C28). When the toggle ships (NDL-004 or later) is a separate decision; the data carries the tags from the start so nothing has to be re-authored.
- **Citation `url` is optional per presentation**, because some entities (Minfilia) have no safe URL at either checkpoint.
- **Frozen outcome:** see [schema.md](schema.md). The council review on 2026-11-14 added citation `availableAt` and `scope`, plus the optional-presentation boundary and persistence rules.

## Open questions

1. **In-client confirmation** of both terminal quests and the C01–C30 passages. Everything is fan transcription, and no official Square Enix page was reachable from the shell.
3. **Selector wording (NDL-004).** Under rule 1 the snapshots include optional story content. The checkpoint help text should say so, for example "includes optional story content available by this patch". The labels themselves stay unchanged.
4. **When the main-story / optional view toggle ships:** NDL-004 or a later story. The data supports it either way.
5. **Surname policy beyond the pilot:** whether to show "Leveilleur" from 2.4 onward. Out of scope for the pilot.
6. **Unverified R rows** (C09, C25) need a lead or content check before NDL-003 accepts them.
