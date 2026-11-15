# Atlas pilot content evidence (NDL-003)

> **Status: accepted.** The user explicitly accepted this content on 2026-11-14, and every record is marked `reviewed`. This is the completed evidence matrix for [`NpcDialogueLinks/atlas.json`](../../NpcDialogueLinks/atlas.json). It supersedes the provisional [discovery evidence](discovery-evidence.md) for every record it covers. AI research and AI review are not canon acceptance; any later content change needs review again.

| File | What it holds |
|---|---|
| [content-review.md](content-review.md) | The readable review sheet: every player-visible record as written, with its evidence |
| [content-claims.md](content-claims.md) | Every claim, with its source quest, patch, scope and locator quote |
| this file | Method, rule decisions, changes from discovery, citation safety, exclusions and open questions |
| `tools/atlas/build_pilot_content.py` | The authoring source. It generates the three outputs above, so they cannot drift apart |

## How the data is built

Edit `tools/atlas/build_pilot_content.py`, never the generated files. Run it from the repository root, then run the tests:

```sh
python3 tools/atlas/build_pilot_content.py
dotnet test NpcDialogueLinks.Tests
```

Review status is **per record and bound to content** (since `NDL-006`). The generator's `ACCEPTED` maps each accepted record to a fingerprint of its accepted content, and a record is emitted `reviewed` only when its current content matches. The fingerprint covers the emitted record and the reviewed context it is shown with: the entity's category for a presentation, the relationship type's labels and symmetry, and the claims behind the record (wording, source and locator). A new record, or any change to an accepted one or to that context, is emitted `pending`. The only exception is a citation's `availableAt`, which the v2 plan allows to move earlier mechanically. `python3 tools/atlas/build_pilot_content.py --self-test` checks these rules.

To record an acceptance, run `python3 tools/atlas/build_pilot_content.py --print-pending`. It prints the key and fingerprint of **only the pending records**. Copy into `ACCEPTED` exactly the lines the user accepted, then regenerate. Never re-record everything: that would accept pending edits nobody reviewed. Strict validation must then pass with no errors (`RealDataTests.Real_StrictIsBlockedOnlyByReviewMarkers`).

New or changed records default to `pending`. Strict validation, and therefore the plugin, refuses the data until those records are reviewed and accepted. Accepted records are never flipped back by editing others.

To browse the real data without FFXIV:

```sh
dotnet run --project NpcDialogueLinks.AtlasViewer -- --data "$PWD/NpcDialogueLinks/atlas.json"
```

Pass an absolute path: `dotnet run` starts the viewer in its own project folder, so a relative `--data` path would not resolve from the repository root.

## Method

Researched 2026-11-14.

**Research lanes.** Four parallel Haiku research lanes each covered one group of the 12-entity roster:
- A: Minfilia, Tataru, the Scions, the Waking Sands;
- B: Thancred, Y'shtola, Urianger;
- C: Alphinaud, Alisaie, Louisoix;
- D: the Crystal Braves, the Rising Stones, and a citation-safety audit of every candidate source page.

Together the lanes swept all 2.0–2.55 main-scenario quest pages for their entities.

**Lead verification.** The lead then re-fetched raw wikitext for all 27 quests cited, through the Console Games Wiki MediaWiki API, and checked every locator in [content-claims.md](content-claims.md) against it. A script confirmed that every quoted fragment of all 53 claims appears verbatim. The check also confirmed that each line sits outside any conditional branch and any optional-dialogue block. The [roster](discovery-evidence.md#provisional-roster-12) and [relationship list](discovery-evidence.md#provisional-relationships-14) from discovery are kept unchanged.

### Evidence rules applied

1. **Main** records rest only on main-scenario text every player sees: journal entries and dialogue outside `-optional start/end` blocks and outside conditional branches. Conditional branches include `> If Legacy character` and starting-city variants.
2. **Optional** records rest on the Binding Coil feature quests in [unlock chain U1](discovery-evidence.md#optional-content-unlock-chains): *Alisaie's Pledge* (2.0), *Another Turn in the Coil* and *Alisaie's Resolve* (2.2), and *Alisaie's Path* (2.4). Each counts from the first checkpoint at or after its release patch (the [available-content rule](../lore-relationship-atlas.md#research-and-content-rules)).
3. **Optional NPC dialogue** inside main-scenario quests is not used for any record. It is player-visible but not required, and it fits neither scope cleanly.
4. **Shown, not occurred.** A fact counts from the checkpoint at or after the patch in which the player is shown it. The Rising Stones (2.1) and the Crystal Braves (2.3) therefore first appear at the 2.55 checkpoint, and their 2.1–2.4 history is described in text (schema rule: intervals snap to checkpoints).
5. **Summaries are original.** Summaries paraphrase the claims. Short quotes appear only as locators in the evidence files.

## Changes from discovery

| Discovery item | NDL-003 outcome |
|---|---|
| C03 (the Scions formed from the Circle of Knowing and the Path of the Twelve) | **Dropped.** It sits in an optional-dialogue block (rule 3). The Scions' founding is described from C31 and C40 instead. |
| C05 (Thancred introduces Y'shtola) | **Replaced** by C31. In *A Wild Rose by Any Other Name*, Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as "your friends in the order", outside every branch. |
| C09 (Thancred freed), open question 6 | **Verified.** It is in the journal of *The Ultimate Weapon*, and the final cutscene shows him returned ("Thancred is with him/her"). Patch 6.1 turned the Lahabrea fight into a solo duty without changing this outcome. The summary says "freed" and "came home", not "fully recovered". |
| C12 ("Do you see, Grandfather?") | **Used as C43**, without naming the grandfather, so the main-story text implies no relationship. |
| C25 (Alphinaud is a Scion), open question 6 | **Verified and strengthened.** *Eyes on Me* (2.0) has "As a Scion of the Seventh Dawn, I stand against our primal and imperial foes". It sits after the Legacy branch closes, so every player sees it. |
| C27 (Louisoix sealed Bahamut) | **Narrowed.** The journal says "seemingly by Louisoix". Summaries say "apparently". |
| C29 (Louisoix's power erased memories of the player) | **Dropped.** The line is shown only to Legacy characters, and it is speculation ("we can only assume"). |
| R04 (Urianger is a Scion), open question 6 | **Supported** by C31 (introduced among "your friends in the order") and C36 (among the captives Y'shtola calls "our fellow Scions"). |
| Alisaie's wording, open question 7 | **Resolved.** The main story never calls her a Scion; it says she walks her own path toward the same goal (C11). Only the optional record says "young Scion" (C30), so the main and full views do not contradict each other. The user decided to keep R14 (2026-11-14). |
| Louisoix's identity as grandfather | No main-scenario line names Louisoix as the twins' grandfather. The 2.3 hint is in optional dialogue. R12 and R13 therefore stay `optional`, and the main-story Louisoix text never mentions grandchildren. |

## Citation safety

Lane D fetched every candidate source page in rendered form. The "Related NPCs" and "Cutscene NPCs" templates print full names, so almost every page shows a banned surname:
- "Minfilia Warde" appears on most 2.0 main-scenario pages.
- "Leveilleur" appears on several 2.2–2.4 pages.

Some pages also carry notes about later patches; for example, *The Parting Glass* names a level-54 quest. Only *Alisaie's Pledge* came out clean.

**Decision (user, 2026-11-14): links on.** Every citation links to its quest article page. The contract does not extend the Atlas's filtering guarantee to destination pages: the link opens only behind the shared external-page spoiler warning (`AtlasText.ExternalLinkWarning`).

- **Each URL names only the quest itself.** None names a character, and none carries a surname or a later title.
- **All 27 URLs resolve.** Each returns HTTP 200, and the wiki API confirms all 27 pages exist with no redirects.
- **Tests guard every link.** `Real_CitationLinksAreSafe` requires `https://ffxiv.consolegameswiki.com/wiki/` article paths with no query, rejects known-unsafe titles, and rejects any Louisoix page at 2.0. The leak sweep also scans each decoded URL for banned terms.

## Spoiler review

`RealDataTests` sweeps every displayed field (names, aliases, summaries, citation titles and URLs, relationship labels) in all four snapshots. It checks for:
- **Surnames and later identities:** Warde, Waters, Rhul, Augurelt, Leveilleur, Taru, Totolymo, Hext, Ascilia/Ascilla, Lyse, Ryne, Exarch, Emet-Selch, Hythlodaeus, Hades, Lightwarden, Wyrmblood and "The First". These are matched case-sensitively as whole words, so "Tataru" never matches "Taru".
- **Later-story phrases:** Oracle of Light, Word of the Mother, Warrior(s) of Darkness, and every later expansion name.
- **At 2.0 only:** anything that exists only from 2.1, namely the Crystal Braves, the Rising Stones, the banquet and regicide.

A mutation check confirmed that the sweep fails when a surname, a 2.55 term in 2.0 text, or an unsafe link is planted.

Deliberately left out of every record, although the 2.0–2.55 text shows some of them:
- **Minfilia:** her birth name and parents (2.1).
- **Y'shtola and Thancred:** their fate after the tunnel collapse.
- **The sultana:** whether she survived. Summaries say the Scions were *accused of plotting* her death, never that she died.
- **The banquet's instigators:** Teledji's and Lolorito's roles, and Captain Ilberd's confession.
- **Urianger:** his final-cutscene meeting in *Before the Dawn*.
- **Moenbryda:** her death.

None of these is needed for the pilot's changes, and several are reframed by later patches.

## Open questions

1. **In-client confirmation.** Every locator is a fan transcription. Spot-checking a few passages in game would raise confidence; the evidence already ties each claim to a specific quest and line.
2. **Content decisions:** resolved on 2026-11-14. Links are on, and R14 and R13 stay. See the [review sheet](content-review.md#decisions-recorded).
3. **Checkpoint help text (NDL-004).** Snapshots include optional story content released by each patch, and the selector's help text should say so.
