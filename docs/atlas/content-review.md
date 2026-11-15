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

## Snapshot overview

Visible records at each step, in the main-story view and the main + optional view. Slice steps (#…) cover only the arc's cast.

| Step | Entities (main) | Entities (+ optional) | Relationships (main) | Relationships (+ optional) |
|---|---|---|---|---|
| #154 After Every Little Thing She Does Is Magitek | 8 | 8 | 4 | 4 |
| #155 After Escape from Castrum Centri | 10 | 10 | 13 | 13 |
| #156 After The Black Wolf's Ultimatum | 10 | 10 | 13 | 13 |
| #157 After Operation Archon | 11 | 11 | 18 | 18 |
| #158 After A Hero in Need | 11 | 11 | 18 | 18 |
| #159 After Hearts on Fire | 11 | 11 | 18 | 18 |
| #160 After Rock the Castrum | 11 | 11 | 17 | 17 |
| 2.0 A Realm Reborn — Patch 2.0 complete | 17 | 17 | 21 | 23 |
| 2.55 A Realm Reborn — Patch 2.55 complete | 19 | 19 | 23 | 26 |

## Arcs

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

## Entities

### Minfilia (`char-minfilia`, character)

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

Evidence for each claim is listed under the entities above and in full in the [claims table](content-claims.md).
