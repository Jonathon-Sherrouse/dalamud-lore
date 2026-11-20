"""Atlas content for patches 5.4–5.55, MSQ #682 Reviving the Legacy to #697 On Official Business, and the cp-shb-5-55
milestone (after Death Unto Dawn). Arc tag p. Data only (docs/atlas/era-modules.md is the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes B23–B26, with B22 for the quests just before);
every locator is an exact substring of a quest's Journal, Steps or main dialogue (stage directions inside cutscenes
included). Spoiler rules this module follows:
  - the Shadowbringers cast reuses the conventional IDs the 5.0–5.3 eras create (char-graha-tia, char-fandaniel,
    char-zenos, char-asahi, char-lyse …); each first presentation here stands on its own as of its step;
  - first names and titles only: no "Leveilleur", "Wyrmblood", "Hext", "Garlond", "Scaeva", "Ul Namo"; "the First" stays
    out of text ("another world"), and so does every name the pages only hint at (the Paragon, the dreamer, the
    gateway's tower, the woman's voice);
  - G'raha Tia carries "The Crystal Exarch" as an alias, as the 5.0 reveal leaves him; that alias needs ALLOW "Exarch";
  - Fandaniel is named from #689, where he introduces himself to you; the body he wears is Asahi's (possessed-by).
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

(X682, X683, X684, X685, X686, X687, X688, X689, X690, X691, X692, X693, X694, X695, X696,
 X697) = (f"cp-msq-{n}" for n in range(682, 698))
MS = "cp-shb-5-55"

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #682 Reviving the Legacy
 "M682a": ("G'raha Tia sets off for the Rising Stones, eager to see Cid, a friend you share.", "Reviving the Legacy", "Eager to be reunited with your mutual friend, he sets off for the Rising Stones at a brisk pace"),
 "M682b": ("With the Empire at war with itself, the Alliance turns again to the primal problem and seeks peace with friendly beast tribes.", "Reviving the Legacy", "With the Empire still at war with itself, the Alliance has turned its attention to the primal problem once more. Working with friendly factions among the beast tribes, they hope to explore new avenues for peace"),
 "M682c": ("Krile, back at the Rising Stones, briefs you on the recent Alliance council.", "Reviving the Legacy", "You get back to the Rising Stones to find Krile also returned, and she briefs you on all that transpired at the recent Alliance council."),
 "M682d": ("G'raha and Cid share a brief, joyous reunion.", "Reviving the Legacy", "G'raha Tia positively beams with delight as Cid enters the chamber, and the pair enjoy a brief but joyous reunion."),
 "M682e": ("With a magitek terminal, Cid finds the password to the dead Allagan Owen's report.", "Reviving the Legacy", "Using the calculating power of a magitek terminal, he succeeds in identifying the late Owen's password"),
 "M682f": ("Tempered souls stagnate, and reviving one would only deepen the victim's fanatical faith.", "Reviving the Legacy", "It is duly confirmed that, like those corrupted by Light, the souls of the tempered are subject to stagnation. … one cannot reanimate a tempered soul without also intensifying the victim's fanatical faith"),
 "M682g": ("G'raha theorizes that an adapted memory transference could revive a tempered soul selectively.", "Reviving the Legacy", "G'raha Tia is inspired to theorize that an adapted version of memory transference might make it possible to perform targeted reanimation"),
 "M682h": ("Aymeric pledges Ishgard's full support for the cure and sends you off with all the ceruleum you need.", "Reviving the Legacy", "Upon learning of your quest to cure tempering, he pledges Ishgard's full support, and sees you off aboard an airship laden with all the ceruleum you require and more."),
 "M682i": ("Nero joins the work, claiming he and Cid are destined to unlock travel across dimensions and through time.", "Reviving the Legacy", "I am reliably informed that Garlond and I are destined to unravel the secrets of travel not only across dimensions, but through time."),
 "M682j": ("The terminals give out, but G'raha memorized the magick: a cure for tempering, yet to be proven.", "Reviving the Legacy", "I was able to memorize the magick before it faded. It still needs to be put to the proof, but...I believe we have our cure!"),
 # #683 Forget Us Not
 "M683a": ("Alisaie chooses the kobold Ga Bu as the first to be treated, his symptoms being mild.", "Forget Us Not", "Well, if we're to test it on someone, then I suggest Ga Bu. His symptoms are relatively mild."),
 "M683b": ("Ga Bu stands in silence until someone moves him.", "Forget Us Not", "Still no change, I'm afraid. He just stands there in silence until we move him."),
 "M683c": ("G'raha imbues the familiar Angelo with the treatment.", "Forget Us Not", "I propose to imbue Angelo with the tempering treatment in much the same manner as I did the spirit vessels."),
 "M683d": ("The imbuing needs a great deal of aether.", "Forget Us Not", "the imbuing process will still require no small amount of aether."),
 "M683e": ("Ga Bu comes back to himself by holding to the faces of his family and friends.", "Forget Us Not", "So I tried to focus on their faces. Theirs and yours."),
 "M683f": ("The treatment heals only the soul, not flesh changed by long exposure to a primal.", "Forget Us Not", "Moreover, the treatment's effects are limited to the soul. It offers no succor to those whose very flesh has been altered through prolonged exposure to a primal's influence."),
 "M683g": ("Alphinaud proposes making an army of porxies.", "Forget Us Not", "Then...the next logical step would be to produce a veritable army of porxies, would it not?"),
 "M683h": ("Y'shtola knows an authority on familiars they may grudgingly turn to.", "Forget Us Not", "Yet there ''is'' an authority on familiars to whom we may grudgingly turn."),
 "M683i": ("Alisaie leaves Ga Bu in the Maelstrom's care.", "Forget Us Not", "I have to go now, Ga Bu, but the people here will look after you, all right?"),
 # #684 Like Master, Like Pupil
 "M684a": ("In another world, Y'shtola took the name Matoya and won the forest folk's respect.", "Like Master, Like Pupil", "There, she took on the name of Matoya, and won the respect of all the children of the forest."),
 "M684b": ("Matoya, the realm's foremost authority on familiars, greets you with her usual bite.", "Like Master, Like Pupil", "Master Matoya, the realm's foremost authority on familiars. … you are greeted by the perennially cantankerous Matoya in typically biting fashion."),
 "M684c": ("Matoya proposes a mother porxie to create the porxies.", "Like Master, Like Pupil", "the elderly Archon proposes creating a mother porxie who would in turn create the necessary porxies"),
 "M684d": ("The ingredients lie in Matoya's abandoned workshop in the Makers' Quarter.", "Like Master, Like Pupil", "The place to which Matoya so fondly alluded is soon revealed to be her abandoned workshop in the Makers' Quarter."),
 "M684e": ("The tamed mother porxie gives birth to three Angelos.", "Like Master, Like Pupil", "to three bouncing baby Angelos, as all look on approvingly."),
 "M684f": ("Making porxies is still hard work, but far more manageable.", "Like Master, Like Pupil", "Though it will still be hard work to create the porxies, the process has been made a great deal more manageable"),
 "M684g": ("Alphinaud means the porxies to go first to Limsa Lominsa.", "Like Master, Like Pupil", "I believe our friends in Limsa Lominsa should be the first beneficiaries."),
 "M684h": ("G'raha Tia is proud to call himself a Scion.", "Like Master, Like Pupil", "G'raha Tia is my name, and I am proud to call myself a Scion."),
 "M684i": ("Only G'raha, of royal blood, can imbue a familiar with the cure's magick.", "Like Master, Like Pupil", "Being the only one possessed of royal blood, I alone can imbue the subject with the necessary magick."),
 # #685 The Admiral's Resolve
 "M685a": ("The Bloody Executioners' captain, Hyllfyr, has long been bedridden with a lung ailment.", "The Admiral's Resolve", "I am given to understand that their leader, Captain Hyllfyr, has been bedridden for some while with an ailment of the lungs."),
 "M685b": ("In Hyllfyr's absence his right hand, Sicard, leads the Executioners.", "The Admiral's Resolve", "In his absence, his right hand leads, a man named Sicard but recently risen to prominence among their ranks."),
 "M685c": ("Lominsans have been at odds with their island neighbors for some seven centuries.", "The Admiral's Resolve", "Since our ancestors came to these shores some seven centuries past, we Lominsans have been at odds with those who share our island home."),
 "M685d": ("The Bloody Executioners would not hear of Merlwyb's approach to a kobold patriarch, and their absence sent a message.", "The Admiral's Resolve", "Acting through a friendly faction among the kobolds, we had intended to seek an audience with a prominent patriarch. … But the Bloody Executioners would not hear of it, and their absence sent a message to the rest."),
 "M685e": ("The Executioners' fortunes rose after Sicard's promotion.", "The Admiral's Resolve", "save that the Bloody Executioners experienced a marked improvement in their fortunes after his promotion."),
 "M685f": ("Sicard is said to have bought his place at Hyllfyr's side with clever coin.", "The Admiral's Resolve", "Found some clever way to make coin, they say, an' traded it fer Moenskaet's place at ol 'Hyllfyr's side."),
 "M685g": ("Crystal prices fell just as the Executioners prospered.", "The Admiral's Resolve", "just as the Executioners began to enjoy better fortunes, the price of crystal went into sharp decline"),
 "M685h": ("Titan and Leviathan have not appeared of late.", "The Admiral's Resolve", "neither Titan nor Leviathan have made an appearance of late, suggesting the kobolds and Sahagin lack the means with which to summon them."),
 "M685i": ("Alisaie vows to learn what Sicard wants.", "The Admiral's Resolve", "We have a nose for the truth. Whatever this Sicard wants, we'll find out."),
 # #686 The Search for Sicard
 "M686a": ("Alphinaud means to pose as a buyer to trace the crystals.", "The Search for Sicard", "After asking around, I was able to gain an introduction, and will shortly pose as a potential buyer, in a bid to establish the crystals' provenance."),
 "M686b": ("G'raha takes the buyer's part, since the merchant would be wary of the Admiral's allies.", "The Search for Sicard", "If he truly is in league with the Bloody Executioners, he will surely be wary of those allied to the Admiral─the Scions not least of all."),
 "M686c": ("The crystals were taken from the kobolds of O'Ghomoro.", "The Search for Sicard", "O'Ghomoro. Taken from the kobolds, just as we suspected."),
 "M686d": ("Sicard names himself acting captain of the Bloody Executioners.", "The Search for Sicard", "I'm Sicard, actin' captain of the Bloody Executioners."),
 "M686e": ("Sicard argues that the law forbids attacks on non-imperial ships but says nothing of beastmen.", "The Search for Sicard", "The law forbids us from attackin' any vessel not flyin' the imperial flag, but it don't say ''nothin' ''about beastmen."),
 "M686f": ("Sicard says the Executioners follow in the Scions' footsteps, keeping beastmen from summoning their gods.", "The Search for Sicard", "And now we're followin' in your footsteps, makin' sure the beastmen never summon their stinkin' gods again."),
 "M686g": ("Sicard agrees to meet the Admiral aboard the Astalicia.", "The Search for Sicard", "I'll even provide the venue—the ''Astalicia''."),
 # #687 On Rough Seas
 "M687a": ("Sicard tells the Admiral that Limsa is a nation of pirates and always will be.", "On Rough Seas", "Ours is a nation of pirates. Always has been, always will be."),
 "M687b": ("Merlwyb says Limsa's ancestors turned to piracy because kobolds held the land.", "On Rough Seas", "Finding the land occupied by kobolds, however, they were forced to turn to piracy in order to survive."),
 "M687c": ("Merlwyb says the Empire teeters on the brink of collapse.", "On Rough Seas", "The empire teeters on the brink of collapse."),
 "M687d": ("Merlwyb accepts Sicard's challenge to a duel.", "On Rough Seas", "Very well. As Admiral of Limsa Lominsa, I accept your challenge."),
 "M687e": ("Merlwyb shoots through Sicard's right knee.", "On Rough Seas", "she successfully shoots through Sicard's right knee."),
 "M687f": ("Captain Hyllfyr tells his crew that the Admiral decides where they sail.", "On Rough Seas", "At the helm o' that ship is the Admiral, an' tis ''she'' who decides where we sail."),
 "M687g": ("Hyllfyr says it will not be long before he takes his rest in the depths.", "On Rough Seas", "Mistbeard's vanished into legend, an' it won't be long afore I take my rest in the depths."),
 "M687h": ("With the Executioners at peace with her, Merlwyb turns to her neighbors.", "On Rough Seas", "All that remains is to do likewise with our neighbors."),
 # #688 The Great Ship Vylbrand
 "M688a": ("Merlwyb would have the kobolds' leader freed from Titan's influence.", "The Great Ship Vylbrand", "And so, in the meeting we seek to arrange with the kobolds, I would have you free their leader of Titan's influence."),
 "M688b": ("Fifty years ago Limsa made an ambiguous covenant with the kobolds, and used it to claim land they believed theirs.", "The Great Ship Vylbrand", "Some fifty years past, when the Sahagin swarmed at our hulls in ever greater numbers, Limsa entered into a covenant with the kobolds. … And we took advantage of it, moving in to claim the northern reaches of La Noscea—which the kobolds believed theirs."),
 "M688c": ("Merlwyb offers herself and the stolen crystals as bait to draw out the patriarch.", "The Great Ship Vylbrand", "proposes using herself and the beastmen's stolen crystals as bait to draw him out"),
 "M688d": ("Ga Bu wants to speak to his leader and join the mission.", "The Great Ship Vylbrand", "The young kobold apparently has something important he wishes to say to his leader, and wants to join you on your mission."),
 "M688e": ("When Merlwyb announces herself, Za Da tries to summon Titan.", "The Great Ship Vylbrand", "no sooner does Merlwyb announce herself to Za Da than he attempts to summon Titan"),
 "M688f": ("Alisaie's treatment takes effect, and Za Da awakens.", "The Great Ship Vylbrand", "After what feels like an eternity, the treatment takes effect, and Za Da awakens from his reverie even as his guards flee in terror."),
 "M688g": ("Alisaie tells Za Da that he sacrificed his own people to summon Titan.", "The Great Ship Vylbrand", "I'm sorry... but they died by your hand. You sacrificed them to summon Titan."),
 "M688h": ("Ga Bu tells Za Da that the Great Father is false and only hurts them.", "The Great Ship Vylbrand", "The Great Father we have been summoning is false. He only hurts us and those we love."),
 "M688i": ("Za Da is convinced to give peace a chance: Limsa's first step toward lasting peace with the kobolds.", "The Great Ship Vylbrand", "the patriarch is eventually convinced to give peace a chance. Thus is it that, after centuries of bloodshed, Limsa Lominsa takes its first tentative step on the road to lasting peace with the kobolds."),
 "M688j": ("The peace extends only to the Second Order, but Merlwyb means to bring every kobold in.", "The Great Ship Vylbrand", "Though the fledgling peace only extends to the Second Order for the present, the Admiral is determined to bring every kobold into the fold, however long it takes."),
 "M688k": ("Za Da does not trust Merlwyb yet, but trusts Ga Bu.", "The Great Ship Vylbrand", "I do not trust you. Not yet. But Ga Bu does. And I will trust him."),
 "M688l": ("Merlwyb passed judgment on her own father with her pistol after he fell thrall to Leviathan.", "The Great Ship Vylbrand", "That is Death Penalty. The pistol I used to pass judgment on my own sire when fell thrall to Leviathan and betrayed his comrades."),
 # #689 Futures Rewritten
 "M689a": ("Towers, apparently of Garlean design, have appeared across the realm.", "Futures Rewritten", "It seems that many more such structures─apparently of Garlean design─have materialized across the realm."),
 "M689b": ("Merlwyb sends you to join the Alliance forces on the eastern front.", "Futures Rewritten", "Merlwyb bids you join the Alliance forces on the eastern front"),
 "M689c": ("Lyse welcomes you to Ala Mhigo just as a great dragon passes overhead.", "Futures Rewritten", "Lyse has scarcely finished welcoming you when an enormous dragon passes overhead"),
 "M689d": ("In the Royal Menagerie you face Asahi, or rather an Ascian in his body, who names himself Fandaniel.", "Futures Rewritten", "you come face-to-face with Asahi...or rather an Ascian in his body. With a self-indulgent flourish, your foe introduces himself as Fandaniel"),
 "M689e": ("Fandaniel means to destroy the world in a recreation of the Final Days, with the towers playing some part.", "Futures Rewritten", "declares his intent to destroy the world in a recreation of the Final Days, in which the towers will play some unspecified part"),
 "M689f": ("Fandaniel's dragon, Lunar Bahamut, sets the rooftop garden ablaze.", "Futures Rewritten", "his dragon─the so-called “Lunar Bahamut”─sets the rooftop garden ablaze"),
 "M689g": ("Fandaniel says his patron, Lord Zenos, awaits you at the heart of the chaos.", "Futures Rewritten", "his patron, Lord Zenos, awaits you at the heart of the chaos"),
 "M689h": ("Fandaniel says Elidibus disagreed with him, and that thanks to you he is free of him.", "Futures Rewritten", "Admittedly, Elidibus was not convinced by that argument. But thanks to you, I'm finally free of his incessant nagging!"),
 "M689i": ("Fandaniel names his band the Telophoroi.", "Futures Rewritten", "We, the Telophoroi, shall be your performers, and this very star our stage!"),
 "M689j": ("Fandaniel says he wants to die and take everyone with him.", "Futures Rewritten", "And I want to die too! Oh yes, I want to die and take everyone with me in a paroxysm of pain and suffering!"),
 "M689k": ("Lyse proposes sending a unit to investigate the nearby tower.", "Futures Rewritten", "Lyse proposes sending a unit to investigate the nearby tower"),
 "M689l": ("Y'shtola delivered the first porxies to the Immortal Flames in Ul'dah.", "Futures Rewritten", "Y'shtola delivered the first litter of porxies to the Immortal Flames in Ul'dah"),
 "M689m": ("Towers have been sighted even in Yanxia, and Krile and Tataru set out to seek Estinien's aid.", "Futures Rewritten", "Krile investigated reports that towers had been sighted not only across Eorzea, but in Yanxia in the Far East. … Krile and Tataru declare their intention to seek the aid of Estinien"),
 "M689n": ("The Amalj'aa say some of their kind have been abducted by men.", "Futures Rewritten", "The Amalj'aa claim that a number of their kind have been abducted...and that men are responsible."),
 "M689o": ("G'raha thinks the dragon some simulacrum born of Ascian magicks.", "Futures Rewritten", "I think it more probable that it is some manner of simulacrum born of Ascian magicks."),
 "M689p": ("Zenos, rising from the imperial throne, seeks a new weapon worthy of his reunion with you, and breaks his katana.", "Futures Rewritten", "Zenos gets up from the throne. … I must find myself a new weapon. One worthy of our long-awaited reunion. … Zenos discards his katana and walks over it, breaking it in half."),
 "M689q": ("Zenos cares only that his friend returns to him.", "Futures Rewritten", "So long as my friend returns to me, fangs bared and claws sharpened, I care not."),
 # #690 Unto the Breach
 "M690a": ("Thancred returns from the imperial capital with strange tidings.", "Unto the Breach", "His reconnaissance mission complete, Thancred makes his long-awaited return to the Rising Stones bearing strange tidings from the imperial capital."),
 "M690b": ("Garlemald's capital lies in deathly silence, save the imperial palace.", "Unto the Breach", "You see, the capital has been plunged into a deathly silence, with one exception: the imperial palace."),
 "M690c": ("The palace's builders work as if possessed or tempered.", "Unto the Breach", "It was as if they were possessed...or tempered."),
 "M690d": ("Resistance scouts sent to a tower tried to murder their comrades, tempered into servants of Garlemald.", "Unto the Breach", "Resistance scouts sent to investigate the tower that had recently appeared nearby subsequently attempted to murder their comrades, having apparently been turned into fanatical servants of Garlemald"),
 "M690e": ("Urianger notes that these souls were tempered to a nation.", "Unto the Breach", "Yet these hapless souls were compelled to accept a ''nation'' as the object of their devotion."),
 "M690f": ("Aymeric's scouts saw black-garbed figures leading shackled Ixal toward the tower in Dravania.", "Unto the Breach", "Our scouts sighted black-garbed figures leading shackled Ixal in the direction of the tower in Dravania."),
 "M690g": ("Nanamo believes Fandaniel, with Zenos's support, has rallied part of the splintered Garlean army to the Telophoroi.", "Unto the Breach", "With the support of Zenos, it seems likely that Fandaniel has rallied a faction of the splintered Garlean army to the banner of the Telophoroi."),
 "M690h": ("Raubahn shelves the plan to march on Garlemald.", "Unto the Breach", "The plan had been to march on Garlemald from the east and west in order to force a peace treaty, but the situation has changed."),
 "M690i": ("Raubahn sends Arenvald and Fordola, both immune to tempering, to the tower.", "Unto the Breach", "Raubahn reveals his intention to send a second party to the tower in the form of Arenvald and Fordola, both of whom are immune to the effects of tempering"),
 "M690j": ("Fordola fought and killed for Garlemald, and needs to know what she was part of.", "Unto the Breach", "I fought for Garlemald. Killed for Garlemald. What was I a part of? I need to know."),
 "M690k": ("Despite Alphinaud's warnings, Arenvald is set on joining the mission to the tower in Paglth'an.", "Unto the Breach", "Despite Alphinaud's warnings, Arenvald expresses his determination to participate in the mission. While he and Fordola investigate the tower in Paglth'an"),
 "M690l": ("Tataru reports that Estinien left for Ishgard on hearing of the elder primal's return, and you give chase.", "Unto the Breach", "she and Krile recently succeeded in catching up with Estinien, though he departed for Ishgard as soon as they informed him of the reappearance of the elder primal. … you decide to give chase in the hope of enlisting his help."),
 # #691 Here Be Dragons
 "M691a": ("Lucia says Estinien comes and goes as he pleases.", "Here Be Dragons", "We were not aware Ser Estinien had returned to Ishgard, but as I expect you remember, he is wont to come and go as he pleases."),
 "M691b": ("G'raha hails Estinien as the dragoon who felled Nidhogg at your side.", "Here Be Dragons", "He who fought and felled the dread wyrm Nidhogg at the Warrior of Light's side!"),
 "M691c": ("Tiamat, Bahamut's mate, remains imprisoned on Azys Lla, bound most by her remorse.", "Here Be Dragons", "Aye, Tiamat, his mate. Even now, she remains imprisoned on Azys Lla, though her remorse binds her faster than any shackle."),
 "M691d": ("Alphinaud proposes going to Azys Lla together.", "Here Be Dragons", "Might I suggest that we make the journey to Azys Lla together?"),
 "M691e": ("Estinien came to Azys Lla concerned that Tiamat had been forced to summon Bahamut.", "Here Be Dragons", "Then your original reason for coming here was out of ''concern'' that Tiamat had been forced to summon Bahamut."),
 "M691h": ("Tiamat told Estinien her hatred for humankind was extinguished long ago.", "Here Be Dragons", "My hatred for your kind was extinguished long ago."),
 "M691f": ("Tiamat's guilt for resurrecting Bahamut still torments her.", "Here Be Dragons", "But the guilt she feels for resurrecting Bahamut burns on undimmed. It ''torments'' her, even now."),
 "M691g": ("In Nidhogg's absence, Estinien watches over Tiamat.", "Here Be Dragons", "In his absence, it falls to me to watch over her."),
 # #692 Righteous Indignation
 "M692a": ("The eikon claimed the souls of Tiamat's kin, who became tools for the Allagans.", "Righteous Indignation", "The eikon claimed their souls when first he manifested. And robbed of their will, they became tools for the Allagans' dark designs."),
 "M692b": ("Tiamat says the dragons of Meracydia are at the mercy of an Ascian.", "Righteous Indignation", "The dragons of Meracydia are at the mercy of this Ascian. There can be no other explanation."),
 "M692c": ("Tiamat fears losing herself to the eikon's influence.", "Righteous Indignation", "Were I to lose myself to the eikon's influence, all would pay the price."),
 "M692d": ("G'raha calls Tiamat a special case for the porxie cure.", "Righteous Indignation", "While porxies have been shown to be effective in curing the tempered, Tiamat must be considered a special case."),
 "M692e": ("The Flagship's nodes recognize G'raha's royal blood.", "Righteous Indignation", "the nodes here granted access to restricted functions, having identified me as being of royal blood."),
 "M692f": ("Tiamat's restraints need an update from a terminal in the Flagship.", "Righteous Indignation", "This issue can be resolved by applying a system update using the corresponding terminal located within the Flagship."),
 # #693 For Vengeance
 "M693a": ("Alphinaud must stay behind to work the terminal.", "For Vengeance", "It does, however, require that I remain here to operate the terminal."),
 "M693b": ("Tiamat says the men of Allag slew her beloved, and in grief she heeded the Ascians.", "For Vengeance", "For the men of Allag slew my beloved, and I, in my rage and sorrow, heeded the envenomed words of the Ascians..."),
 "M693c": ("Alisaie frees Tiamat from Bahamut's influence.", "For Vengeance", "Drawing deeply upon both your and G'raha Tia's reserves of aether, Alisaie succeeds at last in freeing Tiamat from Bahamut's malign influence."),
 "M693d": ("The treatment cannot save the Allagans' other captives, whose flesh was altered.", "For Vengeance", "Many have been subjected to the Allagans' dark arts, their flesh irrevocably altered. For such tortured souls, I fear there can be no salvation."),
 "M693e": ("Urianger reports Lunar Bahamut leading a host, dragons among it, toward Paglth'an.", "For Vengeance", "Bahamut has been sighted leading a host─including dragons─in the direction of Paglth'an."),
 "M693f": ("Tiamat takes to the sky with Estinien on her back, determined to atone.", "For Vengeance", "Determined to atone for past sins, Tiamat immediately takes to the sky with Estinien on her back"),
 "M693g": ("G'raha counsels waiting for the other Scions before battle.", "For Vengeance", "G'raha Tia counsels you to wait for your fellow Scions to assemble before going into battle."),
 # #694 The Flames of War
 "M694a": ("The Immortal Flames have joined the Amalj'aa in defending Paglth'an.", "The Flames of War", "Shortly after your arrival, you are met by Nanamo, who reveals that the Immortal Flames have joined the Amalj'aa in the defense of Paglth'an."),
 "M694b": ("The Syndicate voted to a member for intervention.", "The Flames of War", "All that was required was the agreement of the Syndicate—each of whom voted in favor of intervention."),
 "M694c": ("The defenders face an imperial legion and Lunar Bahamut's draconic horde.", "The Flames of War", "For we face not only the might of an imperial legion, but Lunar Bahamut and his draconic horde besides."),
 "M694d": ("None of the Amalj'aa show signs of tempering despite Lunar Bahamut's nearness.", "The Flames of War", "Our forces report that despite their proximity to Lunar Bahamut, none of the Amalj'aa show any signs of tempering."),
 "M694e": ("Tiamat sends one of her children to carry you to the eikon.", "The Flames of War", "The eikon waiteth in the heavens! My child shall bear thee to him!"),
 "M694f": ("Lunar Bahamut is no more, and the Telophoroi's attempt on Paglth'an ends in defeat.", "The Flames of War", "Now Lunar Bahamut is no more, and the Telophoroi's attempt to conquer Paglth'an has ended in defeat, leaving their routed forces to flee for their lives."),
 "M694g": ("The Amalj'aa war chief declares an end to the war with Ul'dah.", "The Flames of War", "Long have our peoples waged war, but no more."),
 "M694h": ("Tiamat vows the dragons of Meracydia will never again heed the Ascians.", "The Flames of War", "Never again shall the dragons of Meracydia hearken to the lies of the Ascians. This I vow."),
 "M694i": ("Inside the tower, Arenvald and Fordola find unconscious Amalj'aa fused to its walls.", "The Flames of War", "Arenvald sees that several unconscious Amalj'aa are fused to the tower walls, one per cell."),
 "M694j": ("The cells summon Lunar Ifrit, which lunges at Fordola, and Arenvald jumps in front of her.", "The Flames of War", "All of the Amalj'aa cells glow, summoning a monster, Lunar Ifrit. It lunges to attack Fordola. … Arenvald jumps in front of Fordola, facing Lunar Ifrit."),
 "M694k": ("Alphinaud is anxious to learn whether Arenvald has returned.", "The Flames of War", "Alphinaud explains that he is anxious to learn whether Arenvald has returned from his reconnaissance mission to the tower at Paglth'an."),
 # #695 When the Dust Settles
 "M695a": ("Nanamo tells you a friend has been gravely wounded.", "When the Dust Settles", "Upon disembarking at the airship landing, you are met by Nanamo, who reveals that one of your friends has been gravely wounded."),
 "M695b": ("The chirurgeons have done what they can for Arenvald; his fate hangs in the balance.", "When the Dust Settles", "At the Phrontistery, you are told that the chirurgeons have done all they can for your comrade, but that his fate yet hangs in the balance."),
 "M695c": ("Fordola lashes out at Alphinaud's idealism, and Estinien answers that such idealists are remembered as heroes.", "When the Dust Settles", "she lashes out at him, condemning his idealism as naivety. At this, Estinien interjects that those who uphold such ideals are the ones remembered as heroes."),
 "M695d": ("A creature like Ifrit waited in the tower, and more have been sighted near other towers.", "When the Dust Settles", "a creature resembling Ifrit was waiting for them inside the tower, and that further such entities have been sighted in the vicinity of other towers across the realm."),
 "M695e": ("Urianger is all but certain the towers summon primals through those imprisoned inside.", "When the Dust Settles", "'Tis now all but certain that the towers were conceived to facilitate the summoning of primals by those imprisoned within."),
 "M695f": ("The towers resemble a much larger structure Thancred and Urianger saw in Garlemald's capital.", "When the Dust Settles", "the towers bear a striking resemblance to a much larger structure which Urianger and I observed from afar during our visit to the imperial capital."),
 "M695g": ("Nanamo leaves the primals to the Grand Companies, calling on the Scions only as a last resort.", "When the Dust Settles", "Nanamo assures you that the Grand Companies are ready to deal with the threat … we would call upon the Scions only as a last resort."),
 "M695h": ("The Amalj'aa have pledged their full support to the Alliance.", "When the Dust Settles", "our talks with the Amalj'aa have reached an agreeable conclusion. They have pledged their full support to our cause."),
 "M695i": ("Krile leaves for Sharlayan to seek the Forum's help in uncovering the Telophoroi's motives.", "When the Dust Settles", "Krile announces her intention to depart for Sharlayan to petition the Forum's aid in uncovering the Telophoroi's true motives"),
 "M695j": ("Y'shtola can tell that Hydaelyn has made her will known to no one.", "When the Dust Settles", "as far as I am able to tell, Hydaelyn has not made Her will known to anyone."),
 "M695k": ("Krile asks Estinien again to join the cause, and he accepts.", "When the Dust Settles", "she turns at last to Estinien, and invites him once more to join the cause. And, perhaps most surprisingly of all, he accepts."),
 "M695l": ("Fandaniel admits Tiamat's return makes more Meracydian dragons hard to procure.", "When the Dust Settles", "the chances of us being able to procure any more Meracydian dragons are rather slimmer following Tiamat's reappearance."),
 "M695m": ("Zenos says the nation forged for Ascian ends will soon prove its worth.", "When the Dust Settles", "The hour draws nigh. This nation, forged for Ascian ends, will finally prove its worth."),
 "M695n": ("Fandaniel calls the Empire an instrument of the star's destruction.", "When the Dust Settles", "A mighty Empire, now no more than an instrument of this star's destruction!"),
 # #696 The Company We Keep
 "M696a": ("The Alliance summons the Scions to a council in Ala Mhigo, with the beast tribes invited too.", "The Company We Keep", "In addition to the usual Alliance representatives, delegates from the various beast tribes have been invited to attend, in the hope that all the peoples of Eorzea might unite under a single banner."),
 "M696b": ("The Alliance and the beast tribes unite against the Telophoroi as the Grand Company of Eorzea, Alphinaud's long dream.", "The Company We Keep", "with the Alliance and the beast tribes agreeing to set aside their differences and join forces against their common foe, the Telophoroi. The talks culminate in the founding of the Grand Company of Eorzea, a dream long nurtured by Alphinaud in particular."),
 "M696c": ("Za Da says the kobolds now look to the future as allies.", "The Company We Keep", "But today we look to the future, as allies united in purpose."),
 "M696d": ("Kan-E-Senna offers the Ixal the Scions' means of freeing the tempered.", "The Company We Keep", "As Patriarch Za Da will attest, the Scions have granted us a means to free your brethren from their thralldom."),
 "M696e": ("Za Da says a summoning needs both prayer and aether.", "The Company We Keep", "Both prayer and aether are needed for the ritual. Should either one be denied, the summoning would fail!"),
 "M696f": ("Alphinaud means to find the source of the aether the summonings depend on.", "The Company We Keep", "And so we must endeavor to discover the source of the aether on which the process depends."),
 "M696g": ("Alphinaud means to draft a proposal from his time as the Crystal Braves' commander, so the new company avoids their fate.", "The Company We Keep", "Alphinaud also wishes to take this opportunity to draft a proposal based on his experiences as commander of the Crystal Braves, and offer it to the Grand Company of Eorzea that it may avoid a similar fate."),
 "M696h": ("Alisaie and G'raha volunteer to seek out the Braves who abandoned the cause.", "The Company We Keep", "So Alisaie and G'raha volunteer to seek out said individuals"),
 "M696i": ("Riol and Alianne are former Crystal Braves who now serve as Scions.", "The Company We Keep", "At Castrum Oriens, you meet with Riol and Alianne, former Crystal Braves who now serve as Scions."),
 "M696j": ("Riol says many Braves joined for coin or glory, and Tataru kept such people out of the Scions.", "The Company We Keep", "For every swab who signed up with good intentions, there was another who was only in it for the coin, the glory, or both. … 'Cause Tataru sifted out all the glory-hunters 'fore they made it through the door!"),
 "M696k": ("Kan-E-Senna asks you to visit the sylphs of the Ashcrown Consortium, whose counsel will serve the coalition.", "The Company We Keep", "Kan-E-Senna, who requests that you visit the sylphs of the Ashcrown Consortium. As traders in crystal, they are well versed in negotiating with the many and varied peoples of Eorzea"),
 "M696l": ("Aymeric tells the council that together there is nothing they cannot overcome.", "The Company We Keep", "And together, there is nothing in creation we cannot overcome."),
 # #697 On Official Business
 "M697a": ("Fourchenault comes to Gridania as the Forum's representative.", "On Official Business", "here in my capacity as representative of the Forum."),
 "M697b": ("Fourchenault is glad to be reunited with his children, Alphinaud and Alisaie.", "On Official Business", "Alphinaud and Alisaie walk toward Fourchenault. … Circumstances apart, I am grateful that our meeting has afforded me the chance to be reunited with my children at long last."),
 "M697c": ("Fourchenault's father was Louisoix, whose efforts before the Calamity gave Eorzea a means to vanquish the primals.", "On Official Business", "my father, Louisoix … In the days prior to the Seventh Umbral Calamity, it was your father's tireless efforts which granted us a means to vanquish the primals."),
 "M697d": ("Fourchenault opposed his father's decision to intervene, and still does.", "On Official Business", "I must confess, however, that I opposed his decision to intervene. … And my position remains unchanged."),
 "M697e": ("Sharlayan will not intervene in the war between Eorzea and the Empire.", "On Official Business", "Sharlayan will under no circumstances intervene in the conflict between Eorzea and the Garlean Empire."),
 "M697f": ("Fourchenault dismisses the Final Days: were they coming, the Forum would know.", "On Official Business", "If the Final Days were truly upon us, we would know."),
 "M697g": ("Fourchenault strips Alphinaud and Alisaie of the family name.", "On Official Business", "Alphinaud, Alisaie. As of this moment, you shall no longer bear the name of"),
 "M697h": ("Kan-E-Senna: the Forum has refused, and the Alliance must face the Telophoroi alone.", "On Official Business", "The Forum has refused our request for aid, and it falls to us alone to contend with the Telophoroi."),
 "M697i": ("The Forum has forbidden anyone to cooperate with Krile.", "On Official Business", "it appears the Forum has forbidden anyone from cooperating with us."),
 "M697j": ("G'raha wonders if the Forum hides something, and Krile senses it is not as unconcerned as it claims.", "On Official Business", "Could it be that they are hiding something from us? … something tells me they are not as unconcerned about the Telophoroi as they claim."),
 "M697k": ("Krile asks the Scions to join her in Sharlayan when the time is right.", "On Official Business", "To that end, I would like you all to join me here—when the time is right, of course."),
 # #698 Death Unto Dawn (counts from the cp-shb-5-55 milestone)
 "M698a": ("The Telophoroi march through the Ixal's homeland toward the Carteneau Flats, and Kan-E-Senna sends the Twin Adders.", "Death Unto Dawn", "It would seem the Telophoroi have marched straight through the Ixal's homeland, scattering all before them, on their way to the Carteneau Flats. Wasting no time, the Elder Seedseer orders the Twin Adders to ready their airships"),
 "M698b": ("Fordola brings Arenvald, now in a wheelchair from his wounds in the tower, to see Alphinaud.", "Death Unto Dawn", "whom Fordola has brought all the way from Ul'dah in the hope of speaking with Alphinaud. … the youth is now confined to a wheelchair due to the injuries he sustained in the tower at Paglth'an."),
 "M698c": ("Arenvald asks Alphinaud to fight in his stead and be the hero he cannot.", "Death Unto Dawn", "he asks Alphinaud to fight on in his stead and be the hero that he cannot."),
 "M698d": ("The Telophoroi, with tempered beastmen and lunar primals, seek an aetherial confluence deep underground.", "Death Unto Dawn", "Their numbers bolstered by tempered beastmen and lunar primals, the legions of the Telophoroi test the newly forged Grand Company of Eorzea to its breaking point. … the enemy have set their sights on an aetherial confluence buried deep beneath the ground, though their true designs remain a mystery."),
 "M698e": ("You drive the Telophoroi from their prize, and the Grand Company of Eorzea emerges unbroken.", "Death Unto Dawn", "succeed at length in driving the Telophoroi hordes from their prize. … the fact remains that when tested, the Grand Company of Eorzea emerged unbroken"),
 "M698f": ("Fandaniel says your victory has earned you only a stay of execution.", "Death Unto Dawn", "he declares that while the day may be yours, your efforts have earned you no more than a brief stay of execution"),
 "M698g": ("Aymeric asks the Scions to find a means to neutralize the towers.", "Death Unto Dawn", "Lord Aymeric requests that the Scions search instead for a means to neutralize the threat of the towers."),
 "M698h": ("The answer is likely in Sharlayan, but you must wait for Krile to win you entry.", "Death Unto Dawn", "it is agreed that the solution will most likely be found there … you will not be able to confirm your suspicions until Krile has obtained permission for you all to set foot in the infamously insular nation"),
 "M698i": ("The towers are draining the lifeblood of the land itself.", "Death Unto Dawn", "learn to your dismay that they are draining the lifeblood of the land itself."),
 "M698j": ("A voice warns you alone that the end draws nigh and the star's fate is in your hands.", "Death Unto Dawn", "you hear an ephemeral voice call out to you and you alone... … It warns that the end draws nigh...and that the fate of the star is in your hands."),
 "M698k": ("Fandaniel's plan to redirect Carteneau's aether failed, and he means to draw it closer to home.", "Death Unto Dawn", "My plan to redirect the aether from Carteneau came to a rather less-than-satisfactory conclusion. … The obvious solution would be to draw on resources a little closer to home"),
 "M698l": ("Zenos has taken up a scythe as his new weapon.", "Death Unto Dawn", "It is revealed that he has chosen a scythe as a new weapon"),
 "M698m": ("Zenos awaits a final contest with you.", "Death Unto Dawn", "And the stars shall bear witness to our final contest."),
 "M698n": ("A vast tower has been built atop the imperial palace, and Fandaniel calls the gateway complete.", "Death Unto Dawn", "With the “gateway of the gods” complete, all that remains is to gather the necessary aether, and our prize shall be within reach! … that has been constructed on top of the imperial palace."),
}

# ---- Entities ----------------------------------------------------------------------------------------------------
ENTITIES = {
 # recurring from earlier eras (same id and category merge)
 "char-alphinaud": "character", "char-alisaie": "character", "char-yshtola": "character", "char-thancred": "character",
 "char-urianger": "character", "char-tataru": "character", "char-cid": "character", "char-krile": "character",
 "char-matoya": "character", "char-ga-bu": "character", "char-lyse": "character", "char-zenos": "character",
 "char-asahi": "character", "char-raubahn": "character", "char-nanamo": "character", "char-estinien": "character",
 "char-merlwyb": "character", "char-aymeric": "character", "char-kan-e-senna": "character", "char-nero": "character",
 "char-tiamat": "character", "char-titan": "character", "char-arenvald": "character", "char-fordola": "character",
 "char-alianne": "character", "char-louisoix": "character", "char-hydaelyn": "character",
 "org-scions": "organization", "org-eorzean-alliance": "organization", "org-garlean-empire": "organization",
 "org-immortal-flames": "organization", "org-crystal-braves": "organization", "org-ixal": "organization",
 # the Shadowbringers cast (the 5.0–5.3 eras may also define these, under the same ids)
 "char-graha-tia": "character", "char-fandaniel": "character",
 # new in 5.4–5.55
 "char-sicard": "character", "char-hyllfyr": "character", "org-bloody-executioners": "organization",
 "char-za-da": "character", "org-kobolds": "organization", "org-amaljaa": "organization",
 "org-telophoroi": "organization", "char-lunar-bahamut": "character", "org-grand-company-of-eorzea": "organization",
 "char-fourchenault": "character",
 "evt-the-tempering-cure": "event", "evt-the-admirals-peace": "event", "evt-the-towers-rise": "event",
 "evt-tiamats-atonement": "event", "evt-one-banner-for-eorzea": "event",
}

EX = ["The Crystal Exarch"]  # G'raha Tia's alias since the 5.0 reveal (needs ALLOW "Exarch")

# ---- Presentations ---------------------------------------------------------------------------------------------------
PRES = {
 # -- the cure for tempering
 "char-graha-tia": [
   P(X682, None, "main", "G'raha Tia",
     "A Scion back in his own body, who brought an Allagan node to Cid, a friend he was eager to see again. When Owen's recovered report showed that reviving a tempered soul only deepens its faith, "
     "he conceived an adapted memory transference. The terminals gave out, but he memorized the magick: a cure for tempering, not yet proven.",
     ["M682a", "M682d", "M682f", "M682g", "M682j"], EX),
   P(X683, None, "main", "G'raha Tia",
     "A Scion who devised the cure for tempering and imbued it in the familiar Angelo, drawing aether from his friends. It brought Ga Bu back to himself, "
     "but G'raha warns that it heals only the soul, never flesh a primal has changed.",
     ["M682j", "M683c", "M683d", "M683f"], EX),
   P(X684, None, "main", "G'raha Tia",
     "A Scion, and proud to call himself one. Being of royal blood, he alone can imbue a familiar with the cure for tempering, and he did so for Matoya's mother porxie, "
     "which bore three Angelos.",
     ["M684h", "M684i", "M684e"], EX),
   P(X686, None, "main", "G'raha Tia",
     "A Scion who devised the cure for tempering. In Limsa Lominsa he posed as a crystal buyer in Alphinaud's place, since the merchant would be wary of the Admiral's allies, "
     "and learned the crystals were taken from the kobolds.",
     ["M684h", "M686b", "M686c"], EX),
   P(X692, None, "main", "G'raha Tia",
     "A Scion of Allagan royal blood, which the Flagship's nodes on Azys Lla still recognize. He warns that Tiamat is a special case for the porxie cure.",
     ["M684i", "M692e", "M692d"], EX),
   P(X693, None, "main", "G'raha Tia",
     "A Scion of Allagan royal blood whose aether helped Alisaie free Tiamat. He fears there is no saving the Allagans' other captives, whose flesh was altered, "
     "and counseled waiting for the other Scions before facing Lunar Bahamut.",
     ["M684i", "M693c", "M693d", "M693g"], EX),
   P(X696, None, "main", "G'raha Tia",
     "A Scion who devised the cure for tempering. With Alisaie he is seeking out the Crystal Braves who abandoned the cause, for Alphinaud's proposal to the Grand Company of Eorzea.",
     ["M682j", "M696g", "M696h"], EX),
   P(X697, None, "main", "G'raha Tia",
     "A Scion. After the Forum's envoy refused Sharlayan's aid, he wondered aloud whether the Forum is hiding something.",
     ["M684h", "M697e", "M697j"], EX),
 ],
 "char-cid": [
   P(X682, None, "main", "Cid",
     "An engineer of the Ironworks and a friend of G'raha Tia, who greeted him with a joyous reunion. With a magitek terminal he found the password to Owen's Allagan report, "
     "and helped turn it into a cure for tempering.",
     ["M682a", "M682d", "M682e", "M682j"]),
 ],
 "char-nero": [
   P(X682, None, "main", "Nero",
     "A former tribunus who works beside Cid. He joined the work on the cure for tempering, claiming that he and Cid are destined to unlock travel across dimensions and through time.",
     ["M682i"]),
 ],
 "char-aymeric": [
   P(X682, None, "main", "Aymeric",
     "Ser Aymeric of Ishgard. Hearing of your search for a cure for tempering, he pledged Ishgard's full support and sent you off with all the ceruleum you need.",
     ["M682h"]),
   P(X696, None, "main", "Aymeric",
     "Lord Aymeric of Ishgard. At the council in Ala Mhigo, where the Alliance and the beast tribes united as the Grand Company of Eorzea, he told them that together there is nothing they cannot overcome.",
     ["M696b", "M696l"]),
   P(MS, None, "main", "Aymeric",
     "Lord Aymeric of Ishgard. With the Grand Company of Eorzea holding the Telophoroi at bay, he has asked the Scions to find a means to neutralize the towers.",
     ["M698e", "M698g"]),
 ],
 "char-krile": [
   P(X682, None, "main", "Krile",
     "A Scion with the Echo, back at the Rising Stones. She briefed you on the Alliance council: with the Empire at war with itself, the Alliance seeks peace with friendly beast tribes.",
     ["M682c", "M682b"]),
   P(X689, None, "main", "Krile",
     "A Scion with the Echo. She found that the towers have been sighted as far as Yanxia, and has set out with Tataru to seek Estinien's aid against Lunar Bahamut.",
     ["M689m"]),
   P(X695, None, "main", "Krile",
     "A Scion with the Echo, leaving for Sharlayan to ask the Forum's help in uncovering the Telophoroi's motives. Before she left, she asked Estinien again to join the Scions, and he accepted.",
     ["M695i", "M695k"]),
   P(X697, None, "main", "Krile",
     "A Scion in Sharlayan, where the Forum has forbidden anyone to cooperate with her. She senses it is not as unconcerned about the Telophoroi as it claims, and asks the Scions to join her when the time is right.",
     ["M697i", "M697j", "M697k"]),
 ],
 "char-ga-bu": [
   P(X683, None, "main", "Ga Bu",
     "A kobold child in the Maelstrom's care, once silent and lost within himself. The first to receive the cure for tempering, he came back by holding to the faces of his family and friends. "
     "Alisaie has promised to return.",
     ["M683a", "M683b", "M683e", "M683i"]),
   P(X688, None, "main", "Ga Bu",
     "A young kobold cured of tempering. He came to the Navel to speak to his leader, Za Da, and told him the Great Father they summon is false. Za Da, who will not yet trust the Admiral, trusts Ga Bu.",
     ["M688d", "M688h", "M688k"]),
 ],
 "char-yshtola": [
   P(X683, None, "main", "Y'shtola",
     "A Sharlayan Scion who lent her aether to the cure that restored Ga Bu. To make more familiars, she knows an authority they may grudgingly turn to.",
     ["M683d", "M683h"]),
   P(X684, None, "main", "Y'shtola",
     "A Sharlayan Scion and Matoya's pupil. In another world she took her teacher's name, which Matoya has not let pass. She gave the mother porxie the energy to bear three Angelos.",
     ["M684a", "M684b", "M684e"]),
   P(X689, None, "main", "Y'shtola",
     "A Sharlayan Scion who delivered the first porxies to the Immortal Flames in Ul'dah, and brought word that the Amalj'aa say men are abducting their kind.",
     ["M689l", "M689n"]),
   P(X695, None, "main", "Y'shtola",
     "A Sharlayan Scion. As far as she can tell, Hydaelyn has made her will known to no one.",
     ["M695j"]),
 ],
 "char-matoya": [
   P(X684, None, "main", "Matoya",
     "The realm's foremost authority on familiars, and Y'shtola's old teacher, who greeted you with her usual bite. She proposed a mother porxie to make the porxies the cure needs, "
     "with ingredients from her abandoned workshop in the Makers' Quarter.",
     ["M684b", "M684c", "M684d"]),
 ],
 # -- the Admiral's peace
 "char-merlwyb": [
   P(X685, None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa, whose people have been at odds with their island neighbors for seven centuries. Her approach to a kobold patriarch failed when the Bloody Executioners would not hear of it.",
     ["M685c", "M685d"]),
   P(X687, None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa. Aboard the Astalicia she accepted Sicard's challenge, shot through his knee, and won the Bloody Executioners to her course. She says the Empire teeters on the brink of collapse, "
     "and turns next to Limsa's neighbors.",
     ["M687c", "M687d", "M687e", "M687f", "M687h"]),
   P(X688, None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa, who once passed judgment on her own father when he fell thrall to Leviathan. She owns that Limsa twisted an old covenant to take kobold land, "
     "and with herself as bait won the Second Order to a fledgling peace. She means to bring every kobold in.",
     ["M688l", "M688b", "M688c", "M688j"]),
   P(X689, None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa. When towers of Garlean design appeared across the realm, she sent you to join the Alliance forces on the eastern front.",
     ["M689a", "M689b"]),
 ],
 "char-hyllfyr": [
   P(X685, None, "main", "Hyllfyr",
     "Captain of the Bloody Executioners, a pirate crew of Limsa Lominsa, long bedridden with a lung ailment. In his absence his right hand, Sicard, leads them.",
     ["M685a", "M685b"], ["Captain Hyllfyr"]),
   P(X687, None, "main", "Hyllfyr",
     "Captain of the Bloody Executioners. When the Admiral bested Sicard in a duel, he told his crew that she decides where they sail. He says it will not be long before he takes his rest in the depths.",
     ["M687e", "M687f", "M687g"], ["Captain Hyllfyr"]),
 ],
 "char-sicard": [
   P(X685, None, "main", "Sicard",
     "Right hand to the Bloody Executioners' bedridden captain, and their leader in his absence. The crew's fortunes rose after his promotion, which he is said to have bought with clever coin, "
     "just as crystal prices fell.",
     ["M685b", "M685e", "M685f", "M685g"]),
   P(X686, None, "main", "Sicard",
     "Acting captain of the Bloody Executioners, who sell crystals taken from the kobolds. He says the law forbids attacks on any ship but the Empire's yet says nothing of beastmen, "
     "and that his crew keeps them from summoning their gods. He will meet the Admiral aboard the Astalicia.",
     ["M686c", "M686d", "M686e", "M686f", "M686g"]),
   P(X687, None, "main", "Sicard",
     "Right hand to Captain Hyllfyr of the Bloody Executioners. He demanded that the Admiral give up peace with the beastmen and challenged her to a duel, and she shot through his knee. "
     "Hyllfyr then told the crew to follow her.",
     ["M687a", "M687d", "M687e", "M687f"]),
 ],
 "org-bloody-executioners": [
   P(X685, None, "main", "The Bloody Executioners",
     "A pirate crew of Limsa Lominsa, led by Sicard while Captain Hyllfyr lies ill. They would not hear of the Admiral's approach to the kobolds, and have prospered as crystal prices fell.",
     ["M685a", "M685b", "M685d", "M685g"]),
   P(X686, None, "main", "The Bloody Executioners",
     "A pirate crew of Limsa Lominsa, under their acting captain, Sicard. The crystals they sell were taken from the kobolds of O'Ghomoro.",
     ["M686c", "M686d"]),
   P(X687, None, "main", "The Bloody Executioners",
     "A pirate crew of Limsa Lominsa. After the Admiral bested Sicard in a duel aboard the Astalicia, Captain Hyllfyr told them that she decides where they sail.",
     ["M687e", "M687f"]),
 ],
 "char-za-da": [
   P(X688, None, "main", "Za Da",
     "Patriarch of the kobolds' Second Order, who sacrificed his own people to summon Titan. Alisaie's cure freed him from the primal's influence. He does not yet trust the Admiral, "
     "but trusts Ga Bu, and gave peace with Limsa Lominsa a chance.",
     ["M688e", "M688f", "M688g", "M688i", "M688k"], ["Patriarch Za Da"]),
   P(X696, None, "main", "Za Da",
     "Patriarch of the kobolds' Second Order, now at peace with Limsa Lominsa. At the council in Ala Mhigo he said the kobolds look to the future as allies, "
     "and revealed that a summoning needs both prayer and aether.",
     ["M688i", "M696c", "M696e"], ["Patriarch Za Da"]),
 ],
 "org-kobolds": [
   P(X688, None, "main", "The kobolds",
     "A beast tribe of La Noscea, whose land Limsa Lominsa took by twisting an old covenant. Their Second Order, freed of Titan's influence, has made a fledgling peace with Limsa, "
     "and the Admiral means to bring every kobold in.",
     ["M688b", "M688f", "M688i", "M688j"]),
   P(X696, None, "main", "The kobolds",
     "A beast tribe of La Noscea, part of the Grand Company of Eorzea. Their patriarch Za Da says they have not forgotten past crimes, but look to the future as allies.",
     ["M696b", "M696c"]),
 ],
 "char-titan": [
   P(X688, None, "main", "Titan",
     "The primal the kobolds call Great Father. Patriarch Za Da tried to summon him in the Navel, but Alisaie's cure freed Za Da from his influence, and Ga Bu calls the Great Father false.",
     ["M688a", "M688e", "M688f", "M688h"]),
 ],
 # -- the towers
 "char-fandaniel": [
   P(X689, None, "main", "Fandaniel",
     "An Ascian wearing Asahi's body, who means to destroy the world in a recreation of the Final Days, and wants to die and take everyone with him. His towers have risen across the realm, "
     "his band is the Telophoroi, and his dragon is Lunar Bahamut. His patron is Lord Zenos; Elidibus disagreed with him, but thanks to you, he says, he is free of him.",
     ["M689d", "M689e", "M689j", "M689i", "M689f", "M689g", "M689h"]),
   P(X690, None, "main", "Fandaniel",
     "An Ascian in Asahi's body who leads the Telophoroi. With Zenos's support he has rallied part of the splintered Garlean army to them, and his towers temper those who approach to Garlemald itself.",
     ["M689d", "M690g", "M690d", "M690e"]),
   P(X695, None, "main", "Fandaniel",
     "An Ascian in Asahi's body, leading the Telophoroi. Lunar Bahamut has fallen, and he admits Tiamat's return makes more Meracydian dragons hard to come by. "
     "In Garlemald's palace he calls the Empire an instrument of the star's destruction.",
     ["M689d", "M694f", "M695l", "M695n"]),
   P(MS, None, "main", "Fandaniel",
     "An Ascian in Asahi's body, leading the Telophoroi. His bid for a confluence at Carteneau failed, and he told you your victory earned only a stay of execution. "
     "He means to draw aether closer to home, through a gateway he calls complete.",
     ["M689d", "M698f", "M698k", "M698n"]),
 ],
 "char-asahi": [
   P(X689, None, "main", "Asahi",
     "An imperial envoy who died at the exchange in Doma. His body now carries an Ascian, Fandaniel.",
     ["M689d"]),
 ],
 "char-zenos": [
   P(X689, None, "main", "Zenos",
     "The crown prince, on the imperial throne. Fandaniel calls him his patron and says he awaits you at the heart of the chaos. Zenos cares only that his friend returns to him, "
     "and broke his katana to seek a weapon worthy of your reunion.",
     ["M689g", "M689p", "M689q"]),
   P(X690, None, "main", "Zenos",
     "The crown prince, whose support has helped Fandaniel rally part of the splintered Garlean army to the Telophoroi. He seeks a weapon worthy of his reunion with you.",
     ["M689p", "M690g"]),
   P(X695, None, "main", "Zenos",
     "The crown prince, backing Fandaniel and the Telophoroi. He says the nation forged for Ascian ends will soon prove its worth.",
     ["M690g", "M695m"]),
   P(MS, None, "main", "Zenos",
     "The crown prince, backing Fandaniel and the Telophoroi. He has taken up a scythe as his new weapon, and awaits a final contest with you.",
     ["M690g", "M698l", "M698m"]),
 ],
 "char-lunar-bahamut": [
   P(X689, None, "main", "Lunar Bahamut",
     "Fandaniel's dragon, which set the Royal Menagerie's rooftop garden ablaze. G'raha thinks it a simulacrum born of Ascian magicks.",
     ["M689f", "M689o"]),
   P(X693, None, "main", "Lunar Bahamut",
     "Fandaniel's dragon, sighted leading a host, dragons among it, toward Paglth'an.",
     ["M689f", "M693e"]),
   P(X694, None, "main", "Lunar Bahamut",
     "Fandaniel's dragon, which led the Telophoroi's draconic horde against Paglth'an. It is no more.",
     ["M694c", "M694f"]),
 ],
 "org-telophoroi": [
   P(X689, None, "main", "The Telophoroi",
     "The band of Fandaniel, an Ascian who means to destroy the world in a recreation of the Final Days.",
     ["M689e", "M689i"]),
   P(X690, None, "main", "The Telophoroi",
     "Fandaniel's band, joined by part of the splintered Garlean army with Zenos's support. Black-garbed figures have led shackled Ixal toward a tower.",
     ["M690g", "M690f"]),
   P(X694, None, "main", "The Telophoroi",
     "Fandaniel's band. Their attack on Paglth'an ended in defeat, with Lunar Bahamut slain and their forces routed.",
     ["M690g", "M694f"]),
   P(MS, None, "main", "The Telophoroi",
     "Fandaniel's band, swelled with tempered beastmen and lunar primals. At the Carteneau Flats they sought an aetherial confluence, but the Grand Company of Eorzea drove them off.",
     ["M698a", "M698d", "M698e"]),
 ],
 "char-lyse": [
   P(X689, None, "main", "Lyse",
     "An Ala Mhigan of the Resistance, who welcomed you to Ala Mhigo just as Fandaniel's dragon passed overhead. Afterwards she proposed sending a unit to investigate the nearby tower.",
     ["M689c", "M689k"], ["Yda"]),
   P(X690, None, "main", "Lyse",
     "An Ala Mhigan of the Resistance. The scouts she sent to the tower came back tempered to Garlemald, and tried to murder their comrades.",
     ["M689k", "M690d"], ["Yda"]),
 ],
 "char-thancred": [
   P(X690, None, "main", "Thancred",
     "A Scion back from Garlemald with Urianger. The capital lies in deathly silence, save for the imperial palace, whose builders work as if possessed or tempered.",
     ["M690a", "M690b", "M690c"]),
   P(X695, None, "main", "Thancred",
     "A Scion who saw Garlemald's capital with Urianger. He notes the towers resemble a much larger structure they saw there.",
     ["M690a", "M695f"]),
 ],
 "char-urianger": [
   P(X690, None, "main", "Urianger",
     "A Sharlayan Scion back from Garlemald. He notes that the tempered Resistance scouts were bound not to a primal but to a nation.",
     ["M690a", "M690e"]),
   P(X693, None, "main", "Urianger",
     "A Sharlayan Scion, who reported Lunar Bahamut leading a host toward Paglth'an.",
     ["M693e"]),
   P(X695, None, "main", "Urianger",
     "A Sharlayan Scion, all but certain that the towers summon primals through those imprisoned inside.",
     ["M695e"]),
 ],
 "char-raubahn": [
   P(X690, None, "main", "Raubahn",
     "Commander of Ala Mhigo's army. With the towers rising, he has shelved the plan to march on Garlemald, and sent Arenvald and Fordola, both immune to tempering, to the tower in Paglth'an.",
     ["M690h", "M690i", "M690k"], ["Commander Raubahn"]),
 ],
 "char-arenvald": [
   P(X690, None, "main", "Arenvald",
     "A fighter of Ala Mhigo, immune to tempering. Despite Alphinaud's warnings, he went with Fordola to investigate the tower in Paglth'an.",
     ["M690i", "M690k"]),
   P(X694, None, "main", "Arenvald",
     "A fighter immune to tempering, sent with Fordola into the tower in Paglth'an. They found Amalj'aa fused to its cells, which summoned Lunar Ifrit, and he leapt between it and Fordola. "
     "Alphinaud waits anxiously for word of him.",
     ["M694i", "M694j", "M694k"]),
   P(X695, None, "main", "Arenvald",
     "A fighter who leapt between Lunar Ifrit and Fordola in the tower in Paglth'an. He lies gravely wounded in Ul'dah, where the chirurgeons have done what they can, and his fate hangs in the balance.",
     ["M694j", "M695a", "M695b"]),
   P(MS, None, "main", "Arenvald",
     "A fighter now in a wheelchair from the wounds he took in the tower in Paglth'an. Fordola brought him to see Alphinaud, whom he asked to fight in his stead and be the hero he cannot.",
     ["M698b", "M698c"]),
 ],
 "char-fordola": [
   P(X690, None, "main", "Fordola",
     "An Ala Mhigan who once fought and killed for Garlemald, and needs to know what she was part of. Immune to tempering, she went with Arenvald to the tower in Paglth'an.",
     ["M690i", "M690j", "M690k"], ["The Butcher"]),
   P(X695, None, "main", "Fordola",
     "An Ala Mhigan immune to tempering, whom Arenvald shielded from Lunar Ifrit in the tower in Paglth'an. With him gravely wounded, she lashed out at Alphinaud's idealism.",
     ["M694j", "M695b", "M695c"], ["The Butcher"]),
   P(MS, None, "main", "Fordola",
     "An Ala Mhigan immune to tempering, who brought Arenvald, now in a wheelchair, all the way from Ul'dah to see Alphinaud.",
     ["M690i", "M698b"], ["The Butcher"]),
 ],
 "char-tataru": [
   P(X690, None, "main", "Tataru",
     "The Scions' receptionist. With Krile she caught up with Estinien, who left for Ishgard as soon as he heard of the elder primal's return.",
     ["M689m", "M690l"]),
 ],
 "char-estinien": [
   P(X689, None, "main", "Estinien",
     "A dragoon whose aid Krile and Tataru have set out to seek against Fandaniel's dragon, Lunar Bahamut.",
     ["M689m", "M689f"]),
   P(X690, None, "main", "Estinien",
     "A dragoon. Krile and Tataru caught up with him, but he left for Ishgard as soon as he heard of the elder primal's return, and you give chase.",
     ["M690l"]),
   P(X691, None, "main", "Estinien",
     "A dragoon who felled Nidhogg at your side, and comes and goes as he pleases. In Nidhogg's absence he watches over Tiamat, and came to Azys Lla concerned she had been forced to summon Bahamut. "
     "You made the journey together.",
     ["M691a", "M691b", "M691e", "M691g", "M691d"]),
   P(X693, None, "main", "Estinien",
     "A dragoon who watches over Tiamat. Once she was freed, she took to the sky with him on her back, bound for Paglth'an.",
     ["M691g", "M693c", "M693f"]),
   P(X695, None, "main", "Estinien",
     "A dragoon who fought at Paglth'an. When Fordola scorned Alphinaud's ideals, he answered that such idealists are remembered as heroes. At Krile's second asking, he has joined the Scions.",
     ["M693f", "M695c", "M695k"]),
 ],
 "char-tiamat": [
   P(X691, None, "main", "Tiamat",
     "A great wyrm, Bahamut's mate, still imprisoned on Azys Lla, though her remorse binds her more than any shackle. Her hatred for humankind is long gone, but guilt for resurrecting Bahamut torments her, "
     "and Estinien, who watches over her, came out of concern that she had been forced to summon him.",
     ["M691c", "M691h", "M691f", "M691e", "M691g"]),
   P(X692, None, "main", "Tiamat",
     "A great wyrm, Bahamut's mate, still shackled on Azys Lla and tormented by guilt for resurrecting him. She says an Ascian commands the dragons of Meracydia, "
     "and fears losing herself to the eikon's influence. Her restraints need an update from a terminal in the Flagship.",
     ["M691c", "M691f", "M692b", "M692c", "M692f"]),
   P(X693, None, "main", "Tiamat",
     "A great wyrm whose beloved Bahamut the men of Allag slew; in grief she heeded the Ascians. Alisaie's cure freed her from Bahamut's influence, and she flew for Paglth'an with Estinien, "
     "bent on atonement.",
     ["M693b", "M693c", "M693f"]),
   P(X694, None, "main", "Tiamat",
     "A great wyrm, freed of Bahamut's influence. At Paglth'an her children bore you to Lunar Bahamut, and she vowed the dragons of Meracydia will never again heed the Ascians.",
     ["M693c", "M694e", "M694f", "M694h"]),
 ],
 "char-alphinaud": [
   P(X683, None, "main", "Alphinaud",
     "A young Scion who lent his aether to the cure that restored Ga Bu, and proposes making an army of porxies to treat the tempered.",
     ["M683d", "M683g"]),
   P(X685, None, "main", "Alphinaud",
     "A young Scion who means the porxies to go first to Limsa Lominsa. Looking into the Bloody Executioners, he found crystal prices falling as their fortunes rose.",
     ["M684g", "M685g"]),
   P(X690, None, "main", "Alphinaud",
     "A young Scion. He warned Arenvald against the mission to the tower in Paglth'an, in vain, and is chasing Estinien to Ishgard.",
     ["M690k", "M690l"]),
   P(X693, None, "main", "Alphinaud",
     "A young Scion who stayed on the Flagship to work the terminal that released Tiamat's shackles.",
     ["M693a", "M693c"]),
   P(X694, None, "main", "Alphinaud",
     "A young Scion who fought at Paglth'an, and waits anxiously to learn whether Arenvald has returned from the tower.",
     ["M694f", "M694k"]),
   P(X695, None, "main", "Alphinaud",
     "A young Scion whose friend Arenvald lies gravely wounded. Fordola scorned his idealism, and Estinien answered that such idealists are remembered as heroes.",
     ["M695a", "M695b", "M695c"]),
   P(X696, None, "main", "Alphinaud",
     "A young Scion whose long dream, the Grand Company of Eorzea, has been founded. Once the Crystal Braves' commander, he is gathering their former members' testimony for a proposal that will spare the new company their fate, "
     "and means to find the aether behind the summonings.",
     ["M696b", "M696g", "M696f"]),
   P(X697, None, "main", "Alphinaud",
     "A young Scion, Alisaie's twin and grandson of Louisoix. When he and his sister defied their father, Fourchenault, the Forum's envoy, he stripped them of the family name.",
     ["M697b", "M697c", "M697g"]),
   P(MS, None, "main", "Alphinaud",
     "A young Scion, disowned by his father. Before the battle at Carteneau, Arenvald, now in a wheelchair, asked him to fight in his stead and be the hero he cannot.",
     ["M697g", "M698b", "M698c"]),
 ],
 "char-alisaie": [
   P(X682, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion, set on a cure for tempering. She helped bring an Allagan node from Azys Lla to Cid, and the cure is now made, but not yet proven.",
     ["M682a", "M682j"]),
   P(X683, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. She chose the kobold Ga Bu as the first to receive the cure for tempering, which brought him back, and left him in the Maelstrom's care, promising to return.",
     ["M683a", "M683e", "M683i"]),
   P(X685, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion, who has vowed to learn what Sicard of the Bloody Executioners wants.",
     ["M685i"]),
   P(X688, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. In the Navel her cure freed Patriarch Za Da from Titan, and she told him he had sacrificed his own people to summon him.",
     ["M688f", "M688g"]),
   P(X693, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. Drawing on your aether and G'raha's, she freed Tiamat from Bahamut's influence.",
     ["M693c"]),
   P(X696, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. With G'raha she is seeking out the Crystal Braves who abandoned the cause.",
     ["M696h"]),
   P(X697, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion, granddaughter of Louisoix. When she and her brother defied their father, Fourchenault, he stripped them of the family name.",
     ["M697b", "M697c", "M697g"]),
 ],
 # -- Paglth'an
 "char-nanamo": [
   P(X694, None, "main", "Nanamo",
     "The sultana of Ul'dah. With the Syndicate's vote, she sent the Immortal Flames to defend Paglth'an alongside the Amalj'aa.",
     ["M694a", "M694b"], ["Sultana Nanamo"]),
   P(X695, None, "main", "Nanamo",
     "The sultana of Ul'dah. The Amalj'aa have pledged their full support to the Alliance, and she leaves the towers' primals to the Grand Companies, calling on the Scions only as a last resort.",
     ["M695h", "M695g"], ["Sultana Nanamo"]),
 ],
 "org-immortal-flames": [
   P(X694, None, "main", "The Immortal Flames",
     "Ul'dah's army, sent by the Syndicate's vote to defend Paglth'an with the Amalj'aa. Y'shtola brought them the first porxies.",
     ["M694a", "M694b", "M689l"]),
 ],
 "org-amaljaa": [
   P(X689, None, "main", "The Amalj'aa",
     "A beast tribe who say men have abducted some of their kind.",
     ["M689n"]),
   P(X694, None, "main", "The Amalj'aa",
     "A beast tribe who defended Paglth'an with the Immortal Flames, untouched by Lunar Bahamut's tempering. Some of their kind were found fused to the cells of the tower there. "
     "Their war chief has declared their war with Ul'dah over.",
     ["M694a", "M694d", "M694i", "M694g"]),
   P(X695, None, "main", "The Amalj'aa",
     "A beast tribe who have pledged their full support to the Alliance after the battle of Paglth'an.",
     ["M695h"]),
   P(X696, None, "main", "The Amalj'aa",
     "A beast tribe, part of the Grand Company of Eorzea.",
     ["M695h", "M696b"]),
 ],
 "char-hydaelyn": [
   P(X695, None, "main", "Hydaelyn",
     "The power whose chosen champion you are. As far as Y'shtola can tell, she has made her will known to no one, and Krile means to seek answers in Sharlayan.",
     ["M695j", "M695i"]),
 ],
 "org-scions": [
   P(X695, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, back from another world. Estinien has joined them, while Krile leaves for Sharlayan. Ul'dah's sultana will call on them only as a last resort.",
     ["M695k", "M695i", "M695g"]),
   P(X696, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future. Former Crystal Braves Riol and Alianne serve among them, and Tataru kept the glory-hunters out.",
     ["M696i", "M696j"]),
 ],
 # -- the Grand Company of Eorzea
 "org-eorzean-alliance": [
   P(X682, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's nations. With the Empire at war with itself, it has turned again to the primal problem, hoping for peace with friendly beast tribes.",
     ["M682b"]),
   P(X690, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's nations. With towers rising across the realm, its plan to march on Garlemald is on hold.",
     ["M689a", "M690h"]),
   P(X696, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's nations, which with the beast tribes has founded the Grand Company of Eorzea against the Telophoroi.",
     ["M696b"]),
 ],
 "org-ixal": [
   P(X690, None, "main", "The Ixal",
     "A beast tribe, some of whom have been led away in shackles by black-garbed figures toward the tower in Dravania.",
     ["M690f"]),
   P(X696, None, "main", "The Ixal",
     "A beast tribe, part of the Grand Company of Eorzea, to whom Kan-E-Senna offered the Scions' means of freeing the tempered.",
     ["M696b", "M696d"]),
 ],
 "org-grand-company-of-eorzea": [
   P(X696, None, "main", "The Grand Company of Eorzea",
     "The coalition founded at Ala Mhigo, where the Alliance and the beast tribes set aside their differences against the Telophoroi: a dream long nurtured by Alphinaud. "
     "He means to offer it a proposal drawn from the Crystal Braves' fate.",
     ["M696a", "M696b", "M696g"]),
   P(X697, None, "main", "The Grand Company of Eorzea",
     "The coalition of the Alliance and the beast tribes against the Telophoroi, which must face them without Sharlayan's aid.",
     ["M696b", "M697e", "M697h"]),
   P(MS, None, "main", "The Grand Company of Eorzea",
     "The coalition of the Alliance and the beast tribes. Tested at the Carteneau Flats, it emerged unbroken and drove the Telophoroi from their prize.",
     ["M698d", "M698e"]),
 ],
 "char-kan-e-senna": [
   P(X696, None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania. At the council in Ala Mhigo she offered the Ixal the Scions' means of freeing the tempered, and asked you to visit the sylphs of the Ashcrown Consortium.",
     ["M696d", "M696k"], ["the Elder Seedseer"]),
   P(X697, None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania, who received the Forum's envoy. She honored Louisoix's efforts before the Calamity, and accepted that the Telophoroi must be faced without Sharlayan.",
     ["M697c", "M697h"], ["the Elder Seedseer"]),
 ],
 "org-crystal-braves": [
   P(X696, None, "main", "The Crystal Braves",
     "A company Alphinaud once commanded, formed with good intentions; Riol says many joined only for coin or glory. Riol and Alianne now serve the Scions, and Alphinaud gathers former Braves' testimony "
     "so the Grand Company of Eorzea avoids their fate.",
     ["M696i", "M696j", "M696g"]),
 ],
 "char-alianne": [
   P(X696, None, "main", "Alianne",
     "A former Crystal Brave who now serves as a Scion, alongside Riol, at Castrum Oriens.",
     ["M696i"]),
 ],
 "char-fourchenault": [
   P(X697, None, "main", "Fourchenault",
     "The Forum's envoy to Gridania: Louisoix's son, and father of Alphinaud and Alisaie. He opposed his father's intervention in Eorzea, and brought word that Sharlayan will not intervene against the Empire, "
     "dismissing the Final Days. When his children defied him, he stripped them of the family name.",
     ["M697a", "M697b", "M697c", "M697d", "M697e", "M697f", "M697g"], ["Master Fourchenault"]),
 ],
 "char-louisoix": [
   P(X697, None, "main", "Louisoix",
     "A Sharlayan sage whose efforts before the Calamity gave Eorzea a means to vanquish the primals. His son, Fourchenault, opposed his intervention, and still does.",
     ["M697c", "M697d"], ["Archon Louisoix", "Master Louisoix"]),
 ],
 "org-garlean-empire": [
   P(X687, None, "main", "The Garlean Empire",
     "An empire founded by an Ascian, at war with itself. Admiral Merlwyb says it teeters on the brink of collapse.",
     ["M682b", "M687c"]),
   P(X695, None, "main", "The Garlean Empire",
     "An empire at war with itself. Part of its splintered army has rallied to the Telophoroi, and Zenos says the nation forged for Ascian ends will soon prove its worth.",
     ["M690g", "M695m"]),
 ],
}

K1, K2, K3, K4, K5 = ("The Tempering Cure", "The Admiral's Peace", "The Towers Rise", "Tiamat's Atonement", "One Banner for Eorzea")
PRES.update({
 "evt-the-tempering-cure": [
   P(X682, None, "main", K1,
     "Back from Azys Lla, G'raha Tia brought an Allagan node to Cid, who found the password to Owen's report. Reviving a tempered soul would only deepen its faith, so G'raha conceived an adapted memory transference, "
     "and Aymeric sent Ishgard's ceruleum for the work. The terminals gave out, but G'raha memorized the magick: a cure for tempering, still unproven.",
     ["M682a", "M682e", "M682f", "M682g", "M682h", "M682j"]),
   P(X683, None, "main", K1,
     "G'raha's cure, imbued in the familiar Angelo with aether from Y'shtola and Alphinaud, brought the kobold Ga Bu back to himself, holding to his family's faces. "
     "Yet it heals only the soul, not flesh a primal has changed. To treat more of the tempered, Alphinaud wants an army of porxies, and Y'shtola knows an authority on familiars.",
     ["M683a", "M683c", "M683d", "M683e", "M683f", "M683g", "M683h"]),
   P(X684, None, "main", K1,
     "With the cure proven on Ga Bu, Y'shtola took the party to her old teacher, Matoya, who chided her for borrowing her name in another world. "
     "Matoya proposed a mother porxie, made in her abandoned workshop, and once tamed it bore three Angelos. Making porxies is now far more manageable, and Limsa Lominsa will receive them first.",
     ["M683e", "M684a", "M684c", "M684d", "M684e", "M684f", "M684g"]),
 ],
 "evt-the-admirals-peace": [
   P(X685, None, "main", K2,
     "Admiral Merlwyb welcomed the cure, but Limsa has been at odds with its island neighbors for seven centuries, and the Bloody Executioners spurned her approach to the kobolds. "
     "Their captain lies bedridden, and his right hand, Sicard, leads them. Alphinaud found crystal prices falling as the Executioners prospered.",
     ["M685c", "M685d", "M685a", "M685b", "M685g"]),
   P(X686, None, "main", K2,
     "Merlwyb's peace with the kobolds stalled when the Bloody Executioners shunned it. Posing as a buyer, G'raha learned their crystals were taken from the kobolds of O'Ghomoro, and Sicard, their acting captain, confronted you. "
     "He says the law spares beastmen nothing, and he will meet the Admiral aboard the Astalicia.",
     ["M685d", "M686b", "M686c", "M686d", "M686e", "M686g"]),
   P(X687, None, "main", K2,
     "Aboard the Astalicia, Sicard demanded that the Admiral give up peace with the beastmen, and called a duel by pirate custom. Merlwyb shot through his knee, "
     "and Captain Hyllfyr told his crew that the Admiral decides where they sail. With the Executioners at peace with her, Merlwyb turns to her neighbors.",
     ["M687a", "M687d", "M687e", "M687f", "M687h"]),
   P(X688, None, "main", K2,
     "To win the kobolds, Merlwyb made herself and the stolen crystals bait in the Navel, and Patriarch Za Da of the Second Order tried to summon Titan. You held off his guards while Alisaie's cure freed him. "
     "Ga Bu told him the Great Father is false, and Za Da, trusting Ga Bu if not the Admiral, gave peace a chance.",
     ["M688c", "M688e", "M688f", "M688h", "M688i", "M688k"]),
 ],
 "evt-the-towers-rise": [
   P(X689, None, "main", K3,
     "Towers of seemingly Garlean design have risen across the realm. In Ala Mhigo you met an Ascian wearing Asahi's body, Fandaniel, who means to destroy the world in a recreation of the Final Days. "
     "His dragon, Lunar Bahamut, set the palace garden ablaze, and he says his patron, Lord Zenos, awaits you at the heart of the chaos.",
     ["M689a", "M689d", "M689e", "M689f", "M689g"]),
   P(X690, None, "main", K3,
     "Fandaniel leads the Telophoroi, and with Zenos's support has rallied part of the splintered Garlean army. Resistance scouts sent to a tower came back tempered to Garlemald itself, and Ixal have been led in shackles toward another. "
     "Raubahn sent Arenvald and Fordola, immune to tempering, to the tower in Paglth'an, while you chase Estinien to Ishgard.",
     ["M690g", "M690d", "M690f", "M690i", "M690l"]),
   P(X691, None, "main", K3,
     "Arenvald and Fordola scout the tower in Paglth'an while Fandaniel's Lunar Bahamut is at large. You found Estinien in Ishgard: Tiamat, Bahamut's mate, is still imprisoned on Azys Lla, and he feared she had been forced to summon him. "
     "Her hatred for humankind is long gone, but guilt torments her, and Estinien watches over her, so you flew there together.",
     ["M690k", "M691c", "M691e", "M691h", "M691f", "M691g"]),
 ],
 "evt-tiamats-atonement": [
   P(X692, None, "main", K4,
     "On Azys Lla, Tiamat told you an Ascian commands the dragons of Meracydia, and fears losing herself to the eikon if she meets Bahamut again. The Scions mean to cure her with a porxie, though G'raha calls her a special case. "
     "Her shackles cannot be released without an update from a terminal in the Flagship.",
     ["M692b", "M692c", "M692d", "M692f"]),
   P(X693, None, "main", K4,
     "With Alphinaud working the Flagship's terminal, Alisaie's treatment freed Tiamat from Bahamut's influence. Then Urianger reported Lunar Bahamut leading a host, dragons among it, toward Paglth'an, "
     "where Arenvald and Fordola scout a tower. Tiamat flew off with Estinien on her back, bent on atonement, and G'raha counseled waiting for the other Scions.",
     ["M693a", "M693c", "M693e", "M690k", "M693f", "M693g"]),
   P(X694, None, "main", K4,
     "In Paglth'an the Immortal Flames and the Amalj'aa stood against an imperial legion and Lunar Bahamut's dragons. Borne skyward by Tiamat's child, you brought Lunar Bahamut down, the Telophoroi fled, and the Amalj'aa ended their war with Ul'dah. "
     "Inside the tower, captive Amalj'aa summoned Lunar Ifrit, and Arenvald leapt between it and Fordola.",
     ["M694a", "M694c", "M694e", "M694f", "M694g", "M694j"]),
   P(X695, None, "main", K4,
     "Arenvald lies gravely wounded in Ul'dah, his fate in the balance. The towers summon primals through those imprisoned inside, but Nanamo leaves them to the Grand Companies. "
     "Krile leaves for Sharlayan to seek the Forum's help, and Estinien has joined the Scions. In Garlemald, Fandaniel calls the Empire an instrument of the star's destruction.",
     ["M695b", "M695e", "M695g", "M695i", "M695k", "M695n"]),
 ],
 "evt-one-banner-for-eorzea": [
   P(X696, None, "main", K5,
     "In Ala Mhigo the Alliance and the beast tribes united against the Telophoroi as the Grand Company of Eorzea, long Alphinaud's dream. Za Da revealed that a summoning needs prayer and aether alike, "
     "so the Scions seek the towers' source of aether. Alphinaud gathers former Crystal Braves' testimony to spare the new company their fate.",
     ["M696b", "M696e", "M696f", "M696g", "M696h"]),
   P(X697, None, "main", K5,
     "The Forum's envoy to Gridania was Fourchenault, father of Alphinaud and Alisaie, who said Sharlayan will not intervene against the Empire. When the twins defied him, he stripped them of the family name, "
     "so the Grand Company of Eorzea faces the Telophoroi alone. Krile found the Forum closed to her, and suspects it hides its concern.",
     ["M697b", "M697e", "M697g", "M697h", "M697i", "M697j"]),
   P(MS, None, "main", K5,
     "At the Carteneau Flats the Telophoroi, with tempered beastmen and lunar primals, sought an aetherial confluence, but the Grand Company of Eorzea held and drove them off. Fandaniel called it a stay of execution. "
     "Arenvald, now in a wheelchair, asked Alphinaud to be the hero he cannot. The towers drain the land itself, and the Scions wait on Krile to seek an answer in Sharlayan.",
     ["M698d", "M698e", "M698f", "M698c", "M698i", "M698h"]),
 ],
})

# ---- Relationships --------------------------------------------------------------------------------------------------
TYPES = [("child-of", "child of", "parent of", False)]  # as content_3_0_part1 defines it (listed so this era lints alone)

RELS = [
 ("rel-hyllfyr-leads-bloody-executioners", "char-hyllfyr", "leads", "org-bloody-executioners", X685, None, "main", ["M685a", "M685b"]),
 ("rel-sicard-member-of-bloody-executioners", "char-sicard", "member-of", "org-bloody-executioners", X685, None, "main", ["M685b"]),
 ("rel-sicard-leads-bloody-executioners", "char-sicard", "leads", "org-bloody-executioners", X685, X687, "main", ["M685b", "M685e"], ["M687f"]),
 ("rel-bloody-executioners-opposes-merlwyb", "org-bloody-executioners", "opposes", "char-merlwyb", X685, X687, "main", ["M685d"], ["M687f", "M687h"]),
 ("rel-bloody-executioners-serves-merlwyb", "org-bloody-executioners", "serves", "char-merlwyb", X687, None, "main", ["M687f", "M687h"]),
 ("rel-za-da-member-of-kobolds", "char-za-da", "member-of", "org-kobolds", X688, None, "main", ["M688e", "M688j"]),
 ("rel-za-da-allied-with-merlwyb", "char-za-da", "allied-with", "char-merlwyb", X688, None, "main", ["M688i", "M688j"]),
 ("rel-fandaniel-member-of-ascians", "char-fandaniel", "member-of", "org-ascians", X689, None, "main", ["M689d"]),
 ("rel-fandaniel-serves-zenos", "char-fandaniel", "serves", "char-zenos", X689, None, "main", ["M689g"]),
 ("rel-asahi-possessed-by-fandaniel", "char-asahi", "possessed-by", "char-fandaniel", X689, None, "main", ["M689d"]),
 ("rel-fandaniel-leads-telophoroi", "char-fandaniel", "leads", "org-telophoroi", X689, None, "main", ["M689i", "M689e"]),
 ("rel-lunar-bahamut-serves-fandaniel", "char-lunar-bahamut", "serves", "char-fandaniel", X689, X694, "main", ["M689f"], ["M694f"]),
 ("rel-zenos-aids-telophoroi", "char-zenos", "aids", "org-telophoroi", X690, None, "main", ["M690g"]),
 ("rel-telophoroi-opposes-eorzean-alliance", "org-telophoroi", "opposes", "org-eorzean-alliance", X690, None, "main", ["M690d", "M690h"]),
 ("rel-arenvald-aids-eorzean-alliance", "char-arenvald", "aids", "org-eorzean-alliance", X690, None, "main", ["M690i"]),
 ("rel-fordola-aids-eorzean-alliance", "char-fordola", "aids", "org-eorzean-alliance", X690, None, "main", ["M690i", "M690j"]),
 ("rel-estinien-aids-tiamat", "char-estinien", "aids", "char-tiamat", X691, None, "main", ["M691g"]),
 ("rel-tiamat-opposes-ascians", "char-tiamat", "opposes", "org-ascians", X694, None, "main", ["M694h"]),
 ("rel-tiamat-aids-scions", "char-tiamat", "aids", "org-scions", X694, None, "main", ["M694e", "M694h"]),
 ("rel-estinien-member-of-scions", "char-estinien", "member-of", "org-scions", X695, None, "main", ["M695k"]),
 ("rel-amaljaa-allied-with-eorzean-alliance", "org-amaljaa", "allied-with", "org-eorzean-alliance", X695, None, "main", ["M694g", "M695h"]),
 ("rel-eorzean-alliance-member-of-grand-company-of-eorzea", "org-eorzean-alliance", "member-of", "org-grand-company-of-eorzea", X696, None, "main", ["M696b"]),
 ("rel-kobolds-member-of-grand-company-of-eorzea", "org-kobolds", "member-of", "org-grand-company-of-eorzea", X696, None, "main", ["M696b", "M696c"]),
 ("rel-amaljaa-member-of-grand-company-of-eorzea", "org-amaljaa", "member-of", "org-grand-company-of-eorzea", X696, None, "main", ["M696b"]),
 ("rel-ixal-member-of-grand-company-of-eorzea", "org-ixal", "member-of", "org-grand-company-of-eorzea", X696, None, "main", ["M696b", "M696d"]),
 ("rel-telophoroi-opposes-grand-company-of-eorzea", "org-telophoroi", "opposes", "org-grand-company-of-eorzea", X696, None, "main", ["M696b"]),
 ("rel-alphinaud-aids-grand-company-of-eorzea", "char-alphinaud", "aids", "org-grand-company-of-eorzea", X696, None, "main", ["M696g", "M696f"]),
 ("rel-alianne-member-of-scions", "char-alianne", "member-of", "org-scions", X696, None, "main", ["M696i"]),
 ("rel-alphinaud-child-of-fourchenault", "char-alphinaud", "child-of", "char-fourchenault", X697, None, "main", ["M697b"]),
 ("rel-alisaie-child-of-fourchenault", "char-alisaie", "child-of", "char-fourchenault", X697, None, "main", ["M697b"]),
 ("rel-fourchenault-child-of-louisoix", "char-fourchenault", "child-of", "char-louisoix", X697, None, "main", ["M697c"]),
]

# Relationships an earlier era defined, ended here.
ADJUST = {
 "rel-tiamat-held-at-azys-lla": {"until": X693, "end": ["M693c", "M693f"]},          # content_3_0_part2: she is freed and flies to Paglth'an
 "rel-fordola-prisoner-of-lyse": {"until": X690, "end": ["M690i"]},                  # content_4_0_part3: Raubahn sends her to the towers
 "rel-alianne-member-crystal-braves": {"until": X696, "end": ["M696i"]},             # content_2_4_to_2_55: a former Brave, now a Scion
}

# ---- Arcs ------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-p1-the-tempering-cure", "evt-the-tempering-cure", X682, X684),
 ("arc-p2-the-admirals-peace", "evt-the-admirals-peace", X685, X688),
 ("arc-p3-the-towers-rise", "evt-the-towers-rise", X689, X691),
 ("arc-p4-tiamats-atonement", "evt-tiamats-atonement", X692, X695),
 ("arc-p5-one-banner-for-eorzea", "evt-one-banner-for-eorzea", X696, MS),
]

CASTS = {
 "evt-the-tempering-cure": [
   ("char-graha-tia", X682, ["M682g"]), ("char-alisaie", X682, ["M682a"]), ("char-cid", X682, ["M682e"]),
   ("char-nero", X682, ["M682i"]), ("char-aymeric", X682, ["M682h"]), ("char-krile", X682, ["M682c"]),
   ("char-ga-bu", X683, ["M683e"]), ("char-alphinaud", X683, ["M683g"]), ("char-yshtola", X683, ["M683h"]),
   ("char-matoya", X684, ["M684c"]),
 ],
 "evt-the-admirals-peace": [
   ("char-merlwyb", X685, ["M685d"]), ("char-alphinaud", X685, ["M685g"]), ("char-alisaie", X685, ["M685i"]),
   ("char-sicard", X685, ["M685b"]), ("char-hyllfyr", X685, ["M685a"]), ("org-bloody-executioners", X685, ["M685d"]),
   ("char-graha-tia", X686, ["M686b"]), ("char-za-da", X688, ["M688e"]), ("char-ga-bu", X688, ["M688h"]),
   ("org-kobolds", X688, ["M688i"]),
 ],
 "evt-the-towers-rise": [
   ("char-fandaniel", X689, ["M689d"]), ("char-lunar-bahamut", X689, ["M689f"]), ("char-zenos", X689, ["M689g"]),
   ("char-lyse", X689, ["M689k"]), ("char-alphinaud", X689, ["M689d"]), ("char-thancred", X690, ["M690a"]),
   ("char-arenvald", X690, ["M690i"]), ("char-fordola", X690, ["M690i"]), ("char-estinien", X691, ["M691g"]),
   ("char-tiamat", X691, ["M691c"]),
 ],
 "evt-tiamats-atonement": [
   ("char-tiamat", X692, ["M692b"]), ("char-estinien", X692, ["M691g"]), ("char-graha-tia", X692, ["M692d"]),
   ("char-alisaie", X693, ["M693c"]), ("char-alphinaud", X693, ["M693a"]), ("char-lunar-bahamut", X693, ["M693e"]),
   ("char-nanamo", X694, ["M694a"]), ("org-amaljaa", X694, ["M694a"]), ("char-arenvald", X694, ["M694j"]),
   ("char-fordola", X694, ["M694j"]),
 ],
 "evt-one-banner-for-eorzea": [
   ("org-grand-company-of-eorzea", X696, ["M696b"]), ("char-alphinaud", X696, ["M696g"]), ("char-alisaie", X696, ["M696h"]),
   ("char-graha-tia", X696, ["M696h"]), ("char-za-da", X696, ["M696e"]), ("char-kan-e-senna", X696, ["M696k"]),
   ("char-fourchenault", X697, ["M697a"]), ("char-krile", X697, ["M697i"]), ("char-arenvald", MS, ["M698c"]),
   ("char-fandaniel", MS, ["M698f"]),
 ],
}

ARC_NOTES = {
 "arc-p1-the-tempering-cure": "MSQ #682 *Reviving the Legacy* to #684 *Like Master, Like Pupil* (5.4): Owen's report and G'raha's selective reanimation (M682f, M682g), "
   "the first cure on Ga Bu (M683e) and Matoya's mother porxie (M684e). It starts where the 5.1–5.3 era hands over (the node bound for Cid, #681) and ends once the porxies can be made (M684f).",
 "arc-p2-the-admirals-peace": "MSQ #685 *The Admiral's Resolve* to #688 *The Great Ship Vylbrand* (5.4): the Bloody Executioners' obstruction (M685d), Sicard (M686d), the duel (M687e) "
   "and Za Da's cure and peace with the Second Order (M688f, M688i). Ends on the kobold peace, before the towers appear (#689).",
 "arc-p3-the-towers-rise": "MSQ #689 *Futures Rewritten* (5.4) to #691 *Here Be Dragons* (5.5): the towers and Fandaniel (M689a, M689d), the Telophoroi and the tempered scouts (M690g, M690d), "
   "and the hunt for Estinien, which ends on the flight to Tiamat (M691d). Tiamat joins the cast at #691, where Estinien's account first brings her in.",
 "arc-p4-tiamats-atonement": "MSQ #692 *Righteous Indignation* to #695 *When the Dust Settles* (5.5): Tiamat's cure (M693c), the battle of Paglth'an and the tower (M694f, M694j), "
   "and its aftermath: Arenvald's wounds, the towers' purpose and Estinien joining the Scions (M695b, M695e, M695k). Krile and Urianger stay in the entity records, because the cast is full.",
 "arc-p5-one-banner-for-eorzea": "MSQ #696 *The Company We Keep* (5.55) to the cp-shb-5-55 milestone (after *Death Unto Dawn*): the Grand Company of Eorzea (M696b), Fourchenault and the Forum's refusal (M697e, M697g), "
   "and the battle at Carteneau (M698e) with the towers' drain on the land (M698i). Aymeric, Fordola and Zenos appear at the milestone in their entity records; the cast is full.",
}

DECISIONS = [
 "**Five arcs (p1–p5)** cover every step from #682 to cp-shb-5-55 without sharing steps; each is 3–4 steps long, the last ending on the milestone.",
 "**G'raha Tia** (`char-graha-tia`, assumed to be the id the 5.0 era gives the Crystal Exarch's revealed identity) carries \"The Crystal Exarch\" as an alias on every presentation here; that alias is why ALLOW proposes \"Exarch\".",
 "**Fandaniel** (`char-fandaniel`) is named from #689, where he introduces himself to you; Asahi gets a new presentation there and a `possessed-by` edge to him, as Zenos's body had to Elidibus. Lunar Bahamut is its own entry (#689–#694), ending as `serves` Fandaniel when it falls.",
 "**Fourchenault** is new at #697 with `child-of` edges from Alphinaud and Alisaie and to Louisoix. Disowning them is told in text (\"stripped them of the family name\"); \"Leveilleur\" appears only in locators.",
 "**Riol stays text-only**: earlier eras already name him in text without an entity, so an entity first visible at #696 would fail the lint. The lead may backfill `char-riol` from his first mention.",
 "**New organizations:** the Bloody Executioners, the kobolds (`org-kobolds`, named \"The kobolds\" so earlier lowercase mentions don't collide), the Amalj'aa (`org-amaljaa`), the Telophoroi and the Grand Company of Eorzea.",
 "**Left out as entities** (named in text only, or not at all): Owen, Lord Amon, Wedge, Lucia, Moenskaet, Eynzahr, Carvallain, Rhoswen, Marshal Tarupin, Lunar Ifrit, the Restrainment Node, Frixio, Ameliance, the Paragon, the dreamer and the white-haired woman.",
 "**Surnames out:** Estinien's, Lyse's, the twins' and Nanamo's surnames, and \"Garlond\" in Nero's line, appear only in locators.",
]

# Banned terms this era needs, from the first step where it uses them.
ALLOW = {
 "Exarch": X682,  # G'raha Tia's alias "The Crystal Exarch", carried from the 5.0 reveal (the 5.0 era should propose its own earlier step)
}
