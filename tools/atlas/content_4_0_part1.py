"""Atlas content for patch 4.0, part 1: MSQ #380 Beyond the Great Wall to #418 Boys with Boats (cp-msq-380 …
cp-msq-418), including the two Gyr Abania chains (#385–#388 and #385b–#392) and the three-way split at #398. Arc tag h.
Data only (docs/atlas/era-modules.md is the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes S01–S04); every locator is an exact substring
of a quest's Journal, Steps or main dialogue. Spoiler and merge rules this module follows:
  - it continues the accepted 3.56 records (char-lyse, char-zenos, char-gosetsu, char-shinryu, char-omega …) under
    their IDs. The ones another era created are listed in ENTITIES too (same category), so the module lints on its
    own; when every era is loaded the merge keeps the earlier definition;
  - it cites only its own claims, so every record stands on this era's pages;
  - first names only: no "Kemp", "Aldynn", "Tarupin", "rem Lupis", "Hext", "yae Galvus" or "van Baelsar" in
    displayed text. The viceroy becomes "Zenos" at #387, where Grynewaht names him and Raubahn calls him Grynewaht's
    viceroy; the Journal confirms "the imperial viceroy himself" at #403;
  - parallel paths: chain A (#385–#388) is ordered before chain B (#385b–#392); chain B's records never depend on
    chain A's events, and chain A's East End victory reaches the shared records (Conrad, the Resistance) only at #397,
    where both chains are done. The #398 trio and the #387b/#387c pair are written independently too;
  - Doma's acting viceroy is one entity, char-yotsuyu, named "Doma's acting viceroy" at #412 and "Yotsuyu" from
    #416, where Gosetsu names her (the Shinryu pattern).
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

S = {k: f"cp-msq-{k}" for k in
     ["380", "381", "382", "383", "384", "385", "386", "387", "388", "385b", "386b", "387b", "387c", "389", "390",
      "391", "392", "397", "398", "398b", "398c", "401", "402", "403", "404", "405", "406", "407", "408", "409",
      "410", "411", "412", "413", "414", "415", "416", "417", "418"]}

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #380 Beyond the Great Wall
 "M380a": ("After Ilberd's assault on the Wall and his summoning of the primal now called Shinryu, the Alliance had little choice but to occupy Castrum Oriens.", "Beyond the Great Wall", "[[Ilberd]]'s assault on [[Baelsar's Wall]] and subsequent summoning of the primal now known as “[[Shinryu]]” left the [[Eorzean Alliance]] with little choice but to occupy [[Castrum Oriens]]"),
 "M380b": ("Raubahn asks the Scions to secure the Ala Mhigan Resistance's support.", "Beyond the Great Wall", "General [[Raubahn Aldynn]] has asked that [[the Scions of the Seventh Dawn]] secure the support of the [[Ala Mhigan Resistance]]"),
 "M380c": ("Lyse leads the Scions to Ala Mhigo, given her ties to the Resistance.", "Beyond the Great Wall", "with [[Lyse]] to lead the way, given her ties to the Resistance."),
 "M380d": ("Yugiri and Gosetsu return to Doma to aid their comrades against Garlemald.", "Beyond the Great Wall", "The pair have resolved to return to the nation of [[Doma]], in the Far East, to aid their comrades in the fight against Garlemald."),
 "M380e": ("Raubahn will not proceed without the Ala Mhigan people's support, and makes the Scions his emissaries to the Resistance.", "Beyond the Great Wall", "As stated in my message, the Alliance will not proceed without the support and cooperation of the Ala Mhigan people. We would have you serve as our emissaries and make contact with the Resistance."),
 "M380f": ("Cid reports that the search for Omega and Shinryu has found nothing.", "Beyond the Great Wall", "apprises you of the latest developments in the search for [[Omega]] and Shinryu: namely, that there have not been any, the fate and whereabouts of both remaining unknown."),
 "M380g": ("Raubahn fears Omega fell in occupied territory and may be in imperial hands.", "Beyond the Great Wall", "Then 'tis like Omega fell to earth in occupied territory...meaning it may already be in imperial hands."),
 "M380h": ("Gyr Abania has languished under imperial rule for twenty years.", "Beyond the Great Wall", "which has languished under imperial rule for twenty long years"),
 "M380i": ("Raubahn expects Garlemald to answer the primal summoned on its doorstep.", "Beyond the Great Wall", "Ilberd summoned a primal right on their doorstep—and Garlemald is not like to let such shows of defiance go unanswered."),
 "M380j": ("Y'shtola goes with the Scions as a healer.", "Beyond the Great Wall", "I too shall accompany you. Such endeavors are seldom hampered by a surfeit of healers."),
 "M380k": ("Urianger stays as caretaker of the Waking Sands, watching for primals and Ascians.", "Beyond the Great Wall", "Gladly shall I continue to serve as caretaker of the Waking Sands, and there keep watch for signs of primal and Ascian activity both."),
 "M380l": ("Seeing Yugiri and Gosetsu off, Lyse says it is time she went home too.", "Beyond the Great Wall", "I know how you feel. It's time I went home too..."),
 "M380m": ("Thancred stays behind as well.", "Beyond the Great Wall", "there are some troubles that may prove too much for a single Scion—on account of which, I mean to stay."),
 "M380n": ("Cid says the Ironworks engaged Omega's stasis systems.", "Beyond the Great Wall", "Even so, it bears repeating that we engaged the stasis systems."),
 "M380o": ("Cid's people have followed the trail of destruction of Omega and Shinryu without result.", "Beyond the Great Wall", "Omega and—Shinryu, I think the shinobi called it? Anyway, we've been studying their trail of destruction, hoping it might lead us somewhere—which it has singularly failed to do."),
 "M380p": ("Gosetsu says the Domans' purpose and the Scions' are one, though their battlefields lie far apart.", "Beyond the Great Wall", "Though our battlefields be a thousand malms apart, our purpose is one!"),
 "M380q": ("Yugiri thanks the Scions for standing with her people from the first, when they came as refugees.", "Beyond the Great Wall", "You and yours stood with us from the first, when we came to this land as refugees in search of sanctuary."),
 "M380r": ("Yugiri's people have a new home and no longer need her; she and Gosetsu return to their master.", "Beyond the Great Wall", "They have built a new home for themselves, and lo longer need me to shepherd them. The time has come for Gosetsu and I to return to our master—to our home."),
 # #381 Lyse Takes the Lead
 "M381a": ("Lyse takes the Scions to the most influential faction of the Resistance.", "Lyse Takes the Lead", "there are plenty of factions in the Resistance, so I'm taking us to see the one with the most influence."),
 "M381b": ("That faction's headquarters is Rhalgr's Reach, an old temple east across the Velodyna River.", "Lyse Takes the Lead", "Their headquarters are located in a place called Rhalgr's Reach—an old temple, to the east of here, across the Velodyna River."),
 "M381c": ("The imperials fortified the old bridge over the Velodyna as Castellum Velodyna.", "Lyse Takes the Lead", "It's part of Castellum Velodyna. That's what the imperials decided to call the old bridge after they fortified it."),
 "M381d": ("A glamour hides the way into Rhalgr's Reach.", "Lyse Takes the Lead", "So you say, but all I see are rocks. … ...Indeed. A glamour."),
 "M381e": ("Lyse's friend, the messenger who came to the Scions, belongs to this faction.", "Lyse Takes the Lead", "my friend Naago, the messenger who came to the Rising Stones, is a member of this faction."),
 "M381f": ("The Resistance in the Reach was waiting for the Scions.", "Lyse Takes the Lead", "They were waiting for us there. Men and women whose souls still cried out for what was lost."),
 # #382 The Promise of a New Beginning
 "M382a": ("Conrad commands the Ala Mhigan Resistance in Rhalgr's Reach.", "The Promise of a New Beginning", "[[Conrad Kemp]], the commander of the [[Ala Mhigan Resistance]] in [[Rhalgr's Reach]]"),
 "M382b": ("Alphinaud thanks Conrad for sheltering Lyse and Papalymo at great risk.", "The Promise of a New Beginning", "pray allow me to thank you for sheltering Yda—forgive me—Lyse and Papalymo at great risk to yourselves."),
 "M382c": ("Lyse says Papalymo laid down his life to give them a chance at a better future.", "The Promise of a New Beginning", "Papalymo laid down his life to save us—to give us a chance to make a better future for ourselves."),
 "M382d": ("Ilberd led Resistance fighters to the Wall and sacrificed them for his ritual.", "The Promise of a New Beginning", "Followed him all the way to the Wall. Good men and women who never came back. … how the bastard had made sacrifices of them for his twisted ritual"),
 "M382e": ("Alphinaud formally offers the Resistance the Alliance's military assistance.", "The Promise of a New Beginning", "On behalf of the Eorzean Alliance, we do hereby extend a formal offer of military assistance to the Ala Mhigan Resistance."),
 "M382f": ("Conrad sees the offer as the Alliance fighting the Empire by proxy with the Resistance's weaker forces.", "The Promise of a New Beginning", "The Alliance, hoping to avoid a direct confrontation with the superior forces of the Empire, wishes to engage them by proxy with our vastly inferior ones?"),
 "M382g": ("Conrad and his officers must confer before they answer.", "The Promise of a New Beginning", "My comrades and I must confer on your proposal."),
 "M382h": ("Conrad notes Lyse is not the first to fight the Empire under a false name.", "The Promise of a New Beginning", "You're not the first person to take up arms against the Empire under a false name."),
 # #383 A Haven for the Bold
 "M383a": ("Conrad encourages the Scions to look around Rhalgr's Reach.", "A Haven for the Bold", "You are free to look around Rhalgr's Reach. In fact, I would encourage you to do so."),
 "M383b": ("Hellsguard and Seekers of the Sun fight in the Resistance.", "A Haven for the Bold", "We've got Hellsguard from all the way over by the Spine in here, and plenty of Seekers of the Sun like Naago."),
 "M383c": ("One faction will have nothing to do with the Resistance, seeing it as no different from the Garleans.", "A Haven for the Bold", "The rest won't have anything to do with us. We're no different than Garleans to them."),
 "M383d": ("Rhalgr, the breaker of worlds, guided the Ala Mhigans' ancestors to these lands.", "A Haven for the Bold", "The breaker of worlds, who guided our ancestors to these lands all those centuries ago."),
 "M383e": ("Yda told Lyse Rhalgr's story on stormy nights.", "A Haven for the Bold", "Yda used to tell me the story on stormy nights."),
 "M383f": ("The Reach has an infirmary, since the Resistance's operations always cost casualties.", "A Haven for the Bold", "No matter how carefully we planned our operations, casualties were inevitable."),
 "M383g": ("The Resistance depends on brave merchants, its sutlers, for provisions.", "A Haven for the Bold", "The Resistance would be in a bad way without brave merchants to keep it provisioned."),
 # #384 A Bargain Struck
 "M384a": ("Conrad accepts the Eorzean Alliance's proposal.", "A Bargain Struck", "I, Conrad Kemp, do hereby accept the Eorzean Alliance's proposal."),
 "M384b": ("Conrad can speak only for the people of Rhalgr's Reach.", "A Bargain Struck", "Simply put, I can only speak for the people of Rhalgr's Reach."),
 "M384c": ("The Resistance is more fragmented than the Scions realize.", "A Bargain Struck", "But the Resistance is far more fragmented than you realize."),
 "M384d": ("Trusted veterans died at the Wall, and young recruits fill their posts.", "A Bargain Struck", "Some of our most trusted veterans died at the Wall, and we've had to fill their posts with the young and inexperienced."),
 "M384e": ("Alphinaud returns to the Scions' headquarters.", "A Bargain Struck", "I, for my part, shall return to the Rising Stones."),
 "M384f": ("Conrad has another task for the Scions, which M'naago and Meffrid will explain.", "A Bargain Struck", "I had something else in mind for you lot. M'naago and Meffrid will tell you more."),
 "M384g": ("Krile offers healers for the Reach's infirmary.", "A Bargain Struck", "From what I saw, they could do with a few more healers."),
 # #385 A Friend of a Friend in Need
 "M385a": ("M'naago, nursed back to health by the Scions, must deliver Conrad's formal reply to Raubahn, and asks for an escort.", "A Friend of a Friend in Need", "After thanking the [[Scions]] for nursing her back to health, [[M'naago]] explains that she has been tasked with delivering [[Commander Kemp]]'s formal reply to [[General Aldynn]]."),
 "M385b": ("Raubahn commands the forces at Castrum Oriens.", "A Friend of a Friend in Need", "General Aldynn commands the forces at Castrum Oriens."),
 "M385c": ("Most soldiers in Gyr Abania are conscripts from other provinces.", "A Friend of a Friend in Need", "M'naago tells you that most soldiers in [[Gyr Abania]] are conscripts from other provinces."),
 "M385d": ("M'naago warns never to pity a man in magitek armor.", "A Friend of a Friend in Need", "And don't you ''dare'' pity a man in armor."),
 "M385e": ("Alisaie volunteers to escort M'naago too.", "A Friend of a Friend in Need", "prompting [[Alisaie]] to volunteer as well."),
 "M385f": ("On the way you ambush an imperial patrol and its magitek armor.", "A Friend of a Friend in Need", "You ambush and destroy the magitek armor M'naago overheard."),
 # #386 Signed, Sealed, to Be Delivered
 "M386a": ("M'naago presents the Resistance's formal response to Raubahn.", "Signed, Sealed, to Be Delivered", "On behalf of Commander Kemp of the Ala Mhigan Resistance, I present to you our formal response."),
 "M386b": ("Raubahn is glad they have reached an accord.", "Signed, Sealed, to Be Delivered", "I am glad we have reached an accord."),
 "M386c": ("Many of the Resistance's finest died in the doomed assault on the Wall, and recruits are scarce since.", "Signed, Sealed, to Be Delivered", "Some of our finest took part in the Griffin's doomed assault, and we've been struggling to find new recruits ever since."),
 "M386d": ("A shipment of prototype magitek armor has reportedly reached Castellum Velodyna from research facilities near the capital.", "Signed, Sealed, to Be Delivered", "Namely, the arrival of a shipment rumored to have come from the research and development facilities near the capital, containing prototype magitek armor."),
 "M386e": ("Pipin proposes harrying patrols to bait the prototypes to East End, where the Resistance will strike from behind.", "Signed, Sealed, to Be Delivered", "we harry their patrols to bait them into bringing their prototype weapons to East End, where our Resistance allies will take them from behind."),
 "M386f": ("Raubahn sees a joint victory as the Resistance's rallying cry.", "Signed, Sealed, to Be Delivered", "they will have their rallying cry."),
 "M386g": ("Pipin calls Raubahn his father.", "Signed, Sealed, to Be Delivered", "The people need proof of this, Father."),
 "M386h": ("M'naago backs the vice marshal's plan.", "Signed, Sealed, to Be Delivered", "Assuming the vice marshal's intelligence is accurate, I agree with his assessment and fully support his plan."),
 # #387 Best Served with Cold Steel
 "M387a": ("The officer field-testing the prototypes is Grynewaht, the brutish Roegadyn you faced at Carteneau.", "Best Served with Cold Steel", "The imperial officer charged with overseeing the field testing of the prototype magitek weapons is none other than [[Grynewaht]], the brutish [[Roegadyn]] whom you faced on the [[Carteneau Flats]]."),
 "M387b": ("Grynewaht means to bring your head to Zenos.", "Best Served with Cold Steel", "I can't wait to see the look on Zenos's face when I bring him your head!"),
 "M387c": ("Grynewaht's weapon is destroyed; he flees, and the Alliance and Resistance celebrate.", "Best Served with Cold Steel", "As the smoldering wreck of his beloved weapon belches smoke into the sky, the imperial officer flees, leaving the combined force of [[Eorzean Alliance|Alliance]] regulars and [[Ala Mhigan Resistance|Resistance]] fighters to celebrate a momentous victory."),
 "M387d": ("Raubahn tells Grynewaht to run and tell his viceroy that the day belongs to Ala Mhigo.", "Best Served with Cold Steel", "Run and tell your viceroy! The day belongs to Ala Mhigo!"),
 "M387e": ("The operation cost no casualties.", "Best Served with Cold Steel", "Not a single casualty, for which I'm grateful beyond words."),
 "M387f": ("Conrad recalls the record of Raubahn, the Bull of Ala Mhigo, before he went west.", "Best Served with Cold Steel", "The “Bull of Ala Mhigo” had an impressive military record before he went west, as I recall."),
 "M387g": ("Grynewaht vows that your next meeting will be the last.", "Best Served with Cold Steel", "You'll pay for this! Mark my words, the next time we meet will be the last!"),
 # #388 Let Fill Your Hearts with Pride
 "M388a": ("The victory counts for little in practice but much as a symbol.", "Let Fill Your Hearts with Pride", "Our victory may not count for much in practical terms, but its symbolic value can't be overstated."),
 "M388b": ("Conrad calls it the beginning of a united Eorzea's campaign to drive out the Garleans.", "Let Fill Your Hearts with Pride", "the beginning of a campaign by a united Eorzea to drive the Garleans from our lands."),
 "M388c": ("Conrad notes that the Alliance took the field and risked lives for the Resistance's cause.", "Let Fill Your Hearts with Pride", "But the Alliance took the field and risked their lives for our cause."),
 "M388d": ("M'naago will go from village to village spreading word of the victory and the new alliance.", "Let Fill Your Hearts with Pride", "Which is why I intend to go from village to village and spread word of our victory and our new alliance."),
 # #385b A Familiar Face Forgotten
 "M385ba": ("Meffrid, first met in Quarrymill, dissolved his Resistance unit in Gridania and returned to join Conrad's people in Rhalgr's Reach.", "A Familiar Face Forgotten", "how he dissolved his unit of [[Ala Mhigan Resistance|Resistance]] fighters in [[Gridania]] and resolved to return to [[Gyr Abania]] and join [[Conrad]]'s people in [[Rhalgr's Reach]]"),
 "M385bb": ("Risen to a position of responsibility, Meffrid must find recruits, and goes to Ala Gannha, Lyse's birthplace.", "A Familiar Face Forgotten", "Having subsequently risen to a position of responsibility, he has been tasked with finding new recruits, and wishes to pay a visit to the village of [[Ala Gannha]]—[[Lyse]]'s birthplace."),
 "M385bc": ("A temple on the way was razed by the mad king Theodoric, not the Garleans.", "A Familiar Face Forgotten", "was razed not by the [[Garlean Empire|Garleans]] but by the mad king, [[King Theodoric|Theodoric]], in the chaos that preceded the imperial invasion."),
 "M385bd": ("Several youths of Ala Gannha died at the Wall, so others may sympathize with the Resistance.", "A Familiar Face Forgotten", "Several youths hailing from Ala Gannha were said to have lost their lives at [[Baelsar's Wall|the Wall]], and it is possible that others in the village may be sympathetic to the Resistance's cause."),
 "M385be": ("Meffrid says they must speak with the village elder first.", "A Familiar Face Forgotten", "We must speak with the elder first. I know for a fact he can be trusted."),
 "M385bf": ("Meffrid warns that an imperial spy may be listening.", "A Familiar Face Forgotten", "You never know when an imperial spy is listening."),
 "M385bg": ("Lyse finds it strange to come home.", "A Familiar Face Forgotten", "It feels strange coming home like this."),
 "M385bh": ("You first met Meffrid in Quarrymill.", "A Familiar Face Forgotten", "whom [[Killing Him Softly|you first met]] in [[Quarrymill]] what feels like a lifetime ago"),
 # #386b The Prodigal Daughter
 "M386ba": ("Raganfrid says the Empire took the Ala Mhigans' lands, traditions and god.", "The Prodigal Daughter", "They took our lands, our traditions, even our god."),
 "M386bb": ("Meffrid calls the Griffin a traitor and madman whose schemes his people had no part in.", "The Prodigal Daughter", "The Griffin was a traitor and a madman, and we had no part in his schemes."),
 "M386bc": ("Raganfrid recognizes Lyse as her father's daughter.", "The Prodigal Daughter", "Wait... ''I know those eyes''. You're one of Curtis's girls!"),
 "M386bd": ("Lyse says she has come to take back her homeland.", "The Prodigal Daughter", "I'm here to take back my homeland."),
 "M386be": ("Lyse almost did not come home, and her sister never will.", "The Prodigal Daughter", "I almost didn't. And my sister never will."),
 "M386bf": ("Raganfrid says the village can give no more.", "The Prodigal Daughter", "But I say to you again: we can give no more."),
 "M386bg": ("The Resistance party may stay in the village.", "The Prodigal Daughter", "At least we've been granted permission to stay."),
 "M386bh": ("Meffrid decides to approach the villagers directly.", "The Prodigal Daughter", "It's risky, and it's hardly subtle, but I say we approach the villagers directly"),
 "M386bi": ("Meffrid introduces you to the village elder.", "The Prodigal Daughter", "Meffrid would like to introduce you to the village elder."),
 "M386bj": ("Meffrid tells the elder the Resistance has an agreement with the Alliance this time.", "The Prodigal Daughter", "We have made an agreement with the Alliance—this time it will be different!"),
 # #387b Hard Country
 "M387ba": ("An imperial patrol took Griseldis's herb-gathering spear as a rebel's.", "Hard Country", "My weapon marked me as a rebel, or so they said."),
 "M387bb": ("Her father died before she limped home.", "Hard Country", "And by the time I limped back to the hut, it was too late for my father."),
 "M387bc": ("The imperials have made it known she is not to be helped.", "Hard Country", "The imperials, they....they've made it known I'm not to be helped."),
 "M387bd": ("Griseldis had gone out with her spear to gather herbs for her dying father.", "Hard Country", "My father, gods rest his soul, was deathly sick at the time, and so I'd gone out into the forest, spear in hand, to gather herbs."),
 # #387c Death by a Thousand Rocks
 "M387ca": ("The sacks hold saltpeter for making firesand.", "Death by a Thousand Rocks", "It's saltpeter for making firesand, in case you're curious what it's all for."),
 "M387cb": ("The quarry brothers sell it to sutlers who trade with the Resistance.", "Death by a Thousand Rocks", "sweeping bits and pieces off to the side, to bundle up and sell to the sutlers what trade with the Resistance."),
 "M387cc": ("The Empire put their father in uniform and shipped him off fifteen years ago.", "Death by a Thousand Rocks", "putting our father in an imperial uniform and shipping him off to some faraway province fifteen years ago."),
 "M387cd": ("It is a living and a way of fighting back.", "Death by a Thousand Rocks", "It's a living, and a way of fighting back besides."),
 # #389 A Life More Ordinary
 "M389a": ("Imperials raid villages to seize supplies and stop stockpiling.", "A Life More Ordinary", "the imperials have been swooping into villages unannounced and seizing supplies in order to prevent the people from stockpiling"),
 "M389b": ("A villager rages at Lyse for her twenty years away.", "A Life More Ordinary", "And where were you these past twenty years!?"),
 "M389c": ("Lyse accepts that she left them behind.", "A Life More Ordinary", "No matter what I say or do, it doesn't change the fact I left them behind."),
 "M389d": ("Qiqirn attacked villagers taking the tributum to the imperials and carried off a man and the money.", "A Life More Ordinary", "we were taking it to the imperials when the Qiqirn attacked! they took my brother, and our money!"),
 "M389e": ("The Qiqirn took him to the Ziggurat.", "A Life More Ordinary", "The Ziggurat? If the ratmen took him there, he's as good as dead..."),
 "M389f": ("Lyse sets off after them at once.", "A Life More Ordinary", "We've got to get after them!"),
 "M389g": ("Meffrid admits he ran from the Wall too.", "A Life More Ordinary", "I ran too, aye, but if I hadn't, I'd've never met [Forename] or the rest of you"),
 # #390 The Color of Angry Qiqirn
 "M390a": ("Wercrata is held at the Ziggurat by Qiqirn bandits.", "The Color of Angry Qiqirn", "So Wercrata's being held somewhere at the Ziggurat to the south, which has been taken over by a host of Qiqirn bandits."),
 "M390b": ("Wercrata has gone hungry for months.", "The Color of Angry Qiqirn", "I've gone to bed hungry for months. I'm skin and bones!"),
 "M390c": ("He was warned last month for paying short.", "The Color of Angry Qiqirn", "we were given a warning last month for being short!"),
 "M390d": ("Wercrata runs off to deliver the tributum.", "The Color of Angry Qiqirn", "Oh gods, the tributum! The imperials will be wondering where I am! I have to go!"),
 "M390e": ("Lyse has a bad feeling about it.", "The Color of Angry Qiqirn", "I've got a bad feeling about this."),
 # #391 The Black Wolf's Pups
 "M391a": ("The Skulls are a unit of Ala Mhigan conscripts.", "The Black Wolf's Pups", "From a distance, you observe Wercrata meeting with the Skulls─a unit of Ala Mhigan conscripts, judging by their accents."),
 "M391b": ("Meffrid stops Lyse from intervening, since a rescue would invite reprisals against Wercrata's family and village.", "The Black Wolf's Pups", "Lyse rises to intervene but is stopped by Meffrid, who tells her that saving the man would only invite reprisals against his family, if not his whole village."),
 "M391c": ("The Skulls' commander orders them to stop.", "The Black Wolf's Pups", "the Skulls' commander eventually orders them to stop, as they are needed elsewhere."),
 "M391d": ("Fordola calls them off, as Lord Zenos expects their report.", "The Black Wolf's Pups", "That's enough! Lord Zenos is expecting our report."),
 "M391e": ("It sickens Meffrid to see his countrymen doing the viceroy's bidding.", "The Black Wolf's Pups", "It sickens Meffrid to the soul to see his countrymen doing the bidding of the viceroy."),
 "M391f": ("The Skull beating Wercrata insists he is a citizen.", "The Black Wolf's Pups", "I've worked and toiled harder than any man! I'm a citizen, godsdammit!"),
 "M391g": ("Meffrid will cut down every last Skull if it comes to it.", "The Black Wolf's Pups", "But they have made their choice, and he is prepared to cut down every last one of them if it comes to it."),
 # #392 Homeward Bound
 "M392a": ("Wercrata is alive and the tributum paid.", "Homeward Bound", "Wercrata's alive, and the tributum's been paid."),
 "M392b": ("Raganfrid says an intervention would have branded Wercrata and his sister insurgents, perhaps the whole village.", "Homeward Bound", "Wercrata and his sister would've been branded insurgents, if not the whole lot of us."),
 "M392c": ("Raganfrid tells Lyse she is strong like her father.", "Homeward Bound", "And you're strong, like your father."),
 "M392d": ("The village has nothing left to give.", "Homeward Bound", "that we've got nothing left to give. We can't help you."),
 "M392e": ("Raganfrid apologizes for judging Lyse.", "Homeward Bound", "I'll admit I was quick to judge you, Lyse, and for that I apologize."),
 "M392f": ("The young villager who scorned Lyse offers to fight.", "Homeward Bound", "If I truly cared for my people, I'd fight for them. So I will...if you'll have me."),
 "M392g": ("Meffrid welcomes the new recruits to Rhalgr's Reach.", "Homeward Bound", "You and yours are more than welcome at Rhalgr's reach."),
 "M392h": ("Lyse had never seen the Skulls in the flesh before.", "Homeward Bound", "I'd heard about the Skulls, but that was the first time I'd seen them in the flesh."),
 "M392i": ("Lyse says they could have stopped the Skulls beating Wercrata.", "Homeward Bound", "We saw what happened when he met with the Skulls. How they beat him half to death. We could've stopped them."),
 "M392j": ("Meffrid warns that the day they fight Garlean soldiers will come.", "Homeward Bound", "''When'', not if. That day will come, Lyse."),
 # #397 Where Men Go as One
 "M397a": ("Alphinaud brings Scions eager to join the endeavor with the Resistance.", "Where Men Go as One", "There were several amongst the Scions' ranks that were quite eager to take part in our joint endeavor with the Resistance"),
 "M397b": ("Arenvald, a half-breed, comes to fight for a free Ala Mhigo.", "Where Men Go as One", "A...a half-breed, as you can doubtless tell. … I'm here to fight for a free Ala Mhigo."),
 "M397c": ("Arenvald is among the Scions who came to fight for the Resistance; you remember him from the Waking Sands.", "Where Men Go as One", "Alphinaud arrives with several other Scions of the Seventh Dawn who have apparently expressed a desire to fight for the Ala Mhigan Resistance, including one Arenvald"),
 "M397d": ("Conrad welcomes Arenvald as a trueborn son of Gyr Abania.", "Where Men Go as One", "You are a trueborn son of Gyr Abania, same as me."),
 "M397e": ("Once the recruits are trained, Conrad will propose an assault on Castellum Velodyna.", "Where Men Go as One", "Once our new recruits have received sufficient training, I will propose to General Aldynn that we draw up plans for an assault on Castellum Velodyna."),
 "M397f": ("In Ala Mhigo, the Empire learns a prototype unit was destroyed.", "Where Men Go as One", "A unit tasked with field-testing prototype magitek weapons was attacked."),
 "M397g": ("Zenos kills the pilus prior, scorning cowards who hide in the castra.", "Where Men Go as One", "''Zenos kills the pilus prior.'' … Cowards who defer critical missions to their subordinates"),
 "M397h": ("Zenos's father has not granted leave to march on the Alliance's lands.", "Where Men Go as One", "Because my honored father, in his infinite wisdom, has not seen fit to grant us leave to march on their lands."),
 "M397i": ("Zenos has invited his neighbors to Gyr Abania for the sport of kings.", "Where Men Go as One", "Accordingly, we have extended an invitation to our neighbors."),
 "M397j": ("An officer sneers that Fordola, an Ala Mhigan, holds her place in name alone.", "Where Men Go as One", "Silence, Ala Mhigan! You do forget yourself! … Only by the grace of Lord van Baelsar were you afforded a place here—and that in name alone."),
 "M397k": ("Zenos remarks that Fordola yearns to hunt her own, and gives her the floor.", "Where Men Go as One", "yearns to hunt her own...The floor is yours, Commander."),
 "M397l": ("Zenos says the XIIth is no place for the weak.", "Where Men Go as One", "However, the XIIth is no place for the weak."),
 "M397m": ("The scene takes place in the Royal Palace of Ala Mhigo.", "Where Men Go as One", "Meanwhile, in the Royal Palace of Ala Mhigo..."),
 "M397n": ("Fordola has a proposal for Zenos.", "Where Men Go as One", "My lord, I have a proposal!"),
 # #398 Future Rust, Future Dust
 "M398a": ("Beves was a historian before the occupation.", "Future Rust, Future Dust", "Before the occupation I was a humble historian."),
 "M398b": ("Hrotmar joined to avenge a friend the imperials butchered in Ala Mhigo.", "Future Rust, Future Dust", "it was to avenge a friend the imperials butchered before my very eyes, back in Ala Mhigo."),
 "M398c": ("Orella's father and brothers were worked to death building a castrum.", "Future Rust, Future Dust", "My father and my brothers were worked to death while building a castrum."),
 "M398d": ("Hughoc would be fighting for the Empire if not for Ala Mhigo.", "Future Rust, Future Dust", "if I wasn't fighting for Ala Mhigo, I'd be fighting for the Empire."),
 "M398e": ("Beves keeps the fighters' accounts as a window into the struggle.", "Future Rust, Future Dust", "Many years from now, when these tempestuous times pass into memory, their accounts will serve as a window into the struggle."),
 "M398f": ("Hrotmar's friend was killed over a piece of fruit.", "Future Rust, Future Dust", "a passing soldier snatched up a piece of fruit."),
 # #398b A Dash of Green
 "M398ba": ("Ahelissa says there is never enough food or supplies in the Reach.", "A Dash of Green", "It's always like this. Never enough food or supplies to go around."),
 "M398bb": ("Villages give what they can, though many have more deserving children.", "A Dash of Green", "Too many villages, too many children more deserving than us..."),
 "M398bc": ("The Resistance never loses sight of the dream.", "A Dash of Green", "And we never lose sight of the dream."),
 "M398bd": ("Ahelissa needs herbs for her stew.", "A Dash of Green", "could you go and ask Tebbe for a variety of herbs?"),
 # #398c Ye Wayward Brothers
 "M398ca": ("An Ananta battlemaid trains the Resistance's recruits, and five have not arrived.", "Ye Wayward Brothers", "I am a trainer, and I was told to expect new recruitsss thisss eve, yet nary a one has come."),
 "M398cb": ("One recruit was late from praying for a sister the imperials had wronged.", "Ye Wayward Brothers", "After what the imperials did to her, death was a mercy..."),
 "M398cc": ("Another says Ala Mhigo's government is moot until the imperials are driven out.", "Ye Wayward Brothers", "until we drive the imperials from our lands, the question is moot."),
 "M398cd": ("All five recruits are accounted for.", "Ye Wayward Brothers", "All recruitsss are presssent and accounted for."),
 # #401 Token of Faith
 "M401a": ("A fighter has lost his lucky ward.", "Token of Faith", "Seven hells, that's the one! That's my lucky ward!"),
 "M401b": ("The mad king Theodoric burned the Temple of the Fist.", "Token of Faith", "And then Theodoric came and burned it all to the ground, the mad bastard."),
 "M401c": ("The Garleans cared even less for Ala Mhigan beliefs.", "Token of Faith", "And after him came the Garleans, who cared even less for our beliefs."),
 "M401d": ("His mother made a pilgrimage to the Temple of the Fist before he was born.", "Token of Faith", "Before I was born, my mother made a pilgrimage to the Temple of the Fist"),
 "M401e": ("He still keeps to the old ways.", "Token of Faith", "But I still keep to the old ways, as do many others."),
 # #402 Crossing the Velodyna
 "M402a": ("For the first time the Resistance and the Alliance will go on the offensive together.", "Crossing the Velodyna", "For the first time, the Resistance and the Alliance shall go on the offensive and attempt to capture an imperial outpost in occupied territory."),
 "M402b": ("Conrad sends M'naago to present his proposal for an assault on Castellum Velodyna.", "Crossing the Velodyna", "I would have you present my proposal for an assault on Castellum Velodyna to General Aldynn personally."),
 "M402c": ("Y'shtola will not take the field this time.", "Crossing the Velodyna", "I shall refrain from taking the field on this occasion."),
 "M402d": ("Krile came for Minfilia, and that has not changed.", "Crossing the Velodyna", "I came here for Minfilia, and that hasn't changed."),
 "M402e": ("Recruitment has exceeded expectations.", "Crossing the Velodyna", "Our recruitment efforts have exceeded expectations."),
 "M402f": ("Raubahn accepts the proposal and has Pipin assess Velodyna's defenses.", "Crossing the Velodyna", "The Alliance hereby accepts Commander Kemp's proposal. … Pipin—I want Velodyna watched. Assess its defenses."),
 "M402g": ("Alisaie says the choice to fight was made for them before they were born, when the Empire marched on Eorzea.", "Crossing the Velodyna", "The choice was made for us ere we were born, Brother, when the Empire marched on Eorzea."),
 "M402h": ("Ilberd's primal complicates matters.", "Crossing the Velodyna", "further complicated by the existence of Ilberd's primal."),
 # #403 In Crimson It Began
 "M403a": ("Pipin takes you, Alphinaud and Alisaie to reconnoiter Castellum Velodyna.", "In Crimson It Began", "Pipin would have you, Alphinaud, and Alisaie accompany him on a reconnaissance mission."),
 "M403b": ("Cannon fire interrupts you: smoke is rising from Rhalgr's Reach.", "In Crimson It Began", "Your mission is interrupted by the sound of cannon fire from the east. You turn to see a column of smoke on the horizon...rising from Rhalgr's Reach"),
 "M403c": ("No one answers by linkpearl, confirming a coordinated attack.", "In Crimson It Began", "all but confirming your suspicions that a coordinated attack is underway."),
 "M403d": ("Y'shtola lies near death, struck down by Zenos, the imperial viceroy.", "In Crimson It Began", "Y'shtola is on the verge of death, her lifeblood pooling beneath her prostrate form. You turn to confront the man who dealt the blow: Zenos yae Galvus, the imperial viceroy himself."),
 "M403e": ("Lyse is unharmed and Conrad merely unconscious.", "In Crimson It Began", "Lyse is unharmed, and Conrad merely unconscious"),
 "M403f": ("Meffrid calls Fordola a traitor and kinslayer, and she cuts him down.", "In Crimson It Began", "Traitor! Kinslayer! … You're no kin of mine! … ''Fordola cuts down Meffrid.''"),
 "M403g": ("Zenos bests you, then turns his back and walks away.", "In Crimson It Began", "the viceroy sends you flying─the only testament to your resilience the broken blade he flings to the earth as he turns his back on you and walks away."),
 "M403h": ("Raubahn and the Immortal Flames arrive and let the imperials withdraw to tend the wounded.", "In Crimson It Began", "Raubahn and his Immortal Flames soon arrive, but he has seen enough death for one day, and orders his men to let the imperials withdraw and instead attend to the wounded."),
 "M403i": ("Zenos is the crown prince.", "In Crimson It Began", "having come face-to-face with the crown prince himself"),
 "M403j": ("Zenos bids Fordola, his pilus, stand aside, saying you have promise.", "In Crimson It Began", "Stand aside, Pilus. This one has promise."),
 "M403k": ("Krile and Arenvald are among those outside the Reach.", "In Crimson It Began", "you encounter a number of fleeing Resistance fighters, as well as Krile and Arenvald."),
 "M403l": ("Conrad and others made a last desperate stand.", "In Crimson It Began", "of a last desperate stand by Conrad and the others"),
 "M403m": ("Pipin and Alisaie fell to Zenos before you did.", "In Crimson It Began", "Though you endure Zenos's onslaught far longer than Pipin and Alisaie, even you are no match for him."),
 "M403n": ("Raubahn reminds you that your actions saved lives.", "In Crimson It Began", "Raubahn reminds you that your actions saved lives"),
 # #404 The Fires Fade
 "M404a": ("Raubahn sends you to see to the wounded.", "The Fires Fade", "See to the wounded, [Forename]. If they live, help them. If not, move on."),
 "M404b": ("Meffrid lies dead.", "The Fires Fade", "Meffrid lies motionless, having breathed his last."),
 "M404c": ("Conrad calls Meffrid a worrier who always put others first.", "The Fires Fade", "Meffrid was a worrier. Always thinking about others before himself."),
 "M404d": ("Meffrid sent his men in Quarrymill away, thinking they fought for him rather than the cause.", "The Fires Fade", "Did you know that he sent his men in Quarrymill away because he thought they were fighting for him, and not the cause?"),
 "M404e": ("Alphinaud says Meffrid's sacrifice let many live.", "The Fires Fade", "because of his sacrifice, many now live who otherwise would not"),
 "M404f": ("Conrad had high hopes for Meffrid.", "The Fires Fade", "I had...high hopes for him, is all..."),
 "M404g": ("Meffrid died with a charm in his fist, which goes to Conrad.", "The Fires Fade", "That charm must've been important. You'd best take it to Conrad."),
 # #405 Bereft of Hearth and Home
 "M405a": ("The Reach is no longer safe: the imperials could return.", "Bereft of Hearth and Home", "The imperials may have withdrawn, but they could return at any time to finish what they began."),
 "M405b": ("The wounded go to Castrum Oriens by chocobo carriage.", "Bereft of Hearth and Home", "Those who are not fit to make the journey to Castrum Oriens will need to be taken by chocobo carriage."),
 "M405c": ("Y'shtola is strapped into a carriage.", "Bereft of Hearth and Home", "Y'shtola and the others are safely strapped in."),
 "M405d": ("Conrad stays to finish his work and will meet them at the Wall.", "Bereft of Hearth and Home", "I'll see you at the Wall when it's finished."),
 "M405e": ("You gather medical supplies from the infirmary.", "Bereft of Hearth and Home", "Search the infirmary for medical supplies."),
 # #406 Divide and Conquer
 "M406a": ("The Resistance's forces were decimated; there will be no assault on Castellum Velodyna.", "Divide and Conquer", "our forces were decimated. In this state, we'll not be mounting an assault on Castellum Velodyna or anywhere else."),
 "M406b": ("Zenos and his men returned to Specula Imperatoris.", "Divide and Conquer", "As far as we can tell, Zenos and his men returned straightways to Specula Imperatoris after quitting this place."),
 "M406c": ("Raubahn says Zenos is no fool to walk away.", "Divide and Conquer", "Only a fool would turn his back and walk away...but Zenos is no fool."),
 "M406d": ("Lyse saw the Skulls' commander, an Ala Mhigan, cut down Meffrid.", "Divide and Conquer", "When that Skulls commander cut down Meffrid. … It wasn't a Garlean who did it—it was an ''Ala Mhigan''."),
 "M406e": ("The Skulls are Crania Lupi, the Black Wolf's legacy: children born to Ala Mhigan dignitaries during the occupation.", "Divide and Conquer", "Crania Lupi. The Black Wolf's legacy, and our shame. A unit made up of children born to Ala Mhigan dignitaries who came during the age of occupation."),
 "M406f": ("The Skulls are the youths who fight for Zenos.", "Divide and Conquer", "You mean the Skulls... The youths who fight for Zenos."),
 "M406g": ("Before taking charge in Ala Mhigo, Zenos crushed Doma's rebellion.", "Divide and Conquer", "Zenos led the imperial army to Doma, where he crushed the rebellion utterly."),
 "M406h": ("Doma is still in Zenos's charge, and he is Varis's heir.", "Divide and Conquer", "As a matter of fact, Doma remains in his charge to this day. Suffice it to say, Varis's heir is a peerless warrior and an accomplished general."),
 "M406i": ("Raubahn urges the Resistance to hold fast and rebuild, to defeat Zenos together.", "Divide and Conquer", "Have faith in your people, Master Kemp. Them and the Scions. Hold fast, rebuild, and when all is in place, we shall defeat Zenos together."),
 "M406j": ("Conrad agrees to fight on.", "Divide and Conquer", "Very well. For all you have done for us, we will fight on."),
 "M406k": ("Lyse will go to Doma too, to help friends there.", "Divide and Conquer", "If you're going to Doma, I'm coming too. I want to help our friends there...and make sure nothing like this ever happens again."),
 "M406l": ("Conrad grants the plan for Doma promise but fears the Resistance lacks the strength meanwhile.", "Divide and Conquer", "Look, I'll not deny the plan has promise—and I feel for our brothers and sisters in Doma, truly I do—but I fear we lack the strength to see it through."),
 "M406m": ("Zenos is next in line to the Garlean throne.", "Divide and Conquer", "Gods help us if he's next in line to the Garlean throne."),
 # #407 Lies, Damn Lies, and Pirates
 "M407a": ("Alisaie plans a journey to the Far East.", "Lies, Damn Lies, and Pirates", "Alisaie is contemplating the logistics of a journey to the Far East."),
 "M407b": ("Krile will look after Y'shtola and support Arenvald and the others.", "Lies, Damn Lies, and Pirates", "Would you be willing to look after Y'shtola and provide support to Arenvald and the others?"),
 "M407c": ("No airship can make the journey, and an Alliance ship would be noticed.", "Lies, Damn Lies, and Pirates", "it is simply not feasible for an airship to travel such a distance without impossibly large fuel reserves"),
 "M407d": ("Tataru presents Captain Carvallain.", "Lies, Damn Lies, and Pirates", "May I present to you Captain Carvallain of the Kraken's Arms!"),
 "M407e": ("Carvallain can carry them only as far as Kugane, in Hingashi.", "Lies, Damn Lies, and Pirates", "I cannot deliver you to Doma itself. I can take you only as far as Kugane, in Hingashi."),
 "M407f": ("Carvallain agrees to take them this once.", "Lies, Damn Lies, and Pirates", "But so long as you are prepared to abide the capricious whims of fate, I am willing to oblige you this once."),
 # #408 Tales from the Far East
 "M408a": ("Alphinaud sends you and Lyse to the Doman allies in Revenant's Toll.", "Tales from the Far East", "I would like the two of you to return to Revenant's Toll and speak with our Doman allies."),
 "M408b": ("The Domans suffered Garlean tyranny for twenty-five years.", "Tales from the Far East", "For twenty-five years we suffered under their tyranny."),
 "M408c": ("They rose up when the Emperor died and Garlemald fell into chaos.", "Tales from the Far East", "And then we spied an opportunity—the Emperor, dead! Garlemald in chaos!"),
 "M408d": ("Zenos and the XIIth Legion crushed the uprising in an instant.", "Tales from the Far East", "But when Zenos arrived with the XIIth Legion, it was over in an instant..."),
 "M408e": ("Doma Castle is home to the imperial viceroy's witch and her forces.", "Tales from the Far East", "Now it is home to the imperial viceroy's witch, and her host of men and magitek."),
 "M408g": ("Doma Castle, once the shining symbol of Doma's heritage, has become a den for Garleans.", "Tales from the Far East", "To think that what was once the shining symbol of our heritage—and the seat of dear Lord Kaien—has become a den for Garlean dogs..."),
 "M408h": ("Hozan's ancestors held positions in Doma Castle.", "Tales from the Far East", "My ancestors held positions within Doma Castle, even."),
 "M408f": ("Hozan rejoices that you go to join Yugiri and Gosetsu in the fight.", "Tales from the Far East", "That you go to join Yugiri and Gosetsu in the fight fills me with such joy!"),
 # #409 Not without Incident
 "M409a": ("Urianger gives Alisaie a rapier and a cryptic warning, and their rift may be healing.", "Not without Incident", "Urianger arrives bearing a cryptic warning and a practical gift: a rapier made for your young companion. Moved by the gesture, her steely demeanor softens, and you sense that the rift between the two may have finally begun to heal."),
 "M409b": ("Urianger's warning is a Far Eastern verse.", "Not without Incident", "Look ye where the sun doth rise, see crimson embers, dark'ning skies..."),
 "M409c": ("A mysterious force drags the ship off course.", "Not without Incident", "speaking of strange things in the water, and a mysterious force dragging the ''Misery'' off course."),
 "M409d": ("The being the sailors call Lorelei falls, and the voyage resumes.", "Not without Incident", "With the demise of the mysterious being the sailors call Lorelei, the clouds part"),
 "M409e": ("Kugane is Hingashi's only port open to outsiders, across the sea from Doma.", "Not without Incident", "The only port open to outsiders in Hingashi, across the Ruby Sea from Othard. From Doma."),
 "M409f": ("In Kugane's harbor Lyse stands apart, whispering a prayer or an oath.", "Not without Incident", "From the corner of your eye you spy Lyse, standing apart from the others, her lips moving silently. A prayer or an oath, perhaps."),
 "M409g": ("Carvallain and his crew sail the Scions from Limsa Lominsa.", "Not without Incident", "you depart for Limsa Lominsa, where Captain Carvallain and the crew of the ''Misery'' are preparing for your journey to the other side of the world."),
 "M409h": ("Kugane is the nation's only port open to foreign trade.", "Not without Incident", "Regrettably, the only port in this nation open to foreign trade."),
 # #410 The Man from Ul'dah
 "M410a": ("Carvallain pledged to take the Scions only as far as Kugane.", "The Man from Ul'dah", "I realize you pledged only to take us as far as Kugane, and I have no desire to change the terms of our agreement."),
 "M410b": ("Yugiri and Gosetsu must have found a way on, unless they are still in the city.", "The Man from Ul'dah", "They must have found a way to Othard—assuming they are not still in the city."),
 "M410c": ("Hancock of the East Aldenard Trading Company welcomes them on behalf of Chairman Lolorito.", "The Man from Ul'dah", "Hancock, of the East Aldenard Trading Company, at your service. On behalf of Chairman Lolorito, I bid you welcome to Kugane"),
 "M410d": ("Alphinaud distrusts those who serve a master with whom the Scions have a difficult relationship.", "The Man from Ul'dah", "especially those who serve a master with whom we have such a difficult relationship"),
 "M410e": ("Many nations, the Garlean Empire included, keep embassies in Kugane.", "The Man from Ul'dah", "Many notable nations and empires have embassies here, you know—including of course, the Garlean Empire"),
 "M410f": ("Beneath Kugane's trade, world powers wage a war for supremacy.", "The Man from Ul'dah", "Beneath this veneer of bustling trade, a war for supremacy is being waged between world powers."),
 "M410g": ("Alisaie accepts Hancock's invitation for now.", "The Man from Ul'dah", "I say we accept his invitation—for now."),
 # #411 Where the Streets Are Paved with Koban
 "M411a": ("The Ijin-gai is where foreigners may live.", "Where the Streets Are Paved with Koban", "This road leads to the Ijin-gai: the district in which"),
 "M411b": ("The Sekiseigumi punish breaches of the peace severely.", "Where the Streets Are Paved with Koban", "The Sekiseigumi punish breaches of peace quite severely."),
 "M411c": ("A Sekiseigumi samurai cut down a foreign merchant with a single stroke.", "Where the Streets Are Paved with Koban", "The samurai cut him in half with a single stroke."),
 "M411d": ("The Garlean Consulate stands in Kugane.", "Where the Streets Are Paved with Koban", "This, as you may have surmised, is the consulate of you-know-who."),
 "M411e": ("Kugane's markets take every currency, Eorzean gil included.", "Where the Streets Are Paved with Koban", "we accept all manner of currencies. Rest assured, your Eorzean gil are welcome here."),
 # #412 By the Grace of Lord Lolorito
 "M412a": ("Hancock calls the company's aid Lolorito's contrition for the bloody banquet.", "By the Grace of Lord Lolorito", "the chairman bids you consider this as an expression of his heartfelt contrition for the bloody banquet and the unpleasantness which followed."),
 "M412b": ("The company's interests coincide with aiding the Doman Liberation Front.", "By the Grace of Lord Lolorito", "By sheer coincidence, your purpose here happens to coincide with our own interests. That is, assuming you are come to aid the Doman Liberation Front?"),
 "M412c": ("Yugiri and Gosetsu came on a company vessel but could not cross the Ruby Sea.", "By the Grace of Lord Lolorito", "They came here aboard a company vessel, you see. However, they encountered difficulties securing passage across the Ruby Sea."),
 "M412d": ("The Ruby Sea belongs to neither Hingashi nor Doma but to the Confederacy.", "By the Grace of Lord Lolorito", "the Ruby Sea does not fall within the dominion of either Hingashi or Doma, being controlled since antiquity by a third party: namely, the Confederacy."),
 "M412e": ("The Confederacy charges every ship in its waters a toll, the Ruby Tithe, for its protection.", "By the Grace of Lord Lolorito", "demanding that any vessel entering its waters pay a toll referred to as the"),
 "M412f": ("Doma's recently appointed acting viceroy has condemned the Confederacy.", "By the Grace of Lord Lolorito", "The recently appointed acting imperial viceroy of Doma had other ideas, however. She has formally condemned the Confederacy"),
 "M412g": ("Hingashi cut ties with the Confederacy and forbade the Ruby Tithe.", "By the Grace of Lord Lolorito", "Bowing to this pressure, Hingashi severed ties with these toll-takers and forbade the payment of the Ruby Tithe"),
 "M412h": ("Alphinaud will follow Yugiri and Gosetsu's footsteps to Doma.", "By the Grace of Lord Lolorito", "I say we follow in Yugiri and Gosetsu's footsteps and attempt to secure passage to Doma for ourselves."),
 "M412i": ("Alphinaud is reluctant to be in Lolorito's debt but takes the means available.", "By the Grace of Lord Lolorito", "Though I am reluctant to take any action whatsoever that could be construed as placing ourselves in Lord Lolorito's debt"),
 "M412j": ("Garlemald conquered Doma some twenty-five years ago.", "By the Grace of Lord Lolorito", "Garlemald conquered Doma some twenty-five years past"),
 "M412k": ("The Scions come to assist Yugiri and Gosetsu in their fight.", "By the Grace of Lord Lolorito", "we are come in search of our Far Eastern allies, Yugiri and Gosetsu, whom we hope to assist in their fight."),
 # #413 A Good Samurai Is Hard to Find
 "M413a": ("Alphinaud sketched Yugiri and Gosetsu for the search.", "A Good Samurai Is Hard to Find", "I took the liberty of preparing some few sketches of Yugiri and Gosetsu during our voyage."),
 "M413b": ("The hostelry's keeper says the pair sought passage across the Ruby Sea.", "A Good Samurai Is Hard to Find", "The two individuals of whom you speak did indeed come here. they sought passage across the Ruby Sea."),
 "M413c": ("She will also answer those who ask after the Scions.", "A Good Samurai Is Hard to Find", "But if I do, I must ''also'' oblige the ones who ask after ''you''."),
 "M413d": ("A captain refused a Roegadyn who wanted to charter a ship across the Ruby Sea.", "A Good Samurai Is Hard to Find", "He wanted to charter a ship to take him across the Ruby Sea, the mad devil."),
 "M413e": ("A spice trader could not help the Roegadyn bound for Doma.", "A Good Samurai Is Hard to Find", "He was for Doma, but I could not help him."),
 "M413f": ("No captain knows the woman.", "A Good Samurai Is Hard to Find", "The woman is unknown to me, but the man is not."),
 # #414 It's Probably a Trap
 "M414a": ("Gyodo claims to have met the Domans and found them a ship.", "It's Probably a Trap", "claims not only to have met with your Doman friends, but to have helped them secure passage on a ship to Othard."),
 "M414b": ("The Scions conclude it is a trap and spring it anyway.", "It's Probably a Trap", "Your comrades quickly conclude that the Namazu is attempting to lure you into a trap...and that for lack of a better plan, you may as well spring it."),
 "M414c": ("Gyodo betrays them, and Lyse boots him into the air.", "It's Probably a Trap", "Gyodo's sudden but inevitable betrayal comes as no surprise, but the enthusiasm with which Lyse boots him into the air does."),
 "M414d": ("The Sekiseigumi send patrols after you, perhaps taking you for foreign agents.", "It's Probably a Trap", "Perhaps suspecting you of being the agents of foreign powers, the Sekiseigumi dispatch several patrols to the Ijin District"),
 "M414e": ("Your savior is Soroban, a Kojin of the Blue and a merchant who wants an agreement with Hancock.", "It's Probably a Trap", "at last learn the identity of your savior: Soroban, a Kojin of the Blue. … A merchant by trade, he seeks to broker an agreement with Hancock, who is more than happy to do so."),
 "M414f": ("Soroban offers passage across the Ruby Sea.", "It's Probably a Trap", "Ah, yes─you sought passage across the Ruby Sea, did you not?"),
 "M414g": ("Kojin of the Red serve the Empire as mercenaries; the Blue walk a different path.", "It's Probably a Trap", "Kojin of the Red may serve the Empire as mercenaries, but Kojin of the Blue walk a different path."),
 "M414h": ("The viceroy was once a spy herself.", "It's Probably a Trap", "The viceroy was once a spy herself, as I recall."),
 "M414i": ("Lyse carries the unconscious Gyodo back.", "It's Probably a Trap", "the unconscious Gyodo that Lyse carried on her shoulder to the Ruby Bazaar twitches"),
 "M414j": ("Gyodo is a Namazu who frequents the Shiokaze Hostelry.", "It's Probably a Trap", "Gyodo, a Namazu said to frequent the Shiokaze Hostelry"),
 "M414k": ("Gyodo summons the ambushers on the bridge.", "It's Probably a Trap", "To me, to me! These ones are for Doma!"),
 # #415 Making the Catfish Sing
 "M415a": ("Gyodo met only the samurai and introduced him to the Garleans.", "Making the Catfish Sing", "Only the samurai did I meet. Yes, yes, only him! He asked after a ship, so I provided an introduction to...to the Garleans..."),
 "M415b": ("The Garleans offer a bounty for Domans found in Kugane.", "Making the Catfish Sing", "So when the Garleans offered a bounty for any Domans found in Kugane─"),
 "M415c": ("Blades were drawn and the Sekiseigumi took the samurai away.", "Making the Catfish Sing", "Blades were drawn, men were cut down, and the Sekiseigumi came. They took the samurai away."),
 "M415d": ("Hancock means to bribe the right official.", "Making the Catfish Sing", "If he is in the custody of the Sekiseigumi, I need only see to it that the requisite funds find their way into the right official's hands"),
 "M415e": ("The Sekiseigumi keep their word to free the samurai who defeated them, asking him to avoid altercations.", "Making the Catfish Sing", "Our word, once given, may not be broken─but we pray you make every effort to avoid future altercations."),
 "M415f": ("Hancock's help was not needed.", "Making the Catfish Sing", "I gather my assistance was not required?"),
 "M415g": ("Alphinaud keeps watch over Gyodo.", "Making the Catfish Sing", "I will keep an eye on him for the time being."),
 # #416 Once More, to the Ruby Sea
 "M416a": ("Gosetsu won his freedom in a contest of strength just before the Scions arrived.", "Once More, to the Ruby Sea", "he managed to win his freedom through a contest of strength mere moments before you and the others arrived to rescue him."),
 "M416b": ("Gosetsu and Yugiri parted to improve their chances of finding Lord Hien.", "Once More, to the Ruby Sea", "For a time, aye, but we parted ways some while ago, the better to improve our chances of finding Lord Hien."),
 "M416c": ("Lord Hien is heir to Doma's throne and their master.", "Once More, to the Ruby Sea", "Lord Hien is the heir to Doma's throne, and our master."),
 "M416d": ("Hien sent Yugiri to sea with as many people as possible, and stayed to fight.", "Once More, to the Ruby Sea", "Once Lord Hien understood this, he bade Yugiri take to the sea with as many of our people as possible. He, however, would stand and fight, that they might have more time to escape..."),
 "M416e": ("Gosetsu lost Hien in battle, and knows only that he is beyond the Empire's reach.", "Once More, to the Ruby Sea", "And then, one day, in a fierce battle, we were separated. I knew not what became of him─only that he was beyond the Empire's reach"),
 "M416f": ("Doma's new viceroy, Yotsuyu, torments its people and pursues Hien.", "Once More, to the Ruby Sea", "for the new viceroy, Yotsuyu, is a black-hearted villainess who delights in the torment of our people. There is naught she would not do to further her pursuit of Lord Hien."),
 "M416g": ("The Scions come to help the Doman Liberation Front resume its fight.", "Once More, to the Ruby Sea", "we are come to aid the Doman Liberation Front in resuming their efforts to overthrow their imperial oppressors."),
 "M416h": ("Gosetsu joins them and will lead them to the Domans' headquarters and Yugiri.", "Once More, to the Ruby Sea", "Then allow me to join you! … Once there, I can lead you to our headquarters in Yanxia, where we shall all be reunited with Yugiri!"),
 "M416i": ("Alisaie sets Alphinaud to gather intelligence in Kugane with Tataru and Hancock.", "Once More, to the Ruby Sea", "Alphinaud's talents would seem better applied here in Kugane, working closely with Tataru and Hancock to feed us intelligence."),
 "M416j": ("Tataru and Alphinaud remain while you, Lyse, Alisaie and Gosetsu meet Soroban.", "Once More, to the Ruby Sea", "it is decided that [[Tataru]] and Alphinaud will remain, while you, [[Lyse]], [[Alisaie]], and Gosetsu go to meet [[Soroban]] at [[Pier 2|the docks]]."),
 "M416k": ("Hien survived, and the Empire seeks to make an example of him.", "Once More, to the Ruby Sea", "only that he somehow survived, and that the [[Garlean Empire|Empire]] still seeks to make an example of him."),
 "M416l": ("The crown prince and the XIIth left the Domans no chance.", "Once More, to the Ruby Sea", "The crown prince was a merciless foe. Against him and the might of the XIIth, we had no chance."),
 "M416m": ("Hien was a passionate voice for Doman liberation.", "Once More, to the Ruby Sea", "His was a passionate voice for the cause of Doman liberation"),
 "M416n": ("The Ruby Sea is named for the crimson it turns at sunrise.", "Once More, to the Ruby Sea", "Before you lies the vast expanse of the Ruby Sea, so named for the shade of crimson it turns with the morning sun."),
 # #417 Open Water
 "M417a": ("Setting out unprepared invites the Confederacy to claim your vessel and your life.", "Open Water", "To set forth without making the necessary preparations is to invite the Confederacy to claim your vessel─and your life should you resist."),
 "M417b": ("Paying the Ruby Tithe earns the pirate lords' blessing.", "Open Water", "But this fate can be avoided by paying the Ruby Tithe, thereby earning you the blessing of the pirate lords."),
 "M417c": ("Soroban leads them to an isle to the west.", "Open Water", "So─let us go and greet them. Our destination is the isle to the west."),
 "M417d": ("Tansui is a mate serving the Confederacy's captain.", "Open Water", "I am Tansui, a humble mate who serves at the pleasure of the Confederacy's captain."),
 "M417e": ("Tansui expects business from Soroban's company.", "Open Water", "As you are in the company of the shellback, I presume we have business to discuss..."),
 "M417g": ("Tansui greets you by name.", "Open Water", "Most honorable and esteemed [Forename] [Surname]."),
 "M417f": ("Soroban says they must speak with Tansui.", "Open Water", "The one with whom we must speak is a man named Tansui."),
 # #418 Boys with Boats
 "M418a": ("Soroban offers to pay the Scions' passage.", "Boys with Boats", "I would pay for their passage to Othard."),
 "M418b": ("Tansui says the sum is too small for a safe crossing.", "Boys with Boats", "I cannot say with confidence that you would reach your destination safely─unless you tripled it."),
 "M418c": ("Tansui counts the Scions' tithe paid for what he expects they will do.", "Boys with Boats", "I shall consider their tithe paid─not for what they have done, but for what I expect they will do."),
 "M418d": ("An imperial officer scorns the Confederacy's extortion.", "Boys with Boats", "Your feeble attempts at extortion will not work on us."),
 "M418e": ("Defying the Empire would see the Confederacy branded its enemy.", "Boys with Boats", "she'll accuse us of attempting to foment rebellion and brand us enemies of the Empire"),
 "M418f": ("Many in the Confederacy are of Doman descent, and the acting viceroy is no friend of Domans.", "Boys with Boats", "many of my comrades in the Confederacy are of Doman descent─and the acting viceroy...well, she's none too fond of Domans, to say the least."),
 "M418g": ("The acting viceroy continues her purge of Doma's radical elements.", "Boys with Boats", "continues her purge of Doma's “radical elements.”"),
 "M418h": ("Tansui says the Confederacy is outmatched by the imperial army.", "Boys with Boats", "Compared to them, we're boys with boats."),
 "M418i": ("Gosetsu says the viceroy must be stopped.", "Boys with Boats", "She must be stopped. Come, let us find Soroban and put to sea at once!"),
 "M418j": ("Soroban did not want his Red brothers to see him with the Scions.", "Boys with Boats", "As you may have guessed, I was reluctant to be seen in your company by my Red brothers."),
 "M418k": ("With Tansui's business done, they can cross the Ruby Sea without fear.", "Boys with Boats", "Now that our business with Tansui is concluded, we can traverse the Ruby Sea without fear!"),
}

# ---- Entities ----------------------------------------------------------------------------------------------------------
# New in this era, then (same categories) the existing ones this module continues, so it lints on its own; with every
# era loaded the earlier definition stands. Arc entries are listed with the arcs below.
ENTITIES = {
 "char-conrad": "character", "char-mnaago": "character", "char-meffrid": "character", "char-raganfrid": "character",
 "char-grynewaht": "character", "char-fordola": "character", "char-arenvald": "character", "char-carvallain": "character",
 "char-hancock": "character", "char-soroban": "character", "char-gyodo": "character", "char-tansui": "character",
 "char-hien": "character", "char-yotsuyu": "character",
 "org-crania-lupi": "organization", "org-east-aldenard-trading-company": "organization", "org-sekiseigumi": "organization",
 "org-confederacy": "organization", "org-doman-liberation-front": "organization",
 "loc-castrum-oriens": "location", "loc-rhalgrs-reach": "location", "loc-ala-gannha": "location", "loc-kugane": "location",
 "loc-ruby-sea": "location", "loc-castellum-velodyna": "location", "loc-specula-imperatoris": "location",
 "loc-doma-castle": "location",
 # continued from earlier eras
 "char-lyse": "character", "char-zenos": "character", "char-gosetsu": "character", "char-yugiri": "character",
 "char-krile": "character", "char-pipin": "character", "char-ilberd": "character", "char-shinryu": "character",
 "char-omega": "character", "char-lolorito": "character", "char-varis": "character", "char-raubahn": "character",
 "org-ala-mhigan-resistance": "organization", "loc-doma": "location", "org-doman-refugees": "organization",
 "evt-envoys-to-the-resistance": "event", "evt-the-east-end-ambush": "event", "evt-return-to-ala-gannha": "event",
 "evt-blood-in-rhalgrs-reach": "event", "evt-passage-to-the-far-east": "event", "evt-across-the-ruby-sea": "event",
}

# ---- Presentations -----------------------------------------------------------------------------------------------------
PRES = {
 # -- Gyr Abania: places and the Resistance
 "loc-castrum-oriens": [
   P(S["380"], None, "main", "Castrum Oriens",
     "An imperial castrum by the Wall, at the edge of Gyr Abania, which the Eorzean Alliance occupied after the attack on the Wall and the primal's summoning. "
     "From its command center Raubahn holds the Alliance's line, and will not advance into Gyr Abania without the Ala Mhigan Resistance.",
     ["M380a", "M380e"]),
   P(S["405"], None, "main", "Castrum Oriens",
     "An imperial castrum by the Wall, held by the Eorzean Alliance under Raubahn. After the imperial attack on Rhalgr's Reach, Pipin is bringing the Resistance's wounded here by chocobo carriage.",
     ["M380a", "M385b", "M405a", "M405b"]),
 ],
 "loc-rhalgrs-reach": [
   P(S["381"], None, "main", "Rhalgr's Reach",
     "An old temple east of the Velodyna River, hidden behind a glamour that looks like bare rock. It is the headquarters of the most influential faction of the Ala Mhigan Resistance.",
     ["M381a", "M381b", "M381d"]),
   P(S["383"], None, "main", "Rhalgr's Reach",
     "An old temple east of the Velodyna, hidden by a glamour, where the most influential faction of the Ala Mhigan Resistance has its headquarters. "
     "Its statue honors Rhalgr, the breaker of worlds, who guided the Ala Mhigans' ancestors to these lands; it shelters an infirmary for the Resistance's wounded, and sutlers keep it provisioned.",
     ["M381a", "M381b", "M383d", "M383f", "M383g"]),
   P(S["403"], None, "main", "Rhalgr's Reach",
     "The Ala Mhigan Resistance's hidden headquarters, an old temple east of the Velodyna. The imperials attacked it while you were scouting Castellum Velodyna: "
     "Fordola cut down Meffrid there, and Zenos left Y'shtola near death before Raubahn's Immortal Flames arrived.",
     ["M381b", "M403b", "M403d", "M403f", "M403h"]),
   P(S["405"], None, "main", "Rhalgr's Reach",
     "The Ala Mhigan Resistance's headquarters, an old temple east of the Velodyna, which the imperials attacked. It is no longer safe, since they could return at any time, "
     "so Pipin is moving the wounded to Castrum Oriens; Conrad stays behind to finish his work.",
     ["M381b", "M403b", "M405a", "M405b", "M405d"]),
 ],
 "loc-ala-gannha": [
   P(S["385b"], None, "main", "Ala Gannha",
     "A village in the Peaks of Gyr Abania and Lyse's birthplace. Several of its youths died at the Wall, so Conrad sent Meffrid there in search of recruits, "
     "but imperial spies may be listening, and the elder must be approached first.",
     ["M385bb", "M385bd", "M385be", "M385bf"]),
   P(S["386b"], None, "main", "Ala Gannha",
     "A village in the Peaks and Lyse's birthplace. Its elder, Raganfrid, says the Empire took the Ala Mhigans' lands, traditions and god, and that the village can give the Resistance no more, "
     "though Meffrid's party may stay.",
     ["M385bb", "M386ba", "M386bf", "M386bg"]),
   P(S["389"], None, "main", "Ala Gannha",
     "A village in the Peaks and Lyse's birthplace, whose elder will give the Resistance no recruits. The imperials raid such villages to stop them stockpiling, "
     "and Qiqirn attacked villagers carrying its tributum to the imperials.",
     ["M385bb", "M386bf", "M389a", "M389d"]),
   P(S["392"], None, "main", "Ala Gannha",
     "A village in the Peaks and Lyse's birthplace. Its elder says it has nothing left to give the Resistance, but one young villager has asked to fight and gone to Rhalgr's Reach.",
     ["M385bb", "M392d", "M392f", "M392g"]),
 ],
 "loc-castellum-velodyna": [
   P(S["381"], None, "main", "Castellum Velodyna",
     "The old bridge over the Velodyna River in Gyr Abania, which the imperials fortified and named Castellum Velodyna. The way to Rhalgr's Reach passes it by.",
     ["M381b", "M381c"]),
   P(S["386"], None, "main", "Castellum Velodyna",
     "The fortified bridge over the Velodyna River, held by the imperials. A shipment of prototype magitek armor from research facilities near the capital is said to have arrived there for field testing.",
     ["M381c", "M386d"]),
   P(S["402"], None, "main", "Castellum Velodyna",
     "The imperials' fortified bridge over the Velodyna River. Conrad has proposed an assault on it, and Raubahn has accepted: the Resistance and the Alliance's first offensive together, "
     "with Pipin set to assess its defenses.",
     ["M381c", "M397e", "M402a", "M402b", "M402f"]),
   P(S["406"], None, "main", "Castellum Velodyna",
     "The imperials' fortified bridge over the Velodyna River. The planned joint assault on it is off, since the attack on Rhalgr's Reach decimated the Resistance.",
     ["M381c", "M402a", "M406a"]),
 ],
 "loc-specula-imperatoris": [
   P(S["406"], None, "main", "Specula Imperatoris",
     "An imperial post in Gyr Abania, to which Zenos and his men returned straight after their attack on Rhalgr's Reach.",
     ["M406b"]),
 ],
 "loc-doma-castle": [
   P(S["408"], None, "main", "Doma Castle",
     "The castle of Doma, once the shining symbol of Doman heritage, where Hozan's ancestors served. "
     "It is now home to the imperial viceroy's witch and her host of men and magitek.",
     ["M408e", "M408g", "M408h"]),
 ],
 "org-ala-mhigan-resistance": [
   P(S["380"], None, "main", "The Ala Mhigan Resistance",
     "The Ala Mhigan Resistance, which fights the Empire in Gyr Abania, a land under imperial rule for twenty years. The Eorzean Alliance will not advance into Gyr Abania without its support, "
     "and has sent the Scions as its emissaries, with Lyse leading the way.",
     ["M380b", "M380c", "M380e", "M380h"]),
   P(S["381"], None, "main", "The Ala Mhigan Resistance",
     "The Ala Mhigan Resistance, a movement of many factions fighting the Empire in Gyr Abania. The most influential has its headquarters in Rhalgr's Reach, a temple hidden behind a glamour, "
     "and the Alliance's envoys have come to it.",
     ["M380b", "M380e", "M381a", "M381b", "M381f"]),
   P(S["384"], None, "main", "The Ala Mhigan Resistance",
     "The Ala Mhigan Resistance. Conrad, who commands it in Rhalgr's Reach, has accepted the Eorzean Alliance's offer of military aid, but he speaks only for the Reach: "
     "the movement is fragmented, and young recruits fill the posts of veterans who died at the Wall, where Ilberd led them to be sacrificed.",
     ["M382a", "M382d", "M382e", "M384a", "M384b", "M384c", "M384d"]),
   P(S["397"], None, "main", "The Ala Mhigan Resistance",
     "The Ala Mhigan Resistance, allied with the Eorzean Alliance through Conrad in Rhalgr's Reach. Together they destroyed imperial prototype weapons at East End without a single casualty, "
     "and its ranks are swelling with recruits and with Scions; once they are trained, Conrad will propose an assault on Castellum Velodyna.",
     ["M384a", "M387c", "M387e", "M388b", "M397a", "M397e"]),
   P(S["406"], None, "main", "The Ala Mhigan Resistance",
     "The Ala Mhigan Resistance, allied with the Eorzean Alliance. The imperial attack on its headquarters in Rhalgr's Reach decimated its forces, so there will be no assault on Castellum Velodyna, "
     "but Conrad has agreed to fight on, and Raubahn urges it to hold fast and rebuild.",
     ["M384a", "M403b", "M406a", "M406i", "M406j"]),
 ],
 "org-eorzean-alliance": [
   P(S["380"], None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. After the attack on the Wall and the summoning of Shinryu it occupied Castrum Oriens, but it will not march into Gyr Abania "
     "without the consent of the Ala Mhigan people, and has sent the Scions to the Resistance.",
     ["M380a", "M380e"]),
   P(S["384"], None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states, holding Castrum Oriens by the Wall. Through Alphinaud it offered the Ala Mhigan Resistance military aid, and Conrad accepted for Rhalgr's Reach.",
     ["M380a", "M382e", "M384a", "M384b"]),
   P(S["402"], None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states, allied with the Ala Mhigan Resistance. After their joint victory at East End, Raubahn has accepted Conrad's proposal: "
     "for the first time the two will go on the offensive together, against Castellum Velodyna.",
     ["M384a", "M387c", "M402a", "M402f"]),
 ],
 "char-conrad": [
   P(S["382"], None, "main", "Conrad",
     "Commander of the Ala Mhigan Resistance in Rhalgr's Reach, who sheltered Lyse and Papalymo at great risk. He says Ilberd led good men and women to the Wall and sacrificed them. "
     "He reads the Alliance's offer of aid as a war against the Empire by proxy, and must confer with his officers.",
     ["M382a", "M382b", "M382d", "M382f", "M382g"]),
   P(S["384"], None, "main", "Conrad",
     "Commander of the Ala Mhigan Resistance in Rhalgr's Reach. He has accepted the Eorzean Alliance's proposal, but can speak only for the Reach: the Resistance is fragmented, "
     "and young recruits fill the posts of veterans lost at the Wall. He has another task for the Scions.",
     ["M382a", "M384a", "M384b", "M384c", "M384d", "M384f"]),
   P(S["397"], None, "main", "Conrad",
     "Commander of the Ala Mhigan Resistance in Rhalgr's Reach, allied with the Eorzean Alliance. He called the victory at East End the start of a united Eorzea's campaign, "
     "welcomed Arenvald as a trueborn son of Gyr Abania, and will propose an assault on Castellum Velodyna once the recruits are trained.",
     ["M382a", "M388b", "M397d", "M397e"]),
   P(S["403"], None, "main", "Conrad",
     "Commander of the Ala Mhigan Resistance in Rhalgr's Reach. When the imperials attacked the Reach he made a last desperate stand, and was left unconscious.",
     ["M382a", "M403l", "M403e"]),
   P(S["404"], None, "main", "Conrad",
     "Commander of the Ala Mhigan Resistance in Rhalgr's Reach, grieving Meffrid after the imperial attack. He remembers a worrier who put others first and once sent his own men away "
     "so they would fight for the cause rather than for him; he had high hopes for him.",
     ["M382a", "M404c", "M404d", "M404f", "M404g"]),
   P(S["406"], None, "main", "Conrad",
     "Commander of the Ala Mhigan Resistance. The attack on Rhalgr's Reach decimated his forces and ended the plans for Castellum Velodyna; he grants that taking the fight to Doma has promise, but fears they lack the strength to see it through. "
     "Still, he has agreed to fight on.",
     ["M382a", "M406a", "M406j", "M406l"]),
 ],
 "char-mnaago": [
   P(S["384"], None, "main", "M'naago",
     "A fighter of the Ala Mhigan Resistance in Rhalgr's Reach, Lyse's friend, who once carried a message to the Scions. Conrad has charged her and Meffrid with explaining the Scions' next task.",
     ["M381e", "M384f"]),
   P(S["385"], None, "main", "M'naago",
     "A Resistance fighter from Rhalgr's Reach, nursed back to health by the Scions. She is carrying Conrad's formal reply to Raubahn at Castrum Oriens with you and Alisaie as escort, "
     "and warns that the conscripts who fill Gyr Abania's garrisons can still kill, and that no one in magitek armor deserves pity.",
     ["M385a", "M385c", "M385d", "M385e"]),
   P(S["388"], None, "main", "M'naago",
     "A Resistance fighter from Rhalgr's Reach who delivered Conrad's reply to Raubahn. After the victory at East End, small in practice but great as a symbol, "
     "she means to go from village to village spreading word of it and of the new alliance.",
     ["M386a", "M388a", "M388d"]),
   P(S["402"], None, "main", "M'naago",
     "A Resistance fighter from Rhalgr's Reach. Recruitment has exceeded expectations, and Conrad has sent her to present his proposal for an assault on Castellum Velodyna to Raubahn.",
     ["M402b", "M402e"]),
 ],
 "char-meffrid": [
   P(S["384"], None, "main", "Meffrid",
     "A fighter of the Ala Mhigan Resistance in Rhalgr's Reach. Conrad has charged him and M'naago with explaining the Scions' next task.",
     ["M384f"]),
   P(S["385b"], None, "main", "Meffrid",
     "A Resistance fighter you first met in Quarrymill. He dissolved his unit in Gridania and returned to Gyr Abania to join Conrad's people in Rhalgr's Reach, where he rose to a position of responsibility. "
     "Sent to find recruits, he is taking you and Lyse to Ala Gannha, warning that imperial spies may be listening.",
     ["M385bh", "M385ba", "M385bb", "M385bf"]),
   P(S["389"], None, "main", "Meffrid",
     "A Resistance fighter from Rhalgr's Reach, recruiting in Ala Gannha, where the elder will give no help. He admits he once ran from the Wall too, and set out with Lyse after a villager the Qiqirn had taken.",
     ["M385ba", "M386bf", "M389g", "M389d"]),
   P(S["391"], None, "main", "Meffrid",
     "A Resistance fighter from Rhalgr's Reach. He held Lyse back from rescuing a villager the Skulls were beating, since it would bring reprisals on the man's family and village. "
     "It sickens him to see his countrymen doing the viceroy's bidding, and he will cut every last one of them down if it comes to it.",
     ["M385ba", "M391b", "M391e", "M391g"]),
   P(S["392"], None, "main", "Meffrid",
     "A Resistance fighter from Rhalgr's Reach, who welcomed new recruits from Ala Gannha to the Reach. He warns Lyse that the day they face Garlean soldiers in battle will come.",
     ["M385ba", "M392g", "M392j"]),
   P(S["403"], None, "main", "Meffrid",
     "A Resistance fighter from Rhalgr's Reach. When the imperials attacked the Reach he called Fordola a traitor and kinslayer, and she cut him down.",
     ["M385ba", "M403f"]),
   P(S["404"], None, "main", "Meffrid",
     "A Resistance fighter from Rhalgr's Reach, cut down by Fordola in the imperial attack. He died with a charm in his fist. Conrad remembers a worrier who put others first, "
     "and Alphinaud says his sacrifice let many live.",
     ["M403f", "M404b", "M404c", "M404e", "M404g"]),
 ],
 "char-raganfrid": [
   P(S["386b"], None, "main", "Raganfrid",
     "The elder of Ala Gannha. He says the Empire took the Ala Mhigans' lands, traditions and god, and that the village can give the Resistance no more, though he lets Meffrid's party stay. "
     "He knew Lyse at once as her father's daughter.",
     ["M386bi", "M386ba", "M386bc", "M386bf", "M386bg"]),
   P(S["392"], None, "main", "Raganfrid",
     "The elder of Ala Gannha. He thanked you for saving Wercrata, though a rescue from the Skulls would have branded the family, perhaps the village, insurgents. "
     "He apologized to Lyse for judging her, and calls her strong like her father, but the village has nothing left to give.",
     ["M386bi", "M392b", "M392c", "M392d", "M392e"]),
 ],
 "char-arenvald": [
   P(S["397"], None, "main", "Arenvald",
     "A Scion you remember from your first days at the Waking Sands, a half-breed who came with Alphinaud to fight for a free Ala Mhigo. Conrad welcomed him as a trueborn son of Gyr Abania.",
     ["M397b", "M397c", "M397d"]),
   P(S["403"], None, "main", "Arenvald",
     "A Scion fighting for a free Ala Mhigo with the Resistance. When the imperials attacked Rhalgr's Reach, he and Krile were among those you met outside.",
     ["M397b", "M397c", "M403k"]),
 ],
 # -- Chain A: East End
 "char-grynewaht": [
   P(S["387"], None, "main", "Grynewaht",
     "An imperial officer, the brutish Roegadyn you faced on the Carteneau Flats, charged with field-testing prototype magitek in Gyr Abania. He hoped to bring your head to Zenos, "
     "but the Alliance and the Resistance destroyed his weapon at East End, and he fled, vowing that your next meeting will be the last.",
     ["M387a", "M387b", "M387c", "M387g"]),
 ],
 # -- Chain B and the Empire in Gyr Abania
 "char-fordola": [
   P(S["391"], None, "main", "Fordola",
     "Commander of the Skulls, a unit of Ala Mhigan conscripts in imperial service. She called off their beating of a villager from Ala Gannha, because Lord Zenos expects their report.",
     ["M391a", "M391c", "M391d"]),
   P(S["397"], None, "main", "Fordola",
     "An Ala Mhigan commander in imperial service. In the Royal Palace of Ala Mhigo an officer silenced her, sneering that she holds her place in name alone, "
     "but Zenos, remarking that she yearns to hunt her own, gave her the floor for her proposal.",
     ["M397j", "M397k", "M397m", "M397n"]),
   P(S["403"], None, "main", "Fordola",
     "An Ala Mhigan commander in imperial service. In the attack on Rhalgr's Reach she cut down Meffrid, who called her a traitor and kinslayer; Zenos, calling her Pilus, bade her stand aside.",
     ["M397j", "M403f", "M403j"]),
   P(S["406"], None, "main", "Fordola",
     "The Ala Mhigan commander of the Skulls, Crania Lupi, who fight for Zenos. Lyse saw her cut down Meffrid in the attack on Rhalgr's Reach.",
     ["M403f", "M406d", "M406e", "M406f"]),
 ],
 "org-crania-lupi": [
   P(S["391"], None, "main", "The Skulls",
     "A unit of Ala Mhigan conscripts in imperial service. They beat a villager from Ala Gannha for coming late with his tribute, one of them insisting he is a citizen, "
     "until their commander, Fordola, called them off: Lord Zenos expects their report.",
     ["M391a", "M391c", "M391d", "M391f"]),
   P(S["406"], None, "main", "Crania Lupi",
     "The unit the Resistance calls the Skulls: the Black Wolf's legacy, made up of children born to Ala Mhigan dignitaries during the occupation, who fight for Zenos. "
     "Their commander, an Ala Mhigan, cut down Meffrid in the attack on Rhalgr's Reach.",
     ["M406d", "M406e", "M406f"], ["The Skulls"]),
 ],
 "char-zenos": [
   P(S["387"], None, "main", "Zenos",
     "An imperial lord to whom Grynewaht hoped to bring your head. When the Alliance and the Resistance destroyed Grynewaht's prototype weapon at East End, "
     "Raubahn sent him running to tell his viceroy that the day belongs to Ala Mhigo.",
     ["M387b", "M387c", "M387d"], ["The Viceroy", "Lord Zenos"]),
   P(S["397"], None, "main", "Zenos",
     "An imperial lord of the XIIth, holding court in the Royal Palace of Ala Mhigo. Hearing that a prototype unit was destroyed, he killed an officer for cowardice. "
     "His honored father has not granted leave to march on the Alliance's lands, so he has invited them to Gyr Abania for the sport of kings, and gave Fordola the floor.",
     ["M397f", "M397g", "M397h", "M397i", "M397k", "M397l", "M397m"], ["The Viceroy", "Lord Zenos"]),
   P(S["403"], None, "main", "Zenos",
     "The imperial viceroy and crown prince. In the attack on Rhalgr's Reach he struck down Y'shtola, then bested you, judged you to have promise, and turned his back and walked away.",
     ["M403d", "M403g", "M403i", "M403j"], ["The Viceroy", "Lord Zenos"]),
   P(S["406"], None, "main", "Zenos",
     "The imperial viceroy, Varis's heir and next in line to the Garlean throne. Before taking charge in Ala Mhigo he crushed Doma's rebellion, and Doma remains in his charge. "
     "After the attack on Rhalgr's Reach he withdrew to Specula Imperatoris, and the Skulls fight for him.",
     ["M403d", "M406b", "M406c", "M406f", "M406g", "M406h", "M406m"], ["The Viceroy", "Lord Zenos"]),
 ],
 "char-varis": [
   P(S["406"], None, "main", "Varis",
     "Zenos's father, whose heir stands next in line to the Garlean throne. Zenos says his honored father has not granted leave to march on the Alliance's lands.",
     ["M397h", "M406h", "M406m"], ["Emperor Varis"]),
 ],
 # -- Scions and allies
 "char-lyse": [
   P(S["380"], None, "main", "Lyse",
     "A Scion with ties to the Ala Mhigan Resistance, chosen to lead the Scions into Gyr Abania as the Alliance's emissaries. Seeing Yugiri and Gosetsu off for Doma, she said it is time she went home too.",
     ["M380c", "M380e", "M380l"], ["Yda"]),
   P(S["382"], None, "main", "Lyse",
     "A Scion leading the Alliance's envoys to the Resistance, whom Conrad sheltered with Papalymo, at great risk, when she fought the Empire under a false name. "
     "She says Papalymo laid down his life so they could make a better future.",
     ["M380c", "M382b", "M382c", "M382h"], ["Yda"]),
   P(S["386b"], None, "main", "Lyse",
     "A Scion born in Ala Gannha, where she went with Meffrid to find recruits. The elder knew her at once as her father's daughter, and she declared she has come to take back her homeland; "
     "her sister never will.",
     ["M385bb", "M386bc", "M386bd", "M386be"], ["Yda"]),
   P(S["389"], None, "main", "Lyse",
     "A Scion born in Ala Gannha, come home to take back her homeland. A young villager raged at her for her twenty years away, and she accepts that she left them behind.",
     ["M385bb", "M386bd", "M389b", "M389c"], ["Yda"]),
   P(S["392"], None, "main", "Lyse",
     "A Scion born in Ala Gannha. She saw the Skulls in the flesh for the first time and believes you could have stopped their beating of Wercrata. "
     "The elder apologized for judging her and calls her strong like her father.",
     ["M385bb", "M392c", "M392e", "M392h", "M392i"], ["Yda"]),
   P(S["406"], None, "main", "Lyse",
     "A Scion of Ala Mhigan birth. In the attack on Rhalgr's Reach she came through unharmed, but saw the Skulls' commander, an Ala Mhigan, cut down Meffrid, and she dreads that Zenos is next in line to the Garlean throne. "
     "If the Scions go to Doma she is going too, to help friends there and keep such a thing from happening again.",
     ["M403e", "M406d", "M406m", "M406k"], ["Yda"]),
   P(S["409"], None, "main", "Lyse",
     "A Scion of Ala Mhigan birth, sailing with the Scions to help their friends in Doma. As the ship came into Kugane she stood apart, lips moving silently in a prayer or an oath.",
     ["M406k", "M409f"], ["Yda"]),
   P(S["414"], None, "main", "Lyse",
     "A Scion of Ala Mhigan birth, bound for Doma. When Gyodo betrayed you to an ambush in Kugane, she booted him into the air and carried him back unconscious.",
     ["M406k", "M414c", "M414i"], ["Yda"]),
 ],
 "char-alphinaud": [
   P(S["382"], None, "main", "Alphinaud",
     "A young Scion acting as the Alliance's envoy in Gyr Abania. In Rhalgr's Reach he thanked Conrad for sheltering Lyse and Papalymo, and formally offered the Resistance the Alliance's military aid.",
     ["M380b", "M382b", "M382e"]),
   P(S["384"], None, "main", "Alphinaud",
     "A young Scion who brokered the Resistance's acceptance of the Alliance's proposal, then returned to the Scions' headquarters.",
     ["M382e", "M384a", "M384e"]),
   P(S["397"], None, "main", "Alphinaud",
     "A young Scion who has brought fellow Scions eager to fight alongside the Ala Mhigan Resistance, Arenvald among them.",
     ["M384a", "M397a", "M397c"]),
   P(S["406"], None, "main", "Alphinaud",
     "A young Scion. After the attack on Rhalgr's Reach he points out that Zenos crushed Doma's rebellion before taking charge in Ala Mhigo, and still holds Doma as Varis's heir.",
     ["M406g", "M406h"]),
   P(S["412"], None, "main", "Alphinaud",
     "A young Scion in Kugane, wary of serving anyone in Lord Lolorito's debt yet accepting the East Aldenard Trading Company's help. He means to follow Yugiri and Gosetsu's footsteps to Doma.",
     ["M410d", "M412h", "M412i"]),
   P(S["416"], None, "main", "Alphinaud",
     "A young Scion who stays in Kugane with Tataru and Hancock to gather intelligence while the others cross the Ruby Sea, and keeps watch over Gyodo.",
     ["M415g", "M416i", "M416j"]),
 ],
 "char-alisaie": [
   P(S["385"], None, "main", "Alisaie",
     "Alphinaud's twin sister and a Scion. In Gyr Abania she volunteered to escort M'naago, who carries the Resistance's reply to Raubahn at Castrum Oriens.",
     ["M385a", "M385e"]),
   P(S["402"], None, "main", "Alisaie",
     "Alphinaud's twin sister and a Scion fighting beside the Ala Mhigan Resistance. She says the choice to fight was made for them before they were born, when the Empire marched on Eorzea.",
     ["M402a", "M402g"]),
   P(S["403"], None, "main", "Alisaie",
     "Alphinaud's twin sister and a Scion. She scouted Castellum Velodyna with Pipin, and in the attack on Rhalgr's Reach she fell to Zenos.",
     ["M403a", "M403m"]),
   P(S["407"], None, "main", "Alisaie",
     "Alphinaud's twin sister and a Scion, planning the journey to the Far East.",
     ["M403m", "M407a"]),
   P(S["409"], None, "main", "Alisaie",
     "Alphinaud's twin sister and a Scion, bound for Kugane. Before the ship sailed Urianger gave her a rapier and a cryptic warning, and the rift between them may have begun to heal.",
     ["M407a", "M409a", "M409b"]),
   P(S["416"], None, "main", "Alisaie",
     "Alphinaud's twin sister and a Scion. She set her brother to gather intelligence in Kugane, and sails with you, Lyse and Gosetsu across the Ruby Sea toward Doma.",
     ["M416i", "M416j"]),
 ],
 "char-yshtola": [
   P(S["380"], None, "main", "Y'shtola",
     "A Sharlayan Scion, going with the others to Gyr Abania as a healer.",
     ["M380j"]),
   P(S["402"], None, "main", "Y'shtola",
     "A Sharlayan Scion and healer in Gyr Abania. She will not take the field against Castellum Velodyna, and stays with Krile to tend the wounded.",
     ["M380j", "M402c", "M402d"]),
   P(S["403"], None, "main", "Y'shtola",
     "A Sharlayan Scion, struck down by Zenos in the imperial attack on Rhalgr's Reach and left on the verge of death.",
     ["M403d"]),
   P(S["405"], None, "main", "Y'shtola",
     "A Sharlayan Scion, struck down by Zenos in the attack on Rhalgr's Reach. Still unconscious, she is carried by chocobo carriage to Castrum Oriens.",
     ["M403d", "M405b", "M405c"]),
 ],
 "char-krile": [
   P(S["384"], None, "main", "Krile",
     "A Scion who came with the others to Rhalgr's Reach, and offers healers for its infirmary.",
     ["M384g"]),
   P(S["402"], None, "main", "Krile",
     "A Scion who says she came for Minfilia, and that has not changed. She stays in Gyr Abania with Y'shtola to tend the wounded.",
     ["M384g", "M402c", "M402d"]),
   P(S["407"], None, "main", "Krile",
     "A Scion staying in Gyr Abania to look after the wounded Y'shtola and support Arenvald and the others while the Scions travel to the Far East.",
     ["M402d", "M405c", "M407b"]),
 ],
 "char-urianger": [
   P(S["380"], None, "main", "Urianger",
     "A learned Sharlayan Scion who stays behind as caretaker of the Waking Sands, keeping watch for signs of primal and Ascian activity.",
     ["M380k"]),
   P(S["409"], None, "main", "Urianger",
     "A learned Sharlayan Scion and caretaker of the Waking Sands. He gave Alisaie a rapier and a cryptic warning in a Far Eastern verse before she sailed, and the rift between them may have begun to heal.",
     ["M380k", "M409a", "M409b"]),
 ],
 "char-thancred": [
   P(S["380"], None, "main", "Thancred",
     "A Scion who stays behind with Urianger while the others go to Gyr Abania, since some troubles may prove too much for one Scion.",
     ["M380k", "M380m"]),
 ],
 "char-tataru": [
   P(S["407"], None, "main", "Tataru",
     "The Scions' receptionist, who found them a captain for the voyage east: Carvallain, who agreed to carry them as far as Kugane.",
     ["M407d", "M407e", "M407f"]),
   P(S["416"], None, "main", "Tataru",
     "The Scions' receptionist, staying in Kugane with Alphinaud and Hancock to gather intelligence while the others cross the Ruby Sea.",
     ["M416i", "M416j"]),
 ],
 "char-cid": [
   P(S["380"], None, "main", "Cid",
     "An engineer who left the Empire and built the Ironworks. His search parties have followed the trail of Omega and Shinryu without result and cannot venture deeper into occupied territory; "
     "he says they engaged Omega's stasis systems.",
     ["M380f", "M380n", "M380o"]),
 ],
 "char-omega": [
   P(S["380"], None, "main", "Omega",
     "An Allagan weapon, missing since its fight with Shinryu. Raubahn fears it fell in occupied territory and may be in imperial hands, though Cid says its stasis systems were engaged.",
     ["M380f", "M380g", "M380n", "M380o"]),
 ],
 "char-shinryu": [
   P(S["380"], None, "main", "Shinryu",
     "The primal summoned on the Wall, which the Domans call Shinryu. Its summoning drove the Alliance to occupy Castrum Oriens, and its whereabouts, like Omega's, are unknown.",
     ["M380a", "M380f", "M380o"], ["Ilberd's primal"]),
 ],
 "char-ilberd": [
   P(S["380"], None, "main", "Ilberd",
     "The man who assaulted the Wall and summoned the primal now called Shinryu, leaving the Alliance little choice but to occupy Castrum Oriens. Raubahn expects Garlemald to answer such defiance.",
     ["M380a", "M380i"], ["The Griffin"]),
   P(S["382"], None, "main", "Ilberd",
     "The man who assaulted the Wall and summoned the primal now called Shinryu. Conrad says he led good men and women of the Resistance to the Wall and made sacrifices of them for his ritual.",
     ["M380a", "M382d"], ["The Griffin"]),
 ],
 "char-raubahn": [
   P(S["380"], None, "main", "Raubahn",
     "The Flame General, commanding the Alliance at Castrum Oriens. He will not advance into Gyr Abania without the Ala Mhigan people's support and sends the Scions as emissaries to the Resistance; "
     "he expects Garlemald to answer the primal summoned on its doorstep.",
     ["M380b", "M380e", "M380i"], ["General Raubahn"]),
   P(S["386"], None, "main", "Raubahn",
     "The Flame General, commanding the Alliance at Castrum Oriens. He is glad of the accord with the Resistance, and backs his son Pipin's plan for a joint ambush at East End as its rallying cry.",
     ["M385b", "M386b", "M386f", "M386g"], ["General Raubahn"]),
   P(S["387"], None, "main", "Raubahn",
     "The Flame General at Castrum Oriens. At East End he fought beside the Resistance as they destroyed imperial prototype weapons without a single casualty, and sent Grynewaht running to tell his viceroy "
     "that the day belongs to Ala Mhigo. Conrad recalls the Bull of Ala Mhigo's record before he went west.",
     ["M387c", "M387d", "M387e", "M387f"], ["General Raubahn"]),
   P(S["403"], None, "main", "Raubahn",
     "The Flame General at Castrum Oriens. He arrived with the Immortal Flames after the attack on Rhalgr's Reach, let the imperials withdraw to tend the wounded, and reminded you that your actions saved lives.",
     ["M385b", "M403h", "M403n"], ["General Raubahn"]),
   P(S["406"], None, "main", "Raubahn",
     "The Flame General at Castrum Oriens. He says Zenos is no fool to walk away, and urges the Resistance to hold fast and rebuild, so that together they can defeat him.",
     ["M385b", "M406c", "M406i"], ["General Raubahn"]),
 ],
 "char-pipin": [
   P(S["386"], None, "main", "Pipin",
     "Raubahn's son, a vice marshal. Learning that prototype magitek armor from near the capital has reached Castellum Velodyna for field testing, he proposed baiting it to East End for a joint ambush.",
     ["M386d", "M386e", "M386g", "M386h"], ["Vice Marshal Pipin"]),
   P(S["402"], None, "main", "Pipin",
     "Raubahn's son, a vice marshal, whom his father has ordered to watch Castellum Velodyna and assess its defenses before the joint assault.",
     ["M386g", "M386h", "M402f"], ["Vice Marshal Pipin"]),
   P(S["403"], None, "main", "Pipin",
     "Raubahn's son, a vice marshal. He took you, Alphinaud and Alisaie to scout Castellum Velodyna, and in the attack on Rhalgr's Reach he fell to Zenos.",
     ["M386g", "M386h", "M403a", "M403m"], ["Vice Marshal Pipin"]),
   P(S["405"], None, "main", "Pipin",
     "Raubahn's son, a vice marshal. With Rhalgr's Reach no longer safe, he is moving the wounded to Castrum Oriens by chocobo carriage.",
     ["M386g", "M386h", "M405a", "M405b"], ["Vice Marshal Pipin"]),
 ],
 # -- Doma and the Far East
 "loc-doma": [
   P(S["380"], None, "main", "Doma",
     "A nation in the Far East, where Yugiri and Gosetsu return to aid their comrades in the fight against Garlemald.",
     ["M380d", "M380p"]),
   P(S["406"], None, "main", "Doma",
     "A nation in the Far East, whose rebellion Zenos crushed before taking charge in Ala Mhigo; it remains in his charge. Lyse means to go there with the Scions.",
     ["M380d", "M406g", "M406h", "M406k"]),
   P(S["408"], None, "main", "Doma",
     "A nation in the Far East under Garlean rule for twenty-five years. It rose up when the Emperor died, but Zenos and the XIIth Legion crushed the uprising in an instant, "
     "and Doma Castle is now home to the imperial viceroy's witch and her forces.",
     ["M408b", "M408c", "M408d", "M408e"]),
   P(S["412"], None, "main", "Doma",
     "A nation in the Far East, conquered by Garlemald some twenty-five years ago, across the Ruby Sea from Kugane. Its recently appointed acting viceroy has condemned the Confederacy that rules the sea.",
     ["M408b", "M412d", "M412f", "M412j"]),
 ],
 "org-doman-refugees": [
   P(S["408"], None, "main", "The Doman refugees",
     "Refugees from Doma living in Revenant's Toll. They told you and Lyse of twenty-five years of Garlean tyranny, and rejoice that you go to join Yugiri and Gosetsu in the fight.",
     ["M408a", "M408b", "M408f"]),
 ],
 "char-yugiri": [
   P(S["380"], None, "main", "Yugiri",
     "A Doman who led her people to Eorzea as refugees. Now that they have a new home and no longer need her, she and Gosetsu return to their master in Doma to aid their comrades against Garlemald, "
     "thanking the Scions for standing with them from the first.",
     ["M380d", "M380q", "M380r"], ["Lady Yugiri"]),
   P(S["412"], None, "main", "Yugiri",
     "A Doman returning to fight for her homeland. She and Gosetsu reached Kugane aboard an East Aldenard Trading Company ship but could not secure passage across the Ruby Sea.",
     ["M380d", "M412c"], ["Lady Yugiri"]),
   P(S["416"], None, "main", "Yugiri",
     "A Doman in the service of Lord Hien, who sent her to sea with as many of their people as he could. She parted from Gosetsu to search for him, and Gosetsu expects to find her at the Domans' headquarters.",
     ["M416b", "M416c", "M416d", "M416h"], ["Lady Yugiri"]),
 ],
 "char-gosetsu": [
   P(S["380"], None, "main", "Gosetsu",
     "A Doman warrior returning with Yugiri to their master and their home, Doma, to fight Garlemald. He says their purpose and the Scions' are one, though their battlefields lie far apart.",
     ["M380d", "M380p", "M380r"]),
   P(S["413"], None, "main", "Gosetsu",
     "A Doman warrior bound for Doma. He reached Kugane with Yugiri aboard a company ship, but captains there turned the Roegadyn samurai away when he sought passage across the Ruby Sea.",
     ["M412c", "M413d", "M413e"]),
   P(S["415"], None, "main", "Gosetsu",
     "A Doman samurai. In Kugane, Gyodo sold him to the Garleans, who pay a bounty for Domans; he drew his blade, and the Sekiseigumi took him into custody until he won his freedom by defeating them.",
     ["M415a", "M415b", "M415c", "M415e"]),
   P(S["416"], None, "main", "Gosetsu",
     "A Doman samurai, sworn with Yugiri to Lord Hien, heir to Doma's throne. He stood by Hien in their doomed war until they were separated in battle, then parted from Yugiri to search for him. "
     "Freed in Kugane, he joins the Scions to lead them to Yugiri.",
     ["M416a", "M416b", "M416c", "M416e", "M416h"]),
 ],
 "char-hien": [
   P(S["416"], None, "main", "Hien",
     "Lord Hien, heir to Doma's throne and master of Gosetsu and Yugiri, a passionate voice for Doman liberation. When the uprising was doomed he sent Yugiri to sea with as many people as possible and stayed to fight. "
     "Separated from Gosetsu in battle, he survived beyond the Empire's reach, and the Empire seeks to make an example of him.",
     ["M416c", "M416d", "M416e", "M416k", "M416m"], ["Lord Hien"]),
 ],
 "char-yotsuyu": [
   P(S["412"], None, "main", "Doma's acting viceroy",
     "The recently appointed acting imperial viceroy of Doma. She condemned the Confederacy and declared that any who recognize it will be enemies of the Empire, and Hingashi has since banned the Ruby Tithe.",
     ["M412f", "M412g"]),
   P(S["414"], None, "main", "Doma's acting viceroy",
     "The recently appointed acting imperial viceroy of Doma, who condemned the Confederacy. Hancock recalls that she was once a spy herself.",
     ["M412f", "M414h"]),
   P(S["416"], None, "main", "Yotsuyu",
     "Doma's new viceroy, whom Gosetsu calls a black-hearted villainess who delights in tormenting his people. She will stop at nothing in her pursuit of Lord Hien, and has condemned the Confederacy.",
     ["M412f", "M414h", "M416f"], ["Doma's acting viceroy"]),
   P(S["418"], None, "main", "Yotsuyu",
     "Doma's acting viceroy, hunting Lord Hien. She is no friend of Domans and is purging the fishing villages of Doma's radical elements; the Confederacy dares not hinder imperial ships, "
     "lest she brand it an enemy of the Empire.",
     ["M416f", "M418e", "M418f", "M418g"], ["Doma's acting viceroy"]),
 ],
 "org-doman-liberation-front": [
   P(S["412"], None, "main", "The Doman Liberation Front",
     "The Doman resistance against the Empire. Hancock assumes the Scions have come to aid it, and Alphinaud hopes to assist Yugiri and Gosetsu in their fight.",
     ["M412b", "M412k"]),
   P(S["416"], None, "main", "The Doman Liberation Front",
     "The Doman resistance, whose master is Lord Hien, heir to Doma's throne. The Scions have come to help it resume its fight, and Gosetsu will lead them to its headquarters.",
     ["M416c", "M416g", "M416h"]),
 ],
 "char-carvallain": [
   P(S["407"], None, "main", "Carvallain",
     "A ship's captain whom Tataru found in Limsa Lominsa. He cannot sail to Doma itself, but agreed to carry the Scions as far as Kugane, in Hingashi.",
     ["M407d", "M407e", "M407f"]),
   P(S["410"], None, "main", "Carvallain",
     "The captain who sailed the Scions from Limsa Lominsa to Kugane, as far as he pledged; from there they must find their own way to Doma.",
     ["M409g", "M410a"]),
 ],
 "loc-kugane": [
   P(S["407"], None, "main", "Kugane",
     "A port in Hingashi, as far as Carvallain will carry the Scions toward Doma.",
     ["M407e"]),
   P(S["409"], None, "main", "Kugane",
     "A port city in Hingashi, the only one open to outsiders and foreign trade, across the sea from Doma. The Scions have arrived there.",
     ["M409e", "M409h"]),
   P(S["410"], None, "main", "Kugane",
     "The only port in Hingashi open to foreign trade. Many nations, the Garlean Empire among them, keep embassies there, and beneath its bustling trade world powers wage a war for supremacy.",
     ["M409h", "M410e", "M410f"]),
   P(S["411"], None, "main", "Kugane",
     "The only port in Hingashi open to foreign trade, where world powers wage a hidden war. Foreigners may live in the Ijin-gai, the Garlean Consulate stands nearby, "
     "and the Sekiseigumi punish any breach of the peace severely.",
     ["M410e", "M410f", "M411a", "M411b", "M411d"]),
 ],
 "char-hancock": [
   P(S["410"], None, "main", "Hancock",
     "A man of the East Aldenard Trading Company who welcomed the Scions to Kugane on behalf of Chairman Lolorito. He warns that world powers wage a war for supremacy beneath the city's trade.",
     ["M410c", "M410e", "M410f"]),
   P(S["412"], None, "main", "Hancock",
     "An agent of the East Aldenard Trading Company in Kugane. He calls the company's help Lolorito's contrition for the bloody banquet, says its interests coincide with aiding the Doman Liberation Front, "
     "and told the Scions how Yugiri and Gosetsu failed to cross the Ruby Sea.",
     ["M410c", "M412a", "M412b", "M412c"]),
   P(S["415"], None, "main", "Hancock",
     "An agent of the East Aldenard Trading Company in Kugane, who has brokered an agreement with Soroban. He went to bribe the Sekiseigumi to free Gosetsu, but his help was not needed.",
     ["M410c", "M414e", "M415d", "M415f"]),
 ],
 "char-lolorito": [
   P(S["410"], None, "main", "Lolorito",
     "Chairman of the East Aldenard Trading Company, in whose name Hancock welcomed the Scions to Kugane. Alphinaud calls theirs a difficult relationship.",
     ["M410c", "M410d"]),
   P(S["412"], None, "main", "Lolorito",
     "Chairman of the East Aldenard Trading Company. Hancock presents the company's help to the Scions as Lolorito's contrition for the bloody banquet, and Alphinaud is reluctant to be in his debt.",
     ["M410c", "M412a", "M412i"]),
 ],
 "org-east-aldenard-trading-company": [
   P(S["410"], None, "main", "The East Aldenard Trading Company",
     "A trading company chaired by Lolorito, with offices in Kugane. Its man Hancock welcomed the Scions on arrival and offered them hospitality.",
     ["M410c", "M410g"]),
   P(S["412"], None, "main", "The East Aldenard Trading Company",
     "Lolorito's trading company, which hosts the Scions in Kugane. Its aid is offered as contrition for the bloody banquet, and its interests coincide with aiding the Doman Liberation Front; "
     "Yugiri and Gosetsu reached Kugane on one of its ships.",
     ["M410c", "M412a", "M412b", "M412c"]),
   P(S["414"], None, "main", "The East Aldenard Trading Company",
     "Lolorito's trading company in Kugane, which hosts the Scions. Through Hancock it has struck an agreement with Soroban, a Kojin merchant who offers the Scions passage across the Ruby Sea.",
     ["M412a", "M414e", "M414f"]),
 ],
 "org-sekiseigumi": [
   P(S["411"], None, "main", "The Sekiseigumi",
     "Kugane's samurai peacekeepers, who punish breaches of the peace severely; one cut down a foreign merchant with a single stroke.",
     ["M411b", "M411c"]),
   P(S["414"], None, "main", "The Sekiseigumi",
     "Kugane's samurai peacekeepers. After the ambush on the Tasogare Bridge they sent patrols after the Scions, perhaps taking them for agents of foreign powers.",
     ["M411b", "M414d"]),
   P(S["415"], None, "main", "The Sekiseigumi",
     "Kugane's samurai peacekeepers. They took Gosetsu into custody after he drew his blade, but he won his freedom by defeating them, and they keep their word.",
     ["M411b", "M415c", "M415e"]),
 ],
 "char-gyodo": [
   P(S["414"], None, "main", "Gyodo",
     "A Namazu who frequents the Shiokaze Hostelry in Kugane. He claimed to have found Yugiri and Gosetsu a ship, then led the Scions into an imperial ambush on the Tasogare Bridge; "
     "Lyse carried him back unconscious.",
     ["M414j", "M414a", "M414c", "M414k", "M414i"]),
   P(S["415"], None, "main", "Gyodo",
     "A Namazu of Kugane, held by the Scions. He confessed he met only Gosetsu and sold him to the Garleans, who pay a bounty for Domans; Alphinaud keeps watch over him.",
     ["M414c", "M415a", "M415b", "M415g"]),
 ],
 "char-soroban": [
   P(S["414"], None, "main", "Soroban",
     "A Kojin of the Blue, a merchant who hid the Scions from the Sekiseigumi in Kugane and seeks an agreement with Hancock. Unlike the Kojin of the Red, who serve the Empire as mercenaries, "
     "his people walk a different path, and he offers passage across the Ruby Sea.",
     ["M414d", "M414e", "M414f", "M414g"]),
   P(S["418"], None, "main", "Soroban",
     "A Kojin of the Blue and merchant, carrying the Scions across the Ruby Sea. He offered to pay their passage to the Confederacy, and was reluctant to be seen with them by his Red brothers.",
     ["M414e", "M418a", "M418j", "M418k"]),
 ],
 "loc-ruby-sea": [
   P(S["412"], None, "main", "The Ruby Sea",
     "The sea between Hingashi and Doma, controlled since antiquity by the Confederacy, which demands a toll, the Ruby Tithe, from every vessel.",
     ["M412d", "M412e"]),
   P(S["416"], None, "main", "The Ruby Sea",
     "The sea between Hingashi and Doma, named for the crimson it turns with the morning sun. The Confederacy rules it, and the Scions now sail it with Soroban.",
     ["M412d", "M416j", "M416n"]),
 ],
 "org-confederacy": [
   P(S["412"], None, "main", "The Confederacy",
     "A maritime collective that has controlled the Ruby Sea since antiquity, demanding the Ruby Tithe in exchange for its fleet's protection. "
     "Doma's acting viceroy has condemned it, and Hingashi has cut ties with it and banned the payment.",
     ["M412d", "M412e", "M412f", "M412g"]),
   P(S["417"], None, "main", "The Confederacy",
     "The maritime collective that rules the Ruby Sea. Crossing without the Ruby Tithe invites it to claim your vessel, and your life if you resist; paying earns the pirate lords' blessing. "
     "Tansui serves its captain.",
     ["M412d", "M417a", "M417b", "M417d"]),
   P(S["418"], None, "main", "The Confederacy",
     "The maritime collective that rules the Ruby Sea, many of its members of Doman descent. It will not hinder imperial ships, lest Doma's acting viceroy brand it an enemy of the Empire, "
     "but counted the Scions' tithe paid for what it expects of them.",
     ["M412d", "M418c", "M418e", "M418f", "M418h"]),
 ],
 "char-tansui": [
   P(S["417"], None, "main", "Tansui",
     "A mate who serves the Confederacy's captain, waiting on an isle in the Ruby Sea. He greeted you by name, and expects business from anyone traveling with Soroban.",
     ["M417d", "M417e", "M417f", "M417g"]),
   P(S["418"], None, "main", "Tansui",
     "A mate who serves the Confederacy's captain. He judged Soroban's payment too small for a safe crossing yet counted the Scions' tithe paid for what he expects they will do; "
     "the Confederacy, he says, is outmatched by the imperial army.",
     ["M417d", "M418b", "M418c", "M418h"]),
 ],
}

# ---- Arc entries: one recap per step -----------------------------------------------------------------------------------
N1, N2, N3, N4, N5, N6 = ("Envoys to the Resistance", "The East End Ambush", "Return to Ala Gannha", "Blood in Rhalgr's Reach",
                          "Passage to the Far East", "Across the Ruby Sea")

PRES.update({
 "evt-envoys-to-the-resistance": [
   P(S["380"], None, "main", N1,
     "The Alliance has occupied Castrum Oriens beside the Wall, but Raubahn will not march into Gyr Abania without the Ala Mhigan Resistance. He sends the Scions as envoys, "
     "with Lyse leading the way given her ties to the Resistance. Yugiri and Gosetsu have gone home to fight for Doma, and Cid's search for Omega and Shinryu has found nothing.",
     ["M380a", "M380c", "M380d", "M380e", "M380f"]),
   P(S["381"], None, "main", N1,
     "Seeking the Resistance's support for the Alliance, Lyse led you and the Scions east across the Velodyna, past a bridge the imperials have fortified as Castellum Velodyna. "
     "Her goal is the most influential faction of the Resistance, headquartered in Rhalgr's Reach, an old temple hidden behind a glamour. Its people were waiting for you.",
     ["M380e", "M381a", "M381b", "M381c", "M381d", "M381f"]),
   P(S["382"], None, "main", N1,
     "In Rhalgr's Reach, Conrad, who commands the Resistance there, heard Alphinaud's formal offer of Alliance military aid and called it a war fought by proxy with the Resistance's weaker forces. "
     "His officers must confer. Lyse says Papalymo gave his life for a better future, and Conrad tells how Ilberd led Resistance fighters to the Wall and sacrificed them.",
     ["M382a", "M382c", "M382d", "M382e", "M382f", "M382g"]),
   P(S["383"], None, "main", N1,
     "Conrad's officers are weighing the Alliance's offer of military aid, so Lyse showed you around Rhalgr's Reach. Hellsguard, Seekers of the Sun and Ananta fight in the Resistance, "
     "though one faction will have nothing to do with it. The Reach's statue honors Rhalgr, the breaker of worlds, whose story Yda told Lyse on stormy nights.",
     ["M382g", "M383b", "M383c", "M383d", "M383e"]),
   P(S["384"], None, "main", N1,
     "Conrad has accepted the Alliance's proposal, but warns he speaks only for Rhalgr's Reach: the Resistance is fragmented, and young recruits fill the posts of veterans who died at the Wall. "
     "Alphinaud returns to the Scions' headquarters, Krile offers healers for the infirmary, and Conrad has another task for you, which M'naago and Meffrid will explain.",
     ["M384a", "M384b", "M384c", "M384d", "M384e", "M384f", "M384g"]),
 ],
 "evt-the-east-end-ambush": [
   P(S["385"], None, "main", N2,
     "The Resistance in Rhalgr's Reach has accepted the Alliance's proposal. M'naago, nursed back to health by the Scions, is carrying Conrad's formal reply to Raubahn at Castrum Oriens, "
     "with you and Alisaie as escort. On the road you ambushed an imperial patrol, and she warned that the conscripts who fill Gyr Abania's garrisons can still kill.",
     ["M384a", "M385a", "M385c", "M385d", "M385f"]),
   P(S["386"], None, "main", N2,
     "M'naago delivered Conrad's reply, and Raubahn is glad of the accord, though the Resistance lost many of its finest at the Wall and struggles to recruit. "
     "His son Pipin learned that prototype magitek armor has reached Castellum Velodyna, and proposes luring it to East End for a joint ambush that would give the Resistance its rallying cry.",
     ["M386a", "M386b", "M386c", "M386d", "M386e", "M386f"]),
   P(S["387"], None, "main", N2,
     "At East End the Alliance and the Resistance destroyed the prototype magitek armor without a single casualty. Its overseer, Grynewaht, whom you faced at Carteneau, had hoped to bring your head to Zenos, "
     "and fled vowing that your next meeting will be the last. Raubahn sent him to tell his viceroy that the day belongs to Ala Mhigo.",
     ["M387a", "M387b", "M387c", "M387d", "M387e", "M387g"]),
   P(S["388"], None, "main", N2,
     "The Alliance and the Resistance won their first joint battle at East End, destroying an imperial prototype without losses. Back in Rhalgr's Reach, Conrad calls it the start of a united Eorzea's campaign "
     "to drive out the Garleans, and M'naago means to carry word of the victory from village to village to draw recruits.",
     ["M387c", "M387e", "M388a", "M388b", "M388d"]),
 ],
 "evt-return-to-ala-gannha": [
   P(S["385b"], None, "main", N3,
     "The Resistance in Rhalgr's Reach has accepted the Alliance's proposal and needs recruits. Meffrid, whom you met in Quarrymill, now serves Conrad's people and is sent to Ala Gannha, "
     "Lyse's birthplace, where several youths died at the Wall. Lyse came along through ruins the mad king razed, and Meffrid warns that the village elder must be approached first.",
     ["M384a", "M385ba", "M385bb", "M385bc", "M385bd", "M385be"]),
   P(S["386b"], None, "main", N3,
     "In Ala Gannha, Meffrid and Lyse seek recruits for the Resistance. The elder, Raganfrid, says the Empire took their lands, traditions and god and the village can give no more, though he lets them stay. "
     "He knew Lyse for her father's daughter, and she says she has come to take back her homeland, so they will win over the villagers one by one.",
     ["M386ba", "M386bc", "M386bd", "M386bf", "M386bg", "M386bh"]),
   P(S["387b"], None, "main", N3,
     "Raganfrid, elder of Ala Gannha, will give the Resistance no recruits, so you are helping its villagers yourselves. Griseldis, lamed by an imperial patrol that took her herb-gathering spear for a rebel's, "
     "lost her father while she limped home, and the imperials have warned everyone not to help her.",
     ["M386bf", "M386bh", "M387ba", "M387bb", "M387bc", "M387bd"]),
   P(S["387c"], None, "main", N3,
     "Raganfrid, elder of Ala Gannha, will give the Resistance no recruits, so you are winning its villagers over one task at a time. Brothers working the quarry slip saltpeter for firesand to sutlers "
     "who supply the Resistance, a living and a way of fighting back; the Empire put their father in uniform and shipped him off fifteen years ago.",
     ["M386bf", "M386bh", "M387ca", "M387cb", "M387cc", "M387cd"]),
   P(S["389"], None, "main", N3,
     "Meffrid and Lyse are still courting Ala Gannha, where imperials seize supplies to stop stockpiling. A young villager raged at Lyse for her twenty years away, and she accepts that she left them behind. "
     "Then Qiqirn attacked villagers carrying the tributum to the imperials and took Wercrata to the Ziggurat, and Lyse set off to save him.",
     ["M389a", "M389b", "M389c", "M389d", "M389e", "M389f"]),
   P(S["390"], None, "main", N3,
     "Seeking recruits in Ala Gannha, Meffrid, Lyse and you tracked Qiqirn bandits to the Ziggurat and freed Wercrata, starved for months and terrified. "
     "He still owes the imperials their tribute, already warned once for paying short, and ran off to deliver it. Lyse has a bad feeling about it.",
     ["M390a", "M390b", "M390c", "M390d", "M390e"]),
   P(S["391"], None, "main", N3,
     "In the Peaks you followed Wercrata as he delivered Ala Gannha's tributum. The Skulls, a unit of Ala Mhigan conscripts, beat him for coming late, and Meffrid held Lyse back because a rescue "
     "would bring reprisals on his family and village. Their commander, Fordola, called them off: Lord Zenos expects their report.",
     ["M391a", "M391b", "M391c", "M391d"]),
   P(S["392"], None, "main", N3,
     "Wercrata survived the Skulls and the tributum is paid. Raganfrid thanked you and apologized for judging Lyse, saying she is strong like her father, but Ala Gannha has nothing left to give. "
     "Still, the young villager who scorned her has asked to fight, and Meffrid welcomes the new recruits to Rhalgr's Reach.",
     ["M392a", "M392c", "M392d", "M392e", "M392f", "M392g"]),
 ],
 "evt-blood-in-rhalgrs-reach": [
   P(S["397"], None, "main", N4,
     "After the victory at East End and new recruits from the Peaks, the Resistance in Rhalgr's Reach is growing, and Alphinaud has brought Scions eager to join, Arenvald among them. "
     "Conrad will propose an assault on Castellum Velodyna once the recruits are trained. In Ala Mhigo's palace, Zenos killed an officer for cowardice and gave Fordola the floor.",
     ["M397a", "M397b", "M397e", "M397f", "M397g", "M397k", "M397m"]),
   P(S["398"], None, "main", N4,
     "The Resistance in Rhalgr's Reach is preparing for an assault on Castellum Velodyna. For Beves, a historian, you recorded why its fighters joined: Hrotmar to avenge a friend the imperials killed over a piece of fruit, "
     "Orella because her father and brothers were worked to death building a castrum, and Hughoc because otherwise he would be fighting for the Empire.",
     ["M397e", "M398a", "M398b", "M398c", "M398d", "M398f"]),
   P(S["398b"], None, "main", N4,
     "The Resistance in Rhalgr's Reach is preparing for an assault on Castellum Velodyna. Ahelissa, its cook, needed herbs for her stew, and says there is never enough food: "
     "the villages give what they can, though too many have children more deserving. Still, the people of the Reach never lose sight of the dream.",
     ["M397e", "M398ba", "M398bb", "M398bc", "M398bd"]),
   P(S["398c"], None, "main", N4,
     "The Resistance in Rhalgr's Reach is preparing for an assault on Castellum Velodyna, and its newest recruits are in training. You rounded up five who were late to an Ananta battlemaid's drills, "
     "one of them praying for a sister the imperials had wronged; another says Ala Mhigo's future government is moot until the imperials are gone.",
     ["M397e", "M398ca", "M398cb", "M398cc", "M398cd"]),
   P(S["401"], None, "main", N4,
     "The Resistance in Rhalgr's Reach is readying an assault on Castellum Velodyna. You found a fighter's lost ward, and he spoke of the Temple of the Fist, where his mother once made a pilgrimage, "
     "until the mad king burned it; the Garleans who followed cared even less for Ala Mhigo's faith, but he keeps the old ways.",
     ["M397e", "M401a", "M401b", "M401c", "M401d", "M401e"]),
   P(S["402"], None, "main", N4,
     "Conrad's proposal is set: for the first time the Resistance and the Alliance will go on the offensive together, against Castellum Velodyna. Raubahn accepted it at Castrum Oriens and told Pipin "
     "to assess the castellum's defenses, as recruitment has exceeded expectations. Y'shtola and Krile will stay behind to tend the wounded.",
     ["M402a", "M402b", "M402c", "M402d", "M402e", "M402f"]),
   P(S["403"], None, "main", N4,
     "While you scouted Castellum Velodyna with Pipin, Alphinaud and Alisaie, the imperials struck Rhalgr's Reach. Fordola cut Meffrid down, and Zenos, the viceroy and crown prince, left Y'shtola near death, "
     "then bested you and walked away. Raubahn and his Immortal Flames arrived and let the imperials withdraw, reminding you that your actions saved lives.",
     ["M403a", "M403b", "M403d", "M403f", "M403g", "M403h", "M403i", "M403n"]),
   P(S["404"], None, "main", N4,
     "After the imperial attack on Rhalgr's Reach, Raubahn set you to tending the wounded. Meffrid lies dead, a charm in his fist, and Conrad grieves the worrier who always put others first "
     "and once sent his own men away so they would fight for the cause, not for him. Alphinaud says his sacrifice let many live.",
     ["M404a", "M404b", "M404c", "M404d", "M404e", "M404g"]),
   P(S["405"], None, "main", N4,
     "With Rhalgr's Reach no longer safe after the imperial attack and Meffrid's death, Pipin is moving the wounded to Castrum Oriens by chocobo carriage. "
     "You gathered medical supplies for the journey, and Y'shtola, still unconscious, travels with Krile and Lyse at her side. Conrad stays behind to finish his work.",
     ["M404b", "M405a", "M405b", "M405c", "M405d", "M405e"]),
   P(S["406"], None, "main", N4,
     "The attack on Rhalgr's Reach decimated the Resistance, so there will be no assault on Castellum Velodyna, and Zenos withdrew to Specula Imperatoris. The Skulls who cut down Meffrid are Crania Lupi, "
     "the Black Wolf's legacy. Zenos still holds Doma, whose rebellion he crushed, so the Scions will go there, Lyse with them, while Conrad rebuilds and fights on.",
     ["M406a", "M406b", "M406d", "M406e", "M406g", "M406h", "M406j", "M406k"]),
 ],
 "evt-passage-to-the-far-east": [
   P(S["407"], None, "main", N5,
     "The Scions are bound for Doma, which Zenos also holds, though Krile stays to look after Y'shtola and support Arenvald and the others. No airship can fly so far and no Alliance vessel would pass unnoticed, "
     "so in Limsa Lominsa Tataru found a captain, Carvallain, who agreed to carry you only as far as Kugane.",
     ["M406h", "M406k", "M407a", "M407b", "M407c", "M407d", "M407e"]),
   P(S["408"], None, "main", N5,
     "While Carvallain readies his ship for Kugane, Alphinaud sent you and Lyse to the Doman refugees in Revenant's Toll. They told of twenty-five years of Garlean rule, of an uprising launched when the Emperor died "
     "and crushed in an instant by Zenos and the XIIth Legion, and of Doma Castle, now home to the viceroy's witch.",
     ["M407e", "M408a", "M408b", "M408c", "M408d", "M408e"]),
   P(S["409"], None, "main", N5,
     "On the voyage from Limsa Lominsa, Urianger gave Alisaie a rapier and a cryptic warning, and their rift may be healing. A strange force dragged the ship off course until the being the sailors call Lorelei fell. "
     "You have reached Kugane, the only port in Hingashi open to outsiders, across the sea from Doma, where Lyse's lips moved in a silent prayer or oath.",
     ["M409a", "M409c", "M409d", "M409e", "M409f", "M409g"]),
   P(S["410"], None, "main", N5,
     "In Kugane, Carvallain left the Scions to find their own way to Doma, where they hope to find Yugiri and Gosetsu. Hancock of the East Aldenard Trading Company welcomed you on behalf of Chairman Lolorito "
     "and warned of a hidden war between world powers in the city. Alphinaud distrusts him, but Alisaie accepts his hospitality for now.",
     ["M410a", "M410b", "M410c", "M410d", "M410f", "M410g"]),
   P(S["411"], None, "main", N5,
     "In Kugane, Hancock of the East Aldenard Trading Company showed the Scions the markets and the Ijin-gai, where foreigners may live. He warned that the Sekiseigumi punish any breach of the peace severely, "
     "sometimes with a single stroke of the sword, and pointed out the Garlean Consulate. You still seek passage to Doma and word of Yugiri and Gosetsu.",
     ["M410b", "M410c", "M411a", "M411b", "M411c", "M411d"]),
   P(S["412"], None, "main", N5,
     "Hancock calls Lolorito's aid contrition for the bloody banquet, and says Yugiri and Gosetsu reached Kugane on a company ship but could not cross the Ruby Sea. The Confederacy rules those waters and takes a toll, "
     "the Ruby Tithe, but Doma's acting viceroy has condemned it and Hingashi has banned the payment. Alphinaud will follow the pair's footsteps.",
     ["M412a", "M412c", "M412d", "M412e", "M412f", "M412g", "M412h"]),
 ],
 "evt-across-the-ruby-sea": [
   P(S["413"], None, "main", N6,
     "Seeking Yugiri and Gosetsu and a way across the Ruby Sea, the Scions searched Kugane with Alphinaud's sketches. The hostelry's keeper says the pair sought passage there, and three captains turned away "
     "a Roegadyn samurai bound for Doma, but none of them knows the woman. The search has found nothing more.",
     ["M412c", "M413a", "M413b", "M413d", "M413e", "M413f"]),
   P(S["414"], None, "main", N6,
     "Your search for Gosetsu led to Gyodo, a Namazu who claimed to have found the pair a ship; he led you into an imperial ambush on the Tasogare Bridge. "
     "With the Sekiseigumi hunting you, Soroban, a Kojin of the Blue, hid you and offers passage across the Ruby Sea, while Lyse carried the unconscious Gyodo back.",
     ["M414a", "M414c", "M414d", "M414e", "M414f", "M414i", "M414j"]),
   P(S["415"], None, "main", N6,
     "Questioned, Gyodo admitted he met only Gosetsu and sold him to the Garleans, who pay a bounty for Domans in Kugane; Gosetsu drew his blade and the Sekiseigumi took him away. "
     "Hancock went to bribe his jailers, but Gosetsu had already won his freedom by defeating them. Alphinaud keeps Gyodo under watch.",
     ["M415a", "M415b", "M415c", "M415d", "M415e", "M415f", "M415g"]),
   P(S["416"], None, "main", N6,
     "Freed, Gosetsu explained that he and Yugiri parted to seek Lord Hien, heir to Doma's throne, lost in battle after the failed uprising, while Doma's new viceroy, Yotsuyu, hunts him. "
     "Gosetsu will lead the Scions to Yugiri. Alphinaud and Tataru stay in Kugane to gather intelligence, and you, Lyse, Alisaie and Gosetsu sailed with Soroban onto the Ruby Sea.",
     ["M416a", "M416b", "M416c", "M416e", "M416f", "M416h", "M416i", "M416j"]),
   P(S["417"], None, "main", N6,
     "Sailing for Doma with Gosetsu, Lyse and Alisaie on Soroban's ship, you learned the Ruby Sea cannot be crossed without paying the Confederacy's Ruby Tithe, lest it claim your vessel and your life. "
     "On an isle to the west, Soroban introduced you to Tansui, a mate who serves the Confederacy's captain and expects business.",
     ["M416j", "M417a", "M417b", "M417c", "M417d", "M417e"]),
   P(S["418"], None, "main", N6,
     "Tansui judged Soroban's payment too small for a safe crossing, yet counted the Scions' tithe paid for what he expects you will do. An imperial ship showed why the Confederacy, many of them of Doman descent, "
     "will not defy the Empire: Doma's acting viceroy is purging the fishing villages of radical elements. Gosetsu says she must be stopped.",
     ["M418b", "M418c", "M418d", "M418e", "M418f", "M418g", "M418i"]),
 ],
})

# ---- Relationship types and relationships ------------------------------------------------------------------------------
TYPES = [("child-of", "child of", "parent of", False)]   # same labels as content_3_0_part1

RELS = [
 # Gyr Abania
 ("rel-eorzean-alliance-controls-castrum-oriens", "org-eorzean-alliance", "controls", "loc-castrum-oriens", S["380"], None, "main", ["M380a"]),
 ("rel-scions-aids-ala-mhigan-resistance", "org-scions", "aids", "org-ala-mhigan-resistance", S["380"], None, "main", ["M380b", "M380e"]),
 ("rel-lyse-aids-ala-mhigan-resistance", "char-lyse", "aids", "org-ala-mhigan-resistance", S["380"], None, "main", ["M380c"]),
 ("rel-ala-mhigan-resistance-headquartered-at-rhalgrs-reach", "org-ala-mhigan-resistance", "headquartered-at", "loc-rhalgrs-reach", S["381"], None, "main", ["M381a", "M381b"]),
 ("rel-conrad-leads-ala-mhigan-resistance", "char-conrad", "leads", "org-ala-mhigan-resistance", S["382"], None, "main", ["M382a"]),
 ("rel-ala-mhigan-resistance-allied-with-eorzean-alliance", "org-ala-mhigan-resistance", "allied-with", "org-eorzean-alliance", S["384"], None, "main", ["M382e", "M384a"]),
 ("rel-mnaago-member-of-ala-mhigan-resistance", "char-mnaago", "member-of", "org-ala-mhigan-resistance", S["384"], None, "main", ["M381e", "M384f"]),
 ("rel-meffrid-member-of-ala-mhigan-resistance", "char-meffrid", "member-of", "org-ala-mhigan-resistance", S["384"], S["403"], "main", ["M384f"], ["M403f"]),
 ("rel-grynewaht-member-of-garlean-empire", "char-grynewaht", "member-of", "org-garlean-empire", S["387"], None, "main", ["M387a"]),
 ("rel-grynewaht-serves-zenos", "char-grynewaht", "serves", "char-zenos", S["387"], None, "main", ["M387b"]),
 ("rel-raganfrid-leads-ala-gannha", "char-raganfrid", "leads", "loc-ala-gannha", S["386b"], None, "main", ["M386bi", "M386bf"]),
 ("rel-fordola-leads-crania-lupi", "char-fordola", "leads", "org-crania-lupi", S["391"], None, "main", ["M391c", "M391d"]),
 ("rel-crania-lupi-serves-zenos", "org-crania-lupi", "serves", "char-zenos", S["391"], None, "main", ["M391d", "M391e"]),
 ("rel-crania-lupi-member-of-garlean-empire", "org-crania-lupi", "member-of", "org-garlean-empire", S["391"], None, "main", ["M391a", "M391f"]),
 ("rel-fordola-serves-zenos", "char-fordola", "serves", "char-zenos", S["397"], None, "main", ["M397k", "M397n"]),
 ("rel-arenvald-member-of-scions", "char-arenvald", "member-of", "org-scions", S["397"], None, "main", ["M397c"]),
 ("rel-arenvald-aids-ala-mhigan-resistance", "char-arenvald", "aids", "org-ala-mhigan-resistance", S["397"], None, "main", ["M397b", "M397c"]),
 ("rel-zenos-opposes-ala-mhigan-resistance", "char-zenos", "opposes", "org-ala-mhigan-resistance", S["397"], None, "main", ["M397f", "M397i"]),
 ("rel-zenos-opposes-scions", "char-zenos", "opposes", "org-scions", S["403"], None, "main", ["M403d", "M403g"]),
 ("rel-fordola-opposes-ala-mhigan-resistance", "char-fordola", "opposes", "org-ala-mhigan-resistance", S["403"], None, "main", ["M403f"]),
 ("rel-crania-lupi-opposes-ala-mhigan-resistance", "org-crania-lupi", "opposes", "org-ala-mhigan-resistance", S["406"], None, "main", ["M406d", "M406e"]),
 ("rel-zenos-child-of-varis", "char-zenos", "child-of", "char-varis", S["406"], None, "main", ["M397h", "M406h"]),
 ("rel-zenos-controls-doma", "char-zenos", "controls", "loc-doma", S["406"], None, "main", ["M406g", "M406h"]),
 # The Far East
 ("rel-carvallain-aids-scions", "char-carvallain", "aids", "org-scions", S["407"], S["410"], "main", ["M407d", "M407f"], ["M410a"]),
 ("rel-lolorito-leads-east-aldenard-trading-company", "char-lolorito", "leads", "org-east-aldenard-trading-company", S["410"], None, "main", ["M410c"]),
 ("rel-hancock-member-of-east-aldenard-trading-company", "char-hancock", "member-of", "org-east-aldenard-trading-company", S["410"], None, "main", ["M410c"]),
 ("rel-east-aldenard-trading-company-aids-scions", "org-east-aldenard-trading-company", "aids", "org-scions", S["412"], None, "main", ["M412a", "M412i"]),
 ("rel-confederacy-controls-ruby-sea", "org-confederacy", "controls", "loc-ruby-sea", S["412"], None, "main", ["M412d", "M412e"]),
 ("rel-yotsuyu-controls-doma", "char-yotsuyu", "controls", "loc-doma", S["412"], None, "main", ["M412f"]),
 ("rel-yotsuyu-member-of-garlean-empire", "char-yotsuyu", "member-of", "org-garlean-empire", S["412"], None, "main", ["M412f"]),
 ("rel-yotsuyu-opposes-confederacy", "char-yotsuyu", "opposes", "org-confederacy", S["412"], None, "main", ["M412f"]),
 ("rel-gyodo-opposes-scions", "char-gyodo", "opposes", "org-scions", S["414"], None, "main", ["M414c", "M414k"]),
 ("rel-gyodo-prisoner-of-scions", "char-gyodo", "prisoner-of", "org-scions", S["414"], None, "main", ["M414c", "M414i"]),
 ("rel-soroban-aids-scions", "char-soroban", "aids", "org-scions", S["414"], None, "main", ["M414d", "M414f"]),
 ("rel-soroban-allied-with-east-aldenard-trading-company", "char-soroban", "allied-with", "org-east-aldenard-trading-company", S["414"], None, "main", ["M414e"]),
 ("rel-hien-leads-doman-liberation-front", "char-hien", "leads", "org-doman-liberation-front", S["416"], None, "main", ["M416c", "M416g"]),
 ("rel-yugiri-serves-hien", "char-yugiri", "serves", "char-hien", S["416"], None, "main", ["M416c", "M416d"]),
 ("rel-gosetsu-serves-hien", "char-gosetsu", "serves", "char-hien", S["416"], None, "main", ["M416c", "M416e"]),
 ("rel-yugiri-member-of-doman-liberation-front", "char-yugiri", "member-of", "org-doman-liberation-front", S["416"], None, "main", ["M412k", "M416h"]),
 ("rel-gosetsu-member-of-doman-liberation-front", "char-gosetsu", "member-of", "org-doman-liberation-front", S["416"], None, "main", ["M412k", "M416h"]),
 ("rel-yotsuyu-opposes-hien", "char-yotsuyu", "opposes", "char-hien", S["416"], None, "main", ["M416f"]),
 ("rel-tansui-member-of-confederacy", "char-tansui", "member-of", "org-confederacy", S["417"], None, "main", ["M417d"]),
 ("rel-confederacy-aids-scions", "org-confederacy", "aids", "org-scions", S["418"], None, "main", ["M418c", "M418k"]),
]

# Relationships an earlier era defined, ended here. No end claims: cp-msq-380 is the first step after the 3.56 milestone.
ADJUST = {
 "rel-yugiri-leads-doman-refugees": {"until": S["380"]},   # content_2_1_to_2_3: her people no longer need her (M380r)
}

# ---- Arcs ----------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-h1-envoys-to-the-resistance", "evt-envoys-to-the-resistance", S["380"], S["384"]),
 ("arc-h2-the-east-end-ambush", "evt-the-east-end-ambush", S["385"], S["388"]),
 ("arc-h3-return-to-ala-gannha", "evt-return-to-ala-gannha", S["385b"], S["392"]),
 ("arc-h4-blood-in-rhalgrs-reach", "evt-blood-in-rhalgrs-reach", S["397"], S["406"]),
 ("arc-h5-passage-to-the-far-east", "evt-passage-to-the-far-east", S["407"], S["412"]),
 ("arc-h6-across-the-ruby-sea", "evt-across-the-ruby-sea", S["413"], S["418"]),
]

CASTS = {
 "evt-envoys-to-the-resistance": [
   ("char-lyse", S["380"], ["M380c"]), ("char-alphinaud", S["380"], ["M380b"]), ("char-raubahn", S["380"], ["M380e"]),
   ("org-ala-mhigan-resistance", S["380"], ["M380b"]), ("org-eorzean-alliance", S["380"], ["M380a"]),
   ("char-yshtola", S["380"], ["M380j"]), ("char-conrad", S["382"], ["M382a"]), ("char-krile", S["384"], ["M384g"]),
   ("char-mnaago", S["384"], ["M384f"]), ("char-meffrid", S["384"], ["M384f"]),
 ],
 "evt-the-east-end-ambush": [
   ("char-mnaago", S["385"], ["M385a"]), ("char-alisaie", S["385"], ["M385e"]), ("char-conrad", S["385"], ["M385a"]),
   ("org-ala-mhigan-resistance", S["385"], ["M385a"]), ("char-raubahn", S["386"], ["M386b"]), ("char-pipin", S["386"], ["M386e"]),
   ("char-grynewaht", S["387"], ["M387a"]), ("char-zenos", S["387"], ["M387b"]), ("org-eorzean-alliance", S["387"], ["M387c"]),
 ],
 "evt-return-to-ala-gannha": [
   ("char-meffrid", S["385b"], ["M385ba"]), ("char-lyse", S["385b"], ["M385bb"]), ("loc-ala-gannha", S["385b"], ["M385bb"]),
   ("org-ala-mhigan-resistance", S["385b"], ["M385bd"]), ("char-conrad", S["385b"], ["M385ba"]),
   ("char-raganfrid", S["386b"], ["M386bi"]), ("org-crania-lupi", S["391"], ["M391a"]), ("char-fordola", S["391"], ["M391d"]),
   ("char-zenos", S["391"], ["M391d"]),
 ],
 "evt-blood-in-rhalgrs-reach": [
   ("char-conrad", S["397"], ["M397d"]), ("char-alphinaud", S["397"], ["M397a"]), ("char-arenvald", S["397"], ["M397b"]),
   ("char-zenos", S["397"], ["M397g"]), ("char-fordola", S["397"], ["M397k"]), ("org-ala-mhigan-resistance", S["397"], ["M397c"]),
   ("char-raubahn", S["402"], ["M402f"]), ("char-yshtola", S["402"], ["M402c"]), ("char-meffrid", S["403"], ["M403f"]),
   ("char-lyse", S["403"], ["M403e"]),
 ],
 "evt-passage-to-the-far-east": [
   ("char-alisaie", S["407"], ["M407a"]), ("char-alphinaud", S["407"], ["M407c"]), ("char-krile", S["407"], ["M407b"]),
   ("char-tataru", S["407"], ["M407d"]), ("char-carvallain", S["407"], ["M407e"]), ("char-lyse", S["408"], ["M408a"]),
   ("char-urianger", S["409"], ["M409a"]), ("char-hancock", S["410"], ["M410c"]), ("char-yugiri", S["410"], ["M410b"]),
   ("char-gosetsu", S["410"], ["M410b"]),
 ],
 "evt-across-the-ruby-sea": [
   ("char-alphinaud", S["413"], ["M413a"]), ("char-gosetsu", S["413"], ["M413d"]), ("char-lyse", S["414"], ["M414c"]),
   ("char-alisaie", S["414"], ["M414b"]), ("char-gyodo", S["414"], ["M414a"]), ("char-soroban", S["414"], ["M414e"]),
   ("char-hien", S["416"], ["M416c"]), ("char-yotsuyu", S["416"], ["M416f"]), ("char-yugiri", S["416"], ["M416b"]),
   ("char-tansui", S["417"], ["M417d"]),
 ],
}

ARC_NOTES = {
 "arc-h1-envoys-to-the-resistance": "MSQ #380 *Beyond the Great Wall* to #384 *A Bargain Struck*: Raubahn's request that the Scions win the Resistance (M380b) through the journey to "
   "Rhalgr's Reach and Conrad's acceptance with its caveats (M384a, M384b). It ends where the main scenario splits into the two Gyr Abania chains.",
 "arc-h2-the-east-end-ambush": "MSQ #385 *A Friend of a Friend in Need* to #388 *Let Fill Your Hearts with Pride* (chain A): M'naago's errand to Castrum Oriens (M385a), Pipin's plan and "
   "the East End ambush (M387c), ending on Conrad's \"united Eorzea\" (M388b). Its recaps never mention chain B.",
 "arc-h3-return-to-ala-gannha": "MSQ #385b *A Familiar Face Forgotten* to #392 *Homeward Bound* (chain B, with the #387b/#387c pair): Meffrid's recruiting trip to Lyse's birthplace (M385bb), "
   "the elder's refusal, Wercrata and the Skulls (M391a), ending on the first recruit (M392f). Its recaps never mention chain A, and #387b and #387c do not mention each other.",
 "arc-h4-blood-in-rhalgrs-reach": "MSQ #397 *Where Men Go as One* to #406 *Divide and Conquer*: the chains rejoin, the Reach prepares (the #398 trio, written independently), "
   "the attack (M403b), Meffrid's death and the evacuation, ending on the decision to take the fight to Doma (M406k). The name avoids #403's *In Crimson It Began*.",
 "arc-h5-passage-to-the-far-east": "MSQ #407 *Lies, Damn Lies, and Pirates* to #412 *By the Grace of Lord Lolorito*: finding a ship (M407e), the Doman refugees' account, the voyage and "
   "arrival in Kugane (M409e), and Hancock's briefing on the Ruby Sea (M412d).",
 "arc-h6-across-the-ruby-sea": "MSQ #413 *A Good Samurai Is Hard to Find* to #418 *Boys with Boats*: the search for Gosetsu, Gyodo's betrayal and Soroban (M414e), Gosetsu's release and "
   "Lord Hien's story (M416c), and the Confederacy's terms (M418c). It ends on the era's last step; the next era picks up at #419.",
}

DECISIONS = [
 "**Six arcs (h1–h6)** cover all 39 steps from #380 to #418 without sharing steps; the two Gyr Abania chains get one arc each (h2 for chain A, h3 for chain B).",
 "**Parallel chains:** chain A's events (East End, Grynewaht, Pipin's plan) reach records that chain B also shows only at #397, where both chains are done: Conrad and the Resistance get no new record "
 "inside chain A. Raubahn, Pipin, M'naago, Alisaie and Grynewaht change only on chain A, Lyse, Meffrid, Raganfrid and Ala Gannha only on chain B. Zenos is the exception: he is named at #387 (chain A), "
 "because Fordola names \"Lord Zenos\" at #391 (chain B) and the name must already be visible.",
 "**Zenos** keeps `char-zenos`; \"The Viceroy\" becomes an alias from #387, where Grynewaht names him and Raubahn sends Grynewaht to \"your viceroy\"; #403's Journal confirms the title.",
 "**Doma's acting viceroy** is `char-yotsuyu`, unnamed (\"Doma's acting viceroy\") at #412 and #414, and \"Yotsuyu\" from #416. The \"viceroy's witch\" who holds Doma Castle (#408) is not linked to her, "
 "since the pages do not say so.",
 "**The Skulls** are `org-crania-lupi`: \"The Skulls\" at #391, renamed \"Crania Lupi\" (alias \"The Skulls\") at #406, where Conrad names them.",
 "**Surnames and later names kept out:** Kemp, Aldynn, Tarupin (Pipin's title in the 387/405 Journals), rem Lupis, Hext, yae Galvus, van Baelsar, Lentinus/Lentius. Curtis and Theodoric stay unnamed "
 "(\"her father\", \"the mad king\"), and Yanxia and Othard are left out of displayed text.",
 "**Existing entities are listed in ENTITIES** (same categories) so the module lints alone; it cites only its own claims for the same reason.",
 "**Left out as entities** (named in text only, or not at all): Wercrata, Griseldis, Beves, Ahelissa and the other Reach fighters, Lorelei, the Qiqirn, the Kojin of the Red and Blue, Keiten, Kotokaze, "
 "Hozan and the other Domans of Revenant's Toll, Gyr Abania and Ala Mhigo (already named in accepted text), and Castellum Velodyna.",
]

ALLOW = {}
