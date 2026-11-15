# Atlas data schema v2

> **v2 (NDL-006, 2026-11-14).** The loader accepts `schemaVersion: 2` only, and v1 files are rejected. v2 is a superset of v1: every v1 rule below still holds, and the additions are listed in [Schema v2 additions](#schema-v2-additions). The accepted pilot content was regenerated as v2, and its four snapshots are pinned identical to v1 (`RealDataTests.Real_AcceptedSnapshotsArePinnedAcrossTheV2Upgrade`). Product behavior lives in [v2-plan.md](v2-plan.md).

This is the contract the production loader in `NpcDialogueLinks/Atlas/` enforces. The v1 text below was frozen for the pilot. It is frozen from the [discovery evidence](discovery-evidence.md) and the [Atlas contract](../lore-relationship-atlas.md). The four-delegate council reviewed it on 2026-11-14 (see [Review record](#review-record)). Changing it during `NDL-003` requires the one bounded, versioned model-plus-tests amendment that the contract allows.

## File shape

```jsonc
{
  "schemaVersion": 2,
  "checkpoints": [                       // ordered, earliest first; 1–16
    { "id": "cp-arr-2-0", "label": "A Realm Reborn — Patch 2.0 complete" }
  ],
  "relationshipTypes": [                 // closed vocabulary; 1–32
    { "id": "member-of", "outgoingLabel": "member of", "incomingLabel": "has member", "symmetric": false },
    { "id": "twin-of",   "outgoingLabel": "twin of",   "incomingLabel": "twin of",    "symmetric": true }
  ],
  "entities": [                          // 1–64
    {
      "id": "char-example",
      "category": "character",           // character | organization | location
      "presentations": [                 // 1–32
        {
          "validFrom": "cp-arr-2-0",     // checkpoint id, inclusive
          "validUntil": null,            // checkpoint id, exclusive; null or absent = ongoing
          "scope": "main",               // main | optional
          "name": "Example",
          "aliases": [],                 // 0–8; absent = []
          "summary": "Original reviewed text.",
          "citations": [                 // 1–8
            { "title": "Quest title", "url": "https://…", "availableAt": "cp-arr-2-0", "scope": "main" }
          ],
          "review": "pending"            // pending | reviewed
        }
      ]
    }
  ],
  "relationships": [                     // 0–256
    {
      "id": "rel-example",
      "source": "char-example", "type": "member-of", "target": "org-example",
      "validFrom": "cp-arr-2-0", "validUntil": null,
      "scope": "main",
      "citations": [ { "title": "Quest title", "url": null, "availableAt": "cp-arr-2-0", "scope": "main" } ],
      "review": "pending"
    }
  ]
}
```

Unknown properties, comments, trailing commas and duplicate keys are rejected. The whole file is limited to 1 MiB. An absent `validUntil` or `url` means the same as `null`; absent `aliases` means `[]`.

## Field limits

- **IDs:** lowercase kebab-case (`^[a-z0-9]+(-[a-z0-9]+)*$`), at most 64 characters, unique within their collection.
- **Text lengths:**

  | Field | Max characters |
  |---|---|
  | Checkpoint label, type labels, names, aliases | 80 |
  | Summary | 1200 |
  | Citation title | 200 |

  Every text field must be non-empty after trimming.
- **Aliases:** must be unique ignoring case and must not repeat the presentation's name.
- **Citation URL:** an absolute `http` or `https` URL of at most 2048 characters with no fragment (`#…`) and no user info. It may also be `null`, in which case the citation is shown as text only.
- **Symmetric types** must use identical outgoing and incoming labels.

## Semantics

### Intervals

- An interval is `[validFrom, validUntil)` over checkpoint order. `validUntil`, when present, must be later than `validFrom`, so every interval contains at least one checkpoint.
- History that falls entirely between two checkpoints is described in text, never encoded as an interval.

### Scopes and views

**Views**
- There are two content views. **MainStory** uses only `main` records. **MainAndOptional** uses both. This follows the [available-content rule](../lore-relationship-atlas.md#research-and-content-rules).
- **Visibility.** An entity is visible in a view at checkpoint *c* exactly when a presentation whose scope that view includes covers *c*. A relationship is visible under the same test on its own interval and scope.
- A main record is visible in both views. Because of this, visibility is monotonic: anything visible in MainStory is visible in MainAndOptional.

**What `optional` means**
- **Relationships:** `scope: optional` means only eligible optional content supports the relationship at its `validFrom`.
- **Presentations:** `scope: optional` marks the MainAndOptional text for an entity. It includes, or continues from, optional-only knowledge. It may also cite main sources, because it restates main-story context.

**Presentations**
- **Optional replaces, never merges.** In MainAndOptional, an `optional` presentation that covers a checkpoint replaces the `main` one there. It replaces every field: name, aliases, summary and citations. Nothing is inherited from the main presentation, so it must describe the entity completely, restating any main-story context it still needs.
- **Fallback.** Where no optional presentation covers a checkpoint, MainAndOptional uses the main presentation.
- **Optional-only entities.** An entity whose only presentations are `optional` is hidden in MainStory.

**Relationships**
- Optional relationships only add edges in MainAndOptional. They cannot hide, end or replace a main relationship; retraction would be a v2 change.
- If the main story later confirms an optional relationship, end the optional record and start a `main` record for the same triple.

**Pre-toggle default view** (user decision, 2026-11-14). Until a content-view control ships, the runtime uses **MainAndOptional**, as the available-content rule requires.

### Presentation validation

- **No same-scope overlap.** Two presentations of the same scope must not cover the same checkpoint.
- **Optional follows main boundaries.** Each `optional` presentation must either sit entirely inside one `main` presentation's interval, or cover only checkpoints that no `main` presentation covers. This stops it carrying stale text across a main-story change.
- **Optional persists.** Once an `optional` presentation covers a checkpoint, every later checkpoint where the entity is visible in MainAndOptional must also be covered by an `optional` presentation. This stops optional knowledge silently dropping out.
- **No gaps.** In each view, no checkpoint between an entity's first and last visible checkpoint may be missing. Stopping or starting coverage at either end is allowed.

### Relationship validation

- **Basic references.** Both endpoints must exist and differ, and the type must exist.
- **Endpoint visibility.** For every checkpoint in the interval, both endpoints must be visible in every view that shows the relationship. That means both views for `main` relationships and MainAndOptional for `optional` ones.
- **No duplicates.** The same `(source, type, target)` must not appear with overlapping intervals, whatever the scopes.
- **Symmetric types.** A symmetric type is stored once, in one direction. The reversed pair is rejected regardless of interval, so a citation split keeps the stored direction.

### Citation validation

Each citation must be safe to show everywhere its record is shown.

- **Timing.** `availableAt` names the earliest checkpoint at which the cited source is player knowledge, and it must be at or before the record's `validFrom`. Evidence for why an interval *ends* is therefore never a citation on that record; cite it on the later records instead.
- **Scope.** A `main` record may cite only `main` citations. An `optional` record may cite either scope.
- **Consistency.** Citations with the same title must agree on `availableAt` and `scope` across the whole file. One mis-declared copy of a source is then a validation error.
- **Splitting.** To change a record's citations partway through, split it into adjacent records for the same triple or entity. They do not overlap, so this passes the duplicate rule.

### Review modes

- **Draft:** `pending` is allowed.
- **Strict:** every presentation and relationship must be `reviewed`. The runtime always loads in Strict mode.

### Loading and projection

**Loading**
- Loading never throws. A failed load returns structured errors and no dataset.

**Projection**
- `Project(dataset, viewCheckpoint, contentView)` is pure. It filters before anything else: entity lists, search (over names and aliases), counts, neighborhoods, and citations.
- A snapshot holds no reference to hidden records. It exposes no interval bounds.
- The Atlas never derives relationships that are not authored.

**Neighborhoods**
- Incoming and outgoing relationships are listed in order: category (character, organization, location), then entity ID, then relationship ID.
- At most 8 distinct neighbor entities go on the canvas. The full neighbor list is always complete.

## Spoiler-safety invariants

The validator enforces citation timing and scope. The rest is a content-review obligation for `NDL-003`.

- **Display text.** All displayed text and citation metadata must be safe at every checkpoint, and in every view, where the record appears. That covers names, aliases, summaries, citation titles and complete URLs.
- **IDs.** IDs are spoiler-neutral. They must not encode later identities or revelations, and they are never display text or a fallback label.
- **Relationship types.** Type labels reach the UI only through visible relationships. The UI never lists the type vocabulary as a legend or filter.
- **Errors.** The user-facing Atlas error is generic. Structured errors, which contain IDs and paths, go to the log only.
- **Scope of the guarantee.** It covers projected UI surfaces. The bundled `atlas.json` contains future records, and opening the file directly is outside it.

## Spoiler state

Two persisted checkpoint IDs:
- **ceiling:** knowledge approved through.
- **view:** viewing as of. Must be at or below the ceiling.

| Action | Result |
|---|---|
| Default state | Both at the earliest checkpoint. |
| Restore saved state | A missing or unknown ID, or a view above the ceiling, resets both to the earliest checkpoint. |
| Raise the ceiling | Needs explicit confirmation. The view does not move. |
| Lower the ceiling | Clamps the view down to it. |
| Set the view above the ceiling | Rejected. |

Every accepted change tells the UI to clear search, focus, selection and details. The content view is a projection parameter, not a third persisted control, until a toggle is approved.

## Schema v2 additions

**Checkpoints** gain optional fields:

| Field | Default | Rule |
|---|---|---|
| `milestone` | `false` | A patch milestone. Its label is neutral, so it may be listed above the spoiler limit. |
| `questTitle` | absent | A reviewed display title for a quest step; non-empty trimmed text of at most 80 characters. Shown only at or below the limit. |
| `contiguousWithPrevious` | `false` | The previous step is the quest immediately before this one. It must be false on the first checkpoint. |
| `gameQuestIds` | `[]` | 0–8 distinct positive game quest ids whose completion marks the step complete. Used only by Follow. Coverage is all-or-none: once any checkpoint has ids, every checkpoint must, and no id may mark two checkpoints. |

**Category `event`.** A story event or an arc entry. It is ordered last and drawn as a hexagon.

**`endCitations`** (relationships, optional, at most 8) hold reviewed evidence for why a relationship ended. The relationship must have a `validUntil`. Each citation must become available after `validFrom` and no later than `validUntil`. The scope rule (a main record cites only main sources) and the same-title consistency rule apply. They are shown only in the Changes row for that ending, never on the record elsewhere, and never in the Arc lens. So the ending step must be one where Changes is offered: `validUntil` and the step before it must be the same kind (both slices or both milestones).

**`arcs`** (top level, optional, at most 16). Each arc is `{ "id", "entityId", "firstStep", "lastStep" }`, in authored order. Arcs may overlap or nest. Validation:
- The relationship type `participant-in` must exist and must not be symmetric. A `participant-in` edge that targets an arc entry makes its source part of that arc's cast.
- The entry is an `event` entity used by only one arc, and all its presentations are main scope.
- `firstStep` is at or before `lastStep`, and `firstStep` is never the first timeline step, so there is always a baseline before it.
- The entry's first presentation starts exactly at `firstStep`, and the entry stays visible in the main-story view through `lastStep`.
- Every `participant-in` edge to the entry is main scope, starts at or after `firstStep`, and has no `validUntil`. The cast only grows.
- An arc has at most 10 participants at any step; the entry itself is not counted. Overflow fails as `CastTooLarge`.

**New error codes:** `InvalidArc`, `CastTooLarge`, `EndCitationOutOfRange`.

**Spoiler state in v2.**
- The limit rises only to a milestone or to the single next step.
- Pickers above the limit list only milestones and that next step, which is labelled "the next story step".
- `AtlasSession.PendingCeilingPrompt` never names a later quest. Front ends read the pending raise only through `PendingCeilingId` and that prompt.
- Absent or invalid saved state resets both controls to the earliest checkpoint.

**Pure v2 core:**
- `AtlasChanges`: the triple-based snapshot diff, the offering rule and labels.
- `AtlasArcs`: selection, the picker, and the Arc-lens projection with its cumulative cast, "New" and "Ended so far" (rows carry no citations of any kind). `Resolve` reports `PickDropped` when an explicit pick ends because the view fell below its first step; the session must then clear the pick.
- `AtlasFollow`: completed-progress positioning. `CheckpointId` is the clamped view and `ReachedCheckpointId` the real progress step; `AtlasSpoilerPolicy.SetCeilingToFollowed` raises the limit to exactly that step, with confirmation, and leaves the view where it is.
- `AtlasGraphLayout.ComputeWholeCast`.

Arc spans stay internal: the public arc API exposes only ids and names (rule 7).

## Review record

Round 1 (2026-11-14):

| Delegate | Verdict |
|---|---|
| Claude Opus 5.5 | changes requested |
| Claude Fable 5.2 | changes requested |
| GPT Sol | agree |
| GPT Astra | agree |

Adopted:
- **Citation fields.** Citation `availableAt` and `scope` (Opus, blocking). Fable proposed the same rule as non-blocking; Astra and Sol preferred no per-citation fields. The lead chose the field because the evidence matrix already planned a later-quest citation on a 2.0-only edge (R08).
- **Optional presentation rules.** Optional follows main boundaries (Fable, blocking). Optional persists (Opus).
- **Contract sync to per-view semantics** (Fable, blocking).
- **Clarifications from all four:**
  - whole-record replacement, add-only optional relationships, and the meaning of `optional`;
  - cross-scope duplicates;
  - gap wording;
  - the leak-surface invariants;
  - URL fragments and user info rejected;
  - absent fields equal `null`.

Round 2 (2026-11-14): **all four agreed.**

| Delegate | Round 1 | Round 2 |
|---|---|---|
| Claude Opus 5.5 | changes requested | agree |
| Claude Fable 5.2 | changes requested | agree |
| GPT Sol | agree | agree |
| GPT Astra | agree | agree |

The round-2 non-blocking notes were applied without a further round:
- **Opus:** per-view wording in WE-2, a single visibility definition, and a citation-URL typo.
- **Fable:** split `optional` definitions, citation title consistency, the presentation cap raised to 32 (two per checkpoint at the 16-checkpoint bound), stale evidence lines, and four extra planned tests.
- **Symmetric rule:** Opus proposed comparing endpoints unordered; Fable proposed rejecting the reversed pair regardless of interval. The lead took Fable's version, which is simpler, keeps the stored direction fixed, and matches the user's original decision.

**v2 candidate (Opus), not needed for the pilot:** the persistence rule means an optional presentation can never stop, even after the main story catches up, and splitting a main presentation forces its optional twin to split. The cost is mechanical duplication, not spoiler risk.
