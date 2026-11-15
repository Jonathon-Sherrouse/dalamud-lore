# Atlas content review sheet (NDL-003)

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

## Snapshot overview

| | 2.0 main story | 2.0 main + optional | 2.55 main story | 2.55 main + optional |
|---|---|---|---|---|
| Entities | 10 | 10 | 12 | 12 |
| Relationships | 8 | 10 | 10 | 13 |

Hidden at 2.0: the Crystal Braves and the Rising Stones (both first appear in 2.1–2.3), and every relationship that starts at 2.55.

## Entities

### Minfilia (`char-minfilia`, character)

**2.0 · main** · Also searchable as: the Antecedent

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

**2.0 · main**

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

**2.0 · main**

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

**2.0 · main**

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

**2.0 · main**

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

**2.0 · main**

> Alphinaud's twin sister. She doubts her brother's approach and has set out to find her own way to heal the realm's troubles. Alphinaud says that although she walks her own path, the twins share the same goal.

Sources shown: A Hero in the Making — main scenario quest (2.0); Back from the Wood — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C10** Alphinaud and Alisaie are twins. *A Hero in the Making* (2.0, main): "the traveling twins, Alphinaud and Alisaie … And my sister, Alisaie, at your service."
  - **C42** The twins call themselves students of history; Alisaie means to find another way to heal the realm. *A Hero in the Making* (2.0, main): "You might call us students of history … There must be another way to cure what ails this world─and I mean to find it!"
  - **C11** Alisaie walks her own path, but shares her brother's goal. *Back from the Wood* (2.0, main): "Alisaie has chosen to walk her own path─stubborn girl─but you may be assured that our destination remains the same."

</details>

**2.0 · optional**

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

**2.0 · main** · Also searchable as: Archon Louisoix, Master Louisoix

> A revered Archon and man of learning. He never returned from the Battle of Carteneau, and the realm's leaders lament the loss of his wisdom. The Scions still speak of his guidance.

Sources shown: The Lominsan Envoy — main scenario quest (2.0); The Gridanian Envoy — main scenario quest (2.0); Reclamation — main scenario quest (2.0)

<details><summary>Evidence</summary>

  - **C44** Archon Louisoix never returned from Carteneau, and the realm's leaders miss his wisdom. *The Lominsan Envoy* (2.0, main): "Archon Louisoix may well have been able to shed light upon these mysteries, but he, like so many, never returned from Carteneau."
  - **C44b** The Admiral wishes Archon Louisoix were still with them. *The Gridanian Envoy* (2.0, main): "Were Archon Louisoix still with us, he would doubtless shed some light on these unfathomable happenings. Alas, he is not"
  - **C44c** The Scions feel Master Louisoix's guidance still. *Reclamation* (2.0, main): "It is as if the benevolent hand of Master Louisoix guides us still."

</details>

**2.0 · optional** · Also searchable as: Archon Louisoix, Master Louisoix

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

**2.0 · main**

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

**2.0 · main**

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

**2.0 · main**

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

Evidence for each claim is listed under the entities above and in full in the [claims table](content-claims.md).
