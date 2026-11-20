"""Atlas content for patches 6.1–6.3, MSQ #807 Newfound Adventure to #834 Gods Revel, Lands Tremble. Arc tag z.
Data only (docs/atlas/era-modules.md is the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes W21–W25, with W20 for the 6.0 finale just
before); every locator is an exact substring of a quest's Journal, Steps or main dialogue (cutscene stage directions
and duty dialogue included, optional blocks and question branches excluded). Spoiler rules this module follows:
  - the great wyrm is one entry, `char-vrtra` ("Vrtra"), carrying his simulacrum's name "Varshahn" as an alias: the
    6.0 Thavnair chain reveals that Varshahn is Vrtra's vessel, and #810 says so again (G'raha: "Should I continue
    calling you 'Varshahn'?");
  - the dark-robed voidsent is one entry, `char-zero`, named "The dark-robed voidsent" from #807 (her first glimpse)
    and "Zero" from #819, where Y'shtola names her; her tie to Zenos is told from #818, where the dialogue states it;
  - the knight in black (#811) is his own entry and is "revealed as" Golbez at #819, whose Journal names "a knight in
    black named Golbez"; Golbez himself is visible from #817, where Scarmiglione names "Golbez's circle of four";
  - the four elemental Thrones (#811) become "Golbez's archfiends" at #819; the four archfiends' names appear only as
    each page names them (Scarmiglione #817, Barbariccia #821, Cagnazzo #825, Rubicante #833), never from the wiki's
    speaker tags in the #819 echo;
  - first names and titles only: no "Garlond" (the Ironworks), no "Taru" (Tataru's boutique stays unnamed), no
    "Leveilleur"; "Garlemald" and "the Thirteenth" stay text where no entry is needed.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

(Z807, Z808, Z809, Z810, Z811, Z812, Z813, Z814, Z815, Z816, Z817, Z818, Z819, Z820, Z821, Z822, Z823, Z824, Z825,
 Z826, Z827, Z828, Z829, Z830, Z831, Z832, Z833, Z834) = (f"cp-msq-{n}" for n in range(807, 835))

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #807 Newfound Adventure
 "M807a": ("Back from the edge of existence, you wonder what comes next, and Tataru's suggestion to return to adventuring strikes a chord.", "Newfound Adventure", "Tataru inquires into your plans for the future, and her suggestion of returning to your adventuring roots strikes a chord."),
 "M807b": ("You recall Emet-Selch urging you to see the Bounty's undersea ruins for yourself.", "Newfound Adventure", "you recall the words of Emet-Selch, urging you to see with your own eyes the Bounty's undersea ruins"),
 "M807c": ("Tataru names Thavnair as your next destination.", "Newfound Adventure", "Thavnair—that's where you should go next!"),
 "M807d": ("Tataru sews you traveling clothes and asks you to wear them where adventurers gather, to advertise her boutique.", "Newfound Adventure", "she asks that you wear the outfit where other adventurers might see it, and thus garner interest for Tataru Taru's Boutique"),
 "M807e": ("In the Thirteenth, a dark-robed voidsent says it has returned.", "Newfound Adventure", "The scene shifts to an unknown location in the Thirteenth. … x@Dark-robed Voidsent: And thus I am returned."),
 # #808 Bountiful Ruins
 "M808a": ("A legend says the satrap Alzadaal III allied with a dragon and brought riches back from another world.", "Bountiful Ruins", "It is said that this famous satrap not only forged an alliance with a dragon, but also returned from a journey to another world with fabulous riches in his possession."),
 "M808b": ("His treasure vault lies deep beneath the waves, its entrance said to be hidden on an island in the Bounty.", "Bountiful Ruins", "a treasure vault he constructed deep beneath the waves, the entrance to which is supposedly hidden on an island in the middle of the Bounty"),
 "M808c": ("Estinien buys a treasure map that may or may not be genuine.", "Bountiful Ruins", "This map may or may not be genuine. Either way, we'll need a ship to find out for sure."),
 "M808d": ("Estinien invites you on an expedition to recover the vault's legendary riches.", "Bountiful Ruins", "he invites you to join him on an expedition to recover the legendary riches of Alzadaal's Legacy."),
 "M808e": ("Estinien is in Thavnair because Vrtra asked him to train the Radiant Host in lancework.", "Bountiful Ruins", "He wishes me to train the Radiant Host in lancework..."),
 "M808f": ("A young fisher of Akyaali promises to find and stock a seaworthy vessel.", "Bountiful Ruins", "an eager Matsya promises to secure and stock a seaworthy vessel for your expedition."),
 "M808g": ("You agree to recruit G'raha Tia as another companion.", "Bountiful Ruins", "you agree to recruit another companion to your cause─the irrepressible G'raha Tia."),
 "M808h": ("Tataru, an experienced information broker, sends you to the taverns of Radz-at-Han for rumors.", "Bountiful Ruins", "Speaking from her considerable personal experience as an information broker, Tataru cautions you that rumors do not simply fall into one's lap."),
 # #809 Friends for the Road
 "M809a": ("Krile cannot come, being committed to another task, and sends G'raha in her place.", "Friends for the Road", "I would dearly love to accompany you, of course, but I'm afraid I'm committed to another task. … You should go, Raha. I'll stay here and mind the shop, as it were."),
 "M809b": ("G'raha suggests inviting Y'shtola.", "Friends for the Road", "Then might I suggest we invite Y'shtola?"),
 "M809c": ("Since the Scions disbanded, Y'shtola has been cloistered in the Great Gubal Library, seeking a way to cross the rift.", "Friends for the Road", "Ever since the Scions disbanded, she's spent most of her time cloistered within the Great Gubal Library, hoping to piece together a method to traverse the rift."),
 "M809d": ("Y'shtola is researching how to travel from the Source to one of its reflections.", "Friends for the Road", "I've been researching ways to travel from the Source to one of its reflections."),
 "M809e": ("Urianger and Thancred have been on a pilgrimage of sorts, as they planned.", "Friends for the Road", "True to our plan, Thancred and I embarked upon a pilgrimage of sorts"),
 "M809f": ("The Loporrits are convinced that adventurers delight in treasure hunts.", "Friends for the Road", "the Loporrits now stand convinced that adventurers delight in treasure hunts."),
 "M809g": ("Urianger asked the Students for treatises on treasure vaults for the Loporrits.", "Friends for the Road", "He sent the Students a request for materials, you see—treatises on the architecture of treasure vaults and the like."),
 "M809h": ("Thancred sits the expedition out: too many former Scions together might cause concern.", "Friends for the Road", "'tis best I sit this one out. Too many former Scions consorting with one another might be seen as a cause for concern in certain quarters."),
 "M809i": ("Thancred returns to reconnaissance, scouting the Far East.", "Friends for the Road", "I'll return to my usual reconnaissance, and scout out the situation in the Far East."),
 "M809j": ("Counting Estinien, the expedition numbers five.", "Friends for the Road", "Counting Estinien, we number five now, yes?"),
 "M809k": ("Thancred saw much of Ilsabard in chaos.", "Friends for the Road", "as we made our way around Ilsabard, we saw that much of the continent was in various stages of chaos."),
 # #810 Alzadaal's Legacy
 "M810a": ("Through traps and constructs, you reach the vault's treasures.", "Alzadaal's Legacy", "After braving a gauntlet of devilish traps and murderous constructs, you are at last free to claim the glittering treasures of Alzadaal's Legacy..."),
 "M810b": ("In the final chamber, the wyrm's youthful simulacrum Varshahn bids you keep your distance, then explains the mechanism.", "Alzadaal's Legacy", "Varshahn arrives to beg you keep your distance. After some prompting, the wyrm's youthful simulacrum agrees to divulge to you the purpose for which the mechanism was designed."),
 "M810c": ("Behind the wards lies what G'raha identifies as a working gateway to the void.", "Alzadaal's Legacy", "reveals what G'raha identifies as a functioning gateway to the void."),
 "M810d": ("G'raha addresses Varshahn as Vrtra.", "Alzadaal's Legacy", "Vrtra... Ah, my apologies. Should I continue calling you \"Varshahn\"?"),
 "M810e": ("Vrtra's alchemists made the mechanism at his behest.", "Alzadaal's Legacy", "It was crafted by our alchemists at my behest."),
 "M810f": ("A voidgate is made deliberately, unlike a fissure, an incidental tear.", "Alzadaal's Legacy", "A fissure is an incidental tear in the fabric between worlds, whereas a voidgate is the product of deliberate action."),
 "M810g": ("G'raha, the former Exarch, grows nostalgic before the portal.", "Alzadaal's Legacy", "the former Exarch waxes nostalgic about old friends and foes"),
 # #811 A Brother's Grief
 "M811a": ("Five millennia ago, in Allag's war on Meracydia, Emperor Xande made a covenant with the Cloud of Darkness, sovereign of the void.", "A Brother's Grief", "In response, Emperor Xande forged a covenant with the Cloud of Darkness, sovereign among the all-devouring denizens of the void."),
 "M811b": ("Vrtra sped to that war with his sibling Azdaja.", "A Brother's Grief", "...along with my sibling, Azdaja."),
 "M811c": ("Vrtra was the last of the brood to hatch, and Azdaja, an elder sister to him, cared for him.", "A Brother's Grief", "\"elder sister\" is the closest a mortal tongue can come to describing what she meant to me. … I was the last of our brood to hatch, and Azdaja cared for me where my sire could not."),
 "M811d": ("Azdaja plunged through the voidgate to strike at the root of the voidsent's strength.", "A Brother's Grief", "She plunged through the voidgate itself to strike at the root of their strength."),
 "M811e": ("Azdaja has been lost ever since.", "A Brother's Grief", "And Azdaja has been lost to us ever since."),
 "M811f": ("Vrtra's alchemists widened a natural fissure beneath the sea, but his simulacrum found only voidsent beyond it.", "A Brother's Grief", "it was beneath the sea that I chanced to find a natural planar fissure. … With hope in my heart, I used a simulacrum to cross the threshold...but no—I did not find her. … What I found was a host of voidsent, clamoring around the opening they had sensed."),
 "M811g": ("Urianger says Azdaja is trapped beyond a barrier, in the Thirteenth.", "A Brother's Grief", "she was trapped beyond a barrier through which neither roar nor dragon may pass. Even now, in the desolate world of the Thirteenth"),
 "M811h": ("Vrtra believes it is five thousand years too late to rescue his sister, and only guards the gate.", "A Brother's Grief", "Be that as it may, it is too late to rescue my sister. Five thousand years too late. … So when I sensed intruders in the ruins, I came only to ensure that the gate remained closed."),
 "M811i": ("Vrtra means to spend the treasure to ease his people's suffering.", "A Brother's Grief", "But the time has come to spend it, that I might alleviate my people's suffering."),
 "M811j": ("Vrtra grants Y'shtola leave to examine the gate.", "A Brother's Grief", "Would you object if I were to conduct a closer examination of the gate? … Whatever boon you ask of me, you shall have it."),
 "M811k": ("G'raha says a warding scale might let one survive the Thirteenth unchanged.", "A Brother's Grief", "With a warding scale in one's possession, one could conceivably survive a stay in the Thirteenth without being warped by its energies"),
 "M811l": ("G'raha leaves for Sharlayan, where Krile awaits you at the annex.", "A Brother's Grief", "And I must be off to Sharlayan, as well. … Mistress Krile was eager to speak with you about that request, so please come back to the annex as soon as you are able."),
 "M811m": ("Urianger returns to report to the Loporrits.", "A Brother's Grief", "the Loporrits will be anxious to receive my report"),
 "M811n": ("A knight in black sits on a throne beside four smaller elemental thrones.", "A Brother's Grief", "A knight in black walks to a throne. Four smaller elemental thrones next to it activate. The knight in black sits down."),
 "M811o": ("The Throne of Earth sensed a gate breached from the other side.", "A Brother's Grief", "I sssensed the breaching of a gate, but it was not inssstigated from this ssside."),
 "M811p": ("The Throne of Fire says an opportunity long awaited is at hand.", "A Brother's Grief", "An opportunity is upon us, the coming of which we have awaited for nigh on ten thousand years."),
 "M811q": ("The knight in black declares it time to set the war in motion and win redemption for their star.", "A Brother's Grief", "'Tis time we set the war in motion, and win redemption for our star!"),
 # #812 Sharing the Wealth
 "M812a": ("Varshahn asks you to learn the needs of Akyaali and Yedlihmad.", "Sharing the Wealth", "[Forename], you are to visit Akyaali and Yedlihmad."),
 "M812b": ("The treasure was hoarded in Alzadaal's name, a fortune Vrtra set aside for a day of need.", "Sharing the Wealth", "The riches the Radiant Host have retrieved were hoarded in Alzadaal's name—a fortune I set aside for a future day of need."),
 "M812c": ("Vrtra has the treasure sold and invested in the trading port of Yedlihmad.", "Sharing the Wealth", "Firstly, the treasure shall be sold for more convenient currency, thence invested into the trading port of Yedlihmad."),
 "M812d": ("All who receive the treasure must give part of their future earnings to run an orphanage.", "Sharing the Wealth", "A contract shall be written, requiring all who receive of Alzadaal's treasure to commit a portion of their future earnings towards the running of an orphanage."),
 "M812e": ("The initiative is named the Khalzahl Foundation.", "Sharing the Wealth", "Henceforth, this initiative shall be known as the \"Khalzahl Foundation\"!"),
 "M812f": ("Vrtra asks that Khalzahl be remembered as a generous merchant, not as the blasphemy that terrorized Thavnair.", "Sharing the Wealth", "Khalzahl should be remembered not as the blasphemy which terrorized Thavnair, but as a hardworking and generous man who brought much wealth to our shores."),
 # #813 Bridging the Rift
 "M813a": ("Y'shtola has learned how the device keeps the voidgate sealed, but not how to widen it.", "Bridging the Rift", "I was able to determine how it keeps the voidgate sealed, but not how it might instead be employed to expand the opening."),
 "M813b": ("House Daemir once built a man-made voidsent, a simulacrum modeled on a voidsent.", "Bridging the Rift", "After a thorough examination, they created an arcane simulacrum possessed of similar qualities. A man-made voidsent, if you will."),
 "M813c": ("Varshahn is addressed as His Excellency, the satrap.", "Bridging the Rift", "As you wish. Allow me to lead the way, Your Excellency."),
 "M813d": ("The Daemir notes may lie in a forbidden archive.", "Bridging the Rift", "If that's true, then those notes might still be stored in a forbidden archive somewhere."),
 "M813e": ("A Forum scholarch will present the petition, and suggests Fourchenault's support.", "Bridging the Rift", "Your petition would be better received if you also had the support of another well-placed acquaintance. … Why, Master Fourchenault, of course!"),
 "M813f": ("Fourchenault brings the request before the Forum.", "Bridging the Rift", "I will add your request to the list of today's deliberations"),
 "M813g": ("Reminded of the debt it owes you, the Forum grants entry to the archives.", "Bridging the Rift", "it was agreed that allowing you entry to the archives was the least we could do in return."),
 "M813h": ("Fourchenault warns of repercussions if the knowledge is misused.", "Bridging the Rift", "Forbidden knowledge is to be treated with the utmost caution, and there will be repercussions if it is not."),
 "M813i": ("Y'shtola tells of a brother who has given up on reuniting with his sister.", "Bridging the Rift", "But the brother has given up on thoughts of reunion."),
 # #814 Restricted Reading
 "M814a": ("The Daemir log sets out a method for manipulating rift-spanning apertures.", "Restricted Reading", "The following pages detail an advanced method for manipulating rift-spanning apertures as devised by Nuhashahn, the ninth patriarch of House Daemir."),
 "M814b": ("The Atomos absorbed a planar fissure into its flesh and could expand it at will into a gate.", "Restricted Reading", "Our findings revealed that the Atomos had absorbed a planar fissure into its own flesh, which it could expand at will into a functioning gate."),
 "M814c": ("House Daemir built an artificial Atomos.", "Restricted Reading", "We proceeded to embed said prism into an arcane simulacrum, thus completing what we have dubbed our 'artificial Atomos'."),
 "M814d": ("Y'shtola recruits a Hannish alchemist for the House Daemir project.", "Restricted Reading", "Fortunately, we know a Hannish alchemist who would be delighted to involve herself in our House Daemir project."),
 "M814e": ("Nidhana learns of a secret voidgate sealed in the ruins at the bottom of the Bounty.", "Restricted Reading", "So, there's a secret voidgate...and it's sealed in the ruins at the bottom of the Bounty?"),
 "M814f": ("The plan needs Vrtra's authority to command the voidgate.", "Restricted Reading", "The idea I have in mind won't amount to much without his authority to command the voidgate."),
 # #815 Void Theory
 "M815a": ("Y'shtola tests the warding scale against the Thirteenth's corruption.", "Void Theory", "Announcing her intention to test the efficacy of the warding scale against the corrupting influence of the Thirteenth"),
 "M815b": ("The warded familiar is unharmed but its companion begins to change, so the scale needs augmenting.", "Void Theory", "while the warded familiar appears unaffected, its unprotected comrade has already begun to transform into a creature of the void. Y'shtola notes that, although G'raha Tia's hypothesis appears to be correct, the talisman will require augmentation to withstand the relentless influence of the Thirteenth."),
 "M815c": ("The Thirteenth is a reflection of the Source drowned in Darkness.", "Void Theory", "The Thirteenth is a reflection of the Source that was drowned in a flood of Darkness."),
 "M815d": ("Its fall came of the Ascians' attempts to force a Rejoining.", "Void Theory", "In Emet-Selch's own words, this tragedy was a result of the Ascians' attempts to force a Rejoining."),
 "M815e": ("Voidsent break through, and Varshahn bars the gate in the name of Alzadaal III.", "Void Theory", "In the name of Alzadaal III... I bar this door unto the void!"),
 "M815f": ("Nidhana asks for the satrap's family archives to build the Atomos.", "Void Theory", "Might I be so bold as to request access to the satrap's family archives?"),
 "M815g": ("Varshahn argues against the expedition, though his heart seems to say otherwise.", "Void Theory", "Varshahn considers these horrors good reason to discourage your expedition, but something in his demeanor suggests he feels otherwise in his heart of hearts"),
 "M815h": ("Y'shtola brings Varshahn and Estinien along to the vault.", "Void Theory", "Y'shtola has returned from the city with not only Varshahn, but also Estinien in tow."),
 # #816 A Satrap's Duty
 "M816a": ("You bring the talisman to the Ironworks operation in Rhalgr's Reach.", "A Satrap's Duty", "you settle on bringing the problem to the Garlond Ironworks operation in Rhalgr's Reach"),
 "M816b": ("Cid agrees to make a protective case for the talisman, enlisting Nero and his data on the Thirteenth.", "A Satrap's Duty", "Cid agrees to fashion a protective case for the talisman, even promising to enlist the incorrigible Nero and his trove of data on the Thirteenth"),
 "M816c": ("Cid notes that the void's corruption once seeped into Nero through his wounds.", "A Satrap's Duty", "much as the void's corruption seeped into Nero through his wounds."),
 "M816d": ("Nidhana has found the components the Atomos needs.", "A Satrap's Duty", "Nidhana is pleased to speak of her own good fortune in ascertaining the simulacrum's necessary components"),
 "M816e": ("Estinien told the Radiant Host of Vrtra's predicament.", "A Satrap's Duty", "Ser Estinien told us of your predicament."),
 "M816f": ("For centuries he protected Radz-at-Han without showing his true self, and the Radiant Host accepted him as their rightful ruler.", "A Satrap's Duty", "For centuries you have protected Radz-at-Han, never showing your true self. … Your dedication meant more to us than your deceit, and so did we accept you as our rightful ruler."),
 "M816g": ("Nahbdeen calls Varshahn a little brother to them all, and his sister family too.", "A Satrap's Duty", "As I have told you before, you are a little brother to us all. … And if you are family, then so, too, is your sister."),
 "M816h": ("Vrtra entrusts Radz-at-Han to his people for a time to attempt what he has dreamed of for five thousand years.", "A Satrap's Duty", "Vrtra announces he will trust Radz-at-Han to his people for a time, and attempt what he has dreamed of for five thousand long years."),
 "M816i": ("Recalling Nidhogg's grief when they were one, Estinien will follow you if Vrtra can be spared that pain.", "A Satrap's Duty", "When I was one with Nidhogg, his vengeful thoughts were my thoughts. … If there is a chance we can spare Vrtra that pain, then I will follow you."),
 "M816j": ("Y'shtola advises against involving the other ostensibly disbanded Scions.", "A Satrap's Duty", "Y'shtola advises against involving the other ostensibly disbanded Scions in your impending venture into the void."),
 "M816k": ("Guest chambers in Meghaduta will serve as your new headquarters.", "A Satrap's Duty", "guest chambers will soon be at your disposal for use as a new headquarters"),
 "M816l": ("Azdaja kept Vrtra's egg safe and warm when his sire entered dormancy.", "A Satrap's Duty", "My sire entered his dormancy before I was hatched. And so it was Azdaja who kept my egg safe and warm."),
 "M816n": ("The Radiant Host will keep Thavnair safe in the satrap's absence.", "A Satrap's Duty", "We, the Radiant Host, will keep Thavnair safe in your absence!"),
 "M816m": ("Unlike the First, the Thirteenth has been utterly subsumed by Darkness.", "A Satrap's Duty", "Unlike the First, where the Flood of Light was halted before its devastation was complete, the Thirteenth has been utterly subsumed by Darkness."),
 # #817 In Search of Azdaja
 "M817a": ("The reinforced warding scales and the artificial Atomos are complete.", "In Search of Azdaja", "both the reinforced warding scales and the artificial Atomos have been completed."),
 "M817b": ("All is ready for the quest to find Azdaja, Vrtra's sister, in the Thirteenth.", "In Search of Azdaja", "all is now in readiness for your quest to find Azdaja, his sister, in the Thirteenth."),
 "M817c": ("Varshahn is given a new vessel better suited to the dangers ahead.", "In Search of Azdaja", "Varshahn is presented with a new vessel better suited for the dangers ahead"),
 "M817d": ("Nidhana's team crafted the new body.", "In Search of Azdaja", "We spared no effort in crafting the body, and I daresay you'll find it adept at wielding weapons and magicks both."),
 "M817e": ("You are given Hydaelyn's navigational crystal, which harbors the power of Light.", "In Search of Azdaja", "You, too, are given a gift of sorts in the form of Hydaelyn's navigational crystal; harboring the power of Light, the relic could well aid you in your mission."),
 "M817f": ("The Atomos widens the voidgate enough for a man, and beyond lies a castle swarming with voidsent.", "In Search of Azdaja", "the voidgate is revealed, and thence enlarged by the Atomos to a size able to accommodate a man. … Beyond lies a castle swarming with voidsent"),
 "M817g": ("Scarmiglione devours the castle's mistress, then falls to you.", "In Search of Azdaja", "the castle's mistress is devoured by a fearsome voidsent named Scarmiglione, but your fellow uninvited guest soon falls by your hand."),
 "M817h": ("Scarmiglione calls himself archfiend of earth and first of Golbez's circle of four.", "In Search of Azdaja", "I am Scarmiglione—archfiend of earth, and first of Golbez's circle of four!"),
 "M817i": ("Y'shtola makes the castle a base of operations.", "In Search of Azdaja", "This castle should serve as a base of operations for now."),
 "M817j": ("Varshahn tells his sister he is here.", "In Search of Azdaja", "I am here, Sister. Finally here."),
 # #818 Shadowed Remnants
 "M818a": ("Varshahn's vessel cannot call across vast distances.", "Shadowed Remnants", "Alas, this vessel is not capable of calling across vast distances."),
 "M818b": ("Varshahn knows Zenos as the disgraced prince you laid low.", "Shadowed Remnants", "Zenos? The disgraced prince you yourself laid low?"),
 "M818c": ("When Zenos died, his avatar's tie to the Source was severed and it returned to the void.", "Shadowed Remnants", "When Zenos died, its connection to [[Hydaelyn|the Source]] was severed. It was forced to return to [[The Void|the void]]."),
 "M818d": ("The dark-robed voidsent was once Zenos's avatar, until you killed him.", "Shadowed Remnants", "I was once bound to the man named Zenos. … His “avatar”─until you killed him."),
 "M818e": ("Zenos took up a traditional Garlean art and forged a covenant with a being of the void.", "Shadowed Remnants", "In the name of his hunt, Zenos took up that traditional [[Garlean]] art. … And through it, he forged a covenant with a being of the void to lend him strength."),
 "M818f": ("The voidsent says Zenos stole its power and twisted its essence.", "Shadowed Remnants", "He stole my power. There was no equity in the arrangement. … My very essence was altered. Twisted into a tool to serve his desires."),
 "M818g": ("At the touch of Hydaelyn's crystal, the voidsent becomes a reaper resembling a woman.", "Shadowed Remnants", "The player and the voidsent approach each other. Hydaelyn's crystal glows. … The voidsent turns into a [[reaper]] resembling a Hyur woman."),
 "M818h": ("Y'shtola suspects the crystal purged some of her excess Darkness.", "Shadowed Remnants", "the change we witnessed, I suspect, is due to your crystal purging the excess Darkness in her."),
 "M818i": ("Zenos called you friend, and she asks what a friend is.", "Shadowed Remnants", "Zenos called you “friend.” That's what you are? A friend? … What is it? What is a friend?"),
 # #819 Where Everything Begins
 "M819a": ("She is voidsent only in part, touched by Darkness in her mother's womb.", "Where Everything Begins", "The dark-robed voidsent, however, is voidsent only in part, on account of having been touched by Darkness while still in her mother's womb"),
 "M819b": ("The Contramemoria shattered the balance of aether and Darkness engulfed the Thirteenth, turning its life to voidsent.", "Where Everything Begins", "a terrible conflict known as the Contramemoria shattered the balance of aether, causing Darkness to engulf the world. Thus was all life transformed into voidsent."),
 "M819c": ("Y'shtola suggests the name Zero, and she accepts.", "Where Everything Begins", "Desiring a name by which to call her, Y'shtola suggests “Zero”"),
 "M819d": ("In her world no one aids another without gain, so she helps for a price in aether.", "Where Everything Begins", "In this world, she explains, no one aids another unless they themselves stand to gain. The bargain is struck with an offer of aether"),
 "M819e": ("Scarmiglione returns, saying death does not exist in the void.", "Where Everything Begins", "Scarmiglione, whom you had believed slain, sets upon you once more. The archfiend reveals that death doesn't exist in the void"),
 "M819f": ("Zero turns Scarmiglione's minions to crystal, then binds him in crystal.", "Where Everything Begins", "All marvel as she uses her mysterious power to transform Scarmiglione's minions into crystals. … with Zero delivering the coup de grâce and binding him in crystal."),
 "M819g": ("The crystal shows a knight in black named Golbez, his four archfiends, and a wyrm.", "Where Everything Begins", "you experience a vision of the past─of a knight in black named Golbez, and those he proclaimed his four archfiends. Of greater interest, however, is the presence of what appears to be a wyrm..."),
 "M819h": ("Varshahn names the wyrm: Azdaja, his sister.", "Where Everything Begins", "Yes. Azdaja is her name, and she is my sister."),
 "M819i": ("In the vision Golbez bids the four feast on the dragon's aether and arise as his archfiends.", "Where Everything Begins", "Indeed. Feast, my friends. Feast, and arise as my four archfiends!"),
 "M819j": ("Zero still owes you some answers.", "Where Everything Begins", "Fortunately, as Y'shtola observes, Zero still owes you some few answers."),
 # #820 Groping in the Dark
 "M820a": ("Zero is the only one left who wields the power to bind aether in crystal.", "Groping in the Dark", "Many wielded this power during the Contramemoria, but I'm the only one left."),
 "M820b": ("Golbez's archfiends lead armies to ravage and conquer, and devour the useless.", "Groping in the Dark", "His archfiends lead armies to ravage and conquer. They devour those they deem useless."),
 "M820c": ("No one ever sees Golbez himself.", "Groping in the Dark", "He has minions. And those minions have minions. No one ever sees him."),
 "M820d": ("Countless voidsent answer to the archfiends, and they to Golbez.", "Groping in the Dark", "So countless voidsent answer to the archfiends, who in turn answer to Golbez─as your vision did suggest."),
 "M820e": ("Zero agrees to travel with you, paid in aether for each deed.", "Groping in the Dark", "Very well, Zero. I propose you travel with us, and whenever you perform a deed that requires payment, we will provide it in aether."),
 "M820f": ("Voidsent with nowhere else to go gathered in Zero's domain.", "Groping in the Dark", "But over time, others began to gather here. Those who had nowhere else to go."),
 "M820g": ("Zero's domain has one absolute rule: no voidsent may feed on another there.", "Groping in the Dark", "This is my domain's one and only rule─and it is absolute."),
 "M820h": ("A spy flees to warn Golbez.", "Groping in the Dark", "Not good... Lord Golbez must hear of this!"),
 # #821 Nowhere to Run
 "M821a": ("A voidsent who once fought in Golbez's army begged to be devoured so he would never fight again.", "Nowhere to Run", "I wouldn't have guessed that Farfarello once fought in Golbez's army. … So he begged me to devour him, that he would never have to fight again."),
 "M821b": ("Golbez learns that a memoriate has turned Scarmiglione's soul to crystal, and orders her killed.", "Nowhere to Run", "They were aided by one of our world, who transformed Scarmiglione's soul into crystal! … They cannot be suffered to live."),
 "M821c": ("The Throne of Wind, Barbariccia, takes the task.", "Nowhere to Run", "Leave this matter to me, Lord Golbez. … I, Barbariccia, shall strike down any who pose a threat to our plans."),
 "M821d": ("Golbez calls Barbariccia a proven commander.", "Nowhere to Run", "'Tis true you are a proven commander, well suited to leading an assault."),
 "M821e": ("As her reward, Barbariccia asks for the dragon's last aether.", "Nowhere to Run", "The dragon's aether. All that remains."),
 "M821f": ("The archfiends devour or press voidsent into the crusade.", "Nowhere to Run", "We will be devoured or forced to serve. To fight in the crusade."),
 "M821g": ("Barbariccia arrives at the domain, sparing herself a trip to Troia.", "Nowhere to Run", "Excellent. You've saved me the trouble of traveling to Troia."),
 "M821h": ("Barbariccia says Golbez let the dragon live to lure more prey.", "Nowhere to Run", "My Lord Golbez is more clever than I realized. To let the prize live that it might lure more prey to us."),
 "M821i": ("Varshahn agrees to pay Zero from his own aether.", "Nowhere to Run", "So long as you leave me strength enough to see my sister home, you may take as much as you wish."),
 # #822 The Wind Rises
 "M822a": ("On Zero's advice, you resolve to seal Barbariccia away rather than trust her.", "The Wind Rises", "Despite Barbariccia's vague promise of answers regarding Azdaja, on Zero's advice you resolve to seal the archfiend away at the earliest opportunity."),
 "M822b": ("You face her minions on her domain, then Barbariccia herself.", "The Wind Rises", "As you approach Barbariccia's domain, you meet with heavy resistance from her minions."),
 "M822c": ("Zero seals Barbariccia in memoria, but the crystal grants no vision.", "The Wind Rises", "Seizing her moment, Zero descends from on high to seal Barbariccia in memoria. To your disappointment, the resulting crystal does not grant you a vision"),
 "M822d": ("Another of Golbez's champions has fallen.", "The Wind Rises", "you take heart from your victory over one of Golbez's champions"),
 "M822e": ("Zero collapses from exhaustion before she is paid.", "The Wind Rises", "only to collapse from exhaustion before she can receive it."),
 "M822f": ("Varshahn suspends the mission to tend to Zero.", "The Wind Rises", "Let us suspend the mission and tend to Zero."),
 # #823 Return from the Void
 "M823a": ("Zero cannot consent, but there is no choice but to take her to the Source.", "Return from the Void", "Zero cannot give her consent, but it seems we have no choice."),
 "M823b": ("Only the archfiends may enter Golbez's domain, and none but they know where it is.", "Return from the Void", "Only the archfiends are allowed into his domain, wherever it is. None but they know."),
 "M823c": ("Golbez speaks to distant minions through staves.", "Return from the Void", "He has these...scepters? Staves? Whatever they are, he uses them to talk to those far away."),
 "M823d": ("Nahbdeen welcomes Varshahn home.", "Return from the Void", "And we are glad to receive you, Varshahn! Welcome home!"),
 "M823e": ("Varshahn is glad to be home among those he loves.", "Return from the Void", "It is good to be home again, among those whom I love dearly and missed so much."),
 "M823f": ("Y'shtola suspects Hydaelyn had a hand in your meeting Zero.", "Return from the Void", "One might say that Hydaelyn had a hand in your meeting."),
 "M823g": ("Once you leave the Thirteenth, you will not return until ready to resume the search.", "Return from the Void", "once we leave the Thirteenth, we will not return until we are prepared to resume our search."),
 # #824 A World with Light and Life
 "M824a": ("Nidhana tells Zero she is in the Source, the world next door.", "A World with Light and Life", "You're in the Source, my dear─the world next door, so to speak."),
 "M824b": ("Zero has died countless times.", "A World with Light and Life", "And I have died. Countless times."),
 "M824c": ("Varshahn apologizes for bringing her without consent.", "A World with Light and Life", "We brought you to our world without your consent, and for that I apologize."),
 "M824d": ("Varshahn wants to find Golbez and free his sister.", "A World with Light and Life", "I want nothing more than to rush to her aid─to find this Golbez and free her from his clutches, if he still holds her captive."),
 "M824e": ("Varshahn is a soul in a vessel not his own.", "A World with Light and Life", "Were you aware of my nature from the start─that I was a soul occupying a vessel not my own?"),
 "M824f": ("Zero decides it was right to join you.", "A World with Light and Life", "It was the right decision to join you."),
 "M824g": ("The High Crucible's alchemists made Varshahn's bodies.", "A World with Light and Life", "They are the ones who created my bodies, and can provide you with healing as well."),
 # #825 Buried Memory
 "M825a": ("Zero tells of the Contramemoria: the Ascians taught men to summon eidolons, and heroes who bound them in crystal fell to Darkness and made voidsent.", "Buried Memory", "the [[Ascians]] came and sowed the seeds of Darkness, teaching men how to summon eidolons─beings like unto [[primals]]. … With their tainted gifts they transformed men into monsters─[[voidsent]]─and raised armies to wage new wars."),
 "M825b": ("Zero's mother was a memoriate, and both were touched by Darkness.", "Buried Memory", "My mother was one such memoriate. But in fighting to save many, she herself was touched by Darkness─as was I."),
 "M825c": ("Cast into the rift as her world fell, Zero was spared becoming wholly voidsent.", "Buried Memory", "In that moment, Zero was cast into the rift, and so was spared the fate of becoming a voidsent in full."),
 "M825d": ("Y'shtola tells Zero there is yet hope for the Thirteenth.", "Buried Memory", "[[Y'shtola]] reveals to her that there is yet hope for the Thirteenth."),
 "M825e": ("Zero agrees to keep helping in the search for Azdaja, for her price.", "Buried Memory", "she agrees to continue helping you in your quest to find [[Azdaja]]─provided her price is paid."),
 "M825f": ("Varshahn has ascertained that his sister lives.", "Buried Memory", "we managed to ascertain that my sister yet lives."),
 "M825g": ("Golbez and the Throne of Fire plan to eliminate you, with Cagnazzo's cooperation.", "Buried Memory", "If I may, my lord, I have a plan to eliminate them. … In order to guarantee its success, however, I will require Cagnazzo's cooperation."),
 "M825h": ("Cagnazzo joins in for the sport of it.", "Buried Memory", "If there's sport to be had, then I'll play along."),
 "M825i": ("Golbez says the war looms, and no sacrifice is too great.", "Buried Memory", "The war looms nigh. We cannot allow these interlopers to interfere. … No sacrifice is too great. Even should my four archfiends be lost, I will not halt my steps."),
 "M825j": ("Golbez dismisses Scarmiglione and Barbariccia as useless.", "Buried Memory", "First Scarmiglione, and now Barbariccia... Useless, the both of them."),
 "M825k": ("Estinien counts himself a former Scion.", "Buried Memory", "But we Scions─former Scions, begging your pardon─have a habit of not leaving well enough alone."),
 # #826 Once More unto the Void
 "M826a": ("Zero has fully recovered, thanks to a ready supply of food.", "Once More unto the Void", "thanks to a ready supply of food, she has made a full recovery."),
 "M826b": ("Vrtra emerges from the palace and roars, then says, as Varshahn, that he felt his sister's presence far to the north.", "Once More unto the Void", "[[Vrtra]] emerges from the palace and lets out a mighty roar. When he speaks again as Varshahn, he reveals that he felt his sister's presence far to the north."),
 "M826c": ("You set your sights on Garlemald instead of the void.", "Once More unto the Void", "rather than the void, you now set your sights on [[Garlemald]]."),
 "M826d": ("Zero says Zenos treated lives as tools.", "Once More unto the Void", "Lives were tools to him, to be used and discarded at whim."),
 "M826e": ("Zero says Zenos is dead.", "Once More unto the Void", "He is dead, and we are all better for it."),
 "M826f": ("Well fed, Zero is willing to help with the search.", "Once More unto the Void", "You've kept me amply fed. I wouldn't be averse to helping you on your search."),
 # #827 A Cold Reunion
 "M827a": ("Alphinaud says the worst is behind the Garleans, but they have a long road ahead.", "A Cold Reunion", "Though the worst is behind them, the people still have a long road ahead."),
 "M827b": ("Jullus and some soldiers have begun a restoration initiative, joined by more volunteers each day.", "A Cold Reunion", "Meanwhile, Jullus and a number of soldiers have begun a restoration initiative, with more and more volunteers joining by the day."),
 "M827c": ("Powerful voidsent have been appearing.", "A Cold Reunion", "And not the lesser kind that occasionally manifest, but ones possessed of considerable power."),
 "M827d": ("Estinien notes that Azdaja is, by all accounts, Golbez's prisoner.", "A Cold Reunion", "By all accounts, Azdaja is Golbez's prisoner, yet if she was in the Source..."),
 "M827e": ("Reapers forged pacts with voidsent and fought beside them.", "A Cold Reunion", "The scythe-wielders forged pacts with voidsent, and took to battle with the beings at their side."),
 "M827f": ("The reaper order was outlawed when some were unmasked as insurrectionists.", "A Cold Reunion", "And when some were unmasked as insurrectionists, the order was outlawed."),
 "M827g": ("The last working snowcraft lies abandoned in Cerulea Ingens.", "A Cold Reunion", "Should still be over in Cerulea Ingens, where it was abandoned."),
 "M827h": ("An engineer agrees to repair the snowcraft.", "A Cold Reunion", "I'll see if I can get your mammoth roaring again─it's the least I can do to repay your kindness."),
 "M827i": ("Alisaie questions keeping Zenos's former avatar around.", "A Cold Reunion", "Are we sure it's wise to keep Zenos's former avatar around?"),
 "M827j": ("Zero asks Alisaie why she helps these people.", "A Cold Reunion", "Why do you help these people?"),
 # #828 Kindled Spirit
 "M828a": ("The Ilsabard contingent flies in food, medicine and other necessities.", "Kindled Spirit", "The Ilsabard contingent brings in shipments of food, medicine, and other necessities by airship."),
 "M828b": ("With voidsent sightings rising, Alisaie patrols the Eblan Rime.", "Kindled Spirit", "Voidsent sightings have been increasing by the day, which is why I had a mind to go out and patrol the Eblan Rime."),
 "M828c": ("Alisaie says the people need lasting safety and security.", "Kindled Spirit", "They need lasting safety and security."),
 "M828d": ("Zero says she has no comrades.", "Kindled Spirit", "Then no, he's not my comrade. I have none. Nor will I ever, I think."),
 "M828e": ("Zero insists she is only upholding a bargain.", "Kindled Spirit", "Get along? I'm upholding my part of the bargain. There's nothing more to it than that."),
 "M828f": ("Jullus admits Garleans rejected Alphinaud and the contingent at first.", "Kindled Spirit", "When Alphinaud and the contingent first arrived, we rejected them out of hand."),
 "M828g": ("Zero accepts Jullus's buuz, being low on aether.", "Kindled Spirit", "I am running low on aether... Very well."),
 # #829 An Unforeseen Bargain
 "M829a": ("A horde of voidsent approaches from the eastern mountains.", "An Unforeseen Bargain", "A horde of voidsent are approaching from the mountains to the east. Their numbers are beyond anything we've ever seen!"),
 "M829b": ("Zero refuses to help without compensation, until Jullus reminds her of the buuz.", "An Unforeseen Bargain", "she refuses, stating that she will not risk her life without suitable compensation. [[Jullus]], however, succeeds in persuading Zero to help guard [[Tertium]] by reminding her of the buuz he gave her."),
 "M829c": ("Zero goes in Jullus's stead to find a silent supply unit, saves two soldiers and is overwhelmed until you arrive.", "An Unforeseen Bargain", "Zero, much to his surprise, offered to go in his stead. She arrived in time to save a pair of soldiers from voidsent, but soon found herself overwhelmed. Thankfully, you arrived in time to save her and put the enemy to rout."),
 "M829d": ("Jullus says he owes Zero a week's worth of buuz.", "An Unforeseen Bargain", "If anything, I owe you a week's worth of buuz."),
 "M829e": ("Thanks to Zero, there were no more casualties.", "An Unforeseen Bargain", "No, and there weren't any more casualties thanks to you."),
 "M829f": ("Alisaie wonders what moved Zero to risk her life for others.", "An Unforeseen Bargain", "Alisaie muses what might have compelled Zero to─despite her earlier objections─resolve to risk her life to save others"),
 # #830 King of the Mountain
 "M830a": ("Zero offers to come without a bargain, inspired by Alisaie's wish to help others.", "King of the Mountain", "Zero offers to accompany you without the need for a bargain, seemingly having been inspired by Alisaie's earnest desire to help others."),
 "M830b": ("At the voidgate in Lapis Manalis you face Cagnazzo, archfiend of water.", "King of the Mountain", "In the depths of Lapis Manalis, you and your companions finally locate the voidgate. There you come face-to-face with the archfiend of water, [[Cagnazzo]]"),
 "M830c": ("Cagnazzo reveals that what you took for Azdaja was only her eye.", "King of the Mountain", "reveals what you believed to be [[Azdaja|Varshahn's sister]] was, in fact, only her eye."),
 "M830d": ("Dying, Cagnazzo sends you to Golbez and dissipates, leaving Varshahn holding the eye.", "King of the Mountain", "With his dying breath, Cagnazzo bids you seek out [[Golbez]] to learn what has truly become of Azdaja. He then dissipates into [[aether]], leaving a crestfallen [[Varshahn]] holding the eye of his beloved sister."),
 "M830e": ("Cagnazzo says his part is done.", "King of the Mountain", "A pity I will not see the plan to fruition, but my part is done."),
 "M830f": ("You have cause to believe Azdaja yet lives.", "King of the Mountain", "you have cause to believe Azdaja yet lives"),
 "M830g": ("Estinien recalls that Golbez let his archfiends feed on Azdaja's aether.", "King of the Mountain", "In [Forename]'s vision, Golbez let his archfiends feed upon Azdaja's aether."),
 "M830h": ("Y'shtola wonders why the foe strikes now, five thousand years after Azdaja vanished.", "King of the Mountain", "What I find curious is why our foes chose to strike now, some five thousand years after Azdaja vanished into the void."),
 # #831 A Dragon's Resolve
 "M831a": ("Varshahn despairs that even his sister's eye is so spent of aether.", "A Dragon's Resolve", "What has become of you, that even your eye should be so spent of [[aether]]..."),
 "M831b": ("Y'shtola says the eye has not fully succumbed to Darkness, and Azdaja may have resisted.", "A Dragon's Resolve", "Though tainted, the eye has not fully succumbed to Darkness. Azdaja herself may have been able to resist its influence."),
 "M831c": ("Estinien steadies Vrtra.", "A Dragon's Resolve", "Calm yourself, [[Vrtra]]."),
 "M831d": ("Varshahn resolves to keep faith and find his sister.", "A Dragon's Resolve", "I will not lose faith. I will find my sister, wheresoever she may be."),
 "M831e": ("Y'shtola says freeing Azdaja means dealing with Golbez once and for all.", "A Dragon's Resolve", "To free Azdaja, I expect we will have to deal with [[Golbez]] once and for all"),
 "M831f": ("Alphinaud sets his sights on the ceruleum spring, fuel to keep the people warm.", "A Dragon's Resolve", "As for Alphinaud, he's set his sights on the [[ceruleum]] spring. … That much fuel would keep the people warm for a good while."),
 "M831g": ("Alphinaud has ideas for putting the old reaper village to use.", "A Dragon's Resolve", "Though should it prove safe to do so, I have some ideas for how we might put this village to use."),
 "M831h": ("The twins part ways with Zero for now.", "A Dragon's Resolve", "I suppose this is where we part ways for now."),
 # #832 Paths Barred
 "M832a": ("A light over Bhaflau Isle, connected to the vault, can be no coincidence.", "Paths Barred", "Bhaflau Isle is connected to Alzadaal's Legacy. This cannot be a coincidence."),
 "M832b": ("Y'shtola believes the enemy has come for the gate in answer to Cagnazzo's defeat.", "Paths Barred", "In response to Cagnazzo's defeat, they have come for our gate..."),
 "M832c": ("A massive fiend took to the skies.", "Paths Barred", "A massive fiend then took to the skies."),
 "M832d": ("Y'shtola and Estinien go to secure the gate.", "Paths Barred", "Then Estinien and I will make for Alzadaal's Legacy and secure the gate."),
 "M832e": ("Varshahn sends Zero with you to hunt the fiend.", "Paths Barred", "The hunt will go more swiftly with help."),
 "M832f": ("The fiend flew north toward Khadga.", "Paths Barred", "A fiend emerged from the explosion and flew towards Khadga!?"),
 "M832g": ("Estinien warns that another flying creature would spread panic.", "Paths Barred", "If another flying creature were sighted now, others will assume the worst, and panic will spread."),
 # #833 Desires Untold
 "M833a": ("You go to investigate Khadga, where the fiend is believed to be.", "Desires Untold", "you offer to investigate [[Khadga]], where the fiend that arose from the Bhaflau remnants is believed to be."),
 "M833b": ("At the summit you face Rubicante, archfiend of fire.", "Desires Untold", "At the summit of Khadga, you come face to face with the archfiend of fire, [[Rubicante]]."),
 "M833c": ("Rubicante followed Golbez when Darkness consumed the world, for Golbez spoke of salvation.", "Desires Untold", "Such tears I wept when Darkness consumed the world. Until Lord Golbez came and spoke of salvation."),
 "M833d": ("Golbez told his followers there are fourteen worlds, the Ascians' revelation.", "Desires Untold", "The Ascians' revelation. There are other worlds than this. Ours is but one of fourteen."),
 "M833e": ("Golbez means to invade the Source so the void's denizens may die and return to the Lifestream.", "Desires Untold", "Golbez is intent on invading [[the Source]], that the denizens of [[The Void|the void]] may be granted true death and return to the Lifestream."),
 "M833f": ("Golbez and Azdaja are on the moon of the Thirteenth.", "Desires Untold", "Rubicante then reveals where Golbez and [[Azdaja]] may be found: on the moon of [[the Thirteenth]]."),
 "M833g": ("The vault and its furnace have been destroyed to deny you the void; Cagnazzo and the eye were a diversion.", "Desires Untold", "We were too late. The vault has been destroyed, the alchemical furnace with it. … This was their true objective─to deny us entry into the void. … Cagnazzo and Azdaja's eye were a diversion."),
 "M833h": ("Rubicante hints that Golbez has a desire all his own, and dissipates.", "Desires Untold", "A desire which lies beyond his quest to free us from our purgatory. A desire...all his own..."),
 "M833i": ("Zero chastises Rubicante's methods and believes there is a better way.", "Desires Untold", "The revelation rattles [[Zero]], who chastises the archfiend for his methods in pursuit of release. … Zero believes there is a better way forward, a future she hopes to one day see made reality."),
 "M833j": ("Zero has learned from the people of the Source that not everything need be a trade.", "Desires Untold", "Not everything need be a trade. This I learned from the people of this world."),
 # #834 Gods Revel, Lands Tremble
 "M834a": ("The gate in the vault is lost, but Varshahn insists there must be another way to the void.", "Gods Revel, Lands Tremble", "We may have lost the gate in Alzadaal's Legacy, but there must be another way to travel to the void."),
 "M834b": ("Golbez would send voidsent to the Source, where they may die and be reborn.", "Gods Revel, Lands Tremble", "Where they may die and return to the Lifestream to be reborn."),
 "M834c": ("Rubicante deprived you of a means to cross into the void.", "Gods Revel, Lands Tremble", "Rubicante hath deprived us of a means to cross into the void."),
 "M834d": ("Cagnazzo's feint was the part he meant was done.", "Gods Revel, Lands Tremble", "Cagnazzo's feint. That was doubtless what he meant when he said his part was done."),
 "M834e": ("Estinien thinks Golbez sacrificed two archfiends to buy time to break the barrier to your world.", "Gods Revel, Lands Tremble", "Golbez sacrificed two archfiends just to stop us. He must need more time to break the barrier to our world."),
 "M834f": ("Y'shtola leaves for Sharlayan to seek other ways across the rift.", "Gods Revel, Lands Tremble", "Wishing to explore alternative methods of crossing the rift, [[Y'shtola]] departs to [[Sharlayan]] to carry out her research."),
 "M834g": ("Vrtra will seek his alchemists' counsel.", "Gods Revel, Lands Tremble", "By all means. Meanwhile, I shall seek the counsel of our alchemists."),
 "M834h": ("Zero will come next time without payment, for herself, to understand her feelings.", "Gods Revel, Lands Tremble", "Aye. And in case you're wondering, I won't ask for further payment. … I will go for myself. To try and understand why I spoke the words I said to Rubicante..."),
 "M834i": ("Vrtra vows not to fail his sister again.", "Gods Revel, Lands Tremble", "I will not fail you again, Sister..."),
 "M834j": ("Golbez says Cagnazzo and Rubicante played their parts, and he will walk alone.", "Gods Revel, Lands Tremble", "Cagnazzo and Rubicante have joined with the great flow... … You were fine pawns, my archfiends, and you have played your parts to perfection. … Hereon, I shall walk alone."),
 "M834k": ("Azdaja is trapped above Golbez's throne, in a crater on the Thirteenth's moon.", "Gods Revel, Lands Tremble", "A trapped and struggling Azdaja is above Golbez's throne. … Azdaja roars but the barrier constrains her. The camera shows that Golbez'z domain is within a crater on the Thirteenth's moon"),
 "M834l": ("Golbez speaks of an end to life on that star, and to his own suffering.", "Gods Revel, Lands Tremble", "The end to life on that star. And the end to my suffering..."),
}

# ---- Entities -------------------------------------------------------------------------------------------------------
ENTITIES = {
 # recurring from earlier eras (same id and category merge)
 "char-tataru": "character", "char-estinien": "character", "char-graha-tia": "character", "char-yshtola": "character",
 "char-urianger": "character", "char-thancred": "character", "char-krile": "character", "char-cid": "character",
 "char-nero": "character", "char-fourchenault": "character", "char-alphinaud": "character", "char-alisaie": "character",
 "char-zenos": "character",
 # the Endwalker cast the 6.0 eras are expected to introduce (conventional ids; same id and category merge)
 "char-vrtra": "character", "char-nidhana": "character", "char-jullus": "character", "org-radiant-host": "organization",
 # new in 6.1–6.3
 "char-azdaja": "character", "char-zero": "character", "char-knight-in-black": "character", "char-golbez": "character",
 "org-archfiends": "organization", "char-scarmiglione": "character", "char-barbariccia": "character",
 "char-cagnazzo": "character", "char-rubicante": "character",
 "loc-alzadaals-legacy": "location", "loc-the-thirteenth": "location", "loc-fell-court-of-troia": "location",
 "loc-zeros-domain": "location", "loc-red-moon": "location",
 "evt-the-vault-beneath-the-bounty": "event", "evt-the-road-into-the-void": "event", "evt-golbezs-archfiends": "event",
 "evt-the-trail-to-garlemald": "event", "evt-holding-to-hope": "event",
}

EX = ["The Crystal Exarch"]       # G'raha Tia's alias since the 5.0 reveal (ALLOW "Exarch" is accepted from cp-msq-542)
VA = ["Varshahn"]                 # Vrtra's simulacrum, revealed as his vessel in the 6.0 Thavnair chain
ZE = ["The dark-robed voidsent"]  # Zero, before Y'shtola named her (#819)
KB = ["The knight in black"]      # Golbez, as first seen (#811); revealed at #819
FO = ["Master Fourchenault"]
TH = ["The four Thrones"]         # Golbez's archfiends, as first seen (#811)

# ---- Presentations ---------------------------------------------------------------------------------------------------
PRES = {
 # -- the Scions and their friends
 "char-tataru": [
   P(Z807, None, "main", "Tataru",
     "A friend of the Scions with a boutique of her own. When you came back from the edge of existence wondering what came next, she urged you to return to adventuring and named Thavnair as your next destination. "
     "She sewed you new traveling clothes, asking only that you wear them where adventurers gather, to drum up interest in her shop.",
     ["M807a", "M807c", "M807d"]),
   P(Z808, None, "main", "Tataru",
     "A friend of the Scions, a seamstress with a boutique of her own and a seasoned information broker. She set you on a new adventure in Thavnair, sending you to the taverns of Radz-at-Han for rumors.",
     ["M807d", "M808h", "M807c"]),
 ],
 "char-estinien": [
   P(Z808, None, "main", "Estinien",
     "A dragoon, in Thavnair because Vrtra asked him to train the Radiant Host in lancework. In Radz-at-Han he bought a treasure map of doubtful worth and invited you on an expedition to the vault said to lie beneath the Bounty.",
     ["M808e", "M808c", "M808d", "M808b"]),
   P(Z816, None, "main", "Estinien",
     "A dragoon who joined Y'shtola's work on the voidgate beneath the Bounty. He told the Radiant Host of Vrtra's hesitation to seek his lost sister and, remembering Nidhogg's grief from when the two were one, "
     "vowed to follow you if Vrtra might be spared that pain.",
     ["M815h", "M816e", "M816i"]),
   P(Z831, None, "main", "Estinien",
     "A dragoon, and by his own account a former Scion, who has followed Vrtra's search for his sister into the void and on to Garlemald. When Vrtra despaired over Azdaja's drained eye, Estinien steadied him.",
     ["M825k", "M816i", "M831c", "M831a"]),
 ],
 "char-graha-tia": [
   P(Z809, None, "main", "G'raha Tia",
     "A Scion who has been compiling the Students of Baldesion's records with Krile at the Baldesion Annex. She sent him with you on the expedition to the vault beneath the Bounty, and he suggested inviting Y'shtola.",
     ["M809a", "M809b", "M808g"], EX),
   P(Z811, None, "main", "G'raha Tia",
     "A Scion, once the Exarch. In the vault beneath the Bounty he identified a working voidgate, deliberately made, and addressed its keeper Varshahn as Vrtra. He theorized that a warding scale might protect a traveler in the Thirteenth, "
     "then returned to Sharlayan, where Krile awaits your help with another matter.",
     ["M810g", "M810c", "M810d", "M811k", "M811l"], EX),
 ],
 "char-yshtola": [
   P(Z809, None, "main", "Y'shtola",
     "A Sharlayan sorceress and former Scion. Since the Scions disbanded she has been cloistered in Sharlayan's Great Gubal Library, researching how to travel from the Source to one of its reflections. "
     "G'raha recruited her for the expedition to the vault beneath the Bounty.",
     ["M809c", "M809d", "M809b"]),
   P(Z811, None, "main", "Y'shtola",
     "A Sharlayan sorceress, researching travel between the Source and its reflections. In the vault beneath the Bounty she found a working voidgate, and Vrtra gave her leave to study it.",
     ["M809d", "M810c", "M811j"]),
   P(Z814, None, "main", "Y'shtola",
     "A Sharlayan Archon leading the work to open the voidgate beneath the Bounty wide enough to cross. With the Forum's grudging leave she found House Daemir's research on the Atomos, a creature able to widen a planar fissure into a gate, "
     "and recruited the alchemist Nidhana to build an artificial one.",
     ["M813a", "M813g", "M814b", "M814c", "M814d"]),
   P(Z817, None, "main", "Y'shtola",
     "A Sharlayan Archon who tested and opened the way into the Thirteenth to search for Vrtra's sister. She keeps the other disbanded Scions out of the venture, and on the far side of the gate she made a castle of voidsent, Troia, the group's base.",
     ["M815a", "M817f", "M816j", "M817i"]),
   P(Z825, None, "main", "Y'shtola",
     "A Sharlayan Archon searching the Thirteenth for Vrtra's sister. She gave the half-voidsent woman who aids you her name, Zero, suspects Hydaelyn had a hand in your meeting, and has told Zero there is yet hope for her world.",
     ["M819c", "M823f", "M825d"]),
   P(Z834, None, "main", "Y'shtola",
     "A Sharlayan Archon. With the gate beneath the Bounty destroyed, she has left for Sharlayan to research other ways across the rift, so the search for Vrtra's sister may continue in the void.",
     ["M833g", "M834f", "M834a"]),
 ],
 "char-urianger": [
   P(Z809, None, "main", "Urianger",
     "A former Scion who has been on a pilgrimage of sorts with Thancred. He now advises the Loporrits, who are convinced that adventurers delight in treasure hunts, "
     "and joined the expedition to the vault beneath the Bounty to study it for them.",
     ["M809e", "M809f", "M809g"]),
 ],
 "char-thancred": [
   P(Z809, None, "main", "Thancred",
     "A former Scion who traveled Ilsabard with Urianger and found much of it in chaos. He sat out the expedition to the vault beneath the Bounty, wary that too many former Scions together would draw concern, "
     "and went back to scouting, this time in the Far East.",
     ["M809k", "M809h", "M809i"]),
 ],
 "char-krile": [
   P(Z809, None, "main", "Krile",
     "A Scion working with G'raha Tia at the Baldesion Annex in Sharlayan. Committed to another task, she sent him on your expedition in her place, and would like your help with it on your return.",
     ["M809a"]),
 ],
 "char-cid": [
   P(Z816, None, "main", "Cid",
     "An engineer of the Ironworks, whose operation works out of Rhalgr's Reach. He agreed to build a protective case for the warding scale that will shield travelers in the Thirteenth, enlisting Nero and his data on that world.",
     ["M816a", "M816b"]),
 ],
 "char-nero": [
   P(Z816, None, "main", "Nero",
     "A former tribunus who works beside Cid. The void's corruption once seeped into him through his wounds, and his trove of data on the Thirteenth goes into the warding scale's new case.",
     ["M816c", "M816b"]),
 ],
 "char-fourchenault": [
   P(Z813, None, "main", "Fourchenault",
     "Father of Alphinaud and Alisaie, and a voice in Sharlayan's Forum. He brought Y'shtola's request to enter Noumenon's restricted archives before the Forum, which granted it for the debt it owes you, "
     "and he warned of repercussions if the forbidden knowledge is misused.",
     ["M813e", "M813f", "M813g", "M813h"], FO),
 ],
 "char-alphinaud": [
   P(Z827, None, "main", "Alphinaud",
     "A young former Scion helping the Garleans recover in Tertium, beside Jullus's restoration effort. He judges the worst behind them but the road long, and reports powerful voidsent coming from the mountains to the east.",
     ["M827a", "M827b", "M827c"]),
   P(Z831, None, "main", "Alphinaud",
     "A young former Scion helping the Garleans recover. After the fight at the voidgate in Lapis Manalis, he set his sights on its ceruleum spring to keep the people warm, and has ideas for the old reaper village there.",
     ["M827a", "M830b", "M831f", "M831g"]),
 ],
 "char-alisaie": [
   P(Z828, None, "main", "Alisaie",
     "Alphinaud's twin, helping the Garleans recover in Tertium. She patrols the snow against rising voidsent, insisting the people need lasting safety rather than charity, and she is wary of keeping Zenos's former avatar close.",
     ["M827a", "M828b", "M828c", "M827i"]),
   P(Z830, None, "main", "Alisaie",
     "Alphinaud's twin, helping the Garleans recover. Her earnest wish to help others moved Zero, the half-voidsent woman who aids you, to join your search of her own will.",
     ["M828c", "M829f", "M830a"]),
 ],
 "char-zenos": [
   P(Z818, None, "main", "Zenos",
     "The disgraced prince you laid low, now dead. For his hunt he took up a traditional Garlean art and forged a covenant with a being of the void, his avatar, whose power he stole and whose essence he twisted to serve him. "
     "When he died, the avatar was forced back to the void.",
     ["M818b", "M818c", "M818d", "M818e", "M818f"]),
 ],
 "char-jullus": [
   P(Z827, None, "main", "Jullus",
     "A Garlean who, with a number of soldiers, began a restoration effort in Tertium that more volunteers join every day. He told you of the outlawed reapers, who forged pacts with voidsent, "
     "and of the last working snowcraft, abandoned in Cerulea Ingens.",
     ["M827b", "M827e", "M827f", "M827g"]),
   P(Z829, None, "main", "Jullus",
     "A Garlean leading a restoration effort in Tertium, who admits his people first rejected the contingent that brought them aid. When Zero went in his place to rescue a silent supply unit, "
     "he told her he owes her a week's worth of buuz.",
     ["M827b", "M828f", "M829c", "M829d"]),
 ],
 "char-nidhana": [
   P(Z814, None, "main", "Nidhana",
     "A Hannish alchemist of the Great Work in Thavnair, delighted to join Y'shtola's House Daemir project: an artificial Atomos to widen the secret voidgate beneath the Bounty.",
     ["M814d", "M814e", "M814c"]),
   P(Z817, None, "main", "Nidhana",
     "A Hannish alchemist of the Great Work. Working from the satrap's family archives, she completed the artificial Atomos that opened the voidgate beneath the Bounty, and her team built Varshahn a new body for the dangers of the Thirteenth.",
     ["M815f", "M816d", "M817a", "M817d"]),
 ],
 "org-radiant-host": [
   P(Z816, None, "main", "The Radiant Host",
     "Radz-at-Han's military order. Knowing that the great wyrm Vrtra protected the city for centuries without showing his true self, it accepted him as its rightful ruler, "
     "urged him not to abandon his sister, and will keep Thavnair safe while he searches for her.",
     ["M816f", "M816g", "M816n"]),
 ],
 # -- Vrtra and his sister
 "char-vrtra": [
   P(Z808, None, "main", "Vrtra",
     "A great wyrm of Thavnair, who has asked Estinien to come and train the Radiant Host in lancework.",
     ["M808e"], VA),
   P(Z810, None, "main", "Vrtra",
     "A great wyrm who walks among people in a youthful simulacrum, Varshahn. In the vault beneath the Bounty he bade you keep your distance, then lifted the seal on a device his alchemists made at his behest: a working gate to the void.",
     ["M810b", "M810d", "M810e", "M810c"], VA),
   P(Z811, None, "main", "Vrtra",
     "A great wyrm who walks among people as Varshahn. Five thousand years ago his elder sibling Azdaja, who cared for him as the last of their brood, plunged through a voidgate and was lost. "
     "His alchemists widened a fissure beneath the sea, but his simulacrum found only voidsent beyond it. Believing it too late to save her, he only guards the gate.",
     ["M811b", "M811c", "M811d", "M811f", "M811h"], VA),
   P(Z812, None, "main", "Vrtra",
     "A great wyrm who walks among people as Varshahn. He has turned the vault's treasure, set aside long ago for a day of need, to Thavnair's recovery: sold and invested in the port of Yedlihmad, "
     "with a share of future earnings bound to an orphanage, the Khalzahl Foundation.",
     ["M812b", "M812c", "M812d", "M812e"], VA),
   P(Z816, None, "main", "Vrtra",
     "The great wyrm who rules Radz-at-Han as its satrap, walking among people as Varshahn. For centuries he protected the city without showing his true self; the Radiant Host accepted him as its rightful ruler, "
     "and urged him not to abandon his sister. He has entrusted Radz-at-Han to his people for a time to search for her.",
     ["M813c", "M816f", "M816g", "M816h"], VA),
   P(Z817, None, "main", "Vrtra",
     "The great wyrm who rules Radz-at-Han, walking among people as Varshahn. In a new vessel built for the dangers ahead, he has crossed into the Thirteenth to search for his sister Azdaja.",
     ["M813c", "M817c", "M817b", "M817j"], VA),
   P(Z824, None, "main", "Vrtra",
     "The great wyrm who rules Radz-at-Han, a soul in vessels his alchemists made: Varshahn is the one he walks in. A memoria's vision showed his sister Azdaja a captive of Golbez, "
     "and back in the Source to let Zero recover, he vows to cross again and free her.",
     ["M813c", "M824e", "M824g", "M819h", "M824d"], VA),
   P(Z826, None, "main", "Vrtra",
     "The great wyrm who rules Radz-at-Han, walking among people as Varshahn. Roaring from his palace, he felt his sister's presence far to the north, and has turned the search toward Garlemald.",
     ["M813c", "M826b", "M826c"], VA),
   P(Z830, None, "main", "Vrtra",
     "The great wyrm who rules Radz-at-Han, walking among people as Varshahn. In Lapis Manalis the archfiend Cagnazzo revealed that the presence he followed was only his sister's eye, and left him holding it.",
     ["M813c", "M830c", "M830d"], VA),
   P(Z831, None, "main", "Vrtra",
     "The great wyrm who rules Radz-at-Han, walking among people as Varshahn. He despaired over his sister's drained eye until his friends steadied him, and has resolved to keep faith and find her wherever she may be.",
     ["M813c", "M831a", "M831c", "M831d"], VA),
   P(Z834, None, "main", "Vrtra",
     "The great wyrm who rules Radz-at-Han, walking among people as Varshahn. With the gate beneath the Bounty lost, he insists there must be another way to the void, seeks his alchemists' counsel, and vows not to fail his sister again.",
     ["M813c", "M834a", "M834g", "M834i"], VA),
 ],
 "char-azdaja": [
   P(Z811, None, "main", "Azdaja",
     "A dragon, Vrtra's elder sibling, who cared for him as the last of their brood to hatch. Five thousand years ago, in Allag's war, she plunged through a voidgate to strike at the root of the voidsent's strength, "
     "and has been lost ever since, trapped in the Thirteenth.",
     ["M811b", "M811c", "M811d", "M811e", "M811g"]),
   P(Z819, None, "main", "Azdaja",
     "A dragon, Vrtra's elder sibling, lost in the Thirteenth for five thousand years. A memoria's vision showed her a captive of Golbez, whose four archfiends feasted on her aether.",
     ["M811b", "M811e", "M819g", "M819h", "M819i"]),
   P(Z825, None, "main", "Azdaja",
     "A dragon, Vrtra's elder sibling and Golbez's captive in the Thirteenth, whose aether his archfiends feed on. Vrtra has ascertained that she still lives.",
     ["M811b", "M819i", "M821e", "M825f"]),
   P(Z826, None, "main", "Azdaja",
     "A dragon, Vrtra's elder sibling, held captive by Golbez. Vrtra, back in the Source, has felt her presence far to the north.",
     ["M811b", "M819g", "M826b"]),
   P(Z830, None, "main", "Azdaja",
     "A dragon, Vrtra's elder sibling, held captive by Golbez. What Vrtra sensed in the north was only her eye, drained of aether, at a voidgate in Garlemald; the archfiend Cagnazzo sent you to Golbez for answers, "
     "and there is cause to believe she lives.",
     ["M811b", "M830c", "M830d", "M830f"]),
   P(Z833, None, "main", "Azdaja",
     "A dragon, Vrtra's elder sibling, held captive by Golbez on the moon of the Thirteenth. Her eye, taken from her, never fully succumbed to Darkness.",
     ["M811b", "M833f", "M831b"]),
   P(Z834, None, "main", "Azdaja",
     "A dragon, Vrtra's elder sibling, trapped and struggling above Golbez's throne in a crater on the Thirteenth's moon, held by a barrier.",
     ["M811b", "M834k"]),
 ],
 # -- the void
 "char-zero": [
   P(Z807, None, "main", "The dark-robed voidsent",
     "A dark-robed voidsent glimpsed in the Thirteenth, who says it has returned.",
     ["M807e"]),
   P(Z818, None, "main", "The dark-robed voidsent",
     "A voidsent found in the dungeon of Troia's castle. It was bound to Zenos as his avatar until he died and it was forced back to the void; Zenos stole its power and twisted its essence. "
     "At the touch of Hydaelyn's crystal it took the form of a woman, and asked you what a friend is.",
     ["M818d", "M818c", "M818f", "M818g", "M818i"]),
   P(Z819, None, "main", "Zero",
     "A woman of the Thirteenth, Zenos's former avatar, who is only part voidsent, touched by Darkness in her mother's womb. Y'shtola named her Zero. In her world no one aids another without gain, "
     "so she helps for a price in aether; she bound the archfiend Scarmiglione in crystal.",
     ["M818d", "M819a", "M819c", "M819d", "M819f"], ZE),
   P(Z820, None, "main", "Zero",
     "A half-voidsent woman, Zenos's former avatar, and the last memoriate, able to bind aether in crystal. She rules a domain that shelters voidsent with nowhere else to go, where none may feed on another, "
     "and travels with you for payment in aether.",
     ["M818d", "M820a", "M820f", "M820g", "M820e"], ZE),
   P(Z822, None, "main", "Zero",
     "A half-voidsent woman and the last memoriate, whom Golbez has ordered killed. She sealed the archfiend Barbariccia in memoria, then collapsed from exhaustion before she could be paid.",
     ["M820a", "M821b", "M822c", "M822e"], ZE),
   P(Z824, None, "main", "Zero",
     "A half-voidsent woman and the last memoriate, who has died countless times. Drained, she was carried to the Source to recover without her consent; waking there, she decided it was right to join you.",
     ["M820a", "M824b", "M823a", "M824c", "M824f"], ZE),
   P(Z825, None, "main", "Zero",
     "The last memoriate, half-voidsent. Her mother was a memoriate too; both were touched by Darkness, and when the Thirteenth fell she was cast into the rift and spared becoming wholly voidsent. "
     "She keeps helping your search for Azdaja, for her price.",
     ["M820a", "M825b", "M825c", "M825e"], ZE),
   P(Z829, None, "main", "Zero",
     "The last memoriate, half-voidsent, who says she has no comrades and helps only by bargain. Yet in Garlemald she went out alone to rescue a silent supply unit, saved two soldiers, and was overwhelmed until you came.",
     ["M820a", "M828d", "M828e", "M829c"], ZE),
   P(Z830, None, "main", "Zero",
     "The last memoriate, half-voidsent. Moved by Alisaie's wish to help others, she has joined your search of her own will, without a bargain.",
     ["M820a", "M830a"], ZE),
   P(Z833, None, "main", "Zero",
     "The last memoriate, half-voidsent. Rubicante's account of Golbez's plan rattled her: she has learned from the people of the Source that not everything need be a trade, and believes there is a better way.",
     ["M820a", "M833i", "M833j"], ZE),
   P(Z834, None, "main", "Zero",
     "The last memoriate, half-voidsent. She will come when you next venture into the void, asking no payment: she goes for herself, to understand why she spoke as she did to Rubicante.",
     ["M820a", "M834h"], ZE),
 ],
 "char-knight-in-black": [
   P(Z811, None, "main", "The knight in black",
     "A knight in black who sits on a throne beside four elemental thrones. Sensing a gate breached from the other side, he declared it time to set a war in motion and win redemption for their star.",
     ["M811n", "M811o", "M811q"]),
   P(Z819, None, "main", "The knight in black",
     "A knight in black seen on a throne beside four elemental thrones, speaking of war. A memoria's vision named him: Golbez.",
     ["M811n", "M811q", "M819g"]),
 ],
 "char-golbez": [
   P(Z817, None, "main", "Golbez",
     "A lord of the void whom the voidsent Scarmiglione serves: Scarmiglione calls himself the first of Golbez's circle of four.",
     ["M817h"]),
   P(Z819, None, "main", "Golbez",
     "A knight in black of the Thirteenth, who speaks of a war to win redemption for his star. A memoria's vision showed him proclaiming four archfiends and bidding them feast on the aether of a captive wyrm: Vrtra's sister, Azdaja.",
     ["M811q", "M819g", "M819i", "M819h"], KB),
   P(Z821, None, "main", "Golbez",
     "A knight in black of the Thirteenth, whom no one ever sees. Countless voidsent answer to his archfiends, who lead his armies and devour the useless, and he holds Vrtra's sister Azdaja captive. "
     "Learning that a memoriate survives, he ordered her killed.",
     ["M820c", "M820d", "M820b", "M819h", "M821b"], KB),
   P(Z825, None, "main", "Golbez",
     "A knight in black of the Thirteenth, who holds Vrtra's sister Azdaja captive in a domain only his archfiends may enter, and speaks to distant minions through staves. "
     "With two archfiends lost, he says war looms, and that no sacrifice is too great.",
     ["M819h", "M823b", "M823c", "M825j", "M825i"], KB),
   P(Z833, None, "main", "Golbez",
     "A knight in black of the Thirteenth, who promised its people salvation. He means to invade the Source so the void's denizens may truly die and return to the Lifestream, and waits with his captive Azdaja on the moon of the Thirteenth. "
     "His archfiend Rubicante hinted at a desire all his own.",
     ["M833c", "M833e", "M833f", "M833h"], KB),
   P(Z834, None, "main", "Golbez",
     "A knight in black of the Thirteenth, who means to send its voidsent into the Source to die and be reborn. He let Cagnazzo and Rubicante die to stop you, and now walks alone, "
     "with Azdaja trapped above his throne on the moon, speaking of an end to life on that star and to his own suffering.",
     ["M834b", "M834e", "M834j", "M834k", "M834l"], KB),
 ],
 "org-archfiends": [
   P(Z811, None, "main", "The four Thrones",
     "Four elemental thrones of earth, fire, wind and water beside a knight in black's throne. They sensed a gate breached from the other side, and await an opportunity long in coming.",
     ["M811n", "M811o", "M811p"]),
   P(Z819, None, "main", "Golbez's archfiends",
     "Four archfiends whom Golbez proclaimed, bidding them feast on a captive wyrm's aether; they sit in elemental thrones beside him. Scarmiglione, archfiend of earth, called himself the first of them, and Zero has bound him in crystal.",
     ["M819g", "M819i", "M811n", "M817h", "M819f"], TH),
   P(Z821, None, "main", "Golbez's archfiends",
     "Golbez's four archfiends, who lead armies that devour the weak or press them into his crusade. With Scarmiglione sealed in memoria, Barbariccia, the archfiend of wind, has taken up the hunt for the surviving memoriate.",
     ["M820b", "M821f", "M821b", "M821c"], TH),
   P(Z822, None, "main", "Golbez's archfiends",
     "Golbez's four archfiends. Two are sealed in memoria by Zero: Scarmiglione, archfiend of earth, and Barbariccia, archfiend of wind.",
     ["M819f", "M822c", "M822d"], TH),
   P(Z825, None, "main", "Golbez's archfiends",
     "Golbez's four archfiends, two of them sealed in memoria. The Throne of Fire plans to eliminate you, with the help of Cagnazzo.",
     ["M825j", "M825g", "M825h"], TH),
   P(Z830, None, "main", "Golbez's archfiends",
     "Golbez's four archfiends. Scarmiglione and Barbariccia are sealed in memoria, and Cagnazzo, archfiend of water, fell at the voidgate in Lapis Manalis, saying his part was done.",
     ["M822d", "M830b", "M830d", "M830e"], TH),
   P(Z833, None, "main", "Golbez's archfiends",
     "Golbez's four archfiends. Scarmiglione and Barbariccia are sealed in memoria; Cagnazzo fell in Garlemald as a diversion, and Rubicante, archfiend of fire, fell atop Khadga after the vault's gate was destroyed.",
     ["M822d", "M833g", "M833b", "M833h"], TH),
   P(Z834, None, "main", "Golbez's archfiends",
     "Golbez's four archfiends, all sealed or dead. Golbez praised Cagnazzo and Rubicante as fine pawns, and says he needs no more minions.",
     ["M834j", "M834e"], TH),
 ],
 "char-scarmiglione": [
   P(Z817, None, "main", "Scarmiglione",
     "A voidsent who calls himself archfiend of earth and first of Golbez's circle of four. In the castle of Troia he devoured its mistress, then fell to you.",
     ["M817g", "M817h"]),
   P(Z819, None, "main", "Scarmiglione",
     "Golbez's archfiend of earth. He rose again after falling to you, saying death does not exist in the void, until Zero sealed him in crystal; his memoria showed you Golbez and a captive wyrm.",
     ["M817h", "M819e", "M819f", "M819g"]),
 ],
 "char-barbariccia": [
   P(Z821, None, "main", "Barbariccia",
     "Golbez's archfiend of wind and a proven commander. She volunteered to kill the surviving memoriate, asking the captive dragon's last aether as her reward, and descended on Zero's domain to draw you to her own.",
     ["M821c", "M821d", "M821e", "M821g"]),
   P(Z822, None, "main", "Barbariccia",
     "Golbez's archfiend of wind. You subdued her on her stormy domain, and Zero sealed her in memoria, though the crystal showed no vision.",
     ["M821c", "M822b", "M822c"]),
 ],
 "char-cagnazzo": [
   P(Z825, None, "main", "Cagnazzo",
     "One of Golbez's archfiends, who agreed to help the Throne of Fire's plan to eliminate you, for the sport of it.",
     ["M825g", "M825h"]),
   P(Z830, None, "main", "Cagnazzo",
     "Golbez's archfiend of water. You defeated him at the voidgate in Lapis Manalis; content that his part was done, he revealed that what you took for Azdaja was only her eye, sent you to Golbez, and dissipated into aether.",
     ["M830b", "M830e", "M830c", "M830d"]),
 ],
 "char-rubicante": [
   P(Z833, None, "main", "Rubicante",
     "Golbez's archfiend of fire, who followed him when Darkness consumed their world because Golbez spoke of salvation. Defeated atop Khadga, he revealed Golbez's design and where Golbez and Azdaja wait, "
     "hinted that his lord has a desire all his own, and dissipated into aether.",
     ["M833b", "M833c", "M833e", "M833f", "M833h"]),
 ],
 # -- places
 "loc-alzadaals-legacy": [
   P(Z810, None, "main", "Alzadaal's Legacy",
     "The treasure vault of the satrap Alzadaal III, deep beneath the Bounty and entered from an island, guarded by traps and constructs. Its final chamber hides a working gate to the void.",
     ["M808a", "M808b", "M810a", "M810c"]),
   P(Z817, None, "main", "Alzadaal's Legacy",
     "The treasure vault of Alzadaal III beneath the Bounty. Its treasure now funds Thavnair's recovery, and an artificial Atomos has widened its voidgate enough for a person to cross into the Thirteenth.",
     ["M808b", "M812c", "M817f"]),
   P(Z833, None, "main", "Alzadaal's Legacy",
     "The treasure vault of Alzadaal III beneath the Bounty, whose voidgate led to the Thirteenth. Golbez's servants have destroyed it, alchemical furnace and all, to deny you the void.",
     ["M808b", "M817f", "M833g"]),
 ],
 "loc-the-thirteenth": [
   P(Z811, None, "main", "The Thirteenth",
     "A world of the void, where Vrtra's sister Azdaja has been trapped for five thousand years. A warding scale might let a traveler survive it unchanged.",
     ["M811g", "M811k"]),
   P(Z816, None, "main", "The Thirteenth",
     "A reflection of the Source drowned in Darkness when the Ascians tried to force a Rejoining; unlike the First, it was wholly subsumed. Vrtra's sister Azdaja has been trapped there for five thousand years.",
     ["M815c", "M815d", "M816m", "M811g"]),
   P(Z819, None, "main", "The Thirteenth",
     "A reflection of the Source drowned in Darkness. A war called the Contramemoria shattered its balance of aether and turned all its life to voidsent, and the knight in black Golbez holds Vrtra's sister Azdaja captive there.",
     ["M815c", "M819b", "M819g", "M819h"]),
   P(Z825, None, "main", "The Thirteenth",
     "A reflection of the Source drowned in Darkness. Zero tells how the Ascians taught its people to summon eidolons, and how the heroes who bound them in crystal fell to Darkness and made voidsent. Y'shtola believes there is yet hope for it.",
     ["M815c", "M825a", "M825d"]),
 ],
 "loc-fell-court-of-troia": [
   P(Z817, None, "main", "The Fell Court of Troia",
     "A castle swarming with voidsent on the far side of the voidgate beneath the Bounty, whose mistress Scarmiglione devoured. Y'shtola made it the base for the search for Azdaja.",
     ["M817f", "M817g", "M817i"], ["Troia"]),
 ],
 "loc-zeros-domain": [
   P(Z820, None, "main", "Zero's Domain",
     "Zero's refuge in the Thirteenth, where voidsent with nowhere else to go have gathered. Its one absolute rule: no voidsent may feed on another there.",
     ["M820f", "M820g"]),
 ],
 "loc-red-moon": [
   P(Z833, None, "main", "The moon of the Thirteenth",
     "The moon of the void's world, where Golbez waits with his captive, Vrtra's sister Azdaja.",
     ["M833f"]),
   P(Z834, None, "main", "The moon of the Thirteenth",
     "The moon of the void's world, where Golbez's domain lies within a crater; Azdaja is trapped there above his throne.",
     ["M833f", "M834k"]),
 ],
}

# ---- Arc recaps (each arc's entry: one "story so far" per step) ---------------------------------------------------
PRES.update({
 "evt-the-vault-beneath-the-bounty": [
   P(Z807, None, "main", "The Vault beneath the Bounty",
     "Back from the edge of existence and unsure what comes next, you take Tataru's advice to return to adventuring. She names Thavnair as your destination and sews you new traveling clothes, and you recall Emet-Selch urging you to see the Bounty's undersea ruins. "
     "Far away, in the Thirteenth, a dark-robed voidsent says it has returned.",
     ["M807a", "M807c", "M807d", "M807b", "M807e"]),
   P(Z808, None, "main", "The Vault beneath the Bounty",
     "In a tavern of Radz-at-Han you hear of Alzadaal III, a satrap allied with a dragon, who hid a treasure vault beneath the waves with its entrance on an island in the Bounty. "
     "Estinien, in Thavnair to train the Radiant Host, has bought a map of doubtful worth and invites you along. A fisher of Akyaali will find a ship, and you set out to recruit G'raha Tia.",
     ["M808a", "M808b", "M808e", "M808c", "M808d", "M808f", "M808g"]),
   P(Z809, None, "main", "The Vault beneath the Bounty",
     "The expedition gathers its crew. Krile sends G'raha Tia in her place, Y'shtola sets aside her research into travel between worlds, and Urianger joins to study the vault for the Loporrits, who want a treasure hunt of their own. "
     "Thancred sits out, wary that too many former Scions together will draw notice, and five of you set sail.",
     ["M809a", "M809d", "M809f", "M809g", "M809h", "M809j"]),
   P(Z810, None, "main", "The Vault beneath the Bounty",
     "Through traps and constructs you reach the vault's treasures, but in the final chamber Varshahn, the young simulacrum through which the great wyrm Vrtra walks among people, bids you keep your distance. "
     "At his word the seal lifts on a device his alchemists made, and G'raha names it a working gate to the void, deliberately made.",
     ["M810a", "M810b", "M810d", "M810e", "M810c", "M810f"]),
   P(Z811, None, "main", "The Vault beneath the Bounty",
     "Vrtra tells his story. Five thousand years ago his elder sibling Azdaja plunged through a voidgate in Allag's war and was lost in the Thirteenth, and his own crossing found only voidsent. "
     "Believing her beyond rescue, he guards the gate, means to spend the treasure on his people, and lets Y'shtola study it. Elsewhere, a knight in black beside four elemental thrones speaks of war.",
     ["M811b", "M811d", "M811g", "M811f", "M811h", "M811i", "M811j", "M811q"]),
   P(Z812, None, "main", "The Vault beneath the Bounty",
     "Vrtra turns the vault's treasure to Thavnair's recovery. It will be sold to revive the trading port of Yedlihmad, and all who receive it must give part of their future earnings to an orphanage, the Khalzahl Foundation. "
     "Y'shtola studies the gate beneath the Bounty, while the knight in black's war waits, unexplained.",
     ["M812c", "M812d", "M812e", "M811j", "M811q"]),
 ],
 "evt-the-road-into-the-void": [
   P(Z813, None, "main", "The Road into the Void",
     "Y'shtola has learned how the device keeps the voidgate sealed, but not how to widen it, and Vrtra recalls that House Daemir once built a man-made voidsent. "
     "Their notes likely lie in Sharlayan's restricted archives, and with Fourchenault's backing the Forum grudgingly grants entry. Y'shtola quietly tells of a brother who has given up on his sister.",
     ["M813a", "M813b", "M813d", "M813e", "M813f", "M813g", "M813i"]),
   P(Z814, None, "main", "The Road into the Void",
     "In Noumenon's restricted stacks you find House Daemir's research on the Atomos, a creature that absorbs a planar fissure and can widen it into a working gate. "
     "The Daemir built an artificial one, and Y'shtola recruits the Hannish alchemist Nidhana to build another for the gate beneath the Bounty. It will need Vrtra's authority to command the gate.",
     ["M814a", "M814b", "M814c", "M814d", "M814e", "M814f"]),
   P(Z815, None, "main", "The Road into the Void",
     "At the vault, Y'shtola sends two familiars into the void, one carrying a warding scale. The warded one returns unharmed while the other begins to change, so the scale needs reinforcing. "
     "Voidsent break through before Varshahn reseals the gate, yet his heart seems set on the journey, and Nidhana asks for the satrap's family archives to build the Atomos.",
     ["M815a", "M815b", "M815e", "M815g", "M815f"]),
   P(Z816, None, "main", "The Road into the Void",
     "Cid agrees to build a protective case for the warding scale, enlisting Nero and his data on the Thirteenth, and Nidhana finds the parts for the Atomos. "
     "Vrtra still hesitates, until the Radiant Host urges him not to abandon his sister and Estinien vows to follow. He entrusts Radz-at-Han to his people for a time, and guest chambers in his palace become your base.",
     ["M816b", "M816d", "M816f", "M816g", "M816i", "M816h", "M816k"]),
   P(Z817, None, "main", "The Road into the Void",
     "With the scales and the Atomos ready, Varshahn takes a new vessel built for the dangers ahead, and you carry Hydaelyn's navigational crystal. "
     "Beyond the widened gate lies Troia, a castle of voidsent, where Scarmiglione devours its mistress before falling to you, boasting that he is first of Golbez's circle of four. Y'shtola makes the castle your base.",
     ["M817a", "M817c", "M817e", "M817f", "M817g", "M817h", "M817i"]),
   P(Z818, None, "main", "The Road into the Void",
     "Varshahn's new vessel cannot call across the void to Azdaja, so you question the castle's voidsent. In its dungeon you find the dark-robed voidsent, once Zenos's avatar, sent back to the void when he died. "
     "Hydaelyn's crystal purges some of its Darkness, and it takes the form of a woman who asks what a friend is.",
     ["M818a", "M818d", "M818c", "M818g", "M818h", "M818i"]),
 ],
 "evt-golbezs-archfiends": [
   P(Z819, None, "main", "Golbez's Archfiends",
     "For a price in aether the dark-robed voidsent explains her world: the Contramemoria drowned the Thirteenth in Darkness and made its life voidsent, and she is only part voidsent. Y'shtola names her Zero. "
     "When Scarmiglione rises again, Zero binds him in crystal, and his memoria shows a knight in black named Golbez, four archfiends, and Azdaja captive.",
     ["M819d", "M819b", "M819a", "M819c", "M819e", "M819f", "M819g", "M819h"]),
   P(Z820, None, "main", "Golbez's Archfiends",
     "Zero is the last memoriate, able to bind aether in crystal, and she rules a refuge where no voidsent may feed on another. The castle's voidsent say the archfiends lead Golbez's armies and devour the weak, while no one ever sees Golbez himself. "
     "Varshahn hires Zero for payment in aether, and a spy flees to warn Golbez.",
     ["M820a", "M820f", "M820g", "M820b", "M820c", "M820e", "M820h"]),
   P(Z821, None, "main", "Golbez's Archfiends",
     "Hearing that a memoriate lives, Golbez orders her killed, and Barbariccia, archfiend of wind, claims the task, asking the captive dragon's last aether as her reward. "
     "She descends on Zero's domain, boasting that Golbez lets the dragon live to lure more prey, and invites you to her own. Varshahn agrees to pay Zero from his own aether.",
     ["M821b", "M821c", "M821e", "M821g", "M821h", "M821i"]),
   P(Z822, None, "main", "Golbez's Archfiends",
     "On Zero's advice you mean to seal Barbariccia rather than trust her. You fight through her stormy domain and subdue her, and Zero seals her in memoria, though the crystal shows no vision. "
     "Two of Golbez's champions have fallen, but Zero collapses from exhaustion before she is paid, and Varshahn suspends the search to tend her.",
     ["M822a", "M822b", "M822c", "M822d", "M822e", "M822f"]),
   P(Z823, None, "main", "Golbez's Archfiends",
     "Zero lies drained, so you carry her back through the gate to the Source to recover, though she cannot consent. A deserter reveals that only the archfiends may enter Golbez's hidden domain and that he speaks to his minions through staves. "
     "Nahbdeen welcomes Varshahn home, and Y'shtola suspects Hydaelyn had a hand in your meeting Zero.",
     ["M823a", "M823b", "M823c", "M823d", "M823f"]),
   P(Z824, None, "main", "Golbez's Archfiends",
     "Zero wakes in the Source, a world strange to her, and learns to eat. Varshahn apologizes for bringing her without consent, admits he is a soul in a borrowed vessel, and vows to cross back and free his sister from Golbez. "
     "Touring Radz-at-Han, Zero decides it was right to join you.",
     ["M824a", "M824c", "M824e", "M824d", "M824f"]),
   P(Z825, None, "main", "Golbez's Archfiends",
     "Zero tells how the Ascians taught her people to summon eidolons, how the heroes who bound them in crystal fell to Darkness and made voidsent, and how her mother, a memoriate, held fast. "
     "Y'shtola offers hope for the Thirteenth, and Zero keeps helping, for a price. Varshahn knows Azdaja lives, while Golbez and his archfiends plot to destroy you.",
     ["M825a", "M825b", "M825d", "M825e", "M825f", "M825g", "M825i"]),
 ],
 "evt-the-trail-to-garlemald": [
   P(Z826, None, "main", "The Trail to Garlemald",
     "Zero has recovered, and you are about to return to the void when Vrtra roars from his palace: he has felt his sister's presence far to the north. "
     "The search turns from the void to Garlemald, and Zero agrees to come, since you have kept her well fed. She says Zenos treated lives as tools, and that he is dead.",
     ["M826a", "M826b", "M826c", "M826f", "M826d", "M826e"]),
   P(Z827, None, "main", "The Trail to Garlemald",
     "In Tertium you rejoin Alphinaud and Alisaie, helping Garleans recover beside Jullus's restoration effort. They report powerful voidsent from the eastern mountains, and Jullus tells of an outlawed order of reapers who made pacts with voidsent. "
     "An engineer agrees to repair a snowcraft to take you there, while Alisaie wonders whether Zenos's former avatar can be trusted.",
     ["M827a", "M827b", "M827c", "M827e", "M827f", "M827h", "M827i"]),
   P(Z828, None, "main", "The Trail to Garlemald",
     "Alisaie patrols the snow against rising voidsent sightings, insisting the people need lasting safety rather than charity. Back in Tertium, Zero accepts a dish from Jullus, though she says she has no comrades and that her place with you is only a bargain. "
     "Jullus admits Garleans first rejected the contingent that now feeds them.",
     ["M828b", "M828c", "M828g", "M828d", "M828e", "M828f"]),
   P(Z829, None, "main", "The Trail to Garlemald",
     "A horde of voidsent descends on Tertium. Zero refuses to help without payment, then agrees to stand watch for the food Jullus gave her. "
     "When a supply unit goes silent she goes out alone and saves two soldiers, then is swarmed, until you and the twins drive the voidsent off. Jullus says he owes her a week of meals.",
     ["M829a", "M829b", "M829c", "M829d", "M829e"]),
   P(Z830, None, "main", "The Trail to Garlemald",
     "Zero joins you of her own will, moved by Alisaie's kindness, and the snowcraft carries you to the caverns of Lapis Manalis, where a voidgate stands. "
     "There you defeat Cagnazzo, archfiend of water, who reveals that what Varshahn sensed was only Azdaja's eye and sends you to Golbez for answers. The gate closes with his death, leaving Varshahn holding his sister's eye.",
     ["M830a", "M830b", "M830c", "M830d", "M830f"]),
 ],
 "evt-holding-to-hope": [
   P(Z831, None, "main", "Holding to Hope",
     "Varshahn despairs over his sister's eye, so drained of aether, until Estinien steadies him and Y'shtola notes it never fully succumbed to Darkness. "
     "While the twins gather ceruleum to keep Garleans warm, he resolves to keep faith and find her, and Y'shtola says Golbez must be dealt with to free Azdaja. The twins part from Zero, who stays with you.",
     ["M831a", "M831c", "M831b", "M831f", "M831d", "M831e", "M831h"]),
   P(Z832, None, "main", "Holding to Hope",
     "As you prepare to return to the void, a light erupts over Bhaflau Isle, above the vault, and a great fiend takes flight. Y'shtola fears the enemy has come for the gate after Cagnazzo's defeat, and she and Estinien go to secure it. "
     "You and Zero hunt for word of the fiend, which flew north toward Khadga.",
     ["M832a", "M832c", "M832b", "M832d", "M832e", "M832f"]),
   P(Z833, None, "main", "Holding to Hope",
     "Atop Khadga you defeat Rubicante, archfiend of fire. He reveals that Golbez means to invade the Source so the void's denizens may truly die and return to the Lifestream, and that Golbez and Azdaja are on the moon of the Thirteenth. "
     "Meanwhile the vault's gate is destroyed, Cagnazzo and the eye a diversion, and Zero insists there is a better way.",
     ["M833b", "M833e", "M833f", "M833g", "M833i"]),
   P(Z834, None, "main", "Holding to Hope",
     "Back in Radz-at-Han you take stock: the gate beneath the Bounty is lost, and Estinien suspects Golbez sacrificed two archfiends to buy time to break the barrier to your world. "
     "Y'shtola leaves for Sharlayan to seek another way across the rift, and Zero will come next time for her own reasons. On the moon, Golbez walks alone, with Azdaja trapped above his throne.",
     ["M834a", "M834e", "M834f", "M834h", "M834j", "M834k"]),
 ],
})

# ---- Relationships --------------------------------------------------------------------------------------------------
TYPES = [("sibling-of", "sibling of", "sibling of", True)]  # as content_3_0_part1 defines it (listed so this era lints alone)

RELS = [
 ("rel-vrtra-sibling-of-azdaja", "char-vrtra", "sibling-of", "char-azdaja", Z811, None, "main", ["M811b", "M811c"]),
 ("rel-vrtra-controls-alzadaals-legacy", "char-vrtra", "controls", "loc-alzadaals-legacy", Z810, Z833, "main", ["M810b", "M810e"], ["M833g"]),
 ("rel-yshtola-aids-vrtra", "char-yshtola", "aids", "char-vrtra", Z811, None, "main", ["M811j"]),
 ("rel-graha-tia-aids-krile", "char-graha-tia", "aids", "char-krile", Z811, None, "main", ["M809a", "M811l"]),
 ("rel-knight-in-black-leads-archfiends", "char-knight-in-black", "leads", "org-archfiends", Z811, Z819, "main", ["M811n", "M811q"]),
 ("rel-nidhana-aids-yshtola", "char-nidhana", "aids", "char-yshtola", Z814, None, "main", ["M814d", "M814e"]),
 ("rel-fourchenault-aids-yshtola", "char-fourchenault", "aids", "char-yshtola", Z813, Z814, "main", ["M813e", "M813f"]),  # lead: one-step edge, end evidence must come after the start
 ("rel-estinien-aids-vrtra", "char-estinien", "aids", "char-vrtra", Z816, None, "main", ["M816e", "M816i"]),
 ("rel-radiant-host-serves-vrtra", "org-radiant-host", "serves", "char-vrtra", Z816, None, "main", ["M816f", "M816n"]),
 ("rel-cid-aids-yshtola", "char-cid", "aids", "char-yshtola", Z816, None, "main", ["M816a", "M816b"]),
 ("rel-nero-aids-cid", "char-nero", "aids", "char-cid", Z816, None, "main", ["M816b"]),
 ("rel-scarmiglione-serves-golbez", "char-scarmiglione", "serves", "char-golbez", Z817, Z819, "main", ["M817h"], ["M819f"]),
 ("rel-zero-serves-zenos", "char-zero", "serves", "char-zenos", Z818, Z819, "main", ["M818d"]),  # lead: one-step edge, end evidence must come after the start
 ("rel-knight-in-black-revealed-as-golbez", "char-knight-in-black", "revealed-as", "char-golbez", Z819, None, "main", ["M819g", "M811n"]),
 ("rel-golbez-leads-archfiends", "char-golbez", "leads", "org-archfiends", Z819, None, "main", ["M819g", "M819i"]),
 ("rel-azdaja-prisoner-of-golbez", "char-azdaja", "prisoner-of", "char-golbez", Z819, None, "main", ["M819g", "M819h", "M819i"]),
 ("rel-zero-aids-vrtra", "char-zero", "aids", "char-vrtra", Z820, None, "main", ["M820e"]),
 ("rel-zero-controls-zeros-domain", "char-zero", "controls", "loc-zeros-domain", Z820, None, "main", ["M820f", "M820g"]),
 ("rel-zero-opposes-archfiends", "char-zero", "opposes", "org-archfiends", Z819, None, "main", ["M819f"]),
 ("rel-barbariccia-opposes-zero", "char-barbariccia", "opposes", "char-zero", Z821, Z822, "main", ["M821c", "M821g"], ["M822c"]),
 ("rel-golbez-opposes-zero", "char-golbez", "opposes", "char-zero", Z821, None, "main", ["M821b"]),
 ("rel-barbariccia-member-of-archfiends", "char-barbariccia", "member-of", "org-archfiends", Z821, Z822, "main", ["M821c"], ["M822c"]),
 ("rel-cagnazzo-member-of-archfiends", "char-cagnazzo", "member-of", "org-archfiends", Z825, Z830, "main", ["M825g", "M825h"], ["M830d"]),
 ("rel-azdaja-held-at-moon-of-the-thirteenth", "char-azdaja", "held-at", "loc-red-moon", Z833, "cp-msq-841", "main", ["M833f"]),  # content_6_4_to_6_55 continues this triple from #841
]

# ---- Arcs ------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-z1-the-vault-beneath-the-bounty", "evt-the-vault-beneath-the-bounty", Z807, Z812),
 ("arc-z2-the-road-into-the-void", "evt-the-road-into-the-void", Z813, Z818),
 ("arc-z3-golbezs-archfiends", "evt-golbezs-archfiends", Z819, Z825),
 ("arc-z4-the-trail-to-garlemald", "evt-the-trail-to-garlemald", Z826, Z830),
 ("arc-z5-holding-to-hope", "evt-holding-to-hope", Z831, Z834),
]

CASTS = {
 "evt-the-vault-beneath-the-bounty": [
   ("char-tataru", Z807, ["M807a"]), ("char-zero", Z807, ["M807e"]), ("char-estinien", Z808, ["M808d"]),
   ("char-graha-tia", Z809, ["M809a"]), ("char-yshtola", Z809, ["M809d"]), ("char-urianger", Z809, ["M809g"]),
   ("char-vrtra", Z810, ["M810b"]), ("loc-alzadaals-legacy", Z810, ["M810a"]), ("char-azdaja", Z811, ["M811b"]),
   ("char-knight-in-black", Z811, ["M811q"]),
 ],
 "evt-the-road-into-the-void": [
   ("char-yshtola", Z813, ["M813a"]), ("char-vrtra", Z813, ["M813b"]), ("char-fourchenault", Z813, ["M813f"]),
   ("char-nidhana", Z814, ["M814d"]), ("char-estinien", Z815, ["M815h"]), ("char-cid", Z816, ["M816b"]),
   ("loc-fell-court-of-troia", Z817, ["M817f"]), ("char-scarmiglione", Z817, ["M817g"]), ("char-zero", Z818, ["M818d"]),
   ("char-zenos", Z818, ["M818d"]),
 ],
 "evt-golbezs-archfiends": [
   ("char-zero", Z819, ["M819c"]), ("char-golbez", Z819, ["M819g"]), ("org-archfiends", Z819, ["M819i"]),
   ("char-scarmiglione", Z819, ["M819e"]), ("char-azdaja", Z819, ["M819h"]), ("char-vrtra", Z819, ["M819h"]),
   ("char-yshtola", Z819, ["M819c"]), ("loc-zeros-domain", Z820, ["M820g"]), ("char-barbariccia", Z821, ["M821c"]),
   ("char-cagnazzo", Z825, ["M825h"]),
 ],
 "evt-the-trail-to-garlemald": [
   ("char-vrtra", Z826, ["M826b"]), ("char-zero", Z826, ["M826f"]), ("char-azdaja", Z826, ["M826b"]),
   ("char-alphinaud", Z827, ["M827a"]), ("char-alisaie", Z827, ["M827i"]), ("char-jullus", Z827, ["M827b"]),
   ("char-estinien", Z827, ["M827d"]), ("char-cagnazzo", Z830, ["M830b"]), ("char-golbez", Z830, ["M830d"]),
 ],
 "evt-holding-to-hope": [
   ("char-vrtra", Z831, ["M831d"]), ("char-azdaja", Z831, ["M831b"]), ("char-estinien", Z831, ["M831c"]),
   ("char-yshtola", Z831, ["M831e"]), ("char-zero", Z831, ["M831h"]), ("loc-alzadaals-legacy", Z832, ["M832a"]),
   ("char-rubicante", Z833, ["M833b"]), ("char-golbez", Z833, ["M833e"]), ("loc-red-moon", Z833, ["M833f"]),
   ("org-archfiends", Z834, ["M834j"]),
 ],
}

ARC_NOTES = {
 "arc-z1-the-vault-beneath-the-bounty": "MSQ #807 *Newfound Adventure* (6.1) to #812 *Sharing the Wealth*: Tataru's push back to adventuring and Emet-Selch's remembered advice (M807a, M807b), "
   "the map and the crew (M808d, M809j), the vault and its voidgate (M810c), Vrtra's account of Azdaja (M811d) and the treasure turned to Thavnair's recovery (M812c). It starts on the first 6.1 step, where 6.0 hands over, "
   "and ends before Y'shtola's work to widen the gate begins. The knight in black's scene (M811q) opens the thread the next arcs follow.",
 "arc-z2-the-road-into-the-void": "MSQ #813 *Bridging the Rift* to #818 *Shadowed Remnants* (6.1–6.2): the Daemir research and the Atomos (M814b), the warding scale (M815b, M816b), Vrtra's decision (M816h), "
   "the crossing to Troia (M817f) and the dark-robed voidsent unmasked as Zenos's former avatar (M818d). It ends before Zero is named and Golbez revealed (#819).",
 "arc-z3-golbezs-archfiends": "MSQ #819 *Where Everything Begins* to #825 *Buried Memory* (6.2): Zero named and Golbez revealed (M819c, M819g), Zero's domain (M820g), Barbariccia sealed (M822c), "
   "the return to the Source (M823a) and Zero's account of the Contramemoria (M825a). It ends on 6.2's last step, before the search turns north (#826). Cagnazzo joins the cast at #825, where the page first names him.",
 "arc-z4-the-trail-to-garlemald": "MSQ #826 *Once More unto the Void* to #830 *King of the Mountain* (6.3): Vrtra's sense of his sister in the north (M826b), the twins and Jullus in Tertium (M827b), "
   "Zero's turn (M829c, M830a) and Cagnazzo's reveal of the eye (M830c). It ends on Cagnazzo's death. Y'shtola appears in her entity record only; the cast leans on the Garlemald players.",
 "arc-z5-holding-to-hope": "MSQ #831 *A Dragon's Resolve* to #834 *Gods Revel, Lands Tremble* (6.3): Vrtra's despair and resolve (M831d), the fiend over Bhaflau (M832c), Rubicante's revelation of Golbez's design (M833e, M833f) "
   "and the lost gate, with Golbez alone on the moon (M834a, M834j). Its name avoids every quest title. 6.4 picks up from the closed route to the void.",
}

DECISIONS = [
 "**Five arcs (z1–z5)** cover every step from #807 to #834 without sharing steps; they are 6, 6, 7, 5 and 4 steps long. Names avoid every quest title (no \"Alzadaal's Legacy\" before #810, no title of a later step).",
 "**Vrtra is one entry, `char-vrtra`**, named \"Vrtra\" with the alias \"Varshahn\" on every presentation here, on the assumption that the 6.0 era reveals Varshahn as Vrtra's vessel (Marques → Cid style: `char-varshahn` revealed-as `char-vrtra` at #709b). Text says \"Varshahn\" where the pages show the simulacrum acting, and \"Vrtra\" for the wyrm.",
 "**Zero is one entry, `char-zero`**: \"The dark-robed voidsent\" from #807 (the one-line cutscene in the Thirteenth), its tie to Zenos from #818 (dialogue; the #816 stage direction that says so is a wiki note and is not used), and \"Zero\" from #819, when Y'shtola names her, keeping the old name as an alias. Zenos gets one presentation at #818 (his avatar, his death) and an ended `serves` edge from Zero (#818 only, ended at #819 by his death as the page tells it).",
 "**The knight in black → Golbez** follows Marques → Cid: `char-knight-in-black` from #811, `revealed-as` `char-golbez` from #819, whose Journal names \"a knight in black named Golbez\". Golbez himself is visible from #817 (Scarmiglione's duty line, \"first of Golbez's circle of four\").",
 "**The four Thrones → Golbez's archfiends** is one organization (`org-archfiends`) renamed at #819, with \"The four Thrones\" kept as an alias; the archfiends' names appear only from the step whose page names each one (Scarmiglione #817, Barbariccia #821, Cagnazzo #825, Rubicante #833). The #819 echo's wiki speaker tags (which name all four) are never used, and the Throne of Fire is not linked to Rubicante.",
 "**Places:** Alzadaal's Legacy (from #810, its title step), the Thirteenth, the Fell Court of Troia, Zero's Domain and the moon of the Thirteenth. Radz-at-Han, Thavnair, Garlemald, Tertium, Meghaduta and Lapis Manalis stay text only, since earlier eras already name the first three in text.",
 "**Left out as entities** (text only, or not at all): Matsya, Mehrahd, Zasshal, Jalheen, Khalzahl (named only in \"the Khalzahl Foundation\"), Nahbdeen (text only), Montichaigne (\"a Forum scholarch\"), House Daemir, the Atomos, Xande and the Cloud of Darkness, Farfarello and Ciriatto, Furcas and Andromalius, Hydaelyn's crystal.",
 "**Surnames and brands out:** \"Garlond Ironworks\" and \"Tataru Taru's Boutique\" appear only in locators (text says \"the Ironworks\" and \"her boutique\").",
]

ALLOW = {}  # no banned term needed beyond those already accepted ("Exarch", "Emet-Selch", "The First", "Nero")
