# Atlas content review sheet

> **Status: REVIEWED.** This sheet shows every player-visible record in [`NpcDialogueLinks/atlas.json`](../../NpcDialogueLinks/atlas.json), exactly as written there, with the evidence behind it. Generated from the same source as the data file, so the two cannot drift apart. AI research and AI review are not canon acceptance: only your explicit approval marks these records `reviewed`.

How to read it:

- **Main** text is what the main-story view shows. **Optional** text replaces it in the default *main + optional* view, because it includes optional Binding Coil quests that are doable and released by that patch (the [available-content rule](../lore-relationship-atlas.md#research-and-content-rules)).
- Each claim quotes a short locator from the Console Games Wiki transcription of that quest, so you can find it. Patch numbers are when the quest was released, which sets the earliest checkpoint where the claim counts.
- Every source links to its quest page on the Console Games Wiki. The Atlas warns before opening it, because those pages list NPCs by full name and can mention later patches.

## Decisions recorded

The user decided these on 2026-11-14:

1. **Source links: on.** Every citation links to its quest page. The [citation audit](content-evidence.md#citation-safety) found that most quest pages list NPCs by full name ("Warde", and "Leveilleur" from 2.2), so the link opens only behind the Atlas's external-page spoiler warning. Each URL names only the quest itself.
2. **Alisaie as a Scion (R14, optional only): keep.** Its only direct support is the optional *Alisaie's Pledge* journal calling her "the young Scion" (C30).
3. **Alphinaud as Louisoix's grandchild (R13, optional, from 2.55): keep.** It rests on two optional lines read together: Louisoix was Alisaie's grandsire (C13, 2.0), and Alphinaud speaks of "our grandsire" shared with his sister (C26, 2.2).

For arc A4 (`NDL-009`), the user decided on 2026-11-14:

4. **The arc:** A4, MSQ #155 *Escape from Castrum Centri* to #161 *The Ultimate Weapon*, with #154 as the baseline ([v2-discovery.md](v2-discovery.md)).
5. **The cast of 10:** Minfilia, Thancred, Alphinaud and the Scions (already in the Atlas); Cid, Gaius, Livia, Lahabrea and the Eorzean Alliance (new); and the Operation Archon event. The plan's caps were raised by one each: five new entities instead of four, and four new relationship types instead of three (*part of*, *prisoner of*, *possessed by*, *serves*).

Lead decisions, confirmed by the user with the content on 2026-11-14:

6. **First names only**, as in the pilot: Gaius, Livia, Cid. Cid's company is "the Ironworks", never its full name.
7. **Slice steps name only the cast.** Text at #154–160 never names a character the slice doesn't cover (such as Tataru or Y'shtola), because the leak sweep can't tell "met before #154" from "not met yet". Raubahn and Rhitahtyn, who are not Atlas entries, are named only from the quest where they appear.
8. **Current quest versions.** Patch 6.1 reworked *Operation Archon* and *The Ultimate Weapon* (the Lahabrea fight became a solo duty). The wiki transcribes the current versions, which is what a player sees today, so the evidence follows them.
9. **Lahabrea is never written as dead,** and Nero is left out: the 2.0 finale shows neither's end. Livia is written as dead, from Cid's "May her soul know rest" (K62).
10. **The arc's name, *The Black Wolf's Challenge*.** It reveals nothing past its first step: by the end of #155 the Black Wolf's ultimatum is already being debated (K26). It avoids reusing #156's quest title, *The Black Wolf's Ultimatum*.

For A Realm Reborn 2.0 before the Black Wolf (`NDL-012`), the user chose the scope on 2026-11-17 (MSQ #102–#154, with the step bound raised). The lead decided the rest, and it awaits your review; the reasoning is in [ndl-012-discovery.md](ndl-012-discovery.md#decisions-to-review):

11. **Five arcs**: *The Road to Titan* (#103–105), *The Fall of the Waking Sands* (#106–110), *The Search for the Enterprise* (#110–129, sharing #110 with the arc before), *Garuda's Barrier* (#130–141) and *The Road to Castrum Centri* (#142–154, stopping before #155 so the Black Wolf's Challenge stays the default there).
12. **The step bound rises from 16 to 128**: one step per main-scenario quest, both #150 paths included, ordered by MSQ index and then authored order.
13. **Marques is his own entry, with no portrait**, because Cid's portrait shows his later look. From #110 he is *revealed as* Cid, and Cid is searchable as "Marques".
14. **Rule 7 above is relaxed**: with #102–#160 covered, text names any entry that is already visible. The leak tests still forbid any name that isn't visible yet, and any later quest title (so the arcs are not named after #105's or #141's quests).
15. **Left out**, as before: Nero, and surnames. The Company of Heroes holds a "feast", because "banquet" is reserved for the 2.55 story.

## Snapshot overview

Visible records at each step, in the main-story view and the main + optional view. Slice steps (#…) cover only the characters involved in the story so far.

| Step | Entities (main) | Entities (+ optional) | Relationships (main) | Relationships (+ optional) |
|---|---|---|---|---|
| #102 After It Was a Very Good Year | 11 | 11 | 8 | 8 |
| #103 After In the Company of Heroes | 14 | 14 | 11 | 11 |
| #104 After As You Wish | 14 | 14 | 11 | 11 |
| #105 After Lord of Crags | 16 | 16 | 15 | 15 |
| #106 After All Good Things | 21 | 21 | 26 | 26 |
| #107 After You Can't Take It with You | 21 | 21 | 26 | 26 |
| #108 After Bringing out the Dead | 21 | 21 | 26 | 26 |
| #109 After Bury Me Not on the Lone Prairie | 21 | 21 | 26 | 26 |
| #110 After Eyes on Me | 25 | 25 | 35 | 35 |
| #111 After He Who Waited Behind | 25 | 25 | 35 | 35 |
| #112 After Cold Reception | 25 | 25 | 35 | 35 |
| #113 After The Unending War | 26 | 26 | 36 | 36 |
| #114 After Men of Honor | 26 | 26 | 36 | 36 |
| #115 After Three for Three | 28 | 28 | 39 | 39 |
| #116 After The Rose and the Unicorn | 29 | 29 | 40 | 40 |
| #117 After The Talk of Coerthas | 29 | 29 | 40 | 40 |
| #118 After Road to Redemption | 29 | 29 | 41 | 41 |
| #119 After Following the Evidence | 29 | 29 | 41 | 41 |
| #120 After In the Eyes of Gods and Men | 29 | 29 | 41 | 41 |
| #121 After The Final Flight of the Enterprise | 30 | 30 | 42 | 42 |
| #122 After Ye of Little Faith | 30 | 30 | 43 | 43 |
| #123 After Factual Folklore | 30 | 30 | 43 | 43 |
| #124 After The Best Inventions | 30 | 30 | 43 | 43 |
| #125 After Influencing Inquisitors | 30 | 30 | 43 | 43 |
| #126 After By the Lights of Ishgard | 30 | 30 | 43 | 43 |
| #127 After Blood for Blood | 30 | 30 | 44 | 44 |
| #128 After The Heretic among Us | 30 | 30 | 43 | 43 |
| #129 After In Pursuit of the Past | 30 | 30 | 44 | 44 |
| #130 After Into the Eye of the Storm | 31 | 31 | 47 | 47 |
| #131 After Sealed with Science | 31 | 31 | 47 | 47 |
| #132 After With the Utmost Care | 31 | 31 | 47 | 47 |
| #133 After A Promising Prospect | 31 | 31 | 47 | 47 |
| #134 After It's Probably Not Pirates | 31 | 31 | 47 | 47 |
| #135 After Representing the Representative | 31 | 31 | 47 | 47 |
| #136 After The Reluctant Researcher | 31 | 31 | 47 | 47 |
| #137 After Sweet Somethings | 31 | 31 | 47 | 47 |
| #138 After History Repeating | 31 | 31 | 47 | 47 |
| #139 After The Curious Case of Giggity | 31 | 31 | 47 | 47 |
| #140 After Better Late than Never | 31 | 31 | 47 | 47 |
| #141 After Lady of the Vortex | 32 | 32 | 53 | 53 |
| #142 After Reclamation | 34 | 34 | 61 | 61 |
| #143 After Casing the Castrum | 36 | 36 | 67 | 67 |
| #144 After Eyes on the Empire | 36 | 36 | 67 | 67 |
| #145 After Footprints in the Snow | 36 | 36 | 67 | 67 |
| #146 After Monumental Hopes | 36 | 36 | 67 | 67 |
| #147 After Notorious Biggs | 36 | 36 | 69 | 69 |
| #148 After Come-Into-My-Castrum | 37 | 37 | 71 | 71 |
| #149 After Getting Even with Garlemald | 37 | 37 | 71 | 71 |
| #150 After Drowning Out the Voices | 37 | 37 | 71 | 71 |
| #150b After Acting the Part | 37 | 37 | 71 | 71 |
| #151 After Dressed for Conquest | 37 | 37 | 71 | 71 |
| #153 After Fool Me Twice | 37 | 37 | 71 | 71 |
| #154 After Every Little Thing She Does Is Magitek | 37 | 37 | 71 | 71 |
| #155 After Escape from Castrum Centri | 39 | 39 | 76 | 76 |
| #156 After The Black Wolf's Ultimatum | 39 | 39 | 76 | 76 |
| #157 After Operation Archon | 40 | 40 | 80 | 80 |
| #158 After A Hero in Need | 40 | 40 | 80 | 80 |
| #159 After Hearts on Fire | 40 | 40 | 80 | 80 |
| #160 After Rock the Castrum | 40 | 40 | 78 | 78 |
| 2.0 A Realm Reborn — Patch 2.0 complete | 42 | 42 | 77 | 79 |
| 2.55 A Realm Reborn — Patch 2.55 complete | 44 | 44 | 79 | 82 |

## Arcs

### The Road to Titan (`arc-b1-road-to-titan`)

From #103 *After In the Company of Heroes* to #105 *After Lord of Crags*. MSQ #103 *In the Company of Heroes* to #105 *Lord of Crags*, with #102 as the baseline (the first timeline step). The Company of Heroes' test, Riol's secret and Titan's fall, ending with the first sight of Lahabrea beside imperial officers (E105e, K14). The Titan storyline starts before #102; the Atlas does not cover those quests.

| Step | Arc name | Recap | Recap status | Cast at this step |
|---|---|---|---|---|
| #103 | The Road to Titan | The Company of Heroes turned a feast at Costa del Sol into a test, weighing you by deeds rather than reputation. Its five chosen members have judged you a worthy challenger for the primal Titan, and Y'shtola, at your side, warns that the battle has yet to begin. Wheiskaet can tell you how to reach Titan's lair. | new recap | Y'shtola, The Company of Heroes, Titan (3) |
| #104 | The Road to Titan | Five members of the Company of Heroes judged you worthy to challenge the primal Titan. Wheiskaet sent you to Bronze Lake to find Riol, another former member, who guards the secret of how to reach Titan and stays hidden until he hears the right signal. He has answered yours. | new recap | Y'shtola, The Company of Heroes, Titan (3) |
| #105 | The Road to Titan | Riol revealed that the Company of Heroes reached Titan through a beastman aetheryte. Y'shtola stayed behind to keep it working, and you went on alone and struck Titan down in the Navel. Then imperial officers, Rhitahtyn among them, appeared with a figure called Lahabrea, who urged you on: your work is far from done. Y'shtola, troubled that the elusive Ascians would consort with the Empire, stayed behind to investigate. | new recap | Y'shtola, The Company of Heroes, Titan, Rhitahtyn, Lahabrea, The Garlean Empire (6) |

### The Fall of the Waking Sands (`arc-b2-fall-of-the-waking-sands`)

From #106 *After All Good Things* to #110 *After Eyes on Me*. MSQ #106 *All Good Things* to #110 *Eyes on Me*. The raid, Minfilia's capture and the church's sanctuary (E106b, K01), ending when Alphinaud names Marques as Cid (E110c). It shares #110 with the next arc, so overlapping arcs are proven in real content: at #110 the default is this arc (earliest started), and the picker offers both.

| Step | Arc name | Recap | Recap status | Cast at this step |
|---|---|---|---|---|
| #106 | The Fall of the Waking Sands | After Titan fell, Minfilia called you back to the Waking Sands, but imperial forces under Livia got there first. They came for the one who slew Ifrit and Titan, slaughtered many Scions, refused Minfilia's offer to surrender if the innocents were spared, and took her prisoner. The dying sylph Noraxia sent you to the church in eastern Thanalan, where Father Iliud took you in. | new recap | Minfilia, The Scions of the Seventh Dawn, The Waking Sands, Livia, The Garlean Empire, Noraxia, Iliud, Marques (8) |
| #107 | The Fall of the Waking Sands | Imperial forces under Livia raided the Waking Sands, slaughtered many Scions and took Minfilia prisoner. You have taken sanctuary at the church in eastern Thanalan with Father Iliud. There Marques, a survivor of Carteneau, mended a dead man's broken horologe as though his hands remembered the work, and Sister Eluned wondered whether its owner was a Garlean spy. | new recap | Minfilia, The Scions of the Seventh Dawn, The Waking Sands, Livia, The Garlean Empire, Noraxia, Iliud, Marques (8) |
| #108 | The Fall of the Waking Sands | Imperial forces under Livia raided the Waking Sands, slaughtered many Scions and took Minfilia prisoner. From the church in eastern Thanalan, where Father Iliud gave you sanctuary, you helped carry the fallen from the Waking Sands for their rites, and the church will see them to Thal's realm. | new recap | Minfilia, The Scions of the Seventh Dawn, The Waking Sands, Livia, The Garlean Empire, Noraxia, Iliud, Marques (8) |
| #109 | The Fall of the Waking Sands | Imperial forces under Livia raided the Waking Sands, slaughtered many Scions and took Minfilia prisoner. You returned the body of Noraxia, the sylph who died there, to her people in the Black Shroud, who mourned her as brave; Komuxio vowed vengeance on the imperials. The other fallen Scions now rest in the church's lichyard. | new recap | Minfilia, The Scions of the Seventh Dawn, The Waking Sands, Livia, The Garlean Empire, Noraxia, Iliud, Marques (8) |
| #110 | The Fall of the Waking Sands | Imperial forces under Livia raided the Waking Sands, slaughtered many Scions and took Minfilia prisoner. At the church that sheltered you, Marques felt watched, and a stranger attacked you in the lichyard; Father Iliud knew his sword for Garlean steel. Then Alphinaud arrived and named Marques as Cid, an engineer missing since the Calamity. Cid has no memory of his past, but he has joined Alphinaud. | new recap | Minfilia, The Scions of the Seventh Dawn, The Waking Sands, Livia, The Garlean Empire, Noraxia, Iliud, Marques, Alphinaud, Cid (10) |

### The Search for the Enterprise (`arc-b3-search-for-the-enterprise`)

From #110 *After Eyes on Me* to #129 *After In Pursuit of the Past*. MSQ #110 *Eyes on Me* to #129 *In Pursuit of the Past*: the hunt for Cid's airship through Coerthas and Ishgard's heresy crisis, ending when the Enterprise is found in the Stone Vigil (E129d). 20 steps.

| Step | Arc name | Recap | Recap status | Cast at this step |
|---|---|---|---|---|
| #110 | The Search for the Enterprise | At the church in eastern Thanalan, Alphinaud recognized Marques as Cid, an engineer missing since the Calamity. Cid has no memory of his past, but he has joined Alphinaud: the Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. It was last seen over Gridania. | new recap | Alphinaud, Cid, Garuda, The Ixal (4) |
| #111 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Cid still remembers nothing of his past. A tale says the ship flew northwest from Gridania toward Coerthas, and at Florentel's Spire you found Vortefaurt, who saw it pass. | new recap | Alphinaud, Cid, Garuda, The Ixal (4) |
| #112 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Vortefaurt saw the ship vanish over the mountains of Coerthas. The astrologers of Ishgard's Observatorium may have records, but Ser Ludovoix will not let an outsider read them, and Ishgard offers strangers no help. | new recap | Alphinaud, Cid, Garuda, The Ixal (4) |
| #113 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. The Observatorium's records may tell where it went, but they chart a war with the dragons that has raged for generations, and even after you saved a knight from heretics sworn to the dragons, they stay closed. An inquisitor, Guillaime, warned you to keep out of Ishgard's affairs. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime (5) |
| #114 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Ishgard's Observatorium won't open its records to an outsider, and Inquisitor Guillaime has warned you off. House Durendaire owes you for two good deeds, but Lord Portelaine will introduce you to the other High Houses only after a third. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime (5) |
| #115 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Seeking help from Ishgard's High Houses, you recovered a porter's stolen wares, and among them was a draconian rosary in a chest belonging to Lord Francel of House Haillenarte, a house whispered to be full of heretics. Lord Portelaine has told the inquisitors and warned you away from the house. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte (7) |
| #116 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. A draconian rosary found among Lord Francel's belongings has put him under suspicion of heresy, though his former servant swears he is innocent. Francel sent you with a letter to Lord Haurchefant of House Fortemps at Camp Dragonhead, who has promised to make inquiries about the ship. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant (8) |
| #117 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Lord Haurchefant of House Fortemps is making inquiries for you, but the High Houses have nothing to offer: all of Coerthas talks only of heretics. Since Inquisitor Guillaime arrived, countless have been found, even among Ishgard's elite, and the charge against Lord Francel has thrown House Haillenarte into chaos. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant (8) |
| #118 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Lord Haurchefant has found a witness to its flight, but he won't speak to anyone tied to an accused heretic. You saved Lord Francel at the Steel Vigil, where he hoped to prove his devotion. His heresy trial approaches, and his name, and yours with it, must be cleared first. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant (8) |
| #119 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. A witness to its flight won't talk until Lord Francel is cleared of heresy. Haurchefant believes the rosary against Francel was planted, and two parcels bound for Skyfire Locks each held another: a crude attempt to smear House Haillenarte. Francel's trial is at hand. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant (8) |
| #120 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. At Witchdrop, Inquisitor Guillaime ordered Lord Francel to prove his innocence by leaping from the cliff. You protected him, Haurchefant argued that someone was using the trials to set the houses against each other, and a heretic among the Temple Knights was exposed. Guillaime withdrew the charges, pending investigation. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant (8) |
| #121 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. With Lord Francel cleared, the witness spoke: the ship landed near the Stone Vigil before the Calamity, and the outpost is now held by Dravanian forces. Haurchefant has written to Lord Drillemont of Whitebrim Front to ask that you be let in, and Francel warns that those who tried to destroy his house are still unknown. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont (9) |
| #122 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, now held by Dravanian forces. At Whitebrim Front, Inquisitor Guillaime branded you untrustworthy and the Scions a defunct band the Empire had exterminated, and Lord Drillemont barred the way until the outpost is retaken and you declare your true intentions. Alphinaud means to earn his trust. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont (9) |
| #123 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, but Lord Drillemont of Whitebrim Front won't let you in, and Inquisitor Guillaime calls you untrustworthy. To win Drillemont's notice through his knights, you helped the cook feed the hungry barracks. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont (9) |
| #124 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, but Lord Drillemont of Whitebrim Front won't let you in. Cid built the infirmary a better alembic, but Inquisitor Guillaime warned the chirurgeons that your gifts serve an unknown end, and he seems to hate you and your companions. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont (9) |
| #125 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, but Lord Drillemont won't let you in, and Inquisitor Guillaime works against you. You heard he carried an injured knight, Joellaut, to the gates on the night he arrived, and Alphinaud suspects he has other reasons for hindering you. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont (9) |
| #126 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, but Lord Drillemont won't let you in. Retracing Joellaut's story of the inquisitor's first night, you found a frozen corpse in a chasm: the real Inquisitor Guillaime, murdered the day he arrived. The man you know by that name is an impostor, and his true identity and motives are unknown. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont (9) |
| #127 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil. The inquisitor who works against you is an impostor: Prunilla confessed he coerced her and condemned innocent people for carrying draconian rosaries, and that she planted some of his rosaries in shipments to Skyfire Locks. Convinced, Lord Drillemont will let you into the Stone Vigil once the impostor faces justice. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont (9) |
| #128 | The Search for the Enterprise | You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. At Snowcloak, Lord Drillemont named the false inquisitor the murderer of the real Guillaime. The impostor called all Ishgard complicit in the archbishop's lies, took the form of a dragon beside his Dravanian allies, and was defeated, warning that the dragons in the Stone Vigil, where the ship landed, would tear you apart. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont (9) |
| #129 | The Search for the Enterprise | Cid and Alphinaud need Cid's airship, the Enterprise, to reach Garuda, the primal the Ixal have summoned. In the Stone Vigil you found it beside a sleeping dragon, and the Ascian Lahabrea woke the beast, taunting that Garuda is stronger than any primal you have faced. While you held off the dragon, Alphinaud and Cid slipped aboard. Cid knows the ship, though he can't recall more, and it is in no state to weather Garuda's storm. | new recap | Alphinaud, Cid, Garuda, The Ixal, Guillaime, Francel, House Haillenarte, Haurchefant, Drillemont, Lahabrea (10) |

### Garuda's Barrier (`arc-b4-garudas-barrier`)

From #130 *After Into the Eye of the Storm* to #141 *After Lady of the Vortex*. MSQ #130 *Into the Eye of the Storm* to #141 *Lady of the Vortex*: the corrupted-crystal hunt and Garuda, ending when the Empire's weapon absorbs the primals and the Scions resolve to re-form (K11, E141f). Its name avoids #141's title, which may not appear before #141.

| Step | Arc name | Recap | Recap status | Cast at this step |
|---|---|---|---|---|
| #130 | Garuda's Barrier | The Enterprise is back in Cid's hands, but battered as it is, it can't survive the winds around the Howling Eye, Garuda's sanctuary. While the Seedseers house it for repairs, Cid plans to use a corrupted crystal to change the aspect of Garuda's wind barrier, and he has sent you to Lamberteint, a scholar he met while he lived as Marques. | new recap | Cid, Alphinaud, Garuda (3) |
| #131 | Garuda's Barrier | Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. The scholar Lamberteint lent you a warded pot to carry such a crystal safely, and sent you to his pupil Hahasako at Highbridge. | new recap | Cid, Alphinaud, Garuda (3) |
| #132 | Garuda's Barrier | Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. The crystal you broke from the Burning Wall, with Hahasako's help, is wind-aspected, so it would only strengthen the barrier. | new recap | Cid, Alphinaud, Garuda (3) |
| #133 | Garuda's Barrier | Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. The first crystal you found was wind-aspected and useless. Lamberteint's pupil Ceana has found a promising site at Pharos Sirius on the Isles of Umbra, and you found her in Aleport. | new recap | Cid, Alphinaud, Garuda (3) |
| #134 | Garuda's Barrier | Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. Lamberteint's pupil Ceana believes the Isles of Umbra hold such crystals, but the isles are closed, and the Yellowjackets speak of spirits and undead there. | new recap | Cid, Alphinaud, Garuda (3) |
| #135 | Garuda's Barrier | Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. The scholar Ceana believes the Isles of Umbra hold such crystals, and the isles are said to be haunted. Mimidoa gave you a writ of passage there in return for looking into the rumors, and Skyfryn, back from the isles, raves of a woman singing to him. | new recap | Cid, Alphinaud, Garuda (3) |
| #136 | Garuda's Barrier | Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. You crossed to the Isles of Umbra with a writ of passage, but the scholar Ceana fled back to the mainland in fear, and the gate guard, Davyd, can't give you a crystal. | new recap | Cid, Alphinaud, Garuda (3) |
| #137 | Garuda's Barrier | Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. On the Isles of Umbra, the guard Davyd will find you one if you help solve the island's mystery, and adventurers speak of an irresistible voice at the Ship Graveyard. | new recap | Cid, Alphinaud, Garuda (3) |
| #138 | Garuda's Barrier | Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. On the Isles of Umbra, Mimidoa lured a siren ashore and you drove her back into the depths. Davyd kept his word, but the crystal he gave you is fire-aspected and won't help against the wind. | new recap | Cid, Alphinaud, Garuda (3) |
| #139 | Garuda's Barrier | Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. Two crystals proved the wrong aspect. In Gridania, Hedyn told you a spriggan had devoured every corrupted crystal in the Twelveswood; you cut the last one from its gut, and it is ice-aspected. | new recap | Cid, Alphinaud, Garuda (3) |
| #140 | Garuda's Barrier | Cid has been repairing the Enterprise to pass Garuda's wind barrier. You brought him an ice-aspected corrupted crystal, his work is nearly done, and once it passes his tests, he says, nothing will stand between you and Garuda. This, he says, is what he was born to do. | new recap | Cid, Alphinaud, Garuda (3) |
| #141 | Garuda's Barrier | The Enterprise carried you to the Howling Eye, and on the way the Echo let you guide Cid through his lost memories of leaving Garlemald for Eorzea. You struck Garuda down, but her Ixali worshippers' belief raised her again, and her dying captives' cries summoned their own gods. Then Gaius, the Black Wolf, called forth an imperial weapon that seemingly absorbed all three primals. The Scions mean to re-form, and to destroy that weapon. | new recap | Cid, Alphinaud, Garuda, The Ixal, Titan, Gaius, The Garlean Empire, The Scions of the Seventh Dawn (8) |

### The Road to Castrum Centri (`arc-b5-road-to-castrum-centri`)

From #142 *After Reclamation* to #154 *After Every Little Thing She Does Is Magitek*. MSQ #142 *Reclamation* to #154 *Every Little Thing She Does Is Magitek*, including both #150 paths: rebuilding the Scions, finding Biggs and Wedge, and preparing the infiltration, ending when the armor is ready (K09). It stops before #155 so that the accepted Black Wolf's Challenge stays the default arc at #155 (see the discovery doc for the trade-off).

| Step | Arc name | Recap | Recap status | Cast at this step |
|---|---|---|---|---|
| #142 | The Road to Castrum Centri | After the Empire's weapon seemingly absorbed the primals, Alphinaud brought you and Cid back to the ruined Waking Sands to rebuild the Scions. Yda, who was away during the raid, learned that Papalymo and Minfilia were not among the dead, and Y'shtola has found that the captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. Alphinaud believes Gaius means to use Minfilia to understand the Echo. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri (7) |
| #143 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Y'shtola reasons they will be kept alive until the Empire finishes studying the Echo, so you are first going after two escapees, likely Biggs and Wedge, who fled a downed imperial airship and are being hunted in Coerthas. Meanwhile Gaius readies his weapon to purge the land of its gods. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge (9) |
| #144 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. First you are tracking two escapees, likely Biggs and Wedge, who fled a downed imperial airship in Coerthas. Imperial soldiers are hunting them too. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge (9) |
| #145 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. In the snows of Coerthas you found Wedge, one of two escapees from an imperial airship. Biggs went another way to draw their pursuers off and was last seen heading west. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge (9) |
| #146 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. In Coerthas you found Wedge, who escaped from the Empire, but Biggs drew their pursuers away and is still missing. He wasn't in the Fury's Gaze, and Wedge is still determined to find him. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge (9) |
| #147 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Yda and Y'shtola helped you rescue Biggs from imperial troops, so Cid's Ironworks crew is together again. Biggs and Wedge were taken to Castrum Centri too, and escaped by sabotaging an airship. Y'shtola suspects the raiders reached the Waking Sands by teleportation of the kind the Ascians use. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge (9) |
| #148 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. The stronghold is on high alert, so Cid means to march in disguised as imperial troops. At Revenant's Toll you recruited Glaumunt, who bears a grudge against the Empire and knows the castrum, while Y'shtola and Yda scout it. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge, Glaumunt (10) |
| #149 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Cid means to march in disguised as imperial troops. Through a drainage pipe, you overheard guards say the tribunus is obsessed with Minfilia, who they believe has a mystical power. Alphinaud is sure the captives are inside, and Glaumunt is seeking a suit of magitek armor. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge, Glaumunt (10) |
| #150 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Cid and Glaumunt are preparing to march in disguised as imperial troops, with a suit of magitek armor if one can be found. For Cid you took readings at a crystal cluster near Revenant's Toll, so that he can jam imperial communications, though he is reluctant to use the crystals' power. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge, Glaumunt (10) |
| #150b | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Glaumunt's plan is to send you into the castrum dressed as an imperial soldier, so you learned the imperial salute by watching the patrols. Cid is ready to jam imperial communications, and a suit of magitek armor is still needed. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge, Glaumunt (10) |
| #151 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. You, Biggs and Wedge will go in disguised as imperial soldiers. Sark Malark, a friend of Glaumunt's, had you take three sets of imperial gear for the three of you, and the smith Eginolf repaired them. All that's still missing is a suit of magitek armor. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge, Glaumunt (10) |
| #153 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. You, Biggs and Wedge will go in disguised as imperial soldiers. Glaumunt fed the imperials false word of insurgents to draw out a patrol, and with Cid's help you seized a magitek reaper. Biggs and Wedge are repairing it at Cid's workshop. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge, Glaumunt (10) |
| #154 | The Road to Castrum Centri | Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. You, Biggs and Wedge will go in disguised as imperial soldiers. Cid's crew restored the magitek reaper you seized, and after you fought off imperial troops sent to reclaim it, the armor works. The time has come to infiltrate Castrum Centri and rescue the imprisoned Scions. | new recap | Alphinaud, Cid, Yda, Y'shtola, Minfilia, The Scions of the Seventh Dawn, Castrum Centri, Biggs, Wedge, Glaumunt (10) |

### The Black Wolf's Challenge (`arc-a4-black-wolf`)

From #155 *After Escape from Castrum Centri* to 2.0 *A Realm Reborn — Patch 2.0 complete*. MSQ #155 *Escape from Castrum Centri* to #161 *The Ultimate Weapon* (the `cp-arr-2-0` milestone), with #154 as the baseline. It opens with the rescue that frees the Scions and reveals Thancred's possession (K20, C37), and runs through Operation Archon to the Praetorium, where Gaius is slain, the Ultima Weapon destroyed and Thancred freed (K73, C09). Boundaries per [v2-discovery.md](v2-discovery.md#proposed-arc-map).

| Step | Arc name | Recap | Recap status | Cast at this step |
|---|---|---|---|---|
| #155 | The Black Wolf's Challenge | You and Cid's crew broke into Castrum Centri and freed Minfilia and the captive Scions, but the escape revealed that the Ascian Lahabrea has possessed Thancred. The Empire has finished the Ultima Weapon, an ancient Allagan relic, and Gaius, the Black Wolf, has given Eorzea's leaders an ultimatum: submit to his power, or share the primals' fate. | new recap | Minfilia, Thancred, Alphinaud, The Scions of the Seventh Dawn, Cid, Gaius, Livia, Lahabrea, The Eorzean Alliance (9) |
| #156 | The Black Wolf's Challenge | Eorzea's leaders refused the Black Wolf's ultimatum and resolved to fight, with the Scions beside them. Thancred remains in the thrall of the Ascian Lahabrea; Minfilia believes destroying the Crystal of Darkness on his person may free him. The Empire still holds the Ultima Weapon, and Cid now serves as the Alliance's man in Ul'dah. | new recap | Minfilia, Thancred, Alphinaud, The Scions of the Seventh Dawn, Cid, Gaius, Livia, Lahabrea, The Eorzean Alliance (9) |
| #157 | The Black Wolf's Challenge | The Eorzean Alliance has launched Operation Archon, the largest counteroffensive in the realm's history. You led its first phase and slew Rhitahtyn, one of the Black Wolf's most trusted lieutenants, and the Maelstrom and the Order of the Twin Adder now move on imperial castra. The final aim is the Praetorium, where the Ultima Weapon is believed to be housed. Thancred is still possessed. | new recap | Minfilia, Thancred, Alphinaud, The Scions of the Seventh Dawn, Cid, Gaius, Livia, Lahabrea, The Eorzean Alliance, Operation Archon (10) |
| #158 | The Black Wolf's Challenge | Operation Archon's second phase is under way. While the Immortal Flames strike Castrum Meridianum as a diversion, your task is to slip inside and bring down the magitek field around the Praetorium, where the Ultima Weapon waits. First you raised the spirits of the Alliance troops at Camp Bluefog, who dread what may be the bloodiest battle in history. | new recap | Minfilia, Thancred, Alphinaud, The Scions of the Seventh Dawn, Cid, Gaius, Livia, Lahabrea, The Eorzean Alliance, Operation Archon (10) |
| #159 | The Black Wolf's Challenge | With the assault on Castrum Meridianum close, you helped General Raubahn rally the wavering garrison at the Ceruleum Processing Plant. The plan holds: while the Alliance strikes outside, you are to infiltrate the castrum and bring down the magitek field that shields the Praetorium and the Ultima Weapon. Thancred remains in the Ascian Lahabrea's thrall. | new recap | Minfilia, Thancred, Alphinaud, The Scions of the Seventh Dawn, Cid, Gaius, Livia, Lahabrea, The Eorzean Alliance, Operation Archon (10) |
| #160 | The Black Wolf's Challenge | You broke into Castrum Meridianum and, with Cid guiding you, brought down the magitek field around the Praetorium. Livia, the tribunus who captured the Scions, fought you and fell. The Praetorium can now be reached only aboard Cid's airship, the Enterprise, and what remains is to find and destroy the Ultima Weapon. Thancred is still possessed. | new recap | Minfilia, Thancred, Alphinaud, The Scions of the Seventh Dawn, Cid, Gaius, Livia, Lahabrea, The Eorzean Alliance, Operation Archon (10) |
| 2.0 | The Black Wolf's Challenge | Aboard the Enterprise you stormed the Praetorium. Gaius urged Cid to take up his father's mantle in the Empire, and Cid refused. The Black Wolf turned the Ultima Weapon on you and you laid it low; then the Ascian Lahabrea, who had quickened the weapon with the primals' life force, came for you himself, and you freed Thancred from his enthrallment. Gaius is slain and the Ultima Weapon destroyed. | new recap | Minfilia, Thancred, Alphinaud, The Scions of the Seventh Dawn, Cid, Gaius, Livia, Lahabrea, The Eorzean Alliance, Operation Archon (10) |

## Portraits

Each portrait is a game icon drawn from the player's own install at runtime; no image is stored in the repository or the package. The user approved every pick on 2026-11-15 from a page showing each crop beside its source image. Crop: centre x, y and size, as fractions of the image (size of its shorter side).

| Entity | Source in the game | Icon | Crop (x, y, size) |
|---|---|---|---|
| Minfilia | Triple Triad card #56 | 87056 | 0.52, 0.4, 0.75 |
| Thancred | Triple Triad card #46 | 87046 | 0.52, 0.4, 0.75 |
| Y'shtola | Triple Triad card #49 | 87049 | 0.5, 0.45, 0.75 |
| Urianger | Triple Triad card #50 | 87050 | 0.5, 0.42, 0.75 |
| Alphinaud | Triple Triad card #59 (shared with Alisaie), left half | 87059 | 0.3, 0.36, 0.55 |
| Alisaie | Triple Triad card #59 (shared with Alphinaud), right half | 87059 | 0.66, 0.4, 0.55 |
| Louisoix | Triple Triad card #60 | 87060 | 0.52, 0.38, 0.75 |
| Tataru | Triple Triad card #19 | 87019 | 0.42, 0.36, 0.72 |
| The Scions of the Seventh Dawn | Quest illustration, The Scions of the Seventh Dawn (2.0) | 100073 | 0.5, 0.5, 1.0 |
| The Crystal Braves | Quest illustration, Traitor in the Midst (2.4) | 100316 | 0.68, 0.55, 1.0 |
| The Waking Sands | none: keeps its category shape | – | – |
| The Rising Stones | Quest illustration, Build on the Stone (2.1) | 100177 | 0.62, 0.5, 1.0 |
| The Black Wolf's Challenge | Quest illustration, Escape from Castrum Centri (MSQ #155) | 100163 | 0.17, 0.5, 1.0 |
| Operation Archon | Duty art, Castrum Meridianum | 112016 | 0.37, 0.45, 1.0 |
| Cid | Triple Triad card #58 | 87058 | 0.48, 0.38, 0.75 |
| Gaius | Triple Triad card #64 | 87064 | 0.5, 0.38, 0.8 |
| Livia | Triple Triad card #31 | 87031 | 0.45, 0.42, 0.75 |
| Lahabrea | Triple Triad card #57 (the masked Ascian, as first seen) | 87057 | 0.5, 0.42, 0.75 |
| The Eorzean Alliance | Quest illustration, The Black Wolf's Ultimatum (MSQ #156) | 100164 | 0.5, 0.5, 1.0 |
| The Road to Titan | none: keeps its category shape | – | – |
| The Fall of the Waking Sands | none: keeps its category shape | – | – |
| The Search for the Enterprise | none: keeps its category shape | – | – |
| Garuda's Barrier | none: keeps its category shape | – | – |
| The Road to Castrum Centri | none: keeps its category shape | – | – |
| Yda | none: keeps its category shape | – | – |
| Papalymo | none: keeps its category shape | – | – |
| Titan | none: keeps its category shape | – | – |
| Rhitahtyn | none: keeps its category shape | – | – |
| Noraxia | none: keeps its category shape | – | – |
| Iliud | none: keeps its category shape | – | – |
| Marques | none: keeps its category shape | – | – |
| Garuda | none: keeps its category shape | – | – |
| Francel | none: keeps its category shape | – | – |
| Haurchefant | none: keeps its category shape | – | – |
| Guillaime | none: keeps its category shape | – | – |
| Drillemont | none: keeps its category shape | – | – |
| Biggs | none: keeps its category shape | – | – |
| Wedge | none: keeps its category shape | – | – |
| Glaumunt | none: keeps its category shape | – | – |
| The Company of Heroes | none: keeps its category shape | – | – |
| The Garlean Empire | none: keeps its category shape | – | – |
| House Haillenarte | none: keeps its category shape | – | – |
| The Ixal | none: keeps its category shape | – | – |
| Castrum Centri | none: keeps its category shape | – | – |

## Entities

### Minfilia (`char-minfilia`, character)

**#102–#105 · main**

> Leader of the Scions of the Seventh Dawn, who welcomed you at the Waking Sands. Like you, she has the Echo.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **C33** Minfilia has the Echo. *The Scions of the Seventh Dawn* (2.0, main): "That's right. I too possess the Echo."

</details>

**#106–#141 · main**

> Leader of the Scions of the Seventh Dawn, who has the Echo. When imperial forces under Livia raided the Waking Sands, she offered to surrender if the innocents were spared. Livia refused, and took her prisoner, wanting her for the Echo.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **C33** Minfilia has the Echo. *The Scions of the Seventh Dawn* (2.0, main): "That's right. I too possess the Echo."
  - **E106d** Minfilia offered to surrender if the innocents were spared. *All Good Things* (2.0, main): "I surrender myself, on the condition you spare the innocents."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **K02** Livia wants Minfilia for the Echo. *All Good Things* (2.0, main): "They say she also possesses the Echo. I cannot wait to hear her scream."

</details>

**#142–#148 · main**

> Leader of the Scions of the Seventh Dawn, taken prisoner when imperial forces under Livia raided the Waking Sands. She is held at Castrum Centri, an imperial stronghold in Mor Dhona, and Alphinaud believes Gaius means to use her to understand the Echo.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."
  - **E142c** Alphinaud believes Gaius means to use Minfilia to understand the Echo. *Reclamation* (2.0, main): "He means to use Minfilia to gain an understanding of the Echo."

</details>

**#149–#153 · main**

> Leader of the Scions of the Seventh Dawn, taken prisoner when imperial forces under Livia raided the Waking Sands, and held at Castrum Centri. Guards there say the tribunus is obsessed with her, and that she has a mystical power the Garleans lack.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Reclamation — main scenario quest (2.0); Getting Even with Garlemald — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."
  - **E149a** A guard wonders why the tribunus is so obsessed with Minfilia. *Getting Even with Garlemald* (2.0, main): "I do wonder, why is the tribunus so obsessed with this Minfilia woman?"
  - **E149b** The guards say Minfilia has a mystical power the Garleans lack. *Getting Even with Garlemald* (2.0, main): "They say she possesses some mystical power. Something we Garleans don't have."

</details>

**#154 only · main**

> Leader of the Scions of the Seventh Dawn, who has the Echo. When imperial forces under Livia raided the Waking Sands, they refused her surrender and took her prisoner. She and other captured Scions are held at Castrum Centri, and the Empire wants her for the Echo. Cid's crew is ready to break in and rescue them.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Come-Into-My-Castrum — main scenario quest (2.0); Every Little Thing She Does Is Magitek — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **C33** Minfilia has the Echo. *The Scions of the Seventh Dawn* (2.0, main): "That's right. I too possess the Echo."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **K02** Livia wants Minfilia for the Echo. *All Good Things* (2.0, main): "They say she also possesses the Echo. I cannot wait to hear her scream."
  - **K03** Minfilia and the other captured Scions are held at Castrum Centri. *Come-Into-My-Castrum* (2.0, main): "All evidence suggests that Minfilia and the others are being held captive at [[Castrum Centri]]."
  - **K09** Cid's crew restores a suit of magitek armor, and the time comes to infiltrate Castrum Centri and rescue the Scions. *Every Little Thing She Does Is Magitek* (2.0, main): "you are now the proud owner of a fully functional suit of magitek armor. … At long last, the time is come to infiltrate [[Castrum Centri]] and rescue the imprisoned [[Scions]]."

</details>

**#155 only · main**

> Leader of the Scions of the Seventh Dawn, who has the Echo. She was freed from Castrum Centri's storage tower in the rescue, but during the escape the Scions learned that Thancred has been possessed by the Ascian Lahabrea.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **C33** Minfilia has the Echo. *The Scions of the Seventh Dawn* (2.0, main): "That's right. I too possess the Echo."
  - **K20** The rescue party frees the captives held in Castrum Centri's storage tower. *Escape from Castrum Centri* (2.0, main): "and the others are being held within the storage tower. … Though the rescue mission was a success"
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"

</details>

**#156–#160 · main**

> Leader of the Scions of the Seventh Dawn. She urged Eorzea's leaders to reject the Black Wolf's ultimatum, warning that his offer would doom the realm rather than deliver it, and they resolved to fight. She believes destroying the Crystal of Darkness on Thancred's person may free him from the Ascian who possesses him.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); The Black Wolf's Ultimatum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **K31** Minfilia argues that the Black Wolf's offer would doom Eorzea. *The Black Wolf's Ultimatum* (2.0, main): "That which the Black Wolf offers will doom Eorzea, not deliver it"
  - **K30** Eorzea's leaders resolve to fight, and burn the ultimatum. *The Black Wolf's Ultimatum* (2.0, main): "Eorzea's leaders have resolved to fight … The city-state leaders burn the ultimatum."
  - **K33** Destroying the Crystal that binds Thancred, somewhere on his person, may save him. *The Black Wolf's Ultimatum* (2.0, main): "The Crystal that binds Thancred must be somewhere on his person. … One such Crystal may yet be the key to saving Thancred."

</details>

**2.0 only · main** · Also searchable as: the Antecedent

> Leader of the Scions of the Seventh Dawn, who welcomes you at the Waking Sands. Like you, she has the Echo. She was taken prisoner when imperial forces raided the Waking Sands, and after her rescue from Castrum Centri she leads the Scions again.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **C33** Minfilia has the Echo. *The Scions of the Seventh Dawn* (2.0, main): "That's right. I too possess the Echo."
  - **C36** The prisoners are Minfilia, Urianger, Papalymo and Tataru, whom Y'shtola calls "our fellow Scions". *Casing the Castrum* (2.0, main): "Minfilia, Urianger, Papalymo, and Tataru! … the Garleans took our fellow Scions prisoner"
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"

</details>

**2.55 onward · main** · Also searchable as: the Antecedent

> Leader of the Scions of the Seventh Dawn, who has the Echo. She led the Scions' move from the Waking Sands to the Rising Stones in Mor Dhona. When the Scions were accused of plotting the sultana's death at a royal banquet in Ul'dah, she stayed behind during the escape, saying that Hydaelyn was speaking to her. No one has heard from her since.

Sources shown: The Gifted — main scenario quest (2.1); Laying the Foundation — main scenario quest (2.1); The Parting Glass — main scenario quest (2.55); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C45** The Waking Sands stops being the headquarters and passes to Urianger; Alisaie keeps working with him. *The Gifted* (2.1, main): "the Waking Sands will formally cease to be our headquarters, and the premises will be given into the care of Urianger. … Alisaie shall continue to work closely with him"
  - **C14** The Scions find a new home in Revenant's Toll, Mor Dhona. *Laying the Foundation* (2.1, main): "we have found ourselves a new home in Revenant's Toll"
  - **C50** At the banquet the Scions are accused of conspiring to poison the sultana, detained, and branded fugitives. *The Parting Glass* (2.55, main): "I hereby accuse you of regicide! … all members of the Scions of the Seventh Dawn will be detained for questioning … branded fugitives"
  - **C17** Minfilia stays behind, saying Hydaelyn speaks to her. *The Parting Glass* (2.55, main): "Hydaelyn... She speaks to me. … I must remain behind...but you cannot stay with me."
  - **C22** Every other Scion at the banquet is unaccounted for; Minfilia and the others do not respond. *Before the Dawn* (2.55, main): "every other Scion who attended the banquet remains unaccounted for … I tried contacting Minfilia and the others, but no one would respond"

</details>

### Thancred (`char-thancred`, character)

**#102–#153 · main**

> A Scion who serves as the order's man in Ul'dah, and who briefed your first investigation.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C39** Thancred is the Scions' man in Ul'dah and briefs the player's first investigation. *A Wild Rose by Any Other Name* (2.0, main): "He is our man here in Ul'dah, jewel of the desert. … Thancred, would you do the honors?"

</details>

**#154 only · main**

> A Scion who serves as the order's man in Ul'dah, and who briefed your first investigation.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C39** Thancred is the Scions' man in Ul'dah and briefs the player's first investigation. *A Wild Rose by Any Other Name* (2.0, main): "He is our man here in Ul'dah, jewel of the desert. … Thancred, would you do the honors?"

</details>

**#155 only · main**

> A Scion who serves as the order's man in Ul'dah. During the rescue at Castrum Centri, the Scions discovered that the Ascian Lahabrea has possessed him.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C39** Thancred is the Scions' man in Ul'dah and briefs the player's first investigation. *A Wild Rose by Any Other Name* (2.0, main): "He is our man here in Ul'dah, jewel of the desert. … Thancred, would you do the honors?"
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"

</details>

**#156–#160 · main**

> A Scion who serves as the order's man in Ul'dah, now in the thrall of the Ascian Lahabrea. Ascians possess mortals through Crystals of Darkness, and Minfilia believes destroying the Crystal on his person may save him.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0); The Black Wolf's Ultimatum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"
  - **K32** Ascians are immortal beings without physical form who possess mortals through Crystals of Darkness. *The Black Wolf's Ultimatum* (2.0, main): "the Ascians are immortal beings without physical form. … malign artifacts known as Crystals of Darkness."
  - **K33** Destroying the Crystal that binds Thancred, somewhere on his person, may save him. *The Black Wolf's Ultimatum* (2.0, main): "The Crystal that binds Thancred must be somewhere on his person. … One such Crystal may yet be the key to saving Thancred."

</details>

**2.0 only · main**

> A Scion and bard who serves as the order's man in Ul'dah and briefed your first investigation. During the rescue at Castrum Centri, the Scions learned that the Ascian Lahabrea had possessed him. You freed him from that enthrallment, and he came home with you.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0); The Ultimate Weapon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C39** Thancred is the Scions' man in Ul'dah and briefs the player's first investigation. *A Wild Rose by Any Other Name* (2.0, main): "He is our man here in Ul'dah, jewel of the desert. … Thancred, would you do the honors?"
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"
  - **C09** The player frees Thancred from Lahabrea's enthrallment, and he returns with them. *The Ultimate Weapon* (2.0, main): "free your comrade Thancred from his enthrallment … Look! Thancred is with him/her!"

</details>

**2.55 onward · main**

> A Scion and bard. At the royal banquet in Ul'dah he was arrested and accused of spying for the Garlean Empire. He led the escape through a hidden passage in the palace, then stayed behind with Y'shtola to stop the pursuit so the others could get away. He is unaccounted for.

Sources shown: The Parting Glass — main scenario quest (2.55); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C51** Thancred is accused of spying for the Empire, and leads the escape through a hidden passage. *The Parting Glass* (2.55, main): "You stand accused of committing acts of espionage in service to the Garlean Empire. … the passages hidden in the walls of the palace"
  - **C18** Y'shtola and Thancred stay behind to stop the pursuit. *The Parting Glass* (2.55, main): "You two go on ahead. Thancred and I will deal with this."
  - **C22** Every other Scion at the banquet is unaccounted for; Minfilia and the others do not respond. *Before the Dawn* (2.55, main): "every other Scion who attended the banquet remains unaccounted for … I tried contacting Minfilia and the others, but no one would respond"

</details>

### Y'shtola (`char-yshtola`, character)

**#102 only · main**

> A Scion who looks after Limsa Lominsa for the order, and who told you how the Scions were founded.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C40** Y'shtola looks after Limsa Lominsa for the order and tells how the Scions were founded. *A Wild Rose by Any Other Name* (2.0, main): "Limsa Lominsa has the pleasure of being under her care. … together established the Scions of the Seventh Dawn."

</details>

**#103–#104 · main**

> A Scion who looks after Limsa Lominsa for the order. She stood with you when the Company of Heroes judged you worthy to challenge Titan, and warns that the battle has yet to begin.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); In the Company of Heroes — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C40** Y'shtola looks after Limsa Lominsa for the order and tells how the Scions were founded. *A Wild Rose by Any Other Name* (2.0, main): "Limsa Lominsa has the pleasure of being under her care. … together established the Scions of the Seventh Dawn."
  - **E103b** Five members of the Company of Heroes judge you a worthy challenger. *In the Company of Heroes* (2.0, main): "We five of the Company of Heroes hereby judge you a worthy challenger."
  - **E103d** Y'shtola, with you at the feast, says the battle with Titan has yet to begin. *In the Company of Heroes* (2.0, main): "the battle with Titan has yet to begin."

</details>

**#105–#141 · main**

> A Scion who looks after Limsa Lominsa for the order. On the way to Titan she stayed behind to keep the aetheryte working while you went on alone. Afterwards, troubled that the elusive Ascians would consort with the Empire, she stayed behind to investigate.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Lord of Crags — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C40** Y'shtola looks after Limsa Lominsa for the order and tells how the Scions were founded. *A Wild Rose by Any Other Name* (2.0, main): "Limsa Lominsa has the pleasure of being under her care. … together established the Scions of the Seventh Dawn."
  - **E105b** Y'shtola stays behind at the aetheryte, so you go on alone. *Lord of Crags* (2.0, main): "It seems you will have to proceed without me, [Forename]."
  - **K14** The Ascians are elusive, and Y'shtola is troubled that they would consort with the Empire. *Lord of Crags* (2.0, main): "Well, the Ascians are nothing if not elusive. … But that they would choose to consort with the ''Empire''..."
  - **E105f** Y'shtola stays behind to investigate something before she leaves. *Lord of Crags* (2.0, main): "There is something I must investigate before I depart."

</details>

**#142 only · main**

> A Scion who looks after Limsa Lominsa for the order. She has learned that the Scions captured in the raid on the Waking Sands are held at Castrum Centri, an imperial stronghold in Mor Dhona.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C40** Y'shtola looks after Limsa Lominsa for the order and tells how the Scions were founded. *A Wild Rose by Any Other Name* (2.0, main): "Limsa Lominsa has the pleasure of being under her care. … together established the Scions of the Seventh Dawn."
  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."

</details>

**#143–#146 · main**

> A Scion who looks after Limsa Lominsa for the order. She found where the captured Scions are held, and insisted on gathering intelligence before any rescue. She reasons that the captives will be kept alive until the Empire finishes studying the Echo.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C40** Y'shtola looks after Limsa Lominsa for the order and tells how the Scions were founded. *A Wild Rose by Any Other Name* (2.0, main): "Limsa Lominsa has the pleasure of being under her care. … together established the Scions of the Seventh Dawn."
  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."
  - **E143a** Y'shtola wants intelligence first, from Lord Portelaine at the Observatorium. *Casing the Castrum* (2.0, main): "she suggests traveling to [[the Observatorium]] in [[Coerthas]], and there petitioning Lord [[Portelaine]] for aid."
  - **E143d** Y'shtola reasons the captives will not be executed until the study is complete. *Casing the Castrum* (2.0, main): "they will not be executed until such time as the study is complete."

</details>

**#147–#154 · main**

> A Scion who looks after Limsa Lominsa for the order. With Yda she helped you rescue Biggs from imperial troops, and she believes the raiders reached the Waking Sands by teleportation of the kind the Ascians use.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Notorious Biggs — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C40** Y'shtola looks after Limsa Lominsa for the order and tells how the Scions were founded. *A Wild Rose by Any Other Name* (2.0, main): "Limsa Lominsa has the pleasure of being under her care. … together established the Scions of the Seventh Dawn."
  - **E147a** With Yda and Y'shtola you rescue Biggs from imperial troops. *Notorious Biggs* (2.0, main): "With the aid of [[Yda]] and [[Y'shtola]], you succeed in rescuing Biggs from a detachment of imperial troops."
  - **E147b** Y'shtola believes the raiders arrived by teleportation of the kind the Ascians use. *Notorious Biggs* (2.0, main): "they were borne there by potent teleportation magicks─magicks of the kind used by the Ascians."

</details>

**#155–#160 · main**

> A Scion who looks after Limsa Lominsa for the order. During the rescue at Castrum Centri she and Yda rode in aboard your vehicle and confronted Livia, who led the raid on the Waking Sands.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C40** Y'shtola looks after Limsa Lominsa for the order and tells how the Scions were founded. *A Wild Rose by Any Other Name* (2.0, main): "Limsa Lominsa has the pleasure of being under her care. … together established the Scions of the Seventh Dawn."
  - **E155b** Y'shtola and Yda rode into the castrum aboard your vehicle. *Escape from Castrum Centri* (2.0, main): "There chanced to be a commotion outside the castrum's walls which allowed us to avail ourselves of the comforts of your vehicle."
  - **E155a** Y'shtola and Yda confront Livia, who led the raid on the Waking Sands. *Escape from Castrum Centri* (2.0, main): "'Twas you who led the raid on the Waking Sands─you who butchered unarmed men and women for the crime of being unworthy of capture."

</details>

**2.0 only · main**

> A Sharlayan Scion who looks after the order's affairs in Limsa Lominsa. She explains how the Scions came to be: after their leader was lost at Carteneau, they sought out Minfilia and others with the Echo. She helped plan the rescue of the Scions captured in the imperial raid.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C40** Y'shtola looks after Limsa Lominsa for the order and tells how the Scions were founded. *A Wild Rose by Any Other Name* (2.0, main): "Limsa Lominsa has the pleasure of being under her care. … together established the Scions of the Seventh Dawn."
  - **C36** The prisoners are Minfilia, Urianger, Papalymo and Tataru, whom Y'shtola calls "our fellow Scions". *Casing the Castrum* (2.0, main): "Minfilia, Urianger, Papalymo, and Tataru! … the Garleans took our fellow Scions prisoner"

</details>

**2.55 onward · main**

> A Sharlayan Scion. When the Scions fled the royal banquet in Ul'dah through a hidden tunnel, she and Thancred stayed behind, and she brought the tunnel down to stop their pursuers. She is unaccounted for.

Sources shown: The Parting Glass — main scenario quest (2.55); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C18** Y'shtola and Thancred stay behind to stop the pursuit. *The Parting Glass* (2.55, main): "You two go on ahead. Thancred and I will deal with this."
  - **C22** Every other Scion at the banquet is unaccounted for; Minfilia and the others do not respond. *Before the Dawn* (2.55, main): "every other Scion who attended the banquet remains unaccounted for … I tried contacting Minfilia and the others, but no one would respond"

</details>

### Urianger (`char-urianger`, character)

**#102–#142 · main**

> A Scion who presides over the affairs of the Waking Sands.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C41** Urianger presides over the affairs of the Waking Sands. *A Wild Rose by Any Other Name* (2.0, main): "Last but not least is Urianger, who presides over all affairs within these halls."

</details>

**#143–#154 · main**

> A Scion who presides over the affairs of the Waking Sands. Scouts saw him among four prisoners led into Castrum Centri.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C41** Urianger presides over the affairs of the Waking Sands. *A Wild Rose by Any Other Name* (2.0, main): "Last but not least is Urianger, who presides over all affairs within these halls."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."

</details>

**#155–#160 · main**

> A Scion who presides over the affairs of the Waking Sands. He was among the prisoners held at Castrum Centri, and was freed in the rescue.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C41** Urianger presides over the affairs of the Waking Sands. *A Wild Rose by Any Other Name* (2.0, main): "Last but not least is Urianger, who presides over all affairs within these halls."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **K20** The rescue party frees the captives held in Castrum Centri's storage tower. *Escape from Castrum Centri* (2.0, main): "and the others are being held within the storage tower. … Though the rescue mission was a success"

</details>

**2.0 only · main**

> A learned Sharlayan Scion who presides over the affairs of the Waking Sands. He was among the Scions taken prisoner in the imperial raid, and was freed in the rescue at Castrum Centri.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C41** Urianger presides over the affairs of the Waking Sands. *A Wild Rose by Any Other Name* (2.0, main): "Last but not least is Urianger, who presides over all affairs within these halls."
  - **C36** The prisoners are Minfilia, Urianger, Papalymo and Tataru, whom Y'shtola calls "our fellow Scions". *Casing the Castrum* (2.0, main): "Minfilia, Urianger, Papalymo, and Tataru! … the Garleans took our fellow Scions prisoner"
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"

</details>

**2.55 onward · main**

> A learned Sharlayan Scion who once studied under Louisoix. When the Scions moved to the Rising Stones, the Waking Sands was left in his care. After the royal banquet he hid it behind a glamour, so that it now looks like an abandoned storehouse and shelters those fleeing the Crystal Braves.

Sources shown: An Uninvited Ascian — main scenario quest (2.5); The Gifted — main scenario quest (2.1); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C54** Louisoix founded the Circle of Knowing, came to Eorzea, and spared the realm through his sacrifice; Urianger and Moenbryda studied under him. *An Uninvited Ascian* (2.5, main): "Moenbryda and I did study under the sage tutelage of Master Louisoix. … he founded the Circle of Knowing … Through his noble sacrifice was the realm spared its doom."
  - **C45** The Waking Sands stops being the headquarters and passes to Urianger; Alisaie keeps working with him. *The Gifted* (2.1, main): "the Waking Sands will formally cease to be our headquarters, and the premises will be given into the care of Urianger. … Alisaie shall continue to work closely with him"
  - **C21** Urianger hides the Waking Sands behind a glamour that makes it look abandoned, sheltering refugees. *Before the Dawn* (2.55, main): "he used his magicks to weave a glamour around the Waking Sands … our old headquarters now looks like an abandoned storehouse!"

</details>

### Alphinaud (`char-alphinaud`, character)

**#102–#109 · main**

> A young traveler who, with his twin sister, calls himself a student of history.

Sources shown: A Hero in the Making — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C10** Alphinaud and Alisaie are twins. *A Hero in the Making* (2.0, main): "the traveling twins, Alphinaud and Alisaie … And my sister, Alisaie, at your service."
  - **C42** The twins call themselves students of history; Alisaie means to find another way to heal the realm. *A Hero in the Making* (2.0, main): "You might call us students of history … There must be another way to cure what ails this world─and I mean to find it!"

</details>

**#110–#128 · main**

> A young Scion who stands against the primals and the Empire, as his grandfather once did. He recognized Marques as Cid, an engineer missing since the Calamity, and enlisted him to find his lost airship, the Enterprise: the Ixal have summoned Garuda, and the surviving Scions need the ship to reach her.

Sources shown: Eyes on Me — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C25** Alphinaud is a Scion. *Eyes on Me* (2.0, main): "As a Scion of the Seventh Dawn, I stand against our primal and imperial foes─as my grandfather once did."
  - **E110c** Alphinaud declares Marques to be Cid, missing since the Calamity five years ago. *Eyes on Me* (2.0, main): "declares Marques to be none other than Master Cid … who has been missing since the Calamity five years ago."
  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."

</details>

**#129–#140 · main**

> A young Scion who stands against the primals and the Empire, as his grandfather once did. He and Cid recovered the Enterprise from the Stone Vigil, and it must now be repaired to brave the storm around Garuda.

Sources shown: Eyes on Me — main scenario quest (2.0); In Pursuit of the Past — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C25** Alphinaud is a Scion. *Eyes on Me* (2.0, main): "As a Scion of the Seventh Dawn, I stand against our primal and imperial foes─as my grandfather once did."
  - **E129c** Alphinaud and Cid slip aboard the Enterprise while you hold off the dragon. *In Pursuit of the Past* (2.0, main): "Cid─you and I will sneak aboard the ''Enterprise'' and prepare it for launch."
  - **E129e** The Enterprise is in no condition to weather Garuda's storm. *In Pursuit of the Past* (2.0, main): "it is plain the ''Enterprise'' is in no condition to weather the storm"

</details>

**#141 only · main**

> A young Scion who stands against the primals and the Empire, as his grandfather once did. After the Empire's weapon seemingly absorbed the primals at the Howling Eye, he turned the Scions' efforts to destroying it, and resolved to re-form the order at the Waking Sands.

Sources shown: Eyes on Me — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C25** Alphinaud is a Scion. *Eyes on Me* (2.0, main): "As a Scion of the Seventh Dawn, I stand against our primal and imperial foes─as my grandfather once did."
  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."
  - **E141e** All efforts now turn to destroying the Empire's weapon. *Lady of the Vortex* (2.0, main): "all efforts must now be focused upon destroying [[Garlean Empire|the Empire]]'s [[The Ultima Weapon|ultimate weapon]]."
  - **E141f** Cid and Alphinaud resolve to re-form the Scions at the Waking Sands. *Lady of the Vortex* (2.0, main): "Believing the best course of action is to reform [[the Scions of the Seventh Dawn]], they decide to return to [[the Waking Sands]]."

</details>

**#142–#153 · main**

> A young Scion who stands against the primals and the Empire, as his grandfather once did. He has brought the survivors back to the Waking Sands to rebuild the order, and is working to rescue the Scions held at Castrum Centri.

Sources shown: Eyes on Me — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C25** Alphinaud is a Scion. *Eyes on Me* (2.0, main): "As a Scion of the Seventh Dawn, I stand against our primal and imperial foes─as my grandfather once did."
  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E142a** Alphinaud brings you back to the Waking Sands. *Reclamation* (2.0, main): "It is past time that we return to the Waking Sands."
  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."

</details>

**#154–#156 · main**

> A young Scion who stands against the primals and the Empire, as his grandfather once did. Since the raid on the Waking Sands he has worked to rebuild the Scions, and he sought out Cid, the greatest engineer of the age, to help.

Sources shown: Eyes on Me — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C25** Alphinaud is a Scion. *Eyes on Me* (2.0, main): "As a Scion of the Seventh Dawn, I stand against our primal and imperial foes─as my grandfather once did."
  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **K05** Alphinaud seeks out Cid as the greatest engineer of the age. *Eyes on Me* (2.0, main): "I have come in search of a legend─the greatest engineer of our time."

</details>

**#157–#160 · main**

> A young Scion who stands against the primals and the Empire, as his grandfather once did. He briefed you on Operation Archon, the Alliance's great counteroffensive, and advises its main host alongside Minfilia and Cid.

Sources shown: Eyes on Me — main scenario quest (2.0); Operation Archon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C25** Alphinaud is a Scion. *Eyes on Me* (2.0, main): "As a Scion of the Seventh Dawn, I stand against our primal and imperial foes─as my grandfather once did."
  - **K41** It is the largest counteroffensive in the realm's history; its last phase is to destroy the Ultima Weapon in the Praetorium. *Operation Archon* (2.0, main): "the largest single counteroffensive in the realm's troubled history … where they will locate and destroy the Ultima Weapon."
  - **K43** Minfilia, Cid and Alphinaud advise the main host, and the other Scions go with their Grand Companies. *Operation Archon* (2.0, main): "Minfilia, Cid, and I shall accompany the main host in an advisory capacity. … pray accompany your respective organizations on their missions."

</details>

**2.0 only · main**

> A young Scion and Alisaie's twin brother. The twins first appear as self-described students of history, touring the city-states' remembrance services. After the raid on the Waking Sands he worked to rebuild the Scions, and he sees their cause as the dream of his grandfather, who gave his life for the realm.

Sources shown: A Hero in the Making — main scenario quest (2.0); Eyes on Me — main scenario quest (2.0); Reclamation — main scenario quest (2.0); The Ultimate Weapon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C10** Alphinaud and Alisaie are twins. *A Hero in the Making* (2.0, main): "the traveling twins, Alphinaud and Alisaie … And my sister, Alisaie, at your service."
  - **C42** The twins call themselves students of history; Alisaie means to find another way to heal the realm. *A Hero in the Making* (2.0, main): "You might call us students of history … There must be another way to cure what ails this world─and I mean to find it!"
  - **C25** Alphinaud is a Scion. *Eyes on Me* (2.0, main): "As a Scion of the Seventh Dawn, I stand against our primal and imperial foes─as my grandfather once did."
  - **C38** The Scions restore their damaged headquarters. *Reclamation* (2.0, main): "To leave our headquarters in disrepair any longer would be to dishonor the memory of those who fell there."
  - **C43** Alphinaud's grandfather gave his life for a dream Alphinaud carries on. *The Ultimate Weapon* (2.0, main): "Do you see, Grandfather? Our first step towards realizing the dream for which you gave your life."

</details>

**2.55 onward · main**

> A young Scion and Alisaie's twin brother. He founded the Crystal Braves to serve all of Eorzea rather than any one nation, and commanded them. At the royal banquet in Ul'dah the Braves turned on him. He escaped, and now blames himself for treating the Braves and even the Scions as pawns in his plans.

Sources shown: A Hero in the Making — main scenario quest (2.0); Brave New Companions — main scenario quest (2.3); Traitor in the Midst — main scenario quest (2.4); The Parting Glass — main scenario quest (2.55); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C10** Alphinaud and Alisaie are twins. *A Hero in the Making* (2.0, main): "the traveling twins, Alphinaud and Alisaie … And my sister, Alisaie, at your service."
  - **C48** Alphinaud names his company the Crystal Braves: pledged to the Scions, bound to no single nation, fighting for a united Eorzea. *Brave New Companions* (2.3, main): "the name he has chosen for the trial company: the Crystal Braves … beholden to no single nation. You stand as the vanguard for a united Eorzea!"
  - **C16** Alphinaud commands the Crystal Braves, with Captain Ilberd as his second-in-command. *Traitor in the Midst* (2.4, main): "his new station as commander of the Crystal Braves … Captain Ilberd, his second-in-command"
  - **C52** The Braves turn on Alphinaud, who later blames himself for using the Braves and Scions as pawns. *The Parting Glass* (2.55, main): "I thought the Crystal Braves mine till the very moment I felt the blade at my back"
  - **C52b** Alphinaud blames himself. *Before the Dawn* (2.55, main): "I treated the Crystal Braves, and even the Scions themselves, as pawns in my great scheme to save the realm."

</details>

### Alisaie (`char-alisaie`, character)

**2.0 only · main**

> Alphinaud's twin sister. She doubts her brother's approach and has set out to find her own way to heal the realm's troubles. Alphinaud says that although she walks her own path, the twins share the same goal.

Sources shown: A Hero in the Making — main scenario quest (2.0); Back from the Wood — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C10** Alphinaud and Alisaie are twins. *A Hero in the Making* (2.0, main): "the traveling twins, Alphinaud and Alisaie … And my sister, Alisaie, at your service."
  - **C42** The twins call themselves students of history; Alisaie means to find another way to heal the realm. *A Hero in the Making* (2.0, main): "You might call us students of history … There must be another way to cure what ails this world─and I mean to find it!"
  - **C11** Alisaie walks her own path, but shares her brother's goal. *Back from the Wood* (2.0, main): "Alisaie has chosen to walk her own path─stubborn girl─but you may be assured that our destination remains the same."

</details>

**2.0 only · optional**

> Alphinaud's twin sister, a young Scion who walks her own path apart from her brother. She is investigating the Binding Coil of Bahamut, where she believes she saw her grandfather, Louisoix, who is presumed to have died sealing the primal away.

Sources shown: A Hero in the Making — main scenario quest (2.0); Back from the Wood — main scenario quest (2.0); Alisaie's Pledge — optional Binding Coil quest (2.0)

<details><summary>Evidence</summary>

  - **C10** Alphinaud and Alisaie are twins. *A Hero in the Making* (2.0, main): "the traveling twins, Alphinaud and Alisaie … And my sister, Alisaie, at your service."
  - **C11** Alisaie walks her own path, but shares her brother's goal. *Back from the Wood* (2.0, main): "Alisaie has chosen to walk her own path─stubborn girl─but you may be assured that our destination remains the same."
  - **C30** The journal calls Alisaie "the young Scion". *Alisaie's Pledge* (2.0, optional): "Urianger bids you join the young Scion in reflecting upon all that you witnessed within the Binding Coil."
  - **C13** Louisoix was Alisaie's grandfather. *Alisaie's Pledge* (2.0, optional): "Master Louisoix was my lady's grandsire."
  - **C58** Alisaie believes she saw her grandfather alive in the Binding Coil. *Alisaie's Pledge* (2.0, optional): "I saw him with my own two eyes—as did [Forename]."

</details>

**2.55 onward · main**

> Alphinaud's twin sister, who walks her own path. She stayed on at the Waking Sands to work with Urianger when the Scions moved to Mor Dhona, and she was not among them at the royal banquet in Ul'dah. Alphinaud believes she was watching over him during his escape.

Sources shown: A Hero in the Making — main scenario quest (2.0); Back from the Wood — main scenario quest (2.0); The Gifted — main scenario quest (2.1); The Parting Glass — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C10** Alphinaud and Alisaie are twins. *A Hero in the Making* (2.0, main): "the traveling twins, Alphinaud and Alisaie … And my sister, Alisaie, at your service."
  - **C11** Alisaie walks her own path, but shares her brother's goal. *Back from the Wood* (2.0, main): "Alisaie has chosen to walk her own path─stubborn girl─but you may be assured that our destination remains the same."
  - **C45** The Waking Sands stops being the headquarters and passes to Urianger; Alisaie keeps working with him. *The Gifted* (2.1, main): "the Waking Sands will formally cease to be our headquarters, and the premises will be given into the care of Urianger. … Alisaie shall continue to work closely with him"
  - **C23** Alphinaud believes Alisaie was watching over him. *The Parting Glass* (2.55, main): "I had thought to look out for Alisaie, but 'twould appear she was the one watching over me."

</details>

**2.55 onward · optional**

> Alphinaud's twin sister, a young Scion who walks her own path. She learned that the figure she saw in the Binding Coil was only an aetherial shadow of her grandfather, Louisoix, bound to Bahamut. With your help his soul was freed, and she now means to find her own reason to fight for Eorzea. She was not among the Scions at the royal banquet in Ul'dah, and Alphinaud believes she was watching over him during his escape.

Sources shown: A Hero in the Making — main scenario quest (2.0); Alisaie's Pledge — optional Binding Coil quest (2.0); Alisaie's Resolve — optional Binding Coil quest (2.2); Alisaie's Path — optional Binding Coil quest (2.4); The Parting Glass — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C10** Alphinaud and Alisaie are twins. *A Hero in the Making* (2.0, main): "the traveling twins, Alphinaud and Alisaie … And my sister, Alisaie, at your service."
  - **C30** The journal calls Alisaie "the young Scion". *Alisaie's Pledge* (2.0, optional): "Urianger bids you join the young Scion in reflecting upon all that you witnessed within the Binding Coil."
  - **C56** What Alisaie saw was an aetherial shadow of Louisoix bound by Bahamut. *Alisaie's Resolve* (2.2, optional): "'twas but the aetherial shadow of Master Louisoix that Lady Alisaie beheld"
  - **C28** The player freed Louisoix's soul from Bahamut. *Alisaie's Path* (2.4, optional): "You are the one who freed Grandfather's soul and saved Eorzea from Bahamut's wrath."
  - **C57** Alisaie now means to find her own reason to fight for Eorzea. *Alisaie's Path* (2.4, optional): "I mean to find my own reason to fight for Eorzea."
  - **C23** Alphinaud believes Alisaie was watching over him. *The Parting Glass* (2.55, main): "I had thought to look out for Alisaie, but 'twould appear she was the one watching over me."

</details>

### Louisoix (`char-louisoix`, character)

**2.0 only · main** · Also searchable as: Archon Louisoix, Master Louisoix

> A revered Archon and man of learning. He never returned from the Battle of Carteneau, and the realm's leaders lament the loss of his wisdom. The Scions still speak of his guidance.

Sources shown: The Lominsan Envoy — main scenario quest (2.0); The Gridanian Envoy — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C44** Archon Louisoix never returned from Carteneau, and the realm's leaders miss his wisdom. *The Lominsan Envoy* (2.0, main): "Archon Louisoix may well have been able to shed light upon these mysteries, but he, like so many, never returned from Carteneau."
  - **C44b** The Admiral wishes Archon Louisoix were still with them. *The Gridanian Envoy* (2.0, main): "Were Archon Louisoix still with us, he would doubtless shed some light on these unfathomable happenings. Alas, he is not"
  - **C44c** The Scions feel Master Louisoix's guidance still. *Reclamation* (2.0, main): "It is as if the benevolent hand of Master Louisoix guides us still."

</details>

**2.0 only · optional** · Also searchable as: Archon Louisoix, Master Louisoix

> A revered Archon and man of learning, and Alisaie's grandfather. He never returned from the Battle of Carteneau and is presumed dead, having apparently sealed the primal Bahamut away there. Alisaie believes she has seen him alive within the Binding Coil.

Sources shown: The Lominsan Envoy — main scenario quest (2.0); Alisaie's Pledge — optional Binding Coil quest (2.0)

<details><summary>Evidence</summary>

  - **C44** Archon Louisoix never returned from Carteneau, and the realm's leaders miss his wisdom. *The Lominsan Envoy* (2.0, main): "Archon Louisoix may well have been able to shed light upon these mysteries, but he, like so many, never returned from Carteneau."
  - **C13** Louisoix was Alisaie's grandfather. *Alisaie's Pledge* (2.0, optional): "Master Louisoix was my lady's grandsire."
  - **C27** Bahamut was sealed beneath Carteneau, seemingly by Louisoix, who is presumed dead. *Alisaie's Pledge* (2.0, optional): "Bahamut was sealed deep beneath the Carteneau Flats seemingly by Louisoix, who was presumed dead."
  - **C58** Alisaie believes she saw her grandfather alive in the Binding Coil. *Alisaie's Pledge* (2.0, optional): "I saw him with my own two eyes—as did [Forename]."

</details>

**2.55 onward · main** · Also searchable as: Archon Louisoix, Master Louisoix

> A Sharlayan sage who founded the Circle of Knowing in the face of fierce opposition and came to Eorzea. Urianger studied under him. His sacrifice during the Calamity spared the realm, and the Scions still hold to his teachings.

Sources shown: An Uninvited Ascian — main scenario quest (2.5); The Steps of Faith — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C54** Louisoix founded the Circle of Knowing, came to Eorzea, and spared the realm through his sacrifice; Urianger and Moenbryda studied under him. *An Uninvited Ascian* (2.5, main): "Moenbryda and I did study under the sage tutelage of Master Louisoix. … he founded the Circle of Knowing … Through his noble sacrifice was the realm spared its doom."
  - **C55** The Scions still hold to Louisoix's teachings. *The Steps of Faith* (2.55, main): "To do otherwise would go against all that Master Louisoix has taught us."

</details>

**2.55 onward · optional** · Also searchable as: Archon Louisoix, Master Louisoix

> A Sharlayan sage, the twins' grandfather, who founded the Circle of Knowing and came to Eorzea. His sacrifice during the Calamity spared the realm, apparently sealing Bahamut away. The figure Alisaie saw in the Binding Coil was an aetherial shadow of him bound to the primal, and you freed his soul.

Sources shown: An Uninvited Ascian — main scenario quest (2.5); Another Turn in the Coil — optional Binding Coil quest (2.2); Alisaie's Pledge — optional Binding Coil quest (2.0); Alisaie's Resolve — optional Binding Coil quest (2.2); Alisaie's Path — optional Binding Coil quest (2.4)

<details><summary>Evidence</summary>

  - **C54** Louisoix founded the Circle of Knowing, came to Eorzea, and spared the realm through his sacrifice; Urianger and Moenbryda studied under him. *An Uninvited Ascian* (2.5, main): "Moenbryda and I did study under the sage tutelage of Master Louisoix. … he founded the Circle of Knowing … Through his noble sacrifice was the realm spared its doom."
  - **C26** Alphinaud speaks of "our grandsire", shared with his sister. *Another Turn in the Coil* (2.2, optional): "my sister's admiration and affection for our grandsire exceeds even mine own."
  - **C13** Louisoix was Alisaie's grandfather. *Alisaie's Pledge* (2.0, optional): "Master Louisoix was my lady's grandsire."
  - **C27** Bahamut was sealed beneath Carteneau, seemingly by Louisoix, who is presumed dead. *Alisaie's Pledge* (2.0, optional): "Bahamut was sealed deep beneath the Carteneau Flats seemingly by Louisoix, who was presumed dead."
  - **C56** What Alisaie saw was an aetherial shadow of Louisoix bound by Bahamut. *Alisaie's Resolve* (2.2, optional): "'twas but the aetherial shadow of Master Louisoix that Lady Alisaie beheld"
  - **C28** The player freed Louisoix's soul from Bahamut. *Alisaie's Path* (2.4, optional): "You are the one who freed Grandfather's soul and saved Eorzea from Bahamut's wrath."

</details>

### Tataru (`char-tataru`, character)

**#102–#142 · main**

> The Scions' clerk, who makes sure everything runs smoothly.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C32** Tataru is the Scions' clerk. *A Wild Rose by Any Other Name* (2.0, main): "Oh, I should also introduce you to Tataru, our clerk. She ensures that everything runs smoothly."

</details>

**#143–#154 · main**

> The Scions' clerk. Scouts saw her among four prisoners led into Castrum Centri.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C32** Tataru is the Scions' clerk. *A Wild Rose by Any Other Name* (2.0, main): "Oh, I should also introduce you to Tataru, our clerk. She ensures that everything runs smoothly."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."

</details>

**#155–#160 · main**

> The Scions' clerk. She was among the prisoners held at Castrum Centri, and was freed in the rescue.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C32** Tataru is the Scions' clerk. *A Wild Rose by Any Other Name* (2.0, main): "Oh, I should also introduce you to Tataru, our clerk. She ensures that everything runs smoothly."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **K20** The rescue party frees the captives held in Castrum Centri's storage tower. *Escape from Castrum Centri* (2.0, main): "and the others are being held within the storage tower. … Though the rescue mission was a success"

</details>

**2.0 only · main**

> The Scions' clerk, who greets visitors at the Waking Sands and keeps the order running smoothly. She was among those taken prisoner in the imperial raid, and was freed in the rescue at Castrum Centri.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C32** Tataru is the Scions' clerk. *A Wild Rose by Any Other Name* (2.0, main): "Oh, I should also introduce you to Tataru, our clerk. She ensures that everything runs smoothly."
  - **C36** The prisoners are Minfilia, Urianger, Papalymo and Tataru, whom Y'shtola calls "our fellow Scions". *Casing the Castrum* (2.0, main): "Minfilia, Urianger, Papalymo, and Tataru! … the Garleans took our fellow Scions prisoner"
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"

</details>

**2.55 onward · main**

> The Scions' receptionist, who followed them to their new headquarters at the Rising Stones. She briefly left to train as an arcanist so that she could protect others, but gave it up. After the royal banquet in Ul'dah, Crystal Braves turned on her; Yugiri rescued her, and she sheltered at the glamoured Waking Sands before rejoining you.

Sources shown: Build on the Stone — main scenario quest (2.1); Administrative Decision — main scenario quest (2.55); An Unexpected Ambition — main scenario quest (2.55); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C15** The Rising Stones, entered through the Seventh Heaven, is inaugurated as the new headquarters; Tataru is its receptionist. *Build on the Stone* (2.1, main): "celebrate the inauguration of their new headquarters … speak with Tataru inside the Seventh Heaven … your restive receptionist"
  - **C47** Tataru leaves to train as an arcanist so she can protect others, then gives it up. *Administrative Decision* (2.55, main): "When I return, I shall be both your receptionist and your bodyguard!"
  - **C47b** Tataru renounces arcanima. *An Unexpected Ambition* (2.55, main): "Crestfallen, she renounces arcanima and returns to the city."
  - **C20** Crystal Braves turn on the Scions' people in the marketplace. *Before the Dawn* (2.55, main): "And then Crystal Braves─our own people!─turned on us in the marketplace."
  - **C53** Yugiri rescued Tataru from the Crystal Braves. *Before the Dawn* (2.55, main): "the refugee leader having rescued the young receptionist from Crystal Braves"
  - **C21** Urianger hides the Waking Sands behind a glamour that makes it look abandoned, sheltering refugees. *Before the Dawn* (2.55, main): "he used his magicks to weave a glamour around the Waking Sands … our old headquarters now looks like an abandoned storehouse!"

</details>

### The Scions of the Seventh Dawn (`org-scions`, organization)

**#102–#105 · main**

> An order devoted to preserving Eorzea's future, led by Minfilia. It stands above politics, and its headquarters is the Waking Sands in Vesper Bay, western Thanalan.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C34** The Scions stand above politics; their aim is preserving Eorzea's future. *The Scions of the Seventh Dawn* (2.0, main): "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."
  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **C02** The Scions are headquartered at the Waking Sands in Vesper Bay, western Thanalan. *The Scions of the Seventh Dawn* (2.0, main): "the Waking Sands, located in Vesper Bay, out in western Thanalan"

</details>

**#106–#109 · main**

> An order devoted to preserving Eorzea's future, led by Minfilia. Imperial forces raided its headquarters at the Waking Sands, slaughtered many of its members and took prisoners, Minfilia among them. Father Iliud, an old friend of Minfilia's, has given the survivors sanctuary at his church in eastern Thanalan.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C34** The Scions stand above politics; their aim is preserving Eorzea's future. *The Scions of the Seventh Dawn* (2.0, main): "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."
  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **E106f** Father Iliud has known Minfilia since childhood, swore to support her, and offers the same to her fellow Scions. *All Good Things* (2.0, main): "I have known her since she was but a child... … I swore then to do everything in my power to support her, and I will gladly offer the selfsame service to her brother and sister Scions."

</details>

**#110–#140 · main**

> An order devoted to preserving Eorzea's future, led by Minfilia, who was taken prisoner when imperial forces raided its headquarters at the Waking Sands. The surviving Scions, with Alphinaud, are seeking Cid's lost airship to reach the primal Garuda.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Eyes on Me — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C34** The Scions stand above politics; their aim is preserving Eorzea's future. *The Scions of the Seventh Dawn* (2.0, main): "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."
  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."

</details>

**#141 only · main**

> An order devoted to preserving Eorzea's future, led by Minfilia, who was taken prisoner when imperial forces raided its headquarters. After the Empire's weapon seemingly absorbed the primals at the Howling Eye, the survivors resolved to re-form the order at the Waking Sands.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C34** The Scions stand above politics; their aim is preserving Eorzea's future. *The Scions of the Seventh Dawn* (2.0, main): "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."
  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."
  - **E141f** Cid and Alphinaud resolve to re-form the Scions at the Waking Sands. *Lady of the Vortex* (2.0, main): "Believing the best course of action is to reform [[the Scions of the Seventh Dawn]], they decide to return to [[the Waking Sands]]."

</details>

**#142–#153 · main**

> An order devoted to preserving Eorzea's future, led by Minfilia. Its captured members, Minfilia among them, are held at Castrum Centri. Alphinaud is rebuilding the order at its damaged headquarters, the Waking Sands, and its free members are preparing a rescue.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C34** The Scions stand above politics; their aim is preserving Eorzea's future. *The Scions of the Seventh Dawn* (2.0, main): "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."
  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."
  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **C38** The Scions restore their damaged headquarters. *Reclamation* (2.0, main): "To leave our headquarters in disrepair any longer would be to dishonor the memory of those who fell there."

</details>

**#154 only · main**

> An order devoted to preserving Eorzea's future, led by Minfilia. Imperial forces raided its headquarters at the Waking Sands and took members prisoner, Minfilia among them. Alphinaud means to rebuild the order, and its free members are working with Cid to rescue the captives from Castrum Centri.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Reclamation — main scenario quest (2.0); Come-Into-My-Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C34** The Scions stand above politics; their aim is preserving Eorzea's future. *The Scions of the Seventh Dawn* (2.0, main): "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."
  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **C06** Imperial forces raid the Waking Sands and take prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces"
  - **K17** The Scions were taken prisoner by the Empire, and the order must be reborn. *Reclamation* (2.0, main): "[[the Scions]] taken prisoner by the Empire. … [[the Scions of the Seventh Dawn]] must be reborn."
  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **K04** Cid prepares a plan to rescue the captive Scions. *Come-Into-My-Castrum* (2.0, main): "wants to prepare a strategy to rescue"

</details>

**#155–#156 · main**

> An order devoted to preserving Eorzea's future, led by Minfilia. Its captured members were freed from Castrum Centri, though Thancred was found to be possessed by the Ascian Lahabrea. Eorzea's leaders had believed the Scions dead or missing.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C34** The Scions stand above politics; their aim is preserving Eorzea's future. *The Scions of the Seventh Dawn* (2.0, main): "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."
  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **K20** The rescue party frees the captives held in Castrum Centri's storage tower. *Escape from Castrum Centri* (2.0, main): "and the others are being held within the storage tower. … Though the rescue mission was a success"
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"
  - **K26** The Alliance leaders had believed the Scions dead or missing, and now weigh the Black Wolf's ultimatum. *Escape from Castrum Centri* (2.0, main): "The Alliance leaders staked their hopes on the Scions, but now they believe us all dead or missing. … I believe we are all acquainted with the terms of the Black Wolf's ultimatum."

</details>

**#157–#160 · main**

> An order devoted to preserving Eorzea's future, led by Minfilia. It stands with the Eorzean Alliance in Operation Archon: Minfilia and Alphinaud advise the main host, and the other Scions go with their Grand Companies.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); Operation Archon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C34** The Scions stand above politics; their aim is preserving Eorzea's future. *The Scions of the Seventh Dawn* (2.0, main): "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."
  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **K40** Operation Archon is the Eorzean Alliance's eleventh-hour bid to drive out the Empire. *Operation Archon* (2.0, main): "So begins Operation Archon, the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace."
  - **K43** Minfilia, Cid and Alphinaud advise the main host, and the other Scions go with their Grand Companies. *Operation Archon* (2.0, main): "Minfilia, Cid, and I shall accompany the main host in an advisory capacity. … pray accompany your respective organizations on their missions."

</details>

**2.0 only · main**

> An order that stands apart from the city-states' politics, devoted to preserving Eorzea's future. Minfilia leads it from the Waking Sands in Vesper Bay, and its members include Sharlayans who stayed in Eorzea when their countrymen fled. An imperial raid devastated the order and took several members prisoner, but the Scions rescued them and rebuilt.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); A Wild Rose by Any Other Name — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C34** The Scions stand above politics; their aim is preserving Eorzea's future. *The Scions of the Seventh Dawn* (2.0, main): "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."
  - **C01** Minfilia leads the Scions. *The Scions of the Seventh Dawn* (2.0, main): "My name is Minfilia, and I lead the Scions of the Seventh Dawn."
  - **C02** The Scions are headquartered at the Waking Sands in Vesper Bay, western Thanalan. *The Scions of the Seventh Dawn* (2.0, main): "the Waking Sands, located in Vesper Bay, out in western Thanalan"
  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **C06** Imperial forces raid the Waking Sands and take prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces"
  - **C36** The prisoners are Minfilia, Urianger, Papalymo and Tataru, whom Y'shtola calls "our fellow Scions". *Casing the Castrum* (2.0, main): "Minfilia, Urianger, Papalymo, and Tataru! … the Garleans took our fellow Scions prisoner"
  - **C38** The Scions restore their damaged headquarters. *Reclamation* (2.0, main): "To leave our headquarters in disrepair any longer would be to dishonor the memory of those who fell there."

</details>

**2.55 onward · main**

> An order devoted to preserving Eorzea's future, led by Minfilia. It moved its headquarters to the Rising Stones in Mor Dhona. At a royal banquet in Ul'dah, its members were accused of plotting to poison the sultana and branded fugitives, and its own Crystal Braves turned on it. Most of those who attended are unaccounted for, and the few who escaped regroup in Coerthas.

Sources shown: Laying the Foundation — main scenario quest (2.1); Build on the Stone — main scenario quest (2.1); The Parting Glass — main scenario quest (2.55); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C14** The Scions find a new home in Revenant's Toll, Mor Dhona. *Laying the Foundation* (2.1, main): "we have found ourselves a new home in Revenant's Toll"
  - **C15** The Rising Stones, entered through the Seventh Heaven, is inaugurated as the new headquarters; Tataru is its receptionist. *Build on the Stone* (2.1, main): "celebrate the inauguration of their new headquarters … speak with Tataru inside the Seventh Heaven … your restive receptionist"
  - **C50** At the banquet the Scions are accused of conspiring to poison the sultana, detained, and branded fugitives. *The Parting Glass* (2.55, main): "I hereby accuse you of regicide! … all members of the Scions of the Seventh Dawn will be detained for questioning … branded fugitives"
  - **C19** The Crystal Braves seize the Rising Stones and detain the Scions' allies. *The Parting Glass* (2.55, main): "we have detained all those with allegiance to the Scions. The Rising Stones is also under our control."
  - **C20** Crystal Braves turn on the Scions' people in the marketplace. *Before the Dawn* (2.55, main): "And then Crystal Braves─our own people!─turned on us in the marketplace."
  - **C22** Every other Scion at the banquet is unaccounted for; Minfilia and the others do not respond. *Before the Dawn* (2.55, main): "every other Scion who attended the banquet remains unaccounted for … I tried contacting Minfilia and the others, but no one would respond"
  - **C24** The survivors regroup in an intercessory in Coerthas. *Before the Dawn* (2.55, main): "join your companions in the intercessory"

</details>

### The Crystal Braves (`org-crystal-braves`, organization)

**2.55 onward · main**

> A company Alphinaud founded under the Scions, recruiting fighters who serve no single nation, for the sake of a united Eorzea. Alphinaud commanded it, with Captain Ilberd as his second-in-command. At the royal banquet in Ul'dah the Braves turned on the Scions: they detained the Scions' allies, seized the Rising Stones and hunted the fugitives.

Sources shown: Brave New Companions — main scenario quest (2.3); Traitor in the Midst — main scenario quest (2.4); The Parting Glass — main scenario quest (2.55); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C48** Alphinaud names his company the Crystal Braves: pledged to the Scions, bound to no single nation, fighting for a united Eorzea. *Brave New Companions* (2.3, main): "the name he has chosen for the trial company: the Crystal Braves … beholden to no single nation. You stand as the vanguard for a united Eorzea!"
  - **C16** Alphinaud commands the Crystal Braves, with Captain Ilberd as his second-in-command. *Traitor in the Midst* (2.4, main): "his new station as commander of the Crystal Braves … Captain Ilberd, his second-in-command"
  - **C19** The Crystal Braves seize the Rising Stones and detain the Scions' allies. *The Parting Glass* (2.55, main): "we have detained all those with allegiance to the Scions. The Rising Stones is also under our control."
  - **C20** Crystal Braves turn on the Scions' people in the marketplace. *Before the Dawn* (2.55, main): "And then Crystal Braves─our own people!─turned on us in the marketplace."

</details>

### The Waking Sands (`loc-waking-sands`, location)

**#102–#105 · main**

> The Scions' headquarters in Vesper Bay, western Thanalan, where Urianger presides over the order's affairs.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); A Wild Rose by Any Other Name — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C02** The Scions are headquartered at the Waking Sands in Vesper Bay, western Thanalan. *The Scions of the Seventh Dawn* (2.0, main): "the Waking Sands, located in Vesper Bay, out in western Thanalan"
  - **C41** Urianger presides over the affairs of the Waking Sands. *A Wild Rose by Any Other Name* (2.0, main): "Last but not least is Urianger, who presides over all affairs within these halls."

</details>

**#106–#141 · main**

> The Scions' headquarters in Vesper Bay, western Thanalan. Imperial forces raided it, slaughtering many Scions and taking prisoners.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C02** The Scions are headquartered at the Waking Sands in Vesper Bay, western Thanalan. *The Scions of the Seventh Dawn* (2.0, main): "the Waking Sands, located in Vesper Bay, out in western Thanalan"
  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."

</details>

**#142–#160 · main**

> The Scions' headquarters in Vesper Bay, western Thanalan, damaged in the imperial raid. Alphinaud has brought the surviving Scions back to restore it and rebuild the order.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C02** The Scions are headquartered at the Waking Sands in Vesper Bay, western Thanalan. *The Scions of the Seventh Dawn* (2.0, main): "the Waking Sands, located in Vesper Bay, out in western Thanalan"
  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."
  - **E142a** Alphinaud brings you back to the Waking Sands. *Reclamation* (2.0, main): "It is past time that we return to the Waking Sands."
  - **C38** The Scions restore their damaged headquarters. *Reclamation* (2.0, main): "To leave our headquarters in disrepair any longer would be to dishonor the memory of those who fell there."

</details>

**2.0 only · main**

> The Scions' headquarters in Vesper Bay, in western Thanalan, where Minfilia receives visitors. Imperial forces raided it and took prisoners, and the Scions later restored it.

Sources shown: The Scions of the Seventh Dawn — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C02** The Scions are headquartered at the Waking Sands in Vesper Bay, western Thanalan. *The Scions of the Seventh Dawn* (2.0, main): "the Waking Sands, located in Vesper Bay, out in western Thanalan"
  - **C06** Imperial forces raid the Waking Sands and take prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces"
  - **C38** The Scions restore their damaged headquarters. *Reclamation* (2.0, main): "To leave our headquarters in disrepair any longer would be to dishonor the memory of those who fell there."

</details>

**2.55 onward · main**

> The Scions' former headquarters in Vesper Bay. When they moved to the Rising Stones it passed into Urianger's care. After the royal banquet in Ul'dah, Urianger hid it behind a glamour that makes it look like an abandoned storehouse, and it now shelters those fleeing the Crystal Braves.

Sources shown: The Gifted — main scenario quest (2.1); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C45** The Waking Sands stops being the headquarters and passes to Urianger; Alisaie keeps working with him. *The Gifted* (2.1, main): "the Waking Sands will formally cease to be our headquarters, and the premises will be given into the care of Urianger. … Alisaie shall continue to work closely with him"
  - **C21** Urianger hides the Waking Sands behind a glamour that makes it look abandoned, sheltering refugees. *Before the Dawn* (2.55, main): "he used his magicks to weave a glamour around the Waking Sands … our old headquarters now looks like an abandoned storehouse!"
  - **C53** Yugiri rescued Tataru from the Crystal Braves. *Before the Dawn* (2.55, main): "the refugee leader having rescued the young receptionist from Crystal Braves"

</details>

### The Rising Stones (`loc-rising-stones`, location)

**2.55 onward · main**

> The Scions' headquarters in Revenant's Toll, Mor Dhona, entered through the Seventh Heaven. They moved there from the Waking Sands. After the royal banquet in Ul'dah, the Crystal Braves took control of it, and now only Braves remain there.

Sources shown: Laying the Foundation — main scenario quest (2.1); Build on the Stone — main scenario quest (2.1); The Parting Glass — main scenario quest (2.55); Before the Dawn — main scenario quest (2.55)

<details><summary>Evidence</summary>

  - **C14** The Scions find a new home in Revenant's Toll, Mor Dhona. *Laying the Foundation* (2.1, main): "we have found ourselves a new home in Revenant's Toll"
  - **C15** The Rising Stones, entered through the Seventh Heaven, is inaugurated as the new headquarters; Tataru is its receptionist. *Build on the Stone* (2.1, main): "celebrate the inauguration of their new headquarters … speak with Tataru inside the Seventh Heaven … your restive receptionist"
  - **C19** The Crystal Braves seize the Rising Stones and detain the Scions' allies. *The Parting Glass* (2.55, main): "we have detained all those with allegiance to the Scions. The Rising Stones is also under our control."
  - **C19b** Only Crystal Braves remain at the Rising Stones. *Before the Dawn* (2.55, main): "Only Crystal Braves await you there."

</details>

### The Black Wolf's Challenge (`evt-black-wolfs-challenge`, event)

**#155 only · main**

> You and Cid's crew broke into Castrum Centri and freed Minfilia and the captive Scions, but the escape revealed that the Ascian Lahabrea has possessed Thancred. The Empire has finished the Ultima Weapon, an ancient Allagan relic, and Gaius, the Black Wolf, has given Eorzea's leaders an ultimatum: submit to his power, or share the primals' fate.

Sources shown: Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K20** The rescue party frees the captives held in Castrum Centri's storage tower. *Escape from Castrum Centri* (2.0, main): "and the others are being held within the storage tower. … Though the rescue mission was a success"
  - **K21** Cid and Alphinaud create a diversion outside the castrum. *Escape from Castrum Centri* (2.0, main): "Alphinaud and I will create a diversion out here and keep them occupied for as long as we are able."
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"
  - **K23** The Empire has finished the Ultima Weapon, an Allagan relic excavated beneath Ala Mhigo. *Escape from Castrum Centri* (2.0, main): "They finished it. Ultima Weapon... … It is a relic of ancient Allag, excavated from its resting place deep beneath Ala Mhigo."
  - **K25** Gaius demands the realm submit to his power; resistance means sharing the primals' fate. *Escape from Castrum Centri* (2.0, main): "This realm founders for want of a ruler with true power─the power to cast down eikons. … Yet offer resistance, and he swears that we shall share the primals' fate."
  - **K26** The Alliance leaders had believed the Scions dead or missing, and now weigh the Black Wolf's ultimatum. *Escape from Castrum Centri* (2.0, main): "The Alliance leaders staked their hopes on the Scions, but now they believe us all dead or missing. … I believe we are all acquainted with the terms of the Black Wolf's ultimatum."

</details>

**#156 only · main**

> Eorzea's leaders refused the Black Wolf's ultimatum and resolved to fight, with the Scions beside them. Thancred remains in the thrall of the Ascian Lahabrea; Minfilia believes destroying the Crystal of Darkness on his person may free him. The Empire still holds the Ultima Weapon, and Cid now serves as the Alliance's man in Ul'dah.

Sources shown: The Black Wolf's Ultimatum — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K30** Eorzea's leaders resolve to fight, and burn the ultimatum. *The Black Wolf's Ultimatum* (2.0, main): "Eorzea's leaders have resolved to fight … The city-state leaders burn the ultimatum."
  - **K31** Minfilia argues that the Black Wolf's offer would doom Eorzea. *The Black Wolf's Ultimatum* (2.0, main): "That which the Black Wolf offers will doom Eorzea, not deliver it"
  - **K33** Destroying the Crystal that binds Thancred, somewhere on his person, may save him. *The Black Wolf's Ultimatum* (2.0, main): "The Crystal that binds Thancred must be somewhere on his person. … One such Crystal may yet be the key to saving Thancred."
  - **K23** The Empire has finished the Ultima Weapon, an Allagan relic excavated beneath Ala Mhigo. *Escape from Castrum Centri* (2.0, main): "They finished it. Ultima Weapon... … It is a relic of ancient Allag, excavated from its resting place deep beneath Ala Mhigo."
  - **K34** Cid is asked to be the Alliance's man in Ul'dah. *The Black Wolf's Ultimatum* (2.0, main): "Cid, would you be our man in Ul'dah?"

</details>

**#157 only · main**

> The Eorzean Alliance has launched Operation Archon, the largest counteroffensive in the realm's history. You led its first phase and slew Rhitahtyn, one of the Black Wolf's most trusted lieutenants, and the Maelstrom and the Order of the Twin Adder now move on imperial castra. The final aim is the Praetorium, where the Ultima Weapon is believed to be housed. Thancred is still possessed.

Sources shown: Operation Archon — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K40** Operation Archon is the Eorzean Alliance's eleventh-hour bid to drive out the Empire. *Operation Archon* (2.0, main): "So begins Operation Archon, the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace."
  - **K41** It is the largest counteroffensive in the realm's history; its last phase is to destroy the Ultima Weapon in the Praetorium. *Operation Archon* (2.0, main): "the largest single counteroffensive in the realm's troubled history … where they will locate and destroy the Ultima Weapon."
  - **K42** You lead the first phase and slay Rhitahtyn, one of the Black Wolf's most trusted lieutenants. *Operation Archon* (2.0, main): "The first shall see us eliminate one of the Black Wolf's most trusted lieutenants … you deal Rhitahtyn his death-blow"
  - **K44** The Maelstrom and the Order of the Twin Adder move against imperial castra. *Operation Archon* (2.0, main): "the Maelstrom moves to blockade Castrum Occidens and Castrum Marinum. … the Order of the Twin Adder advances upon Castrum Oriens."
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"

</details>

**#158 only · main**

> Operation Archon's second phase is under way. While the Immortal Flames strike Castrum Meridianum as a diversion, your task is to slip inside and bring down the magitek field around the Praetorium, where the Ultima Weapon waits. First you raised the spirits of the Alliance troops at Camp Bluefog, who dread what may be the bloodiest battle in history.

Sources shown: A Hero in Need — main scenario quest (2.0); Operation Archon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K50** Phase two is under way: the Immortal Flames will strike Castrum Meridianum as a diversion while you bring down the magitek field around the Praetorium. *A Hero in Need* (2.0, main): "Phase two of the operation is presently in motion. … The Immortal Flames shall strike at Castrum Meridianum by way of a diversionary maneuver. … you are to infiltrate the stronghold and bring down the magitek field that surrounds the Praetorium."
  - **K41** It is the largest counteroffensive in the realm's history; its last phase is to destroy the Ultima Weapon in the Praetorium. *Operation Archon* (2.0, main): "the largest single counteroffensive in the realm's troubled history … where they will locate and destroy the Ultima Weapon."
  - **K51** The Alliance troops at Camp Bluefog are in low spirits before what may be the bloodiest battle in history. *A Hero in Need* (2.0, main): "the Alliance garrison at [[Camp Bluefog]] is in low spirits and would be better for a hero's visit. … the bloodiest battle in history"

</details>

**#159 only · main**

> With the assault on Castrum Meridianum close, you helped General Raubahn rally the wavering garrison at the Ceruleum Processing Plant. The plan holds: while the Alliance strikes outside, you are to infiltrate the castrum and bring down the magitek field that shields the Praetorium and the Ultima Weapon. Thancred remains in the Ascian Lahabrea's thrall.

Sources shown: Hearts on Fire — main scenario quest (2.0); A Hero in Need — main scenario quest (2.0); Operation Archon — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K55** You help General Raubahn rally the garrison at the Ceruleum Processing Plant. *Hearts on Fire* (2.0, main): "Raubahn bids you rally the garrison at the Ceruleum Processing Plant. … the entire garrison is fairly ablaze with determination."
  - **K50** Phase two is under way: the Immortal Flames will strike Castrum Meridianum as a diversion while you bring down the magitek field around the Praetorium. *A Hero in Need* (2.0, main): "Phase two of the operation is presently in motion. … The Immortal Flames shall strike at Castrum Meridianum by way of a diversionary maneuver. … you are to infiltrate the stronghold and bring down the magitek field that surrounds the Praetorium."
  - **K41** It is the largest counteroffensive in the realm's history; its last phase is to destroy the Ultima Weapon in the Praetorium. *Operation Archon* (2.0, main): "the largest single counteroffensive in the realm's troubled history … where they will locate and destroy the Ultima Weapon."
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"

</details>

**#160 only · main**

> You broke into Castrum Meridianum and, with Cid guiding you, brought down the magitek field around the Praetorium. Livia, the tribunus who captured the Scions, fought you and fell. The Praetorium can now be reached only aboard Cid's airship, the Enterprise, and what remains is to find and destroy the Ultima Weapon. Thancred is still possessed.

Sources shown: Rock the Castrum — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K61** While you create a diversion, Cid finds the generator, and the magitek field comes down. *Rock the Castrum* (2.0, main): "If you could create a diversion─that's to say, wreak lots of havoc─I'll search for the field generator. … we've succeeded in bringing down the generator tower─and with it, the magitek field!"
  - **K22** Livia, the tribunus, captured the Scions and means to study Minfilia's Echo. *Escape from Castrum Centri* (2.0, main): "captured by the tribunus herself! … This “Echo” of yours intrigues us."
  - **K62** Livia, devoted to Gaius, fights you and dies. *Rock the Castrum* (2.0, main): "My minions, my comrades...even my lord Gaius! … Another poor fool who craved Gaius's affection over all else... May her soul know rest."
  - **K63** Only the Enterprise can reach the Praetorium, and all that remains is to destroy the Ultima Weapon. *Rock the Castrum* (2.0, main): "Nay, we'll need to take the ''Enterprise''. … All that remains is the small matter of finding and destroying the Ultima Weapon."
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"

</details>

**2.0 onward · main**

> Aboard the Enterprise you stormed the Praetorium. Gaius urged Cid to take up his father's mantle in the Empire, and Cid refused. The Black Wolf turned the Ultima Weapon on you and you laid it low; then the Ascian Lahabrea, who had quickened the weapon with the primals' life force, came for you himself, and you freed Thancred from his enthrallment. Gaius is slain and the Ultima Weapon destroyed.

Sources shown: The Ultimate Weapon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K70** Gaius asks Cid to take up his father's mantle as the Empire's lead engineer, and Cid refuses. *The Ultimate Weapon* (2.0, main): "Take up your father's mantle, and become the Empire's lead engineer. … I have long known my destiny, and I assure you, it lies ''not'' with the Empire!"
  - **K71** The Black Wolf turns the Ultima Weapon on you, and you lay it low. *The Ultimate Weapon* (2.0, main): "Taking control of the fearsome weapon, the Black Wolf sets upon you once more. … you weather the Ultima Weapon's relentless onslaught and succeed in laying it low."
  - **K72** Lahabrea quickened the weapon's core with the primals' life force, then comes to eliminate you himself. *The Ultimate Weapon* (2.0, main): "I sought the life force of the primals for no other reason but to quicken the core. … now intends to eliminate you himself,"
  - **C09** The player frees Thancred from Lahabrea's enthrallment, and he returns with them. *The Ultimate Weapon* (2.0, main): "free your comrade Thancred from his enthrallment … Look! Thancred is with him/her!"
  - **K73** Gaius is slain and the Ultima Weapon destroyed. *The Ultimate Weapon* (2.0, main): "slain, and the Ultima Weapon destroyed,"

</details>

### Operation Archon (`evt-operation-archon`, event)

**#157–#159 · main**

> The Eorzean Alliance's eleventh-hour bid to drive the Empire from the realm: the largest counteroffensive in its history, in four phases, ending with the destruction of the Ultima Weapon in the Praetorium of Castrum Meridianum. You led the first phase and slew Rhitahtyn, and the Maelstrom and the Order of the Twin Adder move against imperial castra. The Scions and Cid stand with the Alliance.

Sources shown: Operation Archon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K40** Operation Archon is the Eorzean Alliance's eleventh-hour bid to drive out the Empire. *Operation Archon* (2.0, main): "So begins Operation Archon, the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace."
  - **K41** It is the largest counteroffensive in the realm's history; its last phase is to destroy the Ultima Weapon in the Praetorium. *Operation Archon* (2.0, main): "the largest single counteroffensive in the realm's troubled history … where they will locate and destroy the Ultima Weapon."
  - **K42** You lead the first phase and slay Rhitahtyn, one of the Black Wolf's most trusted lieutenants. *Operation Archon* (2.0, main): "The first shall see us eliminate one of the Black Wolf's most trusted lieutenants … you deal Rhitahtyn his death-blow"
  - **K44** The Maelstrom and the Order of the Twin Adder move against imperial castra. *Operation Archon* (2.0, main): "the Maelstrom moves to blockade Castrum Occidens and Castrum Marinum. … the Order of the Twin Adder advances upon Castrum Oriens."
  - **K43** Minfilia, Cid and Alphinaud advise the main host, and the other Scions go with their Grand Companies. *Operation Archon* (2.0, main): "Minfilia, Cid, and I shall accompany the main host in an advisory capacity. … pray accompany your respective organizations on their missions."

</details>

**#160 only · main**

> The Eorzean Alliance's eleventh-hour bid to drive the Empire from the realm, in four phases. You slew Rhitahtyn in the first, the Maelstrom blockaded Castrum Occidens and Castrum Marinum in the second, and in the third you and Cid brought down the magitek field around the Praetorium. The last phase is to destroy the Ultima Weapon within.

Sources shown: Operation Archon — main scenario quest (2.0); Rock the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K40** Operation Archon is the Eorzean Alliance's eleventh-hour bid to drive out the Empire. *Operation Archon* (2.0, main): "So begins Operation Archon, the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace."
  - **K42** You lead the first phase and slay Rhitahtyn, one of the Black Wolf's most trusted lieutenants. *Operation Archon* (2.0, main): "The first shall see us eliminate one of the Black Wolf's most trusted lieutenants … you deal Rhitahtyn his death-blow"
  - **K60** Phase two succeeds: Castrum Occidens and Castrum Marinum are under blockade. *Rock the Castrum* (2.0, main): "Phase two of Operation Archon is a success! … Castrum Occidens and Castrum Marinum are now under blockade!"
  - **K61** While you create a diversion, Cid finds the generator, and the magitek field comes down. *Rock the Castrum* (2.0, main): "If you could create a diversion─that's to say, wreak lots of havoc─I'll search for the field generator. … we've succeeded in bringing down the generator tower─and with it, the magitek field!"
  - **K63** Only the Enterprise can reach the Praetorium, and all that remains is to destroy the Ultima Weapon. *Rock the Castrum* (2.0, main): "Nay, we'll need to take the ''Enterprise''. … All that remains is the small matter of finding and destroying the Ultima Weapon."

</details>

**2.0 onward · main**

> The Eorzean Alliance's eleventh-hour counteroffensive against the Empire, the largest in the realm's history. It ran from the death of Rhitahtyn at Cape Westwind to the Praetorium of Castrum Meridianum, where Gaius was slain and the Ultima Weapon destroyed.

Sources shown: Operation Archon — main scenario quest (2.0); The Ultimate Weapon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K40** Operation Archon is the Eorzean Alliance's eleventh-hour bid to drive out the Empire. *Operation Archon* (2.0, main): "So begins Operation Archon, the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace."
  - **K41** It is the largest counteroffensive in the realm's history; its last phase is to destroy the Ultima Weapon in the Praetorium. *Operation Archon* (2.0, main): "the largest single counteroffensive in the realm's troubled history … where they will locate and destroy the Ultima Weapon."
  - **K42** You lead the first phase and slay Rhitahtyn, one of the Black Wolf's most trusted lieutenants. *Operation Archon* (2.0, main): "The first shall see us eliminate one of the Black Wolf's most trusted lieutenants … you deal Rhitahtyn his death-blow"
  - **K73** Gaius is slain and the Ultima Weapon destroyed. *The Ultimate Weapon* (2.0, main): "slain, and the Ultima Weapon destroyed,"

</details>

### Cid (`char-cid`, character)

**#110–#128 · main** · Also searchable as: Marques

> An engineer, missing since the Calamity, who lived as Marques at the church in eastern Thanalan with no memory of his past. Alphinaud recognized him, and he has joined the search for his lost airship, the Enterprise, which the Scions need to reach Garuda.

Sources shown: Eyes on Me — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110c** Alphinaud declares Marques to be Cid, missing since the Calamity five years ago. *Eyes on Me* (2.0, main): "declares Marques to be none other than Master Cid … who has been missing since the Calamity five years ago."
  - **E110d** Cid has not recovered his memories, but believes Alphinaud and joins him. *Eyes on Me* (2.0, main): "While he has yet to recover his lost memories, Cid senses that the boy speaks the truth, and decides to join him."
  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."

</details>

**#129 only · main** · Also searchable as: Marques

> An engineer, missing since the Calamity, who lived as Marques with no memory of his past. He has his airship, the Enterprise, back from the Stone Vigil, and he knows it, though he can't recall more. It must be repaired before it can brave the storm around Garuda.

Sources shown: Eyes on Me — main scenario quest (2.0); In Pursuit of the Past — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110c** Alphinaud declares Marques to be Cid, missing since the Calamity five years ago. *Eyes on Me* (2.0, main): "declares Marques to be none other than Master Cid … who has been missing since the Calamity five years ago."
  - **E129d** Cid knows the airship, though he cannot say more. *In Pursuit of the Past* (2.0, main): "I...I ''know'' this airship."
  - **E129e** The Enterprise is in no condition to weather Garuda's storm. *In Pursuit of the Past* (2.0, main): "it is plain the ''Enterprise'' is in no condition to weather the storm"

</details>

**#130–#140 · main** · Also searchable as: Marques

> An engineer, missing since the Calamity, who lived as Marques with no memory of his past. He is repairing his airship, the Enterprise, and plans to use a corrupted crystal to change the aspect of Garuda's wind barrier so the ship can pass.

Sources shown: Eyes on Me — main scenario quest (2.0); Into the Eye of the Storm — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110c** Alphinaud declares Marques to be Cid, missing since the Calamity five years ago. *Eyes on Me* (2.0, main): "declares Marques to be none other than Master Cid … who has been missing since the Calamity five years ago."
  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"

</details>

**#141–#146 · main** · Also searchable as: Marques

> A brilliant engineer, born and raised in Garlemald, who left the Empire for Eorzea and built the Ironworks. With the Echo you guided him through the memories he had lost, and he flew the Enterprise to the Howling Eye, where Gaius, who knows him, scorned him for forsaking kin and country.

Sources shown: Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K07** Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks. *Lady of the Vortex* (2.0, main): "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."
  - **E141b** With the Echo you guide Cid through his lost memories of leaving Garlemald for Eorzea. *Lady of the Vortex* (2.0, main): "you guide him through a series of forgotten memories, detailing the path that led the once-loyal engineer to turn his back on [[Garlemald]] and flee to [[Eorzea]]."
  - **E141a** The Enterprise is ready to fly to the Howling Eye. *Lady of the Vortex* (2.0, main): "the ''Enterprise'' is finally ready to make the journey to [[the Howling Eye]]."
  - **K08** Gaius knows Cid, and reproaches him for forsaking kin and country. *Lady of the Vortex* (2.0, main): "Ah, Cid, my boy. You look well─for one who has forsaken ''kin'' and country."

</details>

**#147 only · main** · Also searchable as: Marques

> A brilliant engineer from Garlemald who left the Empire and built the Ironworks. Gaius knows him and scorns him for forsaking kin and country. His Ironworks crew, Biggs and Wedge, are back with him.

Sources shown: Lady of the Vortex — main scenario quest (2.0); Notorious Biggs — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K07** Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks. *Lady of the Vortex* (2.0, main): "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."
  - **K08** Gaius knows Cid, and reproaches him for forsaking kin and country. *Lady of the Vortex* (2.0, main): "Ah, Cid, my boy. You look well─for one who has forsaken ''kin'' and country."
  - **E147e** Cid and his two core Ironworks members are together again. *Notorious Biggs* (2.0, main): "the three core members of [[Garlond Ironworks]] are together again"

</details>

**#148–#153 · main** · Also searchable as: Marques

> A brilliant engineer from Garlemald who left the Empire and built the Ironworks. Gaius knows him and scorns him for forsaking kin and country. With his crew back, he means to break into Castrum Centri disguised as imperial troops and rescue the captive Scions.

Sources shown: Lady of the Vortex — main scenario quest (2.0); Notorious Biggs — main scenario quest (2.0); Come-Into-My-Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K07** Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks. *Lady of the Vortex* (2.0, main): "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."
  - **K08** Gaius knows Cid, and reproaches him for forsaking kin and country. *Lady of the Vortex* (2.0, main): "Ah, Cid, my boy. You look well─for one who has forsaken ''kin'' and country."
  - **E147e** Cid and his two core Ironworks members are together again. *Notorious Biggs* (2.0, main): "the three core members of [[Garlond Ironworks]] are together again"
  - **E148a** Cid means to march in disguised as imperial troops. *Come-Into-My-Castrum* (2.0, main): "Aye, we'll disguise ourselves as imperial troops and march right in."

</details>

**#154 only · main**

> A brilliant engineer, born and raised in Garlemald, who left the Empire for Eorzea and built the Ironworks. He has an airship of his own. Gaius knows him and scorns him for forsaking kin and country. With his crew he restored a suit of magitek armor to break into Castrum Centri and rescue the captive Scions.

Sources shown: Eyes on Me — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0); Come-Into-My-Castrum — main scenario quest (2.0); Every Little Thing She Does Is Magitek — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K05** Alphinaud seeks out Cid as the greatest engineer of the age. *Eyes on Me* (2.0, main): "I have come in search of a legend─the greatest engineer of our time."
  - **K06** Cid has an airship of his own. *Eyes on Me* (2.0, main): "Yes, Cid, you do. Your very own airship."
  - **K07** Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks. *Lady of the Vortex* (2.0, main): "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."
  - **K08** Gaius knows Cid, and reproaches him for forsaking kin and country. *Lady of the Vortex* (2.0, main): "Ah, Cid, my boy. You look well─for one who has forsaken ''kin'' and country."
  - **K04** Cid prepares a plan to rescue the captive Scions. *Come-Into-My-Castrum* (2.0, main): "wants to prepare a strategy to rescue"
  - **K09** Cid's crew restores a suit of magitek armor, and the time comes to infiltrate Castrum Centri and rescue the Scions. *Every Little Thing She Does Is Magitek* (2.0, main): "you are now the proud owner of a fully functional suit of magitek armor. … At long last, the time is come to infiltrate [[Castrum Centri]] and rescue the imprisoned [[Scions]]."

</details>

**#155 only · main**

> A brilliant engineer from Garlemald who left the Empire and built the Ironworks. He planned the rescue at Castrum Centri, and he and Alphinaud drew off the guards while the captive Scions were freed.

Sources shown: Eyes on Me — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K05** Alphinaud seeks out Cid as the greatest engineer of the age. *Eyes on Me* (2.0, main): "I have come in search of a legend─the greatest engineer of our time."
  - **K07** Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks. *Lady of the Vortex* (2.0, main): "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."
  - **K21** Cid and Alphinaud create a diversion outside the castrum. *Escape from Castrum Centri* (2.0, main): "Alphinaud and I will create a diversion out here and keep them occupied for as long as we are able."
  - **K20** The rescue party frees the captives held in Castrum Centri's storage tower. *Escape from Castrum Centri* (2.0, main): "and the others are being held within the storage tower. … Though the rescue mission was a success"

</details>

**#156 only · main**

> A brilliant engineer from Garlemald who left the Empire and built the Ironworks. After the rescue at Castrum Centri, the Alliance asked him to be its man in Ul'dah.

Sources shown: Eyes on Me — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0); The Black Wolf's Ultimatum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K05** Alphinaud seeks out Cid as the greatest engineer of the age. *Eyes on Me* (2.0, main): "I have come in search of a legend─the greatest engineer of our time."
  - **K07** Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks. *Lady of the Vortex* (2.0, main): "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."
  - **K34** Cid is asked to be the Alliance's man in Ul'dah. *The Black Wolf's Ultimatum* (2.0, main): "Cid, would you be our man in Ul'dah?"

</details>

**#157–#159 · main**

> A brilliant engineer from Garlemald who left the Empire and built the Ironworks. The Alliance asked him to be its man in Ul'dah, and he advises the main host of Operation Archon alongside Minfilia and Alphinaud.

Sources shown: Eyes on Me — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0); The Black Wolf's Ultimatum — main scenario quest (2.0); Operation Archon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K05** Alphinaud seeks out Cid as the greatest engineer of the age. *Eyes on Me* (2.0, main): "I have come in search of a legend─the greatest engineer of our time."
  - **K07** Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks. *Lady of the Vortex* (2.0, main): "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."
  - **K34** Cid is asked to be the Alliance's man in Ul'dah. *The Black Wolf's Ultimatum* (2.0, main): "Cid, would you be our man in Ul'dah?"
  - **K43** Minfilia, Cid and Alphinaud advise the main host, and the other Scions go with their Grand Companies. *Operation Archon* (2.0, main): "Minfilia, Cid, and I shall accompany the main host in an advisory capacity. … pray accompany your respective organizations on their missions."

</details>

**#160 only · main**

> A brilliant engineer from Garlemald who left the Empire and built the Ironworks. In the assault on Castrum Meridianum he found the field generator and brought down the magitek field while you created a diversion, and only his airship, the Enterprise, can now reach the Praetorium.

Sources shown: Eyes on Me — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0); Rock the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K05** Alphinaud seeks out Cid as the greatest engineer of the age. *Eyes on Me* (2.0, main): "I have come in search of a legend─the greatest engineer of our time."
  - **K07** Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks. *Lady of the Vortex* (2.0, main): "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."
  - **K61** While you create a diversion, Cid finds the generator, and the magitek field comes down. *Rock the Castrum* (2.0, main): "If you could create a diversion─that's to say, wreak lots of havoc─I'll search for the field generator. … we've succeeded in bringing down the generator tower─and with it, the magitek field!"
  - **K63** Only the Enterprise can reach the Praetorium, and all that remains is to destroy the Ultima Weapon. *Rock the Castrum* (2.0, main): "Nay, we'll need to take the ''Enterprise''. … All that remains is the small matter of finding and destroying the Ultima Weapon."

</details>

**2.0 onward · main**

> A brilliant engineer from Garlemald who left the Empire and built the Ironworks. He flew you into the Praetorium aboard his airship, the Enterprise, where Gaius urged him to take up his father's mantle as the Empire's lead engineer, and he refused.

Sources shown: Eyes on Me — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0); Rock the Castrum — main scenario quest (2.0); The Ultimate Weapon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K05** Alphinaud seeks out Cid as the greatest engineer of the age. *Eyes on Me* (2.0, main): "I have come in search of a legend─the greatest engineer of our time."
  - **K07** Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks. *Lady of the Vortex* (2.0, main): "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."
  - **K63** Only the Enterprise can reach the Praetorium, and all that remains is to destroy the Ultima Weapon. *Rock the Castrum* (2.0, main): "Nay, we'll need to take the ''Enterprise''. … All that remains is the small matter of finding and destroying the Ultima Weapon."
  - **K70** Gaius asks Cid to take up his father's mantle as the Empire's lead engineer, and Cid refuses. *The Ultimate Weapon* (2.0, main): "Take up your father's mantle, and become the Empire's lead engineer. … I have long known my destiny, and I assure you, it lies ''not'' with the Empire!"

</details>

### Gaius (`char-gaius`, character)

**#141–#142 · main** · Also searchable as: the Black Wolf

> The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. At the Howling Eye he called forth an imperial weapon that overpowered and seemingly absorbed three primals. He knows Cid, and scorned him for forsaking kin and country.

Sources shown: Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K10** Gaius, the Black Wolf, is legatus of the XIVth Imperial Legion and commands the Garlean invasion of Eorzea. *Lady of the Vortex* (2.0, main): "legatus of the XIVth Imperial Legion, and supreme commander of the Garlean invasion force in Eorzea. … Of course, the Black Wolf─how could I not realize?"
  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."
  - **K08** Gaius knows Cid, and reproaches him for forsaking kin and country. *Lady of the Vortex* (2.0, main): "Ah, Cid, my boy. You look well─for one who has forsaken ''kin'' and country."

</details>

**#143–#153 · main** · Also searchable as: the Black Wolf

> The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. He called forth an imperial weapon that overpowered and seemingly absorbed three primals, and he means to purge the land of its false gods.

Sources shown: Lady of the Vortex — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K10** Gaius, the Black Wolf, is legatus of the XIVth Imperial Legion and commands the Garlean invasion of Eorzea. *Lady of the Vortex* (2.0, main): "legatus of the XIVth Imperial Legion, and supreme commander of the Garlean invasion force in Eorzea. … Of course, the Black Wolf─how could I not realize?"
  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."
  - **K12** Gaius means to purge Eorzea of its gods. *Casing the Castrum* (2.0, main): "At last, we have the power to purge this land of its false gods."

</details>

**#154 only · main** · Also searchable as: the Black Wolf

> The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. He called forth an imperial weapon that overpowered and seemingly absorbed three primals, and he means to purge the land of its false gods.

Sources shown: Lady of the Vortex — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K10** Gaius, the Black Wolf, is legatus of the XIVth Imperial Legion and commands the Garlean invasion of Eorzea. *Lady of the Vortex* (2.0, main): "legatus of the XIVth Imperial Legion, and supreme commander of the Garlean invasion force in Eorzea. … Of course, the Black Wolf─how could I not realize?"
  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."
  - **K12** Gaius means to purge Eorzea of its gods. *Casing the Castrum* (2.0, main): "At last, we have the power to purge this land of its false gods."

</details>

**#155–#156 · main** · Also searchable as: the Black Wolf

> The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. The Empire has finished the Ultima Weapon, an ancient Allagan relic, and he demands that the realm submit to his power or share the primals' fate. The Ascian Lahabrea stands beside him.

Sources shown: Lady of the Vortex — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K10** Gaius, the Black Wolf, is legatus of the XIVth Imperial Legion and commands the Garlean invasion of Eorzea. *Lady of the Vortex* (2.0, main): "legatus of the XIVth Imperial Legion, and supreme commander of the Garlean invasion force in Eorzea. … Of course, the Black Wolf─how could I not realize?"
  - **K23** The Empire has finished the Ultima Weapon, an Allagan relic excavated beneath Ala Mhigo. *Escape from Castrum Centri* (2.0, main): "They finished it. Ultima Weapon... … It is a relic of ancient Allag, excavated from its resting place deep beneath Ala Mhigo."
  - **K25** Gaius demands the realm submit to his power; resistance means sharing the primals' fate. *Escape from Castrum Centri* (2.0, main): "This realm founders for want of a ruler with true power─the power to cast down eikons. … Yet offer resistance, and he swears that we shall share the primals' fate."
  - **K24** Lahabrea stands beside the Black Wolf. *Escape from Castrum Centri* (2.0, main): "Look! There, beside the Black Wolf!"

</details>

**#157–#160 · main** · Also searchable as: the Black Wolf

> The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. Eorzea's leaders rejected his ultimatum, and when Operation Archon claimed his trusted lieutenant Rhitahtyn, he ordered his tribuni to crush the resistance. He holds the Ultima Weapon.

Sources shown: Lady of the Vortex — main scenario quest (2.0); The Black Wolf's Ultimatum — main scenario quest (2.0); Operation Archon — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K10** Gaius, the Black Wolf, is legatus of the XIVth Imperial Legion and commands the Garlean invasion of Eorzea. *Lady of the Vortex* (2.0, main): "legatus of the XIVth Imperial Legion, and supreme commander of the Garlean invasion force in Eorzea. … Of course, the Black Wolf─how could I not realize?"
  - **K30** Eorzea's leaders resolve to fight, and burn the ultimatum. *The Black Wolf's Ultimatum* (2.0, main): "Eorzea's leaders have resolved to fight … The city-state leaders burn the ultimatum."
  - **K42** You lead the first phase and slay Rhitahtyn, one of the Black Wolf's most trusted lieutenants. *Operation Archon* (2.0, main): "The first shall see us eliminate one of the Black Wolf's most trusted lieutenants … you deal Rhitahtyn his death-blow"
  - **K45** In Gaius's war council, Livia mourns Rhitahtyn, and Gaius orders his tribuni to crush the resistance. *Operation Archon* (2.0, main): "Rhitahtyn... … We shall crush them as we crushed the eikons! … Yes, my lord!"
  - **K23** The Empire has finished the Ultima Weapon, an Allagan relic excavated beneath Ala Mhigo. *Escape from Castrum Centri* (2.0, main): "They finished it. Ultima Weapon... … It is a relic of ancient Allag, excavated from its resting place deep beneath Ala Mhigo."

</details>

**2.0 onward · main** · Also searchable as: the Black Wolf

> The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. In the Praetorium he urged Cid to join the Empire and turned the Ultima Weapon on you. He was slain, and the weapon destroyed.

Sources shown: Lady of the Vortex — main scenario quest (2.0); The Ultimate Weapon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K10** Gaius, the Black Wolf, is legatus of the XIVth Imperial Legion and commands the Garlean invasion of Eorzea. *Lady of the Vortex* (2.0, main): "legatus of the XIVth Imperial Legion, and supreme commander of the Garlean invasion force in Eorzea. … Of course, the Black Wolf─how could I not realize?"
  - **K70** Gaius asks Cid to take up his father's mantle as the Empire's lead engineer, and Cid refuses. *The Ultimate Weapon* (2.0, main): "Take up your father's mantle, and become the Empire's lead engineer. … I have long known my destiny, and I assure you, it lies ''not'' with the Empire!"
  - **K71** The Black Wolf turns the Ultima Weapon on you, and you lay it low. *The Ultimate Weapon* (2.0, main): "Taking control of the fearsome weapon, the Black Wolf sets upon you once more. … you weather the Ultima Weapon's relentless onslaught and succeed in laying it low."
  - **K73** Gaius is slain and the Ultima Weapon destroyed. *The Ultimate Weapon* (2.0, main): "slain, and the Ultima Weapon destroyed,"

</details>

### Livia (`char-livia`, character)

**#106–#153 · main**

> An imperial officer who led the raid on the Waking Sands. She refused Minfilia's surrender, took her prisoner, and is eager to learn about the Echo.

Sources shown: All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **K02** Livia wants Minfilia for the Echo. *All Good Things* (2.0, main): "They say she also possesses the Echo. I cannot wait to hear her scream."

</details>

**#154 only · main**

> An imperial officer who led the raid on the Waking Sands. She refused Minfilia's surrender, took her prisoner, and is eager to learn about the Echo.

Sources shown: All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **K02** Livia wants Minfilia for the Echo. *All Good Things* (2.0, main): "They say she also possesses the Echo. I cannot wait to hear her scream."

</details>

**#155–#156 · main**

> An imperial tribunus who captured the Scions in the raid on the Waking Sands and means to study Minfilia's Echo. The captives escaped her at Castrum Centri.

Sources shown: Escape from Castrum Centri — main scenario quest (2.0); All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K22** Livia, the tribunus, captured the Scions and means to study Minfilia's Echo. *Escape from Castrum Centri* (2.0, main): "captured by the tribunus herself! … This “Echo” of yours intrigues us."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **K20** The rescue party frees the captives held in Castrum Centri's storage tower. *Escape from Castrum Centri* (2.0, main): "and the others are being held within the storage tower. … Though the rescue mission was a success"

</details>

**#157–#159 · main**

> An imperial tribunus who captured the Scions in the raid on the Waking Sands. She stands in Gaius's war council, and mourned Rhitahtyn when Operation Archon claimed him.

Sources shown: Escape from Castrum Centri — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Operation Archon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K22** Livia, the tribunus, captured the Scions and means to study Minfilia's Echo. *Escape from Castrum Centri* (2.0, main): "captured by the tribunus herself! … This “Echo” of yours intrigues us."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **K45** In Gaius's war council, Livia mourns Rhitahtyn, and Gaius orders his tribuni to crush the resistance. *Operation Archon* (2.0, main): "Rhitahtyn... … We shall crush them as we crushed the eikons! … Yes, my lord!"

</details>

**#160 onward · main**

> An imperial tribunus who captured the Scions in the raid on the Waking Sands. Utterly devoted to Gaius, she fought you in Castrum Meridianum and died.

Sources shown: Escape from Castrum Centri — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Rock the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K22** Livia, the tribunus, captured the Scions and means to study Minfilia's Echo. *Escape from Castrum Centri* (2.0, main): "captured by the tribunus herself! … This “Echo” of yours intrigues us."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **K62** Livia, devoted to Gaius, fights you and dies. *Rock the Castrum* (2.0, main): "My minions, my comrades...even my lord Gaius! … Another poor fool who craved Gaius's affection over all else... May her soul know rest."

</details>

### Lahabrea (`char-lahabrea`, character)

**#105–#128 · main**

> A figure who appeared with imperial officers at the Navel after Titan fell, and urged you on, saying your work is far from done. Y'shtola is troubled that the elusive Ascians would consort with the Empire.

Sources shown: Lord of Crags — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E105e** Lahabrea urges you on, saying your work is far from done. *Lord of Crags* (2.0, main): "Carry on, crystal bearer. Far though you have come, your work is far from done."
  - **K14** The Ascians are elusive, and Y'shtola is troubled that they would consort with the Empire. *Lord of Crags* (2.0, main): "Well, the Ascians are nothing if not elusive. … But that they would choose to consort with the ''Empire''..."

</details>

**#129–#140 · main**

> An Ascian, one of an elusive kind that the Scions are troubled to find consorting with the Empire. In the Stone Vigil he woke the dragon that guarded the Enterprise, taunting that Garuda is stronger than any primal you have faced.

Sources shown: In Pursuit of the Past — main scenario quest (2.0); Lord of Crags — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K13** Lahabrea is an Ascian. *In Pursuit of the Past* (2.0, main): "the [[Ascian]] uses his magicks to awaken the dragon"
  - **K14** The Ascians are elusive, and Y'shtola is troubled that they would consort with the Empire. *Lord of Crags* (2.0, main): "Well, the Ascians are nothing if not elusive. … But that they would choose to consort with the ''Empire''..."
  - **E129b** Lahabrea taunts that Garuda is stronger than any primal you have faced. *In Pursuit of the Past* (2.0, main): "And you are aware that her strength greatly exceeds that of your previous primal conquests?"

</details>

**#141–#153 · main**

> An Ascian, one of an elusive kind that the Scions are troubled to find consorting with the Empire. He marveled as the Empire's weapon grew stronger with each primal it consumed.

Sources shown: In Pursuit of the Past — main scenario quest (2.0); Lord of Crags — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K13** Lahabrea is an Ascian. *In Pursuit of the Past* (2.0, main): "the [[Ascian]] uses his magicks to awaken the dragon"
  - **K14** The Ascians are elusive, and Y'shtola is troubled that they would consort with the Empire. *Lord of Crags* (2.0, main): "Well, the Ascians are nothing if not elusive. … But that they would choose to consort with the ''Empire''..."
  - **K15** Lahabrea marvels as the weapon grows stronger with each primal it consumes. *Lady of the Vortex* (2.0, main): "With each primal it consumes, it grows more powerful. A marvel, is it not?"

</details>

**#154 only · main**

> An Ascian, one of an elusive kind that the Scions are troubled to find consorting with the Empire. He marveled as the Empire's weapon grew stronger with each primal it consumed.

Sources shown: In Pursuit of the Past — main scenario quest (2.0); Lord of Crags — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K13** Lahabrea is an Ascian. *In Pursuit of the Past* (2.0, main): "the [[Ascian]] uses his magicks to awaken the dragon"
  - **K14** The Ascians are elusive, and Y'shtola is troubled that they would consort with the Empire. *Lord of Crags* (2.0, main): "Well, the Ascians are nothing if not elusive. … But that they would choose to consort with the ''Empire''..."
  - **K15** Lahabrea marvels as the weapon grows stronger with each primal it consumes. *Lady of the Vortex* (2.0, main): "With each primal it consumes, it grows more powerful. A marvel, is it not?"

</details>

**#155 only · main**

> An Ascian who stands beside the Black Wolf. During the rescue at Castrum Centri, the Scions discovered that he has possessed Thancred.

Sources shown: In Pursuit of the Past — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K13** Lahabrea is an Ascian. *In Pursuit of the Past* (2.0, main): "the [[Ascian]] uses his magicks to awaken the dragon"
  - **K24** Lahabrea stands beside the Black Wolf. *Escape from Castrum Centri* (2.0, main): "Look! There, beside the Black Wolf!"
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"

</details>

**#156–#160 · main**

> An Ascian who stands beside the Black Wolf and has possessed Thancred. Ascians are immortal beings without physical form who possess mortals through Crystals of Darkness.

Sources shown: Escape from Castrum Centri — main scenario quest (2.0); The Black Wolf's Ultimatum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K24** Lahabrea stands beside the Black Wolf. *Escape from Castrum Centri* (2.0, main): "Look! There, beside the Black Wolf!"
  - **C37** The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea. *Escape from Castrum Centri* (2.0, main): "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"
  - **K32** Ascians are immortal beings without physical form who possess mortals through Crystals of Darkness. *The Black Wolf's Ultimatum* (2.0, main): "the Ascians are immortal beings without physical form. … malign artifacts known as Crystals of Darkness."

</details>

**2.0 onward · main**

> An Ascian. He quickened the Ultima Weapon's core with the life force of the primals it absorbed, and when the weapon fell he came for you himself. You freed Thancred, whom he had possessed.

Sources shown: The Ultimate Weapon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K72** Lahabrea quickened the weapon's core with the primals' life force, then comes to eliminate you himself. *The Ultimate Weapon* (2.0, main): "I sought the life force of the primals for no other reason but to quicken the core. … now intends to eliminate you himself,"
  - **C09** The player frees Thancred from Lahabrea's enthrallment, and he returns with them. *The Ultimate Weapon* (2.0, main): "free your comrade Thancred from his enthrallment … Look! Thancred is with him/her!"
  - **K74** The Crystal that bound Thancred is no more. *The Ultimate Weapon* (2.0, main): "Though the Crystal that bound Thancred is no more"

</details>

### The Eorzean Alliance (`org-eorzean-alliance`, organization)

**#155 only · main**

> The alliance of Eorzea's city-states. Its leaders had staked their hopes on the Scions and believed them dead or missing, and they are weighing the Black Wolf's ultimatum.

Sources shown: Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K26** The Alliance leaders had believed the Scions dead or missing, and now weigh the Black Wolf's ultimatum. *Escape from Castrum Centri* (2.0, main): "The Alliance leaders staked their hopes on the Scions, but now they believe us all dead or missing. … I believe we are all acquainted with the terms of the Black Wolf's ultimatum."

</details>

**#156 only · main**

> The alliance of Eorzea's city-states. Its leaders rejected the Black Wolf's ultimatum and resolved to fight: Gridania goes to war, and the Maelstrom will secure the Lominsan coast. They asked Cid to be the Alliance's man in Ul'dah.

Sources shown: The Black Wolf's Ultimatum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K30** Eorzea's leaders resolve to fight, and burn the ultimatum. *The Black Wolf's Ultimatum* (2.0, main): "Eorzea's leaders have resolved to fight … The city-state leaders burn the ultimatum."
  - **K36** Gridania goes to war, and the Maelstrom will secure the Lominsan coast. *The Black Wolf's Ultimatum* (2.0, main): "Gridania will go to war. … The Maelstrom will secure strategic points along the coastline."
  - **K34** Cid is asked to be the Alliance's man in Ul'dah. *The Black Wolf's Ultimatum* (2.0, main): "Cid, would you be our man in Ul'dah?"

</details>

**#157–#160 · main**

> The alliance of Eorzea's city-states, now waging Operation Archon, its eleventh-hour counteroffensive to drive the Empire from the realm.

Sources shown: Operation Archon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K40** Operation Archon is the Eorzean Alliance's eleventh-hour bid to drive out the Empire. *Operation Archon* (2.0, main): "So begins Operation Archon, the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace."
  - **K41** It is the largest counteroffensive in the realm's history; its last phase is to destroy the Ultima Weapon in the Praetorium. *Operation Archon* (2.0, main): "the largest single counteroffensive in the realm's troubled history … where they will locate and destroy the Ultima Weapon."

</details>

**2.0 onward · main**

> The alliance of Eorzea's city-states. Its Operation Archon carried the fight to the Praetorium, where Gaius was slain and the Ultima Weapon destroyed. Its leaders proclaimed the Seventh Astral Era and announced that their Grand Companies will be joined.

Sources shown: Operation Archon — main scenario quest (2.0); The Ultimate Weapon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K40** Operation Archon is the Eorzean Alliance's eleventh-hour bid to drive out the Empire. *Operation Archon* (2.0, main): "So begins Operation Archon, the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace."
  - **K73** Gaius is slain and the Ultima Weapon destroyed. *The Ultimate Weapon* (2.0, main): "slain, and the Ultima Weapon destroyed,"
  - **K75** Eorzea's leaders proclaim the Seventh Astral Era and announce that their Grand Companies will be joined. *The Ultimate Weapon* (2.0, main): "The Seventh Astral Era is come! … So too shall our Grand Companies be joined henceforth,"

</details>

### The Road to Titan (`evt-road-to-titan`, event)

**#103 only · main**

> The Company of Heroes turned a feast at Costa del Sol into a test, weighing you by deeds rather than reputation. Its five chosen members have judged you a worthy challenger for the primal Titan, and Y'shtola, at your side, warns that the battle has yet to begin. Wheiskaet can tell you how to reach Titan's lair.

Sources shown: In the Company of Heroes — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E103a** The feast was a pretext for the Company of Heroes to judge whether you are worthy to face Titan. *In the Company of Heroes* (2.0, main): "the banquet preparations were but an excuse for his comrades to evaluate your worthiness to face"
  - **E103c** The Company weighs anyone who would follow in its footsteps by deeds, not reputation. *In the Company of Heroes* (2.0, main): "That any who would follow in our footsteps must be weighed and measured─not by their reputation, but by their deeds."
  - **E103b** Five members of the Company of Heroes judge you a worthy challenger. *In the Company of Heroes* (2.0, main): "We five of the Company of Heroes hereby judge you a worthy challenger."
  - **E103d** Y'shtola, with you at the feast, says the battle with Titan has yet to begin. *In the Company of Heroes* (2.0, main): "the battle with Titan has yet to begin."
  - **E103e** Wheiskaet can now tell you how to reach Titan's lair. *In the Company of Heroes* (2.0, main): "may now ask him how to reach Titan's lair"

</details>

**#104 only · main**

> Five members of the Company of Heroes judged you worthy to challenge the primal Titan. Wheiskaet sent you to Bronze Lake to find Riol, another former member, who guards the secret of how to reach Titan and stays hidden until he hears the right signal. He has answered yours.

Sources shown: In the Company of Heroes — main scenario quest (2.0); As You Wish — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E103b** Five members of the Company of Heroes judge you a worthy challenger. *In the Company of Heroes* (2.0, main): "We five of the Company of Heroes hereby judge you a worthy challenger."
  - **E104a** Wheiskaet sends you to Bronze Lake to meet Riol, another former member of the Company. *As You Wish* (2.0, main): "There you will meet with Riol, another man who once served with the Company."
  - **E104b** Riol guards the Company's knowledge and stays hidden until he hears the right signal. *As You Wish* (2.0, main): "To ensure that this knowledge does not fall into the wrong hands, he will remain in hiding until you have given the correct signal."

</details>

**#105 onward · main**

> Riol revealed that the Company of Heroes reached Titan through a beastman aetheryte. Y'shtola stayed behind to keep it working, and you went on alone and struck Titan down in the Navel. Then imperial officers, Rhitahtyn among them, appeared with a figure called Lahabrea, who urged you on: your work is far from done. Y'shtola, troubled that the elusive Ascians would consort with the Empire, stayed behind to investigate.

Sources shown: Lord of Crags — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E105a** The Company of Heroes reached Titan through a beastman aetheryte, not the kobold mines. *Lord of Crags* (2.0, main): "Riol reveals that the [[Company of Heroes]] reached [[Titan]] not by fighting their way through the mines of [[O'Ghomoro]], but by using a beastman [[aetheryte]]."
  - **E105b** Y'shtola stays behind at the aetheryte, so you go on alone. *Lord of Crags* (2.0, main): "It seems you will have to proceed without me, [Forename]."
  - **E105c** Titan, whom the kobolds call Great Father and the Lord of Crags, falls. *Lord of Crags* (2.0, main): "The Lord of Crags, Great Father Titan has fallen!"
  - **E105d** Rhitahtyn, an imperial officer at the Navel, refuses to endorse his comrade's plan. *Lord of Crags* (2.0, main): "I cannot endorse this course of action."
  - **E105e** Lahabrea urges you on, saying your work is far from done. *Lord of Crags* (2.0, main): "Carry on, crystal bearer. Far though you have come, your work is far from done."
  - **K14** The Ascians are elusive, and Y'shtola is troubled that they would consort with the Empire. *Lord of Crags* (2.0, main): "Well, the Ascians are nothing if not elusive. … But that they would choose to consort with the ''Empire''..."
  - **E105f** Y'shtola stays behind to investigate something before she leaves. *Lord of Crags* (2.0, main): "There is something I must investigate before I depart."

</details>

### The Fall of the Waking Sands (`evt-fall-of-the-waking-sands`, event)

**#106 only · main**

> After Titan fell, Minfilia called you back to the Waking Sands, but imperial forces under Livia got there first. They came for the one who slew Ifrit and Titan, slaughtered many Scions, refused Minfilia's offer to surrender if the innocents were spared, and took her prisoner. The dying sylph Noraxia sent you to the church in eastern Thanalan, where Father Iliud took you in.

Sources shown: All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106a** Minfilia calls you back to the Waking Sands. *All Good Things* (2.0, main): "We'll be awaiting your return at the Waking Sands. There is much to discuss."
  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."
  - **E106c** The raiders came for the one who slew Ifrit and Titan. *All Good Things* (2.0, main): "We have come for the one who slayed Ifrit and Titan!"
  - **E106d** Minfilia offered to surrender if the innocents were spared. *All Good Things* (2.0, main): "I surrender myself, on the condition you spare the innocents."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **E106e** The dying sylph Noraxia sends you to the church in eastern Thanalan. *All Good Things* (2.0, main): "At church in eastern Thanalan...walking one must claim sanctuary..."
  - **E106f** Father Iliud has known Minfilia since childhood, swore to support her, and offers the same to her fellow Scions. *All Good Things* (2.0, main): "I have known her since she was but a child... … I swore then to do everything in my power to support her, and I will gladly offer the selfsame service to her brother and sister Scions."

</details>

**#107 only · main**

> Imperial forces under Livia raided the Waking Sands, slaughtered many Scions and took Minfilia prisoner. You have taken sanctuary at the church in eastern Thanalan with Father Iliud. There Marques, a survivor of Carteneau, mended a dead man's broken horologe as though his hands remembered the work, and Sister Eluned wondered whether its owner was a Garlean spy.

Sources shown: All Good Things — main scenario quest (2.0); You Can't Take It with You — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **E106f** Father Iliud has known Minfilia since childhood, swore to support her, and offers the same to her fellow Scions. *All Good Things* (2.0, main): "I have known her since she was but a child... … I swore then to do everything in my power to support her, and I will gladly offer the selfsame service to her brother and sister Scions."
  - **E106g** Marques, a survivor of Carteneau whom the church took in, is set to look after you. *All Good Things* (2.0, main): "Marques is a survivor of the battle of Carteneau. … Had we not taken him into our care, he would surely have perished in the desert. … Marques, I want you to look after [Forename]."
  - **E107a** Marques mended a broken horologe as though he had done it countless times. *You Can't Take It with You* (2.0, main): "I knew exactly what to do, as though I had performed the same motions countless times before..."
  - **E107b** Sister Eluned wonders whether the horologe's dead owner was a Garlean spy. *You Can't Take It with You* (2.0, main): "You don't suppose that the owner might have been a Garlean spy?"

</details>

**#108 only · main**

> Imperial forces under Livia raided the Waking Sands, slaughtered many Scions and took Minfilia prisoner. From the church in eastern Thanalan, where Father Iliud gave you sanctuary, you helped carry the fallen from the Waking Sands for their rites, and the church will see them to Thal's realm.

Sources shown: All Good Things — main scenario quest (2.0); Bringing out the Dead — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **E106f** Father Iliud has known Minfilia since childhood, swore to support her, and offers the same to her fellow Scions. *All Good Things* (2.0, main): "I have known her since she was but a child... … I swore then to do everything in my power to support her, and I will gladly offer the selfsame service to her brother and sister Scions."
  - **E108a** The fallen Scions are carried from the Waking Sands for their rites. *Bringing out the Dead* (2.0, main): "the bodies of your comrades are presently being removed from the Waking Sands and prepared for transport here."
  - **E108b** The church will do all it can to see the dead to Thal's realm. *Bringing out the Dead* (2.0, main): "do everything we can to shepherd them to Thal's realm."

</details>

**#109 only · main**

> Imperial forces under Livia raided the Waking Sands, slaughtered many Scions and took Minfilia prisoner. You returned the body of Noraxia, the sylph who died there, to her people in the Black Shroud, who mourned her as brave; Komuxio vowed vengeance on the imperials. The other fallen Scions now rest in the church's lichyard.

Sources shown: All Good Things — main scenario quest (2.0); Bury Me Not on the Lone Prairie — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **E109a** Noraxia's body is returned to her home in the Black Shroud. *Bury Me Not on the Lone Prairie* (2.0, main): "Sister Eluned believes that it would be best if the [[Noraxia's Corpse|sylph's body]] was returned to her home in [[the Black Shroud]]"
  - **E109b** You were with Noraxia at the end, and her people ask that you tell them she was brave. *Bury Me Not on the Lone Prairie* (2.0, main): "Walking one was with Noraxia at the end... Tell this one that Noraxia was brave."
  - **E109c** The sylph Komuxio demands vengeance on the imperials. *Bury Me Not on the Lone Prairie* (2.0, main): "This one demands vengeance! Imperial ones must pay! Imperial ones must suffer!"
  - **E109d** The remaining Scions are buried in the church's lichyard. *Bury Me Not on the Lone Prairie* (2.0, main): "in your absence, we interred the remaining Scions in the lichyard."

</details>

**#110 onward · main**

> Imperial forces under Livia raided the Waking Sands, slaughtered many Scions and took Minfilia prisoner. At the church that sheltered you, Marques felt watched, and a stranger attacked you in the lichyard; Father Iliud knew his sword for Garlean steel. Then Alphinaud arrived and named Marques as Cid, an engineer missing since the Calamity. Cid has no memory of his past, but he has joined Alphinaud.

Sources shown: All Good Things — main scenario quest (2.0); Eyes on Me — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **E110a** A stranger attacks you in the lichyard, and you kill him in self-defense. *Eyes on Me* (2.0, main): "you come under attack from an unknown assailant … After slaying the man in self-defense, you note that his sword is unlike any you have seen before"
  - **E110b** Iliud knows the sword for Garlean steel: an imperial soldier was watching Marques. *Eyes on Me* (2.0, main): "Recognizing the sword you found to be Garlean steel, Father Iliud concludes that the man observing Marques was an imperial soldier."
  - **E110c** Alphinaud declares Marques to be Cid, missing since the Calamity five years ago. *Eyes on Me* (2.0, main): "declares Marques to be none other than Master Cid … who has been missing since the Calamity five years ago."
  - **E110d** Cid has not recovered his memories, but believes Alphinaud and joins him. *Eyes on Me* (2.0, main): "While he has yet to recover his lost memories, Cid senses that the boy speaks the truth, and decides to join him."

</details>

### The Search for the Enterprise (`evt-search-for-the-enterprise`, event)

**#110 only · main**

> At the church in eastern Thanalan, Alphinaud recognized Marques as Cid, an engineer missing since the Calamity. Cid has no memory of his past, but he has joined Alphinaud: the Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. It was last seen over Gridania.

Sources shown: Eyes on Me — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110c** Alphinaud declares Marques to be Cid, missing since the Calamity five years ago. *Eyes on Me* (2.0, main): "declares Marques to be none other than Master Cid … who has been missing since the Calamity five years ago."
  - **E110d** Cid has not recovered his memories, but believes Alphinaud and joins him. *Eyes on Me* (2.0, main): "While he has yet to recover his lost memories, Cid senses that the boy speaks the truth, and decides to join him."
  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E110f** The Enterprise was last seen over Gridania. *Eyes on Me* (2.0, main): "Together with Cid and Alphinaud, make for Gridania, where the ''Enterprise'' was last seen."

</details>

**#111 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Cid still remembers nothing of his past. A tale says the ship flew northwest from Gridania toward Coerthas, and at Florentel's Spire you found Vortefaurt, who saw it pass.

Sources shown: Eyes on Me — main scenario quest (2.0); He Who Waited Behind — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E110d** Cid has not recovered his memories, but believes Alphinaud and joins him. *Eyes on Me* (2.0, main): "While he has yet to recover his lost memories, Cid senses that the boy speaks the truth, and decides to join him."
  - **E111a** A tale says the Enterprise flew northwest from Gridania toward Coerthas. *He Who Waited Behind* (2.0, main): "It states that the ''Enterprise'' flew northwest from Gridania towards Coerthas."
  - **E111b** Vortefaurt saw the airship pass. *He Who Waited Behind* (2.0, main): "Vortefaurt confirms that he bore witness to the vessel's passing."

</details>

**#112 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Vortefaurt saw the ship vanish over the mountains of Coerthas. The astrologers of Ishgard's Observatorium may have records, but Ser Ludovoix will not let an outsider read them, and Ishgard offers strangers no help.

Sources shown: Eyes on Me — main scenario quest (2.0); Cold Reception — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E112a** The Enterprise vanished over the mountains of Coerthas to the northwest. *Cold Reception* (2.0, main): "According to Vortefaurt, the ''Enterprise'' disappeared over the mountains of [[Coerthas]] to the northwest."
  - **E112b** Ser Ludovoix will not let an outsider read the Observatorium's records. *Cold Reception* (2.0, main): "Hah, how absurd! As if we would permit an outsider to peruse the records of the Observatorium."
  - **E112c** Ishgard lets foreigners travel but offers strangers no help. *Cold Reception* (2.0, main): "The Holy See of Ishgard may allow foreigners to travel freely within these lands, but we do not intend to offer succor to strangers."

</details>

**#113 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. The Observatorium's records may tell where it went, but they chart a war with the dragons that has raged for generations, and even after you saved a knight from heretics sworn to the dragons, they stay closed. An inquisitor, Guillaime, warned you to keep out of Ishgard's affairs.

Sources shown: Eyes on Me — main scenario quest (2.0); Cold Reception — main scenario quest (2.0); The Unending War — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E112b** Ser Ludovoix will not let an outsider read the Observatorium's records. *Cold Reception* (2.0, main): "Hah, how absurd! As if we would permit an outsider to peruse the records of the Observatorium."
  - **E113a** The knight's attackers were heretics sworn to the dragons. *The Unending War* (2.0, main): "the [[Ishgard]]ian names the attackers as heretics─those who have pledged their allegiance to the [[dragon]]s."
  - **E113b** The records bear on a war that has raged for generations. *The Unending War* (2.0, main): "Were our records to fall into the wrong hands, it could change the course of a war which has raged for generations!"
  - **E113c** Inquisitor Guillaime subtly warns you away from Ishgard's affairs. *The Unending War* (2.0, main): "subtly cautioning you against becoming involved in Ishgardian affairs"

</details>

**#114 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Ishgard's Observatorium won't open its records to an outsider, and Inquisitor Guillaime has warned you off. House Durendaire owes you for two good deeds, but Lord Portelaine will introduce you to the other High Houses only after a third.

Sources shown: Eyes on Me — main scenario quest (2.0); Men of Honor — main scenario quest (2.0); The Unending War — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E114a** House Durendaire will still not open the Observatorium's records to you. *Men of Honor* (2.0, main): "Even so, they will ''not'' grant you access to the Observatorium's records."
  - **E113c** Inquisitor Guillaime subtly warns you away from Ishgard's affairs. *The Unending War* (2.0, main): "subtly cautioning you against becoming involved in Ishgardian affairs"
  - **E114b** You must petition Lord Portelaine for introductions to the other High Houses. *Men of Honor* (2.0, main): "Approach Lord [[Portelaine]] and petition him for formal introductions to the other [[High Houses]]"
  - **E114c** Portelaine wants a third deed before he endorses you to three High Houses. *Men of Honor* (2.0, main): "But while you have performed ''two'' acts, you would have me endorse you to ''three'' High Houses."

</details>

**#115 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Seeking help from Ishgard's High Houses, you recovered a porter's stolen wares, and among them was a draconian rosary in a chest belonging to Lord Francel of House Haillenarte, a house whispered to be full of heretics. Lord Portelaine has told the inquisitors and warned you away from the house.

Sources shown: Eyes on Me — main scenario quest (2.0); Men of Honor — main scenario quest (2.0); Three for Three — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E114b** You must petition Lord Portelaine for introductions to the other High Houses. *Men of Honor* (2.0, main): "Approach Lord [[Portelaine]] and petition him for formal introductions to the other [[High Houses]]"
  - **E115a** A draconian rosary turns up in a chest belonging to Lord Francel of House Haillenarte. *Three for Three* (2.0, main): "a draconian rosary in a chest belonging to Lord [[Francel]] of [[House Haillenarte]]."
  - **E115b** House Haillenarte is whispered to be full of heretics. *Three for Three* (2.0, main): "House Haillenarte is whispered to be infested with heretics..."
  - **E115c** Portelaine informs the inquisitors and warns you away from House Haillenarte. *Three for Three* (2.0, main): "I shall inform the inquisitors immediately. Under these circumstances, I must strongly advise against associating with House Haillenarte."

</details>

**#116 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. A draconian rosary found among Lord Francel's belongings has put him under suspicion of heresy, though his former servant swears he is innocent. Francel sent you with a letter to Lord Haurchefant of House Fortemps at Camp Dragonhead, who has promised to make inquiries about the ship.

Sources shown: Eyes on Me — main scenario quest (2.0); Three for Three — main scenario quest (2.0); The Rose and the Unicorn — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E115a** A draconian rosary turns up in a chest belonging to Lord Francel of House Haillenarte. *Three for Three* (2.0, main): "a draconian rosary in a chest belonging to Lord [[Francel]] of [[House Haillenarte]]."
  - **E116a** Francel's former servant swears he is no heretic. *The Rose and the Unicorn* (2.0, main): "Lord Francel is no heretic. He is a goodly, righteous man, wholly dedicated to the cause."
  - **E116b** Francel fears the rosary will still be taken as proof against him. *The Rose and the Unicorn* (2.0, main): "Although the draconian rosary was not found in my possession, it will still be considered by many to be proof of my"
  - **E116c** Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead. *The Rose and the Unicorn* (2.0, main): "Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead."
  - **E116e** Haurchefant promises to make inquiries for you. *The Rose and the Unicorn* (2.0, main): "Nevertheless, I will make inquiries on your behalf and share with you my findings in the future."

</details>

**#117 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Lord Haurchefant of House Fortemps is making inquiries for you, but the High Houses have nothing to offer: all of Coerthas talks only of heretics. Since Inquisitor Guillaime arrived, countless have been found, even among Ishgard's elite, and the charge against Lord Francel has thrown House Haillenarte into chaos.

Sources shown: Eyes on Me — main scenario quest (2.0); The Rose and the Unicorn — main scenario quest (2.0); The Talk of Coerthas — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E116e** Haurchefant promises to make inquiries for you. *The Rose and the Unicorn* (2.0, main): "Nevertheless, I will make inquiries on your behalf and share with you my findings in the future."
  - **E117c** All of Coerthas is consumed by talk of heretics in the High Houses. *The Talk of Coerthas* (2.0, main): "It seems the whole of Coerthas is consumed by this talk of heretics in the High Houses."
  - **E117a** Since Inquisitor Guillaime arrived, countless heretics have been found, even among Ishgard's elite. *The Talk of Coerthas* (2.0, main): "Why, in the short time since Inquisitor Guillaime arrived in Coerthas, countless heretics have been discovered, even amongst the elite of Ishgardian society!"
  - **E117b** The heresy accusations have thrown House Haillenarte into chaos. *The Talk of Coerthas* (2.0, main): "But these accusations of heresy have thrown House Haillenarte into chaos."

</details>

**#118 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. Lord Haurchefant has found a witness to its flight, but he won't speak to anyone tied to an accused heretic. You saved Lord Francel at the Steel Vigil, where he hoped to prove his devotion. His heresy trial approaches, and his name, and yours with it, must be cleared first.

Sources shown: Eyes on Me — main scenario quest (2.0); Road to Redemption — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E118c** A witness to the Enterprise's flight has been found, but is reluctant to meet you. *Road to Redemption* (2.0, main): "the witness became understandably reticent to make your acquaintance"
  - **E118a** Francel went to the Steel Vigil hoping to show his devotion by slaying scalekin. *Road to Redemption* (2.0, main): "I had hoped we might demonstrate our devotion by slaying a number of the scalekin."
  - **E118b** Francel's trial approaches. *Road to Redemption* (2.0, main): "The day of my trial approaches."
  - **E118d** Francel's name, and so yours, must be cleared first. *Road to Redemption* (2.0, main): "we must first clear Lord Francel's name─and, by association, yours."

</details>

**#119 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. A witness to its flight won't talk until Lord Francel is cleared of heresy. Haurchefant believes the rosary against Francel was planted, and two parcels bound for Skyfire Locks each held another: a crude attempt to smear House Haillenarte. Francel's trial is at hand.

Sources shown: Eyes on Me — main scenario quest (2.0); Road to Redemption — main scenario quest (2.0); Following the Evidence — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E118c** A witness to the Enterprise's flight has been found, but is reluctant to meet you. *Road to Redemption* (2.0, main): "the witness became understandably reticent to make your acquaintance"
  - **E119a** Haurchefant believes the rosary was planted. *Following the Evidence* (2.0, main): "If the rosary was not his, then someone else with access ''must'' have planted it."
  - **E119b** Two parcels bound for Skyfire Locks each held a draconian rosary. *Following the Evidence* (2.0, main): "the two parcels bound for [[Skyfire Locks]] both contained a draconian rosary!"
  - **E119c** Haurchefant calls it a crass attempt to sully House Haillenarte. *Following the Evidence* (2.0, main): "Even the inquisitors must acknowledge that this is no more than a crass attempt to sully House Haillenarte's reputation."
  - **E119d** Francel's trial is at hand. *Following the Evidence* (2.0, main): "Lord Francel's trial is upon us, and we must act now if we are to clear his name!"

</details>

**#120 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. At Witchdrop, Inquisitor Guillaime ordered Lord Francel to prove his innocence by leaping from the cliff. You protected him, Haurchefant argued that someone was using the trials to set the houses against each other, and a heretic among the Temple Knights was exposed. Guillaime withdrew the charges, pending investigation.

Sources shown: Eyes on Me — main scenario quest (2.0); In the Eyes of Gods and Men — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E120a** Inquisitor Guillaime presides over Francel's trial at Witchdrop. *In the Eyes of Gods and Men* (2.0, main): "Inquisitor Guillaime presides over Lord Francel's trial at Witchdrop even as we speak."
  - **E120b** Guillaime orders Francel to prove his innocence by leaping from the cliff. *In the Eyes of Gods and Men* (2.0, main): "Leap from the cliff and entrust your fate to the Fury."
  - **E120e** Haurchefant says someone has used the trials to sow discord between the houses. *In the Eyes of Gods and Men* (2.0, main): "They have used you and your fellows to sow discord, Inquisitor─to set brother against brother"
  - **E120c** A heretic among the Temple Knights summoned the wyvern. *In the Eyes of Gods and Men* (2.0, main): "it was ''he'' who summoned the wyvern!"
  - **E120d** Guillaime withdraws the charges against Francel, pending investigation. *In the Eyes of Gods and Men* (2.0, main): "I shall withdraw my charges against Lord Francel, pending further investigation."

</details>

**#121 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. With Lord Francel cleared, the witness spoke: the ship landed near the Stone Vigil before the Calamity, and the outpost is now held by Dravanian forces. Haurchefant has written to Lord Drillemont of Whitebrim Front to ask that you be let in, and Francel warns that those who tried to destroy his house are still unknown.

Sources shown: Eyes on Me — main scenario quest (2.0); In the Eyes of Gods and Men — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E120d** Guillaime withdraws the charges against Francel, pending investigation. *In the Eyes of Gods and Men* (2.0, main): "I shall withdraw my charges against Lord Francel, pending further investigation."
  - **E121a** The Enterprise landed near the Stone Vigil days before the Calamity. *The Final Flight of the Enterprise* (2.0, main): "he saw the ''Enterprise'' land near [[the Stone Vigil]] several days before [[the Calamity]]"
  - **E121b** The Stone Vigil is now held by Dravanian forces. *The Final Flight of the Enterprise* (2.0, main): "the Stone Vigil is currently held by [[Dravanian Horde|Dravanian forces]]"
  - **E121c** Haurchefant writes to Lord Drillemont of Whitebrim Front to ask that you be let in. *The Final Flight of the Enterprise* (2.0, main): "I will write a letter to Lord Drillemont of Whitebrim Front and request that he grant you permission to enter."
  - **E121d** Those who tried to destroy House Haillenarte are still unmasked. *The Final Flight of the Enterprise* (2.0, main): "the cravens who attempted to destroy House Haillenarte have yet to be unmasked"

</details>

**#122 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, now held by Dravanian forces. At Whitebrim Front, Inquisitor Guillaime branded you untrustworthy and the Scions a defunct band the Empire had exterminated, and Lord Drillemont barred the way until the outpost is retaken and you declare your true intentions. Alphinaud means to earn his trust.

Sources shown: Eyes on Me — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0); Ye of Little Faith — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E121a** The Enterprise landed near the Stone Vigil days before the Calamity. *The Final Flight of the Enterprise* (2.0, main): "he saw the ''Enterprise'' land near [[the Stone Vigil]] several days before [[the Calamity]]"
  - **E122a** Alphinaud tells Drillemont you came to slay Garuda and seek the Enterprise. *Ye of Little Faith* (2.0, main): "We are come to Coerthas to slay Garuda, Lady of the Vortex. To that end, we seek the ''Enterprise''"
  - **E122c** Guillaime calls Cid presumed dead and the Scions a defunct band the Empire exterminated. *Ye of Little Faith* (2.0, main): "missing and presumed dead since before the Calamity, and two Scions of the Seventh Dawn─a defunct band of misfits recently exterminated by the Empire."
  - **E122d** Guillaime insists you must not be let through to the Stone Vigil. *Ye of Little Faith* (2.0, main): "I know not why these three seek the Stone Vigil, but I know that we cannot permit them to pass."
  - **E122e** Drillemont bars you until the outpost is retaken and you declare your true intentions. *Ye of Little Faith* (2.0, main): "You three will not enter the outpost until we have reclaimed it─and until you declare your ''true'' intentions as well."
  - **E122f** Alphinaud means to earn Drillemont's trust. *Ye of Little Faith* (2.0, main): "we must do whatever it takes to earn Lord Drillemont's trust. Understood?"

</details>

**#123 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, but Lord Drillemont of Whitebrim Front won't let you in, and Inquisitor Guillaime calls you untrustworthy. To win Drillemont's notice through his knights, you helped the cook feed the hungry barracks.

Sources shown: Eyes on Me — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0); Ye of Little Faith — main scenario quest (2.0); Factual Folklore — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E121a** The Enterprise landed near the Stone Vigil days before the Calamity. *The Final Flight of the Enterprise* (2.0, main): "he saw the ''Enterprise'' land near [[the Stone Vigil]] several days before [[the Calamity]]"
  - **E122e** Drillemont bars you until the outpost is retaken and you declare your true intentions. *Ye of Little Faith* (2.0, main): "You three will not enter the outpost until we have reclaimed it─and until you declare your ''true'' intentions as well."
  - **E122c** Guillaime calls Cid presumed dead and the Scions a defunct band the Empire exterminated. *Ye of Little Faith* (2.0, main): "missing and presumed dead since before the Calamity, and two Scions of the Seventh Dawn─a defunct band of misfits recently exterminated by the Empire."
  - **E123a** The cook says winning over the barracks will catch Drillemont's notice. *Factual Folklore* (2.0, main): "Win over the barracks, and he's sure to take notice."

</details>

**#124 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, but Lord Drillemont of Whitebrim Front won't let you in. Cid built the infirmary a better alembic, but Inquisitor Guillaime warned the chirurgeons that your gifts serve an unknown end, and he seems to hate you and your companions.

Sources shown: Eyes on Me — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0); Ye of Little Faith — main scenario quest (2.0); The Best Inventions — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E121a** The Enterprise landed near the Stone Vigil days before the Calamity. *The Final Flight of the Enterprise* (2.0, main): "he saw the ''Enterprise'' land near [[the Stone Vigil]] several days before [[the Calamity]]"
  - **E122e** Drillemont bars you until the outpost is retaken and you declare your true intentions. *Ye of Little Faith* (2.0, main): "You three will not enter the outpost until we have reclaimed it─and until you declare your ''true'' intentions as well."
  - **E124a** Cid builds the infirmary a better alembic from its broken equipment. *The Best Inventions* (2.0, main): "So I used some of their broken equipment to craft a more advanced alembic─both as a gesture of goodwill"
  - **E124c** Guillaime warns that your efforts serve an unknown end. *The Best Inventions* (2.0, main): "Their earnest efforts are but a means to an as-yet-unknown end."
  - **E124d** The inquisitor seems to hate you and your companions. *The Best Inventions* (2.0, main): "The inquisitor appears to have developed a hatred for you and your associates"

</details>

**#125 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, but Lord Drillemont won't let you in, and Inquisitor Guillaime works against you. You heard he carried an injured knight, Joellaut, to the gates on the night he arrived, and Alphinaud suspects he has other reasons for hindering you.

Sources shown: Eyes on Me — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0); Ye of Little Faith — main scenario quest (2.0); Influencing Inquisitors — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E121a** The Enterprise landed near the Stone Vigil days before the Calamity. *The Final Flight of the Enterprise* (2.0, main): "he saw the ''Enterprise'' land near [[the Stone Vigil]] several days before [[the Calamity]]"
  - **E122e** Drillemont bars you until the outpost is retaken and you declare your true intentions. *Ye of Little Faith* (2.0, main): "You three will not enter the outpost until we have reclaimed it─and until you declare your ''true'' intentions as well."
  - **E125a** The knight Joellaut says Guillaime carried him to the gates when he fell. *Influencing Inquisitors* (2.0, main): "Inquisitor Guillaime rescued ''me'', carrying my unconscious body to the gates."
  - **E125b** Alphinaud suspects Guillaime has other reasons for hindering you. *Influencing Inquisitors* (2.0, main): "I am beginning to suspect he has other reasons for hindering us now."

</details>

**#126 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil, but Lord Drillemont won't let you in. Retracing Joellaut's story of the inquisitor's first night, you found a frozen corpse in a chasm: the real Inquisitor Guillaime, murdered the day he arrived. The man you know by that name is an impostor, and his true identity and motives are unknown.

Sources shown: Eyes on Me — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0); Ye of Little Faith — main scenario quest (2.0); By the Lights of Ishgard — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E121a** The Enterprise landed near the Stone Vigil days before the Calamity. *The Final Flight of the Enterprise* (2.0, main): "he saw the ''Enterprise'' land near [[the Stone Vigil]] several days before [[the Calamity]]"
  - **E122e** Drillemont bars you until the outpost is retaken and you declare your true intentions. *Ye of Little Faith* (2.0, main): "You three will not enter the outpost until we have reclaimed it─and until you declare your ''true'' intentions as well."
  - **E126a** A frozen corpse in the chasm closely resembles Guillaime. *By the Lights of Ishgard* (2.0, main): "a frozen corpse in the chasm which bears a striking resemblance to Inquisitor Guillaime"
  - **E126b** The real inquisitor was murdered on the day he arrived in Coerthas. *By the Lights of Ishgard* (2.0, main): "Newly come to Coerthas and murdered on the day of his arrival..."
  - **E126c** The corpse is the real Inquisitor Guillaime. *By the Lights of Ishgard* (2.0, main): "I believe you have just made the acquaintance of the ''real'' Inquisitor Guillaime."
  - **E126d** The impostor's identity and reasons for opposing you are unknown. *By the Lights of Ishgard* (2.0, main): "we have yet to discern his true identity, or why he has decided to oppose us."

</details>

**#127 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. It landed near the Stone Vigil. The inquisitor who works against you is an impostor: Prunilla confessed he coerced her and condemned innocent people for carrying draconian rosaries, and that she planted some of his rosaries in shipments to Skyfire Locks. Convinced, Lord Drillemont will let you into the Stone Vigil once the impostor faces justice.

Sources shown: Eyes on Me — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0); By the Lights of Ishgard — main scenario quest (2.0); Blood for Blood — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E121a** The Enterprise landed near the Stone Vigil days before the Calamity. *The Final Flight of the Enterprise* (2.0, main): "he saw the ''Enterprise'' land near [[the Stone Vigil]] several days before [[the Calamity]]"
  - **E126c** The corpse is the real Inquisitor Guillaime. *By the Lights of Ishgard* (2.0, main): "I believe you have just made the acquaintance of the ''real'' Inquisitor Guillaime."
  - **E127a** The impostor coerced Prunilla with threats against her loved ones. *Blood for Blood* (2.0, main): "if I defied him...everyone I loved would suffer unimaginable horrors before they died."
  - **E127b** The impostor condemned innocent people found carrying draconian rosaries. *Blood for Blood* (2.0, main): "countless men and women of good moral standing, seized whilst in possession of draconian rosaries."
  - **E127c** Prunilla planted rosaries from his chest in shipments bound for Skyfire Locks. *Blood for Blood* (2.0, main): "I took several from his chest and planted them in shipments bound for Skyfire Locks."
  - **E127d** Drillemont is convinced the inquisitor is a heretic. *Blood for Blood* (2.0, main): "Fury take me, the inquisitor is a ''heretic''!?"
  - **E127e** Drillemont will let you into the outpost, but first asks your help. *Blood for Blood* (2.0, main): "I will permit you to enter the outpost─but first, I must needs beg your assistance."

</details>

**#128 only · main**

> You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. At Snowcloak, Lord Drillemont named the false inquisitor the murderer of the real Guillaime. The impostor called all Ishgard complicit in the archbishop's lies, took the form of a dragon beside his Dravanian allies, and was defeated, warning that the dragons in the Stone Vigil, where the ship landed, would tear you apart.

Sources shown: Eyes on Me — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0); The Heretic among Us — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E121a** The Enterprise landed near the Stone Vigil days before the Calamity. *The Final Flight of the Enterprise* (2.0, main): "he saw the ''Enterprise'' land near [[the Stone Vigil]] several days before [[the Calamity]]"
  - **E128a** Drillemont names the impostor a heretic and the murderer of Inquisitor Guillaime. *The Heretic among Us* (2.0, main): "I name thee ''heretic'', murderer of Inquisitor Guillaime and countless innocents!"
  - **E128b** The impostor calls all Ishgard complicit in the archbishop's lies. *The Heretic among Us* (2.0, main): "''All'' are complicit in these crimes, for ''all'' live their lives by the archbishop's lies."
  - **E128c** He summons his Dravanian allies and takes the form of a dragon. *The Heretic among Us* (2.0, main): "he summons his [[Dravanian Horde|Dravanian allies]] and endeavors to defend himself, going so far as to use his magicks to assume the form of a [[dragon]]."
  - **E128f** You defeat the false inquisitor. *The Heretic among Us* (2.0, main): "Alphinaud refuses to revel in your victory over the false inquisitor"
  - **E128d** He warns that the dragons in the Stone Vigil will tear you apart. *The Heretic among Us* (2.0, main): "The dragons within the Stone Vigil will rend you asunder."

</details>

**#129 onward · main**

> Cid and Alphinaud need Cid's airship, the Enterprise, to reach Garuda, the primal the Ixal have summoned. In the Stone Vigil you found it beside a sleeping dragon, and the Ascian Lahabrea woke the beast, taunting that Garuda is stronger than any primal you have faced. While you held off the dragon, Alphinaud and Cid slipped aboard. Cid knows the ship, though he can't recall more, and it is in no state to weather Garuda's storm.

Sources shown: Eyes on Me — main scenario quest (2.0); In Pursuit of the Past — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **K13** Lahabrea is an Ascian. *In Pursuit of the Past* (2.0, main): "the [[Ascian]] uses his magicks to awaken the dragon"
  - **E129b** Lahabrea taunts that Garuda is stronger than any primal you have faced. *In Pursuit of the Past* (2.0, main): "And you are aware that her strength greatly exceeds that of your previous primal conquests?"
  - **E129c** Alphinaud and Cid slip aboard the Enterprise while you hold off the dragon. *In Pursuit of the Past* (2.0, main): "Cid─you and I will sneak aboard the ''Enterprise'' and prepare it for launch."
  - **E129d** Cid knows the airship, though he cannot say more. *In Pursuit of the Past* (2.0, main): "I...I ''know'' this airship."
  - **E129e** The Enterprise is in no condition to weather Garuda's storm. *In Pursuit of the Past* (2.0, main): "it is plain the ''Enterprise'' is in no condition to weather the storm"

</details>

### Garuda's Barrier (`evt-garudas-barrier`, event)

**#130 only · main**

> The Enterprise is back in Cid's hands, but battered as it is, it can't survive the winds around the Howling Eye, Garuda's sanctuary. While the Seedseers house it for repairs, Cid plans to use a corrupted crystal to change the aspect of Garuda's wind barrier, and he has sent you to Lamberteint, a scholar he met while he lived as Marques.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130e** The Seedseers house the Enterprise for its repairs. *Into the Eye of the Storm* (2.0, main): "The Seedseers have granted our request to house the ''Enterprise''."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E130c** Cid knows of a scholar, Lamberteint, in Camp Drybone. *Into the Eye of the Storm* (2.0, main): "A scholar by the name of Lamberteint, who resides in Camp Drybone."
  - **E130d** Cid met Lamberteint while he lived as Marques at the church. *Into the Eye of the Storm* (2.0, main): "Strange as it may sound, I met him during my time at the church. Well, ''Marques'' met him, I suppose."

</details>

**#131 only · main**

> Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. The scholar Lamberteint lent you a warded pot to carry such a crystal safely, and sent you to his pupil Hahasako at Highbridge.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); Sealed with Science — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E131a** Lamberteint lends you a warded pot and sends you to his pupil Hahasako at Highbridge. *Sealed with Science* (2.0, main): "take the pot to Hahasako, a student of mine monitoring the flow of aether at Highbridge."

</details>

**#132 only · main**

> Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. The crystal you broke from the Burning Wall, with Hahasako's help, is wind-aspected, so it would only strengthen the barrier.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); Sealed with Science — main scenario quest (2.0); With the Utmost Care — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E131a** Lamberteint lends you a warded pot and sends you to his pupil Hahasako at Highbridge. *Sealed with Science* (2.0, main): "take the pot to Hahasako, a student of mine monitoring the flow of aether at Highbridge."
  - **E132a** The crystal from the Burning Wall is wind-aspected and would only strengthen the barrier. *With the Utmost Care* (2.0, main): "A corrupted crystal overflowing with wind-aspected aether. … this crystal would only serve to ''strengthen'' the barrier."

</details>

**#133 only · main**

> Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. The first crystal you found was wind-aspected and useless. Lamberteint's pupil Ceana has found a promising site at Pharos Sirius on the Isles of Umbra, and you found her in Aleport.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); With the Utmost Care — main scenario quest (2.0); A Promising Prospect — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E132a** The crystal from the Burning Wall is wind-aspected and would only strengthen the barrier. *With the Utmost Care* (2.0, main): "A corrupted crystal overflowing with wind-aspected aether. … this crystal would only serve to ''strengthen'' the barrier."
  - **E133a** Another pupil, Ceana, has found a promising site at Pharos Sirius on the Isles of Umbra. *A Promising Prospect* (2.0, main): "It was ''western'' La Noscea─Pharos Sirius, on the Isles of Umbra, to be precise."

</details>

**#134 only · main**

> Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. Lamberteint's pupil Ceana believes the Isles of Umbra hold such crystals, but the isles are closed, and the Yellowjackets speak of spirits and undead there.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); A Promising Prospect — main scenario quest (2.0); It's Probably Not Pirates — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E133a** Another pupil, Ceana, has found a promising site at Pharos Sirius on the Isles of Umbra. *A Promising Prospect* (2.0, main): "It was ''western'' La Noscea─Pharos Sirius, on the Isles of Umbra, to be precise."
  - **E134a** Access to the isles is prohibited. *It's Probably Not Pirates* (2.0, main): "all access to the isles is prohibited at present"
  - **E134b** The Yellowjackets speak of spirits and undead on the isles. *It's Probably Not Pirates* (2.0, main): "The three Yellowjackets you elect to question speak of spirits and undead infesting the Isles of Umbra."

</details>

**#135 only · main**

> Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. The scholar Ceana believes the Isles of Umbra hold such crystals, and the isles are said to be haunted. Mimidoa gave you a writ of passage there in return for looking into the rumors, and Skyfryn, back from the isles, raves of a woman singing to him.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); A Promising Prospect — main scenario quest (2.0); It's Probably Not Pirates — main scenario quest (2.0); Representing the Representative — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E133a** Another pupil, Ceana, has found a promising site at Pharos Sirius on the Isles of Umbra. *A Promising Prospect* (2.0, main): "It was ''western'' La Noscea─Pharos Sirius, on the Isles of Umbra, to be precise."
  - **E134b** The Yellowjackets speak of spirits and undead on the isles. *It's Probably Not Pirates* (2.0, main): "The three Yellowjackets you elect to question speak of spirits and undead infesting the Isles of Umbra."
  - **E135a** Mimidoa gives you a writ of passage if you look into the rumors for him. *Representing the Representative* (2.0, main): "Mimidoa offers you a [[Permission for Passage|writ of passage]], on the condition that you look into the rumors on his behalf."
  - **E135b** Skyfryn, back from the isles, says a woman calls and sings to him. *Representing the Representative* (2.0, main): "I...I have to go back. She calls to me...''sings'' to me..."

</details>

**#136 only · main**

> Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. You crossed to the Isles of Umbra with a writ of passage, but the scholar Ceana fled back to the mainland in fear, and the gate guard, Davyd, can't give you a crystal.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); Representing the Representative — main scenario quest (2.0); The Reluctant Researcher — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E135a** Mimidoa gives you a writ of passage if you look into the rumors for him. *Representing the Representative* (2.0, main): "Mimidoa offers you a [[Permission for Passage|writ of passage]], on the condition that you look into the rumors on his behalf."
  - **E136a** Ceana flees back to the mainland in fear. *The Reluctant Researcher* (2.0, main): "In the end, Ceana succumbs to her fear and flees back to the mainland"
  - **E136b** The gate guard, Davyd, cannot give you a crystal. *The Reluctant Researcher* (2.0, main): "Though [[Davyd]] understands your intent, he is nevertheless unable to oblige you."

</details>

**#137 only · main**

> Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. On the Isles of Umbra, the guard Davyd will find you one if you help solve the island's mystery, and adventurers speak of an irresistible voice at the Ship Graveyard.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); The Reluctant Researcher — main scenario quest (2.0); Sweet Somethings — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E136b** The gate guard, Davyd, cannot give you a crystal. *The Reluctant Researcher* (2.0, main): "Though [[Davyd]] understands your intent, he is nevertheless unable to oblige you."
  - **E137a** Davyd will bring you a crystal if you help solve the mystery. *Sweet Somethings* (2.0, main): "help me unravel this mystery, and I'll bring you your corrupted crystal."
  - **E137b** Adventurers speak of an irresistible voice at the Ship Graveyard. *Sweet Somethings* (2.0, main): "The adventurers speak of a beautiful, irresistible voice heard at [[the Ship Graveyard]], which may be connected to the undead."

</details>

**#138 only · main**

> Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. On the Isles of Umbra, Mimidoa lured a siren ashore and you drove her back into the depths. Davyd kept his word, but the crystal he gave you is fire-aspected and won't help against the wind.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); History Repeating — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E138a** Mimidoa is sure a siren is behind the trouble. *History Repeating* (2.0, main): "Aye...I'd bet me bum ear a siren's behind all this."
  - **E138b** The siren retreats into the depths. *History Repeating* (2.0, main): "before at last relenting and retreating to the depths whence she came."
  - **E138c** Davyd gives you the corrupted crystal as promised. *History Repeating* (2.0, main): "the corrupted crystal you wanted, safely sealed within the pot, just as you requested."
  - **E138d** The crystal is fire-aspected, so it won't help against the wind. *History Repeating* (2.0, main): "the corrupted shard is the manifestation of an over-abundance of the element of fire"

</details>

**#139 only · main**

> Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. Two crystals proved the wrong aspect. In Gridania, Hedyn told you a spriggan had devoured every corrupted crystal in the Twelveswood; you cut the last one from its gut, and it is ice-aspected.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); History Repeating — main scenario quest (2.0); The Curious Case of Giggity — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E138d** The crystal is fire-aspected, so it won't help against the wind. *History Repeating* (2.0, main): "the corrupted shard is the manifestation of an over-abundance of the element of fire"
  - **E139a** A spriggan has devoured every corrupted crystal in the Twelveswood. *The Curious Case of Giggity* (2.0, main): "one such creature with an infamously insatiable appetite has single-handedly devoured every corrupted crystal in the Twelveswood."
  - **E139b** You cut the crystal from the spriggan's gut. *The Curious Case of Giggity* (2.0, main): "you rip and tear open the spriggan's huge guts and claim the corrupted crystal nestled deep within."
  - **E139c** Hedyn confirms the crystal is ice-aspected. *The Curious Case of Giggity* (2.0, main): "Hedyn confirms that the foul-smelling, offal-laden crystal is comprised of ice-aspected aether."

</details>

**#140 only · main**

> Cid has been repairing the Enterprise to pass Garuda's wind barrier. You brought him an ice-aspected corrupted crystal, his work is nearly done, and once it passes his tests, he says, nothing will stand between you and Garuda. This, he says, is what he was born to do.

Sources shown: Into the Eye of the Storm — main scenario quest (2.0); The Curious Case of Giggity — main scenario quest (2.0); Better Late than Never — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E139c** Hedyn confirms the crystal is ice-aspected. *The Curious Case of Giggity* (2.0, main): "Hedyn confirms that the foul-smelling, offal-laden crystal is comprised of ice-aspected aether."
  - **E140a** Cid's work on the Enterprise is nearly done; only the crystal remains to be tested. *Better Late than Never* (2.0, main): "Cid's work on the ''Enterprise'' is nearly complete, and all that remains is for him to test the crystal you have brought."
  - **E140b** Cid says nothing will stand between you and Garuda. *Better Late than Never* (2.0, main): "Once you bring me that crystal, nothing will stand between us and Garuda."
  - **E140c** Cid says this is what he was born to do. *Better Late than Never* (2.0, main): "This...this is me. This is what I was born to do."

</details>

**#141 onward · main**

> The Enterprise carried you to the Howling Eye, and on the way the Echo let you guide Cid through his lost memories of leaving Garlemald for Eorzea. You struck Garuda down, but her Ixali worshippers' belief raised her again, and her dying captives' cries summoned their own gods. Then Gaius, the Black Wolf, called forth an imperial weapon that seemingly absorbed all three primals. The Scions mean to re-form, and to destroy that weapon.

Sources shown: Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E141a** The Enterprise is ready to fly to the Howling Eye. *Lady of the Vortex* (2.0, main): "the ''Enterprise'' is finally ready to make the journey to [[the Howling Eye]]."
  - **E141b** With the Echo you guide Cid through his lost memories of leaving Garlemald for Eorzea. *Lady of the Vortex* (2.0, main): "you guide him through a series of forgotten memories, detailing the path that led the once-loyal engineer to turn his back on [[Garlemald]] and flee to [[Eorzea]]."
  - **E141c** You strike Garuda down, but her Ixali worshippers' belief raises her again. *Lady of the Vortex* (2.0, main): "only to see her rise once more, reinvigorated by the belief of her [[Ixal]]i disciples."
  - **E141d** Garuda's dying kobold and Amalj'aa captives cry out and summon their own gods. *Lady of the Vortex* (2.0, main): "slaughtering her captive [[kobold]]s and [[Amalj'aa]], whose cries of agony serve to summon their own patron deities."
  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."
  - **K10** Gaius, the Black Wolf, is legatus of the XIVth Imperial Legion and commands the Garlean invasion of Eorzea. *Lady of the Vortex* (2.0, main): "legatus of the XIVth Imperial Legion, and supreme commander of the Garlean invasion force in Eorzea. … Of course, the Black Wolf─how could I not realize?"
  - **E141e** All efforts now turn to destroying the Empire's weapon. *Lady of the Vortex* (2.0, main): "all efforts must now be focused upon destroying [[Garlean Empire|the Empire]]'s [[The Ultima Weapon|ultimate weapon]]."
  - **E141f** Cid and Alphinaud resolve to re-form the Scions at the Waking Sands. *Lady of the Vortex* (2.0, main): "Believing the best course of action is to reform [[the Scions of the Seventh Dawn]], they decide to return to [[the Waking Sands]]."

</details>

### The Road to Castrum Centri (`evt-road-to-castrum-centri`, event)

**#142 only · main**

> After the Empire's weapon seemingly absorbed the primals, Alphinaud brought you and Cid back to the ruined Waking Sands to rebuild the Scions. Yda, who was away during the raid, learned that Papalymo and Minfilia were not among the dead, and Y'shtola has found that the captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. Alphinaud believes Gaius means to use Minfilia to understand the Echo.

Sources shown: Lady of the Vortex — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."
  - **E142a** Alphinaud brings you back to the Waking Sands. *Reclamation* (2.0, main): "It is past time that we return to the Waking Sands."
  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E142b** Yda learns that Papalymo and Minfilia were not among the dead. *Reclamation* (2.0, main): "Papalymo and Minfilia weren't among the dead, according to the church."
  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."
  - **E142c** Alphinaud believes Gaius means to use Minfilia to understand the Echo. *Reclamation* (2.0, main): "He means to use Minfilia to gain an understanding of the Echo."

</details>

**#143 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Y'shtola reasons they will be kept alive until the Empire finishes studying the Echo, so you are first going after two escapees, likely Biggs and Wedge, who fled a downed imperial airship and are being hunted in Coerthas. Meanwhile Gaius readies his weapon to purge the land of its gods.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E143d** Y'shtola reasons the captives will not be executed until the study is complete. *Casing the Castrum* (2.0, main): "they will not be executed until such time as the study is complete."
  - **E143c** Two men, likely Biggs and Wedge, escaped a downed imperial airship. *Casing the Castrum* (2.0, main): "two men─likely [[Biggs]] and [[Wedge]]─escaped from a downed imperial airship not long ago."
  - **K12** Gaius means to purge Eorzea of its gods. *Casing the Castrum* (2.0, main): "At last, we have the power to purge this land of its false gods."

</details>

**#144 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. First you are tracking two escapees, likely Biggs and Wedge, who fled a downed imperial airship in Coerthas. Imperial soldiers are hunting them too.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Eyes on the Empire — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E143c** Two men, likely Biggs and Wedge, escaped a downed imperial airship. *Casing the Castrum* (2.0, main): "two men─likely [[Biggs]] and [[Wedge]]─escaped from a downed imperial airship not long ago."
  - **E144a** Imperial soldiers are hunting the escapees. *Eyes on the Empire* (2.0, main): "Imperial soldiers have since been sighted in the area, seeking to recapture them."

</details>

**#145 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. In the snows of Coerthas you found Wedge, one of two escapees from an imperial airship. Biggs went another way to draw their pursuers off and was last seen heading west.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Footprints in the Snow — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E143c** Two men, likely Biggs and Wedge, escaped a downed imperial airship. *Casing the Castrum* (2.0, main): "two men─likely [[Biggs]] and [[Wedge]]─escaped from a downed imperial airship not long ago."
  - **E145a** Wedge says Biggs went another way to lure their pursuers off. *Footprints in the Snow* (2.0, main): "He went off in a different direction to lure our pursuers away."
  - **E145b** Biggs headed west. *Footprints in the Snow* (2.0, main): "At any rate, we know for a fact that Biggs headed west."

</details>

**#146 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. In Coerthas you found Wedge, who escaped from the Empire, but Biggs drew their pursuers away and is still missing. He wasn't in the Fury's Gaze, and Wedge is still determined to find him.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Footprints in the Snow — main scenario quest (2.0); Monumental Hopes — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E145a** Wedge says Biggs went another way to lure their pursuers off. *Footprints in the Snow* (2.0, main): "He went off in a different direction to lure our pursuers away."
  - **E146a** The Fury's Gaze holds only vengeful ghosts. *Monumental Hopes* (2.0, main): "Your search of the Fury's Gaze yields nothing but a confrontation with vengeful ghosts."
  - **E146b** Wedge is still determined to find Biggs. *Monumental Hopes* (2.0, main): "is no less determined to find his companion."

</details>

**#147 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Yda and Y'shtola helped you rescue Biggs from imperial troops, so Cid's Ironworks crew is together again. Biggs and Wedge were taken to Castrum Centri too, and escaped by sabotaging an airship. Y'shtola suspects the raiders reached the Waking Sands by teleportation of the kind the Ascians use.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Notorious Biggs — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E147a** With Yda and Y'shtola you rescue Biggs from imperial troops. *Notorious Biggs* (2.0, main): "With the aid of [[Yda]] and [[Y'shtola]], you succeed in rescuing Biggs from a detachment of imperial troops."
  - **E147e** Cid and his two core Ironworks members are together again. *Notorious Biggs* (2.0, main): "the three core members of [[Garlond Ironworks]] are together again"
  - **E147c** Biggs and Wedge were held at Castrum Centri apart from Minfilia and the others. *Notorious Biggs* (2.0, main): "we found ourselves in the midst of an imperial stronghold─Castrum Centri. … Biggs and I were thrown into a detainment cell together, while Minfilia and the others were taken elsewhere."
  - **E147d** They escaped by sabotaging an airship's altitude control. *Notorious Biggs* (2.0, main): "we sabotaged the ship's altitude control and thereby forced an emergency landing."
  - **E147b** Y'shtola believes the raiders arrived by teleportation of the kind the Ascians use. *Notorious Biggs* (2.0, main): "they were borne there by potent teleportation magicks─magicks of the kind used by the Ascians."

</details>

**#148 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. The stronghold is on high alert, so Cid means to march in disguised as imperial troops. At Revenant's Toll you recruited Glaumunt, who bears a grudge against the Empire and knows the castrum, while Y'shtola and Yda scout it.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Come-Into-My-Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E148b** Castrum Centri is on high alert. *Come-Into-My-Castrum* (2.0, main): "Not even a fly could get within a hundred yalms of the walls undetected."
  - **E148a** Cid means to march in disguised as imperial troops. *Come-Into-My-Castrum* (2.0, main): "Aye, we'll disguise ourselves as imperial troops and march right in."
  - **E148c** Glaumunt has a grudge against the Empire and knows Castrum Centri. *Come-Into-My-Castrum* (2.0, main): "The fellow's got a personal grudge against the Empire, and happens to know a deal about Castrum Centri besides."
  - **E148e** Glaumunt will help you. *Come-Into-My-Castrum* (2.0, main): "If his response is any indication, it would seem you can indeed expect his aid."
  - **E148d** Y'shtola and Yda go to scout the stronghold. *Come-Into-My-Castrum* (2.0, main): "Yda and I shall go to reconnoiter Garlean activity at the stronghold."

</details>

**#149 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Cid means to march in disguised as imperial troops. Through a drainage pipe, you overheard guards say the tribunus is obsessed with Minfilia, who they believe has a mystical power. Alphinaud is sure the captives are inside, and Glaumunt is seeking a suit of magitek armor.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Come-Into-My-Castrum — main scenario quest (2.0); Getting Even with Garlemald — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E148a** Cid means to march in disguised as imperial troops. *Come-Into-My-Castrum* (2.0, main): "Aye, we'll disguise ourselves as imperial troops and march right in."
  - **E149e** Glaumunt shows you a drainage pipe from the command tower for listening in. *Getting Even with Garlemald* (2.0, main): "He tells you of a drainage pipe that leads from the stronghold's command tower"
  - **E149a** A guard wonders why the tribunus is so obsessed with Minfilia. *Getting Even with Garlemald* (2.0, main): "I do wonder, why is the tribunus so obsessed with this Minfilia woman?"
  - **E149b** The guards say Minfilia has a mystical power the Garleans lack. *Getting Even with Garlemald* (2.0, main): "They say she possesses some mystical power. Something we Garleans don't have."
  - **E149c** Alphinaud is sure the captives are inside Castrum Centri. *Getting Even with Garlemald* (2.0, main): "So Minfilia and the others are indeed at Castrum Centri!"
  - **E149d** Glaumunt is seeking a suit of magitek armor. *Getting Even with Garlemald* (2.0, main): "Glaumunt is looking into ways to procure a suit of magitek armor."

</details>

**#150 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Cid and Glaumunt are preparing to march in disguised as imperial troops, with a suit of magitek armor if one can be found. For Cid you took readings at a crystal cluster near Revenant's Toll, so that he can jam imperial communications, though he is reluctant to use the crystals' power.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Come-Into-My-Castrum — main scenario quest (2.0); Getting Even with Garlemald — main scenario quest (2.0); Drowning Out the Voices — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E148a** Cid means to march in disguised as imperial troops. *Come-Into-My-Castrum* (2.0, main): "Aye, we'll disguise ourselves as imperial troops and march right in."
  - **E149d** Glaumunt is seeking a suit of magitek armor. *Getting Even with Garlemald* (2.0, main): "Glaumunt is looking into ways to procure a suit of magitek armor."
  - **E150a** Cid prepares to jam imperial communications using crystals that amplify their energy, though he is reluctant to use them. *Drowning Out the Voices* (2.0, main): "Cid is satisfied that the crystals will suit his needs, though he expresses his reluctance to harness their power."

</details>

**#150b only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. Glaumunt's plan is to send you into the castrum dressed as an imperial soldier, so you learned the imperial salute by watching the patrols. Cid is ready to jam imperial communications, and a suit of magitek armor is still needed.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Acting the Part — main scenario quest (2.0); Drowning Out the Voices — main scenario quest (2.0); Getting Even with Garlemald — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E150c** Glaumunt's plan is to send you into Castrum Centri in imperial dress. *Acting the Part* (2.0, main): "The plan's to have you enter Castrum Centri all decked out in imperial duds"
  - **E150d** You learn the imperial salute by watching patrols. *Acting the Part* (2.0, main): "You have committed the imperial salute to your memory."
  - **E150a** Cid prepares to jam imperial communications using crystals that amplify their energy, though he is reluctant to use them. *Drowning Out the Voices* (2.0, main): "Cid is satisfied that the crystals will suit his needs, though he expresses his reluctance to harness their power."
  - **E149d** Glaumunt is seeking a suit of magitek armor. *Getting Even with Garlemald* (2.0, main): "Glaumunt is looking into ways to procure a suit of magitek armor."

</details>

**#151 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. You, Biggs and Wedge will go in disguised as imperial soldiers. Sark Malark, a friend of Glaumunt's, had you take three sets of imperial gear for the three of you, and the smith Eginolf repaired them. All that's still missing is a suit of magitek armor.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Acting the Part — main scenario quest (2.0); Dressed for Conquest — main scenario quest (2.0); Getting Even with Garlemald — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E150c** Glaumunt's plan is to send you into Castrum Centri in imperial dress. *Acting the Part* (2.0, main): "The plan's to have you enter Castrum Centri all decked out in imperial duds"
  - **E151a** Three sets of imperial gear are needed: for Biggs, Wedge and you. *Dressed for Conquest* (2.0, main): "three sets of gear, one for each member of the infiltration team─Biggs, Wedge, and yourself."
  - **E151b** Sark Malark, a friend of Glaumunt's, helps with the disguises, and Eginolf repairs the gear. *Dressed for Conquest* (2.0, main): "I have heard of your plight from my friend Glaumunt. … Yes, these will serve beautifully. The great Eginolf never fails to impress."
  - **E149d** Glaumunt is seeking a suit of magitek armor. *Getting Even with Garlemald* (2.0, main): "Glaumunt is looking into ways to procure a suit of magitek armor."

</details>

**#153 only · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. You, Biggs and Wedge will go in disguised as imperial soldiers. Glaumunt fed the imperials false word of insurgents to draw out a patrol, and with Cid's help you seized a magitek reaper. Biggs and Wedge are repairing it at Cid's workshop.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Dressed for Conquest — main scenario quest (2.0); Fool Me Twice — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E151a** Three sets of imperial gear are needed: for Biggs, Wedge and you. *Dressed for Conquest* (2.0, main): "three sets of gear, one for each member of the infiltration team─Biggs, Wedge, and yourself."
  - **E153a** Glaumunt fed the imperials false intelligence to draw out a patrol. *Fool Me Twice* (2.0, main): "I took the liberty o' feedin' 'em a bit o' the old false intelligence"
  - **E153b** You seize a magitek reaper, which needs repairs. *Fool Me Twice* (2.0, main): "You have succeeded in acquiring a magitek reaper, though some repairs will be required before it can be put to use."
  - **E153c** Biggs and Wedge repair the reaper at Cid's workshop. *Fool Me Twice* (2.0, main): "have already set about repairing the magitek reaper."

</details>

**#154 onward · main**

> Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. You, Biggs and Wedge will go in disguised as imperial soldiers. Cid's crew restored the magitek reaper you seized, and after you fought off imperial troops sent to reclaim it, the armor works. The time has come to infiltrate Castrum Centri and rescue the imprisoned Scions.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Dressed for Conquest — main scenario quest (2.0); Fool Me Twice — main scenario quest (2.0); Every Little Thing She Does Is Magitek — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **K16** Alphinaud means to rebuild the Scions. *Reclamation* (2.0, main): "It is up to us to rebuild the Scions and save Eorzea."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E151a** Three sets of imperial gear are needed: for Biggs, Wedge and you. *Dressed for Conquest* (2.0, main): "three sets of gear, one for each member of the infiltration team─Biggs, Wedge, and yourself."
  - **E153b** You seize a magitek reaper, which needs repairs. *Fool Me Twice* (2.0, main): "You have succeeded in acquiring a magitek reaper, though some repairs will be required before it can be put to use."
  - **K09** Cid's crew restores a suit of magitek armor, and the time comes to infiltrate Castrum Centri and rescue the Scions. *Every Little Thing She Does Is Magitek* (2.0, main): "you are now the proud owner of a fully functional suit of magitek armor. … At long last, the time is come to infiltrate [[Castrum Centri]] and rescue the imprisoned [[Scions]]."

</details>

### Yda (`char-yda`, character)

**#102–#141 · main**

> A Scion, one of the friends Minfilia introduced you to in the order.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."

</details>

**#142–#146 · main**

> A Scion who was away when the Waking Sands was raided. She learned that Papalymo and Minfilia were not among the dead.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **E142b** Yda learns that Papalymo and Minfilia were not among the dead. *Reclamation* (2.0, main): "Papalymo and Minfilia weren't among the dead, according to the church."

</details>

**#147–#154 · main**

> A Scion who was away when the Waking Sands was raided. With Y'shtola she helped you rescue Biggs from imperial troops.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Reclamation — main scenario quest (2.0); Notorious Biggs — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **E142b** Yda learns that Papalymo and Minfilia were not among the dead. *Reclamation* (2.0, main): "Papalymo and Minfilia weren't among the dead, according to the church."
  - **E147a** With Yda and Y'shtola you rescue Biggs from imperial troops. *Notorious Biggs* (2.0, main): "With the aid of [[Yda]] and [[Y'shtola]], you succeed in rescuing Biggs from a detachment of imperial troops."

</details>

**#155 onward · main**

> A Scion who was away when the Waking Sands was raided. During the rescue at Castrum Centri she and Y'shtola rode in aboard your vehicle and confronted Livia, who led the raid.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Reclamation — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **E142b** Yda learns that Papalymo and Minfilia were not among the dead. *Reclamation* (2.0, main): "Papalymo and Minfilia weren't among the dead, according to the church."
  - **E155b** Y'shtola and Yda rode into the castrum aboard your vehicle. *Escape from Castrum Centri* (2.0, main): "There chanced to be a commotion outside the castrum's walls which allowed us to avail ourselves of the comforts of your vehicle."
  - **E155a** Y'shtola and Yda confront Livia, who led the raid on the Waking Sands. *Escape from Castrum Centri* (2.0, main): "'Twas you who led the raid on the Waking Sands─you who butchered unarmed men and women for the crime of being unworthy of capture."

</details>

### Papalymo (`char-papalymo`, character)

**#102–#141 · main**

> A Scion, one of the friends Minfilia introduced you to in the order.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."

</details>

**#142 only · main**

> A Scion. After the raid on the Waking Sands, Yda learned that he was not among the dead.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **E142b** Yda learns that Papalymo and Minfilia were not among the dead. *Reclamation* (2.0, main): "Papalymo and Minfilia weren't among the dead, according to the church."

</details>

**#143–#154 · main**

> A Scion taken in the raid on the Waking Sands. Scouts saw him among four prisoners led into Castrum Centri.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **E142b** Yda learns that Papalymo and Minfilia were not among the dead. *Reclamation* (2.0, main): "Papalymo and Minfilia weren't among the dead, according to the church."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."

</details>

**#155 onward · main**

> A Scion taken in the raid on the Waking Sands. He was among the prisoners held at Castrum Centri, and was freed in the rescue.

Sources shown: A Wild Rose by Any Other Name — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C31** Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled. *A Wild Rose by Any Other Name* (2.0, main): "I would introduce you to your friends in the order. … Those same brave souls stand before you now."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **K20** The rescue party frees the captives held in Castrum Centri's storage tower. *Escape from Castrum Centri* (2.0, main): "and the others are being held within the storage tower. … Though the rescue mission was a success"

</details>

### Titan (`char-titan`, character)

**#103–#104 · main**

> A primal. The Company of Heroes has judged you worthy to challenge him.

Sources shown: In the Company of Heroes — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E103b** Five members of the Company of Heroes judge you a worthy challenger. *In the Company of Heroes* (2.0, main): "We five of the Company of Heroes hereby judge you a worthy challenger."
  - **E103e** Wheiskaet can now tell you how to reach Titan's lair. *In the Company of Heroes* (2.0, main): "may now ask him how to reach Titan's lair"

</details>

**#105–#140 · main** · Also searchable as: the Lord of Crags

> The primal the kobolds call their Great Father, the Lord of Crags. The Company of Heroes once reached him through a beastman aetheryte, and you struck him down in the Navel.

Sources shown: Lord of Crags — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E105c** Titan, whom the kobolds call Great Father and the Lord of Crags, falls. *Lord of Crags* (2.0, main): "The Lord of Crags, Great Father Titan has fallen!"
  - **E105a** The Company of Heroes reached Titan through a beastman aetheryte, not the kobold mines. *Lord of Crags* (2.0, main): "Riol reveals that the [[Company of Heroes]] reached [[Titan]] not by fighting their way through the mines of [[O'Ghomoro]], but by using a beastman [[aetheryte]]."

</details>

**#141 onward · main** · Also searchable as: the Lord of Crags

> The primal the kobolds call their Great Father, the Lord of Crags. You struck him down in the Navel. At the Howling Eye, the dying cries of Garuda's captives summoned their own gods, and the Empire's weapon seemingly absorbed all three primals.

Sources shown: Lord of Crags — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E105c** Titan, whom the kobolds call Great Father and the Lord of Crags, falls. *Lord of Crags* (2.0, main): "The Lord of Crags, Great Father Titan has fallen!"
  - **E141d** Garuda's dying kobold and Amalj'aa captives cry out and summon their own gods. *Lady of the Vortex* (2.0, main): "slaughtering her captive [[kobold]]s and [[Amalj'aa]], whose cries of agony serve to summon their own patron deities."
  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."

</details>

### Rhitahtyn (`char-rhitahtyn`, character)

**#105–#142 · main**

> An imperial officer who appeared at the Navel after Titan fell, and refused to endorse his comrade's plan.

Sources shown: Lord of Crags — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E105d** Rhitahtyn, an imperial officer at the Navel, refuses to endorse his comrade's plan. *Lord of Crags* (2.0, main): "I cannot endorse this course of action."

</details>

**#143–#156 · main**

> An imperial officer who serves Gaius. After Titan fell he refused to endorse a comrade's plan, and Gaius has sent him to Castrum Occidens.

Sources shown: Lord of Crags — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E105d** Rhitahtyn, an imperial officer at the Navel, refuses to endorse his comrade's plan. *Lord of Crags* (2.0, main): "I cannot endorse this course of action."
  - **E143e** Gaius sends Rhitahtyn to Castrum Occidens. *Casing the Castrum* (2.0, main): "Rhitahtyn. You depart for Castrum Occidens at midnight."

</details>

**#157 onward · main**

> An imperial officer who served Gaius as one of the Black Wolf's most trusted lieutenants, sent to Castrum Occidens. You slew him in the first phase of Operation Archon.

Sources shown: Casing the Castrum — main scenario quest (2.0); Operation Archon — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E143e** Gaius sends Rhitahtyn to Castrum Occidens. *Casing the Castrum* (2.0, main): "Rhitahtyn. You depart for Castrum Occidens at midnight."
  - **K42** You lead the first phase and slay Rhitahtyn, one of the Black Wolf's most trusted lieutenants. *Operation Archon* (2.0, main): "The first shall see us eliminate one of the Black Wolf's most trusted lieutenants … you deal Rhitahtyn his death-blow"

</details>

### Noraxia (`char-noraxia`, character)

**#106–#108 · main**

> A sylph you found dying at the Waking Sands after the imperial raid. With her last words she sent you to the church in eastern Thanalan.

Sources shown: All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106e** The dying sylph Noraxia sends you to the church in eastern Thanalan. *All Good Things* (2.0, main): "At church in eastern Thanalan...walking one must claim sanctuary..."

</details>

**#109 onward · main**

> A sylph who died in the imperial raid on the Waking Sands, after sending you to the church in eastern Thanalan. You returned her body to her people in the Black Shroud, who mourned her as brave.

Sources shown: All Good Things — main scenario quest (2.0); Bury Me Not on the Lone Prairie — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106e** The dying sylph Noraxia sends you to the church in eastern Thanalan. *All Good Things* (2.0, main): "At church in eastern Thanalan...walking one must claim sanctuary..."
  - **E109a** Noraxia's body is returned to her home in the Black Shroud. *Bury Me Not on the Lone Prairie* (2.0, main): "Sister Eluned believes that it would be best if the [[Noraxia's Corpse|sylph's body]] was returned to her home in [[the Black Shroud]]"
  - **E109b** You were with Noraxia at the end, and her people ask that you tell them she was brave. *Bury Me Not on the Lone Prairie* (2.0, main): "Walking one was with Noraxia at the end... Tell this one that Noraxia was brave."

</details>

### Iliud (`char-iliud`, character)

**#106–#109 · main** · Also searchable as: Father Iliud

> A priest at the church in eastern Thanalan who has known Minfilia since she was a child, and has sworn to support her and her fellow Scions. He gave you sanctuary after the raid on the Waking Sands.

Sources shown: All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106f** Father Iliud has known Minfilia since childhood, swore to support her, and offers the same to her fellow Scions. *All Good Things* (2.0, main): "I have known her since she was but a child... … I swore then to do everything in my power to support her, and I will gladly offer the selfsame service to her brother and sister Scions."
  - **E106g** Marques, a survivor of Carteneau whom the church took in, is set to look after you. *All Good Things* (2.0, main): "Marques is a survivor of the battle of Carteneau. … Had we not taken him into our care, he would surely have perished in the desert. … Marques, I want you to look after [Forename]."

</details>

**#110 onward · main** · Also searchable as: Father Iliud

> A priest at the church in eastern Thanalan who has known Minfilia since she was a child, and has sworn to support her and her fellow Scions. He sheltered you after the raid on the Waking Sands, and knew the sword of the man watching Marques for Garlean steel.

Sources shown: All Good Things — main scenario quest (2.0); Eyes on Me — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106f** Father Iliud has known Minfilia since childhood, swore to support her, and offers the same to her fellow Scions. *All Good Things* (2.0, main): "I have known her since she was but a child... … I swore then to do everything in my power to support her, and I will gladly offer the selfsame service to her brother and sister Scions."
  - **E110b** Iliud knows the sword for Garlean steel: an imperial soldier was watching Marques. *Eyes on Me* (2.0, main): "Recognizing the sword you found to be Garlean steel, Father Iliud concludes that the man observing Marques was an imperial soldier."

</details>

### Marques (`char-marques`, character)

**#106 only · main**

> A survivor of the battle of Carteneau whom the church in eastern Thanalan took in. Father Iliud has asked him to look after you.

Sources shown: All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106g** Marques, a survivor of Carteneau whom the church took in, is set to look after you. *All Good Things* (2.0, main): "Marques is a survivor of the battle of Carteneau. … Had we not taken him into our care, he would surely have perished in the desert. … Marques, I want you to look after [Forename]."

</details>

**#107–#109 · main**

> A survivor of the battle of Carteneau whom the church in eastern Thanalan took in. He mended a dead man's broken horologe as though his hands remembered the work.

Sources shown: All Good Things — main scenario quest (2.0); You Can't Take It with You — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106g** Marques, a survivor of Carteneau whom the church took in, is set to look after you. *All Good Things* (2.0, main): "Marques is a survivor of the battle of Carteneau. … Had we not taken him into our care, he would surely have perished in the desert. … Marques, I want you to look after [Forename]."
  - **E107a** Marques mended a broken horologe as though he had done it countless times. *You Can't Take It with You* (2.0, main): "I knew exactly what to do, as though I had performed the same motions countless times before..."

</details>

**#110 onward · main**

> The name of a survivor of Carteneau whom the church in eastern Thanalan sheltered. Alphinaud recognized him as Cid, an engineer missing since the Calamity.

Sources shown: All Good Things — main scenario quest (2.0); Eyes on Me — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E106g** Marques, a survivor of Carteneau whom the church took in, is set to look after you. *All Good Things* (2.0, main): "Marques is a survivor of the battle of Carteneau. … Had we not taken him into our care, he would surely have perished in the desert. … Marques, I want you to look after [Forename]."
  - **E110c** Alphinaud declares Marques to be Cid, missing since the Calamity five years ago. *Eyes on Me* (2.0, main): "declares Marques to be none other than Master Cid … who has been missing since the Calamity five years ago."

</details>

### Garuda (`char-garuda`, character)

**#110–#128 · main**

> A primal summoned by the Ixal. The Scions need Cid's lost airship, the Enterprise, to reach her.

Sources shown: Eyes on Me — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."

</details>

**#129 only · main**

> A primal summoned by the Ixal. The Ascian Lahabrea taunts that she is stronger than any primal you have faced, and the Enterprise must be repaired to brave her storm.

Sources shown: Eyes on Me — main scenario quest (2.0); In Pursuit of the Past — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E129b** Lahabrea taunts that Garuda is stronger than any primal you have faced. *In Pursuit of the Past* (2.0, main): "And you are aware that her strength greatly exceeds that of your previous primal conquests?"
  - **E129e** The Enterprise is in no condition to weather Garuda's storm. *In Pursuit of the Past* (2.0, main): "it is plain the ''Enterprise'' is in no condition to weather the storm"

</details>

**#130–#140 · main**

> A primal summoned by the Ixal. Her sanctuary, the Howling Eye, is ringed by winds the battered Enterprise can't survive, and her barrier is wind-aspected aether. The Ascian Lahabrea taunts that she is stronger than any primal you have faced.

Sources shown: Eyes on Me — main scenario quest (2.0); Into the Eye of the Storm — main scenario quest (2.0); In Pursuit of the Past — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E130a** The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary. *Into the Eye of the Storm* (2.0, main): "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."
  - **E130b** Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier. *Into the Eye of the Storm* (2.0, main): "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"
  - **E129b** Lahabrea taunts that Garuda is stronger than any primal you have faced. *In Pursuit of the Past* (2.0, main): "And you are aware that her strength greatly exceeds that of your previous primal conquests?"

</details>

**#141 onward · main** · Also searchable as: the Lady of the Vortex

> A primal summoned by the Ixal. At the Howling Eye you struck her down, but her Ixali worshippers' belief raised her again; then Gaius's imperial weapon seemingly absorbed her, along with the gods her dying captives summoned.

Sources shown: Eyes on Me — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E141c** You strike Garuda down, but her Ixali worshippers' belief raises her again. *Lady of the Vortex* (2.0, main): "only to see her rise once more, reinvigorated by the belief of her [[Ixal]]i disciples."
  - **E141d** Garuda's dying kobold and Amalj'aa captives cry out and summon their own gods. *Lady of the Vortex* (2.0, main): "slaughtering her captive [[kobold]]s and [[Amalj'aa]], whose cries of agony serve to summon their own patron deities."
  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."

</details>

### Francel (`char-francel`, character)

**#115 only · main**

> A lord of House Haillenarte. A draconian rosary has turned up in a chest belonging to him.

Sources shown: Three for Three — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E115a** A draconian rosary turns up in a chest belonging to Lord Francel of House Haillenarte. *Three for Three* (2.0, main): "a draconian rosary in a chest belonging to Lord [[Francel]] of [[House Haillenarte]]."

</details>

**#116–#117 · main**

> A lord of House Haillenarte. A draconian rosary turned up among his belongings, and he fears many will take it as proof of heresy, though his former servant swears he is no heretic. He sent you with a letter to Lord Haurchefant.

Sources shown: Three for Three — main scenario quest (2.0); The Rose and the Unicorn — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E115a** A draconian rosary turns up in a chest belonging to Lord Francel of House Haillenarte. *Three for Three* (2.0, main): "a draconian rosary in a chest belonging to Lord [[Francel]] of [[House Haillenarte]]."
  - **E116b** Francel fears the rosary will still be taken as proof against him. *The Rose and the Unicorn* (2.0, main): "Although the draconian rosary was not found in my possession, it will still be considered by many to be proof of my"
  - **E116a** Francel's former servant swears he is no heretic. *The Rose and the Unicorn* (2.0, main): "Lord Francel is no heretic. He is a goodly, righteous man, wholly dedicated to the cause."
  - **E116d** Francel gives you a letter of introduction to House Fortemps. *The Rose and the Unicorn* (2.0, main): "he furnishes you with a [[Letter to Haurchefant|letter of introduction]] to [[House Fortemps]]"

</details>

**#118–#119 · main**

> A lord of House Haillenarte suspected of heresy over a draconian rosary found among his belongings. You saved him at the Steel Vigil, where he hoped to prove his devotion, and his trial approaches.

Sources shown: Three for Three — main scenario quest (2.0); Road to Redemption — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E115a** A draconian rosary turns up in a chest belonging to Lord Francel of House Haillenarte. *Three for Three* (2.0, main): "a draconian rosary in a chest belonging to Lord [[Francel]] of [[House Haillenarte]]."
  - **E118a** Francel went to the Steel Vigil hoping to show his devotion by slaying scalekin. *Road to Redemption* (2.0, main): "I had hoped we might demonstrate our devotion by slaying a number of the scalekin."
  - **E118b** Francel's trial approaches. *Road to Redemption* (2.0, main): "The day of my trial approaches."

</details>

**#120 onward · main**

> A lord of House Haillenarte tried for heresy over a draconian rosary found among his belongings. At Witchdrop, Inquisitor Guillaime ordered him to prove his innocence by leaping from the cliff. You protected him, and the charges were withdrawn pending investigation.

Sources shown: Three for Three — main scenario quest (2.0); In the Eyes of Gods and Men — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E115a** A draconian rosary turns up in a chest belonging to Lord Francel of House Haillenarte. *Three for Three* (2.0, main): "a draconian rosary in a chest belonging to Lord [[Francel]] of [[House Haillenarte]]."
  - **E120a** Inquisitor Guillaime presides over Francel's trial at Witchdrop. *In the Eyes of Gods and Men* (2.0, main): "Inquisitor Guillaime presides over Lord Francel's trial at Witchdrop even as we speak."
  - **E120b** Guillaime orders Francel to prove his innocence by leaping from the cliff. *In the Eyes of Gods and Men* (2.0, main): "Leap from the cliff and entrust your fate to the Fury."
  - **E120d** Guillaime withdraws the charges against Francel, pending investigation. *In the Eyes of Gods and Men* (2.0, main): "I shall withdraw my charges against Lord Francel, pending further investigation."

</details>

### Haurchefant (`char-haurchefant`, character)

**#116–#117 · main**

> A lord of House Fortemps who commands the garrison at Camp Dragonhead. Lord Francel sent you to him, and he has promised to make inquiries for you.

Sources shown: The Rose and the Unicorn — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E116c** Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead. *The Rose and the Unicorn* (2.0, main): "Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead."
  - **E116d** Francel gives you a letter of introduction to House Fortemps. *The Rose and the Unicorn* (2.0, main): "he furnishes you with a [[Letter to Haurchefant|letter of introduction]] to [[House Fortemps]]"
  - **E116e** Haurchefant promises to make inquiries for you. *The Rose and the Unicorn* (2.0, main): "Nevertheless, I will make inquiries on your behalf and share with you my findings in the future."

</details>

**#118–#119 · main**

> A lord of House Fortemps who commands the garrison at Camp Dragonhead. He has found a witness to the Enterprise's flight, but first means to clear Lord Francel's name, and yours with it.

Sources shown: The Rose and the Unicorn — main scenario quest (2.0); Road to Redemption — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E116c** Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead. *The Rose and the Unicorn* (2.0, main): "Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead."
  - **E118c** A witness to the Enterprise's flight has been found, but is reluctant to meet you. *Road to Redemption* (2.0, main): "the witness became understandably reticent to make your acquaintance"
  - **E118d** Francel's name, and so yours, must be cleared first. *Road to Redemption* (2.0, main): "we must first clear Lord Francel's name─and, by association, yours."

</details>

**#120 only · main**

> A lord of House Fortemps who commands the garrison at Camp Dragonhead. He believes the rosaries against Lord Francel were planted, and at the trial argued that someone was using the trials to set the houses against each other.

Sources shown: The Rose and the Unicorn — main scenario quest (2.0); Following the Evidence — main scenario quest (2.0); In the Eyes of Gods and Men — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E116c** Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead. *The Rose and the Unicorn* (2.0, main): "Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead."
  - **E119a** Haurchefant believes the rosary was planted. *Following the Evidence* (2.0, main): "If the rosary was not his, then someone else with access ''must'' have planted it."
  - **E120e** Haurchefant says someone has used the trials to sow discord between the houses. *In the Eyes of Gods and Men* (2.0, main): "They have used you and your fellows to sow discord, Inquisitor─to set brother against brother"

</details>

**#121 onward · main**

> A lord of House Fortemps who commands the garrison at Camp Dragonhead. He defended Lord Francel at his heresy trial, and wrote to Lord Drillemont of Whitebrim Front asking that you be let into the Stone Vigil.

Sources shown: The Rose and the Unicorn — main scenario quest (2.0); In the Eyes of Gods and Men — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E116c** Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead. *The Rose and the Unicorn* (2.0, main): "Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead."
  - **E120e** Haurchefant says someone has used the trials to sow discord between the houses. *In the Eyes of Gods and Men* (2.0, main): "They have used you and your fellows to sow discord, Inquisitor─to set brother against brother"
  - **E121c** Haurchefant writes to Lord Drillemont of Whitebrim Front to ask that you be let in. *The Final Flight of the Enterprise* (2.0, main): "I will write a letter to Lord Drillemont of Whitebrim Front and request that he grant you permission to enter."

</details>

### Guillaime (`char-guillaime`, character)

**#113–#116 · main** · Also searchable as: Inquisitor Guillaime

> An Ishgardian inquisitor who subtly warned you to stay out of Ishgard's affairs.

Sources shown: The Unending War — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E113c** Inquisitor Guillaime subtly warns you away from Ishgard's affairs. *The Unending War* (2.0, main): "subtly cautioning you against becoming involved in Ishgardian affairs"

</details>

**#117–#119 · main** · Also searchable as: Inquisitor Guillaime

> An Ishgardian inquisitor who warned you to stay out of Ishgard's affairs. Since he arrived in Coerthas, countless heretics have been found, even among Ishgard's elite.

Sources shown: The Unending War — main scenario quest (2.0); The Talk of Coerthas — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E113c** Inquisitor Guillaime subtly warns you away from Ishgard's affairs. *The Unending War* (2.0, main): "subtly cautioning you against becoming involved in Ishgardian affairs"
  - **E117a** Since Inquisitor Guillaime arrived, countless heretics have been found, even among Ishgard's elite. *The Talk of Coerthas* (2.0, main): "Why, in the short time since Inquisitor Guillaime arrived in Coerthas, countless heretics have been discovered, even amongst the elite of Ishgardian society!"

</details>

**#120–#121 · main** · Also searchable as: Inquisitor Guillaime

> An Ishgardian inquisitor under whom countless heretics have been found. He tried Lord Francel at Witchdrop and ordered him to leap from the cliff to prove his innocence, then withdrew the charges pending investigation.

Sources shown: The Talk of Coerthas — main scenario quest (2.0); In the Eyes of Gods and Men — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E117a** Since Inquisitor Guillaime arrived, countless heretics have been found, even among Ishgard's elite. *The Talk of Coerthas* (2.0, main): "Why, in the short time since Inquisitor Guillaime arrived in Coerthas, countless heretics have been discovered, even amongst the elite of Ishgardian society!"
  - **E120a** Inquisitor Guillaime presides over Francel's trial at Witchdrop. *In the Eyes of Gods and Men* (2.0, main): "Inquisitor Guillaime presides over Lord Francel's trial at Witchdrop even as we speak."
  - **E120b** Guillaime orders Francel to prove his innocence by leaping from the cliff. *In the Eyes of Gods and Men* (2.0, main): "Leap from the cliff and entrust your fate to the Fury."
  - **E120d** Guillaime withdraws the charges against Francel, pending investigation. *In the Eyes of Gods and Men* (2.0, main): "I shall withdraw my charges against Lord Francel, pending further investigation."

</details>

**#122–#123 · main** · Also searchable as: Inquisitor Guillaime

> An Ishgardian inquisitor under whom countless heretics have been found. At Whitebrim Front he branded you untrustworthy and the Scions a defunct band the Empire had exterminated, and insists you must not reach the Stone Vigil.

Sources shown: The Talk of Coerthas — main scenario quest (2.0); Ye of Little Faith — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E117a** Since Inquisitor Guillaime arrived, countless heretics have been found, even among Ishgard's elite. *The Talk of Coerthas* (2.0, main): "Why, in the short time since Inquisitor Guillaime arrived in Coerthas, countless heretics have been discovered, even amongst the elite of Ishgardian society!"
  - **E122c** Guillaime calls Cid presumed dead and the Scions a defunct band the Empire exterminated. *Ye of Little Faith* (2.0, main): "missing and presumed dead since before the Calamity, and two Scions of the Seventh Dawn─a defunct band of misfits recently exterminated by the Empire."
  - **E122d** Guillaime insists you must not be let through to the Stone Vigil. *Ye of Little Faith* (2.0, main): "I know not why these three seek the Stone Vigil, but I know that we cannot permit them to pass."

</details>

**#124–#125 · main** · Also searchable as: Inquisitor Guillaime

> An Ishgardian inquisitor under whom countless heretics have been found. He insists you must not reach the Stone Vigil, warned the chirurgeons that your gifts serve an unknown end, and seems to hate you and your companions.

Sources shown: The Talk of Coerthas — main scenario quest (2.0); Ye of Little Faith — main scenario quest (2.0); The Best Inventions — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E117a** Since Inquisitor Guillaime arrived, countless heretics have been found, even among Ishgard's elite. *The Talk of Coerthas* (2.0, main): "Why, in the short time since Inquisitor Guillaime arrived in Coerthas, countless heretics have been discovered, even amongst the elite of Ishgardian society!"
  - **E122d** Guillaime insists you must not be let through to the Stone Vigil. *Ye of Little Faith* (2.0, main): "I know not why these three seek the Stone Vigil, but I know that we cannot permit them to pass."
  - **E124c** Guillaime warns that your efforts serve an unknown end. *The Best Inventions* (2.0, main): "Their earnest efforts are but a means to an as-yet-unknown end."
  - **E124d** The inquisitor seems to hate you and your companions. *The Best Inventions* (2.0, main): "The inquisitor appears to have developed a hatred for you and your associates"

</details>

**#126 only · main** · Also searchable as: Guillaime, Inquisitor Guillaime

> An impostor posing as Inquisitor Guillaime. The real inquisitor was murdered on the day he arrived in Coerthas. The impostor has worked to keep you from the Stone Vigil, and his true identity and motives are unknown.

Sources shown: By the Lights of Ishgard — main scenario quest (2.0); Ye of Little Faith — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E126b** The real inquisitor was murdered on the day he arrived in Coerthas. *By the Lights of Ishgard* (2.0, main): "Newly come to Coerthas and murdered on the day of his arrival..."
  - **E126c** The corpse is the real Inquisitor Guillaime. *By the Lights of Ishgard* (2.0, main): "I believe you have just made the acquaintance of the ''real'' Inquisitor Guillaime."
  - **E126d** The impostor's identity and reasons for opposing you are unknown. *By the Lights of Ishgard* (2.0, main): "we have yet to discern his true identity, or why he has decided to oppose us."
  - **E122d** Guillaime insists you must not be let through to the Stone Vigil. *Ye of Little Faith* (2.0, main): "I know not why these three seek the Stone Vigil, but I know that we cannot permit them to pass."

</details>

**#127 only · main** · Also searchable as: Guillaime, Inquisitor Guillaime

> An impostor posing as Inquisitor Guillaime, whose namesake was murdered on arriving in Coerthas. He coerced Prunilla with threats against her loved ones, and condemned innocent people for carrying draconian rosaries. His true identity is unknown.

Sources shown: By the Lights of Ishgard — main scenario quest (2.0); Blood for Blood — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E126b** The real inquisitor was murdered on the day he arrived in Coerthas. *By the Lights of Ishgard* (2.0, main): "Newly come to Coerthas and murdered on the day of his arrival..."
  - **E126c** The corpse is the real Inquisitor Guillaime. *By the Lights of Ishgard* (2.0, main): "I believe you have just made the acquaintance of the ''real'' Inquisitor Guillaime."
  - **E127a** The impostor coerced Prunilla with threats against her loved ones. *Blood for Blood* (2.0, main): "if I defied him...everyone I loved would suffer unimaginable horrors before they died."
  - **E127b** The impostor condemned innocent people found carrying draconian rosaries. *Blood for Blood* (2.0, main): "countless men and women of good moral standing, seized whilst in possession of draconian rosaries."
  - **E126d** The impostor's identity and reasons for opposing you are unknown. *By the Lights of Ishgard* (2.0, main): "we have yet to discern his true identity, or why he has decided to oppose us."

</details>

**#128 onward · main** · Also searchable as: Guillaime, Inquisitor Guillaime

> An impostor who posed as Inquisitor Guillaime after the real inquisitor was murdered. Unmasked at Snowcloak, he called all Ishgard complicit in the archbishop's lies, summoned his Dravanian allies and took the form of a dragon, and you defeated him.

Sources shown: By the Lights of Ishgard — main scenario quest (2.0); The Heretic among Us — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E126c** The corpse is the real Inquisitor Guillaime. *By the Lights of Ishgard* (2.0, main): "I believe you have just made the acquaintance of the ''real'' Inquisitor Guillaime."
  - **E128a** Drillemont names the impostor a heretic and the murderer of Inquisitor Guillaime. *The Heretic among Us* (2.0, main): "I name thee ''heretic'', murderer of Inquisitor Guillaime and countless innocents!"
  - **E128b** The impostor calls all Ishgard complicit in the archbishop's lies. *The Heretic among Us* (2.0, main): "''All'' are complicit in these crimes, for ''all'' live their lives by the archbishop's lies."
  - **E128c** He summons his Dravanian allies and takes the form of a dragon. *The Heretic among Us* (2.0, main): "he summons his [[Dravanian Horde|Dravanian allies]] and endeavors to defend himself, going so far as to use his magicks to assume the form of a [[dragon]]."
  - **E128f** You defeat the false inquisitor. *The Heretic among Us* (2.0, main): "Alphinaud refuses to revel in your victory over the false inquisitor"

</details>

### Drillemont (`char-drillemont`, character)

**#121 only · main**

> Lord of Whitebrim Front, whose leave you need to enter the Stone Vigil. Lord Haurchefant has written to him on your behalf.

Sources shown: The Final Flight of the Enterprise — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E121c** Haurchefant writes to Lord Drillemont of Whitebrim Front to ask that you be let in. *The Final Flight of the Enterprise* (2.0, main): "I will write a letter to Lord Drillemont of Whitebrim Front and request that he grant you permission to enter."

</details>

**#122–#126 · main**

> Lord of Whitebrim Front. He was astonished to find Cid alive, but bars you from the Stone Vigil until it is retaken and you declare your true intentions.

Sources shown: The Final Flight of the Enterprise — main scenario quest (2.0); Ye of Little Faith — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E121c** Haurchefant writes to Lord Drillemont of Whitebrim Front to ask that you be let in. *The Final Flight of the Enterprise* (2.0, main): "I will write a letter to Lord Drillemont of Whitebrim Front and request that he grant you permission to enter."
  - **E122b** Drillemont is astonished that Cid is alive. *Ye of Little Faith* (2.0, main): "you're ''alive''!? But that's impossible!"
  - **E122e** Drillemont bars you until the outpost is retaken and you declare your true intentions. *Ye of Little Faith* (2.0, main): "You three will not enter the outpost until we have reclaimed it─and until you declare your ''true'' intentions as well."

</details>

**#127 only · main**

> Lord of Whitebrim Front. Convinced that the inquisitor who opposed you is a heretic, he will let you into the Stone Vigil once the impostor is brought to justice.

Sources shown: Ye of Little Faith — main scenario quest (2.0); Blood for Blood — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E122b** Drillemont is astonished that Cid is alive. *Ye of Little Faith* (2.0, main): "you're ''alive''!? But that's impossible!"
  - **E127d** Drillemont is convinced the inquisitor is a heretic. *Blood for Blood* (2.0, main): "Fury take me, the inquisitor is a ''heretic''!?"
  - **E127e** Drillemont will let you into the outpost, but first asks your help. *Blood for Blood* (2.0, main): "I will permit you to enter the outpost─but first, I must needs beg your assistance."

</details>

**#128 onward · main**

> Lord of Whitebrim Front. He confronted the false inquisitor at Snowcloak, naming him the murderer of Inquisitor Guillaime, and opened the way to the Stone Vigil and your airship.

Sources shown: Blood for Blood — main scenario quest (2.0); The Heretic among Us — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E127e** Drillemont will let you into the outpost, but first asks your help. *Blood for Blood* (2.0, main): "I will permit you to enter the outpost─but first, I must needs beg your assistance."
  - **E128a** Drillemont names the impostor a heretic and the murderer of Inquisitor Guillaime. *The Heretic among Us* (2.0, main): "I name thee ''heretic'', murderer of Inquisitor Guillaime and countless innocents!"
  - **E128e** Drillemont says it is time you were reunited with your airship. *The Heretic among Us* (2.0, main): "It is past time that you were reunited with your airship."

</details>

### Biggs (`char-biggs`, character)

**#143–#144 · main**

> One of two men, likely Biggs and Wedge, who escaped from a downed imperial airship in Coerthas and are being hunted.

Sources shown: Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E143c** Two men, likely Biggs and Wedge, escaped a downed imperial airship. *Casing the Castrum* (2.0, main): "two men─likely [[Biggs]] and [[Wedge]]─escaped from a downed imperial airship not long ago."

</details>

**#145–#146 · main**

> One of two escapees from a downed imperial airship in Coerthas. He drew the pursuers away from Wedge and was last seen heading west. Cid says he has always looked after Wedge.

Sources shown: Casing the Castrum — main scenario quest (2.0); Footprints in the Snow — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E143c** Two men, likely Biggs and Wedge, escaped a downed imperial airship. *Casing the Castrum* (2.0, main): "two men─likely [[Biggs]] and [[Wedge]]─escaped from a downed imperial airship not long ago."
  - **E145a** Wedge says Biggs went another way to lure their pursuers off. *Footprints in the Snow* (2.0, main): "He went off in a different direction to lure our pursuers away."
  - **E145b** Biggs headed west. *Footprints in the Snow* (2.0, main): "At any rate, we know for a fact that Biggs headed west."
  - **E145d** Cid says Biggs has always taken care of Wedge. *Footprints in the Snow* (2.0, main): "For all the tongue-lashings he gives Wedge, he's always taken care of him."

</details>

**#147–#151 · main**

> A member of Cid's Ironworks crew. The imperials took him and Wedge from the Waking Sands to Castrum Centri, and they escaped by sabotaging an airship. Yda and Y'shtola helped you rescue him from imperial troops.

Sources shown: Notorious Biggs — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E147e** Cid and his two core Ironworks members are together again. *Notorious Biggs* (2.0, main): "the three core members of [[Garlond Ironworks]] are together again"
  - **E147c** Biggs and Wedge were held at Castrum Centri apart from Minfilia and the others. *Notorious Biggs* (2.0, main): "we found ourselves in the midst of an imperial stronghold─Castrum Centri. … Biggs and I were thrown into a detainment cell together, while Minfilia and the others were taken elsewhere."
  - **E147d** They escaped by sabotaging an airship's altitude control. *Notorious Biggs* (2.0, main): "we sabotaged the ship's altitude control and thereby forced an emergency landing."
  - **E147a** With Yda and Y'shtola you rescue Biggs from imperial troops. *Notorious Biggs* (2.0, main): "With the aid of [[Yda]] and [[Y'shtola]], you succeed in rescuing Biggs from a detachment of imperial troops."

</details>

**#153 onward · main**

> A member of Cid's Ironworks crew who escaped from Castrum Centri. He is to go back in with Wedge and you, disguised as imperial soldiers, and he and Wedge repaired the magitek reaper you seized.

Sources shown: Notorious Biggs — main scenario quest (2.0); Dressed for Conquest — main scenario quest (2.0); Fool Me Twice — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E147e** Cid and his two core Ironworks members are together again. *Notorious Biggs* (2.0, main): "the three core members of [[Garlond Ironworks]] are together again"
  - **E147c** Biggs and Wedge were held at Castrum Centri apart from Minfilia and the others. *Notorious Biggs* (2.0, main): "we found ourselves in the midst of an imperial stronghold─Castrum Centri. … Biggs and I were thrown into a detainment cell together, while Minfilia and the others were taken elsewhere."
  - **E151a** Three sets of imperial gear are needed: for Biggs, Wedge and you. *Dressed for Conquest* (2.0, main): "three sets of gear, one for each member of the infiltration team─Biggs, Wedge, and yourself."
  - **E153c** Biggs and Wedge repair the reaper at Cid's workshop. *Fool Me Twice* (2.0, main): "have already set about repairing the magitek reaper."

</details>

### Wedge (`char-wedge`, character)

**#143–#144 · main**

> One of two men, likely Biggs and Wedge, who escaped from a downed imperial airship in Coerthas and are being hunted.

Sources shown: Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E143c** Two men, likely Biggs and Wedge, escaped a downed imperial airship. *Casing the Castrum* (2.0, main): "two men─likely [[Biggs]] and [[Wedge]]─escaped from a downed imperial airship not long ago."

</details>

**#145–#146 · main**

> One of two escapees from a downed imperial airship in Coerthas. You found him hiding under a bridge after Biggs drew off their pursuers, and he was overjoyed to find Cid alive.

Sources shown: Casing the Castrum — main scenario quest (2.0); Footprints in the Snow — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E143c** Two men, likely Biggs and Wedge, escaped a downed imperial airship. *Casing the Castrum* (2.0, main): "two men─likely [[Biggs]] and [[Wedge]]─escaped from a downed imperial airship not long ago."
  - **E145a** Wedge says Biggs went another way to lure their pursuers off. *Footprints in the Snow* (2.0, main): "He went off in a different direction to lure our pursuers away."
  - **E145c** Wedge recognizes Cid, alive after five years. *Footprints in the Snow* (2.0, main): "Dare I hope...? Was that...Master"

</details>

**#147–#151 · main**

> A member of Cid's Ironworks crew. The imperials took him and Biggs from the Waking Sands to Castrum Centri, and they escaped by sabotaging an airship.

Sources shown: Notorious Biggs — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E147e** Cid and his two core Ironworks members are together again. *Notorious Biggs* (2.0, main): "the three core members of [[Garlond Ironworks]] are together again"
  - **E147c** Biggs and Wedge were held at Castrum Centri apart from Minfilia and the others. *Notorious Biggs* (2.0, main): "we found ourselves in the midst of an imperial stronghold─Castrum Centri. … Biggs and I were thrown into a detainment cell together, while Minfilia and the others were taken elsewhere."
  - **E147d** They escaped by sabotaging an airship's altitude control. *Notorious Biggs* (2.0, main): "we sabotaged the ship's altitude control and thereby forced an emergency landing."

</details>

**#153 onward · main**

> A member of Cid's Ironworks crew who escaped from Castrum Centri. He is to go back in with Biggs and you, disguised as imperial soldiers, and he and Biggs repaired the magitek reaper you seized.

Sources shown: Notorious Biggs — main scenario quest (2.0); Dressed for Conquest — main scenario quest (2.0); Fool Me Twice — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E147e** Cid and his two core Ironworks members are together again. *Notorious Biggs* (2.0, main): "the three core members of [[Garlond Ironworks]] are together again"
  - **E147c** Biggs and Wedge were held at Castrum Centri apart from Minfilia and the others. *Notorious Biggs* (2.0, main): "we found ourselves in the midst of an imperial stronghold─Castrum Centri. … Biggs and I were thrown into a detainment cell together, while Minfilia and the others were taken elsewhere."
  - **E151a** Three sets of imperial gear are needed: for Biggs, Wedge and you. *Dressed for Conquest* (2.0, main): "three sets of gear, one for each member of the infiltration team─Biggs, Wedge, and yourself."
  - **E153c** Biggs and Wedge repair the reaper at Cid's workshop. *Fool Me Twice* (2.0, main): "have already set about repairing the magitek reaper."

</details>

### Glaumunt (`char-glaumunt`, character)

**#148 only · main**

> A man at Revenant's Toll with a personal grudge against the Empire, who knows a great deal about Castrum Centri. He has agreed to help you get inside.

Sources shown: Come-Into-My-Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E148c** Glaumunt has a grudge against the Empire and knows Castrum Centri. *Come-Into-My-Castrum* (2.0, main): "The fellow's got a personal grudge against the Empire, and happens to know a deal about Castrum Centri besides."
  - **E148e** Glaumunt will help you. *Come-Into-My-Castrum* (2.0, main): "If his response is any indication, it would seem you can indeed expect his aid."

</details>

**#149–#151 · main**

> A man at Revenant's Toll with a grudge against the Empire, who knows a great deal about Castrum Centri. He showed you a drainage pipe for listening in on the castrum, and is seeking a suit of magitek armor for the infiltration.

Sources shown: Come-Into-My-Castrum — main scenario quest (2.0); Getting Even with Garlemald — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E148c** Glaumunt has a grudge against the Empire and knows Castrum Centri. *Come-Into-My-Castrum* (2.0, main): "The fellow's got a personal grudge against the Empire, and happens to know a deal about Castrum Centri besides."
  - **E149e** Glaumunt shows you a drainage pipe from the command tower for listening in. *Getting Even with Garlemald* (2.0, main): "He tells you of a drainage pipe that leads from the stronghold's command tower"
  - **E149d** Glaumunt is seeking a suit of magitek armor. *Getting Even with Garlemald* (2.0, main): "Glaumunt is looking into ways to procure a suit of magitek armor."

</details>

**#153 onward · main**

> A man at Revenant's Toll with a grudge against the Empire, who knows a great deal about Castrum Centri. He planned your disguise, and fed the imperials false word of insurgents so you could seize a magitek reaper.

Sources shown: Come-Into-My-Castrum — main scenario quest (2.0); Acting the Part — main scenario quest (2.0); Fool Me Twice — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E148c** Glaumunt has a grudge against the Empire and knows Castrum Centri. *Come-Into-My-Castrum* (2.0, main): "The fellow's got a personal grudge against the Empire, and happens to know a deal about Castrum Centri besides."
  - **E150c** Glaumunt's plan is to send you into Castrum Centri in imperial dress. *Acting the Part* (2.0, main): "The plan's to have you enter Castrum Centri all decked out in imperial duds"
  - **E153a** Glaumunt fed the imperials false intelligence to draw out a patrol. *Fool Me Twice* (2.0, main): "I took the liberty o' feedin' 'em a bit o' the old false intelligence"
  - **E153b** You seize a magitek reaper, which needs repairs. *Fool Me Twice* (2.0, main): "You have succeeded in acquiring a magitek reaper, though some repairs will be required before it can be put to use."

</details>

### The Company of Heroes (`org-company-of-heroes`, organization)

**#103–#104 · main**

> A disbanded company whose five chosen members judged you worthy to challenge Titan, weighing you by deeds rather than reputation.

Sources shown: In the Company of Heroes — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E103f** The five were chosen by their comrades before the Company of Heroes disbanded. *In the Company of Heroes* (2.0, main): "We five were chosen by our brothers and sisters, and before the Company of Heroes disbanded"
  - **E103b** Five members of the Company of Heroes judge you a worthy challenger. *In the Company of Heroes* (2.0, main): "We five of the Company of Heroes hereby judge you a worthy challenger."
  - **E103c** The Company weighs anyone who would follow in its footsteps by deeds, not reputation. *In the Company of Heroes* (2.0, main): "That any who would follow in our footsteps must be weighed and measured─not by their reputation, but by their deeds."

</details>

**#105 onward · main**

> A disbanded company whose five chosen members judged you worthy to challenge Titan. Riol, another former member, revealed that the Company once reached Titan through a beastman aetheryte.

Sources shown: In the Company of Heroes — main scenario quest (2.0); As You Wish — main scenario quest (2.0); Lord of Crags — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E103f** The five were chosen by their comrades before the Company of Heroes disbanded. *In the Company of Heroes* (2.0, main): "We five were chosen by our brothers and sisters, and before the Company of Heroes disbanded"
  - **E103b** Five members of the Company of Heroes judge you a worthy challenger. *In the Company of Heroes* (2.0, main): "We five of the Company of Heroes hereby judge you a worthy challenger."
  - **E104a** Wheiskaet sends you to Bronze Lake to meet Riol, another former member of the Company. *As You Wish* (2.0, main): "There you will meet with Riol, another man who once served with the Company."
  - **E105a** The Company of Heroes reached Titan through a beastman aetheryte, not the kobold mines. *Lord of Crags* (2.0, main): "Riol reveals that the [[Company of Heroes]] reached [[Titan]] not by fighting their way through the mines of [[O'Ghomoro]], but by using a beastman [[aetheryte]]."

</details>

### The Garlean Empire (`org-garlean-empire`, organization)

**#102–#104 · main** · Also searchable as: the Empire

> An empire that conquers other lands, and has tried to conquer Eorzea.

Sources shown: That Weight — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E100a** The Empire conquered the lands of the deserter Drest, as it tried to conquer Eorzea. *That Weight* (2.0, main): "They conquered my lands just like they tried to conquer yours!"

</details>

**#105 only · main** · Also searchable as: the Empire

> An empire that conquers other lands, and has tried to conquer Eorzea. After Titan fell, its officers appeared at the Navel with a figure called Lahabrea, and Y'shtola is troubled that the Ascians would consort with the Empire.

Sources shown: That Weight — main scenario quest (2.0); Lord of Crags — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E100a** The Empire conquered the lands of the deserter Drest, as it tried to conquer Eorzea. *That Weight* (2.0, main): "They conquered my lands just like they tried to conquer yours!"
  - **E105d** Rhitahtyn, an imperial officer at the Navel, refuses to endorse his comrade's plan. *Lord of Crags* (2.0, main): "I cannot endorse this course of action."
  - **K14** The Ascians are elusive, and Y'shtola is troubled that they would consort with the Empire. *Lord of Crags* (2.0, main): "Well, the Ascians are nothing if not elusive. … But that they would choose to consort with the ''Empire''..."

</details>

**#106–#140 · main** · Also searchable as: the Empire

> An empire that conquers other lands, and has tried to conquer Eorzea. Its forces, led by Livia, raided the Waking Sands, slaughtered many Scions and took prisoners, Minfilia among them.

Sources shown: That Weight — main scenario quest (2.0); All Good Things — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E100a** The Empire conquered the lands of the deserter Drest, as it tried to conquer Eorzea. *That Weight* (2.0, main): "They conquered my lands just like they tried to conquer yours!"
  - **E106b** Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners. *All Good Things* (2.0, main): "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."

</details>

**#141 onward · main** · Also searchable as: the Empire

> An empire that has tried to conquer Eorzea. Its forces under Livia raided the Waking Sands and took the Scions' leader prisoner, and at the Howling Eye Gaius, the Black Wolf, called forth a weapon that seemingly absorbed three primals.

Sources shown: That Weight — main scenario quest (2.0); All Good Things — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E100a** The Empire conquered the lands of the deserter Drest, as it tried to conquer Eorzea. *That Weight* (2.0, main): "They conquered my lands just like they tried to conquer yours!"
  - **K01** Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner. *All Good Things* (2.0, main): "Conditions of surrender...denied. … We leave! Bring the prisoners."
  - **K10** Gaius, the Black Wolf, is legatus of the XIVth Imperial Legion and commands the Garlean invasion of Eorzea. *Lady of the Vortex* (2.0, main): "legatus of the XIVth Imperial Legion, and supreme commander of the Garlean invasion force in Eorzea. … Of course, the Black Wolf─how could I not realize?"
  - **K11** The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals. *Lady of the Vortex* (2.0, main): "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."

</details>

### House Haillenarte (`org-house-haillenarte`, organization)

**#115–#116 · main**

> One of Ishgard's High Houses, whispered to be full of heretics. A draconian rosary turned up in a chest belonging to its Lord Francel.

Sources shown: Three for Three — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E115a** A draconian rosary turns up in a chest belonging to Lord Francel of House Haillenarte. *Three for Three* (2.0, main): "a draconian rosary in a chest belonging to Lord [[Francel]] of [[House Haillenarte]]."
  - **E115b** House Haillenarte is whispered to be full of heretics. *Three for Three* (2.0, main): "House Haillenarte is whispered to be infested with heretics..."

</details>

**#117–#118 · main**

> One of Ishgard's High Houses, whispered to be full of heretics. Accusations of heresy against its Lord Francel have thrown the house into chaos.

Sources shown: Three for Three — main scenario quest (2.0); The Talk of Coerthas — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E115a** A draconian rosary turns up in a chest belonging to Lord Francel of House Haillenarte. *Three for Three* (2.0, main): "a draconian rosary in a chest belonging to Lord [[Francel]] of [[House Haillenarte]]."
  - **E115b** House Haillenarte is whispered to be full of heretics. *Three for Three* (2.0, main): "House Haillenarte is whispered to be infested with heretics..."
  - **E117b** The heresy accusations have thrown House Haillenarte into chaos. *The Talk of Coerthas* (2.0, main): "But these accusations of heresy have thrown House Haillenarte into chaos."

</details>

**#119–#120 · main**

> One of Ishgard's High Houses, accused of harboring heretics. Draconian rosaries planted in shipments to Skyfire Locks look like a crude attempt to smear the house.

Sources shown: Three for Three — main scenario quest (2.0); Following the Evidence — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E115b** House Haillenarte is whispered to be full of heretics. *Three for Three* (2.0, main): "House Haillenarte is whispered to be infested with heretics..."
  - **E119b** Two parcels bound for Skyfire Locks each held a draconian rosary. *Following the Evidence* (2.0, main): "the two parcels bound for [[Skyfire Locks]] both contained a draconian rosary!"
  - **E119c** Haurchefant calls it a crass attempt to sully House Haillenarte. *Following the Evidence* (2.0, main): "Even the inquisitors must acknowledge that this is no more than a crass attempt to sully House Haillenarte's reputation."

</details>

**#121–#126 · main**

> One of Ishgard's High Houses, accused of harboring heretics. Its Lord Francel was cleared of heresy at his trial, but those who tried to destroy the house are still unknown.

Sources shown: Three for Three — main scenario quest (2.0); In the Eyes of Gods and Men — main scenario quest (2.0); The Final Flight of the Enterprise — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E115b** House Haillenarte is whispered to be full of heretics. *Three for Three* (2.0, main): "House Haillenarte is whispered to be infested with heretics..."
  - **E120d** Guillaime withdraws the charges against Francel, pending investigation. *In the Eyes of Gods and Men* (2.0, main): "I shall withdraw my charges against Lord Francel, pending further investigation."
  - **E121d** Those who tried to destroy House Haillenarte are still unmasked. *The Final Flight of the Enterprise* (2.0, main): "the cravens who attempted to destroy House Haillenarte have yet to be unmasked"

</details>

**#127 onward · main**

> One of Ishgard's High Houses, accused of harboring heretics. Its Lord Francel was cleared of heresy at his trial, and Prunilla has confessed that she planted rosaries from the false inquisitor's chest in shipments to Skyfire Locks.

Sources shown: Three for Three — main scenario quest (2.0); In the Eyes of Gods and Men — main scenario quest (2.0); Blood for Blood — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E115b** House Haillenarte is whispered to be full of heretics. *Three for Three* (2.0, main): "House Haillenarte is whispered to be infested with heretics..."
  - **E120d** Guillaime withdraws the charges against Francel, pending investigation. *In the Eyes of Gods and Men* (2.0, main): "I shall withdraw my charges against Lord Francel, pending further investigation."
  - **E127c** Prunilla planted rosaries from his chest in shipments bound for Skyfire Locks. *Blood for Blood* (2.0, main): "I took several from his chest and planted them in shipments bound for Skyfire Locks."

</details>

### The Ixal (`org-ixal`, organization)

**#110–#140 · main**

> A beast tribe that has summoned the primal Garuda.

Sources shown: Eyes on Me — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."

</details>

**#141 onward · main**

> A beast tribe that summoned the primal Garuda. When you struck her down at the Howling Eye, their belief raised her again.

Sources shown: Eyes on Me — main scenario quest (2.0); Lady of the Vortex — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E110e** The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. *Eyes on Me* (2.0, main): "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."
  - **E141c** You strike Garuda down, but her Ixali worshippers' belief raises her again. *Lady of the Vortex* (2.0, main): "only to see her rise once more, reinvigorated by the belief of her [[Ixal]]i disciples."

</details>

### Castrum Centri (`loc-castrum-centri`, location)

**#142 only · main**

> An imperial stronghold in Mor Dhona, where the Scions captured in the raid on the Waking Sands are held.

Sources shown: Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."

</details>

**#143–#147 · main**

> An imperial stronghold in Mor Dhona. Scouts saw four prisoners matching Minfilia, Urianger, Papalymo and Tataru led inside.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."

</details>

**#148–#154 · main**

> An imperial stronghold in Mor Dhona, where Minfilia, Urianger, Papalymo and Tataru are held. It is on such high alert that you must go in disguised as imperial troops.

Sources shown: Reclamation — main scenario quest (2.0); Casing the Castrum — main scenario quest (2.0); Come-Into-My-Castrum — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."
  - **E143b** Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri. *Casing the Castrum* (2.0, main): "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."
  - **E148b** Castrum Centri is on high alert. *Come-Into-My-Castrum* (2.0, main): "Not even a fly could get within a hundred yalms of the walls undetected."
  - **E148a** Cid means to march in disguised as imperial troops. *Come-Into-My-Castrum* (2.0, main): "Aye, we'll disguise ourselves as imperial troops and march right in."

</details>

**#155 onward · main**

> An imperial stronghold in Mor Dhona where the captured Scions were held, until a rescue freed them from its storage tower.

Sources shown: Reclamation — main scenario quest (2.0); Escape from Castrum Centri — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **E142d** The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona. *Reclamation* (2.0, main): "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."
  - **K20** The rescue party frees the captives held in Castrum Centri's storage tower. *Escape from Castrum Centri* (2.0, main): "and the others are being held within the storage tower. … Though the rescue mission was a success"

</details>

## Relationships

| ID | Edge | Visible | Scope | Claims |
|---|---|---|---|---|
| R01 | Minfilia → *leads* → The Scions of the Seventh Dawn | 2.0 onward | main | C01 |
| R02 | Thancred → *member of* → The Scions of the Seventh Dawn | 2.0 onward | main | C31 |
| R03 | Y'shtola → *member of* → The Scions of the Seventh Dawn | 2.0 onward | main | C31, C40 |
| R04 | Urianger → *member of* → The Scions of the Seventh Dawn | 2.0 onward | main | C31, C36 |
| R05 | Alphinaud → *member of* → The Scions of the Seventh Dawn | 2.0 onward | main | C25 |
| R06 | Tataru → *member of* → The Scions of the Seventh Dawn | 2.0 onward | main | C32, C36 |
| R07 | Alphinaud → *twin of* → Alisaie | 2.0 onward | main | C10 |
| R08 | The Scions of the Seventh Dawn → *headquartered at* → The Waking Sands | 2.0 only | main | C02 |
| R09 | The Crystal Braves → *controls* → The Rising Stones | 2.55 onward | main | C19, C19b |
| R10 | The Crystal Braves → *turned against* → The Scions of the Seventh Dawn | 2.55 onward | main | C19, C20 |
| R11 | Urianger → *conceals* → The Waking Sands | 2.55 onward | main | C21 |
| R12 | Alisaie → *grandchild of* → Louisoix | 2.0 onward | optional | C13 |
| R13 | Alphinaud → *grandchild of* → Louisoix | 2.55 onward | optional | C26, C13 |
| R14 | Alisaie → *member of* → The Scions of the Seventh Dawn | 2.0 onward | optional | C30 |
| R15 | Minfilia → *leads* → The Scions of the Seventh Dawn | #154–#160 | main | C01 |
| R16 | Thancred → *member of* → The Scions of the Seventh Dawn | #154–#160 | main | C31 |
| R17 | Alphinaud → *member of* → The Scions of the Seventh Dawn | #154–#160 | main | C25 |
| R18 | Minfilia → *prisoner of* → Livia | #154 only | main | K01, K03 · ends: K20 |
| R19 | Thancred → *possessed by* → Lahabrea | #155–#160 | main | C37 |
| R20 | Livia → *serves* → Gaius | #157–#159 | main | K45 · ends: K62 |
| R21 | The Eorzean Alliance → *part of* → Operation Archon | #157 onward | main | K40 |
| R22 | The Scions of the Seventh Dawn → *part of* → Operation Archon | #157 onward | main | K43 |
| R23 | Cid → *part of* → Operation Archon | #157 onward | main | K43 |
| P1 | Minfilia → *part of* → The Black Wolf's Challenge | #155 onward | main | K20 |
| P2 | Thancred → *part of* → The Black Wolf's Challenge | #155 onward | main | C37 |
| P3 | Alphinaud → *part of* → The Black Wolf's Challenge | #155 onward | main | K21 |
| P4 | The Scions of the Seventh Dawn → *part of* → The Black Wolf's Challenge | #155 onward | main | K20 |
| P5 | Cid → *part of* → The Black Wolf's Challenge | #155 onward | main | K21 |
| P6 | Gaius → *part of* → The Black Wolf's Challenge | #155 onward | main | K25 |
| P7 | Livia → *part of* → The Black Wolf's Challenge | #155 onward | main | K22 |
| P8 | Lahabrea → *part of* → The Black Wolf's Challenge | #155 onward | main | C37 |
| P9 | The Eorzean Alliance → *part of* → The Black Wolf's Challenge | #155 onward | main | K26 |
| P10 | Operation Archon → *part of* → The Black Wolf's Challenge | #157 onward | main | K40 |
| R24 | Minfilia → *leads* → The Scions of the Seventh Dawn | #102–#153 | main | C01 |
| R25 | Thancred → *member of* → The Scions of the Seventh Dawn | #102–#153 | main | C31 |
| R26 | Y'shtola → *member of* → The Scions of the Seventh Dawn | #102–#160 | main | C31, C40 |
| R27 | Urianger → *member of* → The Scions of the Seventh Dawn | #102–#160 | main | C31 |
| R28 | Tataru → *member of* → The Scions of the Seventh Dawn | #102–#160 | main | C32 |
| R29 | Alphinaud → *member of* → The Scions of the Seventh Dawn | #110–#153 | main | C25 |
| R30 | The Scions of the Seventh Dawn → *headquartered at* → The Waking Sands | #102–#160 | main | C02 |
| R31 | Minfilia → *prisoner of* → Livia | #106–#153 | main | K01, E106d |
| R32 | Yda → *member of* → The Scions of the Seventh Dawn | #102 onward | main | C31 |
| R33 | Papalymo → *member of* → The Scions of the Seventh Dawn | #102 onward | main | C31 |
| R34 | Lahabrea → *allied with* → The Garlean Empire | #105 onward | main | K14 |
| R35 | Livia → *member of* → The Garlean Empire | #106–#159 | main | K01, E106b · ends: K62 |
| R36 | Iliud → *aids* → The Scions of the Seventh Dawn | #106 onward | main | E106f |
| R37 | Marques → *revealed as* → Cid | #110 onward | main | E110c |
| R38 | Garuda → *summoned by* → The Ixal | #110 onward | main | E110e |
| R39 | Francel → *member of* → House Haillenarte | #115 onward | main | E115a |
| R40 | Haurchefant → *aids* → Francel | #118 onward | main | E118d |
| R41 | Guillaime → *opposes* → Alphinaud | #122–#127 | main | E122d, E122c · ends: E128f |
| R42 | Drillemont → *aids* → Alphinaud | #127 onward | main | E127e |
| R43 | Gaius → *member of* → The Garlean Empire | #141–#160 | main | K10 |
| R44 | Minfilia → *held at* → Castrum Centri | #142–#154 | main | E142d · ends: K20 |
| R45 | Urianger → *held at* → Castrum Centri | #143–#154 | main | E143b · ends: K20 |
| R46 | Papalymo → *held at* → Castrum Centri | #143–#154 | main | E143b · ends: K20 |
| R47 | Tataru → *held at* → Castrum Centri | #143–#154 | main | E143b · ends: K20 |
| R48 | Rhitahtyn → *serves* → Gaius | #143–#156 | main | E143e · ends: K42 |
| R49 | Biggs → *serves* → Cid | #147 onward | main | E147e |
| R50 | Wedge → *serves* → Cid | #147 onward | main | E147e |
| R51 | Glaumunt → *aids* → The Scions of the Seventh Dawn | #148 onward | main | E148c, E148e |
| P11 | Y'shtola → *part of* → The Road to Titan | #103 onward | main | E103d |
| P12 | The Company of Heroes → *part of* → The Road to Titan | #103 onward | main | E103b |
| P13 | Titan → *part of* → The Road to Titan | #103 onward | main | E103b |
| P14 | Rhitahtyn → *part of* → The Road to Titan | #105 onward | main | E105d |
| P15 | Lahabrea → *part of* → The Road to Titan | #105 onward | main | E105e |
| P16 | The Garlean Empire → *part of* → The Road to Titan | #105 onward | main | K14 |
| P17 | Minfilia → *part of* → The Fall of the Waking Sands | #106 onward | main | K01 |
| P18 | The Scions of the Seventh Dawn → *part of* → The Fall of the Waking Sands | #106 onward | main | E106b |
| P19 | The Waking Sands → *part of* → The Fall of the Waking Sands | #106 onward | main | E106b |
| P20 | Livia → *part of* → The Fall of the Waking Sands | #106 onward | main | K01 |
| P21 | The Garlean Empire → *part of* → The Fall of the Waking Sands | #106 onward | main | E106b |
| P22 | Noraxia → *part of* → The Fall of the Waking Sands | #106 onward | main | E106e |
| P23 | Iliud → *part of* → The Fall of the Waking Sands | #106 onward | main | E106f |
| P24 | Marques → *part of* → The Fall of the Waking Sands | #106 onward | main | E106g |
| P25 | Alphinaud → *part of* → The Fall of the Waking Sands | #110 onward | main | E110c |
| P26 | Cid → *part of* → The Fall of the Waking Sands | #110 onward | main | E110c |
| P27 | Alphinaud → *part of* → The Search for the Enterprise | #110 onward | main | E110c |
| P28 | Cid → *part of* → The Search for the Enterprise | #110 onward | main | E110d |
| P29 | Garuda → *part of* → The Search for the Enterprise | #110 onward | main | E110e |
| P30 | The Ixal → *part of* → The Search for the Enterprise | #110 onward | main | E110e |
| P31 | Guillaime → *part of* → The Search for the Enterprise | #113 onward | main | E113c |
| P32 | Francel → *part of* → The Search for the Enterprise | #115 onward | main | E115a |
| P33 | House Haillenarte → *part of* → The Search for the Enterprise | #115 onward | main | E115a |
| P34 | Haurchefant → *part of* → The Search for the Enterprise | #116 onward | main | E116e |
| P35 | Drillemont → *part of* → The Search for the Enterprise | #121 onward | main | E121c |
| P36 | Lahabrea → *part of* → The Search for the Enterprise | #129 onward | main | E129b |
| P37 | Cid → *part of* → Garuda's Barrier | #130 onward | main | E130b |
| P38 | Alphinaud → *part of* → Garuda's Barrier | #130 onward | main | E130e |
| P39 | Garuda → *part of* → Garuda's Barrier | #130 onward | main | E130a |
| P40 | The Ixal → *part of* → Garuda's Barrier | #141 onward | main | E141c |
| P41 | Titan → *part of* → Garuda's Barrier | #141 onward | main | E141d |
| P42 | Gaius → *part of* → Garuda's Barrier | #141 onward | main | K11 |
| P43 | The Garlean Empire → *part of* → Garuda's Barrier | #141 onward | main | E141e |
| P44 | The Scions of the Seventh Dawn → *part of* → Garuda's Barrier | #141 onward | main | E141f |
| P45 | Alphinaud → *part of* → The Road to Castrum Centri | #142 onward | main | E142a |
| P46 | Cid → *part of* → The Road to Castrum Centri | #142 onward | main | E142a |
| P47 | Yda → *part of* → The Road to Castrum Centri | #142 onward | main | E142b |
| P48 | Y'shtola → *part of* → The Road to Castrum Centri | #142 onward | main | E142d |
| P49 | Minfilia → *part of* → The Road to Castrum Centri | #142 onward | main | E142d |
| P50 | The Scions of the Seventh Dawn → *part of* → The Road to Castrum Centri | #142 onward | main | K16 |
| P51 | Castrum Centri → *part of* → The Road to Castrum Centri | #142 onward | main | E142d |
| P52 | Biggs → *part of* → The Road to Castrum Centri | #143 onward | main | E143c |
| P53 | Wedge → *part of* → The Road to Castrum Centri | #143 onward | main | E143c |
| P54 | Glaumunt → *part of* → The Road to Castrum Centri | #148 onward | main | E148c |

Evidence for each claim is listed under the entities above and in full in the [claims table](content-claims.md).
