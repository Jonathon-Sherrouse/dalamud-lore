"""Atlas content for patch 4.0, part 2: MSQ #419 To Bend with the Wind to #464 The Hour of Reckoning, including the
three-way split at #421 (cp-msq-421, cp-msq-421b, cp-msq-421c). Arc tag i. Data only (docs/atlas/era-modules.md is
the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes S05–S09); every locator is an exact substring
of a quest's Journal, Steps or main dialogue, outside optional blocks and conditional branches. Spoiler rules this
module follows:
  - recurring 4.0 entities use the contract's conventional IDs (char-hien, char-yotsuyu, char-gosetsu, char-yugiri,
    char-zenos, org-mol, loc-doma …); each first presentation here stands on its own as of its step, because the
    era before this one (Gyr Abania, Kugane) is written in parallel;
  - first names only: Zenos, Yotsuyu, Alphinaud, Alisaie, Yugiri (the pages' "yae Galvus", "Leveilleur" and
    "Mistwalker" appear only in locators, never in displayed text);
  - "Naadam" is the title of #461, so before cp-msq-461 the contest is "the Steppe's great ritual battle";
  - nothing on the parallel #421 paths depends on another path, and no entity starts on them.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

(I419, I420, I421, I421B, I421C) = ("cp-msq-419", "cp-msq-420", "cp-msq-421", "cp-msq-421b", "cp-msq-421c")
(I424, I425, I426, I427, I428, I429, I430, I431, I432, I433, I434, I435, I436, I437, I438, I439, I440, I441, I442,
 I443, I444, I445, I446, I447, I448, I449, I450, I451, I452, I453, I454, I455, I456, I457, I458, I459, I460, I461,
 I462, I463, I464) = (f"cp-msq-{n}" for n in range(424, 465))

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
Q = {419: "To Bend with the Wind", 420: "Confederate Consternation", 421: "The Solace of the Sea",
     "421b": "The Arrows of Misfortune", "421c": "The Last Voyage", 424: "Alisaie's Stones", 425: "Under the Sea",
     426: "Of Kojin and Kami", 427: "In Soroban We Trust", 428: "Forever and Ever Apart",
     429: "In Darkness the Magatama Dreams", 430: "The Whims of the Divine", 431: "Breaking and Delivering",
     432: "The Lord of the Revel", 433: "Tide Goes in, Imperials Go Out", 434: "A Silence in Three Parts",
     435: "Life after Doma", 436: "A Glimpse of Madness", 437: "The Stubborn Remainder", 438: "The Ones We Leave Behind",
     439: "A New Ruby Tithe", 440: "The Will to Live", 441: "Daughter of the Deep", 442: "Path of No Return",
     443: "The Time between the Seconds", 444: "All the Little Angels", 445: "Here There Be Xaela",
     446: "The Search for Lord Hien", 447: "A Season for War", 448: "An Impossible Dream", 449: "Stars in the Dark",
     450: "A Warrior's Welcome", 451: "The Heart of Nations", 452: "A Trial Before the Trial",
     453: "In the Footsteps of Bardam the Brave", 454: "The Children of Azim", 455: "The Labors of Magnai",
     456: "For Love of the Moon", 457: "Sworn Enemies of the Sun", 458: "The Undying Ones", 459: "A Final Peace",
     460: "As the Gods Will", 461: "Naadam", 462: "Glory to the Khagan", 463: "In Crimson They Walked",
     464: "The Hour of Reckoning"}

_RAW = [
 # #419 To Bend with the Wind
 ("M419a", 419, "Soroban, relieved that you will not judge his Blue Kojin for the deeds of the Red, carries you on to Othard.", "Relieved that you will not judge him and his fellow Blue Kojin harshly for the deeds of the Red, Soroban is eager to take you the rest of the way to Othard"),
 ("M419b", 419, "Isari, a village on Othard's coast, is occupied by imperial forces.", "turn your attentions to Isari, which you soon discover to be occupied by imperial forces"),
 ("M419c", 419, "There you see Yotsuyu, the imperial viceroy, and Grynewaht, whom you have beaten in Gyr Abania and Carteneau.", "From afar, you catch your first glimpse of Yotsuyu, the imperial viceroy, and Grynewaht of all people, who seems none the worse for the trouncings you dealt him in Gyr Abania and Carteneau"),
 ("M419d", 419, "Yotsuyu forces one villager to execute another, then has him shot for refusing to kill his own parents.", "Yotsuyu forces one villager to execute another, before having him shot for refusing to kill his own parents."),
 ("M419e", 419, "Gosetsu surrenders himself to the viceroy, expecting her to question him and give you time to plan a rescue.", "Gosetsu resolves to end the madness by surrendering himself into the viceroy's custody, reasoning that she will wish to question him thoroughly, giving you time to formulate a rescue plan"),
 ("M419f", 419, "Gosetsu is led away into the village tavern.", "you can only watch as he is led away into the local tavern."),
 ("M419g", 419, "Gosetsu calls Yotsuyu the traitor who sold her homelands to the Garleans.", "The traitor who sold her homelands to the Garleans—Yotsuyu!"),
 ("M419h", 419, "The large settlement on Onokoro, with its own aetheryte, is under the Confederacy's control.", "It would seem that Gosetsu intended for you to seek the aid of the Confederacy, as the large settlement─complete with its own aetheryte─appears to be under their control."),
 ("M419i", 419, "Gosetsu bade you seek aid at the tower to the northeast.", "Recalling that Gosetsu bade you seek aid at the mysterious tower to the northeast"),
 ("M419j", 419, "Gosetsu thanks Soroban as a clever and industrious merchant.", "Truly, we are blessed to have befriended such a clever and industrious merchant!"),
 ("M419k", 419, "There seems little chance the Confederacy will answer your call.", "there is surely little chance that they will answer your call."),
 ("M419l", 419, "Gosetsu is a former leader of the rebellion and a known fugitive.", "As a former leader of the rebellion and known fugitive, they will wish to detain me until they are certain they have learned all I know."),
 ("M419n", 419, "Tansui spoke of Doma's viceroy holding court in one of the fishing villages.", "Recalling that Tansui spoke of Doma's viceroy “holding court” in one of the fishing villages"),
 ("M419o", 419, "Alisaie and Lyse swim for the isle of Onokoro.", "she takes to the water with Lyse, and begins swimming for the isle of Onokoro."),
 ("M419m", 419, "Alisaie, frustrated, swims with Lyse for Onokoro.", "Though Alisaie is frustrated by this turn of events, she recognizes that what is done is done, and that you have no choice but to find a solution."),
 # #420 Confederate Consternation
 ("M420a", 420, "Tansui takes you to the Confederacy's captain, Rasho.", "Come with me. I will take you to the captain─Rasho."),
 ("M420b", 420, "Rasho knows Gosetsu as a former leader of the rebellion.", "Gosetsu. A former leader of the rebellion. Aye, I know of him."),
 ("M420c", 420, "To join the Confederacy is to renounce all other ties; it is beholden to and allied with none.", "to join the Confederacy is to renounce all other ties. We are beholden to none─allied with none."),
 ("M420d", 420, "The Confederacy did not rush to Doma's defense when the Empire invaded twenty-five years ago.", "When Doma was invaded by the Empire twenty-five years ago, we did not rush to her defense."),
 ("M420e", 420, "Rasho says hate is a luxury they cannot afford, and refuses further aid.", "Hate is a luxury we cannot afford.<br>You are free to come and go as you please, but you will receive no further aid."),
 ("M420f", 420, "Alisaie plans to win trust by helping people with mundane problems.", "seeking out people with mundane problems and offering them our expert assistance"),
 ("M420g", 420, "Alisaie thinks the settlement may be the Confederacy's headquarters.", "It would seem we have found a Confederate settlement─mayhap even their headquarters, judging by the size of the place."),
 # #421 The Solace of the Sea
 ("M421a", 421, "Afumi says the captain was once of Doma, and cast all aside when the imperials took his lands and family.", "The captain too was once of Doma, though he cast all aside twenty and five years ago, when the imperials took his lands and the lives of his parents and brothers."),
 ("M421b", 421, "Afumi sends medicine to a seasick Doman at Quickscape Pier.", "Then to Quickscape Pier and the hapless Doman bemoaning his wretched fate."),
 ("M421c", 421, "Afumi wonders whether you too will renounce your ties and join them.", "Perhaps you too will renounce your ties and join us someday?"),
 # #421b The Arrows of Misfortune
 ("M421ba", "421b", "Kajika says they would not normally hunt gyuki as game, but these are not normal times.", "Under normal circumstances, we would not bother hunting gyuki as game, but as you may have heard, these are not normal circumstances."),
 ("M421bb", "421b", "Even arrows must be reused.", "Arrows too must be reused when possible. A prudent measure become necessary, alas."),
 ("M421bc", "421b", "Kajika sends you to a gyuki carcass on the beach to the west.", "On the beach far to the west lies the carcass of a gyuki, feathered with arrows."),
 # #421c The Last Voyage
 ("M421ca", "421c", "Aranami sends you after a recruit he ordered to patrol Onokoro's northern edge.", "A new recruit I ordered to patrol the northern edge of Onokoro."),
 ("M421cb", "421c", "The recruit mourns a comrade who died hunting deadly game in treacherous waters.", "She hunted rare and deadly game in treacherous waters, and lost her life for it."),
 ("M421cc", "421c", "Aranami admits he judged the recruit too quickly.", "Too quick was I to judge him."),
 # #424 Alisaie's Stones
 ("M424a", 424, "Kojin chasing a group of pirates asked whether they were Doman.", "Before the Kojin started chasing us, their leader asked us if we were Doman..."),
 ("M424b", 424, "A pirate calls the Kojin Yotsuyu's catchers.", "They're Yotsuyu's catchers, I know it! First Isari, and now this!"),
 ("M424c", 424, "Alisaie sees Kojin mercenaries rounding up Doman Confederates.", "Kojin mercenaries rounding up Doman Confederates? Surely Yotsuyu has crossed the line now..."),
 ("M424d", 424, "Rasho will take no revenge until the enemy is weaker; he waits for a sign.", "Until the day our enemy is grown weaker, and we stronger, there can be no retribution. We will wait for a sign."),
 ("M424e", 424, "Alisaie vows to deprive the Garleans of a key ally, the Kojin.", "Accordingly, we shall demonstrate our seriousness by depriving the Garleans of a key ally: the Kojin."),
 ("M424f", 424, "The wager: if you succeed, the Confederacy helps liberate Isari.", "If we succeed, you help us liberate Isari. If we fail, you lose nothing."),
 ("M424g", 424, "Rasho will weigh you by your deeds.", "Words are air. We will weigh you by your deeds."),
 # #425 Under the Sea
 ("M425a", 425, "The Kojin mercenaries who serve the Empire are of the Red.", "The mercenaries who serve the Empire belong to the Red."),
 ("M425b", 425, "The Blue Kojin are traders with no pact with the Empire, who may aid you.", "Those who belong to the Blue are the traders. They have made no pact with the imperials, and so may be willing to aid your cause."),
 ("M425c", 425, "Soroban welcomes you to Tamamizu.", "Just so. I bid you welcome to Tamamizu!"),
 ("M425d", 425, "Lyse says Yda and her father knew how to inspire people.", "Yda and my father had a way with words. They knew how to inspire people─how to bring them together."),
 ("M425e", 425, "Lyse fears she lacks that gift.", "I always hoped I might have something of that in me too, but I'm starting to think I don't."),
 ("M425f", 425, "Tamamizu lies inside a giant bubble.", "We, uh...appear to be standing inside a giant bubble."),
 # #426 Of Kojin and Kami
 ("M426a", 426, "Soroban introduces Bunchin, leader of the Blue Kojin.", "Very well. I shall introduce you to our leader, Bunchin."),
 ("M426b", 426, "The Blue uphold the old ways, trading and valuing peace; the Red live by the sword.", "While our Red brothers live by the sword, we Blue Kojin uphold the old ways, engaging in trade and valuing peace."),
 ("M426c", 426, "The Red Kojin resolved to join the Empire.", "Wiser to join with them. So resolved the Red Kojin."),
 ("M426d", 426, "Hingashi held the Yasakani-no-Magatama until it presented the jewel to the Garleans.", "This jewel, this most sacred of Kojin relics, was in the possession of Hingashi─until they decided to present it to the Garleans in a gesture of conciliation."),
 ("M426e", 426, "In the chaos when the Red seized the ship, the Magatama was lost to the sea.", "in the ensuing chaos the Magatama was lost to the sea."),
 ("M426f", 426, "The Blue want to recover the jewel before the Red.", "We wish to recover the sacred jewel before our brothers."),
 ("M426g", 426, "The Red pose as mercenaries and never speak of their faith before their masters.", "So the Red masquerade as mercenaries who seek money and power and never speak of their faith in the presence of their masters."),
 ("M426h", 426, "The people of Sui-no-Sato can guide you better than the Kojin.", "The shell-less of Sui-no-Sato can provide you with better guidance than we."),
 # #427 In Soroban We Trust
 ("M427a", 427, "Soroban's ritual lets you travel the depths to search for the Yasakani-no-Magatama.", "to let you traverse the depths as easily as any [[Kojin]], that you might begin your search for the [[Yasakani-no-Magatama]]."),
 ("M427b", 427, "On rays he summons, you set out for Sui-no-Sato.", "with the aid of the striped rays, you embark on your journey to [[Sui-no-Sato]]."),
 ("M427c", 427, "Alisaie: first win over the Confederacy, rescue Gosetsu and liberate your homelands.", "after we've won over the Confederacy, rescued Gosetsu, and liberated your respective homelands."),
 ("M427d", 427, "Sui-no-Sato is the underwater village of the reclusive Raen.", "the underwater village of the [[Raen]]. But will these reclusive people be willing to aid your cause?"),
 # #428 Forever and Ever Apart
 ("M428a", 428, "Shiosai is high priest of Shisui of the Violet Tides.", "I am high priest of Shisui of the Violet Tides. Shiosai."),
 ("M428b", 428, "The Raen live under the Ruby Princess, sovereign of Shisui.", "Under the benevolent leadership of the Ruby Princess, sovereign of Shisui, we Raen enjoy humble yet fulfilling lives."),
 ("M428c", 428, "When Doma fell twenty-five years ago, the Ruby Princess decreed the Raen would take no part.", "So it was when Doma fell twenty-five years past. The Ruby Princess, in her wisdom, decreed that we would take no part."),
 ("M428d", 428, "Shiosai will not betray his people by letting outsiders stay.", "For me to defy their will and permit outsiders to remain would be a gross betrayal of my responsibilities."),
 ("M428e", 428, "Yotsuyu presses Gosetsu about Doma's missing heir.", "To wit, I would ask you again to help me resolve this vexing matter of Doma's missing heir."),
 ("M428f", 428, "The Garleans want the heir found, living or dead; Yotsuyu knows Gosetsu helped Lord Hien flee.", "Living or dead, it makes no difference really … I know you helped him flee. So, tell me: what became of Lord Hien?"),
 ("M428g", 428, "Grynewaht beats the bound Gosetsu.", "''Grynewaht beats up a bound Gosetsu.''"),
 ("M428h", 428, "Yotsuyu mocks the late Lord Kaien as the leader of a fallen nation.", "Poor, poor Lord Kaien─kami rest his soul! Noble leader of a fallen nation..."),
 ("M428i", 428, "Gosetsu claims the details escape him.", "To my dismay, the details escape me at present."),
 # #429 In Darkness the Magatama Dreams
 ("M429a", 429, "Ihanami and Yunagi's daughter fought in the rebellion and has not been heard from since.", "Our daughter fought in the rebellion. We have heard naught from her since."),
 ("M429b", 429, "The Ruby Princess of the day forbade Yugiri's return.", "When the then Ruby Princess learned of this, she forbade Yugiri's return, lest she bring misfortune to us all."),
 ("M429c", 429, "As a child Yugiri went to Doma and met a proud son of Yanxia.", "To Doma they went, where they met a young boy─a proud son of Yanxia."),
 ("M429d", 429, "Ihanami sends you to search a sunken ship to the east.", "There is a sunken ship to the east. Though the currents may have spirited away her cargo, you should begin your search there."),
 ("M429e", 429, "Alisaie confirms the jewel is the Yasakani-no-Magatama.", "This...this is it! The Yasakani-no-Magatama, exactly as Soroban described!"),
 ("M429f", 429, "Yunagi asks you to tell Yugiri her family thinks of her every day.", "pray tell her not a day goes by that her parents and her brothers do not think of her."),
 ("M429g", 429, "Lyse says you are looking for Yugiri too.", "We're looking for her too, actually, but I'm sure she's all right."),
 # #430 The Whims of the Divine
 ("M430a", 430, "The Magatama is one of three Kojin treasures; the other two lie in the vault.", "The Yasakani-no-Magatama is one of three most coveted treasures of the Kojin. The other two lie within the vault."),
 ("M430b", 430, "Bunchin's ceremonial knife opens the Kojin vault on the Isle of Zekki.", "Before this blade, that which is sealed shall open. The treasure vault of the Kojin, on the Isle of Zekki."),
 ("M430c", 430, "An attack on the vault would summon Kojin from all around to defend it.", "Were the vault to be attacked, their response would by necessity be immediate. Kojin would be summoned from malms around to defend their treasures."),
 ("M430d", 430, "Without the Kojin, the imperials lack the troops to hold Isari.", "Without the Kojin, the imperials don't have nearly enough troops in Isari to hold off the pirates."),
 ("M430e", 430, "Soroban will tell the Confederacy to be ready to act.", "I shall inform the Confederacy of your plans, and bid them make ready to act when the time is right."),
 ("M430f", 430, "Soroban says the Magatama chose you to bear it.", "The Magatama has chosen you to bear it to its brothers."),
 # #431 Breaking and Delivering
 ("M431a", 431, "Alisaie's plan: two draw the guards while the third goes for the vault.", "How about two of us get the guards' attention while the third heads straight for the vault?"),
 ("M431b", 431, "The three treasures glow and rise into the air.", "''The three treasures begin glowing and become airborne.''"),
 ("M431c", 431, "A Red commander hails a great kami of the sacred treasures.", "Hark! A great kami stirs... Yes, yes, a great kami of the sacred treasures!"),
 ("M431d", 431, "The Red have guarded the kami's blade and glass for generations.", "We who have guarded your blade and glass for generations─your faithful Kojin!"),
 ("M431e", 431, "The kami names itself Susano.", "We are Susano, and in revelry do we rejoice!"),
 ("M431f", 431, "Alisaie resolves to defeat the primal.", "We have to defeat that primal!"),
 ("M431g", 431, "Susano marvels that you delivered the jewel to your enemy's vault.", "Thou didst freely deliver our jewel unto thine enemy's own treasure vault?"),
 # #432 The Lord of the Revel
 ("M432a", 432, "Susano is a primal by another name, summoned when the treasures reacted to the Magatama.", "summoning forth from the aether the great kami [[Susano]]—a [[primal]] by another name."),
 ("M432b", 432, "The great kami is no more.", "The great kami is no more"),
 ("M432c", 432, "Alisaie stays to give you and Lyse an opening to escape.", "Alisaie steps forward, resolved to provide you and Lyse with an opening in which to escape."),
 ("M432d", 432, "Rasho means to keep the Confederacy's bargain with the Eorzeans.", "We made a bargain with the Eorzeans, and I mean to uphold our end of it."),
 ("M432e", 432, "Yotsuyu swears to find Lord Hien.", "Mark me, samurai─I will find Lord Hien, be it with your help or with your heads."),
 ("M432f", 432, "Grynewaht says Gosetsu is iron.", "This one is iron. My hands will break before he speaks."),
 ("M432g", 432, "Lyse meant to go back for Alisaie, who turns up right behind her.", "No sooner have you reached the beach south of Isari than Lyse declares her intention to return to the Isle of Zekki and help Alisaie."),
 ("M432h", 432, "The Red sounded the alarm and rushed to defend the Isle of Zekki.", "The Red have sounded the alarum. The Isle of Zekki under attack; fierce fighting in the stronghold."),
 ("M432i", 432, "Grynewaht addresses Yotsuyu as his lady.", "My lady, I... I'm going outside!"),
 ("M432j", 432, "A Red marine cries that Susano is slain.", "S-Susano is slain! Slain by the shell-less one!"),
 ("M432k", 432, "Rasho means to remind the Garleans that the sea belongs to the Confederacy.", "I mean to remind the Garleans that this is our sea─that all here belongs to the Confederacy!"),
 ("M432l", 432, "Alisaie is safe behind Lyse.", "as is the shock of hearing Alisaie's voice coming from right behind her."),
 # #433 Tide Goes in, Imperials Go Out
 ("M433a", 433, "The imperials fled Isari once their Kojin reinforcements failed to come.", "Fled. They stood their ground for a time─until it became clear that their Kojin reinforcements would not be coming."),
 ("M433b", 433, "The Empire believes the Confederacy attacked Isari alone, in retaliation for the viceroy's actions.", "So far as the Empire is concerned, the Confederacy attacked Isari in retaliation for the viceroy's actions─and without the aid of insurrectionists, I might add."),
 ("M433c", 433, "The Confederacy expects the Empire's undivided attention.", "we are prepared to be the subject of their undivided attention for the foreseeable future."),
 ("M433d", 433, "Gosetsu and the captives are alive.", "Gosetsu! You're alive! You're all alive..."),
 ("M433e", 433, "Rasho regrets letting Yotsuyu slip away; her bodyguard is dangerous in battle.", "my deeper regret is having let Yotsuyu slip through my fingers. That bodyguard of hers may be a half-wit, but he's a mean bastard on the battlefield."),
 ("M433f", 433, "Gosetsu trusts his allies yet live, and will plan the next step once he finds them.", "I have faith that our allies yet live. … Once we have found them, we will plan our next step."),
 ("M433g", 433, "Rasho calls Yanxia the crucible of the rebellion, where Yotsuyu did worse.", "Yanxia was the crucible of the rebellion. What happened here pales in comparison to what Yotsuyu did there."),
 ("M433h", 433, "The Confederates rescued the fishermen and their kidnapped comrades.", "Thanks to you, we managed to rescue the fishermen and my kidnapped comrades"),
 # #434 A Silence in Three Parts
 ("M434a", 434, "Confederate forces drove Yotsuyu from Isari, and the captives survived.", "[[Yotsuyu]] and her imperials have been driven from [[Isari]], and their former captives managed to survive their ordeal."),
 ("M434b", 434, "Zenos left Doma after crushing the rebellion and named Yotsuyu to serve in his stead.", "[[Zenos]] had no desire to remain in Doma after he crushed the rebellion, and so he named Yotsuyu to serve in his stead."),
 ("M434c", 434, "The acting viceroy waged an indiscriminate campaign of terror on the villages.", "The acting viceroy waged an indiscriminate campaign of terror, marching into villages without warning"),
 ("M434d", 434, "The purges ceased, but their memory keeps the people from resisting.", "After a time, these purges ceased, but the memory remains, and with it the promise of punishment should the people resist."),
 ("M434e", 434, "Gosetsu is still hurt from Grynewaht's interrogation.", "Despite his assurances, [[Gosetsu]] is clearly still troubled by the injuries he sustained from [[Grynewaht]]'s brutal interrogation."),
 ("M434f", 434, "Grynewaht cuts down the Red Kojin there and destroys most of their treasure.", "''Grynewaht defeats all of the Red Kojin and destroys most of the treasure.''"),
 ("M434g", 434, "Yotsuyu takes a katana, one of the Red's treasures.", "And what do we have here? One of the vaunted treasures of the Red?"),
 ("M434h", 434, "Grynewaht wants Zenos to reinstate him so he can return to Eorzea.", "How long before Lord Zenos reinstates me, d'you reckon? I've got unfinished business back in Eorzea..."),
 ("M434i", 434, "Gosetsu leads you to Namai, a farming village to the west.", "Gosetsu leads you to [[Namai]], a humble farming village a little ways to the west."),
 ("M434j", 434, "Yotsuyu rebukes the Red Kojin for abandoning the posts she contracted them for.", "So this is why you abandoned your posts─and without a word of explanation at that. … What is the point of contracting your services if you are not here when they are required?"),
 # #435 Life after Doma
 ("M435a", 435, "Isse names Gosetsu as Lord Kaien's retainer, a leader of the rebellion wanted by the Empire.", "Lord Kaien's retainer and leader of the rebellion—Gosetsu! Notorious fugitive, wanted dead or alive by the Empire!"),
 ("M435b", 435, "The rebels died, and the imperials came looking for more.", "They fought, and they died. Every last one. And then the imperials came looking for more. Because of them."),
 ("M435c", 435, "Gosetsu cannot leave things as they are.", "surely he must know that I cannot leave things as they are."),
 ("M435d", 435, "The House of the Fierce is the Doman Liberation Front's headquarters.", "We must continue on towards our final destination—the House of the Fierce. Proud headquarters of the Doman Liberation Front."),
 ("M435e", 435, "Isse wants Namai left out of the plotting.", "Whatever it is you're plotting, leave us out of it!"),
 ("M435f", 435, "A secret entrance north of Namai leads through a small spring.", "There is a secret entrance to the north of Namai, by way of a small spring."),
 # #436 A Glimpse of Madness
 ("M436a", 436, "Lord Hien is the son of Lord Kaien, who perished during the rebellion.", "he speaks of Lord Hien, son of Lord Kaien, who perished during the rebellion."),
 ("M436b", 436, "Hien sent his people to safety, then fought on as heir until a grievous wound left him vanished.", "When it became clear that all hope of victory had gone, Lord Hien bade us deliver as many of our people as we could to safety beyond our borders. But as his father's heir, he was determined to fight on, and so he did─until he suffered a grievous wound in battle and vanished without a trace..."),
 ("M436c", 436, "Yugiri has found Lord Hien on the Azim Steppe.", "For I have found Lord Hien─seen and spoken with him. On the Azim Steppe."),
 ("M436d", 436, "Hien will offer Doma his blade if it still thirsts for freedom, or else his head to its conquerors.", "If Doma yet thirsts for the blood of patriots and tyrants, I shall offer unto her my blade. But if she has had her fill of bitter draughts, I shall offer unto her conquerors my head."),
 ("M436e", 436, "Hien asks Yugiri to learn the truth of Doma's heart.", "Learn the truth of her heart and return to me"),
 ("M436f", 436, "Zenos ended the Front's hopes with the secrets Yotsuyu sold.", "But Zenos soon put paid to that, with the aid of Yotsuyu and the secrets she sold."),
 ("M436g", 436, "Zenos desired hate, not obedience.", "He did not desire obedience. He desired hate...and men consumed by it."),
 ("M436h", 436, "Zenos has wielded Far Eastern blades ever since.", "Since that day, he has ever wielded Far Eastern blades."),
 ("M436i", 436, "The Front is few and weak, its enemies legion.", "We are few, and our enemies legion. We are weak, and they strong."),
 ("M436j", 436, "The Front disabled its aetheryte.", "As you can see, they went to great lengths to disable the aetheryte."),
 ("M436k", 436, "Zenos made the Front's soldiers watch their comrades die.", "One...after...another. He made us watch. Do you understand? He made us watch."),
 # #437 The Stubborn Remainder
 ("M437a", 437, "Yugiri proposes going among the people to witness their hardship.", "Let us go among the people and with our own eyes bear witness to their hardship."),
 ("M437b", 437, "You pose as traveling merchants, with you as leader.", "We shall pose as traveling merchants─[Forename] as our leader,"),
 ("M437c", 437, "The samurai lords of Monzen all died in battle or in the purges.", "Once, I would have directed you to the samurai lords of Monzen─had they not all died in battle or in the purges."),
 ("M437d", 437, "The Doman Enclave lies beyond the Dairyu Moon Gates.", "There is the Doman Enclave, of course, but that lies beyond the Dairyu Moon Gates."),
 ("M437e", 437, "The villagers have been pushed beyond the brink.", "Lyse and I encountered much of the same. They have been pushed beyond the brink."),
 ("M437f", 437, "Unless the villagers change their minds, Yugiri fears she cannot bring Lord Hien back.", "Unless we can convince them otherwise, I fear I cannot convince Lord Hien to return"),
 ("M437g", 437, "The villagers question the wisdom of opposing imperial rule at all.", "not so much that they would come to question the wisdom of opposing imperial rule in the first place"),
 # #438 The Ones We Leave Behind
 ("M438a", 438, "Isse's parents believed in the rebellion and left to fight for Lord Kaien.", "My mother and father believed in the rebellion. They left to fight for Lord Kaien."),
 ("M438b", 438, "Imperial soldiers beat the rebels' families in the village square.", "They beat us in the village square─with their hands, with sticks, with anything."),
 ("M438c", 438, "A soldier threatened what he would do to Isse's sister.", "One leaned close and whispered in my ear what he'd do to my sister if they had to come back."),
 ("M438d", 438, "The imperials are never far, and the wrong word brings them back.", "They're gone, but they're never far. All it takes is the wrong word in the wrong ear, and they'll return."),
 ("M438e", 438, "Yugiri wonders whether Lord Hien foresaw how broken his people would be.", "Could Lord Hien have foreseen this? That our people's spirits would be broken so?"),
 ("M438f", 438, "Isse will not report you to the imperials.", "I'm not going to report you to the imperials, or anything stupid like that."),
 # #439 A New Ruby Tithe
 ("M439a", 439, "Imperial soldiers select villagers to serve the Garleans, ending with Isse.", "the pilus prior begins to select villagers one by one, ending with Isse, the young man who implored you to leave Namai and never return."),
 ("M439b", 439, "The pilus calls the battle at Isari an act that will not go unanswered.", "He tells the gathered people of the battle between Confederate and imperial forces in Isari, declaring it a brazen, unconscionable act that will not go unanswered."),
 ("M439c", 439, "Yugiri sees an attempt to intimidate those who supported the Confederacy.", "This is but a thinly veiled attempt to intimidate those who supported the Confederacy's actions"),
 ("M439d", 439, "Yugiri gives you a blowgun and sleeping darts.", "she furnishes you with a blowgun and darts that you can use to put imperial soldiers to sleep."),
 ("M439e", 439, "The villagers are held in the castrum Fluminis.", "The villagers are being held in the castrum to the south─Fluminis."),
 ("M439f", 439, "The captives realize they have been sentenced to servitude.", "it finally dawns on the gathered Domans that they have been effectively sentenced to a life of servitude."),
 ("M439g", 439, "Yugiri sends Lyse back to the House of the Fierce.", "After Yugiri convinces Lyse to return to the House of the Fierce to inform the others of this development"),
 # #440 The Will to Live
 ("M440a", 440, "Yugiri means to infiltrate the castrum without raising the alarm.", "To wit, we must infiltrate the castrum without raising the alarum."),
 ("M440b", 440, "You steal a uniform from a sleeping soldier.", "Steal a suitable uniform from a sleeping soldier."),
 ("M440c", 440, "Isse says the villagers are lost and afraid and can change nothing.", "We're lost and afraid! We hate this─all of this─but we can't do a damn thing to change it!"),
 ("M440d", 440, "An elder says the survivors are forced to bend the knee.", "We who survived are forced to bend the knee─to sell our souls and surrender our dignity."),
 ("M440e", 440, "Yugiri swears by all the kami to free them.", "I swear by all the kami in creation that I will free you from this torment."),
 ("M440f", 440, "Isse asks whether Yugiri is Lord Hien's retainer.", "You are Lord Hien's retainer?"),
 ("M440g", 440, "Yugiri has dealt with the imperials and tells the villagers to flee.", "We have dealt with the imperials for now, but you must flee this place, quickly!"),
 # #441 Daughter of the Deep
 ("M441a", 441, "Yugiri was born beneath the waves of the Ruby Sea.", "in truth I am not of Doma. I was born beneath the waves of the Ruby Sea..."),
 ("M441b", 441, "Yugiri met Lord Kaien, his son and their loyal samurai Gosetsu.", "It was then that I met Lord Kaien and his son, and their loyal samurai, Gosetsu."),
 ("M441c", 441, "Yotsuyu governs Doma, but Zenos is its anointed viceroy and has come in person.", "Though Yotsuyu governs Doma, Zenos remains the province's anointed viceroy─and it would seem he has come to assess the current situation in person."),
 ("M441d", 441, "Zenos defeated the Alliance, the Resistance and the Scions.", "He faced the Alliance, the Resistance and the Scions, and he defeated us all."),
 ("M441j", 441, "The Scions encountered Zenos at Rhalgr's Reach.", "You may recall that we encountered Zenos at Rhalgr's Reach."),
 ("M441e", 441, "The crown prince has come to Doma.", "The crown prince is come to Doma."),
 ("M441f", 441, "Gosetsu warns Zenos's death would not free Doma, more likely doom it.", "Even should you succeed, Zenos's death will not win Doma her freedom─more likely her doom."),
 ("M441g", 441, "Yugiri will not squander the chance.", "I will not squander this opportunity!"),
 ("M441h", 441, "An imperial airship is bound for Doma Castle.", "It is bound for Doma Castle. Quickly, we must rejoin the others!"),
 ("M441i", 441, "Yugiri learned the shinobi's secrets and was sent to assist the Doman Liberation Front.", "After a time, my skills were recognized, and I was dispatched to assist the Doman Liberation Front."),
 # #442 Path of No Return
 ("M442a", 442, "Gosetsu will not pursue Yugiri.", "I will not pursue her. It is for her to think on our master's words"),
 ("M442b", 442, "Zenos will inspect the Moon Gates this evening.", "He wishes to inspect the Moon Gates this very eve."),
 ("M442c", 442, "Zenos arrived without warning, giving Yotsuyu no time to prepare.", "He arrived without warning and gave Yotsuyu no time to prepare."),
 ("M442e", 442, "You are to meet Yugiri at Yuzuka Manor.", "Rendezvous with Yugiri at [[Yuzuka Manor]]."),
 ("M442f", 442, "Isse overheard two rebels plotting to kill the crown prince.", "No one knows you overheard two rebels plotting...to kill the crown prince..."),
 ("M442g", 442, "Yugiri thanks you for joining her.", "Thank you. Thank you. I...I cannot well express what this means to me."),
 # #443 The Time between the Seconds
 ("M443a", 443, "Yugiri resolved to assassinate Zenos over her comrades' protests, and only you agreed to help.", "Yugiri has resolved, over the protestations of your comrades, to assassinate him. You alone have agreed to support her in this endeavor"),
 ("M443b", 443, "Zenos's new katana unleashes crimson energy that fells Yugiri and the soldiers.", "until your foe elects to bring a new katana to bear against you. At once, his body begins to crackle with a crimson energy, which bursts forth and fells both Yugiri and the viceroy's few remaining soldiers."),
 ("M443c", 443, "Zenos recognizes you as the champion of the savages in Ala Mhigo.", "recognizes you as the champion of the savages in Ala Mhigo"),
 ("M443d", 443, "He urges you to live, grow stronger and face him again.", "he implores you to live on, to endure, to grow stronger, and to face him once more"),
 ("M443e", 443, "Armed villagers, Gosetsu and Alisaie stand ready to save Yugiri.", "pauses when confronted by a group of armed villagers, as well as Gosetsu and Alisaie, who are determined to save the ninja's life."),
 ("M443f", 443, "Zenos withdraws without a word.", "Nevertheless, Zenos withdraws without a word, leaving you and your comrades free to withdraw to safety."),
 ("M443g", 443, "Alphinaud convinced the others to rush to your defense.", "for it was he who convinced the others to rush to your defense."),
 ("M443h", 443, "Zenos says the Empire sowed hatred and fear to train the Domans as beasts.", "We labored long to sow the seeds of hatred, of fear─to train them as beasts."),
 # #444 All the Little Angels
 ("M444a", 444, "Yugiri apologizes for rashly pursuing Zenos.", "[[Yugiri]] also offers an apology for her rash decision to pursue [[Zenos]]."),
 ("M444b", 444, "Yugiri sets out for the Azim Steppe to find Lord Hien.", "Yugiri decides to travel to [[Azim Steppe]] again to find [[Hien|Lord Hien]]."),
 ("M444c", 444, "Tataru and Hancock report that the Empire withdrew most of its forces from Doma this past year.", "according to Tataru and Hancock's intelligence, the Empire has withdrawn most of its forces from Doma in the past year"),
 ("M444d", 444, "Alphinaud believes an uprising led by the Liberation Front could threaten Doma Castle.", "a popular uprising spearheaded by the full might of the Doman Liberation Front may feasibly be sufficient to threaten the seat of provincial government, namely Doma Castle."),
 ("M444e", 444, "The Alliance cannot be looked to for aid.", "we cannot look to the Alliance for aid."),
 ("M444f", 444, "Gosetsu says the people's open defiance of Zenos is the proof Hien wanted.", "He desired proof of his subjects' conviction, and they have provided it─through no less a deed than openly opposing Zenos himself!"),
 ("M444g", 444, "Zenos chose Yotsuyu for her petty hatreds, to bleed her kinsmen of hope.", "Because of your petty hatreds.<br>They render you the perfect instrument to bleed your kinsmen of hope"),
 ("M444h", 444, "Zenos warns Yotsuyu she will get no second chance if she yields Doma.", "If you yield Doma to the rebels, you will not be given another chance to beg forgiveness."),
 ("M444i", 444, "A familiar man has found a great chasm in Gyr Abania.", "Meanwhile in [[Gyr Abania]], a strange, but familiar man has stumbled on a large, mysterious chasm."),
 ("M444j", 444, "Yotsuyu hears that your Eorzean is helping the rebels.", "They say your Eorzean is helping the rebels."),
 ("M444k", 444, "Isse vows Namai will finish what it started.", "When you come back, we'll finish what we started."),
 ("M444l", 444, "Isse apologizes for his earlier disdain.", "Isse offers an apology for his earlier disdain towards the adventurer."),
 ("M444m", 444, "At the crater, Estinien recalls swearing to leave his old life behind once the shade was banished.", "Aye, this is the place. … When his shade was banished, you swore to leave this life behind."),
 # #445 Here There Be Xaela
 ("M445a", 445, "Convinced this is Lord Hien's sign, you set out for the Azim Steppe to bring him home to lead a new rebellion.", "Convinced that this is the sign that Lord [[Hien]] has been waiting for, you and your comrades embark on a journey to the [[Azim Steppe]] to seek out the young heir and convince him to return to lead his people in a new rebellion against the [[Garlean Empire|Empire]]."),
 ("M445b", 445, "The failed attempt on Zenos spurred Doma's people to openly oppose the imperials.", "it spurred the people of [[Doma]] to rise up and openly oppose the imperials in battle."),
 ("M445c", 445, "Domans rarely venture so far north.", "Despite the close proximity, Domans rarely venture this far north."),
 ("M445d", 445, "The search for Lord Hien begins at Reunion.", "Welcome to Reunion, my friends. Here is where we will begin our search for Lord Hien."),
 ("M445e", 445, "The route runs north from Isari through a mountain tunnel.", "From [[Isari]] you must continue north, towards a tunnel leading through the mountains."),
 ("M445f", 445, "Reunion is a marketplace filled with Xaela from across the Steppe.", "You come to the gates of what appears to be a bustling marketplace, filled with [[Xaela]] from all across the Steppe."),
 # #446 The Search for Lord Hien
 ("M446a", 446, "More than fifty Xaela tribes roam the Steppe, ranked through ritual combat.", "More than fifty roam these lands, and though they do not constitute a nation, there is a hierarchy of sorts, determined through ritual combat."),
 ("M446b", 446, "The Steppe's thin soil and harsh weather were not made for men.", "These lands were not made for men. The soil is thin, and the weather unforgiving."),
 ("M446c", 446, "The Doman comes and goes with a Mol girl.", "I know of whom you speak. He comes and goes with a Mol girl."),
 ("M446d", 446, "Cirina is of the Mol.", "Yes? I am Mol. My name is Cirina. May I help you?"),
 ("M446e", 446, "Cirina realizes you are looking for Hien.", "Oh... Oh, I see. You are looking for Hien."),
 ("M446f", 446, "Cirina cannot leave Reunion without the kinsai.", "I cannot leave Reunion without that kinsai..."),
 # #447 A Season for War
 ("M447a", 447, "Cirina says the Mol are lambs among wolves, long content to live apart.", "The Mol are lambs among wolves. Long were we content to remain apart and live quietly, but..."),
 ("M447b", 447, "The Oronir and Dotharl are the two strongest tribes.", "Those boys are of the Oronir and Dotharl. The two strongest tribes."),
 ("M447c", 447, "The tribe that triumphs in the Naadam rules until the next Tsagaan Sar.", "The tribe which triumphs in the Naadam rules until the next Tsagaan Sar."),
 ("M447d", 447, "Fighting in Reunion means banishment.", "To fight in Reunion is forbidden, and to break the peace is to be banished forever."),
 ("M447e", 447, "Cirina knows where Hien may be.", "You seek Hien, yes? I know where he may be."),
 # #448 An Impossible Dream
 ("M448a", 448, "Guided by her grandmother's vision, Cirina found Hien near death in the southern mountains.", "Long ago, guided by a vision received by her grandmother, she ventured into the southern mountains and there found Hien, near death."),
 ("M448b", 448, "The Mol nursed Hien back to health, and he has stayed to repay them.", "Cirina brought the Doman lord to her village, where they nursed him back to health, and there he has remained ever since, until such time as he can repay his debt to them."),
 ("M448c", 448, "You meet the young heir to Doma's throne, who greets you as a friend.", "you come face–to–face with the young heir to Doma's throne, who greets you as a friend."),
 ("M448d", 448, "Hien will not go home until he wins the Naadam and earns the right to lead the Xaela to Doma.", "he states that he cannot go home─not until he has won the ceremonial battle known as the Naadam and thereby earned the right to bid the Xaela follow him to Doma."),
 ("M448e", 448, "The Liberation Front's forces are depleted.", "given the Liberation Front's depleted forces."),
 ("M448f", 448, "Yugiri presents the Scions as friends who sheltered the Domans who fled to Eorzea.", "The Scions of the Seventh Dawn, my lord─good and true friends who opened their hearts and homes to us when we fled to Eorzea."),
 ("M448g", 448, "Hien's father ruled in name only for twenty-five years.", "For twenty-five years did my father rule in name only."),
 ("M448h", 448, "Hien sends Yugiri back to Yanxia to take charge of their forces.", "Yugiri, I bid you return to Yanxia and take charge of our forces in preparation for my homecoming."),
 ("M448i", 448, "Hien's impossible dream is a revolution against the most powerful empire in the world.", "For ours is an impossible dream─to set in motion a revolution that will rattle the very firmament, and shake off the yoke of the most powerful empire in the world!"),
 ("M448j", 448, "Yugiri says the people of Yanxia are ready to rise up and fight.", "The people of Yanxia remain loyal to Doma. I have seen the fire in their eyes─they are ready to rise up and fight."),
 # #449 Stars in the Dark
 ("M449a", 449, "Hien asks to fight in the Naadam as a warrior of the Mol.", "To that end, I wish to fight in the Naadam─as a warrior of the Mol. Will you grant me this honor?"),
 ("M449b", 449, "Victory beside a more favored tribe would be credited to it, and none would follow Hien.", "Were we to join hands with a more favored tribe, our victory would inevitably be attributed to them. And no one would follow me to Doma."),
 ("M449c", 449, "No foreigner has ever taken part in a Naadam, let alone won.", "To my knowledge no foreigners have ever participated, much less triumphed in a Naadam."),
 ("M449d", 449, "Cirina says the Mol are weak and few.", "There is no path to victory! We are weak and our numbers few."),
 ("M449e", 449, "Temulun, khatun of the Mol, invites you to join them in the Naadam.", "As khatun of the Mol, I invite you all to join with us in the Naadam."),
 ("M449f", 449, "Temulun says the gods and stars know you.", "The gods know you, child...as do the stars in the heavens, which shone bright at your coming."),
 ("M449g", 449, "To be recognized as Mol warriors you must overcome a trial.", "To be recognized as warriors of the Mol, there is a trial you must overcome."),
 ("M449h", 449, "The Mol hearken to the whispers of the elder gods.", "The Mol hearken to the whispers of the elder gods, which guide us in our daily lives."),
 # #450 A Warrior's Welcome
 ("M450a", 450, "The trial sends you to the far reaches of the Steppe, as the warrior Bardam once went.", "You will journey unto the far reaches of the Steppe to confront a terrible foe, as did the warrior Bardam in the days of yore."),
 ("M450b", 450, "Many who follow Bardam's footsteps perish.", "Many who follow in his footsteps perish, lacking in strength of body and mind."),
 ("M450c", 450, "For the feast, gulo gulo are to be lured to slaughter.", "For today's feast the gods decreed that we lure gulo gulo to slaughter with entrails."),
 ("M450d", 450, "Hien splits the bait between you for a contest.", "I have six bags of entrails with which we may lure our gulo gulo. Three for you, and three for me."),
 # #451 The Heart of Nations
 ("M451a", 451, "A Mol boy says the soil belongs to one and all.", "Ours is the soil of one and all."),
 ("M451b", 451, "Hien says he should have fled after his father died.", "I know I should have fled with the others after Father died, instead of blindly fighting on."),
 ("M451c", 451, "His people called for the sword, so that is what he must be.", "Instead they have called for the sword, so that is what I must be."),
 ("M451d", 451, "Gosetsu calls Hien Master Shun.", "Mina's little Master Shun. What a fine young man you've become!"),
 ("M451e", 451, "Gosetsu has amends to make before he meets his ancestors.", "I myself am in no hurry to meet those who have gone before—not while I have still to make amends."),
 ("M451f", 451, "Hien declares it time for your trial.", "Then what better time than now to undertake our trial, and become full-fledged warriors of the Mol!"),
 # #452 A Trial Before the Trial
 ("M452a", 452, "To be warriors of the Steppe, you must follow in the footsteps of Bardam.", "to be recognized as warriors of the Steppe, one must follow in the footsteps of the legendary warrior Bardam."),
 ("M452b", 452, "Bardam walked to a holy place, thereafter named Bardam's Mettle.", "walked for many malms until he came to a holy place, thereafter named Bardam's Mettle."),
 ("M452c", 452, "You must tame a yol at the altar's breeding grounds.", "The altar lies deep within the breeding grounds of the yol. To complete your trial, you must tame one."),
 ("M452d", 452, "On the eve of the Naadam, some tribes abduct and enslave other tribes' warriors.", "On the eve of the Naadam, many strive to improve their fortunes—some by abducting and enslaving the warriors of other tribes."),
 ("M452e", 452, "Attackers left you no choice but to fight.", "Ah, there you are. As you can see, they left us little choice."),
 ("M452f", 452, "You reach the pass to Bardam's Mettle.", "Right. This must be the pass that leads to Bardam's Mettle."),
 # #453 In the Footsteps of Bardam the Brave
 ("M453a", 453, "To fight alongside the Mol, you must first be recognized as warriors of the Steppe.", "If you are to participate in the [[Naadam]] and fight alongside the [[Mol]], you must first be recognized as a warrior of the [[Azim Steppe|Steppe]]."),
 ("M453b", 453, "You tame a wild yol in Bardam's Mettle.", "At the end of a strange and bewildering journey through Bardam's Mettle, you manage to tame a wild yol in the traditional fashion."),
 ("M453c", 453, "Lyse completes her trial too, but Hien and Gosetsu have not emerged.", "[[Lyse]] emerges from the pass not long after you do, her trial also complete. However, there is still no sign of [[Hien]] or [[Gosetsu]]..."),
 ("M453d", 453, "You are now warriors of the Steppe.", "There can be no doubt: you are now warriors of the Steppe."),
 ("M453e", 453, "Bardam grants you the Steppe and everything in it.", "Yours is the Steppe and everything in it!"),
 # #454 The Children of Azim
 ("M454a", 454, "Hien and Gosetsu emerge, and Oronir surround you and take you to their khan.", "you find yourself surrounded by a party of Oronir, their leader demanding that you return with him to meet with his khan."),
 ("M454b", 454, "Magnai is leader of the Oronir and lord of the Dawn Throne.", "The most radiant brother Magnai, leader of the Oronir and lord of the Dawn Throne, recognizes you as warriors of the Steppe."),
 ("M454c", 454, "Magnai demands you acknowledge his supreme authority and pay tribute.", "He demands that you acknowledge his supreme authority and pay tribute"),
 ("M454d", 454, "Magnai says the Oronir are born of the Sun.", "Born of the Sun are Oronir, and born of the earth are you."),
 ("M454e", 454, "Magnai demands fealty to the Sun.", "Swear fealty to the Sun. Pledge to him your body and soul."),
 ("M454f", 454, "Baatu, who led your escort, will give you your duties.", "The details of the duties he would demand from you, however, shall be given by Baatu, the warrior who commanded your escort from Bardam's Mettle."),
 ("M454g", 454, "Hien sees a chance to learn of his foes and future allies.", "Hien considers this an opportunity to learn more of his foes and soon-to-be allies"),
 # #455 The Labors of Magnai
 ("M455a", 455, "Baatu says you will not die today, but will serve the Oronir cause.", "By the grace of our most radiant brother, you will not die this day, but instead be granted an opportunity to contribute to our cause."),
 ("M455b", 455, "Lyse is set to milk the Oronir's beasts.", "You, the red woman. You will milk our beasts."),
 ("M455c", 455, "You are to gather swordgrass from the bed of Azim Khaat.", "You are to dive into Azim Khaat, below the Dawn Throne, and gather swordgrass from the lakebed."),
 ("M455d", 455, "The swordgrass makes paralysis potions.", "Lest you wonder, we will use it to prepare potions to induce paralysis."),
 ("M455e", 455, "Hien asks how the Oronir can be children of Azim if they are Xaela born of Nhaama.", "How can Oronir be the children of Azim, if they are Xaela born of Nhaama?"),
 ("M455f", 455, "Magnai sends Hien to the elders to learn the truth of the world.", "Very well. I bid you speak with our elders and learn the truth of this world."),
 ("M455g", 455, "Gosetsu is set to repair arms and armor.", "We have arms and armor in need of repair."),
 # #456 For Love of the Moon
 ("M456a", 456, "Udutai says Azim and Nhaama were lovers.", "But what it does not mention is this: Azim and Nhaama were lovers."),
 ("M456b", 456, "Sun and moon must remain apart, lest creation end.", "Alas, he was of the sun and she of the moon. Apart they must remain, lest day and night cease to be, and with them all creation."),
 ("M456c", 456, "Azim's avatar was the first Oronir.", "Yea, he was the first Oronir. We are of his flesh and blood."),
 ("M456d", 456, "Udutai says the Xaela must be made to kneel.", "Xaela are not wont to kneel. They must be made to—only then will they heed reason."),
 ("M456e", 456, "Hien says the Oronir's arrogance comes from seeing themselves as caretakers of all Xaela.", "Their arrogance is rooted in the belief that they must act as caretakers of all Xaela."),
 ("M456f", 456, "Magnai requires one more thing before your freedom.", "However, if it is freedom you must desire, then there is one more thing you must do..."),
 ("M456g", 456, "Hien seeks the elder Udutai as a teacher.", "I met an elder—a storyteller—named Udutai. Mayhap he can be our teacher."),
 # #457 Sworn Enemies of the Sun
 ("M457a", 457, "As prisoners of the Oronir, you have been coerced into menial tribute.", "As prisoners of the tribe, you have been coerced into performing menial tasks as expressions of tribute."),
 ("M457b", 457, "For the next task, two will go and two will remain.", "For this task, two will go, and two will remain."),
 ("M457c", 457, "If the two flee or fall, the others will be enslaved.", "Should the two who embark upon this expedition choose to flee, or be captured or killed by the Dotharl, then the others will be taken as slaves and serve the Sun unto death."),
 ("M457d", 457, "Sadu is khatun of the Dotharl.", "Sadu, khatun of the Dotharl, who spares but a moment for her fallen kinsman before demanding to know who you are."),
 ("M457e", 457, "Sadu grants you leave to walk among the Dotharl.", "For your deeds, I grant you leave to walk among us."),
 ("M457f", 457, "Sadu scorns the Mol as little lambs.", "The Mol? The little lambs who wander to and fro at the behest of their gods?"),
 ("M457g", 457, "Hien and Lyse may not take part in scouting the Dotharl.", "it seems he and Lyse will not be allowed to take part in your next duty─to reconnoiter the encampment of the Dotharl."),
 ("M457h", 457, "You saved one hunter, but his comrade was beyond help.", "You reach the embattled Xaela and slay the beasts in time to save his life. Alas, as you suspected, it is too late for his comrade."),
 # #458 The Undying Ones
 ("M458a", 458, "Sadu says Geser will return.", "Geser was a great warrior. He will return to us in time."),
 ("M458b", 458, "The flesh rots, but the soul endures and returns.", "The flesh rots, but the soul endures. And ere the seasons have turned, so he shall return."),
 ("M458c", 458, "A returned warrior, glimpsed in a newborn's eyes, is given the same name.", "When he is glimpsed in the eyes of a newborn, he is blessed with the same name, that he may grow into a great warrior once more."),
 ("M458d", 458, "The Dotharl do not fear death.", "None are braver than the Dotharl, for we do not fear death."),
 ("M458e", 458, "Gosetsu sees the Dotharl are fewer.", "'tis plain to see that their numbers are inferior."),
 ("M458f", 458, "Gosetsu cannot ignore Sadu's callousness toward her kinsman.", "I cannot in good conscience ignore the callous disregard that woman showed for her kinsman!"),
 # #459 A Final Peace
 ("M459a", 459, "Sadu says the Dotharl need no tricks, only strength.", "Others rely on tricks and traps. Subterfuge. Lies. We have need of naught but our own strength."),
 ("M459b", 459, "The Dotharl kill many, and many of them are killed.", "While we kill many, many are killed in turn."),
 ("M459c", 459, "A warrior who dies before having children does not return.", "Yet one cannot return unless there is a vessel to inherit the soul, and if warriors die ere they birth children, then that is that."),
 ("M459d", 459, "Sadu offers that you fight for the Dotharl and live.", "Or you could fight for us and live."),
 ("M459e", 459, "Hien and Lyse are in prison.", "''Hien and Lyse are in prison.''"),
 ("M459f", 459, "Hien was still in his mother's womb when Doma fell twenty-five years ago.", "when my homeland fell twenty-five years past, I was still in my mother's womb."),
 ("M459g", 459, "Lyse means to seize the future she wants.", "I'm going to seize the future I want with my own two hands!"),
 ("M459h", 459, "Gosetsu finds the fallen hunter left for the vultures.", "Left for the vultures... It seems an insult to the man."),
 # #460 As the Gods Will
 ("M460a", 460, "Magnai says the Dotharl are not schemers and live only for war.", "The Dotharl are not schemers. They live only for war—for the contest of strength and will."),
 ("M460b", 460, "Magnai called the Steppe's women to see whether Nhaama looked back from their eyes.", "The most radiant brother called to him the women of the Steppe, that he might look into their eyes and see if Nhaama looked back."),
 ("M460c", 460, "Sadu gave great offense after the last Naadam.", "After the last Naadam, she gave great offense."),
 ("M460d", 460, "Magnai demands you swear to the law of the Steppe.", "Swear, here and now, to abide by the law of the Steppe."),
 ("M460e", 460, "You may return to the Mol to make ready.", "You may return to the Mol and make ready for the Naadam...on one condition."),
 ("M460f", 460, "Cirina and the Mol are waiting.", "Come, come—Cirina and the others are waiting!"),
 ("M460g", 460, "Magnai has the others fetched from their cells.", "Go and fetch the others from their cells."),
 # #461 Naadam
 ("M461a", 461, "The Naadam is the ceremonial battle for rule of the Steppe.", "The ceremonial battle for rulership over the [[Azim Steppe|Steppe]], or [[The Naadam|Naadam]], will commence with the rising of the sun"),
 ("M461b", 461, "You stand a khagan crowned.", "As the ovoo evaporates into motes of fading light, you stand a khagan crowned."),
 ("M461c", 461, "The Mol now claim the Dawn Throne.", "The Naadam is ended, and we Mol now claim the Dawn Throne."),
 ("M461d", 461, "Grynewaht arrives with an imperial squadron to kill you, but faces a united Steppe.", "for [[Grynewaht]] suddenly appears at the head of an imperial squadron, and declares his intention to kill you once and for all. Yet in coming a moment too late, he faces a Steppe united."),
 ("M461e", 461, "Hien convinces the Oronir and Dotharl to march south and fight for Doma.", "for [[Hien]] succeeds in convincing the two tribes to travel south with him and fight for [[Doma]]'s liberation."),
 ("M461f", 461, "Magnai pledges that the Sun will answer Hien's call.", "The Sun shall answer your call, Doman."),
 ("M461g", 461, "Hien hands Cirina command of the gathered forces.", "I have kept my promise, Cirina. They are yours to command."),
 ("M461h", 461, "Temulun says the Xaela were made for battle.", "We were made for battle—to kill and be killed."),
 ("M461i", 461, "With the Oronir and Dotharl, you slay the invaders and send Grynewaht off again.", "With the aid of the Oronir and the Dotharl, you slay the invaders and send Grynewaht on his way once more."),
 ("M461j", 461, "Sadu asks whether Hien would have the Dotharl fight his war for Doma.", "To Doma would you have us go, to fight your war and win your freedom?"),
 ("M461k", 461, "Hien and the Liberation Front are a step closer to freeing Doma.", "By your deeds are Lord Hien and the Doman Liberation Front one step closer to freeing their home from the yoke of imperial oppression."),
 # #462 Glory to the Khagan
 ("M462a", 462, "Temulun credits you with the Mol's victory and the safe return of all her kinsmen.", "Not only did you bring us victory in the Naadam, but you ensured that every one of my kinsmen returned with their lives."),
 ("M462b", 462, "None of the Mol were lost.", "Some were more gravely wounded than others, but none were lost to us."),
 ("M462c", 462, "You were declared khagan at the ovoo.", "As well as the moment when you became one with the ovoo and were declared khagan!"),
 ("M462d", 462, "Cirina and her grandmother discuss how to thank you.", "Grandmother and I have been discussing how we might express our gratitude to you."),
 ("M462e", 462, "Cirina gives you a morin khuur.", "This is a morin khuur—a traditional instrument of our people."),
 ("M462f", 462, "The Mol preserve their heroes' feats in song.", "The feats of our greatest heroes, like Bardam and Chakha, are preserved in song."),
 # #463 In Crimson They Walked
 ("M463a", 463, "Hien has his Xaela army and is ready to lead Doma to war.", "Lord Hien has his Xaela army, and is ready to return to Doma and lead his people to war against the Empire."),
 ("M463b", 463, "Magnai renews his vow to aid the Domans.", "Magnai renews his vow to render aid to the Domans without a second thought."),
 ("M463c", 463, "Magnai wonders whether Cirina is his long-sought moon.", "he then begins to muse aloud about whether or not Cirina could be his long-sought moon."),
 ("M463d", 463, "Cirina says Magnai is mistaken.", "I know not of what you speak, Brother Magnai, but I am certain you are mistaken."),
 ("M463e", 463, "Sadu reaffirms that the Dotharl will go to war for Hien.", "Sadu too does not hesitate to reiterate that the Dotharl will gladly go to war for Lord Hien"),
 ("M463f", 463, "The Dotharl sealed the southern passage with magicks during the Doman rebellion.", "The Dotharl sealed it with their magicks during the Doman rebellion, when more men in iron came from afar."),
 ("M463g", 463, "Geser's seed has quickened in his lover.", "Geser's seed has quickened in his lover."),
 ("M463h", 463, "Cirina gives Lyse a banner of the Mol.", "Wait, is this a banner of the Mol tribe?"),
 ("M463i", 463, "Magnai says you are not allies.", "We are not allies, traveler—far from it."),
 ("M463j", 463, "The Oronir yet occupy the Dawn Throne.", "The most radiant brother of the Oronir, who yet occupy the Dawn Throne, is to be first."),
 ("M463k", 463, "The long-sealed passage south is open.", "you resume your journey south towards a passage long sealed by the Dotharl's magicks, but no longer."),
 ("M463l", 463, "Cirina parts from you until you call the Mol to battle.", "It is here we must part ways, until the day you call us to battle."),
 # #464 The Hour of Reckoning
 ("M464a", 464, "Hien leads you to the House of the Fierce.", "Right, then. To the House of the Fierce. With me, my friends!"),
 ("M464b", 464, "Yugiri greets Hien; Gosetsu told them of your trials on the Steppe.", "Gosetsu told us of your trials and tribulations on the Steppe."),
 ("M464c", 464, "Hien meets Alphinaud and Alisaie, to whom he owes much.", "I am told we owe you much. It is a pleasure to meet you both."),
 ("M464d", 464, "The Xaela tribes have pledged their might to the cause.", "The Xaela tribes of the Azim Steppe have pledged their military might to the cause."),
 ("M464e", 464, "Alisaie secured the Confederacy and many Domans.", "We, meanwhile, have secured the support of the Confederacy, and a not insignificant number of your countrymen."),
 ("M464f", 464, "The Blue Kojin will fight if Hien agrees to trade terms after Doma is freed.", "The Blue Kojin, too, have expressed a willingness to join the fight—provided you agree to certain trade agreements following the liberation of Doma."),
 ("M464g", 464, "The shinobi will help, but Sui-no-Sato refused the call.", "The shinobi will render what aid they can. However, Sui-no-Sato refused to answer our call."),
 ("M464h", 464, "Zenos left Doma soon after you went to find Hien, for Gyr Abania.", "You should know that Zenos departed Doma not long after you left to find Lord Hien. We know not the reason why, but it would seem he was eager to return to Gyr Abania."),
 ("M464i", 464, "Yotsuyu remains acting viceroy, and Doma Castle's garrison is preparing a massive operation.", "Yotsuyu retains her position as acting viceroy, and we have reports that the garrison at Doma Castle is preparing for a massive operation..."),
 ("M464j", 464, "The Scions suspect a purge of Doma's remaining resistance.", "We suspect that the Empire's attempt to eliminate you on the Steppe may have been a prelude to a larger effort to purge the remaining pockets of resistance within Doma."),
 ("M464k", 464, "Hien rallies his people: twenty-five years of oppression end with them.", "Twenty-five years of oppression, of tyranny, of shame—it ends with us! We will prevail!"),
 ("M464l", 464, "Alphinaud and Alisaie have worked to restore the aetheryte.", "Alisaie and I have been hard at work attempting to restore the aetheryte here to its former glory"),
]
CLAIMS = {k: (claim, Q[q], loc) for k, q, claim, loc in _RAW}

# ---- New entities ------------------------------------------------------------------------------------------------------
ENTITIES = {
 "char-yotsuyu": "character", "char-grynewaht": "character", "char-soroban": "character", "char-tansui": "character",
 "char-rasho": "character", "char-bunchin": "character", "char-shiosai": "character", "char-susano": "character",
 "char-hien": "character", "char-kaien": "character", "char-isse": "character", "char-cirina": "character",
 "char-temulun": "character", "char-magnai": "character", "char-sadu": "character",
 "org-confederacy": "organization", "org-blue-kojin": "organization", "org-red-kojin": "organization",
 "org-raen": "organization", "org-doman-liberation-front": "organization", "org-mol": "organization",
 "org-oronir": "organization", "org-dotharl": "organization",
 "loc-isari": "location", "loc-yanxia": "location", "loc-namai": "location", "loc-house-of-the-fierce": "location",
 "loc-doma-castle": "location", "loc-azim-steppe": "location", "loc-dawn-throne": "location",
 # earlier eras' entities, repeated so this module lints on its own (the merge keeps the first definition)
 "char-gosetsu": "character", "char-yugiri": "character", "char-lyse": "character", "char-estinien": "character",
 "char-zenos": "character", "loc-doma": "location",
 "evt-a-bargain-with-the-confederacy": "event", "evt-the-kojin-treasures": "event", "evt-the-silence-of-yanxia": "event",
 "evt-lord-hien-on-the-steppe": "event", "evt-captives-of-the-oronir": "event", "evt-the-steppe-rides-south": "event",
}

# ---- Presentations ---------------------------------------------------------------------------------------------------
Y = "The imperial viceroy, whom Gosetsu calls the traitor who sold her homelands to the Garleans. "
YD = "The acting viceroy of Doma, named by Zenos to rule in his stead after he crushed the rebellion. "
G = "A Doman samurai, a former leader of the rebellion and a known fugitive. "
GK = "A Doman samurai, once Lord Kaien's retainer and a leader of the failed rebellion. "
H = "Lord Hien, young heir to Doma's throne. "
CF = "The pirates of the Ruby Sea, led by their captain, Rasho, from Onokoro. "
YU = "A shinobi of the Doman Liberation Front, born beneath the Ruby Sea, who serves Lord Hien. "

PRES = {
 # -- The viceroy's people
 "char-yotsuyu": [
   P(I419, None, "main", "Yotsuyu",
     "The imperial viceroy, holding court in Isari, a fishing village on Othard's coast under imperial occupation, with Grynewaht at her side. "
     "Gosetsu calls her the traitor who sold her homelands to the Garleans. Before your eyes she forced one villager to execute another, "
     "then had him shot for refusing to kill his own parents, and she took Gosetsu into custody when he surrendered.",
     ["M419b", "M419c", "M419g", "M419d", "M419e"]),
   P(I428, None, "main", "Yotsuyu",
     Y + "She holds Gosetsu in Isari's tavern and demands to know what became of Lord Hien, Doma's missing heir, whom she knows Gosetsu helped flee: "
     "the Garleans want the matter settled, living or dead. She mocks the late Lord Kaien as the leader of a fallen nation.",
     ["M419g", "M428e", "M428f", "M428h", "M428g"]),
   P(I433, None, "main", "Yotsuyu",
     Y + "She held Gosetsu and captive Confederates in Isari, swearing to find Lord Hien, but fled when the Confederacy attacked and her Kojin reinforcements never came. "
     "Rasho regrets letting her slip through his fingers.",
     ["M419g", "M432e", "M433a", "M433e"]),
   P(I434, None, "main", "Yotsuyu",
     YD + "She waged an indiscriminate campaign of terror on the villages, and though her purges ceased, their memory keeps the people in line. "
     "After Isari she rebuked the Red Kojin she had contracted for abandoning their posts, had them punished, and took one of their treasures, a katana.",
     ["M434b", "M434c", "M434d", "M434j", "M434f", "M434g"]),
   P(I436, None, "main", "Yotsuyu",
     YD + "Gosetsu says the secrets she sold helped Zenos crush the Doman Liberation Front, and the memory of her purges still keeps the villages cowed.",
     ["M434b", "M436f", "M434c", "M434d"]),
   P(I444, None, "main", "Yotsuyu",
     YD + "He says he chose her for her petty hatreds, the perfect instrument to bleed her kinsmen of hope and make an example of Doma, "
     "and warned that if she yields Doma to the rebels she will get no second chance. Told that an Eorzean is helping the rebels, she wants you dead.",
     ["M434b", "M444g", "M444h", "M444j"]),
   P(I464, None, "main", "Yotsuyu",
     YD + "Zenos has since left Doma, but she remains acting viceroy, and the garrison at Doma Castle is preparing for a massive operation, "
     "which the Scions suspect is meant to purge the last pockets of resistance.",
     ["M434b", "M464h", "M464i", "M464j"]),
 ],
 "char-grynewaht": [
   P(I419, None, "main", "Grynewaht",
     "An imperial officer you have beaten before, in Gyr Abania and at Carteneau. He is in occupied Isari at the side of Yotsuyu, the imperial viceroy.",
     ["M419c"]),
   P(I428, None, "main", "Grynewaht",
     "An imperial officer you have beaten before, in Gyr Abania and at Carteneau, now at Yotsuyu's side in occupied Isari. "
     "In the village tavern he beats the bound Gosetsu while she questions him.",
     ["M419c", "M428g"]),
   P(I433, None, "main", "Grynewaht",
     "Yotsuyu's bodyguard, an imperial officer you have beaten before. He brutally interrogated Gosetsu in Isari, boasting that the samurai was iron. "
     "Rasho calls him a half-wit, but a mean one on the battlefield.",
     ["M419c", "M432f", "M432i", "M433e"]),
   P(I434, None, "main", "Grynewaht",
     "Yotsuyu's bodyguard, an imperial officer you have beaten before, whose interrogation left Gosetsu injured. "
     "On her orders he defeated the Red Kojin who abandoned their posts and destroyed most of their treasure. "
     "He hopes Zenos will reinstate him, so he can settle unfinished business in Eorzea.",
     ["M432i", "M434e", "M434f", "M434h"]),
   P(I461, None, "main", "Grynewaht",
     "Yotsuyu's bodyguard, an imperial officer bent on returning to Eorzea and on killing you. At the end of the Naadam he arrived at the head of an imperial squadron to do it, "
     "but came a moment too late and faced a united Steppe, which sent him on his way once more.",
     ["M432i", "M434h", "M461d", "M461i"]),
 ],
 # -- The Ruby Sea
 "char-soroban": [
   P(I419, None, "main", "Soroban",
     "A Kojin of the Blue and a merchant, whom Gosetsu thanks as clever and industrious. Relieved that you will not judge his people for the deeds of the Red, "
     "he carried you across the sea to Othard's coast.",
     ["M419a", "M419j"]),
   P(I425, None, "main", "Soroban",
     "A Blue Kojin merchant who carried you to Othard. His people are traders with no pact with the Empire, and he welcomed you to Tamamizu, "
     "their village in a great bubble beneath the sea.",
     ["M419a", "M425b", "M425c", "M425f"]),
   P(I427, None, "main", "Soroban",
     "A Blue Kojin merchant of Tamamizu. His people want the sacred Yasakani-no-Magatama recovered before the Red find it, and his ritual lets you breathe and travel the depths "
     "to search for it, riding rays he summoned.",
     ["M425c", "M426f", "M427a", "M427b"]),
   P(I430, None, "main", "Soroban",
     "A Blue Kojin merchant of Tamamizu. He believes the Yasakani-no-Magatama chose you to bear it, and will tell the Confederacy to be ready to strike "
     "once your raid on the Kojin vault draws the Red from Isari.",
     ["M425c", "M430f", "M430e", "M430d"]),
 ],
 "char-tansui": [
   P(I420, None, "main", "Tansui",
     "A mate of the Confederacy, who brought you to its captain, Rasho. He reminds you that to join the Confederacy is to renounce every other tie, "
     "and that it did not rush to Doma's defense when the Empire invaded twenty-five years ago.",
     ["M420a", "M420c", "M420d"]),
   P(I433, None, "main", "Tansui",
     "A mate of the Confederacy and its captain's right hand. After the pirates freed Isari, he notes that the Empire believes they acted alone in retaliation for the viceroy's deeds, "
     "and expects its undivided attention for the foreseeable future.",
     ["M420a", "M433b", "M433c"]),
 ],
 "char-rasho": [
   P(I420, None, "main", "Rasho",
     "Captain and leader of the Confederacy. He knows Gosetsu as a former leader of Doma's rebellion, but refused to help free Isari: "
     "hate, he says, is a luxury the Confederacy cannot afford.",
     ["M420a", "M420b", "M420e"]),
   P(I424, None, "main", "Rasho",
     "Captain and leader of the Confederacy. Though Yotsuyu's Kojin catchers prey on his people, he will take no revenge until the enemy grows weaker, and waits for a sign. "
     "He accepted Alisaie's wager: if you deprive the Garleans of the Kojin, the Confederacy will help liberate Isari. He will weigh you by your deeds.",
     ["M420a", "M424b", "M424d", "M424f", "M424g"]),
   P(I432, None, "main", "Rasho",
     "Captain and leader of the Confederacy. When the Red Kojin rushed from their posts to defend their isle, he led his pirates against Isari to keep their bargain with the Eorzeans "
     "and remind the Garleans that the sea is theirs.",
     ["M420a", "M432h", "M432d", "M432k"]),
   P(I433, None, "main", "Rasho",
     "Captain and leader of the Confederacy. His pirates drove the imperials from Isari, though he regrets letting Yotsuyu slip through his fingers. "
     "Yanxia, he says, was the crucible of the rebellion, and suffered far worse at her hands.",
     ["M420a", "M433a", "M433e", "M433g"]),
 ],
 "org-confederacy": [
   P(I419, None, "main", "The Confederacy",
     "The pirates of the Ruby Sea. Their large settlement on the isle of Onokoro, complete with its own aetheryte, lies near Isari, a village the Empire occupies. "
     "Gosetsu sent you to them for aid, though there seems little chance they will answer.",
     ["M419b", "M419h", "M419i", "M419k"]),
   P(I420, None, "main", "The Confederacy",
     CF + "Members renounce every other tie, and the Confederacy is allied with none. It did not defend Doma when the Empire invaded twenty-five years ago, "
     "and Rasho refuses to fight the Empire over Isari.",
     ["M420a", "M420c", "M420d", "M420e"]),
   P(I424, None, "main", "The Confederacy",
     CF + "Kojin catchers working for Yotsuyu have been rounding up the Domans among them. Rasho accepted a wager from Alisaie: "
     "if you deprive the Garleans of their Kojin allies, the Confederacy will help liberate Isari.",
     ["M420a", "M424b", "M424c", "M424f"]),
   P(I432, None, "main", "The Confederacy",
     CF + "Keeping its bargain with the Eorzeans, it attacked Isari once the Red Kojin abandoned their posts.",
     ["M420a", "M432d", "M432h"]),
   P(I433, None, "main", "The Confederacy",
     CF + "It drove the imperials from Isari and rescued the fishermen and its kidnapped comrades. The Empire believes it acted alone, in retaliation for the viceroy's deeds, "
     "and it expects the Empire's undivided attention.",
     ["M420a", "M433a", "M433h", "M433b", "M433c"]),
   P(I464, None, "main", "The Confederacy",
     CF + "After it freed Isari, Alisaie and Alphinaud secured its support for Lord Hien's rising against the Empire.",
     ["M420a", "M433a", "M464e"]),
 ],
 "loc-isari": [
   P(I419, None, "main", "Isari",
     "A fishing village on Othard's coast, occupied by imperial forces, where the viceroy Yotsuyu holds court. Gosetsu is held in its tavern.",
     ["M419b", "M419c", "M419f"]),
   P(I433, None, "main", "Isari",
     "A fishing village on Othard's coast. The Confederacy drove out its imperial occupiers and rescued the captives held there.",
     ["M419b", "M433a", "M433h"]),
 ],
 "org-blue-kojin": [
   P(I419, None, "main", "The Blue Kojin",
     "Soroban's people, Kojin of the Blue. He hopes you will not judge them harshly for the deeds of the Red.",
     ["M419a"]),
   P(I425, None, "main", "The Blue Kojin",
     "Kojin traders who, unlike the Red, have made no pact with the Empire, and so may aid your cause. Their village, Tamamizu, lies in a great bubble beneath the sea.",
     ["M425b", "M425a", "M425c", "M425f"]),
   P(I426, None, "main", "The Blue Kojin",
     "Kojin traders of Tamamizu, beneath the sea, led by the elder Bunchin. They uphold the old ways, trading and valuing peace, while the Red live by the sword, "
     "and they want to recover the sacred Yasakani-no-Magatama before the Red do.",
     ["M426a", "M426b", "M426f", "M425c"]),
   P(I464, None, "main", "The Blue Kojin",
     "Kojin traders of Tamamizu, led by the elder Bunchin, who keep no pact with the Empire. They are willing to join the fight for Doma, provided Lord Hien agrees to certain trade agreements once Doma is free.",
     ["M426a", "M425b", "M464f"]),
 ],
 "org-red-kojin": [
   P(I424, None, "main", "The Red Kojin",
     "Kojin mercenaries who serve the Garleans. A rescued pirate calls them Yotsuyu's catchers: they have been chasing down Confederates and asking whether they are Doman. "
     "Alisaie has vowed to deprive the Garleans of them.",
     ["M424a", "M424b", "M424c", "M424e"]),
   P(I426, None, "main", "The Red Kojin",
     "Kojin who live by the sword and chose to join the Empire rather than fight it, serving as mercenaries and never speaking of their faith before their masters. "
     "Yotsuyu uses them to catch Domans. They seized the ship carrying the sacred Yasakani-no-Magatama, and the jewel was lost at sea.",
     ["M425a", "M426c", "M426g", "M424b", "M426e"]),
   P(I430, None, "main", "The Red Kojin",
     "Kojin mercenaries who serve the Empire and help hold Isari for it. They fiercely guard the Kojin vault on the Isle of Zekki, and an attack there would draw them from their posts.",
     ["M425a", "M430b", "M430c", "M430d"]),
   P(I431, None, "main", "The Red Kojin",
     "Kojin mercenaries who serve the Empire. In their vault on the Isle of Zekki, the treasures they have guarded for generations woke as the great kami Susano, "
     "whom their commander hailed.",
     ["M425a", "M431c", "M431d", "M431e"]),
   P(I432, None, "main", "The Red Kojin",
     "Kojin mercenaries of the Empire, who abandoned their posts at Isari to defend the Isle of Zekki. Their great kami, Susano, has been slain.",
     ["M425a", "M432h", "M432j"]),
   P(I434, None, "main", "The Red Kojin",
     "Kojin mercenaries Yotsuyu contracted, who abandoned their posts to defend their isle. She had Grynewaht defeat those she found and destroy most of their treasure, "
     "and took one of their treasures, a katana, for herself.",
     ["M434j", "M434f", "M434g"]),
 ],
 "char-bunchin": [
   P(I426, None, "main", "Bunchin",
     "The honored elder and leader of the Blue Kojin in Tamamizu. He told you that the Red chose to join the Empire, and the Blue want the sacred Yasakani-no-Magatama back before the Red find it.",
     ["M426a", "M426c", "M426f"]),
   P(I430, None, "main", "Bunchin",
     "The honored elder and leader of the Blue Kojin. He gave you a ceremonial knife to open the Kojin vault on the Isle of Zekki, where the Magatama's two siblings lie.",
     ["M426a", "M430a", "M430b"]),
 ],
 "org-raen": [
   P(I427, None, "main", "The Raen",
     "A reclusive people who live in Sui-no-Sato, a village beneath the sea, and may guide your search for the Yasakani-no-Magatama better than the Kojin can.",
     ["M426h", "M427b", "M427d"]),
   P(I428, None, "main", "The Raen",
     "The people of Sui-no-Sato, beneath the sea, who live under the Ruby Princess, sovereign of Shisui. When Doma fell twenty-five years ago she decreed they would take no part, "
     "and their high priest, Shiosai, will not let outsiders stay.",
     ["M428b", "M428c", "M428a", "M428d"]),
   P(I464, None, "main", "The Raen",
     "The people of Sui-no-Sato, beneath the sea, who live under the Ruby Princess and took no part when Doma fell. Sui-no-Sato has refused to answer the call to fight for Doma.",
     ["M428b", "M428c", "M464g"]),
 ],
 "char-shiosai": [
   P(I428, None, "main", "Shiosai",
     "High priest of Shisui of the Violet Tides, who speaks for the Raen of Sui-no-Sato. Bound by his people's will and by the Ruby Princess's decree to take no part in Doma's wars, "
     "he refused to let you stay.",
     ["M428a", "M428c", "M428d"]),
 ],
 "char-susano": [
   P(I431, None, "main", "Susano",
     "A great kami of the Kojin's sacred treasures, which the Red have guarded for generations. When you carried the Yasakani-no-Magatama into their vault on the Isle of Zekki, "
     "the treasures rose into the air, and Susano took form, rejoicing in revelry and marveling that you delivered the jewel to its enemy's vault.",
     ["M431b", "M431c", "M431d", "M431e", "M431g"]),
   P(I432, None, "main", "Susano",
     "A great kami, a primal by another name, summoned from the aether when the Kojin's treasures reacted to the Yasakani-no-Magatama. You slew it.",
     ["M432a", "M432b", "M432j"]),
 ],
 # -- Doma
 "char-hien": [
   P(I428, None, "main", "Hien",
     "Lord Hien, Doma's missing heir. Gosetsu helped him flee, and Yotsuyu, pressed by the Garleans to settle the matter, demands to know what became of him.",
     ["M428e", "M428f"], aliases=["Lord Hien"]),
   P(I436, None, "main", "Hien",
     "Lord Hien, son of Lord Kaien, who perished during Doma's rebellion. When defeat was certain Hien sent as many of his people to safety as he could, "
     "then fought on as his father's heir until a grievous wound left him missing. Yugiri has found him alive on the Azim Steppe: "
     "he will offer Doma his blade if it still thirsts for freedom, and otherwise his head to its conquerors, and asked her to learn the truth of its heart.",
     ["M436a", "M436b", "M436c", "M436d", "M436e"], aliases=["Lord Hien"]),
   P(I444, None, "main", "Hien",
     "Lord Hien, son of the late Lord Kaien and Doma's heir, alive on the Azim Steppe. He wanted proof that his people still want freedom, "
     "and Gosetsu says Namai's open defiance of Zenos is that proof. Yugiri has gone to bring him home.",
     ["M436a", "M436c", "M444f", "M444b"], aliases=["Lord Hien"]),
   P(I448, None, "main", "Hien",
     H + "Cirina found him near death in the southern mountains, and the Mol nursed him back to health; he has stayed to repay them. "
     "He greets you as a friend, but will not go home until he wins the Steppe's ceremonial battle and earns the right to lead the Xaela to Doma, "
     "for the Liberation Front's forces are depleted. His father ruled in name only for twenty-five years, and Hien dreams of a revolution against the most powerful empire in the world.",
     ["M448a", "M448b", "M448c", "M448d", "M448e", "M448g", "M448i"], aliases=["Lord Hien"]),
   P(I451, None, "main", "Hien",
     H + "Nursed back to health by the Mol, he means to win the Steppe's great ritual battle so the Xaela will follow him to Doma. "
     "He admits he should have fled when his father died rather than fight on, but his people called for the sword. Gosetsu still calls him by his childhood name, Shun.",
     ["M448c", "M448b", "M448d", "M451b", "M451c", "M451d"], aliases=["Lord Hien"]),
   P(I459, None, "main", "Hien",
     H + "He and Lyse are held in the Oronir's prison as hostages while you scout their rivals. Doma fell twenty-five years ago, he told her, while he was still in his mother's womb.",
     ["M448c", "M457b", "M459e", "M459f"], aliases=["Lord Hien"]),
   P(I461, None, "main", "Hien",
     H + "After you won the Naadam for the Mol, he persuaded the Oronir and the Dotharl to march south and fight for Doma's liberation, and placed the forces he gathered under Cirina's command.",
     ["M448c", "M461e", "M461f", "M461g"], aliases=["Lord Hien"]),
   P(I464, None, "main", "Hien",
     H + "He has returned to the House of the Fierce with the pledged might of the Xaela tribes, reunited with Yugiri and met Alphinaud and Alisaie, "
     "and rallied his people: twenty-five years of oppression, he vows, end with them.",
     ["M448c", "M464a", "M464b", "M464c", "M464d", "M464k"], aliases=["Lord Hien"]),
 ],
 "char-kaien": [
   P(I428, None, "main", "Kaien",
     "The late Lord Kaien, whom Yotsuyu mocks as the noble leader of a fallen nation.",
     ["M428h"], aliases=["Lord Kaien"]),
   P(I436, None, "main", "Kaien",
     "Lord Kaien, father of Lord Hien, who perished during Doma's rebellion. Gosetsu was his retainer.",
     ["M436a", "M435a"], aliases=["Lord Kaien"]),
   P(I448, None, "main", "Kaien",
     "Lord Kaien, father of Lord Hien, who perished during Doma's rebellion; Gosetsu was his retainer. For twenty-five years, Hien says, his father ruled Doma in name only.",
     ["M436a", "M435a", "M448g"], aliases=["Lord Kaien"]),
 ],
 "char-isse": [
   P(I435, None, "main", "Isse",
     "A young farmer of Namai. He named Gosetsu a notorious fugitive, blamed the rebels for the imperials' reprisals, and begged you to leave the village out of whatever Gosetsu is plotting.",
     ["M435a", "M435b", "M435e"]),
   P(I438, None, "main", "Isse",
     "A young farmer of Namai. His parents believed in the rebellion and left to fight for Lord Kaien; afterwards imperial soldiers beat the rebels' families in the village square, "
     "and one threatened his little sister. He will not report you, but wants you gone.",
     ["M438a", "M438b", "M438c", "M438f"]),
   P(I439, None, "main", "Isse",
     "A young farmer of Namai who wanted no part of the rebels. Imperial soldiers took him and other villagers away to serve the Garleans.",
     ["M435e", "M439a"]),
   P(I440, None, "main", "Isse",
     "A young farmer of Namai. You and Yugiri freed him and the other villagers from the castrum Fluminis, but he says they are lost and afraid, and can do nothing to change things.",
     ["M439e", "M440g", "M440c"]),
   P(I442, None, "main", "Isse",
     "A young farmer of Namai, freed from imperial forced labor. He overheard Yugiri plotting to kill the crown prince, and fears what will follow.",
     ["M440g", "M442f"]),
   P(I444, None, "main", "Isse",
     "A young farmer of Namai. After the ambush on Zenos he apologized for his earlier disdain, and asks you to come back so the village can finish what it started.",
     ["M444l", "M444k", "M444f"]),
 ],
 "org-doman-liberation-front": [
   P(I435, None, "main", "The Doman Liberation Front",
     "Doma's rebels, whose proud headquarters, the House of the Fierce, lies hidden behind a spring north of Namai. Gosetsu, a leader of the failed rebellion, led you there.",
     ["M435d", "M435f", "M435a"]),
   P(I436, None, "main", "The Doman Liberation Front",
     "Doma's rebels, headquartered at the House of the Fierce. Its people are few and their enemies legion: Zenos, aided by secrets Yotsuyu sold, crushed its hopes "
     "and made its last soldiers watch their comrades die, and its aetheryte has been disabled.",
     ["M435d", "M436i", "M436f", "M436k", "M436j"]),
   P(I444, None, "main", "The Doman Liberation Front",
     "Doma's rebels, headquartered at the House of the Fierce. With most imperial forces withdrawn from Doma, Alphinaud believes an uprising led by the Front could threaten Doma Castle.",
     ["M435d", "M444c", "M444d"]),
   P(I448, None, "main", "The Doman Liberation Front",
     "Doma's rebels, headquartered at the House of the Fierce, led by Lord Hien. Its forces are depleted, and Hien has sent Yugiri back to Yanxia to take charge of them before his homecoming.",
     ["M435d", "M448e", "M448h"]),
   P(I464, None, "main", "The Doman Liberation Front",
     "Doma's rebels, led by Lord Hien, who has returned to the House of the Fierce with the pledged might of the Xaela tribes. "
     "The Confederacy, many Domans and, on terms, the Blue Kojin have joined the cause.",
     ["M435d", "M464a", "M464d", "M464e", "M464f"]),
 ],
 "loc-house-of-the-fierce": [
   P(I435, None, "main", "The House of the Fierce",
     "Proud headquarters of the Doman Liberation Front in Yanxia, reached by a secret entrance through a small spring north of Namai.",
     ["M435d", "M435f"]),
   P(I464, None, "main", "The House of the Fierce",
     "Headquarters of the Doman Liberation Front, near Namai. Lord Hien has returned there to rally his people, and Alphinaud and Alisaie have been restoring its aetheryte.",
     ["M435d", "M464a", "M464l"]),
 ],
 "loc-yanxia": [
   P(I433, None, "main", "Yanxia",
     "A region of Doma that Rasho calls the crucible of the rebellion, where Yotsuyu did far worse than at Isari. Gosetsu has faith that his allies there yet live.",
     ["M433g", "M433f"]),
   P(I434, None, "main", "Yanxia",
     "A region of Doma, the crucible of the rebellion. Yotsuyu's purges of its villages have ceased, but their memory keeps the people in line, so there is little need for imperial patrols.",
     ["M433g", "M434c", "M434d"]),
 ],
 "loc-namai": [
   P(I434, None, "main", "Namai",
     "A humble farming village in Yanxia, where Gosetsu led you.",
     ["M434i"]),
   P(I439, None, "main", "Namai",
     "A farming village in Yanxia, still cowed by the imperials' reprisals. Soldiers marched in and took villagers, Isse among them, to serve the Garleans, "
     "calling it the answer to the Confederacy's attack on Isari.",
     ["M434i", "M438b", "M439a", "M439b"]),
   P(I444, None, "main", "Namai",
     "A farming village in Yanxia. After its people openly opposed Zenos, Isse vows they will finish what they started.",
     ["M434i", "M444f", "M444k"]),
 ],
 "loc-doma-castle": [
   P(I441, None, "main", "Doma Castle",
     "The castle of Doma, where an imperial airship carried Zenos, the crown prince.",
     ["M441h", "M441e"]),
   P(I444, None, "main", "Doma Castle",
     "The castle of Doma, seat of its provincial government. Alphinaud believes a popular uprising could threaten it.",
     ["M441h", "M444d"]),
   P(I464, None, "main", "Doma Castle",
     "The castle of Doma, seat of its provincial government and the target of Lord Hien's rising. Its garrison is preparing for a massive operation.",
     ["M444d", "M464i"]),
 ],
 # -- The Azim Steppe
 "loc-azim-steppe": [
   P(I436, None, "main", "The Azim Steppe",
     "The land where Yugiri found Lord Hien alive.",
     ["M436c"]),
   P(I445, None, "main", "The Azim Steppe",
     "Vast lands north of Isari, beyond a tunnel through the mountains, where Domans rarely venture. Xaela from all across the Steppe trade at Reunion, its marketplace.",
     ["M445e", "M445c", "M445f"]),
   P(I446, None, "main", "The Azim Steppe",
     "Lands north of Doma, unfit for men, whose thin soil and harsh weather the Empire has left alone. More than fifty Xaela tribes roam it, ranked through ritual combat, "
     "and they trade at Reunion.",
     ["M445c", "M446b", "M446a", "M445f"]),
   P(I447, None, "main", "The Azim Steppe",
     "Lands north of Doma where more than fifty Xaela tribes roam, ranked through ritual combat. The Oronir and the Dotharl are the strongest, "
     "and the tribe that wins the great ritual battle rules until the next Tsagaan Sar. Fighting in Reunion is punished with banishment.",
     ["M446a", "M447b", "M447d"]),
   P(I461, None, "main", "The Azim Steppe",
     "Lands north of Doma where more than fifty Xaela tribes roam. The Mol, fighting beside you, won the Naadam, the ceremonial battle for rule of the Steppe, and claim the Dawn Throne.",
     ["M446a", "M461a", "M461c"]),
 ],
 "char-cirina": [
   P(I446, None, "main", "Cirina",
     "A young woman of the Mol, found at Reunion's market. She knew at once that you seek Hien, but cannot leave until she has the kinsai she is bargaining for.",
     ["M446d", "M446e", "M446f"]),
   P(I447, None, "main", "Cirina",
     "A young woman of the Mol, a tribe she calls lambs among wolves. With her kinsai in hand, she explained the Steppe's tribes, and knows where Hien may be.",
     ["M446d", "M447a", "M447b", "M447e"]),
   P(I448, None, "main", "Cirina",
     "A young woman of the Mol. Guided by her grandmother's vision, she found Lord Hien near death in the southern mountains, and the Mol nursed him back to health.",
     ["M446d", "M448a", "M448b"]),
   P(I449, None, "main", "Cirina",
     "A young woman of the Mol, who found Lord Hien near death. She fears her people are too weak and few to win the great battle, "
     "and says you must first pass a trial to be recognized as Mol warriors.",
     ["M448a", "M449d", "M449g"]),
   P(I461, None, "main", "Cirina",
     "A young woman of the Mol, who found Lord Hien near death. After the Naadam, Hien placed the Xaela forces he had gathered under her command.",
     ["M448a", "M461g"]),
   P(I462, None, "main", "Cirina",
     "A young woman of the Mol, granddaughter of their khatun, who found Lord Hien near death. With her grandmother she thanked you, the new khagan, with a morin khuur.",
     ["M448a", "M462d", "M462e"]),
   P(I463, None, "main", "Cirina",
     "A young woman of the Mol, granddaughter of their khatun. Magnai wondered aloud whether she is his long-sought moon, and she told him he is mistaken. "
     "She gave Lyse a Mol banner as you parted for Doma, until the day you call the Mol to battle.",
     ["M462d", "M463c", "M463d", "M463h", "M463l"]),
 ],
 "org-mol": [
   P(I446, None, "main", "The Mol",
     "A Xaela tribe of the Azim Steppe. At Reunion, a Doman comes and goes with a Mol girl, Cirina.",
     ["M446c", "M446d"]),
   P(I447, None, "main", "The Mol",
     "A small Xaela tribe of the Azim Steppe, lambs among wolves, long content to live apart.",
     ["M446d", "M447a"]),
   P(I448, None, "main", "The Mol",
     "A small Xaela tribe of the Azim Steppe, lambs among wolves. They nursed Lord Hien back to health, and he has stayed to repay them.",
     ["M447a", "M448b"]),
   P(I449, None, "main", "The Mol",
     "A small Xaela tribe that hearkens to the whispers of the elder gods, led by their khatun, Temulun. She has invited you and Lord Hien to fight beside them in the great battle, "
     "though Cirina says they are weak and few.",
     ["M449h", "M449e", "M449d", "M448b"]),
   P(I461, None, "main", "The Mol",
     "A small Xaela tribe led by their khatun, Temulun. Fighting beside you, they won the Naadam, the ceremonial battle for rule of the Steppe, and claim the Dawn Throne.",
     ["M449e", "M461a", "M461c"]),
   P(I462, None, "main", "The Mol",
     "A small Xaela tribe led by their khatun, Temulun. They won the Naadam beside you and claim the Dawn Throne, and none of their warriors were lost.",
     ["M449e", "M461c", "M462a", "M462b"]),
 ],
 "char-temulun": [
   P(I449, None, "main", "Temulun",
     "Khatun of the Mol. She invited you and Lord Hien to fight beside her people in the great battle, saying the gods know you, and the stars shone at your coming.",
     ["M449e", "M449f"], aliases=["Temulun Khatun"]),
   P(I461, None, "main", "Temulun",
     "Khatun of the Mol. On the eve of the Naadam she reminded the young warriors that the Xaela were made for battle.",
     ["M449e", "M461h"], aliases=["Temulun Khatun"]),
   P(I462, None, "main", "Temulun",
     "Khatun of the Mol and Cirina's grandmother. She credits you with the Mol's victory in the Naadam, and with bringing every one of her kinsmen home alive.",
     ["M449e", "M462d", "M462a", "M462b"], aliases=["Temulun Khatun"]),
 ],
 "org-oronir": [
   P(I447, None, "main", "The Oronir",
     "One of the two strongest Xaela tribes of the Azim Steppe, with the Dotharl.",
     ["M447b"]),
   P(I454, None, "main", "The Oronir",
     "One of the strongest Xaela tribes, led by Magnai from the Dawn Throne. They hold that they are born of the Sun, and have taken your party to pay them tribute.",
     ["M447b", "M454b", "M454d", "M454c"]),
   P(I456, None, "main", "The Oronir",
     "One of the strongest Xaela tribes, led by Magnai from the Dawn Throne. Their elder Udutai says Azim himself came down as the first Oronir, "
     "and that the Xaela must be made to kneel; Hien sees in them would-be caretakers of all Xaela.",
     ["M454b", "M456c", "M456d", "M456e"]),
   P(I461, None, "main", "The Oronir",
     "One of the strongest Xaela tribes, led by Magnai. Defeated in the Naadam, they answered Lord Hien's call to fight for Doma.",
     ["M454b", "M461e", "M461f"]),
   P(I463, None, "main", "The Oronir",
     "One of the strongest Xaela tribes, led by Magnai, who still occupy the Dawn Throne. Magnai has renewed his vow to aid the Domans.",
     ["M454b", "M463j", "M463b"]),
 ],
 "char-magnai": [
   P(I454, None, "main", "Magnai",
     "The most radiant brother, leader of the Oronir and lord of the Dawn Throne. Holding that the Oronir are born of the Sun, he demands tribute and fealty from your party, "
     "and Baatu, who led your escort, will set your tasks.",
     ["M454b", "M454d", "M454c", "M454e", "M454f"]),
   P(I456, None, "main", "Magnai",
     "The most radiant brother, leader of the Oronir and lord of the Dawn Throne, who holds your party to labor as tribute. He sent Hien to the elders to learn the truth of the world, "
     "and demands one more task before your freedom.",
     ["M454b", "M455f", "M456f"]),
   P(I457, None, "main", "Magnai",
     "The most radiant brother, leader of the Oronir. He sent you and Gosetsu to scout the Dotharl, warning that the hostages left behind will be enslaved if you flee or fall.",
     ["M454b", "M457b", "M457c"]),
   P(I460, None, "main", "Magnai",
     "The most radiant brother, leader of the Oronir. He freed your party once you swore to abide by the law of the Steppe, and let you return to the Mol. "
     "Baatu says he once called the women of the Steppe to look into their eyes for Nhaama.",
     ["M454b", "M460d", "M460e", "M460g", "M460b"]),
   P(I461, None, "main", "Magnai",
     "The most radiant brother, leader of the Oronir. Defeated in the Naadam, he pledged that the Sun will answer Lord Hien's call.",
     ["M454b", "M461f", "M461e"]),
   P(I463, None, "main", "Magnai",
     "The most radiant brother, leader of the Oronir. He renewed his vow to aid the Domans, while insisting you are not allies, and wondered aloud whether Cirina is his long-sought moon.",
     ["M454b", "M463b", "M463i", "M463c"]),
 ],
 "loc-dawn-throne": [
   P(I454, None, "main", "The Dawn Throne",
     "Seat of Magnai, leader of the Oronir, on the Azim Steppe.",
     ["M454b"]),
   P(I461, None, "main", "The Dawn Throne",
     "Seat of the Oronir and their leader Magnai. After winning the Naadam, the Mol claim it.",
     ["M454b", "M461c"]),
   P(I463, None, "main", "The Dawn Throne",
     "Seat of the Oronir, claimed by the Mol after the Naadam. The Oronir still occupy it.",
     ["M461c", "M463j"]),
 ],
 "org-dotharl": [
   P(I447, None, "main", "The Dotharl",
     "One of the two strongest Xaela tribes of the Azim Steppe, with the Oronir.",
     ["M447b"]),
   P(I457, None, "main", "The Dotharl",
     "One of the strongest Xaela tribes, led by their khatun, Sadu, who scorns the Mol as little lambs. For saving one of their hunters, she let you walk among them.",
     ["M447b", "M457d", "M457f", "M457e"]),
   P(I458, None, "main", "The Dotharl",
     "One of the strongest Xaela tribes, led by Sadu. They do not fear death: a fallen warrior's soul returns, glimpsed in the eyes of a newborn who is given his name. "
     "Gosetsu judges them formidable but fewer than the Oronir.",
     ["M457d", "M458b", "M458c", "M458d", "M458e"]),
   P(I459, None, "main", "The Dotharl",
     "A Xaela tribe led by Sadu that does not fear death, believing its fallen return in newborns. They need no tricks, only strength, and are few because they kill many and many are killed; "
     "a warrior who dies before having children does not return.",
     ["M457d", "M458c", "M459a", "M459b", "M459c"]),
   P(I461, None, "main", "The Dotharl",
     "A Xaela tribe led by Sadu that does not fear death. After the Naadam, they agreed to fight for Doma.",
     ["M457d", "M458d", "M461e", "M461j"]),
   P(I463, None, "main", "The Dotharl",
     "A Xaela tribe led by Sadu that does not fear death. They will gladly go to war for Lord Hien, and have opened the southern pass they sealed with magicks during the Doman rebellion.",
     ["M457d", "M463e", "M463f", "M463k"]),
 ],
 "char-sadu": [
   P(I457, None, "main", "Sadu",
     "Khatun of the Dotharl. She spared her fallen kinsman only a moment, scorns the Mol as little lambs, and let you walk among her people for saving a hunter's life.",
     ["M457d", "M457f", "M457e", "M457h"], aliases=["Sadu Khatun"]),
   P(I458, None, "main", "Sadu",
     "Khatun of the Dotharl. She says the fallen hunter, Geser, will return in a newborn who takes his name, for her people do not fear death.",
     ["M457d", "M458a", "M458c", "M458d"], aliases=["Sadu Khatun"]),
   P(I459, None, "main", "Sadu",
     "Khatun of the Dotharl, whose people rely on strength alone. She told you to go back to the Mol, or fight for the Dotharl and live.",
     ["M457d", "M459a", "M459d"], aliases=["Sadu Khatun"]),
   P(I461, None, "main", "Sadu",
     "Khatun of the Dotharl. Defeated in the Naadam, she agreed that her people will go to Doma and fight Lord Hien's war.",
     ["M457d", "M461j", "M461e"], aliases=["Sadu Khatun"]),
   P(I463, None, "main", "Sadu",
     "Khatun of the Dotharl. She promises Lord Hien that the Dotharl will gladly go to war for him, told you Geser's seed has quickened in his lover, and unsealed the southern pass.",
     ["M457d", "M463e", "M463g", "M463f", "M463k"], aliases=["Sadu Khatun"]),
 ],
 # -- Continuing entities
 "char-gosetsu": [
   P(I419, None, "main", "Gosetsu",
     G + "In occupied Isari he denounced the viceroy Yotsuyu as a traitor and surrendered himself to her, buying you time to plan his rescue, "
     "and was led away into the village tavern. He sent you to seek aid at the tower to the northeast.",
     ["M419l", "M419g", "M419e", "M419f", "M419i"]),
   P(I428, None, "main", "Gosetsu",
     G + "Held in Isari's tavern, he was beaten by Grynewaht while Yotsuyu demanded to know what became of Lord Hien, whom he helped flee; the details, he says, escape him.",
     ["M419l", "M428g", "M428f", "M428i"]),
   P(I433, None, "main", "Gosetsu",
     G + "The Confederacy freed him and the other captives from Isari after Grynewaht's brutal interrogation. He has faith his allies in Yanxia yet live, "
     "and will plan the next step once he finds them.",
     ["M419l", "M432f", "M433d", "M433f"]),
   P(I435, None, "main", "Gosetsu",
     GK + "Namai's people fear the Empire's reprisals and want him gone, but he cannot leave things as they are, and led you to the House of the Fierce, headquarters of the Doman Liberation Front.",
     ["M435a", "M435b", "M435c", "M435d"]),
   P(I441, None, "main", "Gosetsu",
     GK + "He served Lord Kaien and his son in the Liberation Front alongside Yugiri. He warned her that killing Zenos would not win Doma its freedom, more likely its doom, "
     "and she went ahead regardless.",
     ["M435a", "M441b", "M441f", "M441g"]),
   P(I443, None, "main", "Gosetsu",
     GK + "With Alisaie and armed villagers, sent by Alphinaud, he stood over Yugiri when Zenos had felled her, until Zenos withdrew.",
     ["M435a", "M443e", "M443g", "M443f"]),
   P(I444, None, "main", "Gosetsu",
     GK + "He says Lord Hien wanted proof of his people's conviction, and Namai's open defiance of Zenos has provided it.",
     ["M435a", "M444f"]),
   P(I451, None, "main", "Gosetsu",
     GK + "He stays at Lord Hien's side on the Steppe, still calls him by his childhood name, Shun, and is in no hurry to meet his ancestors while he has amends to make.",
     ["M435a", "M448h", "M451d", "M451e"]),
   P(I458, None, "main", "Gosetsu",
     GK + "He scouted the Dotharl with you while Lord Hien and Lyse are held hostage by the Oronir, was outraged by Sadu's disregard for a fallen kinsman, "
     "and judges the Dotharl formidable but few.",
     ["M435a", "M457b", "M458f", "M458e"]),
   P(I464, None, "main", "Gosetsu",
     GK + "He has returned with Lord Hien to the House of the Fierce, having told Yugiri of your trials on the Steppe.",
     ["M435a", "M464a", "M464b"]),
 ],
 "char-yugiri": [
   P(I429, None, "main", "Yugiri",
     "A Doman shinobi who has aided the Scions, and whom you are looking for in Othard. In Sui-no-Sato, a village beneath the Ruby Sea, Ihanami and Yunagi told you their daughter Yugiri "
     "went to Doma as a child, was forbidden to return by the Ruby Princess of the day, and fought in the rebellion; they have heard nothing since, and asked you to tell her they think of her every day.",
     ["M429g", "M429c", "M429b", "M429a", "M429f"]),
   P(I436, None, "main", "Yugiri",
     "A shinobi of the Doman Liberation Front, whom you found at the House of the Fierce. She has found Lord Hien alive on the Azim Steppe, and he bade her learn the truth of Doma's heart and return.",
     ["M435d", "M436c", "M436e"]),
   P(I441, None, "main", "Yugiri",
     YU + "She learned the shinobi's secrets to protect her home and was sent to assist the Liberation Front, where she met Lord Kaien, his son and Gosetsu. "
     "When Zenos came to Doma, she resolved to kill him despite Gosetsu's warning.",
     ["M441a", "M441i", "M441b", "M441g", "M441f"]),
   P(I443, None, "main", "Yugiri",
     YU + "Her ambush of Zenos failed: his new katana's crimson energy felled her, and only the armed villagers, Gosetsu and Alisaie, sent by Alphinaud, saved her life.",
     ["M441a", "M436e", "M443b", "M443e", "M443g"]),
   P(I444, None, "main", "Yugiri",
     YU + "She apologized for her rash pursuit of Zenos, and has set out for the Azim Steppe to bring Lord Hien home.",
     ["M441a", "M436e", "M444a", "M444b"]),
   P(I448, None, "main", "Yugiri",
     YU + "She brought you to Lord Hien on the Steppe, and he has sent her back to Yanxia to take charge of the Liberation Front's forces for his homecoming.",
     ["M441a", "M448f", "M448h"]),
   P(I464, None, "main", "Yugiri",
     YU + "She welcomed Lord Hien home to the House of the Fierce. The shinobi will give what aid they can, though Sui-no-Sato refused to answer the call.",
     ["M441a", "M464b", "M464g"]),
 ],
 "char-lyse": [
   P(I419, None, "main", "Lyse",
     "A Scion traveling with you and Alisaie to Othard. When Gosetsu surrendered to the viceroy at Isari, she swam with Alisaie for the Confederacy's settlement on Onokoro.",
     ["M419o", "M419e", "M419h"]),
   P(I425, None, "main", "Lyse",
     "A Scion traveling with you and Alisaie in the Far East. She confided that her sister Yda and their father had a way with words that inspired people, "
     "and fears she has none of it.",
     ["M419o", "M425d", "M425e"]),
   P(I432, None, "main", "Lyse",
     "A Scion fighting for her homeland. When Alisaie stayed behind on the Isle of Zekki to hold off the Red Kojin, Lyse meant to go back for her, and found her safe right behind her.",
     ["M427c", "M432c", "M432g", "M432l"]),
   P(I453, None, "main", "Lyse",
     "A Scion fighting for her homeland, now at Lord Hien's side on the Azim Steppe. She completed Bardam's trial and is a warrior of the Steppe.",
     ["M427c", "M453c", "M453d"]),
   P(I459, None, "main", "Lyse",
     "A Scion fighting for her homeland, and a warrior of the Steppe. Held hostage in the Oronir's prison with Lord Hien, she vowed to seize the future she wants with her own two hands.",
     ["M453d", "M459e", "M459g"]),
   P(I463, None, "main", "Lyse",
     "A Scion fighting for her homeland, and a warrior of the Steppe who has vowed to seize the future she wants. As you parted from the Mol for Doma, Cirina gave her a Mol banner.",
     ["M453d", "M459g", "M463h"]),
 ],
 "char-alisaie": [
   P(I419, None, "main", "Alisaie",
     "A Scion traveling with you and Lyse to Othard. In occupied Isari she could not stop Gosetsu from surrendering, and led the way to the Confederacy's settlement on Onokoro.",
     ["M419m", "M419e", "M419h"]),
   P(I424, None, "main", "Alisaie",
     "A Scion in the Far East. She made Rasho a wager: you will deprive the Garleans of their Kojin allies, and if you succeed, the Confederacy will help liberate Isari.",
     ["M424e", "M424f"]),
   P(I432, None, "main", "Alisaie",
     "A Scion in the Far East. On the Isle of Zekki she held back the Red Kojin so you and Lyse could escape, then made it out herself.",
     ["M424e", "M432c", "M432l"]),
   P(I443, None, "main", "Alisaie",
     "A Scion in Doma. With Gosetsu and armed villagers, sent by Alphinaud, she stood ready to save Yugiri after Zenos felled her.",
     ["M443e", "M443g"]),
   P(I464, None, "main", "Alisaie",
     "A Scion in Doma. With Alphinaud she has secured the Confederacy, many Domans and, on trade terms, the Blue Kojin for Lord Hien's rising, "
     "and she suspects Doma Castle's garrison is preparing a purge of the remaining resistance.",
     ["M464e", "M464f", "M464i", "M464j"]),
 ],
 "char-alphinaud": [
   P(I443, None, "main", "Alphinaud",
     "A young Scion. When you and Yugiri ambushed Zenos, he convinced the others to rush to your defense, and so saved Yugiri's life.",
     ["M443g"]),
   P(I444, None, "main", "Alphinaud",
     "A young Scion in Doma. With Tataru and Hancock's intelligence that the Empire has withdrawn most of its forces from Doma, and no aid to be had from the Alliance, "
     "he plans a popular uprising led by the Doman Liberation Front to threaten Doma Castle.",
     ["M444c", "M444e", "M444d"]),
   P(I464, None, "main", "Alphinaud",
     "A young Scion in Doma. He reports that Zenos left Doma for Gyr Abania soon after you went to find Lord Hien, and he and Alisaie have been restoring the aetheryte at the House of the Fierce.",
     ["M444d", "M464h", "M464l"]),
 ],
 "char-tataru": [
   P(I444, None, "main", "Tataru",
     "The Scions' receptionist. With Hancock she has gathered intelligence that the Empire withdrew most of its forces from Doma in the past year.",
     ["M444c"]),
 ],
 "char-estinien": [
   P(I444, None, "main", "Estinien",
     "Freed from Nidhogg, he swore to leave his old life behind once the wyrm's shade was banished. Now, in Gyr Abania, he has found a great and mysterious crater.",
     ["M444m", "M444i"]),
 ],
 "char-zenos": [
   P(I434, None, "main", "Zenos",
     "An imperial lord who crushed Doma's rebellion, then had no wish to remain and named Yotsuyu to serve in his stead. Grynewaht hopes Lord Zenos will reinstate him.",
     ["M434b", "M434h"], aliases=["The Viceroy"]),
   P(I436, None, "main", "Zenos",
     "An imperial lord who crushed Doma's rebellion with the secrets Yotsuyu sold, then left her to rule. He made the Liberation Front's last soldiers watch their comrades die, "
     "desiring hate rather than obedience, and has wielded Far Eastern blades ever since he took a fallen samurai's sword.",
     ["M434b", "M436f", "M436k", "M436g", "M436h"], aliases=["The Viceroy"]),
   P(I441, None, "main", "Zenos",
     "The crown prince, who crushed Doma's rebellion and remains its anointed viceroy, though Yotsuyu governs in his stead. He defeated the Alliance, the Resistance and the Scions "
     "at Rhalgr's Reach, and an imperial airship has brought him to Doma Castle.",
     ["M441e", "M441c", "M434b", "M441d", "M441j", "M441h"], aliases=["The Viceroy"]),
   P(I443, None, "main", "Zenos",
     "The crown prince and Doma's anointed viceroy. When you and Yugiri ambushed him, a new katana's crimson energy felled you both; he recognized you as the champion of the savages he had faced before, "
     "urged you to live and grow stronger to face him again, and withdrew. He says the Empire sowed hatred and fear in the Domans to train them as beasts.",
     ["M441e", "M441c", "M443b", "M443c", "M443d", "M443f", "M443h"], aliases=["The Viceroy"]),
   P(I444, None, "main", "Zenos",
     "The crown prince and Doma's anointed viceroy, who chose Yotsuyu for her petty hatreds to bleed her kinsmen of hope. He warned her that if she yields Doma to the rebels, "
     "she will get no second chance.",
     ["M441e", "M441c", "M444g", "M444h"], aliases=["The Viceroy"]),
   P(I464, None, "main", "Zenos",
     "The crown prince and Doma's anointed viceroy. He left Doma not long after you went to find Lord Hien, seemingly eager to return to Gyr Abania.",
     ["M441e", "M441c", "M464h"], aliases=["The Viceroy"]),
 ],
 "loc-doma": [
   P(I419, None, "main", "Doma",
     "An eastern nation under the Empire. Its viceroy, Yotsuyu, holds court in one of its fishing villages, and Gosetsu calls her the traitor who sold her homelands to the Garleans.",
     ["M419n", "M419c", "M419g"]),
   P(I434, None, "main", "Doma",
     "An eastern nation that the Empire invaded twenty-five years ago. Zenos crushed its latest rebellion and named Yotsuyu, as acting viceroy, to rule in his stead; "
     "her purges have ceased, but their memory keeps its people in line.",
     ["M420d", "M434b", "M434c", "M434d"]),
   P(I464, None, "main", "Doma",
     "An eastern nation under imperial rule for twenty-five years, governed by the acting viceroy Yotsuyu. Lord Hien has returned with a Xaela army to free it, "
     "and the garrison at Doma Castle is preparing for a massive operation.",
     ["M420d", "M464i", "M464d", "M464k"]),
 ],
}

# ---- Arc recaps ---------------------------------------------------------------------------------------------------------
N1, N2, N3 = "A Bargain with the Confederacy", "The Kojin Treasures", "The Silence of Yanxia"
N4, N5, N6 = "Lord Hien on the Steppe", "Captives of the Oronir", "The Steppe Rides South"
L1 = "Yotsuyu holds Gosetsu prisoner in Isari, a village the Empire occupies, and you seek help from the Confederacy on Onokoro. "
L2 = "To win the Confederacy's help in freeing Isari, where Yotsuyu holds Gosetsu, you wagered to deprive the Garleans of their Kojin allies. "
L3 = "In Yanxia, where memories of Yotsuyu's purges keep the people cowed, Gosetsu is seeking his allies. "
L4 = "Lord Hien, alive on the Azim Steppe, will lead Doma again only if its people still want freedom. "
L5 = "Zenos, the crown prince and Doma's anointed viceroy, has come to Doma, and Yugiri means to kill him though Gosetsu warns it will doom Doma. "
L6 = "You crossed to the Azim Steppe with Yugiri, Lyse and Gosetsu to bring Lord Hien home to lead Doma's rebellion. "
L7 = "Lord Hien means to win the Steppe's great ritual battle beside the Mol, so that the Xaela will follow him to Doma. "
L8 = "Magnai, leader of the Oronir, holds your party at the Dawn Throne and demands tribute. "

PRES.update({
 "evt-a-bargain-with-the-confederacy": [
   P(I419, None, "main", N1,
     "Soroban, a Blue Kojin, carried you to Othard's coast. In Isari, occupied by imperial forces, the viceroy Yotsuyu forced one villager to execute another, "
     "and Gosetsu, who calls her a traitor to her homeland, surrendered to her so you could plan his rescue. On his advice, Alisaie and Lyse led you to Onokoro, a large settlement held by the Confederacy.",
     ["M419a", "M419b", "M419c", "M419d", "M419g", "M419e", "M419h"]),
   P(I420, None, "main", N1,
     L1 + "Its captain, Rasho, knows Gosetsu as a former leader of the rebellion, but refused: the Confederacy renounces every tie, did not defend Doma when the Empire invaded, "
     "and cannot afford hatred. Alisaie means to earn its trust by helping its people.",
     ["M419e", "M419h", "M420a", "M420b", "M420c", "M420d", "M420e", "M420f"]),
   P(I421, None, "main", N1,
     L1 + "Working among the pirates, you carried medicine to a seasick Doman recruit for Afumi, who says their captain was once of Doma and cast everything aside "
     "when the imperials took his lands and family.",
     ["M419e", "M419h", "M421b", "M421a"]),
   P(I421B, None, "main", N1,
     L1 + "Working among the pirates, you recovered arrows and meat from a gyuki carcass for Kajika, who says hard times force them to hunt such game and reuse every arrow.",
     ["M419e", "M419h", "M421bc", "M421ba", "M421bb"]),
   P(I421C, None, "main", N1,
     L1 + "Working among the pirates, you found a recruit Aranami thought had shirked his patrol, keeping vigil for a comrade who died hunting deadly game, and Aranami admitted he judged too quickly.",
     ["M419e", "M419h", "M421ca", "M421cb", "M421cc"]),
   P(I424, None, "main", N1,
     "Yotsuyu holds Gosetsu prisoner in Isari. Rescuing missing pirates, you learned that Kojin mercenaries, Yotsuyu's catchers, are rounding up Domans among the Confederates, "
     "yet Rasho will wait for a sign before taking revenge. Alisaie offered a wager: if you deprive the Garleans of the Kojin, the Confederacy will help liberate Isari. Rasho will judge you by deeds.",
     ["M419e", "M424a", "M424b", "M424c", "M424d", "M424e", "M424f", "M424g"]),
   P(I425, None, "main", N1,
     L2 + "Rasho explained that the Red Kojin serve the Empire, while the Blue are traders with no pact. On the way, Lyse confided she doubts she can inspire people as Yda and her father did, "
     "and Soroban welcomed you to Tamamizu, the Blue Kojin village beneath the sea.",
     ["M419e", "M424e", "M424f", "M425a", "M425b", "M425d", "M425e", "M425c"]),
   P(I426, None, "main", N1,
     L2 + "In Tamamizu, Bunchin, leader of the Blue Kojin, said the Red chose to join the Empire. The Blue want back a sacred jewel, the Yasakani-no-Magatama, "
     "which Hingashi gave the Garleans and which was lost at sea when the Red seized the ship carrying it.",
     ["M419e", "M424e", "M424f", "M426a", "M426c", "M426d", "M426e", "M426f"]),
   P(I427, None, "main", N1,
     L2 + "Soroban's ritual lets you breathe and travel beneath the waves to search for the Yasakani-no-Magatama, a sacred jewel the Blue Kojin want back before the Red find it. "
     "Riding rays he summoned, you set out for Sui-no-Sato, a village of a reclusive people.",
     ["M419e", "M424e", "M426f", "M427a", "M427b", "M427d"]),
   P(I428, None, "main", N1,
     L2 + "At Sui-no-Sato, Shiosai, high priest of the Raen, refused to let you stay, for when Doma fell the Ruby Princess decreed they would take no part. "
     "In Isari's tavern, Grynewaht beat the bound Gosetsu while Yotsuyu demanded to know what became of Lord Hien, Doma's missing heir.",
     ["M419e", "M424e", "M428a", "M428c", "M428d", "M428g", "M428e", "M428f"]),
 ],
 "evt-the-kojin-treasures": [
   P(I429, None, "main", N2,
     "To win the Confederacy's help in freeing Isari, you wagered to deprive the Empire of its Red Kojin allies. Searching for the sacred jewel the Blue Kojin seek, "
     "you met Yugiri's parents in Sui-no-Sato, who have had no word of her since she fought in Doma's rebellion. Their lamps led you to the Yasakani-no-Magatama in a sunken ship.",
     ["M424e", "M424f", "M426f", "M429a", "M429d", "M429e"]),
   P(I430, None, "main", N2,
     "You found the Yasakani-no-Magatama, a sacred Kojin jewel, while seeking a way to draw the Red Kojin away from the imperial garrison in Isari. "
     "Bunchin gave you a knife to open the Kojin vault on the Isle of Zekki, which holds the jewel's two siblings: an attack there would pull the Red from their posts. "
     "Soroban will ready the Confederacy to strike.",
     ["M429e", "M430a", "M430b", "M430c", "M430d", "M430e"]),
   P(I431, None, "main", N2,
     "To draw the Red Kojin away from Isari, you broke into their vault on the Isle of Zekki carrying the Yasakani-no-Magatama. In the Pool of Tribute the three treasures rose "
     "and woke a great kami the Red have guarded for generations. It named itself Susano, and Alisaie vowed to defeat the primal.",
     ["M430c", "M430d", "M431a", "M431b", "M431c", "M431d", "M431e", "M431f"]),
   P(I432, None, "main", N2,
     "You slew Susano, a primal woken from the Kojin treasures, and Alisaie held back the Red Kojin so you and Lyse could escape; Lyse turned back for her, only to find her safe. "
     "The Red abandoned their posts to defend their isle, and Rasho led the Confederacy against Isari to keep his bargain, while Yotsuyu, interrogating Gosetsu, swore to find Lord Hien.",
     ["M432a", "M432b", "M432c", "M432g", "M432l", "M432h", "M432d", "M432e"]),
   P(I433, None, "main", N2,
     "The Confederacy freed Isari: the imperials fled when their Red Kojin reinforcements never came, and Gosetsu and the captives are alive. "
     "The Empire believes the Confederacy acted alone and will turn its attention on it, and Rasho regrets letting Yotsuyu escape. Gosetsu means to find his allies in Yanxia, the crucible of the rebellion.",
     ["M433a", "M433d", "M433b", "M433c", "M433e", "M433f", "M433g"]),
 ],
 "evt-the-silence-of-yanxia": [
   P(I434, None, "main", N3,
     "With Isari freed, Gosetsu, still hurt from Grynewaht's interrogation, led you into Yanxia. After crushing Doma's rebellion, Zenos left and named Yotsuyu to rule in his stead, "
     "and her purges of the villages ended long ago, but their memory keeps the people in line. Elsewhere, Grynewaht defeated the Red Kojin who abandoned their posts.",
     ["M434a", "M434e", "M434b", "M434c", "M434d", "M434f"]),
   P(I435, None, "main", N3,
     L3 + "At Namai, the young farmer Isse named Gosetsu a fugitive and blamed the rebels for the imperials' reprisals, begging you to leave the village be. "
     "Gosetsu would not let things stand, and led you to the House of the Fierce, headquarters of the Doman Liberation Front.",
     ["M434c", "M434d", "M435a", "M435b", "M435e", "M435c", "M435d"]),
   P(I436, None, "main", N3,
     "At the House of the Fierce, the Doman Liberation Front's hidden headquarters, Yugiri reported that she found Lord Hien, son of the late Lord Kaien, alive on the Azim Steppe. "
     "He will fight only if Doma still thirsts for freedom, and asked her to learn the truth of its heart. The Front is few and weak, broken by Zenos with Yotsuyu's help.",
     ["M435d", "M436a", "M436c", "M436d", "M436e", "M436i", "M436f"]),
   P(I437, None, "main", N3,
     L4 + "Posing as merchants in Namai with Yugiri and Lyse, you found the villagers pushed beyond the brink, their samurai lords dead and the Doman Enclave shut behind the Moon Gates. "
     "Yugiri fears they now doubt the wisdom of resisting at all.",
     ["M436c", "M436d", "M437b", "M437e", "M437c", "M437d", "M437g", "M437f"]),
   P(I438, None, "main", N3,
     L4 + "In Namai, Isse told you how imperial soldiers beat the rebels' families in the village square and threatened his sister, and begged you to go. "
     "Yugiri wonders whether Lord Hien foresaw how broken his people's spirits would be.",
     ["M436c", "M436d", "M438b", "M438c", "M438d", "M438e"]),
   P(I439, None, "main", N3,
     "Yugiri is gauging whether Doma's people want freedom enough for Lord Hien to return. When imperial soldiers took Namai's villagers, Isse among them, calling it the answer to Isari, "
     "she armed you with a blowgun and sleeping darts. You cleared the way to the castrum Fluminis, where the captives face a life of servitude.",
     ["M436e", "M439a", "M439b", "M439d", "M439e", "M439f"]),
   P(I440, None, "main", N3,
     "Imperial soldiers seized Namai's villagers, Isse among them, for forced labor at the castrum Fluminis. Disguised in a stolen uniform, you helped Yugiri put the guards to sleep and free them, "
     "but the villagers say the Empire cannot be escaped and that survivors must bend the knee. Yugiri swore by all the kami to free them.",
     ["M439a", "M439e", "M440b", "M440g", "M440c", "M440d", "M440e"]),
   P(I441, None, "main", N3,
     "You and Yugiri freed Namai's villagers from imperial forced labor, and she confided she was born beneath the Ruby Sea and trained as a shinobi. "
     "Then an imperial airship brought Zenos, the crown prince and Doma's anointed viceroy, who defeated the Alliance and the Scions at Rhalgr's Reach. "
     "Yugiri resolved to kill him, though Gosetsu warns it would doom Doma.",
     ["M440g", "M441a", "M441i", "M441h", "M441c", "M441d", "M441j", "M441g", "M441f"]),
   P(I442, None, "main", N3,
     L5 + "Gosetsu would not pursue her, but you did: Zenos will inspect the Moon Gates this very evening, and you agreed to join her ambush from Yuzuka Manor. "
     "Isse overheard, and fears what will follow.",
     ["M441c", "M441g", "M441f", "M442a", "M442b", "M442g", "M442e", "M442f"]),
   P(I443, None, "main", N3,
     "You and Yugiri ambushed Zenos near Yuzuka Manor. His new katana's crimson energy felled you both, and he recognized you as the champion of the savages he had faced before, urging you to live and grow stronger for a rematch. "
     "When armed villagers, Gosetsu and Alisaie stood over Yugiri, he withdrew; Alphinaud had convinced them to come to your defense.",
     ["M443a", "M443b", "M443c", "M443d", "M443e", "M443f", "M443g"]),
   P(I444, None, "main", N3,
     "Your failed ambush of Zenos stirred Namai to defy him, the proof of conviction Lord Hien wanted. With most imperial forces gone from Doma, Alphinaud plans an uprising against Doma Castle, "
     "and Yugiri leaves for the Azim Steppe to fetch Lord Hien. Zenos warned Yotsuyu not to yield Doma, and in Gyr Abania, Estinien found a great crater.",
     ["M444f", "M444c", "M444d", "M444b", "M444h", "M444i", "M444m"]),
 ],
 "evt-lord-hien-on-the-steppe": [
   P(I445, None, "main", N4,
     "Your attempt on Zenos stirred Doma's people to rise against the imperials, the sign Lord Hien was waiting for. You, Yugiri, Lyse and Gosetsu went north from Isari, "
     "through the mountains, to the Azim Steppe to bring him home to lead a new rebellion. Yugiri brought you to Reunion, a Xaela marketplace, to begin the search.",
     ["M445b", "M445a", "M445e", "M445f", "M445d"]),
   P(I446, None, "main", N4,
     L6 + "In Reunion, where some of the Steppe's fifty Xaela tribes trade, a horsemaster said the Doman comes and goes with a Mol girl. "
     "You found her, Cirina, who knows you seek Hien, but she would not leave until she had bought a kinsai.",
     ["M445a", "M445d", "M446a", "M446c", "M446d", "M446e", "M446f"]),
   P(I447, None, "main", N4,
     L6 + "Once Cirina had her kinsai, she explained the Steppe: the Oronir and the Dotharl are the strongest tribes, her own Mol are lambs among wolves, "
     "and the tribe that wins a great ritual battle rules the Steppe for a year. She knows where Hien may be.",
     ["M445a", "M447b", "M447a", "M447c", "M447e"]),
   P(I448, None, "main", N4,
     "Cirina found Lord Hien near death long ago, and the Mol nursed him back to health. You met him above Reunion: Doma's young heir will not go home until he wins the Steppe's ceremonial battle "
     "and earns the right to lead the Xaela to Doma. Yugiri returned to Yanxia to ready the Liberation Front's forces, while you, Lyse and Gosetsu stay with him.",
     ["M448a", "M448b", "M448c", "M448d", "M448e", "M448h"]),
   P(I449, None, "main", N4,
     L7 + "At Mol Iloh he asked Temulun, khatun of the Mol, to let you fight as Mol warriors, since victory beside a stronger tribe would be credited to it. "
     "Temulun welcomed you, saying the stars shone at your coming, though Cirina says her people are too few to win.",
     ["M448d", "M449a", "M449b", "M449e", "M449f", "M449d"]),
   P(I450, None, "main", N4,
     L7 + "To fight for the Mol, you must first pass a trial in the footsteps of the warrior Bardam, which many do not survive. Meanwhile you hunted gulo gulo for a Mol feast, and Hien made it a contest.",
     ["M448d", "M449a", "M449g", "M450a", "M450b", "M450c", "M450d"]),
   P(I451, None, "main", N4,
     L7 + "Gathering fuel with Lyse and the Mol children, you heard that the Mol hold the soil to belong to all. Sparring with Gosetsu, who calls him by his childhood name, "
     "Hien admitted he should have fled when his father died, and declared it time for your trial.",
     ["M448d", "M449a", "M451a", "M451d", "M451b", "M451f"]),
   P(I452, None, "main", N4,
     L7 + "To be warriors of the Steppe, you must walk Bardam's pilgrimage to the holy place named for him and tame a yol at its altar. "
     "Warned that some tribes enslave rival warriors before the battle, you fought off attackers on the way and reached the pass to Bardam's Mettle.",
     ["M448d", "M452a", "M452b", "M452c", "M452d", "M452e", "M452f"]),
   P(I453, None, "main", N4,
     L7 + "In Bardam's Mettle, the legendary warrior's trials judged you worthy, and you and Lyse each tamed a yol and became warriors of the Steppe. Hien and Gosetsu have not yet emerged.",
     ["M448d", "M449a", "M453a", "M453e", "M453b", "M453c", "M453d"]),
 ],
 "evt-captives-of-the-oronir": [
   P(I454, None, "main", N5,
     "Lord Hien hopes to win the Steppe's great ritual battle beside the Mol. Leaving Bardam's Mettle as warriors of the Steppe, your party was surrounded by Oronir and taken to the Dawn Throne, "
     "where their leader Magnai, who calls his people born of the Sun, demanded tribute and fealty. For now you humor him.",
     ["M448d", "M449a", "M454a", "M454b", "M454d", "M454c", "M454e"]),
   P(I455, None, "main", N5,
     L8 + "Baatu set your labors: Lyse milks the beasts, Gosetsu mends armor, and you gathered swordgrass from Azim Khaat for paralysis potions. "
     "Hien asked how the Oronir can be children of Azim if all Xaela are born of Nhaama, and Magnai sent him to the elders.",
     ["M454b", "M454c", "M455a", "M455b", "M455g", "M455c", "M455d", "M455e"]),
   P(I456, None, "main", N5,
     L8 + "The elder Udutai told you that Azim and Nhaama were lovers kept apart, and that Azim came down as the first Oronir. "
     "Hien hopes the Oronir's belief that they must guard all Xaela can become an alliance, and Magnai demands one more task before your freedom.",
     ["M454b", "M454c", "M456a", "M456b", "M456c", "M456e", "M456f"]),
   P(I457, None, "main", N5,
     L8 + "He sent you and Gosetsu to scout the Dotharl, keeping Hien and Lyse as hostages who will be enslaved if you fail. "
     "You saved a Dotharl hunter, and Sadu, their khatun, scorned the Mol but let you walk among her people.",
     ["M454b", "M457a", "M457b", "M457c", "M457h", "M457d", "M457f", "M457e"]),
   P(I458, None, "main", N5,
     L8 + "Scouting the Dotharl for him while Hien and Lyse stay hostage, you learned from Sadu that her people fear no death: a fallen warrior returns in a newborn who takes his name. "
     "Gosetsu judges them formidable but few.",
     ["M454b", "M457a", "M457b", "M458a", "M458c", "M458d", "M458e"]),
   P(I459, None, "main", N5,
     L8 + "Sadu told you the Dotharl need only strength and are few because they kill and are killed, and invited you to fight for them. "
     "Gosetsu mourned at a fallen hunter's grave, while in the Oronir prison Lyse vowed to seize the future she wants.",
     ["M454b", "M457a", "M459a", "M459b", "M459d", "M459h", "M459e", "M459g"]),
   P(I460, None, "main", N5,
     "Back at the Dawn Throne, Magnai heard that the Dotharl have no secret plans, and freed your party once you swore to abide by the law of the Steppe. "
     "Baatu says Magnai seeks Nhaama in the eyes of the Steppe's women. Hien and Lyse left their cells, and you rejoined Cirina and the Mol to prepare for the great battle.",
     ["M460a", "M460d", "M460b", "M460g", "M460e", "M460f"]),
 ],
 "evt-the-steppe-rides-south": [
   P(I461, None, "main", N6,
     "In the Naadam, the ceremonial battle for rule of the Steppe, you led the Mol past the Oronir and the Dotharl to claim the ovoo, and stand crowned khagan. "
     "When Grynewaht came with imperial troops to kill you, the united Steppe drove him off. Hien persuaded the Oronir and the Dotharl to march south and fight for Doma's liberation.",
     ["M461a", "M461b", "M461c", "M461d", "M461i", "M461e"]),
   P(I462, None, "main", N6,
     "The Mol won the Naadam beside you, their crowned khagan, and every one of their warriors came home. Temulun and Cirina thanked you with a morin khuur, "
     "for the Mol keep their heroes' deeds alive in song. The Oronir and the Dotharl have agreed to fight for Doma at Lord Hien's call.",
     ["M462a", "M462b", "M462c", "M462d", "M462e", "M462f", "M461e"]),
   P(I463, None, "main", N6,
     "With the Naadam won, Lord Hien has his Xaela army. Magnai renewed his vow to aid the Domans, though he insists you are not allies and wondered whether Cirina is his long-sought moon, "
     "and Sadu promised Dotharl warriors and unsealed the southern pass. Cirina gave Lyse a Mol banner as you parted for Doma.",
     ["M463a", "M463b", "M463i", "M463c", "M463e", "M463k", "M463h"]),
   P(I464, None, "main", N6,
     "Lord Hien returned to the House of the Fierce with his Xaela army and was reunited with Yugiri. Alphinaud and Alisaie have won over the Confederacy, many Domans and, on trade terms, "
     "the Blue Kojin, though Sui-no-Sato refused. Zenos has left for Gyr Abania, but Yotsuyu remains acting viceroy, and Doma Castle's garrison may be readying a purge.",
     ["M464a", "M464b", "M464d", "M464e", "M464f", "M464g", "M464h", "M464i"]),
 ],
})

# ---- Relationship types and relationships ----
TYPES = [("child-of", "child of", "parent of", False)]  # as content_3_1_to_3_56 defines it

# ----------------------------------------------------------------------------------------------------
RELS = [
 # The viceroy and her people
 ("rel-yotsuyu-member-of-garlean-empire", "char-yotsuyu", "member-of", "org-garlean-empire", I419, None, "main", ["M419c"]),
 ("rel-yotsuyu-turned-against-doma", "char-yotsuyu", "turned-against", "loc-doma", I419, None, "main", ["M419g"]),
 ("rel-yotsuyu-controls-isari", "char-yotsuyu", "controls", "loc-isari", I419, I433, "main", ["M419b", "M419c"], ["M433a"]),
 ("rel-yotsuyu-serves-zenos", "char-yotsuyu", "serves", "char-zenos", I434, None, "main", ["M434b"]),
 ("rel-yotsuyu-controls-doma", "char-yotsuyu", "controls", "loc-doma", I434, None, "main", ["M434b", "M434c"]),
 ("rel-grynewaht-serves-yotsuyu", "char-grynewaht", "serves", "char-yotsuyu", I432, None, "main", ["M432i", "M432f"]),
 ("rel-grynewaht-member-of-garlean-empire", "char-grynewaht", "member-of", "org-garlean-empire", I434, None, "main", ["M434h"]),
 ("rel-gosetsu-prisoner-of-yotsuyu", "char-gosetsu", "prisoner-of", "char-yotsuyu", I419, I433, "main", ["M419e", "M419f"], ["M433d", "M433a"]),
 ("rel-gosetsu-held-at-isari", "char-gosetsu", "held-at", "loc-isari", I419, I433, "main", ["M419f"], ["M433d", "M433a"]),
 ("rel-zenos-controls-doma", "char-zenos", "controls", "loc-doma", I441, None, "main", ["M441c"]),
 ("rel-zenos-opposes-doman-liberation-front", "char-zenos", "opposes", "org-doman-liberation-front", I436, None, "main", ["M436f", "M436k"]),
 # The Ruby Sea
 ("rel-soroban-member-of-blue-kojin", "char-soroban", "member-of", "org-blue-kojin", I419, None, "main", ["M419a"]),
 ("rel-soroban-aids-scions", "char-soroban", "aids", "org-scions", I419, None, "main", ["M419a", "M419j"]),
 ("rel-rasho-leads-confederacy", "char-rasho", "leads", "org-confederacy", I420, None, "main", ["M420a"]),
 ("rel-tansui-member-of-confederacy", "char-tansui", "member-of", "org-confederacy", I420, None, "main", ["M420a", "M420c"]),
 ("rel-confederacy-aids-scions", "org-confederacy", "aids", "org-scions", I432, None, "main", ["M432d"]),
 ("rel-confederacy-opposes-garlean-empire", "org-confederacy", "opposes", "org-garlean-empire", I432, None, "main", ["M432k", "M432d"]),
 ("rel-red-kojin-serves-garlean-empire", "org-red-kojin", "serves", "org-garlean-empire", I424, I434, "main", ["M424c", "M424e"], ["M434j", "M434f"]),
 ("rel-red-kojin-serves-susano", "org-red-kojin", "serves", "char-susano", I431, I432, "main", ["M431c", "M431d"], ["M432b", "M432j"]),
 ("rel-bunchin-leads-blue-kojin", "char-bunchin", "leads", "org-blue-kojin", I426, None, "main", ["M426a"]),
 ("rel-shiosai-member-of-raen", "char-shiosai", "member-of", "org-raen", I428, None, "main", ["M428a", "M428b"]),
 # Doma
 ("rel-hien-child-of-kaien", "char-hien", "child-of", "char-kaien", I436, None, "main", ["M436a"]),
 ("rel-yugiri-serves-hien", "char-yugiri", "serves", "char-hien", I436, None, "main", ["M436e", "M436c"]),
 ("rel-gosetsu-serves-hien", "char-gosetsu", "serves", "char-hien", I441, None, "main", ["M441b"]),
 ("rel-gosetsu-member-of-doman-liberation-front", "char-gosetsu", "member-of", "org-doman-liberation-front", I435, None, "main", ["M435a", "M435d"]),
 ("rel-yugiri-member-of-doman-liberation-front", "char-yugiri", "member-of", "org-doman-liberation-front", I441, None, "main", ["M441i"]),
 ("rel-doman-liberation-front-headquartered-at-house-of-the-fierce", "org-doman-liberation-front", "headquartered-at", "loc-house-of-the-fierce", I435, None, "main", ["M435d"]),
 ("rel-hien-leads-doman-liberation-front", "char-hien", "leads", "org-doman-liberation-front", I448, None, "main", ["M448h", "M448e"]),
 ("rel-yugiri-opposes-zenos", "char-yugiri", "opposes", "char-zenos", I441, None, "main", ["M441g", "M441f"]),
 ("rel-isse-prisoner-of-garlean-empire", "char-isse", "prisoner-of", "org-garlean-empire", I439, I440, "main", ["M439a", "M439e"], ["M440g"]),
 ("rel-alphinaud-aids-doman-liberation-front", "char-alphinaud", "aids", "org-doman-liberation-front", I444, None, "main", ["M444d"]),
 ("rel-alisaie-aids-doman-liberation-front", "char-alisaie", "aids", "org-doman-liberation-front", I464, None, "main", ["M464e"]),
 ("rel-confederacy-aids-doman-liberation-front", "org-confederacy", "aids", "org-doman-liberation-front", I464, None, "main", ["M464e"]),
 ("rel-blue-kojin-aids-doman-liberation-front", "org-blue-kojin", "aids", "org-doman-liberation-front", I464, None, "main", ["M464f"]),
 # The Azim Steppe
 ("rel-cirina-member-of-mol", "char-cirina", "member-of", "org-mol", I446, None, "main", ["M446d"]),
 ("rel-mol-aids-hien", "org-mol", "aids", "char-hien", I448, None, "main", ["M448b"]),
 ("rel-temulun-leads-mol", "char-temulun", "leads", "org-mol", I449, None, "main", ["M449e"]),
 ("rel-cirina-grandchild-of-temulun", "char-cirina", "grandchild-of", "char-temulun", I462, None, "main", ["M462d"]),
 ("rel-magnai-leads-oronir", "char-magnai", "leads", "org-oronir", I454, None, "main", ["M454b"]),
 ("rel-oronir-headquartered-at-dawn-throne", "org-oronir", "headquartered-at", "loc-dawn-throne", I454, None, "main", ["M454b"]),
 ("rel-hien-prisoner-of-oronir", "char-hien", "prisoner-of", "org-oronir", I454, I460, "main", ["M454a", "M454c"], ["M460g", "M460d"]),
 ("rel-lyse-prisoner-of-oronir", "char-lyse", "prisoner-of", "org-oronir", I454, I460, "main", ["M454a", "M454c"], ["M460g", "M460d"]),
 ("rel-gosetsu-prisoner-of-oronir", "char-gosetsu", "prisoner-of", "org-oronir", I454, I460, "main", ["M454a", "M454c"], ["M460d"]),
 ("rel-sadu-leads-dotharl", "char-sadu", "leads", "org-dotharl", I457, None, "main", ["M457d"]),
 ("rel-oronir-opposes-dotharl", "org-oronir", "opposes", "org-dotharl", I457, None, "main", ["M457g", "M457c"]),
 ("rel-mol-controls-dawn-throne", "org-mol", "controls", "loc-dawn-throne", I461, None, "main", ["M461c"]),
 ("rel-oronir-aids-hien", "org-oronir", "aids", "char-hien", I461, None, "main", ["M461e", "M461f"]),
 ("rel-dotharl-aids-hien", "org-dotharl", "aids", "char-hien", I461, None, "main", ["M461e", "M461j"]),
]

# Relationships an earlier era defined, ended here.
ADJUST = {
 "rel-grynewaht-serves-zenos": {"until": I434, "end": ["M434h"]},  # content_4_0_part1: he now waits for Zenos to reinstate him
}

# ---- Arcs ----------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-i1-a-bargain-with-the-confederacy", "evt-a-bargain-with-the-confederacy", I419, I428),
 ("arc-i2-the-kojin-treasures", "evt-the-kojin-treasures", I429, I433),
 ("arc-i3-the-silence-of-yanxia", "evt-the-silence-of-yanxia", I434, I444),
 ("arc-i4-lord-hien-on-the-steppe", "evt-lord-hien-on-the-steppe", I445, I453),
 ("arc-i5-captives-of-the-oronir", "evt-captives-of-the-oronir", I454, I460),
 ("arc-i6-the-steppe-rides-south", "evt-the-steppe-rides-south", I461, I464),
]

CASTS = {
 "evt-a-bargain-with-the-confederacy": [
   ("char-soroban", I419, ["M419a"]), ("char-gosetsu", I419, ["M419e"]), ("char-yotsuyu", I419, ["M419c"]),
   ("char-alisaie", I419, ["M419m"]), ("org-confederacy", I419, ["M419h"]), ("char-rasho", I420, ["M420a"]),
   ("org-red-kojin", I424, ["M424c"]), ("org-blue-kojin", I425, ["M425b"]), ("char-lyse", I425, ["M425d"]),
   ("org-raen", I428, ["M428b"]),
 ],
 "evt-the-kojin-treasures": [
   ("char-alisaie", I429, ["M429e"]), ("char-lyse", I429, ["M429g"]), ("char-soroban", I430, ["M430e"]),
   ("char-bunchin", I430, ["M430b"]), ("org-red-kojin", I430, ["M430c"]), ("char-susano", I431, ["M431e"]),
   ("org-confederacy", I432, ["M432d"]), ("char-rasho", I432, ["M432d"]), ("char-yotsuyu", I432, ["M432e"]),
   ("char-gosetsu", I432, ["M432f"]),
 ],
 "evt-the-silence-of-yanxia": [
   ("char-gosetsu", I434, ["M434e"]), ("char-yotsuyu", I434, ["M434b"]), ("char-zenos", I434, ["M434b"]),
   ("char-isse", I435, ["M435a"]), ("org-doman-liberation-front", I435, ["M435d"]), ("char-yugiri", I436, ["M436c"]),
   ("char-hien", I436, ["M436c"]), ("char-lyse", I437, ["M437e"]), ("char-alisaie", I443, ["M443e"]),
   ("char-alphinaud", I443, ["M443g"]),
 ],
 "evt-lord-hien-on-the-steppe": [
   ("char-hien", I445, ["M445a"]), ("char-yugiri", I445, ["M445d"]), ("char-lyse", I445, ["M445a"]),
   ("char-gosetsu", I445, ["M445a"]), ("char-cirina", I446, ["M446d"]), ("org-mol", I446, ["M446c"]),
   ("org-oronir", I447, ["M447b"]), ("org-dotharl", I447, ["M447b"]), ("char-temulun", I449, ["M449e"]),
 ],
 "evt-captives-of-the-oronir": [
   ("char-hien", I454, ["M454a"]), ("char-lyse", I454, ["M454a"]), ("char-gosetsu", I454, ["M454a"]),
   ("char-magnai", I454, ["M454b"]), ("org-oronir", I454, ["M454b"]), ("org-dotharl", I457, ["M457d"]),
   ("char-sadu", I457, ["M457d"]), ("char-cirina", I460, ["M460f"]), ("org-mol", I460, ["M460e"]),
 ],
 "evt-the-steppe-rides-south": [
   ("char-hien", I461, ["M461e"]), ("char-cirina", I461, ["M461g"]), ("org-mol", I461, ["M461c"]),
   ("char-magnai", I461, ["M461f"]), ("org-oronir", I461, ["M461e"]), ("char-sadu", I461, ["M461j"]),
   ("org-dotharl", I461, ["M461e"]), ("char-grynewaht", I461, ["M461d"]), ("char-yugiri", I464, ["M464b"]),
   ("char-alphinaud", I464, ["M464h"]),
 ],
}

ARC_NOTES = {
 "arc-i1-a-bargain-with-the-confederacy": "MSQ #419 *To Bend with the Wind* to #428 *Forever and Ever Apart*, including the three parallel #421 paths: "
   "the landing at Isari and Gosetsu's surrender (M419e), Rasho's refusal (M420e), the wager (M424f) and the Blue Kojin's jewel hunt, ending when the Raen refuse "
   "and Yotsuyu presses Gosetsu about Lord Hien (M428d, M428f). Each #421 recap opens with the same lead and names only its own path's errand.",
 "arc-i2-the-kojin-treasures": "MSQ #429 *In Darkness the Magatama Dreams* to #433 *Tide Goes in, Imperials Go Out*: the Magatama found (M429e), the vault raid, "
   "Susano woken and slain (M431e, M432b), ending when the Confederacy frees Isari and Gosetsu (M433a, M433d), which pays off the wager.",
 "arc-i3-the-silence-of-yanxia": "MSQ #434 *A Silence in Three Parts* to #444 *All the Little Angels*: Yanxia under Yotsuyu's memory of purges (M434d), the House of the Fierce, "
   "Yugiri's news of Hien (M436c), Namai's despair, Fluminis, and the failed ambush of Zenos (M443b), ending when Yugiri leaves for the Steppe (M444b). 11 steps.",
 "arc-i4-lord-hien-on-the-steppe": "MSQ #445 *Here There Be Xaela* to #453 *In the Footsteps of Bardam the Brave*: Reunion, Cirina, Hien found (M448c) and the Mol's trial, "
   "ending as you and Lyse become warriors of the Steppe (M453d). Its recaps call the contest \"the Steppe's great ritual battle\", because #461's title is *Naadam*.",
 "arc-i5-captives-of-the-oronir": "MSQ #454 *The Children of Azim* to #460 *As the Gods Will*: Magnai's tribute, the Oronir origin tale, the Dotharl scouting with Hien and Lyse as hostages "
   "(M457b), ending when Magnai frees the party (M460g). Its name avoids #457's *Sworn Enemies of the Sun*.",
 "arc-i6-the-steppe-rides-south": "MSQ #461 *Naadam* to #464 *The Hour of Reckoning*: the Mol's victory (M461c), Grynewaht driven off, the Oronir and Dotharl pledged (M461e), "
   "and Hien's return to the House of the Fierce (M464a). It ends on this era's last step, so the next era's arc opens at #465.",
}

DECISIONS = [
 "**Six arcs (i1–i6)** cover all 46 steps from #419 to #464 without sharing a step; each cast stops at ten.",
 "**The three #421 paths** (The Solace of the Sea, The Arrows of Misfortune, The Last Voyage) get recaps that share one lead and describe only their own errand; no entity, relationship or cast member starts on them.",
 "**\"Naadam\" waits for #461**, whose title it is: before then the text says \"the Steppe's great ritual battle\". ",
 "**Kojin as two groups**, `org-red-kojin` (mercenaries of the Empire, from #424, when Kojin catchers first prey on the Confederates) and `org-blue-kojin` (Soroban's traders, from #419). The Red's service to the Empire ends at #434, when Yotsuyu has Grynewaht defeat those who abandoned their posts.",
 "**Susano** is `char-susano`: woken at #431, slain at #432; the Red's service to it ends there with the Red marine's cry (M432j).",
 "**Zenos** is named \"Zenos\" from #434 (the Journal names him), with \"The Viceroy\" (his 3.56 name) as an alias. \"yae Galvus\" appears only in the pages' speaker tags and locators.",
 "**Lord Hien** (`char-hien`, alias \"Lord Hien\") starts at #428, where Yotsuyu names Doma's missing heir; his father Lord Kaien (`char-kaien`) starts there too, as Yotsuyu's \"fallen\" lord.",
 "**Prisoners of the Oronir** (Hien, Lyse, Gosetsu) run #454–#460, from the escort to the Dawn Throne to Magnai's \"fetch the others from their cells\".",
 "**Left out as entities** (named in text only): Afumi, Kajika, Aranami, Ihanami, Yunagi, Baatu, Udutai, Daidukul, Geser, Hancock, the Ruby Princess, Tamamizu, Sui-no-Sato, Reunion, Mol Iloh, Fluminis, Bardam and Bardam's Mettle.",
]
