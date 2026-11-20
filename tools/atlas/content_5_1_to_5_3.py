"""Atlas content for patches 5.1–5.3 (and the first two 5.4 quests), MSQ #648 Shaken Resolve to #681 The Wisdom of Allag.
Arc tag o. Data only (docs/atlas/era-modules.md is the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes B16–B22); every locator is an exact substring of a
quest's Journal, Steps or main dialogue (stage directions inside cutscenes included). Spoiler rules this module follows:
  - the Shadowbringers cast reuses the contract's conventional IDs (char-graha-tia for the Crystal Exarch's revealed
    identity, char-ryne, char-lyna, char-ardbert, char-emet-selch, char-hythlodaeus, char-elidibus) plus first-name IDs for
    the 5.0 people this era carries on (char-chai-nuzz, char-dulia-chai, char-kai-shirr, char-halric, char-runar,
    char-seto, loc-eulmore); each first presentation here stands on its own as of its step;
  - the Exarch's story is carried by char-graha-tia (alias "The Crystal Exarch"), the identity 5.0 reveals; text calls him
    "the Crystal Exarch" or "the Exarch", as the pages do, until #679, where the pages name G'raha Tia as the youth who
    joins the Scions;
  - Elidibus wearing Ardbert's body is a possession, not a second entity: the player sees him in that body at #657, so the
    impostor of #661 needs no reveal edge (char-ardbert possessed-by char-elidibus, #657 to #675);
  - the white-robed figure (#657, #667) is revealed as Fandaniel at #679, wearing Asahi's body: Marques → Cid pattern;
  - first names and titles only: no "Baelsar", "yae Galvus", "Aldynn" (Raubahn's surname in "Commander Aldynn"), "Hext",
    "Brutus"; minor people are named in text only (Riol, Mowen, Hathenbet, Tolshs Aath, Almet, Tiuna, Bismarck, Ken,
    Theyler, Vonard, Moren, Riqi-Tio, Eirwel, Rammbroes, Owen) or not at all;
  - ALLOW proposes Exarch, Ryne and "The First" from #648, Zodiark from #657, Emet-Selch from #661, Venat from #666,
    Hythlodaeus from #673 and Fandaniel from #679 (the first step in this era whose pages establish each).
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

(O648, O649, O650, O651, O652, O653, O654, O655, O656, O657, O658, O659, O660, O661, O662, O663, O664, O665, O666, O667,
 O668, O669, O670, O671, O672, O673, O674, O675, O676, O677, O678, O679, O680, O681) = (f"cp-msq-{n}" for n in range(648, 682))

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #648 Shaken Resolve
 "M648a": ("You tell Tataru and F'lhaminn of Minfilia's sacrifice and of Ryne, the girl who carries on her legacy.", "Shaken Resolve", "of Minfilia's sacrifice, and of the young girl Ryne who now carries on her legacy."),
 "M648b": ("Riol has had no word from Tataru's helper in the Empire and will sneak in himself.", "Shaken Resolve", "Fearing the worst, Riol is resolved to sneak into the Empire himself in the hopes he might finally make contact."),
 "M648c": ("Krile finds the link between the stricken Scions' bodies and souls weakening.", "Shaken Resolve", "the tenuous link between their bodies and their souls is weakening."),
 "M648d": ("Thancred shows the most notable signs, followed by Y'shtola and Urianger.", "Shaken Resolve", "Thancred exhibits the most notable signs, followed by Y'shtola and Urianger."),
 "M648e": ("Krile will consult Matoya on keeping their bodies' aether stable.", "Shaken Resolve", "she will consult Master Matoya on a means to maintain the stability of their corporeal aether for as long as possible."),
 "M648f": ("The Scions plan to pour their spirits into auracite so you can carry them back to the Source.", "Shaken Resolve", "to pour their spirits into auracite, theoretically enabling you to bear them safely across the rift and back to the Source"),
 "M648g": ("The Crystal Exarch may know someone who can help.", "Shaken Resolve", "Luckily, the Crystal Exarch may know of someone who can help."),
 "M648h": ("The Exarch's spell, meant for you, found those close to you and summoned them incomplete.", "Shaken Resolve", "Instead of you, the spell found those close to you, and ended up summoning them in their incomplete state..."),
 "M648j": ("Krile is glad the Exarch never had the chance to see his plan through.", "Shaken Resolve", "His plan might well have worked, but I for one am glad he never had the opportunity to see it through."),
 "M648k": ("Krile calls the Exarch Raha, always a reckless young fool.", "Shaken Resolve", "Raha always was a reckless young fool..."),
 "M648l": ("Thancred and Ryne are pursuing their investigation of the Empty.", "Shaken Resolve", "they beg leave to pursue their investigation of the Empty to its conclusion."),
 # #649 A Grand Adventure
 "M649a": ("Urianger stays behind to fashion white auracite.", "A Grand Adventure", "Urianger, however, begs permission to work on fashioning white auracite instead"),
 "M649c": ("At its heart you find Beq Lugg, the Exarch's promised master of soulcraft.", "A Grand Adventure", "the presence of Beq Lugg, the Exarch's promised master of soulcraft."),
 "M649d": ("The Seeker of Solitude reverts to their Nu Mou form.", "A Grand Adventure", "The Seeker of Solitude reverts back to their Nu Mou form."),
 "M649e": ("Beq Lugg hid from the world of men to escape such temptation.", "A Grand Adventure", "It was to escape such words of temptation that I hid myself from the world of men..."),
 "M649f": ("A court mage's good intentions and Beq Lugg's naivety once cost countless innocent lives.", "A Grand Adventure", "That damned court mage seemed to have the best of intentions too, and countless innocents died for my naivety!"),
 "M649g": ("The Exarch tells Beq Lugg that his comrades' souls are in danger.", "A Grand Adventure", "Our comrades' very souls are in danger."),
 "M649h": ("Beq Lugg gives in, and a deal is struck.", "A Grand Adventure", "the Nu Mou inevitably gives in to the inveigling words of your companions, and a deal is struck."),
 # #650 A Welcome Guest
 "M650a": ("Beq Lugg learns that the Scions hail from another world.", "A Welcome Guest", "But that you hail from another world as well!?"),
 "M650b": ("Beq Lugg agrees to help.", "A Welcome Guest", "I will. I would see my knowledge put to good use for a change."),
 "M650c": ("The Scions' souls could become immutable to transference.", "A Welcome Guest", "They could very well become immutable to transference, never to be restored to their bodies."),
 "M650d": ("Halric's soul is too far gone, his mind held together by the finest of threads.", "A Welcome Guest", "The boy's soul is too far gone, his mind held together by the finest of threads."),
 "M650e": ("With night restored, the Light's corruption of the patients will grow no further.", "A Welcome Guest", "with the restoration of night, the corrupting influence of Light will no longer grow."),
 "M650f": ("Beq Lugg's soul tonic came to be used by the knights of Voeburt.", "A Welcome Guest", "After some refinement, it came to be used by the knights of Voeburt."),
 "M650g": ("The most severely afflicted show no response to the tonic, Alisaie reports.", "A Welcome Guest", "The more severely afflicted show no response."),
 "M650h": ("Treating the patients might teach something of the Scions' own predicament.", "A Welcome Guest", "we might learn something of relevance to your own predicament..."),
 # #651 Good for the Soul
 "M651a": ("Beq Lugg needs pure water, fine clay and a fae lantern.", "Good for the Soul", "The purest of waters and finest of clays, as well as a fae lantern brimming with pixie magick."),
 "M651b": ("Beq Lugg's knowledge once brought a plague like none seen before.", "Good for the Soul", "A plague the like of which none had ever seen."),
 "M651d": ("The familiar's power lies in what its maker believes it embodies.", "Good for the Soul", "Which is why the only thing of import is what you believe this figure embodies."),
 "M651e": ("Stirred by the familiar, Halric manages a few words.", "Good for the Soul", "M... Mother... I..."),
 "M651f": ("Beq Lugg believes a spell could induce stagnation for the Scions.", "Good for the Soul", "I believe I can fashion a spell to produce the opposite effect."),
 "M651g": ("Alisaie thinks the method could help Ga Bu, whose soul was suffused with Titan's aether.", "Good for the Soul", "the only difference being that his soul was suffused with earth-aspected aether from summoning Titan, rather than Light."),
 "M651h": ("Kai-Shirr brings word that the future of Eulmore is at stake.", "Good for the Soul", "Sorry for bothering you and all that, but she says the future of Eulmore's at stake."),
 "M651i": ("The magick works best when its invoker knows the patients and wishes to help them.", "Good for the Soul", "A deep understanding of the subjects' physical state, combined with a strong desire to help them, can drastically increase the magick's effect."),
 "M651j": ("Kai-Shirr says Lady Chai is beside herself.", "Good for the Soul", "There's trouble back in Eulmore. Lady Chai's beside herself."),
 # #652 Nowhere to Turn
 "M652a": ("Kai-Shirr brings you to Lady Chai in her parlor.", "Nowhere to Turn", "Lady Chai's up in the parlor. Best not keep her waiting, eh?"),
 "M652b": ("Eulmore's mayorship fell to her husband.", "Nowhere to Turn", "the mayorship fell upon my dear husband."),
 "M652c": ("With Lord Vauthry gone, a new leader had to be chosen, and no one volunteered to stand.", "Nowhere to Turn", "With Lord Vauthry out of the way, we all agreed that a new leader must be chosen... … Not a single person volunteered to stand, you see."),
 "M652d": ("Shortly after, he vanished without a word.", "Nowhere to Turn", "For shortly after that, he vanished without a word..."),
 "M652e": ("Lady Chai fears she pushed him too hard.", "Nowhere to Turn", "But perhaps I was too forceful in my attempt to encourage him."),
 "M652f": ("Alphinaud is convinced he has not fled.", "Nowhere to Turn", "The one thing he has not done is flee"),
 "M652g": ("Alphinaud promises to find him.", "Nowhere to Turn", "Wherever he may have gone, rest assured we will find him."),
 "M652h": ("Chai had proven himself at Daedalus Stoneworks.", "Nowhere to Turn", "But even before then, he had proven himself at Daedalus Stoneworks, don't forget."),
 # #653 A Notable Absence
 "M653a": ("Chai worried about Eulmore's neglect of industry.", "A Notable Absence", "Concerned about Eulmore's neglect of industry, you see."),
 "M653b": ("Many of Eulmore's soldiers are still recovering from your confrontation with Lord Vauthry.", "A Notable Absence", "Many of our men are still recovering after your confrontation with Lord Vauthry"),
 "M653c": ("The guard proposed filling its ranks with volunteers from the Derelicts and Gatetown.", "A Notable Absence", "funding permitting, I proposed replenishing our ranks with volunteers from the Derelicts and Gatetown."),
 "M653d": ("Chai was last seen heading for Gatetown.", "A Notable Absence", "Looked like he was headed for Gatetown when I last saw him."),
 "M653e": ("He discussed admitting customers from outside Eulmore to the Queen Bee.", "A Notable Absence", "They discussed the possibility of granting admission to customers from outside Eulmore"),
 # #654 For the People
 "M654a": ("You, Alphinaud and Kai-Shirr split up to search Kholusia.", "For the People", "Gatetown I leave to you, Kai-Shirr."),
 "M654b": ("Chai is set on salvaging goodwill among Kholusia's settlements, and Amity is his likely destination.", "For the People", "He seems determined to salvage what goodwill might yet remain among the settlements of Kholusia, the only likely place he has left to go being Amity."),
 "M654d": ("Chai has been asking about the people's grievances.", "For the People", "you have been inquiring about the people's grievances."),
 "M654e": ("Chai will not take office until he has secured resources.", "For the People", "Tackling our many challengers will require resources, and until I have secured them, it would not be right to assume the role of mayor."),
 "M654f": ("Wrenden's values fell out of favor in Lord Vauthry's paradise.", "For the People", "But in time, my values fell out of favor. There was no need for them in this paradise Vauthry was creating."),
 "M654g": ("Wrenden would first see Chai solve one problem on his own.", "For the People", "You ask me to help you solve Eulmore's problems, but first, I would see you solve one on your own."),
 "M654h": ("Chai is heir to Daedalus Stoneworks, and Talos are his field.", "For the People", "Well, as the heir to Daedalus Stoneworks, it just so happens that Talos are my field of expertise."),
 "M654j": ("Wrenden was chief advisor to Lord Vauthry's father.", "For the People", "He served as chief advisor to Vauthry's father when he was in office."),
 "M654k": ("Kai-Shirr asks to come along.", "For the People", "If you let me come with you, that is."),
 # #655 Finding Good Help
 "M655a": ("Chai proposes capturing the abandoned Talos that roam Kholusia.", "Finding Good Help", "Chai-Nuzz proposes capturing the long-abandoned Talos which wander the wilds of Kholusia."),
 "M655b": ("His canisters can halt the flow of aether in a Talos.", "Finding Good Help", "capable of halting the flow of aether in a Talos."),
 "M655c": ("Chai subdues three Talos himself.", "Finding Good Help", "succeeding at length in subduing a trio of Talos."),
 "M655d": ("Lady Chai is near speechless at the sight of her husband.", "Finding Good Help", "Among them, you spy Lady Chai, who is near speechless at the sight of her husband."),
 "M655e": ("Wrenden judges Chai more than qualified to be mayor.", "Finding Good Help", "You, sir, are more than qualified to be the next mayor of Eulmore."),
 "M655f": ("Chai admits he is ignorant of politics and asks Wrenden's counsel.", "Finding Good Help", "I thank you for your vote of confidence, but the fact remains, I am wholly ignorant of the world of politics."),
 # #656 Moving Forward
 "M656a": ("Chai was chosen in an election to succeed Lord Vauthry.", "Moving Forward", "I had the honor of being chosen to succeed Lord Vauthry."),
 "M656b": ("He does not mean to hold the post indefinitely.", "Moving Forward", "Let it be known that I do not intend to hold this post indefinitely."),
 "M656c": ("Lord Vauthry's systems must be undone.", "Moving Forward", "The systems put in place by Lord Vauthry must be undone."),
 "M656d": ("He proposes an open forum on Eulmore's future.", "Moving Forward", "And so I propose that an open forum be held, that we might all discuss how best to strive towards a better future."),
 "M656e": ("Food, relations with neighbors and industry come first.", "Moving Forward", "Securing new sources of food, rebuilding relations with our neighbors, re-establishing industry"),
 "M656g": ("Alphinaud judges it time for the Scions to go their own way.", "Moving Forward", "I have every confidence they will find their way, and I believe it is time we went on ours."),
 "M656h": ("Kai-Shirr wants to be part of the new Eulmore.", "Moving Forward", "And I reckon I want to be a part of it."),
 # #657 Vows of Virtue, Deeds of Cruelty
 "M657a": ("The Scions conclude white auracite is ill-suited to their purpose.", "Vows of Virtue, Deeds of Cruelty", "concluded at length that white auracite was ill-suited for our purposes."),
 "M657b": ("Their original plan would have broken the link between mind and soul.", "Vows of Virtue, Deeds of Cruelty", "their original plans would inevitably have broken the link between mind and soul."),
 "M657c": ("Estinien brings troubling tidings from the Empire.", "Vows of Virtue, Deeds of Cruelty", "by the elusive Estinien, who brings troubling tidings from the Empire."),
 "M657d": ("Estinien met Gaius, who styles himself Shadowhunter, in a provincial factory.", "Vows of Virtue, Deeds of Cruelty", "It was then, inside a provincial factory, that I encountered the one who styles himself Shadowhunter."),
 "M657e": ("Zenos's soul lives on, and he has wrested back his flesh.", "Vows of Virtue, Deeds of Cruelty", "But his soul lives on. And he has wrested back his flesh."),
 "M657f": ("Zenos murdered his father, and the Emperor is dead.", "Vows of Virtue, Deeds of Cruelty", "For no sooner had we arrived than he murdered his sire in cold blood. The Emperor is dead."),
 "M657g": ("The Echo shows a machine much like the Ultima Weapon.", "Vows of Virtue, Deeds of Cruelty", "an encounter with a mechanical monstrosity bearing a striking resemblance to the Ultima Weapon."),
 "M657h": ("Conquest is no longer Gaius's objective.", "Vows of Virtue, Deeds of Cruelty", "Conquest is no longer his objective."),
 "M657i": ("Imperial soldiers fight over who will take the throne.", "Vows of Virtue, Deeds of Cruelty", "Traitors! You would dare deny Lord Nerva the throne!?"),
 "M657j": ("A white-robed figure tells Zenos he knows the prey Zenos will seek next.", "Vows of Virtue, Deeds of Cruelty", "For I know full well the prey you would seek next."),
 "M657k": ("Elidibus appears, possessing Ardbert's body.", "Vows of Virtue, Deeds of Cruelty", "Elidibus, possessing Ardbert's body, appears."),
 "M657l": ("Elidibus would see a feeble flame of hope rekindled.", "Vows of Virtue, Deeds of Cruelty", "So long as I yet live, I would see that feeble flame rekindled."),
 "M657m": ("His contract with Tataru fulfilled, Estinien leaves.", "Vows of Virtue, Deeds of Cruelty", "His contract with Tataru thus fulfilled, your old friend gruffly takes his leave"),
 "M657n": ("Estinien judges the Empire no threat for now; where Zenos will resurface is unknown.", "Vows of Virtue, Deeds of Cruelty", "concluding at length that the Empire poses no threat for the present, though it remains to be seen where Zenos will next resurface."),
 "M657o": ("The Scions in the First pursue another solution.", "Vows of Virtue, Deeds of Cruelty", "your comrades have decided to pursue an alternative solution"),
 "M657p": ("You and Krile see Estinien's memories through the Echo.", "Vows of Virtue, Deeds of Cruelty", "both you and Krile are overcome by the power of the Echo."),
 "M657q": ("The Scions realized auracite would weaken the link perilously.", "Vows of Virtue, Deeds of Cruelty", "be weakened most perilously in the process of rendering our souls dormant, as auracite doth require."),
 # #658 Old Enemies, New Threats
 "M658a": ("Maxima, a former Garlean ambassador, remains in Eorzea under Commander Raubahn.", "Old Enemies, New Threats", "Maxima, former Garlean ambassador. I remain here in Eorzea under the auspices of Commander Aldynn"),
 "M658b": ("The Alliance's main host has withdrawn, leaving the Resistance to watch the border.", "Old Enemies, New Threats", "the main host of the Alliance has withdrawn, leaving the Ala Mhigan Resistance to keep watch over the border."),
 "M658c": ("Gaius and Estinien, the only witnesses to the murder, had to flee.", "Old Enemies, New Threats", "Being the sole witnesses to this crime, and in no position to defend our innocence, we were then forced to flee"),
 "M658d": ("The Empire is developing a new Ultima Weapon.", "Old Enemies, New Threats", "The Empire is developing a new Ultima Weapon."),
 "M658e": ("The work is secret research by the VIIth Imperial Legion.", "Old Enemies, New Threats", "primarily through secret research conducted by the VIIth Imperial Legion, it would seem."),
 "M658f": ("Gaius once sought to harness the Ultima Weapon and became the Ascians' pawn.", "Old Enemies, New Threats", "In my foolishness, I sought to harness its power─and became the Ascians' pawn in so doing."),
 "M658g": ("One of several prototypes is on its way to Eorzea.", "Old Enemies, New Threats", "a number of prototypes have been produced...and that one of them is on its way to Eorzea."),
 "M658h": ("Raubahn asks for your strength when your comrades can spare you.", "Old Enemies, New Threats", "I bid you lend us your strength."),
 "M658k": ("The Resistance is strengthening its presence in the Ghimlyt Dark and assembling a force.", "Old Enemies, New Threats", "we've begun to strengthen our presence in the Ghimlyt Dark, and are assembling a force to meet the coming threat."),
 # #659 The Way Home
 "M659a": ("The Exarch has made a breakthrough on a means to return the Scions home.", "The Way Home", "I've made something of a breakthrough in my research on the soul and a means to return the Scions home."),
 "M659b": ("The spirit vessel is an ark for soul and mind, to ferry them between worlds.", "The Way Home", "An ark for soul and mind both, that will allow your incorporeal self in its entirety to be ferried between worlds..."),
 "M659c": ("The gift of passing on memory lives only in the blood of the Allagan emperors.", "The Way Home", "A gift that lives on only through the blood of the Allagan emperors...which certainly does not flow within auracite, or any other crystal."),
 "M659d": ("The vessel can hold mind and memory but cannot yet receive them.", "The Way Home", "Though the vessel is possessed of the requisite qualities to hold mind and memory"),
 "M659e": ("The Exarch must change the process or let his blood permeate the vessel.", "The Way Home", "or determine a means by which my blood may permeate the vessel."),
 "M659f": ("With the Emperor slain and Zenos returned, Garlemald is unpredictable.", "The Way Home", "With the Emperor slain and Zenos returned, it is impossible to predict how matters will unfold in Garlemald."),
 "M659g": ("Lyna hopes to speak with you.", "The Way Home", "I had hoped to speak with the Warrior of Darkness."),
 "M659h": ("Alphinaud offers to help Lyna.", "The Way Home", "I may yet be of some use to Lyna."),
 # #660 Seeking Counsel
 "M660a": ("Lyna asks your help slaying a sin eater in Lakeland.", "Seeking Counsel", "A sin eater has been sighted in Lakeland, and I ask for your assistance in slaying it."),
 "M660d": ("The sin eater's slayer called himself a Warrior of Light.", "Seeking Counsel", "No, I'm a Warrior of Light."),
 "M660e": ("The Exarch told Lyna the truth of Ardbert and his comrades.", "Seeking Counsel", "The Exarch told me the truth of Ardbert and his comrades' deeds"),
 "M660f": ("Since returning from the tempest, the Exarch is not as he was.", "Seeking Counsel", "Since he returned from the tempest, the Exarch is... not as he was."),
 "M660g": ("He seems a younger man.", "Seeking Counsel", "He seems a different man. A ''younger'' man."),
 "M660i": ("Lyna is a captain.", "Seeking Counsel", "Alphinaud is eager to assist Captain Lyna."),
 # #661 Facing the Truth
 "M661a": ("Alphinaud proposes telling the Crystarium the truth.", "Facing the Truth", "If the people of the Crystarium seek the truth, I say we give it to them."),
 "M661b": ("The books call the Warriors of Light sin eaters or worse.", "Facing the Truth", "nearly everything I've come across describes them as sin eaters or worse."),
 "M661c": ("Only the story that the Warriors caused the Flood remained.", "Facing the Truth", "only one truth remained─that they were the cause of the Flood."),
 "M661d": ("Ardbert appears in the crowd, calling himself a Warrior of Light.", "Facing the Truth", "People of the Crystarium! I am Ardbert, one of those you know as a Warrior of Light."),
 "M661e": ("He says the will of the star brought him back.", "Facing the Truth", "he proclaims it was the will of the star that brought him back from the beyond"),
 "M661f": ("He urges the people to rise themselves.", "Facing the Truth", "The time to rely on saviors from afar has passed. It is ''you'' who must rise."),
 "M661h": ("The Scions conclude it is an Ascian ploy, and only Elidibus remains to employ it.", "Facing the Truth", "The Scions conclude that it must be an Ascian ploy, and to your knowledge only Elidibus remains to employ such a tactic."),
 "M661i": ("Given Emet-Selch's demise, this must be an impostor.", "Facing the Truth", "Considering the events leading to Emet-Selch's demise, there is no question you have been faced with an imposter."),
 "M661j": ("Urianger advises watching from a distance.", "Facing the Truth", "Let the rest of us maintain an inconspicuous distance─for the present, at least."),
 # #662 A Sleep Disturbed
 "M662a": ("The Exarch has no doubt he is an impostor.", "A Sleep Disturbed", "He is an impostor, of that there is no doubt."),
 "M662b": ("Almet and her sisters found unexplored chambers in the Qitana Ravel.", "A Sleep Disturbed", "Almet and her sisters have discovered hitherto unexplored chambers in the Qitana Ravel that may offer new insight into the Ascians and their motives."),
 "M662c": ("The archmage Tiuna is said to have had a gift like the Echo.", "A Sleep Disturbed", "it is said she was possessed of a gift suspiciously similar to the Echo."),
 "M662d": ("The mural says that gift awoke after a starshower.", "A Sleep Disturbed", "Its inscription suggests this ability was awakened after beholding a starshower."),
 "M662e": ("Y'shtola links the mural to what Emet-Selch showed you in Amaurot.", "A Sleep Disturbed", "Moreover, does it not recall that which Emet-Selch invited us to witness in Amaurot?"),
 "M662g": ("You find the tomb of the archmage Tiuna, a hero of Ronka.", "A Sleep Disturbed", "Within the innermost reaches of the ruins you discover the tomb of the archmage Tiuna, a legendary hero of Ronka."),
 # #663 An Old Friend
 "M663a": ("The false Ardbert slays a nearby sin eater before visiting any town.", "An Old Friend", "Before visiting any towns or villages, Ardbert would hunt down and slay a nearby sin eater to earn the locals' trust."),
 "M663b": ("Halric's treatment goes well but slowly.", "An Old Friend", "Their treatment is going well, but progress is slow and exhausting─for all of us."),
 "M663c": ("Thancred and Ryne are back from the Empty and searching too.", "An Old Friend", "Thankfully, Thancred and Ryne are returned from the Empty and have taken up the search."),
 "M663d": ("The impostor admits he is Elidibus.", "An Old Friend", "Yes, it is I, Elidibus."),
 "M663e": ("Elidibus enacts the will of the Convocation.", "An Old Friend", "I seek to enact the will of the Convocation, of course."),
 "M663f": ("Alphinaud recalls Emet-Selch's last words.", "An Old Friend", "“Remember that we once lived,” he said."),
 "M663g": ("Elidibus sees no common ground with the Scions.", "An Old Friend", "There is no common ground to be found between you and I."),
 "M663h": ("Alphinaud believes Elidibus's objective is the Rejoining.", "An Old Friend", "And 'tis safe to say his objective is the Rejoining."),
 # #664 Deep Designs
 "M664a": ("The benthos have pillaged the Ondo's stores of mnyiri liver.", "Deep Designs", "Rather than hunt for their own meals, the benthos have pillaged our stores of mnyiri liver."),
 "M664b": ("The benthos have raided Kholusian storehouses too.", "Deep Designs", "it seems the benthos have been raiding Kholusian storehouses as well as those of the Ondo."),
 "M664d": ("The benthos would build an army for revenge on the finless.", "Deep Designs", "They seek to build an army, and with it take revenge upon the finless."),
 "M664e": ("The ruins are key to the benthos' plans.", "Deep Designs", "I believe that the ruins are, in fact, key to the benthos' plans."),
 "M664f": ("The ruins lie deep within the illuminated land, newly discovered.", "Deep Designs", "These ruins, which lie deep within the illuminated land, are a recent discovery."),
 "M664g": ("Urianger would call on another's help to go deeper.", "Deep Designs", "If what we seek lieth deeper still, beyond Amaurot, I would call upon the assistance of another..."),
 "M664h": ("Tolshs Aath is chieftain of the Ondo.", "Deep Designs", "As chieftain, he is doubtless privy to a great many secrets."),
 # #665 A Whale's Tale
 "M665a": ("Urianger leads the Scions to seek an audience with Bismarck once more.", "A Whale's Tale", "Aye, I speak of Bismarck. Pray follow me to Sullen that we might seek an audience with him once more."),
 "M665b": ("Bismarck asks that his underbelly be cleansed of barnacles.", "A Whale's Tale", "Bismarck hath asked us to cleanse his underbelly of barnacles."),
 "M665c": ("A man named Ken made a home on Bismarck's back.", "A Whale's Tale", "He came and made a home on my back. Ken was his name."),
 "M665e": ("Ken died less than a century ago, yet history has forgotten him.", "A Whale's Tale", "He passed not even one hundred years ago, yet the truth has slipped from history."),
 "M665g": ("They must press on to bring Elidibus's schemes to light.", "A Whale's Tale", "We must needs press on if we are to bring Elidibus's schemes to light."),
 "M665h": ("Urianger dealt with the Fuath to learn his water magick.", "A Whale's Tale", "To perfect this magick I went so far as to deal with the Fuath"),
 # #666 Beneath the Surface
 "M666a": ("Bismarck carries you deep into the illuminated land.", "Beneath the Surface", "allow him to take you deep into the illuminated land, where secrets of the past yet slumber."),
 "M666b": ("Rukshs Deem is vanquished.", "Beneath the Surface", "and with Rukshs Deem vanquished, they are yours for the taking."),
 "M666c": ("A device shows ancients summoning Hydaelyn, led by Venat.", "Beneath the Surface", "regarding the summoning of Hydaelyn, of all things, which was apparently spearheaded by a personage named Venat."),
 "M666d": ("Venat became Hydaelyn's heart, and Elidibus Zodiark's.", "Beneath the Surface", "reveals this Venat became Hydaelyn's heart... and Elidibus, Zodiark's."),
 "M666e": ("Venat alone might serve as Her heart to oppose Him.", "Beneath the Surface", "If Hydaelyn is to stand a chance of opposing Him, I am the only one who might suffice as Her heart."),
 "M666f": ("Venat vows not to vanish from the world.", "Beneath the Surface", "I shall not vanish from this world. The form I take shall ever remain my choice."),
 "M666g": ("Urianger wonders whether the Elidibus you know is a successor.", "Beneath the Surface", "Perchance the Elidibus at Zodiark's heart and the emissary with whom we are acquainted be not one and the same, but predecessor and successor."),
 "M666h": ("Y'shtola stays in Anamnesis Anyder to coax more from the device.", "Beneath the Surface", "The group trusts to Y'shtola to remain in Anamnesis Anyder and coax out more from the facility"),
 "M666i": ("You are left confounded by Elidibus's true identity.", "Beneath the Surface", "you are left confounded as to the true identity of Elidibus, who by rights should have long since ceased to be."),
 # #667 Echoes of a Fallen Star
 "M667a": ("The false Ardbert's words have kindled heroic zeal in the people.", "Echoes of a Fallen Star", "It seems the words of “Ardbert” have had the intended effect, kindling such heroic zeal in the people"),
 "M667b": ("Elidibus proclaims those who hear the call Warriors of Light.", "Echoes of a Fallen Star", "Elidibus appears, proclaiming to those who hear it that they, too, are Warriors of Light"),
 "M667c": ("The meteors were his illusion.", "Echoes of a Fallen Star", "he does confirm that the meteors were an illusion of his own making."),
 "M667d": ("He woke the gift by rekindling memory, as Hydaelyn does for new minions.", "Echoes of a Fallen Star", "Through the rekindling of memory, I have awoken the ability—just as Hydaelyn is wont to do when She has need of new minions."),
 "M667f": ("Thancred will keep watch over Elidibus.", "Echoes of a Fallen Star", "Thancred proposes he use his ample experience in subterfuge to keep watch over Elidibus, and all readily agree."),
 "M667h": ("The vessel may need the Exarch's blood after all.", "Echoes of a Fallen Star", "we may need to devise a way to infuse the vessel with my blood after all"),
 "M667i": ("The Exarch feels pain in his crystallized arm.", "Echoes of a Fallen Star", "The Exarch feels a pain in his crystallized right arm."),
 "M667j": ("The white-robed figure says precious few remember the Final Days.", "Echoes of a Fallen Star", "Could Emet-Selch have found a way...? Precious few possess memories of the Final Days."),
 "M667k": ("Elidibus vanishes with an ominous promise to save the world.", "Echoes of a Fallen Star", "With an ominous promise to save the world, he vanishes"),
 "M667l": ("Beq Lugg and the Exarch are developing a way to move memory into spirit vessels.", "Echoes of a Fallen Star", "confident though Beq Lugg and the Exarch are of developing a means to transfer memory into spirit vessels"),
 "M667m": ("Zenos has always dreamed of fire falling and the world ablaze.", "Echoes of a Fallen Star", "I have always dreamed of it... Fire falling from the heavens, and the city─nay, the whole world ablaze."),
 "M667n": ("The illusion was meant to wake what is left in the people's sundered souls.", "Echoes of a Fallen Star", "A convenient illusion apt to awaken what little is left of the power that once resided in your sundered souls."),
 # #668 In the Name of the Light
 "M668b": ("After the Flood, the title came to revile rather than exalt.", "In the Name of the Light", "In the wake of the Flood, however, Light came to be regarded with fear; the title used not to exalt, but to revile."),
 "M668c": ("Many have been hailed as Warriors of Light in Vrandtic history.", "In the Name of the Light", "many individuals have been hailed as Warriors of Light throughout Vrandtic history"),
 "M668d": ("Alphinaud posits Hydaelyn is the common thread.", "In the Name of the Light", "posits that Hydaelyn is likely the common thread."),
 "M668e": ("Riqi-Tio wants to be an apothecary who heals people.", "In the Name of the Light", "No, I want to be the kind that fights with potions and heals people! An apothecary!"),
 "M668f": ("Elidibus only gave the wish to help a name.", "In the Name of the Light", "Elidibus did no more than give it a name."),
 "M668g": ("Alphinaud will not leave until Elidibus is dealt with.", "In the Name of the Light", "I cannot leave in good conscience—not until we have dealt with Elidibus."),
 # #669 Heroic Dreams
 "M669c": ("Alisaie will stay fractured rather than don an Ascian mask.", "Heroic Dreams", "But lest you worry, I'm perfectly happy to ''remain'' fractured and have no intention of donning an Ascian mask."),
 "M669d": ("Elidibus accuses you of murdering his brothers.", "Heroic Dreams", "You who have murdered my brothers"),
 "M669e": ("Emet-Selch mistook you for another, Elidibus says.", "Heroic Dreams", "As if he mistook you for another."),
 "M669f": ("The crystal is the tower compensating the Exarch for his demands on it.", "Heroic Dreams", "It is the tower's way of compensating me for the demands I have placed on it."),
 "M669g": ("The Exarch has a plan and will ask one more favor of you.", "Heroic Dreams", "Needless to say, I have a plan. And...when all is said and done, I will ask yet another favor of you."),
 "M669h": ("Elidibus vows to strike you down.", "Heroic Dreams", "I will strike you down..."),
 "M669i": ("Alisaie wishes she knew what Elidibus is plotting.", "Heroic Dreams", "I just wish we knew what Elidibus was plotting..."),
 "M669j": ("Ryne brings word that Thancred has collapsed.", "Heroic Dreams", "It's Thancred! He's collapsed!"),
 # #670 Fraying Threads
 "M670a": ("Thancred collapsed after returning to the Crystarium.", "Fraying Threads", "Ryne informs you and the Exarch that Thancred collapsed shortly after returning to the Crystarium."),
 "M670b": ("He has been unwell since he rescued Urianger from drowning.", "Fraying Threads", "He reveals that he has not been in the best of health since plucking Urianger from a watery grave"),
 "M670c": ("The link between his body and soul has weakened further.", "Fraying Threads", "it seems certain that the link between his body and soul has weakened further."),
 "M670d": ("Black-clad strangers have been seen wherever Elidibus has gone.", "Fraying Threads", "that in each of the places he has visited, there have been sightings of suspicious black-clad strangers."),
 "M670e": ("Thancred lost sight of Elidibus near the Crystarium.", "Fraying Threads", "He'd been shadowing Elidibus around the realm, only to lose sight of him near the Crystarium."),
 "M670g": ("The sleeping Scions have taken a turn for the worse.", "Fraying Threads", "Your slumbering friends, she reveals, have taken a turn for the worse."),
 "M670h": ("Krile says their souls' return cannot come soon enough.", "Fraying Threads", "she stresses that their souls' return cannot come soon enough."),
 "M670i": ("Krile offers to bring an expert in Allagan lore.", "Fraying Threads", "she offers to solicit the aid of an individual who is an expert in the field."),
 "M670j": ("Tataru and Krile kept the decline quiet.", "Fraying Threads", "She didn't want everyone to worry, so we've been keeping it quiet..."),
 # #671 Food for the Soul
 "M671b": ("Memory transference was the sole province of Allagan royalty.", "Food for the Soul", "Memory transference was the sole province of Allagan royalty, its mechanisms closely guarded secrets."),
 "M671c": ("Rammbroes sends word that they never doubted the Exarch.", "Food for the Soul", "Tell him...Tell him that we never doubted him."),
 "M671d": ("The Exarch would fuse the vessels with his crystallized essence.", "Food for the Soul", "we might fuse the vessel not with normal blood, but with my crystallized essence."),
 "M671e": ("There are six vessels for five Scions.", "Food for the Soul", "Forgive me, but I count ''six'' vessels. And there are only five of us."),
 "M671f": ("The Exarch will test one vessel himself.", "Food for the Soul", "One is for testing purposes. I will personally use it to see whether the crystal functions as it should."),
 "M671g": ("The Exarch's soul should merge with that of his younger self.", "Food for the Soul", "the Exarch's soul should successfully merge with that of his younger self."),
 "M671h": ("He cast aside his very name to become the Crystal Exarch.", "Food for the Soul", "And to that singular end did he cast aside his very name, that he might assume the mantle of the Crystal Exarch."),
 "M671i": ("The black-masked Ascians are of inferior rank.", "Food for the Soul", "Lest a grave predicament be made to seem hopeless, it should be noted that they are of inferior rank."),
 # #672 Faded Memories
 "M672a": ("While the others tend to black-masked Ascians, Thancred sends you to Y'shtola.", "Faded Memories", "While he and the others tend to the black-masked Ascians, Thancred bids you join Y'shtola at Anamnesis Anyder as a precautionary measure."),
 "M672b": ("You find Y'shtola unconscious, and Elidibus spirits her away.", "Faded Memories", "you arrive at Anyder to find Y'shtola unconscious. Before you can go to her aid, however, Elidibus appears and spirits her away."),
 "M672c": ("The trial pits you against faces from your past, then Elidibus as Ardbert.", "Faded Memories", "The trial pits you against recreations of myriad faces from your past, and at the last the Ascian himself enters the fray in the guise of Ardbert"),
 "M672d": ("Y'shtola exposes him as a primal, strengthened by the desire for salvation.", "Faded Memories", "she proceeds to expose him for what he truly is: a primal, granted strength by the desire for salvation."),
 "M672e": ("That is why he inspires the masses to rise as Warriors of Light.", "Faded Memories", "Thus has he sought to inspire the masses to rise up as Warriors of Light."),
 "M672f": ("Y'shtola knows he sacrificed himself to become Zodiark's heart.", "Faded Memories", "I know that you sacrificed yourself to become Zodiark's heart."),
 "M672g": ("Elidibus confirms it.", "Faded Memories", "Correct on all counts. Such is my nature, and such are my methods."),
 "M672i": ("He vanishes, intent on gaining the power to defeat you.", "Faded Memories", "he vanishes, but not before serving notice of his intent to gain the power to defeat you."),
 "M672l": ("The aether carries you to Emet-Selch's phantom Amaurot.", "Faded Memories", "You ride the aether to emerge in Emet-Selch's phantom Amaurot, where Elidibus instructs you to fight your way to the Capitol."),
 # #673 Etched in the Stars
 "M673b": ("Each crystal holds an account of a member of the Convocation.", "Etched in the Stars", "each crystal bears an account of the life of a member of the Convocation as remembered by the unsundered."),
 "M673d": ("A member of the Convocation opposed Zodiark's summoning and defected, leaving an office vacant.", "Etched in the Stars", "there was a member of the Convocation who opposed Zodiark's summoning and defected. One whose office was left vacant..."),
 "M673f": ("Its crystal holds the magick to summon the stars to your side.", "Etched in the Stars", "Such is the magick sealed within that crystal—the magick to summon the stars to your side."),
 "M673g": ("Hythlodaeus gives you the crystal.", "Etched in the Stars", "Hythlodaeus bestows Azem's crystal to the player."),
 "M673h": ("Hythlodaeus reminds you of your promise to Emet-Selch, to remember.", "Etched in the Stars", "If you do not, how will you keep your promise to Emet-Selch? The promise to remember?"),
 "M673i": ("Hythlodaeus cannot say whether he acts by his own will or his recreator's.", "Etched in the Stars", "After all, I cannot say whether I act of my own volition or by the will of my recreator!"),
 "M673j": ("Y'shtola suggests reaching out to Emet-Selch's brethren.", "Etched in the Stars", "perhaps you might consider reaching out to his brethren."),
 "M673l": ("Hythlodaeus is long departed.", "Etched in the Stars", "It is not my place to do so, long-departed as I am."),
 # #674 The Converging Light
 "M674a": ("Your comrades are grim to learn Elidibus is a primal.", "The Converging Light", "their faces turning grim at the revelation that Elidibus is a primal."),
 "M674b": ("A starshower over Eulmore brings an illusion of Amaurot.", "The Converging Light", "another starshower appears in the skies over Eulmore, this time accompanied by an illusion of Amaurot"),
 "M674c": ("Spectral warriors emerge from rings like the Exarch's summonings.", "The Converging Light", "you are promptly set upon by spectral warriors who emerge from arcane rings resembling those conjured in the Exarch's summoning rituals."),
 "M674d": ("Your airship is forced down in Amh Araeng.", "The Converging Light", "the airship sustains heavy damage and you are forced to land in the wastes of Amh Araeng."),
 "M674e": ("Elidibus stole the Exarch's spirit vessel and with it control of the Crystal Tower.", "The Converging Light", "the Ascian has stolen the Exarch's spirit vessel─and has thus acquired the means to control the Crystal Tower."),
 "M674f": ("The vessel bears his memories and his Allagan royal blood.", "The Converging Light", "The vessel bears not only my memories, but my blood─the blood of Allagan royalty"),
 "M674g": ("Despite his crystallization, the Exarch is determined to stop Elidibus.", "The Converging Light", "Despite his fast-advancing crystallization, the Exarch expresses his determination to help you to put a stop to Elidibus's plot"),
 "M674h": ("Lyna takes charge in the Crystarium and shares a heartfelt moment with the Exarch.", "The Converging Light", "Lyna arrives to take charge of the situation in the Crystarium. Knowing all too well what is at stake, the two share a brief but heartfelt moment"),
 "M674i": ("The ward the Exarch and Beq Lugg raised over the tower holds.", "The Converging Light", "the ward he and Beq Lugg raised over the tower still holds."),
 "M674j": ("Elidibus will summon heroes from other worlds, as the Exarch did.", "The Converging Light", "I will summon heroes from other worlds unto the First, just as you did."),
 "M674k": ("The spectral foes are heroes from other shards.", "The Converging Light", "Are heroes hailing from other shards, summoned hither to deliver this world from its doom."),
 "M674m": ("Beq Lugg lies wounded.", "The Converging Light", "Our friend Beq Lugg lies wounded in a clearing to the west."),
 # #675 Hope's Confluence
 "M675b": ("Elidibus takes the power of more heroes to become the Warrior of Light incarnate.", "Hope's Confluence", "In defiance of his fading memories, the Ascian clings to his name and duty, and takes unto himself the power of yet more heroes to arise as the Warrior of Light incarnate."),
 "M675c": ("Hythlodaeus's crystal lets you summon champions to your aid.", "Hope's Confluence", "In your hand shines the constellation crystal you received from Hythlodaeus, while around you an array of arcane rings stand ready to summon champions from beyond the rift to your aid."),
 "M675d": ("You bring Elidibus to his knees.", "Hope's Confluence", "it is ultimately you who delivers the final blow, bringing Elidibus to his knees."),
 "M675e": ("The Exarch strips the primal of his power.", "Hope's Confluence", "Harnessing the Crystal Tower's vast reservoir of energy, he strips the primal of his power and entraps his scattered essence."),
 "M675f": ("You restore Elidibus's memories before he fades into oblivion.", "Hope's Confluence", "Before the Ascian fades into oblivion, however, you choose to restore his lost memories to him, granting him a semblance of peace at the last."),
 "M675g": ("As his flesh turns to crystal, the Exarch asks for a journey together.", "Hope's Confluence", "As what remains of his flesh turns into crystal, he begs one last favor of you: a journey together."),
 "M675h": ("He entrusts his mind and memories to you.", "Hope's Confluence", "he entrusts to you his mind and memories before commencing his silent vigil..."),
 "M675i": ("Ryne reports that all is normal in Norvrandt.", "Hope's Confluence", "you learn from Ryne that all has returned to normal in Norvrandt."),
 "M675j": ("Elidibus blames his misstep for the deaths of Lahabrea and Emet-Selch.", "Hope's Confluence", "But I was wrong, and for my misstep did Lahabrea and Emet-Selch pay the ultimate price."),
 "M675k": ("Elidibus vows to resurrect Zodiark.", "Hope's Confluence", "I will resurrect Lord Zodiark."),
 "M675l": ("Elidibus is emissary of the Convocation of Fourteen.", "Hope's Confluence", "upon my honor as Elidibus, emissary of the Convocation of Fourteen, I will see this done."),
 "M675n": ("A specter at your side proves to be Emet-Selch.", "Hope's Confluence", "revealing themselves to be Emet-Selch."),
 "M675p": ("The Exarch's exertions have taken a fatal toll.", "Hope's Confluence", "the Exarch's exertions have taken a fatal toll."),
 # #676 Nothing Unsaid
 "M676b": ("Y'shtola calls it a gift from Emet-Selch, who knew Elidibus's plight.", "Nothing Unsaid", "A gift from Emet-Selch. He knew of Elidibus's plight."),
 "M676c": ("Foreseeing his death, Emet-Selch made provisions to end Elidibus's suffering, Y'shtola believes.", "Nothing Unsaid", "Foreseeing his own death, he made provisions to bring Elidibus's suffering to an end"),
 "M676d": ("The Exarch's soul and memories are intact in his vessel.", "Nothing Unsaid", "Both his soul and memories seem intact. Good."),
 "M676e": ("No one knows whether his body will accept his soul.", "Nothing Unsaid", "Will his body accept his soul? Will his essences blend properly? Will he awaken whole of mind?"),
 "M676h": ("Alisaie says goodbye, for it is time to go home.", "Nothing Unsaid", "I've come to say good-bye. It's time for me to return home."),
 "M676i": ("Beq Lugg will oversee Halric's treatments in her stead.", "Nothing Unsaid", "Beq Lugg will come to oversee them in my stead."),
 "M676k": ("Alphinaud once, in his hubris, thought himself worthy to lord it over others.", "Nothing Unsaid", "There was a time when I too, in my hubris, believed myself worthy to lord it over others."),
 "M676l": ("Alphinaud will cherish his memories of Norvrandt.", "Nothing Unsaid", "I shall cherish my memories of Norvrandt"),
 "M676m": ("Ryne asks you to go to Nabaath Areng with her.", "Nothing Unsaid", "And then we could go to Nabaath Areng together"),
 "M676o": ("Lady Chai is heartbroken at Alphinaud's farewell.", "Nothing Unsaid", "It's more than my poor heart can bear!"),
 "M676q": ("Ryne wants flowers for Minfilia.", "Nothing Unsaid", "Um...I've been meaning to get some flowers. For Minfilia."),
 # #677 The Journey Continues
 "M677a": ("Urianger found an object after your victory over Elidibus.", "The Journey Continues", "An object I chanced to find after thy victory over Elidibus."),
 "M677b": ("It is a crystal that likely belonged to Ardbert.", "The Journey Continues", "One that did, in all likelihood, once belong to Ardbert."),
 "M677c": ("Elidibus consumed Ardbert's body to fuel his transformation, and the crystal fell free.", "The Journey Continues", "consumed by thy foe to fuel his transformation, I posit that the crystal did tumble free."),
 "M677d": ("Save what abides in you, it is all that remains of Ardbert.", "The Journey Continues", "Save that which doth abide in thee, it is all that remaineth of our friend."),
 "M677e": ("Seto grieves that Ardbert's enemies profited even from his death.", "The Journey Continues", "Then even in death, his enemies found a way to profit from his sacrifice."),
 "M677f": ("Ardbert appears before Seto and greets his old friend.", "The Journey Continues", "Seto, my old friend. You've grown!"),
 "M677g": ("Seto will not yet bid Ardbert rest, for he travels with you.", "The Journey Continues", "Then I will not yet bid him rest. With you, he may look forward to many more adventures."),
 "M677h": ("Seto means to go on a little adventure himself.", "The Journey Continues", "Perhaps I too will go on a little adventure."),
 "M677i": ("Their tale, rightly told, will inspire new Warriors of Light.", "The Journey Continues", "And their tale, now rightly told, shall inspire new Warriors of Light for generations to come."),
 # #678 Unto the Morrow
 "M678a": ("Y'shtola has said her goodbyes to all but Runar.", "Unto the Morrow", "To everyone save Runar, that is. He's nowhere to be seen..."),
 "M678b": ("Runar begs her to stay.", "Unto the Morrow", "I could not bear it if you were to leave. Please stay! I beg of you!"),
 "M678c": ("Y'shtola will find a way to travel between worlds.", "Unto the Morrow", "Since a means to travel between worlds exists, you can be sure I will find a way to employ it."),
 "M678e": ("Thancred is ready to leave.", "Unto the Morrow", "At any rate, we've done what we came to do—which means I'm ready to leave."),
 "M678f": ("Ryne has chosen her own path.", "Unto the Morrow", "Ryne has chosen to walk her own path, and she doesn't need me under her feet."),
 "M678g": ("The Crystarium never asked the Exarch about his past, but now believes it knows.", "Unto the Morrow", "To the last, we did not question the Exarch about his past. It is only now, when he can no longer tell us, that we believe we know the answer."),
 "M678h": ("Lyna's message: he need no longer hide who he truly is.", "Unto the Morrow", "That he need no longer hide who he truly is. That he should live his own life to the fullest."),
 "M678i": ("Lyna asks you to carry a message when their lord awakens.", "Unto the Morrow", "And so, when our lord awakens, I bid you give him a message."),
 "M678j": ("The Crystarium sends off friends with a smile.", "Unto the Morrow", "it has ever been our way to send off friends with a smile."),
 # #679 Reflections in Crystal
 "M679a": ("Beq Lugg has the Scions commit their memories, then their souls, to spirit vessels.", "Reflections in Crystal", "directing the Scions to commit first their memories to the spirit vessels, and then their very souls."),
 "M679b": ("No mage has ever carried a soul across the rift.", "Reflections in Crystal", "Even the greatest mages in history knew better than to transport a soul across the rift."),
 "M679c": ("One by one, your friends awaken in their own bodies.", "Reflections in Crystal", "one by one, your friends awaken in their own bodies once more."),
 "M679e": ("You offer the Exarch's spirit vessel to the tower, and it opens.", "Reflections in Crystal", "The player offers the Exarch's spirit vessel to the closed entrance to the tower, causing it to open."),
 "M679f": ("G'raha Tia accepts a place among the Scions.", "Reflections in Crystal", "I accept. Henceforth, I shall count myself a Scion of the Seventh Dawn."),
 "M679g": ("The Scions welcome a bright-eyed youth named G'raha Tia.", "Reflections in Crystal", "the Scions welcome a new addition to their ranks: a bright-eyed youth named G'raha Tia."),
 "M679h": ("G'raha Tia has woven the tower's ward anew.", "Reflections in Crystal", "We succeeded in weaving it anew, albeit at a slightly diminished potency than when I had Beq Lugg's assistance."),
 "M679i": ("As a boy, G'raha Tia yearned to stand tall as the heroes of old.", "Reflections in Crystal", "When I was a boy, many long years ago, I yearned to stand tall as the heroes of eld."),
 "M679j": ("Zenos sits on the imperial throne.", "Reflections in Crystal", "The scene changes to Zenos, sitting on the imperial throne."),
 "M679k": ("Zenos dreams night after night of a dying world's end.", "Reflections in Crystal", "The memory of a dying world's end, night after night... And I thought it but a tired old dream."),
 "M679l": ("The white-robed figure reveals Asahi's face.", "Reflections in Crystal", "The white-robed figure reveals his face as [[Asahi]]'s."),
 "M679m": ("He names himself Fandaniel, laboring for his lord's ambitions.", "Reflections in Crystal", "And I, faithful Fandaniel, labor only to advance my lord's ambitions."),
 "M679n": ("Fandaniel shows his Ascian glyph.", "Reflections in Crystal", "Fandaniel shows his Ascian glyph."),
 "M679p": ("Fandaniel wonders whether the last of the unsundered is gone.", "Reflections in Crystal", "That the last of the unsundered...is gone?"),
 "M679q": ("The palace is in their hands.", "Reflections in Crystal", "with the palace in our hands, we may now proceed with the next phase of the plan."),
 "M679r": ("Fandaniel offers to prepare a hunting ground for Zenos.", "Reflections in Crystal", "Your Radiance. But give the word, and I shall go forth and prepare for you your hunting ground."),
 "M679s": ("The body he wears serves only as a vessel.", "Reflections in Crystal", "Whatever this flesh may have been before, it serves only as a vessel now."),
 "M679t": ("Krile is exhausted from restoring the ward.", "Reflections in Crystal", "By Mistress Krile's exhausted state, may I assume that the ward hath been restored?"),
 "M679u": ("He has a vast fortune at his disposal.", "Reflections in Crystal", "I have a vast fortune at my disposal."),
 # #680 Alisaie's Quest
 "M680a": ("Lyse is a former Scion and hero of the Resistance.", "Alisaie's Quest", "former Scion and hero of the Ala Mhigan Resistance."),
 "M680b": ("Lyse reports civil war in the Empire and invites you to an Alliance council in Ala Mhigo.", "Alisaie's Quest", "your old friend reports that civil war has broken out in the Empire, and invites you to an Alliance council in Ala Mhigo."),
 "M680c": ("After Varis's assassination, his cousin made a bid for the throne.", "Alisaie's Quest", "So, after Emperor Varis's assassination, it seems his cousin “Nerva” made a bid for the throne."),
 "M680d": ("Swaths of the imperial capital are in rubble.", "Alisaie's Quest", "Early reports say huge swaths of the imperial capital have been reduced to rubble."),
 "M680e": ("Thancred means to go to Garlemald to learn the truth.", "Alisaie's Quest", "I've a mind to pay a visit to Garlemald to ascertain the truth of the matter."),
 "M680f": ("Urianger suspects Zenos is orchestrating events from the shadows.", "Alisaie's Quest", "Not least if it should prove that Zenos doth indeed orchestrate events from the shadows."),
 "M680g": ("Y'shtola: now they understand the nature of their adversary.", "Alisaie's Quest", "A difficult truth to bear, yes. But at last we understand the nature of our adversary."),
 "M680h": ("Alisaie wants to find a way to cure the tempered.", "Alisaie's Quest", "I want to find a way to cure the tempered."),
 "M680i": ("To save Ga Bu, Alisaie hopes the sin eater treatment could work on the tempered.", "Alisaie's Quest", "Wishing above all else to save the young kobold Ga Bu, Alisaie is hopeful that the treatment used to help those corrupted by sin eaters might also prove effective on the tempered."),
 "M680j": ("G'raha Tia suggests the Aetherochemical Research Facility on Azys Lla.", "Alisaie's Quest", "no place is more likely to have the answers you seek than the Aetherochemical Research Facility on Azys Lla."),
 "M680k": ("Tataru built a new airship, the Bonanza.", "Alisaie's Quest", "which Tataru proudly announces she built herself."),
 "M680l": ("The Scions have fully settled back into their bodies.", "Alisaie's Quest", "the Archons have fully settled back into their bodies"),
 "M680m": ("Hydaelyn and Zodiark are primals.", "Alisaie's Quest", "this business about Hydaelyn and Zodiark being primals"),
 "M680n": ("You and G'raha Tia join Alisaie's quest for a cure for tempering.", "Alisaie's Quest", "you and G'raha Tia opt to assist Alisaie in her quest to find a cure for tempering."),
 "M680o": ("The others will travel to Gyr Abania.", "Alisaie's Quest", "While the others agree to travel to Gyr Abania"),
 "M680p": ("Without more calamities there will be no Rejoinings, so Zodiark cannot regain His full strength.", "Alisaie's Quest", "And if there are no further calamities, neither will there be Rejoinings, meaning Zodiark will never regain His full strength."),
 "M680q": ("Zodiark is the oldest and mightiest of primals.", "Alisaie's Quest", "as the oldest and mightiest of primals, He remains a force to be feared."),
 "M680r": ("The Alliance will convene in Ala Mhigo to decide on a course of action.", "Alisaie's Quest", "The Alliance will soon convene in Ala Mhigo to decide on a course of action"),
 # #681 The Wisdom of Allag
 "M681a": ("The report's contents have been deleted.", "The Wisdom of Allag", "Confound it. The contents appear to have been deleted."),
 "M681b": ("Its author, Owen, would have had quarters on the Habisphere.", "The Wisdom of Allag", "Assuming he was a researcher here, he will have had quarters on the Habisphere."),
 "M681d": ("A surge of energy should restart the system and release the locks.", "The Wisdom of Allag", "Were we to send a surge of energy through yonder control mechanism, it ''should'' prompt the system to restart, releasing the locks."),
 "M681e": ("The archive node identifies G'raha Tia as a member of the royal family.", "The Wisdom of Allag", "Guest identified as: member of the royal family."),
 "M681f": ("His password guesses are rejected.", "The Wisdom of Allag", "Password incorrect. Please try again."),
 "M681g": ("The node is a task for Cid and his colleagues.", "The Wisdom of Allag", "I believe this may be a task for Cid and his colleagues."),
}

# ---- Entities ---------------------------------------------------------------------------------------------------------
ENTITIES = {
 # recurring from earlier eras (same id and category merge; listed so this era lints alone)
 "char-thancred": "character", "char-urianger": "character", "char-yshtola": "character", "char-alphinaud": "character",
 "char-alisaie": "character", "char-tataru": "character", "char-krile": "character", "char-elidibus": "character",
 "char-zenos": "character", "char-estinien": "character", "char-gaius": "character", "char-varis": "character",
 "char-maxima": "character", "char-lyse": "character", "char-ga-bu": "character",
 "char-asahi": "character",
 "org-scions": "organization", "org-ascians": "organization", "org-garlean-empire": "organization",
 "org-eorzean-alliance": "organization", "org-ala-mhigan-resistance": "organization",
 # the Shadowbringers cast (the 5.0 eras may define these too, under the same ids)
 "char-graha-tia": "character", "char-ryne": "character", "char-lyna": "character", "char-ardbert": "character",
 "char-emet-selch": "character", "char-hythlodaeus": "character", "char-chai-nuzz": "character",
 "char-dulia-chai": "character", "char-kai-shirr": "character", "char-halric": "character", "char-runar": "character",
 "char-seto": "character", "loc-eulmore": "location",
 # new in 5.1–5.3
 "char-beq-lugg": "character", "char-wrenden": "character", "char-venat": "character", "char-zodiark": "character",
 "char-white-robed-figure": "character", "char-fandaniel": "character",
 "evt-souls-adrift": "event", "evt-the-missing-mayor": "event", "evt-an-emperor-slain": "event",
 "evt-the-false-hero": "event", "evt-records-of-the-ancients": "event", "evt-the-emissary-unmasked": "event",
 "evt-the-exarchs-vigil": "event", "evt-homeward-bound": "event",
}

# ---- Presentations ---------------------------------------------------------------------------------------------------
EX = ["The Crystal Exarch"]
PRES = {
 # -- The Exarch (his revealed identity carries the story; the pages call him the Exarch until #679)
 "char-graha-tia": [
   P(O648, None, "main", "G'raha Tia",
     "The Crystal Exarch, whom Krile still calls Raha. His summoning spell was meant for you, but it found those close to you instead and brought them to the First incomplete, "
     "and now the link to their bodies in the Source is weakening. Krile is glad his reckless plan to undo it never came to pass. He may know someone who can help.",
     ["M648k", "M648h", "M648c", "M648j", "M648g"], EX),
   P(O659, None, "main", "G'raha Tia",
     "The Crystal Exarch, whom Krile calls Raha. With Beq Lugg and Urianger he has made a spirit vessel to ferry the Scions' souls and minds home, "
     "but only the blood of the Allagan emperors can let it receive memory, so he must change the process or let his own blood permeate it.",
     ["M648k", "M659a", "M659b", "M659c", "M659e"], EX),
   P(O667, None, "main", "G'raha Tia",
     "The Crystal Exarch, working with Beq Lugg on a way to move memory into the spirit vessels. Their experiments falter, he fears the vessel may need his blood after all, "
     "and his crystallized arm has begun to pain him.",
     ["M667l", "M667h", "M667i"], EX),
   P(O669, None, "main", "G'raha Tia",
     "The Crystal Exarch, whose body is turning to crystal: the tower's way, he says, of compensating him for the demands he has placed on it. "
     "He has a plan, and when all is done he will ask one more favor of you.",
     ["M669f", "M669g"], EX),
   P(O671, None, "main", "G'raha Tia",
     "The Crystal Exarch, who cast aside his very name to take up that mantle. He means to fuse the spirit vessels with his own crystallized essence, and will test a sixth vessel himself; "
     "if it works, Urianger says, his soul should merge with that of his younger self.",
     ["M671h", "M671d", "M671e", "M671f", "M671g"], EX),
   P(O674, None, "main", "G'raha Tia",
     "The Crystal Exarch, fast turning to crystal. Elidibus has stolen his spirit vessel, which bears his memories and his Allagan royal blood, and with it the means to control the Crystal Tower. "
     "He and Beq Lugg sealed the tower with a ward, and he is determined to help you stop Elidibus.",
     ["M674e", "M674f", "M674g", "M674i"], EX),
   P(O675, None, "main", "G'raha Tia",
     "The Crystal Exarch. Atop the tower he drew on its vast reservoir of energy to strip Elidibus of his power, but his exertions took a fatal toll, and his body turned wholly to crystal. "
     "He entrusted his mind and memories to you, for one last journey together.",
     ["M675e", "M675p", "M675g", "M675h"], EX),
   P(O678, None, "main", "G'raha Tia",
     "The Crystal Exarch, whose soul and memories travel with you in his spirit vessel. The Crystarium never asked about his past, but now believes it knows, "
     "and Lyna bids you tell him, when he wakes, that he need no longer hide who he truly is.",
     ["M675h", "M676d", "M678g", "M678h", "M678i"], EX),
   P(O679, None, "main", "G'raha Tia",
     "A bright-eyed youth of the Crystal Tower, the younger self with whom the Crystal Exarch's soul was meant to merge. After you carried the Exarch's spirit vessel to the tower in the Source, "
     "he rewove its ward and accepted a place among the Scions. As a boy, he yearned to stand tall as the heroes of old.",
     ["M671g", "M679e", "M679g", "M679h", "M679f", "M679i"], EX),
   P(O680, None, "main", "G'raha Tia",
     "A young Scion versed in Allagan lore, once the Crystal Exarch. He suggested seeking a cure for tempering at the Aetherochemical Research Facility on Azys Lla, and went there with you and Alisaie.",
     ["M671h", "M679f", "M680j", "M680n"], EX),
   P(O681, None, "main", "G'raha Tia",
     "A young Scion, once the Crystal Exarch. On Azys Lla an Allagan archive node recognized him as a member of the royal family, but rejected his guesses at its password, "
     "so he is taking it back for Cid.",
     ["M679f", "M681e", "M681f", "M681g"], EX),
 ],
 "char-beq-lugg": [
   P(O649, None, "main", "Beq Lugg",
     "A Nu Mou mage and master of soulcraft, who hid from the world of men in the Grand Cosmos and met you first as the Seeker of Solitude. "
     "Long ago, a court mage's good intentions and Beq Lugg's naivety cost countless innocent lives. Petitioned by the Crystal Exarch to save his comrades' souls, Beq Lugg struck a deal.",
     ["M649c", "M649d", "M649e", "M649f", "M649g", "M649h"], ["The Seeker of Solitude"]),
   P(O650, None, "main", "Beq Lugg",
     "A Nu Mou master of soulcraft, now helping the Scions. Beq Lugg warns that their unstable souls could become impossible to transfer, "
     "and is treating patients whose souls stagnate under the Light with a soul tonic once used by the knights of Voeburt, hoping to learn from them.",
     ["M650b", "M650c", "M650e", "M650f", "M650h"], ["The Seeker of Solitude"]),
   P(O651, None, "main", "Beq Lugg",
     "A Nu Mou master of soulcraft whose knowledge once brought a plague. With water, clay and a fae lantern, Beq Lugg had Alisaie make a familiar that stirred Halric's soul, "
     "and believes a spell could induce stagnation to carry the Scions' souls safely home.",
     ["M651b", "M651a", "M651i", "M651e", "M651f"], ["The Seeker of Solitude"]),
   P(O659, None, "main", "Beq Lugg",
     "A Nu Mou master of soulcraft. With the Crystal Exarch and Urianger, Beq Lugg made a crystal spirit vessel to ferry the Scions' souls and minds between worlds, "
     "though it cannot yet receive memory.",
     ["M659a", "M659b", "M659d"], ["The Seeker of Solitude"]),
   P(O674, None, "main", "Beq Lugg",
     "A Nu Mou master of soulcraft, left wounded when Elidibus stole the Crystal Exarch's spirit vessel. With the Exarch, Beq Lugg raised a ward over the Crystal Tower to hold Elidibus inside.",
     ["M674m", "M674e", "M674i"], ["The Seeker of Solitude"]),
   P(O676, None, "main", "Beq Lugg",
     "A Nu Mou master of soulcraft, who found the Crystal Exarch's soul and memories intact in his vessel and will try to return them to his body, though there is no knowing whether it will accept them. "
     "Beq Lugg will also oversee Halric's treatment once Alisaie leaves.",
     ["M676d", "M676e", "M676i"], ["The Seeker of Solitude"]),
   P(O679, None, "main", "Beq Lugg",
     "A Nu Mou master of soulcraft, who had the Scions commit their memories and then their souls to spirit vessels, so that you could carry them across the rift, something no mage had dared before.",
     ["M679a", "M679b", "M679c"], ["The Seeker of Solitude"]),
 ],
 "char-halric": [
   P(O650, None, "main", "Halric",
     "A boy among patients whose souls stagnate under the Light. His soul is too far gone for a quick cure, his mind held together by the finest of threads.",
     ["M650d", "M650e"]),
   P(O651, None, "main", "Halric",
     "A boy whose soul stagnates under the Light. A familiar that Alisaie sculpted with Beq Lugg's magick stirred him enough to speak a few words.",
     ["M651i", "M651d", "M651e"]),
   P(O676, None, "main", "Halric",
     "A boy recovering, slowly, from a stagnant soul. Alisaie has said goodbye, and Beq Lugg will oversee his treatment in her stead.",
     ["M663b", "M676h", "M676i"]),
 ],
 "char-kai-shirr": [
   P(O651, None, "main", "Kai-Shirr",
     "A Eulmoran who came looking for Alphinaud with word of trouble in the city, whose future, he is told, is at stake.",
     ["M651h"]),
   P(O654, None, "main", "Kai-Shirr",
     "A Eulmoran who helped search Kholusia's settlements for the city's missing mayor, and asked to come along with you.",
     ["M654a", "M654k"]),
   P(O656, None, "main", "Kai-Shirr",
     "A Eulmoran who helped find the city's mayor, and now wants to be part of building the new Eulmore.",
     ["M654a", "M656h"]),
 ],
 "char-dulia-chai": [
   P(O652, None, "main", "Dulia-Chai",
     "Wife of Chai-Nuzz, who was elected mayor of Eulmore and soon vanished without a word. Beside herself, she sent Kai-Shirr to bring Alphinaud back, and fears she pushed her husband too hard.",
     ["M651j", "M652a", "M652b", "M652d", "M652e"], ["Lady Chai"]),
   P(O655, None, "main", "Dulia-Chai",
     "Wife of Chai-Nuzz, Eulmore's new mayor. She was near speechless at the sight of her husband marching home with three captured Talos.",
     ["M655c", "M655d"], ["Lady Chai"]),
 ],
 "char-chai-nuzz": [
   P(O652, None, "main", "Chai-Nuzz",
     "A Eulmoran who proved himself at Daedalus Stoneworks. When no one stood for mayor after Lord Vauthry's fall, the post fell to him, and soon after he vanished without a word. "
     "Alphinaud is sure he has not fled.",
     ["M652h", "M652c", "M652b", "M652d", "M652f"], ["Master Chai"]),
   P(O653, None, "main", "Chai-Nuzz",
     "Eulmore's missing mayor. Before he vanished he worried over the city's neglected industry, and spoke of opening the Queen Bee to outsiders; he was last seen heading for Gatetown.",
     ["M652d", "M653a", "M653e", "M653d"], ["Master Chai"]),
   P(O654, None, "main", "Chai-Nuzz",
     "Eulmore's elected mayor and heir to Daedalus Stoneworks, found in Kholusia trying to win back its settlements' goodwill. He will not take office until he has secured resources, "
     "and sought the counsel of Wrenden, who first wants him to solve one problem alone; Chai means to do it with Talos.",
     ["M654b", "M654d", "M654e", "M654g", "M654h"], ["Master Chai"]),
   P(O655, None, "main", "Chai-Nuzz",
     "Eulmore's mayor-elect, heir to Daedalus Stoneworks. He captured three abandoned Talos himself and marched them home, and Wrenden, who judges him more than qualified, will counsel him in politics.",
     ["M654h", "M655a", "M655c", "M655e", "M655f"], ["Master Chai"]),
   P(O656, None, "main", "Chai-Nuzz",
     "Eulmore's interim mayor, chosen to succeed Lord Vauthry. He has promised to undo Lord Vauthry's systems and hold an open forum on the city's future, "
     "and names food, its neighbors and industry as the first tasks.",
     ["M656a", "M656b", "M656c", "M656d", "M656e"], ["Master Chai"]),
 ],
 "char-wrenden": [
   P(O654, None, "main", "Wrenden",
     "Once chief advisor to Lord Vauthry's father, who left Eulmore when his values fell out of favor. Chai-Nuzz seeks his counsel, but Wrenden would first see him solve one of the city's problems on his own.",
     ["M654j", "M654f", "M654g"]),
   P(O655, None, "main", "Wrenden",
     "A former advisor of Eulmore's rulers, who judges Chai-Nuzz more than qualified to be mayor now that he has captured three Talos alone. Chai has asked for his counsel in politics.",
     ["M654j", "M655c", "M655e", "M655f"]),
 ],
 "loc-eulmore": [
   P(O652, None, "main", "Eulmore",
     "A city that had to choose a new leader after Lord Vauthry's fall. No one volunteered, so the mayorship fell to Chai-Nuzz, who soon vanished.",
     ["M652c", "M652b", "M652d"]),
   P(O656, None, "main", "Eulmore",
     "A city led now by an interim mayor, Chai-Nuzz, who has promised to undo Lord Vauthry's systems and hold an open forum on its future.",
     ["M656a", "M656b", "M656c", "M656d"]),
 ],
 # -- The Scions
 "char-thancred": [
   P(O648, None, "main", "Thancred",
     "A Scion whose soul is stranded in the First. Of the stricken Scions' bodies, his shows the most notable signs that the link to his soul is weakening. "
     "He and Ryne are pursuing an investigation of the Empty.",
     ["M648c", "M648d", "M648l"]),
   P(O663, None, "main", "Thancred",
     "A Scion whose soul is in the First. Back from the Empty with Ryne, he helped hunt the false Ardbert.",
     ["M663c", "M663a"]),
   P(O667, None, "main", "Thancred",
     "A Scion whose soul is in the First, now using his experience in subterfuge to keep watch over Elidibus.",
     ["M667f"]),
   P(O670, None, "main", "Thancred",
     "A Scion whose soul is in the First. He collapsed after shadowing Elidibus, the link between his body and soul weakening since he rescued Urianger from drowning, "
     "and he reports black-clad strangers wherever Elidibus has gone.",
     ["M670a", "M670b", "M670c", "M670d", "M670e"]),
   P(O678, None, "main", "Thancred",
     "A Scion ready to leave the First, his work there done. He leaves Ryne to walk her own path.",
     ["M678e", "M678f"]),
   P(O680, None, "main", "Thancred",
     "A Scion, back in his own body in the Source. He means to go to Garlemald to learn the truth of the Emperor's death.",
     ["M679c", "M680e"]),
 ],
 "char-urianger": [
   P(O649, None, "main", "Urianger",
     "A Sharlayan Scion whose soul is in the First. He stayed behind to fashion white auracite, to carry the Scions' souls home.",
     ["M648f", "M649a"]),
   P(O657, None, "main", "Urianger",
     "A Sharlayan Scion whose soul is in the First. He and the others found that auracite would perilously weaken the link between mind and soul, and are seeking another way.",
     ["M657a", "M657q", "M657o"]),
   P(O665, None, "main", "Urianger",
     "A Sharlayan Scion who once dealt with the Fuath to learn to walk on water. To bring Elidibus's schemes to light, he has led the Scions to Bismarck, who could carry them down to the ruins below.",
     ["M665h", "M665g", "M665a", "M665b"]),
   P(O666, None, "main", "Urianger",
     "A Sharlayan Scion, who wonders after Anamnesis Anyder whether the Elidibus at Zodiark's heart and the emissary you know are predecessor and successor.",
     ["M666d", "M666g"]),
   P(O677, None, "main", "Urianger",
     "A Sharlayan Scion who found Ardbert's crystal after the battle with Elidibus, and believes the heroes' tale, now rightly told, will inspire new Warriors of Light.",
     ["M677a", "M677b", "M677i"]),
   P(O680, None, "main", "Urianger",
     "A Sharlayan Scion, back in his own body. He suspects Zenos is orchestrating events in the Empire from the shadows.",
     ["M679c", "M680f"]),
 ],
 "char-yshtola": [
   P(O662, None, "main", "Y'shtola",
     "A Sharlayan Scion whose soul is in the First. In a Ronkan tomb she found a mural linking a gift like the Echo to a starshower, which recalls what Emet-Selch showed you in Amaurot.",
     ["M662c", "M662d", "M662e"]),
   P(O666, None, "main", "Y'shtola",
     "A Sharlayan Scion who stayed in Anamnesis Anyder to coax more from its device, which showed Venat becoming Hydaelyn's heart and Elidibus Zodiark's.",
     ["M666d", "M666h"]),
   P(O672, None, "main", "Y'shtola",
     "A Sharlayan Scion whom Elidibus spirited away from Anamnesis Anyder. She freed herself and exposed him as a primal, Zodiark's heart, strengthened by the desire for salvation.",
     ["M672b", "M672d", "M672f"]),
   P(O673, None, "main", "Y'shtola",
     "A Sharlayan Scion who exposed Elidibus as a primal. Since Emet-Selch sought common ground with you, she suggests reaching out to his brethren.",
     ["M672d", "M673j"]),
   P(O678, None, "main", "Y'shtola",
     "A Sharlayan Scion leaving the First. She promised Runar she will find a way to travel between worlds.",
     ["M678a", "M678c"]),
   P(O680, None, "main", "Y'shtola",
     "A Sharlayan Scion, back in her own body. She accepts that Hydaelyn and Zodiark are primals, and that the Scions now understand their adversary.",
     ["M679c", "M680m", "M680g"]),
 ],
 "char-alphinaud": [
   P(O652, None, "main", "Alphinaud",
     "A young Scion whose soul is in the First. Called back to Eulmore by Kai-Shirr, he has promised Lady Chai to find her missing husband, the city's new mayor.",
     ["M652a", "M652d", "M652g"]),
   P(O656, None, "main", "Alphinaud",
     "A young Scion whose soul is in the First. With Chai-Nuzz in office as Eulmore's interim mayor, he judges it time for the Scions to go their own way.",
     ["M656a", "M656g"]),
   P(O661, None, "main", "Alphinaud",
     "A young Scion whose soul is in the First. He urged the Scions to tell the Crystarium the truth of the Warriors of Light, whom its books call sin eaters or worse.",
     ["M661a", "M661b"]),
   P(O668, None, "main", "Alphinaud",
     "A young Scion, who believes Hydaelyn is the thread behind every Warrior of Light. He saw that the wish to help others was the people's own, and Elidibus only gave it a name; "
     "he will not leave the First until Elidibus is dealt with.",
     ["M668d", "M668f", "M668g"]),
   P(O676, None, "main", "Alphinaud",
     "A young Scion who once, in his hubris, believed himself worthy to lord it over others. He has said goodbye to the Chais in Eulmore and will cherish his memories of Norvrandt.",
     ["M676k", "M676l", "M676o"]),
   P(O680, None, "main", "Alphinaud",
     "A young Scion, back in his own body in the Source. With the others he will go to Ala Mhigo for the Alliance's council on the civil war in the Empire.",
     ["M679c", "M680b", "M680o"]),
 ],
 "char-alisaie": [
   P(O650, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion whose soul is in the First. She helps Beq Lugg treat patients whose souls stagnate under the Light, hoping to learn something of the Scions' own plight.",
     ["M648f", "M650g", "M650h"]),
   P(O651, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion whose soul is in the First. She sculpted a familiar that stirred Halric's soul, and hopes the same method could help Ga Bu.",
     ["M651i", "M651e", "M651g"]),
   P(O669, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion whose soul is in the First. Her fractured soul is making her memories fade, but she would rather stay fractured than don an Ascian mask.",
     ["M669c", "M669i"]),
   P(O676, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion. She has said goodbye to Halric and his carers, leaving his treatment to Beq Lugg, for it is time to go home.",
     ["M676h", "M676i"]),
   P(O680, None, "main", "Alisaie",
     "Alphinaud's twin, back in her own body in the Source. Wishing above all to save Ga Bu, she has set out to find a cure for tempering, and flew to Azys Lla with you and G'raha Tia.",
     ["M679c", "M680h", "M680i", "M680j", "M680n"]),
 ],
 "char-ga-bu": [
   P(O651, None, "main", "Ga Bu",
     "A kobold child whose soul was suffused with earth-aspected aether from Titan's summoning. Alisaie hopes the treatment for souls corrupted by Light could help him.",
     ["M651g"]),
   P(O680, None, "main", "Ga Bu",
     "A young kobold, tempered by Titan's aether. Alisaie's search for a cure for tempering is above all for him.",
     ["M651g", "M680i"]),
 ],
 "char-tataru": [
   P(O648, None, "main", "Tataru",
     "The Scions' receptionist at the Rising Stones. You told her of Minfilia's sacrifice and of Ryne, who carries on her legacy. Her helper behind enemy lines has gone silent, so Riol has gone into the Empire.",
     ["M648a", "M648b"]),
   P(O670, None, "main", "Tataru",
     "The Scions' receptionist, who has helped Krile keep quiet that the sleeping Scions have taken a turn for the worse.",
     ["M670g", "M670j"]),
   P(O680, None, "main", "Tataru",
     "The Scions' receptionist, who built them their own airship, the Bonanza, and flew you, Alisaie and G'raha Tia to Azys Lla.",
     ["M680k", "M680n"]),
 ],
 "char-krile": [
   P(O648, None, "main", "Krile",
     "A Sharlayan Scion with the Echo, tending the stricken Scions' bodies. She has found the link to their souls weakening, worst in Thancred, "
     "and will consult Matoya on keeping their aether stable while you carry word to the First.",
     ["M648c", "M648d", "M648e"]),
   P(O657, None, "main", "Krile",
     "A Sharlayan Scion with the Echo, who tends the Scions' sleeping bodies. Through the Echo, she and you saw Estinien's memories of the imperial palace.",
     ["M657c", "M657p"]),
   P(O670, None, "main", "Krile",
     "A Sharlayan Scion who tends the sleeping Scions. They have taken a turn for the worse and their souls' return cannot come soon enough, so she offered to bring an expert in Allagan lore.",
     ["M670g", "M670h", "M670i"]),
   P(O679, None, "main", "Krile",
     "A Sharlayan Scion who watched over the sleeping Scions until you brought their souls home and they woke in their own bodies. She has since worn herself out restoring the Crystal Tower's ward.",
     ["M679c", "M679t"]),
 ],
 "char-lyse": [
   P(O680, None, "main", "Lyse",
     "An Ala Mhigan, former Scion and hero of the Resistance. She brought the Scions word of civil war in the Empire, and invited them to an Alliance council in Ala Mhigo.",
     ["M680a", "M680b", "M680r"], ["Yda"]),
 ],
 "org-scions": [
   P(O648, None, "main", "The Scions of the Seventh Dawn",
     "An order whose five stricken members lie in the Source while their souls are stranded in the First, and the link between them weakens.",
     ["M648c", "M648f"]),
   P(O679, None, "main", "The Scions of the Seventh Dawn",
     "An order whose stricken members woke in their own bodies once you carried their souls home from the First. A bright-eyed youth, G'raha Tia, has joined its ranks.",
     ["M679c", "M679g", "M679f"]),
 ],
 # -- The Empire and the Alliance
 "char-estinien": [
   P(O657, None, "main", "Estinien",
     "A dragoon, hired by Tataru, who went into the Empire and met Gaius there. In the imperial palace he saw Zenos murder the Emperor, and fought a machine like the Ultima Weapon. "
     "He judges the Empire no threat for now, and with his contract fulfilled has left again.",
     ["M657m", "M657d", "M657f", "M657g", "M657n"]),
 ],
 "char-gaius": [
   P(O657, None, "main", "Gaius",
     "The Black Wolf, who now styles himself Shadowhunter. With Estinien he entered the imperial palace and saw Zenos murder the Emperor; conquest, Estinien says, is no longer his aim.",
     ["M657d", "M657f", "M657h"], ["the Black Wolf", "Shadowhunter"]),
   P(O658, None, "main", "Gaius",
     "The Black Wolf, who once sought to harness the Ultima Weapon and became the Ascians' pawn. A fugitive witness to the Emperor's murder, he warned that the VIIth Legion is secretly building a new Ultima Weapon, "
     "and that a prototype is bound for Eorzea.",
     ["M658f", "M658c", "M658d", "M658e", "M658g"], ["the Black Wolf", "Shadowhunter"]),
 ],
 "char-zenos": [
   P(O657, None, "main", "Zenos",
     "The crown prince, whose soul lived on while an Ascian wore his body. He has wrested back his flesh and murdered his father, Emperor Varis. "
     "A white-robed figure says he knows the prey Zenos will seek next.",
     ["M657e", "M657f", "M657j"]),
   P(O667, None, "main", "Zenos",
     "The crown prince who murdered his father. He has always dreamed of fire falling from the heavens and the world ablaze, and the white-robed figure says precious few remember the Final Days.",
     ["M657f", "M667m", "M667j"]),
   P(O679, None, "main", "Zenos",
     "The prince who murdered his father, now sitting on the imperial throne with the palace in his hands. The dying world's end comes back to him night after night, "
     "and the Ascian Fandaniel offers to prepare him a hunting ground.",
     ["M657f", "M679j", "M679k", "M679q", "M679r"]),
 ],
 "char-varis": [
   P(O657, None, "main", "Varis",
     "The Emperor of Garlemald, murdered by his own son, Zenos, after Zenos wrested back his flesh. Imperial soldiers now fight over the throne.",
     ["M657e", "M657f", "M657i"], ["Emperor Varis"]),
 ],
 "char-asahi": [
   P(O679, None, "main", "Asahi",
     "An imperial envoy, now dead. His body serves the Ascian Fandaniel as a vessel, and with it a vast fortune.",
     ["M679l", "M679s", "M679m", "M679u"]),
 ],
 "org-garlean-empire": [
   P(O657, None, "main", "The Garlean Empire",
     "An empire without an emperor: Zenos murdered his father, Varis, and imperial soldiers fight over the throne. A machine like the Ultima Weapon guards its palace.",
     ["M657f", "M657i", "M657g"]),
   P(O658, None, "main", "The Garlean Empire",
     "An empire whose emperor Zenos murdered. Through the VIIth Legion's secret research it is building a new Ultima Weapon, and a prototype is bound for Eorzea.",
     ["M657f", "M658d", "M658e", "M658g"]),
   P(O680, None, "main", "The Garlean Empire",
     "An empire in civil war since Emperor Varis's assassination, when his cousin made a bid for the throne. Swaths of its capital lie in rubble, and Zenos sits on the imperial throne.",
     ["M680c", "M680d", "M680b", "M679j"]),
 ],
 "char-maxima": [
   P(O658, None, "main", "Maxima",
     "A former Garlean ambassador who remains in Eorzea under Commander Raubahn. He brought you and Krile to the talks where Gaius warned of a new Ultima Weapon.",
     ["M658a", "M658d"]),
 ],
 "org-ala-mhigan-resistance": [
   P(O658, None, "main", "The Ala Mhigan Resistance",
     "The army of free Ala Mhigo, left to keep watch over the imperial border now that the Alliance's main host has withdrawn. It is strengthening its presence in the Ghimlyt Dark.",
     ["M658b", "M658k"]),
 ],
 "org-eorzean-alliance": [
   P(O658, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's nations. Its main host has withdrawn from the border, leaving the Resistance on watch, and Gaius has warned that a new Ultima Weapon is bound for Eorzea.",
     ["M658b", "M658d", "M658g"]),
   P(O680, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's nations, soon to convene in Ala Mhigo to decide what to do about the civil war in the Empire.",
     ["M680b", "M680r"]),
 ],
 # -- The First
 "char-ryne": [
   P(O648, None, "main", "Ryne",
     "A young girl of the First who carries on Minfilia's legacy after Minfilia's sacrifice. She and Thancred are investigating the Empty.",
     ["M648a", "M648l"]),
   P(O663, None, "main", "Ryne",
     "A young girl of the First who carries on Minfilia's legacy. Back from the Empty with Thancred, she helped hunt the false Ardbert.",
     ["M648a", "M663c"]),
   P(O676, None, "main", "Ryne",
     "A young girl of the First who carries on Minfilia's legacy. She has asked you to pick flowers for Minfilia, and to go with her to Nabaath Areng.",
     ["M648a", "M676q", "M676m"]),
   P(O678, None, "main", "Ryne",
     "A young girl of the First who carries on Minfilia's legacy. She has chosen to walk her own path, and Thancred leaves her to it.",
     ["M648a", "M678f"]),
 ],
 "char-lyna": [
   P(O659, None, "main", "Lyna",
     "One of the Crystarium, who came to the Ocular hoping to speak with you. Alphinaud offered to help her.",
     ["M659g", "M659h"]),
   P(O660, None, "main", "Lyna",
     "A captain of the Crystarium. She sought your help with a sin eater in Lakeland, already slain by a man calling himself a Warrior of Light, "
     "and confided that the Exarch has not been the same since he returned from the tempest: he seems younger.",
     ["M660i", "M660a", "M660d", "M660f", "M660g"], ["Captain Lyna"]),
   P(O674, None, "main", "Lyna",
     "A captain of the Crystarium, who took charge there as Elidibus's summoned warriors attacked, and shared a brief, heartfelt moment with the Exarch.",
     ["M660i", "M674h"], ["Captain Lyna"]),
   P(O678, None, "main", "Lyna",
     "A captain of the Crystarium, who saw the Scions off with a smile. She bids you tell the Exarch, when he wakes, that he need no longer hide who he truly is.",
     ["M660i", "M678j", "M678h", "M678i"], ["Captain Lyna"]),
 ],
 "char-ardbert": [
   P(O657, None, "main", "Ardbert",
     "A man whose body Elidibus has taken possession of.",
     ["M657k"]),
   P(O661, None, "main", "Ardbert",
     "One of the Warriors of Light of the First, long remembered only as the cause of the Flood; the Exarch told Lyna the truth of their deeds. "
     "A figure wearing his face has come before the Crystarium claiming the star brought him back, and the Scions are sure he is an impostor.",
     ["M660e", "M661c", "M661d", "M661e", "M661h"]),
   P(O677, None, "main", "Ardbert",
     "A Warrior of Light of the First. Elidibus consumed his body to fuel his transformation, and Urianger found his crystal, which you took to his old friend Seto. "
     "Save what abides in you, it is all that remains of him.",
     ["M677b", "M677c", "M677d", "M677f"]),
 ],
 "char-seto": [
   P(O677, None, "main", "Seto",
     "An old friend of Ardbert's, who grieves that Ardbert's enemies profited even from his death. When you brought him Ardbert's crystal he saw Ardbert in your place, "
     "and he means to go on a little adventure of his own.",
     ["M677e", "M677f", "M677g", "M677h"]),
 ],
 "char-runar": [
   P(O678, None, "main", "Runar",
     "A man of Slitherbough, the last to whom Y'shtola said goodbye. He begged her to stay, and she promised to find a way to travel between worlds.",
     ["M678a", "M678b", "M678c"]),
 ],
 # -- Elidibus and the Ascians
 "char-elidibus": [
   P(O657, None, "main", "Elidibus",
     "An Ascian and emissary who wore Zenos's body until Zenos wrested back his flesh. He now walks in Ardbert's body, saying he would see a feeble flame of hope rekindled.",
     ["M657e", "M657k", "M657l"]),
   P(O661, None, "main", "Elidibus",
     "An Ascian, the only one left to your knowledge since Emet-Selch's demise. Wearing Ardbert's body, he came before the Crystarium claiming the star brought him back, "
     "and urged the people to become Warriors of Light themselves; the Scions watch him from a distance.",
     ["M661i", "M661h", "M661d", "M661e", "M661f", "M661j"]),
   P(O663, None, "main", "Elidibus",
     "An Ascian wearing Ardbert's body, who dropped the pretense before the Scions. He enacts the will of the Convocation and sees no common ground with them, and Alphinaud believes he seeks the Rejoining.",
     ["M663d", "M663e", "M663g", "M663h"]),
   P(O666, None, "main", "Elidibus",
     "An Ascian and emissary wearing Ardbert's body. An ancient record shows an Elidibus who became Zodiark's heart, and should long since have ceased to be; "
     "Urianger wonders whether the two are predecessor and successor.",
     ["M663d", "M666d", "M666i", "M666g"]),
   P(O667, None, "main", "Elidibus",
     "An Ascian wearing Ardbert's body. He conjured a false starshower over the Crystarium to wake the gift in the people's sundered souls, as Hydaelyn does for Her minions, "
     "hailed them as Warriors of Light, and vanished promising to save the world.",
     ["M667c", "M667n", "M667d", "M667b", "M667k"]),
   P(O669, None, "main", "Elidibus",
     "An Ascian wearing Ardbert's body. He accused you of murdering his brothers and vowed to strike you down, saying Emet-Selch mistook you for another.",
     ["M669d", "M669h", "M669e"]),
   P(O672, None, "main", "Elidibus",
     "A primal: Zodiark's heart, strengthened by the desire for salvation, which is why he makes Warriors of Light. Y'shtola exposed him after he spirited her away, "
     "and he confirmed it, vowing to gain the power to defeat you.",
     ["M672f", "M672d", "M672e", "M672b", "M672g", "M672i"]),
   P(O674, None, "main", "Elidibus",
     "A primal and Ascian, who stole the Crystal Exarch's spirit vessel and with it the means to control the Crystal Tower. He summons heroes from other worlds, as the Exarch did, and waits inside the tower's ward.",
     ["M674a", "M674e", "M674j", "M674k", "M674i"]),
   P(O675, None, "main", "Elidibus",
     "Emissary of the Convocation of Fourteen and a primal, who blamed his own misstep for Lahabrea's and Emet-Selch's deaths and vowed to resurrect Zodiark. "
     "Atop the tower you defeated him, the Exarch stripped him of his power, and you restored his memories before he faded into oblivion.",
     ["M675l", "M675j", "M675k", "M675d", "M675e", "M675f"]),
 ],
 "org-ascians": [
   P(O671, None, "main", "The Ascians",
     "A group whose black-clad, black-masked members have been seen wherever Elidibus goes, though they are of inferior rank.",
     ["M670d", "M671i"]),
 ],
 "char-emet-selch": [
   P(O661, None, "main", "Emet-Selch",
     "An Ascian, now dead. His demise leaves Elidibus the only Ascian you know who could be behind the impostor wearing Ardbert's face.",
     ["M661i", "M661h"]),
   P(O673, None, "main", "Emet-Selch",
     "An Ascian, now dead, whose last words bade you remember that his people once lived. Hythlodaeus reminds you of that promise, and Y'shtola says he sought common ground with you.",
     ["M661i", "M663f", "M673h", "M673j"]),
   P(O676, None, "main", "Emet-Selch",
     "An Ascian, now dead, who sought common ground with you. In the battle with Elidibus a specter at your side proved to be him, "
     "and Y'shtola believes that, foreseeing his own death, he arranged a way to end Elidibus's suffering.",
     ["M661i", "M673j", "M675n", "M676b", "M676c"]),
 ],
 "char-hythlodaeus": [
   P(O673, None, "main", "Hythlodaeus",
     "A long-departed shade of the ancients, who met you again in the Capitol of Emet-Selch's phantom Amaurot. He gave you the crystal of the Convocation's vacant Fourteenth seat, "
     "whose magick summons the stars to your side, and cannot say whether he acts by his own will or his recreator's.",
     ["M673l", "M672l", "M673d", "M673f", "M673g", "M673i"]),
 ],
 "char-venat": [
   P(O666, None, "main", "Venat",
     "An ancient who, by the record in Anamnesis Anyder, led the summoning of Hydaelyn and became Her heart to oppose Zodiark, vowing not to vanish from the world.",
     ["M666c", "M666d", "M666e", "M666f"]),
 ],
 "char-zodiark": [
   P(O666, None, "main", "Zodiark",
     "A power of the ancients whose heart, the record in Anamnesis Anyder shows, was Elidibus. Hydaelyn was summoned to oppose Him.",
     ["M666d", "M666e"]),
   P(O675, None, "main", "Zodiark",
     "The power whose heart Elidibus became. Elidibus vowed to resurrect Lord Zodiark before he was defeated and faded away.",
     ["M666d", "M675k", "M675f"]),
   P(O680, None, "main", "Zodiark",
     "The oldest and mightiest of primals, as Hydaelyn is a primal too. Without further calamities there will be no Rejoinings, so He cannot regain His full strength.",
     ["M680m", "M680q", "M680p"]),
 ],
 "char-white-robed-figure": [
   P(O657, None, "main", "The white-robed figure",
     "A figure in white robes at Zenos's side after he wrested back his flesh, who says he knows full well the prey Zenos will seek next.",
     ["M657e", "M657j"]),
   P(O667, None, "main", "The white-robed figure",
     "A figure in white robes at Zenos's side. Hearing of Zenos's dream of the world ablaze, he wondered whether Emet-Selch had found a way, for precious few remember the Final Days.",
     ["M657j", "M667m", "M667j"]),
   P(O679, None, "main", "The white-robed figure",
     "The figure in white robes at Zenos's side, who wears Asahi's face and names himself Fandaniel.",
     ["M679l", "M679m"]),
 ],
 "char-fandaniel": [
   P(O679, None, "main", "Fandaniel",
     "An Ascian, the white-robed figure at Zenos's side. He wears Asahi's body as a mere vessel, with its vast fortune, and labors for his lord's ambitions now that the palace is theirs. "
     "He wonders gleefully whether Elidibus, the last of the unsundered, is gone.",
     ["M679l", "M679s", "M679u", "M679m", "M679n", "M679q", "M679p"], ["The white-robed figure"]),
 ],
}

# ---- Arc recaps -------------------------------------------------------------------------------------------------------
N1, N2, N3, N4, N5, N6, N7, N8 = ("Souls Adrift", "The Missing Mayor", "An Emperor Slain", "The False Hero", "Records of the Ancients",
                                  "The Emissary Unmasked", "The Exarch's Vigil", "A Long Way Home")
PRES.update({
 "evt-souls-adrift": [
   P(O648, None, "main", N1,
     "Krile has found that the link between the stricken Scions' bodies and their souls, stranded in the First, is weakening, worst in Thancred. "
     "You carried the news to the First, where the Scions settled on pouring their spirits into auracite so you could carry them home. "
     "The Crystal Exarch, whose summoning stranded them, may know someone who can help.",
     ["M648c", "M648d", "M648f", "M648h", "M648g"]),
   P(O649, None, "main", N1,
     "The Scions' souls are stranded in the First while their bodies weaken, and Urianger stayed behind to fashion white auracite to carry them. "
     "The Crystal Exarch led the rest of you to the Grand Cosmos, where you fought past its reclusive mage's familiars. "
     "The mage proved to be Beq Lugg, a Nu Mou master of soulcraft, who grudgingly struck a deal.",
     ["M648c", "M649a", "M649c", "M649d", "M649g", "M649h"]),
   P(O650, None, "main", N1,
     "Beq Lugg, a Nu Mou master of soulcraft, learned that the Scions come from another world and agreed to help, warning that their unstable souls could become impossible to transfer. "
     "Among patients whose souls stagnate under the Light, a soul tonic eased some, but the worst afflicted did not respond, and Halric's soul is too far gone.",
     ["M650a", "M650b", "M650c", "M650e", "M650g", "M650d"]),
   P(O651, None, "main", N1,
     "To stir the stagnant patients' souls, Beq Lugg had you gather pure water, clay and a fae lantern, and Alisaie sculpted a familiar that moved Halric to speak. "
     "Beq Lugg now believes a spell could induce stagnation to carry the Scions home, and Alisaie hopes the method could help Ga Bu. "
     "Then Kai-Shirr arrived with word that his city's future is at stake.",
     ["M651a", "M651i", "M651e", "M651f", "M651g", "M651h"]),
 ],
 "evt-the-missing-mayor": [
   P(O652, None, "main", N2,
     "Kai-Shirr brought you and Alphinaud back to Eulmore, where Lady Chai is beside herself. No one stood for mayor after Lord Vauthry's fall, so the post fell to her husband, Chai-Nuzz, "
     "who soon vanished without a word. She fears she pushed him too hard, but Alphinaud is sure he has not fled and has promised to find him.",
     ["M652a", "M651j", "M652c", "M652b", "M652d", "M652e", "M652f", "M652g"]),
   P(O653, None, "main", N2,
     "Eulmore's new mayor, Chai-Nuzz, has vanished, so you and Alphinaud questioned its people. Before he left, he fretted over the city's neglected industry and its thin defenses, "
     "with many soldiers still recovering from your clash with Lord Vauthry. He spoke of opening the Queen Bee to outsiders, and was last seen heading for Gatetown.",
     ["M653a", "M653b", "M653c", "M653e", "M653d"]),
   P(O654, None, "main", N2,
     "Searching Kholusia's settlements for Eulmore's missing mayor, you found Chai-Nuzz trying to win back their goodwill. He will not take office until he has secured resources, "
     "and sought the counsel of Wrenden, once chief advisor to Lord Vauthry's father. Wrenden would first see him solve one problem alone, and Chai, heir to Daedalus Stoneworks, means to do it with Talos.",
     ["M654a", "M654b", "M654e", "M654j", "M654g", "M654h"]),
   P(O655, None, "main", N2,
     "To prove himself to Wrenden, Chai-Nuzz captured three of the abandoned Talos that roam Kholusia, disabling them with canisters while you kept watch. "
     "The Talos marched home, where Lady Chai was near speechless at the sight of her husband. Wrenden judged him more than qualified to be mayor, and Chai asked for his counsel.",
     ["M655a", "M655b", "M655c", "M655d", "M655e", "M655f"]),
   P(O656, None, "main", N2,
     "Chai-Nuzz has taken office as Eulmore's interim mayor, chosen to succeed Lord Vauthry. Before the people he vowed to undo Lord Vauthry's systems, proposed an open forum on the city's future, "
     "and named food, its neighbors and industry as the first tasks. Kai-Shirr wants to help build the new Eulmore, and Alphinaud judges it time for the Scions to go their own way.",
     ["M656a", "M656b", "M656c", "M656d", "M656e", "M656h", "M656g"]),
 ],
 "evt-an-emperor-slain": [
   P(O657, None, "main", N3,
     "The Scions found that white auracite would sever mind from soul, and are seeking another way. In the Source, Estinien's memories reached you through the Echo: "
     "Zenos has his own flesh back and murdered his father, Emperor Varis, before Estinien and Gaius. Imperial soldiers now fight over the throne, a white-robed figure counsels Zenos, and Elidibus walks in Ardbert's body.",
     ["M657a", "M657b", "M657p", "M657e", "M657f", "M657i", "M657j", "M657k"]),
   P(O658, None, "main", N3,
     "Emperor Varis is dead at Zenos's hand, and imperial soldiers fight over the throne. Maxima brought you and Krile to Raubahn, who sat in talks with Gaius. "
     "The Black Wolf warned that the VIIth Legion is secretly building a new Ultima Weapon, with a prototype bound for Eorzea. Raubahn is gathering a force in the Ghimlyt Dark and asks for your strength.",
     ["M657f", "M657i", "M658a", "M658d", "M658e", "M658g", "M658k", "M658h"]),
   P(O659, None, "main", N3,
     "With the Emperor slain and Zenos returned, Garlemald's course is impossible to predict. In the First, the Crystal Exarch, Beq Lugg and Urianger have made a spirit vessel to carry the Scions' souls and minds home, "
     "but it cannot receive memory without the blood of the Allagan emperors. The Exarch is seeking a way, and Lyna has asked to speak with you.",
     ["M659f", "M659a", "M659b", "M659c", "M659d", "M659e", "M659g"]),
 ],
 "evt-the-false-hero": [
   P(O660, None, "main", N4,
     "Captain Lyna asked your help with a sin eater in Lakeland, but a stranger calling himself a Warrior of Light had already slain it. "
     "Afterwards she confided in Alphinaud that the Crystal Exarch has not been the same since he returned from the tempest, and seems younger. "
     "From him she knows the truth of Ardbert and his comrades.",
     ["M660i", "M660a", "M660d", "M660f", "M660g", "M660e"]),
   P(O661, None, "main", N4,
     "Alphinaud urged the Scions to tell the Crystarium the truth of the Warriors of Light, whom its books call sin eaters or worse. As you spoke, Ardbert appeared in the crowd, "
     "claiming the star had brought him back, and urged the people to become Warriors of Light themselves. Since Emet-Selch's demise only Elidibus could be behind it, so the Scions watch from afar.",
     ["M661a", "M661b", "M661d", "M661e", "M661f", "M661i", "M661h", "M661j"]),
   P(O662, None, "main", N4,
     "An impostor wearing Ardbert's face, surely Elidibus, urges the people to become Warriors of Light. Y'shtola took you to the Qitana Ravel, where the Viis had found new chambers, "
     "and in the tomb of the archmage Tiuna, said to have had a gift like the Echo, a mural tied that gift to a starshower. Y'shtola sees in it what Emet-Selch showed you in Amaurot.",
     ["M661h", "M662a", "M662b", "M662g", "M662c", "M662d", "M662e"]),
   P(O663, None, "main", N4,
     "The Scions learned that the false Ardbert slays a nearby sin eater before visiting any town, to win its trust. With Thancred and Ryne, back from the Empty, you tracked him down, "
     "and he dropped the pretense: he is Elidibus, enacting the will of the Convocation. He scorned Alphinaud's appeal to Emet-Selch's last words, and Alphinaud believes he seeks the Rejoining.",
     ["M663a", "M663c", "M663d", "M663e", "M663f", "M663g", "M663h"]),
   P(O664, None, "main", N4,
     "Elidibus, who wore Ardbert's face, seeks the Rejoining, and the Scions hope ancient ruins may explain him. Tolshs Aath, chieftain of the Ondo, told you that benthos raiding Ondo and Kholusian stores "
     "are raising an army against the finless, and covet ruins newly found deep within the illuminated land. Urianger would call on another's help to reach them.",
     ["M663h", "M664h", "M664a", "M664b", "M664d", "M664e", "M664f", "M664g"]),
 ],
 "evt-records-of-the-ancients": [
   P(O665, None, "main", N5,
     "To reach the ruins deep within the illuminated land and bring Elidibus's schemes to light, Urianger led the Scions to Bismarck. "
     "The great creature will carry you down once his underbelly is cleared of barnacles, a task Urianger cannot do from the surface. "
     "Bismarck told you of Ken, a man who made a home on his back, and whom history has already forgotten.",
     ["M664f", "M665g", "M665a", "M665b", "M665c", "M665e"]),
   P(O666, None, "main", N5,
     "Bismarck carried the Scions down into Anamnesis Anyder, where you fought past the benthos and their leader. In its central chamber a device showed ancients summoning Hydaelyn, led by Venat, "
     "who became Her heart, while Elidibus became Zodiark's. Urianger wonders whether the Elidibus you know is a successor, and Y'shtola stayed behind to coax more from the device.",
     ["M666a", "M666b", "M666c", "M666d", "M666g", "M666h"]),
   P(O667, None, "main", N5,
     "Y'shtola is studying Anamnesis Anyder while the false Ardbert's words stir the Crystarium. At the Exedra, Elidibus conjured a false starshower to wake the Echo in the people's sundered souls, "
     "as Hydaelyn does for Her minions, and hailed them as Warriors of Light. Thancred will shadow him, and the Exarch's memory experiments falter.",
     ["M666h", "M667a", "M667c", "M667n", "M667d", "M667b", "M667f", "M667h"]),
   P(O668, None, "main", N5,
     "Elidibus's false starshower has stirred would-be Warriors of Light across the Crystarium, and Thancred shadows him. The librarian Moren taught you that many in Vrandtic history bore that title, "
     "until the Flood made it an insult, and Alphinaud suspects Hydaelyn is the common thread. Helping young Riqi-Tio toward becoming an apothecary, he saw that the wish to help was the people's own.",
     ["M667b", "M667f", "M668c", "M668b", "M668d", "M668e", "M668f"]),
 ],
 "evt-the-emissary-unmasked": [
   P(O669, None, "main", N6,
     "Elidibus has stirred the people to become Warriors of Light. At the Crystarium's lookout he accused you of murdering his brothers and vowed to strike you down. "
     "Alisaie admits her fractured soul is fading her memories, the Exarch's body is turning to crystal as he readies a plan, and Ryne has come running: Thancred has collapsed.",
     ["M667b", "M669d", "M669h", "M669c", "M669f", "M669g", "M669j"]),
   P(O670, None, "main", N6,
     "Thancred collapsed, the link between his body and soul weakening since he rescued Urianger from drowning, and he reports black-clad strangers wherever Elidibus has gone. "
     "In the Source, the Scions' sleeping bodies have taken a turn for the worse, which Tataru and Krile kept quiet. Krile warns that their souls must return soon, and will bring an expert in Allagan lore.",
     ["M670a", "M670b", "M670c", "M670d", "M670g", "M670j", "M670h", "M670i"]),
   P(O671, None, "main", N6,
     "With the sleeping Scions failing, Krile brought Rammbroes, an expert in Allag, who had no answer: memory transference belonged to Allagan royalty alone. "
     "In the First, the Crystal Exarch means to fuse the spirit vessels with his own crystallized essence and test a sixth on himself. If it works, Urianger says, his soul should merge with his younger self's.",
     ["M670g", "M671b", "M671c", "M671d", "M671e", "M671f", "M671g"]),
   P(O672, None, "main", N6,
     "While the others tended to black-masked Ascians, Thancred sent you to check on Y'shtola at Anamnesis Anyder, but Elidibus spirited her away and set you a trial of faces from your past. "
     "Y'shtola freed herself and exposed him as a primal, Zodiark's heart, strengthened by the desire for salvation. He confirmed it and vanished, vowing to gain the power to defeat you.",
     ["M672a", "M672b", "M672c", "M672d", "M672f", "M672g", "M672i"]),
   P(O673, None, "main", N6,
     "Y'shtola has exposed Elidibus as a primal, and he means to gain the power to defeat you. In the Capitol of phantom Amaurot you gathered crystals holding accounts of the Convocation, "
     "and Hythlodaeus gave you the crystal of its vacant Fourteenth seat, whose magick summons the stars to your side. Y'shtola suggests reaching out to Emet-Selch's brethren.",
     ["M672d", "M672i", "M672l", "M673b", "M673d", "M673f", "M673g", "M673j"]),
 ],
 "evt-the-exarchs-vigil": [
   P(O674, None, "main", N7,
     "Over Eulmore a second starshower brought an illusion of Amaurot and spectral warriors, heroes Elidibus summons from other worlds. Your airship came down in Amh Araeng, "
     "and near the Crystarium you found the Exarch and a wounded Beq Lugg. Elidibus has stolen the Exarch's spirit vessel, and with his royal blood the means to control the Crystal Tower, now sealed by their ward.",
     ["M674b", "M674c", "M674k", "M674d", "M674m", "M674e", "M674f", "M674i"]),
   P(O675, None, "main", N7,
     "Holding the Crystal Tower with the Exarch's stolen vessel, Elidibus took the power of countless summoned heroes and rose as the Warrior of Light incarnate. "
     "With Hythlodaeus's crystal you called champions of your own and beat him. The Exarch stripped him of his power, you restored his memories before he faded, "
     "and the Exarch, turned wholly to crystal, entrusted his mind and memories to you.",
     ["M674e", "M675b", "M675c", "M675d", "M675e", "M675f", "M675g", "M675h"]),
   P(O676, None, "main", N7,
     "Elidibus has faded, and the Exarch's mind and memories travel with you in his spirit vessel, which Beq Lugg will try to return to his body. Y'shtola believes Emet-Selch foresaw his death and arranged Elidibus's release. "
     "Now the Scions say their farewells: Alisaie to Halric, Alphinaud to the Chais, and Ryne asks you to bring flowers for Minfilia.",
     ["M675f", "M675h", "M676d", "M676e", "M676c", "M676h", "M676l", "M676q"]),
   P(O677, None, "main", N7,
     "With Elidibus gone, the Scions are saying farewell to Norvrandt. Urianger found a crystal after the battle, likely Ardbert's, which fell free when Elidibus consumed his body. "
     "You took it to Ardbert's old friend Seto, who saw Ardbert in your place and resolved to go on an adventure of his own.",
     ["M676h", "M677a", "M677b", "M677c", "M677f", "M677g", "M677h"]),
 ],
 "evt-homeward-bound": [
   P(O678, None, "main", N8,
     "With Elidibus defeated and the Exarch's soul in your keeping, the Scions said their goodbyes. Y'shtola promised Runar she would find a way to travel between worlds, "
     "and Thancred, ready to leave, lets Ryne walk her own path. In the Crystarium, Lyna bade you tell the Exarch, when he wakes, that he need no longer hide who he truly is.",
     ["M675h", "M678a", "M678c", "M678e", "M678f", "M678h", "M678i"]),
   P(O679, None, "main", N8,
     "Beq Lugg moved the Scions' memories and souls into spirit vessels, and in the Source your friends woke in their own bodies. You carried the Exarch's vessel to the Crystal Tower, "
     "and days later a bright-eyed youth named G'raha Tia joined the Scions. In the imperial palace, Zenos sits on the throne beside the Ascian Fandaniel, who wears Asahi's body.",
     ["M679a", "M679c", "M679e", "M679g", "M679j", "M679l", "M679m", "M679n"]),
   P(O680, None, "main", N8,
     "With the Scions back in their bodies, Lyse brought word of civil war in the Empire since the Emperor's assassination, and invited them to an Alliance council in Ala Mhigo. "
     "Thancred means to go to Garlemald. You and G'raha Tia instead joined Alisaie's search for a cure for tempering, for Ga Bu's sake, and flew to Azys Lla on Tataru's new airship.",
     ["M680l", "M680b", "M680c", "M680e", "M680n", "M680i", "M680k"]),
   P(O681, None, "main", N8,
     "While the other Scions head for the Alliance council, you, Alisaie and G'raha Tia seek a cure for tempering on Azys Lla. The report you sought had been deleted, "
     "but its author's archive node lay in the sealed Habisphere. Once G'raha restarted the locks, the node recognized him as royalty but refused his passwords, so you are taking it to Cid.",
     ["M680o", "M680n", "M681a", "M681b", "M681d", "M681e", "M681f", "M681g"]),
 ],
})

# ---- Relationships --------------------------------------------------------------------------------------------------
RELS = [
 ("rel-beq-lugg-aids-scions", "char-beq-lugg", "aids", "org-scions", O650, None, "main", ["M649h", "M650b"]),
 ("rel-alisaie-aids-halric", "char-alisaie", "aids", "char-halric", O650, O676, "main", ["M650g", "M650h"], ["M676h", "M676i"]),
 ("rel-beq-lugg-aids-halric", "char-beq-lugg", "aids", "char-halric", O676, None, "main", ["M676i"]),
 ("rel-kai-shirr-aids-chai-nuzz", "char-kai-shirr", "aids", "char-chai-nuzz", O654, None, "main", ["M654a", "M654k"]),
 ("rel-wrenden-aids-chai-nuzz", "char-wrenden", "aids", "char-chai-nuzz", O655, None, "main", ["M655e", "M655f"]),
 ("rel-chai-nuzz-leads-eulmore", "char-chai-nuzz", "leads", "loc-eulmore", O656, None, "main", ["M656a", "M656b"]),
 ("rel-ardbert-possessed-by-elidibus", "char-ardbert", "possessed-by", "char-elidibus", O657, O675, "main", ["M657k"], ["M675b", "M675e"]),
 ("rel-elidibus-opposes-scions", "char-elidibus", "opposes", "org-scions", O663, O675, "main", ["M663d", "M663g"], ["M675d", "M675f"]),
 ("rel-white-robed-figure-aids-zenos", "char-white-robed-figure", "aids", "char-zenos", O657, O679, "main", ["M657j"], ["M679l", "M679m"]),
 ("rel-white-robed-figure-revealed-as-fandaniel", "char-white-robed-figure", "revealed-as", "char-fandaniel", O679, None, "main", ["M679l", "M679m"]),
 ("rel-fandaniel-serves-zenos", "char-fandaniel", "serves", "char-zenos", O679, None, "main", ["M679m", "M679r"]),
 ("rel-fandaniel-member-of-ascians", "char-fandaniel", "member-of", "org-ascians", O679, None, "main", ["M679n"]),
 ("rel-asahi-possessed-by-fandaniel", "char-asahi", "possessed-by", "char-fandaniel", O679, None, "main", ["M679l", "M679s"]),
 ("rel-gaius-aids-eorzean-alliance", "char-gaius", "aids", "org-eorzean-alliance", O658, None, "main", ["M658d", "M658g"]),
 ("rel-graha-tia-member-of-scions", "char-graha-tia", "member-of", "org-scions", O679, None, "main", ["M679f", "M679g"]),
]

# Relationships the accepted content or an earlier era defined, ended here (reported unknown when this era lints alone).
ADJUST = {
 "rel-zenos-possessed-by-elidibus": {"until": O657, "end": ["M657e"]},          # content_4_1_to_4_56: Zenos wrests back his flesh
 "rel-varis-leads-garlean-empire": {"until": O657, "end": ["M657f"]},           # the Emperor is murdered
 "rel-varis-opposes-eorzean-alliance": {"until": O657, "end": ["M657f"]},       # content_4_1_to_4_56
 "rel-elidibus-aids-varis": {"until": O657, "end": ["M657f"]},                  # content_4_0_part3
 "rel-alphinaud-opposes-varis": {"until": O657, "end": ["M657f"]},
 "rel-elidibus-member-ascians": {"until": O675, "end": ["M675f"]},              # he fades into oblivion
}

# ---- Arcs ------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-o1-souls-adrift", "evt-souls-adrift", O648, O651),
 ("arc-o2-the-missing-mayor", "evt-the-missing-mayor", O652, O656),
 ("arc-o3-an-emperor-slain", "evt-an-emperor-slain", O657, O659),
 ("arc-o4-the-false-hero", "evt-the-false-hero", O660, O664),
 ("arc-o5-records-of-the-ancients", "evt-records-of-the-ancients", O665, O668),
 ("arc-o6-the-emissary-unmasked", "evt-the-emissary-unmasked", O669, O673),
 ("arc-o7-the-exarchs-vigil", "evt-the-exarchs-vigil", O674, O677),
 ("arc-o8-homeward-bound", "evt-homeward-bound", O678, O681),
]

CASTS = {
 "evt-souls-adrift": [
   ("char-tataru", O648, ["M648a"]), ("char-krile", O648, ["M648c"]), ("char-graha-tia", O648, ["M648g"]),
   ("char-urianger", O649, ["M649a"]), ("char-beq-lugg", O649, ["M649c"]), ("char-alisaie", O650, ["M650g"]),
   ("char-alphinaud", O650, ["M650b"]), ("char-halric", O650, ["M650d"]), ("char-ga-bu", O651, ["M651g"]),
   ("char-kai-shirr", O651, ["M651h"]),
 ],
 "evt-the-missing-mayor": [
   ("char-alphinaud", O652, ["M652g"]), ("char-kai-shirr", O652, ["M652a"]), ("char-dulia-chai", O652, ["M652e"]),
   ("char-chai-nuzz", O652, ["M652d"]), ("loc-eulmore", O652, ["M652c"]), ("char-wrenden", O654, ["M654g"]),
 ],
 "evt-an-emperor-slain": [
   ("char-estinien", O657, ["M657c"]), ("char-krile", O657, ["M657p"]), ("char-zenos", O657, ["M657e"]),
   ("char-varis", O657, ["M657f"]), ("char-gaius", O657, ["M657d"]), ("char-elidibus", O657, ["M657k"]),
   ("char-white-robed-figure", O657, ["M657j"]), ("char-maxima", O658, ["M658a"]), ("char-yshtola", O659, ["M659c"]),
   ("char-graha-tia", O659, ["M659a"]),
 ],
 "evt-the-false-hero": [
   ("char-lyna", O660, ["M660a"]), ("char-alphinaud", O660, ["M660a"]), ("char-graha-tia", O660, ["M660f"]),
   ("char-ardbert", O660, ["M660e"]), ("char-elidibus", O661, ["M661h"]), ("char-urianger", O661, ["M661j"]),
   ("char-emet-selch", O661, ["M661i"]), ("char-yshtola", O662, ["M662e"]), ("char-thancred", O663, ["M663c"]),
   ("char-ryne", O663, ["M663c"]),
 ],
 "evt-records-of-the-ancients": [
   ("char-urianger", O665, ["M665a"]), ("char-yshtola", O666, ["M666h"]), ("char-venat", O666, ["M666c"]),
   ("char-white-robed-figure", O667, ["M667j"]), ("char-zodiark", O666, ["M666d"]), ("char-elidibus", O666, ["M666d"]),
   ("char-thancred", O667, ["M667f"]), ("char-graha-tia", O667, ["M667h"]), ("char-zenos", O667, ["M667m"]),
   ("char-alphinaud", O668, ["M668d"]),
 ],
 "evt-the-emissary-unmasked": [
   ("char-elidibus", O669, ["M669d"]), ("char-alisaie", O669, ["M669c"]), ("char-graha-tia", O669, ["M669f"]),
   ("char-ryne", O669, ["M669j"]), ("char-thancred", O670, ["M670a"]), ("char-krile", O670, ["M670h"]),
   ("char-tataru", O670, ["M670j"]), ("char-yshtola", O672, ["M672b"]), ("char-hythlodaeus", O673, ["M673g"]),
   ("char-emet-selch", O673, ["M673h"]),
 ],
 "evt-the-exarchs-vigil": [
   ("char-graha-tia", O674, ["M674e"]), ("char-elidibus", O674, ["M674e"]), ("char-beq-lugg", O674, ["M674m"]),
   ("char-lyna", O674, ["M674h"]), ("char-yshtola", O674, ["M674a"]), ("char-ryne", O675, ["M675i"]),
   ("char-emet-selch", O675, ["M675n"]), ("char-alisaie", O676, ["M676h"]), ("char-urianger", O677, ["M677a"]),
   ("char-seto", O677, ["M677f"]),
 ],
 "evt-homeward-bound": [
   ("char-yshtola", O678, ["M678c"]), ("char-thancred", O678, ["M678e"]), ("char-ryne", O678, ["M678f"]),
   ("char-lyna", O678, ["M678h"]), ("char-beq-lugg", O679, ["M679a"]), ("char-graha-tia", O679, ["M679g"]),
   ("char-fandaniel", O679, ["M679m"]), ("char-zenos", O679, ["M679j"]), ("char-alisaie", O680, ["M680h"]),
   ("char-lyse", O680, ["M680b"]),
 ],
}

ARC_NOTES = {
 "arc-o1-souls-adrift": "MSQ #648 *Shaken Resolve* to #651 *Good for the Soul* (5.1): the Scions' failing bodies (M648c) and the auracite plan (M648f), "
   "Beq Lugg found and won over (M649c, M650b), and the first cure for a stagnant soul (M651e). It ends where Kai-Shirr's summons turns the story to Eulmore (M651h).",
 "arc-o2-the-missing-mayor": "MSQ #652 *Nowhere to Turn* to #656 *Moving Forward* (5.1): Chai-Nuzz's disappearance (M652d), the search through Kholusia (M654b), "
   "the Talos (M655c) and his inaugural address (M656a). It ends as Alphinaud turns back to the Scions' own work (M656g).",
 "arc-o3-an-emperor-slain": "MSQ #657 *Vows of Virtue, Deeds of Cruelty* to #659 *The Way Home* (5.1–5.2): Varis's murder and the civil war (M657f, M657i), "
   "the new Ultima Weapon (M658d) and the spirit vessel that cannot yet receive memory (M659d). It ends on Lyna's request (M659g), which opens the next arc.",
 "arc-o4-the-false-hero": "MSQ #660 *Seeking Counsel* to #664 *Deep Designs* (5.2): the stranger calling himself a Warrior of Light (M660d), the false Ardbert at the Exedra (M661d), "
   "the Ronkan mural (M662d) and Elidibus unmasked (M663d), ending on the benthos and the ruins beneath the Tempest (M664f). Its name avoids #663's *An Old Friend*.",
 "arc-o5-records-of-the-ancients": "MSQ #665 *A Whale's Tale* to #668 *In the Name of the Light* (5.2–5.3): Bismarck (M665a), the Anamnesis Anyder record of Venat and Elidibus (M666d), "
   "the false starshower (M667c) and Moren's history of the title (M668c). It ends on Alphinaud's resolve to stay until Elidibus is dealt with (M668g).",
 "arc-o6-the-emissary-unmasked": "MSQ #669 *Heroic Dreams* to #673 *Etched in the Stars* (5.3): Elidibus's vow (M669h), Thancred's collapse (M670a), the Exarch's crystal plan (M671d) "
   "and Elidibus exposed as a primal (M672d), ending with Hythlodaeus's crystal (M673g). Urianger and Beq Lugg live in the entity records, because the cast is full.",
 "arc-o7-the-exarchs-vigil": "MSQ #674 *The Converging Light* to #677 *The Journey Continues* (5.3): the stolen vessel (M674e), the battle atop the tower and the Exarch's crystallization (M675e, M675g), "
   "and the farewells, ending with Ardbert's crystal returned to Seto (M677f). Its name comes from the Journal's \"silent vigil\" (M675h).",
 "arc-o8-homeward-bound": "MSQ #678 *Unto the Morrow* to #681 *The Wisdom of Allag* (5.3–5.4): the last goodbyes (M678h), the Scions waking in the Source and G'raha Tia joining them (M679c, M679f), "
   "and Alisaie's search for a cure for tempering (M680h), which the 5.4 era carries on from #682. Runar and Tataru are in the entity records rather than the cast.",
}

DECISIONS = [
 "**Eight arcs (o1–o8)** cover every step from #648 to #681 without sharing steps; each is 3–5 steps long. The last arc ends at the era's edge, mid-way through Alisaie's search, which the 5.4 era continues.",
 "**The Exarch is `char-graha-tia`** (alias \"The Crystal Exarch\"), the identity 5.0 reveals (#636, #639). Text calls him the Exarch, as the pages do; his 5.1 claims cite Krile calling him \"Raha\" (M648k) and Urianger's \"cast aside his very name\" (M671h). From #679 the pages name G'raha Tia, the youth who joins the Scions (`member-of` the Scions).",
 "**Elidibus in Ardbert's body is a possession** (`char-ardbert` possessed-by `char-elidibus`, #657–#675), not a reveal: the player sees him take the body at #657, so the impostor of #661 is Elidibus from the start. Elidibus carries no \"Ardbert\" alias, so the name keeps pointing at Ardbert.",
 "**The white-robed figure → Fandaniel** follows the Marques → Cid pattern: `char-white-robed-figure` from #657, `revealed-as` `char-fandaniel` at #679, where he shows Asahi's face and names himself. Asahi (dead) is `possessed-by` Fandaniel from #679. House Brutus stays out of text (surname).",
 "**Zenos's body** is no longer Elidibus's from #657 (ADJUST ends `rel-zenos-possessed-by-elidibus`), and Varis's ties end at #657, where Zenos murders him.",
 "**Commander Aldynn** (the 5.2 Journal's name for Raubahn) appears only in locators; claims and text say Raubahn. \"Lyse Hext\" is only in a locator, \"Nerva\" too (text says \"his cousin\").",
 "**Left out as entities** (named in text only, or not at all): Riol, F'lhaminn, Mowen, Hathenbet, the Queen Bee, Tolshs Aath, the benthos, Almet, Tiuna, Bismarck, Ken, Theyler and Vonard, Moren, Riqi-Tio, Eirwel, Rammbroes, Angelo, Owen, Nerva, Azem.",
]

ALLOW = {  # proposed: the first step in this era whose pages establish each term (5.0 establishes most of them earlier)
 "Exarch": O648, "Ryne": O648, "The First": O648, "Zodiark": O657, "Emet-Selch": O661, "Venat": O666,
 "Hythlodaeus": O673, "Fandaniel": O679,
}
