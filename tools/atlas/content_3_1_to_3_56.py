"""Atlas content for patches 3.1–3.56, MSQ #336 An Uncertain Future to #378 Fly Free, My Pretty, and the cp-hw-3-56
milestone (after The Far Edge of Fate). Arc tag g. Data only (docs/atlas/era-modules.md is the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes L20–L26); every locator is an exact substring
of a quest's Journal, Steps or main dialogue. Spoiler rules this module follows:
  - the Heavensward cast reuses the contract's conventional IDs (char-aymeric, char-estinien, char-nidhogg …); each
    first presentation here stands on its own as of its step;
  - entities whose names already appear in accepted text (Ishgard, House Fortemps, Raubahn, Yugiri, Hydaelyn) are
    left to the earlier eras, so this module only names them in text; Ilberd is the exception (the Griffin reveal
    needs him): he gets one record, at #374, on top of the earlier eras' records;
  - banned terms are proposed in ALLOW from the step where the pages establish them: "Warriors of Darkness" (#340),
    "Word of the Mother" (#345, a quest title), "The First" (#362, a quest title; never used in text), "Nero" (#376,
    where he introduces himself) and "Lyse" (cp-hw-3-56). Surnames stay out (no "de Borel", "Roaille", "tol Scaeva",
    "yae Galvus", "Garlond", "Hext"); Baelsar's Wall is "the Wall".
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

(G336, G337, G338, G339, G340, G341, G342, G343, G344, G345, G346, G347, G348, G349, G350, G351, G352, G353, G354, G355,
 G356, G357, G358, G359, G360, G361, G362, G363, G364, G365, G366, G367, G368, G369, G370, G371, G372, G373, G374, G375,
 G376, G377, G378) = (f"cp-msq-{n}" for n in range(336, 379))
MS = "cp-hw-3-56"

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #336 An Uncertain Future
 "M336a": ("With the archbishop's seat vacant after his father's passing, Aymeric has assumed its responsibilities under canon law.", "An Uncertain Future", "With my father's passing, the seat of the archbishop lies vacant. And so, in accordance with canon law, I have assumed his responsibilities."),
 "M336b": ("Aymeric made public how his father, the archbishop, disappeared.", "An Uncertain Future", "Despite Ser Aymeric's decision to disclose the circumstances surrounding [[Thordan VII|his father]]'s disappearance"),
 "M336c": ("Ishgard is divided: some dispute Aymeric's account, and many who accept it question how the archbishop was stopped.", "An Uncertain Future", "Some dispute the lord commander's version of events, while many who do accept the truth question the measures taken to stop the archbishop."),
 "M336d": ("Aymeric sends you to escort Lucia to Anyx Trine to treat with Vidofnir and restore relations with Hraesvelgr's brood.", "An Uncertain Future", "Ser Aymeric bids you escort [[Lucia]] to [[Anyx Trine]], that she might treat with [[Vidofnir]] and thereby reestablish diplomatic relations with [[Hraesvelgr]]'s brood."),
 "M336f": ("Nidhogg now holds both his eyes and the Azure Dragoon's body.", "An Uncertain Future", "Nidhogg, now possessed of his two eyes and the body of the Azure dragoon─prizes to which he had laid claim"),
 "M336g": ("The hunt for Minfilia and Thancred is at a standstill.", "An Uncertain Future", "the hunt for [[Minfilia Warde|Minfilia]] and [[Thancred]] remains at a standstill."),
 "M336h": ("Riol's men report that F'lhaminn slipped aboard a ship for Radz-at-Han.", "An Uncertain Future", "according to Riol, she crept aboard a ship bound for Radz-at-Han, where she's been hiding ever since."),
 "M336i": ("Riol thinks Yda and Papalymo threw away their linkpearls after escaping the Royal Promenade.", "An Uncertain Future", "Riol thinks they must have disposed of them after escaping from the Royal Promenade."),
 "M336j": ("A Sharlayan scholar of the Students of Baldesion has been enlisted to help the search.", "An Uncertain Future", "we've enlisted the services of a Sharlayan scholar─one of the Students of Baldesion─to aid in the search"),
 "M336k": ("Alphinaud and you are summoned to a private audience with Aymeric.", "An Uncertain Future", "have been summoned for a private audience with Ser [[Aymeric]] to discuss an undisclosed matter"),
 # #337 Breaking the Cycle
 "M337a": ("Lucia tells Vidofnir that King Thordan and his knights betrayed and murdered Ratatoskr.", "Breaking the Cycle", "King Thordan and his knights twelve did willfully betray and murder the great wyrm Ratatoskr, shattering the peace between our peoples."),
 "M337b": ("Ishgard's leaders hid that truth for a thousand years until you, the Azure Dragoon and Ysayle exposed it.", "Breaking the Cycle", "For one thousand years, our leaders conspired to conceal this truth - a truth which was at last laid bare by the Warrior of Light, the Azure Dragoon...and Ysayle."),
 "M337c": ("Vidofnir must consult her sire before she answers.", "Breaking the Cycle", "This matter concerneth my sire. He must needs be consulted."),
 "M337d": ("Vidofnir says the Gnath grow bold again.", "Breaking the Cycle", "Moreover, the Gnath grow bold, even as they did before, and I would not leave my people at the mercy of the swarm."),
 "M337e": ("Alphinaud came to see Ysayle as a noble, if misguided, soul.", "Breaking the Cycle", "whom he once viewed as a murderous fanatic, but later came to see as a noble, if misguided, soul."),
 "M337f": ("You leave Lucia and head west to join Y'shtola in welcoming the visiting scholar.", "Breaking the Cycle", "Your business in [[Anyx Trine]] thus concluded, you bid farewell to Lucia so that you may continue west to [[Sharlayan]] and join [[Y'shtola]] in welcoming the visiting scholar."),
 # #338 Another Time, Another Place
 "M338a": ("The scholar is Krile, a dear friend of Minfilia.", "Another Time, Another Place", "The scholar is revealed to be none other than [[Krile]], a dear friend of Minfilia."),
 "M338b": ("Krile knew the twins at the Studium.", "Another Time, Another Place", "you learn that the woman also knew the Leveilleur twins during their time at the [[The Studium|Studium]]."),
 "M338c": ("Krile's plan to find Thancred needs Matoya's Crystal Eye.", "Another Time, Another Place", "she explains that she has a plan to locate Thancred. However, it will require the use of Master [[Matoya]]'s Crystal Eye"),
 "M338d": ("Vidofnir seemed open to Aymeric's proposal.", "Another Time, Another Place", "She must discuss Ser Aymeric's proposal with Hraesvelgr, of course, but she seemed amenable to the suggestion."),
 "M338e": ("Krile is recently come from the Sharlayan homeland.", "Another Time, Another Place", "Pray allow me to introduce Krile, who is recently come from the Sharlayan motherland."),
 "M338g": ("The Crystal Eye is one of Matoya's most cherished relics.", "Another Time, Another Place", "The Crystal Eye is one of Master Matoya's most cherished relics."),
 "M338f": ("Krile hopes to follow a trail Thancred left when Y'shtola sent him away.", "Another Time, Another Place", "Simply put, assuming Thancred left some manner of trail when you whisked him away"),
 # #339 In the Eye of the Beholder
 "M339a": ("Krile has the Echo, and the blessing of Light preserved her when the Isle of Val was attacked.", "In the Eye of the Beholder", "Krile reveals not only that she possesses the Echo, but that she has availed herself of the blessing of Light's protection"),
 "M339b": ("The Students of Baldesion's headquarters and the Isle of Val itself were obliterated by a powerful magick.", "In the Eye of the Beholder", "Regrettably, our order's headquarters—and the isle itself—were obliterated by a magick of immense power."),
 "M339c": ("Krile befriended Minfilia while studying with the Students.", "In the Eye of the Beholder", "It was in the course of these studies that I met and subsequently befriended Minfilia."),
 "M339d": ("Matoya's Crystal Eye is an ancient Crystal of Light.", "In the Eye of the Beholder", "You have in your possession an ancient Crystal of Light"),
 "M339e": ("Matoya agrees to Krile's plan.", "In the Eye of the Beholder", "Having taken a liking to the girl, Matoya consents to Krile's plan"),
 "M339f": ("In a trance, Krile sees Thancred emerge from the Lifestream near Sohm Al.", "In the Eye of the Beholder", "In a trance, she declares that Thancred emerged from the [[Lifestream]] near the base of [[Sohm Al]]"),
 "M339g": ("A Vath trader came to Tailfeather seeking garments for a man of refinement.", "In the Eye of the Beholder", "one of a [[Vath]] trader who came to Tailfeather in search of garments fit for a"),
 # #340 A Little Slow, a Little Late
 "M340a": ("The Vath say Thancred went to Loth ast Gnath when he heard the Gnath had summoned their god again.", "A Little Slow, a Little Late", "Gone to Loth ast Gnath. Not long ago. When he heard the Onemind had summoned our god once more."),
 "M340b": ("The Gnath have summoned Ravana again.", "A Little Slow, a Little Late", "the [[Gnath]] had summoned forth [[Ravana]] from the aether once more"),
 "M340c": ("Y'shtola's forbidden magicks sent Thancred into the wilderness.", "A Little Slow, a Little Late", "Had I known you intended to use forbidden magicks to deliver me to some godsforsaken wilderness..."),
 "M340d": ("A party of adventurers was already beating Ravana when you arrived.", "A Little Slow, a Little Late", "a party of adventurers locked in combat with the Lord of the Hive, and having seized the upper hand no less."),
 "M340e": ("Their leader names them the Warriors of Darkness, walkers of a different path.", "A Little Slow, a Little Late", "Mark well our faces, Warrior of Light, for we are the Warriors of Darkness. Walkers of a different path."),
 "M340f": ("Krile saw in the leader's memory a fight with a man in black, perhaps an Ascian.", "A Little Slow, a Little Late", "They were confronting a man in black. An Ascian, I think."),
 "M340g": ("Thancred learned of Ravana from the Vath.", "A Little Slow, a Little Late", "From them I learned of Ravana, and of the great warrior who had once laid him low."),
 # #341 Dreams of the Lost
 "M341a": ("Vidofnir is pleased that Ravana has fallen.", "Dreams of the Lost", "Vidofnir is nevertheless pleased to learn of Ravana's defeat."),
 "M341b": ("Hraesvelgr has mourned for a thousand years his beloved, who gave her life for a peace a king betrayed.", "Dreams of the Lost", "For a thousand years I have mourned my beloved, who gave her life to forge a peace thy king betrayed."),
 "M341c": ("Vidofnir will journey to Ishgard on behalf of her people.", "Dreams of the Lost", "Let it be known that I, Vidofnir, shall journey unto Ishgard on behalf of my people."),
 "M341d": ("The Warriors of Darkness have plainly fought primals before.", "Dreams of the Lost", "it seems all but certain that the [[Warriors of Darkness]] have fought such beings before."),
 "M341e": ("Alphinaud says they have the Echo and are driven to put down primals.", "Dreams of the Lost", "Blessed with the power of the Echo, and driven to put down primals"),
 "M341f": ("Aymeric will recover from the attack on him, but it was only the beginning.", "Dreams of the Lost", "Though he is like to make a full recovery, the attack was only the beginning"),
 "M341g": ("The knife of honorable men set the city aflame.", "Dreams of the Lost", "Honorable men, whose knife in the dark was the spark which set the city aflame."),
 "M341h": ("Hilda says the fires multiply faster than they can be put out.", "Dreams of the Lost", "We've been dowsin' the fires, but for every one we put out, it seems like two more start up."),
 "M341i": ("Krile goes to ask Matoya's help in the search for Minfilia.", "Dreams of the Lost", "If you have need of me, I shall be with Master Matoya. I would beg her assistance with the search for Minfilia."),
 "M341j": ("Thancred is saddened that Yda, Papalymo and Minfilia are still missing.", "Dreams of the Lost", "he is saddened to learn that [[Yda]], [[Papalymo]], and [[Minfilia Warde|Minfilia]] are still missing."),
 # #342 Against the Dying of the Light
 "M342a": ("Lucia sets you to finding witnesses and suspects.", "Against the Dying of the Light", "Witnesses must be found; suspects must be identified."),
 "M342b": ("Refugees are sheltered and fed in the Vault on Aymeric's initiative.", "Against the Dying of the Light", "the [[The Hoplon|Hoplon]] has been inundated with refugees on their way to receive food and shelter in the [[The Vault (Landmark)|Vault]]—an initiative of Ser [[Aymeric]]'s, apparently."),
 "M342c": ("Thancred tricks a captured arsonist into confessing.", "Against the Dying of the Light", "Thancred tricks the man into confessing by claiming his highborn master betrayed his trust."),
 "M342d": ("The arsons were orchestrated by a person or persons of influence.", "Against the Dying of the Light", "we have at last confirmed that these arsons were orchestrated by a person or persons of influence."),
 "M342e": ("Artoirel's father is slandered, and his half-brother is newly dead.", "Against the Dying of the Light", "His father is widely slandered, and his half-brother not yet cold in the grave."),
 "M342f": ("House Fortemps has known much tragedy.", "Against the Dying of the Light", "Truly, none can deny that [[House Fortemps]] has known much tragedy of late"),
 "M342g": ("Artoirel brings a salve for Aymeric on his father's behalf.", "Against the Dying of the Light", "who has come on [[Edmont de Fortemps|his father]]'s behalf to deliver a special salve for Ser Aymeric."),
 # #343 As Goes Light, So Goes Darkness
 "M343a": ("The True Brothers of the Faith seized the Vault and took the refugees there hostage.", "As Goes Light, So Goes Darkness", "a rebel faction calling themselves the True Brothers of the Faith have seized control of the [[The Vault (Landmark)|Vault]], and taken the refugees sheltering within hostage."),
 "M343b": ("You, Aymeric and Artoirel rescue all but one of the captives.", "As Goes Light, So Goes Darkness", "together you are able to rescue all but one of their captives"),
 "M343c": ("A priest throws the girl Maelie from the ledge, and a great white dragon, Vidofnir, catches her.", "As Goes Light, So Goes Darkness", "In a final act of defiance, he throws Maelie from the ledge, sending the child tumbling towards the plaza. … a great white dragon swoops down to pluck her from the very jaws of death."),
 "M343d": ("Nidhogg and his brood have flown for skies unknown.", "As Goes Light, So Goes Darkness", "It would seem [[Nidhogg]] and his brood have flown for skies unknown."),
 "M343e": ("Vidofnir can say nothing of Estinien.", "As Goes Light, So Goes Darkness", "Such matters are beyond my ken."),
 "M343f": ("Count Edmont steps aside so that Artoirel will head House Fortemps.", "As Goes Light, So Goes Darkness", "reveals that Count Edmont means to step aside, leaving him to take his father's place as the head of [[House Fortemps]]."),
 "M343g": ("Edmont would rid the house of suspicion that it joined a coup by Aymeric.", "As Goes Light, So Goes Darkness", "In this way, Count Edmont intends to rid the house of the lingering suspicion that it was complicit in a coup d'etat orchestrated by Ser Aymeric."),
 "M343h": ("Artoirel vows to follow Haurchefant's example.", "As Goes Light, So Goes Darkness", "And so he vows to follow [[Haurchefant]]'s proud example and labor for the greater good of Ishgard."),
 "M343i": ("Y'shtola suspects Thancred's aetheric flow is disrupted, keeping him from magicks and teleportation.", "As Goes Light, So Goes Darkness", "his aetheric flow has been disrupted in a manner which would theoretically prevent him from wielding all magicks, teleportation included."),
 "M343j": ("At the Great Gubal Library, Urianger meets Elidibus and the Warriors' leader.", "As Goes Light, So Goes Darkness", "[Urianger is in the Great Gubal Library. He meets with Elidibus and the Warrior of Darkness.]"),
 "M343k": ("Elidibus tells Urianger their fates were ordained long ago.", "As Goes Light, So Goes Darkness", "Our fates were ordained long ago, Archon. The Garleans are no exception."),
 "M343l": ("At an Ala Mhigan Resistance camp, Yda says the Masks will attack once all units are in place.", "As Goes Light, So Goes Darkness", "[At an Ala Mhigan Resistance camp] … The Masks will attack as soon as all units are in position."),
 # #344 As It Once Was
 "M344a": ("F'lhaminn, Hoary Boulder and Coultenet are coming home to the Scions.", "As It Once Was", "[[Tataru]] proudly informs you that [[F'lhaminn]], [[Hoary Boulder]], and [[Coultenet]]—the three"),
 "M344b": ("Krile proposes that Hydaelyn's intercession must leave a trace in the aether.", "As It Once Was", "I propose that such intervention, however, subtle, must surely leave some residual trace."),
 "M344c": ("Krile and Thancred will analyze the aether in Castrum Meridianum.", "As It Once Was", "Krile and I will infiltrate the castrum and analyze the aether therein."),
 "M344d": ("F'lhaminn asks after her daughter Minfilia.", "As It Once Was", "Eager to speak with her daughter, F'lhaminn asks after Minfilia"),
 "M344e": ("Thancred calls Minfilia the Scions' guiding light after the Calamity.", "As It Once Was", "In those dark days following the Calamity, she was our guiding light—our hope for a brighter future."),
 "M344f": ("Alphinaud blames his ambition for the Scions' flight.", "As It Once Was", "'Twas the chaos born of my foolish ambition which forced them to flee."),
 "M344g": ("Tataru insists Minfilia, Yda and Papalymo will be found.", "As It Once Was", "We'll find them, Alphinaud—I know we will! Minfilia, Yda, Papalymo...every last one!"),
 # #345 The Word of the Mother
 "M345a": ("The aether at the Praetorium and the aqueducts bears a signature also found at the Isle of Val.", "The Word of the Mother", "the readings from these two locations yielded a unique aetheric signature—one which was also detected at the [[Isle of Val]]"),
 "M345b": ("Krile believes Hydaelyn guided Minfilia to her realm.", "The Word of the Mother", "Krile surmises that Hydaelyn—who has a demonstrated capacity to summon the consciousness of those blessed with the Echo to Her realm—may have guided Minfilia"),
 "M345c": ("The Antitower is a Sharlayan structure overlooking the aetherial sea.", "The Word of the Mother", "I speak of the Antitower—a Sharlayan construction conceived to provide scholars a vantage point over the aetherial sea."),
 "M345d": ("Matoya keeps Krile behind to restore the ward.", "The Word of the Mother", "she demands that Krile stays behind to help her restore the ward over the door"),
 "M345e": ("A voice calling itself the Word of the Mother says it was once Minfilia.", "The Word of the Mother", "We are the Word of the Mother. We who were once called"),
 "M345f": ("Hydaelyn banished the Darkness when it coveted power.", "The Word of the Mother", "But the Darkness coveted power, and the balance was broken. Thus was I forced to banish Him unto the distant heavens"),
 "M345g": ("Seven times the Ascians have succeeded, and the Darkness grown stronger.", "The Word of the Mother", "Seven times have they succeeded. Seven times has the Darkness grown stronger. Seven times have I failed."),
 "M345h": ("Krile concludes Minfilia, joined with Hydaelyn, struggles to keep her own form.", "The Word of the Mother", "it is not hard to see why Minfilia, having joined with Her, might struggle to maintain her own form."),
 "M345i": ("Matoya tells Alphinaud Minfilia threw herself on the fire for the Scions' cause.", "The Word of the Mother", "She threw herself on the fire to fuel your"),
 "M345j": ("Thancred storms out without a word.", "The Word of the Mother", "while Thancred storms out without uttering a word, leaving you alone with Alphinaud and Matoya"),
 "M345k": ("The Forum gave Matoya the Antitower's custodianship.", "The Word of the Mother", "Role? Hardly. The Forum foisted the title on me."),
 # #346 This War of Ours
 "M346a": ("Alphinaud will tell Tataru and Urianger of Minfilia's fate, but asks you to tell no one else, least of all F'lhaminn.", "This War of Ours", "Although [[Alphinaud]] intends to inform [[Tataru]] and [[Urianger]] of [[Minfilia Warde|Minfilia's]] fate, he asks that you share with no one else what you have learned—especially [[F'lhaminn]]."),
 "M346b": ("Vidofnir's rescue of a child gave hope of peace between man and dragon.", "This War of Ours", "Yet in adversity were we blessed with the promise of peace between man and dragon, through Vidofnir's timely rescue of an innocent child."),
 "M346c": ("Aymeric is arranging a peace conference at Falcon's Nest, to be attended by Vidofnir.", "This War of Ours", "he has begun making formal arrangements for a peace conference in [[Falcon's Nest]], to be attended by [[Vidofnir]]"),
 "M346d": ("Aymeric fears Nidhogg, implacably opposed to peace, may disrupt the conference.", "This War of Ours", "Given Nidhogg's implacable opposition to the peace, it is possible that he and his followers may attempt to disrupt proceedings"),
 "M346e": ("Lucia was sent to Ishgard as a foreign spy.", "This War of Ours", "Dispatched to a foreign nation as a spy, it was her duty to infiltrate [[Ishgard]]ian society for her masters' ends."),
 "M346f": ("Lucia chose instead to pledge herself to Ishgard's cause and war.", "This War of Ours", "In the end, however, she chose a different path—to pledge herself to another nation's cause, and to join in their war."),
 "M346g": ("A relief at Falcon's Nest will be unveiled during the conference.", "This War of Ours", "It conceals a relief that will be unveiled during the conference."),
 # #347 Staunch Conviction
 "M347a": ("A small party of Convictors has pledged to attack any Dravanians bound for Falcon's Nest.", "Staunch Conviction", "The majority were willing to do so, but a small party have instead pledged to engage any Dravanians bound for Falcon's Nest."),
 "M347b": ("Lucia rides out with Artoirel, since a lord of House Fortemps will make the Convictors reluctant to oppose her.", "Staunch Conviction", "They should be far more reluctant to oppose us were a lord of House Fortemps present."),
 "M347c": ("Artoirel asks you to look after Emmanellain.", "Staunch Conviction", "I must ask: would you look after Emmanellain while I am away?"),
 "M347d": ("Artoirel calls Emmanellain impulsive and lately melancholy.", "Staunch Conviction", "he has ever been an impulsive, changeable child, but recently he seems to have been suffering from a bout of melancholy."),
 "M347e": ("Lords Artoirel and Emmanellain have volunteered at Falcon's Nest.", "Staunch Conviction", "you may meet lords Artoirel and Emmanellain, who have graciously volunteered their services."),
 # #348 Once More, a Favor
 "M348a": ("Emmanellain is forbidden to leave Falcon's Nest.", "Once More, a Favor", "The wasteland beyond the walls must be kept safe for travelers, yet I have been forbidden from leaving Falcon's Nest."),
 "M348b": ("You find Thancred, who saved two heretics from wolves.", "Once More, a Favor", "You find Thancred, as well as two heretics he seemingly saved from a ravenous wolf pack."),
 "M348c": ("Thancred says the young lord took advantage of you both.", "Once More, a Favor", "The young lord wasted no time taking advantage of you, did he? And me, I suppose."),
 # #349 For Those We Have Lost
 "M349a": ("A waitress drugs you in the tavern.", "For Those We Have Lost", "You crumple to the ground, and as all fades to black, you hear her whisper to sleep, to sleep..."),
 "M349b": ("The woman cries for vengeance on the Dravanians, and Emmanellain, panicking, commands a knight to act.", "For Those We Have Lost", "She cries out for vengeance against the [[Dravania]]ns, and Emmanellain, in a panic, commands a nearby knight to act."),
 "M349c": ("The knight shoots her, and a second arrow fells her.", "For Those We Have Lost", "As the crowd looks on, the knight shoots, striking her in the arm. … before a second arrow silences her, and she falls from sight."),
 "M349d": ("The knight says he did as Emmanellain ordered.", "For Those We Have Lost", "I-I only did as you ordered, my lord..."),
 "M349e": ("The peace conference has no chance in this climate.", "For Those We Have Lost", "the peace conference clearly has no chance of success in this climate."),
 "M349f": ("The people will remember a young lordling ordering an unarmed protester's execution.", "For Those We Have Lost", "the people will not soon forget the image of a young lordling ordering the public execution of an unarmed protestor"),
 # #350 Consequences
 "M350a": ("The Convictory incident was likely a ruse, and the protest leader yet lives.", "Consequences", "They reveal that the incident at the [[The Convictory|Convictory]] was more than likely a ruse intended to draw them away from the hamlet, and that the protest leader, while gravely wounded, yet lives."),
 "M350b": ("The protesters infiltrated Falcon's Nest as servants and guests.", "Consequences", "She and her conspirators infiltrated Falcon's Nest posing as servants and guests."),
 "M350c": ("Artoirel orders Emmanellain back to Ishgard to answer for his actions.", "Consequences", "Lord Artoirel duly orders his brother to return to [[Ishgard]] and answer for his actions"),
 "M350d": ("Honoroit was beaten for trying to stop the smallfolk leaving.", "Consequences", "he attempted to dissuade the smallfolk from leaving"),
 "M350e": ("Thancred strikes Emmanellain.", "Consequences", "Thancred, in turn, deals Lord Emmanellain a swingeing blow, snarling that he knows nothing of him and his failures."),
 "M350f": ("Thancred has tried everything to save those dear to him, and failed.", "Consequences", "I have fought tooth and nail for the people I hold dear—done ''everything'' in my power to save them...and I have failed."),
 "M350g": ("Lucia suspends the peace conference pending Aymeric's decision.", "Consequences", "I have no choice but to suspend the peace conference, pending Ser Amyeric's final decision."),
 "M350h": ("Artoirel has detained the Convictors for questioning.", "Consequences", "Accordingly, we have detained them for questioning."),
 "M350i": ("Lucia is the first commander.", "Consequences", "Recalling that Lord [[Artoirel]] and the [[Lucia|first commander]] should have returned by now"),
 "M350j": ("Honoroit is Emmanellain's manservant.", "Consequences", "calling for his manservant to accompany him. [[Honoroit]], however, is nowhere to be seen."),
 # #351 Choices
 "M351a": ("The Alliance proposed joint exercises, which Aymeric would present as a grand melee.", "Choices", "The other members of the [[The Eorzean Alliance|Eorzean Alliance]] have recently proposed joint military exercises, which Ser Aymeric believes could be presented as a"),
 "M351b": ("Edmont asks that his younger son fight in the melee to make amends.", "Choices", "his only request is that his younger son take part in the melee, that he might make amends for his mistakes in [[Falcon's Nest]]."),
 "M351c": ("Lucia, likely a Garlean citizen once, has seen such spectacles rally people to the imperial cause.", "Choices", "Doubtless, as a [[Garlean]] citizen, she bore witness to similar spectacles intended to rally the people to the imperial cause"),
 "M351d": ("Inspired by Aymeric, Emmanellain begs leave to fight in the melee.", "Choices", "So inspired, he begs leave to participate in the grand melee"),
 "M351e": ("Aymeric's father trusted only himself.", "Choices", "He did not believe the people strong enough to bring about their own deliverance, trusting only in himself."),
 "M351f": ("People call Aymeric a patricide in the streets.", "Choices", "They decry you as a patricide in the streets."),
 "M351g": ("You agree to fight for Ishgard.", "Choices", "you agree to fight for Ishgard, and a jubilant Ser Aymeric declares that you shall give the people a spectacle for the ages."),
 "M351h": ("Thancred recalls that the Ascians sought to profit from the war.", "Choices", "In any event, let us not forget that the Ascians sought to profit from this war."),
 # #352 A Spectacle for the Ages
 "M352a": ("The grand melee is held in central Coerthas, outside the city.", "A Spectacle for the Ages", "Lucia informs you that the grand melee is to be held in [[Coerthas Central Highlands|central Coerthas]], just outside the city."),
 "M352b": ("General Raubahn swept aside all comers and challenged you to single combat.", "A Spectacle for the Ages", "General of the [[Immortal Flames]], the Bull of Ala Mhigo himself, swept aside all comers and challenged you to single combat."),
 "M352c": ("Aymeric proclaims victory for Ishgard.", "A Spectacle for the Ages", "It was then that Ser [[Aymeric]], raising both sword and voice to the heavens, proclaimed victory for Ishgard, for the day was theirs."),
 "M352d": ("You bear House Fortemps's colors into battle.", "A Spectacle for the Ages", "we believe the men would find it inspiring if you bore the colors of House Fortemps into battle."),
 "M352e": ("The melee is opened in the Eorzean Alliance's name.", "A Spectacle for the Ages", "Brave men and women of the Eorzean Alliance. Let the grand melee begin!"),
 # #353 For Those We Can Yet Save
 "M353a": ("Honoroit, Emmanellain's manservant, has fully recovered.", "For Those We Can Yet Save", "[[Honoroit]], Lord [[Emmanellain]]'s manservant, has made a full recovery and is eager to resume his duties."),
 "M353b": ("Aymeric orders the conference reconvened with Vidofnir.", "For Those We Can Yet Save", "Reconvene the conference and summon Vidofnir to Falcon's Nest."),
 "M353c": ("Aymeric and Vidofnir speak of peace.", "For Those We Can Yet Save", "Ser Aymeric and [[Vidofnir]] come together and speak of peace"),
 "M353d": ("Estinien drives his lance into Vidofnir's back.", "For Those We Can Yet Save", "[[Estinien]] leaps down from on high and drives his lance into Vidofnir's back"),
 "M353e": ("Nidhogg's eyes are fused to Estinien, who speaks with a wyrm's voice.", "For Those We Can Yet Save", "two massive, twitching [[Eyes of Nidhogg|eyes]] fused to his arm and shoulder … And when he speaks, it is not with the voice of a man, but a wyrm."),
 "M353f": ("He declares the final chorus nigh.", "For Those We Can Yet Save", "The final chorus is nigh, and all will be held to account!"),
 "M353g": ("Vidofnir is carried to Anyx Trine to be cared for.", "For Those We Can Yet Save", "The dragon was spirited away to Anyx Trine to receive care from her brethren."),
 "M353h": ("Edmont puts Emmanellain at his brother's disposal.", "For Those We Can Yet Save", "Emmanellain—you will place yourself at your brother's disposal. He will be glad of your assistance."),
 # #354 Causes and Costs
 "M354a": ("Though Aymeric and Ishgard may sacrifice Estinien to slay Nidhogg, Alphinaud will not.", "Causes and Costs", "Even if Ser [[Aymeric]] and all of [[Ishgard]] are willing to sacrifice [[Estinien]] to slay [[Nidhogg]], he is not."),
 "M354b": ("Alphinaud will not sacrifice friends for a cause.", "Causes and Costs", "I do not want to be a man who sacrifices his friends and family for a cause."),
 "M354c": ("Alphinaud expects Nidhogg to lead the Horde, and Aymeric to do what he must.", "Causes and Costs", "When Nidhogg leads the Horde into battle, Ser Aymeric and his forces will do what they believe must be done."),
 "M354d": ("Krile felt the wyrm's hatred about Estinien even before his change.", "Causes and Costs", "Even before his transformation, I could feel the wyrm's hatred swirling about Estinien."),
 "M354e": ("Nidhogg cries for vengeance, and his kin raise the final chorus.", "Causes and Costs", "For in those twilight hours did Nidhogg cry out for vengeance, and his brethern raise their voices for the final chorus of the Dragonsong war."),
 "M354g": ("Papalymo warns Yda not to place her faith in them too soon.", "Causes and Costs", "Do not be so eager to place your faith in them."),
 # #355 The Man Within
 "M355a": ("Y'shtola and Krile conclude Estinien's spirit may survive within Nidhogg's will.", "The Man Within", "concluding at last that Estinien's spirit may indeed have survived, having apparently been enveloped but not consumed by Nidhogg's vengeful will."),
 "M355b": ("Alphinaud thinks removing Nidhogg's eyes from the armor could free Estinien.", "The Man Within", "Alphinaud speculates that removing the great wyrm's [[Eyes of Nidhogg|eyes]] from the dragoon's armor could potentially free him."),
 "M355c": ("Krile warns his would-be savior might become Nidhogg's next host.", "The Man Within", "his would-be savior might become Nidhogg's next host"),
 "M355d": ("Nidhogg's shade, in the Azure Dragoon's flesh, spilled the blood of his own kind.", "The Man Within", "But the lingering shade of Nidhogg, clad in the flesh of the Azure Dragoon, did mark the occasion by spilling the blood of his own kind."),
 "M355e": ("Fear turned to fury, and the call to arms rang out anew.", "The Man Within", "And when fear gave way to fury, the call to arms rang out anew:"),
 # #356 An Ally for Ishgard
 "M356a": ("Aymeric believes only Hraesvelgr, Nidhogg's brood-brother, can stand against the shade.", "An Ally for Ishgard", "the lord commander believes that there is only one being capable of standing against the vengeful shade—Nidhogg's own brood-brother, [[Hraesvelgr]]."),
 "M356b": ("No mortal force can repel Nidhogg now that he has both eyes.", "An Ally for Ishgard", "now that Nidhogg is possessed of both his eyes, no mortal force we can muster will repel him."),
 "M356c": ("Aymeric says the battle with Nidhogg will end his tenure as acting head of church and state.", "An Ally for Ishgard", "the battle with Nidhogg will mark the end of my tenure as the acting head of church and state."),
 "M356d": ("Estinien reported Hraesvelgr's unwillingness to meddle in men's affairs.", "An Ally for Ishgard", "Estinien's report was most particular about Hraesvelgr's unwillingness to involve himself in the affairs of men."),
 "M356e": ("Vidofnir's wound was deep but not mortal.", "An Ally for Ishgard", "The thrust was deep, but not mortal. I will heal in time."),
 "M356f": ("Vidofnir thinks her sire will refuse.", "An Ally for Ishgard", "Folly. Thou know'st as well as I how he will answer."),
 # #357 Winning Over the Wyrm
 "M357a": ("Hraesvelgr says men's treacherous forefathers tore down the bridge between man and dragon.", "Winning Over the Wyrm", "a bridge which thy treacherous forefathers saw fit to tear down, as thou well knowest."),
 "M357b": ("Aymeric admits his father corrupted himself with a primal's power, and he asked you to slay him.", "Winning Over the Wyrm", "When my father corrupted himself and his followers with the power of a primal, I beseeched the Warrior of Light to slay him"),
 "M357c": ("Hraesvelgr bore Ysayle because she sought to balance her past sins.", "Winning Over the Wyrm", "The child did lament her past sins, and sought to balance the scales with her remaining days."),
 "M357d": ("Only when Midgardsormr appears does Hraesvelgr agree to test you.", "Winning Over the Wyrm", "it is not until [[Midgardsormr]] himself appears that Hraesvelgr finally assents to test you and your companions' resolve."),
 "M357e": ("Hraesvelgr pledges to aid you against Nidhogg.", "Winning Over the Wyrm", "Hraesvelgr commends you and your companions for your unwavering determination, and pledges to aid you in the coming battle with [[Nidhogg]]."),
 "M357f": ("A roar signals the Dravanian Horde's advance.", "Winning Over the Wyrm", "Scarcely have the words left his lips, however, when a thunderous roar echoes across the sky, signaling the advance of the [[Dravanian Horde]]."),
 "M357g": ("Hraesvelgr lets his children aid you, and will warn Ishgard of his brood-brother's coming.", "Winning Over the Wyrm", "I permit my children to offer or deny thee aid as they see fit; to warn thy people of my brood-brother's coming."),
 # #358 An End to the Song
 "M358a": ("Hraesvelgr tries in vain to turn Nidhogg from vengeance.", "An End to the Song", "who attempts in vain to persuade his brother from his vengeful course."),
 "M358b": ("Hraesvelgr falls beaten onto the bridge.", "An End to the Song", "The city's defenders watch transfixed as Hraesvelgr tumbles onto the bridge, beaten and bloody, Ishgard's fate seemingly sealed."),
 "M358c": ("Hraesvelgr has given you half his power.", "An End to the Song", "only to learn that his fallen sibling has entrusted you with a gift: one half of his power."),
 "M358d": ("You subdue Nidhogg's shade.", "An End to the Song", "You have succeeded in subduing Nidhogg's shade."),
 "M358e": ("You tear Nidhogg's eyes from Estinien and cast them into the abyss.", "An End to the Song", "With one final heave, you succeed in separating man and wyrm, and for an instant you glimpse Nidhogg's disembodied spirit, before casting his eyes into the abyss."),
 "M358f": ("Nidhogg's spirit is undone by mortal will.", "An End to the Song", "Undone by mortal will. Whither now...?"),
 "M358g": ("Estinien lives, and Aymeric bears him back to Ishgard.", "An End to the Song", "He lives. ah, Estinien, my ill-fated friend. … you watch as Ser [[Aymeric]] bears him back to Ishgard."),
 "M358h": ("The Horde scatters after its master falls.", "An End to the Song", "The Horde have sensed the fall of their master, and scattered to the winds."),
 # #359 Heroes of the Hour
 "M359a": ("Alphinaud counts freeing Estinien the greater feat.", "Heroes of the Hour", "[[Alphinaud]] praises you for your epochal victory over [[Nidhogg]], but admits that freeing [[Estinien]] felt the greater accomplishment."),
 "M359b": ("Estinien has not yet woken.", "Heroes of the Hour", "[[Lucia]] informs you that Estinien has yet to regain consciousness."),
 "M359c": ("Estinien's mind and body were held hostage for many days.", "Heroes of the Hour", "But as you know, Estinien's mind and body were held hostage for many days."),
 "M359e": ("Alphinaud sits at Estinien's bedside.", "Heroes of the Hour", "When he begged to sit at Estinien's side, I could not well refuse him."),
 # #360 Litany of Peace
 "M360a": ("Aymeric abolishes the archbishops' thousand-year rule, opening the way to a republic.", "Litany of Peace", "Echoing Estinien's resolve, Ser Aymeric finally moves to abolish the thousand-year rule of the archbishops, paving the way for a new republic."),
 "M360b": ("Ishgard is now governed by a House of Commons and a House of Lords, and Aymeric is elected to the Lords' highest seat.", "Litany of Peace", "[[Ishgard]]'s governance is placed in the hands of a newly formed House of Commons and House of Lords. And though Ser Aymeric would like nothing more than to lay down the reins of state, he soon finds himself elected to the highest seat in the latter."),
 "M360c": ("Estinien lays down the mantle of Azure Dragoon, his hunt at an end.", "Litany of Peace", "Lord Commander, my hunt is at an end. I would lay down the mantle of Azure Dragoon."),
 "M360d": ("Estinien's hatred began when Nidhogg slew his family.", "Litany of Peace", "the hatred I felt after Nidhogg slew my family, when no path remained save vengeance against dragonkind."),
 "M360e": ("Aymeric and Estinien were the only survivors of a company a dragon attacked.", "Litany of Peace", "our company was set upon by a dragon, and we were the only two to survive."),
 "M360f": ("Estinien has disappeared, and Aymeric asks you to carry him a message.", "Litany of Peace", "He then reveals that Estinien has disappeared, and asks that you give him a message should your paths ever chance to cross."),
 "M360h": ("Elidibus tells the Warriors' leader that the others will play their part, as they will theirs.", "Litany of Peace", "They will play their part, and we will play ours..."),
 "M360i": ("The Warriors' leader catches Alisaie eavesdropping, and Thancred intervenes.", "Litany of Peace", "notices Alisaie eavesdropping and attacks her but is interrupted by Thancred."),
 "M360j": ("You escort Hraesvelgr back to Zenith on Midgardsormr's wings.", "Litany of Peace", "borrow [[Midgardsormr]]'s wings to escort [[Hraesvelgr]] back to [[Zenith]]"),
 # #361 Promises Kept
 "M361a": ("Aymeric, newly lord speaker of the House of Lords, invites you to dine at his estate.", "Promises Kept", "fresh from his appointment as lord speaker of the House of Lords, has extended to you a formal invitation to dine with him at his estate."),
 "M361b": ("Aymeric is lord speaker of the House of Lords and lord commander of the Temple Knights.", "Promises Kept", "lord speaker of the House of Lords, lord commander of the Temple Knights"),
 "M361c": ("The wounded maiden is Alisaie, Alphinaud's twin, who long ago parted from her brother.", "Promises Kept", "The maiden is revealed to be none other than [[Alisaie]], [[Alphinaud]]'s twin sister, who had long ago decided to part ways with her brother."),
 "M361d": ("Thancred, tracking the Warriors of Darkness, found Alisaie on their trail too.", "Promises Kept", "Thancred explains that after tracking the [[Warriors of Darkness]] for some time, he discovered that she too had attempted to learn more of the enigmatic adventurers."),
 "M361e": ("Alisaie, struck by a poisoned arrow, is near death.", "Promises Kept", "Struck by a poisoned arrow as they fled, Alisaie now teeters on the brink of death"),
 "M361f": ("Alisaie warns that Garuda will soon be summoned in Xelphatol, to be slain by the Warriors of Darkness.", "Promises Kept", "she musters the strength to warn you of [[Garuda]]'s imminent summoning in [[Xelphatol]]—and of the [[primal]]'s planned death at the hands of the Warriors of Darkness."),
 "M361g": ("The Warriors of Darkness conspire with the Ascians to goad the Ixal into summoning.", "Promises Kept", "The Warriors of Darkness are conspiring with the [[Ascians]] to goad the [[Ixal]] into summoning their patron deity"),
 "M361h": ("Ishgard's Lords and Commons offer the Scions patronage.", "Promises Kept", "The Lords and Commons agree on very little, but not a soul in either house begrudges your order this offer of patronage."),
 # #362 Shadows of the First
 "M362b": ("You lay low the Ixali occultist leading the summoning.", "Shadows of the First", "you confront the Ixali occultist overseeing the summoning ritual, and in a pitched battle manage to lay him low"),
 "M362c": ("With the ritual unfinished, Garuda is no longer a threat.", "Shadows of the First", "So they were unable to see the ritual to its completion... Then Garuda is no longer a threat"),
 "M362d": ("The Warriors' world held far more Light than Dark.", "Shadows of the First", "But not all worlds hold Light and Dark in equal measure. In ours, the power of Light was greater by far."),
 "M362e": ("The Warriors joined hands with their former enemies to come to the Source.", "Shadows of the First", "And so we joined hands with our former enemies, and with their aid came here...to the Source."),
 "M362f": ("They intend another Umbral Calamity to break down the barriers between worlds.", "Shadows of the First", "Here, they intend to bring about another Umbral Calamity, for only through such unbridled destruction may the barriers between planes be broken down"),
 "M362g": ("Their leader says only the Ardor can save their home.", "Shadows of the First", "For there is but one way to restore the balance and save our home: the Ardor."),
 "M362h": ("He asks whether you are prepared to do whatever it takes.", "Shadows of the First", "We are prepared to do whatever it takes! Are you?"),
 "M362i": ("Alphinaud vows the sacrifice ends here.", "Shadows of the First", "The sacrifice, the loss—it ends here."),
 # #363 Two Sides of a Coin
 "M363a": ("Alisaie has regained consciousness.", "Two Sides of a Coin", "I am pleased to report that she has regained consciousness."),
 "M363b": ("Thancred and Alisaie found evidence that the Ascians keep crystals flowing to the beast tribes.", "Two Sides of a Coin", "Alisaie and I have uncovered evidence that the Ascians have been manipulating certain parties to ensure that a constant stream of crystals flows into the hands of the beast tribes."),
 "M363c": ("An Ascian observed that the powerless will turn to another god when the old ones fail.", "Two Sides of a Coin", "The Ascian himself observed that once the powerless realize that the old gods have failed them, they will have little recourse but to look to a new one."),
 "M363d": ("Y'shtola and Krile go to Xelphatol to learn the Ixal's source.", "Two Sides of a Coin", "Agreed. Krile and I shall journey to Xelphatol and learn what we can of the Ixal's source."),
 "M363f": ("Urianger reports the kobolds may soon summon Titan again.", "Two Sides of a Coin", "the [[kobolds]] of [[Vylbrand]] are rumored to be on the verge of summoning [[Titan]] once more"),
 "M363g": ("Alisaie asks Urianger to research the Warriors' claims.", "Two Sides of a Coin", "I would ask that you research this for us."),
 "M363h": ("The Scions reach Vylbrand in the nick of time.", "Two Sides of a Coin", "It would seem that the Scions of the Seventh Dawn have arrived in Vylbrand in the nick of time."),
 # #364 Unlikely Allies
 "M364a": ("Commander Bloeidin confirms the kobolds have grown more aggressive.", "Unlikely Allies", "Commander [[Bloeidin]] confirms [[Urianger]]'s report that the [[kobolds]] of [[U'Ghamaro]] have grown more aggressive of late."),
 "M364b": ("The kobold child is Ga Bu, of the 620th Order.", "Unlikely Allies", "Pickman Ga Bu of the 620th Order!"),
 "M364c": ("Ga Bu's parents spoke against the patriarch and were taken away.", "Unlikely Allies", "Ga Bu goes on to explain that his parents, along with other like-minded kobolds, spoke out against the patriarch's plans, only to be taken away to serve as"),
 "M364d": ("The patriarch means to summon the Great Father again.", "Unlikely Allies", "The patriarch is going to summon the Great Father again, and you have to stop him"),
 "M364e": ("The Scions will infiltrate the stronghold, secure the crystals and free the prisoners.", "Unlikely Allies", "declares that the [[Scions]] will attempt to infiltrate the kobold stronghold, secure the crystals, and free the prisoners."),
 # #365 The Beast That Mourned at the Heart of the Mountain
 "M365a": ("The kobolds' crystals were smuggled out of Ishgard.", "The Beast That Mourned at the Heart of the Mountain", "the crate must have been smuggled out of Ishgard and transported across the sea"),
 "M365b": ("Ga Bu's parents and the other prisoners have already been executed.", "The Beast That Mourned at the Heart of the Mountain", "they and the other prisoners have already been executed"),
 "M365c": ("Ga Bu's anguish birthed a primal as surely as a ritual.", "The Beast That Mourned at the Heart of the Mountain", "His anguish and despair have served to birth a primal, just as surely as would the supplications of the faithful."),
 "M365d": ("The Titan born of the child's anguish must be faced.", "The Beast That Mourned at the Heart of the Mountain", "the Titan born of the child's anguish is nevertheless a threat which cannot be ignored"),
 "M365e": ("Titan is no more.", "The Beast That Mourned at the Heart of the Mountain", "Nevertheless, Titan is no more, and you are free to return to Camp Overlook and the others."),
 "M365f": ("Ga Bu may have fallen under the primal's influence.", "The Beast That Mourned at the Heart of the Mountain", "Alphinaud gives voice to the unhappy possibility that Ga Bu may have fallen prey to the primal's influence."),
 # #366 Beneath a Star-filled Sky
 "M366a": ("Alisaie entrusts Ga Bu to Commander Bloeidin's care.", "Beneath a Star-filled Sky", "she surrenders him into Commander Bloeidin's care, entreating him to show the young [[kobold]] every kindness."),
 "M366b": ("Ga Bu may one day recover.", "Beneath a Star-filled Sky", "Ga Bu may one day recover from his trauma."),
 "M366c": ("A Rejoining would kill everyone on a reflection of the Source.", "Beneath a Star-filled Sky", "a passage which suggests that a [[Rejoining]] would result in the deaths of all those living upon a reflection of the [[The Source|Source]]"),
 "M366d": ("The Ishgardian smugglers are remnants of the Ivy's network.", "Beneath a Star-filled Sky", "the Ishgardian smugglers supplying the beast tribes with crystals have been identified as remnants of the criminal network established by [[Eline Roaille]]—the infamous [[Garlean]] spymaster, the Ivy."),
 "M366e": ("They also sent crystals to refugees fighting for Ala Mhigan liberation.", "Beneath a Star-filled Sky", "refugees devoted to the cause of [[Ala Mhigo|Ala Mhigan]] liberation"),
 "M366f": ("The smugglers worked for a man in black robes.", "Beneath a Star-filled Sky", "a man in black robes."),
 "M366g": ("Alisaie treats Urianger with deep suspicion.", "Beneath a Star-filled Sky", "her words and actions seem to indicate a deep-seated suspicion. But why?"),
 "M366h": ("A masked man tells the Warriors' leader the Ardor is not the Ascians' alone to invoke.", "Beneath a Star-filled Sky", "the power to invoke the Ardor belongeth not unto the Ascians alone."),
 # #367 When We Were Free
 "M367a": ("Members of the Ala Mhigan Resistance in Little Ala Mhigo received large crystal shipments.", "When We Were Free", "members of the Ala Mhigan Resistance operating here have taken receipt of several large shipments of crystals"),
 "M367b": ("The Griffin is a masked revolutionary leader who has rallied many refugees.", "When We Were Free", "a revolutionary leader who always wears a mask in public. A charismatic figure, he seems to have inspired a good many of the refugees to rally to his standard"),
 "M367c": ("The Griffin and his Masks are said to have a secret weapon against the Garleans.", "When We Were Free", "there are even rumors that he and his Masks have a secret weapon they plan to use against the [[Garlean]] occupiers"),
 "M367d": ("The Masks most likely received the crystals from Ishgard.", "When We Were Free", "it is highly likely that the Masks are the group who received the shipment of crystals from [[Ishgard]]"),
 "M367e": ("At Qarn you find Yda and Papalymo.", "When We Were Free", "and catches sight of two very familiar faces: [[Yda]] and [[Papalymo]]!"),
 "M367f": ("Yda and Papalymo fled Ul'dah with old Resistance friends and have helped them since.", "When We Were Free", "they slipped out of the city with the aid of some old friends from the Resistance"),
 "M367g": ("The Crystal Braves were denounced and Raubahn reinstated, clearing the Scions.", "When We Were Free", "the [[The Crystal Braves|Crystal Braves]] had been denounced and General [[Raubahn]] reinstated"),
 "M367h": ("The man at the temple was an impersonator, not the Griffin.", "When We Were Free", "the man you saw was not in fact the Griffin, but an impersonator"),
 "M367j": ("Papalymo's letter to the Scions was likely intercepted by the Masks.", "When We Were Free", "it seems likely that his missive was intercepted by the Masks"),
 # #368 Honorable Heroes
 "M368a": ("The impostor speaks with the Griffin's voice and procured the crystals at his behest.", "Honorable Heroes", "But I speak with his voice, and it was at his behest that we procured those crystals."),
 "M368b": ("The Masks traded the crystals to the Amalj'aa for their aid.", "Honorable Heroes", "In exchange for crystals to summon their god, they will aid us in the fight for Ala Mhigan liberation."),
 "M368c": ("Yda names the god Ifrit and fears for the Resistance.", "Honorable Heroes", "When people find out you helped the lizardmen summon Ifrit, they'll turn on the Resistance!"),
 "M368d": ("Many joined the Masks because you saved them.", "Honorable Heroes", "a great many who have joined us did so because you saved them"),
 "M368e": ("Papalymo forbids Yda to join the Masks.", "Honorable Heroes", "You cannot seriously be contemplating taking up arms with that band of cutthroats?"),
 "M368f": ("Papalymo and Yda will search for the cache.", "Honorable Heroes", "If there a cache to be found, Yda and I will find it."),
 # #369 One Life for One World
 "M369a": ("The crystals are said to be in Zahar'ak, where the Amalj'aa may summon Ifrit.", "One Life for One World", "where the [[Amalj'aa]] are presumably preparing to summon [[Ifrit]]"),
 "M369b": ("The masked man calls himself author of the drama to come.", "One Life for One World", "the drama of which I am author, gods forgive me, shall at last be performed."),
 "M369c": ("In the Bowl of Embers the Warriors of Darkness come to kill you, to bring about a Calamity.", "One Life for One World", "This time, however, they are come not to slay a primal, but you, the Warrior of Light, in the belief that your death will plunge the realm into chaos and bring about another Umbral Calamity."),
 "M369d": ("Urianger breaks your chains, revealed as a double agent who manipulated the Warriors.", "One Life for One World", "[[Urianger]] appears from nowhere, and breaks the aetheric chains around you, revealing himself to have manipulated the Warriors of Darkness as a double agent."),
 "M369e": ("The masked man is Urianger.", "One Life for One World", "By the Twelve—Urianger!"),
 "M369f": ("The Warriors of Darkness are already dead.", "One Life for One World", "these desperate men and women of [[the First]] are already dead"),
 "M369g": ("They were adventurers chosen by their Mothercrystal as Warriors of Light, whose world fell to ruin anyway.", "One Life for One World", "their leader declares that they were humble adventurers chosen by the Mothercrystal to serve as Warriors of Light. They did everything that was asked of them, and yet, for all their efforts, and all their many triumphs, their world still fell to ruin."),
 "M369h": ("Urianger orchestrated events to grant Minfilia her freedom.", "One Life for One World", "the [[Archon]] confesses to having orchestrated events to grant Minfilia her freedom"),
 "M369i": ("Minfilia says Hydaelyn has freed her to serve as Her emissary.", "One Life for One World", "She has grown strong enough to set me free, that I might serve as Her emissary."),
 "M369j": ("She will go to the Warriors' world and take its rising Light into herself.", "One Life for One World", "I will hie me to your world and there take unto myself the Light which riseth even now to drown it"),
 "M369k": ("The Warriors ask to be taken home, and you bid them and Minfilia farewell.", "One Life for One World", "Their journey at an end, the broken Warriors of Light have a simple request for your departing friend"),
 "M369l": ("Minfilia promises to return one day.", "One Life for One World", "Someday, when I have found a way to free this star from Her sorrow, I promise you I shall repay the favor."),
 # #370 An Ending to Mark a New Beginning
 "M370a": ("Thancred goes back alone to secure the crystals in Zahar'ak.", "An Ending to Mark a New Beginning", "Leave them to me. I will go back into Zahar'ak and secure them."),
 "M370b": ("Alisaie cannot condone Urianger's deception.", "An Ending to Mark a New Beginning", "Alisaie, however, cannot bring herself to condone his actions."),
 "M370c": ("Papalymo says it is past time he and Yda rejoined the Scions.", "An Ending to Mark a New Beginning", "I believe it is past time Yda and I rejoined the Scions."),
 "M370d": ("Gundobald knew Yda's father, who fought in the revolution against the King of Ruin.", "An Ending to Mark a New Beginning", "who is apparently acquainted with both Yda and [[Curtis Hext|her father]], with whom he fought in the revolution against the [[King Theodoric|King of Ruin]] twenty years ago."),
 "M370e": ("Yda's work for the Circle of Knowing and the Scions required absolute secrecy.", "An Ending to Mark a New Beginning", "her involvement in the [[The Circle of Knowing|Circle of Knowing]] and its successor, the Scions of the Seventh Dawn, necessitated absolute secrecy"),
 "M370f": ("Alphinaud has each Scion pursue what best keeps the realm safe, rather than a strict hierarchy.", "An Ending to Mark a New Beginning", "Rather than holding to a strict hierarchy, he believes that each member should be allowed to pursue whatever activities they think would best serve to ensure the safety and security of the realm."),
 "M370g": ("Krile and Alisaie are welcomed as full Scions.", "An Ending to Mark a New Beginning", "[[Krile]] and Alisaie are welcomed as a fully fledged Scions"),
 "M370h": ("Urianger is haunted by guilt over Minfilia's fate.", "An Ending to Mark a New Beginning", "plainly haunted by feelings of guilt towards his role in [[Minfilia Warde|Minfilia's]] fate"),
 "M370i": ("Papalymo asks to keep Tupsimati, as Louisoix's disciple.", "An Ending to Mark a New Beginning", "My friends. If I may, I would ask that you entrust Tupsimati to me. … as Master Louisoix's disciple, I would keep it close at hand."),
 "M370j": ("Elidibus gives the Griffin the Eyes of Nidhogg, judging him most deserving.", "An Ending to Mark a New Beginning", "The Eyes of Nidhogg. Many were the candidates considered, but by your deeds, you have proven yourself the most deserving."),
 "M370l": ("Every surviving senior Scion is back at the Rising Stones.", "An Ending to Mark a New Beginning", "With every surviving senior Scion now safely back at the Rising Stones"),
 "M370k": ("Elidibus calls a world without equilibrium a void in waiting.", "An Ending to Mark a New Beginning", "a world bereft of equilibrium is but a void in waiting."),
 # #371 Tidings from Gyr Abania
 "M371a": ("Alphinaud proposes electing a coordinator of operations as Minfilia's successor.", "Tidings from Gyr Abania", "Thus I propose we elect a successor to Minfilia—not to serve as a fully fledged Antecedent, perhaps, but as a coordinator of operations."),
 "M371b": ("A Resistance messenger warns that the masked Griffin is set on a dangerous course.", "Tidings from Gyr Abania", "one of the Resistance leaders—a masked man known as the [[The Griffin|Griffin]]—has embarked upon a course"),
 "M371c": ("The Griffin means to assault the Wall from the Ala Mhigan side.", "Tidings from Gyr Abania", "He means to assault Baelsar's Wall from the Ala Mhigan side."),
 "M371d": ("He wants the fires of war to spread to Eorzea.", "Tidings from Gyr Abania", "From what I understand, he wants the fires of war to spread to Eorzea."),
 "M371e": ("Y'shtola sends you to urge Aymeric to send an envoy.", "Tidings from Gyr Abania", "You will be our voice in Ishgard. Explain the situation to Ser Aymeric, and encourage him to send an envoy."),
 "M371f": ("Aymeric agrees to send an envoy to the Alliance council.", "Tidings from Gyr Abania", "the lord commander soon agrees to send an envoy to the Alliance council."),
 "M371h": ("The Diamond Forge artisans measure you for clothes.", "Tidings from Gyr Abania", "After being ambushed by the Diamond Forge artisans and their measuring tapes"),
 # #372 An Envoy for Ishgard
 "M372a": ("Aymeric will be Ishgard's envoy, with the House of Commons' agreement.", "An Envoy for Ishgard", "my counterpart in the House of Commons agreed that I should act as Ishgard's envoy."),
 "M372b": ("Emmanellain is the new garrison commander at Camp Dragonhead, with Honoroit's practical help.", "An Envoy for Ishgard", "invite you to meet the newly appointed garrison commander. Much to your surprise, you discover that it is none other than Ser [[Emmanellain]]—ably abetted by the rather more practically minded [[Honoroit]]."),
 "M372c": ("Aymeric readies the garrison against trouble in the Black Shroud.", "An Envoy for Ishgard", "Given the trouble brewing in the Black Shroud, I would see that the garrison is ready to defend the border."),
 "M372d": ("Emmanellain doubts he will feel worthy of the post.", "An Envoy for Ishgard", "I doubt I'll ever feel worthy to sit where he sat..."),
 # #373 An Allied Decision
 "M373b": ("Raubahn warns the fighting will spill into the Black Shroud.", "An Allied Decision", "the resulting fighting is all but certain to spill over into the Black Shroud..."),
 "M373c": ("Aymeric asks leave to deploy an Ishgardian force in Gridania.", "An Allied Decision", "Elder Seedseer—I do hereby request leave to deploy a defensive force within the borders of Gridania."),
 "M373d": ("Yugiri offers the Alliance her seasoned shinobi.", "An Allied Decision", "We are few, but our most seasoned shinobi are at your disposal."),
 "M373e": ("The council agrees to reinforce Gridania's border.", "An Allied Decision", "the council members agree that the [[Gridania]]n border must be preemptively reinforced."),
 "M373f": ("Alphinaud fears the Alliance is giving the Griffin what he wants.", "An Allied Decision", "In making ready for war, is the Alliance not granting the Griffin the very thing he desired?"),
 "M373g": ("Riol reports that the missing Scions have been found.", "An Allied Decision", "I was glad to hear from Riol that the missing Scions have now been found."),
 "M373h": ("Alphinaud says the intelligence comes from the Resistance's inner circle.", "An Allied Decision", "Our information comes directly from a member of the Resistance's inner circle, and we have no cause to doubt its veracity."),
 # #374 Griffin, Griffin on the Wall
 "M374a": ("Papalymo, Yda, Thancred and Yugiri go through the tunnels to confront the Griffin.", "Griffin, Griffin on the Wall", "it is decided that [[Papalymo]], [[Yda]], [[Thancred]], and [[Yugiri]] will brave the secret tunnels"),
 "M374b": ("The Griffin's soldiers attack the Wall in Grand Company uniforms.", "Griffin, Griffin on the Wall", "Scouts report that the Griffin has begun his assault, his soldiers apparently clad in [[Grand Company]] uniforms..."),
 "M374c": ("Alphinaud sees the Wall was bait.", "Griffin, Griffin on the Wall", "The Wall was never the Griffin's target—it was bait."),
 "M374d": ("The Griffin is Ilberd, the disgraced captain of the Crystal Braves.", "Griffin, Griffin on the Wall", "Beneath the mask, the Griffin is revealed to be none other than [[Ilberd]], the disgraced captain of the [[Crystal Braves]]."),
 "M374e": ("Ilberd's ritual summons a primal empowered by Ala Mhigan desperation and Nidhogg's eyes.", "Griffin, Griffin on the Wall", "a ritual to summon a nightmarish [[primal]] empowered by [[Ala Mhigo|Ala Mhigan]] desperation and the might of [[Nidhogg]]'s [[Eyes of Nidhogg|eyes]]."),
 "M374f": ("Ilberd's death completes the ritual.", "Griffin, Griffin on the Wall", "His death completed the ritual. The primal is taking shape."),
 "M374g": ("Papalymo's forbidden magick swallows him and seals the primal in a cocoon of light.", "Griffin, Griffin on the Wall", "the incantation swallows Papalymo and encases the newborn entity in a vast cocoon of light."),
 "M374h": ("Papalymo works the magick with Tupsimati.", "Griffin, Griffin on the Wall", "Papalymo steps forward with [[Tupsimati]], and grimly begins to weave a forbidden magick of confinement..."),
 "M374i": ("You escape on Hilda's airship.", "Griffin, Griffin on the Wall", "You barely have time to escape on [[Hilda]]'s [[airship]]"),
 "M374j": ("Yda is broken by the loss of her dearest friend.", "Griffin, Griffin on the Wall", "Stunned by the unexpected summoning and the loss of her dearest friend, Yda's irrepressible spirit seems to have been broken at last."),
 "M374k": ("Ilberd calls on a deity more terrible than the black wyrm of the Calamity.", "Griffin, Griffin on the Wall", "which is why I will call upon a deity more terrible than the very black wyrm of the Calamity itself!"),
 # #375 Louisoix's Finest Student
 "M375a": ("Alphinaud breaks the news of Papalymo's passing.", "Louisoix's Finest Student", "Alphinaud finally breaks the news of [[Papalymo]]'s passing."),
 "M375b": ("Ilberd's primal will not be contained forever.", "Louisoix's Finest Student", "the [[primal]] summoned by [[Ilberd]] will not be contained forever..."),
 "M375c": ("Y'shtola and Krile will inspect the cocoon.", "Louisoix's Finest Student", "We must inspect the cocoon of light, and ascertain the state of the primal trapped within."),
 "M375d": ("No one knows yet how Ilberd came by Nidhogg's eyes.", "Louisoix's Finest Student", "I have as yet been unable to explain how Ilberd came to possess Nidhogg's eyes."),
 "M375e": ("Urianger says the pupil followed the master even unto the grave.", "Louisoix's Finest Student", "Thus did the pupil follow in the footsteps of the master...even unto the grave."),
 "M375f": ("Alphinaud calls for preparations to face Ilberd's creation.", "Louisoix's Finest Student", "We must begin preparations to face Ilberd's accursed creation without delay."),
 # #376 The Obvious Solution
 "M376a": ("Y'shtola has confirmed a primal in the cocoon.", "The Obvious Solution", "Archon Y'shtola has confirmed the presence of a primal entity..."),
 "M376b": ("A Garlean airship that approached the cocoon was destroyed.", "The Obvious Solution", "A Garlean airship was observed making an approach, but the vessel was destroyed when it drew near."),
 "M376c": ("Nero, a former tribunus of the XIVth Legion, proposes Omega against the primal.", "The Obvious Solution", "Nero tol Scaeva, former tribunus of the XIVth Legion of the Garlean Empire. … I speak, of course, of Omega."),
 "M376d": ("Nero claims to have restored the Ultima Weapon.", "The Obvious Solution", "the mechanical genius who restored the Ultima Weapon to full operational capacity!"),
 "M376e": ("Nero studied beside Cid at the Academy.", "The Obvious Solution", "All those years studying side by side at the Academy, sharing both trial and triumph."),
 "M376f": ("Omega has lain beneath Carteneau since the Allagans.", "The Obvious Solution", "That hulk has been gathering dust beneath the plains of Carteneau since the Allagans breathed their last!"),
 "M376g": ("The council sends a contingent to Carteneau to take command of Omega.", "The Obvious Solution", "Let the records show that we invest this contingent with the authority to enter Carteneau and take command of Omega."),
 "M376h": ("Alisaie says Nero may be killed if he proves treacherous.", "The Obvious Solution", "If you suspected any foul play from Nero, you would be welcome to kill him."),
 "M376i": ("Alphinaud wonders how Nero learned of the council meeting.", "The Obvious Solution", "not least among them how Nero chanced to learn of the council meeting in the first place."),
 # #377 The Greater Obeisance
 "M377a": ("Alisaie insists Nero never leave her sight.", "The Greater Obeisance", "your sister was adamant that he would never leave her sight."),
 "M377b": ("Gosetsu brings word that his master is in peril and Doma calls Yugiri home.", "The Greater Obeisance", "Our master languishes in dire peril, and Doma calls her daughter home!"),
 "M377c": ("Urianger came to Gosetsu's aid when he collapsed.", "The Greater Obeisance", "Collapsed in the street like an unfed stray, I was, until Lord Urianger came to my aid."),
 "M377e": ("Yugiri stays to play her part in the crisis.", "The Greater Obeisance", "A crisis threatens all within this realm, Eorzean and Doman alike, and I go to play my part in its resolution."),
 "M377f": ("Gosetsu's blade is oathbound against the imperials.", "The Greater Obeisance", "My blade is oathbound to fall upon the ranks of the imperials wheresoever they march!"),
 "M377g": ("Tataru sews a blood pearl charm into your new outfit.", "The Greater Obeisance", "I also sewed in a blood pearl charm to...you know...bring you home."),
 "M377h": ("The Omega contingent assembles at the airship landing.", "The Greater Obeisance", "the [[Omega]] contingent is assembling at the [[airship]] landing."),
 # #378 Fly Free, My Pretty
 "M378a": ("Cid and Nero will rouse Omega while you, Yda and the Domans keep watch.", "Fly Free, My Pretty", "Nero and I will focus on rousing Omega, while"),
 "M378b": ("Nero has been to Omega's control room before.", "Fly Free, My Pretty", "How convenient. ...You've been here before."),
 "M378c": ("An imperial officer, Grynewaht, calls Cid a traitor.", "Fly Free, My Pretty", "I chase down a suspect airship, and who should I find but the traitor"),
 "M378d": ("Omega is expected to seek out and capture the primal at the Wall.", "Fly Free, My Pretty", "Once we release Omega, we can be fairly certain it will attempt to capture the primal at Baelsar's Wall."),
 "M378e": ("Yda launches Omega for Papalymo's sake.", "Fly Free, My Pretty", "You gave too much for us to waste this chance, Papalymo. So this is for you...and me."),
 "M378f": ("Omega's signal falls silent, and Cid reengages its stasis.", "Fly Free, My Pretty", "the signal emanating from the weapon falls silent, prompting Cid to reengage its stasis systems."),
 "M378g": ("Papalymo's spell, bound to his aether, is fading.", "Fly Free, My Pretty", "Papalymo's spell is fading. It was bound to his aether, you see...and if the connection is broken..."),
 "M378h": ("The Empire has long known of Omega.", "Fly Free, My Pretty", "we can be sure that the Empire has long been aware of its existence."),
 # The Far Edge of Fate (cp-hw-3-56)
 "M379a": ("The cocoon hatched as Omega arrived, and a great dragon rose from it.", "The Far Edge of Fate", "the cocoon hatched even as Omega arrived, and from its midst rose a great dragon."),
 "M379b": ("Omega and the primal fell together onto Ala Mhigan soil.", "The Far Edge of Fate", "I saw the pair fall motionless from the sky, coming to rest somewhere on Ala Mhigan soil."),
 "M379c": ("The Domans call the primal Shinryu.", "The Far Edge of Fate", "the Domans were heard to whisper the name … Shinryu"),
 "M379d": ("The Alliance moves to secure the Wall.", "The Far Edge of Fate", "the Alliance now intends to exploit the resulting confusion by moving to secure [[Baelsar's Wall]]."),
 "M379e": ("Omega's stasis was reengaged, so it is useless to the Empire.", "The Far Edge of Fate", "we quickly reengaged Omega's stasis systems"),
 "M379f": ("Aymeric proposes contacting the Resistance in Gyr Abania.", "The Far Edge of Fate", "I humbly submit that the time has come for us to make contact with the Resistance representatives in Gyr Abania."),
 "M379g": ("Yda is not Yda: she is Lyse, the fallen Archon's younger sister.", "The Far Edge of Fate", "revealing at last that she is not Yda at all, but the fallen [[Archon]]'s younger sister, [[Lyse]]."),
 "M379h": ("Her real name is Lyse.", "The Far Edge of Fate", "I'm sorry for lying to you. My real name is Lyse."),
 "M379i": ("Yda died six years ago smuggling refugees out of Ala Mhigo.", "The Far Edge of Fate", "Yda died six years ago, on a mission to smuggle refugees out of Ala Mhigo."),
 "M379j": ("Papalymo brought Lyse Yda's mask as a keepsake, and she chose to take up her sister's work.", "The Far Edge of Fate", "When Papalymo brought me Yda's mask, it was meant as a keepsake. But I decided I wanted to be his new partner; to keep alive all the good that she had done."),
 "M379k": ("Papalymo persuaded the others to keep up the charade.", "The Far Edge of Fate", "'Twas Papalymo who persuaded us to maintain the charade."),
 "M379l": ("Lyse will continue her family's fight for Ala Mhigo.", "The Far Edge of Fate", "...And I choose to continue my family's fight."),
 "M379m": ("Their father fought to overthrow the mad king Theodoric.", "The Far Edge of Fate", "He had fought to overthrow the mad king, Theodoric."),
 "M379n": ("The Wall has fallen to the Alliance, as an officer reports to the Viceroy.", "The Far Edge of Fate", "My lord Viceroy—our scouts have confirmed the preliminary reports. Baelsar's Wall has fallen to the Eorzean Alliance."),
 "M379o": ("The Viceroy, Zenos, has heard the Domans call the primal Shinryu, and expects interesting days.", "The Far Edge of Fate", "My spies tell me the Domans call it"),
 "M379p": ("Zenos expects the coming days to be most interesting.", "The Far Edge of Fate", "Yes...the coming days promise to be most interesting."),
}

# ---- New entities ----------------------------------------------------------------------------------------------------
# The Heavensward cast uses the contract's conventional IDs, so an earlier era's record of the same entity merges with
# these. Arc entries (events) are listed with the arcs below.
ENTITIES = {
 "char-aymeric": "character", "char-lucia": "character", "char-estinien": "character", "char-nidhogg": "character",
 "char-hraesvelgr": "character", "char-vidofnir": "character", "char-krile": "character", "char-matoya": "character",
 "char-artoirel": "character", "char-emmanellain": "character", "char-edmont": "character", "char-honoroit": "character",
 "char-ilberd": "character", "char-elidibus": "character", "char-masked-man": "character", "char-griffin": "character",
 "char-ga-bu": "character", "char-nero": "character", "char-shinryu": "character",
 "char-gosetsu": "character", "char-lyse": "character", "char-zenos": "character",
 "org-warriors-of-darkness": "organization", "org-masks": "organization", "org-ala-mhigan-resistance": "organization",
 "org-house-of-lords": "organization", "org-holy-see": "organization", "org-ascians": "organization",
 "org-dravanian-horde": "organization",
 "evt-the-lost-scions": "event", "evt-falcons-nest-conference": "event", "evt-the-final-chorus": "event",
 "evt-the-warriors-plot": "event", "evt-a-trail-of-crystals": "event", "evt-the-griffins-gambit": "event",
 "evt-waking-omega": "event",
}

# ---- Presentations ---------------------------------------------------------------------------------------------------
PRES = {
 # -- Ishgard
 "char-aymeric": [
   P(G336, None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander. With the archbishop's seat vacant after his father's passing, he has taken on its duties under canon law. "
     "He made public how his father disappeared, and the city is divided: some dispute his account, and many who accept it question how the archbishop was stopped. "
     "He has sent Lucia to Anyx Trine to restore relations with Hraesvelgr's brood.",
     ["M336a", "M336b", "M336c", "M336d"]),
   P(G341, None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander, who has taken on the vacant archbishop's duties. He is recovering from a knife in the dark, "
     "but the attack was only the beginning: fires are spreading through the city.",
     ["M336a", "M336c", "M341f", "M341g", "M341h"]),
   P(G343, None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander and acting head of its church. He opened the Vault to refugees from the fires, and when the True Brothers of the Faith seized it, "
     "he, you and Lord Artoirel stormed it and freed all but one captive, a girl whom Vidofnir caught when a priest threw her from the ledge. "
     "Count Edmont is stepping aside to rid House Fortemps of suspicion that it joined a coup by Aymeric.",
     ["M336a", "M342b", "M343a", "M343b", "M343c", "M343g"]),
   P(G346, None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander and acting head of its church. Vidofnir's rescue of a child gave hope of peace between man and dragon, "
     "and he is arranging a peace conference at Falcon's Nest for her to attend. He wants you there, fearing that Nidhogg, implacably opposed to peace, will try to disrupt it.",
     ["M336a", "M346b", "M346c", "M346d"]),
   P(G351, None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander and acting head of its church. After a protest ended his peace conference at Falcon's Nest in bloodshed, "
     "he means to lift Ishgard's spirits by presenting the Alliance's joint exercises as a grand melee. Some in the streets call him a patricide; "
     "his father, he says, trusted only in himself.",
     ["M336a", "M349e", "M351a", "M351f", "M351e"]),
   P(G353, None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander and acting head of its church. After Ishgard won the grand melee, he reconvened the peace conference at Falcon's Nest, "
     "but as he and Vidofnir spoke of peace, Estinien drove a lance into her back.",
     ["M336a", "M352c", "M353b", "M353c", "M353d"]),
   P(G356, None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander and acting head of its church. Now that Nidhogg has both eyes, no mortal force can repel him, "
     "so Aymeric seeks Nidhogg's brood-brother Hraesvelgr as an ally. He says the battle with Nidhogg will end his tenure as acting head of church and state.",
     ["M356a", "M356b", "M356c"]),
   P(G357, None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander and acting head of its church. At Zenith he admitted that when his father corrupted himself with a primal's power, "
     "he asked you to slay him. Hraesvelgr has pledged to aid you against Nidhogg.",
     ["M356c", "M357b", "M357e"]),
   P(G360, None, "main", "Aymeric",
     "Ser Aymeric, Estinien's oldest friend: they alone survived a dragon's attack on their company. After Nidhogg's fall he abolished the archbishops' thousand-year rule, "
     "and Ishgard is now governed by a House of Commons and a House of Lords. He would have laid down the reins of state, but was elected to the Lords' highest seat. "
     "Estinien has disappeared, and Aymeric has asked you to carry him a message.",
     ["M360a", "M360b", "M360e", "M360f"]),
   P(G361, None, "main", "Aymeric",
     "Ser Aymeric, lord speaker of Ishgard's House of Lords and lord commander of the Temple Knights, since the archbishops' rule was abolished. "
     "He hosted you at last for a long-promised dinner at his estate, and the Lords and Commons offer the Scions their patronage.",
     ["M360a", "M361a", "M361b", "M361h"]),
   P(G373, None, "main", "Aymeric",
     "Ser Aymeric, lord speaker of Ishgard's House of Lords and lord commander of the Temple Knights. With the House of Commons' agreement he went as Ishgard's envoy "
     "to the Alliance council in Gridania, and asked leave to deploy an Ishgardian force there against the Griffin's threatened attack. The council agreed to reinforce the border.",
     ["M361b", "M372a", "M372c", "M373c", "M373e"]),
   P(MS, None, "main", "Aymeric",
     "Ser Aymeric, lord speaker of Ishgard's House of Lords and lord commander of the Temple Knights, and Ishgard's envoy to the Alliance council. "
     "After Omega and the primal fell together in Gyr Abania, he proposed that the Alliance contact the Resistance there.",
     ["M361b", "M372a", "M379b", "M379f"]),
 ],
 "char-lucia": [
   P(G336, None, "main", "Lucia",
     "Sent by Ser Aymeric to Anyx Trine, to treat with Vidofnir and restore relations with Hraesvelgr's brood.",
     ["M336d"]),
   P(G337, None, "main", "Lucia",
     "Ser Aymeric's envoy to Anyx Trine. She told Vidofnir that King Thordan and his knights betrayed and murdered Ratatoskr, a truth Ishgard's leaders hid for a thousand years, "
     "and asked for friendship. Vidofnir must consult her sire before answering.",
     ["M336d", "M337a", "M337b", "M337c"]),
   P(G342, None, "main", "Lucia",
     "Ser Aymeric's envoy to Vidofnir at Anyx Trine. Back in Ishgard she leads the hunt for whoever is setting Ishgard's fires, "
     "which proved to be orchestrated by someone of influence.",
     ["M336d", "M342a", "M342d"]),
   P(G346, None, "main", "Lucia",
     "In Ser Aymeric's service. She was once sent to Ishgard as a foreign spy, but chose instead to pledge herself to its cause and its war. "
     "At Falcon's Nest she oversees a relief to be unveiled at Aymeric's peace conference.",
     ["M346e", "M346f", "M346g"]),
   P(G350, None, "main", "Lucia",
     "Ser Aymeric's first commander, once a foreign spy who chose Ishgard's cause. While a Convictory incident, likely a ruse, drew her away, a protest at Falcon's Nest "
     "ended in bloodshed, and she has suspended the peace conference pending Aymeric's decision.",
     ["M350i", "M346f", "M350a", "M350g"]),
   P(G351, None, "main", "Lucia",
     "Ser Aymeric's first commander, once a foreign spy who chose Ishgard's cause. She has reservations about Aymeric's grand melee: "
     "as a Garlean citizen, it seems, she saw such spectacles rally people to the imperial cause.",
     ["M350i", "M346e", "M346f", "M351c"]),
 ],
 "char-estinien": [
   P(G336, None, "main", "Estinien",
     "The Azure Dragoon, whose body Nidhogg has claimed along with both of the wyrm's eyes.",
     ["M336f"]),
   P(G343, None, "main", "Estinien",
     "The Azure Dragoon, whose body Nidhogg has claimed along with both of the wyrm's eyes. Vidofnir can say nothing of his fate.",
     ["M336f", "M343e"]),
   P(G353, None, "main", "Estinien",
     "The Azure Dragoon, whose body Nidhogg has claimed. At the peace conference at Falcon's Nest he leapt down and drove his lance into Vidofnir's back, "
     "Nidhogg's eyes fused to his arm and shoulder, and declared with a wyrm's voice that the final chorus is nigh.",
     ["M336f", "M353d", "M353e", "M353f"]),
   P(G355, None, "main", "Estinien",
     "The Azure Dragoon, whose body Nidhogg has claimed, and who struck down Vidofnir at Falcon's Nest. Y'shtola and Krile believe his spirit survives, enveloped but not consumed "
     "by the wyrm's will. Alphinaud thinks tearing the eyes from his armor could free him, though Krile warns whoever does might become Nidhogg's next host.",
     ["M353d", "M355a", "M355b", "M355c"]),
   P(G358, None, "main", "Estinien",
     "The Azure Dragoon, whose body Nidhogg had claimed. On the Steps of Faith you subdued Nidhogg's shade, tore the eyes from Estinien's armor and cast them into the abyss. "
     "He lives, and Aymeric bore him back to Ishgard.",
     ["M353d", "M358d", "M358e", "M358g"]),
   P(G359, None, "main", "Estinien",
     "The Azure Dragoon, freed from Nidhogg when you tore the wyrm's eyes from his armor. His mind and body were held hostage for many days, and he has not yet woken; "
     "Alphinaud keeps vigil at his bedside.",
     ["M358e", "M359b", "M359c", "M359e"]),
   P(G360, None, "main", "Estinien",
     "Freed from Nidhogg, who once slew his family; the hatred he felt then mirrored the wyrm's own. He and Aymeric alone survived a dragon's attack on their company. "
     "On waking he laid down the mantle of Azure Dragoon, his hunt at an end, and then disappeared from his sickroom.",
     ["M358e", "M360c", "M360d", "M360e", "M360f"]),
 ],
 "char-nidhogg": [
   P(G336, None, "main", "Nidhogg",
     "A great wyrm whose shade has claimed both his eyes and the Azure Dragoon's body, and is gathering strength.",
     ["M336f"]),
   P(G343, None, "main", "Nidhogg",
     "A great wyrm whose shade has claimed both his eyes and the Azure Dragoon's body. He and his brood have flown for skies unknown.",
     ["M336f", "M343d"]),
   P(G346, None, "main", "Nidhogg",
     "A great wyrm whose shade has claimed both his eyes and the Azure Dragoon's body. Implacably opposed to peace between Ishgard and the dragons, "
     "he may try to disrupt Ser Aymeric's peace conference at Falcon's Nest.",
     ["M336f", "M343d", "M346d"]),
   P(G353, None, "main", "Nidhogg",
     "A great wyrm whose shade wears the body of the Azure Dragoon, Estinien, with both eyes fused to it. At the peace conference at Falcon's Nest he struck down Vidofnir "
     "through Estinien and declared the final chorus nigh.",
     ["M336f", "M353d", "M353e", "M353f"]),
   P(G356, None, "main", "Nidhogg",
     "A great wyrm whose shade wears Estinien's body, with both eyes fused to it. He struck down Vidofnir at Falcon's Nest, and his kin raise the final chorus of the Dragonsong War. "
     "No mortal force can repel him now; only his brood-brother Hraesvelgr might stand against him.",
     ["M353d", "M353e", "M354e", "M356a", "M356b"]),
   P(G357, None, "main", "Nidhogg",
     "A great wyrm whose shade wears Estinien's body, with both eyes fused to it. No mortal force can repel him, and his kin raise the final chorus of the Dragonsong War. "
     "His brood-brother Hraesvelgr has pledged to aid you against him, and a roar signals his Horde's advance.",
     ["M353d", "M354e", "M356b", "M357e", "M357f"]),
   P(G358, None, "main", "Nidhogg",
     "A great wyrm whose shade held the Azure Dragoon Estinien's body. On the Steps of Faith he beat his brood-brother Hraesvelgr, but you, bearing half of Hraesvelgr's power, "
     "subdued his shade and cast his eyes into the abyss. His spirit was undone by mortal will, and his Horde scattered.",
     ["M358b", "M358c", "M358d", "M358e", "M358f", "M358h"]),
   P(G370, None, "main", "Nidhogg",
     "A great wyrm whose shade held the Azure Dragoon Estinien's body until you subdued it and cast his eyes into the abyss; his spirit was undone by mortal will. "
     "Now Elidibus has presented the Eyes of Nidhogg to the Griffin.",
     ["M358e", "M358f", "M370j"]),
   P(G374, None, "main", "Nidhogg",
     "A great wyrm whose shade held the Azure Dragoon Estinien's body until you subdued it and cast his eyes into the abyss. "
     "His eyes resurfaced: Ilberd used them to summon a primal on the Wall.",
     ["M358e", "M358f", "M374e"]),
 ],
 "char-hraesvelgr": [
   P(G336, None, "main", "Hraesvelgr",
     "A great wyrm whose brood Ishgard hopes to win back: Ser Aymeric has sent Lucia to treat with Vidofnir at Anyx Trine.",
     ["M336d"]),
   P(G341, None, "main", "Hraesvelgr",
     "A great wyrm, Vidofnir's sire. For a thousand years he has mourned his beloved, who gave her life for a peace a king betrayed. "
     "Asked by Ishgard for friendship, he left the choice to Vidofnir, who will journey to Ishgard for her people.",
     ["M337c", "M341b", "M341c"]),
   P(G356, None, "main", "Hraesvelgr",
     "A great wyrm, Vidofnir's sire and Nidhogg's brood-brother, who mourns his beloved. Ser Aymeric believes only he can stand against Nidhogg's shade, "
     "but Estinien reported his unwillingness to meddle in men's affairs, and Vidofnir expects him to refuse.",
     ["M341b", "M356a", "M356d", "M356f"]),
   P(G357, None, "main", "Hraesvelgr",
     "A great wyrm, Vidofnir's sire and Nidhogg's brood-brother. At Zenith he recalled how men's forefathers tore down the bridge between man and dragon, "
     "and how he bore Ysayle for her remaining days. Only when Midgardsormr appeared did he agree to test you; after the trial at Sohr Khai he pledged to aid you against Nidhogg.",
     ["M357a", "M357c", "M357d", "M357e", "M357g"]),
   P(G358, None, "main", "Hraesvelgr",
     "A great wyrm, Nidhogg's brood-brother. On the Steps of Faith he tried in vain to turn Nidhogg from vengeance and fell beaten onto the bridge, "
     "but he had given you half his power, and with it you subdued Nidhogg's shade.",
     ["M357e", "M358a", "M358b", "M358c"]),
   P(G360, None, "main", "Hraesvelgr",
     "A great wyrm, Nidhogg's brood-brother. He fell to Nidhogg on the Steps of Faith but gave you half his power, and with it you subdued Nidhogg's shade. "
     "You escorted him home to Zenith on Midgardsormr's wings.",
     ["M358b", "M358c", "M360j"]),
 ],
 "char-vidofnir": [
   P(G336, None, "main", "Vidofnir",
     "A dragon of Hraesvelgr's brood at Anyx Trine, with whom Ser Aymeric has sent Lucia to treat.",
     ["M336d"]),
   P(G337, None, "main", "Vidofnir",
     "Hraesvelgr's daughter, at Anyx Trine. Lucia asked her for Ishgard's friendship, telling her that King Thordan betrayed and murdered Ratatoskr. "
     "She must consult her sire before answering, and will not leave her people while the Gnath grow bold.",
     ["M337a", "M337c", "M337d"]),
   P(G341, None, "main", "Vidofnir",
     "Hraesvelgr's daughter, at Anyx Trine. She is glad that Ravana has fallen, and, her sire having left the choice to her, she will journey to Ishgard on behalf of her people.",
     ["M337c", "M341a", "M341b", "M341c"]),
   P(G343, None, "main", "Vidofnir",
     "Hraesvelgr's daughter. She came to Ishgard and caught the girl Maelie when a priest threw her from the Vault, then warned that Nidhogg and his brood have flown for skies unknown.",
     ["M337c", "M343c", "M343d"]),
   P(G346, None, "main", "Vidofnir",
     "Hraesvelgr's daughter. Her rescue of a child in Ishgard gave hope of peace between man and dragon, and Ser Aymeric is arranging a peace conference at Falcon's Nest for her to attend.",
     ["M337c", "M346b", "M346c"]),
   P(G353, None, "main", "Vidofnir",
     "Hraesvelgr's daughter. At the reconvened peace conference at Falcon's Nest, as she and Ser Aymeric spoke of peace, Estinien drove a lance into her back. "
     "She was carried to Anyx Trine to be cared for.",
     ["M337c", "M353c", "M353d", "M353g"]),
   P(G356, None, "main", "Vidofnir",
     "Hraesvelgr's daughter, recovering at Anyx Trine from the lance Estinien drove into her back; the wound was deep but not mortal. "
     "She expects her sire to refuse Ser Aymeric's plea for help against Nidhogg.",
     ["M337c", "M353d", "M356e", "M356f"]),
 ],
 "char-artoirel": [
   P(G342, None, "main", "Artoirel",
     "A lord of House Fortemps. His father is widely slandered and his half-brother newly dead; he brought a salve for Ser Aymeric on his father's behalf.",
     ["M342e", "M342f", "M342g"]),
   P(G343, None, "main", "Artoirel",
     "A lord of House Fortemps, who fought beside you and Ser Aymeric to retake the Vault. His father, Count Edmont, is stepping aside so that Artoirel will head the house, "
     "and he has vowed to follow his late brother Haurchefant's example.",
     ["M343b", "M343f", "M343h"]),
   P(G347, None, "main", "Artoirel",
     "Heir to House Fortemps, who vowed to follow his late brother Haurchefant's example. At Falcon's Nest he rode out with Lucia to Convictors who threatened the peace conference, "
     "leaving his brother Emmanellain in your care.",
     ["M343f", "M343h", "M347b", "M347c"]),
   P(G350, None, "main", "Artoirel",
     "Heir to House Fortemps. The Convictory incident that drew him and Lucia from Falcon's Nest was likely a ruse; he has detained the Convictors for questioning, "
     "and ordered Emmanellain back to Ishgard to answer for the protester's shooting.",
     ["M343f", "M350a", "M350h", "M350c"]),
 ],
 "char-emmanellain": [
   P(G347, None, "main", "Emmanellain",
     "A lord of House Fortemps and Artoirel's brother, impulsive and lately melancholy. He volunteered at Falcon's Nest, and Artoirel asked you to look after him.",
     ["M347c", "M347d", "M347e"]),
   P(G349, None, "main", "Emmanellain",
     "A lord of House Fortemps and Artoirel's brother. When a protester at Falcon's Nest cried for vengeance on the Dravanians, he panicked and commanded a knight to act; "
     "the knight shot her down and says he followed Emmanellain's order. The people will not soon forget it.",
     ["M347e", "M349b", "M349c", "M349d", "M349f"]),
   P(G350, None, "main", "Emmanellain",
     "A lord of House Fortemps, disgraced when his knight shot down a protester at Falcon's Nest. Artoirel ordered him back to Ishgard to answer for it, "
     "and when he blamed his beaten manservant and lashed out at Thancred, Thancred struck him.",
     ["M349b", "M349d", "M350c", "M350d", "M350e"]),
   P(G351, None, "main", "Emmanellain",
     "A lord of House Fortemps, disgraced at Falcon's Nest. His father wants him to fight in Ser Aymeric's grand melee to make amends, and, inspired by Aymeric, "
     "he begged leave to fight of his own accord.",
     ["M349d", "M350c", "M351b", "M351d"]),
   P(G352, None, "main", "Emmanellain",
     "A lord of House Fortemps, disgraced at Falcon's Nest, who fought in the grand melee to make amends. He gave you House Fortemps's colors to bear, and Ishgard won the day.",
     ["M351d", "M352d", "M352c"]),
   P(G353, None, "main", "Emmanellain",
     "A lord of House Fortemps, who fought in the grand melee to make amends for Falcon's Nest. His father has placed him at his brother Artoirel's disposal.",
     ["M351d", "M353h"]),
   P(G372, None, "main", "Emmanellain",
     "Ser Emmanellain of House Fortemps, newly appointed garrison commander at Camp Dragonhead, with Honoroit's practical help. He doubts he will ever feel worthy of the post.",
     ["M372b", "M372d"]),
 ],
 "char-edmont": [
   P(G343, None, "main", "Edmont",
     "Count Edmont, head of House Fortemps and Artoirel's father. He is widely slandered, suspected of joining a coup by Ser Aymeric, "
     "and is stepping aside so that Artoirel will head the house.",
     ["M342e", "M342g", "M343f", "M343g"], ["Count Edmont"]),
   P(G351, None, "main", "Edmont",
     "Count Edmont of House Fortemps, who is stepping aside for his son Artoirel. He asked that his younger son, Emmanellain, fight in the grand melee to make amends for Falcon's Nest.",
     ["M343f", "M351b"], ["Count Edmont"]),
   P(G353, None, "main", "Edmont",
     "Count Edmont of House Fortemps, who is stepping aside for his son Artoirel. After the grand melee he placed his younger son, Emmanellain, at Artoirel's disposal.",
     ["M343f", "M351b", "M353h"], ["Count Edmont"]),
 ],
 "char-honoroit": [
   P(G350, None, "main", "Honoroit",
     "Emmanellain's young manservant, badly beaten at Falcon's Nest when he tried to stop the smallfolk from leaving.",
     ["M350j", "M350d"]),
   P(G353, None, "main", "Honoroit",
     "Emmanellain's manservant, beaten at Falcon's Nest, who has fully recovered and is eager to resume his duties.",
     ["M350d", "M353a"]),
   P(G372, None, "main", "Honoroit",
     "Emmanellain's manservant, who brings a more practical mind to Emmanellain's new post as garrison commander at Camp Dragonhead.",
     ["M353a", "M372b"]),
 ],
 "org-holy-see": [
   P(G336, None, "main", "The Holy See",
     "The archbishops' rule over Ishgard. With the archbishop's seat vacant, Ser Aymeric has taken on its responsibilities under canon law, "
     "and the city is divided over how the archbishop was stopped.",
     ["M336a", "M336c"]),
   P(G360, None, "main", "The Holy See",
     "The archbishops' thousand-year rule over Ishgard, which Ser Aymeric has abolished; a House of Commons and a House of Lords now govern.",
     ["M360a", "M360b"]),
 ],
 "org-house-of-lords": [
   P(G360, None, "main", "The House of Lords",
     "One of the two houses that, with the House of Commons, now govern Ishgard after the archbishops' rule was abolished. Ser Aymeric was elected to its highest seat.",
     ["M360a", "M360b"]),
   P(G361, None, "main", "The House of Lords",
     "One of the two houses that, with the House of Commons, now govern Ishgard. Ser Aymeric is its lord speaker, and the Lords and Commons offer the Scions their patronage.",
     ["M360b", "M361a", "M361h"]),
 ],
 "org-dravanian-horde": [
   P(G357, None, "main", "The Dravanian Horde",
     "Nidhogg's forces. A roar across the sky signals their advance.",
     ["M354c", "M357f"]),
   P(G358, None, "main", "The Dravanian Horde",
     "Nidhogg's forces. When his shade fell on the Steps of Faith, the Horde sensed it and scattered.",
     ["M357f", "M358h"]),
 ],
 # -- The Scions' search and the Warriors of Darkness
 "char-krile": [
   P(G338, None, "main", "Krile",
     "A Sharlayan scholar of the Students of Baldesion, recently come from the Sharlayan homeland to help find the missing Scions. She is Minfilia's dear friend, and knew the twins at the Studium. "
     "She means to follow the trail Thancred left when Y'shtola sent him away, but needs Matoya's Crystal Eye.",
     ["M336j", "M338a", "M338b", "M338e", "M338f", "M338c"]),
   P(G339, None, "main", "Krile",
     "A Sharlayan scholar and Minfilia's dear friend, whom she met while studying with the Students of Baldesion. She has the Echo, and the blessing of Light preserved her when the "
     "Students' headquarters and the Isle of Val were obliterated. With Matoya's Crystal Eye she traced Thancred to the foot of Sohm Al.",
     ["M338a", "M339a", "M339b", "M339c", "M339f"]),
   P(G341, None, "main", "Krile",
     "A Sharlayan scholar with the Echo, and Minfilia's dear friend. After you found Thancred, she went to Matoya to ask her help in the search for Minfilia.",
     ["M338a", "M339a", "M341i"]),
   P(G344, None, "main", "Krile",
     "A Sharlayan scholar with the Echo, and Minfilia's dear friend. She believes Hydaelyn's intercession must leave a trace in the aether, and has gone with Thancred to read it in Castrum Meridianum.",
     ["M338a", "M339a", "M344b", "M344c"]),
   P(G345, None, "main", "Krile",
     "A Sharlayan scholar with the Echo, and Minfilia's dear friend. Her readings matched a signature found at the Isle of Val, and she believes Hydaelyn guided Minfilia to Her realm. "
     "After the Word of the Mother spoke atop the Antitower, she concluded that Minfilia, joined with Hydaelyn, struggles to keep her own form.",
     ["M338a", "M345a", "M345b", "M345e", "M345h"]),
   P(G355, None, "main", "Krile",
     "A Sharlayan scholar with the Echo, and Minfilia's friend. She felt the wyrm's hatred about Estinien even before his change, and with Y'shtola concluded that his spirit may survive; "
     "but she warns that whoever frees him might become Nidhogg's next host.",
     ["M339a", "M354d", "M355a", "M355c"]),
   P(G363, None, "main", "Krile",
     "A Sharlayan scholar with the Echo, and Minfilia's friend. She goes with Y'shtola to Xelphatol to learn where the Ixal get their crystals.",
     ["M338a", "M339a", "M363d"]),
   P(G370, None, "main", "Krile",
     "A Sharlayan scholar with the Echo, and Minfilia's dear friend, now welcomed as a full Scion.",
     ["M338a", "M339a", "M370g"]),
 ],
 "char-matoya": [
   P(G338, None, "main", "Matoya",
     "Master Matoya, whose Crystal Eye, one of her most cherished relics, Krile needs to find Thancred.",
     ["M338c", "M338g"]),
   P(G339, None, "main", "Matoya",
     "A hermit scholar whose Crystal Eye is an ancient Crystal of Light. Taking a liking to Krile, she let her use it to trace Thancred.",
     ["M339d", "M339e"]),
   P(G345, None, "main", "Matoya",
     "A hermit scholar, owner of the Crystal Eye, whom the Forum made custodian of the Antitower, a Sharlayan structure overlooking the aetherial sea. "
     "She let you climb it but kept Krile behind to restore its ward. Afterwards she told Alphinaud that Minfilia had thrown herself on the fire for the Scions' cause.",
     ["M339d", "M345c", "M345k", "M345d", "M345i"]),
 ],
 "org-warriors-of-darkness": [
   P(G340, None, "main", "The Warriors of Darkness",
     "A party of adventurers who had beaten Ravana before you arrived. Their leader named them the Warriors of Darkness, walkers of a different path, "
     "and a memory he showed recalled a fight with a man in black, perhaps an Ascian.",
     ["M340d", "M340e", "M340f"]),
   P(G341, None, "main", "The Warriors of Darkness",
     "A party of adventurers, walkers of a different path, who beat Ravana before you arrived. They have the Echo, are driven to put down primals, and have plainly fought such beings before.",
     ["M340e", "M341d", "M341e"]),
   P(G361, None, "main", "The Warriors of Darkness",
     "Adventurers with the Echo, driven to put down primals. Thancred tracked them, and Alisaie, who shadowed them too, was struck by a poisoned arrow. "
     "They conspire with the Ascians to goad the Ixal into summoning Garuda, so that they can slay her.",
     ["M341e", "M361d", "M361e", "M361f", "M361g"]),
   P(G362, None, "main", "The Warriors of Darkness",
     "Adventurers from a world where Light grew far stronger than Dark. They joined hands with their former enemies, the Ascians, to come here and bring about another Umbral Calamity: "
     "only the Ardor, they say, can save their home. In Xelphatol you stopped the summoning they had goaded the Ixal into.",
     ["M361g", "M362b", "M362d", "M362e", "M362f", "M362g"]),
   P(G366, None, "main", "The Warriors of Darkness",
     "Adventurers from a world overwhelmed by Light, allied with the Ascians to bring about another Umbral Calamity, for they believe only the Ardor can save their home. "
     "A masked man tells their leader the Ardor is not the Ascians' alone to invoke.",
     ["M362d", "M362e", "M362g", "M366h"]),
   P(G369, None, "main", "The Warriors of Darkness",
     "Adventurers from a world overwhelmed by Light. In the Bowl of Embers they came to kill you to bring about a Calamity, but Urianger, a double agent, broke your chains. "
     "They were already dead: chosen as Warriors of Light in their own world, which fell to ruin anyway. They asked to be taken home, and left with Minfilia.",
     ["M369c", "M369d", "M369f", "M369g", "M369k"]),
 ],
 "char-elidibus": [
   P(G343, None, "main", "Elidibus",
     "A figure who met Urianger and the Warriors of Darkness's leader at the Great Gubal Library, and told Urianger, whom he calls Archon, that their fates were ordained long ago.",
     ["M343j", "M343k"]),
   P(G360, None, "main", "Elidibus",
     "A figure who plots with the Warriors of Darkness's leader. By the chasm where Nidhogg's eyes were cast, he told him that the others will play their part, as they will theirs.",
     ["M343k", "M360h"]),
   P(G370, None, "main", "Elidibus",
     "A figure who plotted with the Warriors of Darkness. He presented the Eyes of Nidhogg to the Griffin, judging him the most deserving of many candidates, "
     "and calls a world without equilibrium a void in waiting.",
     ["M360h", "M370j", "M370k"]),
 ],
 "org-ascians": [
   P(G345, None, "main", "The Ascians",
     "The Word of the Mother says the Ascians' work has succeeded seven times, and each time the Darkness, which Hydaelyn banished, grew stronger.",
     ["M345f", "M345g"]),
   P(G361, None, "main", "The Ascians",
     "A group whose work, the Word of the Mother says, has strengthened the Darkness seven times. They conspire with the Warriors of Darkness to goad the Ixal into summoning Garuda.",
     ["M345g", "M361g"]),
   P(G363, None, "main", "The Ascians",
     "A group whose work has strengthened the Darkness, and who conspire with the Warriors of Darkness. Thancred and Alisaie found evidence that they keep crystals flowing to the beast tribes, "
     "and one observed that the powerless will turn to another god when the old ones fail.",
     ["M345g", "M361g", "M363b", "M363c"]),
 ],
 "char-masked-man": [
   P(G366, None, "main", "The masked man",
     "A masked figure who tells the Warriors of Darkness's leader that the Ardor is not the Ascians' alone to invoke.",
     ["M366h"]),
   P(G369, None, "main", "The masked man",
     "A masked figure who called himself the author of the drama in the Bowl of Embers. He was Urianger, a double agent who had manipulated the Warriors of Darkness.",
     ["M369b", "M369d", "M369e"]),
 ],
 # -- Vylbrand and Ala Mhigo
 "char-ga-bu": [
   P(G364, None, "main", "Ga Bu",
     "A kobold child of the 620th Order who came to Camp Overlook to beg the Maelstrom to stop the patriarch from summoning Titan again. "
     "His parents spoke out against the patriarch and were taken away.",
     ["M364b", "M364c", "M364d"]),
   P(G365, None, "main", "Ga Bu",
     "A kobold child of the 620th Order. His parents and the other prisoners had already been executed, and his anguish birthed Titan. "
     "Titan is no more, but Ga Bu may have fallen under the primal's influence.",
     ["M365b", "M365c", "M365e", "M365f"]),
   P(G366, None, "main", "Ga Bu",
     "A kobold child whose parents were executed, and whose grief birthed Titan. Alisaie entrusted him to Commander Bloeidin's care, and he may one day recover.",
     ["M365b", "M365c", "M366a", "M366b"]),
 ],
 "org-ala-mhigan-resistance": [
   P(G343, None, "main", "The Ala Mhigan Resistance",
     "The Ala Mhigan Resistance, fighting the imperials. Yda and Papalymo are at one of its camps.",
     ["M343l"]),
   P(G367, None, "main", "The Ala Mhigan Resistance",
     "The Ala Mhigan Resistance, active among the refugees of Little Ala Mhigo, some of whose members received large shipments of crystals. "
     "Old Resistance friends helped Yda and Papalymo flee Ul'dah, and the two have helped its operations since.",
     ["M343l", "M367a", "M367f"]),
   P(G371, None, "main", "The Ala Mhigan Resistance",
     "The Ala Mhigan Resistance. One of its leaders, the masked Griffin, means to assault the Wall from the Ala Mhigan side and spread war to Eorzea; "
     "a wounded messenger brought the Scions warning.",
     ["M367a", "M371b", "M371c", "M371d"]),
   P(MS, None, "main", "The Ala Mhigan Resistance",
     "The Ala Mhigan Resistance. After its leader the Griffin was unmasked as Ilberd, Ser Aymeric proposed that the Alliance contact its representatives in Gyr Abania, "
     "and Lyse means to continue her family's fight for Ala Mhigo.",
     ["M374d", "M379f", "M379l"]),
 ],
 "org-masks": [
   P(G343, None, "main", "The Masks",
     "A band of the Ala Mhigan Resistance. At a Resistance camp, Yda says they will attack the imperials once all units are in place.",
     ["M343l"]),
   P(G367, None, "main", "The Masks",
     "Followers of the masked revolutionary called the Griffin, among the refugees of Little Ala Mhigo. They are rumored to hold a secret weapon against the Garleans, "
     "most likely received the crystals smuggled from Ishgard, and seem to have intercepted Papalymo's letter to the Scions.",
     ["M367b", "M367c", "M367d", "M367j"]),
   P(G368, None, "main", "The Masks",
     "Followers of the masked Griffin. At his behest they traded crystals from Ishgard to the Amalj'aa, who will help them fight for Ala Mhigan liberation. "
     "Many joined them because you once saved them.",
     ["M367b", "M368a", "M368b", "M368d"]),
   P(G374, None, "main", "The Masks",
     "Followers of the masked Griffin, who traded crystals to the Amalj'aa. On the Wall the Griffin was unmasked as Ilberd, and died completing his summoning.",
     ["M368b", "M374d", "M374f"]),
 ],
 "char-griffin": [
   P(G367, None, "main", "The Griffin",
     "A masked revolutionary leader in Little Ala Mhigo who has rallied many refugees. He and his Masks are rumored to have a secret weapon against the Garleans, "
     "and most likely received the crystals smuggled from Ishgard. The speaker you heard at Qarn was an impersonator.",
     ["M367b", "M367c", "M367d", "M367h"]),
   P(G368, None, "main", "The Griffin",
     "A masked revolutionary leader of the Masks. His double speaks with his voice: at the Griffin's behest the Masks traded crystals to the Amalj'aa, who will help them fight for Ala Mhigo.",
     ["M367b", "M368a", "M368b"]),
   P(G370, None, "main", "The Griffin",
     "A masked revolutionary leader of the Masks, who traded crystals to the Amalj'aa. Elidibus has presented him with the Eyes of Nidhogg.",
     ["M367b", "M368b", "M370j"]),
   P(G371, None, "main", "The Griffin",
     "A masked leader of the Ala Mhigan Resistance, who holds the Eyes of Nidhogg. A wounded messenger warns that he means to assault the Wall from the Ala Mhigan side, to spread war to Eorzea.",
     ["M370j", "M371b", "M371c", "M371d"]),
   P(G374, None, "main", "The Griffin",
     "The name of a masked Resistance leader who attacked the Wall with soldiers in Grand Company uniforms, as bait. On the Wall he was unmasked as Ilberd, the disgraced captain of the Crystal Braves.",
     ["M374b", "M374c", "M374d"]),
 ],
 "char-ilberd": [
   P(G374, None, "main", "Ilberd",
     "The disgraced captain of the Crystal Braves, unmasked as the Griffin on the Wall. With Nidhogg's eyes and Ala Mhigan desperation he called on a deity more terrible than "
     "the Calamity's black wyrm; his death completed the ritual, and the primal took shape.",
     ["M374d", "M374e", "M374k", "M374f"], ["The Griffin"]),
 ],
 "char-shinryu": [
   P(G374, None, "main", "Ilberd's primal",
     "A primal Ilberd summoned on the Wall, empowered by Ala Mhigan desperation and Nidhogg's eyes and completed by his death. "
     "Papalymo sealed it in a cocoon of light at the cost of his own life.",
     ["M374e", "M374f", "M374g"]),
   P(G376, None, "main", "Ilberd's primal",
     "A primal Ilberd summoned on the Wall, sealed in a cocoon of light by Papalymo's sacrifice. Y'shtola confirmed it within, and a Garlean airship that approached was destroyed. "
     "The Alliance means to meet it with Omega.",
     ["M374g", "M376a", "M376b", "M376g"]),
   P(G378, None, "main", "Ilberd's primal",
     "A primal Ilberd summoned on the Wall, sealed in a cocoon of light by Papalymo's spell, which, bound to his aether, is fading. Omega has been launched to seek it out.",
     ["M374g", "M378d", "M378e", "M378g"]),
   P(MS, None, "main", "Shinryu",
     "The name the Domans give the primal Ilberd summoned on the Wall. The cocoon of light hatched as Omega arrived, a great dragon rose from it, "
     "and the two fought over Gyr Abania before falling together onto Ala Mhigan soil.",
     ["M374e", "M379a", "M379b", "M379c"], ["Ilberd's primal"]),
 ],
 # -- Omega
 "char-nero": [
   P(G376, None, "main", "Nero",
     "A former tribunus of the XIVth Legion, who claims to have restored the Ultima Weapon and studied beside Cid at the Academy. He proposed waking Omega against the primal, "
     "and the Alliance sent him with Cid's contingent. Alisaie says he may be killed if he proves treacherous, and Alphinaud wonders how he learned of the council meeting.",
     ["M376c", "M376d", "M376e", "M376g", "M376h", "M376i"]),
   P(G378, None, "main", "Nero",
     "A former tribunus of the XIVth Legion who studied beside Cid, and whom Alisaie insists never leave her sight. He has been to Omega's control room before, and with Cid he woke the machine.",
     ["M376c", "M376e", "M377a", "M378a", "M378b"]),
 ],
 "char-gosetsu": [
   P(G377, None, "main", "Gosetsu",
     "A Doman warrior who came to Eorzea with word that his master is in peril and Doma calls Yugiri home; Urianger found him collapsed in the street. "
     "When Yugiri chose to stay and face the crisis, he joined the Omega expedition, his blade oathbound against the imperials.",
     ["M377b", "M377c", "M377e", "M377f"]),
 ],
 "char-lyse": [
   P(MS, None, "main", "Lyse",
     "The Scion you knew as Yda: Yda's younger sister, who served for years in her mask and name. Yda died six years ago smuggling refugees out of Ala Mhigo; "
     "Papalymo brought Lyse her mask as a keepsake, she chose to carry on her sister's work, and Papalymo persuaded those who knew to keep the secret. "
     "Their father fought to overthrow Ala Mhigo's mad king, and now she means to continue her family's fight for Ala Mhigo.",
     ["M379g", "M379h", "M379i", "M379j", "M379k", "M379m", "M379l"], ["Yda"]),
 ],
 "char-zenos": [
   P(MS, None, "main", "The Viceroy",
     "An imperial lord in Ala Mhigo, addressed as Viceroy, to whom an officer reports that the Wall has fallen to the Alliance. His spies say the Domans call the primal Shinryu "
     "and that it proved a match for Omega, and he expects the coming days to be most interesting.",
     ["M379n", "M379o", "M379p"]),
 ],
 # -- Entities the Atlas already has
 "char-minfilia": [
   P(G336, None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. She stayed behind when the Scions fled the royal banquet in Ul'dah, saying Hydaelyn spoke to her, "
     "and the hunt for her is at a standstill.",
     ["C01", "C33", "C17", "M336g"], ["the Antecedent"]),
   P(G341, None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, missing since the royal banquet in Ul'dah. Krile, her dear friend from her studies with the Students of Baldesion, "
     "has gone to Matoya for help in the search.",
     ["C01", "M339c", "M341i", "M341j"], ["the Antecedent"]),
   P(G344, None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, missing since the royal banquet in Ul'dah, and F'lhaminn's daughter. Thancred calls her the Scions' guiding light after the Calamity, "
     "and Tataru insists she will be found. Krile believes Hydaelyn's intercession left a trace that could lead to her.",
     ["C01", "M344d", "M344e", "M344g", "M344b"], ["the Antecedent"]),
   P(G345, None, "main", "Minfilia",
     "Once leader of the Scions. Krile believes Hydaelyn guided her to Her realm. Atop the Antitower a voice calling itself the Word of the Mother said it was once Minfilia; "
     "Krile concludes that Minfilia, joined with Hydaelyn, struggles to keep her own form, and Matoya says she threw herself on the fire for the Scions' cause.",
     ["M345b", "M345e", "M345h", "M345i"], ["the Antecedent", "the Word of the Mother"]),
   P(G369, None, "main", "Minfilia",
     "Once leader of the Scions, who joined with Hydaelyn and spoke as the Word of the Mother. Urianger orchestrated events to grant her freedom, and in the Bowl of Embers "
     "Hydaelyn set her free to serve as Her emissary. She left with the Warriors of Darkness for their world, to take its rising Light into herself, and promised to return one day.",
     ["M345e", "M369h", "M369i", "M369j", "M369l"], ["the Antecedent", "the Word of the Mother"]),
 ],
 "char-thancred": [
   P(G339, None, "main", "Thancred",
     "A Scion and bard, lost since he and Y'shtola stayed behind to stop the pursuit at the royal banquet in Ul'dah. Krile followed his trail with Matoya's Crystal Eye: "
     "he emerged from the Lifestream near Sohm Al, where hunters speak of an axe-wielding stranger.",
     ["C18", "M336g", "M338f", "M339f"]),
   P(G340, None, "main", "Thancred",
     "A Scion and bard, found at last. Y'shtola's forbidden magicks sent him into the wilderness after the royal banquet; he learned of Ravana from the Vath, "
     "and went to the Gnath when they summoned him again, arriving as the Warriors of Darkness beat the primal.",
     ["M340c", "M340g", "M340a", "M340d"]),
   P(G343, None, "main", "Thancred",
     "A Scion and bard, back with the Scions, and saddened that Yda, Papalymo and Minfilia are still missing. Y'shtola suspects his aetheric flow has been disrupted, "
     "keeping him from all magicks, teleportation included.",
     ["M341j", "M343i"]),
   P(G345, None, "main", "Thancred",
     "A Scion and bard, whose aetheric flow seems disrupted. He calls Minfilia the Scions' guiding light; with Krile he read the aether in Castrum Meridianum, "
     "and when the Word of the Mother spoke for her, he stormed out without a word.",
     ["M343i", "M344e", "M344c", "M345j"]),
   P(G350, None, "main", "Thancred",
     "A Scion and bard. At Falcon's Nest, when Emmanellain blamed his beaten manservant and lashed out, Thancred struck him: he has fought to save those dear to him, and failed.",
     ["M345j", "M350e", "M350f"]),
   P(G361, None, "main", "Thancred",
     "A Scion and bard. He tracked the Warriors of Darkness, rescued Alisaie, who was on their trail too, and brought her to Ishgard struck by a poisoned arrow.",
     ["M361d", "M361e"]),
   P(G363, None, "main", "Thancred",
     "A Scion and bard who tracked the Warriors of Darkness. With Alisaie he found evidence that the Ascians keep crystals flowing to the beast tribes.",
     ["M361d", "M363b"]),
   P(G370, None, "main", "Thancred",
     "A Scion and bard who tracked the Warriors of Darkness. He went back alone into Zahar'ak to secure the crystals smuggled from Ishgard.",
     ["M361d", "M370a"]),
   P(G374, None, "main", "Thancred",
     "A Scion and bard. He went with Papalymo, Yda and Yugiri through the tunnels beneath the Wall to confront the Griffin, and saw Papalymo give his life to seal Ilberd's primal.",
     ["M374a", "M374g"]),
 ],
 "char-yshtola": [
   P(G338, None, "main", "Y'shtola",
     "A Sharlayan Scion. At Idyllshire she welcomed Krile, a scholar come from the Sharlayan homeland to help find the missing Scions.",
     ["M337f", "M338e"]),
   P(G340, None, "main", "Y'shtola",
     "A Sharlayan Scion. When she and Thancred stayed behind at the royal banquet, her forbidden magicks sent him into the wilderness; now he is found.",
     ["C18", "M340c"]),
   P(G343, None, "main", "Y'shtola",
     "A Sharlayan Scion, whose forbidden magicks once sent Thancred into the wilderness. She suspects his aetheric flow has been disrupted, keeping him from magicks and teleportation.",
     ["M340c", "M343i"]),
   P(G363, None, "main", "Y'shtola",
     "A Sharlayan Scion. She goes with Krile to Xelphatol to learn where the Ixal get their crystals.",
     ["M363d"]),
   P(G376, None, "main", "Y'shtola",
     "A Sharlayan Scion. With Krile she inspected the cocoon of light above the Wall, and confirmed a primal within.",
     ["M375c", "M376a"]),
 ],
 "char-urianger": [
   P(G343, None, "main", "Urianger",
     "A learned Sharlayan Scion who studied under Louisoix. At the Great Gubal Library he met Elidibus, who calls him Archon, and the Warriors of Darkness's leader; "
     "Elidibus told him their fates were ordained long ago.",
     ["C54", "M343j", "M343k"]),
   P(G363, None, "main", "Urianger",
     "A learned Sharlayan Scion who studied under Louisoix. At the Waking Sands he pointed you to the kobolds, who may soon summon Titan again, and Alisaie asked him to research the Warriors' claims.",
     ["C54", "M363f", "M363g"]),
   P(G366, None, "main", "Urianger",
     "A learned Sharlayan Scion who studied under Louisoix. He found that a Rejoining would kill everyone on a reflection of the Source, and traced the Ishgardian smugglers to the Ivy's old network. "
     "Alisaie treats him with deep suspicion.",
     ["C54", "M366c", "M366d", "M366g"]),
   P(G369, None, "main", "Urianger",
     "A learned Sharlayan Scion who studied under Louisoix. He was the masked man: a double agent who manipulated the Warriors of Darkness, and in the Bowl of Embers he broke your chains. "
     "He confessed he orchestrated events to grant Minfilia her freedom.",
     ["C54", "M369d", "M369e", "M369h"], ["the masked man"]),
   P(G370, None, "main", "Urianger",
     "A learned Sharlayan Scion who, as the masked man, played double agent with the Warriors of Darkness to free Minfilia. He is haunted by guilt over her fate, "
     "and Alisaie cannot condone his deception.",
     ["M369d", "M369h", "M370h", "M370b"], ["the masked man"]),
 ],
 "char-alphinaud": [
   P(G337, None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother. Summoned with you to Ser Aymeric, he led the way to Anyx Trine with Lucia. He once saw Ysayle as a murderous fanatic, "
     "but came to see her as a noble, if misguided, soul.",
     ["C10", "M336k", "M336d", "M337e"]),
   P(G344, None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother. He blames his own ambition for forcing the Scions to flee, and worries for those still missing.",
     ["C10", "M344f"]),
   P(G346, None, "main", "Alphinaud",
     "A young Scion who blames his ambition for the Scions' flight. After Matoya told him Minfilia threw herself on the fire for the Scions' cause, he will tell only Tataru and Urianger "
     "of her fate, and asks you to keep it from the others, especially F'lhaminn.",
     ["M344f", "M345i", "M346a"]),
   P(G354, None, "main", "Alphinaud",
     "A young Scion. Though Ser Aymeric and Ishgard may sacrifice Estinien to slay Nidhogg, Alphinaud will not: he refuses to be a man who sacrifices friends for a cause.",
     ["M354a", "M354b"]),
   P(G359, None, "main", "Alphinaud",
     "A young Scion who refused to sacrifice Estinien. After Nidhogg's fall he counts freeing Estinien the greater feat, and keeps vigil at his bedside.",
     ["M354b", "M359a", "M359e"]),
   P(G362, None, "main", "Alphinaud",
     "A young Scion, Alisaie's twin. In Xelphatol he helped stop Garuda's summoning, and when the Warriors of Darkness revealed their aims, he vowed the sacrifice ends here.",
     ["M361c", "M362c", "M362i"]),
   P(G370, None, "main", "Alphinaud",
     "A young Scion, Alisaie's twin. With the Scions together again, he proposed that each member pursue what best keeps the realm safe, rather than follow a strict hierarchy.",
     ["M361c", "M370f"]),
   P(G371, None, "main", "Alphinaud",
     "A young Scion, Alisaie's twin, who reshaped the Scions so that each member pursues what best keeps the realm safe. He proposes electing a coordinator of operations as Minfilia's successor.",
     ["M370f", "M371a"]),
   P(G373, None, "main", "Alphinaud",
     "A young Scion. At the Alliance council he vouched for the Scions' source in the Resistance's inner circle, but fears that readying for war gives the Griffin what he wants.",
     ["M371a", "M373h", "M373f"]),
   P(G375, None, "main", "Alphinaud",
     "A young Scion. He saw that the Griffin's attack on the Wall was bait, and broke the news of Papalymo's passing to the Scions. He calls for preparations to face Ilberd's creation, "
     "though he cannot yet explain how Ilberd came by Nidhogg's eyes.",
     ["M374c", "M375a", "M375d", "M375f"]),
   P(G376, None, "main", "Alphinaud",
     "A young Scion preparing to face Ilberd's primal. When Nero offered the Alliance Omega, Alphinaud wondered how he learned of the council meeting at all.",
     ["M375f", "M376c", "M376i"]),
 ],
 "char-alisaie": [
   P(G361, None, "main", "Alisaie",
     "Alphinaud's twin sister, who long ago parted from him to walk her own path. She shadowed the Warriors of Darkness until Thancred rescued her; struck by a poisoned arrow, "
     "she reached Ishgard near death, warning that Garuda would soon be summoned in Xelphatol.",
     ["M361c", "M361d", "M361e", "M361f"]),
   P(G363, None, "main", "Alisaie",
     "Alphinaud's twin sister. She has regained consciousness, and with Thancred found evidence that the Ascians keep crystals flowing to the beast tribes. "
     "She asked Urianger to research the Warriors' claims.",
     ["M361c", "M363a", "M363b", "M363g"]),
   P(G366, None, "main", "Alisaie",
     "Alphinaud's twin sister. She entrusted the grieving kobold Ga Bu to Commander Bloeidin's care, and treats Urianger with a deep suspicion her brother cannot explain.",
     ["M361c", "M366a", "M366g"]),
   P(G370, None, "main", "Alisaie",
     "Alphinaud's twin sister, now welcomed as a full Scion. She cannot condone Urianger's deception, though it freed Minfilia.",
     ["M370g", "M370b", "M369h"]),
   P(G376, None, "main", "Alisaie",
     "Alphinaud's twin sister and a full Scion. She told the Alliance that Nero may be killed if he proves treacherous.",
     ["M370g", "M376h"]),
 ],
 "char-tataru": [
   P(G336, None, "main", "Tataru",
     "The Scions' receptionist. She relays word from Riol's men: F'lhaminn is hiding in Radz-at-Han, and Yda and Papalymo seem to have discarded their linkpearls. "
     "A Sharlayan scholar of the Students of Baldesion has been enlisted to help the search.",
     ["C15", "M336h", "M336i", "M336j"]),
   P(G344, None, "main", "Tataru",
     "The Scions' receptionist. She welcomed F'lhaminn, Hoary Boulder and Coultenet home, and insists Minfilia, Yda and Papalymo will be found.",
     ["C15", "M344a", "M344g"]),
   P(G377, None, "main", "Tataru",
     "The Scions' receptionist. After having you measured at the Diamond Forge, she sewed you a traveling outfit with a blood pearl charm to bring you home.",
     ["C15", "M371h", "M377g"]),
 ],
 "org-scions": [
   P(G344, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future. F'lhaminn, Hoary Boulder and Coultenet have come home, but Minfilia, Yda and Papalymo are still missing.",
     ["C34", "M344a", "M344g"]),
   P(G345, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future. Its leader, Minfilia, is lost to it: a voice calling itself the Word of the Mother said it was once her, "
     "and Matoya says she threw herself on the fire for the Scions' cause. Yda and Papalymo are still missing.",
     ["C34", "M345e", "M345i", "M344g"]),
   P(G361, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, which has lost Minfilia. Ishgard's Lords and Commons offer it their patronage.",
     ["C34", "M345e", "M361h"]),
   P(G370, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, which has lost Minfilia. Yda and Papalymo have rejoined; Alphinaud proposed that each member pursue what best keeps the realm safe "
     "rather than follow a strict hierarchy, and Krile and Alisaie were welcomed as full members.",
     ["M345e", "M370c", "M370f", "M370g"]),
   P(G374, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, whose members each pursue what best keeps the realm safe. Papalymo gave his life on the Wall to seal Ilberd's primal.",
     ["M370f", "M374g"]),
 ],
 "char-cid": [
   P(G376, None, "main", "Cid",
     "An engineer who left the Empire and built the Ironworks. Nero, who claims to have restored the Ultima Weapon, studied beside him at the Academy. "
     "The Alliance council gave his contingent authority to take command of Omega beneath Carteneau.",
     ["M376d", "M376e", "M376g"]),
   P(G378, None, "main", "Cid",
     "An engineer who left the Empire and built the Ironworks. With Nero he woke Omega in Carteneau, where an imperial officer called him a traitor; "
     "once Omega launched, its signal fell silent and he reengaged its stasis.",
     ["M376e", "M378a", "M378c", "M378f"]),
 ],
 "char-yda": [
   P(G343, None, "main", "Yda",
     "A Scion missing since the royal banquet in Ul'dah. She is with Papalymo at an Ala Mhigan Resistance camp, where she says the Masks will attack the imperials once all units are in place.",
     ["M341j", "M343l"]),
   P(G354, None, "main", "Yda",
     "A Scion missing since the royal banquet, now with Papalymo at an Ala Mhigan Resistance camp. Papalymo warns her not to place her faith in them too soon.",
     ["M343l", "M354g"]),
   P(G367, None, "main", "Yda",
     "A Scion who, with Papalymo, slipped out of Ul'dah after the banquet with old Resistance friends, and has helped the Resistance in Little Ala Mhigo since. You found them at Qarn.",
     ["M367e", "M367f"]),
   P(G368, None, "main", "Yda",
     "A Scion who has helped the Resistance in Little Ala Mhigo. She named the Amalj'aa's god as Ifrit, fearing for the Resistance, and was tempted to join the Masks until Papalymo forbade it.",
     ["M367f", "M368c", "M368e"]),
   P(G370, None, "main", "Yda",
     "A Scion. Gundobald of Little Ala Mhigo knew her father, who fought in the revolution against the King of Ruin; she explained that her work for the Circle of Knowing "
     "and the Scions required secrecy. She and Papalymo have rejoined the Scions.",
     ["M370c", "M370d", "M370e"]),
   P(G374, None, "main", "Yda",
     "A Scion. She went with Papalymo, Thancred and Yugiri through the tunnels beneath the Wall, and Papalymo gave his life to seal Ilberd's primal; "
     "the loss of her dearest friend has broken her spirit.",
     ["M374a", "M374h", "M374g", "M374j"]),
   P(G378, None, "main", "Yda",
     "A Scion grieving her dearest friend, Papalymo. She launched Omega in his name, and fears his spell, bound to his aether, is fading.",
     ["M374j", "M378e", "M378g"]),
   P(MS, None, "main", "Yda",
     "The name under which Lyse served the Scions, wearing the mask of her sister Yda, who died six years ago smuggling refugees out of Ala Mhigo.",
     ["M379g", "M379i", "M379j"]),
 ],
 "char-papalymo": [
   P(G343, None, "main", "Papalymo",
     "A Scion missing since the royal banquet in Ul'dah, now with Yda at an Ala Mhigan Resistance camp.",
     ["M341j", "M343l"]),
   P(G354, None, "main", "Papalymo",
     "A Scion missing since the royal banquet, now with Yda at an Ala Mhigan Resistance camp. He warns Yda not to place her faith in them too soon.",
     ["M343l", "M354g"]),
   P(G367, None, "main", "Papalymo",
     "A Scion who, with Yda, slipped out of Ul'dah with old Resistance friends and has helped the Resistance in Little Ala Mhigo since. Hearing the Scions were cleared, "
     "he wrote to them, but the Masks likely intercepted his letter.",
     ["M367e", "M367f", "M367g", "M367j"]),
   P(G368, None, "main", "Papalymo",
     "A Scion who has helped the Resistance in Little Ala Mhigo. He forbade Yda to join the Masks, and will search their camp for the crystal cache.",
     ["M367f", "M368e", "M368f"]),
   P(G370, None, "main", "Papalymo",
     "A Scion and Louisoix's disciple. He and Yda have rejoined the Scions, and he asked to keep Louisoix's staff, Tupsimati.",
     ["M370c", "M370i"]),
   P(G374, None, "main", "Papalymo",
     "A Scion and Louisoix's disciple. On the Wall, with Tupsimati, he wove a forbidden magick of confinement that swallowed him and sealed Ilberd's primal in a cocoon of light.",
     ["M370i", "M374h", "M374g"]),
   P(G375, None, "main", "Papalymo",
     "A Scion and Louisoix's disciple, who gave his life on the Wall to seal Ilberd's primal in a cocoon of light. Urianger says the pupil followed the master even unto the grave.",
     ["M374g", "M375a", "M375e"]),
   P(G378, None, "main", "Papalymo",
     "A Scion and Louisoix's disciple, who gave his life on the Wall to seal Ilberd's primal. His spell, bound to his aether, is fading.",
     ["M374g", "M375a", "M378g"]),
   P(MS, None, "main", "Papalymo",
     "A Scion and Louisoix's disciple, who gave his life on the Wall to seal Ilberd's primal. He brought Lyse her sister Yda's mask as a keepsake, and persuaded those who knew to keep the secret.",
     ["M374g", "M379j", "M379k"]),
 ],
 "char-titan": [
   P(G365, None, "main", "Titan",
     "The primal the kobolds call Great Father. Their patriarch meant to summon him again; instead the grief of Ga Bu, whose parents were executed, birthed him. "
     "You faced him in the Navel, and Titan is no more.",
     ["M364d", "M365b", "M365c", "M365d", "M365e"]),
 ],
 "char-garuda": [
   P(G362, None, "main", "Garuda",
     "A primal of the Ixal. The Warriors of Darkness and the Ascians goaded the Ixal into summoning her again in Xelphatol, so the Warriors could slay her, "
     "but you laid the occultist low before the ritual was done, and she is no longer a threat.",
     ["M361f", "M361g", "M362b", "M362c"]),
 ],
 "org-eorzean-alliance": [
   P(G352, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. Its forces met Ishgard's in a grand melee outside the city, where General Raubahn challenged you to single combat; Ishgard won the day.",
     ["M351a", "M352b", "M352c", "M352e"]),
   P(G373, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. Its council, joined by Ishgard's envoy Ser Aymeric, agreed to reinforce Gridania's border against the Griffin's threatened assault, "
     "with Yugiri's shinobi at its disposal. Raubahn warns the fighting will spill into the Black Shroud.",
     ["M372a", "M373b", "M373c", "M373d", "M373e"]),
   P(G376, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. Its council sent a contingent under Cid to take command of Omega against the primal in the cocoon.",
     ["M373e", "M376g"]),
   P(MS, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. After Omega and the primal fell in Gyr Abania, it moved to secure the Wall, which has fallen to it.",
     ["M379b", "M379d", "M379n"]),
 ],
 "org-garlean-empire": [
   P(MS, None, "main", "The Garlean Empire",
     "An empire that has tried to conquer Eorzea, and has long known of Omega. It has lost the Wall to the Alliance; in Ala Mhigo, its Viceroy expects the coming days to be most interesting.",
     ["M378h", "M379n", "M379p"]),
 ],
}

# ---- Arc entries: one recap per step -----------------------------------------------------------------------------------
N1, N2, N3, N4, N5, N6, N7 = ("The Lost Scions", "The Conference at Falcon's Nest", "The Final Chorus", "The Warriors' Plot",
                              "A Trail of Crystals", "The Griffin's Gambit", "Waking Omega")
LEAD1 = "Thancred and Minfilia have been missing since the Scions fled the royal banquet in Ul'dah. "
LEAD2 = "Ser Aymeric has called a peace conference at Falcon's Nest, to be attended by Vidofnir, though Nidhogg opposes any peace. "
LEAD3 = "Nidhogg's shade wears Estinien's body, and struck down Vidofnir at the peace conference. "
LEAD4 = "The Warriors of Darkness and the Ascians mean to bring about another Umbral Calamity. "
LEAD5 = "Crystals smuggled out of Ishgard reached refugees fighting for Ala Mhigan liberation. "
LEAD6 = "The masked Griffin of the Ala Mhigan Resistance means to assault the Wall from the Ala Mhigan side and spread war to Eorzea. "

PRES.update({
 "evt-the-lost-scions": [
   P(G336, None, "main", N1,
     "In Ishgard, Ser Aymeric has taken up the vacant archbishop's duties, and sends Lucia, with you and Alphinaud, to Anyx Trine to restore relations with Hraesvelgr's brood through Vidofnir. "
     "Meanwhile the hunt for Minfilia and Thancred is at a standstill, though Riol's men have leads on F'lhaminn, Yda and Papalymo, and a Sharlayan scholar of the Students of Baldesion is coming to help.",
     ["M336a", "M336d", "M336g", "M336h", "M336i", "M336j"]),
   P(G337, None, "main", N1,
     LEAD1 + "At Anyx Trine, Lucia told Vidofnir that King Thordan betrayed and murdered Ratatoskr; Vidofnir must consult her sire before answering. "
     "You went on west to join Y'shtola in welcoming the Sharlayan scholar who will help the search.",
     ["M336g", "M337a", "M337c", "M337f", "M336j"]),
   P(G338, None, "main", N1,
     LEAD1 + "The Sharlayan scholar who came to help is Krile, Minfilia's dear friend, who knew the twins at the Studium. She hopes to follow the trail Thancred left when Y'shtola sent him away, "
     "but needs Matoya's Crystal Eye. Vidofnir seemed open to Ishgard's proposal.",
     ["M336g", "M338a", "M338b", "M338f", "M338c", "M338d"]),
   P(G339, None, "main", N1,
     LEAD1 + "Krile, who has the Echo, persuaded Matoya to lend her the Crystal Eye, an ancient Crystal of Light, and traced Thancred to the foot of Sohm Al. "
     "Tailfeather's hunters speak of an axe-wielding stranger, and a Vath trader sought fine garments for someone.",
     ["M336g", "M339a", "M339d", "M339e", "M339f", "M339g"]),
   P(G340, None, "main", N1,
     "Minfilia has been missing since the Scions fled the royal banquet in Ul'dah, but you found Thancred: Y'shtola's forbidden magicks sent him into the wilderness, "
     "and he followed the Vath's tales to the Gnath, who had summoned Ravana again. A party of adventurers had already beaten Ravana; their leader named them the Warriors of Darkness, "
     "walkers of a different path, and a memory he showed recalled a man in black, perhaps an Ascian.",
     ["C17", "M340c", "M340a", "M340b", "M340d", "M340e", "M340f"]),
   P(G341, None, "main", N1,
     "Thancred is back, but Minfilia, Yda and Papalymo are still missing, and Krile has gone to Matoya for help finding Minfilia. Vidofnir, glad Ravana fell, will journey to Ishgard "
     "with Hraesvelgr's leave. The Warriors of Darkness have the Echo and are driven to put down primals. In Ishgard, Ser Aymeric was stabbed, and fires are spreading through the city.",
     ["M341j", "M341i", "M341a", "M341c", "M341e", "M341f", "M341h"]),
   P(G342, None, "main", N1,
     "Minfilia, Yda and Papalymo are still missing. In Ishgard, where Ser Aymeric was stabbed, Lucia set you hunting the arsonists behind the spreading fires. "
     "Thancred tricked a captive into confessing, and the fires proved the work of someone of influence. House Fortemps grieves: Lord Artoirel's father is slandered and his half-brother newly dead.",
     ["M341j", "M341f", "M342a", "M342c", "M342d", "M342e"]),
   P(G343, None, "main", N1,
     "Minfilia is still missing. In Ishgard the True Brothers of the Faith seized the Vault and its refugees; you, Aymeric and Artoirel freed all but one, "
     "and Vidofnir caught the girl Maelie when a priest threw her from the ledge, then warned Nidhogg and his brood have flown. Count Edmont steps aside for Artoirel, "
     "and Y'shtola suspects Thancred has lost his magicks. Urianger met Elidibus and the Warriors' leader, and Yda and Papalymo are with the Ala Mhigan Resistance.",
     ["M343a", "M343b", "M343c", "M343d", "M343f", "M343i", "M343j", "M343l"]),
   P(G344, None, "main", N1,
     "F'lhaminn, Hoary Boulder and Coultenet are home, but Minfilia, Yda and Papalymo are still missing, and F'lhaminn asks after her daughter. Alphinaud blames his ambition for the Scions' flight. "
     "Krile believes Hydaelyn's intercession left a trace that could lead to Minfilia, and has gone with Thancred to read the aether in Castrum Meridianum.",
     ["M344a", "M344g", "M344d", "M344f", "M344b", "M344c"]),
   P(G345, None, "main", N1,
     "Krile found the aether signature of Hydaelyn's intercession, and believes Hydaelyn guided Minfilia to Her realm. In the Antitower, a Sharlayan watchtower over the aetherial sea, "
     "a voice calling itself the Word of the Mother said it was once Minfilia. It told how Hydaelyn banished the Darkness, and how the Ascians have succeeded seven times. "
     "Krile thinks Minfilia, joined with Hydaelyn, struggles to keep her form; Matoya says she threw herself on the fire, and Thancred stormed out.",
     ["M345a", "M345b", "M345c", "M345e", "M345f", "M345g", "M345h", "M345i", "M345j"]),
 ],
 "evt-falcons-nest-conference": [
   P(G346, None, "main", N2,
     "Ser Aymeric means to make peace with the Dravanians: Vidofnir's rescue of a child gave hope, and he is arranging a peace conference at Falcon's Nest for her to attend, "
     "with you there in case Nidhogg, implacably opposed, tries to disrupt it. There Lucia, once a foreign spy who pledged herself to Ishgard, oversees a relief to be unveiled. "
     "Alphinaud asks you to keep Minfilia's fate from the others.",
     ["M346b", "M346c", "M346d", "M346e", "M346f", "M346g", "M346a"]),
   P(G347, None, "main", N2,
     LEAD2 + "A small party of Convictors has pledged to attack any Dravanians flying in, so Lucia rode out to them with Lord Artoirel, "
     "who asked you to look after his impulsive, melancholy brother Emmanellain.",
     ["M346c", "M346d", "M347a", "M347b", "M347c", "M347d"]),
   P(G348, None, "main", N2,
     LEAD2 + "Lucia and Lord Artoirel have ridden out to defiant Convictors. Emmanellain, forbidden to leave, sent you and Thancred to cull wolves in the wastes, where Thancred saved two heretics.",
     ["M346c", "M347b", "M348a", "M348b", "M348c"]),
   P(G349, None, "main", N2,
     LEAD2 + "Then a waitress drugged you, and a protest turned to bloodshed: when its leader cried for vengeance on the Dravanians, Emmanellain panicked and commanded a knight to act, "
     "and she was shot down. The knight says he followed Emmanellain's order, and the conference has no chance in this climate.",
     ["M346c", "M349a", "M349b", "M349c", "M349d", "M349e"]),
   P(G350, None, "main", N2,
     "Ser Aymeric's peace conference at Falcon's Nest ended in bloodshed: protesters came in as servants and guests, a Convictory incident drew Lucia and Lord Artoirel away, "
     "and Emmanellain's knight shot down the protest leader, who yet lives. Lucia has suspended the conference pending Aymeric's decision, and Artoirel ordered Emmanellain home. "
     "Honoroit was beaten for trying to stop the smallfolk leaving, and Thancred struck Emmanellain when he lashed out.",
     ["M350a", "M350b", "M350c", "M350d", "M350e", "M350g"]),
   P(G351, None, "main", N2,
     "The peace conference at Falcon's Nest was suspended after a protest ended in bloodshed and Emmanellain's disgrace. To lift Ishgard's spirits, Ser Aymeric will present the Alliance's "
     "joint exercises as a grand melee, and you have agreed to fight for Ishgard; Emmanellain, inspired by Aymeric, begged to fight too. "
     "Some in the streets call Aymeric a patricide, and Thancred reminds you the Ascians sought to profit from the war.",
     ["M350g", "M351a", "M351g", "M351d", "M351f", "M351h"]),
   P(G352, None, "main", N2,
     "The peace conference at Falcon's Nest was suspended after a protest ended in bloodshed. At the grand melee outside Ishgard you bore House Fortemps's colors; "
     "General Raubahn swept aside all comers and challenged you to single combat, and when you prevailed, Ser Aymeric proclaimed victory for Ishgard.",
     ["M350g", "M352a", "M352b", "M352c", "M352d"]),
   P(G353, None, "main", N2,
     "After Ishgard's victory in the grand melee, Ser Aymeric reconvened the peace conference at Falcon's Nest. As he and Vidofnir spoke of peace at the unveiling, "
     "Estinien leapt down and drove his lance into her back: Nidhogg's eyes are fused to him, and with a wyrm's voice he declared the final chorus nigh. Vidofnir was carried to Anyx Trine.",
     ["M352c", "M353b", "M353c", "M353d", "M353e", "M353f", "M353g"]),
   P(G354, None, "main", N2,
     "At the reconvened peace conference, Estinien, possessed by Nidhogg, struck down Vidofnir, and Nidhogg's kin raise the final chorus of the Dragonsong War. "
     "Alphinaud expects Ser Aymeric to do what he must when Nidhogg leads the Horde; though Ishgard may sacrifice Estinien to slay the wyrm, Alphinaud will not. "
     "Krile felt the wyrm's hatred about Estinien even before his change. Far away, Papalymo warns Yda not to trust too soon.",
     ["M353d", "M353e", "M354e", "M354c", "M354a", "M354d", "M354g"]),
 ],
 "evt-the-final-chorus": [
   P(G355, None, "main", N3,
     LEAD3 + "Y'shtola and Krile believe Estinien's spirit survives within the wyrm's will, and Alphinaud means to free him by tearing the eyes from his armor, "
     "though Krile warns whoever does may become Nidhogg's next host. In Ishgard, fear has turned to fury.",
     ["M353d", "M355a", "M355b", "M355c", "M355d", "M355e"]),
   P(G356, None, "main", N3,
     LEAD3 + "With both eyes he cannot be repelled by any mortal force, so Ser Aymeric seeks his brood-brother Hraesvelgr as Ishgard's ally, though Estinien reported Hraesvelgr's unwillingness "
     "to meddle in men's affairs. At Anyx Trine the wounded Vidofnir expects her sire to refuse.",
     ["M353d", "M356a", "M356b", "M356d", "M356e", "M356f"]),
   P(G357, None, "main", N3,
     LEAD3 + "At Zenith, Hraesvelgr recalled how men tore down the bridge between man and dragon, and Ser Aymeric admitted he asked you to slay his own father. "
     "Only when Midgardsormr appeared did Hraesvelgr agree to test you, and after the trial at Sohr Khai he pledged his aid against Nidhogg. Then a roar announced the Dravanian Horde's advance.",
     ["M353d", "M357a", "M357b", "M357d", "M357e", "M357f"]),
   P(G358, None, "main", N3,
     "Hraesvelgr carried you to Ishgard and tried in vain to turn Nidhogg from vengeance, then fell beaten on the bridge, having given you half his power. "
     "With it you subdued Nidhogg's shade, tore his eyes from Estinien's armor and cast them into the abyss; Nidhogg's spirit was undone by mortal will, and his Horde scattered. "
     "Estinien lives, and Ser Aymeric bore him home.",
     ["M358a", "M358b", "M358c", "M358d", "M358e", "M358f", "M358g", "M358h"]),
   P(G359, None, "main", N3,
     "With Hraesvelgr's aid you destroyed Nidhogg's shade and freed Estinien, and the Horde scattered. Ishgard hails you, but Estinien has not woken: his mind and body were held hostage "
     "for many days, and Alphinaud, who counts freeing him the greater feat, keeps vigil at his bedside.",
     ["M358f", "M358h", "M359a", "M359b", "M359c", "M359e"]),
   P(G360, None, "main", N3,
     "Nidhogg is destroyed and Estinien freed. On waking, Estinien laid down the mantle of Azure Dragoon, and Ser Aymeric abolished the archbishops' thousand-year rule: "
     "a House of Commons and a House of Lords now govern Ishgard, and Aymeric sits in the Lords' highest seat. Estinien has disappeared. "
     "Elsewhere, Elidibus and the Warriors of Darkness's leader plot together, and caught Alisaie eavesdropping before Thancred intervened.",
     ["M358f", "M360c", "M360a", "M360b", "M360f", "M360h", "M360i"]),
 ],
 "evt-the-warriors-plot": [
   P(G361, None, "main", N4,
     "Over dinner with Ser Aymeric, now lord speaker of Ishgard's House of Lords, news came that Thancred had returned with Alisaie, Alphinaud's twin, poisoned on the trail of the Warriors of Darkness. "
     "She warned that the Warriors and the Ascians are goading the Ixal to summon Garuda in Xelphatol, so the Warriors can slay her.",
     ["M361a", "M361c", "M361d", "M361e", "M361f", "M361g"]),
   P(G362, None, "main", N4,
     "The Warriors of Darkness and the Ascians goaded the Ixal into summoning Garuda, but in Xelphatol you stopped the ritual. Then the Warriors' leader explained: "
     "their world held far more Light than Dark, and they joined their former enemies, the Ascians, to come here and bring another Umbral Calamity, for only the Ardor can save their home. "
     "Alphinaud vows the sacrifice ends here.",
     ["M361g", "M362b", "M362c", "M362d", "M362e", "M362f", "M362g", "M362i"]),
   P(G363, None, "main", N4,
     LEAD4 + "Alisaie is recovering, and with Thancred found that the Ascians keep crystals flowing to the beast tribes. The Scions split up to cut off the supply: "
     "Y'shtola and Krile go to Xelphatol, and you, Alphinaud and Alisaie, on Urianger's word, to Vylbrand, where the kobolds may summon Titan again.",
     ["M362f", "M363a", "M363b", "M363d", "M363f", "M363h"]),
   P(G364, None, "main", N4,
     LEAD4 + "In Vylbrand, the kobold child Ga Bu begged the Maelstrom to stop his patriarch from summoning Titan again; his parents spoke out and were taken away. "
     "You and the twins will infiltrate the stronghold, secure the crystals and free the prisoners.",
     ["M362f", "M364a", "M364b", "M364c", "M364d", "M364e"]),
   P(G365, None, "main", N4,
     LEAD4 + "In Vylbrand, the kobolds' crystals proved smuggled out of Ishgard. In the Navel you found Ga Bu's parents and the other prisoners already executed, and his grief birthed Titan. "
     "Titan is no more, but Ga Bu may have fallen under the primal's influence.",
     ["M362f", "M365a", "M365b", "M365c", "M365e", "M365f"]),
 ],
 "evt-a-trail-of-crystals": [
   P(G366, None, "main", N5,
     "After Titan's fall, Alisaie left the grieving Ga Bu with Commander Bloeidin. Urianger found a Rejoining would kill everyone on a reflection of the Source, "
     "and traced the Ishgardian smugglers to the Ivy's network: they served a man in black robes, and sent crystals to refugees fighting for Ala Mhigan liberation. "
     "You head for Little Ala Mhigo, while Alisaie watches Urianger with suspicion. A masked man tells the Warriors of Darkness's leader the Ardor is not the Ascians' alone.",
     ["M366a", "M366c", "M366d", "M366f", "M366e", "M366g", "M366h"]),
   P(G367, None, "main", N5,
     LEAD5 + "In Little Ala Mhigo the trail leads to the Masks, followers of a masked revolutionary called the Griffin, rumored to hold a secret weapon against the Garleans. "
     "At Qarn you found Yda and Papalymo, who fled Ul'dah with Resistance friends, and learned the speaker you heard was not the Griffin but an impersonator.",
     ["M366e", "M367b", "M367c", "M367d", "M367e", "M367f", "M367h"]),
   P(G368, None, "main", N5,
     LEAD5 + "The Griffin's double admits the Masks traded them to the Amalj'aa, to summon their god in return for help fighting for Ala Mhigo; Yda names the god as Ifrit. "
     "Papalymo forbade Yda to join the Masks, and the two will search for the cache.",
     ["M366e", "M368a", "M368b", "M368c", "M368e", "M368f"]),
   P(G369, None, "main", N5,
     "The crystals led to Zahar'ak, but in the Bowl of Embers the Warriors of Darkness waited to kill you. The masked man, Urianger, broke your chains: a double agent who had manipulated them. "
     "The Warriors were already dead, heroes of a world that fell anyway. Urianger confessed he did it to free Minfilia: Hydaelyn set her free as Her emissary, "
     "and she left with the Warriors for their world, promising to return.",
     ["M369a", "M369c", "M369d", "M369e", "M369f", "M369g", "M369h", "M369i", "M369l"]),
   P(G370, None, "main", N5,
     "Minfilia has gone with the Warriors of Darkness to their world, freed by a plan of Urianger's that Alisaie cannot condone. Thancred secured the crystals, and Yda and Papalymo rejoined the Scions, "
     "who now let each member pursue what best keeps the realm safe; Krile and Alisaie are full members. Elsewhere, Elidibus presented the Eyes of Nidhogg to the Griffin.",
     ["M369i", "M370a", "M370b", "M370c", "M370f", "M370g", "M370j"]),
 ],
 "evt-the-griffins-gambit": [
   P(G371, None, "main", N6,
     "A wounded Resistance messenger reached the Scions: the masked Griffin, one of the Resistance leaders, means to assault the Wall from the Ala Mhigan side to spread war to Eorzea. "
     "Y'shtola sent you to Ishgard, where Ser Aymeric agreed to send an envoy to the Alliance council. Alphinaud proposes electing a coordinator as Minfilia's successor.",
     ["M371b", "M371c", "M371d", "M371e", "M371f", "M371a"]),
   P(G372, None, "main", N6,
     LEAD6 + "Ser Aymeric goes to the Alliance council as Ishgard's envoy, having readied Camp Dragonhead, now under Emmanellain, against trouble in the Black Shroud.",
     ["M371c", "M372a", "M372b", "M372c"]),
   P(G373, None, "main", N6,
     LEAD6 + "The Alliance council, joined by Ser Aymeric, agreed to reinforce Gridania's border with an Ishgardian force and Doman shinobi, but Alphinaud fears readying for war "
     "gives the Griffin what he wants. Riol reports the missing Scions have been found.",
     ["M371c", "M373c", "M373d", "M373e", "M373f", "M373g"]),
   P(G374, None, "main", N6,
     "The Griffin's soldiers attacked the Wall in Grand Company uniforms: the Wall was bait. On top you beat him, and he was unmasked as Ilberd, the disgraced captain of the Crystal Braves. "
     "With Nidhogg's eyes and Ala Mhigan desperation, his death completed a ritual to summon a primal. Papalymo, with Tupsimati, sealed it in a cocoon of light at the cost of his life, "
     "leaving Yda broken, and you escaped on Hilda's airship.",
     ["M374b", "M374c", "M374d", "M374e", "M374f", "M374g", "M374i", "M374j"]),
   P(G375, None, "main", N6,
     "On the Wall, the Griffin was unmasked as Ilberd, whose death summoned a primal, and Papalymo gave his life to seal it in a cocoon of light. The Scions mourn him; "
     "the primal will not be contained forever, Y'shtola and Krile will inspect the cocoon, and no one knows how Ilberd came by Nidhogg's eyes. Alphinaud calls for preparations.",
     ["M374d", "M374g", "M375a", "M375b", "M375c", "M375d", "M375f"]),
 ],
 "evt-waking-omega": [
   P(G376, None, "main", N7,
     "The primal Ilberd summoned waits in a cocoon of light above the Wall, sealed by Papalymo's sacrifice; a Garlean airship that approached was destroyed. "
     "Nero, a former tribunus who studied beside Cid, offered the Alliance council Omega, an Allagan weapon beneath Carteneau, and the council sent Cid's contingent to take command of it. "
     "Alphinaud wonders how Nero learned of the meeting.",
     ["M374g", "M376a", "M376b", "M376c", "M376e", "M376f", "M376g", "M376i"]),
   P(G377, None, "main", N7,
     "The Alliance sent Cid's contingent, with Nero, to wake Omega beneath Carteneau against the primal in the cocoon, and Alisaie insists Nero never leave her sight. "
     "Gosetsu brought word that Doma calls Yugiri home, but she stays to face the crisis, and Gosetsu joins the expedition. Tataru sewed you an outfit with a charm to bring you home.",
     ["M376g", "M377a", "M377b", "M377e", "M377f", "M377g", "M377h"]),
   P(G378, None, "main", N7,
     "In Carteneau, Cid and Nero roused Omega while you, Yda and the Domans held off an imperial attack. Omega was expected to seek out the primal at the Wall. "
     "Yda launched it for Papalymo's sake; then its signal fell silent and Cid reengaged its stasis, and Papalymo's spell, bound to his aether, is fading.",
     ["M378a", "M378c", "M378d", "M378e", "M378f", "M378g"]),
   P(MS, None, "main", N7,
     "Omega reached the cocoon as it hatched, and a great dragon the Domans call Shinryu rose from it; the two fought over Gyr Abania and fell together onto Ala Mhigan soil. "
     "The Alliance has taken the Wall, and Ser Aymeric proposes contacting the Resistance. Yda revealed she is Lyse, sister of the true Yda, who died six years ago, "
     "and she will carry on her family's fight for Ala Mhigo. In Ala Mhigo, an imperial Viceroy expects interesting days.",
     ["M379a", "M379b", "M379c", "M379n", "M379f", "M379g", "M379i", "M379l", "M379p"]),
 ],
})

# ---- Relationship types and relationships ------------------------------------------------------------------------------
TYPES = [("child-of", "child of", "parent of", False)]

RELS = [
 ("rel-aymeric-leads-holy-see", "char-aymeric", "leads", "org-holy-see", G336, G360, "main", ["M336a"], ["M360a"]),
 ("rel-aymeric-leads-house-of-lords", "char-aymeric", "leads", "org-house-of-lords", G360, None, "main", ["M360b"]),
 ("rel-vidofnir-child-of-hraesvelgr", "char-vidofnir", "child-of", "char-hraesvelgr", G337, None, "main", ["M337c"]),
 ("rel-vidofnir-aids-aymeric", "char-vidofnir", "aids", "char-aymeric", G341, None, "main", ["M341c"]),
 ("rel-nidhogg-opposes-vidofnir", "char-nidhogg", "opposes", "char-vidofnir", G353, G358, "main", ["M353d", "M353e"], ["M358f"]),
 ("rel-hraesvelgr-opposes-nidhogg", "char-hraesvelgr", "opposes", "char-nidhogg", G357, G358, "main", ["M357e"], ["M358f"]),
 ("rel-hraesvelgr-aids-aymeric", "char-hraesvelgr", "aids", "char-aymeric", G357, None, "main", ["M357e", "M357g"]),
 ("rel-alphinaud-aids-estinien", "char-alphinaud", "aids", "char-estinien", G354, None, "main", ["M354a", "M354b"]),
 ("rel-emmanellain-serves-artoirel", "char-emmanellain", "serves", "char-artoirel", G353, None, "main", ["M353h"]),
 ("rel-krile-aids-scions", "char-krile", "aids", "org-scions", G338, G370, "main", ["M336j", "M338a"], ["M370g"]),
 ("rel-krile-member-scions", "char-krile", "member-of", "org-scions", G370, None, "main", ["M370g"]),
 ("rel-elidibus-allied-with-warriors-of-darkness", "char-elidibus", "allied-with", "org-warriors-of-darkness", G360, G369, "main", ["M343j", "M360h"], ["M369k"]),
 ("rel-warriors-of-darkness-allied-with-ascians", "org-warriors-of-darkness", "allied-with", "org-ascians", G361, G369, "main", ["M361g"], ["M369k"]),
 ("rel-warriors-of-darkness-opposes-scions", "org-warriors-of-darkness", "opposes", "org-scions", G362, G369, "main", ["M362h", "M362i"], ["M369c", "M369k"]),
 ("rel-masked-man-aids-warriors-of-darkness", "char-masked-man", "aids", "org-warriors-of-darkness", G366, G369, "main", ["M366h"], ["M369d"]),
 ("rel-masked-man-revealed-as-urianger", "char-masked-man", "revealed-as", "char-urianger", G369, None, "main", ["M369d", "M369e"]),
 ("rel-ga-bu-aids-scions", "char-ga-bu", "aids", "org-scions", G364, None, "main", ["M364b", "M364e"]),
 ("rel-masks-member-of-ala-mhigan-resistance", "org-masks", "member-of", "org-ala-mhigan-resistance", G343, None, "main", ["M343l"]),
 ("rel-yda-aids-ala-mhigan-resistance", "char-yda", "aids", "org-ala-mhigan-resistance", G367, G370, "main", ["M367f"], ["M370c"]),
 ("rel-papalymo-aids-ala-mhigan-resistance", "char-papalymo", "aids", "org-ala-mhigan-resistance", G367, G370, "main", ["M367f"], ["M370c"]),
 ("rel-griffin-leads-masks", "char-griffin", "leads", "org-masks", G367, G374, "main", ["M367b", "M367c"], ["M374f"]),
 ("rel-griffin-member-of-ala-mhigan-resistance", "char-griffin", "member-of", "org-ala-mhigan-resistance", G371, G374, "main", ["M371b"], ["M374f"]),
 ("rel-elidibus-aids-griffin", "char-elidibus", "aids", "char-griffin", G370, G374, "main", ["M370j"], ["M374f"]),
 ("rel-griffin-revealed-as-ilberd", "char-griffin", "revealed-as", "char-ilberd", G374, None, "main", ["M374d"]),
 ("rel-shinryu-summoned-by-ilberd", "char-shinryu", "summoned-by", "char-ilberd", G374, None, "main", ["M374e", "M374f"]),
 ("rel-nero-aids-eorzean-alliance", "char-nero", "aids", "org-eorzean-alliance", G376, None, "main", ["M376c", "M376g"]),
 ("rel-gosetsu-aids-scions", "char-gosetsu", "aids", "org-scions", G377, None, "main", ["M377e", "M377f"]),
 ("rel-yda-revealed-as-lyse", "char-yda", "revealed-as", "char-lyse", MS, None, "main", ["M379g", "M379h"]),
 ("rel-lyse-member-scions", "char-lyse", "member-of", "org-scions", MS, None, "main", ["M379g", "M379k"]),
 ("rel-zenos-member-garlean-empire", "char-zenos", "member-of", "org-garlean-empire", MS, None, "main", ["M379n", "M379o"]),
]

# Relationships the accepted content or an earlier era defined, ended here.
ADJUST = {
 "rel-minfilia-leads-scions": {"until": G345, "end": ["M345e", "M345i"]},          # accepted (pilot)
 "rel-papalymo-member-scions": {"until": G374, "end": ["M374g"]},                  # accepted (NDL-012)
 "rel-yda-member-scions": {"until": MS},                                           # accepted (NDL-012); Lyse carries it on
 "rel-estinien-possessed-by-nidhogg": {"until": G358, "end": ["M358e", "M358f"]},  # content_3_0_part2
 "rel-estinien-opposes-nidhogg": {"until": G358, "end": ["M358f"]},                 # content_3_0_part1: the shade is undone
 "rel-nidhogg-leads-dravanian-horde": {"until": G358, "end": ["M358h"]},            # content_2_4_to_2_55 / content_3_0_part1
 "rel-scions-headquartered-at-fortemps-manor": {"until": G370, "end": ["M370l"]},   # content_3_0_part1: back at the Rising Stones
}

# ---- Arcs ----------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-g1-the-lost-scions", "evt-the-lost-scions", G336, G345),
 ("arc-g2-falcons-nest-conference", "evt-falcons-nest-conference", G346, G354),
 ("arc-g3-the-final-chorus", "evt-the-final-chorus", G355, G360),
 ("arc-g4-the-warriors-plot", "evt-the-warriors-plot", G361, G365),
 ("arc-g5-a-trail-of-crystals", "evt-a-trail-of-crystals", G366, G370),
 ("arc-g6-the-griffins-gambit", "evt-the-griffins-gambit", G371, G375),
 ("arc-g7-waking-omega", "evt-waking-omega", G376, MS),
]

CASTS = {
 "evt-the-lost-scions": [
   ("char-alphinaud", G336, ["M336k"]), ("char-aymeric", G336, ["M336a"]), ("char-lucia", G336, ["M336d"]),
   ("char-vidofnir", G336, ["M336d"]), ("char-minfilia", G336, ["M336g"]), ("char-yshtola", G337, ["M337f"]),
   ("char-krile", G338, ["M338a"]), ("char-matoya", G338, ["M338c"]), ("char-thancred", G339, ["M339f"]),
   ("org-warriors-of-darkness", G340, ["M340e"]),
 ],
 "evt-falcons-nest-conference": [
   ("char-aymeric", G346, ["M346c"]), ("char-lucia", G346, ["M346e"]), ("char-alphinaud", G346, ["M346a"]),
   ("char-nidhogg", G346, ["M346d"]), ("char-vidofnir", G346, ["M346c"]), ("char-artoirel", G347, ["M347b"]),
   ("char-emmanellain", G347, ["M347c"]), ("char-thancred", G348, ["M348b"]), ("char-honoroit", G350, ["M350d"]),
   ("char-estinien", G353, ["M353d"]),
 ],
 "evt-the-final-chorus": [
   ("char-alphinaud", G355, ["M355b"]), ("char-krile", G355, ["M355c"]), ("char-yshtola", G355, ["M355a"]),
   ("char-estinien", G355, ["M355a"]), ("char-nidhogg", G355, ["M355d"]), ("char-aymeric", G356, ["M356a"]),
   ("char-hraesvelgr", G356, ["M356a"]), ("char-vidofnir", G356, ["M356e"]), ("org-dravanian-horde", G357, ["M357f"]),
   ("char-elidibus", G360, ["M360h"]),
 ],
 "evt-the-warriors-plot": [
   ("char-alisaie", G361, ["M361c"]), ("char-thancred", G361, ["M361d"]), ("char-alphinaud", G361, ["M361c"]),
   ("org-warriors-of-darkness", G361, ["M361g"]), ("org-ascians", G361, ["M361g"]), ("char-garuda", G361, ["M361f"]),
   ("char-yshtola", G363, ["M363d"]), ("char-urianger", G363, ["M363f"]), ("char-titan", G363, ["M363f"]),
   ("char-ga-bu", G364, ["M364b"]),
 ],
 "evt-a-trail-of-crystals": [
   ("char-alphinaud", G366, ["M366e"]), ("char-alisaie", G366, ["M366g"]), ("char-urianger", G366, ["M366c"]),
   ("char-masked-man", G366, ["M366h"]), ("char-griffin", G367, ["M367b"]), ("org-masks", G367, ["M367d"]),
   ("char-yda", G367, ["M367e"]), ("char-papalymo", G367, ["M367e"]), ("org-warriors-of-darkness", G369, ["M369c"]),
   ("char-minfilia", G369, ["M369i"]),
 ],
 "evt-the-griffins-gambit": [
   ("char-alphinaud", G371, ["M371a"]), ("char-yshtola", G371, ["M371e"]), ("char-griffin", G371, ["M371b"]),
   ("org-ala-mhigan-resistance", G371, ["M371b"]), ("char-aymeric", G371, ["M371f"]), ("org-eorzean-alliance", G373, ["M373e"]),
   ("char-papalymo", G374, ["M374g"]), ("char-yda", G374, ["M374j"]), ("char-ilberd", G374, ["M374d"]),
   ("char-shinryu", G374, ["M374e"]),
 ],
 "evt-waking-omega": [
   ("char-cid", G376, ["M376g"]), ("char-nero", G376, ["M376c"]), ("char-alphinaud", G376, ["M376i"]),
   ("char-shinryu", G376, ["M376a"]), ("org-eorzean-alliance", G376, ["M376g"]), ("char-alisaie", G376, ["M376h"]),
   ("char-gosetsu", G377, ["M377f"]), ("char-yda", G378, ["M378e"]), ("char-lyse", MS, ["M379g"]),
   ("char-zenos", MS, ["M379n"]),
 ],
}

ARC_NOTES = {
 "arc-g1-the-lost-scions": "MSQ #336 *An Uncertain Future* to #345 *The Word of the Mother* (patches 3.1 and the start of 3.2): the search for the Scions lost at the 2.55 banquet, "
   "from the standstill (M336g) through Krile, Thancred's return and the Warriors of Darkness, to Minfilia's fate atop the Antitower (M345e). Ishgard's arson and the Vault siege (#341–#343) "
   "run inside it as a second strand; its cast leaves them to the entity records. Its name avoids #341's *Dreams of the Lost*.",
 "arc-g2-falcons-nest-conference": "MSQ #346 *This War of Ours* to #354 *Causes and Costs*: Aymeric's peace conference, from its announcement (M346c) through the protest, "
   "the grand melee and Estinien's attack on Vidofnir (M353d), ending on Alphinaud's vow to save Estinien (M354a).",
 "arc-g3-the-final-chorus": "MSQ #355 *The Man Within* to #360 *Litany of Peace* (3.3): the plan to free Estinien, Hraesvelgr's alliance and Nidhogg's end (M358f), "
   "closing on the new republic (M360a). The final step also shows Elidibus with the Warriors, which opens the next arc.",
 "arc-g4-the-warriors-plot": "MSQ #361 *Promises Kept* to #365 *The Beast That Mourned at the Heart of the Mountain*: Alisaie's warning (M361g), Xelphatol and the Warriors' aims (M362e), "
   "and the crystal trail to Vylbrand ending in Titan's fall (M365e).",
 "arc-g5-a-trail-of-crystals": "MSQ #366 *Beneath a Star-filled Sky* to #370 *An Ending to Mark a New Beginning*: the smugglers' crystals lead to Little Ala Mhigo and the Masks (M366e, M367d), "
   "then to the Bowl of Embers, Urianger's reveal and Minfilia's departure (M369d, M369i), closing on the Scions' new shape (M370f). The name avoids the entity name \"The Masks\", "
   "which is not visible at #366.",
 "arc-g6-the-griffins-gambit": "MSQ #371 *Tidings from Gyr Abania* to #375 *Louisoix's Finest Student* (3.5): the Griffin's threat (M371c) through the Alliance council and the Wall, "
   "where he is unmasked as Ilberd and Papalymo seals the primal (M374d, M374g), ending on the Scions' mourning.",
 "arc-g7-waking-omega": "MSQ #376 *The Obvious Solution* to the cp-hw-3-56 milestone (after *The Far Edge of Fate*, 3.56): Nero's offer of Omega (M376c), the expedition, "
   "the launch, and the milestone's outcome: Shinryu named, the Wall taken, and Yda revealed as Lyse (M379g).",
}

DECISIONS = [
 "**Seven arcs (g1–g7)** cover every step from #336 to cp-hw-3-56 without sharing steps; casts stop at ten, so the Ishgard arson strand of 3.1 lives in the entity records rather than g1's cast.",
 "**Reveals as relationships:** the masked man → Urianger (#369), the Griffin → Ilberd (#374) and Yda → Lyse (cp-hw-3-56) follow the Marques → Cid pattern; each new identity carries the old name as an alias.",
 "**The primal** is one entity, `char-shinryu`, named \"Ilberd's primal\" from #374 and \"Shinryu\" only at cp-hw-3-56, where the pages first name it.",
 "**The Viceroy** (`char-zenos`) is named \"The Viceroy\": the 3.56 page names him only in a speaker tag (`Zenos yae Galvus@Viceroy`), so the game shows his title, not his name.",
 "**The Warriors of Darkness' leader** stays unnamed (\"the Warriors' leader\"): the pages name him only in speaker tags; the band is `org-warriors-of-darkness`.",
 "**Baelsar's Wall** is \"the Wall\" in displayed text, because \"Baelsar\" is a banned surname.",
 "**Accepted relationships ended here:** Minfilia stops leading the Scions at #345, Papalymo's membership ends at #374 (his death), and Yda's at cp-hw-3-56, where `rel-lyse-member-scions` carries it on.",
 "**Ilberd** (`char-ilberd`, from the 2.1 era) gets one record here, at #374, where he is unmasked as the Griffin.",
 "**Omega has no entity here:** 2.x text already names it (#190), so an entity first visible at #376 fails the lint. Its three records are kept in `OMEGA_DRAFT` for an earlier era to adopt with `char-omega`.",
 "**Left out as entities** (named in text only, since accepted text already names them or they are incidental): Ishgard, House Fortemps, Raubahn, Yugiri, Hydaelyn, Midgardsormr, Hilda, Gundobald, Bloeidin, F'lhaminn.",
]

ALLOW = {
 "Warriors of Darkness": G340,   # the band names itself in #340's main dialogue
 "Word of the Mother": G345,     # #345's quest title, and the voice's own name there
 "The First": G362,              # #362's quest title (Shadows of the First); never used in displayed text
 "Nero": G376,                   # introduces himself to the Alliance council in #376
 "Lyse": MS,                     # revealed in The Far Edge of Fate (the cp-hw-3-56 milestone)
}

# Not loaded by the builder: Omega's records for this era, for the lead to merge if an earlier era creates char-omega
# (2.x text already names Omega from #190, so this era cannot introduce the entity). Relationship drafts:
#   ("rel-cid-controls-omega", "char-cid", "controls", "char-omega", G376, None, "main", ["M376g"]),
#   ("rel-omega-opposes-shinryu", "char-omega", "opposes", "char-shinryu", G378, None, "main", ["M378d", "M378e"]),
OMEGA_DRAFT = {
 "char-omega": [
   P(G376, None, "main", "Omega",
     "An Allagan weapon that has lain beneath Carteneau since the Allagans fell. Nero proposed it against the primal in the cocoon, "
     "and the Alliance gave Cid's contingent authority to take command of it.",
     ["M376c", "M376f", "M376g"]),
   P(G378, None, "main", "Omega",
     "An Allagan weapon from beneath Carteneau, which the Empire has long known of. Cid and Nero roused it, expecting it to seek out the primal at the Wall, and Yda launched it; "
     "then its signal fell silent, and Cid reengaged its stasis.",
     ["M376f", "M378a", "M378d", "M378e", "M378f", "M378h"]),
   P(MS, None, "main", "Omega",
     "An Allagan weapon from beneath Carteneau. The cocoon hatched as it arrived, and it fought the great dragon that rose from it; the two fell together onto Ala Mhigan soil. "
     "With its stasis reengaged, it is useless to the Empire.",
     ["M379a", "M379b", "M379e"]),
 ],
}
