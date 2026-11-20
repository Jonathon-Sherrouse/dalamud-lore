"""Atlas content for A Realm Reborn 2.0, MSQ #62 *Back from the Wood* to #101 *Battle Scars* (arc tag u).

Data only; build_pilot_content.py merges it (see docs/atlas/era-modules.md). Researched 2026-11-19 from the saved
Console Games Wiki wikitext in lanes A13–A16; every locator quotes the Journal, Steps or main dialogue verbatim.

Six arcs, from Minfilia's first word of Lahabrea to the eve of the feast at Costa del Sol that opens the accepted
"Road to Titan" arc (#103):
  u1 The Masked Man (#62–#65), u2 The Refugees' Trust (#66–#73), u3 The Youngbloods of Little Ala Mhigo (#74–#77),
  u4 Murders in the Shroud (#78–#84, both #80 paths), u5 Titan Reawakened (#85–#89), u6 A Feast at Costa del Sol
  (#90–#101).
Rules followed: first names only (Shamani, Brayflox, Merlwyb; Lady Amandine's house is named as a family, as
House Haillenarte is); "feast", never "banquet"; no later quest titles (so no "Lord of Crags" before #105); the
starting cities and Grand Companies are not referred to.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

def S(n):
    return f"cp-msq-{n}"

S80B = "cp-msq-80b"

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #62 Back from the Wood
 "M62a": ("The sylphs' matter is laid to rest, and Minfilia calls you back to the Waking Sands.", "Back from the Wood", "The Antecedent expresses relief that the matter of [[Ramuh]] has been laid to rest, and requests your presence at [[the Waking Sands]]."),
 "M62b": ("Gridania credits the Scions' mediation with averting a needless conflict with the sylphs.", "Back from the Wood", "Had the Scions of the Seventh Dawn not offered to mediate between our peoples, suspicion and doubt may well have led us into needless conflict."),
 "M62c": ("The sylph Noraxia comes to the Waking Sands as a friend, sent by the elder Frixio to help the Scions.", "Back from the Wood", "Is sent by elder one Frixio to help walking ones! … This one comes as a friend."),
 "M62d": ("Minfilia hears of a man named Lahabrea, in a red mask and black robes.", "Back from the Wood", "A man named Lahabrea, sporting a red mask and robed in black...?"),
 "M62e": ("The Ascians stayed hidden before the Calamity, and Minfilia is alarmed that they now cast off their secrecy.", "Back from the Wood", "Prior to the Calamity, the Ascians took great pains to remain hidden... Why would they choose to cast off their veil of secrecy now?"),
 "M62f": ("Minfilia means to use the lull in primal hostilities to learn all she can of Lahabrea and his designs.", "Back from the Wood", "We must take advantage of the present lull in primal hostilities and investigate this Lahabrea─learn all we can of him and his designs."),
 "M62k": ("Minfilia wonders what the appearance of the Ascians portends.", "Back from the Wood", "she cannot help but wonder at the appearance of the [[Ascians]]. What might their presence portend?"),
 "M62h": ("Minfilia is glad to see the Scions' family keep growing.", "Back from the Wood", "But it takes all kinds to make a family, and it pleases me to no end to see ours continue to grow."),
 "M62j": ("Minfilia has scarcely seen Alisaie of late.", "Back from the Wood", "I feel as if I have scarcely seen her in recent days."),
 # #63 Shadow of Darkness
 "M63a": ("Minfilia names Lahabrea an Ascian and sets you to uncover his motives.", "Shadow of Darkness", "We must delve further into the motivations of the masked man─the Ascian known as Lahabrea."),
 "M63b": ("Minfilia suspects the Ascians are behind the chaos racking the realm.", "Shadow of Darkness", "I should not be surprised if these beings are behind the chaos that racks the realm."),
 "M63c": ("Minfilia asked each Grand Company for help, and the Immortal Flames answered with word of a possible sighting.", "Shadow of Darkness", "Earlier, I sent word to each Grand Company to solicit cooperation. The Immortal Flames responded to the effect that they have information on a potential sighting."),
 "M63d": ("Flame Commander Swift receives you at the Hall of Flames in Ul'dah.", "Shadow of Darkness", "Go speak with Flame Commander Swift at the Hall of Flames in Ul'dah to inquire further."),
 "M63e": ("A Brass Blade at Highbridge reported the masked man, then was killed by Qiqirn.", "Shadow of Darkness", "According to Commander Swift, a [[The Brass Blades|Brass Blade]] stationed at [[Highbridge]] has reported seeing a suspicious masked man, but the sentry has since died in the line of duty. … I'm afraid he died not two days ago, slain by a marauding horde of Qiqirn."),
 "M63f": ("Swift sends you to the Highbridge merchant Hihibaru, who hints he knows of the masked man.", "Shadow of Darkness", "speak with a merchant named [[Hihibaru]]. … Hihibaru hints at knowing of the masked man, but his mannerisms do not instill you with much confidence."),
 # #64 Highbridge Times
 "M64a": ("Endless beastman raids keep travelers away from Highbridge.", "Highbridge Times", "But thanks to the nigh-endless beastman raids, folk are too afraid to come within a malm of here."),
 "M64b": ("The masked man has been seen elsewhere about Thanalan too.", "Highbridge Times", "Seems he's been appearing not only around Highbridge, but elsewhere about Thanalan, too."),
 "M64c": ("Hihibaru suspects someone is orchestrating the Qiqirn raids and inciting the beast tribes.", "Highbridge Times", "The Qiqirn raids are so constant, so organized, we're beginning to suspect that someone is orchestrating it all. … Hihibaru suspects that someone may be inciting the [[Tribes|beast tribes]]."),
 "M64d": ("Hihibaru promises to watch for the masked man.", "Highbridge Times", "I promise to keep an eye out for your masked man."),
 # #65 Where There Is Smoke
 "M65a": ("Hihibaru saw a masked man meeting beastman accomplices in secret.", "Where There Is Smoke", "Hihibaru claims to have witnessed a masked man meeting his [[beastman]] accomplices in secret."),
 "M65b": ("Your smoke draws a bandit carrying a scroll marked with Rhalgr, the Destroyer.", "Where There Is Smoke", "The smoldering coal gives rise to a column of smoke, which serves to summon [[Corpse Brigade Footsoldier|a bandit]]. … bearing [[Rhalgr|the mark of Rhalgr, the Destroyer]]"),
 "M65c": ("Rhalgr is the guardian deity of Ala Mhigo, which is under Garlean rule.", "Where There Is Smoke", "Rhalgr is the guardian deity of [[Ala Mhigo]], which is currently under [[Garlean Empire|Garlean]] rule."),
 "M65d": ("Lahabrea seems to have secret ties to the Qiqirn and the Ala Mhigans.", "Where There Is Smoke", "It would seem that Lahabrea has clandestine connections not only with the [[Qiqirn]], but also the [[Ala Mhigo|Ala Mhigans]]."),
 # #66 On to Little Ala Mhigo
 "M66a": ("Hihibaru sends you to Little Ala Mhigo, a lawless place where his daughter Hihira lives.", "On to Little Ala Mhigo", "His daughter, a lass named [[Hihira]], has taken up residence there … And for all intents and purposes, it's a lawless place."),
 "M66b": ("Gundobald leads the refugee settlement.", "On to Little Ala Mhigo", "She recommends you speak with a man named [[Gundobald]], the leader of the refugee settlement."),
 "M66c": ("Gundobald turns you away.", "On to Little Ala Mhigo", "You are not welcome here. Begone."),
 # #67 Tea for Three
 "M67a": ("Gisilbehrt of the Immortal Flames heads security at Little Ala Mhigo.", "Tea for Three", "I'm Gisilbehrt, head of security here at Little Ala Mhigo. … Gisilbehrt of [[the Immortal Flames]] believes that one of his lookouts may have seen the man you seek."),
 "M67b": ("A lookout saw a masked figure talking with Ala Mhigans.", "Tea for Three", "he was talking with some Ala Mhigans. I assumed he was one of them."),
 "M67c": ("Lahabrea seems connected to Little Ala Mhigo.", "Tea for Three", "it would seem that [[Lahabrea]] is in some way connected to [[Little Ala Mhigo]]."),
 "M67d": ("The refugees trust no one but themselves, and you will need their cooperation.", "Tea for Three", "Owing to their hardships, the refugees don't trust anyone but themselves. … seems to me you'll need the cooperation of the Ala Mhigans."),
 # #68 Foot in the Door
 "M68a": ("Gundobald belongs to the Ala Mhigan Resistance.", "Foot in the Door", "Gundobald belongs to the Ala Mhigan Resistance, so your best bet would be someone who's part of the same crew."),
 "M68b": ("The Ala Mhigans' shared purpose is freeing their home from the Garleans.", "Foot in the Door", "That purpose is, of course, the liberation of their home from the Garleans."),
 "M68c": ("The city-states cannot take in all the displaced, and Minfilia thinks only reclaiming their homeland would last.", "Foot in the Door", "none of the three city-states have the means to take in all those who were displaced. … I fear that nothing short of reclaiming their homeland would be a lasting solution."),
 "M68d": ("There is an Ala Mhigan native among the Scions.", "Foot in the Door", "there is an Ala Mhigan native among the Scions. I should be pleased to introduce him to you."),
 "M68e": ("The refugees will trust you only if a respected compatriot vouches for you.", "Foot in the Door", "the best way to win that trust is to get a compatriot of theirs─someone they respect─to vouch for you."),
 # #69 Meeting with the Resistance
 "M69a": ("Haribehrt joined the Scions hoping to find a way to free his homeland.", "Meeting with the Resistance", "He joined our cause in the hopes that he might find a way to liberate his homeland."),
 "M69b": ("Haribehrt left the Ala Mhigan Resistance for the Scions, and his old comrades shun him.", "Meeting with the Resistance", "I used to be a member of the [[Ala Mhigan Resistance]], you see, but I left in favor of joining the Scions. … I abandoned my comrades, and they'll have nothing to do with me."),
 "M69c": ("At Quarrymill, an angry Albreda sends you to Meffrid, a captain of the Resistance.", "Meeting with the Resistance", "Take yourself to [[Quarrymill]] in the [[South Shroud]], and introduce yourself to a woman named [[Albreda]]. … Mentioning Haribehrt's name to Albreda earns you an angry outburst. Nonetheless, she relents to your request and refers you to a man named [[Meffrid]], a captain of the Ala Mhigan Resistance."),
 # #70 Killing Him Softly
 "M70a": ("Gallien, one of Meffrid's men, has a festering wound.", "Killing Him Softly", "His wound's gone an' festered, an' he's burnin' up!"),
 "M70b": ("Quarrymill's villagers refused help even when Meffrid begged.", "Killing Him Softly", "I asked the villagers for aid─got on my knees and ''begged''─but they refused to lift a finger!"),
 "M70c": ("The Hearer Charline denies the Ala Mhigans' petition, saying only the elementals may grant it.", "Killing Him Softly", "This authority belongs only to the elementals, eternal guardians of the Twelveswood. … Alas, the Ala Mhigans' petition has been denied."),
 # #71 Helping Horn
 "M71a": ("Meffrid tries an old Ala Mhigan remedy of long antelope horn.", "Helping Horn", "In my homeland, long antelope horn is a traditional remedy with poison-purging properties."),
 "M71b": ("Buscarron, once saved by the same remedy from an Ala Mhigan friend, makes the medicine.", "Helping Horn", "An Ala Mhigan friend once used it to treat my festering wound, years and years ago. Safe to say he saved my life."),
 "M71d": ("Meffrid sends you to Buscarron, proprietor of Buscarron's Druthers, who is said never to turn away folk in need.", "Helping Horn", "They said he never turns away folk in need, no matter where they're from. … He bids you take them to [[Buscarron's Druthers]] in order to have the proprietor, [[Buscarron]], make the [[medicine]] in his stead."),
 "M71c": ("Gallien's chances improve, and Meffrid's brothers in the Resistance begin to trust you.", "Helping Horn", "Thanks to your aid, [[Gallien]] now has a much improved chance of survival. Slowly but surely, you are winning the trust of Meffrid and his brothers in the [[Ala Mhigan Resistance]]."),
 # #72 He Ain't Heavy
 "M72a": ("Gallien leaves Quarrymill alone so as not to burden his fellows.", "He Ain't Heavy", "decided to leave Quarrymill of his own volition, in an attempt to not burden his fellows any longer."),
 "M72b": ("Meffrid reminds Gallien of their oath to return to Ala Mhigo together or not at all.", "He Ain't Heavy", "We'll set foot on Ala Mhigan soil again─''together''─or not at all!"),
 "M72c": ("Gallien is expected to make a full recovery.", "He Ain't Heavy", "Gallien's expected to make a full recovery."),
 # #73 Come Highly Recommended
 "M73a": ("Meffrid gives you a letter of introduction to Gundobald.", "Come Highly Recommended", "He provides you with a [[Meffrid's Recommendation|letter of introduction]], and instructs you to show it to [[Gundobald]] at [[Little Ala Mhigo]]."),
 "M73b": ("Gundobald mentored Meffrid when he joined the Resistance.", "Come Highly Recommended", "The old bear was my mentor when I first joined the Resistance."),
 "M73c": ("Gundobald casts aside his mistrust and will tell you what he knows of the masked stranger.", "Come Highly Recommended", "Thanks to Meffrid's letter, Gundobald casts aside his mistrust and offers you his hand in friendship. … I know of this masked stranger you seek, and will tell you what I can"),
 # #74 The Bear and the Young'uns' Cares
 "M74a": ("Some youths of Little Ala Mhigo are meeting the masked man in secret.", "The Bear and the Young'uns' Cares", "it seems that some of our youngbloods are meeting him in secret."),
 "M74b": ("Something is afoot among the youths, and Lahabrea may be involved.", "The Bear and the Young'uns' Cares", "Judging by the youths' reactions, it would seem that something is indeed in the offing, and [[Lahabrea]] may be involved."),
 "M74c": ("Two decades ago Gundobald and his brothers rose against Ala Mhigo's despot, and it cost them their freedom.", "The Bear and the Young'uns' Cares", "Two decades ago, that same anger drove me and my brothers to rise against the despot who ruled Ala Mhigo. … but it cost us our freedom."),
 "M74d": ("Blinded by hate, the rebels danced to the Empire's tune, and Ala Mhigo fell.", "The Bear and the Young'uns' Cares", "Blinded by our hate, we didn't realize that we had been dancing to the Empire's tune. … Ala Mhigo had fallen."),
 "M74e": ("Gundobald fears the youths will commit some great folly.", "The Bear and the Young'uns' Cares", "Gundobald fears that the youths may be involved in something they do not fully understand, and are likely to commit some great folly."),
 # #75 Wilred Wants You
 "M75a": ("Wilred is something of a leader among the young people.", "Wilred Wants You", "Lad's something of a leader among the young ones here."),
 "M75b": ("Wilred's invitation is a trap, and you overpower him and his cronies.", "Wilred Wants You", "the rendezvous turns out to be a trap. Wilred and his cronies fall upon you, but you succeed in overpowering them."),
 "M75c": ("Wilred's group means to obtain the power to bring down the Empire and reclaim their homeland.", "Wilred Wants You", "We're going to obtain the power to bring down the Empire, and with it we'll reclaim our homeland!"),
 "M75d": ("Gundobald fears the youths will harm others or themselves.", "Wilred Wants You", "Left to their own devices, the young fools are like to harm others, if not themselves."),
 # #76 Big Trouble in Little Ala Mhigo
 "M76b": ("Wilred's friends plotted to summon Rhalgr with crystals stolen from an Amalj'aa stronghold.", "Big Trouble in Little Ala Mhigo", "It seems that Wilred and his friends have been plotting to summon [[Rhalgr]]. … they seek to infiltrate an [[Amalj'aa]] stronghold and steal the [[beastmen]]'s cache of [[crystals]]."),
 "M76c": ("The masked stranger first gave the youths the idea of summoning Rhalgr.", "Big Trouble in Little Ala Mhigo", "Wilred reveals that it was the masked stranger who first prompted him and his friends to entertain the notion of summoning Rhalgr."),
 "M76d": ("The masked man told them they could defeat the Empire by summoning Rhalgr.", "Big Trouble in Little Ala Mhigo", "The masked man told us we could defeat the Empire if we summoned Rhalgr!"),
 "M76e": ("Wilred's plan fails, and with it his hope of reclaiming his homeland.", "Big Trouble in Little Ala Mhigo", "Wilred's plan has come to naught, as have his hopes of reclaiming his homeland."),
 "M76f": ("Gundobald tells Wilred he owes his life to you, an outsider.", "Big Trouble in Little Ala Mhigo", "never forget that you owe it to this adventurer─an ''outsider''."),
 # #77 Back to Square One
 "M77a": ("Gundobald's people have nothing more to tell of the masked stranger.", "Back to Square One", "There is no more that Gundobald and his people can tell you of the masked stranger."),
 "M77b": ("Minfilia sees Ascian deception in the plot.", "Back to Square One", "Precisely the kind of deception the Ascians would employ..."),
 "M77c": ("Minfilia believes some of the land's ills come from a malign will.", "Back to Square One", "While many of the ills that ail the land can be attributed to the Calamity, some are being brought about by a malign will."),
 "M77d": ("Minfilia promises to look further into the matter.", "Back to Square One", "Thanking you for your efforts, she promises to look further into the matter."),
 "M77e": ("Gundobald prays you will end the masked stranger, for the young ones who died by his words.", "Back to Square One", "I pray that you'll find and put a swift end to the creature─for the sake of the young ones who died by his poisoned words."),
 # #78 Terror at Fallgourd
 "M78a": ("Someone fitting Lahabrea's description has been sighted in the North Shroud.", "Terror at Fallgourd", "An individual fitting Lahabrea's description has been sighted in the North Shroud."),
 "M78b": ("The sighting follows a series of mysterious deaths there.", "Terror at Fallgourd", "This sighting comes in the wake of a series of mysterious deaths in the selfsame area."),
 "M78c": ("Noraxia tells you that a miner, Medrod, saw a masked character in the wood.", "Terror at Fallgourd", "Noraxia tells you that a miner named [[Medrod]] witnessed an unsavory masked character in the wood."),
 "M78d": ("Medrod saw the masked man with a winged creature that was all eyeball and teeth.", "Terror at Fallgourd", "He had a hideous fiend in tow, a winged creature that was all eyeball and jagged teeth."),
 "M78e": ("The masked man appears connected to the mysterious deaths.", "Terror at Fallgourd", "it appears that this individual is indeed connected to the recent spate of mysterious deaths."),
 "M78f": ("Aideen and Ivaurault offer to help.", "Terror at Fallgourd", "If that's the case, we'll help you in whatever way we can!"),
 # #79 Ziz Is So Ridiculous
 "M79a": ("The victims were all found with their faces torn to shreds.", "Ziz Is So Ridiculous", "all the victims were found with their faces torn to shreds."),
 "M79b": ("Aideen rules out the ziz and turns back to the masked man and his winged eyeball.", "Ziz Is So Ridiculous", "Aideen strikes ziz from her list of suspects, and turns her attention once more towards the masked man and his winged eyeball."),
 # #80 Seeing Eye to Winged Eye
 "M80a": ("Ivaurault also saw the winged eyeball, at the same moment as Medrod.", "Seeing Eye to Winged Eye", "I have been keeping this to myself, lest I worsen Medrod's paranoia, but I, too, have seen the winged eyeball. … my sighting took place precisely the same time as Medrod's."),
 "M80b": ("A monstrous banemite attacks you where he saw it, and Ivaurault begins to doubt himself.", "Seeing Eye to Winged Eye", "Instead of the winged eyeball, a [[Heavy Banemite|monstrous banemite]] appears, and you are forced to defend yourself. … he wonders whether he only imagined seeing the winged eyeball."),
 # #80 Rock of Rancor (the other #80 path)
 "M80ba": ("All the victims have been comely maidens.", "Rock of Rancor", "It appears ''all'' the victims have been comely maidens."),
 "M80bb": ("A rumored rock of rancor proves to hold ordinary crystals, nothing to do with the masked stranger.", "Rock of Rancor", "her rancor went into the great big rock southwest of here, causing it to flash and moan. … Nothing to do with the masked stranger."),
 # #82 Power of Deduction
 "M82a": ("Ivaurault is now sure he saw a winged eyeball, and the three friends leave the investigating to you.", "Power of Deduction", "While uncertain for a time, [[Ivaurault]] is now convinced that it was a winged eyeball that he encountered at the rocky area to the west. … The three friends would leave the task of investigating to the expert─you."),
 "M82b": ("You find another victim and bring the body to Aethelmaer.", "Power of Deduction", "As the three friends had feared, there was indeed another victim. … show it to [[Aethelmaer]]."),
 "M82c": ("Identical deaths in the Central Shroud; the winged eyeball seems to be moving the bodies.", "Power of Deduction", "Identical deaths have been reported in the Central Shroud. … The creature appears to be ''moving'' the bodies, but to what end, none can say."),
 "M82d": ("A button engraved with a lily is found on this victim, as on an earlier one.", "Power of Deduction", "A cursory examination of the body turns up a [[Lily Button|button engraved with a lily motif]]. A similar object had been discovered upon an earlier victim."),
 # #83 Secret of the White Lily
 "M83a": ("Aethelmaer entrusts you with the lily button, the best lead in the murders.", "Secret of the White Lily", "Aethelmaer entrusts you with the [[Lily Button|lily button]], thus far the most promising lead in the murder investigation"),
 "M83b": ("Ceinguled recalls Ursandel wearing an identical button.", "Secret of the White Lily", "Ceinguled recalls having seen a man named [[Ursandel]] wearing an identical button upon the breast of his jacket."),
 "M83c": ("Ursandel knows the sigil as the Dartancours family's.", "Secret of the White Lily", "Ursandel instantly recognizes the sigil as that of the old and proud Dartancours family."),
 "M83d": ("Ursandel will tell the truth of the deaths if you promise to end his lady's madness.", "Secret of the White Lily", "I shall reveal to you the truth of the deaths, but on one condition: you promise to put an end to my lady's madness and free her from her torment."),
 # #84 Skeletons in Her Closet
 "M84a": ("Ursandel once waited upon Lady Amandine, mistress of the Dartancours household.", "Skeletons in Her Closet", "During that time, I had the honor of waiting upon Lady Amandine, mistress of the household."),
 "M84b": ("Disfigured in the Calamity, Amandine held rites of rejuvenation at masked men's urging, spilling maiden blood.", "Skeletons in Her Closet", "how [[Lady Amandine]], his once beautiful mistress, was disfigured in [[the Calamity]], and how she subsequently began to hold rites of rejuvenation at the urging of masked men. It would seem these rites involve the spilling of maiden blood."),
 "M84c": ("You defeat Amandine, and two masked men appear who seem to have masterminded the atrocities.", "Skeletons in Her Closet", "No sooner have you defeated Lady Amandine than two masked men appear, their ominous exchange suggesting that it was they who masterminded the atrocities committed within the manor."),
 "M84d": ("The two Ascians came to take your measure for Master Lahabrea, and then leave.", "Skeletons in Her Closet", "we came here not to play, but to take the measure of your strength for Master Lahabrea."),
 "M84f": ("Ursandel will surrender himself for keeping silent.", "Skeletons in Her Closet", "I will surrender myself to the authorities and accept whatever punishment they deem just."),
 "M84g": ("Minfilia is sure the Ascians have begun to move in earnest, to what end she cannot say.", "Skeletons in Her Closet", "It is beyond doubt, then─the Ascians have begun to move in earnest. Would that we knew to what end."),
 "M84h": ("Minfilia will urge the three nations to heighten their vigil.", "Skeletons in Her Closet", "We must needs alert the three nations to the presence of this elusive enemy, and recommend that they heighten their vigil."),
 "M84i": ("The Ascians call you the Bringer of Light.", "Skeletons in Her Closet", "Fare you well, Bringer of Light."),
 # #85 Wrath of the Titan
 "M85a": ("The Maelstrom asks the Scions to slay Titan, summoned by a tribe of kobolds near Limsa Lominsa.", "Wrath of the Titan", "[[The Maelstrom]] has requested that [[the Scions]] slay the [[primal]] [[Titan]], who has been summoned by a tribe of [[kobolds]] who reside near [[Limsa Lominsa]]."),
 "M85b": ("The only force known to have bested Titan, the Company of Heroes, disbanded five years ago.", "Wrath of the Titan", "the only force known to have bested him─the modestly named “Company of Heroes”─disbanded five years since"),
 "M85c": ("Admiral Merlwyb pledges the Maelstrom's full support.", "Wrath of the Titan", "you are received by Admiral [[Merlwyb]] Bloefhiswyn herself, who pledges the full support of the Maelstrom in the forthcoming operation."),
 "M85d": ("Y'shtola recalls the pact that kept each to its own lands; Merlwyb owns that the Lominsans broke it.", "Wrath of the Titan", "Did not the thalassocracy make a pact with the beastmen that each would keep to their own lands, and that no blood would be shed? … And the wrong is mine. Freely do I claim it."),
 "M85e": ("The kobolds gather crystals as fodder for their primal.", "Wrath of the Titan", "Crystals. Fodder for their fell primal."),
 "M85f": ("Y'shtola proposes learning about Titan from former members of the Company of Heroes.", "Wrath of the Titan", "[[Y'shtola]] proposes that you learn more about your foe by speaking to former members of the [[Company of Heroes]]─the famous band of mercenaries who defeated the dread primal once before."),
 "M85g": ("Minfilia sends Y'shtola with you.", "Wrath of the Titan", "May I ask that of you, Y'shtola? … I never thought it in question."),
 "M85h": ("When Titan rose before, Limsa Lominsa turned to the Company of Heroes.", "Wrath of the Titan", "In the past, when Titan rose to threaten the peace, it was to the Company of Heroes we turned."),
 "M85i": ("Trachtoum calls himself the best axeman of the Company of Heroes.", "Wrath of the Titan", "Your search leads you to [[Trachtoum]], the self-proclaimed “best axeman” of the Company of Heroes."),
 "M85j": ("Minfilia pledges the Scions' full support.", "Wrath of the Titan", "You may count on the full support of the Scions of the Seventh Dawn."),
 "M85k": ("Merlwyb turns to the Scions as Limsa's best hope.", "Wrath of the Titan", "So it is that we turn now to the Scions of the Seventh Dawn, confident in the belief that you are Limsa's best hope."),
 "M85m": ("Y'shtola speaks of the Grand Company's reformation, years after Titan last struck.", "Wrath of the Titan", "Years before the Grand Company's reformation, two primals, Leviathan and Titan, chanced to converge upon the seawall"),
 "M85l": ("The Maelstrom has long kept watch on the beast tribes, the kobolds above all.", "Wrath of the Titan", "The Maelstrom has kept a watchful eye upon the beast tribes─and the kobolds in particular─ever since."),
 # #86 Tales from the Tidus Slayer
 "M86a": ("Trachtoum withholds the Company's secret strategy unless you clear a rats' nest.", "Tales from the Tidus Slayer", "refuses to reveal [[Company of Heroes|the Company]]'s secret strategy─that is, unless you destroy a nest of wild rats"),
 "M86b": ("Trachtoum used you to do work he had been given.", "Tales from the Tidus Slayer", "It would appear that Trachtoum used you to handle work he himself had been tasked to do."),
 # #87 Hungry Hungry Goobbues
 "M87a": ("Trachtoum doubts you can face a primal, and even slaying a goobbue does not win his confidence.", "Hungry Hungry Goobbues", "Trachtoum is concerned that you lack the strength to face a [[primal]] in battle. … Your deeds serve to shock the veteran [[marauder]], but they are not enough to earn his confidence."),
 "M87b": ("The goobbue you slew had been harassing the millers.", "Hungry Hungry Goobbues", "that goobbue that was harassin' the millers is dead?"),
 # #88 The Lominsan Way
 "M88a": ("Bested in a contest, Trachtoum admits he was never in the Company; one of its former captains works at Costa del Sol.", "The Lominsan Way", "After besting Trachtoum in a boulder-breaking contest, you discover that the marauder was never a member of the [[Company of Heroes]]. However, he tells you that one of the Company's former captains now works at [[Costa del Sol]]."),
 "M88b": ("Wheiskaet says the Company's victories were bought with lifeblood, and Titan took some of its best.", "The Lominsan Way", "each victory was bought with the lifeblood of brave men and women. … but he took from us some of our very best."),
 "M88c": ("Wheiskaet oversees security for Master Gegeruju's estates.", "The Lominsan Way", "I oversee security for Master Gegeruju's estates."),
 "M88d": ("Wheiskaet will not send you into O'Ghomoro on a whim; you must complete his challenges.", "The Lominsan Way", "But I will not send you into O'Ghomoro on a whim. … you must yet again prove yourself by completing Wheiskaet's challenges."),
 "M88e": ("Y'shtola asks you to undertake his task alone while she sees to other preparations.", "The Lominsan Way", "Forgive me, but I must ask you to undertake this task alone. I will use the time to see to the remaining preparations."),
 "M88f": ("The Scions lack only the knowledge of how to enter Titan's lair.", "The Lominsan Way", "We lack only the knowledge of how to enter Titan's lair."),
 # #89 Nix That
 "M89a": ("Wheiskaet tests you with a simple task first.", "Nix That", "Before he bothers giving you a truly demanding task, Wheiskaet would first have you attend to a simple one."),
 "M89b": ("A former employee who falsely claimed Company service has made Wheiskaet wary of strangers.", "Nix That", "He claimed to have served in the Company of Heroes, but I knew for a fact he did not. … Wheiskaet explains that a recent incident with a former employee has forced him to treat strangers with greater caution."),
 "M89c": ("Wheiskaet is ready to set you a real challenge.", "Nix That", "he is now willing to give you a challenge as befits your talents."),
 "M89d": ("You slay a nix near Costa del Sol as proof.", "Nix That", "You dispatch the slimy creature with great fanfare and sever one of [[Nix Leg|its legs]] as proof of your kill."),
 # #90 A Modest Proposal
 "M90a": ("Master Gegeruju will welcome two distinguished visitors to Costa del Sol with a feast, and you are to gather its ingredients.", "A Modest Proposal", "Two highly distinguished individuals are scheduled to visit [[Costa del Sol]], and Master [[Gegeruju]] wishes to welcome them with an elaborate banquet. Wheiskaet bids you assist in this endeavor by bringing him the ingredients required for this exotic feast."),
 "M90b": ("Many of Wheiskaet's old mercenaries still live and will guide you.", "A Modest Proposal", "Many of the mercenaries who once served under my command still live, and they will guide you in your quest."),
 "M90c": ("Landenel knows you as the one who would challenge Titan, but will give only information.", "A Modest Proposal", "So this is the one who would challenge Titan. … From me you will receive only information."),
 "M90d": ("The first ingredient is a giant adamantoise's egg.", "A Modest Proposal", "You learn that the first ingredient is the [[Adamantoise Egg|egg of a giant adamantoise]]."),
 "M90e": ("Landenel is at Camp Tranquil in the South Shroud.", "A Modest Proposal", "To obtain the first ingredient, you must seek out [[Landenel]] at [[Camp Tranquil]] in the [[South Shroud]]."),
 # #91 Trial by Turtle
 "M91a": ("Landenel served with the Company and keeps that a secret.", "Trial by Turtle", "See, I don't regret my time spent with the Company in the slightest. … this business between you, me, and the captain must remain a secret."),
 "M91b": ("You take the egg despite the mother adamantoise, and Landenel takes it on Wheiskaet's behalf.", "Trial by Turtle", "As Landenel suspected, you were immediately attacked by the mother [[Adamantoise (Mob)|adamantoise]] when you touched the egg. … After taking the egg on behalf of [[Wheiskaet]]"),
 "M91c": ("Landenel sends you to U'odh Nunh at Forgotten Springs, who refuses to help.", "Trial by Turtle", "he bids you journey to [[Forgotten Springs]] in [[southern Thanalan]] and speak with a man named [[U'odh Nunh]] … Contrary to what Landenel said, U'odh Nunh has no intention of aiding you in your quest. It seems the old [[Miqo'te]] will require some convincing..."),
 "M91d": ("Landenel believes you will die taking the egg.", "Trial by Turtle", "he believes that you will surely perish if you attempt to take it"),
 # #92 The Perfect Prey
 "M92a": ("U'odh Nunh joined the Company of Heroes to hone his skills.", "The Perfect Prey", "Many years ago, I joined the Company of Heroes to hone my skills, instead of challenging my predecessor before I was ready."),
 "M92b": ("U'odh Nunh sets you to slay an Amalj'aa veteran.", "The Perfect Prey", "U'odh Nunh has bid you slay an [[Stonespike Tanadd Gah|Amalj'aa veteran]] who dwells in the encampment to the east of [[Forgotten Springs]]."),
 "M92c": ("Impressed, U'odh Nunh will tell you of the ingredient.", "The Perfect Prey", "U'odh Nunh is impressed with your accomplishment, and is at last willing to tell you of the ingredient that you seek."),
 "M92d": ("The Children of the Sands do not help strangers.", "The Perfect Prey", "The Children of the Sands do not offer aid to strangers."),
 # #93 When the Worm Turns
 "M93a": ("The second ingredient is Wellwick worm meat, which U'odh Nunh will send to Wheiskaet.", "When the Worm Turns", "The ingredient you seek is the [[Wellwick Worm Meat|meat of a Wellwick worm]]. … he promises to send it to [[Wheiskaet]] in time for the banquet."),
 "M93b": ("U'odh Nunh does not know where the third ingredient is.", "When the Worm Turns", "I regret to say that I know naught of its location."),
 # #94 There and Back Again
 "M94a": ("U'odh Nunh was a reckless youth when he joined, and Wheiskaet could have cast him out.", "There and Back Again", "I was a rrreckless, angry youth when I first joined the Company, and he would have been well within his rights to cast me out."),
 "M94b": ("You deliver U'odh Nunh's brandewine, and Wheiskaet resolves to thank his old comrade.", "There and Back Again", "Wheiskaet is surprised by the gift, and resolves to thank his old comrade when next they meet."),
 # #95 The Things We Do for Cheese
 "M95a": ("Brayflox, Wheiskaet's former quartermaster, was to bring the last ingredient, but something befell her people.", "The Things We Do for Cheese", "[[Brayflox]], his former quartermaster, was planning to deliver it to [[Costa del Sol]] herself. However, something appears to have befallen Brayflox and her people"),
 "M95b": ("A flying beast drove the goblins from their lands; you slay the dragon and send them home.", "The Things We Do for Cheese", "a large flying beast has driven the goblins from their lands. … you slay the invading [[dragon]] and return the displaced goblins to their beloved homes."),
 "M95c": ("Brayflox gives you goblin cheese.", "The Things We Do for Cheese", "Brayflox proudly presents to you a [[Goblin Cheese|hunk of gobbie gouda]]."),
 "M95d": ("Wheiskaet won't say how the cheese is made.", "The Things We Do for Cheese", "When pressed as to how the cheese is made, he replies that some things are best left unknown."),
 # #96 What Do You Mean You Forgot the Wine
 "M96a": ("Wheiskaet still keeps Titan's secrets and sends you for the finest wine from Shamani, a former Company member.", "What Do You Mean You Forgot the Wine", "Wheiskaet applauds your performance, but still refuses to tell you of [[Titan]]'s secrets. … you must procure a bottle of the very finest wine from [[Shamani Lohmani]], a former member of [[Company of Heroes|the Company]]."),
 "M96b": ("Shamani has lost his sight, and reads the order by smell.", "What Do You Mean You Forgot the Wine", "When one loses his vision, he is forced to compensate in other ways. … Shamani Lohmani immediately deduces your intent with his impressive sense of smell."),
 "M96c": ("Shamani is in Wineport.", "What Do You Mean You Forgot the Wine", "Make your way to Wineport and seek out Shamani Lohmani, another former member of the Company."),
 # #97 An Offer You Can Refuse
 "M97a": ("Only Byrglaent, owner of Vylbrand's largest winery, has wines fit for the feast.", "An Offer You Can Refuse", "Shamani Lohmani tells you that the only suitable wines for Master [[Gegeruju]]'s banquet are in the possession of [[Byrglaent]], who owns and operates the largest winery in [[Vylbrand]]."),
 "M97b": ("Byrglaent refuses, offering goobbue urine instead.", "An Offer You Can Refuse", "Byrglaent is less than receptive to your requests, and instead offers to serve you [[Goobbue (Mob)|goobbue]] urine."),
 "M97c": ("Shamani became a vintner with his savings from his years as a mercenary.", "An Offer You Can Refuse", "It wouldn't have been possible if not for the savings I amassed during my time as a mercenary, of course."),
 "M97d": ("Shamani calls Byrglaent the Wine Baron of Limsa Lominsa, a man not known for tact.", "An Offer You Can Refuse", "the Wine Baron of Limsa Lominsa is not a man known for his tact."),
 # #98 It Won't Work
 "M98a": ("Most Bacchus wine was destroyed in the Calamity, and the vignerons have none.", "It Won't Work", "most stores were destroyed during [[the Calamity]]. … Alas, the vignerons reiterate that there is no point in searching for Bacchus wine."),
 "M98b": ("Titan blinded Shamani beneath O'Ghomoro, and he fell into despair.", "It Won't Work", "After Titan blinded me in our battle beneath O'Ghomoro, I fell into a deep depression."),
 "M98c": ("Bacchus wine is why Shamani became a vintner.", "It Won't Work", "It is, after all, the very reason I decided to become a vintner."),
 # #99 Give a Man a Drink
 "M99a": ("Shamani cannot bear to disappoint his former captain and swears to find a suitable wine.", "Give a Man a Drink", "Shamani Lohmani has decided that he cannot bear to disappoint his former captain, and he swears that he will find a suitable wine for the banquet."),
 "M99b": ("Drest took Shamani in and nursed him back to health.", "Give a Man a Drink", "It was there that a man named Drest took me in and nursed me back to health."),
 "M99c": ("Shamani misses his life with the Company.", "Give a Man a Drink", "Indeed, there is much I miss about my life with the Company of Heroes."),
 "M99d": ("Drest lives alone at the Severed String.", "Give a Man a Drink", "However, he does know that Drest lives alone at [[the Severed String]], which lies far to the southwest of the docks."),
 "M99e": ("Drest accepts the wine with great trepidation; something is very wrong with him.", "Give a Man a Drink", "Though he accepts your gift of wine, he does so with great trepidation. It is immediately clear to you that there is something very, very wrong with this disheveled, nervous man..."),
 # #100 That Weight (E100a, the accepted claim, also cites it)
 "M100a": ("Drest confesses he is an imperial deserter, though not Garlean.", "That Weight", "Drest confesses that he is an imperial deserter, though he himself is not [[Garlean]]."),
 "M100b": ("His unit was caught by the Maelstrom on a reconnaissance mission, and no one else survived.", "That Weight", "on a reconnaissance mission when the Maelstrom caught us by surprise. … N-No one else survived."),
 "M100c": ("Drest bears Eorzeans no ill will, and toils in secret hoping to go home.", "That Weight", "he holds no ill will towards the people of [[Eorzea]]. Nevertheless, he had no choice but to come to [[Vylbrand]], where he now toils in secret so that one day he might return home."),
 "M100d": ("You clear the midges that kept Drest from sleeping.", "That Weight", "Drest cannot sleep due to the incessant buzzing of [[Dung Midge Swarm|midge swarms]]."),
 # #101 Battle Scars
 "M101a": ("Calmer now, Drest sends Shamani palm wine in thanks.", "Battle Scars", "[[Drest]] appears to be in greater control of his faculties. … To express his gratitude to [[Shamani Lohmani]], Drest has asked you to deliver three [[Palm Wine|coconuts filled with palm wine]]"),
 "M101b": ("Shamani sees Drest and himself as two men struggling not to let their scars define them.", "Battle Scars", "Two men who have long struggled not to let our scars define us..."),
 "M101c": ("Shamani resolves to spend more time with Drest.", "Battle Scars", "Shamani Lohmani then thanks you for looking after Drest, with whom he resolves to spend more time."),
}

# ---- Entities this era introduces ----------------------------------------------------------------------------------
E_MASK, E_TRUST, E_YOUNG, E_SHROUD, E_TITAN, E_FEAST = (
    "evt-the-masked-man", "evt-the-refugees-trust", "evt-youngbloods-of-little-ala-mhigo",
    "evt-murders-in-the-shroud", "evt-titan-reawakened", "evt-a-feast-at-costa-del-sol")

ENTITIES = {
 E_MASK: "event", E_TRUST: "event", E_YOUNG: "event", E_SHROUD: "event", E_TITAN: "event", E_FEAST: "event",
 "char-swift": "character", "char-hihibaru": "character", "char-gundobald": "character", "char-haribehrt": "character",
 "char-meffrid": "character", "char-wilred": "character", "char-medrod": "character", "char-aideen": "character",
 "char-ivaurault": "character", "char-ursandel": "character", "char-amandine": "character", "char-merlwyb": "character",
 "char-trachtoum": "character", "char-wheiskaet": "character", "char-gegeruju": "character", "char-landenel": "character",
 "char-uodh-nunh": "character", "char-brayflox": "character", "char-shamani": "character", "char-byrglaent": "character",
 "char-drest": "character", "char-buscarron": "character",
 "org-ascians": "organization", "org-immortal-flames": "organization", "org-ala-mhigan-resistance": "organization",
 "org-maelstrom": "organization", "org-kobolds": "organization",
 "loc-little-ala-mhigo": "location", "loc-ala-mhigo": "location",
}

# ---- Presentations -------------------------------------------------------------------------------------------------
N_MASK, N_TRUST, N_YOUNG, N_SHROUD, N_TITAN, N_FEAST = (
    "The Masked Man", "The Refugees' Trust", "The Youngbloods of Little Ala Mhigo", "Murders in the Shroud",
    "Titan Reawakened", "A Feast at Costa del Sol")

PRES = {
 # ---- Arc recaps ----
 E_MASK: [
   P(S(62), None, "main", N_MASK,
     "With the sylph dispute settled, Gridania credits the Scions' mediation, and the sylph Noraxia has come to the Waking Sands as a friend. "
     "Then Minfilia heard of a man named Lahabrea, red-masked and robed in black. The Ascians hid before the Calamity, and fearing that they now act openly, she has set you to learn all you can of him.",
     ["M62b", "M62c", "M62d", "M62e", "M62f"]),
   P(S(63), None, "main", N_MASK,
     "Minfilia has set you to uncover the motives of Lahabrea, a masked Ascian, fearing his kind are behind the chaos racking the realm. "
     "The Immortal Flames answered her call: Flame Commander Swift told you a Brass Blade at Highbridge saw the masked stranger before Qiqirn killed him, and sent you to Hihibaru, a merchant there.",
     ["M63a", "M63b", "M63c", "M63d", "M63e", "M63f"]),
   P(S(64), None, "main", N_MASK,
     "You are hunting Lahabrea, the masked Ascian whom Minfilia fears is behind the realm's troubles. At Highbridge, where beastman raids keep travelers away, "
     "the merchants offered only rumors that he has been seen across Thanalan. Hihibaru suspects someone is orchestrating the Qiqirn raids, and has promised to watch for your quarry.",
     ["M63a", "M63b", "M64a", "M64b", "M64c", "M64d"]),
   P(S(65), None, "main", N_MASK,
     "You are hunting Lahabrea, the masked Ascian whom Minfilia fears is behind the realm's troubles. Hihibaru saw a masked man meeting beastmen in secret, so you lit a fire of your own, and it drew an armed bandit. "
     "His scroll bears the mark of Rhalgr, guardian of Ala Mhigo, a land the Empire rules: Lahabrea seems tied to the Ala Mhigans.",
     ["M63a", "M65a", "M65b", "M65c", "M65d"]),
 ],
 E_TRUST: [
   P(S(66), None, "main", N_TRUST,
     "The trail of Lahabrea, the masked Ascian, points to the Ala Mhigans. Hihibaru sent you to Little Ala Mhigo, a lawless refugee settlement where his daughter Hihira lives. "
     "She knew nothing of the masked stranger, and the settlement's leader, Gundobald, turned you away.",
     ["M65d", "M66a", "M66b", "M66c"]),
   P(S(67), None, "main", N_TRUST,
     "Seeking Lahabrea among the Ala Mhigans, you were turned away by Gundobald, leader of Little Ala Mhigo. Gisilbehrt of the Immortal Flames, head of security there, sent you to his lookouts, "
     "and one saw a masked figure talking with Ala Mhigans. The refugees trust no one but themselves, and you will need their cooperation.",
     ["M66b", "M66c", "M67a", "M67b", "M67c", "M67d"]),
   P(S(68), None, "main", N_TRUST,
     "Lahabrea seems tied to Little Ala Mhigo, but its refugees trust only their own. Their leader, Gundobald, belongs to the Ala Mhigan Resistance, and only a respected compatriot's word will win you a hearing. "
     "At the Waking Sands, Minfilia offered to introduce you to an Ala Mhigan among the Scions.",
     ["M67c", "M67d", "M68a", "M68e", "M68d"]),
   P(S(69), None, "main", N_TRUST,
     "To win the trust of Little Ala Mhigo, whose leader Gundobald belongs to the Ala Mhigan Resistance, you need a compatriot to vouch for you. "
     "The Scion Haribehrt left the Resistance and is shunned by his old comrades, but sent you to Albreda at Quarrymill. Angry at his name, she pointed you to Meffrid, a captain of the Resistance.",
     ["M68a", "M68e", "M69a", "M69b", "M69c"]),
   P(S(70), None, "main", N_TRUST,
     "You are seeking the trust of the Ala Mhigan Resistance, whose member Gundobald leads Little Ala Mhigo. At Quarrymill, Meffrid's comrade Gallien has a festering wound, and the villagers refused to help even when Meffrid begged. "
     "Their Hearer, Charline, denied the petition, saying the right belongs only to the elementals.",
     ["M68a", "M69c", "M70a", "M70b", "M70c"]),
   P(S(71), None, "main", N_TRUST,
     "You are seeking the trust of the Ala Mhigan Resistance, whose member Gundobald leads Little Ala Mhigo. With Quarrymill refusing aid, Meffrid tried an old Ala Mhigan remedy of antelope horn, "
     "and the tavern keeper Buscarron made the medicine. Gallien's chances have improved, and Meffrid's brothers are starting to trust you.",
     ["M68a", "M70b", "M71a", "M71b", "M71c"]),
   P(S(72), None, "main", N_TRUST,
     "You are seeking the trust of the Ala Mhigan Resistance, whose member Gundobald leads Little Ala Mhigo. The wounded Gallien slipped away from Quarrymill so as not to burden his comrades, and you tracked him down. "
     "Meffrid reminded him of their oath to set foot on Ala Mhigan soil again together or not at all, and Gallien is expected to recover.",
     ["M68a", "M72a", "M72b", "M72c"]),
   P(S(73), None, "main", N_TRUST,
     "For your help with his wounded comrade, Meffrid gave you a letter of introduction to Gundobald, the leader of Little Ala Mhigo, who mentored him in the Resistance. "
     "Gundobald has cast aside his mistrust and offered you his friendship. He knows of the masked stranger you seek, and will tell you what he can.",
     ["M66b", "M73a", "M73b", "M73c"]),
 ],
 E_YOUNG: [
   P(S(74), None, "main", N_YOUNG,
     "Gundobald, leader of Little Ala Mhigo, now trusts you, and says some of the settlement's youngbloods are meeting the masked stranger in secret. The youths' reactions suggest something is afoot, and Lahabrea may be involved. "
     "Gundobald, who once rose with his brothers against Ala Mhigo's despot only to see it fall to the Empire, fears they will commit some great folly.",
     ["M73c", "M74a", "M74b", "M74c", "M74d", "M74e"]),
   P(S(75), None, "main", N_YOUNG,
     "Some of Little Ala Mhigo's youths have been meeting the masked stranger in secret. Their leader, Wilred, lured you into an ambush, and when you overpowered his band he boasted that they will obtain the power to bring down the Empire and reclaim their homeland. "
     "He slipped away, and Gundobald fears the young fools will harm others, if not themselves.",
     ["M74a", "M75a", "M75b", "M75c", "M75d"]),
   P(S(76), None, "main", N_YOUNG,
     "Wilred and his friends, youths of Little Ala Mhigo, set out to steal crystals from an Amalj'aa stronghold and summon Rhalgr, guardian of their lost homeland, but you stopped them. "
     "Wilred admitted that the masked stranger gave them the idea, promising it would let them defeat the Empire. Gundobald told him he owes his life to you.",
     ["M75a", "M76b", "M76c", "M76d", "M76e", "M76f"]),
   P(S(77), None, "main", N_YOUNG,
     "A masked stranger, perhaps Lahabrea, set youths of Little Ala Mhigo on summoning Rhalgr, and you thwarted their plot. Gundobald has nothing more to tell you. "
     "Back at the Waking Sands, Minfilia sees in it the kind of deception the Ascians would use, believes a malign will is behind some of the land's ills, and has promised to look further.",
     ["M74b", "M76c", "M76e", "M77a", "M77b", "M77c", "M77d"]),
 ],
 E_SHROUD: [
   P(S(78), None, "main", N_SHROUD,
     "Someone fitting Lahabrea's description has been seen in the North Shroud, in the wake of a series of mysterious deaths. The sylph Noraxia sent you to Medrod, a miner at Fallgourd Float, "
     "who saw a masked man with a winged creature that was all eyeball and teeth. His friends Aideen and Ivaurault have offered to help.",
     ["M78a", "M78b", "M78c", "M78d", "M78e", "M78f"]),
   P(S(79), None, "main", N_SHROUD,
     "A masked man, perhaps Lahabrea, was seen in the North Shroud with a winged eyeball, amid a spate of mysterious deaths. At Fallgourd Float, Aideen told you the victims' faces were torn to shreds, which folk blame on the ziz. "
     "You culled three and found nothing, so she has turned back to the masked stranger and his winged eyeball.",
     ["M78a", "M78d", "M78e", "M79a", "M79b"]),
   P(S(80), None, "main", N_SHROUD,
     "A masked man, perhaps Lahabrea, was seen in the North Shroud with a winged eyeball, amid deaths that left the victims' faces torn to shreds. Ivaurault confessed that he too saw the eyeball, at the same moment as Medrod. "
     "Where he saw it, a monstrous banemite attacked you instead, and he now wonders whether he imagined it.",
     ["M78a", "M78d", "M79a", "M80a", "M80b"]),
   P(S80B, None, "main", N_SHROUD,
     "A masked man, perhaps Lahabrea, was seen in the North Shroud with a winged eyeball, amid deaths that left the victims' faces torn to shreds. Aideen learned that every victim has been a comely maiden, and a rumor said their rancor went into a rock. "
     "You blasted it apart, but its flashes came from ordinary crystals, nothing to do with the masked stranger.",
     ["M78a", "M78d", "M79a", "M80ba", "M80bb"]),
   P(S(82), None, "main", N_SHROUD,
     "Mysterious deaths in the North Shroud follow sightings of a masked man and a winged eyeball, and every victim has been a comely maiden. Ivaurault is sure of what he saw, and the friends at Fallgourd Float have left the case to you. "
     "You found another body, and Aethelmaer found on it a button engraved with a lily, like one from an earlier victim.",
     ["M78d", "M80ba", "M82a", "M82b", "M82d"]),
   P(S(83), None, "main", N_SHROUD,
     "Mysterious deaths in the North Shroud follow sightings of a masked man and a winged eyeball. Aethelmaer gave you a lily button found on two victims, the best lead yet. "
     "In Gridania, Ursandel knew the sigil as the Dartancours family's, and will tell the truth of the murders if you promise to end his lady's madness.",
     ["M78d", "M82d", "M83a", "M83c", "M83d"]),
   P(S(84), None, "main", N_SHROUD,
     "Ursandel told you how Lady Amandine of the Dartancours, disfigured in the Calamity, held rites of rejuvenation that spilled maiden blood, urged on by masked men. You defeated her in Haukke Manor. "
     "Then two masked Ascians appeared, said they had come to measure your strength for Master Lahabrea, and vanished; Minfilia is sure the Ascians have begun to move in earnest.",
     ["M84a", "M84b", "M84c", "M84d", "M84g"]),
 ],
 E_TITAN: [
   P(S(85), None, "main", N_TITAN,
     "A tribe of kobolds near Limsa Lominsa has summoned Titan again, and the Maelstrom has asked the Scions to slay the primal. Admiral Merlwyb pledged her full support, though she owned that the Lominsans broke their pact with the beastmen. "
     "The only force known to have bested Titan, the Company of Heroes, has disbanded, so Y'shtola sent you to find a former member, Trachtoum.",
     ["M85a", "M85c", "M85d", "M85b", "M85f", "M85i"]),
   P(S(86), None, "main", N_TITAN,
     "The kobolds have summoned Titan, and the Scions have agreed to slay him with the Maelstrom's support. To learn how the Company of Heroes once beat him, you found Trachtoum, a marauder at the Grey Fleet mills who boasts of serving with it. "
     "He would share the Company's secret strategy only if you cleared a rats' nest, which turned out to be his own chore.",
     ["M85a", "M85c", "M85i", "M86a", "M86b"]),
   P(S(87), None, "main", N_TITAN,
     "The kobolds have summoned Titan, and the Scions have agreed to slay him with the Maelstrom's support. Trachtoum, who boasts of serving with the Company of Heroes, the band that once beat Titan, doubts you can face a primal. "
     "You slew a goobbue that was harassing the millers, but even that did not earn his confidence.",
     ["M85a", "M85c", "M85i", "M87a", "M87b"]),
   P(S(88), None, "main", N_TITAN,
     "The kobolds have summoned Titan, and the Scions mean to slay him. Trachtoum confessed he was never in the Company of Heroes, and sent you to Wheiskaet, one of its former captains, at Costa del Sol. "
     "Wheiskaet says Titan took some of the Company's best, and won't send you into O'Ghomoro on a whim; Y'shtola has left you to meet his conditions alone.",
     ["M85a", "M88a", "M88b", "M88d", "M88e"]),
   P(S(89), None, "main", N_TITAN,
     "The Scions mean to slay Titan, whom the kobolds have summoned, but they lack the knowledge of how to enter his lair, and Wheiskaet, a former captain of the Company of Heroes, holds it. "
     "A former employee who lied about serving in the Company has made him wary of strangers. You passed his simple test by slaying a nix, and he is ready to set you a real challenge.",
     ["M85a", "M88f", "M88a", "M89a", "M89b", "M89c", "M89d"]),
 ],
 E_FEAST: [
   P(S(90), None, "main", N_FEAST,
     "Wheiskaet, a former captain of the Company of Heroes, knows how to reach Titan's lair, but first wants proof of your worth. Master Gegeruju, whose estates he guards, will welcome two distinguished visitors to Costa del Sol with an elaborate feast, "
     "and you are to gather its ingredients, guided by the Company's old mercenaries. Landenel, at Camp Tranquil, told you how to take a giant adamantoise's egg.",
     ["M88a", "M88f", "M88c", "M90a", "M90b", "M90e", "M90d"]),
   P(S(91), None, "main", N_FEAST,
     "To earn Wheiskaet's knowledge of how to reach Titan, you are gathering ingredients for Master Gegeruju's feast at Costa del Sol. Landenel, who keeps his time with the Company of Heroes a secret, was sure you would die taking a giant adamantoise's egg, but you claimed it. "
     "He sent you on to U'odh Nunh at Forgotten Springs, who refuses to help.",
     ["M88f", "M90a", "M91a", "M91d", "M91b", "M91c"]),
   P(S(92), None, "main", N_FEAST,
     "To earn Wheiskaet's knowledge of how to reach Titan, you are gathering ingredients for Master Gegeruju's feast at Costa del Sol, and Landenel has the first. U'odh Nunh, who joined the Company of Heroes to hone his skills, would not aid a stranger. "
     "You lured out and slew an Amalj'aa veteran, and he will now tell you the second ingredient.",
     ["M88f", "M90a", "M91b", "M92a", "M92d", "M92b", "M92c"]),
   P(S(93), None, "main", N_FEAST,
     "To earn Wheiskaet's knowledge of how to reach Titan, you are gathering ingredients for Master Gegeruju's feast at Costa del Sol. You have the adamantoise egg, and at U'odh Nunh's suggestion you baited and slew a Wellwick worm for its meat, "
     "which he will send to Wheiskaet. He does not know where the third ingredient is.",
     ["M88f", "M90a", "M91b", "M93a", "M93b"]),
   P(S(94), None, "main", N_FEAST,
     "To earn Wheiskaet's knowledge of how to reach Titan, you are gathering ingredients for Master Gegeruju's feast at Costa del Sol, and two are on their way. "
     "You carried a bottle of brandewine from U'odh Nunh, once a reckless young recruit in the Company of Heroes, to his old captain. Wheiskaet was surprised and touched, and one ingredient remains.",
     ["M88f", "M90a", "M93a", "M94a", "M94b"]),
   P(S(95), None, "main", N_FEAST,
     "To earn Wheiskaet's knowledge of how to reach Titan, you are gathering ingredients for Master Gegeruju's feast at Costa del Sol. The last was to come from Brayflox, Wheiskaet's former quartermaster, but a dragon had driven her goblins from their lands. "
     "You slew it and brought Wheiskaet her goblin cheese, though he won't say how it is made.",
     ["M88f", "M90a", "M95a", "M95b", "M95c", "M95d"]),
   P(S(96), None, "main", N_FEAST,
     "You have gathered an egg, worm meat and goblin cheese for Master Gegeruju's feast at Costa del Sol, but Wheiskaet still keeps Titan's secrets. Now he wants the finest wine, and sent you to Shamani, a former member of the Company of Heroes and a vintner at Wineport. "
     "Shamani, who has lost his sight, read the order by its smell.",
     ["M90a", "M95c", "M96a", "M96c", "M96b"]),
   P(S(97), None, "main", N_FEAST,
     "Wheiskaet still keeps Titan's secrets until you bring the finest wine for Master Gegeruju's feast at Costa del Sol. Shamani, a blind former mercenary of the Company of Heroes turned vintner, says only Byrglaent, who owns the largest winery in Vylbrand, has wine good enough. "
     "Byrglaent refused, offering goobbue urine instead.",
     ["M90a", "M96a", "M96b", "M97c", "M97a", "M97b"]),
   P(S(98), None, "main", N_FEAST,
     "Wheiskaet still keeps Titan's secrets until you bring the finest wine for Master Gegeruju's feast. Shamani sent you looking for Bacchus wine, but the Calamity destroyed most of it and Wineport's vignerons have none. "
     "Shamani told you Titan blinded him beneath O'Ghomoro, and that Bacchus wine pulled him from despair and made him a vintner.",
     ["M96a", "M97a", "M98a", "M98b", "M98c"]),
   P(S(99), None, "main", N_FEAST,
     "Wheiskaet still keeps Titan's secrets until you bring the finest wine for Master Gegeruju's feast. Shamani, who cannot bear to disappoint his former captain, swore to find one, and sent his own wine to Drest, the man who once nursed him back to health. "
     "You found Drest living alone at the Severed String, nervous and plainly unwell.",
     ["M96a", "M99a", "M99b", "M99d", "M99e"]),
   P(S(100), None, "main", N_FEAST,
     "While Shamani seeks a wine fit for Master Gegeruju's feast, you took his gift to Drest, the hermit who once nursed him back to health. After you cleared the midges that kept him from sleep, "
     "Drest confessed that he is an imperial deserter, though not Garlean, and the only survivor of his unit. He toils in secret, hoping one day to go home.",
     ["M99a", "M99b", "M100d", "M100a", "M100b", "M100c"]),
   P(S(101), None, "main", N_FEAST,
     "Shamani is still seeking a wine fit for Master Gegeruju's feast, which Wheiskaet demands before he will tell you how to reach Titan. Drest, the imperial deserter who once nursed Shamani back to health, is calmer now, and sent him palm wine in thanks. "
     "Shamani sees in Drest a man who, like himself, struggles not to let his scars define him.",
     ["M99a", "M96a", "M100a", "M101a", "M101b", "M101c"]),
 ],

 # ---- The Scions and their circle ----
 "char-minfilia": [
   P(S(62), None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. She is glad to see the Scions' family keep growing, but alarmed that the Ascians, who stayed hidden before the Calamity, now seem to act openly. "
     "She has set you to learn all you can of a red-masked man named Lahabrea.",
     ["C01", "C33", "M62h", "M62e", "M62d", "M62f"]),
   P(S(77), None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. She has set you to investigate the Ascian Lahabrea, and in the plot at Little Ala Mhigo she sees the kind of deception the Ascians would use. "
     "She believes some of the land's ills are brought about by a malign will, and has promised to look further.",
     ["C01", "C33", "M63a", "M77b", "M77c", "M77d"]),
   P(S(84), None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. After two of Lahabrea's minions took your measure in Haukke Manor, she is sure the Ascians have begun to move in earnest, "
     "and means to urge the three nations to heighten their vigil.",
     ["C01", "C33", "M84d", "M84g", "M84h"]),
   P(S(85), None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. When the Maelstrom asked the Scions to slay Titan, she pledged the order's full support and sent Y'shtola with you to Limsa Lominsa. "
     "She has also warned the three nations to heighten their vigil against the Ascians.",
     ["C01", "C33", "M85a", "M85j", "M85g", "M84h"]),
 ],
 "char-alphinaud": [
   P(S(62), None, "main", "Alphinaud",
     "A young traveler who, with his twin sister, calls himself a student of history. Calling on Minfilia at the Waking Sands, he told her that Alisaie has chosen to walk her own path, though the twins' destination remains the same.",
     ["C10", "C42", "M62j", "C11"]),
 ],
 "char-alisaie": [
   P(S(62), None, "main", "Alisaie",
     "Alphinaud's twin sister, who means to find another way to heal the realm's troubles. Minfilia has scarcely seen her of late: Alphinaud says she has chosen to walk her own path, though the twins share the same destination.",
     ["C10", "C42", "M62j", "C11"]),
 ],
 "char-yshtola": [
   P(S(85), None, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order. Minfilia has sent her with you to face Titan. She reminded Admiral Merlwyb that the Lominsans broke their pact with the beastmen, "
     "and proposes learning how the Company of Heroes once bested the primal.",
     ["C40", "M85g", "M85d", "M85f"]),
   P(S(88), None, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order. The Scions lack only the knowledge of how to enter Titan's lair, and she found Wheiskaet, a former captain of the Company of Heroes who holds it, "
     "but left you to meet his conditions alone while she sees to the other preparations.",
     ["C40", "M88f", "M88a", "M88e"]),
 ],
 "org-scions": [
   P(S(62), None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia from the Waking Sands. Gridania credits its mediation with averting a needless conflict with the sylphs, "
     "and its family keeps growing: the sylph Noraxia has come to offer her aid.",
     ["C34", "C01", "C02", "M62b", "M62h", "M62c"]),
   P(S(85), None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia from the Waking Sands. The Maelstrom has asked it to slay the primal Titan, and Minfilia has pledged the order's full support.",
     ["C34", "C01", "C02", "M85a", "M85j"]),
 ],
 "char-noraxia": [
   P(S(62), None, "main", "Noraxia",
     "A sylph who has come to the Waking Sands as a friend, sent by the elder Frixio to help the Scions.",
     ["M62c"]),
   P(S(78), None, "main", "Noraxia",
     "A sylph who came to the Waking Sands as a friend, sent by the elder Frixio to help the Scions. She passed on word that a miner in the North Shroud, Medrod, saw a masked man in the wood.",
     ["M62c", "M78c"]),
 ],
 "char-haribehrt": [
   P(S(69), None, "main", "Haribehrt",
     "An Ala Mhigan member of the Scions, who joined hoping to find a way to free his homeland. He left the Ala Mhigan Resistance to do so, and his former comrades will have nothing to do with him.",
     ["M68d", "M69a", "M69b"]),
 ],

 # ---- Lahabrea and the Ascians ----
 "char-lahabrea": [
   P(S(62), None, "main", "Lahabrea",
     "An Ascian in a red mask and black robes. When you told Minfilia of him, she was alarmed that the Ascians, who hid before the Calamity, now act openly, and she has set you to learn all you can of him and his designs.",
     ["M62d", "M62k", "M62e", "M62f"]),
   P(S(63), None, "main", "Lahabrea",
     "An Ascian in a red mask and black robes, whose motives Minfilia has set you to uncover. The Immortal Flames reported that a Brass Blade saw the masked stranger near Highbridge.",
     ["M63a", "M62d", "M63c", "M63e"]),
   P(S(65), None, "main", "Lahabrea",
     "An Ascian in a red mask and black robes, whose motives you are investigating. He has been seen about Thanalan and meeting beastmen in secret, and the trail points to clandestine ties with the Qiqirn and the Ala Mhigans.",
     ["M63a", "M62d", "M64b", "M65a", "M65d"]),
   P(S(67), None, "main", "Lahabrea",
     "An Ascian in a red mask and black robes, whose motives you are investigating. He seems tied to the Ala Mhigans and to Little Ala Mhigo, where a lookout saw a masked figure talking with refugees.",
     ["M63a", "M65d", "M67b", "M67c"]),
   P(S(76), None, "main", "Lahabrea",
     "An Ascian whose motives you are investigating. At Little Ala Mhigo a masked stranger, who may have been him, taught a band of youths to summon Rhalgr with stolen crystals, promising they could defeat the Empire.",
     ["M63a", "M74b", "M76c", "M76d"]),
   P(S(78), None, "main", "Lahabrea",
     "An Ascian whose motives you are investigating. A masked stranger, perhaps him, set youths of Little Ala Mhigo on summoning Rhalgr. Someone fitting his description has now been seen in the North Shroud, in the wake of a series of mysterious deaths.",
     ["M63a", "M74b", "M76c", "M78a", "M78b"]),
   P(S(84), None, "main", "Lahabrea",
     "An Ascian whom Minfilia has set you to investigate. A masked stranger, perhaps him, set youths of Little Ala Mhigo on summoning Rhalgr. "
     "In Haukke Manor two other masked Ascians, calling him their master, came to measure your strength for him, and Minfilia is now sure the Ascians are moving in earnest.",
     ["M63a", "M76c", "M84c", "M84d", "M84g"]),
 ],
 "org-ascians": [
   P(S(62), None, "main", "The Ascians",
     "Beings who took great pains to stay hidden before the Calamity. Minfilia is alarmed that they now seem to be casting off their secrecy, as a red-masked man named Lahabrea appears.",
     ["M62e", "M62d"], ["the Bringers of Chaos"]),
   P(S(63), None, "main", "The Ascians",
     "Beings who took great pains to stay hidden before the Calamity. Minfilia names the masked Lahabrea as one of them, and suspects they are behind the chaos racking the realm.",
     ["M62e", "M63a", "M63b"], ["the Bringers of Chaos"]),
   P(S(77), None, "main", "The Ascians",
     "Beings who hid before the Calamity, Lahabrea among them, whom Minfilia suspects of the chaos racking the realm. "
     "She sees their kind of deception in the masked stranger who set Little Ala Mhigo's youths on summoning Rhalgr.",
     ["M62e", "M63a", "M63b", "M77b", "M76c"], ["the Bringers of Chaos"]),
   P(S(84), None, "main", "The Ascians",
     "Masked beings who hid before the Calamity but now act openly, Lahabrea among them. In Haukke Manor two of them, who seem to have masterminded its atrocities, took your measure for their master Lahabrea, "
     "called you the Bringer of Light and vanished. Minfilia is sure they have begun to move in earnest.",
     ["M62e", "M63a", "M84c", "M84d", "M84i", "M84g"], ["the Bringers of Chaos"]),
 ],

 # ---- Highbridge and Little Ala Mhigo ----
 "org-immortal-flames": [
   P(S(63), None, "main", "The Immortal Flames",
     "A Grand Company whose Flame Commander, Swift, serves at the Hall of Flames in Ul'dah. When Minfilia asked each Grand Company for help, it answered with word of a possible sighting of the masked Lahabrea.",
     ["M63c", "M63d"]),
   P(S(67), None, "main", "The Immortal Flames",
     "A Grand Company whose Flame Commander, Swift, serves at the Hall of Flames in Ul'dah. It answered Minfilia's call for help with word of a sighting of Lahabrea, and its Gisilbehrt heads security at Little Ala Mhigo.",
     ["M63c", "M63d", "M67a"]),
 ],
 "char-swift": [
   P(S(63), None, "main", "Flame Commander Swift",
     "Flame Commander of the Immortal Flames, at the Hall of Flames in Ul'dah. He told you a Brass Blade at Highbridge reported the masked stranger before dying in a Qiqirn raid, and sent you to the merchant Hihibaru.",
     ["M63d", "M63e", "M63f"]),
 ],
 "char-hihibaru": [
   P(S(63), None, "main", "Hihibaru",
     "A merchant at Highbridge in eastern Thanalan. Swift sent you to him for word of the masked stranger, and he hints that he knows something, though his manner inspires little confidence.",
     ["M63f"]),
   P(S(64), None, "main", "Hihibaru",
     "A merchant at Highbridge, where endless beastman raids keep customers away. He suspects someone is orchestrating the Qiqirn raids and inciting the beast tribes, and has promised to watch for the masked stranger.",
     ["M63f", "M64a", "M64c", "M64d"]),
   P(S(65), None, "main", "Hihibaru",
     "A merchant at Highbridge, who suspects someone is inciting the beast tribes. He saw the masked stranger meeting beastmen in secret, "
     "and knew the scroll you took from a bandit for the mark of Rhalgr, guardian deity of Ala Mhigo.",
     ["M64c", "M65a", "M65b", "M65c"]),
   P(S(66), None, "main", "Hihibaru",
     "A merchant at Highbridge, who saw the masked stranger meeting beastmen in secret and traced a bandit's scroll to the Ala Mhigans. He sent you on to Little Ala Mhigo, where his daughter Hihira lives.",
     ["M65a", "M65c", "M66a"]),
 ],
 "loc-little-ala-mhigo": [
   P(S(66), None, "main", "Little Ala Mhigo",
     "A settlement of Ala Mhigan refugees, led by Gundobald. Hihibaru calls it a lawless place, and its leader turned you away.",
     ["M66a", "M66b", "M66c"]),
   P(S(67), None, "main", "Little Ala Mhigo",
     "A settlement of Ala Mhigan refugees, led by Gundobald. The refugees trust no one but themselves, and Lahabrea seems connected to the settlement: a lookout saw a masked figure talking with Ala Mhigans.",
     ["M66b", "M67d", "M67c", "M67b"]),
   P(S(68), None, "main", "Little Ala Mhigo",
     "A settlement of Ala Mhigan refugees, led by Gundobald. The city-states cannot take in all the displaced, and Minfilia believes only reclaiming their homeland would be a lasting solution. "
     "Lahabrea seems connected to the settlement.",
     ["M66b", "M68c", "M67c"]),
   P(S(74), None, "main", "Little Ala Mhigo",
     "A settlement of Ala Mhigan refugees, led by Gundobald, who has offered you his friendship. Some of its young people are meeting the masked stranger in secret.",
     ["M66b", "M73c", "M74a"]),
   P(S(76), None, "main", "Little Ala Mhigo",
     "A settlement of Ala Mhigan refugees, led by Gundobald. A band of its youths, led by Wilred, plotted to summon Rhalgr with crystals stolen from the Amalj'aa at the masked stranger's urging, and you thwarted them.",
     ["M66b", "M75a", "M76b", "M76c", "M76e"]),
 ],
 "loc-ala-mhigo": [
   P(S(65), None, "main", "Ala Mhigo",
     "A land under Garlean rule, whose guardian deity is Rhalgr, the Destroyer.",
     ["M65c", "M65b"]),
   P(S(68), None, "main", "Ala Mhigo",
     "A land under Garlean rule, whose guardian deity is Rhalgr. Its refugees share one purpose, freeing their home from the Garleans; "
     "the city-states cannot take in all the displaced, and Minfilia believes only reclaiming their homeland would be a lasting solution.",
     ["M65c", "M68b", "M68c"]),
   P(S(74), None, "main", "Ala Mhigo",
     "A land under Garlean rule, whose guardian deity is Rhalgr. Two decades ago Gundobald and his brothers rose against the despot who ruled it, "
     "but blinded by hate they were dancing to the Empire's tune, and Ala Mhigo fell. Its refugees share one purpose, freeing their home from the Garleans.",
     ["M65c", "M74c", "M74d", "M68b"]),
 ],
 "char-gundobald": [
   P(S(66), None, "main", "Gundobald",
     "Leader of Little Ala Mhigo, a settlement of Ala Mhigan refugees. He turned you away.",
     ["M66b", "M66c"]),
   P(S(68), None, "main", "Gundobald",
     "Leader of Little Ala Mhigo and a member of the Ala Mhigan Resistance. He turned you away, and the refugees will trust you only if a respected compatriot vouches for you.",
     ["M66b", "M68a", "M66c", "M68e"]),
   P(S(73), None, "main", "Gundobald",
     "Leader of Little Ala Mhigo and a member of the Ala Mhigan Resistance, who once mentored Meffrid. Meffrid's letter of introduction won him over, and he will tell you what he knows of the masked stranger.",
     ["M66b", "M68a", "M73b", "M73c"]),
   P(S(74), None, "main", "Gundobald",
     "Leader of Little Ala Mhigo and a member of the Ala Mhigan Resistance. Two decades ago he and his brothers rose against the despot who ruled Ala Mhigo, but blinded by hate they danced to the Empire's tune, and Ala Mhigo fell. "
     "Now he fears for youths meeting the masked stranger in secret.",
     ["M66b", "M68a", "M74c", "M74d", "M74a"]),
   P(S(76), None, "main", "Gundobald",
     "Leader of Little Ala Mhigo and a member of the Ala Mhigan Resistance. Two decades ago he rose against Ala Mhigo's despot, only to see it fall to the Empire. "
     "When the settlement's youths tried to summon Rhalgr, he told their leader, Wilred, that he owes his life to you.",
     ["M66b", "M68a", "M74c", "M74d", "M76b", "M76f"]),
   P(S(77), None, "main", "Gundobald",
     "Leader of Little Ala Mhigo and a member of the Ala Mhigan Resistance, who once rose against Ala Mhigo's despot, only to see it fall to the Empire. "
     "He has nothing more to tell of the masked stranger, and prays you will put an end to him for the sake of the young ones who died by his poisoned words.",
     ["M66b", "M68a", "M74c", "M74d", "M77a", "M77e"]),
 ],
 "org-ala-mhigan-resistance": [
   P(S(68), None, "main", "The Ala Mhigan Resistance",
     "Ala Mhigans whose shared purpose is freeing their homeland from the Garleans. Gundobald, leader of Little Ala Mhigo, belongs to it.",
     ["M68b", "M68a"]),
   P(S(69), None, "main", "The Ala Mhigan Resistance",
     "Ala Mhigans whose shared purpose is freeing their homeland from the Garleans. Gundobald, leader of Little Ala Mhigo, belongs to it, and its captain Meffrid is at Quarrymill in the South Shroud. "
     "Haribehrt left it to join the Scions, and his old comrades shun him.",
     ["M68b", "M68a", "M69c", "M69b"]),
   P(S(72), None, "main", "The Ala Mhigan Resistance",
     "Ala Mhigans whose shared purpose is freeing their homeland from the Garleans. Gundobald, leader of Little Ala Mhigo, belongs to it, and so does Meffrid, a captain at Quarrymill. "
     "Meffrid's men have sworn to set foot on Ala Mhigan soil again together or not at all, and since you helped save his wounded comrade, they have begun to trust you.",
     ["M68b", "M68a", "M69c", "M72b", "M71c"]),
 ],
 "char-meffrid": [
   P(S(69), None, "main", "Meffrid",
     "A captain of the Ala Mhigan Resistance at Quarrymill in the South Shroud.",
     ["M69c"]),
   P(S(70), None, "main", "Meffrid",
     "A captain of the Ala Mhigan Resistance at Quarrymill in the South Shroud. One of his men, Gallien, has a festering wound, and the villagers refused to help even when Meffrid begged; their Hearer denied the Ala Mhigans' petition.",
     ["M69c", "M70a", "M70b", "M70c"]),
   P(S(71), None, "main", "Meffrid",
     "A captain of the Ala Mhigan Resistance at Quarrymill in the South Shroud. With an old Ala Mhigan remedy of antelope horn, made into medicine by Buscarron, his wounded comrade Gallien's chances improved, and his men are starting to trust you.",
     ["M69c", "M71a", "M71b", "M71c"]),
   P(S(72), None, "main", "Meffrid",
     "A captain of the Ala Mhigan Resistance at Quarrymill in the South Shroud. When his wounded comrade Gallien left alone to spare them the burden, he had you track him down, and reminded him of their oath to return to Ala Mhigo together or not at all.",
     ["M69c", "M72a", "M72b", "M72c"]),
   P(S(73), None, "main", "Meffrid",
     "A captain of the Ala Mhigan Resistance at Quarrymill in the South Shroud, sworn to return to Ala Mhigo with his comrades or not at all. "
     "Grateful for your help, he gave you a letter of introduction to his old mentor, Gundobald of Little Ala Mhigo.",
     ["M69c", "M72b", "M73a", "M73b"]),
 ],
 "char-buscarron": [
   P(S(71), None, "main", "Buscarron",
     "Proprietor of Buscarron's Druthers, said never to turn away folk in need. An Ala Mhigan friend once saved his life with an antelope-horn remedy, "
     "so he gave you medicine from his own stores for Meffrid's wounded comrade.",
     ["M71d", "M71b", "M71a"]),
 ],
 "char-wilred": [
   P(S(75), None, "main", "Wilred",
     "A youth of Little Ala Mhigo, something of a leader among its young people. He lured you into a trap, then slipped away after boasting that his band will obtain the power to bring down the Empire and reclaim their homeland.",
     ["M75a", "M75b", "M75c"]),
   P(S(76), None, "main", "Wilred",
     "A youth of Little Ala Mhigo, something of a leader among its young people. At the masked stranger's urging, he and his friends plotted to summon Rhalgr with crystals stolen from an Amalj'aa stronghold, believing it would let them defeat the Empire. "
     "The plot failed, and Gundobald told him he owes his life to you.",
     ["M75a", "M76b", "M76c", "M76d", "M76e", "M76f"]),
 ],
 "org-garlean-empire": [
   P(S(65), None, "main", "The Garlean Empire",
     "An empire that rules Ala Mhigo, the land whose guardian deity is Rhalgr.",
     ["M65c"], ["the Empire"]),
   P(S(68), None, "main", "The Garlean Empire",
     "An empire that rules Ala Mhigo. Freeing their home from the Garleans is the shared purpose of the Ala Mhigan refugees.",
     ["M65c", "M68b"], ["the Empire"]),
   P(S(74), None, "main", "The Garlean Empire",
     "An empire that rules Ala Mhigo. Two decades ago the land fell when rebels, blinded by hate, danced to the Empire's tune. Freeing their home from the Garleans is the shared purpose of the Ala Mhigan refugees.",
     ["M65c", "M74d", "M68b"], ["the Empire"]),
   P(S(100), None, "main", "The Garlean Empire",
     "An empire that conquers other lands, and has tried to conquer Eorzea. It rules Ala Mhigo, and Drest, an imperial deserter who is not Garlean, says it conquered his lands too.",
     ["E100a", "M65c", "M74d", "M100a"], ["the Empire"]),
 ],

 # ---- The North Shroud ----
 "char-medrod": [
   P(S(78), None, "main", "Medrod",
     "A miner at Fallgourd Float in the North Shroud, who saw a masked man in the wood with a winged creature that was all eyeball and teeth.",
     ["M78c", "M78d"]),
   P(S(82), None, "main", "Medrod",
     "A miner at Fallgourd Float in the North Shroud, who saw a masked man with a winged eyeball amid a spate of murders. With Aideen and Ivaurault he has left the investigation to you.",
     ["M78d", "M78b", "M82a"]),
 ],
 "char-aideen": [
   P(S(78), None, "main", "Aideen",
     "A local at Fallgourd Float in the North Shroud, who has offered to help find the masked stranger Medrod saw.",
     ["M78f", "M78c"]),
   P(S(79), None, "main", "Aideen",
     "A local at Fallgourd Float in the North Shroud, helping you investigate the mysterious deaths. The victims' faces were torn to shreds, but she has ruled out the ziz and turned back to the masked stranger and his winged eyeball.",
     ["M78f", "M79a", "M79b"]),
   P(S80B, None, "main", "Aideen",
     "A local at Fallgourd Float in the North Shroud, helping you investigate the mysterious deaths. She learned that every victim has been a comely maiden, but a rumored rock of rancor held only ordinary crystals.",
     ["M79a", "M79b", "M80ba", "M80bb"]),
   P(S(82), None, "main", "Aideen",
     "A local at Fallgourd Float in the North Shroud. She helped you investigate the murders of comely maidens there, then with Medrod and Ivaurault left the case to you.",
     ["M79b", "M80ba", "M82a"]),
 ],
 "char-ivaurault": [
   P(S(78), None, "main", "Ivaurault",
     "A local at Fallgourd Float in the North Shroud, who has offered to help find the masked stranger Medrod saw.",
     ["M78f", "M78c"]),
   P(S(80), None, "main", "Ivaurault",
     "A local at Fallgourd Float in the North Shroud. He confessed that he too saw the winged eyeball, at the same moment as Medrod, but where he saw it a monstrous banemite attacked you instead, and he began to doubt himself.",
     ["M78f", "M80a", "M80b"]),
   P(S(82), None, "main", "Ivaurault",
     "A local at Fallgourd Float in the North Shroud, who saw the winged eyeball at the same moment as Medrod. He is now convinced of what he saw, and with his friends has left the investigation to you.",
     ["M80a", "M82a"]),
 ],
 "char-ursandel": [
   P(S(83), None, "main", "Ursandel",
     "A man in Gridania who wears a button bearing the lily sigil of the Dartancours family. He will tell the truth of the North Shroud murders if you promise to end his lady's madness.",
     ["M83b", "M83c", "M83d"]),
   P(S(84), None, "main", "Ursandel",
     "A former servant of Lady Amandine, mistress of the Dartancours household. He told you how the Calamity disfigured her and masked men urged her into rites that spilled maiden blood. "
     "With her defeated, he will surrender himself for keeping silent.",
     ["M84a", "M83c", "M84b", "M84f"]),
 ],
 "char-amandine": [
   P(S(84), None, "main", "Amandine",
     "Mistress of the Dartancours household, disfigured in the Calamity. At the urging of masked men she held rites of rejuvenation that spilled maiden blood, until you defeated her in Haukke Manor.",
     ["M84a", "M83c", "M84b", "M84c"], ["Lady Amandine"]),
 ],

 # ---- Titan and Limsa Lominsa ----
 "char-titan": [
   P(S(85), None, "main", "Titan",
     "A primal, summoned once more by a tribe of kobolds near Limsa Lominsa, who gather crystals as fodder for him. The Maelstrom has asked the Scions to slay him. "
     "The only force known to have bested him, the Company of Heroes, disbanded five years ago.",
     ["M85a", "M85e", "M85b"]),
   P(S(88), None, "main", "Titan",
     "A primal summoned once more by a tribe of kobolds near Limsa Lominsa, whom the Scions have been asked to slay. Wheiskaet, a former captain of the Company of Heroes, says Titan took some of the Company's very best, "
     "and won't send you into O'Ghomoro to face him on a whim.",
     ["M85a", "M88a", "M88b", "M88d"]),
   P(S(98), None, "main", "Titan",
     "A primal summoned once more by a tribe of kobolds near Limsa Lominsa, whom the Scions have been asked to slay. The Company of Heroes once beat him, but he took some of its very best, "
     "and in battle beneath O'Ghomoro he blinded Shamani, once of the Company.",
     ["M85a", "M85b", "M88b", "M98b"]),
 ],
 "org-kobolds": [
   P(S(85), None, "main", "The kobolds",
     "A tribe living near Limsa Lominsa, which has summoned the primal Titan once more and gathers crystals as fodder for him. Y'shtola recalls a pact that kept each people to its own lands, and Admiral Merlwyb owns that the Lominsans broke it.",
     ["M85a", "M85e", "M85d"]),
 ],
 "org-maelstrom": [
   P(S(85), None, "main", "The Maelstrom",
     "Limsa Lominsa's Grand Company, under Admiral Merlwyb, which has kept watch on the kobolds since before its reformation. It has asked the Scions to slay Titan, and pledged its full support.",
     ["M85m", "M85l", "M85a", "M85c"]),
 ],
 "char-merlwyb": [
   P(S(85), None, "main", "Merlwyb",
     "The Admiral, who commands the Maelstrom in Limsa Lominsa. With Titan summoned once more, she turned to the Scions as Limsa's best hope and pledged the Maelstrom's full support, "
     "owning that the Lominsans broke their pact with the beastmen.",
     ["M85c", "M85k", "M85d"], ["Admiral Merlwyb", "the Admiral"]),
 ],
 "org-company-of-heroes": [
   P(S(85), None, "main", "The Company of Heroes",
     "A famous band of mercenaries, the only force known to have bested Titan. Limsa Lominsa turned to it when Titan rose before, but it disbanded five years ago.",
     ["M85f", "M85b", "M85h"]),
   P(S(88), None, "main", "The Company of Heroes",
     "A famous band of mercenaries, the only force known to have bested Titan, disbanded five years ago. One of its former captains, Wheiskaet, works at Costa del Sol. "
     "He says its victories over primals were bought with lifeblood, and Titan took some of its very best.",
     ["M85f", "M85b", "M88a", "M88b"]),
   P(S(90), None, "main", "The Company of Heroes",
     "A disbanded band of mercenaries, the only force known to have bested Titan, though he took some of its very best. Its former captain, Wheiskaet, has set you to gather the ingredients of a feast, "
     "and many of his old mercenaries still live to guide you.",
     ["M85b", "M88a", "M88b", "M90a", "M90b"]),
   P(S(99), None, "main", "The Company of Heroes",
     "A disbanded band of mercenaries, the only force known to have bested Titan, though he took some of its very best. Its former members Landenel, U'odh Nunh and Shamani have helped you gather the ingredients of a feast for Wheiskaet, "
     "their old captain. Shamani misses his life with the Company.",
     ["M85b", "M88b", "M91a", "M92a", "M96a", "M99c"]),
 ],
 "char-trachtoum": [
   P(S(85), None, "main", "Trachtoum",
     "A man at the Grey Fleet mills in lower La Noscea, the self-proclaimed best axeman of the Company of Heroes.",
     ["M85i"]),
   P(S(86), None, "main", "Trachtoum",
     "A marauder at the Grey Fleet mills, the self-proclaimed best axeman of the Company of Heroes. He won't share the Company's secret strategy until you prove yourself, and the rats' nest he had you clear turned out to be his own chore.",
     ["M85i", "M86a", "M86b"]),
   P(S(88), None, "main", "Trachtoum",
     "A marauder at the Grey Fleet mills who claimed to be the best axeman of the Company of Heroes. Bested in a boulder-breaking contest, he confessed he was never a member, and pointed you to Wheiskaet, one of its former captains.",
     ["M85i", "M88a"]),
 ],
 "char-wheiskaet": [
   P(S(88), None, "main", "Wheiskaet",
     "A former captain of the Company of Heroes, who oversees security for Master Gegeruju's estates at Costa del Sol. He says Titan took some of the Company's very best, "
     "and won't send you into O'Ghomoro on a whim: first you must complete his challenges.",
     ["M88a", "M88c", "M88b", "M88d"]),
   P(S(90), None, "main", "Wheiskaet",
     "A former captain of the Company of Heroes, who guards Master Gegeruju's estates at Costa del Sol and knows how to reach Titan. A man who lied about serving in the Company has made him wary, "
     "so after a simple test he set you to gather the ingredients of a feast for Master Gegeruju's distinguished guests, guided by his old mercenaries.",
     ["M88a", "M88c", "M88f", "M89b", "M90a", "M90b"]),
   P(S(96), None, "main", "Wheiskaet",
     "A former captain of the Company of Heroes, who guards Master Gegeruju's estates at Costa del Sol. You brought him an egg, worm meat and goblin cheese for Master Gegeruju's feast, "
     "but he still keeps Titan's secrets until you bring the finest wine.",
     ["M88a", "M88c", "M90a", "M95c", "M96a"]),
 ],
 "char-gegeruju": [
   P(S(88), None, "main", "Gegeruju",
     "A master whose estates Wheiskaet guards.",
     ["M88c"], ["Master Gegeruju"]),
   P(S(90), None, "main", "Gegeruju",
     "A master whose estates at Costa del Sol Wheiskaet guards. He means to welcome two distinguished visitors with an elaborate feast.",
     ["M88c", "M90a"], ["Master Gegeruju"]),
 ],
 "char-landenel": [
   P(S(90), None, "main", "Landenel",
     "A man at Camp Tranquil in the South Shroud, who knew you as the one who would challenge Titan. He would not help you openly, but told you how to take a giant adamantoise's egg.",
     ["M90e", "M90c", "M90d"]),
   P(S(91), None, "main", "Landenel",
     "A man at Camp Tranquil in the South Shroud, who once served with the Company of Heroes and keeps that past a secret. He was sure you would die taking a giant adamantoise's egg, "
     "and when you brought it he sent it on to Wheiskaet and pointed you to U'odh Nunh.",
     ["M90e", "M91a", "M91d", "M91b", "M91c"]),
 ],
 "char-uodh-nunh": [
   P(S(91), None, "main", "U'odh Nunh",
     "A Miqo'te at Forgotten Springs in southern Thanalan, to whom Landenel sent you for the next ingredient. He has no intention of helping you.",
     ["M91c"]),
   P(S(92), None, "main", "U'odh Nunh",
     "A Miqo'te at Forgotten Springs in southern Thanalan, who joined the Company of Heroes long ago to hone his skills. He would not aid a stranger, but after you slew an Amalj'aa veteran he agreed to tell you the ingredient you seek.",
     ["M91c", "M92a", "M92d", "M92b", "M92c"]),
   P(S(94), None, "main", "U'odh Nunh",
     "A Miqo'te at Forgotten Springs who joined the Company of Heroes as a reckless youth, when his captain, Wheiskaet, could have cast him out. "
     "He prepared Wellwick worm meat for Wheiskaet's feast, and you carried his gift of brandewine to his old captain.",
     ["M92a", "M94a", "M93a", "M94b"]),
 ],
 "char-brayflox": [
   P(S(95), None, "main", "Brayflox",
     "Wheiskaet's former quartermaster, who was to bring the last ingredient for the feast. When a dragon drove her goblin people from their lands, you slew it, and she gave you a hunk of goblin cheese.",
     ["M95a", "M95b", "M95c"]),
 ],
 "char-shamani": [
   P(S(96), None, "main", "Shamani",
     "A former member of the Company of Heroes, now a vintner at Wineport, who has lost his sight and reads much by smell. Wheiskaet sent you to him for the finest wine.",
     ["M96a", "M96c", "M96b"]),
   P(S(97), None, "main", "Shamani",
     "A blind vintner at Wineport, once a mercenary of the Company of Heroes, who used his savings to take up wine. He says the only wines fit for Master Gegeruju's feast belong to Byrglaent, who refused you.",
     ["M96a", "M96b", "M97c", "M97a", "M97b"]),
   P(S(98), None, "main", "Shamani",
     "A blind vintner at Wineport, once of the Company of Heroes. Titan blinded him beneath O'Ghomoro, and Bacchus wine lifted him from despair and made him a vintner, but the vignerons have none left.",
     ["M96a", "M96b", "M98b", "M98c", "M98a"]),
   P(S(99), None, "main", "Shamani",
     "A blind vintner at Wineport, once of the Company of Heroes, whom Titan blinded beneath O'Ghomoro. He misses his life with the Company and cannot bear to disappoint his former captain. "
     "He sent his own wine to Drest, the man who once nursed him back to health.",
     ["M96a", "M98b", "M99c", "M99a", "M99b"]),
   P(S(101), None, "main", "Shamani",
     "A blind vintner at Wineport, once of the Company of Heroes, still seeking a wine for his former captain. "
     "He sees in Drest, the man who once nursed him back to health, another who struggles not to let his scars define him, and resolves to spend more time with him.",
     ["M96a", "M99a", "M99b", "M101b", "M101c"]),
 ],
 "char-byrglaent": [
   P(S(97), None, "main", "Byrglaent",
     "Owner of the largest winery in Vylbrand, whom Shamani calls the Wine Baron of Limsa Lominsa, a man not known for his tact. He refused to sell wine for Master Gegeruju's feast, offering goobbue urine instead.",
     ["M97a", "M97d", "M97b"]),
 ],
 "char-drest": [
   P(S(99), None, "main", "Drest",
     "A man who once took Shamani in and nursed him back to health, and now lives alone at the Severed String. He accepted Shamani's wine with great trepidation; something is very wrong with him.",
     ["M99b", "M99d", "M99e"]),
   P(S(100), None, "main", "Drest",
     "A hermit at the Severed String who once nursed Shamani back to health. He confessed that he is an imperial deserter, though not Garlean: the Empire conquered his lands. "
     "The Maelstrom caught his unit on a reconnaissance mission and no one else survived, and he toils in secret, hoping one day to go home.",
     ["M99b", "M100a", "E100a", "M100b", "M100c"]),
   P(S(101), None, "main", "Drest",
     "A hermit at the Severed String, an imperial deserter who is not Garlean and hopes one day to go home. Calmer now, he sent palm wine to Shamani, whom he once nursed back to health, and Shamani means to spend more time with him.",
     ["M100a", "M100c", "M99b", "M101a", "M101c"]),
 ],
}

# ---- Relationship types and relationships --------------------------------------------------------------------------
TYPES = [
 ("deserted", "deserted", "deserted by", False),
]

RELS = [
 ("rel-noraxia-aids-scions", "char-noraxia", "aids", "org-scions", S(62), S(106), "main", ["M62c"], ["E106e"]),
 # Backfill for a relationship a later era defines with later evidence (so ADJUST frm cannot move it): it ends
 # exactly where the later record begins.
 ("rel-lahabrea-member-ascians-arr", "char-lahabrea", "member-of", "org-ascians", S(63), S(169), "main", ["M63a"]),
 # New (Meffrid's membership is a backfill too: the 4.0 era records it from #384)
 ("rel-swift-member-immortal-flames", "char-swift", "member-of", "org-immortal-flames", S(63), None, "main", ["M63d"]),
 ("rel-gundobald-leads-little-ala-mhigo", "char-gundobald", "leads", "loc-little-ala-mhigo", S(66), None, "main", ["M66b"]),
 ("rel-gundobald-member-ala-mhigan-resistance", "char-gundobald", "member-of", "org-ala-mhigan-resistance", S(68), None, "main", ["M68a"]),
 ("rel-haribehrt-member-scions", "char-haribehrt", "member-of", "org-scions", S(69), None, "main", ["M68d", "M69a"]),
 ("rel-meffrid-member-ala-mhigan-resistance", "char-meffrid", "member-of", "org-ala-mhigan-resistance", S(69), S(384), "main", ["M69c"]),
 ("rel-titan-summoned-by-kobolds", "char-titan", "summoned-by", "org-kobolds", S(85), None, "main", ["M85a"]),
 ("rel-wheiskaet-serves-gegeruju", "char-wheiskaet", "serves", "char-gegeruju", S(88), None, "main", ["M88c"]),
 ("rel-drest-deserted-garlean-empire", "char-drest", "deserted", "org-garlean-empire", S(100), None, "main", ["M100a"]),
]

ADJUST = {}

ARCS = [
 ("arc-u1-the-masked-man", E_MASK, S(62), S(65)),
 ("arc-u2-the-refugees-trust", E_TRUST, S(66), S(73)),
 ("arc-u3-youngbloods-of-little-ala-mhigo", E_YOUNG, S(74), S(77)),
 ("arc-u4-murders-in-the-shroud", E_SHROUD, S(78), S(84)),
 ("arc-u5-titan-reawakened", E_TITAN, S(85), S(89)),
 ("arc-u6-a-feast-at-costa-del-sol", E_FEAST, S(90), S(101)),
]

CASTS = {
 E_MASK: [("char-minfilia", S(62), ["M62f"]), ("char-lahabrea", S(62), ["M62d"]), ("org-ascians", S(62), ["M62e"]),
          ("org-immortal-flames", S(63), ["M63c"]), ("char-swift", S(63), ["M63d"]), ("char-hihibaru", S(63), ["M63f"]),
          ("org-garlean-empire", S(65), ["M65c"])],
 E_TRUST: [("char-lahabrea", S(66), ["M65d"]), ("char-hihibaru", S(66), ["M66a"]), ("char-gundobald", S(66), ["M66b"]),
           ("loc-little-ala-mhigo", S(66), ["M66b"]), ("org-ala-mhigan-resistance", S(68), ["M68a"]),
           ("char-minfilia", S(68), ["M68d"]), ("char-haribehrt", S(69), ["M69a"]), ("char-meffrid", S(69), ["M69c"])],
 E_YOUNG: [("char-gundobald", S(74), ["M74a"]), ("loc-little-ala-mhigo", S(74), ["M74a"]), ("char-lahabrea", S(74), ["M74b"]),
           ("char-wilred", S(75), ["M75a"]), ("org-garlean-empire", S(75), ["M75c"]), ("loc-ala-mhigo", S(74), ["M74c"]), ("char-minfilia", S(77), ["M77b"]),
           ("org-ascians", S(77), ["M77b"])],
 E_SHROUD: [("char-lahabrea", S(78), ["M78a"]), ("char-minfilia", S(78), ["M78a"]), ("char-noraxia", S(78), ["M78c"]),
            ("char-medrod", S(78), ["M78c"]), ("char-aideen", S(78), ["M78f"]), ("char-ivaurault", S(78), ["M78f"]),
            ("char-ursandel", S(83), ["M83b"]), ("char-amandine", S(84), ["M84a"]), ("org-ascians", S(84), ["M84d"])],
 E_TITAN: [("char-titan", S(85), ["M85a"]), ("org-kobolds", S(85), ["M85a"]), ("org-maelstrom", S(85), ["M85a"]),
           ("char-merlwyb", S(85), ["M85c"]), ("char-minfilia", S(85), ["M85j"]), ("char-yshtola", S(85), ["M85g"]),
           ("org-company-of-heroes", S(85), ["M85b"]), ("char-trachtoum", S(85), ["M85i"]), ("char-wheiskaet", S(88), ["M88a"])],
 E_FEAST: [("char-wheiskaet", S(90), ["M90a"]), ("char-gegeruju", S(90), ["M90a"]), ("char-titan", S(90), ["M90c"]),
           ("org-company-of-heroes", S(90), ["M90b"]), ("char-landenel", S(90), ["M90c"]), ("char-uodh-nunh", S(91), ["M91c"]),
           ("char-brayflox", S(95), ["M95a"]), ("char-shamani", S(96), ["M96a"]), ("char-byrglaent", S(97), ["M97a"]),
           ("char-drest", S(99), ["M99b"])],
}

ARC_NOTES = {
 "arc-u1-the-masked-man": "MSQ #62 *Back from the Wood* to #65 *Where There Is Smoke*. Minfilia first hears of Lahabrea (M62d) and sets you on him; "
   "the trail runs through Swift and Hihibaru to a bandit's Rhalgr scroll, which ties the masked stranger to the Ala Mhigans (M65d). The next arc starts where that lead sends you.",
 "arc-u2-the-refugees-trust": "MSQ #66 *On to Little Ala Mhigo* to #73 *Come Highly Recommended*: Gundobald turns you away (M66c), and the Quarrymill detour with "
   "Haribehrt, Meffrid and Gallien earns the letter that wins him over (M73c). Gallien, Albreda, Charline and Buscarron are named without entries (one-quest roles).",
 "arc-u3-youngbloods-of-little-ala-mhigo": "MSQ #74 to #77 *Back to Square One*: Wilred's band and the failed attempt to summon Rhalgr, ending when the lead is "
   "exhausted and Minfilia reads it as Ascian deception (M77a, M77b). Its name avoids the plot's reveal at #76.",
 "arc-u4-murders-in-the-shroud": "MSQ #78 *Terror at Fallgourd* to #84 *Skeletons in Her Closet*, including both #80 paths (*Seeing Eye to Winged Eye* and *Rock of Rancor*, "
   "both needed for #82). Each #80 recap uses only its own quest and earlier ones, so it reads true in either order. It ends with the two Ascians in Haukke Manor (M84d).",
 "arc-u5-titan-reawakened": "MSQ #85 *Wrath of the Titan* to #89 *Nix That*: the Maelstrom's request (M85a), Trachtoum's false claim and Wheiskaet's first test. "
   "It stops before #90 so that the feast, which runs straight into the accepted Road to Titan (#103), is one arc.",
 "arc-u6-a-feast-at-costa-del-sol": "MSQ #90 *A Modest Proposal* to #101 *Battle Scars*: the ingredient hunt through the Company's veterans and Shamani's search for "
   "wine, with Drest's story (#99–#101). #102 stays the baseline of the accepted content, whose first arc (#103) opens on the same feast. 10 cast members, the cap.",
}

DECISIONS = [
 "Lahabrea is an Ascian from #63 (M63a), but `rel-lahabrea-member-ascians` (#169) cites a later quest, so ADJUST frm cannot move it; "
 "`rel-lahabrea-member-ascians-arr` backfills #63–#169. Merlwyb's leadership of the Maelstrom is already backfilled by the starting-city eras (`rel-merlwyb-leads-maelstrom-arr`).",
 "Noraxia aids the Scions from #62 and the relationship ends at #106, where the accepted content has her dying (end claim E106e).",
 "Titan, the Company of Heroes, Y'shtola, Minfilia and the Scions get presentations here that the accepted #102/#103 records close; Wheiskaet, whom the accepted #103 recap names without an entry, becomes an entity from #88.",
 "Drest's desertion uses a new relationship type, `deserted` (\"deserted\" / \"deserted by\"), rather than `turned-against`: he bears Eorzea no ill will and only wants to go home (M100c).",
 "Minor one-quest figures (Hihira, Gisilbehrt, Albreda, Gallien, Charline, Buscarron, Aethelmaer, Bertliana) are named in text without entries.",
]
