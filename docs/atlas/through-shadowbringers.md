# The Atlas through Shadowbringers (5.0–5.55)

> **Status: on the branch, 2026-11-19, with no story card** (Atlas content skips the story workflow, as for
> [Heavensward](through-heavensward.md) and [Stormblood](through-stormblood.md)). The new records are marked
> `reviewed` by the lead after verification. Nothing here was played in game.

## Coverage

| | Through Stormblood | Through Shadowbringers |
|---|---|---|
| Story points | 440 | **597**: one per quest to *On Official Business* (#697), plus the 5.0 and 5.55 milestones |
| Arcs | 62 | **95** |
| Entities | 268 | **358** (276 with portraits) |
| Relationships | 962 | **1363** |
| Claims (verbatim locators) | 2,967 | **4,338** |
| `atlas.json` | about 2.9 MB | about 3.9 MB (cap 8 MiB) |

The timeline is `tools/atlas/timeline_5x.py`: 155 steps in the wiki's list order, which keeps each parallel path
together (the Kholusia and Amh Araeng chains from #545, the three pixie errands at #570). *Shadowbringers* and *Death
Unto Dawn* are the milestones `cp-shb-5-0` and `cp-shb-5-55`.

## Method

Same pipeline as before ([era-modules.md](era-modules.md)):

1. The raw wikitext of all 157 quests was saved once.
2. **26 Haiku 5.5 research lanes** read the pages; the lead re-checked **all 1,531 lane quote fragments** by script, and every one matched.
3. **Five Opus era authors** wrote one module each (5.0 in three parts, 5.1–5.3, 5.4–5.55).
4. **Integration (lead):** the Lightwardens start at their own quest (#563) and Halric at his first mention (#551b);
   Hydaelyn's First-side records, drafted by parts 2 and 3, are adopted; Eline's service to Varis ends at his murder
   (#657); an alias that clashed with the Source's Matoya and an arc name that matched a later quest title were fixed.
5. **Verification:** `--verify-locators` matches **all 4,053 post-2.0 claims (4,222 fragments)** against the saved pages,
   none from optional dialogue or a branch line; `--lint` passes; the host tests pass.

## Arcs added

| Era | Arc | Steps |
|---|---|---|
| 5.0 part 1 | *Answering the Summons* | The Syrcus Trench → Travelers of Norvrandt |
| 5.0 part 1 | *Behind Eulmore's Gate* | In Search of Alphinaud → Emergent Splendor |
| 5.0 part 1 | *The Inn at Journey's Head* | In Search of Alisaie → Tears on the Sand |
| 5.0 part 1 | *Night over Lakeland* | The Lightwardens → Warrior of Darkness |
| 5.0 part 1 | *The Laxan Loft Rescue* | An Unwelcome Guest → The Oracle of Light |
| 5.0 part 1 | *The Pixies' Games* | Il Mheg, the Faerie Kingdom → Courting Cooperation |
| 5.0 part 1 | *The Sealed King* | The Key to the Castle → The Lawless Ones |
| 5.0 part 2 | *The Throne of Lyhe Ghiah* | The Elder's Answer → Acht-la Ormh Inn |
| 5.0 part 2 | *The Ascian's Offer* | The Wheel Turns → Into the Dark |
| 5.0 part 2 | *Darkness in the Greatwood* | A Day in the Neighborhood → An Unwanted Proposal |
| 5.0 part 2 | *Allies of Ronka* | Put to the Proof → Legend of the Not-so-hidden Temple |
| 5.0 part 2 | *The Warden of the Greatwood* | The Aftermath → Out of the Wood |
| 5.0 part 2 | *The Siege of the Crystarium* | When It Rains → The Best Way Out |
| 5.0 part 2 | *The Road to Nabaath Areng* | Free Trade → The Truth Hurts |
| 5.0 part 2 | *The Oracle's Fork in the Road* (renamed 2026-11-19: 7.1 has a quest called Crossroads) | A Convenient Distraction → Crossing Paths |
| 5.0 part 3 | *The Last Foothold* | A Fresh Start → The Ladder |
| 5.0 part 3 | *A Talos for Mt. Gulg* | The View from Above → Rich Veins of Hope |
| 5.0 part 3 | *The Final Warden* | That None Shall Ever Again → In His Garden |
| 5.0 part 3 | *Beneath the Tempest* | The Unbroken Thread → The Illuminated Land |
| 5.0 part 3 | *Amaurot* | The End of a World → Shadowbringers — Patch 5.0 complete |
| 5.1–5.3 | *Souls Adrift* | Shaken Resolve → Good for the Soul |
| 5.1–5.3 | *The Missing Mayor* | Nowhere to Turn → Moving Forward |
| 5.1–5.3 | *An Emperor Slain* | Vows of Virtue, Deeds of Cruelty → The Way Home |
| 5.1–5.3 | *The False Hero* | Seeking Counsel → Deep Designs |
| 5.1–5.3 | *Records of the Ancients* | A Whale's Tale → In the Name of the Light |
| 5.1–5.3 | *The Emissary Unmasked* | Heroic Dreams → Etched in the Stars |
| 5.1–5.3 | *The Exarch's Vigil* | The Converging Light → The Journey Continues |
| 5.1–5.3 | *A Long Way Home* | Unto the Morrow → The Wisdom of Allag |
| 5.4–5.55 | *The Tempering Cure* | Reviving the Legacy → Like Master, Like Pupil |
| 5.4–5.55 | *The Admiral's Peace* | The Admiral's Resolve → The Great Ship Vylbrand |
| 5.4–5.55 | *The Towers Rise* | Futures Rewritten → Here Be Dragons |
| 5.4–5.55 | *Tiamat's Atonement* | Righteous Indignation → When the Dust Settles |
| 5.4–5.55 | *One Banner for Eorzea* | The Company We Keep → Shadowbringers — Patch 5.55 complete |

## Decisions

- **Shadowbringers terms open from the step the pages establish them**, the earliest any era found: Exarch and "the
  First" (#542), Oracle of Light (#543), Lightwarden (#563), Emet-Selch (#584), Zodiark (#603), Ryne (#620),
  Hythlodaeus (#646), Hades (5.0). Surnames, "Endwalker" and "Shadowbringers" (outside citation titles) stay out.
- **Reveals** follow Marques → Cid: the enigmatic figure → the Crystal Exarch (#542) → G'raha Tia (#639); Solus →
  Emet-Selch (#584) → Hades (5.0); the girl called Minfilia is her own entry, named Ryne from #620; the white-robed
  figure → Fandaniel (#679). Earlier names stay searchable as aliases.
- **Portraits:** 63 new picks. The Crystal Exarch, the white-robed figure and Fandaniel have none, because a face
  would give away who they are; Vauthry, Venat and Zodiark have none because their only cards show later forms.
- **The per-entity presentation bound rose to 512** (Alisaie has 122 records through 5.55).
- **The host suite now takes over 10 minutes**: the real-timeline sweep scales with the step count.

## Known gaps

- The Changes lens isn't offered on the step after a milestone (#542, #648), as before.
- MSQ #1–#101 is still not covered.
