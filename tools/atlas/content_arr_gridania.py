"""Atlas content for A Realm Reborn 2.0, the Gridania starting-city chain: MSQ #1 Close to Home (Gridania) to #23 Call of
the Sea (Gridania), steps cp-msq-1 to cp-msq-23. Data only; build_pilot_content.py merges it (see docs/atlas/era-modules.md).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes A01, A02 and the first quest of A03). Every
locator quotes a quest's Journal, Steps or main dialogue; class-, gender- and "[unknown trigger]" branches are not cited.

The three starting chains are mutually exclusive in game but run one after another in the timeline, and this chain
comes first. So every record here stays visible through the Limsa Lominsa and Ul'dah chains until a later record
replaces it. Presentations therefore state facts about the entity (no "you"), and only the arc recaps speak to the
player. cp-msq-1 is the first step of the whole timeline, so no arc starts on it.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

S = {n: f"cp-msq-{n}" for n in range(1, 24)}

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #1 Close to Home (Gridania)
 "M1a": ("Miounne, proprietress of the Carline Canopy, sets a new adventurer three tasks to learn the fundamentals of adventuring.", "Close to Home (Gridania)",
         "[[Miounne]], proprietress of [[the Carline Canopy]], wants you to perform three tasks that will help you learn the fundamentals of [[Adventurer|adventuring]]."),
 "M1b": ("Miounne's newcomers are formal members of the Adventurers' Guild.", "Close to Home (Gridania)",
         "Now that you are a formal member of the Adventurers' Guild, we must be sure you have a firm grasp of the fundamentals of adventuring."),
 "M1c": ("Miounne advises building a reputation by helping citizens in need.", "Close to Home (Gridania)",
         "prove your worth and build a reputation, and in time folk will be more inclined to entrust you with matters of moment."),
 "M1d": ("New adventurers are sent around Gridania to help citizens in need.", "Close to Home (Gridania)",
         "As you make your way around [[Gridania]], try approaching citizens who appear to be in need of help."),
 "M1e": ("The city's markets lie at the heart of Old Gridania's commercial district.", "Close to Home (Gridania)",
         "I would have you visit the markets at the heart of [[Old Gridania]]'s commercial district."),
 # #2 To the Bannock
 "M2a": ("The Bannock, just outside the city, is where the Order of the Twin Adder drills its soldiers.", "To the Bannock",
         "It is a training ground found just outside the city where the soldiers of the [[The Order of the Twin Adder|Order of the Twin Adder]] are drilled in swordplay and other martial matters."),
 "M2b": ("Galfrid trains the Twin Adder's recruits.", "To the Bannock", "My name is Galfrid, and I am responsible for training our Twin Adder recruits."),
 "M2c": ("The Calamity of five years past left deep scars on the Twelveswood.", "To the Bannock",
         "[[the Calamity]] of five years past has left deep scars on [[The Black Shroud|the Twelveswood]]"),
 "M2d": ("The elementals' power is waning, and the forest's harmony gives way to chaos.", "To the Bannock",
         "The power of the elementals wanes, and the harmony of the forest gives way to chaos."),
 "M2e": ("For Gridanians, restoring the forest is a sacred duty.", "To the Bannock",
         "For the citizens of [[Gridania]], the restoration of the forest is a sacred duty."),
 # #3 Passing Muster
 "M3a": ("Galfrid is the Bannock's chief instructor, and now gives you missions.", "Passing Muster",
         "Galfrid has determined that your equipment passes muster. You are now eligible to undertake missions from the chief instructor."),
 "M3b": ("Since the Seventh Umbral Era began, many of the Twelveswood's creatures have turned into vicious monsters.", "Passing Muster",
         "in the five years since the dawn of the [[Seventh Umbral Era]], many of the [[The Black Shroud|Twelveswood]]'s creatures have transformed into vicious, bloodthirsty monsters."),
 # #4 Chasing Shadows
 "M4a": ("Ixali activity has been rising since an unknown individual appeared in the Twelveswood, and Galfrid suspects a connection.", "Chasing Shadows",
         "you learn that [[Ixal]]i activity has been steadily increasing since the appearance of an as-yet-unknown individual in the Twelveswood. Suspecting a connection, Galfrid bids you investigate [[Lifemend Stump]] to the northeast."),
 "M4b": ("The quarry is so elusive he seems to know the patrols' movements ahead of time.", "Chasing Shadows",
         "almost as if he knows our movements ahead of time."),
 "M4c": ("At Lifemend Stump a sword is thrust into the stump, and a dead Ixal lies nearby.", "Chasing Shadows",
         "a [[Magicked Blade|sword]] has been thrust into the stump, and an Ixal lies dead nearby."),
 "M4d": ("Galfrid identifies the blade as Ixali, of a kind used only in their rituals.", "Chasing Shadows",
         "I can say with absolute certainty that this blade is of Ixali origin. It is of a kind used exclusively in the beastmen's rituals."),
 "M4e": ("The dead Ixal was a chieftain, far inside enemy territory; the beastmen may be acting under orders.", "Chasing Shadows",
         "An Ixal. And no ordinary Ixal, either—a chieftain. … That they would venture this deep into enemy territory... The [[beastmen]] may indeed be acting under orders."),
 "M4f": ("In a vision, a voice names herself Hydaelyn.", "Chasing Shadows", "I am Hydaelyn. All made one."),
 "M4g": ("Hydaelyn says the realm's Light has grown dim and Darkness has risen in its stead.", "Chasing Shadows",
         "A Light there once was that shone throughout this realm... yet it hath since grown dim. … And as it hath faltered, so hath Darkness risen up in its stead, presaging an end to Life."),
 "M4h": ("Hydaelyn bids you lay claim to the Crystals of Light, which can banish the Darkness.", "Chasing Shadows",
         "The power to banish the Darkness dwelleth in the Crystals of Light. Journey forth and lay claim to them."),
 "M4i": ("The Hyuran Yda and the Lalafellin Papalymo are scholars, friends of Gridania who assist the Gods' Quiver and the Wood Wailers.", "Chasing Shadows",
         "It turns out that the [[Hyur]]an lass and [[Lalafell]]in lad you encountered are friends of [[Gridania]]. Named [[Yda]] and [[Papalymo]], respectively, the pair are scholars who are assisting [[the Gods' Quiver]] and [[the Wood Wailers]]."),
 "M4j": ("Gridania counts Yda and Papalymo among its staunchest allies: scholars from a distant land, there since before the Calamity.", "Chasing Shadows",
         "Gridania counts them among her staunchest allies. Both are scholars hailing from a distant land, and have been with us since before the Calamity."),
 # #5 Eggs over Queasy
 "M5a": ("Galfrid needs an extra hand after his subordinates were injured.", "Eggs over Queasy",
         "Galfrid requires an extra hand after his subordinates were injured."),
 "M5b": ("Chigoes carry the Creeping Death, and Gridanian researchers check them to prevent outbreaks.", "Eggs over Queasy",
         "Chigoes are known carriers of the Creeping Death"),
 "M5c": ("One outbreak of the Creeping Death once killed a third of Gridania's Hyur.", "Eggs over Queasy",
         "Indeed, a single outbreak once claimed the lives of a third of the Hyuran population here in [[Gridania]]."),
 "M5d": ("The Twin Adder and the Wood Wailers collect samples for the Trappers' League.", "Eggs over Queasy",
         "Members of [[The Order of the Twin Adder|the Twin Adder]] and [[the Wood Wailers]] are assisting the league by collecting the samples they need to check for signs of sickness."),
 "M5e": ("The Twin Adder treats newcome adventurers and forestborn Gridanians alike.", "Eggs over Queasy",
         "The Order of the Twin Adder makes no distinction between newcome adventurers and forestborn Gridanians."),
 # #6 Surveying the Damage
 "M6a": ("A startled recruit left surveying equipment behind in a cave.", "Surveying the Damage",
         "needs you to recover the surveying equipment left behind in a cave by a startled recruit."),
 "M6b": ("The Calamity reshaped the forest, so the conjurer Pauline asked the Twin Adder to survey it.", "Surveying the Damage",
         "[[The Calamity]] has dramatically altered the forest's geography, prompting a [[conjurer]] named Pauline to request that [[the Order of the Twin Adder]] carry out topographical surveys."),
 "M6c": ("Pauline says old knowledge of the Twelveswood can no longer be relied on.", "Surveying the Damage",
         "We can no longer rely on our past knowledge of the [[The Black Shroud|Twelveswood]]."),
 # #7 A Soldier's Breakfast
 "M7a": ("Anoles coming down from the mountains are disrupting the conjurers' communion with the elementals.", "A Soldier's Breakfast",
         "A growing number of anoles are venturing down from the mountains and disrupting the conjurers' communion with the elementals."),
 "M7b": ("You thinned the anoles and took an egg for a soldier's breakfast at the Bannock.", "A Soldier's Breakfast",
         "Large and rich in nutrients, anole eggs make a perfect breakfast for a soldier. Deliver it to Tsubh Khamazom at the Bannock."),
 # #8 Spirithold Broken
 "M8a": ("Conjurers and their Wood Wailer escort were attacked by a towering shadow during a sacred rite in Spirithold.", "Spirithold Broken",
         "a party of [[conjurer]]s and their [[The Wood Wailers|Wood Wailer]] escort were attacked by a towering shadow while performing a sacred rite inside Spirithold."),
 "M8b": ("Galfrid fears the Ixal are trying to weaken the bond between man and elemental.", "Spirithold Broken",
         "I fear the Ixal somehow caught wind of our plans, and are attempting to disrupt the rite in an effort to weaken the bond between man and elemental."),
 "M8c": ("A masked mage loosed a clay golem on you; Yda and Papalymo arrived as you destroyed it.", "Spirithold Broken",
         "You encounter a mysterious masked mage who unleashes a [[Clay Golem|clay golem]] upon you. After a desperate struggle, you manage to dispatch the automaton just as [[Yda]] and [[Papalymo]] arrive."),
 "M8d": ("Papalymo says the masked mage has eluded them yet again.", "Spirithold Broken", "Damnation! He has eluded us yet again!"),
 "M8e": ("The rite failed; Papalymo will see the Hearer to safety and send for his peers to finish it.", "Spirithold Broken",
         "We shall see the Hearer to safety, and send for his peers to finish the rite."),
 "M8f": ("Yda and Papalymo are surveying the Twelveswood together.", "Spirithold Broken", "Papalymo and I are surveying the Twelveswood together!"),
 "M8g": ("The Wood Wailer Alestan promises to investigate the masked mage.", "Spirithold Broken",
         "the Wood Wailer promises to investigate the masked mage"),
 "M8h": ("Miounne asks that the tale of walking statues be kept quiet until the Hearers make their will known.", "Spirithold Broken",
         "Until the Hearers have made their will on the matter known, it would be best to avoid unsettling people with stories of walking statues."),
 # #9 On to Bentbranch
 "M9a": ("Miounne sends you on to Bentbranch Meadows, whose farmhands need help with chores around the ranch.", "On to Bentbranch",
         "the farmhands at Bentbranch Meadows are looking for someone to help out with various chores around the ranch. Make your way to [[Bentbranch]] and speak with [[Keitha]], the head wrangler."),
 # #10 You Shall Not Trespass
 "M10a": ("A Qiqirn broke a chocobo egg during a robbery at Bentbranch.", "You Shall Not Trespass",
          "It would seem that a Qiqirn broke a chocobo egg during a robbery at Bentbranch Meadows."),
 "M10b": ("Roseline orders an example made of exactly four Qiqirn scramblers.", "You Shall Not Trespass",
          "Find the lair to the west of here and make an example of exactly ''four'' Qiqirn scramblers."),
 # #11 Don't Look Down
 "M11a": ("Osha Jaab, a Wood Wailer, asks for blue trumpets to be plucked from the heavenspillar root.", "Don't Look Down",
          "[[Osha Jaab]], a [[The Wood Wailers|Wood Wailer]] at [[the Matron's Lethe]], is looking for a sure-footed [[adventurer]] to pluck blue trumpets from the root of the nearby heavenspillar."),
 "M11b": ("The root is one of the few ways across the Central Shroud since the Calamity all but split it.", "Don't Look Down",
          "It's one of the few ways folk can traverse the Central Shroud since the Calamity all but split the area in twain."),
 "M11c": ("Clearing the mushrooms saved the root from rot.", "Don't Look Down",
          "Your simple act of mushroom picking has saved the root of the heavenspillar from a rotten fate."),
 # #12 In the Grim Darkness of the Forest
 "M12a": ("Theodore noticed a shadowy figure in the woods north of the Matron's Lethe.", "In the Grim Darkness of the Forest",
          "Theodore noticed a shadowy figure in the woods north of [[the Matron's Lethe]]."),
 "M12b": ("Beside a still-warm campfire lies a worn leather bag.", "In the Grim Darkness of the Forest",
          "Next to the still-warm remnants of an old campfire, you discover a worn leather bag."),
 "M12c": ("Roseline believes the bag belongs to a stranger said to be meddling with the chocobos.", "In the Grim Darkness of the Forest",
          "Bugger me, I think this belongs to that stranger said to be meddling with the chocobos!"),
 "M12d": ("Roseline swears to find the shadow.", "In the Grim Darkness of the Forest", "I swear we will find this shadow."),
 # #13 Threat Level Elevated
 "M13a": ("Roseline entrusts you with a letter on everything she has learned about the stranger.", "Threat Level Elevated",
          "Roseline entrusts you with a letter detailing everything she has learned about the suspicious stranger."),
 "M13b": ("The sentry Bernard is sure the stranger has designs on Bentbranch.", "Threat Level Elevated", "They clearly have designs on Bentbranch."),
 "M13c": ("Eylgar is pleased that you warned the other sentries.", "Threat Level Elevated",
          "Eylgar is pleased by your efforts to warn the other sentries."),
 # #14 Migrant Marauders
 "M14a": ("A peddler swears winged beasts attacked him on the road south of Bentbranch.", "Migrant Marauders",
          "who swears that winged beasts attacked him on the road south of [[Bentbranch]]."),
 "M14b": ("Two northern vultures defend a nest beside a large egg.", "Migrant Marauders",
          "After stumbling upon a large vulture egg, two [[Northern Vulture|northern vultures]] descend to defend their nest."),
 "M14c": ("The nest was hidden less than twenty yalms from Lothaire's post.", "Migrant Marauders",
          "Lothaire is shocked to learn of the nest hidden less than twenty yalms from his post."),
 # #15 A Hearer Is Often Late
 "M15a": ("Hearer Leonnie must remain at the Hedgetree to commune with the elementals.", "A Hearer Is Often Late",
          "Hearer Leonnie must remain at the Hedgetree to commune with the [[elementals]]."),
 "M15b": ("The elementals murmur of a malevolent presence near the Tam-Tara Deepcroft.", "A Hearer Is Often Late",
          "the elementals murmur of a malevolent presence in the vicinity of the Tam-Tara Deepcroft."),
 "M15c": ("Leonnie's passage is rebooked on a later vessel.", "A Hearer Is Often Late",
          "who resigns herself to booking the conjurer passage on a later vessel."),
 # #16 Salvaging the Scene
 "M16a": ("Armelle asks you to retrieve the cargo of a wagon attacked by a forest beast.", "Salvaging the Scene",
          "Armelle has asked that you retrieve the cargo from a wagon that was attacked by some vicious denizen of the forest."),
 "M16b": ("Keitha frets over bandits prowling the woods.", "Salvaging the Scene", "or bandit cutthroats prowlin' the woods hereabouts."),
 "M16c": ("Keitha asks you to stand ready should Bentbranch need you.", "Salvaging the Scene",
          "She asks that you stand ready should Bentbranch Meadows have need of your skills."),
 # #17 Leia's Legacy
 "M17a": ("An egg has been stolen from Luquelot's stables.", "Leia's Legacy",
          "Luquelot informs you that [[Leia's Egg|an egg]] has been stolen from the stables."),
 "M17b": ("The thief seems to be a man from Luquelot's homeland of Ishgard, and fled to the Tam-Tara Deepcroft.", "Leia's Legacy",
          "The egg thief appears to be a man from Luquelot's homeland of [[Ishgard]]. Follow the thief's trail to [[The Tam-Tara Deepcroft|the Tam–Tara Deepcroft]], and retrieve Leia's egg."),
 "M17c": ("A moogle snatched the egg from the thief and ran with it.", "Leia's Legacy",
          "So I snatched it up as quickly as I could and made a run for it."),
 "M17d": ("You returned the egg to Bentbranch, to the ranch's relief.", "Leia's Legacy",
          "You have retrieved Leia's egg and returned it to Bentbranch Meadows, much to the relief of everyone at the ranch."),
 "M17e": ("Luquelot saw something alarming while you were away.", "Leia's Legacy",
          "Luquelot reveals that he bore witness to a most alarming sight while you were away."),
 # #18 Dread Is in the Air
 "M18a": ("Ixali dirigibles have been crossing the Twelveswood's borders at will, and Luquelot sends his sightings to Miounne.", "Dread Is in the Air",
          "you learn from Luquelot that [[Ixal]]i dirigibles have been crossing [[The Black Shroud|the Twelveswood]]'s borders seemingly at will."),
 "M18b": ("They fly over the sacred Guardian Tree, and the elementals have not objected.", "Dread Is in the Air",
          "the patch of sky directly above the Guardian Tree. … Yet the birdmen have been coming and going as they please, with nary a sign of protest from the guardians of the Twelveswood."),
 "M18c": ("Luquelot wonders whether the much-talked-about suspicious individual did something to the elementals.", "Dread Is in the Air",
          "many and more strange things have been occurring in the forest. Could it be that he did something to the elementals?"),
 "M18d": ("Miounne turns pale reading Luquelot's letter.", "Dread Is in the Air", "Miounne's face turns deathly pale as she reads"),
 # #19 To Guard a Guardian
 "M19a": ("Miounne warns that the Guardian Tree, sacred to Gridanians, may fall under Ixali attack, and sends a letter to Bowlord Lewin at the Seat of the First Bow.", "To Guard a Guardian",
          "Miounne tells you that [[the Guardian Tree]], held sacred by the [[Gridania]]ns, may fall under [[Ixal]]i attack. She gives you a letter and bids you deliver it to Bowlord [[Lewin]] at the [[Seat of the First Bow]]."),
 "M19b": ("Miounne bases her warning on Luquelot's observations.", "To Guard a Guardian",
          "Based on Luquelot's observations, the Ixal have designs on the Guardian Tree, and they mean to act soon."),
 "M19c": ("The Guardian Tree is the oldest living thing in the forest, held sacred by every forestborn Gridanian.", "To Guard a Guardian",
          "The tree is the oldest living thing in this ancient forest, and it is held sacred by every forestborn Gridanian."),
 "M19d": ("Lewin is Bowlord at the Seat of the First Bow in Quiver's Hold.", "To Guard a Guardian",
          "please see this letter to the hands of Bowlord Lewin, at the Seat of the First Bow in Quiver's Hold."),
 "M19e": ("Lewin suspects the masked devil who has long eluded them.", "To Guard a Guardian",
          "I cannot help but think this plot bears the mark of the masked devil who has eluded us for so long."),
 "M19f": ("The Ixali chieftain means to take a great crystal from the tree as an offering to Garuda.", "To Guard a Guardian",
          "From this tree, a great crystal we take! Unto Garuda, an offering we shall make!"),
 "M19g": ("Lewin leads his Quivermen in the tree's defense.", "To Guard a Guardian",
          "It is high time we reminded our Ixal guests why we Quivermen are to be feared!"),
 "M19h": ("The Ixal were repelled, and evidence suggests they acted under the masked mage's command.", "To Guard a Guardian",
          "You have succeeded in repelling the Ixal, whom evidence suggests were acting under the command of the mysterious masked mage."),
 "M19i": ("Yda and Papalymo join the fight against the masked mage.", "To Guard a Guardian", "I trust you won't object to our assistance!"),
 "M19j": ("The masked mage falls, lamenting that the wisdom of the Paragons was brought low by mortals.", "To Guard a Guardian",
          "That the wisdom of the Paragons should be brought low...by mere mortals..."),
 "M19k": ("Papalymo names them the Bringers of Chaos, or Ascians.", "To Guard a Guardian",
          "The Bringers of Chaos...or ''Ascians'', to give them their proper name."),
 "M19l": ("Papalymo says the Ascians have been manipulating the beast tribes.", "To Guard a Guardian",
          "It would seem our suspicions were correct─it is they who have been manipulating the beast tribes."),
 "M19m": ("Lewin confirms the fallen mage is the man who eluded them so long.", "To Guard a Guardian",
          "So ''this'' is the man who has eluded us for so long?"),
 "M19n": ("A black crystal was left at the scene, and the two scholars are from Sharlayan.", "To Guard a Guardian",
          "What is the significance of the black crystal that was left at the scene, and who exactly are the two scholars from [[Sharlayan]]?"),
 "M19o": ("Yda says she and Papalymo have been helping the Gridanians for years.", "To Guard a Guardian",
          "Despite what it looks like, Papalymo and I are actually ''helping'' the Gridanians. And we've been doing so for a good few years, too."),
 "M19p": ("Yda confirms they are Sharlayans.", "To Guard a Guardian", "Why, yes, we ''are'' Sharlayans!"),
 "M19q": ("Papalymo keeps some private suspicion to himself.", "To Guard a Guardian", "So I ''wasn't'' mistaken... … Nothing. Nothing at all."),
 "M19r": ("Kan-E-Senna comes to give thanks for the defense of the Guardian Tree.", "To Guard a Guardian",
          "I am come to express my gratitude for your valiant efforts before the Guardian Tree."),
 "M19s": ("Kan-E-Senna's solemn charge is to watch over all who call Gridania home.", "To Guard a Guardian",
          "My name is Kan-E-Senna, and it is my solemn charge to watch over all who call Gridania home."),
 "M19t": ("Kan-E-Senna invites you to serve as Emissary in the coming Greenbliss ceremony.", "To Guard a Guardian",
          "she invites you to serve as Emissary in the forthcoming Greenbliss ceremony."),
 # #20 Festive Endeavors
 "M20a": ("Lewin marvels that the Elder Seedseer chose you as Emissary.", "Festive Endeavors", "She chose you to play the role of Emissary, for gods' sakes!"),
 "M20b": ("The Emissary is a bridge between the people and the guardians of the Twelveswood.", "Festive Endeavors",
          "In the ceremony, the Emissary serves as a conduit—a bridge between the people and the guardians of the Twelveswood."),
 "M20c": ("Seldom have the non-forestborn been chosen as Emissary.", "Festive Endeavors", "Seldom in history have non-forestborn been chosen for the role"),
 "M20d": ("The timbermaster hands over a wooden lockbox with a sinister warning.", "Festive Endeavors",
          "The timbermaster has given you a [[Wooden Lockbox|wooden lockbox]], along with a sinister warning."),
 "M20e": ("The Monoa mask is carved from consecrated lumber of the Guardian Tree.", "Festive Endeavors",
          "is carved from consecrated lumber rendered up by [[the Guardian Tree]]."),
 # #21 Renewing the Covenant
 "M21a": ("At Greenbliss, Kan-E-Senna tells of the Warriors of Light, adventurers who fought for Eorzea five years ago, and you see a vision of their last stand at Carteneau.", "Renewing the Covenant",
          "At the ceremony, [[Kan-E-Senna|Kan-E-Senna]] tells you of the [[Warrior of Light|Warriors of Light]]─the [[adventurer]]s who fought for the survival of [[Eorzea]] five years ago. The tale of these brave souls triggers inside your mind a vision of their final stand at the [[Battle of Carteneau]]."),
 "M21b": ("No one can recall the Warriors of Light's names.", "Renewing the Covenant",
          "Yet when we try to recall their names, we find the pages of our memories are blank, as if bleached by the sun."),
 "M21c": ("Kan-E-Senna believes the Crystal has chosen you, and that the Echo resides within you.", "Renewing the Covenant",
          "The Crystal has chosen you for a purpose. … For the power of the Echo resides within you."),
 "M21d": ("At Carteneau, Kan-E-Senna urged the Admiral and the General to withdraw.", "Renewing the Covenant",
          "Admiral, General—we can do no more. We must give the order to withdraw."),
 "M21e": ("Eorzea's leaders went to take their place beside Archon Louisoix.", "Renewing the Covenant",
          "We go to take our place beside Archon Louisoix! To your positions!"),
 "M21f": ("A hidden voice exults at beholding Bahamut once more.", "Renewing the Covenant", "That I should live to behold Bahamut once more..."),
 "M21g": ("You collapsed mid-ceremony and woke at the Carline Canopy.", "Renewing the Covenant",
          "You collapsed in the middle of the ceremony—gave us all a good fright."),
 "M21h": ("Kan-E-Senna means to ask a favor, and no simple one.", "Renewing the Covenant",
          "It appears that Kan-E-Senna means to ask a favor of you, and no simple one at that."),
 # #22 The Gridanian Envoy
 "M22a": ("Kan-E-Senna makes you her personal envoy, to carry a missive to the Alliance's other two leaders.", "The Gridanian Envoy",
          "Appointing you her personal envoy, Kan-E-Senna bids you deliver a missive to the other two leaders of the [[Eorzean Alliance]]."),
 "M22b": ("The Eorzean Alliance is Gridania, Limsa Lominsa and Ul'dah.", "The Gridanian Envoy",
          "In addition to [[Gridania]], the Eorzean Alliance encompasses the city–states of [[Limsa Lominsa]] and [[Ul'dah]]."),
 "M22c": ("The missive proposes a memorial service on the anniversary of the Battle of Carteneau.", "The Gridanian Envoy",
          "In remembrance of them, a memorial service will soon be held upon the anniversary of the Battle of Carteneau."),
 "M22d": ("Miounne calls Limsa Lominsa the city of pirates and Ul'dah the jewel of the desert.", "The Gridanian Envoy",
          "They are, of course, Limsa Lominsa, city of pirates, and Ul'dah, jewel of the desert."),
 "M22e": ("Merlwyb is Admiral of Limsa Lominsa and commander of the Maelstrom.", "The Gridanian Envoy",
          "I am Merlwyb Bloefhiswyn, Admiral of Limsa Lominsa, and commander of the Maelstrom."),
 "M22f": ("Against the imperial threat, the city-states formed the Grand Companies and forged the Alliance anew.", "The Gridanian Envoy",
          "It was in answer to the imperial threat that the city-states formed the Grand Companies, and forged the Eorzean Alliance anew."),
 "M22g": ("The Empire's Meteor project meant to cast the lesser moon Dalamud down on Eorzea.", "The Gridanian Envoy",
          "intended to \"cleanse\" our realm by snatching the lesser moon, Dalamud, from the heavens and casting it down upon our heads."),
 "M22h": ("At Carteneau the elder primal Bahamut emerged from Dalamud.", "The Gridanian Envoy",
          "From inside the shell of Dalamud came a winged nightmare … 'Twas the elder primal Bahamut, bent on making an eighth hell of Eorzea."),
 "M22i": ("Merlwyb warns that the Empire has not forsaken its claim on Eorzea.", "The Gridanian Envoy",
          "Do not imagine that the Empire has forsaken its claim on Eorzea. The imperials crowd our borders, waiting to strike."),
 "M22j": ("Merlwyb accepts Kan-E-Senna's proposal.", "The Gridanian Envoy", "Aye, Kan-E-Senna has the right of it. I accept her proposal."),
 "M22k": ("The Empire still threatens Eorzea, with Legatus Gaius's XIVth Imperial Legion entrenched in the border regions.", "The Gridanian Envoy",
          "It appears the [[Garlean Empire]] still poses a grave threat to [[Eorzea]], with the [[XIVth Imperial Legion]], led by Legatus [[Gaius van Baelsar]], deeply entrenched in the border regions."),
 "M22l": ("Fifteen years ago an imperial fleet bound for Mor Dhona met a host of dragons and lost its flagship.", "The Gridanian Envoy",
          "Fifteen years since the imperial fleet set course for Mor Dhona, led by the Agrius, mightiest of all vessels. … Our invincible flagship was lost, and all hope of victory with her."),
 "M22m": ("Gaius says Eorzea has twice eluded the Empire, Meteor included.", "The Gridanian Envoy",
          "Twice now it has eluded the Empire's grasp. … For all the destruction it wrought, even Meteor, the Great Sin, failed to yield us control over it."),
 "M22n": ("Gaius holds that only Garlean rule can bring order to Eorzea.", "The Gridanian Envoy",
          "Only Garlean rule can bring order to Eorzea. It falls to us to deliver the misguided masses from their ignorance."),
 "M22o": ("The legion is preparing a large new campaign.", "The Gridanian Envoy",
          "We're in the midst of preparing for a new campaign, and a huge one at that!"),
 "M22p": ("Raubahn is General of Ul'dah's Immortal Flames.", "The Gridanian Envoy",
          "Welcome to the sultanate of Ul'dah. I am Raubahn Aldynn, General of the Immortal Flames."),
 "M22q": ("Raubahn warns the XIVth Legion is entrenched within their borders, under a legatus long ambitious of conquest.", "The Gridanian Envoy",
          "But the XIVth Imperial Legion is still entrenched within our borders. … And their commander, Legatus Gaius van Baelsar, has long harbored ambitions of conquest."),
 "M22r": ("Raubahn calls Eorzea a realm divided, an alliance in name only.", "The Gridanian Envoy",
          "We are a realm divided, adventurer. An alliance in name only."),
 "M22s": ("Raubahn agrees to the memorial.", "The Gridanian Envoy", "Kan-E will have her memorial."),
 # #23 Call of the Sea (Gridania)
 "M23a": ("An aide who once traveled with the Flame General to Limsa Lominsa knows Baderon, proprietor of the Drowning Wench.", "Call of the Sea (Gridania)",
          "I once accompanied the Flame General on an official visit to the seaside city-state, during which time I became acquainted with Baderon, the proprietor of the Drowning Wench."),
 "M23b": ("Baderon has need of a capable adventurer.", "Call of the Sea (Gridania)",
          "[[Baderon]], the proprietor of the [[Drowning Wench]] in [[Limsa Lominsa]], has need of a capable [[adventurer]]."),
 "M23c": ("Baderon warns that the job will be dangerous.", "Call of the Sea (Gridania)",
          "Baderon warns you that the job will entail considerable danger."),
}

# ---- Entities this era introduces ----------------------------------------------------------------------------------
ARC1, ARC2 = "evt-shadows-over-the-twelveswood", "evt-seedseers-envoy"
ENTITIES = {
 ARC1: "event", ARC2: "event",
 "char-miounne": "character", "char-galfrid": "character", "char-lewin": "character", "char-masked-mage": "character",
 "char-baderon": "character", "org-twin-adder": "organization", "loc-gridania": "location",
 "loc-limsa-lominsa": "location", "loc-uldah": "location",
 # existing entities, given their first presentations here
 "char-yda": "character", "char-papalymo": "character", "char-hydaelyn": "character", "org-ixal": "organization",
 "char-garuda": "character", "org-ascians": "organization", "char-kan-e-senna": "character", "char-merlwyb": "character",
 "char-raubahn": "character", "char-gaius": "character", "char-louisoix": "character", "org-garlean-empire": "organization",
 "org-eorzean-alliance": "organization", "org-maelstrom": "organization", "org-immortal-flames": "organization",
}

N1, N2 = "Shadows over the Twelveswood", "The Seedseer's Envoy"
# Shared openings, so each step's recap reads on its own.
L1 = "Ixali activity in the Twelveswood rose with sightings of an unknown individual, and a dead Ixali chieftain lay beside a ritual blade at Lifemend Stump. "
L2 = "A masked mage broke a Hearer's rite at Spirithold and eluded Yda and Papalymo, while Ixali activity rises with sightings of a stranger in the Twelveswood. "
L3 = "A shadowy stranger meddling with chocobos has been seen near the Matron's Lethe, and a masked mage broke a Hearer's rite at Spirithold, as Ixali activity rises. "

PRES = {
 # ---- arc entries ----
 ARC1: [
   P(S[4], None, "main", N1,
     "Ixali activity in the Twelveswood rose sharply with the first sightings of an unknown individual, so Galfrid sent you to Lifemend Stump. There a ritual blade was thrust into the stump beside a dead Ixali chieftain, and in a vision Hydaelyn bade you claim the Crystals of Light. "
     "Two scholars you met there, Yda and Papalymo, turned out to be friends of Gridania.",
     ["M4a", "M4c", "M4e", "M4h", "M4i"]),
   P(S[5], None, "main", N1,
     L1 + "Standing in for Galfrid's injured men, you gathered chigoe egg sacs: chigoes carry the Creeping Death, and one outbreak once killed a third of Gridania's Hyur.",
     ["M4a", "M4c", "M5a", "M5b", "M5c"]),
   P(S[6], None, "main", N1,
     L1 + "You recovered survey gear a startled Twin Adder recruit left in a cave. The Calamity has reshaped the forest, and the conjurer Pauline says its old maps can no longer be trusted.",
     ["M4a", "M4c", "M6a", "M6b", "M6c"]),
   P(S[7], None, "main", N1,
     L1 + "Anoles driven down from the mountains have been disturbing the conjurers' communion with the elementals, so you thinned them at Naked Rock and brought an egg back for a soldier's breakfast.",
     ["M4a", "M4c", "M7a", "M7b"]),
   P(S[8], None, "main", N1,
     "A towering shadow broke a Hearer's sacred rite at Spirithold, and inside you met a masked mage who loosed a clay golem on you. Yda and Papalymo arrived as you destroyed it, but the mage had eluded them again. "
     "Miounne asks that the tale be kept quiet until the Hearers decide, as Ixali activity rises with sightings of a stranger.",
     ["M8a", "M8c", "M8d", "M8h", "M4a"]),
   P(S[9], None, "main", N1,
     L2 + "Miounne has sent you on to Bentbranch Meadows, whose farmhands need help with chores around the chocobo ranch.",
     ["M8c", "M8d", "M4a", "M9a"]),
   P(S[10], None, "main", N1,
     L2 + "At Bentbranch a Qiqirn thief broke a chocobo egg, and on the soldier Roseline's orders you made an example of exactly four Qiqirn scramblers.",
     ["M8c", "M8d", "M4a", "M10a", "M10b"]),
   P(S[11], None, "main", N1,
     L2 + "Near the Matron's Lethe you cleared spreading mushrooms from the heavenspillar root, one of the few ways across the Central Shroud since the Calamity all but split it.",
     ["M8c", "M8d", "M4a", "M11a", "M11b", "M11c"]),
   P(S[12], None, "main", N1,
     "Ixali activity in the Twelveswood rises with sightings of an unknown individual, and a masked mage broke a Hearer's rite at Spirithold. Now Theodore has spotted a shadowy figure north of the Matron's Lethe, "
     "and by a still-warm campfire you found a bag that Roseline believes belongs to a stranger meddling with the chocobos. She has sworn to find this shadow.",
     ["M4a", "M8c", "M12a", "M12b", "M12c", "M12d"]),
   P(S[13], None, "main", N1,
     L3 + "Carrying Roseline's letter about the stranger, you warned the sentries from the Bannock to the Bentbranch stables, where the guard Bernard is sure the stranger has designs on the ranch.",
     ["M12c", "M8c", "M4a", "M13a", "M13b", "M13c"]),
   P(S[14], None, "main", N1,
     L3 + "Checking a peddler's tale of winged beasts on the road south of Bentbranch, you found a vulture nest hidden less than twenty yalms from the guard Lothaire's post.",
     ["M12c", "M8c", "M4a", "M14a", "M14b", "M14c"]),
   P(S[15], None, "main", N1,
     L3 + "The Hearer Leonnie has put off her voyage to stay at the Hedgetree, for the elementals murmur of a malevolent presence near the Tam-Tara Deepcroft.",
     ["M12c", "M8c", "M4a", "M15a", "M15b", "M15c"]),
   P(S[16], None, "main", N1,
     L3 + "You salvaged the cargo of a wagon a forest beast attacked, and Keitha of Bentbranch, uneasy about bandits in the woods, asks you to stand ready should the ranch need you.",
     ["M12c", "M8c", "M4a", "M16a", "M16b", "M16c"]),
   P(S[17], None, "main", N1,
     L3 + "When a thief stole a prized egg from Luquelot's stables, you followed him into the Tam-Tara Deepcroft, where a moogle had snatched it back, and returned it. Luquelot has since seen something alarming.",
     ["M12c", "M8c", "M4a", "M17a", "M17b", "M17c", "M17d", "M17e"]),
   P(S[18], None, "main", N1,
     L3 + "Luquelot reports Ixali dirigibles crossing the forest's borders at will and flying over the sacred Guardian Tree, and wonders whether the stranger has done something to the elementals. His letter turned Miounne pale.",
     ["M12c", "M8c", "M4a", "M18a", "M18b", "M18c", "M18d"]),
   P(S[19], None, "main", N1,
     "Ixali activity in the Twelveswood rose with sightings of a stranger, and Luquelot's sightings warned that the Ixal had designs on Gridania's sacred Guardian Tree. When they massed there to take its great crystal as an offering to Garuda, "
     "you helped repel them and, with Yda and Papalymo, brought down the masked mage commanding them. Papalymo named his kind the Ascians, who have been manipulating the beast tribes.",
     ["M4a", "M19b", "M19f", "M19h", "M19i", "M19k", "M19l"]),
 ],
 ARC2: [
   P(S[19], None, "main", N2,
     "After you helped defend Gridania's Guardian Tree from the Ixal and the masked mage who commanded them, the Elder Seedseer Kan-E-Senna came to the Seat of the First Bow to give thanks. "
     "She watches over all who call Gridania home, and she has invited you to serve as Emissary in the coming Greenbliss ceremony.",
     ["M19h", "M19r", "M19s", "M19t"]),
   P(S[20], None, "main", N2,
     "Kan-E-Senna, Gridania's Elder Seedseer, chose you as Emissary for the Greenbliss ceremony, a role seldom given to anyone not forestborn. Miounne explained that the Emissary is a bridge between the people and the Twelveswood's guardians, "
     "and the timbermaster handed over the Monoa mask, carved from the Guardian Tree's consecrated lumber, with a sinister warning.",
     ["M19t", "M20a", "M20c", "M20b", "M20d", "M20e"]),
   P(S[21], None, "main", N2,
     "As Emissary at Greenbliss, you heard Kan-E-Senna tell of the Warriors of Light, adventurers who fought for Eorzea five years ago and whose names no one can recall. She believes the Crystal has chosen you, and that the Echo resides within you. "
     "A vision showed you their last stand at Carteneau, where a hidden voice exulted over Bahamut, before you woke at the Carline Canopy.",
     ["M21a", "M21b", "M21c", "M21f", "M21g"]),
   P(S[22], None, "main", N2,
     "After the vision at Greenbliss, Kan-E-Senna made you her envoy, to carry word of a memorial for the fallen of Carteneau to the Alliance's other leaders. Admiral Merlwyb of Limsa Lominsa and General Raubahn of Ul'dah agreed, "
     "though both warn that the XIVth Imperial Legion, under Legatus Gaius, waits within Eorzea's borders. Raubahn calls the realm an alliance in name only.",
     ["M22a", "M22c", "M22j", "M22s", "M22k", "M22q", "M22r"]),
   P(S[23], None, "main", N2,
     "As Kan-E-Senna's envoy you carried word of a memorial for the fallen of Carteneau to Admiral Merlwyb and General Raubahn, who both agreed, and learned of the imperial legion entrenched on Eorzea's borders. "
     "In Ul'dah, an aide who once traveled with the General told you that Baderon of the Drowning Wench, in Limsa Lominsa, has a dangerous job for a capable adventurer.",
     ["M22a", "M22j", "M22s", "M22k", "M23a", "M23b", "M23c"]),
 ],
 # ---- new cast ----
 "char-miounne": [
   P(S[1], None, "main", "Miounne",
     "Proprietress of the Carline Canopy. She sets new members of the Adventurers' Guild three tasks to learn the fundamentals of adventuring, and urges them to build a reputation by helping citizens in need.",
     ["M1a", "M1b", "M1c"], ["Mother Miounne"]),
   P(S[8], None, "main", "Miounne",
     "Proprietress of the Carline Canopy, who looks after the adventurers of the guild there. After a towering shadow broke a Hearer's rite at Spirithold, she asked that the tale of walking statues be kept quiet until the Hearers make their will known.",
     ["M1a", "M8a", "M8h"], ["Mother Miounne"]),
   P(S[19], None, "main", "Miounne",
     "Proprietress of the Carline Canopy. Reading a Bentbranch rancher's report of Ixali airships over the Guardian Tree, she judged that the Ixal meant to attack the tree soon, and sent a warning to Bowlord Lewin at the Seat of the First Bow.",
     ["M1a", "M18a", "M18b", "M19b", "M19a"], ["Mother Miounne"]),
 ],
 "char-galfrid": [
   P(S[2], None, "main", "Galfrid",
     "An instructor at the Bannock, a training ground just outside Gridania where the soldiers of the Order of the Twin Adder are drilled. He trains the order's recruits, and holds that restoring the Calamity-scarred Twelveswood is a sacred duty for Gridanians.",
     ["M2a", "M2b", "M2c", "M2e"]),
   P(S[4], None, "main", "Galfrid",
     "Chief instructor at the Bannock, who trains the Order of the Twin Adder's recruits. He suspects that rising Ixali activity in the Twelveswood is tied to an unknown individual seen there, and judged the blade found beside a dead Ixal at Lifemend Stump to be an Ixali ritual weapon.",
     ["M3a", "M2b", "M4a", "M4c", "M4d"]),
 ],
 "char-lewin": [
   P(S[19], None, "main", "Lewin",
     "Bowlord at the Seat of the First Bow in Quiver's Hold, who led his Quivermen in defense of the Guardian Tree when the Ixal massed there. He had long hunted the masked mage who commanded them, and saw him fall.",
     ["M19d", "M19g", "M19h", "M19e", "M19m"], ["Bowlord Lewin"]),
 ],
 "char-masked-mage": [
   P(S[8], None, "main", "The masked mage",
     "A mysterious masked mage who loosed a clay golem in Spirithold, where a towering shadow had broken a Hearer's sacred rite. Yda and Papalymo are pursuing him, and he eluded them again; the Wood Wailers have promised to investigate.",
     ["M8a", "M8c", "M8d", "M8g"]),
   P(S[19], None, "main", "The masked mage",
     "A mysterious masked mage who, the evidence suggests, commanded the Ixal when they massed at the Guardian Tree, and whom Bowlord Lewin had long hunted. "
     "He fell there lamenting that the wisdom of the Paragons had been brought low, a black crystal was left at the scene, and Papalymo named his kind the Ascians.",
     ["M19h", "M19m", "M19j", "M19n", "M19k"]),
 ],
 "char-baderon": [
   P(S[23], None, "main", "Baderon",
     "Proprietor of the Drowning Wench in Limsa Lominsa. He has sent word that he needs a capable adventurer, and warns that the job will be dangerous.",
     ["M23a", "M23b", "M23c"]),
 ],
 "org-twin-adder": [
   P(S[2], None, "main", "The Order of the Twin Adder",
     "An order of Gridanian soldiers, drilled at the Bannock, a training ground just outside the city. Galfrid trains its recruits.",
     ["M2a", "M2b"], ["the Twin Adder"]),
   P(S[6], None, "main", "The Order of the Twin Adder",
     "An order of Gridanian soldiers, drilled at the Bannock under Galfrid. It makes no distinction between newcome adventurers and forestborn Gridanians, collects samples with the Wood Wailers so the Creeping Death can be tracked, "
     "and surveys the forest, whose geography the Calamity has dramatically altered.",
     ["M2a", "M2b", "M5e", "M5d", "M6b"], ["the Twin Adder"]),
 ],
 "loc-gridania": [
   P(S[1], None, "main", "Gridania",
     "A city whose Carline Canopy sets new members of the Adventurers' Guild their first tasks, and whose citizens often need an adventurer's help. Its markets lie at the heart of Old Gridania's commercial district.",
     ["M1a", "M1d", "M1e"]),
   P(S[2], None, "main", "Gridania",
     "A nation of the Twelveswood, a forest the Calamity of five years past left deeply scarred. Its people hold restoring the forest to be a sacred duty, and the Order of the Twin Adder drills its soldiers just outside the city.",
     ["M2c", "M2d", "M2e", "M2a"]),
   P(S[19], None, "main", "Gridania",
     "A nation of the Twelveswood, whose people hold restoring the Calamity-scarred forest to be a sacred duty. Its Guardian Tree, the oldest living thing in the forest, is held sacred by every forestborn Gridanian, "
     "and the Elder Seedseer, Kan-E-Senna, is charged with watching over all who call Gridania home.",
     ["M2e", "M19c", "M19s"]),
   P(S[22], None, "main", "Gridania",
     "A nation of the Twelveswood and one of the three city-states of the Eorzean Alliance, with Limsa Lominsa and Ul'dah. Its Elder Seedseer, Kan-E-Senna, watches over its people, and its Guardian Tree is held sacred by every forestborn Gridanian.",
     ["M22b", "M19s", "M19c"]),
 ],
 "loc-limsa-lominsa": [
   P(S[22], None, "main", "Limsa Lominsa",
     "A city-state of the Eorzean Alliance, known as the city of pirates. Its Admiral, Merlwyb, commands the Maelstrom.",
     ["M22b", "M22d", "M22e"]),
 ],
 "loc-uldah": [
   P(S[22], None, "main", "Ul'dah",
     "A city-state of the Eorzean Alliance: a sultanate known as the jewel of the desert, whose Immortal Flames are led by General Raubahn.",
     ["M22b", "M22d", "M22p"]),
 ],
 # ---- existing entities: earlier presentations, closed by the merge where the next one begins ----
 "char-yda": [
   P(S[4], None, "main", "Yda",
     "A Hyuran scholar from a distant land who, with Papalymo, has been with Gridania since before the Calamity. Gridania counts the pair among its staunchest allies, and they often assist the Gods' Quiver and the Wood Wailers.",
     ["M4i", "M4j"]),
   P(S[8], None, "main", "Yda",
     "A Hyuran scholar who, with Papalymo, has helped Gridania since before the Calamity and is surveying the Twelveswood. The pair are pursuing a masked mage, who loosed a clay golem in Spirithold and eluded them again.",
     ["M4j", "M8f", "M8c", "M8d"]),
   P(S[19], None, "main", "Yda",
     "A Sharlayan scholar who, with Papalymo, has spent years helping the Gridanians. The pair joined the fight against the masked mage at the Guardian Tree, and Papalymo named his kind the Ascians, who have been manipulating the beast tribes.",
     ["M19p", "M19o", "M19i", "M19k", "M19l"]),
 ],
 "char-papalymo": [
   P(S[4], None, "main", "Papalymo",
     "A Lalafellin scholar from a distant land who, with Yda, has been with Gridania since before the Calamity. Gridania counts the pair among its staunchest allies. Finding a dead Ixali chieftain deep in Gridanian territory, he judged that the beastmen may be acting under orders.",
     ["M4i", "M4j", "M4e"]),
   P(S[8], None, "main", "Papalymo",
     "A Lalafellin scholar who, with Yda, has helped Gridania since before the Calamity. At Spirithold, where a Hearer's rite was broken, the masked mage they pursue eluded them again; Papalymo saw the Hearer to safety and sent for his peers to finish the rite.",
     ["M4j", "M8a", "M8d", "M8e"]),
   P(S[19], None, "main", "Papalymo",
     "A Sharlayan scholar who, with Yda, has spent years helping the Gridanians. When the masked mage fell at the Guardian Tree lamenting the wisdom of the Paragons, Papalymo named his kind the Bringers of Chaos, or Ascians, who have been manipulating the beast tribes. "
     "He keeps some private suspicion to himself.",
     ["M19p", "M19o", "M19j", "M19k", "M19l", "M19q"]),
 ],
 "char-hydaelyn": [
   P(S[4], None, "main", "Hydaelyn",
     "A voice in a vision who names herself Hydaelyn. She says the Light that once shone throughout the realm has grown dim and Darkness has risen in its stead, and bids a crystal bearer lay claim to the Crystals of Light, which hold the power to banish it.",
     ["M4f", "M4g", "M4h"]),
 ],
 "org-ixal": [
   P(S[4], None, "main", "The Ixal",
     "A beast tribe whose activity in the Twelveswood has risen sharply since an unknown individual appeared there. A dead Ixali chieftain lay beside one of their ritual blades at Lifemend Stump, deep in Gridanian territory.",
     ["M4a", "M4c", "M4d", "M4e"]),
   P(S[18], None, "main", "The Ixal",
     "A beast tribe whose activity in the Twelveswood has risen since an unknown individual appeared there. Their dirigibles cross the forest's borders at will, flying over Gridania's sacred Guardian Tree.",
     ["M4a", "M18a", "M18b"]),
   P(S[19], None, "main", "The Ixal",
     "A beast tribe that massed at Gridania's Guardian Tree to take its great crystal as an offering to Garuda, acting, the evidence suggests, under the command of a masked mage. They were repelled.",
     ["M19f", "M19h"]),
 ],
 "char-garuda": [
   P(S[19], None, "main", "Garuda",
     "A power the Ixal revere. When they massed at Gridania's Guardian Tree, their chieftain vowed to take its great crystal as an offering unto Garuda.",
     ["M19f"]),
 ],
 "org-ascians": [
   P(S[19], None, "main", "The Ascians",
     "The Bringers of Chaos, as Papalymo names them, who he judges have been manipulating the beast tribes. The masked mage who commanded the Ixal at Gridania's Guardian Tree fell there lamenting the wisdom of the Paragons.",
     ["M19k", "M19l", "M19j", "M19h"], ["the Bringers of Chaos"]),
 ],
 "char-kan-e-senna": [
   P(S[19], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania, whose solemn charge is to watch over all who call it home. She gave thanks for the defense of the Guardian Tree, and invited its defender to serve as Emissary in the coming Greenbliss ceremony.",
     ["M19s", "M19r", "M19t"], ["the Elder Seedseer"]),
   P(S[21], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania. At Greenbliss she told of the Warriors of Light, the adventurers who fought for Eorzea five years ago and whose names no one can recall. "
     "At the Battle of Carteneau she urged Eorzea's other commanders to withdraw, saying they could do no more.",
     ["M19s", "M21a", "M21b", "M21d"], ["the Elder Seedseer"]),
   P(S[22], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania, one of the three leaders of the Eorzean Alliance. Five years after the Battle of Carteneau, she has proposed a memorial service for the fallen on its anniversary, and Admiral Merlwyb and General Raubahn have both agreed.",
     ["M19s", "M22a", "M22c", "M22j", "M22s"], ["the Elder Seedseer"]),
 ],
 "char-merlwyb": [
   P(S[22], None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa and commander of the Maelstrom. She fought at the Battle of Carteneau, where the elder primal Bahamut burst from Dalamud, and warns that the Empire has not forsaken its claim on Eorzea. "
     "She has accepted Kan-E-Senna's proposal of a memorial for the fallen.",
     ["M22e", "M22h", "M22i", "M22j"], ["Admiral Merlwyb", "the Admiral"]),
 ],
 "char-raubahn": [
   P(S[22], None, "main", "Raubahn",
     "General of Ul'dah's Immortal Flames. He warns that the Empire's XIVth Imperial Legion is still entrenched within the Alliance's borders under a legatus long ambitious of conquest, and calls Eorzea a realm divided, an alliance in name only. "
     "He has agreed to Kan-E-Senna's memorial.",
     ["M22p", "M22q", "M22r", "M22s"], ["General Raubahn"]),
 ],
 "char-gaius": [
   P(S[22], None, "main", "Gaius",
     "Legatus of the Empire's XIVth Imperial Legion, which remains entrenched in Eorzea's border regions. Eorzea has twice eluded the Empire, but he holds that only Garlean rule can bring order to it, and his legion is preparing a new campaign.",
     ["M22k", "M22m", "M22n", "M22o"]),
 ],
 "char-louisoix": [
   P(S[22], None, "main", "Louisoix",
     "An Archon who stood at the Battle of Carteneau: as the battle was lost, Eorzea's leaders went to take their place beside him. He is no longer with them, and the Admiral fears they will want for his wisdom.",
     ["M21e", "C44b"], ["Archon Louisoix"]),
 ],
 "org-garlean-empire": [
   P(S[22], None, "main", "The Garlean Empire",
     "An empire that has twice failed to take Eorzea: fifteen years ago its fleet met a host of dragons and lost its flagship, and its Meteor project, which meant to cast the lesser moon Dalamud down on the realm, failed to win it control. "
     "Its XIVth Imperial Legion is still entrenched in Eorzea's border regions.",
     ["M22l", "M22m", "M22g", "M22k"], ["the Empire"]),
 ],
 "org-eorzean-alliance": [
   P(S[22], None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's three city-states, Gridania, Limsa Lominsa and Ul'dah, forged anew against the imperial threat. Five years after the Battle of Carteneau, General Raubahn calls it an alliance in name only, "
     "and its leaders have agreed to a memorial for the battle's fallen.",
     ["M22b", "M22f", "M22r", "M22c", "M22j", "M22s"]),
 ],
 "org-maelstrom": [
   P(S[22], None, "main", "The Maelstrom",
     "Limsa Lominsa's Grand Company, commanded by Admiral Merlwyb: one of the Grand Companies the city-states formed in answer to the imperial threat.",
     ["M22e", "M22f"]),
 ],
 "org-immortal-flames": [
   P(S[22], None, "main", "The Immortal Flames",
     "Ul'dah's Grand Company, under General Raubahn: one of the Grand Companies the city-states formed in answer to the imperial threat.",
     ["M22p", "M22f"]),
 ],
}

# ---- Relationships -------------------------------------------------------------------------------------------------
# The -arr records are earlier intervals of a later era's relationship whose own claims come too late to ADJUST its
# start: each ends exactly where the later record begins.
RELS = [
 ("rel-galfrid-member-twin-adder", "char-galfrid", "member-of", "org-twin-adder", S[2], None, "main", ["M2b"]),
 ("rel-yda-aids-gridania", "char-yda", "aids", "loc-gridania", S[4], None, "main", ["M4i", "M4j"]),
 ("rel-papalymo-aids-gridania", "char-papalymo", "aids", "loc-gridania", S[4], None, "main", ["M4i", "M4j"]),
 ("rel-masked-mage-member-ascians", "char-masked-mage", "member-of", "org-ascians", S[19], None, "main", ["M19j", "M19k"]),
 ("rel-ixal-serves-garuda", "org-ixal", "serves", "char-garuda", S[19], None, "main", ["M19f"]),
 ("rel-kan-e-senna-leads-gridania", "char-kan-e-senna", "leads", "loc-gridania", S[19], None, "main", ["M19s"]),
 ("rel-merlwyb-leads-limsa-lominsa", "char-merlwyb", "leads", "loc-limsa-lominsa", S[22], None, "main", ["M22e"]),
 ("rel-gridania-member-eorzean-alliance", "loc-gridania", "member-of", "org-eorzean-alliance", S[22], None, "main", ["M22b"]),
 ("rel-limsa-lominsa-member-eorzean-alliance", "loc-limsa-lominsa", "member-of", "org-eorzean-alliance", S[22], None, "main", ["M22b"]),
 ("rel-uldah-member-eorzean-alliance", "loc-uldah", "member-of", "org-eorzean-alliance", S[22], None, "main", ["M22b"]),
 ("rel-merlwyb-leads-maelstrom-arr", "char-merlwyb", "leads", "org-maelstrom", S[22], "cp-msq-179", "main", ["M22e"]),
 ("rel-raubahn-leads-immortal-flames-arr", "char-raubahn", "leads", "org-immortal-flames", S[22], "cp-msq-200", "main", ["M22p"]),
 ("rel-gaius-member-empire-arr", "char-gaius", "member-of", "org-garlean-empire", S[22], "cp-msq-141", "main", ["M22k"]),
]

CASTS = {
 ARC1: [("char-galfrid", S[4], ["M4a"]), ("org-ixal", S[4], ["M4a"]), ("char-yda", S[4], ["M4i"]), ("char-papalymo", S[4], ["M4i"]),
        ("char-hydaelyn", S[4], ["M4h"]), ("char-masked-mage", S[8], ["M8c"]), ("char-miounne", S[8], ["M8h"]),
        ("char-lewin", S[19], ["M19e"]), ("char-garuda", S[19], ["M19f"]), ("org-ascians", S[19], ["M19k"])],
 ARC2: [("char-kan-e-senna", S[19], ["M19t"]), ("loc-gridania", S[19], ["M19s"]), ("char-miounne", S[20], ["M20b"]),
        ("char-lewin", S[20], ["M20a"]), ("org-eorzean-alliance", S[22], ["M22a"]), ("char-merlwyb", S[22], ["M22j"]),
        ("char-raubahn", S[22], ["M22s"]), ("char-gaius", S[22], ["M22k"]), ("org-garlean-empire", S[22], ["M22k"]),
        ("char-baderon", S[23], ["M23b"])],
}

ARCS = [
 ("arc-q1-shadows-over-the-twelveswood", ARC1, S[4], S[19]),
 ("arc-q2-seedseers-envoy", ARC2, S[19], S[23]),
]
ARC_NOTES = {
 "arc-q1-shadows-over-the-twelveswood": "MSQ #4 *Chasing Shadows* to #19 *To Guard a Guardian*: from the first word of the unknown individual tied to rising "
   "Ixali activity (M4a) to the masked mage's fall at the Guardian Tree, where Papalymo names the Ascians (M19h, M19k). #1–#3 are onboarding "
   "(cp-msq-1 is the timeline's first step, so no arc may start there). The errands of #5–#7, #9–#11 and #13–#17 sit inside it, each recap "
   "keeping the open threads in its first sentence. 16 steps.",
 "arc-q2-seedseers-envoy": "MSQ #19 *To Guard a Guardian* to #23 *Call of the Sea (Gridania)*: Kan-E-Senna's invitation to be Emissary (M19t), "
   "Greenbliss and the Carteneau vision, the envoy's journey to the Admiral and the General, and the hand-off to Baderon in Limsa Lominsa (M23b). "
   "It shares #19 with the first arc, as b2/b3 share #110: at #19 the default is the earlier arc, and the picker offers both.",
}

DECISIONS = [
 "Gridania chain: presentations state facts about each entity and never say \"you\", because they stay visible through the Limsa Lominsa and Ul'dah chains that follow in the timeline; only arc recaps address the player.",
 "Lahabrea is not named at #21: the flashback voice is tagged \"Lahabrea@???\", so the game never shows his name there. The recap says \"a hidden voice\".",
 "Bartholomew and Zanthael stay unnamed (\"an aide who once traveled with the General\"), so a later Ul'dah-chain entry for them is not named before it is visible.",
 "Gaius, Merlwyb, Raubahn, the Maelstrom and the Immortal Flames enter at #22, where the pages first name them; the -arr relationships carry their memberships until the later eras' records begin (#141, #179, #200).",
 "The masked mage is his own entry (no name is given on the pages); from #19 he is a member of the Ascians, as Papalymo names the Paragons he invokes.",
]
