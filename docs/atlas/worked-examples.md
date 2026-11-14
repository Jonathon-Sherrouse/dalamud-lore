# Atlas discovery worked examples (NDL-002)

> **Status: PROVISIONAL / UNREVIEWED.** These examples illustrate the [Atlas contract](../lore-relationship-atlas.md) using claims from the [discovery evidence matrix](discovery-evidence.md). The summaries are draft wording to make the examples concrete. They are not reviewed canon and are never packaged.

Each example lists the planned synthetic test cases that exercise it. The tests do not exist yet: NDL-002 step 3 implements them in `NpcDialogueLinks.Tests/` against synthetic fixtures modeled on these examples, and this table gets updated with the real test names when they land.

## WE-1 — A relationship ends while new entities and edges appear

**Claims:** C02, C14, C15, C19, C20, C21 · **Edges:** R08–R11

| | `cp-arr-2-0` | `cp-arr-2-55` |
|---|---|---|
| Scions → headquartered-at → Waking Sands (R08) | shown | hidden (ended) |
| Crystal Braves (entity) | hidden: not formed yet | shown |
| Rising Stones (entity) | hidden: not introduced yet | shown |
| Crystal Braves → controls → Rising Stones (R09) | hidden | shown |
| Crystal Braves → turned-against → Scions (R10) | hidden | shown |
| Urianger → conceals → Waking Sands (R11) | hidden, though both endpoints are visible | shown |
| Scions headquartered at Rising Stones (2.1 to 2.55) | not an edge | not an edge; mentioned in the Rising Stones description |

Draft 2.55 Rising Stones summary: *"The Scions' headquarters in Mor Dhona after they left the Waking Sands, now held by the Crystal Braves."*

Requirements exercised:
- **Interval semantics:** `[from, until)` is exclusive at the end.
- **Edges that begin later:** an edge can start at a later checkpoint while both endpoints are visible earlier (R11).
- **Entity visibility:** an entity can first become visible at a later checkpoint.
- **No leak through hidden entities:** they leave no trace in search results, counts, neighbor lists, or citations.
- **Endpoint validation:** both endpoints must be visible for the edge's whole interval.
- **Rule 3:** history that falls between checkpoints goes in descriptions, not edges.

| Planned test | Asserts |
|---|---|
| `Projection_EdgeEndsAtExclusiveBound` | R08 appears at 2.0 and is absent at 2.55. |
| `Projection_EntityHiddenBeforeValidFrom` | Crystal Braves and Rising Stones are absent from the 2.0 entity list, search, and neighbor lists. |
| `Projection_EdgeBeginsLaterWithVisibleEndpoints` | R11 is absent at 2.0 although Urianger and the Waking Sands are visible. |
| `Projection_HiddenCountsNotDisclosed` | Waking Sands' 2.0 neighbor count includes only edges visible at 2.0, with no "+N hidden". |
| `Validation_RejectsEdgeWhoseEndpointIsHidden` | An edge from Rising Stones starting at 2.0 fails validation. |
| `Validation_RejectsIntervalBetweenCheckpoints` | A from/until pair with no checkpoint inside the interval is rejected. |

## WE-2 — The same entity, described differently per snapshot

**Claims:** C01, C17, C02, C21, C06 · **Entities:** `char-minfilia`, `loc-waking-sands`

| Entity | Draft summary @2.0 | Draft summary @2.55 |
|---|---|---|
| Minfilia | Leader of the Scions of the Seventh Dawn, guiding them from the Waking Sands. | Leader of the Scions, last seen staying behind during their flight, saying Hydaelyn was speaking to her. Her whereabouts are unknown. |
| Waking Sands | The Scions' base in Vesper Bay. Raided by imperial forces, then reclaimed. | The Scions' former headquarters, now glamoured by Urianger to look abandoned, sheltering survivors. |

Requirements exercised:
- **One presentation per checkpoint:** exactly one reviewed presentation per visible entity at each checkpoint.
- **Clean interval tiling:** presentations must not overlap or leave gaps.
- **No backfill:** viewing as of 2.0 with the ceiling at 2.55 shows only 2.0 text.
- **Citations per snapshot:** each presentation carries its own citations, and a later citation never appears in an earlier view. Minfilia has no safe URL at either checkpoint, so the citation title is shown with no link.

| Planned test | Asserts |
|---|---|
| `Projection_SelectsPresentationForViewCheckpoint` | Each checkpoint yields its own summary. |
| `Projection_ReverseViewingDoesNotBackfill` | Ceiling 2.55 with view 2.0 returns exactly the 2.0 summary and citations. |
| `Validation_RejectsOverlappingPresentations` | Two presentations covering 2.55 fail validation. |
| `Validation_RejectsGapInVisibility` | An entity visible at 2.0 and 2.55 with no 2.55 presentation fails validation. |
| `Projection_CitationWithoutUrlIsAllowed` | A citation with no URL validates and projects as text-only. |
| `Search_MatchesOnlyVisiblePresentationText` | Searching "glamour" at 2.0 returns nothing. |

## WE-3 — True in-universe, but not yet player knowledge

**Claims:** C10, C12, C13, C16, C26, C27, C28 · **Edges:** R07, R12, R13 · **Rule:** available-content rule (evidence rule 1)

Four cases look alike and resolve differently:

- **Twins (R07), shown from 2.0.** Lane C first dated the sibling tie to 2.2 from a Coil quest. The lead found it stated outright in a required 2.0 main-scenario quest, *A Hero in the Making* ("the traveling twins, Alphinaud and Alisaie"). The edge starts at `cp-arr-2-0`.
- **Alisaie's grandfather (R12), shown from 2.0.** Only optional content says it: *Alisaie's Pledge*. That quest is 2.0 content, and its whole unlock chain (U1) needs nothing beyond *The Ultimate Weapon*, so it counts at `cp-arr-2-0`.
- **Alphinaud's grandfather (R13), shown from 2.55.** The explicit line is in *Another Turn in the Coil*. Today's game lets a player reach it right after 2.0, but it was released in 2.2, so the release-patch condition puts it at `cp-arr-2-55`. At 2.0 the fact is inferable from R07 + R12, but the Atlas shows only stated facts and never derives edges. Alphinaud's unnamed "Grandfather" address (C12) is not enough either.
- **Louisoix's fate (C27 → C28), a description change.** At 2.0 he is presumed dead after sealing Bahamut. At 2.55 the player has freed his soul (*Alisaie's Path*, released 2.4).

Alphinaud commanding the Crystal Braves (C16) stays description-only, under evidence rule 3. It begins and ends between the checkpoints.

Draft summaries for Louisoix:
- **2.0:** *"The twins' grandfather, whose power spared the Warrior of Light at the Calamity; believed lost after sealing Bahamut."*
- **2.55:** *"... whose soul the Warrior of Light freed from Bahamut."*

Requirements exercised:
- Separating when something occurred from when the player learns it.
- The available-content rule, including the release-patch condition, which is enforced in review rather than at runtime.
- No derived edges: the projection shows only authored edges.
- The ceiling and view rule: raising the ceiling never changes what an earlier view shows.

| Planned test | Asserts |
|---|---|
| `Projection_EdgeVisibleFromFirstCheckpoint` | R07 appears at both 2.0 and 2.55, in both directions (incoming and outgoing labels). |
| `Projection_EdgeBeginsLaterWithVisibleEndpoints` | R13 is absent at 2.0 although Alphinaud and Louisoix are visible (shared with WE-1). |
| `Projection_NoDerivedEdges` | At 2.0, Alphinaud's neighbors include Alisaie but not Louisoix, despite R07 + R12. |
| `Validation_RejectsReverseDuplicateOfSymmetricEdge` | Adding Alisaie → twin-of → Alphinaud alongside R07 is rejected or normalized. |
| `State_RaisingCeilingDoesNotAdvanceView` | Raising the ceiling from 2.0 to 2.55 leaves the view at 2.0. |
| `State_LoweringCeilingClampsView` | Ceiling 2.0 forces view 2.0. |
| `State_UnknownSavedCheckpointResetsToEarliest` | A saved ID such as `cp-hw-3-0` resets both controls to `cp-arr-2-0`. |

## Coverage

All three examples use only the two pilot checkpoints and the 12-entity provisional roster. Together they cover both required changes:

- **Description change:** WE-2.
- **Relationship change:** WE-1.

The remaining contract tests (bounds, malformed or missing data, unsupported schema version, draft vs. strict review modes) do not depend on lore and use generic synthetic fixtures.
