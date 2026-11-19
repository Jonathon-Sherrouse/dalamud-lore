# Atlas era modules (patches 2.1–3.56)

Starting 2026-11-19, the Atlas covers every main-scenario quest through *A Requiem for Heroes* (4.56). The content after
2.0 lives in data-only Python modules under `tools/atlas/`, one per era. `build_pilot_content.py` merges them with
the accepted content (the pilot, A4 and NDL-012), emits `atlas.json` and the review sheets, and lints them.

| Module | Era | Steps it may start records on | Arc tag |
|---|---|---|---|
| `content_2_1_to_2_3.py` | 2.1 *A Realm Awoken* to 2.3 *Defenders of Eorzea* | `cp-msq-162` … `cp-msq-199` | `c` |
| `content_2_4_to_2_55.py` | 2.4 *Dreams of Ice* to 2.55 *Before the Fall* | `cp-msq-200` … `cp-arr-2-55` | `d` |
| `content_3_0_part1.py` | 3.0, *Coming to Ishgard* to *New Winds, Old Friends* | `cp-msq-242` … `cp-msq-291` | `e` |
| `content_3_0_part2.py` | 3.0, *A General Summons* to *Heavensward* | `cp-msq-292` … `cp-hw-3-0` | `f` |
| `content_3_1_to_3_56.py` | 3.1 to 3.56 | `cp-msq-336` … `cp-hw-3-56` | `g` |
| `content_4_0_part1.py` | 4.0, *Beyond the Great Wall* to *Boys with Boats* | `cp-msq-380` … `cp-msq-418` | `h` |
| `content_4_0_part2.py` | 4.0, *To Bend with the Wind* to *The Hour of Reckoning* | `cp-msq-419` … `cp-msq-464` | `i` |
| `content_4_0_part3.py` | 4.0, *The Room Where It Happened* to *Stormblood* | `cp-msq-465` … `cp-sb-4-0` | `j` |
| `content_4_1_to_4_56.py` | 4.1 to 4.56 | `cp-msq-502` … `cp-sb-4-56` | `k` |

The timeline itself is `timeline_2x_3x.py` and, for Stormblood, `timeline_4x.py`: one step per quest, `cp-msq-<msq-index>`, with `b`/`c` suffixes where
parallel paths share an index (`cp-msq-234b`, `cp-msq-245b` … `cp-msq-251b`, `cp-msq-282b`, `cp-msq-282c`). Each step
means "after this quest". Each patch's last quest is a milestone instead of a step: `cp-arr-2-55` (after *Before the
Dawn*), `cp-hw-3-0` (after *Heavensward*), `cp-hw-3-56` (after *The Far Edge of Fate*), `cp-sb-4-0` (after *Stormblood*) and
`cp-sb-4-56` (after *A Requiem for Heroes*). The 2.0 milestone,
`cp-arr-2-0`, comes right before `cp-msq-162`.

## Commands

Run from the repository root:

```bash
python3 tools/atlas/build_pilot_content.py --lint content_2_4_to_2_55   # one era on top of the accepted content
python3 tools/atlas/build_pilot_content.py --lint                       # every era together
python3 tools/atlas/build_pilot_content.py --verify-locators <pages dir> # every era claim's locator against saved wikitext
python3 tools/atlas/build_pilot_content.py                              # write atlas.json and the review sheets
python3 tools/atlas/build_pilot_content.py --accept-pending             # record pending records' fingerprints (lead only)
```

`--lint` and `--verify-locators` write nothing. Then run `dotnet test NpcDialogueLinks.Tests`.

## Module contract

A module holds only data. Every name below is optional.

```python
def P(frm, until, scope, name, summary, claims, aliases=()):   # copy this helper
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

CLAIMS = {"M200a": ("Own-words claim.", "Traitor in the Midst", "verbatim locator from the wiki page")}
ENTITIES = {"char-ilberd": "character"}          # entities this era introduces: id -> character|organization|location|event
PRES = {"char-ilberd": [P("cp-msq-200", None, "main", "Ilberd", "...", ["M200a"])],
        "char-alphinaud": [P("cp-msq-200", None, "main", "Alphinaud", "...", ["M200b", "C10"])]}  # new or existing entities
TYPES = [("betrays", "betrays", "betrayed by", False)]   # new relationship types: (id, outgoing, incoming, symmetric)
RELS = [("rel-ilberd-member-crystal-braves", "char-ilberd", "member-of", "org-crystal-braves", "cp-msq-200", None, "main", ["M200a"])]
ADJUST = {"rel-scions-hq-waking-sands": {"until": "cp-msq-171"}}  # change an earlier relationship: frm, until, end
ARCS = [("arc-d1-the-braves-take-shape", "evt-the-braves-take-shape", "cp-msq-200", "cp-msq-210")]
CASTS = {"evt-the-braves-take-shape": [("char-alphinaud", "cp-msq-200", ["M200b"])]}   # member, from step, claims
ARC_NOTES = {"arc-d1-the-braves-take-shape": "Why the arc starts and ends where it does (review sheet)."}
DECISIONS = ["Editorial decisions worth reviewing, one Markdown line each."]
ALLOW = {}  # a banned term this era needs -> the first step it may appear (the lead must accept it)
```

### Merging rules

- **Presentations** of one entity and scope are sorted by step, and each one runs until the next one starts. Write
  `until=None` and let the merge close it. An earlier record, including an accepted one, is closed where yours begins.
  An entity never disappears once visible, and two presentations may not start on the same step.
- **Relationships** keep the interval you give. End one with `until` (the first step it no longer holds) and, if the
  reason is on the page, end claims as a ninth element: `(..., ["M210c"])`. End claims are shown only on that step's
  Changes row, so they can't end on a milestone or on the first step after one (`cp-msq-162`, `cp-msq-242`,
  `cp-msq-336`).
- **ADJUST** changes a relationship that the accepted content or an earlier module defined. It may set `frm`, `until`
  (a step in your era) and `end` (end claims). It never deletes one.
- **Arcs.** An arc's cast is at most 10 members, counted cumulatively over the arc. Arcs may share at most one step,
  because the Arc lens shows the earliest-started arc that contains the view, so a long arc hides any arc inside it.
  Each arc's entry is an `event` entity with one recap presentation per step: the "story so far", standing on its own.
  An era's last arc may end on its milestone.

### IDs

- Entities: `char-`, `org-`, `loc-` or `evt-`, then the lowercase first name or name, ASCII, hyphens for spaces, no
  apostrophes (`char-yshtola`, `char-kan-e-senna`, `org-crystal-braves`). Use exactly the existing IDs for anyone
  already in the Atlas (see `atlas.json`), and these for names that recur across eras:

  | Name | ID |
  |---|---|
  | Ishgard, Ul'dah, Limsa Lominsa, Gridania, Sharlayan, Doma | `loc-ishgard`, `loc-uldah`, `loc-limsa-lominsa`, `loc-gridania`, `loc-sharlayan`, `loc-doma` |
  | Revenant's Toll | `loc-revenants-toll` |
  | The Ironworks (never its full name) | `org-ironworks` |
  | The Ascians as a group | `org-ascians` |
  | The Immortal Flames, the Maelstrom, the Twin Adder | `org-immortal-flames`, `org-maelstrom`, `org-twin-adder` |
  | Ul'dah's Syndicate; the Monetarists | `org-syndicate`, `org-monetarists` |
  | Doman refugees | `org-doman-refugees` |
  | The Temple Knights; the Heavens' Ward; House Fortemps; the Holy See | `org-temple-knights`, `org-heavens-ward`, `org-house-fortemps`, `org-holy-see` |
  | The Dravanian Horde | `org-dravanian-horde` |
  | Beast tribes | `org-<tribe>`, as `org-ixal` (`org-sahagin`, `org-kobolds`, `org-amaljaa`, `org-sylphs`, `org-moogles`, `org-gnath`, `org-vanu-vanu`) |
  | Primals and dragons | `char-<name>`, as `char-titan` (`char-leviathan`, `char-ramuh`, `char-shiva`, `char-nidhogg` …) |
  | Ala Mhigo, Gyr Abania's resistance; Doma's people; the Xaela tribes | `loc-ala-mhigo`, `org-ala-mhigan-resistance`, `org-doman-refugees`, `org-<tribe>` (`org-mol`, `org-oronir`, `org-dotharl` …) |
  | Zenos (the 3.56 entry is `char-zenos`, named "The Viceroy") | `char-zenos` |

- Relationships: `rel-<source without prefix>-<type>-<target without prefix>`, with `-2`, `-3` for a later interval
  of the same triple. Arcs: `arc-<tag><n>-<slug>`. Claims: `M` + the step's number and suffix + a letter (`M200a`,
  `M245ba`). Existing claim IDs (`C…`, `K…`, `E…`) may be cited.

### Relationship types

Reuse these before adding one: `leads`, `member-of`, `twin-of`, `grandchild-of`, `headquartered-at`, `controls`,
`turned-against`, `conceals`, `participant-in` (arc casts only), `prisoner-of`, `possessed-by`, `serves`, `aids`,
`opposes`, `summoned-by`, `allied-with` (symmetric), `revealed-as`, `held-at`. A new type needs both labels in lower
case. If two modules add the same id, the labels must match exactly.

## Content rules

The host tests enforce these, and `--lint` checks them first.

1. **Evidence.** Every presentation and relationship cites 1–8 claims' worth of distinct sources. Each claim is
   in your own words, with a verbatim locator from the quest's saved wikitext: the Journal, Steps or main dialogue,
   never optional dialogue or conditional branches. ` … ` joins exact fragments of one page. A claim counts from its
   quest's step, so a record can cite only quests at or before its own step (a relationship's end claims, at or
   before its end).
2. **No memory.** Write only what the pages say. If nothing says where someone is, the Atlas doesn't either.
3. **Nothing ahead of the step.** Displayed text (names, aliases, summaries) must not contain:
   - the title of any later quest (case-sensitive, so watch common words: *Revolution*, *Choices*, *Consequences*,
     *Disclosure*, *Bloodlines*, *First Blood*, *Familiar Faces*, *Moving On*, *Still Waters*, *Heavensward*);
   - the name or alias of an entity that isn't visible yet. If your text names someone likely to become an Atlas
     entry, make them an entity visible by then;
   - surnames, or the names and phrases banned in `RealDataTests` (Nero, Lyse, "the First", "Word of the Mother",
     "Warriors of Darkness", Nabriales, Igeyorhm, Midas, Zodiark …) unless `ALLOW` proposes a first step for one
     and the lead accepts it;
   - wiki markup or placeholders (`[[`, `''`, `[Forename]`). Say "you" for the player.
4. **First names and titles only:** "Ser Aymeric", "Lord Haurchefant", "Captain Ilberd". The Ironworks, never its
   full name.
5. **Reveals as relationships.** When someone turns out to be someone else, keep the first entry, as with Marques →
   Cid: a second entity, a `revealed-as` edge from the reveal step, and the old name as an alias of the new entry
   from then on.
6. **Main scope only.** These modules cover the main scenario; leave optional scope to the accepted Binding Coil records.
7. **New text only on real change.** Give an existing entity a new presentation only when what the player knows
   about them changes. Each one reads on its own: who they are, then where things stand now.
8. **Bounds:** summary ≤ 1,200 characters (aim for 250–600), name and aliases ≤ 80, at most 8 aliases, at most 64
   presentations per entity.
