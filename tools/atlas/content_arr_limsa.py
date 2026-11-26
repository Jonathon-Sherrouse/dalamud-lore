"""Atlas content for A Realm Reborn 2.0, the Limsa Lominsa starting-city chain: MSQ #1 Close to Home (Limsa Lominsa) to
#22 The Lominsan Envoy (steps cp-msq-1b … cp-msq-22b). Era tag r.

Data only, per docs/atlas/era-modules.md. Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes A03,
A04 and the first quest of A05); every locator is an exact substring of the quest's saved page (Journal, Steps or main
dialogue). Limsa starters go on to the shared Call of the Sea at cp-msq-23 (the Gridania chain's step), so this chain
ends at The Lominsan Envoy.

Spoiler and chain handling:
  - first names only: no "Bloefhiswyn", "Aldynn", "van Baelsar" or "Sthalmoenwyn" in displayed text;
  - the voice in the Carteneau vision (tagged Lahabrea@??? on the page) stays unnamed, as do the castrum commander and
    the Garlean officer of #22; Nero, Midgardsormr, Eline and Solus stay out of displayed text;
  - "feast", never "banquet" (reserved for 2.55); the Order of the Twin Adder and the Immortal Flames are not named,
    since neither is an entry this early;
  - shared entities (Baderon, Y'shtola, Merlwyb, the Maelstrom, Limsa Lominsa, the Alliance leaders, Hydaelyn …) state
    facts about the entity, not what "you" did in this chain, because the other chains' players see them too. Only the
    arc recaps say "you".
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

S = {n: f"cp-msq-{n}b" for n in range(1, 23)}

Q1 = "Close to Home (Limsa Lominsa)"

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #1 Close to Home (Limsa Lominsa)
 "M1ba": ("Baderon, proprietor of the Drowning Wench, sets you three tasks to learn the basics of adventuring.", Q1, "[[Baderon]], proprietor of [[the Drowning Wench]], wants you to perform three tasks that will help you learn the fundamentals of [[Adventurer|adventuring]]."),
 "M1bb": ("The Yellowjackets keep the peace in the city.", Q1, "I am Sundhimal, one of the Yellowjackets tasked with keeping the peace in the city."),
 "M1bc": ("Baderon blames the Calamity for his poor memory.", Q1, "That bloody Calamity's made a right mess o' me memory, I swear."),
 "M1bd": ("Baderon has sent many novice adventurers to the city's aetheryte.", Q1, "Ah, another novice adventurer. Aye, Baderon has sent more than a few of your kind this way of late."),
 "M1be": ("Baderon urges newcomers to listen to anyone who needs help.", Q1, "if ye 'appen to pass any poor sods what look like they might need yer 'elp, consider givin' their tale o' woe a listen, eh?"),
 "M1bf": ("Your first tasks take you around Limsa Lominsa.", Q1, "As you make your way around [[Limsa Lominsa]], try approaching citizens who appear to be in need of help."),
 # #2 On to Summerford
 "M2ba": ("Baderon sends you to lend a hand at Summerford Farms.", "On to Summerford", "[[Baderon]], proprietor of [[the Drowning Wench]], wants you to lend a hand at [[Summerford Farms]]."),
 "M2bb": ("Staelwyrn, the farm's owner, is an old friend of Baderon.", "On to Summerford", "The owner, Staelwyrn, is an old mate o' mine."),
 "M2bc": ("Many of the farmhands were once pirates.", "On to Summerford", "A good number of the lads and lasses workin' here once terrorized the high seas."),
 "M2bd": ("Staelwyrn's ship was lost in the Calamity.", "On to Summerford", "a vessel lost in the destruction of [[the Calamity]]."),
 "M2be": ("The Calamity ruined the soil, and Staelwyrn is trying to revive the fields.", "On to Summerford", "'as been tryin' to bring a bit o' life back to the fields after the Calamity ruined the soil."),
 "M2bf": ("Staelwyrn accepted an initiative to put landlocked pirates to work in the fields.", "On to Summerford", "Admiral Merlwyb's initiative to get us landlocked buccaneers workin' the fields seemed too fine an offer to refuse."),
 "M2bg": ("Staelwyrn needs a tougher hand to help.", "On to Summerford", "I need a tougher soul like you to step in and help where it's needed."),
 "M2bh": ("The botanists hired to train the ex-pirates despair.", "On to Summerford", "the botanists I called in to train 'em have been wringin' their hands in black despair."),
 # #3 Dressed to Call
 "M3ba": ("Staelwyrn inspects your gear before giving you work.", "Dressed to Call", "Equip your [[head]], [[body]], [[hands]], [[legs]], and [[feet]] with gear of [[Item Level|item level]] 5 or above and present yourself to Staelwyrn for inspection."),
 "M3bb": ("Former buccaneers love the sea and care little for the laws of the land.", "Dressed to Call", "Erstwhile buccaneers are an ornery lot. They rage in love for the sea, and care little for the laws of the land."),
 "M3bc": ("Staelwyrn has work for you once you are ready.", "Dressed to Call", "has work for you whenever you are ready."),
 # #4 Lurkers in the Grotto
 "M4ba": ("Citizens have been vanishing from all over Limsa Lominsa.", "Lurkers in the Grotto", "citizens have been disappearin' from every corner of [[Limsa Lominsa]], as if plucked from the face of Hydaelyn, boots and all, by an unseen hand."),
 "M4bb": ("The farmhands believe the unwelcome visitors are the kidnappers.", "Lurkers in the Grotto", "The farmhands believe the unwelcome visitors to be the rumored kidnappers"),
 "M4bc": ("Men with azure-tattooed faces have been spying on Staelwyrn's yeomen.", "Lurkers in the Grotto", "a collection of right unsavory fellows with azure-tattooed faces has been creepin' up to the edges of the fields and spyin' on my yeomen."),
 "M4bd": ("A woman you meet at the grotto becomes convinced the kidnappers are pirates.", "Lurkers in the Grotto", "the woman seems convinced that the perpetrators of the kidnappings are pirates."),
 "M4be": ("In a vision, a voice tells you the power to banish the Darkness dwells in the Crystals of Light.", "Lurkers in the Grotto", "The power to banish the Darkness dwelleth in the Crystals of Light. Journey forth and lay claim to them."),
 "M4bf": ("The woman at the grotto judges the aetheric disturbance there unnatural.", "Lurkers in the Grotto", "As I suspected, the aetheric disturbance here is no natural occurrence."),
 "M4bg": ("Staelwyrn names the woman as Y'shtola.", "Lurkers in the Grotto", "A woman with a strange contraption...? Ah... [[Y'shtola]]!"),
 "M4bh": ("Staelwyrn vouches that Y'shtola is not one to consort with kidnappers.", "Lurkers in the Grotto", "but she's not the kind to associate with kidnappers. You may take my word for that."),
 "M4bi": ("Staelwyrn suspects pirates have come to lure his farmhands back to plunder.", "Lurkers in the Grotto", "I'm startin' to think that these ruffians are pirates, come to lure my farmhands back to a life of plunder."),
 # #5 Washed Up
 "M5ba": ("Staelwyrn asks you to round up his delinquent yeomen.", "Washed Up", "The old pirate captain requests that you round up the delinquent yeomen and send them back to him."),
 "M5bb": ("Staelwyrn blames Sevrin for the idleness.", "Washed Up", "That sea-sloth Sevrin and his lot"),
 "M5bc": ("Every yeoman returns to work except Sevrin.", "Washed Up", "Staelwyrn informs you that all the yeomen have returned to work except [[Sevrin]]."),
 "M5bd": ("Staelwyrn has let Sevrin slip away many times.", "Washed Up", "I've let that worm wriggle through my fingers more times than I can count."),
 # #6 Double Dealing
 "M6ba": ("Sevrin made off with a sack of oranges to sell to goblins.", "Double Dealing", "[[Sevrin]] has made off with a sack of oranges with the intention of fencing it to [[goblin]]s."),
 "M6bb": ("Sevrin's goblin deal went wrong, leaving his partners in trouble.", "Double Dealing", "His deal with the goblins has gone awry, and his partners in crime are in trouble."),
 "M6bc": ("You save Sevrin's mates from goblin muggers.", "Double Dealing", "You have saved Sevrin's mates from an unfortunate fate at the hands of the [[Goblin Mugger|goblin muggers]]."),
 "M6bd": ("Staelwyrn warns that a man who would leave his mates for dead might do anything.", "Double Dealing", "If he'd leave his own mates for dead, there's no tellin' what he'd do to ''you''."),
 # #7 Loam Maintenance
 "M7ba": ("You gather blackloam from the aurochs' lair called the Cookpot.", "Loam Maintenance", "gather three bushels of blackloam from the lair of [[aurochs]] known as [[the Cookpot]]."),
 "M7bb": ("The soil at Tiller's Rest is barren.", "Loam Maintenance", "Argh, even the weeds wither and die in this desolate dirt."),
 "M7bc": ("Pfrewahl expects a bountiful harvest from the blackloam.", "Loam Maintenance", "we can expect a bountiful harvest as a result."),
 # #8 Plowshares to Swords
 "M8ba": ("Pirates stole farm tools from Tiller's Rest.", "Plowshares to Swords", "Pirates have stolen farm tools from [[Tiller's Rest]]."),
 "M8bb": ("The pirates melt the shovels down into axes.", "Plowshares to Swords", "Stealin' our shovels to melt and forge into axes, of all things."),
 "M8bc": ("The thieves are Serpent Reavers lingering in the area.", "Plowshares to Swords", "dispatch [[The Serpent Reavers|the Reavers]] who linger in the area and recover the tools."),
 "M8bd": ("Pfrewahl saw Sevrin meeting the thieving pirates in secret.", "Plowshares to Swords", "Pfrewahl tells you that he spied [[Sevrin]] consorting surreptitiously with the thieving pirates."),
 "M8be": ("Summerford Farms is safe for now, but not while Sevrin remains.", "Plowshares to Swords", "[[Summerford Farms]] is safe for the time being, but none can rest easy so long as Sevrin remains."),
 "M8bf": ("Staelwyrn vows that Sevrin's treachery will not go unpunished.", "Plowshares to Swords", "His treachery won't go unpunished."),
 # #9 Just Deserts
 "M9ba": ("Sevrin absconded with his band after receiving a curious letter.", "Just Deserts", "Apparently, Sevrin began behaving suspiciously after receiving a curious letter, and subsequently absconded with his band of scoundrels."),
 "M9bb": ("Sevrin lured his lackeys into a trap with the promise of drink.", "Just Deserts", "According to [[Aylmer]], Sevrin lured his lackeys into a trap with the promise of drink."),
 "M9bc": ("A masked mage unleashes a clay golem on you.", "Just Deserts", "you encounter a masked mage who unleashes a towering [[Clay Golem|clay golem]] upon you."),
 "M9bd": ("Y'shtola's presence conjures visions of the past in your mind.", "Just Deserts", "For reasons unknown, [[Y'shtola]]'s presence conjures visions from the past in your mind."),
 "M9be": ("Sevrin was once a Serpent Reaver, who deserted and found a new home at Summerford Farms under a new name.", "Just Deserts", "I was once a Serpent Reaver. … So I crept off one night, got myself a new name, an' found myself a new home─Summerford Farms."),
 "M9bf": ("Sevrin meant to hand his crewmen to the Serpent Reavers, but could not go through with it.", "Just Deserts", "Sevrin explains that he had planned to serve up his crewmen to [[the Serpent Reavers]] as recompense for deserting them, but that in the end he could not bear to sell his soul to save his own skin."),
 "M9bg": ("Staelwyrn takes Sevrin back, but Sevrin means to pay for his crimes.", "Just Deserts", "Though Staelwyrn has taken the penitent pirate back, Sevrin seems determined to pay for his crimes."),
 "M9bh": ("Staelwyrn says the Reavers act like pirates but are the Sahagin's flunkies.", "Just Deserts", "Reavers may look and sound and act like pirates, but they're naught but the fishbacks' flunkies."),
 "M9bi": ("A few years ago the Reavers began seizing law-abiding Lominsans.", "Just Deserts", "A few years back, they started snatchin' law-abidin' Lominsans."),
 "M9bj": ("Y'shtola says the tattooed men are no common pirates but minions of the Sahagin.", "Just Deserts", "But then these tattooed wretches are no common pirates─they are the minions of the Sahagin."),
 "M9bk": ("Y'shtola wonders whether the tribes are planning to summon their primals.", "Just Deserts", "Could it be that the tribes are planning to summon their primals?"),
 "M9bl": ("Sevrin decides to hand himself over to the Yellowjackets.", "Just Deserts", "That's why I'm going to hand myself over to the Yellowjackets."),
 "M9bm": ("Baderon's voice carries weight with the Yellowjackets.", "Just Deserts", "Aware that [[Baderon]]'s voice carries weight with [[the Yellowjackets]]"),
 "M9bn": ("The Yellowjacket who hands out punishments is a good friend of Baderon.", "Just Deserts", "The Yellowjacket as 'ands out the punishments is a good mate o' mine."),
 "M9bo": ("Desertion from the Reavers is punished by death, but they offered Sevrin his freedom in exchange for his mates.", "Just Deserts", "The penalty for desertion is death, but the Reavers offered me a way out instead─my freedom in exchange for my mates'."),
 # #10 Sky-high
 "M10ba": ("Baderon sends you to Wyrkrhit, head of the Skylift.", "Sky-high", "Track down the 'ead o' the operation─bloke by the name o' Wyrkrhit─and 'e'll be sure to put ye to work on a task or two."),
 "M10bb": ("The Skylift is scaffolding attached to the Descent.", "Sky-high", "It's that big bleedin' scaffoldin' attached to the Descent."),
 "M10bc": ("A huge dragon's blast split the ground in half.", "Sky-high", "One blast o' fiery hell from that huge dragon was all it took to split the ground in half."),
 "M10bd": ("The Skylift is overwhelmed with cargo for the restoration.", "Sky-high", "The Skylift is being overwhelmed with the constant flood of cargo needed for the restoration efforts."),
 # #11 Thanks a Million
 "M11ba": ("A wagon driver dropped his load and fled when a creature appeared in his cargo.", "Thanks a Million", "A wagon driver was so startled by the appearance of some nightmarish creature from the midst of his cargo that he dropped the load over the side before fleeing back to the Skylift."),
 "M11bb": ("Wyrkrhit sends you to deliver the seedling to Lyulf at Swiftperch.", "Thanks a Million", "I need ye to head down the road, recover that seedling, an' deliver it to Lyulf over at Swiftperch in western La Noscea."),
 "M11bc": ("Lyulf has gambled his fortune on millioncorn.", "Thanks a Million", "Though I understood there were risks in gambling my entire fortune on a crop of millioncorn"),
 "M11bd": ("Lyulf means to restore hope to Swiftperch with a vast crop of corn.", "Thanks a Million", "Thus I mean to restore a modicum of hope to its residents by growing a veritable ocean of corn!"),
 "M11be": ("The locals of Swiftperch are as desolate as its fields.", "Thanks a Million", "You arrive in Swiftperch to find the locals as desolate of life as the surrounding fields."),
 # #12 Relighting the Torch
 "M12ba": ("Fraeloef, a Yellowjacket at Swiftperch, sends you to find out why the Brewer's Beacon is dimming.", "Relighting the Torch", "[[Fraeloef]], a [[The Yellowjackets|Yellowjacket]] on guard duty in [[Swiftperch]], wants you to visit [[the Brewer's Beacon]] and investigate the reason behind the waning light."),
 "M12bb": ("The bomb that fuels the beacon's furnace has escaped.", "Relighting the Torch", "The bomb what fuels me furnace has up an' buggered off, ye see."),
 "M12bc": ("The keeper doubts her makeshift repairs.", "Relighting the Torch", "Khanswys is dubious about the quality of her makeshift repairs."),
 "M12bd": ("You are to ask Forgemaster H'naanza to oversee the repairs.", "Relighting the Torch", "ask Forgemaster [[H'naanza]] to oversee the necessary repairs"),
 "M12be": ("Something else may have caused the furnace to fail.", "Relighting the Torch", "but could there be another reason for the device's failure...?"),
 # #13 On to the Drydocks
 "M13ba": ("H'naanza sends you to help at the Moraby Drydocks.", "On to the Drydocks", "Forgemaster [[H'naanza]], head of [[Naldiq & Vymelli's]], wants you to assist with the workload over at the [[Moraby Drydocks]]."),
 "M13bb": ("Ahtbyrm is the head shipwright at the Moraby Drydocks.", "On to the Drydocks", "deliver a [[Naldiq & Vymelli Missive|missive]] to [[Ahtbyrm]], the head shipwright at the Moraby Drydocks."),
 "M13bc": ("The Victory is the first new vessel at the docks since the Calamity.", "On to the Drydocks", "this proud maiden you see taking shape before you is the Victory, the first new vessel to grace the docks since the Calamity."),
 "M13bd": ("The Maelstrom lost most of its ships in the Calamity, and the Victory is the start of restoring its fleet.", "On to the Drydocks", "We may have lost the bulk of our ships that fateful day, but starting with this beauty, we will restore the Maelstrom's fleet to its former glory."),
 "M13be": ("Another delay in materials infuriates Ahtbyrm.", "On to the Drydocks", "Blast and botheration! Another delay? I am well aware of the shortage of skilled artisans, but this is insufferable!"),
 "M13bf": ("Ahtbyrm is hiring veteran shipwrights from abroad.", "On to the Drydocks", "even going so far as to hire veteran shipwrights from outside the thalassocracy."),
 # #14 Without a Doubt
 "M14ba": ("Ahtbyrm's young shipwright Fyrilsmyd went for supplies and has not returned.", "Without a Doubt", "A shipwright of mine─a young man named Fyrilsmyd─recently left Candlekeep Quay to retrieve several crates of supplies ordered from Limsa Lominsa"),
 "M14bb": ("Ahtbyrm doubts that Haldbroda is telling the whole truth.", "Without a Doubt", "That man knows something, and I severely doubt he is telling me the whole truth."),
 "M14bc": ("Haldbroda swears he knows nothing of Fyrilsmyd.", "Without a Doubt", "I swear on my poor nana's grave, Navigator rest her soul, I know naught of this Fyrilsmyd, nor his precious supplies."),
 "M14bd": ("Fyrilsmyd may have been caught in a wreck off the Salt Strand.", "Without a Doubt", "Could it be that the young shipwright was somehow caught up in the tragedy that claimed a ship off of [[the Salt Strand]]?"),
 # #15 Righting the Shipwright
 "M15ba": ("Fyrilsmyd's boat was flung into a Lominsan galley.", "Righting the Shipwright", "and we was flung headlong into the Lominsan galley."),
 "M15bb": ("The lost cargo is guarded by Qiqirn beachcombers.", "Righting the Shipwright", "the cargo that is now guarded by deadly [[Qiqirn Beachcomber|Qiqirn beachcombers]]."),
 "M15bc": ("You salvage all three missing pieces of cargo.", "Righting the Shipwright", "You have salvaged all three missing pieces of cargo."),
 "M15bd": ("Ahtbyrm suspects the Sahagin conjured the trouble off Candlekeep Quay.", "Righting the Shipwright", "This leads me to believe that the trouble the ships encountered off Candlekeep Quay was of a less natural sort─the sort which the Sahagin have been known to conjure."),
 # #16 Do Angry Pirates Dream
 "M16ba": ("Ghimthota heads the Moraby Drydocks watch and seeks help with suspicious campers on the Gods' Grip.", "Do Angry Pirates Dream", "Head of the [[Moraby Drydocks]] watch, [[Ghimthota]] has asked ''Victory'' foreman Ahtbyrm to recommend an [[adventurer]] to assist the watch in learning more about a band of suspicious individuals who have recently made camp on [[the Gods' Grip]]."),
 "M16bb": ("Ghimthota believes they are pirates planning to sabotage the Victory.", "Do Angry Pirates Dream", "Ghimthota believes the suspicious individuals in question to be pirates who are planning to sabotage the ''Victory''."),
 "M16bc": ("Ghimthota asks you to pose as a lost adventurer.", "Do Angry Pirates Dream", "I would have you approach the men, posing as a lost adventurer, and see if you cannot somehow learn of their intentions."),
 "M16bd": ("They truly are pirates, and may be plotting a kidnapping.", "Do Angry Pirates Dream", "they truly are pirates, and that they could be plotting a kidnapping."),
 "M16be": ("One pirate wants \"me boy\" back.", "Do Angry Pirates Dream", "Once we 'ave me boy back, I'm puttin' this godsforsaken piss'ole of an island so far behind me"),
 "M16bf": ("Ghimthota wonders whether the Victory was ever their target.", "Do Angry Pirates Dream", "Could it be that their target never was the Victory?"),
 "M16bg": ("Ghimthota increases patrols.", "Do Angry Pirates Dream", "Upon learning of the pirates' plot, Ghimthota resolves to increase patrols of the area."),
 # #17 Victory in Peril
 "M17ba": ("Ghimthota is convinced the pirates mean to sabotage the Victory.", "Victory in Peril", "Ghimthota is convinced that a gang of treacherous pirates aims to sabotage the construction of the ''Victory''."),
 "M17bb": ("The pirates at the shipyard carry explosives.", "Victory in Peril", "Seemed to be carrying...explosives..."),
 "M17bc": ("The pirates' leader, Ahtzapfyn, is Ahtbyrm's father.", "Victory in Peril", "the leader of the pirates, [[Ahtzapfyn]], is actually [[Ahtbyrm]]'s father."),
 "M17bd": ("Ahtzapfyn calls the Victory a symbol of all that went wrong with the world, and means to shatter it.", "Victory in Peril", "This ship's a symbol alright─of everythin' what went wrong with the world. An' I mean to shatter it into a hunnerd thousand pieces!"),
 "M17be": ("Mamool Ja mercenaries fight alongside Ahtzapfyn by agreement.", "Victory in Peril", "As we agreed, Ahtzapfyn! … I'll take the Mamool Ja. You focus on Ahtzapfyn."),
 "M17bf": ("Ahtzapfyn is defeated.", "Victory in Peril", "I...I must be gettin' old, lettin' some green 'venturer get the best o' me."),
 "M17bg": ("Ahtbyrm says his father has always turned his life upside down.", "Victory in Peril", "Ever did my father have a way of turning my life upside down."),
 "M17bh": ("The defeated pirates are handed to the Yellowjackets, and Reyner's men take over the investigation.", "Victory in Peril", "the pirates we defeated have been handed over to the Yellowjackets. Reyner's men will be taking over the investigation."),
 "M17bi": ("Ghimthota recovered an unusual object.", "Victory in Peril", "Before the Yellowjackets moved in, however, we recovered a most unusual object."),
 # #18 Men of the Blue Tattoos
 "M18ba": ("A coded missive is found among the belongings of Ahtzapfyn, the pirate behind the plot.", "Men of the Blue Tattoos", "Among the possessions of [[Ahtzapfyn]], the pirate behind the plot to sabotage the ''Victory'', a [[Arcane Epistle|missive]] written in some manner of code has been discovered."),
 "M18bb": ("The Yellowjackets turn to Baderon and his connections in such cases.", "Men of the Blue Tattoos", "In cases such as this, I am told the Yellowjackets are wont to turn to Baderon and his convenient...connections."),
 "M18bc": ("Ahtbyrm is still reeling at his father's part in the plot.", "Men of the Blue Tattoos", "Poor sod was still reelin' at 'is old man's part in the business"),
 "M18bd": ("Having read the missive, Baderon is visibly worried.", "Men of the Blue Tattoos", "a visibly worried Baderon bids you prepare for the worst."),
 "M18be": ("Baderon says trouble is brewing.", "Men of the Blue Tattoos", "We've got us some trouble brewin', 'ere, an' no mistake."),
 # #19 Feint and Strike
 "M19ba": ("The missive ordered the Victory destroyed and named Swiftperch as a feint, but Baderon believes the Serpent Reavers will strike it in full force.", "Feint and Strike", "The missive Baderon deciphered contains orders for the destruction of the ''Victory''. While the message meant for [[Ahtzapfyn]] also mentioned that [[Swiftperch]] would be the site of a simple feint operation, the [[Drowning Wench|Wench]]'s proprietor seems convinced that the [[The Serpent Reavers|Serpent Reavers]] intend to commit their full forces to the attack on the struggling settlement."),
 "M19bb": ("Baderon says the attack on the Victory was meant as a distraction.", "Feint and Strike", "That mess at the ''Victory''─that was meant to be the bloody distraction!"),
 "M19bc": ("The Victory is the Maelstrom's new flagship.", "Feint and Strike", "then 'it the Maelstrom's new flagship in the confusion."),
 "M19bd": ("Commodore Reyner is at the Coral Tower.", "Feint and Strike", "deliver it to Commodore [[Reyner]] at the [[Coral Tower]]."),
 "M19be": ("Reyner marshals the Yellowjackets for battle.", "Feint and Strike", "I will marshal the Yellowjackets for battle immediately."),
 "M19bf": ("Sahagin forces assault South Tidegate.", "Feint and Strike", "Reyner receives word that the [[South Tidegate]] is under assault by [[Sahagin]] forces."),
 "M19bg": ("Reyner says the Serpent Reavers are in league with the Sahagin.", "Feint and Strike", "Aye, the Serpent Reavers are in league with the Sahagin."),
 "M19bh": ("You and the Yellowjackets defeat the Reavers at Swiftperch; Y'shtola, a Sharlayan, says a masked Ascian was manipulating the Sahagin and their pirate allies.", "Feint and Strike", "you have defeated the marauding Serpent Reavers and protected the residents of Swiftperch. According to the [[Sharlayan]] native, [[Y'shtola]], it seems that the Sahagin and their pirate allies were being manipulated by a masked mage she called an “[[Ascian]].”"),
 "M19bi": ("A strange black crystal lay near the mage's remains, and the truth behind the kidnappings has come to light.", "Feint and Strike", "not the least of which is a strange black crystal you discovered near the mage's remains, the truth behind the kidnappings has finally come to light."),
 "M19bj": ("The Ascians are known as the Bringers of Chaos.", "Feint and Strike", "They are known as the Bringers of Chaos...or ''Ascians'', to give them their proper name."),
 "M19bk": ("Y'shtola says the Ascians have been manipulating the beast tribes.", "Feint and Strike", "it is they who have been manipulating the beast tribes."),
 "M19bl": ("Y'shtola has worked with the Yellowjackets for some time.", "Feint and Strike", "Y'shtola has been working with us for quite some time, you see."),
 "M19bm": ("Y'shtola assisted the Yellowjackets' kidnapping investigation, a stalwart ally of Limsa Lominsa.", "Feint and Strike", "And she was only too willing to assist the Yellowjackets in the kidnapping investigation, proving herself a stalwart ally of Limsa Lominsa yet again."),
 "M19bn": ("Admiral Merlwyb thanks you for your service to Limsa Lominsa and invites you to a feast.", "Feint and Strike", "Admiral [[Merlwyb]] expresses her heartfelt gratitude for the numerous deeds you have performed in the service of [[Limsa Lominsa]]. As part of your reward, the Admiral insists that you attend an upcoming banquet and be honored before the gathered dignitaries."),
 "M19bo": ("Merlwyb calls Baderon a good friend, and hears of your deeds from him and Reyner.", "Feint and Strike", "my good friend Baderon and Commodore Reyner have taken turns of regaling me with tales of your exploits."),
 "M19bp": ("Merlwyb is Admiral of Limsa Lominsa.", "Feint and Strike", "Admiral of Limsa Lominsa."),
 # #20 High Society
 "M20ba": ("Reyner says the Admiral's invitation is an honor even her own officers rarely receive.", "High Society", "It is a highly coveted honor. Why, even the officers under her direct command are rarely afforded such recognition!"),
 "M20bb": ("Baderon sends you to J'nasshym of the Brugaire Consortium at the Octant.", "High Society", "Take yerself over to the Octant an' speak to J'nasshym o' the Brugaire Consortium."),
 "M20bc": ("The dress shoes are a gift from Baderon and the people you have helped.", "High Society", "the footwear is a gift from him, and from all the people you have aided on your travels."),
 # #21 A Mizzenmast Repast
 "M21ba": ("At the feast Merlwyb recounts the Warriors of Light, and the tale triggers a vision of the Battle of Carteneau.", "A Mizzenmast Repast", "At the banquet, [[Merlwyb]] recounts the deeds of the half-remembered heroes whom [[Eorzea]]ns now call the [[Warrior of Light|Warriors of Light]]. The tale triggers inside your mind a vision of the final moments of the [[Battle of Carteneau]]."),
 "M21bb": ("The Serpent Reavers have pledged themselves to the primal Leviathan.", "A Mizzenmast Repast", "Their ranks are formed of cutthroats and madmen who have pledged themselves body and soul to the primal Leviathan."),
 "M21bc": ("The Reavers swelled their numbers by spiriting people away.", "A Mizzenmast Repast", "they sought to swell their numbers by spiriting away any soul unfortunate enough to cross their path."),
 "M21bd": ("Leviathan is the Sahagin's god, and Limsa Lominsa bears the Sahagin deep animosity.", "A Mizzenmast Repast", "I need not tell you the depth of the animosity between us and the Sahagin. How any seaman worth his salt could devote himself to the fishbacks' god"),
 "M21be": ("Y'shtola identifies your crystal as one of the Crystals of Light.", "A Mizzenmast Repast", "This...is one of the Crystals of Light."),
 "M21bf": ("Merlwyb calls you the vessel of a higher power: the Mothercrystal of your vision.", "A Mizzenmast Repast", "You are the vessel of a higher power. … This...being from your vision was the Mothercrystal."),
 "M21bg": ("It is Hydaelyn who speaks.", "A Mizzenmast Repast", "Heed well Her words, adventurer. For it is Hydaelyn Herself who speaks."),
 "M21bh": ("The Warriors of Light joined the Grand Companies against the Garlean conquest and helped reforge the Eorzean Alliance.", "A Mizzenmast Repast", "When the Garlean Empire began its conquest of the realm, these heroes joined the Grand Companies, and helped reforge the Eorzean Alliance."),
 "M21bi": ("The Warriors of Light were lost at Carteneau.", "A Mizzenmast Repast", "It was on that day, in the midst of that hell...that we lost them."),
 "M21bj": ("No one can speak the Warriors of Light's names.", "A Mizzenmast Repast", "Yet, whenever we try to shout their names, the sound dies in our throats."),
 "M21bk": ("At Carteneau Merlwyb ordered all Maelstrom units to fall back.", "A Mizzenmast Repast", "Belay previous orders! All Maelstrom units are commanded to fall back, effective immediately!"),
 "M21bl": ("A voice in the vision says the planet will soon regain its true form.", "A Mizzenmast Repast", "It has begun. Soon the planet will regain its true form."),
 "M21bm": ("You wake in the Drowning Wench with no idea how you got there.", "A Mizzenmast Repast", "you are surprised to find yourself in a room at [[the Drowning Wench]], with no idea how you got there."),
 "M21bn": ("Merlwyb has a task she would entrust to no one else.", "A Mizzenmast Repast", "Merlwyb has a task for you─one which she would entrust to no other."),
 # #22 The Lominsan Envoy
 "M22ba": ("Merlwyb makes you her personal envoy to the other two Alliance leaders.", "The Lominsan Envoy", "Appointing you her personal envoy, Merlwyb bids you deliver a missive to the other two leaders of the [[Eorzean Alliance]]."),
 "M22bb": ("Merlwyb proposes a memorial service in each city-state on the fifth anniversary of Carteneau.", "The Lominsan Envoy", "To that end, I am proposing that a memorial service be held in each of the city–states on the fifth anniversary of the Battle of Carteneau."),
 "M22bc": ("The Eorzean Alliance is Limsa Lominsa, Gridania and Ul'dah.", "The Lominsan Envoy", "In addition to [[Limsa Lominsa]], the Eorzean Alliance encompasses the city–states of [[Gridania]] and [[Ul'dah]]."),
 "M22bd": ("Kan-E-Senna is Elder Seedseer of Gridania and leads its Grand Company.", "The Lominsan Envoy", "I am Kan-E-Senna, Elder Seedseer of Gridania, and leader of the Order of the Twin Adder, our nation's Grand Company."),
 "M22be": ("The Garleans' Meteor project would tear the lesser moon, Dalamud, from the heavens.", "The Lominsan Envoy", "the Meteor project, by which the lesser moon, Dalamud, would be torn down from the heavens to annihilate all life below."),
 "M22bf": ("The elder primal Bahamut emerged from Dalamud and rained fire on Eorzea.", "The Lominsan Envoy", "from it emerged the elder primal Bahamut, who proceeded to rain fire upon Eorzea."),
 "M22bg": ("The devastation is called the Calamity, and the nations still struggle to rebuild.", "The Lominsan Envoy", "The Calamity, as the devastation wrought by Bahamut has come to be known, laid our nations nigh to waste, and to this day we struggle to rebuild our lives and homes."),
 "M22bh": ("Kan-E-Senna approves the memorial.", "The Lominsan Envoy", "I wholeheartedly approve of the Admiral's proposal."),
 "M22bi": ("Kan-E-Senna hopes a remembrance service will rekindle the Alliance's spirit of unity.", "The Lominsan Envoy", "A remembrance service may well present an opportunity to rekindle the spirit of unity which first gave rise to the Alliance."),
 "M22bj": ("Raubahn is the Flame General of Ul'dah.", "The Lominsan Envoy", "Having safely arrived in Ul'dah, you must now seek an audience with [[Raubahn|the Flame General]]."),
 "M22bk": ("The XIVth Imperial Legion is still entrenched within Eorzea's borders.", "The Lominsan Envoy", "But the XIVth Imperial Legion is still entrenched within our borders."),
 "M22bl": ("Raubahn says the Legion's commander has long harbored ambitions of conquest.", "The Lominsan Envoy", "has long harbored ambitions of conquest."),
 "M22bm": ("Raubahn calls the realm an alliance in name only.", "The Lominsan Envoy", "We are a realm divided, adventurer. An alliance in name only."),
 "M22bn": ("Raubahn agrees to the memorial.", "The Lominsan Envoy", "Merlwyb will have her memorial."),
 "M22bo": ("Once the Garleans mastered magitek, they seized their neighbors' lands, then set their sights on Eorzea.", "The Lominsan Envoy", "No sooner had they learned how to use magitek than they began seizing territory from their neighbors. … An empire which then set its sights upon Eorzea."),
 "M22bp": ("The XIVth Imperial Legion is led by Legatus Gaius.", "The Lominsan Envoy", "with the [[XIVth Imperial Legion]], led by Legatus [[Gaius van Baelsar]], deeply entrenched in the border regions."),
 "M22bq": ("In an imperial castrum, a commander recalls the failed invasion of Mor Dhona fifteen years ago.", "The Lominsan Envoy", "Fifteen years since the imperial fleet set course for Mor Dhona … Our invincible flagship was lost, and all hope of victory with her."),
 "M22br": ("He declares that only Garlean rule can bring order to Eorzea.", "The Lominsan Envoy", "Only Garlean rule can bring order to Eorzea."),
 "M22bs": ("Eorzea's city-states formed the Grand Companies and allied against the Empire.", "The Lominsan Envoy", "Rising in resistance, the city–states of Eorzea formed the Grand Companies, and joined hands in alliance."),
 "M22bt": ("Ul'dah is a sultanate.", "The Lominsan Envoy", "Welcome to the sultanate of Ul'dah."),
 "M22bu": ("Five years have passed since Carteneau.", "The Lominsan Envoy", "It has been five years since those of us who were spared dragged ourselves from the ashes"),
 "M22bv": ("The beast tribes keep summoning primals while the Empire encroaches on Eorzea's borders.", "The Lominsan Envoy", "the beast tribes continue to summon their primals, while the Empire encroaches upon our borders, consolidating its foothold in Eorzea."),
}

# ---- Entities this era introduces ---------------------------------------------------------------------------------
# Shared IDs that later eras (2.1–2.3) create are listed too, with the same category, so this module lints on its own.
ARC_SUMMERFORD, ARC_REBUILD, ARC_DRYDOCKS, ARC_HONOR = (
    "evt-trouble-at-summerford", "evt-rebuilding-la-noscea", "evt-the-drydocks-plot", "evt-the-admirals-honor")
ENTITIES = {
 ARC_SUMMERFORD: "event", ARC_REBUILD: "event", ARC_DRYDOCKS: "event", ARC_HONOR: "event",
 "char-baderon": "character", "char-staelwyrn": "character", "char-sevrin": "character",
 "char-ahtbyrm": "character", "char-ahtzapfyn": "character", "char-ghimthota": "character", "char-reyner": "character",
 "org-yellowjackets": "organization", "loc-summerford-farms": "location",
 "loc-limsa-lominsa": "location", "loc-gridania": "location", "loc-uldah": "location",
 # created by later eras (content_2_1_to_2_3); same categories
 "char-merlwyb": "character", "char-kan-e-senna": "character", "char-raubahn": "character", "char-hydaelyn": "character",
 "char-leviathan": "character", "org-maelstrom": "organization", "org-serpent-reavers": "organization",
 "org-sahagin": "organization", "org-ascians": "organization",
}

N_SUM, N_REB, N_DRY, N_HON = "Trouble at Summerford", "Rebuilding La Noscea", "The Drydocks Plot", "The Admiral's Honor"
REB_LEAD = "La Noscea is rebuilding after the Calamity. "

# ---- Presentations ------------------------------------------------------------------------------------------------
PRES = {
 # Arc entries: one recap per step
 ARC_SUMMERFORD: [
   P(S[2], None, "main", N_SUM,
     "Baderon of the Drowning Wench sent you to Summerford Farms, run by his old friend Staelwyrn. A former pirate captain whose ship was lost in the Calamity, "
     "Staelwyrn is trying to revive soil the Calamity ruined with farmhands who once sailed as pirates. His botanists despair of training them, and he has asked you to step in.",
     ["M2ba", "M2bb", "M2bd", "M2be", "M2bc", "M2bh", "M2bg"]),
   P(S[3], None, "main", N_SUM,
     "At Summerford Farms, Baderon's old friend Staelwyrn, a former pirate captain, is reviving fields the Calamity ruined with a crew of ex-pirates. "
     "Those ornery buccaneers love the sea and care little for the laws of the land, so he wouldn't hand you work until you were properly kitted out. Now he has work for you.",
     ["M2bb", "M2be", "M2bc", "M3bb", "M3ba", "M3bc"]),
   P(S[4], None, "main", N_SUM,
     "Citizens are vanishing all over Limsa Lominsa, and Staelwyrn's farmhands blame azure-tattooed men spying on the fields. At Seasong Grotto you met Y'shtola, "
     "who found the aetheric disturbance there unnatural, and a vision told you to claim the Crystals of Light. She now believes the kidnappers are pirates, "
     "and Staelwyrn suspects they mean to lure his farmhands back to plunder.",
     ["M4ba", "M4bb", "M4bc", "M4bg", "M4bf", "M4be", "M4bd", "M4bi"]),
   P(S[5], None, "main", N_SUM,
     "Citizens are vanishing across Limsa Lominsa, and Staelwyrn suspects pirates of luring his ex-pirate farmhands back to plunder. "
     "When his yeomen wandered off you rounded up all five, but Sevrin, whom Staelwyrn blames for the idleness, slipped away again, as he has many times before.",
     ["M4ba", "M4bi", "M5ba", "M5bb", "M5bc", "M5bd"]),
   P(S[6], None, "main", N_SUM,
     "Staelwyrn fears pirates are luring his farmhands back to plunder. Sevrin, the yeoman who keeps slipping away, stole a sack of oranges to sell to goblins, "
     "and when the deal went wrong he left his mates in trouble. You saved them, and Staelwyrn warns that a man who would leave his own mates for dead might do anything.",
     ["M4bi", "M5bc", "M6ba", "M6bb", "M6bc", "M6bd"]),
   P(S[7], None, "main", N_SUM,
     "Staelwyrn fears pirates are luring his farmhands back to plunder, and Sevrin, who abandoned his mates over a goblin deal, is not to be trusted. "
     "Meanwhile you fetched blackloam from an aurochs' lair, the Cookpot, for the barren fields of Tiller's Rest, where Pfrewahl now expects a bountiful harvest.",
     ["M4bi", "M6bb", "M6bd", "M7ba", "M7bb", "M7bc"]),
   P(S[8], None, "main", N_SUM,
     "Pirates of the Serpent Reavers stole farm tools from Tiller's Rest to melt into axes, and you took them back. "
     "Pfrewahl says he saw Sevrin, the Summerford yeoman who abandoned his mates, meeting the thieves in secret. "
     "Summerford Farms is safe for now, but Staelwyrn swears Sevrin's treachery won't go unpunished.",
     ["M8ba", "M8bb", "M8bc", "M8bd", "M6bb", "M8be", "M8bf"]),
   P(S[9], None, "main", N_SUM,
     "Sevrin led his mates into a trap, where you saved them and fought a masked mage's clay golem. He confessed that he deserted the Serpent Reavers and meant to trade his mates "
     "for his freedom, but couldn't. Y'shtola says the tattooed Reavers serve the Sahagin, and wonders whether the tribes mean to summon their primals. "
     "Sevrin will give himself up to the Yellowjackets.",
     ["M9bb", "M9bc", "M9be", "M9bo", "M9bf", "M9bj", "M9bk", "M9bl"]),
 ],
 ARC_REBUILD: [
   P(S[10], None, "main", N_REB,
     REB_LEAD + "Baderon sent you to the Skylift, scaffolding on the Descent where a huge dragon's blast once split the ground in half. "
     "It is swamped with cargo for the restoration, and its head, Wyrkrhit, has odd jobs for you.",
     ["M10ba", "M10bb", "M10bc", "M10bd"]),
   P(S[11], None, "main", N_REB,
     REB_LEAD + "When a creature burst from a millioncorn seedling bound from the Skylift and its driver fled, you recovered the seedling for Lyulf at Swiftperch, "
     "who has gambled his whole fortune on corn to bring hope back to the desolate settlement.",
     ["M10bd", "M11ba", "M11bb", "M11bc", "M11bd", "M11be"]),
   P(S[12], None, "main", N_REB,
     REB_LEAD + "At Swiftperch, the Yellowjacket Fraeloef sent you to the Brewer's Beacon, whose light was failing because the bomb fueling its furnace had escaped. "
     "The keeper made a makeshift repair, but Forgemaster H'naanza wonders whether something else made the furnace fail.",
     ["M12ba", "M12bb", "M12bc", "M12bd", "M12be"]),
   P(S[13], None, "main", N_REB,
     REB_LEAD + "Forgemaster H'naanza sent you to the Moraby Drydocks, where the head shipwright, Ahtbyrm, is building the Victory: the first new ship there since the Calamity "
     "and the start of restoring the Maelstrom's fleet. Delayed materials infuriate him, but he has work for you.",
     ["M13ba", "M13bb", "M13bc", "M13bd", "M13be"]),
   P(S[14], None, "main", N_REB,
     "At the Moraby Drydocks, the head shipwright Ahtbyrm is building the Victory to restore the Maelstrom's fleet, but materials keep running late. "
     "His shipwright Fyrilsmyd vanished on a supply run, and Ahtbyrm sent you to press Haldbroda at Candlekeep Quay. "
     "Haldbroda swears he knows nothing, and the young man may have been caught in a wreck off the Salt Strand.",
     ["M13bb", "M13bd", "M13be", "M14ba", "M14bb", "M14bc", "M14bd"]),
   P(S[15], None, "main", N_REB,
     "Ahtbyrm is building the Victory at the Moraby Drydocks to restore the Maelstrom's fleet. You found his missing shipwright, Fyrilsmyd, alive on the Salt Strand "
     "after his boat was flung into a Lominsan galley, and won back the ship's lost cargo from Qiqirn beachcombers. Ahtbyrm suspects the Sahagin conjured the trouble.",
     ["M13bb", "M13bd", "M14ba", "M15ba", "M15bb", "M15bc", "M15bd"]),
 ],
 ARC_DRYDOCKS: [
   P(S[16], None, "main", N_DRY,
     "Ghimthota, head of the Moraby Drydocks watch, believes pirates camped on the Gods' Grip mean to sabotage the Victory, the warship Ahtbyrm is building. "
     "Posing as a lost adventurer, you learned they truly are pirates, perhaps plotting a kidnapping: one wants his boy back. "
     "Ghimthota wonders whether the Victory was ever their target, and has stepped up patrols.",
     ["M16ba", "M16bb", "M13bb", "M16bc", "M16bd", "M16be", "M16bf", "M16bg"]),
   P(S[17], None, "main", N_DRY,
     "Pirates with explosives struck the Moraby Drydocks to destroy the Victory, and you fought them off. Their leader, Ahtzapfyn, is the shipwright Ahtbyrm's father, "
     "and calls the ship a symbol of everything that went wrong with the world; Mamool Ja mercenaries fought beside him. "
     "The captured pirates went to the Yellowjackets.",
     ["M17ba", "M17bb", "M17bc", "M17bd", "M17be", "M17bf", "M17bh"]),
   P(S[18], None, "main", N_DRY,
     "Pirates led by Ahtzapfyn, the shipwright Ahtbyrm's own father, tried to destroy the Victory at the Moraby Drydocks. "
     "Among Ahtzapfyn's belongings was a missive in code, so Ghimthota sent you to Baderon, whose connections the Yellowjackets rely on. "
     "Having read it, a worried Baderon says trouble is brewing.",
     ["M17bc", "M17bd", "M18ba", "M18bb", "M18bd", "M18be"]),
   P(S[19], None, "main", N_DRY,
     "Baderon decoded the pirates' missive: the attack on the Victory was a distraction, and the Serpent Reavers, in league with the Sahagin, were after Swiftperch. "
     "While the Sahagin assaulted South Tidegate, you helped the Yellowjackets drive the Reavers off, and Y'shtola named the masked mage behind them an Ascian. "
     "Admiral Merlwyb has thanked you and invited you to a feast.",
     ["M19ba", "M19bb", "M19bg", "M19bf", "M19bh", "M19bn"]),
 ],
 ARC_HONOR: [
   P(S[20], None, "main", N_HON,
     "After you saved Swiftperch from the Serpent Reavers, Admiral Merlwyb invited you to a feast, an honor Commodore Reyner says even her own officers rarely receive. "
     "To look the part, you collected a box from J'nasshym at the Octant, and Baderon presented the dress shoes inside, a gift from him and everyone you have helped.",
     ["M19bh", "M19bn", "M20ba", "M20bb", "M20bc"]),
   P(S[21], None, "main", N_HON,
     "At Admiral Merlwyb's feast, Y'shtola recognized your crystal as one of the Crystals of Light, and Merlwyb named you the vessel of the Mothercrystal, Hydaelyn. "
     "Her tale of the lost Warriors of Light brought on a vision of the Battle of Carteneau, where a voice proclaimed that the planet would regain its true form. "
     "You woke at the Drowning Wench, and Merlwyb has a task for you.",
     ["M21be", "M21bf", "M21bg", "M21ba", "M21bi", "M21bl", "M21bm", "M21bn"]),
   P(S[22], None, "main", N_HON,
     "Admiral Merlwyb made you her envoy, carrying letters that propose memorials on the fifth anniversary of Carteneau. In Gridania, Kan-E-Senna told how Bahamut rose from Dalamud "
     "and burned Eorzea, and approved; in Ul'dah, Raubahn warned that the XIVth Imperial Legion is entrenched in a divided realm, and agreed. "
     "Meanwhile, in an imperial castrum, a commander vowed Garlean rule over Eorzea.",
     ["M22ba", "M22bb", "M22bf", "M22bh", "M22bk", "M22bm", "M22bn", "M22br"]),
 ],

 # Shared with the other chains and later eras: facts about the entity, not what "you" did in this chain.
 "char-baderon": [
   P(S[1], None, "main", "Baderon",
     "Proprietor of the Drowning Wench in Limsa Lominsa, who sets newly arrived adventurers simple tasks to learn the basics, and urges them to help anyone in need. "
     "He blames the Calamity for his poor memory.",
     ["M1ba", "M1bd", "M1be", "M1bc"]),
   P(S[9], None, "main", "Baderon",
     "Proprietor of the Drowning Wench in Limsa Lominsa, who finds work for adventurers around La Noscea. "
     "His voice carries weight with the Yellowjackets, and the one who hands out their punishments is a good friend of his.",
     ["M1ba", "M2ba", "M9bm", "M9bn"]),
   P(S[19], None, "main", "Baderon",
     "Proprietor of the Drowning Wench in Limsa Lominsa and a good friend of Admiral Merlwyb. The Yellowjackets turn to him and his connections in unusual cases: "
     "he decoded a pirate missive revealing that an attack on the warship Victory was a distraction, and that the Serpent Reavers meant to strike Swiftperch.",
     ["M1ba", "M19bo", "M18bb", "M19bb", "M19ba"]),
 ],
 "char-staelwyrn": [
   P(S[2], None, "main", "Staelwyrn",
     "Owner of Summerford Farms and an old friend of Baderon. A former pirate captain whose ship was lost in the Calamity, he took up an offer to put landlocked buccaneers to work in the fields, "
     "and is trying to revive the ruined soil with farmhands who once sailed as pirates.",
     ["M2bb", "M2bd", "M2bf", "M2be", "M2bc"]),
   P(S[4], None, "main", "Staelwyrn",
     "Owner of Summerford Farms, a former pirate captain who now works the land with ex-pirates. His farmhands fear azure-tattooed men spying on the fields, "
     "and he suspects pirates have come to lure his crew back to plunder.",
     ["M2bb", "M2bc", "M4bc", "M4bb", "M4bi"]),
   P(S[9], None, "main", "Staelwyrn",
     "Owner of Summerford Farms, a former pirate captain who now works the land with ex-pirates. He took back Sevrin, the yeoman who nearly betrayed his mates to the Serpent Reavers, "
     "and says the Reavers may act like pirates but are the Sahagin's flunkies.",
     ["M2bb", "M2bc", "M9bg", "M9bf", "M9bh"]),
 ],
 "char-sevrin": [
   P(S[5], None, "main", "Sevrin",
     "A yeoman at Summerford Farms whom Staelwyrn blames for his crew's idleness. He keeps slipping away from work.",
     ["M5bb", "M5bc", "M5bd"]),
   P(S[6], None, "main", "Sevrin",
     "A yeoman at Summerford Farms who keeps slipping away from work. He stole a sack of oranges to sell to goblins, and when the deal went wrong he left his mates in trouble.",
     ["M5bc", "M6ba", "M6bb", "M6bd"]),
   P(S[8], None, "main", "Sevrin",
     "A yeoman at Summerford Farms who stole from the farm and left his mates in trouble over a goblin deal. "
     "He was seen meeting in secret with the pirates who stole tools from Tiller's Rest, and Staelwyrn vows his treachery won't go unpunished.",
     ["M6ba", "M6bb", "M8bd", "M8ba", "M8bf"]),
   P(S[9], None, "main", "Sevrin",
     "A former Serpent Reaver who deserted, took a new name and found a home at Summerford Farms. The Reavers offered him his freedom in exchange for his mates, "
     "and he led them into a trap, but couldn't go through with it. Staelwyrn has taken him back, and he means to hand himself over to the Yellowjackets.",
     ["M9be", "M9bo", "M9bb", "M9bf", "M9bg", "M9bl"]),
 ],
 "loc-summerford-farms": [
   P(S[2], None, "main", "Summerford Farms",
     "A farm owned by Staelwyrn, a former pirate captain, and worked largely by ex-pirates who are trying to bring fields ruined by the Calamity back to life.",
     ["M2ba", "M2bb", "M2bc", "M2be"]),
 ],
 "char-yshtola": [
   P(S[4], None, "main", "Y'shtola",
     "A conjurer who has been looking into an aetheric disturbance in Seasong Grotto, which she judged no natural occurrence. "
     "Staelwyrn vouches that she is not one to consort with kidnappers, and she believes the kidnappers plaguing Limsa Lominsa are pirates.",
     ["M4bg", "M4bf", "M4bh", "M4bd", "M4ba"]),
   P(S[9], None, "main", "Y'shtola",
     "A conjurer looking into the kidnappings around Limsa Lominsa. She says the tattooed men behind them are no common pirates but minions of the Sahagin, "
     "and wonders whether the tribes are planning to summon their primals.",
     ["M4bd", "M9bj", "M9bk"]),
   P(S[19], None, "main", "Y'shtola",
     "A Sharlayan conjurer who has long worked with the Yellowjackets, helping their investigation of the kidnappings in Limsa Lominsa. "
     "She named the masked mage who was manipulating the Sahagin and their pirate allies an Ascian, one of the Bringers of Chaos who work through the beast tribes.",
     ["M19bh", "M19bl", "M19bm", "M19bj", "M19bk"]),
 ],
 "org-yellowjackets": [
   P(S[1], None, "main", "The Yellowjackets",
     "The guards who keep the peace in Limsa Lominsa.",
     ["M1bb", "M1bf"], ["Yellowjackets"]),
   P(S[17], None, "main", "The Yellowjackets",
     "The guards who keep the peace in Limsa Lominsa. They took custody of the pirates who attacked the Moraby Drydocks, and are investigating the plot.",
     ["M1bb", "M17bh"], ["Yellowjackets"]),
   P(S[19], None, "main", "The Yellowjackets",
     "The guards who keep the peace in Limsa Lominsa, under Commodore Reyner at the Coral Tower. In unusual cases they turn to Baderon and his connections, "
     "and Y'shtola has long assisted their investigation of the kidnappings. Their soldiers drove the Serpent Reavers out of Swiftperch.",
     ["M1bb", "M19bd", "M19be", "M18bb", "M19bm", "M19bh"], ["Yellowjackets"]),
 ],
 "char-reyner": [
   P(S[19], None, "main", "Reyner",
     "A commodore of the Yellowjackets, Limsa Lominsa's peacekeepers, based at the Coral Tower. He marshaled them when the Sahagin assaulted South Tidegate, "
     "and says the Serpent Reavers are in league with the Sahagin. Y'shtola has worked with him for some time.",
     ["M19bd", "M19be", "M1bb", "M19bf", "M19bg", "M19bl"], ["Commodore Reyner"]),
 ],
 "char-ahtbyrm": [
   P(S[13], None, "main", "Ahtbyrm",
     "Head shipwright at the Moraby Drydocks, building the Victory: the first new vessel there since the Calamity, and the start of rebuilding the Maelstrom's fleet. "
     "He is hiring veteran shipwrights from abroad, and delays in materials infuriate him.",
     ["M13bb", "M13bc", "M13bd", "M13bf", "M13be"]),
   P(S[15], None, "main", "Ahtbyrm",
     "Head shipwright at the Moraby Drydocks, building the Victory to restore the Maelstrom's fleet. "
     "After a wreck off Candlekeep Quay delayed his supplies, he suspects the Sahagin conjured the trouble.",
     ["M13bb", "M13bd", "M14ba", "M15bd"]),
   P(S[17], None, "main", "Ahtbyrm",
     "Head shipwright at the Moraby Drydocks, building the Victory to restore the Maelstrom's fleet. "
     "The pirates who tried to blow up the ship were led by his own father, Ahtzapfyn, who he says has always turned his life upside down.",
     ["M13bb", "M13bd", "M17bc", "M17bb", "M17bg"]),
 ],
 "char-ahtzapfyn": [
   P(S[17], None, "main", "Ahtzapfyn",
     "A pirate leader, and the father of Ahtbyrm, the shipwright building the Victory. Calling the ship a symbol of everything that went wrong with the world, "
     "he led an attack with explosives and Mamool Ja mercenaries to destroy it, and was defeated. His men were handed over to the Yellowjackets.",
     ["M17bc", "M17bd", "M17bb", "M17be", "M17bf", "M17bh"]),
   P(S[19], None, "main", "Ahtzapfyn",
     "A pirate leader, and the father of Ahtbyrm, the shipwright building the Victory. He led the attack that tried to destroy the ship and was defeated. "
     "A coded missive meant for him held orders for the ship's destruction, and named Swiftperch as the site of a feint.",
     ["M17bc", "M17bd", "M17bf", "M18ba", "M19ba"]),
 ],
 "char-ghimthota": [
   P(S[16], None, "main", "Ghimthota",
     "Head of the watch at the Moraby Drydocks, where the Victory is being built. She suspects pirates camped on the Gods' Grip of planning to sabotage the ship, "
     "wonders whether it was ever their target, and has stepped up patrols.",
     ["M16ba", "M16bb", "M16bf", "M16bg"]),
   P(S[18], None, "main", "Ghimthota",
     "Head of the watch at the Moraby Drydocks, where the Victory is being built. After pirates attacked the ship, a coded missive was found among their leader Ahtzapfyn's belongings, "
     "and she sent it to Baderon, to whom the Yellowjackets turn in such cases.",
     ["M16ba", "M17ba", "M18ba", "M18bb"]),
 ],
 "org-serpent-reavers": [
   P(S[8], None, "main", "The Serpent Reavers",
     "Pirates lingering near Tiller's Rest, who stole the farmers' tools to melt down into axes.",
     ["M8ba", "M8bb", "M8bc"]),
   P(S[9], None, "main", "The Serpent Reavers",
     "Pirates who for some years have been seizing law-abiding Lominsans. They look and act like pirates, but serve the Sahagin, and they punish desertion with death.",
     ["M9bi", "M9bh", "M9bj", "M9bo"]),
   P(S[19], None, "main", "The Serpent Reavers",
     "Pirates in league with the Sahagin, who have been seizing Lominsans for years. A masked Ascian was manipulating them. "
     "Their attack on the warship Victory was a distraction for an assault on Swiftperch, which the Yellowjackets drove back.",
     ["M9bi", "M19bg", "M19bh", "M19bb", "M19ba"]),
   P(S[21], None, "main", "The Serpent Reavers",
     "Cutthroats and madmen who look like pirates but have pledged themselves body and soul to the primal Leviathan, the Sahagin's god. "
     "They swelled their numbers by spiriting people away, until their assault on Swiftperch was driven back.",
     ["M21bb", "M21bd", "M9bh", "M21bc", "M19bh"]),
 ],
 "org-sahagin": [
   P(S[9], None, "main", "The Sahagin",
     "A beast tribe whose minions include the tattooed pirates of the Serpent Reavers. Y'shtola wonders whether the tribes are planning to summon their primals.",
     ["M9bj", "M9bh", "M9bk"]),
   P(S[19], None, "main", "The Sahagin",
     "A beast tribe in league with the Serpent Reavers, and manipulated, Y'shtola says, by a masked Ascian. They assaulted South Tidegate while the Reavers struck Swiftperch.",
     ["M19bg", "M19bh", "M19bf"]),
   P(S[21], None, "main", "The Sahagin",
     "A beast tribe, long at odds with Limsa Lominsa, whose god is the primal Leviathan. Their allies the Serpent Reavers have pledged themselves to him, "
     "and a masked Ascian was found manipulating them both.",
     ["M21bd", "M21bb", "M19bg", "M19bh"]),
 ],
 "org-ascians": [
   P(S[19], None, "main", "The Ascians",
     "Masked mages known as the Bringers of Chaos. Y'shtola says they have been manipulating the beast tribes, and one was found working through the Sahagin and the Serpent Reavers.",
     ["M19bj", "M19bk", "M19bh"]),
 ],
 "org-maelstrom": [
   P(S[13], None, "main", "The Maelstrom",
     "A force that lost most of its ships in the Calamity. The Victory, the first new vessel built at the Moraby Drydocks since then, is to begin restoring its fleet.",
     ["M13bd", "M13bc"]),
   P(S[21], None, "main", "The Maelstrom",
     "A force that fought at the Battle of Carteneau under Admiral Merlwyb, who ordered its units to fall back. It lost most of its ships in the Calamity, "
     "and the Victory, its new flagship, is to begin restoring its fleet.",
     ["M21bk", "M13bd", "M19bc"]),
 ],
 "loc-limsa-lominsa": [
   P(S[1], None, "main", "Limsa Lominsa",
     "A city whose peace is kept by the Yellowjackets, and where Baderon, proprietor of the Drowning Wench, finds work for newly arrived adventurers.",
     ["M1bb", "M1bf", "M1ba"]),
   P(S[19], None, "main", "Limsa Lominsa",
     "A city under Admiral Merlwyb, its peace kept by the Yellowjackets. For years the Serpent Reavers seized its people, until the truth behind the kidnappings came to light.",
     ["M19bp", "M1bb", "M9bi", "M19bi"]),
   P(S[22], None, "main", "Limsa Lominsa",
     "A city-state of the Eorzean Alliance, with Gridania and Ul'dah, under Admiral Merlwyb. Its peace is kept by the Yellowjackets.",
     ["M22bc", "M19bp", "M1bb"]),
 ],
 "char-merlwyb": [
   P(S[19], None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa, and a good friend of Baderon. She rewards those who serve the city with the honor of a place at her feasts.",
     ["M19bp", "M19bo", "M19bn"], ["Admiral Merlwyb", "the Admiral"]),
   P(S[21], None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa. At the Battle of Carteneau she commanded the Maelstrom's units and ordered them to fall back. "
     "She honors the Warriors of Light, the heroes lost in that battle whose names no one can speak, and says the Serpent Reavers have pledged themselves to the primal Leviathan.",
     ["M19bp", "M21bk", "M21ba", "M21bi", "M21bj", "M21bb"], ["Admiral Merlwyb", "the Admiral"]),
   P(S[22], None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa, who led the Maelstrom at Carteneau. Five years on she backs memorial services in each city-state of the Eorzean Alliance "
     "on the battle's fifth anniversary, so that the realm can face its past and press on.",
     ["M19bp", "M21bk", "M22bu", "M22bb", "M22bc"], ["Admiral Merlwyb", "the Admiral"]),
 ],
 "char-hydaelyn": [
   P(S[21], None, "main", "Hydaelyn",
     "The Mothercrystal: a higher power who speaks through visions. Her voice has told of the Crystals of Light, in which dwells the power to banish the Darkness.",
     ["M21bf", "M21bg", "M4be"], ["the Mothercrystal"]),
 ],
 "char-leviathan": [
   P(S[21], None, "main", "Leviathan",
     "A primal, the god of the Sahagin, to whom the Serpent Reavers have pledged themselves body and soul.",
     ["M21bb", "M21bd"]),
 ],
 "char-kan-e-senna": [
   P(S[22], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania and leader of its Grand Company. She survived Carteneau, where the elder primal Bahamut emerged from Dalamud, "
     "and laments that Archon Louisoix, who might have explained what followed, never returned. She hopes remembrance services will rekindle the Alliance's unity.",
     ["M22bd", "M22bf", "C44", "M22bi"], ["the Elder Seedseer"]),
 ],
 "char-raubahn": [
   P(S[22], None, "main", "Raubahn",
     "The Flame General of Ul'dah. He warns that the XIVth Imperial Legion is still entrenched within Eorzea's borders, under a commander with long ambitions of conquest, "
     "and calls the realm an alliance in name only.",
     ["M22bj", "M22bk", "M22bl", "M22bm"], ["General Raubahn", "the Flame General"]),
 ],
 "char-gaius": [
   P(S[22], None, "main", "Gaius",
     "Legatus of the XIVth Imperial Legion, which remains entrenched within Eorzea's borders. General Raubahn says he has long harbored ambitions of conquest.",
     ["M22bp", "M22bk", "M22bl"]),
 ],
 "org-garlean-empire": [
   P(S[22], None, "main", "The Garlean Empire",
     "An empire that, once it mastered magitek, seized its neighbors' lands and set its sights on Eorzea. "
     "Its plan to bring down the lesser moon, Dalamud, was met at Carteneau five years ago, and its XIVth Imperial Legion remains entrenched within Eorzea's borders.",
     ["M22bo", "M22be", "M22bu", "M22bk"], ["the Empire"]),
 ],
 "org-eorzean-alliance": [
   P(S[22], None, "main", "The Eorzean Alliance",
     "The alliance of Limsa Lominsa, Gridania and Ul'dah, whose city-states formed the Grand Companies to resist the Garlean Empire. "
     "Weakened since the Calamity, it is, in General Raubahn's words, an alliance in name only, and its leaders hope remembrance services for Carteneau will rekindle its unity.",
     ["M22bc", "M22bs", "M22bg", "M22bm", "M22bi"]),
 ],
 "char-louisoix": [
   P(S[22], None, "main", "Louisoix",
     "A revered Archon who never returned from the Battle of Carteneau. Kan-E-Senna believes he might have explained the changes the land underwent in the Calamity.",
     ["C44", "M22bg"], ["Archon Louisoix"]),
 ],
 "loc-gridania": [
   P(S[22], None, "main", "Gridania",
     "A city-state of the Eorzean Alliance, whose Elder Seedseer is Kan-E-Senna.",
     ["M22bc", "M22bd"]),
 ],
 "loc-uldah": [
   P(S[22], None, "main", "Ul'dah",
     "A sultanate, and a city-state of the Eorzean Alliance, whose Flame General is Raubahn.",
     ["M22bc", "M22bt", "M22bj"]),
 ],
}

# ---- Relationships ------------------------------------------------------------------------------------------------
TYPES = [("child-of", "child of", "parent of", False)]  # as content_3_0_part1 defines it (listed so this era lints alone)

# (id, source, type, target, from, until, scope, claims[, end claims]). The -arr ids repeat a later era's triple for the
# steps before it, ending exactly where that era's record begins (the accepted 2.0 backfill pattern).
RELS = [
 ("rel-staelwyrn-controls-summerford-farms", "char-staelwyrn", "controls", "loc-summerford-farms", S[2], None, "main", ["M2bb", "M2ba"]),
 ("rel-serpent-reavers-aids-sahagin-arr", "org-serpent-reavers", "aids", "org-sahagin", S[9], "cp-msq-179", "main", ["M9bh", "M9bj"]),
 ("rel-ahtbyrm-child-of-ahtzapfyn", "char-ahtbyrm", "child-of", "char-ahtzapfyn", S[17], None, "main", ["M17bc"]),
 ("rel-ahtzapfyn-prisoner-of-yellowjackets", "char-ahtzapfyn", "prisoner-of", "org-yellowjackets", S[17], None, "main", ["M17bf", "M17bh"]),
 ("rel-reyner-leads-yellowjackets", "char-reyner", "leads", "org-yellowjackets", S[19], None, "main", ["M19bd", "M19be"]),
 ("rel-yshtola-aids-yellowjackets", "char-yshtola", "aids", "org-yellowjackets", S[19], None, "main", ["M19bl", "M19bm"]),
 ("rel-ascians-controls-sahagin", "org-ascians", "controls", "org-sahagin", S[19], None, "main", ["M19bh"]),
 ("rel-baderon-allied-with-merlwyb", "char-baderon", "allied-with", "char-merlwyb", S[19], None, "main", ["M19bo"]),
 ("rel-merlwyb-leads-maelstrom-arr", "char-merlwyb", "leads", "org-maelstrom", S[21], "cp-msq-179", "main", ["M21bk"]),
 ("rel-serpent-reavers-serves-leviathan", "org-serpent-reavers", "serves", "char-leviathan", S[21], None, "main", ["M21bb"]),
 ("rel-limsa-lominsa-member-eorzean-alliance", "loc-limsa-lominsa", "member-of", "org-eorzean-alliance", S[22], None, "main", ["M22bc"]),
 ("rel-gridania-member-eorzean-alliance", "loc-gridania", "member-of", "org-eorzean-alliance", S[22], None, "main", ["M22bc"]),
 ("rel-uldah-member-eorzean-alliance", "loc-uldah", "member-of", "org-eorzean-alliance", S[22], None, "main", ["M22bc"]),
 ("rel-gaius-member-empire-arr", "char-gaius", "member-of", "org-garlean-empire", S[22], "cp-msq-141", "main", ["M22bp", "M22bk"]),
]

# ---- Arcs ---------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-r1-trouble-at-summerford", ARC_SUMMERFORD, S[2], S[9]),
 ("arc-r2-rebuilding-la-noscea", ARC_REBUILD, S[10], S[15]),
 ("arc-r3-the-drydocks-plot", ARC_DRYDOCKS, S[16], S[19]),
 ("arc-r4-the-admirals-honor", ARC_HONOR, S[20], S[22]),
]
CASTS = {
 ARC_SUMMERFORD: [("char-baderon", S[2], ["M2ba"]), ("char-staelwyrn", S[2], ["M2bb"]), ("loc-summerford-farms", S[2], ["M2ba"]),
                  ("char-yshtola", S[4], ["M4bg"]), ("char-sevrin", S[5], ["M5bb"]), ("org-serpent-reavers", S[8], ["M8bc"]),
                  ("org-sahagin", S[9], ["M9bj"]), ("org-yellowjackets", S[9], ["M9bl"])],
 ARC_REBUILD: [("char-baderon", S[10], ["M10ba"]), ("org-yellowjackets", S[12], ["M12ba"]), ("char-ahtbyrm", S[13], ["M13bb"]),
               ("org-maelstrom", S[13], ["M13bd"]), ("org-sahagin", S[15], ["M15bd"])],
 ARC_DRYDOCKS: [("char-ghimthota", S[16], ["M16ba"]), ("char-ahtbyrm", S[16], ["M16ba"]), ("char-ahtzapfyn", S[17], ["M17bc"]),
                ("org-yellowjackets", S[17], ["M17bh"]), ("char-baderon", S[18], ["M18bb"]), ("org-serpent-reavers", S[19], ["M19ba"]),
                ("org-sahagin", S[19], ["M19bf"]), ("char-yshtola", S[19], ["M19bh"]), ("org-ascians", S[19], ["M19bh"]),
                ("char-reyner", S[19], ["M19bd"])],
 ARC_HONOR: [("char-merlwyb", S[20], ["M20ba"]), ("char-reyner", S[20], ["M20ba"]), ("char-baderon", S[20], ["M20bb"]),
             ("char-yshtola", S[21], ["M21be"]), ("char-hydaelyn", S[21], ["M21bg"]), ("char-kan-e-senna", S[22], ["M22bd"]),
             ("char-raubahn", S[22], ["M22bj"]), ("char-gaius", S[22], ["M22bp"]), ("org-eorzean-alliance", S[22], ["M22bc"]),
             ("org-garlean-empire", S[22], ["M22bo"])],
}
ARC_NOTES = {
 "arc-r1-trouble-at-summerford": "Limsa MSQ #2 *On to Summerford* to #9 *Just Deserts*, with #1 *Close to Home (Limsa Lominsa)* as the chain's baseline. "
   "Staelwyrn's farm of ex-pirates, the kidnappings and Sevrin's double life, ending when Sevrin confesses his Serpent Reaver past and Y'shtola ties the Reavers to the Sahagin (M9be, M9bj).",
 "arc-r2-rebuilding-la-noscea": "Limsa MSQ #10 *Sky-high* to #15 *Righting the Shipwright*: the post-Calamity restoration jobs (the Skylift, Swiftperch, the Brewer's Beacon) "
   "that lead to the Victory at the Moraby Drydocks, ending when Fyrilsmyd is found and Ahtbyrm first suspects the Sahagin (M15bd).",
 "arc-r3-the-drydocks-plot": "Limsa MSQ #16 *Do Angry Pirates Dream* to #19 *Feint and Strike*: the pirate plot against the Victory, Ahtzapfyn, Baderon's decoding and the Reavers' "
   "assault on Swiftperch, ending with the first named Ascian and Merlwyb's invitation (M19bh, M19bn). Its cast is exactly 10; Merlwyb enters the next arc instead.",
 "arc-r4-the-admirals-honor": "Limsa MSQ #20 *High Society* to #22 *The Lominsan Envoy*: the Admiral's feast, the Crystal of Light and the Carteneau vision, and the envoy run to "
   "Gridania and Ul'dah. The chain ends here: Limsa starters go on to the shared Call of the Sea at cp-msq-23.",
}
DECISIONS = [
 "The vision voice of #4 is never named in this chain's text until #21, where Merlwyb names Hydaelyn and the Mothercrystal; Hydaelyn becomes visible from cp-msq-21b.",
 "The Carteneau voice (Lahabrea@??? on the page) and the castrum commander of #22 stay unnamed, as the game shows them.",
 "Y'shtola, Baderon, Merlwyb, the Maelstrom, Limsa Lominsa and the Alliance leaders are written as chain-neutral facts, because Ul'dah starters see these entries at their own steps.",
 "Backfills (-arr ids) cover the Reavers aiding the Sahagin and Merlwyb leading the Maelstrom until 2.2 (cp-msq-179), and Gaius in the Empire until #141, since their claims are earlier than the accepted ones.",
]
