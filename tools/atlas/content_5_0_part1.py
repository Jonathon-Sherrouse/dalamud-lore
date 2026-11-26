"""Atlas content for patch 5.0, part 1: MSQ #542 The Syrcus Trench to #579 The Lawless Ones, including both parallel
chains from #545 (Alphinaud on Kholusia, #545–#553; Alisaie in Amh Araeng, #545b–#553b) and the three pixie chores at
#570 (#570, #570b, #570c). Arc tag l. Data only (docs/atlas/era-modules.md is the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes B01–B05); every locator is an exact substring of
a quest's Journal, Steps or main dialogue (stage directions inside cutscenes included), never an optional line or a
choice branch. Spoiler rules this module follows:
  - continues the 4.56 records: the voice and the hooded figure (char-enigmatic-figure) are revealed at #542 as the
    Crystal Exarch, who thanks you for answering his summons (Marques -> Cid pattern); he carries "The enigmatic
    figure" as an alias from then on. His true identity is not shown in this era (a choice branch names a candidate;
    it stays out);
  - the girl called Minfilia is a new entity, char-ryne (the id the later 5.0 eras use; ids are never displayed),
    shown as "Minfilia of the First" (after the wiki's "Minfilia (The First)" label) from #565, where she is first named. char-minfilia, the Scions' Minfilia, gains the
    alias "the Oracle of Light" at #565 (Moren and Alisaie tie the two), and at #574 the Minfilia of old speaks through
    the girl, calling her a vessel (possessed-by);
  - "Emet-Selch" stays out: #568 shows the name only as a speaker tag, while its stage directions (#553, #568) name the
    watcher Solus, so the watcher is char-solus;
  - the parallel chains are written so that a record on one chain never cites the other chain's quests; the timeline
    puts #545b–#553b after #553, so records begun on the Alphinaud chain stay visible there, which is unavoidable;
  - quest titles that come later stay out of text (Warrior of Darkness at #564 among them, so #552b and #563 say
    "Warriors of Darkness" or describe the tale); first names only; no surnames (a locator may contain one).
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

(L542, L543, L544, L545, L546, L547, L548, L549, L550, L551, L552, L553) = (f"cp-msq-{n}" for n in range(542, 554))
(L545B, L546B, L547B, L548B, L549B, L550B, L551B, L552B, L553B) = (f"cp-msq-{n}b" for n in range(545, 554))
(L563, L564, L565, L566, L567, L568, L569) = (f"cp-msq-{n}" for n in range(563, 570))
L570, L570B, L570C = "cp-msq-570", "cp-msq-570b", "cp-msq-570c"
(L573, L574, L575, L576, L577, L578, L579) = (f"cp-msq-{n}" for n in range(573, 580))

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #542 The Syrcus Trench
 "M542a": ("A hidden path has opened the hollows at the foot of the Crystal Tower to the search for the beacon.", "The Syrcus Trench", "Apparently, our colleagues have stumbled across a hidden path leading down into the hollows around the base of the Crystal Tower."),
 "M542b": ("Tataru means to wake the sleeping Scions before the Empire comes calling again.", "The Syrcus Trench", "We have to find a way to wake them up─and ''before'' the Empire comes calling again!"),
 "M542c": ("Biggs and Wedge join the search because the Scions asked for aid.", "The Syrcus Trench", "Aye, aye, well we could hardly say no to a call for aid from the Scions."),
 "M542d": ("When you find the beacon, the mysterious voice calls to you clearly and carries you to a distant land.", "The Syrcus Trench", "Having stumbled rather fortuitously on what turns out to be the beacon, you are subject to yet another visitation by the mysterious voice. This time, however, it rings triumphantly clear. Moments later, you find yourself transported to a distant and unfamiliar land."),
 "M542e": ("Tataru bids you find your friends and bring them home.", "The Syrcus Trench", "Safe journey, Warrior of Light. Find our friends, and bring them home!"),
 "M542f": ("A peddler sends you to the Crystarium, the largest settlement for malms around.", "The Syrcus Trench", "'Tis the biggest settlement for malms around. … They'll take good care of you in the Crystarium."),
 "M542g": ("The guard at the Crystarium's gate bars you for refusing to say where you are from.", "The Syrcus Trench", "But instead you chose concealment, and I will not suffer you to pass..."),
 "M542h": ("A hooded man declares you his guest, and the guard captain calls him her lord.", "The Syrcus Trench", "she is interrupted by the arrival of a hooded man who smoothly declares you to be his guest. … Quite all right, my lord."),
 "M542i": ("The hooded man thanks you for answering his summons.", "The Syrcus Trench", "let me first thank you for answering my summons."),
 "M542j": ("He bears the title of Crystal Exarch, as caretaker of the Crystarium.", "The Syrcus Trench", "Having been awarded the rather grandiose title of “Crystal Exarch,” I─in my capacity as caretaker of the Crystarium─thought to seek the aid of you and your companions."),
 "M542k": ("This world is the First, one of the thirteen shards, though its people hardly know it.", "The Syrcus Trench", "The realm in which you now find yourself belongs to one of the thirteen reflections or shards─the First, to be precise─even if its inhabitants are largely oblivious to the fact."),
 "M542l": ("A century ago a luminous flood swallowed more than nine-tenths of the First.", "The Syrcus Trench", "A luminous flood swallowing everything in its path. More than nine-tenths of this star was lost."),
 "M542m": ("The survivors are hounded by abominations called sin eaters.", "The Syrcus Trench", "And the fortunate few who survived are hounded by abominations born of that catastrophe even now. … we call them. The creature you saw earlier was one such monstrosity."),
 "M542n": ("The Exarch learned to bridge worlds to summon the greatest of heroes, taking the Source's champion to save both worlds.", "The Syrcus Trench", "It was to save the First from this menace that I learned to bridge the rift between worlds─that I might call upon the aid of the greatest of heroes. … Though it meant depriving a world of its champion, I had to try─for in saving the First, you would bring salvation to the Source as well."),
 "M542o": ("No dark night has fallen there in over a hundred years.", "The Syrcus Trench", "Over a hundred bleedin' years ago, that's when!"),
 "M542p": ("The guard is the Crystarium's gatekeeper.", "The Syrcus Trench", "This is the threshold of the Crystarium, stranger, and I am its gatekeeper."),
 # #543 City of the First
 "M543a": ("The Exarch sends you to the Crystarium's civic leaders to learn of the world and its plight.", "City of the First", "To that end, I would like you to visit a few of the Crystarium's civic leaders, and glean something of this world and its predicament."),
 "M543b": ("The First's people know nothing of other stars.", "City of the First", "the people of this world are unaware of the existence of other stars, and will struggle to accept the truth of your origin."),
 "M543c": ("They say the Exarch's magicks pulled the Crystal Tower out of thin air.", "City of the First", "They say his grand magicks summoned the Crystal Tower into existence─pulled the entire thing out of thin air."),
 "M543d": ("The eldest swear the Exarch looks just as he did decades ago.", "City of the First", "yet the eldest among us swear the Exarch looks exactly the same as he did back then..."),
 "M543e": ("A century ago, villains called the Warriors of Light slew the Shadowkeeper, the steward of Darkness.", "City of the First", "A hundred years ago─or near enough not to matter─villains known as the Warriors of Light slew the Shadowkeeper, the steward of Darkness."),
 "M543f": ("Light then poured into the world until a great wave swept it: the Flood of Light.", "City of the First", "It pooled and swelled without cease, until the day an enormous, blinding wave rose up and swept across our star. … We called this calamity the “Flood of Light.”"),
 "M543g": ("The Oracle of Light stayed the Flood, sparing Norvrandt alone.", "City of the First", "The Oracle of Light. She stood 'twixt us and approaching doom, and by her power did she stay the Flood. Thus was Norvrandt, and Norvrandt alone, spared the fate of erasure."),
 "M543h": ("The sin eaters are Light incarnate, and stole the night from Norvrandt's sky.", "City of the First", "These “sin eaters” were Light incarnate, and their fulgent presence stole the night from Norvrandt's sky."),
 "M543i": ("The Crystal Tower is the one from the Source, moved whole to the First.", "City of the First", "The structure is, in fact, the selfsame one you know from the Source, transported to the First in its entirety."),
 "M543j": ("The Exarch does not know which era he took the tower from, but its arrival set fate in motion.", "City of the First", "And although I do not know which era I tore it from, I ''do'' know that its arrival served to set the wheels of fate in motion."),
 # #544 Travelers of Norvrandt
 "M544a": ("Your fellow Scions are in the First.", "Travelers of Norvrandt", "To put it simply, they are here in the First..."),
 "M544b": ("Time in the First runs at a different, unpredictable pace from the Source.", "Travelers of Norvrandt", "In the space of a single hour in your home world, an entire year might pass in the First─and the reverse could also be true."),
 "M544c": ("Y'shtola and Urianger have spent three winters in the First, Thancred five.", "Travelers of Norvrandt", "Y'shtola and Urianger have dwelled here for three winters all told, while Thancred's count stands at five."),
 "M544d": ("Alphinaud and Alisaie have lived in the First for almost a year.", "Travelers of Norvrandt", "Even our more “recent” arrivals, Alphinaud and Alisaie, have lived in the First for almost a year."),
 "M544e": ("The Scions there are only spirits that can be seen and touched.", "Travelers of Norvrandt", "Though they may appear to possess corporeal bodies, they are, in truth, merely spirits that one can see and touch."),
 "M544f": ("You can cross between worlds, but the Scions are stranded.", "Travelers of Norvrandt", "Consequently, while you yourself will be able to pass between worlds with relative freedom, they will not."),
 "M544g": ("Urianger foresaw the First rejoined with the Source, bringing the Eighth Umbral Calamity.", "Travelers of Norvrandt", "In his vision of tomorrow, the First was rejoined with the Source... … This collision of worlds brought about the Eighth Umbral Calamity, and the deaths of countless multitudes."),
 "M544h": ("In that vision, Urianger watched you die.", "Travelers of Norvrandt", "Amongst those who perished, Urianger clearly saw the fall of the Scions' mightiest champion. He watched you die."),
 "M544i": ("The Scions established that eliminating the sin eaters will prevent the calamity.", "Travelers of Norvrandt", "it was they who finally established that the elimination of the sin eaters will indeed serve to prevent the calamity."),
 "M544j": ("The Exarch promises to find a way to send your friends home.", "Travelers of Norvrandt", "Meanwhile, I promise I will not rest until I have found a way to help your friends return home."),
 "M544k": ("The Exarch introduces Feo Ul of the pixies, who makes a pact with you.", "Travelers of Norvrandt", "As you heard, that was Feo Ul of the pixies."),
 "M544l": ("The ghost names himself Ardbert, and used an alias in the Source.", "Travelers of Norvrandt", "My real name is Ardbert. I used an alias in the Source."),
 "M544m": ("Ardbert and his comrades caused the Flood after letting the Ascians guide them to the Source.", "Travelers of Norvrandt", "If you recall my tale, it was my comrades and I who caused the Flood. … And so we listened to the Ascians─let them guide us to the Source, and tried to hasten their godsdamned Ardor."),
 "M544n": ("After their defeat, Minfilia heard their pleas and returned their souls to the First.", "Travelers of Norvrandt", "I remember our audience with Minfilia─how she listened to our pleas, and returned our souls to the First."),
 "M544o": ("Minfilia and Ardbert's friends gave all they had left to hold back the Flood, and faded.", "Travelers of Norvrandt", "Minfilia and my friends, they...they surrendered what little they had left to hold it back. Just faded away...leaving me to bear witness."),
 "M544p": ("Ardbert is a shade cursed to drift.", "Travelers of Norvrandt", "I am a shade, cursed to do naught but drift."),
 "M544q": ("Ardbert thinks the world beyond saving.", "Travelers of Norvrandt", "A waste of time. This world is beyond saving─like those who try to save it."),
 "M544r": ("Y'shtola is stationed in the forests of Rak'tika, to the east.", "Travelers of Norvrandt", "To the east lies the once-prosperous civilization of Rak'tika. Y'shtola is stationed there, in the heart of the forest."),
 "M544s": ("Urianger is in the faerie kingdom of Il Mheg, to the north.", "Travelers of Norvrandt", "To the north is the faerie kingdom of Il Mheg. That is where you will find Urianger."),
 "M544t": ("Thancred has a new companion and wanders as a hunter of sin eaters.", "Travelers of Norvrandt", "He has taken up with...a new companion, and is presently engaged as a wandering hunter of sin eaters."),
 "M544u": ("Alphinaud is on the island of Kholusia.", "Travelers of Norvrandt", "Alphinaud is on Kholusia, an island off the western shore."),
 "M544v": ("Alisaie went south to the arid wastes of Amh Araeng.", "Travelers of Norvrandt", "Alisaie, meanwhile, traveled south to the arid wastes of Amh Araeng."),
 "M544w": ("The Exarch meant to summon only you, but his fumbling hand also seized those closest to your fate.", "Travelers of Norvrandt", "My intention had been to summon only you, but the art of reaching across worlds has proven exceedingly difficult to master. Thus it was that my ''fumbling'' hand closed upon those to whom your fate is most closely bound as well."),
 # #545 In Search of Alphinaud
 "M545a": ("The Exarch sends you to Szem Djenmai, the Master of Beasts, to reach Alphinaud.", "In Search of Alphinaud", "Here is a letter of introduction. Present it to Szem Djenmai, the Master of Beasts at Temenos Rookery, and he will take care of you."),
 "M545b": ("Eulmore's elite fancy themselves masters of what remains of the world.", "In Search of Alphinaud", "For years, the Eulmoran elite have fancied themselves the masters of what remains of our broken world."),
 "M545c": ("The Crystarium resists Eulmore's authority, and their relations are strained, though not at war.", "In Search of Alphinaud", "The Crystarium is one among many who resist their heavy-handed authority, and while we are not at war, our relationship with Eulmore is strained at best."),
 "M545d": ("You are advised to hide your ties with the Exarch near Eulmore.", "In Search of Alphinaud", "It may be wise to conceal your ties with the Exarch during your stay here, especially in the vicinity of the city."),
 # #546 A Still Tide
 "M546a": ("Eulmore is richer than all of Norvrandt, while those outside it struggle to survive.", "A Still Tide", "Eulmore's richer than all of Norvrandt put together, but it's a different story for them as live outside the city."),
 "M546b": ("Alphinaud is reunited with you, and has heard the news from the Exarch and Alisaie.", "A Still Tide", "Both the Exarch and Alisaie told me what they knew of events, but I had stubbornly clung on to the hope that all-out war might yet be avoidable..."),
 "M546d": ("A Rejoining requires both worlds to face an existential threat.", "A Still Tide", "But I can tell you the process requires that both worlds─the Source and the First─be facing an existential threat."),
 "M546e": ("Alphinaud believes any solution must be sought in Eulmore, a center of power.", "A Still Tide", "it is nonetheless a center of power and authority. … If any solutions are to be found, I believe our search should begin there."),
 # #547 Open Arms, Closed Gate
 "M547a": ("Alphinaud has not managed to set foot in Eulmore.", "Open Arms, Closed Gate", "you may be lucky enough to see why I have yet to set foot in Eulmore─despite my best efforts to do so..."),
 "M547b": ("A poor man could sooner pass through a needle's eye than Eulmore's gates.", "Open Arms, Closed Gate", "A poor man could sooner pass through the eye of a needle than Eulmore's gates."),
 "M547c": ("Eulmore is known as the city of final pleasures.", "Open Arms, Closed Gate", "It is also known as the “city of final pleasures.”"),
 "M547d": ("Its admission policy has stood two decades, since its current ruler came to power.", "Open Arms, Closed Gate", "They say this policy has been in place for the past two decades, ever since Eulmore's current ruler came into power."),
 "M547e": ("Gatetown's people depend on handouts of meol and believe Eulmore will answer all their woes.", "Open Arms, Closed Gate", "They've become dependent on handouts of meol, and believe Eulmore is the answer to all their woes."),
 # #548 A Fickle Existence
 "M548a": ("Alphinaud has a scheme to get inside Eulmore.", "A Fickle Existence", "I have been working on a scheme to insinuate myself into the city"),
 "M548b": ("Kai-Shirr posed as Alphinaud's lackey, desperate to join his friends in Eulmore.", "A Fickle Existence", "I loaded your lackey up with the goods not long ago. … That's where all my friends are. We made a promise that we'd live together in paradise..."),
 "M548c": ("Alphinaud hands Kai-Shirr his place in a trade with the Ondo.", "A Fickle Existence", "I was to make my deal with the Ondo at the Clave. … I'm giving you a chance, nothing more. What comes of it is entirely up to you."),
 "M548d": ("An artist without a patron was flung into the sea on Lord Vauthry's judgment.", "A Fickle Existence", "I was left penniless and patronless─a grave sin in Lord Vauthry's city. … Little did I know how soon he would grant me my wish! They flung me over the balustrade into the godsdamned ocean!"),
 "M548e": ("No one in Eulmore questions Lord Vauthry's judgments.", "A Fickle Existence", "When Lord Vauthry passes judgment, no one so much as ''blinks,'' let alone argues."),
 "M548f": ("The artist gives Alphinaud his favorite paintbrush.", "A Fickle Existence", "It's my favorite paintbrush."),
 # #549 City of Final Pleasures
 "M549a": ("Alphinaud poses as a painter, with you as his assistant.", "City of Final Pleasures", "he will pose as a painter, and you will play the role of his faithful assistant."),
 "M549b": ("The jongleurs invite you both into Eulmore.", "City of Final Pleasures", "the jongleurs emerge to recruit a new artist, and Alphinaud's act proves sufficiently convincing to earn you both an invitation into Eulmore."),
 "M549c": ("Eulmore's citizens are either free, under Lord Vauthry's favor, or bonded to the free.", "City of Final Pleasures", "There are the “free,” who are blessed with the favor of Lord Vauthry, and the “bonded,” who work in the employ of the free."),
 "M549d": ("You are bonded as painter and assistant to a Mystel couple, the Chais.", "City of Final Pleasures", "You will be joining the ranks of the bonded. … Chai-Nuzz and Dulia-Chai─a Mystel couple whom most refer to as the “Chais.”"),
 # #550 Free to Sightsee
 "M550a": ("A free citizen gives all property to the city on registration.", "Free to Sightsee", "Upon registration, all of our property─financial, intellectual, or otherwise─is given over to the city."),
 "M550b": ("An attendant says Eulmore knows no war or conflict.", "Free to Sightsee", "There is no war here, no conflict... The residents all treat each other with warmth and respect."),
 "M550c": ("Alphinaud sends you to explore the city.", "Free to Sightsee", "Explore the city, top to bottom."),
 "M550d": ("Freedom from earning coin makes the residents content.", "Free to Sightsee", "Being liberated from the concern of earning coin has an almost miraculous effect on people's outlook."),
 # #551 A Taste of Honey
 "M551a": ("Lord Vauthry is said to have been born able to command the sin eaters, so no Eulmoran need fight.", "A Taste of Honey", "They say Lord Vauthry was born with the power to command them—which means no Eulmoran need ever raise a weapon in defense of the city."),
 "M551b": ("About twenty years ago, the old ruler's son took power and the sin eaters grew docile.", "A Taste of Honey", "Things changed for us, oh, around twenty years ago now, when the old ruler's son came to power! … He's got this way with the eaters, you see—turns them docile as house cats."),
 "M551c": ("Eulmore's army suffered grievous losses in its war against the sin eaters.", "A Taste of Honey", "but even our forces saw grievous losses in the war against the sin eaters."),
 # #552 A Blessed Instrument
 "M552a": ("Of the many who enter Eulmore, few are ever seen to leave.", "A Blessed Instrument", "Of the many hopefuls who enter the city, very few are ever seen to leave."),
 "M552b": ("A free citizen will have Lord Vauthry arrange his voiceless singer's ascension.", "A Blessed Instrument", "Then I shall have a word with Lord Vauthry, and arrange for your ascension."),
 "M552c": ("Eulmore holds that sin eaters gather innocent souls into the Celestial paradise.", "A Blessed Instrument", "As all know, the sin eaters exist to devour the sinful. But also do they serve to gather the souls of the innocent, and shepherd them unto the Celestial paradise."),
 "M552d": ("Alphinaud wonders where all the newcomers go.", "A Blessed Instrument", "If so many folk have entered the city over the years, then where do they go...?"),
 # #553 Emergent Splendor
 "M553a": ("Vauthry ordered Kai-Shirr, sentenced for fraud, to leap from the balcony, then to carve an offering from his own flesh.", "Emergent Splendor", "To atone for this crime, I ordered that he fling himself from the balcony. … So─I demanded an offering of flesh! Carved by his own hand, from his own hide!"),
 "M553b": ("Vauthry says the sin eaters must be fed living aether, and that he alone commands them.", "Emergent Splendor", "Sin eaters are part of Eulmore's society. But they must be fed with aether─''living'' aether. … I alone can offer these things, for I alone can command the sin eaters."),
 "M553c": ("Vauthry calls any who oppose him villains to be punished.", "Emergent Splendor", "And thus am I alone the voice of justice─and any who oppose me villains to be punished!"),
 "M553d": ("Alphinaud admits he offered Kai-Shirr a way in without weighing the risks.", "Emergent Splendor", "You were hungry and desperate, and I offered you a solution without once considering the risks inherent in you accepting it."),
 "M553e": ("Kai-Shirr stays in Kholusia to learn to stand on his own.", "Emergent Splendor", "I need to do some thinking─learn how to stand on my own two feet."),
 "M553f": ("Vauthry vows to enslave, torture and kill Alphinaud's party.", "Emergent Splendor", "I'll enslave their minds! I'll─I'll torment them─torture them! Then tear out their hearts!"),
 "M553g": ("Solus eavesdrops on Vauthry's tirade.", "Emergent Splendor", "''Solus zos Galvus eavesdrops.''"),
 "M553h": ("Alphinaud expects few allies in Kholusia against the sin eaters.", "Emergent Splendor", "I've seen enough of the world's self-proclaimed “capital city” to convince me that our battle against the sin eaters will find few allies in Kholusia."),
 "M553i": ("Alphinaud means to speak with the Exarch and chart a new course.", "Emergent Splendor", "Alphinaud declares that it is time to speak with the Exarch, that you might chart a new course."),
 "M553j": ("Vauthry takes Alphinaud's words as an insult.", "Emergent Splendor", "Did...did that little worm just insult me?"),
 # #545b In Search of Alisaie
 "M545ba": ("The Exarch arranges your journey to Amh Araeng to find Alisaie.", "In Search of Alisaie", "the Exarch offers to arrange transportation for the journey to Amh Araeng."),
 "M545bb": ("He hopes to soothe Alisaie's anger at her ill-timed summoning.", "In Search of Alisaie", "and hopefully soothe any lingering anger from her ill-timed summoning─"),
 "M545bc": ("Alisaie is staying at the Inn at Journey's Head.", "In Search of Alisaie", "the Inn at Journey's Head, which is where this Alisaie friend of yours is staying."),
 "M545bd": ("Great swaths of Nabaath Areng, its great city included, were lost to the Light.", "In Search of Alisaie", "Great chunks of Nabaath Areng's lands were lost to the Light, its great city included."),
 "M545be": ("The caravan reaches the town of Mord Souq.", "In Search of Alisaie", "Here we are─Mord Souq! By the blessed shadow, I love this town!"),
 # #546b City of the Mord
 "M546ba": ("Mord Souq has long sheltered those the Flood displaced.", "City of the Mord", "It has long been a refuge for folk displaced by the Flood, so the population is nothing if not diverse."),
 "M546bb": ("Newcomers must observe a custom, and the Exarch paid for your first purchase.", "City of the Mord", "there's a little custom all newcomers are expected to observe... … the Exarch sent a little something to cover this very expense."),
 "M546bc": ("Merchants come from afar to buy the relics the Mord dig up.", "City of the Mord", "Merchants come from malms around to purchase the relics the Mord dig up."),
 "M546bd": ("You honored the custom with a hearty meal.", "City of the Mord", "You honored our custom, and with great relish!"),
 # #547b Working Off the Meal
 "M547ba": ("Tesleen, a carer at the Inn, has come to know Alisaie well since she took up guard duties there.", "Working Off the Meal", "I work as a carer at the Inn, and I've gotten to know Alisaie quite well since she took up guard duties there."),
 "M547bb": ("The caravan master has you collect his purchases from the market.", "Working Off the Meal", "I have a receipt here for some goods that need picking up from the market."),
 "M547bc": ("A misplaced order delays the caravan master.", "Working Off the Meal", "I'll have to drag in my middleman and sort this mess out."),
 # #548b A Desert Crossing
 "M548ba": ("The Inn at Journey's Head is home to the afflicted and a few carers.", "A Desert Crossing", "It's not much, but it's home for the afflicted and a handful of carers."),
 "M548bb": ("Alisaie has been desperate to see you.", "A Desert Crossing", "Alisaie has been desperate to see you, [Forename], so let's get you to her sooner rather than later!"),
 "M548bc": ("The local coyotes prey on folk coming home from the markets.", "A Desert Crossing", "the local coyotes have learned to prey on folk heading home from the markets."),
 "M548bd": ("Tesleen leaves the full explanation to Alisaie.", "A Desert Crossing", "it may be best to have Alisaie give you the full explanation."),
 # #549b Following in Her Footprints
 "M549ba": ("You find Alisaie pursuing a fleeing sin eater.", "Following in Her Footprints", "you witness Alisaie leaping off a nearby building in pursuit of a fleeing sin eater."),
 "M549bb": ("A colossal wave of Light drowned the world, sparing only Norvrandt.", "Following in Her Footprints", "A colossal wave of pure Light, drowning everything in its wake. Only Norvrandt was spared."),
 "M549bc": ("Sin eaters were once living creatures, or people, caught in the Flood.", "Following in Her Footprints", "They were once living creatures─or people─that were caught in the path of the Flood."),
 "M549bd": ("The stronger sin eaters plant Light in people, and the Inn's infirmary is full of their victims.", "Following in Her Footprints", "The stronger sin eaters can plant Light in us like seeds in soil, corrupting our aether, and triggering the birth of new monstrosities. … The infirmary is full of the sin eaters' victims, left here to spend their final hours waiting for the change to overtake them..."),
 "M549be": ("The afflicted are feared.", "Following in Her Footprints", "And to add insult to injury, the afflicted are feared."),
 "M549bf": ("Alisaie does not doubt Urianger's vision.", "Following in Her Footprints", "I do not doubt for one moment that he saw what he claims."),
 # #550b Culling Their Ranks
 "M550ba": ("Lesser sin eaters flock to the strongest of their kind.", "Culling Their Ranks", "they have an unfortunate tendency to flock to the strongest of their kind."),
 "M550bb": ("The patrols cull them so their numbers stay manageable.", "Culling Their Ranks", "to cull their ranks often enough that their numbers won't be overwhelming when the big ones come out to play."),
 "M550bc": ("Tesleen says Alisaie has badly missed you.", "Culling Their Ranks", "You have no idea how badly Alisaie has missed your company!"),
 # #551b A Purchase of Fruit
 "M551ba": ("The Light left the land beyond Mord Souq an empty white nothingness.", "A Purchase of Fruit", "That's what the land became after the Light flooded in. An empty white nothingness."),
 "M551bb": ("Every one of the Inn's patients will turn, sooner or later.", "A Purchase of Fruit", "Sooner or later, every single one of them will turn."),
 "M551bc": ("The carers mix poison into a patient's favorite food.", "A Purchase of Fruit", "The preferred method is mixing poison into their favorite food."),
 "M551bd": ("The nectarine you bought is Halric's favorite fruit.", "A Purchase of Fruit", "That nectarine you bought...it's Halric's favorite fruit."),
 # #552b The Time Left to Us
 "M552ba": ("Halric goes missing from the Inn.", "The Time Left to Us", "a frantic carer rushes up to report that Halric has gone missing..."),
 "M552bb": ("Tesleen sacrifices herself to save the boy.", "The Time Left to Us", "Alas, you arrive too late to prevent Tesleen from sacrificing herself to save the boy"),
 "M552bc": ("Tesleen came to the Inn with her mother, who was showing the early signs.", "The Time Left to Us", "I remember when I first came here with my mother. She was showing the early signs..."),
 "M552bd": ("Tesleen wishes the folk tale's warrior of darkness would end her patients' lives for her.", "The Time Left to Us", "I often find myself wishing the Warrior of Darkness would come and do that part for me."),
 "M552be": ("Tesleen turns into a sin eater and flies off.", "The Time Left to Us", "Tesleen emerges from the cocoon as a sin eater."),
 "M552bf": ("With no body left, the carers cannot bury her.", "The Time Left to Us", "Without a body, we can't even give her a proper burial!"),
 "M552bg": ("Those who come to the Inn wait for the mercy of a painless death.", "The Time Left to Us", "Beaten, broken souls come to wait out the inevitable. To receive the mercy of a painless death."),
 # #553b Tears on the Sand
 "M553ba": ("Alisaie gives up her role at the Inn.", "Tears on the Sand", "I'm sorry, but I've come to a decision: I won't be continuing in my role here."),
 "M553bb": ("She will use the skills she gained there to hurt the sin eaters.", "Tears on the Sand", "I may not be able to repel the eaters on my own...but I can still use the skills I have gained here to hurt them."),
 "M553bc": ("Alisaie rides for the Crystarium at once.", "Tears on the Sand", "Your swiftest amaro! I need to return to the Crystarium─immediately!"),
 "M553bd": ("She means to plan with the Exarch how to wipe out the sin eaters.", "Tears on the Sand", "We need to talk about how we're going to wipe the sin eaters out."),
 "M553be": ("Alisaie asks the carers to delay Halric's last meal as long as they can.", "Tears on the Sand", "that you will delay Halric's last meal for as long as you possibly can."),
 # #563 The Lightwardens
 "M563a": ("Sin eaters serve the strongest of their kind, the few Lightwardens.", "The Lightwardens", "Sin eaters are drawn to serve the strongest of their kind─a class of creature we call “Lightwardens.” And from what we have been able to ascertain, only a handful of these entities exist."),
 "M563b": ("A Lightwarden's death should scatter the lesser eaters around it.", "The Lightwardens", "we believe that the death of a Lightwarden will cause the lesser creatures within its sphere of influence to disperse."),
 "M563c": ("Vauthry's command over the sin eaters keeps Eulmore safe and obedient.", "The Lightwardens", "Vauthry's command over the sin eaters is integral to Eulmoran society. In seeming to guarantee his people's safety, it guarantees their obedience."),
 "M563d": ("A single star was divided into fourteen worlds: the Source and thirteen shards, the First among them.", "The Lightwardens", "In the ancient past, a single star was divided into fourteen worlds. … This is the Source─your home. These others are the thirteen shards, in whose number we find the First."),
 "M563e": ("Seven times a calamity has struck the Source and a shard been absorbed.", "The Lightwardens", "Seven times has a calamity befallen the Source; seven times has a shard been absorbed."),
 "M563f": ("The Light-drowned First is close to the conditions for a Rejoining.", "The Lightwardens", "At present, the Light-drowned realm of the First stands perilously close to meeting the conditions for a Rejoining."),
 "M563g": ("The Lightwardens' Light banishes night even from Norvrandt.", "The Lightwardens", "Even here in the Flood-spared region of Norvrandt, their influence is strong enough to banish night from the sky."),
 "M563h": ("Every Lightwarden must be put to the sword.", "The Lightwardens", "it is imperative that we put each and every Lightwarden to the sword."),
 "M563i": ("Sin eaters attack Holminster Switch in force.", "The Lightwardens", "They say the sin eaters are attacking in force, and the village could soon be overrun."),
 "M563j": ("A slain Warden's aether turns the nearest living being into a new Warden.", "The Lightwardens", "Vile aether will billow outwards and envelop the nearest living being─a reckless young swordswoman, perhaps─and turn her into a brand-new Warden."),
 "M563k": ("You absorb the slain Warden's energy without ill effect.", "The Lightwardens", "as you absorb the energy it releases without apparent ill effect."),
 "M563l": ("With the Lightwarden of Lakeland slain, night returns for the first time in a century.", "The Lightwardens", "You have vanquished the Lightwarden of Lakeland, and for the first time in a century darkness has returned to the mantle of night."),
 "M563m": ("The crowd cries that the Warrior of Darkness has come.", "The Lightwardens", "The Warrior of Darkness has come!"),
 "M563n": ("The Exarch concedes it was wrong to summon you against your will, and swears to atone.", "The Lightwardens", "I concede it was wrong of me to summon you to this fight against your will. … I swear on my life, I will one day atone for that deed."),
 "M563o": ("The Exarch calls himself an old man burdened with painful memories.", "The Lightwardens", "Despite appearances, I am an old man─one burdened with many...difficult memories, some too painful to recall."),
 "M563p": ("The Exarch calls you and the twins his Warriors of Darkness.", "The Lightwardens", "Come then, my Warriors of Darkness"),
 # #564 Warrior of Darkness
 "M564a": ("The Exarch asks you to keep your part in the Lightwarden's death hidden for now.", "Warrior of Darkness", "Would you be so kind as to conceal your involvement in this endeavor for the time being?"),
 "M564c": ("Lyna expects to be told the whole truth one day.", "Warrior of Darkness", "...Although I expect to be told the whole truth of it one day. About all of you."),
 "M564d": ("Alisaie stays in Holminster Switch, saying she knew one of the eaters.", "Warrior of Darkness", "I ''knew'' one of those eaters, and I can't just... I can't rest, not now."),
 "M564e": ("Rumor says the Warrior of Darkness destroyed a Lightwarden.", "Warrior of Darkness", "They say a Lightwarden was destroyed without a damn trace, and it was the Warrior of Darkness who did the deed!"),
 "M564g": ("Ardbert says it is your lot's turn to be the Warriors of Darkness.", "Warrior of Darkness", "So it's your lot's turn to be the Warriors of Darkness, is it?"),
 "M564h": ("Ardbert remembers the twins from his band's battle in the Source.", "Warrior of Darkness", "Those white-haired twins who were with you... I remember them from our battle in the Source."),
 "M564j": ("Estinien was tracked down and conscripted by the Scions.", "Warrior of Darkness", "Through no choice of my own. They tracked me down, and conscripted me to their cause."),
 "M564k": ("Estinien is to root out the Empire's new weapon.", "Warrior of Darkness", "Thus it has fallen to me to root out any trace of the Empire's new weapon."),
 "M564l": ("Gaius's people destroyed a Black Rose factory, but the Empire has built more.", "Warrior of Darkness", "If it is Black Rose you seek, you are too late. My people have already completed your mission here. … Yet this is but one factory among many."),
 "M564m": ("Black Rose brings the flow of aether in living beings to a standstill.", "Warrior of Darkness", "It was created to disrupt the aether in living beings─to bring the flow of their life energies to a standstill."),
 "M564n": ("Gaius invites Estinien to join him.", "Warrior of Darkness", "Since it would seem we seek the same answers...you are welcome to join us."),
 "M564o": ("Gaius means to return to Garlemald.", "Warrior of Darkness", "Thus I would return to the capital, that I might behold the truth of this corruption with my own eyes. … My path leads to Garlemald."),
 # #565 An Unwelcome Guest
 "M565a": ("Angered by a Lightwarden's death, Eulmore sends its army's commander, General Ran'jit, to the Exarch.", "An Unwelcome Guest", "Angered by the death of a Lightwarden, Eulmore has sent the commander of its army, the formidable General Ran'jit, to demand answers of the Exarch."),
 "M565b": ("Ran'jit threatens the Crystarium with retribution if it abetted the Lightwarden's killers.", "An Unwelcome Guest", "Should it transpire that the Crystarium is guilty of abetting the villains responsible for this outrage... … My lord has decreed that it suffer the same...retribution."),
 "M565c": ("The Exarch says the Crystarium rejoices in the Lightwarden's death.", "An Unwelcome Guest", "Regardless of who is responsible, the Crystarium ''rejoices'' in the Lightwarden's death, and welcomes the return of the night sky."),
 "M565d": ("Ran'jit is searching for a young artist and his assistant.", "An Unwelcome Guest", "We are searching for a young artist and his assistant."),
 "M565e": ("Ran'jit has led Eulmore's army since before Vauthry's time.", "An Unwelcome Guest", "He is a warrior of fearsome repute who has led Eulmore's army since before Vauthry's time, when the nation still spearheaded the fight against the sin eaters."),
 "M565f": ("Ran'jit reports to Lord Vauthry.", "An Unwelcome Guest", "I shall relay your words to Lord Vauthry."),
 "M565g": ("Eulmore's forces at Laxan Loft have taken prisoner a young woman believed to be the Oracle of Light, Minfilia.", "An Unwelcome Guest", "A young woman believed to be none other than the Oracle of Light─Minfilia."),
 "M565h": ("Ran'jit has mentored generations of Minfilias.", "An Unwelcome Guest", "Having mentored generations of Minfilias, it would not surprise me if he had made her capture his chief concern."),
 "M565i": ("The maiden who halted the Flood was named Minfilia, and came to be revered as the Oracle of Light.", "An Unwelcome Guest", "Naught was known about her save that her name was Minfilia. And for delivering the realm, she came to be revered as the Oracle of Light."),
 "M565j": ("Girls believed to be her reincarnations were called by her name and fought the sin eaters for Eulmore's army.", "An Unwelcome Guest", "Believed to be reincarnations of the original Minfilia, they came to be called by her name, and brought their powers to bear against the sin eaters as soldiers of the Eulmoran Army."),
 "M565k": ("The reborn Oracle does not inherit her predecessors' memories.", "An Unwelcome Guest", "Though the Oracle is reborn with certain common traits, she does not inherit the memories or the knowledge of her previous incarnations."),
 "M565l": ("Eulmore's army found the current Minfilia ten years ago and kept her a prisoner in all but name.", "An Unwelcome Guest", "She was found by the Eulmoran Army some ten years ago and taken into their care. … She was a prisoner in all but name."),
 "M565m": ("Under Vauthry, Eulmore abandoned resistance for decadence.", "An Unwelcome Guest", "For by that time, under Lord Vauthry's rule, Eulmore had already abandoned resistance in favor of decadence."),
 "M565n": ("Three years ago, someone stole into Eulmore and rescued her.", "An Unwelcome Guest", "But then, three years ago, a gallant soul stole into the city and rescued her from their clutches!"),
 "M565o": ("Her rescuer was Thancred, and the two have wandered together since.", "An Unwelcome Guest", "As you will have already surmised, the gallant soul who rescued Minfilia was none other than our own dear Thancred. … They have since been wandering the land together, never remaining in one place for long"),
 "M565p": ("Alisaie says the original Oracle of Light was the Minfilia they knew, Hydaelyn's emissary.", "An Unwelcome Guest", "We know that Minfilia journeyed here as Hydaelyn's emissary to halt the Flood of Light. … It could only be her that the people of the First witnessed a hundred years ago. The original Oracle of Light."),
 "M565q": ("Since the girls lack her memories, Alisaie thinks they are not the same person.", "An Unwelcome Guest", "the fact that these girls do not share her memories must surely mean they are not the same person."),
 "M565r": ("Minfilia is held at Laxan Loft, and the Exarch asks that the Crystarium lead her rescue.", "An Unwelcome Guest", "Our scouts have confirmed that the Eulmoran forces at Laxan Loft do indeed have Minfilia in their custody. … I ask that you entrust this undertaking to us, the people of the Crystarium."),
 "M565s": ("Eulmore has ever wanted to rule what remains of the world.", "An Unwelcome Guest", "Eulmore has ever yearned to rule over what remains of the world."),
 # #566 The Crystarium's Resolve
 "M566a": ("Ran'jit warned of war if the Crystarium sides with the Warrior of Darkness.", "The Crystarium's Resolve", "should the Crystarium cast its lot with the Warrior of Darkness, there would be war."),
 "M566b": ("The Crystarium's leaders resolve to rescue the Oracle as their answer to Eulmore's ultimatum.", "The Crystarium's Resolve", "So I move that we rescue the Oracle, grant her a place among us, and let ''that'' be our answer to Eulmore's ultimatum!"),
 "M566c": ("If Eulmore calls them villains, the Crystarium will embrace villainy.", "The Crystarium's Resolve", "If Eulmore wishes to denounce us as villains, then we shall embrace our villainy."),
 "M566d": ("Eulmore fears the power she holds over the sin eaters.", "The Crystarium's Resolve", "They fear the power she holds over the sin eaters, and doubtless intend to imprison her once more."),
 "M566e": ("Lyna plans to fill the skies with amaro and scatter dream powder over the enemy.", "The Crystarium's Resolve", "we begin by deploying amaro to occupy the skies over Lakeland. They should serve to delay the airship's departure. … At the same time, we scatter dream powder from the air."),
 "M566f": ("You join the guard under Captain Lyna.", "The Crystarium's Resolve", "If excitement is your desire, then I bid you join the guard. Captain Lyna will give you your orders."),
 "M566g": ("The Oracle's safe liberation is the raid's sole objective.", "The Crystarium's Resolve", "Her safe liberation is our sole objective; engagement is to be avoided wherever possible."),
 # #567 Logistics of War
 "M567a": ("The Ostall Imperative is one of the Crystarium's key strongholds in Lakeland.", "Logistics of War", "I bid you welcome to the Ostall Imperative, one of our key strongholds in Lakeland."),
 "M567b": ("You delivered an amaro to Lyna's post.", "Logistics of War", "So, it seems that rather than the amaro delivering you, you delivered the amaro."),
 # #568 The Oracle of Light
 "M568a": ("At Lyna's command you descend on Laxan Loft to rescue Minfilia.", "The Oracle of Light", "At Lyna's command, you mount your amaro and descend on the stronghold to rescue Minfilia."),
 "M568b": ("Minfilia refuses to go back to her cell.", "The Oracle of Light", "N-No! I won't go back to that cell!"),
 "M568c": ("Ran'jit overpowers you, until Thancred arrives.", "The Oracle of Light", "You make your way through Laxan Loft and succeed in finding Minfilia, only to find your path barred by General Ran'jit, who effortlessly overpowers you. Just when it seems twisted Eulmoran justice is to be your fate, help arrives in the form of Thancred."),
 "M568d": ("Ran'jit knows Thancred for the one who stole the Oracle from Eulmore.", "The Oracle of Light", "So! ''You'' are the wretch who stole her from us..."),
 "M568e": ("Ran'jit says you resemble the artist his master seeks.", "The Oracle of Light", "You bear a striking resemblance to the artist my master seeks."),
 "M568f": ("The Exarch halts Ran'jit and tells him his quarry goes to the faerie kingdom of Il Mheg.", "The Oracle of Light", "For your quarry goes to a place where even Eulmore dare not bare its steel... … Il Mheg, the faerie kingdom."),
 "M568g": ("Solus, watching from afar, wonders how the Exarch brought the hero of the Source to the First.", "The Oracle of Light", "''Solus zos Galvus observes from afar.'' … How did the so-called Crystal Exarch bring the hero of the Source to the First?"),
 "M568h": ("The watcher says his plan has gone awry.", "The Oracle of Light", "And now the plan has gone awry."),
 "M568i": ("Il Mheg was once the kingdom of Voeburt, which the sin eaters destroyed; fae folk now dwell there.", "The Oracle of Light", "Not so long ago, here in the shadow of the northern ranges, lay the great kingdom of Voeburt. … Since that time, these lands have become a haven for fae folk."),
 "M568j": ("Thancred and the girl Minfilia traveled together hunting sin eaters.", "The Oracle of Light", "The girl, Minfilia. She and I were traveling together, hunting sin eaters."),
 "M568k": ("Near Lakeland she ran off alone, and the Eulmorans took her.", "The Oracle of Light", "But as we were nearing Lakeland, she abruptly ran off on her own. … I found her too late to stop the Eulmorans from taking her prisoner."),
 "M568l": ("The Exarch bids them meet Urianger and slay Il Mheg's Lightwarden.", "The Oracle of Light", "First, rendezvous with Urianger. … And second, eliminate the Lightwarden of this land."),
 "M568m": ("Minfilia ran toward a presence she felt: someone she was meant to meet, you.", "The Oracle of Light", "You. The hero from another world. … I was asleep when I felt it. A presence. Someone I was meant to meet."),
 "M568n": ("The pixies of Il Mheg trick all trespassers with powerful illusions.", "The Oracle of Light", "The most prominent among them are the pixies, who have a penchant for making mischief. They use powerful illusions to play tricks on all who venture into their domain."),
 # #569 Il Mheg, the Faerie Kingdom
 "M569b": ("Minfilia has been told of the Scions' situation.", "Il Mheg, the Faerie Kingdom", "Oh, and I should mention that Minfilia has been informed of our situation."),
 "M569c": ("With looking grass, the hidden pixies are found out.", "Il Mheg, the Faerie Kingdom", "Nooo, we are found! How did this mortal know our trick!?"),
 "M569d": ("Urianger won his place in Il Mheg with a seven-day riddle contest.", "Il Mheg, the Faerie Kingdom", "In return for a place in Il Mheg, he agreed to a riddle contest with us! For seven days and seven nights! Without any sleep!"),
 "M569e": ("The pixies will let you see Urianger only once you have solved their troubles.", "Il Mheg, the Faerie Kingdom", "Once you've helped solve all of our troubles, we'll let you see Urianger."),
 "M569f": ("Thancred suggests splitting up to do the pixies' chores.", "Il Mheg, the Faerie Kingdom", "Well, there you have it. Pixie chores. I suggest we split up."),
 # #570 Sul Uin's Request
 "M570a": ("The pixies' village, Lydha Lran, means flower house.", "Sul Uin's Request", "which means “flower house,” in case you weren't aware."),
 "M570b": ("A mortal city called Voeburt stood there until the sin eaters came.", "Sul Uin's Request", "There used to be a city of mortals here. A great big, bustling place called Voeburt or Boevurt or some such. … But the sin eaters came and everyone disappeared."),
 "M570c": ("The pixies once lived in a lush forest that the light swallowed.", "Sul Uin's Request", "We used to live deep in a lush forest. It was beautiful beyond compare, but almost all of it was swallowed up by the light."),
 "M570d": ("A pixie has you sow everbloom seeds around the village.", "Sul Uin's Request", "So, here are some everbloom seeds. Take them and sow them here, there, and everywhere around the village."),
 # #570b Ys Iala's Errand
 "M570ba": ("Pixies take nothing as seriously as having fun.", "Ys Iala's Errand", "If there's one thing we pixies are serious about, it's having fun!"),
 "M570bb": ("Pixies hate sin eaters, which are dull and painful.", "Ys Iala's Errand", "Sin eaters are dull and painful both, so we hate them especially!"),
 "M570bc": ("A hungry pixie sends you to shake fruit from two belltrees.", "Ys Iala's Errand", "Just outside the village, you'll find a hillock. Two great belltrees grow there."),
 # #570c Oul Sigun's Plea
 "M570ca": ("The Fuath live in the lake and play rough.", "Oul Sigun's Plea", "Oh, but be warned: the Fuath make their home in the lake. They tend to play rough, so have care!"),
 "M570cb": ("The faeries' leafmen were mortals; they tried to enchant you too, but it did not catch.", "Oul Sigun's Plea", "You and yours would've been our children too, but the enchantment didn't catch as well as we'd hoped."),
 "M570cc": ("You water the leafmen, the faeries' children.", "Oul Sigun's Plea", "You've given water to our children? Thank you ever so much!"),
 # #573 Unto the Truth
 "M573a": ("The pixies will never be satisfied enough to let you go.", "Unto the Truth", "After being subjected to a host of menial tasks and pranks, you and your comrades conclude that the pixies will never be satisfied and let you leave."),
 "M573b": ("Pixies are believed to be born from the souls of those who died as children.", "Unto the Truth", "They're born from the souls of those who died as children, or so it's believed."),
 "M573c": ("Feo Ul is won over and coerces the other pixies into letting you go.", "Unto the Truth", "You succeed in winning over Feo Ul, who promptly coerces the other pixies into letting you go."),
 "M573d": ("Feo Ul claims you as theirs alone.", "Unto the Truth", "Now, let me make something clear: that mortal is ''mine''!"),
 "M573e": ("Urianger lives in an abandoned manor called the Bookman's Shelves.", "Unto the Truth", "Thancred informs you that Urianger has taken up residence in the abandoned manor of a nobleman and scholar: a place known as the Bookman's Shelves."),
 "M573f": ("In Urianger's vision, the Garleans facing defeat turn to Black Rose.", "Unto the Truth", "Faced with defeat, the Garleans turned to a weapon most vile─Black Rose."),
 "M573g": ("The gas wreaks carnage across Eorzea and the Empire alike.", "Unto the Truth", "Once released, the gas took on a life of its own, wreaking untold carnage not only in Eorzea, but in the provinces of the Empire besides."),
 "M573h": ("The weapon spares no one, not even you.", "Unto the Truth", "For the weapon spared not one. Not even thee."),
 "M573i": ("Light, the power of stasis, flows in from the First and thins the Source's aether.", "Unto the Truth", "The phenomenon of aetheric thinning observed in the Source is the consequence of Light─the power of stasis─flowing in from the First"),
 "M573k": ("The surge of Light in the First will amplify Black Rose into the Eighth Umbral Calamity.", "Unto the Truth", "the surge of light in the First will amplify the potency of the alchemical weapon Black Rose, thereby giving rise to the Eighth Umbral Calamity in the Source."),
 "M573l": ("Il Mheg's Lightwarden is almost surely in Lyhe Ghiah, the castle in the lake, and the pixies' aid is needed to enter.", "Unto the Truth", "'Tis all but certainly ensconced within Lyhe Ghiah, the castle which standeth in the midst of the lake. … To enter said stronghold, we must needs turn to the pixies for aid."),
 "M573m": ("Urianger will go with you to keep his vision from coming to pass.", "Unto the Truth", "Henceforth shall I accompany you, and do all in my power to ensure that my vision doth not come to pass."),
 "M573n": ("To forestall tragedy in both worlds, every Lightwarden must be eliminated.", "Unto the Truth", "to forestall tragedy in both worlds, you must eliminate all of the Lightwardens."),
 # #574 Courting Cooperation
 "M574a": ("Thwarting a Rejoining will set the Scions against those who crave one: their eternal enemies.", "Courting Cooperation", "Our mission being to thwart a Rejoining, we will most assuredly cross paths with those who crave the contrary. Our eternal enemies."),
 "M574b": ("Urianger stays in aether-rich Il Mheg to build a trap for the Ascians' essence.", "Courting Cooperation", "Thus did I choose to abide in this aether-rich land, the better to fashion a trap for the Ascians' essence."),
 "M574c": ("Thancred cannot manipulate aether, his body being left in the Source.", "Courting Cooperation", "Though my body remained behind in the Source, its limitations saw fit to accompany me. Which is to say, I cannot manipulate aether."),
 "M574d": ("Minfilia has a talent for imbuing Thancred's ammunition.", "Courting Cooperation", "Luckily for me, Minfilia has quite a talent for it."),
 "M574e": ("Thancred freed young Minfilia from captivity in Eulmore three years ago.", "Courting Cooperation", "As you know, I freed young Minfilia from captivity in Eulmore some three years past."),
 "M574f": ("At the edge of the Empty, the Minfilia of old awoke within the girl.", "Courting Cooperation", "To the edge of the Empty, where the Flood was halted. … 'Twas there that she awakened. The Minfilia of old. My Minfilia..."),
 "M574g": ("The Oracle called herself no different from an Ascian, and the girl only a vessel.", "Courting Cooperation", "As I am now, I am no different from an Ascian. This child is but a vessel."),
 "M574h": ("She has used many vessels, each of whom died without living her own life.", "Courting Cooperation", "One of many I have used, that I might spread word of Her enduring blessing and preserve the flame of hope. … In my name, each has died never having lived her own life."),
 "M574i": ("Should the girl choose to master her own destiny, the Oracle will bequeath her all.", "Courting Cooperation", "But should she wish instead to become the master of her own destiny... … Then shall I bequeath to her my all."),
 "M574j": ("She asked Thancred to protect and teach the girl.", "Courting Cooperation", "Now I ask that you do the same for her. Protect her. Teach her. Stand by her as you stood by me."),
 "M574k": ("The girl remembers none of it, and Thancred has never spoken of that day.", "Courting Cooperation", "Minfilia─the girl─claims to have no recollection of any of it. … But of that day, I have not spoken."),
 "M574l": ("Urianger asks who will take up the flame of hope Minfilia has borne.", "Courting Cooperation", "Who shall take up the flame of hope which Minfilia hath borne for so long? Whether we will it or no, the choice must soon be made."),
 "M574m": ("The pixies are delighted with your gifts and will return the kindness.", "Courting Cooperation", "You've done us a great kindness, and it's fae custom to return the gesture."),
 # #575 The Key to the Castle
 "M575a": ("Il Mheg's Lightwarden is the faeries' king and ruler, Titania.", "The Key to the Castle", "...Is our king and ruler, Titania."),
 "M575b": ("Titania fought and beat the first Lightwarden to threaten Il Mheg, and its light corrupted them into a new one.", "The Key to the Castle", "Our king fought the first Lightwarden that threatened our home, you see. Fought it, and won. … But all the horrible light that came out went and corrupted them, turning them into a new Lightwarden."),
 "M575c": ("Nothing remains of the wise ruler, and the fae sealed Titania in the castle.", "The Key to the Castle", "Naught remains of the wise and just ruler that used to be. We had no choice but to seal them in the castle."),
 "M575d": ("The magick to break the seal was split among four relics.", "The Key to the Castle", "The magick for breaking the seal, we divided into four, and wove each into a different relic"),
 "M575e": ("The pixies give you a dress; the Fuath, Nu Mou and amaro hold the other relics.", "The Key to the Castle", "And this dress is one of them. … The shell crown is with the Fuath, the stone scepter is with the Nu Mou, and the crystal shoes are with the amaro."),
 "M575f": ("The Fuath will give the shell crown for thrilling sport.", "The Key to the Castle", "Give us thrilling sport. And we will give you the crown!"),
 "M575g": ("Having given up the crown, the Fuath try to keep you.", "The Key to the Castle", "You may have the crown...but in exchange, we will have ''you''!"),
 "M575h": ("Ardbert wakes you beneath the lake; the Fuath are said to be born of the drowned.", "The Key to the Castle", "Wake up! Wake up, damn you! … It's said that they are born from the souls of the drowned."),
 "M575i": ("Voeburt's royal capital lies under the lake, its people long dead.", "The Key to the Castle", "That's the royal capital of the Kingdom of Voeburt down there. … All dead and buried now. Them and anyone else who might remember."),
 "M575j": ("Ardbert wonders what all he and his friends gave was for.", "The Key to the Castle", "Everything we did...everything we ''gave''... What was it for?"),
 "M575k": ("Armed men, likely the Eulmoran Army, are closing on Il Mheg.", "The Key to the Castle", "armed men are drawing close to Il Mheg─the Eulmoran Army in all likelihood."),
 "M575l": ("Alphinaud and Alisaie go to meet the army, leaving the relic hunt to you.", "The Key to the Castle", "I'm afraid we must leave the rest of the relic hunt in your hands."),
 # #576 A Visit to the Nu Mou
 "M576a": ("The Nu Mou are the fae friendliest to men, and have served Urianger.", "A Visit to the Nu Mou", "They are also the friendliest to men, and have served me faithfully whensoever I have called upon them."),
 "M576b": ("Voeburt was drowned only when the Fuath came after the Flood.", "A Visit to the Nu Mou", "'Twas only when the Fuath came, in the wake of the Flood, that the settlement was drowned."),
 "M576c": ("Urianger brought together the Warriors of Darkness and Minfilia.", "A Visit to the Nu Mou", "'Twas these hands which brought together the Warriors of Darkness and Minfilia, lest thou forget."),
 "M576d": ("Many Nu Mou laid down their lives to seal their light-corrupted king.", "A Visit to the Nu Mou", "Thus did full many of us lay down our lives to seal away our king when they were corrupted by light!"),
 "M576e": ("The Nu Mou have been starved of patronage since Voeburt fell.", "A Visit to the Nu Mou", "Since the Kingdom of Voeburt fell, however, we've been starved of man's patronage."),
 "M576f": ("The elder asks you to stay and be the Nu Mou's patron while they decide.", "A Visit to the Nu Mou", "In return, I ask that you and yours remain here the while, and bestow upon us your patronage."),
 # #577 A Fitting Payment
 "M577a": ("A Nu Mou artisan was once esteemed by the knights of Voeburt.", "A Fitting Payment", "They are one of our foremost artisans, once held in the highest esteem by the knights of Voeburt."),
 "M577b": ("Nu Mou honor demands a task be paid exactly what it is worth.", "A Fitting Payment", "You see, for there to be honor in a task, we must receive precisely what it is worth."),
 "M577c": ("With the knights gone, the artisan has had no work.", "A Fitting Payment", "With the knights gone, however, Marn Ose has had no opportunity to put their skills to use."),
 # #578 Spore Sweeper
 "M578a": ("Minfilia is caught watching you.", "Spore Sweeper", "I-I wasn't spying on you or anything."),
 "M578b": ("The Voeburtites built the castle and named it Gruenes Licht.", "Spore Sweeper", "Back then the castle wasn't called Lyhe Ghiah. The Voeburtites built it, and they named it Gruenes Licht."),
 "M578c": ("The Voeburtites are all gone.", "Spore Sweeper", "And now they're gone, all of them. Nobles and knights and commonfolk alike..."),
 "M578d": ("A Nu Mou merchant asks you, as patron, to clear the flamespores from the cave.", "Spore Sweeper", "As my patron, I ask that you remove the noxious mushrooms that grow in our cave."),
 # #579 The Lawless Ones
 "M579a": ("Lawless Nu Mou stole another Nu Mou's invisible ink.", "The Lawless Ones", "The lawless ones took my invisible ink, and without it I can't make my arcane wares."),
 "M579b": ("Eulmore held the girl captive so she would not fight as earlier Minfilias had.", "The Lawless Ones", "But that had all changed by the time I was found. They held me captive so that I wouldn't follow in the others' footsteps."),
 "M579c": ("Thancred told her she would face the Lightwardens if your summoning failed.", "The Lawless Ones", "Thancred once told me that if the efforts to summon you failed, it would fall to me to face the Lightwardens."),
 "M579d": ("She believes Thancred keeps her close only as a contingency, because she is not his Minfilia.", "The Lawless Ones", "I realized then that it was the only reason he kept me close─as a contingency. … Because I'm not her. I'm not his Minfilia."),
 "M579e": ("At Nabaath Areng, something spoke through her that was not her.", "The Lawless Ones", "I have a vague feeling that I said something to him. Only it wasn't me at all. It was ''her''."),
 "M579f": ("She sought you out because she knew the other Minfilia wanted it.", "The Lawless Ones", "She should be the one to live on. That's why I tried to find you─because I ''knew'' that was what she wanted."),
 "M579g": ("She is unsure what she was meant to do once she found you.", "The Lawless Ones", "But now that you're here...I'm not entirely sure what it was she intended me to do."),
 "M579h": ("Titania's voice cries from the castle, demanding why they were imprisoned and begging you to play.", "The Lawless Ones", "Why? Why did you imprison us? … Come. Come and play with us..."),
 "M579i": ("The king kept some instincts, whose longing to play leaks through the seal.", "The Lawless Ones", "However, the king has retained some of their instincts. … This manifests in the desire to play and be free. So strong is that desire, it often leaks through the seal to invade our consciousness."),
 "M579j": ("A being that becomes a sin eater ordinarily loses everything that defined its mind.", "The Lawless Ones", "Ordinarily, when a living being turns into a sin eater, it loses everything about its mind that defined it."),
}

# ---- Entities -------------------------------------------------------------------------------------------------------
ENTITIES = {
 # recurring from earlier eras (same id and category merge; listed so this era lints alone)
 "char-alphinaud": "character", "char-alisaie": "character", "char-yshtola": "character", "char-thancred": "character",
 "char-urianger": "character", "char-tataru": "character", "char-biggs": "character", "char-wedge": "character",
 "char-minfilia": "character", "char-estinien": "character", "char-gaius": "character", "char-solus": "character",
 "char-enigmatic-figure": "character", "org-scions": "organization", "org-ascians": "organization",
 "org-garlean-empire": "organization", "org-warriors-of-darkness": "organization",
 # new in 5.0 part 1
 "char-crystal-exarch": "character", "char-lyna": "character", "char-ardbert": "character", "char-feo-ul": "character",
 "char-vauthry": "character", "char-kai-shirr": "character", "char-tesleen": "character", "char-ranjit": "character",
 "char-ryne": "character", "char-titania": "character",
 "org-sin-eaters": "organization", "org-pixies": "organization", "org-nu-mou": "organization",
 "loc-the-first": "location", "loc-crystarium": "location", "loc-eulmore": "location", "loc-il-mheg": "location",
 "evt-answering-the-summons": "event", "evt-behind-eulmores-gate": "event", "evt-the-inn-at-journeys-head": "event",
 "evt-night-over-lakeland": "event", "evt-the-laxan-loft-rescue": "event", "evt-the-pixies-games": "event",
 "evt-the-sealed-king": "event",
}

# ---- Presentations ---------------------------------------------------------------------------------------------------
PRES = {
 # -- The summons and the Crystarium
 "char-enigmatic-figure": [
   P(L542, None, "main", "The enigmatic figure",
     "The voice that called to the Scions and to you, and the hooded figure who bade you go to the Crystal Tower. When you found the beacon there, the voice called clearly and carried you to another world. "
     "It is the Crystal Exarch, who thanked you for answering his summons.",
     ["M542d", "M542i", "M542j"], ["The voice", "The hooded figure"]),
 ],
 "char-crystal-exarch": [
   P(L542, None, "main", "The Crystal Exarch",
     "A hooded man who bears the title of Crystal Exarch as caretaker of the Crystarium. He is the voice that summoned you: he learned to bridge worlds to call the greatest of heroes to the First, "
     "though it meant taking the Source's champion, and he vouched for you at the city's gate.",
     ["M542d", "M542h", "M542i", "M542j", "M542n"], ["The Exarch", "The enigmatic figure"]),
   P(L543, None, "main", "The Crystal Exarch",
     "The hooded caretaker of the Crystarium who summoned you to the First. Its people say his magicks pulled the Crystal Tower from thin air, and the eldest swear he has not aged in decades. "
     "He says the tower is the one from the Source, moved whole, and that its arrival set fate in motion.",
     ["M542i", "M542j", "M543c", "M543d", "M543i", "M543j"], ["The Exarch", "The enigmatic figure"]),
   P(L544, None, "main", "The Crystal Exarch",
     "The caretaker of the Crystarium, who summoned you to the First. His summons, meant for you alone, also drew the souls of the Scions closest to you, who now live there as spirits unable to return. "
     "He has promised to find them a way home.",
     ["M542j", "M544w", "M544e", "M544f", "M544j"], ["The Exarch", "The enigmatic figure"]),
   P(L563, None, "main", "The Crystal Exarch",
     "The caretaker of the Crystarium, who summoned you to the First to destroy the Lightwardens. When you slew Lakeland's Lightwarden and absorbed its Light, he hailed his Warriors of Darkness, "
     "conceded it was wrong to summon you against your will, and swore to atone. Despite appearances, he says, he is an old man burdened with painful memories.",
     ["M542j", "M563h", "M563k", "M563p", "M563n", "M563o"], ["The Exarch", "The enigmatic figure"]),
   P(L565, None, "main", "The Crystal Exarch",
     "The caretaker of the Crystarium, who summoned you to the First. When Eulmore's General Ran'jit came demanding answers for the Lightwarden's death, he declared that the Crystarium rejoices in it, "
     "and asked that his people lead the rescue of the girl Minfilia from Laxan Loft.",
     ["M542j", "M565a", "M565c", "M565r"], ["The Exarch", "The enigmatic figure"]),
   P(L568, None, "main", "The Crystal Exarch",
     "The caretaker of the Crystarium, who rallied its leaders to defy Eulmore and rescue the girl Minfilia, embracing the name of villains. When Ran'jit pursued the rescuers from Laxan Loft, "
     "he held the general back and sent you on to the faerie kingdom of Il Mheg.",
     ["M542j", "M566b", "M566c", "M568f"], ["The Exarch", "The enigmatic figure"]),
 ],
 "char-lyna": [
   P(L542, None, "main", "Lyna",
     "The captain of the guard and gatekeeper of the Crystarium, who calls the Crystal Exarch her lord. She barred you for refusing to say where you came from, until the Exarch declared you his guest.",
     ["M542g", "M542h", "M542p"], ["Captain Lyna"]),
   P(L563, None, "main", "Lyna",
     "The captain of the Crystarium's guard, who serves the Crystal Exarch. She went with you into Holminster Switch, warning that a slain Warden's aether turns the nearest living being into a new one, "
     "and saw you absorb it unharmed.",
     ["M542h", "M563i", "M563j", "M563k"], ["Captain Lyna"]),
   P(L566, None, "main", "Lyna",
     "The captain of the Crystarium's guard, who expects to be told the whole truth about you one day. She planned the raid to free the girl Minfilia from Laxan Loft with amaro and dream powder, "
     "and you have joined her guard.",
     ["M564c", "M566e", "M566f", "M566g"], ["Captain Lyna"]),
 ],
 "loc-crystarium": [
   P(L542, None, "main", "The Crystarium",
     "A city in the First, the largest settlement for malms around. Its caretaker is the Crystal Exarch, and Captain Lyna guards its gate.",
     ["M542f", "M542j", "M542p"]),
   P(L543, None, "main", "The Crystarium",
     "A city in the First that stands around the Crystal Tower, which its people say the Crystal Exarch pulled from thin air. The tower is the one from the Source, moved whole to the First.",
     ["M542j", "M543c", "M543i"]),
   P(L566, None, "main", "The Crystarium",
     "A city in the First, led by the Crystal Exarch, at odds with Eulmore. Warned that siding with the Warrior of Darkness means war, its leaders resolved to rescue the girl Minfilia as their answer, "
     "and to embrace the name of villains.",
     ["M545c", "M566a", "M566b", "M566c"]),
 ],
 "loc-the-first": [
   P(L542, None, "main", "The world of the First",
     "One of the thirteen shards of the Source, all but consumed by Light since a flood a century ago swallowed more than nine-tenths of it. Its survivors are hounded by sin eaters, and no dark night has fallen there in over a hundred years.",
     ["M542k", "M542l", "M542m", "M542o"]),
   P(L543, None, "main", "The world of the First",
     "One of the thirteen shards of the Source, whose people know nothing of other stars. They tell how villains called the Warriors of Light slew the Shadowkeeper a century ago. "
     "Then the Flood of Light swept the world, until the Oracle of Light stayed it and spared only Norvrandt.",
     ["M542k", "M543b", "M543e", "M543f", "M543g"]),
   P(L544, None, "main", "The world of the First",
     "A shard of the Source drowned in Light, where time runs at its own pace. Urianger foresaw it rejoined with the Source in the Eighth Umbral Calamity, and the Scions learned that eliminating the sin eaters can prevent it.",
     ["M542k", "M544b", "M544g", "M544i"]),
   P(L563, None, "main", "The world of the First",
     "One of thirteen shards split from a single star along with the Source, which has absorbed seven of them in calamities. Drowned in Light, it stands close to the conditions for a Rejoining, "
     "and its Lightwardens' Light keeps night from the sky.",
     ["M563d", "M563e", "M563f", "M563g"]),
   P(L573, None, "main", "The world of the First",
     "A shard of the Source close to a Rejoining. Its Light, the power of stasis, flows into the Source and thins its aether, and Urianger foresees that this surge will amplify Black Rose into the Eighth Umbral Calamity.",
     ["M563f", "M573i", "M573k"]),
 ],
 "org-sin-eaters": [
   P(L542, None, "main", "The sin eaters",
     "Abominations born of the flood of Light that swallowed most of the First, which hound its survivors.",
     ["M542l", "M542m"]),
   P(L543, None, "main", "The sin eaters",
     "Abominations of Light incarnate that descended on the First's survivors after the Flood of Light, and stole the night from Norvrandt's sky.",
     ["M542m", "M543h"]),
   P(L544, None, "main", "The sin eaters",
     "Abominations of Light incarnate that hunt the survivors of the Flood of Light. The Scions have learned that eliminating them can prevent the Eighth Umbral Calamity.",
     ["M543h", "M544i"]),
   P(L551, None, "main", "The sin eaters",
     "Abominations of Light incarnate that hunt the First's survivors. Eulmore's army suffered grievous losses fighting them, but some twenty years ago they grew docile, and Eulmorans say Lord Vauthry was born with the power to command them.",
     ["M543h", "M551c", "M551b", "M551a"]),
   P(L553, None, "main", "The sin eaters",
     "Abominations of Light incarnate that hunt the First's survivors. In Eulmore they are held to shepherd innocent souls to paradise, and Lord Vauthry says they must be fed living aether, and that he alone commands them.",
     ["M543h", "M552c", "M553b"]),
   P(L549B, None, "main", "The sin eaters",
     "Monsters that were once living creatures, or people, caught in the Flood. The stronger ones plant Light in their victims, corrupting them into new sin eaters, and the afflicted wait at the Inn at Journey's Head for the change.",
     ["M549bc", "M549bd"]),
   P(L550B, None, "main", "The sin eaters",
     "Monsters that were once living creatures caught in the Flood. Lesser ones flock to the strongest of their kind, and the stronger plant Light in their victims, turning them into new sin eaters.",
     ["M549bc", "M549bd", "M550ba"]),
   P(L563, None, "main", "The sin eaters",
     "Monsters of Light, once living creatures caught in the Flood, that serve the strongest of their kind, the few Lightwardens. A slain Warden's aether turns the nearest living being into a new one, "
     "and in Eulmore, Vauthry's command over them guarantees obedience.",
     ["M549bc", "M563a", "M563j", "M563c"]),
 ],
 # -- The Source's side
 "char-tataru": [
   P(L542, None, "main", "Tataru",
     "The Scions' receptionist, who led the search for the beacon below the Crystal Tower, desperate to wake the sleeping Scions before the Empire returns. When you found it, she bade you find your friends and bring them home.",
     ["M542a", "M542b", "M542e"]),
 ],
 "char-biggs": [
   P(L542, None, "main", "Biggs",
     "A member of Cid's Ironworks crew, who answered the Scions' call for aid and joined Wedge in the search for the beacon below the Crystal Tower.",
     ["M542a", "M542c"]),
 ],
 "char-wedge": [
   P(L542, None, "main", "Wedge",
     "A member of Cid's Ironworks crew, who answered the Scions' call for aid and joined Biggs in the search for the beacon below the Crystal Tower.",
     ["M542a", "M542c"]),
 ],
 "char-estinien": [
   P(L564, None, "main", "Estinien",
     "A dragoon whom the Scions tracked down and conscripted to root out the Empire's new weapon. In an imperial magitek facility he met Gaius, who invited him to join his hunt.",
     ["M564j", "M564k", "M564n"]),
 ],
 "char-gaius": [
   P(L564, None, "main", "Gaius",
     "The Black Wolf, a former imperial legatus who hunts Ascians as Shadowhunter. His people destroyed a Black Rose factory, though the Empire has built more; he invited Estinien to join him, "
     "and means to return to Garlemald to see the Ascians' corruption for himself.",
     ["M564l", "M564n", "M564o"], ["the Black Wolf", "Shadowhunter"]),
 ],
 "org-garlean-empire": [
   P(L564, None, "main", "The Garlean Empire",
     "An empire whose new weapon, Black Rose, brings the aether of living beings to a standstill. When one factory was destroyed, it built more to keep production going.",
     ["M564l", "M564m"]),
   P(L573, None, "main", "The Garlean Empire",
     "An empire whose weapon, Black Rose, halts the aether of living beings. In Urianger's vision, the Empire, facing defeat, unleashes it, bringing carnage across Eorzea and its own provinces.",
     ["M564m", "M573f", "M573g"]),
 ],
 "char-solus": [
   P(L553, None, "main", "Solus",
     "A former emperor of Garlemald. He has been seen in the First, eavesdropping as Lord Vauthry raged at Alphinaud in Eulmore.",
     ["M553g", "M553f"], ["Emperor Solus"]),
   P(L568, None, "main", "Solus",
     "A former emperor of Garlemald, seen in the First. Watching from afar as you escaped Laxan Loft, he wondered how the Exarch brought the hero of the Source to the First, and said his plan has gone awry.",
     ["M553g", "M568g", "M568h"], ["Emperor Solus"]),
 ],
 # -- The Scions in the First
 "org-scions": [
   P(L544, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future. The Exarch's summons drew five Scions' souls into the First, where they live as spirits unable to return, while their bodies sleep in the Source. "
     "They have learned that eliminating the sin eaters can avert the Eighth Umbral Calamity.",
     ["M542b", "M544a", "M544w", "M544f", "M544i"]),
 ],
 "char-yshtola": [
   P(L544, None, "main", "Y'shtola",
     "A Sharlayan Scion whose soul, drawn into the First by the Exarch's summons, has lived there for three winters. She is stationed in the forests of Rak'tika, to the east.",
     ["M544w", "M544c", "M544r"]),
 ],
 "char-urianger": [
   P(L544, None, "main", "Urianger",
     "A Sharlayan Scion whose soul has lived in the First for three winters, in Il Mheg. Crossing the rift, he saw a vision of the First rejoined with the Source in the Eighth Umbral Calamity, and of your death.",
     ["M544c", "M544s", "M544g", "M544h"]),
   P(L573, None, "main", "Urianger",
     "A Sharlayan Scion who lives in the Bookman's Shelves in Il Mheg. In his vision, the Empire unleashes Black Rose, which the First's Light amplifies into the Eighth Umbral Calamity, killing even you. "
     "He has joined you to stop it, starting with Il Mheg's Lightwarden.",
     ["M573e", "M573f", "M573h", "M573k", "M573m", "M573l"]),
   P(L574, None, "main", "Urianger",
     "A Sharlayan Scion traveling with you in Il Mheg, where he is building a trap for the Ascians' essence. He won the pixies' favor with gifts, and asks who will take up the flame of hope Minfilia has borne.",
     ["M574a", "M574b", "M574m", "M574l"]),
   P(L576, None, "main", "Urianger",
     "A Sharlayan Scion hunting Il Mheg's Lightwarden, who once brought together the Warriors of Darkness and Minfilia. The Nu Mou have served him faithfully, and he has brought you to them for the stone scepter.",
     ["M576c", "M576a", "M575e"]),
 ],
 "char-thancred": [
   P(L544, None, "main", "Thancred",
     "A Scion whose soul has lived in the First for five years. He wanders as a hunter of sin eaters, with a new companion.",
     ["M544c", "M544t"]),
   P(L565, None, "main", "Thancred",
     "A Scion who has spent five years in the First. Three years ago he stole into Eulmore and rescued the girl called Minfilia, and the two have wandered together since.",
     ["M544c", "M565n", "M565o"]),
   P(L568, None, "main", "Thancred",
     "A Scion who traveled with the girl Minfilia hunting sin eaters, until she ran off and Eulmore took her. At Laxan Loft he faced Ran'jit, who knows him as the one who stole her, "
     "and on the Exarch's orders took you to Il Mheg to find Urianger and slay its Lightwarden.",
     ["M568j", "M568k", "M568c", "M568d", "M568l"]),
   P(L574, None, "main", "Thancred",
     "A Scion who cannot manipulate aether, his body being left in the Source, so the girl Minfilia imbues his ammunition. At the edge of the Empty the Minfilia of old once woke within her, "
     "and asked him to protect and teach her. He has never told the girl of that day.",
     ["M574c", "M574d", "M574f", "M574j", "M574k"]),
 ],
 "char-alphinaud": [
   P(L544, None, "main", "Alphinaud",
     "A young Scion whose soul has lived in the First for almost a year, on the island of Kholusia.",
     ["M544d", "M544u"]),
   P(L546, None, "main", "Alphinaud",
     "A young Scion who has lived in the First for almost a year. Reunited with you on Kholusia, he believes any solution must be sought in Eulmore, the land's center of power.",
     ["M544d", "M546b", "M546e"]),
   P(L549, None, "main", "Alphinaud",
     "A young Scion who has talked his way into Eulmore posing as a painter, with you as his assistant. You are both bonded to a Mystel couple, the Chais.",
     ["M549a", "M549b", "M549d"]),
   P(L553, None, "main", "Alphinaud",
     "A young Scion who left Eulmore after insulting Lord Vauthry, who swore to torture him and his companions. Seeing few allies there against the sin eaters, he has returned to the Exarch to chart a new course.",
     ["M553j", "M553f", "M553h", "M553i"]),
   P(L575, None, "main", "Alphinaud",
     "A young Scion helping hunt Il Mheg's Lightwarden. With Eulmore's army marching on Il Mheg, he and Alisaie went to meet it, leaving the relic hunt to you.",
     ["M575k", "M575l"]),
 ],
 "char-alisaie": [
   P(L544, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion, whose soul has lived in the First for almost a year, in the arid wastes of Amh Araeng.",
     ["M544d", "M544v"]),
   P(L549B, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion, still angry at the Exarch's ill-timed summons. She guards the Inn at Journey's Head in Amh Araeng, hunts sin eaters, and does not doubt Urianger's vision.",
     ["M545bb", "M547ba", "M549ba", "M549bf"]),
   P(L553B, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. After Tesleen died saving a patient and turned into a sin eater, she gave up her post at the Inn at Journey's Head to turn her skills against the eaters, "
     "and rode for the Crystarium to plan their end with the Exarch.",
     ["M552bb", "M552be", "M553ba", "M553bb", "M553bd"]),
   P(L564, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. After fighting with you at Holminster Switch, she stayed behind there alone, saying she knew one of the eaters.",
     ["M563i", "M564d"]),
   P(L575, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. With Eulmore's army marching on Il Mheg, she and her brother went to meet it, leaving the relic hunt to you.",
     ["M575k", "M575l"]),
 ],
 # -- Ardbert, Minfilia and the Warriors of Darkness
 "char-ardbert": [
   P(L544, None, "main", "Ardbert",
     "A ghost who used an alias in the Source, one of the band who caused the Flood after the Ascians guided them there. After your victory, Minfilia returned their souls to the First, "
     "where she and his friends faded holding back the Flood; for a century he has drifted as a shade, and thinks the world beyond saving.",
     ["M544l", "M544m", "M544n", "M544o", "M544p", "M544q"]),
   P(L564, None, "main", "Ardbert",
     "A shade from the band who caused the Flood, whom no one else can see. He remembers the twins from his band's battle in the Source, and says it is your lot's turn to be the Warriors of Darkness.",
     ["M544m", "M544p", "M564h", "M564g"]),
   P(L575, None, "main", "Ardbert",
     "A shade from the band who caused the Flood. He woke you beneath Il Mheg's lake, by the drowned capital of Voeburt, whose people he once knew, and wonders what all his band gave was for.",
     ["M544m", "M575h", "M575i", "M575j"]),
 ],
 "org-warriors-of-darkness": [
   P(L544, None, "main", "The Warriors of Darkness",
     "Adventurers from the First who, believing their home doomed, let the Ascians guide them to the Source; they caused the Flood. After you defeated them, Minfilia returned their souls to the First, "
     "where all but Ardbert faded with her holding the Flood back.",
     ["M544m", "M544n", "M544o"]),
 ],
 "char-minfilia": [
   P(L544, None, "main", "Minfilia",
     "Once leader of the Scions, who left with the Warriors of Darkness for their world as Hydaelyn's emissary. Ardbert says she returned their souls to the First, then gave all she had left with his friends to hold back the Flood, and faded.",
     ["M544n", "M544o"], ["the Antecedent", "the Word of the Mother"]),
   P(L565, None, "main", "Minfilia",
     "Once leader of the Scions, who came to the First as Hydaelyn's emissary and halted the Flood a century ago, revered there as the Oracle of Light. "
     "Girls with her looks and powers have since been found and called by her name, though they lack her memories, and Alisaie thinks them not the same person.",
     ["M565i", "M565p", "M565j", "M565k", "M565q"], ["the Antecedent", "the Word of the Mother"]),
   P(L574, None, "main", "Minfilia",
     "Once leader of the Scions, revered in the First as the Oracle of Light. At the edge of the Empty she woke within the girl who bears her name, calling herself no different from an Ascian and the girl a vessel, one of many. "
     "Should the girl choose her own destiny, she will bequeath her all, and she asked Thancred to protect her.",
     ["M565i", "M574f", "M574g", "M574h", "M574i", "M574j"], ["the Antecedent", "the Word of the Mother"]),
 ],
 "char-ryne": [
   P(L565, None, "main", "Minfilia of the First",
     "The current girl called Minfilia, one of the line believed to be the Oracle of Light reborn. Eulmore's army found her ten years ago and kept her a prisoner in all but name, until Thancred rescued her three years ago. "
     "Now Eulmore's forces hold her again at Laxan Loft.",
     ["M565j", "M565l", "M565o", "M565g", "M565r"], ["Minfilia"]),
   P(L568, None, "main", "Minfilia of the First",
     "A girl called Minfilia, hailed as the Oracle reborn, who traveled with Thancred hunting sin eaters. She ran off sensing someone she was meant to meet, you, and was taken by Eulmore; "
     "the Crystarium's raid freed her from Laxan Loft, and she refused to go back to her cell.",
     ["M565j", "M568j", "M568m", "M568k", "M568a", "M568b"], ["Minfilia"]),
   P(L574, None, "main", "Minfilia of the First",
     "A girl called Minfilia who travels with Thancred and imbues his ammunition. At the edge of the Empty, the Minfilia of old spoke through her; she remembers none of it.",
     ["M574e", "M574d", "M574f", "M574k"], ["Minfilia"]),
   P(L579, None, "main", "Minfilia of the First",
     "A girl called Minfilia whom Eulmore held captive so she would not fight as earlier Minfilias had. She believes Thancred keeps her close only as a contingency, since she is not his Minfilia. "
     "She sought you because she knew the other Minfilia wanted it, but is unsure what she was meant to do.",
     ["M579b", "M579c", "M579d", "M579f", "M579g"], ["Minfilia"]),
 ],
 # -- Eulmore
 "loc-eulmore": [
   P(L545, None, "main", "Eulmore",
     "A city on Kholusia whose elite fancy themselves masters of what remains of the world. Many resist its authority, the Crystarium among them, and their relations are strained, though not at war.",
     ["M545b", "M545c", "M545d"]),
   P(L547, None, "main", "Eulmore",
     "The rich city of Kholusia, known as the city of final pleasures, whose gates a poor man could sooner pass through the eye of a needle. In Gatetown outside, hopefuls queue for admission and live on its handouts of meol, "
     "under a policy two decades old.",
     ["M546a", "M547c", "M547b", "M547e", "M547d"]),
   P(L550, None, "main", "Eulmore",
     "The rich city of Kholusia, where the free live under Lord Vauthry's favor and the bonded serve them. Free citizens give all their property to the city on registration, and say they know no war or conflict.",
     ["M549c", "M550a", "M550b", "M550d"]),
   P(L552, None, "main", "Eulmore",
     "The rich city of Kholusia, ruled by Lord Vauthry. Its people hold that sin eaters carry innocent souls to paradise, and of the many who enter the city, few are ever seen to leave.",
     ["M548e", "M552c", "M552a"]),
   P(L565, None, "main", "Eulmore",
     "The rich city of Kholusia, which has ever wanted to rule what remains of the world, and under Lord Vauthry abandoned resistance for decadence. "
     "Angered by the Lightwarden's death, it sent General Ran'jit to threaten the Crystarium, and its forces hold the girl Minfilia.",
     ["M565s", "M565m", "M565a", "M565b", "M565g"]),
 ],
 "char-vauthry": [
   P(L548, None, "main", "Vauthry",
     "The lord of Eulmore, whose judgments no one there questions. When an artist lost his patron, Vauthry granted his wish to leave by having him flung into the sea.",
     ["M548d", "M548e"], ["Lord Vauthry"]),
   P(L551, None, "main", "Vauthry",
     "The lord of Eulmore, whose word is law. Eulmorans say he was born with the power to command the sin eaters, so no citizen need take up arms.",
     ["M548e", "M549c", "M551a"], ["Lord Vauthry"]),
   P(L553, None, "main", "Vauthry",
     "The lord of Eulmore, who says the sin eaters must be fed living aether and that he alone commands them. He made Kai-Shirr carve an offering from his own flesh, "
     "and when Alphinaud insulted him he swore to torture you all.",
     ["M553b", "M553c", "M553a", "M553j", "M553f"], ["Lord Vauthry"]),
   P(L565, None, "main", "Vauthry",
     "The lord of Eulmore, who commands the sin eaters. His general, Ran'jit, threatened the Crystarium with retribution for the Lightwarden's death, and seeks for him a young artist and his assistant.",
     ["M553b", "M565b", "M565d", "M565f"], ["Lord Vauthry"]),
 ],
 "char-kai-shirr": [
   P(L548, None, "main", "Kai-Shirr",
     "A young Mystel who posed as Alphinaud's lackey to make off with his goods, desperate to join his friends in Eulmore. Alphinaud gave him his place in a trade with the Ondo instead.",
     ["M548b", "M548c"]),
   P(L553, None, "main", "Kai-Shirr",
     "A young Mystel who got into Eulmore through Alphinaud's deal. Sentenced for fraud, he was made to carve an offering from his own flesh; you and Alphinaud fled with him, "
     "and he stays on Kholusia to learn to stand on his own.",
     ["M553a", "M553d", "M553e"]),
 ],
 "char-ranjit": [
   P(L565, None, "main", "Ran'jit",
     "The general who has led Eulmore's army since before Vauthry's time, and mentored generations of Minfilias. Angered by the Lightwarden's death, he threatened the Crystarium with retribution, "
     "and is searching for a young artist and his assistant.",
     ["M565a", "M565e", "M565h", "M565b", "M565d"], ["General Ran'jit"]),
   P(L568, None, "main", "Ran'jit",
     "The general of Eulmore's army. At Laxan Loft he overpowered the rescuers until Thancred, whom he knows as the one who stole the Oracle, arrived; he noted you resemble the artist his master seeks.",
     ["M565e", "M568c", "M568d", "M568e"], ["General Ran'jit"]),
 ],
 # -- Amh Araeng
 "char-tesleen": [
   P(L547B, None, "main", "Tesleen",
     "A carer at the Inn at Journey's Head in Amh Araeng, who has come to know Alisaie well since she took up guard duties there.",
     ["M547ba"]),
   P(L551B, None, "main", "Tesleen",
     "A carer at the Inn at Journey's Head, home to the afflicted, who will all turn into sin eaters one day. The carers spare them with poison mixed into their favorite food.",
     ["M547ba", "M548ba", "M551bb", "M551bc"]),
   P(L552B, None, "main", "Tesleen",
     "A carer at the Inn at Journey's Head, who came there with her mother when her mother showed the early signs. When a sin eater carried off the patient Halric, she gave her life to save him, "
     "turned into a sin eater herself and flew away.",
     ["M547ba", "M552bc", "M552ba", "M552bb", "M552be"]),
 ],
 # -- Il Mheg
 "loc-il-mheg": [
   P(L544, None, "main", "Il Mheg",
     "The faerie kingdom in the north of the First's surviving lands, where Urianger dwells.",
     ["M544s"]),
   P(L568, None, "main", "Il Mheg",
     "The faerie kingdom of the First, a haven of fae folk where even Eulmore dare not bare its steel. It was once the kingdom of Voeburt, until the sin eaters cut it short, and its pixies trick trespassers with illusions.",
     ["M568f", "M568i", "M568n"]),
   P(L575, None, "main", "Il Mheg",
     "The faerie kingdom, once Voeburt, whose drowned capital lies under its lake. Its faerie king, Titania, has become its Lightwarden and is sealed in the castle of Lyhe Ghiah, "
     "and Eulmore's army is marching on it.",
     ["M568i", "M575i", "M575a", "M575c", "M575k"]),
 ],
 "org-pixies": [
   P(L569, None, "main", "The pixies",
     "Fae of Il Mheg who use illusions to trick trespassers into their games. Once you exposed them with looking grass, they agreed to let you see Urianger, who won his place there with a seven-day riddle contest, "
     "but only after you do their chores.",
     ["M568n", "M569c", "M569d", "M569e"]),
   P(L570, None, "main", "The pixies",
     "Fae of Il Mheg, whose village of Lydha Lran means flower house. They once lived in a lush forest that the light swallowed, and settled where the mortal city of Voeburt stood before the sin eaters came.",
     ["M570a", "M570c", "M570b"]),
   P(L570B, None, "main", "The pixies",
     "Fae of Il Mheg who take nothing as seriously as having fun. They hate the sin eaters, which are dull and painful.",
     ["M570ba", "M570bb"]),
   P(L570C, None, "main", "The pixies",
     "Fae of Il Mheg who keep enchanted mortals, the leafmen, as their children. They tried to enchant you too, but it did not catch.",
     ["M570cb", "M570cc"]),
   P(L573, None, "main", "The pixies",
     "Fae of Il Mheg, believed born from the souls of those who died as children, who live to play and would never have let you go. Your pact-mate Feo Ul forced them to release you.",
     ["M573b", "M573a", "M573c"]),
   P(L575, None, "main", "The pixies",
     "Fae of Il Mheg, pleased by your gifts. Their king, Titania, slew the first Lightwarden and was corrupted into a new one, so they sealed Titania in the castle; they gave you a dress, one of the four relics that break the seal.",
     ["M574m", "M575a", "M575b", "M575c", "M575e"]),
 ],
 "char-feo-ul": [
   P(L573, None, "main", "Feo Ul",
     "A pixie who made a pact with you at the Crystarium. Neglected ever since, Feo Ul sulked until you called earnestly, then claimed you as theirs alone and forced the other pixies to let you go.",
     ["M544k", "M573c", "M573d"]),
 ],
 "char-titania": [
   P(L575, None, "main", "Titania",
     "The king of the faeries of Il Mheg, who fought and beat the first Lightwarden to threaten it, only to be corrupted into a new Lightwarden by its light. Nothing remains of the wise and just ruler, "
     "and the fae sealed Titania in the castle of Lyhe Ghiah; four relics are needed to break the seal.",
     ["M575a", "M575b", "M575c", "M575d"]),
   P(L576, None, "main", "Titania",
     "The faerie king of Il Mheg, turned Lightwarden and sealed in Lyhe Ghiah. Many Nu Mou laid down their lives to make that seal, which four relics can break.",
     ["M575a", "M575c", "M576d", "M575d"]),
   P(L579, None, "main", "Titania",
     "The faerie king of Il Mheg, turned Lightwarden and sealed in the castle. A sin eater ordinarily loses its mind, but Titania kept some instincts, and their longing to play leaks through the seal: "
     "their voice cries out, demanding why they were imprisoned and begging you to come and play.",
     ["M575a", "M579j", "M579i", "M579h"]),
 ],
 "org-nu-mou": [
   P(L576, None, "main", "The Nu Mou",
     "Fae of Il Mheg, the friendliest to men, who have served Urianger. Many laid down their lives to seal their corrupted king, and their stone scepter is part of that seal; "
     "starved of patronage since Voeburt fell, they ask you to stay as their patron while they decide whether to lend it.",
     ["M576a", "M576d", "M576e", "M576f"]),
   P(L577, None, "main", "The Nu Mou",
     "Fae of Il Mheg weighing whether to lend you their stone scepter, while you act as their patron. Their honor demands a task be paid exactly what it is worth, and their artisans have been idle since the knights of Voeburt were lost.",
     ["M576f", "M577b", "M577a", "M577c"]),
 ],
 "org-ascians": [
   P(L574, None, "main", "The Ascians",
     "A group who sow strife and discord, and who once guided Ardbert's band to the Source. They crave the Rejoining the Scions mean to thwart, and Urianger is building a trap for their essence.",
     ["M544m", "M574a", "M574b"]),
 ],
}

# ---- Arc recaps ---------------------------------------------------------------------------------------------------
N1, N2, N3, N4, N5, N6, N7 = ("Answering the Summons", "Behind Eulmore's Gate", "The Inn at Journey's Head", "Night over Lakeland",
                              "The Laxan Loft Rescue", "The Pixies' Games", "The Sealed King")
PRES.update({
 "evt-answering-the-summons": [
   P(L542, None, "main", N1,
     "Searching beneath the Crystal Tower with Tataru, Biggs and Wedge, you found the beacon, and the voice carried you to the First, a world drowned in Light and hounded by sin eaters. "
     "At the Crystarium's gate, Captain Lyna turned you away until a hooded man vouched for you. He is the Crystal Exarch, the voice that summoned you to save this world.",
     ["M542a", "M542c", "M542d", "M542k", "M542m", "M542g", "M542h", "M542i"]),
   P(L543, None, "main", N1,
     "The Crystal Exarch, who summoned you to the First, sent you to learn the Crystarium's ways. Its people know nothing of other worlds, and say his magicks pulled the Crystal Tower from thin air. "
     "A century ago the Flood of Light swept their world, until the Oracle of Light stayed it and spared Norvrandt alone, leaving sin eaters to hunt the survivors.",
     ["M542i", "M543a", "M543b", "M543c", "M543f", "M543g", "M543h"]),
   P(L544, None, "main", N1,
     "The Exarch revealed that his summons, meant for you alone, drew the souls of five Scions into the First, where they live as spirits who cannot go home. "
     "Urianger foresaw the First rejoined with the Source in an Eighth Umbral Calamity that kills you, and the Scions learned that slaying sin eaters can stop it. In your room, the ghost of Ardbert waited.",
     ["M544w", "M544e", "M544f", "M544g", "M544h", "M544i", "M544l"]),
 ],
 "evt-behind-eulmores-gate": [
   P(L545, None, "main", N2,
     "Seeking Alphinaud on Kholusia, you flew there by amaro at the Exarch's arrangement. Its city, Eulmore, is ruled by an elite who fancy themselves masters of what remains of the world, "
     "and the Crystarium is among those who resist them. You were warned to hide your ties with the Exarch near the city.",
     ["M545a", "M545b", "M545c", "M545d"]),
   P(L546, None, "main", N2,
     "On Kholusia you found Alphinaud, who has lived in the First almost a year. He explained that a Rejoining needs both worlds to face an existential threat, as the sin eaters are here. "
     "Since Eulmore, richer than all Norvrandt, is the land's center of power, he believes any solution must be sought there.",
     ["M544d", "M546b", "M546d", "M546a", "M546e"]),
   P(L547, None, "main", N2,
     "Alphinaud has tried in vain to enter Eulmore, the “city of final pleasures,” where a poor man could sooner pass through the eye of a needle than the gates. "
     "Outside, the people of Gatetown queue for admission and live on handouts of meol, believing the city is the answer to all their woes, under a policy two decades old.",
     ["M547a", "M547b", "M547c", "M547e", "M547d"]),
   P(L548, None, "main", N2,
     "Alphinaud is scheming to get inside Eulmore. A young Mystel, Kai-Shirr, posed as his lackey to steal goods for a trade with the Ondo, desperate to join his friends in the city, and Alphinaud handed him the deal instead. "
     "You also rescued an artist flung into the sea on Lord Vauthry's word, which no one in Eulmore questions.",
     ["M548a", "M548b", "M548c", "M548d", "M548e", "M548f"]),
   P(L549, None, "main", N2,
     "Posing as a painter with you as his assistant, Alphinaud won you both a way into Eulmore. Its citizens are free, under Lord Vauthry's favor, or bonded to the free. "
     "You were registered as bonded to a Mystel couple, the Chais, who want a portrait.",
     ["M549a", "M549b", "M549c", "M549d"]),
   P(L550, None, "main", N2,
     "Inside Eulmore as the Chais' bonded painter and assistant, Alphinaud sent you to explore the city. A free citizen told you that on registration all property passes to the city, "
     "freeing its people from any care for coin, and her attendant says Eulmore knows no war or conflict.",
     ["M549d", "M550c", "M550a", "M550d", "M550b"]),
   P(L551, None, "main", N2,
     "Exploring Eulmore for Alphinaud, you heard at the Beehive that Lord Vauthry was born with the power to command the sin eaters, so no citizen need take up arms. "
     "A performer recalled that the eaters grew docile some twenty years ago, when the old ruler's son took power, after the army suffered grievous losses fighting them.",
     ["M550c", "M551a", "M551b", "M551c"]),
   P(L552, None, "main", N2,
     "In Eulmore's lower layers, an apothecary told you that of the many who enter the city, few are ever seen to leave. "
     "A free citizen arranged with Lord Vauthry for his voiceless singer's “ascension,” saying the sin eaters shepherd innocent souls to paradise. Alphinaud wonders where all the newcomers go.",
     ["M552a", "M552b", "M552c", "M552d"]),
   P(L553, None, "main", N2,
     "At the Offer, Lord Vauthry, who says the sin eaters must be fed living aether and that he alone commands them, made Kai-Shirr carve an offering from his own flesh. "
     "When Alphinaud insulted him, Vauthry swore to torture you all, and you fled with Kai-Shirr. Unseen, Solus listened, and Alphinaud returned to the Exarch.",
     ["M553a", "M553b", "M553j", "M553f", "M553d", "M553g", "M553i"]),
 ],
 "evt-the-inn-at-journeys-head": [
   P(L545B, None, "main", N3,
     "The Exarch arranged your journey to Alisaie in Amh Araeng, hoping to soothe her anger at her ill-timed summons. A caravan master led you across the desert, where the Light swallowed much of Nabaath Areng, "
     "to the town of Mord Souq. Alisaie is staying at the Inn at Journey's Head.",
     ["M545ba", "M545bb", "M545bd", "M545be", "M545bc"]),
   P(L546B, None, "main", N3,
     "On the way to Alisaie at the Inn at Journey's Head, you reached Mord Souq in Amh Araeng, long a refuge for those the Flood displaced. "
     "Its merchants trade in relics the Mord dig up, and newcomers must observe a custom, so you spent the Exarch's coin at an eatery and ate your fill.",
     ["M545bc", "M546ba", "M546bc", "M546bb", "M546bd"]),
   P(L547B, None, "main", N3,
     "Still in Mord Souq on the way to Alisaie, you collected a caravan master's purchases from the market. When he was delayed, Tesleen offered to guide you instead: "
     "a carer at the Inn at Journey's Head who has come to know Alisaie well since she took up guard duties there.",
     ["M545bc", "M547bb", "M547bc", "M547ba"]),
   P(L548B, None, "main", N3,
     "Tesleen, a carer from the Inn at Journey's Head, led you across the desert to Alisaie, who has been desperate to see you, while you cleared coyotes that prey on travelers. "
     "The Inn is home to the afflicted and a handful of carers, though Tesleen left it to Alisaie to explain what that means.",
     ["M547ba", "M548bb", "M548bc", "M548ba", "M548bd"]),
   P(L549B, None, "main", N3,
     "At the Inn at Journey's Head you found Alisaie hunting a sin eater. She explained that sin eaters were once living creatures caught in the Flood, and that the stronger ones plant Light in people, turning them into new monsters. "
     "The Inn's infirmary holds their victims, feared and shunned, waiting for the change.",
     ["M549ba", "M549bc", "M549bd", "M549be"]),
   P(L550B, None, "main", N3,
     "Reunited with Alisaie at the Inn at Journey's Head, you helped her cull the sin eaters around it, since the lesser ones flock to the strongest of their kind. "
     "The Inn shelters the afflicted, whom the stronger eaters' Light will turn. Tesleen says Alisaie has badly missed your company.",
     ["M549bd", "M550ba", "M550bb", "M550bc"]),
   P(L551B, None, "main", N3,
     "At the Inn at Journey's Head, every patient touched by the stronger sin eaters will one day turn. Alisaie showed you the white nothingness the Light left beyond Mord Souq, "
     "and told you the carers mix poison into a patient's favorite food as a mercy. The nectarine you fetched is the patient Halric's favorite.",
     ["M551bb", "M551ba", "M551bc", "M551bd"]),
   P(L552B, None, "main", N3,
     "At the Inn at Journey's Head, the afflicted wait for the mercy of a painless death before they turn. When the patient Halric went missing, a great sin eater carried him off, and Tesleen gave her life to save him. "
     "Dying, she turned into a sin eater herself and flew away, leaving no body to bury.",
     ["M552bg", "M552ba", "M552bb", "M552be", "M552bf"]),
   P(L553B, None, "main", N3,
     "After Tesleen died saving Halric and became a sin eater, Alisaie gave up her post at the Inn at Journey's Head. She will turn the skills she gained there against the eaters, "
     "and asked the carers to delay Halric's last meal as long as they can. She rode for the Crystarium to plan the eaters' end with the Exarch.",
     ["M552bb", "M552be", "M553ba", "M553bb", "M553be", "M553bc", "M553bd"]),
 ],
 "evt-night-over-lakeland": [
   P(L563, None, "main", N4,
     "Back at the Crystarium, the Exarch explained that sin eaters serve a few mighty Lightwardens, whose Light keeps night from the sky and drives the First toward a Rejoining. "
     "At Holminster Switch you slew Lakeland's Lightwarden and absorbed its aether unharmed, and night returned. The Exarch hailed his Warriors of Darkness, and admitted he was wrong to summon you against your will.",
     ["M563a", "M563g", "M563f", "M563i", "M563k", "M563l", "M563p", "M563n"]),
   P(L564, None, "main", N4,
     "Night has returned to Lakeland, and rumor credits the Warrior of Darkness with slaying its Lightwarden, so the Exarch asked you to hide your part. Alisaie stayed alone in Holminster Switch, saying she knew one of the eaters. "
     "In the Source, Estinien, conscripted by the Scions, met Gaius, who destroyed a Black Rose factory and is bound for Garlemald.",
     ["M563l", "M564e", "M564a", "M564d", "M564j", "M564l", "M564o"]),
 ],
 "evt-the-laxan-loft-rescue": [
   P(L565, None, "main", N5,
     "Angered by the Lightwarden's death, Eulmore sent General Ran'jit to threaten the Crystarium, but the Exarch defied him. Eulmore's forces hold the girl called Minfilia, hailed as the Oracle of Light reborn, at Laxan Loft. "
     "Thancred once rescued her, and the Exarch asked that the Crystarium lead her rescue.",
     ["M565a", "M565b", "M565c", "M565g", "M565j", "M565o", "M565r"]),
   P(L566, None, "main", N5,
     "Eulmore's General Ran'jit has warned of war if the Crystarium sides with the Warrior of Darkness. Its leaders chose to defy him and rescue the girl called Minfilia from Laxan Loft, embracing the name of villains. "
     "Captain Lyna planned an airborne raid with amaro and dream powder, and you joined her guard.",
     ["M566a", "M565r", "M566b", "M566c", "M566e", "M566f"]),
   P(L567, None, "main", N5,
     "The Crystarium will raid Laxan Loft to free the girl called Minfilia from Eulmore's army, with amaro scattering dream powder over the fort. "
     "Having joined the guard, you delivered an amaro to the Ostall Imperative, one of Lakeland's key strongholds, and reported to Captain Lyna for your next task.",
     ["M565r", "M566e", "M566f", "M567a", "M567b"]),
   P(L568, None, "main", N5,
     "The Crystarium's raid freed the girl Minfilia from Laxan Loft, but Ran'jit overpowered you all until Thancred arrived. He had traveled with her until she ran off, sensing you near. "
     "The Exarch stalled Ran'jit and sent you to the faerie kingdom of Il Mheg, with orders to find Urianger and slay the land's Lightwarden.",
     ["M568a", "M568c", "M568j", "M568k", "M568m", "M568f", "M568l"]),
 ],
 "evt-the-pixies-games": [
   P(L569, None, "main", N6,
     "Fleeing Eulmore's army with the rescued Minfilia, you reached Il Mheg, where the pixies' illusions lead travelers astray. With looking grass, Thancred exposed them, "
     "but they will let you see Urianger, who won his place there with a seven-day riddle contest, only after you finish their chores. You and your friends split up to do them.",
     ["M568f", "M568n", "M569c", "M569d", "M569e", "M569f"]),
   P(L570, None, "main", N6,
     "To win the pixies' leave to see Urianger, you are doing their chores in Il Mheg. One had you sow everbloom seeds around Lydha Lran, the flower house. "
     "The pixies once lived in a lush forest that the light swallowed, and a mortal city, Voeburt, stood here until the sin eaters came.",
     ["M569e", "M570d", "M570a", "M570c", "M570b"]),
   P(L570B, None, "main", N6,
     "To win the pixies' leave to see Urianger, you are doing their chores in Il Mheg. A hungry pixie sent you to shake fruit from two belltrees, and laughed when bugs fell with it. "
     "Pixies take nothing as seriously as fun, and hate the sin eaters, dull and painful as they are.",
     ["M569e", "M570bc", "M570ba", "M570bb"]),
   P(L570C, None, "main", N6,
     "To win the pixies' leave to see Urianger, you are doing their chores in Il Mheg. A faerie sent you to water the leafmen with water from the lake, braving the Fuath who play rough there. "
     "The leafmen were once stray mortals the faeries enchanted, and they tried it on you too, though it did not catch.",
     ["M569e", "M570cc", "M570ca", "M570cb"]),
   P(L573, None, "main", N6,
     "The pixies would never have let you go, until your pact-mate Feo Ul forced them to. At the Bookman's Shelves, Urianger shared his vision: facing defeat, the Empire unleashes Black Rose, "
     "the First's Light amplifies it, and the Eighth Umbral Calamity kills even you. To prevent it, every Lightwarden must die, starting with Il Mheg's.",
     ["M573a", "M573c", "M573e", "M573f", "M573k", "M573h", "M573n", "M573l"]),
   P(L574, None, "main", N6,
     "Urianger means to trap the Ascians' essence, and won the pixies' favor with gifts so you can enter the castle where Il Mheg's Lightwarden waits. "
     "Thancred revealed that the Minfilia of old once woke within the girl at the edge of the Empty, calling her a vessel, and offered her all her power should she choose her own destiny. The girl remembers nothing.",
     ["M574b", "M573l", "M574m", "M574f", "M574g", "M574i", "M574k"]),
 ],
 "evt-the-sealed-king": [
   P(L575, None, "main", N7,
     "Il Mheg's Lightwarden is the faerie king Titania, corrupted after slaying the first Lightwarden and sealed in the castle of Lyhe Ghiah by the fae. Breaking the seal takes four relics. "
     "You won the shell crown from the Fuath, and Ardbert woke you beneath the lake. Now Eulmore's army marches on Il Mheg, and the twins have gone to meet it.",
     ["M575a", "M575b", "M575c", "M575d", "M575g", "M575h", "M575k", "M575l"]),
   P(L576, None, "main", N7,
     "To break the seal on Titania, the faerie king turned Lightwarden, you need four relics, and hold the dress and the shell crown. Urianger led you to the Nu Mou for their stone scepter, but many of them died to seal their king. "
     "Starved of patronage since Voeburt fell, they ask you to stay as their patron while they decide.",
     ["M575a", "M575d", "M575e", "M576a", "M576d", "M576e", "M576f"]),
   P(L577, None, "main", N7,
     "The Nu Mou are weighing whether to lend you their stone scepter, one of the four relics that can break Titania's seal, and meanwhile you act as their patron. "
     "A Nu Mou artisan, idle since the knights of Voeburt were lost, served you for a fitting price, since Nu Mou honor demands a task be paid exactly what it is worth.",
     ["M575d", "M576f", "M577a", "M577c", "M577b"]),
   P(L578, None, "main", N7,
     "While the Nu Mou weigh lending you the stone scepter to break Titania's seal, you serve them as patron. Clearing a merchant's cave of flamespores, you learned that the castle where Titania is sealed was built by the Voeburtites, "
     "who named it Gruenes Licht. The girl Minfilia was caught watching you.",
     ["M576f", "M578d", "M578b", "M578c", "M578a"]),
   P(L579, None, "main", N7,
     "Serving the Nu Mou as patron, you recovered stolen ink with the girl Minfilia, who believes Thancred keeps her close only as a contingency, since she is not his Minfilia. "
     "She sought you out because she knew the Minfilia of old wished it. Then Titania's voice cried out from the sealed castle, begging you to come and play.",
     ["M576f", "M579a", "M579d", "M579f", "M579h"]),
 ],
})

# ---- Relationships --------------------------------------------------------------------------------------------------
RELS = [
 ("rel-enigmatic-figure-revealed-as-crystal-exarch", "char-enigmatic-figure", "revealed-as", "char-crystal-exarch", L542, None, "main", ["M542d", "M542i", "M542n"]),
 ("rel-crystal-exarch-leads-crystarium", "char-crystal-exarch", "leads", "loc-crystarium", L542, None, "main", ["M542j"]),
 ("rel-lyna-serves-crystal-exarch", "char-lyna", "serves", "char-crystal-exarch", L542, None, "main", ["M542h", "M542p"]),
 ("rel-ardbert-member-of-warriors-of-darkness", "char-ardbert", "member-of", "org-warriors-of-darkness", L544, None, "main", ["M544l", "M544m", "M544n"]),
 ("rel-eulmore-opposes-crystarium", "loc-eulmore", "opposes", "loc-crystarium", L545, None, "main", ["M545c"]),
 ("rel-vauthry-controls-eulmore", "char-vauthry", "controls", "loc-eulmore", L548, None, "main", ["M548d", "M548e"]),
 ("rel-vauthry-controls-sin-eaters", "char-vauthry", "controls", "org-sin-eaters", L553, None, "main", ["M553b"]),
 ("rel-vauthry-opposes-alphinaud", "char-vauthry", "opposes", "char-alphinaud", L553, None, "main", ["M553j", "M553f"]),
 ("rel-tesleen-member-of-sin-eaters", "char-tesleen", "member-of", "org-sin-eaters", L552B, None, "main", ["M552bb", "M552be"]),
 ("rel-estinien-aids-scions", "char-estinien", "aids", "org-scions", L564, None, "main", ["M564j", "M564k"]),
 ("rel-ranjit-serves-vauthry", "char-ranjit", "serves", "char-vauthry", L565, None, "main", ["M565b", "M565f"]),
 ("rel-ryne-prisoner-of-eulmore", "char-ryne", "prisoner-of", "loc-eulmore", L565, L568, "main", ["M565g", "M565r"], ["M568a", "M568b"]),
 ("rel-thancred-aids-ryne", "char-thancred", "aids", "char-ryne", L565, None, "main", ["M565n", "M565o"]),
 ("rel-crystarium-opposes-eulmore", "loc-crystarium", "opposes", "loc-eulmore", L566, None, "main", ["M566b", "M566c"]),
 ("rel-feo-ul-member-of-pixies", "char-feo-ul", "member-of", "org-pixies", L573, None, "main", ["M544k", "M573c"]),
 ("rel-ryne-possessed-by-minfilia", "char-ryne", "possessed-by", "char-minfilia", L574, None, "main", ["M574f", "M574g", "M574h"]),
 ("rel-titania-member-of-sin-eaters", "char-titania", "member-of", "org-sin-eaters", L575, None, "main", ["M575a", "M575b"]),
 ("rel-titania-prisoner-of-pixies", "char-titania", "prisoner-of", "org-pixies", L575, None, "main", ["M575c"]),
 ("rel-nu-mou-aids-urianger", "org-nu-mou", "aids", "char-urianger", L576, None, "main", ["M576a"]),
]

ADJUST = {}

# ---- Arcs ------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-l1-answering-the-summons", "evt-answering-the-summons", L542, L544),
 ("arc-l2-behind-eulmores-gate", "evt-behind-eulmores-gate", L545, L553),
 ("arc-l3-the-inn-at-journeys-head", "evt-the-inn-at-journeys-head", L545B, L553B),
 ("arc-l4-night-over-lakeland", "evt-night-over-lakeland", L563, L564),
 ("arc-l5-the-laxan-loft-rescue", "evt-the-laxan-loft-rescue", L565, L568),
 ("arc-l6-the-pixies-games", "evt-the-pixies-games", L569, L574),
 ("arc-l7-the-sealed-king", "evt-the-sealed-king", L575, L579),
]

CASTS = {
 "evt-answering-the-summons": [
   ("char-tataru", L542, ["M542b"]), ("char-biggs", L542, ["M542c"]), ("char-wedge", L542, ["M542c"]),
   ("char-crystal-exarch", L542, ["M542i"]), ("char-lyna", L542, ["M542g"]), ("loc-the-first", L542, ["M542k"]),
   ("org-sin-eaters", L542, ["M542m"]), ("org-scions", L544, ["M544a"]), ("char-urianger", L544, ["M544g"]),
   ("char-ardbert", L544, ["M544l"]),
 ],
 "evt-behind-eulmores-gate": [
   ("char-alphinaud", L545, ["M545a"]), ("char-crystal-exarch", L545, ["M545a"]), ("loc-eulmore", L545, ["M545b"]),
   ("char-kai-shirr", L548, ["M548b"]), ("char-vauthry", L548, ["M548d"]), ("org-sin-eaters", L551, ["M551a"]),
   ("char-solus", L553, ["M553g"]),
 ],
 "evt-the-inn-at-journeys-head": [
   ("char-alisaie", L545B, ["M545bc"]), ("char-crystal-exarch", L545B, ["M545ba"]), ("char-tesleen", L547B, ["M547ba"]),
   ("org-sin-eaters", L549B, ["M549bc"]), ("char-urianger", L549B, ["M549bf"]),
 ],
 "evt-night-over-lakeland": [
   ("char-crystal-exarch", L563, ["M563a"]), ("char-alphinaud", L563, ["M563c"]), ("char-alisaie", L563, ["M563p"]),
   ("char-lyna", L563, ["M563j"]), ("char-vauthry", L563, ["M563c"]), ("org-sin-eaters", L563, ["M563a"]),
   ("char-estinien", L564, ["M564j"]), ("char-gaius", L564, ["M564l"]),
 ],
 "evt-the-laxan-loft-rescue": [
   ("char-ranjit", L565, ["M565a"]), ("char-crystal-exarch", L565, ["M565c"]), ("char-vauthry", L565, ["M565f"]),
   ("char-ryne", L565, ["M565g"]), ("char-thancred", L565, ["M565o"]), ("char-minfilia", L565, ["M565i"]),
   ("loc-crystarium", L566, ["M566b"]), ("char-lyna", L566, ["M566e"]), ("char-solus", L568, ["M568g"]),
   ("loc-il-mheg", L568, ["M568f"]),
 ],
 "evt-the-pixies-games": [
   ("char-thancred", L569, ["M569f"]), ("char-ryne", L569, ["M569b"]), ("org-pixies", L569, ["M569c"]),
   ("char-urianger", L569, ["M569d"]), ("char-feo-ul", L573, ["M573c"]), ("org-garlean-empire", L573, ["M573f"]),
   ("org-ascians", L574, ["M574b"]), ("char-minfilia", L574, ["M574f"]),
 ],
 "evt-the-sealed-king": [
   ("char-titania", L575, ["M575a"]), ("org-pixies", L575, ["M575c"]), ("char-urianger", L575, ["M575e"]),
   ("char-ardbert", L575, ["M575h"]), ("org-nu-mou", L576, ["M576d"]), ("char-ryne", L578, ["M578a"]),
 ],
}

ARC_NOTES = {
 "arc-l1-answering-the-summons": "MSQ #542 *The Syrcus Trench* to #544 *Travelers of Norvrandt* (5.0): the beacon and the crossing (M542d), the Exarch revealed as the voice (M542i), "
   "the First's history (M543f, M543g), and where the Scions are and why (M544w, M544g). It ends where the story splits into the two #545 chains.",
 "arc-l2-behind-eulmores-gate": "MSQ #545 *In Search of Alphinaud* to #553 *Emergent Splendor*: the Kholusia chain, from the flight to Kholusia (M545a) through the infiltration (M549b) "
   "to Vauthry's tirade and the flight back to the Exarch (M553f, M553i). Its records cite only its own chain and the shared opening.",
 "arc-l3-the-inn-at-journeys-head": "MSQ #545b *In Search of Alisaie* to #553b *Tears on the Sand*: the Amh Araeng chain, from the caravan to Mord Souq (M545be) through Tesleen's death (M552bb, M552be) "
   "to Alisaie's departure for the Crystarium (M553bc). It never cites the Kholusia chain, so a player who takes Amh Araeng first reads nothing from Kholusia in this arc.",
 "arc-l4-night-over-lakeland": "MSQ #563 *The Lightwardens* and #564 *Warrior of Darkness*, where the chains rejoin: the Lightwardens explained (M563a), Lakeland's slain (M563l), and the aftermath, "
   "with Estinien and Gaius in the Source (M564j, M564o). Its name avoids #564's title, which may not appear at #563.",
 "arc-l5-the-laxan-loft-rescue": "MSQ #565 *An Unwelcome Guest* to #568 *The Oracle of Light*: Ran'jit's ultimatum (M565b), the girl Minfilia's history and capture (M565j, M565g), the Crystarium's resolve (M566b) "
   "and the raid (M568a), ending with the flight into Il Mheg (M568f).",
 "arc-l6-the-pixies-games": "MSQ #569 *Il Mheg, the Faerie Kingdom* to #574 *Courting Cooperation*, including the three #570 chores: the pixies' games (M569e), Feo Ul (M573c), Urianger's vision (M573k), "
   "and the Minfilia of old's words to Thancred (M574g). Each chore's recap cites only #569 and its own quest.",
 "arc-l7-the-sealed-king": "MSQ #575 *The Key to the Castle* to #579 *The Lawless Ones*: Titania revealed (M575a), the relics (M575d), the Nu Mou's patronage (M576f), and the girl's confession and Titania's voice (M579d, M579h). "
   "It ends at #579, the last step this era may start a record on; the scepter and the shoes are still to come.",
}

DECISIONS = [
 "**Seven arcs (l1–l7)** cover every step from #542 to #579 without sharing steps; the two #545 chains are arcs of their own (l2, l3), and the three #570 chores sit inside l6.",
 "**The voice → the Crystal Exarch** follows the Marques → Cid pattern: `char-enigmatic-figure` gets a last presentation at #542 and a `revealed-as` edge to the new `char-crystal-exarch`, who carries \"The enigmatic figure\" as an alias. "
   "#542's Journal has the voice call you through the beacon, and the Exarch thanks you for answering his summons; #544 adds that his summons also drew the Scions' souls.",
 "**The girl called Minfilia** is `char-ryne` (the id parts 2 and 3 use) (\"Minfilia of the First\", alias \"Minfilia\"), from #565, where Lyna and the Journal first name her; the #564 cutscene shows her unnamed. "
   "`char-minfilia` gains the alias \"the Oracle of Light\" at #565, and at #574 the girl is `possessed-by` her (the Oracle calls the girl a vessel she has used). Her later name is not used.",
 "**Emet-Selch stays out:** #568 shows that name only as a speaker tag, while the stage directions of #553 and #568 name the watcher \"Solus zos Galvus\"; the watcher's records go to `char-solus`.",
 "**Parallel chains:** no record on #545–#553 cites #545b–#553b or the reverse; records begun at #546–#553 (Alphinaud, Eulmore, Vauthry, sin eaters) stay visible on the Alisaie chain because the timeline orders it later. "
   "The sin eaters get a fresh, Eulmore-free presentation at #549b for that reason.",
 "**Quest titles:** #564 *Warrior of Darkness* comes after #552b and #563, so Tesleen's folk tale is described, and #563 uses the Exarch's own \"Warriors of Darkness\". *Il Mheg, the Faerie Kingdom* (#569) is avoided before #569.",
 "**Ardbert** is a member of the Warriors of Darkness from #544, where he names himself and says his comrades and he caused the Flood; his \"Warrior of Darkness\" line there is a choice branch and stays out. "
   "His #564 lines about following you are branches too; only his main-line words are used.",
 "**Titania** goes by \"they\", as the pages do, and is `prisoner-of` the pixies (sealed by the fae, #575) and `member-of` the sin eaters as a Lightwarden.",
 "**Left out as entities** (in text only, or not at all): the Crystal Tower, Norvrandt, Kholusia, Amh Araeng, Lakeland, Gatetown, Mord Souq, the Inn at Journey's Head, Laxan Loft, Lyhe Ghiah, Voeburt, the Chais, Tristol, "
   "Szem Djenmai, Cassard, Moren, Katliss, Bragi, Halric, Sul Uin, Ys Iala, Oul Sigun, the Fuath, Wyd Aenc, Marn Ose, Ys Gyuf, Wyd Lad, Black Rose.",
]

# Banned terms this era's text needs, from the first step whose pages establish them (spoken or shown, not a speaker tag):
ALLOW = {
 "Exarch": L542,           # the Exarch names his own title, "Crystal Exarch", in The Syrcus Trench
 "The First": L542,        # the Exarch: "one of the thirteen reflections or shards─the First"
 "Oracle of Light": L543,  # Moren tells the tale of the Oracle of Light in City of the First
 "Lightwarden": L563,      # the Exarch explains the Lightwardens in The Lightwardens
}
