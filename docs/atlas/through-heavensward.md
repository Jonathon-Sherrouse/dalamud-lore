# The Atlas through Heavensward (2.1–3.56)

> **Status: shipped on the branch, 2026-11-19, with no story card.** You asked for the Atlas to cover every quest through
> Heavensward, with Haiku subagents doing the research and without the story workflow. The new records are marked
> `reviewed` by the lead under that waiver (see [Review](#review)). Nothing here was played in game.

## Coverage

| | Before (NDL-012) | After |
|---|---|---|
| Story points | 61 (MSQ #102–#160, 2.0, 2.55) | **278**: one per quest from #102 to *Fly Free, My Pretty* (#378), plus the 2.0, 2.55, 3.0 and 3.56 milestones |
| Arcs | 6 | **37** |
| Entities | 44 | **170** |
| Relationships | 105 | **574** |
| Claims (verbatim locators) | 285 | **1,664** |
| `atlas.json` | about 360 KB | about 1.8 MB (cap now 4 MiB) |

The timeline is generated from the wiki's quest infoboxes into `tools/atlas/timeline_2x_3x.py`: 215 steps in the wiki's
list order, which keeps each parallel path together (2.55's two pairs, the Artoirel then Emmanellain chains, the three
moogle trials). Each patch's last quest is a milestone, as *The Ultimate Weapon* already was.

## Method

1. **Pages.** The raw wikitext of all 218 quests (2.1–3.56) was saved once, so research and verification read the
   same copy.
2. **Research: 26 Haiku 5.5 lanes**, one per run of 5–12 quests. Each read only the saved pages and reported every quest
   in the fixed format (present, beat, 4–10 facts with verbatim quotes, threads, spoiler notes, flagged optional lines).
   The lead re-checked **all 1,850 lane quote fragments** by script: every one matched.
3. **Writing: five Opus era authors in parallel**, one module each, against a fixed contract
   ([era-modules.md](era-modules.md)). Each linted and verified its own module.
4. **Integration (lead).** The build now merges the eras: presentations close where the next begins, optional
   (Binding Coil) records follow the new main ones, and duplicate relationships written by two eras collapse into the
   earlier one. `content_lead_integration.py` adds earlier entries for names accepted text already uses (Revenant's
   Toll from #148, Raubahn from #159, Omega from #190). An Opus editor brought 43 arc recaps inside the recap rules.
5. **Verification.** `--verify-locators` checks **all 1,379 new claims (1,417 fragments) against the saved pages: 0
   mismatches**, and none sits in an optional-dialogue section or a `>` branch. `--lint` passes. All 1,966 host tests
   pass, including a new leak sweep over every story point, both content views, all three lenses and every arc.

## Arcs added

| Era | Arc | Steps |
|---|---|---|
| 2.1–2.3 | *A Home Beyond Ul'dah* | The Price of Principles → Laying the Foundation |
| 2.1–2.3 | *Myths Made Manifest* | It's Possibly a Primal → Build on the Stone |
| 2.1–2.3 | *Crystals and Exiles* | Still Waters → All Due Respect |
| 2.1–2.3 | *Tide of the Sahagin* | All Due Respect → Through the Maelstrom |
| 2.1–2.3 | *Unrest in Ul'dah* | The Great Divide → Stories We Tell |
| 2.1–2.3 | *Judgment in the Twelveswood* | Stories We Tell → What Little Gods Are Made Of |
| 2.1–2.3 | *A Company for All Eorzea* | Guardian of Eorzea → Brave New Companions |
| 2.4–2.55 | *Spies and Heretics* | Traitor in the Midst → In Flagrante Delicto |
| 2.4–2.55 | *The Saint of the Heretics* | A Simple Plan → Let Us Cling Together |
| 2.4–2.55 | *A Blade for the Ascians* | Good Intentions → In Memory of Moenbryda |
| 2.4–2.55 | *The Horde at the Gates* | Mask of Grief → Administrative Decision |
| 2.4–2.55 | *The Royal Banquet* | An Unexpected Ambition → A Realm Reborn — Patch 2.55 complete |
| 3.0 part 1 | *Wards of House Fortemps* | Coming to Ishgard → Knights Be Not Proud |
| 3.0 part 1 | *The Sea of Clouds* | Onwards and Upwards → A Reward Long in Coming |
| 3.0 part 1 | *Friends in Chains* | Divine Intervention → Keeping the Flame Alive |
| 3.0 part 1 | *The Hunt for Lady Iceheart* | To Siege or Not to Siege → Purple Flame, Purple Flame |
| 3.0 part 1 | *The Road to Sohm Al* | Where the Chocobos Roam → Beyond the Clouds |
| 3.0 part 1 | *The Great Wyrm's Answer* | Mountaintop Diplomacy → New Winds, Old Friends |
| 3.0 part 2 | *Ul'dah Set Right* | A General Summons → Ready to Fly |
| 3.0 part 2 | *The Fall of Nidhogg* | Ready to Fly → Unrest in Ishgard |
| 3.0 part 2 | *Ishgard's Founding Lie* | He Who Would Not Be Denied → The Sins of Antiquity |
| 3.0 part 2 | *The Key in the Clouds* | In Search of the Soleil → One Good Turn |
| 3.0 part 2 | *The Aetheric Ram* | An Engineering Enterprise → Hour of Departure |
| 3.0 part 2 | *The Floating Isle* | The First Flight of the Excelsior → Heavensward — Patch 3.0 complete |
| 3.1–3.56 | *The Lost Scions* | An Uncertain Future → The Word of the Mother |
| 3.1–3.56 | *The Conference at Falcon's Nest* | This War of Ours → Causes and Costs |
| 3.1–3.56 | *The Final Chorus* | The Man Within → Litany of Peace |
| 3.1–3.56 | *The Warriors' Plot* | Promises Kept → The Beast That Mourned at the Heart of the Mountain |
| 3.1–3.56 | *A Trail of Crystals* | Beneath a Star-filled Sky → An Ending to Mark a New Beginning |
| 3.1–3.56 | *The Griffin's Gambit* | Tidings from Gyr Abania → Louisoix's Finest Student |
| 3.1–3.56 | *Waking Omega* | The Obvious Solution → Heavensward — Patch 3.56 complete |

## Decisions

The era authors' editorial decisions are listed, numbered, in [content-review.md](content-review.md#decisions-recorded).
The lead's calls:

1. **Banned terms the story itself establishes** may appear from that step: Nabriales (#224), Warriors of Darkness
   (#340), Word of the Mother (#345), Nero (#376), Lyse (3.56), and Heavensward (3.0). Surnames stay out.
2. **Citation titles are exempt from the name lists.** A citation shows only its own quest's title, which is public and
   only appears once that quest is reached (*Still Waters*, *Shadows of the First*).
3. **Reveals follow Marques → Cid:** Iceheart → Ysayle, the Ivy → Eline, the masked man → Urianger, the Griffin →
   Ilberd, Yda → Lyse.
4. **Accepted records changed only mechanically.** The merge closed accepted presentations where newer ones begin, and
   relationships gained their endings (for example, the Scions leave the Waking Sands at #171, and Papalymo's membership
   ends at his death, #374). No accepted wording changed, and the accepted 2.0 and 2.55 snapshot digests still match.
5. **The leak sweep on the real data** runs every view at its own limit (the strictest picker check), in both content
   views and every lens, with no pick, each arc containing the view and the most recently ended arc, plus a held walk for
   every arc. The exhaustive limit × view × walk sweep still runs on the synthetic datasets, which cover the code paths.
6. **Bounds raised:** 512 checkpoints, 256 entities, 1,024 relationships, 64 types, 64 arcs, 64 presentations per entity,
   4 MiB.
7. **The point pickers** open scrolled to the current point, and the Raise menu is capped at 16 rows.

## Known gaps

- **No portraits** for the 126 entries added after 2.0; they keep their category shapes (as NDL-012's did).
- **Changes isn't offered** on the first step after a milestone (#162, #242, #336) or on a milestone, as before.
- **MSQ #1–#101** (the start of ARR) is still not covered.
- **A few stale-but-safe texts:** an entry keeps its last text until its next record, so some characters' 2.x
  descriptions run on through 3.0 (Raubahn, Yugiri and Ilberd have no 3.0 records). It's out of date, never ahead.

## Review

The records after 2.0 are emitted `reviewed` via `tools/atlas/accepted_later.json` (`--accept-pending`). The records
you accepted story by story are still bound to `ACCEPTED`. To put the new content back behind your review, delete
`accepted_later.json` and rebuild: every new record goes back to `pending`, and Strict loading will refuse it.
