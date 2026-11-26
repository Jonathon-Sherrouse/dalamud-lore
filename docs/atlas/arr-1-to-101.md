# The Atlas from the very start: ARR MSQ #1–#101

> **Status: on the branch, 2026-11-19, with no story card** (Atlas content skips the story workflow). The new records
> are marked `reviewed` by the lead after verification. Nothing here was played in game.

## Coverage

| | Before | After |
|---|---|---|
| Story points | 597 (from MSQ #102) | **747**: every main-scenario quest from *Close to Home* (#1) |
| Arcs | 95 | **116** |
| Entities | 358 | **438** (305 with portraits) |
| Relationships | 1,363 | **1603** |
| Claims (verbatim locators) | 4,338 | **5,160** |

The timeline is `tools/atlas/timeline_arr_early.py`: 150 steps.

**Starting cities (user decision, 2026-11-19).** The game opens with three mutually exclusive chains; a player does one.
All three are in the timeline, one after another: Gridania (`cp-msq-1` …), Limsa Lominsa (`cp-msq-1b` …), Ul'dah
(`cp-msq-1c` …), each not contiguous at its start. You pick the step for your city. A starter of a later chain also
sees the earlier chains' records when viewing their own steps: out of order, but never later story. So presentations
of entities shared across chains state facts about them, and only the arc recaps say "you". The Grand Company pairs at
#41–#42 work the same way.

- Gridania and Limsa starters share one *Call of the Sea* (66210 in the game data), so the Limsa chain ends at
  *The Lominsan Envoy*. Duplicate titles keep their city in the step name ("Close to Home (Ul'dah)").
- Before the Scions appear (#30) the Atlas has no home entry, so the Story point lens opens with nothing focused.

## Method

Same pipeline as before ([era-modules.md](era-modules.md)): the 150 quest pages saved once; **16 Haiku 5.5 lanes**
(all 1,092 lane quote fragments re-checked by script, every one matched); **five Opus era authors** (one per city chain,
then #25–#61 and #62–#101); lead integration and checks. `--verify-locators` matches **all 4,875 post-2.0-baseline claims**
against the saved pages, none from optional dialogue or a branch line; `--lint` passes.

Where an existing relationship from #102 cites later quests, the eras wrote an early `-arr` copy ending where it begins,
instead of moving its start (a record may never cite a quest after its own start).

## Arcs added

| Era | Arc | Steps |
|---|---|---|
| Gridania chain | *Shadows over the Twelveswood* | Chasing Shadows → To Guard a Guardian |
| Gridania chain | *The Seedseer's Envoy* | To Guard a Guardian → Call of the Sea (Gridania) |
| Limsa Lominsa chain | *Trouble at Summerford* | On to Summerford → Just Deserts |
| Limsa Lominsa chain | *Rebuilding La Noscea* | Sky-high → Righting the Shipwright |
| Limsa Lominsa chain | *The Drydocks Plot* | Do Angry Pirates Dream → Feint and Strike |
| Limsa Lominsa chain | *The Admiral's Honor* | High Society → The Lominsan Envoy |
| Ul'dah chain | *A Newcomer in Ul'dah* | Close to Home (Ul'dah) → Out of House and Home |
| Ul'dah chain | *Ore and Gil* | Way Down in the Hole → Secrets and Lies |
| Ul'dah chain | *The Sultana's Crown* | Duty, Honor, Country → A Royal Reception |
| Ul'dah chain | *The Flame General's Envoy* | The Ul'dahn Envoy → Call of the Sea (Ul'dah) |
| #25–#61 | *The Adventurer of the Moment* | It's Probably Pirates → The Scions of the Seventh Dawn |
| #25–#61 | *The Drybone Vanishings* | A Wild Rose by Any Other Name → Lord of the Inferno |
| #25–#61 | *Choosing a Grand Company* | A Hero in the Making → Wood's Will Be Done |
| #25–#61 | *Envoys to the Sylphs* | Sylph-management → Brotherly Love |
| #25–#61 | *The Missing Elder* | Spirited Away → Believe in Your Sylph |
| #62–#101 | *The Masked Man* | Back from the Wood → Where There Is Smoke |
| #62–#101 | *The Refugees' Trust* | On to Little Ala Mhigo → Come Highly Recommended |
| #62–#101 | *The Youngbloods of Little Ala Mhigo* | The Bear and the Young'uns' Cares → Back to Square One |
| #62–#101 | *Murders in the Shroud* | Terror at Fallgourd → Skeletons in Her Closet |
| #62–#101 | *Titan Reawakened* | Wrath of the Titan → Nix That |
| #62–#101 | *A Feast at Costa del Sol* | A Modest Proposal → Battle Scars |

## Known gaps

- Most of the minor early NPCs have no portrait: no card or quest image clearly shows them.
- A few accepted #102+ texts read slightly behind the new early ones (the #143 recap says "likely Biggs and Wedge",
  whom the Grand Company quests already named).
