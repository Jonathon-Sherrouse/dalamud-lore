"""Atlas content for A Realm Reborn 2.0, MSQ #25 *It's Probably Pirates* to #61 *Believe in Your Sylph* (arc tag t).

Data only (docs/atlas/era-modules.md). This is where every starting city converges: the Adventurers' Guild jobs in all
three city-states, the Scions and Minfilia (#30–31), the Drybone vanishings and Ifrit (#31–39), the remembrance services
and the twins (#40), the three Grand Company pairs (#41/42, #41b/42b, #41c/42c) and the sylphs of the Twelveswood
(#43–61). Researched 2026-11-19 from raw Console Games Wiki wikitext (lanes A07–A12); every locator quotes the saved
page's Journal, Steps or main dialogue.

Rules this module follows:
  - The Grand Company pairs are mutually exclusive picks run one after another. Each pair's records cite only its own
    pages and describe only its own company; Biggs and Wedge get one presentation per pair step, so a player of one
    company never sees another company's rescue. The company organizations themselves are described only with facts
    from #40 and their own pair, never with what "you" did.
  - Entities shared with the accepted content (Minfilia, the Scions, the Waking Sands, Thancred, Y'shtola, Urianger,
    Tataru, Yda, Papalymo, Alphinaud, Marques, Lahabrea, Noraxia …) get presentations from the step they first appear
    here; the merge closes ours where the next era's or the accepted record begins. Where the story adds nothing new
    before #102, the text repeats the accepted #102 text (Y'shtola, Urianger).
  - The accepted "-arr" relationships whose claims come from #30, #31 or #40 start earlier through ADJUST. Later
    relationships whose claims come after this era get a backfill ("-arr") that ends exactly where they begin.
  - First names only (Minfilia, Raubahn, Merlwyb, Nanamo, Vorsaile, Rolfe); the Ironworks never by its full name; Nero
    stays out of displayed text (the #59 vision names "an imperial officer").
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

S = {n: f"cp-msq-{n}" for n in list(range(25, 41)) + list(range(43, 62))}
S.update({"41": "cp-msq-41", "42": "cp-msq-42", "41b": "cp-msq-41b", "42b": "cp-msq-42b", "41c": "cp-msq-41c", "42c": "cp-msq-42c"})
S41, S42, S41B, S42B, S41C, S42C = S["41"], S["42"], S["41b"], S["42b"], S["41c"], S["42c"]

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) -----------------------------------------------
PIR, FOR, GLO, DES, COP = "It's Probably Pirates", "Call of the Forest", "Fire in the Gloom", "Call of the Desert", "Into a Copper Hell"
SCI, ROSE, UNS, POOR, BUR = "The Scions of the Seventh Dawn", "A Wild Rose by Any Other Name", "Unsolved Mystery", "What Poor People Think", "A Proper Burial"
CHI, AMA, DRE, MAT, INF, HERO = "For the Children", "Amalj'aa Wrong Places", "Dressed to Deceive", "Life, Materia and Everything", "Lord of the Inferno", "A Hero in the Making"
IF1, IF2 = "The Company You Keep (Immortal Flames)", "For Coin and Country"
MA1, MA2 = "The Company You Keep (Maelstrom)", "Till Sea Swallows All"
TA1, TA2 = "The Company You Keep (Twin Adder)", "Wood's Will Be Done"
SYL, PEACE, STUD, IMP, CONT, DANCE, FRI = "Sylph-management", "We Come in Peace", "Sylphic Studies", "First Impressions", "First Contact", "Dance Dance Diplomacy", "Forest Friend"
ENEMY, BRO, SPIR, RULES, NEVER, BREW, WINE = "Presence of the Enemy", "Brotherly Love", "Spirited Away", "Druthers House Rules", "Never Forget", "Microbrewing", "Like Fine Wine"
CONC, RICH, MAW, GIFT, BEL = "Sylphish Concerns", "Nouveau Riche", "Into the Beast's Maw", "A Simple Gift", "Believe in Your Sylph"

CLAIMS = {
 # #25 It's Probably Pirates
 "M25a": ("Baderon, proprietor of the Drowning Wench, needs a capable adventurer.", PIR, "[[Baderon]], the proprietor of [[the Drowning Wench]], has need of a capable [[adventurer]]."),
 "M25b": ("The Yellowjackets fear that men seen entering Sastasha belong to the Serpent Reavers, pirate allies of the Sahagin.", PIR, "The Yellowjackets are concerned that the unsavory-looking men seen entering Sastasha may belong to [[the Serpent Reavers]], the pirate allies of the [[Sahagin]]."),
 "M25c": ("The Serpent Reavers and their Sahagin masters are using the Sastasha caves as a base.", PIR, "it would appear the Serpent Reavers and their Sahagin masters are using the caves as a base for their nefarious operations."),
 "M25d": ("Baderon recalls that the Sahagin's pet pirates raided Limsa not long ago.", PIR, "But it weren't so long ago as the [[Sahagin|fishbacks]]' pet pirates paid us an unwelcome visit"),
 "M25e": ("Baderon passes on a job from the Adventurers' Guild in Gridania.", PIR, "It seems the Adventurers' Guild in [[Gridania]] wishes to employ the services of a seasoned adventurer."),
 "M25f": ("The Hall of the Novice is the Adventurers' Guild building north of Aleport.", PIR, "Make your way to the [[Adventurers' Guild]] building located north of Aleport"),
 # #26 Call of the Forest
 "M26a": ("Miounne, proprietress of the Carline Canopy, has a task from the Adventurers' Guild in Gridania.", FOR, "According to Baderon, the [[Adventurers' Guild]] in [[Gridania]] is recruiting people for an as-yet-undisclosed task. You can learn more by speaking with [[Miounne]], the proprietress of [[the Carline Canopy]]."),
 "M26b": ("Baderon calls Mother Miounne his counterpart in Gridania.", FOR, "Mother Miounne, me counterpart in Gridania"),
 "M26c": ("Miounne says there is a fair bit to tell about the task.", FOR, "With regard to the task in question, there is a fair bit to tell."),
 # #27 Fire in the Gloom
 "M27a": ("A cult called the Lambs of Dalamud has been active in the Tam-Tara Deepcroft.", GLO, "It would seem that a cult known as [[the Lambs of Dalamud]] has been engaging in suspicious activity in [[The Tam-Tara Deepcroft|the Tam–Tara Deepcroft]]."),
 "M27b": ("The cult blames Eorzeans for the destruction of Dalamud, its god, and seeks to avenge it.", GLO, "Since [[Dalamud]]'s apparent destruction─for which they blame the people of [[Eorzea]]─it seems they have been seeking a means to avenge their god."),
 "M27c": ("A vengeful spirit woken in Galvanth's corpse attacks you; you send it back to the abyss and foil the cult's plot.", GLO, "you are assailed by a vengeful spirit who had been awakened in the corse of [[Galvanth the Dominator]]. After a titanic struggle, you succeed in sending this dark being back to the abyss, thus foiling the cultists' plot."),
 "M27d": ("Miounne says adventurers are dying more often as unprepared people take on tasks beyond them.", GLO, "Miounne reveals that death is becoming an ever more common occurrence within the adventuring fraternity. She attributes this unfortunate trend to the burgeoning demand for [[adventurer]]s' services, which has allowed unprepared individuals to take on tasks which are beyond them."),
 "M27e": ("Miounne passes you on to the Adventurers' Guild in Ul'dah.", GLO, "Miounne informs you that the [[Adventurers' Guild]] in [[Ul'dah]] is recruiting."),
 "M27f": ("Lewin says the Lambs of Dalamud are a doomsday cult that arose before the Calamity.", GLO, "the Lambs of Dalamud, a doomsday cult which sprung up prior to the Calamity."),
 # #28 Call of the Desert
 "M28a": ("Momodi, proprietress of the Quicksand, has a task from the Adventurers' Guild in Ul'dah.", DES, "the [[Adventurers' Guild]] in [[Ul'dah]] is recruiting people for an as-yet-undisclosed task. You can learn more by speaking to [[Momodi]], the proprietress of [[the Quicksand]]."),
 "M28b": ("Miounne calls Momodi the sultanate's version of herself.", DES, "Think of her as the sultanate's version of myself."),
 "M28c": ("Miounne called you the adventurer of the moment.", DES, "She also made a point of callin' you the adventurer of the moment."),
 "M28d": ("Miounne expects Momodi's task to be dangerous.", DES, "Chances are she'll send you into the midst of danger"),
 # #29 Into a Copper Hell
 "M29a": ("Giants, hecatoncheires, have been wreaking havoc in Copperbell Mines.", COP, "It would seem that a horde of [[hecatoncheir]]es has been wreaking havoc in the depths of [[Copperbell Mines]]."),
 "M29b": ("The mines were reopened to meet the demand for building materials after the Calamity, which Ul'dah's recovery needs.", COP, "Copperbell Mines were reopened in order to meet the pressing demand for building materials created in the wake of [[the Calamity]]. Without a steady supply, [[Ul'dah]]'s nascent recovery may slow to a standstill."),
 "M29c": ("Miners of old collapsed the lowest levels of the mines to contain the hecatoncheires.", COP, "In a desperate bid to contain the unbridled fury of the hecatoncheires, our ancestors induced the collapse of the mines' lowermost levels."),
 "M29d": ("You subdue the hecatoncheires.", COP, "You have succeeded in subduing the hecatoncheires."),
 "M29e": ("Mining can resume, and Ul'dah will have materials to rebuild.", COP, "Thanks to you, our minin' operations can resume, and Ul'dah will have the materials she needs to rebuild."),
 "M29f": ("Momodi warns that the Scions are no ordinary folk and do no ordinary work.", COP, "the Scions ain't no ordinary folk, and the work they do ain't no ordinary work."),
 # #30 The Scions of the Seventh Dawn
 "M30a": ("Momodi says the Scions seek capable people for their cause, and your exploits have drawn their attention.", SCI, "Given the multitude of problems facing the realm, they are always looking for capable individuals to join their cause, and it appears your recent exploits have drawn their attention."),
 "M30b": ("Minfilia believes your Echo is the key to the primal problem facing Eorzea.", SCI, "who expresses her belief that your power─[[the Echo]]─is the key to solving the [[primal]] problem facing Eorzea."),
 "M30c": ("The Echo lets one pass through the walls of a soul and hear its past.", SCI, "The Echo allows you to pass through the walls of a man's soul, and hear the resonations of his past."),
 "M30d": ("Minfilia calls the primals a bane upon Eorzea and the world.", SCI, "Their existence is a bane upon Eorzea─nay, the world at large, and we have striven to find a lasting solution to the threat they pose."),
 "M30e": ("Minfilia asks you to lend your strength to the Scions and gives you the order's password.", SCI, "she implores you to lend your strength to the Scions' cause, and entrusts you with the order's password"),
 "M30f": ("Tataru welcomes you to the Waking Sands, the Scions' headquarters.", SCI, "Ahem! I bid you welcome to the Waking Sands, headquarters of the Scions of the Seventh Dawn!"),
 "M30g": ("Tataru looks forward to assisting you.", SCI, "My name is Tataru, and I look forward to assisting you during your time with us."),
 # #31 A Wild Rose by Any Other Name
 "M31a": ("Minfilia accepts your pledge and welcomes you to the Scions.", ROSE, "Minfilia accepts your whimsical utterance in the spirit it was intended, and welcomes you to the Scions."),
 "M31b": ("Your first task is to investigate crimes in Ul'dah that the Scions suspect involve a primal.", ROSE, "you are assigned your first task─to investigate a series of crimes committed in [[Ul'dah]], which the Scions suspect to be [[primal]]-related."),
 "M31c": ("A crystal caravan of Amajina & Sons was robbed of its cargo.", ROSE, "Some days ago, a crystal caravan registered to Amajina & Sons Mineral Concern was waylaid and divested of its cargo."),
 "M31d": ("The evidence implicates the Amalj'aa, known worshipers of Ifrit.", ROSE, "the evidence left behind implicates the Amalj'aa, who are known worshipers of Ifrit."),
 "M31e": ("Thancred believes the robbery and the disappearances are connected.", ROSE, "Thancred believes that the caravan robbery and the recent spate of disappearances are connected."),
 "M31f": ("Isembard is the de facto leader of Camp Drybone.", ROSE, "A fellow by the name of Isembard serves as the camp's de facto leader."),
 "M31g": ("Yda and Papalymo survey the Twelveswood for the Scions.", ROSE, "The masked woman is Yda, and beside her is Papalymo. The two are charged with surveying the Twelveswood."),
 "M31h": ("Y'shtola says the Scions' leader was taken at the Battle of Carteneau, but they kept their purpose.", ROSE, "At the Battle of Carteneau, our leader was taken from us. But we did not stray from our purpose."),
 "M31j": ("Isembard offers you his full cooperation.", ROSE, "Arriving at Camp Drybone, you speak with Isembard, who offers you his full cooperation in the investigation."),
 # #32 Unsolved Mystery
 "M32a": ("The Amalj'aa have butchered commonfolk, whose bodies Isembard wants buried.", UNS, "Isembard informs you that the [[Amalj'aa]] have butchered a number of commonfolk, and asks that you retrieve the [[Ripe Corpse|ripe corpses]] so that he may see them properly interred."),
 "M32b": ("Callers at the Church of Saint Adama Landama were murdered.", UNS, "There have been brutal murders of callers at the Church of Saint Adama Landama"),
 "M32c": ("The Amalj'aa cannot be acting alone; Isembard suspects another conspirator.", UNS, "it is impossible that the Amalj'aa have been acting alone in the recent wave of disappearances. Isembard cannot help but wonder if another conspirator has had a hand in these troubling incidents."),
 # #33 What Poor People Think
 "M33a": ("Ungust is a merchant born in Drybone and raised in the Golden Bazaar.", POOR, "There is a merchant by the name of Ungust who was born here in Drybone and grew up in the Golden Bazaar."),
 "M33b": ("Ungust recognizes you as the adventurer who threatened him in Ul'dah.", POOR, "You're that bloody adventurer who threatened me back in Ul'dah!"),
 "M33c": ("Ungust seems unconcerned about the growing number of missing people.", POOR, "Ungust seems unconcerned about the growing list of missing people around [[Camp Drybone|Drybone]]."),
 "M33d": ("The frightened commonfolk tell you little.", POOR, "In their terror, the commonfolk tell you little of use."),
 "M33e": ("Isembard thinks the people hold their tongues because they trust only their gods.", POOR, "Isembard believes that perhaps the people are holding their tongues because they have come to trust only in their gods."),
 # #34 A Proper Burial
 "M34a": ("Marques tends the graves of the church's lichyard.", BUR, "Seek out a man named Marques─he tends the graves of the lichyard."),
 "M34b": ("Marques knows little of the commonfolk and sends you to Sister Ourcen.", BUR, "Marques admits to knowing little of the commonfolk. He suggests you speak to Sister [[Ourcen]] within the church."),
 "M34c": ("Ourcen is the medium through whom the commonfolk speak to Thal.", BUR, "When they wish to speak to their keeper, Thal, I am the medium through which they do."),
 "M34d": ("Ourcen has heard nothing that helps the investigation.", BUR, "she has not heard anything that might help your investigation"),
 "M34e": ("Thancred suspects Ourcen, who takes the commonfolk's confession; Isembard is not convinced.", BUR, "he suspects that the only person who could take the vigilant commonfolk by surprise is the very Sister Ourcen who takes their confession. Isembard, however, is not so easily convinced."),
 "M34f": ("Thancred swears he has seen the lichkeeper Marques's face before.", BUR, "Still, the lichkeeper Marques... I'd swear to the Twelve I've seen that face elsewhere before..."),
 "M34g": ("Thancred has joined the search for the missing.", BUR, "The name is Thancred, and I share a passion with you and our mutual friend here for learning what has become of these missing persons and why."),
 # #35 For the Children
 "M35a": ("Isembard refuses to believe Ourcen is behind the disappearances.", CHI, "Isembard refuses to believe that Sister Ourcen is behind the mysterious disappearances"),
 "M35b": ("You rescue Ourcen from undead soldiers.", CHI, "You have rescued Ourcen from a grisly fate at the hands of undead soldiers."),
 "M35c": ("Ourcen went out to recover an orphan's ring, a gift from his late mother.", CHI, "It is a ring given him by his mother before she passed."),
 "M35d": ("Isembard is more convinced than ever that Ourcen is innocent.", CHI, "Isembard is more convinced than ever that Sister Ourcen is not in any way responsible for the vanishings."),
 # #36 Amalj'aa Wrong Places
 "M36a": ("Thancred asks you to search an Amalj'aa encampment for evidence of the vanishings.", AMA, "He asks that you enter and search for evidence of their involvement in the vanishings at Camp Drybone."),
 "M36b": ("The leaflet you find offers the poor work.", AMA, "It looks to be some sort of assembly to provide the poor with work."),
 "M36c": ("Ourcen confirms the leaflet is not of the Order's making, and garments have gone missing from the church.", AMA, "Sister Ourcen confirms that the leaflet is not of the Order's making, and goes on to tell you that the church was recently plagued by a rash of missing garments."),
 "M36d": ("Thancred thinks the culprit is posing as a priest of the Order.", AMA, "Thancred believes it likely that the culprit behind the vanishings is posing as a priest of the Order."),
 "M36e": ("Thancred withdraws to consider his next move.", AMA, "Thancred, meanwhile, has withdrawn to consider the situation more carefully."),
 # #37 Dressed to Deceive
 "M37a": ("You and Thancred pose as impoverished souls to catch the false priest.", DRE, "[[Thancred]] suggests that the two of you pose as impoverished souls in order to ensnare the false priest."),
 "M37b": ("The poor have a commune by a pond north of Sandgate.", DRE, "the poor have established a commune by a pond north of [[Sandgate]], to the east of Camp Drybone."),
 "M37c": ("The false priest is Ungust, whom you first found preying on a refugee woman in Ul'dah.", DRE, "The false priest turns out to be none other than [[Ungust]], the obnoxious merchant whom you first found preying upon a refugee woman in [[Ul'dah]]."),
 "M37d": ("Ungust has been abducting people at the behest of the Amalj'aa.", DRE, "The man reveals that he has been abducting people at the behest of the [[Amalj'aa]]."),
 "M37e": ("The Amalj'aa first wanted the schedule of crystal shipments from the Nanawa Mines.", DRE, "First of all, they wanted the schedule for crystal shipments from the Nanawa Mines."),
 "M37f": ("Ungust posed as a priest to lure the vulnerable to the Amalj'aa.", DRE, "So, I posed as a priest to lure in the vulnerable and give them over to the Amalj'aa."),
 "M37g": ("Only the Amalj'aa know where the abducted were taken.", DRE, "we must ascertain where the abducted were taken...and none but the Amalj'aa know the answer."),
 "M37h": ("Minfilia says an encounter with the Amalj'aa is inevitable.", DRE, "Minfilia tells you that an encounter with the Amalj'aa is inevitable."),
 "M37i": ("Thancred asks whether Ungust also leaked the Immortal Flames' patrol routes.", DRE, "Were you the one leaking the Immortal Flames' patrol routes to the enemy as well?"),
 # #38 Life, Materia and Everything
 "M38a": ("Minfilia seeks a peaceful solution to the primal problem, but wants the Scions ready to fight.", MAT, "Though we seek a peaceful solution to the primal problem, we must needs be ready to fight for our cause."),
 "M38b": ("Minfilia sends you to a goblin scholar who brought a new method of enhancing gear to Eorzea.", MAT, "Minfilia would like you to meet a goblin scholar named Mutamix, who she claims is responsible for introducing a revolutionary method of enhancing gear to Eorzea."),
 "M38c": ("Materia is a crystal melded to items to enhance them.", MAT, "materia, a type of crystal which can be melded to items to enhance their properties."),
 # #39 Lord of the Inferno
 "M39a": ("The Immortal Flames plan to capture Amalj'aa with Ungust as bait, and you go as the Scions' representative.", INF, "the Immortal Flames have devised a plan to capture [[Amalj'aa]], using the false priest [[Ungust]] as bait. Minfilia bids you take part in the operation as [[The Scions of the Seventh Dawn|the Scions]]' representative."),
 "M39b": ("A traitor in the ranks gives you away, and you are captured with the Flames.", INF, "you learn that there is a traitor in the ranks, and are swiftly subdued. After an indeterminate amount of time, you awake to find yourself imprisoned within an Amalj'aa stronghold, along with the Flames."),
 "M39c": ("The Amalj'aa mean to offer you and your companions to their primal, Ifrit.", INF, "It appears the Amalj'aa mean to make an offering of you and your companions to their [[primal]], [[Ifrit]]."),
 "M39d": ("Ifrit can bind mortals to his will, but you are immune; he tries to kill you and is outmatched.", INF, "It would appear that Ifrit has the power to bind mortals to his will, but for reasons yet unknown you are immune to his influence. Having failed to make you his minion, Ifrit elects to exterminate you instead, only to find himself outmatched."),
 "M39e": ("The crystal robbery and the abductions served to advance Ifrit's cause.", INF, "explaining to you how the crystal robbery and the abductions served to advance Ifrit's cause."),
 "M39f": ("To keep the primal from gaining strength, his tempered victims must be put to death.", INF, "in order to prevent the primal from gaining strength, his “tempered” victims must be put to death."),
 "M39g": ("Those with the Echo are immune to primal influence.", INF, "We know not the why of it, but those blessed with the Echo are immune to primal influence."),
 # #40 A Hero in the Making
 "M40a": ("All three Grand Companies of Eorzea want you in their ranks.", HERO, "It would seem your recent exploits have garnered the attention of all three of the Grand Companies of Eorzea."),
 "M40b": ("Each company would have Ifrit's bane for its own, and each has sent an officer to court you.", HERO, "Each organization would have Ifrit's bane for its own. To this end, all three have sent officers to ''court'' you."),
 "M40c": ("The three Grand Companies are the Maelstrom of Limsa Lominsa, the Order of the Twin Adder of Gridania and the Immortal Flames of Ul'dah.", HERO, "There are presently three such organizations in Eorzea: the Maelstrom of Limsa Lominsa, the Order of the Twin Adder of Gridania, and the Immortal Flames of Ul'dah."),
 "M40d": ("The Grand Companies protect their own nations, while the Scions seek to preserve all Eorzea's future.", HERO, "The Grand Companies seek to protect their own nations. We Scions, on the other hand, seek to preserve the future of Eorzea as a whole."),
 "M40e": ("Kan-E-Senna is supreme commander of the Order of the Twin Adder.", HERO, "As supreme commander of the Order of the Twin Adder, ever shall I bear the weight of our people's sacrifice."),
 "M40f": ("Kan-E-Senna says the Ixal have returned in force.", HERO, "To compound our woes, the Ixal have returned in force, emboldened by our suffering."),
 "M40g": ("Kan-E-Senna says the Empire is raising steel fortresses in the Twelveswood and remains the greatest threat.", HERO, "the Empire has set about raising steel fortresses here in the Twelveswood. … Let none be mistaken─the Garleans remain the greatest threat to our survival."),
 "M40h": ("Alphinaud says the warlike Ixal summon their primal, Garuda.", HERO, "The Ixal are unquestionably the more troublesome, being of a naturally warlike disposition, and wont to summon their bloodthirsty primal, Garuda."),
 "M40i": ("Flame General Raubahn addresses Ul'dah at its remembrance service.", HERO, "Next, you'll need to go to Ul'dah, where Flame General Raubahn Aldynn will be addressing the masses at the Royal Promenade."),
 "M40j": ("Raubahn warns that the Amalj'aa strangle Ul'dah's trade and the Garleans mock its borders.", HERO, "The savage hordes of the Amalj'aa wait beside our roads, strangling the lifelines of trade. … Meanwhile, the Garleans make mock of our borders, and despoil our land of its natural wealth."),
 "M40k": ("Raubahn warns that a divided Ul'dah stands to fall.", HERO, "all must recognize that a divided Ul'dah stands to fall."),
 "M40l": ("Nanamo, seventeenth in the line of Ul, says Ul'dah's true wealth lies in its people's health, happiness and hopes.", HERO, "People of Ul'dah! I, Nanamo, seventeenth in the line of Ul, address you. … For the true wealth of Ul'dah lies in the health, happiness, and hopes of her people."),
 "M40m": ("The Amalj'aa summon Ifrit more and more often.", HERO, "It has been observed that the Amalj'aa are summoning him with ever-increasing frequency."),
 "M40n": ("The Maelstrom was reborn under its standard when the Garlean Empire marched on Eorzea.", HERO, "When the Garlean Empire marched upon Eorzea, we assembled beneath the Maelstrom's standard, and our Grand Company was reborn."),
 "M40o": ("Merlwyb warns of the Sahagin, the kobolds and the Garleans, whose flags fly within Limsa's borders.", HERO, "The Sahagin creep ashore seeking blood for their accursed god. … Even now, the curs fly their flags within our borders."),
 "M40p": ("Merlwyb calls for mending the rift between pirate and Maelstrom.", HERO, "How can we hope to repel our many enemies when mutiny breeds below deck? … We must mend the rift the Calamity has reopened 'twixt pirate and Maelstrom"),
 "M40q": ("Alphinaud believes the task of healing Eorzea falls to the Scions, helped by the Grand Companies.", HERO, "So the task of salving Eorzea's wounds falls to the Scions of the Seventh Dawn—with a little help from our friends the Grand Companies."),
 "M40r": ("Alisaie calls the remembrance services little more than standard-waving rallies.", HERO, "The so-called “remembrance” ceremonies were little more than standard-waving rallies."),
 "M40s": ("Alphinaud says the twins' paths may differ, but their destination is the same.", HERO, "Our paths may differ, but our destination is the same."),
 "M40t": ("You must choose and give your answer to the officer of the company you would join.", HERO, "Weigh your decision well, and give your answer to the officer of the Grand Company you would join."),
 "M40u": ("Kan-E-Senna, the Elder Seedseer, speaks at Mih Khetto's Amphitheatre.", HERO, "Elder Seedseer Kan-E-Senna will deliver her address at Mih Khetto's Amphitheatre."),
 "M40v": ("A sentry says the Admiral is about to give her address.", HERO, "the Admiral is due to give her address at any moment."),
 "M40w": ("Merlwyb is Chief Admiral of the Maelstrom.", HERO, "where Maelstrom Chief Admiral Merlwyb Bloefhiswyn will be giving her address."),
 "M40x": ("The Garlean Empire brought a war of conquest to Eorzea, and the Alliance met it at Carteneau five years ago.", HERO, "When the Garlean Empire brought its war of conquest to Eorzea … Five years ago, the Alliance met the armies of the Empire upon the fields of Carteneau."),
 "M40y": ("The sylphs grew aloof at about the time they summoned the primal Ramuh.", HERO, "Alas, they have grown aloof, a change observed at roughly the time they summoned the primal Ramuh."),
 "M40z": ("Each victory over Ifrit costs Ul'dah blood, a war of attrition it cannot sustain.", HERO, "Every time they do so, the Ul'dahns send their forces to smite the primal, and though they invariably succeed, each victory is bought with blood."),
 # #41 / #42: the Immortal Flames
 "M41a": ("You confirm that you will join the Immortal Flames.", IF1, "You have confirmed your intention to join the ranks of the Immortal Flames."),
 "M41b": ("Your induction is interrupted by an imperial attack on an airship near Horizon's Edge.", IF1, "Your formal induction into the Immortal Flames is interrupted by an urgent report concerning an imperial attack on a Highwind Skyways airship. Head to Horizon's Edge"),
 "M41c": ("The crew, Biggs and Wedge, are Ironworks engineers, and the Ironworks' master has been missing since the Calamity.", IF1, "You learn that the vessel's crew, Biggs and Wedge, are engineers from Garlond Ironworks, and that Master Garlond himself has been missing since the Calamity."),
 "M41d": ("You defeat the imperial soldiers trying to requisition the downed airship.", IF1, "You have defeated the imperial soldiers intent on requisitioning the downed airship."),
 "M41e": ("It is the first airship the Ironworks has built since the Calamity.", IF1, "It's the first airship we've built since the Calamity"),
 "M41f": ("The Flames are in the midst of a large operation against the Amalj'aa.", IF1, "We're in the midst of a large-scale operation against the Amalj'aa, and we have no one to spare in western Thanalan."),
 "M41g": ("The two engineers are able to continue on their way.", IF1, "reassures you that the two engineers you encountered were able to continue on their way."),
 "M42a": ("You are sworn into the Immortal Flames, Ul'dah's Grand Company.", IF2, "You have been sworn into the service of Ul'dah's Grand Company, the Immortal Flames."),
 "M42b": ("Flame recruits must forsake all other nations.", IF2, "To join our ranks, you must forsake all other nations."),
 "M42c": ("The Flames would lay down their lives at a word from Raubahn to keep Ul'dah at peace.", IF2, "And at a word from Flame General Raubahn Aldynn, we would gladly lay down our lives to maintain the peace and prosperity of Ul'dah."),
 "M42d": ("Biggs and Wedge are now under the protection of the Scions.", IF2, "Minfilia announces that Biggs and Wedge, the Garlond Ironworks engineers, are now under the protection of the Scions of the Seventh Dawn."),
 "M42e": ("As a neutral party, the Scions keep airship technology, and the Ironworks sent two engineers to help.", IF2, "As a neutral party, it was judged that we Scions should serve as the keepers of this technology. … we requested the assistance of Garlond Ironworks, who very kindly sent us two of their finest engineers."),
 # #41b / #42b: the Maelstrom
 "M41ba": ("You confirm that you will join the Maelstrom.", MA1, "You have confirmed your intention to join the ranks of the Maelstrom."),
 "M41bb": ("Your induction is interrupted by an imperial attack on an airship in Cedarwood.", MA1, "Your formal induction into the Maelstrom is interrupted by an urgent report concerning an imperial attack on a Highwind Skyways airship. Head to Cedarwood"),
 "M41bc": ("The crew, Biggs and Wedge, are Ironworks engineers, and the Ironworks' master has been missing since the Calamity.", MA1, "You learn that the vessel's crew, Biggs and Wedge, are engineers from Garlond Ironworks, and that Master Garlond himself has been missing since the Calamity."),
 "M41bd": ("You defeat the imperial soldiers trying to requisition the downed airship.", MA1, "You have defeated the imperial soldiers intent on requisitioning the downed airship."),
 "M41be": ("It is the first airship the Ironworks has built since the Calamity.", MA1, "It's the first airship we've built since the Calamity"),
 "M41bf": ("The two engineers make it home without further incident.", MA1, "assures you that the two engineers you encountered made it home without further incident."),
 "M42ba": ("You are sworn into the Maelstrom, Limsa Lominsa's Grand Company.", MA2, "You have been sworn into the service of Limsa Lominsa's Grand Company, the Maelstrom."),
 "M42bb": ("The Maelstrom is charged with meeting the threats of the primals and the Empire, and with the Calamity's many problems.", MA2, "We of the Maelstrom are charged with meeting the threats posed by the primals and the Garlean Empire, and solving the many problems caused by the Calamity."),
 "M42bc": ("Biggs and Wedge are now under the protection of the Scions.", MA2, "Minfilia announces that Biggs and Wedge, the Garlond Ironworks engineers, are now under the protection of the Scions of the Seventh Dawn."),
 "M42bd": ("As a neutral party, the Scions keep airship technology, and the Ironworks sent two engineers to help.", MA2, "As a neutral party, it was judged that we Scions should serve as the keepers of this technology. … we requested the assistance of Garlond Ironworks, who very kindly sent us two of their finest engineers."),
 "M42be": ("You are a storm private third class, a soldier of the Maelstrom.", MA2, "I hereby assign you the rank of storm private third class. You are now officially a soldier of the Maelstrom."),
 # #41c / #42c: the Order of the Twin Adder
 "M41ca": ("You confirm that you will join the Order of the Twin Adder.", TA1, "You have confirmed your intention to join the ranks of the Order of the Twin Adder."),
 "M41cb": ("Your induction is interrupted by an imperial attack on an airship southeast of Nine Ivies.", TA1, "Your formal induction into the Order of the Twin Adder is interrupted by an urgent report concerning an imperial attack on a Highwind Skyways airship. Head to the area southeast of Nine Ivies"),
 "M41cc": ("The crew, Biggs and Wedge, are Ironworks engineers, and the Ironworks' master has been missing since the Calamity.", TA1, "You learn that the vessel's crew, Biggs and Wedge, are engineers from Garlond Ironworks, and that Master Garlond himself has been missing since the Calamity."),
 "M41cd": ("You defeat the imperial soldiers trying to requisition the downed airship.", TA1, "You have defeated the imperial soldiers intent on requisitioning the downed airship."),
 "M41ce": ("It is the first airship the Ironworks has built since the Calamity.", TA1, "It's the first airship we've built since the Calamity"),
 "M41cf": ("The two engineers are able to continue on their way.", TA1, "reassures you that the two engineers you encountered were able to continue on their way."),
 "M42ca": ("You are sworn into the Order of the Twin Adder, Gridania's Grand Company.", TA2, "You have been sworn into the service of Gridania's Grand Company, the Order of the Twin Adder."),
 "M42cb": ("The Order was formed before the Calamity to fight the Garlean Empire and the beast tribes and their primals.", TA2, "Our order was formed in the days before the Calamity, in readiness to fight the Garlean Empire, and to combat the beast tribes and their primals."),
 "M42cc": ("Kan-E-Senna is the supreme commander of the Order's forces.", TA2, "Elder Seedseer Kan-E-Senna is the supreme commander of our forces."),
 "M42cd": ("Biggs and Wedge are now under the protection of the Scions.", TA2, "Minfilia announces that Biggs and Wedge, the Garlond Ironworks engineers, are now under the protection of the Scions of the Seventh Dawn."),
 "M42ce": ("As a neutral party, the Scions keep airship technology, and the Ironworks sent two engineers to help.", TA2, "As a neutral party, it was judged that we Scions should serve as the keepers of this technology. … we requested the assistance of Garlond Ironworks, who very kindly sent us two of their finest engineers."),
 "M42cf": ("The Order draws together Gridania's martial, economic and technological resources.", TA2, "It brings together the martial, economic, and technological resources of our nation"),
 # #43 Sylph-management
 "M43a": ("Minfilia asks you to learn the sylphs' intentions with the Echo, reporting first to Commander Vorsaile at the Adders' Nest.", SYL, "Minfilia would have you ascertain the [[Sylph Daily Quests|sylph tribe]]'s intentions, aided by the power of [[the Echo]]. Before making contact with the diminutive [[beastmen]], report to Commander [[Vorsaile Heuloix]] at [[the Adders' Nest]] in [[Gridania]]."),
 "M43b": ("The Scions studied the sylphs, a beast tribe of the Twelveswood, for the Order of the Twin Adder.", SYL, "We have conducted a study at the behest of the Order of the Twin Adder. … Our task was to survey the behavior of the sylphs, a beast tribe indigenous to the Twelveswood."),
 "M43c": ("Yda says the sylphs worship the primal Ramuh.", SYL, "That worship the primal Ramuh."),
 "M43d": ("The sylphs seem no longer to summon Ramuh, but the threat should not be assumed past.", SYL, "While Ramuh's existence is well documented, the sylphs do not─or perhaps, can not─summon the primal any longer, insofar as can be ascertained. … It would be unwise to assume that the threat posed by the primal has passed."),
 "M43e": ("Gridania has its hands full fending off Garuda, among the most savage of primals.", SYL, "What we ''can'' say with absolute certainty is that Gridania has its hands full fending off Garuda. … Who, I need hardly remind you, is among the most savage and terrible of all known primals."),
 "M43f": ("Winning the sylphs' favor may bring the Scions closer to mitigating the primal threat.", SYL, "Winning the sylphs' favor may well bring us a step closer to mitigating the threat of the primals."),
 "M43g": ("Vorsaile admits Gridania knows far too little of the sylphs to plan.", SYL, "We know far too little of the sylphs to lay any worthwhile plans."),
 "M43h": ("Yda and Papalymo will help you with the sylphs.", SYL, "Yda and Papalymo, however, should be able to see the forest for the trees."),
 # #44 We Come in Peace
 "M44a": ("Vorsaile wants an impartial liaison to hear the sylphs themselves.", PEACE, "I would hear from the other side─the sylphs themselves─and seek an impartial party to serve as my liaison."),
 "M44b": ("Gridania cannot decide whether to strike at Ramuh or leave the sylphs alone.", PEACE, "Do we strike at Ramuh, or leave the sylphs to their own ways? That is the question"),
 "M44c": ("The sylphs are mostly peaceable, and the Elder Seedseer wants no new war.", PEACE, "The sylphs are, for the most part, a peaceable bunch─much to the delight of the Elder Seedseer, who has no desire to see her people embroiled in yet another fruitless war."),
 "M44d": ("The sylphs' ties to Ramuh have raised a warning in the Twin Adder's ranks.", PEACE, "the sylphs' relation to the primal Ramuh has raised a flag of warning amongst our ranks."),
 "M44f": ("The sylphs have been wary since the Empire came to the Shroud.", PEACE, "Particularly since the Empire has come to the Shroud."),
 # #45–#46
 "M45a": ("Rolfe, patriarch of a beekeeping family, is said to know sylphic customs.", STUD, "[[Rolfe Hawthorne]], patriarch of the beekeeping Hawthorne family, is said to be well versed in sylphic customs."),
 "M45b": ("Rolfe's memory is failing, but he has shared his stories with those around the hut.", STUD, "Rolfe's memory is not what it used to be, but it turns out that he has previously shared his stories with those around the hut."),
 "M45c": ("Rolfe recalls that dancing is the sylphs' traditional greeting.", STUD, "he recalls that dancing is the traditional greeting among the sylphs."),
 "M46a": ("Sylphs dislike guests who arrive empty-handed.", IMP, "They don't take kindly to guests who show up empty-handed."),
 "M46b": ("Rosa says the sylphs are fond of milkroot, which comes from ochus.", IMP, "Rosa informs you that the sylphs are said to be quite fond of [[milkroot]], which can be obtained from [[Ochu (Enemy)|ochu]]s."),
 "M46c": ("Rolfe says a gift of milkroot will make the sylphs call you friend.", IMP, "a gift of milkroot will have the sylphs calling you friend"),
 # #47 First Contact
 "M47a": ("Amelain gives you a letter from the Elder Seedseer for Komuxio of Little Solace.", CONT, "Amelain has entrusted you with [[Letter to the Elder (First Contact)|a missive]] penned by [[Kan-E-Senna|the Elder Seedseer]] herself. Deliver it safely to [[Komuxio]] at [[Little Solace]]."),
 "M47b": ("The letter vouches for the envoy and restates Gridania's wish for harmony with the sylphs.", CONT, "it vouches for the integrity of our envoy─that would be you─and restates Gridania's desire to maintain a harmonious relationship with our long-standing friends of the forest."),
 "M47c": ("The war with the Ixal has taken a toll on Gridania's resources.", CONT, "The war with the Ixal has taken a toll on our resources; we can ill afford to get mired in another conflict."),
 "M47d": ("Komuxio accepts your gifts but remains unconvinced, and you are denied an audience with the elder of Little Solace.", CONT, "Despite accepting your gifts, Komuxio remains unconvinced as to your intentions. Is there no way to gain the [[sylph]]'s trust and secure an audience with the elder of Little Solace?"),
 "M47e": ("Komuxio says the elder has no words for Gridania.", CONT, "Elder one has no words for Gridania. Walking ones waste every one's time."),
 "M47f": ("Papalymo thinks recent events have left the sylphs uncommonly wary.", CONT, "something tells me recent events have our erstwhile fluttery friends feeling uncommonly wary."),
 # #48–#49
 "M48a": ("Yda thinks dancing for the sylphs of Little Solace is the best way to earn their trust.", DANCE, "Yda believes that the best way to earn the sylphs' trust is to [[Dance|/dance]] for those who reside in [[Little Solace]]."),
 "M48b": ("Your dancing won smiles, but whether it won the sylphs' hearts remains to be seen.", DANCE, "Your dancing has won many a smile, but have you truly succeeded in winning the hearts of the sylphs of Little Solace? This remains to be seen."),
 "M48c": ("Yda says the dancing brought smiles and high spirits to Little Solace.", DANCE, "your lovely dancing has brought smiles and high spirits to all of Little Solace!"),
 "M49a": ("The sylphs of Little Solace were driven from their woodland home.", FRI, "The sylphs who make their home in Little Solace do so having been driven from their woodland home."),
 "M49b": ("Little Solace is a temporary settlement without defenses.", FRI, "Being a temporary settlement, Little Solace wants for amenities, not least a stout set of defenses."),
 "M49c": ("The sylphs have begun to warm to you, gradually.", FRI, "It would seem the sylphs have begun to warm to your presence, albeit gradually."),
 "M49d": ("Komuxio thinks he may have been wrong not to trust you.", FRI, "Perhaps this one was wrong not to trust dancing one, after all."),
 # #50 Presence of the Enemy
 "M50a": ("Komuxio is troubled by strangers seen in the forest.", ENEMY, "Komuxio is troubled by sightings of unfamiliar walking ones in the forest."),
 "M50b": ("Imperial soldiers guarding boxes attack you, and the boxes hold a log of imperial supplies for delivery.", ENEMY, "Stumbling upon a stack of suspicious boxes, you are attacked by a group of imperial soldiers. After fending them off, you search the boxes to uncover a [[Quartermaster's Log|quartermaster's log]] detailing a list of imperial supplies for delivery."),
 "M50c": ("Komuxio deduces the log was written by someone who knows the forest: perhaps a traitor.", ENEMY, "Komuxio deduces that the log must have been penned by someone with knowledge of the forest. Could there be a traitor in your midst?"),
 "M50d": ("Komuxio makes you promise always to be a friend to the sylphs.", ENEMY, "Dancing one must promise to always be friend to these ones."),
 # #51 Brotherly Love
 "M51a": ("Komuxio fears for his friend Claxio, who wandered off alone.", BRO, "Komuxio fears for the safety of his friend [[Claxio]], who has wandered off unaccompanied."),
 "M51b": ("The sylphs in the forest have been tempered by the primal Ramuh.", BRO, "These sylphs have been tempered―brought under the thrall of the primal Ramuh."),
 "M51c": ("Like the Amalj'aa tempered by Ifrit, tempered sylphs exist only to serve their primal.", BRO, "Akin to the Amalj'aa tempered by Ifrit, these sylphs exist only to serve their deity."),
 "M51d": ("You save Claxio from tempered sylphs, and he returns to Little Solace.", BRO, "You find Claxio just in time to prevent tempered sylphs from spiriting him away. Following an emotional reunion with Komuxio, Claxio agrees to return to Little Solace."),
 "M51e": ("Claxio feared the sylphs of Little Solace were forgetting who they are.", BRO, "This one feared that these ones were forgetting who these ones are"),
 "M51f": ("You have earned Komuxio's unreserved trust; whether the sylph elder will accept you is uncertain.", BRO, "Your efforts on his friend's behalf have earned you Komuxio's unreserved trust. Will the sylph elder be as accepting?"),
 # #52 Spirited Away
 "M52a": ("Komuxio confesses that his elder is missing and asks you to seek the Twin Adder's help from Commander Vorsaile.", SPIR, "Komuxio confesses to you that his elder has gone missing, and beseeches you to seek the aid of [[the Order of the Twin Adder]]. Make for [[the Adders' Nest]] and inquire with Commander [[Vorsaile Heuloix]]"),
 "M52b": ("The elder went into the forest and has not come back.", SPIR, "Elder one went into forest yesterday, but has not come back..."),
 "M52c": ("Vorsaile fears a crisis if the elder ends up with the tempered sylphs.", SPIR, "Why, if he were to end up in the hands of the tempered ones, we'd have a crisis on our hands."),
 "M52d": ("Vorsaile agrees to help search for the sylph elder, with his Serpents watching night and day.", SPIR, "Commander Vorsaile Heuloix consents to assist in the search for the sylph elder. … You can assure the sylphs that my sharpest-eyed Serpents will be on the lookout night and day."),
 "M52e": ("The Wood Wailers pledge their cooperation in the search.", SPIR, "Giah Molkoh has pledged [[the Wood Wailers]]' cooperation in the search effort."),
 "M52f": ("Buscarron agrees to listen among his many customers for news of the elder.", SPIR, "You speak with [[Buscarron]], who agrees to keep an ear out amongst his many customers for any news of the sylph elder's whereabouts."),
 "M52g": ("Buscarron's home is near where the elder disappeared.", SPIR, "Near where elder one disappeared is the home of a walking one named Buscarron."),
 "M52h": ("Buscarron's Druthers is in the South Shroud.", SPIR, "Take yourself to [[Buscarron's Druthers]] in the [[South Shroud]] and speak with the proprietor."),
 # #53–#56 Buscarron and Teteroon
 "M53a": ("Buscarron has no word of the sylph elder yet.", RULES, "No word on the sylph elder yet, but I'm sure it's only a matter of time."),
 "M53c": ("Buscarron opens his doors to all who pay and stay out of trouble.", RULES, "Buscarron prides himself on opening his doors to all customers─even those with unsavory reputations─so long as they pay good coin and stay out of trouble."),
 "M54a": ("After the Calamity Buscarron found the Qiqirn Teteroon fallen in the Shroud and nursed him back to health.", NEVER, "It was right after the [[Calamity]] that I came across him fallen in the [[The Black Shroud|Shroud]]. … So, I took him in and nursed him back to health best I could."),
 "M54b": ("Teteroon went north to Memeroon's Trading Post on Bronze Lake.", NEVER, "I reckon he meant the one right on the shore of [[Bronze Lake]]─[[Memeroon's Trading Post]]."),
 "M54c": ("You deliver Teteroon's forgotten earring, and he remembers Buscarron fondly.", NEVER, "You have delivered the scarlet earring to Teteroon. Reminded of [[Buscarron]], he promptly lapses into nostalgic reminiscences of former days."),
 "M55a": ("Teteroon says he would be dead without Buscarron.", BREW, "Good Buscaroon help Teteroon. Teteroon dead without good Buscaroon."),
 "M55b": ("Teteroon is brewing Qiqirn firewater.", BREW, "Teteroon has set about brewing his Qiqirn firewater from the ingredients you have provided."),
 "M56a": ("Teteroon has finished his gift for Buscarron.", WINE, "Teteroon has finally finished his gift for Buscarron."),
 "M56b": ("Buscarron is delighted with his old friend's liquor, though it should age a year.", WINE, "Buscarron is delighted to receive the hard liquor brewed by his old friend. However, he is less delighted when he realizes it would be best to age it a year before finally cracking it open."),
 # #57 Sylphish Concerns
 "M57a": ("Sylphs have been seen in a part of the wood beyond their domain.", CONC, "Sightings of sylphs in a region of the wood beyond their domain have given cause for concern."),
 "M57b": ("Buscarron thinks the missing sylph elder is likely among them.", CONC, "More than like, the missing sylph elder's among them."),
 "M57c": ("Garlean soldiers were never before able to reach the forest depths.", CONC, "Buscarron tells you that [[Garlean]] soldiers were never before able to penetrate the forest depths."),
 "M57d": ("The evidence suggests a traitor in Gridania is aiding the imperial advance.", CONC, "The mounting evidence seems to suggest that there is a traitor in [[Gridania]] aiding the imperial advance."),
 "M57e": ("Buscarron reasons that only someone who knew the Wailers' spires and watches could have guided them: a Gridanian traitor.", CONC, "Unless someone guided them through. Someone who knew where the spires stand, and when the Wailers watch. A Gridanian traitor."),
 # #58 Nouveau Riche
 "M58a": ("Suspicion surrounds the sudden good fortune of Laurentius.", RICH, "Suspicion surrounds the recent good fortune of a man named [[Laurentius]]."),
 "M58b": ("Laurentius is a Wood Wailer.", RICH, "Were he a merchant, I'd prob'ly think nothing of it, but this lad's a Wood Wailer."),
 "M58c": ("Laurentius confesses to selling maps and rations to the Empire.", RICH, "Aye, I sold maps and rations to the Empire. It was I."),
 "M58d": ("Laurentius repents and resolves to give himself up to the Order of the Twin Adder.", RICH, "he repents his decision to sell information and supplies to the Garleans, and resolves to give himself up to [[the Order of the Twin Adder]]."),
 "M58e": ("Buscarron brings news that the missing sylph elder has been found.", RICH, "He then shares some exciting news: the missing sylph elder has been found."),
 "M58f": ("You defeat a squad of imperial troops.", RICH, "You vanquish a squad of imperial troops, prompting Laurentius to admit defeat at long last."),
 # #59 Into the Beast's Maw
 "M59a": ("Fleeing Garlean soldiers, the sylph elder Frixio has gone into the Thousand Maws of Toto-Rak.", MAW, "Fleeing from [[Garlean]] soldiers, the sylph elder, [[Frixio]], has ventured into [[The Thousand Maws of Toto-Rak|the Thousand Maws of Toto–Rak]]."),
 "M59b": ("Were harm to befall him, the effort to make peace between man and sylph would be undone.", MAW, "Were any misfortune to befall him, the effort to secure peace between man and [[sylph]] would surely be undone."),
 "M59c": ("Noraxia reports that the elder went into Toto-Rak and has not returned.", MAW, "Elder one went into Toto–Rak, but has not returned!"),
 "M59d": ("Frixio is the eldest of the sylphs of Little Solace.", MAW, "This one is called Frixio, eldest of these ones of Little Solace."),
 "M59e": ("In Toto-Rak you meet Lahabrea of the Ascians, who sets a gigantic banemite on you.", MAW, "Within the bowels of Toto–Rak, you encounter [[Lahabrea]] of the [[Ascians]], who unleashes a gigantic banemite upon you."),
 "M59f": ("Lahabrea says all that stands between the world and Darkness is the Echo, an irksome anomaly in the aether.", MAW, "All that stands between this world and Darkness is an irksome anomaly in the aether─the Echo."),
 "M59h": ("An imperial centurion admits they pushed captured sylphs too hard to summon their eikon.", MAW, "I fear we may have been...overzealous in our efforts to compel them to summon their eikon."),
 "M59i": ("You find Frixio shaken but unharmed; he agrees to speak with you about Ramuh at Little Solace.", MAW, "you find Frixio, shaken but unharmed. Grateful for your timely intervention, he agrees to speak with you regarding [[Ramuh]], and bids you meet him later at [[Little Solace]]."),
 "M59j": ("Peace between man and sylph is now within reach.", MAW, "Owing to your efforts, peace between man and sylph is now within reach."),
 # #60 A Simple Gift
 "M60a": ("Buscarron sends a peace offering of rose oil to Knolexia in Little Solace.", GIFT, "Buscarron would like to send a peace offering to the sylphs of [[Little Solace]] in hopes of reinforcing the current spirit of cooperation."),
 "M60b": ("Buscarron says the Calamity weakened the elementals.", GIFT, "The wood is not what it once was. The Calamity changed the elementals─weakened them."),
 "M60c": ("Buscarron believes Gridanians and sylphs survive only by working together.", GIFT, "Only by working together and fighting together will we survive together─and the Twelveswood with us."),
 "M60d": ("The gift moves Knolexia, and may strengthen relations between Gridanians and sylphs.", GIFT, "Buscarron's thoughtful gift has moved Knolexia. With any luck, this act and similar future gestures will serve to further strengthen relations between [[Gridania]]ns and sylphs."),
 # #61 Believe in Your Sylph
 "M61a": ("Komuxio asks you to observe his tempered kindred so your word can reassure the Gridanians.", BEL, "Komuxio has asked you to observe his tempered kindred in the [[sylph]] homeland, hoping that your testimony might serve to reassure the [[Gridania]]ns that they have nothing to fear from his people."),
 "M61b": ("Frixio says the sylphs summoned Ramuh to protect the wood from imperial soldiers.", BEL, "These ones resorted to summoning Lord Ramuh to protect the wood from imperial ones."),
 "M61c": ("Ramuh was summoned against Frixio's wishes, and all who took part were tempered.", BEL, "Against this one's wishes, Lord Ramuh was summoned...and all those ones who took part became touched ones."),
 "M61d": ("Frixio fled to Little Solace with all who did not wish to be bound to Ramuh.", BEL, "So this one fled to Little Solace with all those ones who did not wish to be bound to Lord Ramuh."),
 "M61e": ("Papalymo says Ramuh's influence has made the tempered sylphs fiercely protective of their homeland.", BEL, "In the case of the sylphs, Ramuh's influence has made them ''fiercely'' protective of their homeland."),
 "M61f": ("Frixio gives you a crystal he says will one day be of use.", BEL, "Mark this one well: that crystal will one day be of use to walking one."),
 "M61g": ("Frixio warns that you are destined for a fate crueler than he can imagine.", BEL, "Walking one is destined to walk a fate far crueler than this one can imagine."),
 "M61h": ("Vorsaile is relieved that the sylphs want no conflict and do not intend to summon Ramuh.", BEL, "So the sylphs have no desire for conflict, nor do they intend to summon Ramuh."),
}

# ---- New entities --------------------------------------------------------------------------------------------------
ARC_GUILD, ARC_DRY, ARC_GC, ARC_ENV, ARC_ELDER = (
    "evt-adventurer-of-the-moment", "evt-drybone-vanishings", "evt-choosing-a-grand-company", "evt-envoys-to-the-sylphs", "evt-the-missing-elder")
ENTITIES = {
 ARC_GUILD: "event", ARC_DRY: "event", ARC_GC: "event", ARC_ENV: "event", ARC_ELDER: "event",
 "char-baderon": "character", "char-miounne": "character", "char-momodi": "character",
 "org-adventurers-guild": "organization", "org-lambs-of-dalamud": "organization",
 "char-isembard": "character", "char-ungust": "character", "char-ourcen": "character", "char-ifrit": "character",
 "org-twin-adder": "organization", "char-vorsaile": "character", "char-komuxio": "character", "char-frixio": "character",
 "char-buscarron": "character", "char-laurentius": "character", "org-wood-wailers": "organization",
 # Existing ids, listed so the module stands alone when linted by itself; the merge keeps the existing category.
 "org-serpent-reavers": "organization", "org-sahagin": "organization", "org-amaljaa": "organization",
 "org-immortal-flames": "organization", "org-maelstrom": "organization", "org-sylphs": "organization",
 "char-kan-e-senna": "character", "char-raubahn": "character", "char-merlwyb": "character", "char-nanamo": "character",
 "char-ramuh": "character",
}

N_GUILD = "The Adventurer of the Moment"
N_DRY = "The Drybone Vanishings"
N_GC = "Choosing a Grand Company"
N_ENV = "Envoys to the Sylphs"
N_ELDER = "The Missing Elder"

# Shared openings for the Grand Company recaps (each pair's own text follows).
GC_LEAD = "Officers of all three Grand Companies came to the Waking Sands to court Ifrit's bane, and you heard each company's leader at the remembrance services. "
ELDER_LEAD = "The elder of the sylphs of Little Solace has gone missing, and Commander Vorsaile fears a crisis if the tempered sylphs take him. "

BIGGS_41 = ("An engineer of the Ironworks who crewed its first airship since the Calamity with Wedge; the Ironworks' master has been missing since then. "
            "Imperial soldiers shot the ship down near {place} and tried to seize it, but were driven off, and the two engineers got away.")
BIGGS_42 = ("An engineer of the Ironworks, whose first airship since the Calamity he and Wedge crewed until imperial soldiers shot it down. "
            "The two are now under the Scions' protection at the Waking Sands: as a neutral party, the Scions keep this airship technology, and the Ironworks sent its engineers to help.")
WEDGE_41 = ("An engineer of the Ironworks who crewed its first airship since the Calamity with Biggs; the Ironworks' master has been missing since then. "
            "Imperial soldiers shot the ship down near {place} and tried to seize it, but were driven off, and the two engineers got away.")
WEDGE_42 = ("An engineer of the Ironworks, whose first airship since the Calamity he and Biggs crewed until imperial soldiers shot it down. "
            "The two are now under the Scions' protection at the Waking Sands: as a neutral party, the Scions keep this airship technology, and the Ironworks sent its engineers to help.")

PRES = {
 # ---- Arc t1: The Adventurer of the Moment (#25–#30) ----
 ARC_GUILD: [
   P(S[25], None, "main", N_GUILD,
     "Baderon of the Drowning Wench in Limsa Lominsa sent you to the Sastasha Seagrot, where the Yellowjackets feared pirates were gathering. "
     "You found the Serpent Reavers and their Sahagin masters using its caves as a base. Baderon then passed you a job from the Adventurers' Guild in Gridania.",
     ["M25a", "M25b", "M25c", "M25e"]),
   P(S[26], None, "main", N_GUILD,
     "After you uncovered the Serpent Reavers' base in the Sastasha Seagrot, Baderon sent you on to Gridania. "
     "There Miounne, proprietress of the Carline Canopy, speaks for the Adventurers' Guild, and she has a task for you with a fair bit to tell.",
     ["M25c", "M26a", "M26b", "M26c"]),
   P(S[27], None, "main", N_GUILD,
     "Work for the Adventurers' Guild has taken you from Limsa Lominsa to Gridania. For Miounne you broke up the Lambs of Dalamud, a doomsday cult that blames Eorzeans for the lesser moon's destruction, in the Tam-Tara Deepcroft. "
     "She worries that adventurers are dying as the unprepared take on jobs beyond them, and has passed you on to Ul'dah.",
     ["M25e", "M27a", "M27b", "M27c", "M27d", "M27e"]),
   P(S[28], None, "main", N_GUILD,
     "For the Adventurers' Guild you have cleared pirates from Sastasha in La Noscea and a doomsday cult from the Tam-Tara Deepcroft in the Twelveswood. "
     "Now Miounne has sent you to Ul'dah, praising you to Momodi of the Quicksand as the adventurer of the moment, and warning that Momodi's task will likely be dangerous.",
     ["M25c", "M27c", "M28a", "M28c", "M28d"]),
   P(S[29], None, "main", N_GUILD,
     "Momodi of the Quicksand sent you into Copperbell Mines, reopened to supply Ul'dah's rebuilding, where giants that miners of old had sealed in its depths were wreaking havoc. "
     "You subdued them, so mining can resume and Ul'dah will have the materials it needs to rebuild. Miounne's adventurer of the moment has now proved useful in all three city-states.",
     ["M29a", "M29b", "M29c", "M29d", "M29e", "M28c"]),
   P(S[30], None, "main", N_GUILD,
     "Your deeds for the Adventurers' Guild drew the notice of the Scions of the Seventh Dawn, who are headquartered at the Waking Sands in Vesper Bay and stand above politics. "
     "Their leader, Minfilia, shares your gift, the Echo, which lets you hear the past within another's soul. She believes it is the key to the primal threat, and has given you the order's password.",
     ["M30a", "C34", "C01", "C02", "C33", "M30c", "M30b", "M30e"]),
 ],
 "char-baderon": [
   P(S[25], None, "main", "Baderon",
     "Proprietor of the Drowning Wench in Limsa Lominsa, who finds work for capable adventurers. He sent you to the Sastasha Seagrot, where the Serpent Reavers and their Sahagin masters had made a base, "
     "and then passed on a job from the Adventurers' Guild in Gridania.",
     ["M25a", "M25c", "M25e"]),
 ],
 "char-miounne": [
   P(S[26], None, "main", "Miounne",
     "Proprietress of the Carline Canopy in Gridania, through whom the Adventurers' Guild there hires adventurers. Baderon of Limsa Lominsa calls her his counterpart.",
     ["M26a", "M26b"], ["Mother Miounne"]),
   P(S[27], None, "main", "Miounne",
     "Proprietress of the Carline Canopy in Gridania, through whom the Adventurers' Guild there hires adventurers. She sent you to break up the Lambs of Dalamud in the Tam-Tara Deepcroft, "
     "and worries that adventurers are dying more often as the unprepared take on jobs beyond them.",
     ["M26a", "M27a", "M27c", "M27d"], ["Mother Miounne"]),
 ],
 "char-momodi": [
   P(S[28], None, "main", "Momodi",
     "Proprietress of the Quicksand in Ul'dah, through whom the Adventurers' Guild there hires adventurers. Miounne calls her Ul'dah's version of herself.",
     ["M28a", "M28b"]),
   P(S[30], None, "main", "Momodi",
     "Proprietress of the Quicksand in Ul'dah, through whom the Adventurers' Guild there hires adventurers. She sent you into Copperbell Mines, "
     "and she speaks well of the Scions of the Seventh Dawn, warning that their work is no ordinary work; she told you where to find them.",
     ["M28a", "M29a", "M29f", "M30a"]),
 ],
 "org-adventurers-guild": [
   P(S[25], None, "main", "The Adventurers' Guild",
     "A guild that hires out adventurers. It keeps a building north of Aleport in La Noscea, and its branch in Gridania has asked for a seasoned adventurer.",
     ["M25f", "M25e"]),
   P(S[27], None, "main", "The Adventurers' Guild",
     "A guild that hires out adventurers, with branches in Gridania, where Miounne speaks for it, and in Ul'dah. "
     "Demand for adventurers has grown so much that the unprepared take on tasks beyond them, and deaths are becoming more common.",
     ["M26a", "M27d", "M27e"]),
 ],
 "org-serpent-reavers": [
   P(S[25], None, "main", "The Serpent Reavers",
     "Pirates allied with the Sahagin, who are their masters. The Yellowjackets feared Reavers were gathering in the Sastasha Seagrot, and you found them and the Sahagin using its caves as a base.",
     ["M25b", "M25c"]),
 ],
 "org-sahagin": [
   P(S[25], None, "main", "The Sahagin",
     "A beast tribe, masters of the pirate Serpent Reavers. Baderon recalls their pirates raiding Limsa Lominsa not long ago, and you found the two using the Sastasha Seagrot as a base.",
     ["M25c", "M25d"]),
   P(S[40], None, "main", "The Sahagin",
     "A beast tribe, masters of the pirate Serpent Reavers, who used the Sastasha Seagrot as a base. At Limsa Lominsa's remembrance service, Admiral Merlwyb warned that the Sahagin creep ashore seeking blood for their god.",
     ["M25c", "M40o"]),
 ],
 "org-lambs-of-dalamud": [
   P(S[27], None, "main", "The Lambs of Dalamud",
     "A doomsday cult that arose before the Calamity and holds the lesser moon Dalamud divine. Blaming Eorzeans for its apparent destruction, the cult seeks to avenge its god. "
     "You broke up its rite in the Tam-Tara Deepcroft and sent the spirit it woke back to the abyss.",
     ["M27f", "M27b", "M27c"]),
 ],
 "org-scions": [
   P(S[30], None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. It stands above politics, and its headquarters is the Waking Sands in Vesper Bay, western Thanalan.",
     ["C34", "C01", "C02"]),
   P(S[31], None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia from the Waking Sands in Vesper Bay. Its leading members are Sharlayans who stayed in Eorzea when their countrymen fled; "
     "their own leader was taken from them at the Battle of Carteneau. It is investigating crimes near Ul'dah that it suspects involve a primal.",
     ["C34", "C01", "C31", "M31h", "M31b"]),
   P(S[43], None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving the future of all Eorzea, where the Grand Companies protect their own nations, led by Minfilia from the Waking Sands. "
     "It studied the sylphs for the Order of the Twin Adder, and now hopes to win their favor to ease the primal threat.",
     ["C34", "C01", "M40d", "M43b", "M43f"]),
 ],
 "loc-waking-sands": [
   P(S[30], None, "main", "The Waking Sands",
     "The Scions' headquarters in Vesper Bay, western Thanalan, where Tataru welcomes visitors and Minfilia receives them.",
     ["C02", "M30f", "M30b"]),
   P(S[31], None, "main", "The Waking Sands",
     "The Scions' headquarters in Vesper Bay, western Thanalan, where Urianger presides over the order's affairs.",
     ["C02", "C41"]),
 ],
 "char-minfilia": [
   P(S[30], None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who welcomed you at the Waking Sands. Like you, she has the Echo, and she believes it is the key to dealing with the primals, a bane upon Eorzea.",
     ["C01", "C33", "M30b", "M30d"]),
   P(S[39], None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. She sent you to an Immortal Flames ambush as the Scions' representative, "
     "and after you struck down Ifrit she told you that those with the Echo are immune to a primal's influence. She seeks a peaceful answer to the primals, but wants the Scions ready to fight.",
     ["C01", "C33", "M39a", "M39g", "M38a"]),
   P(S[43], None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. She has asked you to learn the sylphs' intentions with the Echo, "
     "hoping their favor will bring the Scions closer to mitigating the primal threat.",
     ["C01", "C33", "M43a", "M43f"]),
 ],
 "char-tataru": [
   P(S[30], None, "main", "Tataru",
     "A Lalafell who welcomed you to the Waking Sands, headquarters of the Scions of the Seventh Dawn, and looks forward to assisting you.",
     ["M30f", "M30g"]),
   P(S[31], None, "main", "Tataru",
     "The Scions' clerk, who makes sure everything runs smoothly.",
     ["C32"]),
 ],
 "char-thancred": [
   P(S[31], None, "main", "Thancred",
     "A Scion who serves as the order's man in Ul'dah, and who briefed your first investigation.",
     ["C31", "C39"]),
   P(S[34], None, "main", "Thancred",
     "A Scion who serves as the order's man in Ul'dah. He has joined your hunt for the missing at Camp Drybone, and suspects Sister Ourcen, who hears the commonfolk's confessions. "
     "He swears he has seen the face of the lichkeeper Marques somewhere before.",
     ["C39", "M34g", "M34e", "M34f"]),
   P(S[37], None, "main", "Thancred",
     "A Scion who serves as the order's man in Ul'dah. After a leaflet led him to suspect the culprit behind the Drybone vanishings was posing as a priest, "
     "he and you disguised yourselves as vagrants and exposed the false priest Ungust. He suspects someone also leaked the Immortal Flames' patrol routes.",
     ["C39", "M36d", "M37a", "M37c", "M37i"]),
   P(S[39], None, "main", "Thancred",
     "A Scion who serves as the order's man in Ul'dah, and who led your investigation of the Drybone vanishings. After you struck down Ifrit, "
     "he revealed that to keep the primal from gaining strength, its tempered victims must be put to death.",
     ["C39", "M37c", "M39f"]),
 ],
 "char-yshtola": [
   P(S[31], None, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order, and who told you how the Scions were founded.",
     ["C31", "C40"]),
 ],
 "char-urianger": [
   P(S[31], None, "main", "Urianger",
     "A Scion who presides over the affairs of the Waking Sands.",
     ["C31", "C41"]),
 ],
 "char-yda": [
   P(S[31], None, "main", "Yda",
     "A masked Scion who, with Papalymo, surveys the Twelveswood for the order.",
     ["C31", "M31g"]),
   P(S[43], None, "main", "Yda",
     "A masked Scion who, with Papalymo, surveys the Twelveswood for the order. The two studied the sylphs for the Order of the Twin Adder, and are helping you win the sylphs' trust.",
     ["M31g", "M43b", "M43h"]),
 ],
 "char-papalymo": [
   P(S[31], None, "main", "Papalymo",
     "A Scion who, with Yda, surveys the Twelveswood for the order.",
     ["C31", "M31g"]),
   P(S[43], None, "main", "Papalymo",
     "A Scion who, with Yda, surveys the Twelveswood for the order. The two studied the sylphs for the Order of the Twin Adder, and are helping you win the sylphs' trust.",
     ["M31g", "M43b", "M43h"]),
   P(S[51], None, "main", "Papalymo",
     "A Scion who, with Yda, surveys the Twelveswood and is helping you win the sylphs' trust. He explained that sylphs in the forest have been tempered by Ramuh, "
     "and like the Amalj'aa tempered by Ifrit, exist only to serve their primal.",
     ["M31g", "M43h", "M51b", "M51c"]),
   P(S[61], None, "main", "Papalymo",
     "A Scion who, with Yda, surveys the Twelveswood and helped you make peace with the sylphs. He explained that tempered followers take on their primal's nature: "
     "Ramuh's influence has made his tempered sylphs fiercely protective of their homeland.",
     ["M31g", "M51b", "M61e"]),
 ],
 # ---- Arc t2: The Drybone Vanishings (#31–#39) ----
 ARC_DRY: [
   P(S[31], None, "main", N_DRY,
     "You pledged yourself to the Scions of the Seventh Dawn and met their leading members. Your first task is a crystal caravan robbery and a wave of disappearances near Ul'dah; "
     "the evidence points to the Amalj'aa, worshipers of the primal Ifrit. Thancred sent you to Isembard, the de facto leader of Camp Drybone, who has offered his full cooperation.",
     ["M31a", "M31b", "M31c", "M31d", "M31e", "M31f", "M31j"]),
   P(S[32], None, "main", N_DRY,
     "The Scions suspect a primal behind a crystal robbery and a wave of disappearances near Ul'dah. At Camp Drybone you recovered the bodies of churchgoers the Amalj'aa butchered, so Isembard could bury them. "
     "He doubts the Amalj'aa act alone in the vanishings, and wonders who else has a hand in them.",
     ["M31b", "M31e", "M32a", "M32b", "M32c"]),
   P(S[33], None, "main", N_DRY,
     "Isembard of Camp Drybone doubts the Amalj'aa alone are behind the vanishings around the camp. He sent you to Ungust, a Drybone-born merchant who recognized you as the adventurer who once threatened him in Ul'dah. "
     "Ungust waves the disappearances away, and the frightened commonfolk say little; Isembard thinks they trust only their gods.",
     ["M32c", "M33a", "M33b", "M33c", "M33d", "M33e"]),
   P(S[34], None, "main", N_DRY,
     "The search for whoever is helping the Amalj'aa with the Drybone vanishings led you to the Church of Saint Adama Landama. Its lichkeeper, Marques, knew little, and Sister Ourcen, the commonfolk's confidante, had heard nothing useful. "
     "Thancred has joined the hunt: he suspects Ourcen, to Isembard's dismay, and swears he has seen Marques's face before.",
     ["M32c", "M34a", "M34b", "M34c", "M34d", "M34e", "M34f"]),
   P(S[35], None, "main", N_DRY,
     "Thancred suspects Sister Ourcen, who hears the commonfolk's confessions, of a hand in the Drybone vanishings, but Isembard refuses to believe it. "
     "When she went out alone to find an orphan's lost ring, you saved her from undead soldiers. Isembard is now more certain than ever of her innocence.",
     ["M34e", "M35a", "M35c", "M35b", "M35d"]),
   P(S[36], None, "main", N_DRY,
     "Searching an Amalj'aa camp near Drybone for Thancred, you found a leaflet offering the poor work. Sister Ourcen said it was not of her Order's making, and that garments had gone missing from the church. "
     "Thancred reasons that whoever is behind the vanishings is posing as a priest, and has withdrawn to plan.",
     ["M36a", "M36b", "M36c", "M36d", "M36e"]),
   P(S[37], None, "main", N_DRY,
     "Posing as vagrants, you and Thancred drew out the false priest behind the Drybone vanishings at a commune of the poor north of Sandgate. He was Ungust, who confessed to luring people to the Amalj'aa and selling them crystal shipment schedules. "
     "Only the Amalj'aa know where the abductees were taken, and Minfilia says a clash with them is inevitable.",
     ["M37a", "M37b", "M37c", "M37d", "M37e", "M37g", "M37h"]),
   P(S[38], None, "main", N_DRY,
     "Ungust, the false priest of Drybone, confessed to handing the poor he lured to the Amalj'aa, and only the Amalj'aa know where they were taken. "
     "While a clash with them looms, Minfilia, who seeks a peaceful answer to the primals but wants you ready to fight, sent you to a goblin scholar to learn how materia can strengthen your gear.",
     ["M37c", "M37f", "M37g", "M37h", "M38a", "M38b", "M38c"]),
   P(S[39], None, "main", N_DRY,
     "To find the abductees, the Immortal Flames set an ambush for the Amalj'aa with Ungust as bait, and Minfilia sent you as the Scions' representative. "
     "A traitor in the Flames' ranks gave you away, and you woke as an offering to the primal Ifrit. Immune to him through the Echo, you struck him down, but his tempered victims must be put to death.",
     ["M39a", "M39b", "M39c", "M39d", "M39g", "M39f"]),
 ],
 "char-isembard": [
   P(S[31], None, "main", "Isembard",
     "The de facto leader of Camp Drybone in eastern Thanalan, who has offered you his full cooperation in the Scions' investigation of the disappearances.",
     ["M31f", "M31j"]),
   P(S[32], None, "main", "Isembard",
     "The de facto leader of Camp Drybone, who is helping you look into the disappearances there. He buried the churchgoers the Amalj'aa butchered, "
     "and believes the Amalj'aa cannot be acting alone: someone else must have a hand in the vanishings.",
     ["M31f", "M32a", "M32c"]),
   P(S[35], None, "main", "Isembard",
     "The de facto leader of Camp Drybone, who is helping you look into the vanishings there and suspects the Amalj'aa have help. "
     "He refuses to believe Thancred's suspicion of Sister Ourcen, and since you saved her he is more convinced than ever that she is innocent.",
     ["M31f", "M32c", "M34e", "M35a", "M35d"]),
 ],
 "char-ungust": [
   P(S[33], None, "main", "Ungust",
     "A merchant born in Drybone and raised in the Golden Bazaar, said to know the commonfolk best. He recognized you as the adventurer who threatened him in Ul'dah, "
     "and seems unconcerned by the growing number of missing people around Drybone.",
     ["M33a", "M33b", "M33c"]),
   P(S[37], None, "main", "Ungust",
     "A Drybone-born merchant whom you first found preying on a refugee woman in Ul'dah. He was unmasked as the false priest behind the Drybone vanishings: "
     "at the behest of the Amalj'aa he lured the vulnerable to them, after first selling them the schedule of crystal shipments from the Nanawa Mines.",
     ["M33a", "M37c", "M37d", "M37f", "M37e"]),
   P(S[39], None, "main", "Ungust",
     "A Drybone-born merchant who, as a false priest, lured the vulnerable to the Amalj'aa. The Immortal Flames used him as bait to capture Amalj'aa, "
     "but a traitor in their ranks sprang a trap on them.",
     ["M37c", "M37f", "M39a", "M39b"]),
 ],
 "char-ourcen": [
   P(S[34], None, "main", "Ourcen",
     "A sister of the Church of Saint Adama Landama, through whom the commonfolk of Drybone speak to their keeper, Thal. She has heard nothing that helps your investigation, "
     "but Thancred suspects her, since she hears the commonfolk's confessions.",
     ["M34b", "M34c", "M34d", "M34e"], ["Sister Ourcen"]),
   P(S[35], None, "main", "Ourcen",
     "A sister of the Church of Saint Adama Landama and confidante of the commonfolk of Drybone. Thancred suspects her of a hand in the vanishings, "
     "but after she risked her life to recover an orphan's ring and you saved her from undead soldiers, Isembard is sure she is innocent.",
     ["M34c", "M34e", "M35c", "M35b", "M35d"], ["Sister Ourcen"]),
   P(S[36], None, "main", "Ourcen",
     "A sister of the Church of Saint Adama Landama and confidante of the commonfolk of Drybone, whom Isembard believes innocent of the vanishings. "
     "She told you a leaflet found in an Amalj'aa camp was not of her Order's making, and that garments had gone missing from the church.",
     ["M34c", "M35d", "M36c"], ["Sister Ourcen"]),
 ],
 "char-marques": [
   P(S[34], None, "main", "Marques",
     "A man who tends the graves of the lichyard at the Church of Saint Adama Landama, near Camp Drybone, and knows little of the commonfolk. Thancred swears he has seen his face somewhere before.",
     ["M34a", "M34b", "M34f"]),
 ],
 "char-ifrit": [
   P(S[31], None, "main", "Ifrit",
     "A primal worshiped by the Amalj'aa. The Scions suspect a primal is behind a crystal robbery and a wave of disappearances near Ul'dah, and the evidence points to the Amalj'aa.",
     ["M31d", "M31b", "M31e"]),
   P(S[39], None, "main", "Ifrit",
     "A primal of the Amalj'aa, who can bind mortals to his will. The crystal robbery and abductions near Ul'dah served his cause, and the Amalj'aa meant to offer you and captured Immortal Flames to him. "
     "The Echo made you immune, and you struck him down; his tempered victims must be put to death to keep him from gaining strength.",
     ["M39d", "M39e", "M39c", "M39f"]),
   P(S[40], None, "main", "Ifrit",
     "A primal of the Amalj'aa, who can bind mortals to his will; you struck him down, immune through the Echo. The Amalj'aa summon him more and more often, "
     "and though Ul'dah's forces always smite him, each victory costs blood.",
     ["M39d", "M40b", "M40m", "M40z"]),
 ],
 "org-amaljaa": [
   P(S[31], None, "main", "The Amalj'aa",
     "A beast tribe known to worship the primal Ifrit. Evidence left at a robbed crystal caravan near Ul'dah implicates them, and the Scions suspect a primal is involved.",
     ["M31d", "M31c", "M31b"]),
   P(S[32], None, "main", "The Amalj'aa",
     "A beast tribe that worships the primal Ifrit, implicated in a crystal robbery near Ul'dah. They have butchered churchgoers near Camp Drybone, but Isembard doubts they act alone in the disappearances there.",
     ["M31d", "M32a", "M32c"]),
   P(S[37], None, "main", "The Amalj'aa",
     "A beast tribe that worships the primal Ifrit. The false priest Ungust confessed that he lured the poor of Drybone to them, after selling them the schedule of crystal shipments from the Nanawa Mines; "
     "only they know where the abductees were taken.",
     ["M31d", "M37d", "M37e", "M37g"]),
   P(S[39], None, "main", "The Amalj'aa",
     "A beast tribe that worships the primal Ifrit. The crystal robbery and abductions they carried out near Ul'dah served his cause, and they meant to offer you and the Immortal Flames they captured to him.",
     ["M39e", "M39b", "M39c"]),
   P(S[40], None, "main", "The Amalj'aa",
     "A beast tribe that summons the primal Ifrit, and does so more and more often. At Ul'dah's remembrance service, Raubahn warned that their hordes wait beside the roads, strangling the city's trade.",
     ["M40m", "M40j"]),
 ],
 "org-immortal-flames": [
   P(S[39], None, "main", "The Immortal Flames",
     "A force that, with you as the Scions' representative, set an ambush to capture Amalj'aa using the false priest Ungust as bait. A traitor in its ranks gave the plan away, "
     "and its soldiers were taken captive to be offered to Ifrit.",
     ["M39a", "M39b", "M39c"]),
   P(S[40], None, "main", "The Immortal Flames",
     "Ul'dah's Grand Company, led by Flame General Raubahn, which has sent an officer to the Waking Sands to recruit you. Its forces always smite Ifrit when the Amalj'aa summon him, "
     "but each victory costs blood, a war of attrition Ul'dah cannot well sustain.",
     ["M40c", "M40i", "M40b", "M40z"]),
   P(S42, None, "main", "The Immortal Flames",
     "Ul'dah's Grand Company, whose soldiers would lay down their lives at a word from Flame General Raubahn to keep Ul'dah at peace. Recruits must forsake all other nations. "
     "It is fighting a large operation against the Amalj'aa in western Thanalan.",
     ["M40c", "M42c", "M42b", "M41f"]),
 ],
 # ---- Arc t3: Choosing a Grand Company (#40–#42c) ----
 ARC_GC: [
   P(S[40], None, "main", N_GC,
     "Word of how you bested Ifrit has brought officers of all three Grand Companies to the Waking Sands to court you. At the remembrance services, Kan-E-Senna, Raubahn and Merlwyb each spoke of their city-state's troubles, "
     "while the twins Alphinaud and Alisaie looked on. Now you must choose a company and give your answer to its officer.",
     ["M40a", "M40b", "M40u", "M40i", "M40w", "C10", "M40t"]),
   P(S41, None, "main", N_GC,
     GC_LEAD + "You chose the Immortal Flames of Ul'dah. Your induction at the Hall of Flames was cut short by an imperial attack on an airship near Horizon's Edge, "
     "and you helped drive off the soldiers trying to seize it, saving its crew, Biggs and Wedge, engineers of the Ironworks.",
     ["M40b", "M41a", "M41b", "M41d", "M41c"]),
   P(S42, None, "main", N_GC,
     "You chose the Immortal Flames, Ul'dah's Grand Company, and after rescuing two Ironworks engineers from imperial soldiers you swore its oath, forsaking all other nations. "
     "Back at the Waking Sands, Minfilia announced that the engineers, Biggs and Wedge, are now under the Scions' protection: as a neutral party, the Scions will keep their airship technology.",
     ["M41a", "M41c", "M42a", "M42b", "M42d", "M42e"]),
   P(S41B, None, "main", N_GC,
     GC_LEAD + "You chose the Maelstrom of Limsa Lominsa. Your induction at Maelstrom Command was cut short by an imperial attack on an airship in Cedarwood, "
     "and you helped drive off the soldiers trying to seize it, saving its crew, Biggs and Wedge, engineers of the Ironworks.",
     ["M40b", "M41ba", "M41bb", "M41bd", "M41bc"]),
   P(S42B, None, "main", N_GC,
     "You chose the Maelstrom, Limsa Lominsa's Grand Company, and after rescuing two Ironworks engineers from imperial soldiers you were sworn in as a storm private third class. "
     "Back at the Waking Sands, Minfilia announced that the engineers, Biggs and Wedge, are now under the Scions' protection: as a neutral party, the Scions will keep their airship technology.",
     ["M41ba", "M41bc", "M42ba", "M42be", "M42bc", "M42bd"]),
   P(S41C, None, "main", N_GC,
     GC_LEAD + "You chose the Order of the Twin Adder of Gridania. Your induction at the Adders' Nest was cut short by an imperial attack on an airship southeast of Nine Ivies, "
     "and you helped drive off the soldiers trying to seize it, saving its crew, Biggs and Wedge, engineers of the Ironworks.",
     ["M40b", "M41ca", "M41cb", "M41cd", "M41cc"]),
   P(S42C, None, "main", N_GC,
     "You chose the Order of the Twin Adder, Gridania's Grand Company, and after rescuing two Ironworks engineers from imperial soldiers you were sworn into its ranks. "
     "Back at the Waking Sands, Minfilia announced that the engineers, Biggs and Wedge, are now under the Scions' protection: as a neutral party, the Scions will keep their airship technology.",
     ["M41ca", "M41cc", "M42ca", "M42cd", "M42ce"]),
 ],
 "char-alphinaud": [
   P(S[40], None, "main", "Alphinaud",
     "A young traveler who, with his twin sister, calls himself a student of history. At the remembrance services he weighed each city-state's troubles, "
     "and he believes the task of healing Eorzea's wounds falls to the Scions of the Seventh Dawn, with help from the Grand Companies.",
     ["C10", "C42", "M40q"]),
 ],
 "char-alisaie": [
   P(S[40], None, "main", "Alisaie",
     "Alphinaud's twin sister, who with him calls herself a student of history. She scorned the remembrance services as standard-waving rallies, and means to find another way to heal the realm, "
     "though her brother says their destination is the same.",
     ["C10", "C42", "M40r", "M40s"]),
 ],
 "char-kan-e-senna": [
   P(S[40], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania and supreme commander of its Grand Company, the Order of the Twin Adder. At the remembrance service she warned that the Ixal have returned in force, "
     "and that the Garleans, raising steel fortresses in the Twelveswood, remain the greatest threat.",
     ["M40u", "M40e", "M40f", "M40g"], ["the Elder Seedseer"]),
   P(S[47], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania and supreme commander of the Order of the Twin Adder. She has no wish to see her people in another war, "
     "and has sent the sylphs a letter vouching for Gridania's envoy and restating its wish for harmony with them.",
     ["M40e", "M44c", "M47a", "M47b"], ["the Elder Seedseer"]),
 ],
 "char-raubahn": [
   P(S[40], None, "main", "Raubahn",
     "The Flame General of Ul'dah, at the head of its Grand Company, the Immortal Flames. At the remembrance service he called on a divided people to unite, "
     "warning that the Amalj'aa strangle the city's trade while the Garleans make mock of its borders.",
     ["M40i", "M40j", "M40k"], ["General Raubahn"]),
 ],
 "char-nanamo": [
   P(S[40], None, "main", "Nanamo",
     "The sultana of Ul'dah, seventeenth in the line of Ul. At the remembrance service she told her people that Ul'dah's true wealth lies in their health, happiness and hopes.",
     ["M40l"], ["the sultana"]),
 ],
 "char-merlwyb": [
   P(S[40], None, "main", "Merlwyb",
     "The Admiral of Limsa Lominsa and Chief Admiral of its Grand Company, the Maelstrom. At the remembrance service she warned that beast tribes and the Garleans press on Limsa while mutiny breeds below deck, "
     "and called for pirates and the Maelstrom to mend their rift.",
     ["M40v", "M40w", "M40o", "M40p"], ["Admiral Merlwyb", "the Admiral"]),
 ],
 "org-maelstrom": [
   P(S[40], None, "main", "The Maelstrom",
     "Limsa Lominsa's Grand Company, under Admiral Merlwyb, reborn when the Garlean Empire marched on Eorzea. It has sent an officer to the Waking Sands to recruit you, "
     "and Merlwyb calls for mending the rift between pirates and the Maelstrom.",
     ["M40c", "M40w", "M40n", "M40b", "M40p"]),
   P(S42B, None, "main", "The Maelstrom",
     "Limsa Lominsa's Grand Company, under Admiral Merlwyb, reborn when the Garlean Empire marched on Eorzea. "
     "Its soldiers are charged with meeting the threats of the primals and the Empire, and with solving the many problems the Calamity caused.",
     ["M40c", "M40w", "M40n", "M42bb"]),
 ],
 "org-twin-adder": [
   P(S[40], None, "main", "The Order of the Twin Adder",
     "Gridania's Grand Company, under the supreme command of Elder Seedseer Kan-E-Senna. It has sent an officer to the Waking Sands to recruit you. "
     "Kan-E-Senna says the Ixal have returned in force and the Empire is raising steel fortresses in the Twelveswood.",
     ["M40c", "M40e", "M40b", "M40f", "M40g"], ["the Twin Adder"]),
   P(S42C, None, "main", "The Order of the Twin Adder",
     "Gridania's Grand Company, under the supreme command of Elder Seedseer Kan-E-Senna. It was formed before the Calamity to fight the Garlean Empire and the beast tribes and their primals, "
     "and draws together the nation's martial, economic and technological resources.",
     ["M40c", "M42cc", "M42cb", "M42cf"], ["the Twin Adder"]),
   P(S[44], None, "main", "The Order of the Twin Adder",
     "Gridania's Grand Company, under the supreme command of Elder Seedseer Kan-E-Senna, which asked the Scions to study the sylphs. "
     "The sylphs' ties to the primal Ramuh have raised a warning in its ranks, and Commander Vorsaile has asked the Scions to serve as an impartial liaison to them.",
     ["M40c", "M40e", "M43b", "M44d", "M44a"], ["the Twin Adder"]),
 ],
 "char-garuda": [
   P(S[40], None, "main", "Garuda",
     "A bloodthirsty primal summoned by the Ixal, a warlike beast tribe.",
     ["M40h"]),
   P(S[43], None, "main", "Garuda",
     "A bloodthirsty primal summoned by the warlike Ixal. Papalymo counts her among the most savage of all primals, and Gridania has its hands full fending her off.",
     ["M40h", "M43e"]),
 ],
 "org-ixal": [
   P(S[40], None, "main", "The Ixal",
     "A warlike beast tribe that summons the primal Garuda. Kan-E-Senna says they have returned in force, emboldened by Gridania's suffering.",
     ["M40h", "M40f"]),
   P(S[47], None, "main", "The Ixal",
     "A warlike beast tribe that summons the primal Garuda and has returned in force against Gridania. The war with them has taken a toll on Gridania's resources.",
     ["M40h", "M40f", "M47c"]),
 ],
 "org-garlean-empire": [
   P(S[40], None, "main", "The Garlean Empire",
     "An empire that brought a war of conquest to Eorzea, and whose armies the Alliance met at Carteneau five years ago. "
     "Kan-E-Senna calls the Garleans the greatest threat as they raise steel fortresses in the Twelveswood, and Merlwyb says their flags fly within Limsa Lominsa's borders.",
     ["M40x", "M40g", "M40o"], ["the Empire"]),
   P(S[50], None, "main", "The Garlean Empire",
     "An empire that brought a war of conquest to Eorzea and is raising fortresses in the Twelveswood. The sylphs have been wary since it came to the Shroud, "
     "and in the East Shroud you fought imperial soldiers guarding a cache of supplies, logged by someone who knows the forest.",
     ["M40x", "M40g", "M44f", "M50b", "M50c"], ["the Empire"]),
   P(S[58], None, "main", "The Garlean Empire",
     "An empire that brought a war of conquest to Eorzea and is raising fortresses in the Twelveswood. Its soldiers, never before able to reach the forest depths, "
     "got there with the help of a Gridanian traitor, the Wood Wailer Laurentius, who sold them maps and rations.",
     ["M40x", "M40g", "M57c", "M57d", "M58c"], ["the Empire"]),
   P(S[59], None, "main", "The Garlean Empire",
     "An empire that brought a war of conquest to Eorzea and has sent soldiers deep into the Twelveswood, guided by a Gridanian traitor. "
     "The sylph elder fled from them into the Thousand Maws of Toto-Rak, and a vision showed imperial officers who had pushed captured sylphs too hard to summon their eikon.",
     ["M40x", "M57d", "M58c", "M59a", "M59h"], ["the Empire"]),
 ],
}

PRES.update({
 "char-biggs": [
   P(S41, None, "main", "Biggs", BIGGS_41.format(place="Horizon's Edge"), ["M41c", "M41e", "M41b", "M41d", "M41g"]),
   P(S42, None, "main", "Biggs", BIGGS_42, ["M41c", "M41e", "M42d", "M42e"]),
   P(S41B, None, "main", "Biggs", BIGGS_41.format(place="Cedarwood"), ["M41bc", "M41be", "M41bb", "M41bd", "M41bf"]),
   P(S42B, None, "main", "Biggs", BIGGS_42, ["M41bc", "M41be", "M42bc", "M42bd"]),
   P(S41C, None, "main", "Biggs", BIGGS_41.format(place="Nine Ivies"), ["M41cc", "M41ce", "M41cb", "M41cd", "M41cf"]),
   P(S42C, None, "main", "Biggs", BIGGS_42, ["M41cc", "M41ce", "M42cd", "M42ce"]),
 ],
 "char-wedge": [
   P(S41, None, "main", "Wedge", WEDGE_41.format(place="Horizon's Edge"), ["M41c", "M41e", "M41b", "M41d", "M41g"]),
   P(S42, None, "main", "Wedge", WEDGE_42, ["M41c", "M41e", "M42d", "M42e"]),
   P(S41B, None, "main", "Wedge", WEDGE_41.format(place="Cedarwood"), ["M41bc", "M41be", "M41bb", "M41bd", "M41bf"]),
   P(S42B, None, "main", "Wedge", WEDGE_42, ["M41bc", "M41be", "M42bc", "M42bd"]),
   P(S41C, None, "main", "Wedge", WEDGE_41.format(place="Nine Ivies"), ["M41cc", "M41ce", "M41cb", "M41cd", "M41cf"]),
   P(S42C, None, "main", "Wedge", WEDGE_42, ["M41cc", "M41ce", "M42cd", "M42ce"]),
 ],
 # ---- Arc t4: Envoys to the Sylphs (#43–#51) ----
 ARC_ENV: [
   P(S[43], None, "main", N_ENV,
     "Minfilia has asked you to learn the intentions of the sylphs, a beast tribe of the Twelveswood that worships the primal Ramuh. Yda and Papalymo, who studied them for the Order of the Twin Adder, will help you. "
     "The sylphs seem no longer to summon Ramuh, and winning their favor could ease the primal threat while Gridania fends off Garuda.",
     ["M43a", "M43b", "M43c", "M43h", "M43d", "M43f", "M43e"]),
   P(S[44], None, "main", N_ENV,
     "The Scions hope to win the favor of the sylphs, who worship the primal Ramuh. Commander Vorsaile of the Twin Adder cannot decide whether to strike at Ramuh or leave the sylphs in peace, "
     "so he has asked the Scions to act as an impartial liaison. In the East Shroud, you were told the sylphs have been wary since the Empire came to the Shroud.",
     ["M43f", "M43c", "M44b", "M44a", "M44f"]),
   P(S[45], None, "main", N_ENV,
     "Commander Vorsaile of the Twin Adder has asked the Scions to serve as an impartial liaison to the sylphs, whose ties to the primal Ramuh worry Gridania. "
     "At the Hawthorne Hut, the old beekeeper Rolfe struggled to recall the sylphs' customs, but with help from those he had told his stories, he remembered their traditional greeting: a dance.",
     ["M44a", "M44d", "M45a", "M45b", "M45c"]),
   P(S[46], None, "main", N_ENV,
     "As Gridania's impartial liaison to the sylphs, you are learning their customs from Rolfe, a beekeeper at the Hawthorne Hut. Dancing is their traditional greeting, and they dislike guests who arrive empty-handed. "
     "His wife Rosa named the gift they love, milkroot from an ochu, and you have fetched some.",
     ["M44a", "M45a", "M45c", "M46a", "M46b", "M46c"]),
   P(S[47], None, "main", N_ENV,
     "Carrying milkroot and a letter from the Elder Seedseer vouching for Gridania's envoy, you reached the sylphs of Little Solace and danced their greeting. "
     "Komuxio accepted the gifts but called them a trick and refused you an audience with the elder, and Papalymo thinks recent events have left the sylphs wary.",
     ["M46c", "M47a", "M47b", "M47d", "M47e", "M47f"]),
   P(S[48], None, "main", N_ENV,
     "As envoys for Gridania and the Scions, you are trying to win the trust of the wary sylphs of Little Solace. Komuxio refused you an audience with their elder, "
     "so at Yda's urging you danced for the villagers instead. Your dancing brought smiles to all of Little Solace, though whether it won their hearts remains to be seen.",
     ["M47b", "M47d", "M48a", "M48c", "M48b"]),
   P(S[49], None, "main", N_ENV,
     "Komuxio of Little Solace refused you, Gridania's envoy, an audience with the sylph elder. Papalymo urged you to help the sylphs, who were driven from their woodland home and live in a settlement without defenses. "
     "You cleared the beasts that troubled them, and Komuxio admits he may have been wrong not to trust you.",
     ["M47d", "M49a", "M49b", "M49c", "M49d"]),
   P(S[50], None, "main", N_ENV,
     "The sylphs of Little Solace are slowly warming to you, Gridania's envoy. Komuxio sent you to look into strangers seen in the forest, and you fought off imperial soldiers guarding a cache of supplies. "
     "Their log was written by someone who knows the forest, which suggests a traitor; Komuxio made you promise to stay a friend to the sylphs.",
     ["M49c", "M50a", "M50b", "M50c", "M50d"]),
   P(S[51], None, "main", N_ENV,
     "Komuxio of Little Solace now trusts you without reserve. His friend Claxio had wandered off, fearing the sylphs of Little Solace were forgetting who they are, "
     "and you, Yda and Papalymo saved him from sylphs tempered by Ramuh, who exist only to serve the primal. Whether the sylph elder will be as accepting remains to be seen.",
     ["M51f", "M51a", "M51e", "M51d", "M51b", "M51c"]),
 ],
 "char-vorsaile": [
   P(S[43], None, "main", "Vorsaile",
     "A commander at the Adders' Nest in Gridania, to whom you report before approaching the sylphs. He admits Gridania knows far too little of the sylphs to lay any worthwhile plans.",
     ["M43a", "M43g"], ["Commander Vorsaile"]),
   P(S[44], None, "main", "Vorsaile",
     "A commander of the Order of the Twin Adder at the Adders' Nest in Gridania. Unable to decide whether to strike at the primal Ramuh or leave the sylphs to their ways, "
     "he has asked the Scions to serve as an impartial liaison to them.",
     ["M44d", "M44b", "M44a"], ["Commander Vorsaile"]),
   P(S[52], None, "main", "Vorsaile",
     "A commander of the Order of the Twin Adder at the Adders' Nest, who asked the Scions to act as liaison to the sylphs. "
     "He has agreed to help search for the missing sylph elder, with his Serpents watching night and day, fearing a crisis if the tempered sylphs take him.",
     ["M44a", "M52a", "M52d", "M52c"], ["Commander Vorsaile"]),
   P(S[61], None, "main", "Vorsaile",
     "A commander of the Order of the Twin Adder at the Adders' Nest, who asked the Scions to act as liaison to the sylphs. "
     "The sylph elder's letter has relieved him: the sylphs want no conflict with Gridania and do not intend to summon Ramuh.",
     ["M44a", "M52a", "M61h"], ["Commander Vorsaile"]),
 ],
 "org-sylphs": [
   P(S[43], None, "main", "The sylphs",
     "A beast tribe of the Twelveswood that worships the primal Ramuh. As far as anyone can tell, they no longer summon him. The Scions studied them for the Twin Adder and hope to win their favor.",
     ["M43b", "M43c", "M43d", "M43f"]),
   P(S[47], None, "main", "The sylphs",
     "A beast tribe of the Twelveswood that worships the primal Ramuh. Those of Little Solace accepted Gridania's gifts and your dance, but Komuxio refused you an audience with their elder; "
     "they have grown wary since the Empire came to the Shroud.",
     ["M43b", "M43c", "M47d", "M47f", "M44f"]),
   P(S[49], None, "main", "The sylphs",
     "A beast tribe of the Twelveswood that worships the primal Ramuh. Those of Little Solace were driven from their woodland home and live in a temporary settlement without defenses. "
     "Wary of Gridania's envoys at first, they are slowly warming to you.",
     ["M43b", "M43c", "M49a", "M49b", "M49c"]),
   P(S[51], None, "main", "The sylphs",
     "A beast tribe of the Twelveswood that worships the primal Ramuh. Those of Little Solace were driven from their home and are warming to you. "
     "In the forest, sylphs tempered by Ramuh exist only to serve him, and one of Little Solace's own fled in fear that his people were forgetting who they are.",
     ["M43b", "M49a", "M49c", "M51b", "M51c", "M51e"]),
   P(S[61], None, "main", "The sylphs",
     "A beast tribe of the Twelveswood. Against their elder Frixio's wishes, some summoned Ramuh to protect the wood from imperial soldiers, and all who took part were tempered; "
     "Frixio fled to Little Solace with those who refused. The sylphs want no conflict with Gridania and do not intend to summon Ramuh.",
     ["M43b", "M61b", "M61c", "M61d", "M61h"]),
 ],
 "char-ramuh": [
   P(S[43], None, "main", "Ramuh",
     "A primal worshiped by the sylphs, whose existence is well documented. The sylphs seem no longer to summon him, but the Scions warn it would be unwise to assume the threat has passed.",
     ["M43c", "M43d"]),
   P(S[51], None, "main", "Ramuh",
     "A primal worshiped by the sylphs. Sylphs in the forest have been tempered by him, and like the Amalj'aa tempered by Ifrit, exist only to serve him.",
     ["M43c", "M51b", "M51c"]),
   P(S[61], None, "main", "Ramuh",
     "A primal of the sylphs. Against their elder's wishes, some sylphs summoned him to protect the wood from imperial soldiers, and all who took part were tempered, "
     "fiercely protective of their homeland. The sylphs do not intend to summon him again.",
     ["M61b", "M61c", "M61e", "M61h"]),
 ],
 "char-komuxio": [
   P(S[47], None, "main", "Komuxio",
     "A sylph of Little Solace, to whom Gridania's envoy must bring its letter. He accepted your gifts and dance but called them a trick, and sent you away: the elder has no words for Gridania.",
     ["M47a", "M47d", "M47e"]),
   P(S[49], None, "main", "Komuxio",
     "A sylph of Little Solace, slow to trust Gridania's envoys, who once refused you an audience with the elder. Since you helped his people, he admits he may have been wrong not to trust you.",
     ["M47d", "M49c", "M49d"]),
   P(S[51], None, "main", "Komuxio",
     "A sylph of Little Solace. After you saved his friend Claxio from sylphs tempered by Ramuh, he trusts you without reserve.",
     ["M51a", "M51d", "M51f"]),
   P(S[52], None, "main", "Komuxio",
     "A sylph of Little Solace who trusts you without reserve. He confessed that the elder went into the forest and has not come back, and begged you to seek the Order of the Twin Adder's help.",
     ["M51f", "M52a", "M52b"]),
   P(S[61], None, "main", "Komuxio",
     "A sylph of Little Solace who trusts you without reserve. With the elder Frixio safe, he asked you to observe the tempered sylphs so your word could reassure the Gridanians that they have nothing to fear.",
     ["M51f", "M59i", "M61a"]),
 ],
 # ---- Arc t5: The Missing Elder (#52–#61) ----
 ARC_ELDER: [
   P(S[52], None, "main", N_ELDER,
     "Komuxio confessed that the elder of the sylphs of Little Solace went into the forest and has not come back. Commander Vorsaile, fearing a crisis if the tempered sylphs take him, has his Serpents watching, "
     "and the Wood Wailers have pledged their help. Buscarron, whose tavern in the South Shroud stands near where the elder vanished, will listen for news.",
     ["M52a", "M52b", "M52c", "M52d", "M52e", "M52f", "M52g"]),
   P(S[53], None, "main", N_ELDER,
     "The elder of the sylphs of Little Solace is missing, and the Twin Adder and the Wood Wailers are searching. Buscarron, whose tavern in the South Shroud stands near where the elder vanished, has no news yet. "
     "Meanwhile you cooled a brawl at his door, for he serves any who pay and behave.",
     ["M52a", "M52d", "M52e", "M52g", "M53a", "M53c"]),
   P(S[54], None, "main", N_ELDER,
     ELDER_LEAD + "Buscarron of the South Shroud is listening for news. Meanwhile he had you return an earring to Teteroon, a Qiqirn he found fallen in the Shroud after the Calamity "
     "and nursed back to health, who now trades on Bronze Lake.",
     ["M52a", "M52c", "M52f", "M54a", "M54b", "M54c"]),
   P(S[55], None, "main", N_ELDER,
     ELDER_LEAD + "Buscarron of the South Shroud is listening for news. You found Teteroon, a Qiqirn Buscarron nursed back to health after the Calamity, "
     "and he is brewing firewater to thank the man without whom he would be dead.",
     ["M52a", "M52c", "M52f", "M54a", "M55a", "M55b"]),
   P(S[56], None, "main", N_ELDER,
     ELDER_LEAD + "Buscarron of the South Shroud is listening for news. You brought him firewater from Teteroon, the Qiqirn he once nursed back to health. "
     "He is delighted, though the gift should age a full year.",
     ["M52a", "M52c", "M52f", "M54a", "M56a", "M56b"]),
   P(S[57], None, "main", N_ELDER,
     "Sylphs have been seen in a part of the Twelveswood beyond their lands, and Buscarron thinks the missing elder of Little Solace is likely among them. "
     "Surveying the area for him, you found Garlean soldiers, who had never before reached the forest depths. Buscarron reasons that a Gridanian traitor who knows the Wood Wailers' spires must be guiding them.",
     ["M57a", "M57b", "M57c", "M57e", "M57d"]),
   P(S[58], None, "main", N_ELDER,
     "Searching for the missing sylph elder, you found Garlean soldiers deep in the Twelveswood, guided by a traitor. Buscarron suspected Laurentius, a newly rich Wood Wailer; "
     "after you beat the imperials, Laurentius confessed to selling maps and rations to the Empire and went to give himself up to the Twin Adder. Then Buscarron brought news: the elder has been found.",
     ["M57c", "M57d", "M58a", "M58b", "M58f", "M58c", "M58d", "M58e"]),
   P(S[59], None, "main", N_ELDER,
     "Fleeing Garlean soldiers, Frixio, the elder of the sylphs of Little Solace, went into the Thousand Maws of Toto-Rak; had he come to harm, the hope of peace between man and sylph would have died. "
     "Inside you met the Ascian Lahabrea, who loosed a gigantic banemite on you. You found Frixio shaken but unharmed, and he has agreed to speak with you about Ramuh.",
     ["M59a", "M59d", "M59b", "M59e", "M59i"]),
   P(S[60], None, "main", N_ELDER,
     "You rescued Frixio, elder of the sylphs of Little Solace, from the Thousand Maws of Toto-Rak, and peace between man and sylph is within reach. "
     "Buscarron, who believes the two peoples must stand together now that the Calamity has weakened the elementals, sent the sylphs a peace offering, and it moved them.",
     ["M59a", "M59i", "M59j", "M60a", "M60b", "M60c", "M60d"]),
   P(S[61], None, "main", N_ELDER,
     "Frixio told you that some sylphs summoned Ramuh to protect the wood from imperial soldiers, against his wishes, and that all who took part were tempered; he fled to Little Solace with those who refused. "
     "You watched the tempered sylphs without incident and carried his letter to Commander Vorsaile, who is relieved that the sylphs want no conflict.",
     ["M61b", "M61c", "M61d", "M61a", "M61h"]),
 ],
 "char-frixio": [
   P(S[52], None, "main", "The sylph elder",
     "The elder of the sylphs of Little Solace, who went into the forest and has not come back. Commander Vorsaile fears a crisis if the tempered sylphs take him.",
     ["M52a", "M52b", "M52c"]),
   P(S[57], None, "main", "The sylph elder",
     "The missing elder of the sylphs of Little Solace. Sylphs have been seen in a part of the Twelveswood beyond their lands, and Buscarron thinks the elder is likely among them.",
     ["M52a", "M57a", "M57b"]),
   P(S[58], None, "main", "The sylph elder",
     "The elder of the sylphs of Little Solace, who went missing in the forest. Buscarron has brought news that he has been found.",
     ["M52a", "M58e"]),
   P(S[59], None, "main", "Frixio",
     "The eldest of the sylphs of Little Solace. Fleeing Garlean soldiers, he went into the Thousand Maws of Toto-Rak, where you found him shaken but unharmed, "
     "and he has agreed to speak with you about Ramuh. Had he come to harm, the hope of peace between man and sylph would have died.",
     ["M59d", "M59a", "M59i", "M59b"]),
   P(S[61], None, "main", "Frixio",
     "The eldest of the sylphs of Little Solace. He told you that some sylphs summoned Ramuh against his wishes to protect the wood from imperial soldiers, and that all who took part were tempered; "
     "he fled to Little Solace with those who refused. He gave you a crystal he says will one day be of use, and warned that a crueler fate awaits you than he can imagine.",
     ["M59d", "M61b", "M61c", "M61d", "M61f", "M61g"]),
 ],
 "char-buscarron": [
   P(S[52], None, "main", "Buscarron",
     "Proprietor of Buscarron's Druthers in the South Shroud, near where the sylph elder vanished. He has agreed to listen among his many customers for news of the elder.",
     ["M52h", "M52g", "M52f"]),
   P(S[54], None, "main", "Buscarron",
     "Proprietor of Buscarron's Druthers in the South Shroud, who serves any who pay and stay out of trouble, and is listening for news of the missing sylph elder. "
     "After the Calamity he found the Qiqirn Teteroon fallen in the Shroud and nursed him back to health; Teteroon remembers him fondly.",
     ["M52h", "M52f", "M53c", "M54a", "M54c"]),
   P(S[57], None, "main", "Buscarron",
     "Proprietor of Buscarron's Druthers in the South Shroud, who is helping search for the missing sylph elder. Having found Garlean soldiers deep in the forest, "
     "he reasons that a Gridanian traitor who knows the Wood Wailers' spires must be guiding them.",
     ["M52h", "M52f", "M57c", "M57e"]),
   P(S[60], None, "main", "Buscarron",
     "Proprietor of Buscarron's Druthers in the South Shroud, who helped find the sylph elder and unmask a traitor among the Wood Wailers. "
     "Believing Gridanians and sylphs must work together now that the Calamity has weakened the elementals, he sent the sylphs a peace offering.",
     ["M52h", "M58e", "M58c", "M60b", "M60c", "M60a"]),
 ],
 "char-laurentius": [
   P(S[58], None, "main", "Laurentius",
     "A Wood Wailer whose sudden good fortune roused Buscarron's suspicion. He confessed to selling maps and rations to the Empire, repented, "
     "and has gone to give himself up to the Order of the Twin Adder.",
     ["M58a", "M58b", "M58c", "M58d"]),
 ],
 "org-wood-wailers": [
   P(S[52], None, "main", "The Wood Wailers",
     "Gridanian sentries of the forest, who have pledged their cooperation in the search for the missing sylph elder.",
     ["M52e"]),
   P(S[57], None, "main", "The Wood Wailers",
     "Gridanian sentries who watch the forest from their spires, and are helping search for the missing sylph elder. "
     "Buscarron believes Garlean soldiers slipped past their watch only because a Gridanian traitor guided them.",
     ["M52e", "M57e"]),
   P(S[58], None, "main", "The Wood Wailers",
     "Gridanian sentries who watch the forest from their spires. One of their own, Laurentius, sold maps and rations to the Empire, then repented and gave himself up to the Order of the Twin Adder.",
     ["M57e", "M58b", "M58c", "M58d"]),
 ],
 "char-lahabrea": [
   P(S[59], None, "main", "Lahabrea",
     "An Ascian. In the Thousand Maws of Toto-Rak he set a gigantic banemite upon you, saying that all that stands between this world and Darkness is an irksome anomaly in the aether: the Echo.",
     ["M59e", "M59f"]),
 ],
 "char-noraxia": [
   P(S[59], None, "main", "Noraxia",
     "A sylph who told you that the elder of Little Solace had gone into the Thousand Maws of Toto-Rak and had not returned.",
     ["M59c", "M59d"]),
 ],
})

# ---- Relationships -------------------------------------------------------------------------------------------------
# (id, source, type, target, from, until, scope, claims[, end claims]). Backfills ("-arr") end exactly where a later
# era's relationship of the same triple begins, because that one's claims come after this era.
RELS = [
 ("rel-isembard-aids-scions", "char-isembard", "aids", "org-scions", S[31], None, "main", ["M31f", "M31j"]),
 ("rel-ungust-aids-amaljaa", "char-ungust", "aids", "org-amaljaa", S[37], None, "main", ["M37d", "M37f", "M37e"]),
 ("rel-ifrit-summoned-by-amaljaa", "char-ifrit", "summoned-by", "org-amaljaa", S[40], None, "main", ["M40m"]),
 ("rel-garuda-summoned-ixal-arr", "char-garuda", "summoned-by", "org-ixal", S[40], "cp-msq-110", "main", ["M40h"]),
 ("rel-kan-e-senna-leads-twin-adder", "char-kan-e-senna", "leads", "org-twin-adder", S[40], None, "main", ["M40e"]),
 ("rel-ramuh-summoned-by-sylphs-arr", "char-ramuh", "summoned-by", "org-sylphs", S[43], "cp-msq-192", "main", ["M40y", "M43c"]),
 ("rel-komuxio-member-sylphs", "char-komuxio", "member-of", "org-sylphs", S[47], None, "main", ["M47d", "M47e"]),
 ("rel-frixio-leads-sylphs", "char-frixio", "leads", "org-sylphs", S[52], None, "main", ["M52a", "M52b"]),
 ("rel-vorsaile-member-twin-adder", "char-vorsaile", "member-of", "org-twin-adder", S[52], None, "main", ["M52a", "M52d"]),
 ("rel-buscarron-aids-sylphs", "char-buscarron", "aids", "org-sylphs", S[52], None, "main", ["M52f"]),
 ("rel-laurentius-member-wood-wailers", "char-laurentius", "member-of", "org-wood-wailers", S[58], None, "main", ["M58b"]),
 ("rel-laurentius-turned-against-wood-wailers", "char-laurentius", "turned-against", "org-wood-wailers", S[58], None, "main", ["M58c", "M57e"]),
 ("rel-noraxia-member-sylphs", "char-noraxia", "member-of", "org-sylphs", S[59], None, "main", ["M59c"]),
]

# The accepted relationships whose claims come from quests in this era start where the pages establish them.
ADJUST = {
 "rel-minfilia-leads-scions-arr": {"frm": S[30]},       # C01, The Scions of the Seventh Dawn
 "rel-scions-hq-waking-sands-arr": {"frm": S[30]},      # C02
 "rel-thancred-member-scions-arr": {"frm": S[31]},      # C31, A Wild Rose by Any Other Name
 "rel-yshtola-member-scions-arr": {"frm": S[31]},       # C31, C40
 "rel-urianger-member-scions-arr": {"frm": S[31]},      # C31
 "rel-tataru-member-scions-arr": {"frm": S[31]},        # C32
 "rel-yda-member-scions": {"frm": S[31]},               # C31
 "rel-papalymo-member-scions": {"frm": S[31]},          # C31
 "rel-alphinaud-twin-alisaie": {"frm": S[40]},          # C10, A Hero in the Making
}

# ---- Arcs ----------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-t1-adventurer-of-the-moment", ARC_GUILD, S[25], S[30]),
 ("arc-t2-drybone-vanishings", ARC_DRY, S[31], S[39]),
 ("arc-t3-choosing-a-grand-company", ARC_GC, S[40], S42C),
 ("arc-t4-envoys-to-the-sylphs", ARC_ENV, S[43], S[51]),
 ("arc-t5-the-missing-elder", ARC_ELDER, S[52], S[61]),
]
CASTS = {
 ARC_GUILD: [("char-baderon", S[25], ["M25a"]), ("org-serpent-reavers", S[25], ["M25b"]), ("org-sahagin", S[25], ["M25c"]),
             ("org-adventurers-guild", S[25], ["M25e"]), ("char-miounne", S[26], ["M26a"]), ("org-lambs-of-dalamud", S[27], ["M27a"]),
             ("char-momodi", S[28], ["M28a"]), ("char-minfilia", S[30], ["M30b"]), ("org-scions", S[30], ["C34"])],
 ARC_DRY: [("char-thancred", S[31], ["M31e"]), ("char-isembard", S[31], ["M31f"]), ("org-amaljaa", S[31], ["M31d"]),
           ("char-ifrit", S[31], ["M31d"]), ("char-minfilia", S[31], ["M31b"]), ("char-ungust", S[33], ["M33a"]),
           ("char-ourcen", S[34], ["M34c"]), ("char-marques", S[34], ["M34a"]), ("org-immortal-flames", S[39], ["M39a"])],
 ARC_GC: [("char-alphinaud", S[40], ["C10"]), ("char-alisaie", S[40], ["C10"]), ("char-kan-e-senna", S[40], ["M40e"]),
          ("char-raubahn", S[40], ["M40i"]), ("char-merlwyb", S[40], ["M40w"]), ("org-immortal-flames", S[40], ["M40c"]),
          ("org-maelstrom", S[40], ["M40c"]), ("org-twin-adder", S[40], ["M40c"]), ("char-biggs", S41, ["M41c"]),
          ("char-wedge", S41, ["M41c"])],
 ARC_ENV: [("char-minfilia", S[43], ["M43a"]), ("char-yda", S[43], ["M43h"]), ("char-papalymo", S[43], ["M43h"]),
           ("char-vorsaile", S[43], ["M43a"]), ("org-sylphs", S[43], ["M43b"]), ("char-ramuh", S[43], ["M43c"]),
           ("org-twin-adder", S[43], ["M43b"]), ("char-komuxio", S[47], ["M47d"]), ("org-garlean-empire", S[50], ["M50b"])],
 ARC_ELDER: [("char-frixio", S[52], ["M52a"]), ("char-komuxio", S[52], ["M52a"]), ("char-vorsaile", S[52], ["M52d"]),
             ("org-wood-wailers", S[52], ["M52e"]), ("char-buscarron", S[52], ["M52f"]), ("org-sylphs", S[52], ["M52a"]),
             ("org-garlean-empire", S[57], ["M57c"]), ("char-laurentius", S[58], ["M58c"]), ("char-lahabrea", S[59], ["M59e"]),
             ("char-ramuh", S[59], ["M59i"])],
}
ARC_NOTES = {
 "arc-t1-adventurer-of-the-moment": "MSQ #25 *It's Probably Pirates* to #30 *The Scions of the Seventh Dawn*: the converged Adventurers' Guild jobs in all three "
   "city-states (Sastasha, the Tam-Tara Deepcroft, Copperbell Mines), ending when the Scions take you in (M30b). The name is Momodi's word for you via Miounne (M28c).",
 "arc-t2-drybone-vanishings": "MSQ #31 *A Wild Rose by Any Other Name* to #39 *Lord of the Inferno*: the Scions' first mission, from the caravan robbery and "
   "disappearances to Ifrit's fall (M39d). Its name avoids #39's title, which may not appear before #39.",
 "arc-t3-choosing-a-grand-company": "MSQ #40 *A Hero in the Making* to #42c *Wood's Will Be Done*: the remembrance services and the three mutually exclusive "
   "Grand Company pairs, which run one after another. Each pair's recap names only its own company and cites only its own pages.",
 "arc-t4-envoys-to-the-sylphs": "MSQ #43 *Sylph-management* to #51 *Brotherly Love*: the Scions' liaison to the sylphs of Little Solace, ending when Komuxio "
   "trusts you and the elder is still out of reach (M51f).",
 "arc-t5-the-missing-elder": "MSQ #52 *Spirited Away* to #61 *Believe in Your Sylph*: the search for the elder, Buscarron's errands, the Wood Wailer traitor, "
   "Toto-Rak and the peace with Gridania (M61h). Buscarron's Teteroon errands (#54–#56) stay inside the arc with a shared opening.",
}
DECISIONS = [
 "Each Grand Company pair (#41/#42, #41b/#42b, #41c/#42c) has its own Biggs and Wedge presentations and its own arc recaps, citing only that pair's pages, so no company's player sees another company's rescue as their own.",
 "The Grand Company organizations are described only from #40 and their own pair, never with the player's oath; the company-specific facts appear at the pair's second step (#42, #42b, #42c).",
 "The sylph elder is \"The sylph elder\" from #52 (Komuxio's confession) and Frixio from #59, where the page first names him. No reveal edge and no alias: it is the same person, newly named, and an alias \"the sylph elder\" would make the earlier lowercase mentions read as naming him before he is visible.",
 "The Ixal–Garuda and sylphs–Ramuh edges are backfills (\"-arr\") ending where the later era's own edge begins, because the later edges cite later quests. Raubahn, Merlwyb and the Serpent Reavers already have \"-arr\" backfills from the starting-city modules, so none is repeated here.",
 "Lahabrea and the Ascians appear at #59 (Toto-Rak), well before the accepted #105 text, which introduces him as \"a figure\"; the lead may want to soften #105.",
 "Thancred's #34 remark that he has seen Marques's face before is main dialogue and is kept; it reads as a hint, not a reveal (Cid is not named until #110).",
]
