# The Atlas through Dawntrail (7.0–7.56)

> **Status: on the branch, 2026-11-19, with no story card.** Atlas content skips the story workflow, as for the earlier
> expansions ([Endwalker](through-endwalker.md)). The lead marked the new records `reviewed` after verification.
> Nothing here was played in game. 7.56 (*Windborne*) is the latest patch on the wiki as of this date.

## Coverage

| | Through Endwalker | Through Dawntrail 7.56 |
|---|---|---|
| Story points | 902 | **1,045**: one per quest to *The World Locked in Ice* (#995), plus the 7.0 and 7.56 milestones |
| Arcs | 144 | **169** |
| Entities | 542 | **670** (416 with portraits) |
| Relationships | 2,054 | **2,458** |
| Claims (verbatim locators) | 6,624 | **8,004** |
| `atlas.json` | about 5.7 MB | about 6.7 MB (cap 8 MiB) |

The timeline lives in `tools/atlas/timeline_7x.py`: 141 steps in the wiki's list order.

- **Parallel chains.** The Kozama'uka chain (#859–#864) comes first, then the Urqopacha chain
  (`cp-msq-859b` … `cp-msq-865b`), then #872.
- **Milestones.** *Dawntrail* is `cp-dt-7-0`, and *Windborne* is `cp-dt-7-56`.
- **Shared quest title.** Dawntrail's *On Track* (#911) has the same title as a Shadowbringers quest. So its source key
  is "On Track (Dawntrail)" (`SOURCE_KEYS`), and the step still shows the plain title.

**The next patch** needs these changes:
- a new `timeline_7x.py` step list;
- the 7.56 milestone moved to the new last quest;
- the C# checkpoint pins in `RealDataTests` updated.

At about 6.7 MB, `atlas.json` has roughly one more expansion of room before the 8 MiB file cap.

## Method

This used the same pipeline as before ([era-modules.md](era-modules.md)):

1. **Pages.** The raw wikitext of all 143 quests was saved once, from a fresh copy of the MSQ list.
2. **Research.** 24 Haiku 5.5 lanes read the pages. The lead re-checked **all 1,429 lane quote fragments** by script.
   One had a trailing "..." trimmed; the rest matched.
3. **Authoring.** Five Opus era authors wrote one module each: 7.0 in three parts, 7.1–7.3 and 7.4–7.56.
4. **Integration (lead):**
   - Valigarmanda's records, which 7.0 part 1 drafted, were adopted from #851, where 6.55 text already names it.
   - The Hhetsarro got an earlier entry from #911.
   - Bakool Ja Ja's opposition to Wuk Lamat now ends at #899, and Sareel Ja's service to Zoraal Ja at #905.
   - Wihuwte's entry now starts at #909. At #908 only a dialogue choice names him, and that line was replaced.
5. **Collisions with earlier eras:**
   - The 5.0 arc *The Oracle's Crossroads* is now *The Oracle's Fork in the Road*, because 7.1 has a quest called
     *Crossroads*.
   - A citation title may now contain a later quest title, as with *Travelers at the Crossroads* and Shadowbringers'
     *On Track*. Such a title is the cited quest's own name, which is reached by then. Both `--lint` and the C# leak
     sweep now skip available citation titles for that check.
6. **Verification:**
   - `--verify-locators` matched **all 7,719 era claims (8,205 fragments)**.
   - The optional-dialogue scan left only "talk to everyone" sections, where every listed NPC is required.
   - `--lint` passes, and so do the host tests.

## Arcs added

| Era | Arc | Steps |
|---|---|---|
| 7.0 part 1 | *Landfall in Tuliyollal* | A New World to Explore → The Rite of Succession |
| 7.0 part 1 | *The Reeds of Ok'hanu* | To Kozama'uka → Knowing the Hanuhanu |
| 7.0 part 1 | *Trading Up in Urqopacha* | To Urqopacha → Knowing the Pelupelu |
| 7.0 part 1 | *The Moblin Potpact* | The Success of Others → The Shape of Peace |
| 7.0 part 1 | *The Third Promise Taken* | Lost Promise → Sibling Rescue |
| 7.0 part 1 | *The Vidraal Unbound* | History's Keepers → The Promise of Peace |
| 7.0 part 2 | *A Feast to End a War* | The Leap to Yak T'el → Into the Traverse |
| 7.0 part 2 | *The Cloister of Mamook* | City of Silence → The Feat of the Brotherhood |
| 7.0 part 2 | *Two Vows for Tuliyollal* | Road to the Golden City → The Long Road to Xak Tural |
| 7.0 part 2 | *The Bandits of Shaaloani* | Saddled Up → One with Nature |
| 7.0 part 2 | *Siege from the Dome* | And the Land Would Tremble → All Aboard |
| 7.0 part 3 | *Beyond the Barrier* | The Land of Levin → Solution Nine |
| 7.0 part 3 | *The Queen's Secret* | The Queen's Tour → At a Crossroads |
| 7.0 part 3 | *The Summit of Everkeep* | The Protector and the Destroyer → In Pursuit of Sphene |
| 7.0 part 3 | *The Unlost World* | Through the Gate of Gold → Leafing through the Past |
| 7.0 part 3 | *The Last Terminal* | An Explorer's Delight → Dawntrail — Patch 7.0 complete |
| 7.1–7.3 | *Children Left Behind* | A Royal Invitation → Crossroads |
| 7.1–7.3 | *The Queen Who Slept* | A Glimmer of the Past → A Jewel Shattered |
| 7.1–7.3 | *Beneath Everkeep* | The Meeting → Seekers of Eternity |
| 7.1–7.3 | *The Harvest of Five Thousand* | Targeted Tragedy → Preservation Their Purpose |
| 7.1–7.3 | *The Fear of Death* | A Calculated Evolution → The Promise of Tomorrow |
| 7.4–7.56 | *Survivors of the Storm Surge* | With the Winds → To Work |
| 7.4–7.56 | *The Speaker's Heir* | In Her Heart → Into the Mist |
| 7.4–7.56 | *The Thinning Veil* | In Fate's Footsteps → Trail to the Heavens |
| 7.4–7.56 | *The Ice-Locked Sky* | A Winter's Dream → Dawntrail — Patch 7.56 complete |

## Decisions

- **No new banned terms were opened.** The surnames that the pages print (Krile's, Galuf's) stay in the locators only.
  - Zoraal Ja's son is "Gulool Ja, son of Zoraal Ja", never a bare "Gulool Ja", because that matches inside "Gulool Ja Ja".
- **Sphene has two entries.**
  - `char-sphene` is the Endless queen of 7.0. She is named "Endless Sphene" from #961.
  - `char-original-sphene` is the living queen found in 7.2.
  - The impostor of 7.1 is `char-simulant`.
- **Reveals:**
  - The Vulture → Wihuwte (#909), following the Marques → Cid pattern.
  - Valigarmanda carries "The Skyruin" as an alias from #888.
- **Portraits: 51 new picks.**
  - Some faces would give a reveal or a later form away, so they get none: Cahciua (a human face before #943), the
    Vulture and Wihuwte, Zoraal Ja (his only card shows a later form), Halmarut (disguised at first), Calyx (who changes
    form) and the simulant.
  - Most Turali minor characters have no faithful image, so they get none either.
- **New relationship types:** `guardian-of` ("guardian of" / "ward of") and `kept-by` ("kept by" / "keeps").

## Known gaps

- The Changes lens isn't offered on the step after a milestone (#854, #954), as before.
- Several "aids Wuk Lamat" relationships from 6.55 and 7.0 stay open; only Erenville's ends (#979).
