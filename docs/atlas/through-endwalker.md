# The Atlas through Endwalker (6.0–6.55)

> **Status: on the branch, 2026-11-19, with no story card.** Atlas content skips the story workflow, as for
> [Heavensward](through-heavensward.md), [Stormblood](through-stormblood.md) and
> [Shadowbringers](through-shadowbringers.md). The lead marked the new records `reviewed` after verification. Nothing
> here has been played in game.

## Coverage

| | Through Shadowbringers (and ARR #1–#101) | Through Endwalker |
|---|---|---|
| Story points | 747 | **902**: one per quest to *The Game Is Afoot* (#852), plus the 6.0 and 6.55 milestones |
| Arcs | 116 | **144** |
| Entities | 438 | **542** (365 with portraits) |
| Relationships | 1,603 | **2,054** |
| Claims (verbatim locators) | 5,160 | **6,624** |
| `atlas.json` | about 4 MB | about 5.7 MB (cap 8 MiB) |

The timeline is `tools/atlas/timeline_6x.py`: 153 steps in the wiki's list order. The Old Sharlayan chain (#701–#709)
comes first, then the Thavnair chain (`cp-msq-701b` … `cp-msq-709b`), then #719. *Endwalker* is the milestone `cp-ew-6-0`
and *The Coming Dawn* is `cp-ew-6-55`. The late 6.0 titles that the game glitches on purpose (*A §trαnge New World*,
*F//εsh AbanΔon┨Δ* …) are kept exactly as the wiki spells them.

**The loader bounds rose** to 2,048 checkpoints, 1,024 entities, 4,096 relationships and 256 arcs: Endwalker passed the
old caps of 512 entities, 2,048 relationships and 128 arcs.

## Method

This used the same pipeline as before ([era-modules.md](era-modules.md)):

1. **Pages.** The raw wikitext of all 155 quests was saved once.
2. **Research.** 28 Haiku 5.5 research lanes read the pages. The lead re-checked **all 1,590 lane quote fragments**
   by script, and every one matched.
3. **Authoring.** **Six Opus era authors** wrote one module each: 6.0 in four parts, 6.1–6.3 and 6.4–6.55.
   `--lint <module>` now loads every accepted era along with the module (but not the other modules being written at
   the same time), so an era can build on the ones before it.
4. **Integration (lead):**
   - Galuf and Khalzahl get earlier entries (#700 and #702b), because 6.0 text names them there.
   - The cross-era endings are written: Zodiark's fall and Fandaniel's death (#740), Elidibus's end (#762), Azdaja's
     release (#842) and Golbez's opposition to Zero (#848). The edges against Zenos close after the 6.0 milestone.
   - Five one-step relationships lost their end evidence, which came from their own start quest. A reversed duplicate
     of the Forum–Loporrit alliance was dropped.
   - `--lint` now catches both of those validator rules.
5. **Verification:**
   - `--verify-locators` matches **all 6,339 era claims (6,725 fragments)** against the saved pages.
   - A scan for optional dialogue and choice branches found one Endwalker claim quoting a dialogue choice, which was
     replaced. Its only other hit is required reading.
   - `--lint` passes, and so do the host tests.

## Arcs added

| Era | Arc | Steps |
|---|---|---|
| 6.0 part 1 | *A Nation of Secrets* | The Next Ship to Sail → A Seat at the Last Stand |
| 6.0 part 1 | *The Forum's Charge* | A Labyrinthine Descent → Estate Visitor |
| 6.0 part 1 | *Shadows over Thavnair* | For Thavnair Bound → The Satrap of Radz-at-Han |
| 6.0 part 1 | *The Tip of the Spear* | In the Dark of the Tower → Best of the Best |
| 6.0 part 1 | *The Frozen Capital* | A Frosty Reception → Personae non Gratae |
| 6.0 part 2 | *Guests of the Ist* | His Park Materials → Strange Bedfellows |
| 6.0 part 2 | *Fandaniel's Endgame* | In from the Cold → The Martyr |
| 6.0 part 2 | *The Moon's Pilots* | In Shadow's Wake → Returning Home |
| 6.0 part 2 | *Thavnair's Burning Sky* | Skies Aflame → That We Might Live |
| 6.0 part 2 | *The Satrap's Secret* | When All Hope Seems Lost → At World's End |
| 6.0 part 3 | *The River of Time* | Return to the Crystarium → Ponder, Warrant, Cherish, Welcome |
| 6.0 part 3 | *The Overseer's Doubts* | Lives Apart → Verdict and Execution |
| 6.0 part 3 | *Venat's Inquiry* | Travelers at the Crossroads → A Flower upon Your Return |
| 6.0 part 3 | *Meteion's Report* | Hunger in the Garden → Thou Must Live, Die, and Know |
| 6.0 part 4 | *The Forum's Wager* | As the Heavens Burn → No Job Too Small |
| 6.0 part 4 | *Guests from the Moon* | Wise Guides → Once Forged |
| 6.0 part 4 | *The Mothercrystal's Answer* | Bonds of Adamant(ite) → Friends Gathered |
| 6.0 part 4 | *Isles of Despair* | Unto the Heavens → Where Kn∞wledge Leads |
| 6.0 part 4 | *The Last Song* | Vic┨οry ̈ ̈ ̈╳, │̆││ε Lost → Endwalker — Patch 6.0 complete |
| 6.1–6.3 | *The Vault beneath the Bounty* | Newfound Adventure → Sharing the Wealth |
| 6.1–6.3 | *The Road into the Void* | Bridging the Rift → Shadowed Remnants |
| 6.1–6.3 | *Golbez's Archfiends* | Where Everything Begins → Buried Memory |
| 6.1–6.3 | *The Trail to Garlemald* | Once More unto the Void → King of the Mountain |
| 6.1–6.3 | *Holding to Hope* | A Dragon's Resolve → Gods Revel, Lands Tremble |
| 6.4–6.55 | *The Price of the Tower* | Currying Flavor → Bonds of Trust |
| 6.4–6.55 | *Chains on the Red Moon* | Lunar Rendezvous → The Dark Throne |
| 6.4–6.55 | *Light Across the Rift* | Seeking the Light → Reunited at Last |
| 6.4–6.55 | *A Letter from Tural* | Growing Light → Endwalker — Patch 6.55 complete |

## Decisions

- **No new banned terms opened.** Every author wrote around the ones still banned (surnames, "Endwalker" outside
  citation titles, Igeyorhm). Some names would match inside common words, so they stay in text only, never as an entry
  or alias: "Amon" (inside "Among"), "Garlemald", and "Sir" (inside "Pharos Sirius"). Some entries carry a fuller name
  for the same reason: the Forum is "The Forum of Sharlayan" and the Ea are "The Ea of Ultima Thule".
- **Reveals** follow Marques → Cid, each from the step whose page states it. In each pair below, the earlier name stays
  searchable as an alias:
  - Varshahn → Vrtra (#709b);
  - Fandaniel → Hermes (#762);
  - Venat → Hydaelyn (#791);
  - M-017 → Stigma-1 (#803);
  - the knight in black → Golbez (#819);
  - Golbez → Durante (#848).
- **Portraits:** 60 new picks.
  - Left without one, because a face or a later form would give a reveal away: Zero (a hooded voidsent until #818),
    Azdaja (her only card is the Shadow Dragon), Azem, the watcher, Al End, Stigma-1, M-017 and the knight in black.
  - Left without one for lack of a faithful image: Erenville, Ameliance, Galuf and a few dozen minor characters, groups
    and places. `tools/atlas/portraits_later.py` lists them all.
  - Hydaelyn still has none: her card shows her Endwalker form, and her entry starts at #4.
- **Zenos** breathes his last at the 6.0 milestone, per the Journal. The edges opposing him close on the next step,
  with no end evidence, because none may sit there.

## Known gaps

- The Changes lens isn't offered on the step after a milestone (#699, #807), as before.
- The Elpis records (Hermes's leadership, the Convocation and so on) stay open after you return to the present, as the
  Amaurot records did in Shadowbringers.
