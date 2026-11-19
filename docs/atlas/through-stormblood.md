# The Atlas through Stormblood (4.0–4.56)

> **Status: on the branch, 2026-11-19, with no story card** (Atlas content skips the story workflow, as for
> [Heavensward](through-heavensward.md)). The new records are marked `reviewed` by the lead after verification. Nothing
> here was played in game.

## Coverage

| | Through Heavensward | Through Stormblood |
|---|---|---|
| Story points | 278 | **440**: one per quest to *A Brief Reprieve* (#540), plus the 4.0 and 4.56 milestones |
| Arcs | 37 | **62** |
| Entities | 170 | **268** (213 with portraits) |
| Relationships | 574 | **962** |
| Claims (verbatim locators) | 1,664 | **2,967** |

The timeline is `tools/atlas/timeline_4x.py`: 160 steps in the wiki's list order, which keeps each parallel path together
(the two Gyr Abania chains from #385, the three-way splits at #398 and #421). *Stormblood* and *A Requiem for Heroes*
are the milestones `cp-sb-4-0` and `cp-sb-4-56`.

## Method

Same pipeline as Heavensward ([era-modules.md](era-modules.md)):

1. The raw wikitext of all 162 quests was saved once.
2. **21 Haiku 5.5 research lanes** read the pages; the lead re-checked **all 1,497 lane quote fragments** by script, and every one matched.
3. **Four Opus era authors** wrote one module each (4.0 in three parts, then 4.1–4.56).
4. **Integration (lead):** Ala Mhigo starts from #200, where text first names it, and adopts the drafted 4.x records;
   part 3's later records for Castellum Velodyna and Specula Imperatoris, which part 1 creates, are adopted too.
5. **Verification:** `--verify-locators` matches **all 2,682 post-2.0 claims (2,749 fragments)** against the saved pages,
   none from optional dialogue or a branch line; `--lint` passes; all 2,928 host tests pass.

## Arcs added

| Era | Arc | Steps |
|---|---|---|
| 4.0 part 1 | *Envoys to the Resistance* | Beyond the Great Wall → A Bargain Struck |
| 4.0 part 1 | *The East End Ambush* | A Friend of a Friend in Need → Let Fill Your Hearts with Pride |
| 4.0 part 1 | *Return to Ala Gannha* | A Familiar Face Forgotten → Homeward Bound |
| 4.0 part 1 | *Blood in Rhalgr's Reach* | Where Men Go as One → Divide and Conquer |
| 4.0 part 1 | *Passage to the Far East* | Lies, Damn Lies, and Pirates → By the Grace of Lord Lolorito |
| 4.0 part 1 | *Across the Ruby Sea* | A Good Samurai Is Hard to Find → Boys with Boats |
| 4.0 part 2 | *A Bargain with the Confederacy* | To Bend with the Wind → Forever and Ever Apart |
| 4.0 part 2 | *The Kojin Treasures* | In Darkness the Magatama Dreams → Tide Goes in, Imperials Go Out |
| 4.0 part 2 | *The Silence of Yanxia* | A Silence in Three Parts → All the Little Angels |
| 4.0 part 2 | *Lord Hien on the Steppe* | Here There Be Xaela → In the Footsteps of Bardam the Brave |
| 4.0 part 2 | *Captives of the Oronir* | The Children of Azim → As the Gods Will |
| 4.0 part 2 | *The Steppe Rides South* | Naadam → The Hour of Reckoning |
| 4.0 part 3 | *The Flood at Doma Castle* | The Room Where It Happened → The World Turned Upside Down |
| 4.0 part 3 | *Back to Gyr Abania* | A Swift and Secret Departure → The Fortunes of War |
| 4.0 part 3 | *The Qalyana's Goddess* | Rising Fortunes, Rising Spirits → The Silence of the Gods |
| 4.0 part 3 | *The Siege of Specula Imperatoris* | The First of Many → The Road Home |
| 4.0 part 3 | *The Cannon at Castrum Abania* | For the Living and the Dead → The Price of Freedom |
| 4.0 part 3 | *The March on Ala Mhigo* | Raubahn's Invitation → Stormblood — Patch 4.0 complete |
| 4.1–4.56 | *Spoils of Liberation* | Arenvald's Adventure → Echoes of an Echo |
| 4.1–4.56 | *The Sultana's Bargain* | A Sultana's Strings → Return of the Bull |
| 4.1–4.56 | *Gosetsu's Return* | Tidings from the East → Rise of a New Sun |
| 4.1–4.56 | *The Prisoner Exchange* | Gosetsu and Tsuyu → The Primary Agreement |
| 4.1–4.56 | *The Empty Grave* | Under the Moonlight → Shadows in the Empire |
| 4.1–4.56 | *Allies and Sleepers* | A Power in Slumber → A Defector's Tidings |
| 4.1–4.56 | *War on the Border* | Seiryu's Wall → Stormblood — Patch 4.56 complete |

## Decisions

- **No new allowed terms.** Surnames (Galvus, Brutus, Hext, Aldynn …), "Baelsar" and "Exarch" stay out of displayed
  text; the hooded figure of 4.4–4.56 is "the enigmatic figure". "Stormblood" appears only in citation titles.
- **Reveals and second names:** Yotsuyu carries "Tsuyu" as an alias from #512; Shadowhunter is `revealed as` Gaius at #537.
- **Accepted records changed only mechanically:** earlier records close where Stormblood ones begin, and relationships
  gain endings (Yugiri stops leading the Doman refugees at #380, Raubahn's command of the Flames ends at #512).
- **Portraits:** 63 new picks from cards, quest illustrations and duty art (Doma Castle, Castrum Abania, Kugane Castle,
  the Sirensong Sea, Ala Mhigo, Bardam's Mettle, the Burn). Entries without a faithful image keep their shapes, as do
  Shadowhunter and the enigmatic figure, whose faces would give them away; the list is in `tools/atlas/portraits_later.py`.
- **Bounds raised again:** 1,024 checkpoints, 512 entities, 2,048 relationships, 128 arcs, 128 presentations per entity, 8 MiB.
- **Tooling fixes:** `--lint <module>` no longer crashes on portraits of entities that module doesn't load, and
  `--accept-pending` replaces a re-accepted record's fingerprint instead of keeping both.

## Known gaps

- The Changes lens isn't offered on the step after a milestone (#380, #502), as before.
- MSQ #1–#101 is still not covered.
