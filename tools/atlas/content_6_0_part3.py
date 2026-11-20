"""Atlas content for patch 6.0, MSQ #761 Return to the Crystarium to #780 Thou Must Live, Die, and Know: the journey to
Elpis. Arc tag x. Data only (docs/atlas/era-modules.md is the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes W12–W15); every locator is an exact substring
of a quest's Journal, Steps or main dialogue (stage directions inside cutscenes included). Spoiler rules this module
follows:
  - the Shadowbringers cast reuses the accepted IDs (char-emet-selch, char-hythlodaeus, char-elidibus, char-venat,
    char-fandaniel, char-hydaelyn, org-convocation-of-fourteen); in Elpis they appear as they were in the distant past,
    and each presentation says so on its own;
  - Fandaniel is revealed as Hermes at #762, where Elidibus and the Journal state it (Marques → Cid: the entry you knew
    first, a revealed-as edge to the new entry, and the old name as the new entry's alias);
  - the man who holds the seat of Fandaniel in Elpis is a different person, written as "the present Fandaniel" or
    "his predecessor", never as an entity;
  - "Azem" is the seat's current holder, Venat's successor (an entry with no face: see the report); Venat is only ever
    "the previous Azem";
  - nothing here names what Meteion becomes later; she is a winged girl, an entelechy and her sisters' one voice.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

(X761, X762, X763, X764, X765, X766, X767, X768, X769, X770, X771, X772, X773, X774, X775, X776, X777, X778, X779,
 X780) = (f"cp-msq-{n}" for n in range(761, 781))

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #761 Return to the Crystarium
 "M761a": ("G'raha Tia gives you his empty spirit vessel, which can work the tower's systems in the Umbilicus.", "Return to the Crystarium", "Empty now, of course, but it should allow you to operate the tower's systems in the Umbilicus."),
 "M761b": ("G'raha hopes some fragment of Elidibus's essence remains to be found.", "Return to the Crystarium", "If even the smallest fragment of Elidibus's essence remains, it should be possible to locate it."),
 "M761c": ("G'raha bids you tell anyone who asks that he is living his life to the fullest.", "Return to the Crystarium", "Should she or anyone else ask after me, tell them...I am living my life to the fullest."),
 "M761d": ("Lyna says the peace holds, and the Crystarium's people are building new lives.", "Return to the Crystarium", "The peace you gifted us continues, and we work hard to build new lives for ourselves."),
 "M761e": ("Debate rages over how to govern the city in the Exarch's absence.", "Return to the Crystarium", "Even as we speak, debate rages on over how we should run the city in the Exarch's absence."),
 "M761f": ("However they proceed, Lyna says, no one will replace their lord.", "Return to the Crystarium", "Thus far nothing is set in stone, but however we choose to proceed, we will not replace our lord. No one could."),
 "M761g": ("Ryne is the Oracle of Light, yet has never heard Hydaelyn's call.", "Return to the Crystarium", "I'm the Oracle of Light, but I've never spoken with Hydaelyn. Never once heard Her call."),
 "M761h": ("Ryne felt her connection to something immense severed one night, and saw the sky ablaze.", "Return to the Crystarium", "And then, the other night, I was jolted awake by the feeling it had been completely severed. … to my horror, the sky was ablaze."),
 "M761i": ("Hearing of the Source, Ryne knows the doom they witnessed in Amaurot has come again.", "Return to the Crystarium", "It wasn't my imagination, then. The doom we witnessed in Amaurot has come again..."),
 # #762 Hope Upon a Flower
 "M762a": ("With the spirit vessel, the Umbilicus's console finds Elidibus's imprisoned essence and projects his image.", "Hope Upon a Flower", "which locates Elidibus's imprisoned essence and projects his image into the chamber."),
 "M762b": ("Elidibus learns that Zodiark has fallen and his brethren's souls have returned to the star.", "Hope Upon a Flower", "So. He is fallen, and my brethren's souls returned to the star..."),
 "M762c": ("The doom the ancients sacrificed so much to prevent has come again.", "Hope Upon a Flower", "The doom we sacrificed so much to prevent is come again. Old burdens, now yours to bear."),
 "M762d": ("Long ago, Fandaniel shed light on the Final Days and devoted himself to a countermeasure.", "Hope Upon a Flower", "it was none other than Fandaniel who shed light upon the phenomenon of the Final Days, and thence dedicated himself to devising a countermeasure."),
 "M762e": ("Before joining the Convocation, Fandaniel was Hermes, chief of Elpis, a facility for evaluating creations.", "Hope Upon a Flower", "Prior to joining the Convocation, he served as the chief of Elpis─a facility for the evaluation of creations─and was known as Hermes."),
 "M762f": ("Elidibus finds Fandaniel's last incarnation consumed by self-loathing and hate.", "Hope Upon a Flower", "And though he inherited that noble soul...how different, this last incarnation. So consumed by self-loathing and hate."),
 "M762g": ("Elidibus sends you to Elpis, in the time when Hermes was its chief.", "Hope Upon a Flower", "You must travel to Elpis—to the time when Hermes served as its chief."),
 "M762h": ("Elidibus warns that your own reality exists as a result of the Final Days, so the past cannot be reshaped.", "Hope Upon a Flower", "For the reality you wish to save—the reality to which you must return—exists as a result of the Final Days."),
 "M762i": ("The magick consumes Elidibus's essence, and he goes to join his brethren.", "Hope Upon a Flower", "The magick consumes Elidibus's essence once and for all, and he goes to join his beloved brethren"),
 "M762j": ("Hythlodaeus is chief of the Bureau of the Architect.", "Hope Upon a Flower", "Greetings! I am Hythlodaeus, chief of the Bureau of the Architect."),
 "M762k": ("Hythlodaeus and Emet-Selch, who can see souls, spot you, and Emet-Selch makes you visible.", "Hope Upon a Flower", "Due to their talent for seeing souls, they readily catch sight of you, and at his companion's insistence, Emet-Selch augments your aether and adjusts your size."),
 "M762l": ("Hythlodaeus finds your soul's color almost identical to Azem's.", "Hope Upon a Flower", "the color of its soul is almost identical to Azem's."),
 "M762m": ("Elpis is where living beings and some arcane entities are brought for observation and research.", "Hope Upon a Flower", "Hythlodaeus explains that Elpis is where living beings and certain arcane entities are brought for in-depth observation and research."),
 "M762n": ("Hythlodaeus introduces Emet-Selch of the Convocation of Fourteen.", "Hope Upon a Flower", "Sulking beside me is the most honorable Emet-Selch of the Convocation of Fourteen."),
 "M762o": ("The two have come to speak with Hermes, on Emet-Selch's charge, and Hythlodaeus offers to guide you.", "Hope Upon a Flower", "We are here to speak with Hermes, the chief overseer of this facility"),
 "M762p": ("Having absorbed Elidibus's empowered essence, the tower holds an abundance of energy.", "Hope Upon a Flower", "Which, having absorbed my empowered essence, now harbors an abundance of energy."),
 "M762q": ("Elpis is the testing ground of creation at heavens' edge.", "Hope Upon a Flower", "the testing ground of creation at heavens' edge: Elpis."),
 # #763 Petalouda Hunt
 "M763a": ("Hythlodaeus means to look for Hermes at the main observation hub first.", "Petalouda Hunt", "Chances are he will be at the main observation hub, so let us seek him out there first."),
 "M763b": ("You stand out, and Emet-Selch wants a low profile for his errand.", "Petalouda Hunt", "Attired as you are, however, you stand out a little too much. Our dear Emet-Selch wishes to keep a low profile for his errand, so..."),
 "M763c": ("Hythlodaeus has you capture two petaloudai to make your disguise.", "Petalouda Hunt", "An aetheric rope. I want you to use it to capture, shall we say, two petaloudai."),
 "M763d": ("Even disguised, your unusual nature will be plain to anyone who looks.", "Petalouda Hunt", "Even dressed like us, your unusual nature will be plain to those who think to look."),
 "M763e": ("You will pass as Azem's familiar.", "Petalouda Hunt", "Ah, of course—Azem's."),
 # #764 In Search of Hermes
 "M764a": ("Hythlodaeus and Hermes are close collaborators who have not met in a long while.", "In Search of Hermes", "Too long indeed for close collaborators."),
 "M764b": ("Hermes is chief overseer of Elpis.", "In Search of Hermes", "Do I have the honor of addressing Hermes, chief overseer of Elpis?"),
 "M764c": ("Hermes calls Meteion a pet project, still in preliminary testing.", "In Search of Hermes", "She's a pet project of mine—still undergoing preliminary testing."),
 "M764d": ("The winged girl at his side speaks straight into your mind and wants to be friends.", "In Search of Hermes", "she can speak fluently and directly to you in your mind, and expresses her desire to be friends."),
 "M764e": ("Emet-Selch has come on official business.", "In Search of Hermes", "By my coming, I trust you already anticipate the subject."),
 "M764f": ("Hermes welcomes you to Elpis.", "In Search of Hermes", "As chief overseer of Elpis, permit me to welcome you to our facility."),
 "M764g": ("Hermes is the man who will become Fandaniel.", "In Search of Hermes", "do you strike up an acquaintance with the man who will become Fandaniel."),
 # #765 Ponder, Warrant, Cherish, Welcome
 "M765a": ("Fandaniel means to step down and has named Hermes his preferred successor.", "Ponder, Warrant, Cherish, Welcome", "Aye. Fandaniel has declared his intention to step down, and named you as his preferred successor."),
 "M765b": ("Fandaniel will return to the star of his own volition, as many have before him.", "Ponder, Warrant, Cherish, Welcome", "Of his own volition, yes. Like so many others have before him."),
 "M765c": ("For the Convocation, to retire is to return to the star.", "Ponder, Warrant, Cherish, Welcome", "Our office becomes our lives, and to retire is to return."),
 "M765d": ("Meteion is sad when others are sad: that is how Hermes made her.", "Ponder, Warrant, Cherish, Welcome", "When others are sad, I'm sad too. That's how I am. How he made me."),
 "M765e": ("Meteion reads the emotions of those around her and projects her own.", "Ponder, Warrant, Cherish, Welcome", "This is my power. I can read the emotions of those around me, and project my emotions to others in return."),
 "M765f": ("Every life-form must be tested in Elpis for its fitness to exist.", "Ponder, Warrant, Cherish, Welcome", "No, any and all life-forms must undergo extensive testing to determine their fitness to exist. Testing which is conducted here in Elpis."),
 "M765g": ("Emet-Selch insists you have nothing to do with the Convocation.", "Ponder, Warrant, Cherish, Welcome", "We simply chanced to meet at Propylaion."),
 "M765h": ("Hermes invites you along on his inspection.", "Ponder, Warrant, Cherish, Welcome", "If you wish to learn more, perhaps you would like to come too?"),
 "M765i": ("Fandaniel told Hermes he would pass the torch to him once his purpose was fulfilled.", "Ponder, Warrant, Cherish, Welcome", "He told me that, when he fulfilled his purpose, he wished to pass the torch to me."),
 # #766 Lives Apart
 "M766a": ("Hermes sets out to check on creations.", "Lives Apart", "If everyone is ready, there are a few creations I need to check on."),
 "M766b": ("The Elpis flowers' energy is what Nidhana called akasa.", "Lives Apart", "Akasa... Though I'm not familiar with the term, your description suggests it is the selfsame energy."),
 "M766c": ("Beings made of aether cannot make practical use of dynamis.", "Lives Apart", "On account of which, beings comprised of and reliant upon aether, like you and I, are unable to make practical use of dynamis."),
 "M766d": ("Meteion is an entelechy, the first possessed of free will.", "Lives Apart", "And no ordinary one at that, but the first possessed of free will."),
 "M766e": ("Hermes turned to dynamis because aether is scarce beyond the star.", "Lives Apart", "The relative scarcity of aether beyond the bounds of this star was a concern, and so I looked to another source of energy by necessity."),
 "M766f": ("The Bureau of the Architect must judge whether Meteion is living or arcane.", "Lives Apart", "it ultimately falls to the Bureau of the Architect to pass judgment."),
 # #767 Their Greatest Contribution
 "M767a": ("None of the Fourteen specializes in the celestial, so Hermes would be welcome.", "Their Greatest Contribution", "Given that there are none among the Fourteen who specialize in the celestial, he would be a welcome addition."),
 "M767b": ("Transforming before others is thought vainglorious.", "Their Greatest Contribution", "transforming in the presence of others is considered vainglorious in the extreme."),
 "M767c": ("Hermes offers to transform and fly beside a charybdis until it finds its wings.", "Their Greatest Contribution", "I shall transform and fly with it, helping it to manipulate wind until it finds its wings."),
 "M767d": ("Hythlodaeus declined a Convocation seat.", "Their Greatest Contribution", "But I declined the offer. For though my vision is exceptional, I am pedestrian in all other aspects."),
 "M767e": ("Hythlodaeus recommended Emet-Selch for the office in his stead.", "Their Greatest Contribution", "Thus did I recommend him for the office in my stead."),
 "M767f": ("Emet-Selch teaches the charybdis to fly.", "Their Greatest Contribution", "The creature needed some small assistance at first, but soon it was flying more or less on its own."),
 "M767g": ("Hermes insists the creatures be given a chance to prove themselves.", "Their Greatest Contribution", "Hermes, however, is adamant that they continue to be given a chance to prove themselves a worthy addition to the star"),
 "M767h": ("So far you have found no clear connection to the Final Days.", "Their Greatest Contribution", "thus far have uncovered no clear connection to the Final Days"),
 # #768 Aether to Aether
 "M768a": ("Doros will revert the lykaones once the paperwork is done.", "Aether to Aether", "Doros will revert them all once the paperwork is in order."),
 "M768b": ("Kairos is a memory reconfiguration system the chief created.", "Aether to Aether", "A memory reconfiguration system. The chief himself created it."),
 "M768c": ("Even a fresh slate from Kairos did not change the lykaones' behavior.", "Aether to Aether", "Even when we used Kairos to begin with a fresh slate, their behavior was unchanged."),
 "M768d": ("Creations deemed detrimental are unmade.", "Aether to Aether", "If a creation is deemed a detrimental existence, we unmake it."),
 "M768e": ("Hermes abhors altering memories, but prefers it to execution.", "Aether to Aether", "To manipulate a subject's memories is an intrusive act I deeply abhor. But it is still preferable to execution."),
 "M768f": ("Hermes asks that every option be exhausted first.", "Aether to Aether", "Before we seal their fates, we owe it to these beings to exhaust all options."),
 "M768g": ("Meteion says that to man, other beings are things to be used.", "Aether to Aether", "To man, other beings are just things. To be used and controlled. Like magic."),
 # #769 A Sentimental Gift
 "M769a": ("Meteion wants to cheer Hermes with a flower.", "A Sentimental Gift", "The meeting will make Hermes sad. I want to cheer him up. With a flower."),
 "M769b": ("The flowers are entelechies like her, and darken with Hermes's pain.", "A Sentimental Gift", "Like me, they're entelechies. Like me, they feel his pain and turn dark..."),
 "M769c": ("Hermes has been in a dark place since before he made Meteion.", "A Sentimental Gift", "He has been in a dark place. Since before he created me."),
 "M769d": ("Hermes made beings of dynamis that can cross the emptiness between stars.", "A Sentimental Gift", "I created beings of dynamis, who can traverse the vast emptiness between the stars."),
 "M769e": ("Meteion has many sisters, already departed on their journey.", "A Sentimental Gift", "She has a great many of them, and they have already departed on their journey."),
 "M769f": ("Man discards creations he deems useless without a second thought.", "A Sentimental Gift", "Creations that he deems useless are discarded with nary a second thought."),
 "M769g": ("Hermes is at times plagued by doubt in his duties.", "A Sentimental Gift", "And yet, in carrying out my duties here, there are times when I am plagued by doubt."),
 # #770 Verdict and Execution
 "M770a": ("All seven lykaones must be unmade.", "Verdict and Execution", "...And all seven must be unmade."),
 "M770b": ("Hermes will petition the Bureau of the Architect to preserve the lykaon concept as a restricted hazardous life-form.", "Verdict and Execution", "I intend to petition the Bureau of the Architect to have the concept preserved as a restricted-purpose hazardous life-form."),
 "M770c": ("Hermes finds no fault in Doros, who followed protocol.", "Verdict and Execution", "Doros has followed the correct protocols, and, as chief overseer, I can find no fault in his judgment."),
 "M770d": ("Hermes ends the last lykaon with a wind spell.", "Verdict and Execution", "Hermes summons a staff and defeats the lykaon with a wind spell."),
 "M770e": ("Taking the seat of Fandaniel would, to Hermes, mean approving his predecessor's death.", "Verdict and Execution", "Were I to take up the seat of Fandaniel, it would be tantamount to approving my predecessor's death."),
 "M770f": ("Hermes doubts he is fit to represent mankind.", "Verdict and Execution", "And to be torn by such thoughts...I do not know if I am fit to represent mankind."),
 "M770g": ("Emet-Selch tells Hermes to join the Convocation: he does not belong in Elpis.", "Verdict and Execution", "Join the Convocation, Hermes. … You do not belong here."),
 "M770h": ("Hermes asks for time to gather his thoughts.", "Verdict and Execution", "If you would still consider me in spite of everything, I beg some time to gather my thoughts."),
 "M770i": ("Hermes asks whether it is right to sacrifice lives for the star.", "Verdict and Execution", "Do you think it right that we sacrifice all these lives for the sake of the star?"),
 "M770j": ("Hermes bids the lykaon not be forgotten.", "Verdict and Execution", "Be not forgotten. In concept endure to reclaim form and one day live again."),
 "M770k": ("Doros stopped four lykaones, and three escaped.", "Verdict and Execution", "I was able to stop four. The other three escaped..."),
 # #771 Travelers at the Crossroads
 "M771a": ("Venat is the previous Azem.", "Travelers at the Crossroads", "Venat is her name, and she is the previous Azem."),
 "M771b": ("Venat recognizes her own magick on you and deduces you come from the future.", "Travelers at the Crossroads", "Venat, as she is called, recognizes the mark of her own magick upon you, and quickly deduces your origin as a traveler from the future."),
 "M771c": ("Venat is identical to the figure you met on the ship to Old Sharlayan.", "Travelers at the Crossroads", "The player realizes that the woman is identical to the shade they encountered while on the ship to Old Sharlayan."),
 "M771d": ("Emet-Selch blames his frown lines on Venat's unruly successor.", "Travelers at the Crossroads", "Easier said than done thanks to your unruly successor."),
 "M771e": ("Venat entrusted the seat of Azem to her whimsical successor.", "Travelers at the Crossroads", "Naturally, the need for such journeys has lessened considerably since I entrusted the position to my whimsical successor..."),
 "M771f": ("As Azem, Venat traveled the star to solve people's problems.", "Travelers at the Crossroads", "Long ago, when I held the seat of Azem, I was forever trekking back and forth across the star in search of answers to people's problems."),
 "M771g": ("Venat reasons she must have marked you and sent you to herself in the past.", "Travelers at the Crossroads", "Else I wouldn't have marked you so clearly and sent you unto myself in the past."),
 "M771h": ("Emet-Selch will hear your whole story as a representative of the Convocation.", "Travelers at the Crossroads", "As a representative of the Convocation, I will hear it all."),
 "M771i": ("Unlike most of the Convocation, Venat did not return to the star when she stepped down.", "Travelers at the Crossroads", "Well, she is not among said majority. Even after stepping down, she carries on with her work."),
 "M771j": ("You recover the lost crystal for Venat.", "Travelers at the Crossroads", "You deliver the crystal to Venat, who applauds your knack for finding lost items."),
 # #772 A Past, Not Yet Come to Pass
 "M772a": ("You tell Venat of Hydaelyn, the Ascians, the phantom Amaurot, Zodiark's defeat and the second Final Days.", "A Past, Not Yet Come to Pass", "The player explains the existence of Hydaelyn, the Ascians, Emet-Selch's phantom Amaurot, the defeat of Zodiark, and the beginning of the second Final Days."),
 "M772b": ("The Final Days would bring death to all Venat holds dear.", "A Past, Not Yet Come to Pass", "If the Final Days are indeed as described, they will bring death to all that I hold dear."),
 "M772c": ("Emet-Selch rejects your claim that he recreated Amaurot with phantoms.", "A Past, Not Yet Come to Pass", "Yet you claim I recreated Amaurot and populated it with phantoms of our people."),
 "M772d": ("Emet-Selch dismisses your tale and returns to his duty.", "A Past, Not Yet Come to Pass", "I've had my fill of your fiction. I will return to my duty...and you will not bother me again."),
 "M772e": ("Venat wonders whether she is Hydaelyn.", "A Past, Not Yet Come to Pass", "And if Hydaelyn is indeed me, She would believe the same."),
 "M772f": ("Venat cannot say why she would oppose the Fourteen and create Hydaelyn.", "A Past, Not Yet Come to Pass", "Why would I feel I had no recourse but to oppose the Fourteen and create this Hydaelyn..."),
 "M772g": ("Only Hermes has significant knowledge of dynamis, Venat concludes.", "A Past, Not Yet Come to Pass", "Which leads me to believe that the only person with any significant knowledge of dynamis is Hermes himself."),
 "M772h": ("Hermes's colleagues see Meteion as his personal project.", "A Past, Not Yet Come to Pass", "Hermes's colleagues view Meteion as his personal project"),
 # #773 Witness to the Spectacle
 "M773a": ("Venat will keep learning all she can about Hermes and Meteion.", "Witness to the Spectacle", "Thus I am inclined to stay our current course, and learn all we can about the chief overseer and his familiar."),
 "M773b": ("A researcher saw Hermes send a host of Meteion into the sky one night.", "Witness to the Spectacle", "She was returning late one night when she caught sight of Chief Hermes sending Meteion heavensward. A host of them."),
 "M773c": ("Hermes says he needs more tests before he can reveal his work.", "Witness to the Spectacle", "Alas, he said that he couldn't reveal anything just yet—that he needed to conduct further tests."),
 "M773d": ("Venat fears someone will misuse his discoveries, or that Hermes will help cause the Final Days.", "Witness to the Spectacle", "Which suggests that either someone will appropriate his discoveries and make use of them...or that Hermes himself will have a hand in causing the Final Days."),
 "M773e": ("While people need help, Venat cannot return to the star.", "Witness to the Spectacle", "And so long as they need help, I cannot return to the star."),
 # #774 Worthy of His Back
 "M774a": ("Venat wants to visit the site from which Hermes sent forth the Meteia.", "Worthy of His Back", "I should like to visit the site from which Hermes sent forth the Meteia."),
 "M774b": ("Argos has traveled every corner of the star with Venat, but is obstinate with strangers.", "Worthy of His Back", "Stubborn creature. There is no place on this great star we have not together traveled, and still he remains obstinate in the presence of strangers."),
 "M774c": ("Venat once sparred with Azem, less than half her age.", "Worthy of His Back", "I made the same mistake with Azem when we first sparred. Despite being less than half my age"),
 "M774d": ("Venat sees you have weathered more hardship than your tales suggest.", "Worthy of His Back", "'Tis plain you have weathered considerable hardship. Far more, even, than your tales would suggest."),
 "M774e": ("Argos has warmed to you.", "Worthy of His Back", "Well now, I daresay he has warmed to you."),
 "M774f": ("Venat hopes to find no festering wish for oblivion behind Hermes's work.", "Worthy of His Back", "My hope is that we find no connection—no festering wish for oblivion."),
 # #775 A Flower upon Your Return
 "M775a": ("A glimpse of the past shows Meteion reporting to Hermes on her sisters.", "A Flower upon Your Return", "Venat suggests a glimpse into the past, which reveals to you a conversation wherein Meteion reports to Hermes on the progress of her star-fairing sisters."),
 "M775b": ("All units are on course for their stars.", "A Flower upon Your Return", "All units fully functional and proceeding on course towards their respective stars."),
 "M775c": ("Ktisis Hyperboreia is the largest facility in Elpis.", "A Flower upon Your Return", "Venat directs your search for Hermes to Ktisis Hyperboreia - the largest facility in Elpis."),
 "M775d": ("Most of Elpis's observers, and its chief overseer, work inside Ktisis.", "A Flower upon Your Return", "'Tis there, within those sprawling habitats, that the chief overseer and most of Elpis's observers conduct the bulk of their work."),
 "M775e": ("By your account, the Fourteen tied the celestial currents to the Final Days but never found the root cause.", "A Flower upon Your Return", "According to your story, the Fourteen divined the connection between the celestial currents and the Final Days, but were never able to pinpoint the root cause of the calamity."),
 "M775f": ("Hythlodaeus wonders how Hermes, as Fandaniel, missed the subject of his own research.", "A Flower upon Your Return", "how did Hermes, in his role as Fandaniel, not recognize the subject of his own research?"),
 "M775g": ("Emet-Selch is certain Hermes has no conscious wish for the world to end.", "A Flower upon Your Return", "Hermes has no conscious wish for the world to end. Of that, I am certain."),
 "M775h": ("Venat proposes telling Hermes your tale.", "A Flower upon Your Return", "I propose that we reveal your tale to Hermes himself."),
 "M775i": ("Everyone has reached much the same conclusions about Hermes and his research.", "A Flower upon Your Return", "you realize that all have arrived at much the same conclusions with regards to the chief overseer and his research."),
 # #776 Hunger in the Garden
 "M776a": ("Hermes and Meteion are on the next isle over.", "Hunger in the Garden", "...There he is. On the next isle over. Meteion is with him."),
 "M776b": ("Emet-Selch stays back: Hermes would think he came to press the Fandaniel matter.", "Hunger in the Garden", "If I were to go, he would assume I was only there to press him on the Fandaniel matter."),
 "M776c": ("Hermes will come once his work in the gardens is done.", "Hunger in the Garden", "Then, yes, I will come. As soon as my work here is finished."),
 "M776d": ("Hythlodaeus hopes the Emet-Selch who would raise Amaurot beneath the sea never comes to be.", "Hunger in the Garden", "the Emet-Selch who would recreate Amaurot in the depths of the ocean"),
 "M776e": ("Hermes has yet to make his decision on Fandaniel.", "Hunger in the Garden", "And unrelated to my decision on Fandaniel, you say?"),
 "M776f": ("Hermes is in the Hungering Gardens.", "Hunger in the Garden", "They are close by, within the Hungering Gardens."),
 # #777 Words without Sound
 "M777a": ("Venat says the Final Days' phenomena are likely a dynamis reaction.", "Words without Sound", "The phenomena observed during these star-encompassing calamities is likely the product of a dynamis reaction."),
 "M777b": ("The first Final Days warped creation magicks; the second warped the people.", "Words without Sound", "In the first Final Days, it warped creation magicks. In the second, it warped the people themselves."),
 "M777c": ("Sundered, the people of the future hold only a fraction of the ancients' aether.", "Words without Sound", "In contrast, having been sundered, the people of the future are composed of but a fraction of our aether."),
 "M777d": ("Dynamis needs a source that shares its victims' negative emotions.", "Words without Sound", "A source to which the victims must be attuned—one that harbors the selfsame negative emotions."),
 "M777e": ("Someone or something is instigating the star's demise, Venat concludes.", "Words without Sound", "Someone—or something—is instigating the star's demise."),
 "M777f": ("Meteion cries out in pain and hatred.", "Words without Sound", "Why...why...why do we...they...hurt...hurt...hate...HATE!"),
 "M777g": ("The Meteia share one consciousness across any distance.", "Words without Sound", "The Meteia are linked to a single mind—a shared consciousness which connects them across any distance."),
 "M777h": ("Emet-Selch sends you to follow Meteion's voice.", "Words without Sound", "Follow her voice, and try to track her down."),
 # #778 Follow, Wander, Stumble, Listen
 "M778a": ("Meteion hides by matching her aether to her surroundings.", "Follow, Wander, Stumble, Listen", "Meteion renders herself invisible by matching her aetheric density to that of her surroundings, does she not?"),
 "M778b": ("Meteion cannot fly, and fears her functions are being restricted.", "Follow, Wander, Stumble, Listen", "Why can't I fly? Are my functions being restricted!?"),
 "M778c": ("Meteion's report: a star at war annihilated itself with weapons of mass destruction.", "Follow, Wander, Stumble, Listen", "deployment of weapons of mass destruction resulted in total annihilation of local population shortly thereafter."),
 "M778d": ("Hermes tasked Meteion with asking what others live for.", "Follow, Wander, Stumble, Listen", "I tasked her with asking what others live for. What gives their lives...meaning..."),
 "M778e": ("Emet-Selch asks whether the premise of the question was flawed.", "Follow, Wander, Stumble, Listen", "Did you consider what may happen if the premise of the question is flawed?"),
 "M778f": ("Venat orders Meteion to suspend her mission and return.", "Follow, Wander, Stumble, Listen", "Meteion, enough. Suspend your mission and return hither at once."),
 "M778g": ("Emet-Selch will take Meteion to Amaurot, needed to bring back her sisters.", "Follow, Wander, Stumble, Listen", "We are taking Meteion back to Amaurot. As I understand, we will need her if we are to bring back all of her sisters."),
 "M778h": ("Hermes will not let Meteion be taken before her report is finished.", "Follow, Wander, Stumble, Listen", "You cannot take Meteion. Not until she has finished her report."),
 "M778i": ("Emet-Selch asks why Hermes could not leave well enough alone.", "Follow, Wander, Stumble, Listen", "Why, Hermes? Why could you not leave well enough alone!?"),
 # #779 Caging the Messenger
 "M779a": ("Hermes has fled to Ktisis.", "Caging the Messenger", "Hermes has headed to Ktisis."),
 "M779b": ("Emet-Selch holds Meteion a potential threat to bring under the Convocation's control.", "Caging the Messenger", "Meteion is a potential threat that needs to be brought under our control."),
 "M779c": ("A dampening field covers Ktisis, raised for escaped entities.", "Caging the Messenger", "A field of dampening magick is draped over the entire facility, usually in response to escaped entities and the like."),
 "M779d": ("Meteion promises to free mankind from the yoke of existence.", "Caging the Messenger", "Rejoice, for we will free you from the cruel yoke of existence."),
 "M779e": ("Hermes, as chief overseer, will judge man's fitness to exist.", "Caging the Messenger", "In my authority as chief overseer of Elpis, I will make a judgment on man's fitness to exist."),
 "M779f": ("Hermes summons Kairos to wipe everyone's memories of the time since your arrival.", "Caging the Messenger", "the chief summons Kairos to alter the memories of everyone present, such that all that occurred since your arrival in Elpis would be wiped clean."),
 "M779g": ("Hermes bids Meteion flee to the edge of the universe, knowing he will believe her and her sisters lost in an accident.", "Caging the Messenger", "he bids Meteion escape to the edge of the universe, knowing that he will soon believe her and her sisters to have perished in an accident."),
 "M779h": ("Emet-Selch briefly reveals his Ascian sigil.", "Caging the Messenger", "Emet-Selch briefly reveals his Ascian sigil."),
 "M779i": ("Argos bears you and Venat through the portal, beyond the memory wipe.", "Caging the Messenger", "Venat returns from her failed pursuit just in time to have Argos bear you both through the portal and evade the Kairos-induced amnesia."),
 "M779j": ("Hythlodaeus and Emet-Selch do not escape the wipe.", "Caging the Messenger", "Hythlodaeus and Emet-Selch are not so fortunate, and now it falls to you and Venat to remember - and safeguard - your respective realities."),
 "M779k": ("Venat placed an enchantment on Meteion to follow her trail.", "Caging the Messenger", "Ere she made good her escape, I placed an enchantment upon her. One which allows us to follow her trail."),
 "M779l": ("Hermes will one day face the Final Days as Fandaniel.", "Caging the Messenger", "one day hence, he will face the advent of the Final Days in the role of Fandaniel..."),
 "M779m": ("Meteion means to relieve all life of the burden of existence.", "Caging the Messenger", "She declares her intention to relieve all life of the burden of existence"),
 "M779n": ("Venat breaks her shackles and chases Meteion into the sky.", "Caging the Messenger", "It is then that Venat breaks her shackles and chases the entelechy into the sky."),
 "M779o": ("Emet-Selch tears a hole in space for your escape.", "Caging the Messenger", "while Emet-Selch tears a hole in the spatial confluence to afford you and escape route"),
 # #780 Thou Must Live, Die, and Know
 "M780a": ("You must preserve what Hermes sought to erase, and fight in your own age.", "Thou Must Live, Die, and Know", "No, we must instead ensure that the experiences Hermes sought to expunge are preserved. … You must fight this battle in your age, and I in mine..."),
 "M780b": ("With Meteion free, the Final Days are only a matter of time.", "Thou Must Live, Die, and Know", "With Meteion free to pursue her designs, 'tis only a matter of time until the Final Days are upon us."),
 "M780c": ("The report must stay secret, so Venat will work apart from the Convocation.", "Thou Must Live, Die, and Know", "we cannot allow the report that set this calamity in motion to become common knowledge. … Which is why I must work independently of the Convocation."),
 "M780d": ("A wish for a fair determination drove Hermes to erase their memories.", "Thou Must Live, Die, and Know", "it was the desire for a fair determination that drove Hermes to attempt to erase our memories"),
 "M780e": ("Hermes vows to bring honor to the seat of Fandaniel.", "Thou Must Live, Die, and Know", "From this day forth, I shall strive to bring honor to the seat of Fandaniel."),
 "M780f": ("Half of mankind was sacrificed to bring forth Zodiark, and a shroud of aether forestalled the Final Days.", "Thou Must Live, Die, and Know", "That day, mankind saw half of its number sacrificed to bring forth Zodiark. … And covering the star in a shroud of aether, we forestalled the Final Days."),
 "M780g": ("Venat sunders the star, so that man must walk.", "Thou Must Live, Die, and Know", "No more shall man have wings to bear him to paradise. … Henceforth, he shall walk."),
 "M780h": ("Venat's voice, as Hydaelyn, speaks of a conjunction between your time and hers.", "Thou Must Live, Die, and Know", "Venat@Hydaelyn: A conjunction has begun to form; an intertwining of your time and mine."),
 "M780i": ("Krile welcomes you back: there have been developments while you were away.", "Thou Must Live, Die, and Know", "Well, as so often seems to be the case, while you were away, we've had some few developments..."),
 "M780j": ("Mankind must prove itself worthy to exist.", "Thou Must Live, Die, and Know", "We must prove that mankind is worthy to exist."),
}

ENTITIES = {
 # recurring from earlier eras (same id and category merge)
 "char-graha-tia": "character", "char-lyna": "character", "char-ryne": "character", "char-elidibus": "character",
 "char-fandaniel": "character", "char-emet-selch": "character", "char-hythlodaeus": "character",
 "char-venat": "character", "char-hydaelyn": "character", "char-zodiark": "character", "char-krile": "character",
 "org-convocation-of-fourteen": "organization", "loc-crystal-tower": "location", "loc-crystarium": "location",
 # may also come from the 6.0 eras before this one (same id and category merge)
 "char-argos": "character",
 # new here
 "char-hermes": "character", "char-meteion": "character", "char-azem": "character", "char-doros": "character",
 "org-meteia": "organization", "org-bureau-of-the-architect": "organization",
 "loc-elpis": "location", "loc-ktisis-hyperboreia": "location",
 "evt-the-river-of-time": "event", "evt-the-overseers-doubts": "event", "evt-venats-inquiry": "event",
 "evt-meteions-report": "event",
}

A1, A2, A3, A4 = "evt-the-river-of-time", "evt-the-overseers-doubts", "evt-venats-inquiry", "evt-meteions-report"
FAN = ["Fandaniel"]            # Hermes's alias from the #762 reveal (Marques → Cid)
LYNA = ["Captain Lyna"]
MS = ["Meteion's sisters"]     # the Meteia's alias once they are named (#774)

# ---- Presentations ---------------------------------------------------------------------------------------------------
PRES = {
 # -- the Crystarium and the way back
 "char-ryne": [
   P(X761, None, "main", "Ryne",
     "A young girl of the First who carries on Minfilia's legacy, and the Oracle of Light, though she has never once heard Hydaelyn's call. "
     "One night she felt her bond to something immense sever, and saw the sky ablaze. When you told her of the Source, she knew the doom of Amaurot had come again.",
     ["M648a", "M761g", "M761h", "M761i"]),
 ],
 "char-lyna": [
   P(X761, None, "main", "Lyna",
     "A captain of the Crystarium, which keeps the peace you won and is building new lives. Debate rages over how to govern the city in the Exarch's absence, "
     "but whatever its people choose, she says, no one will replace their lord.",
     ["M660i", "M761d", "M761e", "M761f"], LYNA),
 ],
 "loc-crystal-tower": [
   P(X762, None, "main", "The Crystal Tower",
     "A tower woken in the Source of a later age and sent back to the First, whose heart is the Umbilicus. What remained of Elidibus lingered in its core: "
     "with G'raha Tia's spirit vessel you woke him at its console, and the energy his essence had left in the tower carried you into the distant past.",
     ["M639d", "M761a", "M762a", "M762p", "M762i"]),
 ],
 "char-elidibus": [
   P(X762, None, "main", "Elidibus",
     "Emissary of the Convocation of Fourteen and Zodiark's heart, whose imprisoned essence lingered in the Crystal Tower. Woken by its console, he learned that Zodiark has fallen and his brethren's souls have returned to the star. "
     "He told you that Fandaniel was once Hermes, chief of Elpis, and spent the last of his essence sending you back to that age before going to join his brethren.",
     ["M675l", "M672f", "M762a", "M762b", "M762e", "M762g", "M762i"]),
 ],
 "char-fandaniel": [
   P(X762, None, "main", "Fandaniel",
     "An Ascian who wore Asahi's body and led the Telophoroi. Elidibus says that long ago Fandaniel shed light on the Final Days and devised a countermeasure, "
     "and that before he joined the Convocation and took that title he was Hermes, chief of Elpis. This last incarnation, Elidibus says, was consumed by self-loathing and hate.",
     ["M689d", "M689i", "M762d", "M762e", "M762f"]),
 ],
 # -- Elpis
 "loc-elpis": [
   P(X762, None, "main", "Elpis",
     "The testing ground of creation at heavens' edge, in the distant past, where living beings and certain arcane entities are brought for observation and research. "
     "Hermes was its chief before he became Fandaniel.",
     ["M762q", "M762m", "M762e"]),
   P(X765, None, "main", "Elpis",
     "The testing ground of creation at heavens' edge, in the distant past. Every life-form must pass its tests to be judged fit to exist before it is released into the world. "
     "Its chief overseer is Hermes, the man who will become Fandaniel.",
     ["M762q", "M765f", "M764b", "M764g"]),
   P(X768, None, "main", "Elpis",
     "The testing ground of creation at heavens' edge, where every life-form is tested for its fitness to exist. Creations judged detrimental are unmade, "
     "and Kairos, a system that rewrites memories, can give a troubled creation a fresh slate.",
     ["M762q", "M765f", "M768d", "M768b", "M768c"]),
 ],
 "char-hermes": [
   P(X762, None, "main", "Hermes",
     "The name Fandaniel bore long ago, Elidibus says, before he joined the Convocation: Hermes, chief of Elpis, a facility for the evaluation of creations. "
     "Elidibus sent you back to the time when Hermes served as its chief.",
     ["M762e", "M762g"], FAN),
   P(X764, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. After you helped him rescue a wayward creature from a tree, he welcomed you to Elpis. "
     "At his side is Meteion, a winged girl he calls a pet project, and Hythlodaeus is a close collaborator of his.",
     ["M764b", "M764g", "M764f", "M764c", "M764a"], FAN),
   P(X765, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. The present Fandaniel will step down and return to the star, and has named Hermes his preferred successor; "
     "Emet-Selch has come to assess him for the Convocation. He made Meteion, who feels what those around her feel.",
     ["M764b", "M764g", "M765a", "M765b", "M765i", "M765d"], FAN),
   P(X766, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel, weighed by the Convocation as a successor. On his rounds he told you of dynamis, an energy beings of aether cannot readily use, "
     "and that he made Meteion of it, because aether is scarce beyond the star.",
     ["M764b", "M764g", "M765a", "M766c", "M766d", "M766e"], FAN),
   P(X767, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. He offered to transform before others, a vainglorious act, to teach a flightless charybdis to fly, "
     "and insists his creations be given every chance. Emet-Selch would welcome him into the Convocation, which has no master of the celestial.",
     ["M764b", "M764g", "M767c", "M767b", "M767g", "M767a"], FAN),
   P(X768, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. When Doros moved to unmake the lykaones, which slaughtered other creatures, "
     "Hermes, who abhors altering memories but prefers it to execution, asked that every option be exhausted first.",
     ["M764b", "M764g", "M768a", "M768e", "M768f"], FAN),
   P(X769, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. He confided his doubts: man discards the creations he deems useless without a second thought. "
     "He made Meteion and her many sisters of dynamis to cross the emptiness between stars, and the sisters have already departed.",
     ["M764b", "M764g", "M769f", "M769g", "M769d", "M769e"], FAN),
   P(X770, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. He accepted that all seven lykaones be unmade, and ended the last himself. "
     "Emet-Selch urged him to join the Convocation, but he fears that taking the seat of Fandaniel would approve his predecessor's death, doubts he is fit to represent mankind, and asked for time.",
     ["M764b", "M770a", "M770d", "M770g", "M770e", "M770f", "M770h"], FAN),
   P(X773, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel, still weighing the Convocation's offer. A researcher saw him send a host of Meteion into the night sky, "
     "and he says his work needs more tests before he can reveal it. Venat fears he may have a hand in the Final Days.",
     ["M764b", "M764g", "M770h", "M773b", "M773c", "M773d"], FAN),
   P(X775, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. A glimpse of the past showed Meteion telling him her sisters are on course to their stars. "
     "Emet-Selch is certain he has no conscious wish for the world to end, and Hythlodaeus wonders how, as Fandaniel, he could miss the subject of his own research.",
     ["M764b", "M764g", "M775a", "M775b", "M775g", "M775f"], FAN),
   P(X776, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel, still to decide on the Convocation's seat. Found at work with Meteion in the Hungering Gardens, he agreed to hear you out once his work is done.",
     ["M764b", "M764g", "M776e", "M776f", "M776c"], FAN),
   P(X777, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. Hearing your tale, he explained that the first Final Days warped creation magicks and the second warped the people, sundered and thin in aether. "
     "His Meteia share one mind, and only Meteion can reach her sisters.",
     ["M764b", "M764g", "M777b", "M777c", "M777g"], FAN),
   P(X778, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. He had tasked Meteion with asking what others live for. "
     "When Emet-Selch moved to take her to Amaurot, Hermes refused to give her up before her report was finished, and fled with her.",
     ["M764b", "M764g", "M778d", "M778g", "M778h"], FAN),
   P(X779, None, "main", "Hermes",
     "Chief overseer of Elpis, and the man who will become Fandaniel. When Meteion declared she would free all life from existence, he took it as a judgment of man's fitness to exist: "
     "he bound your company, bade her flee to the edge of the universe, and set Kairos to wipe everyone's memories of your visit. Venat says he will take up the seat of Fandaniel.",
     ["M779d", "M779m", "M779e", "M779g", "M779f", "M779l"], FAN),
   P(X780, None, "main", "Hermes",
     "The chief overseer of Elpis who erased the memories of your visit, believing it would keep his judgment of mankind fair, and who will become Fandaniel. "
     "In the rift you saw him swear to bring honor to that seat. Venat cannot say whether, knowing what he did, he would remain a friend.",
     ["M779f", "M780d", "M780e", "M779l"], FAN),
 ],
 "char-meteion": [
   P(X764, None, "main", "Meteion",
     "A winged girl at Hermes's side in Elpis, whom he calls a pet project still in preliminary testing. She speaks straight into your mind, and wants to be your friend.",
     ["M764c", "M764d"]),
   P(X765, None, "main", "Meteion",
     "Hermes's creation, a winged girl in Elpis. She reads the emotions of those around her and projects her own, so she is sad when others are sad: that is how he made her.",
     ["M764c", "M765d", "M765e"]),
   P(X766, None, "main", "Meteion",
     "Hermes's creation, a winged girl who shares the feelings of those around her. She is an entelechy, the first with free will, made of dynamis because aether is scarce beyond the star; "
     "the Bureau of the Architect must judge whether she is a living being.",
     ["M765d", "M766d", "M766e", "M766f"]),
   P(X769, None, "main", "Meteion",
     "Hermes's creation, an entelechy of dynamis who shares the feelings of those around her. She wanted to cheer Hermes with an Elpis flower, since such flowers darken with his pain. "
     "Her many sisters, made like her to cross between the stars, have already departed.",
     ["M765d", "M766d", "M769a", "M769b", "M769d", "M769e"]),
   P(X773, None, "main", "Meteion",
     "Hermes's creation, an entelechy of dynamis who shares the feelings of those around her. A researcher saw Hermes send a host of Meteion into the night sky, "
     "and his colleagues know her only as his personal project.",
     ["M765d", "M766d", "M773b", "M772h"]),
   P(X775, None, "main", "Meteion",
     "Hermes's creation, an entelechy of dynamis. A glimpse of the past showed her reporting to him that all her sisters are on course to their stars.",
     ["M765d", "M766d", "M775a", "M775b"]),
   P(X777, None, "main", "Meteion",
     "Hermes's creation, an entelechy of dynamis, and the one way to reach her sisters, who share a single mind. As you spoke with Hermes she cried out in pain and hatred, and vanished.",
     ["M765d", "M777g", "M777f"]),
   P(X778, None, "main", "Meteion",
     "Hermes's creation, the voice of the Meteia. Cornered, she told of stars whose peoples perished, one annihilated by weapons of mass destruction. "
     "When Emet-Selch moved to take her to Amaurot, Hermes fled with her.",
     ["M765d", "M777g", "M778c", "M778g", "M778h"]),
   P(X779, None, "main", "Meteion",
     "Hermes's creation, the voice of the Meteia. She declared that she will free all life from the cruel yoke of existence, and fled to the edge of the universe at Hermes's bidding. "
     "Venat placed an enchantment on her that lets her trail be followed.",
     ["M765d", "M779d", "M779m", "M779g", "M779k"]),
   P(X780, None, "main", "Meteion",
     "Hermes's creation, who fled to the edge of the universe meaning to free all life from existence. With her free, Venat says, the Final Days are only a matter of time.",
     ["M765d", "M779g", "M779m", "M780b"]),
 ],
 "org-meteia": [
   P(X769, None, "main", "Meteion's sisters",
     "Meteion's many sisters, beings of dynamis that Hermes made to cross the emptiness between the stars. They have already departed on their journey.",
     ["M769d", "M769e"]),
   P(X774, None, "main", "The Meteia",
     "Meteion and her sisters, beings of dynamis that Hermes made to cross between the stars. A researcher saw him send a host of them into the night sky, "
     "and Venat means to visit the isle they left from.",
     ["M769d", "M773b", "M774a"], MS),
   P(X777, None, "main", "The Meteia",
     "Meteion and her sisters, beings of dynamis that Hermes made to cross between the stars. They are linked to a single mind across any distance, so only Meteion can reach them.",
     ["M769d", "M777g"], MS),
   P(X778, None, "main", "The Meteia",
     "Beings of dynamis that Hermes made to cross between the stars, linked to a single mind. Hermes tasked them with asking what others live for, "
     "and Meteion's report tells of stars whose peoples perished, one annihilated by weapons of mass destruction.",
     ["M769d", "M777g", "M778d", "M778c"], MS),
   P(X779, None, "main", "The Meteia",
     "Beings of dynamis that Hermes made to cross between the stars, linked to a single mind. Meteion has fled to the edge of the universe, "
     "and Hermes, his memory altered, will believe her and her sisters lost in an accident.",
     ["M769d", "M777g", "M779g"], MS),
 ],
 "org-bureau-of-the-architect": [
   P(X762, None, "main", "The Bureau of the Architect",
     "A bureau of the ancients in the distant past, led by Hythlodaeus.",
     ["M762j"]),
   P(X766, None, "main", "The Bureau of the Architect",
     "A bureau of the ancients, led by Hythlodaeus, which judges whether a creation such as Meteion is a living being or an arcane entity.",
     ["M762j", "M766f"]),
   P(X770, None, "main", "The Bureau of the Architect",
     "A bureau of the ancients, led by Hythlodaeus, which judges the nature of creations. Hermes means to petition it to preserve the unmade lykaones' concept as a restricted hazardous life-form.",
     ["M762j", "M766f", "M770b"]),
 ],
 "char-azem": [
   P(X762, None, "main", "Azem",
     "Someone Hythlodaeus knows in the distant past, whose soul's color Hythlodaeus finds almost identical to yours.",
     ["M762l"]),
   P(X763, None, "main", "Azem",
     "Someone Hythlodaeus knows in Elpis's age, whose soul's color he finds almost identical to yours. Since your unusual nature shows to anyone who looks, "
     "you pass in Elpis as Azem's familiar.",
     ["M762l", "M763d", "M763e"]),
   P(X771, None, "main", "Azem",
     "Venat's successor in the seat of Azem, a whimsical traveler whom Emet-Selch calls unruly. Hythlodaeus finds your soul's color almost identical to Azem's, "
     "and in Elpis you pass as Azem's familiar.",
     ["M771e", "M771d", "M762l", "M763e"]),
   P(X774, None, "main", "Azem",
     "Venat's successor in the seat of Azem, a whimsical traveler whom Emet-Selch calls unruly. When they first sparred, Venat underestimated Azem, then less than half her age. "
     "In Elpis you pass as Azem's familiar.",
     ["M771e", "M771d", "M774c", "M763e"]),
 ],
 "char-emet-selch": [
   P(X762, None, "main", "Emet-Selch",
     "An Ascian, long dead in your own age. In the distant past you meet him alive in Elpis, Emet-Selch of the Convocation of Fourteen, come with his friend Hythlodaeus to see Hermes. "
     "The two can see souls, and he made you visible.",
     ["M661i", "M762n", "M762o", "M762k"]),
   P(X765, None, "main", "Emet-Selch",
     "An Ascian, long dead in your own age, whom you meet alive in Elpis as a member of the Convocation of Fourteen. He has come to assess Hermes, whom the present Fandaniel named his successor, "
     "and insists you have nothing to do with the Convocation.",
     ["M661i", "M762n", "M765a", "M765g"]),
   P(X767, None, "main", "Emet-Selch",
     "An Ascian, long dead in your own age, whom you meet alive in Elpis as a member of the Convocation, a seat Hythlodaeus recommended him for. He would welcome Hermes among the Fourteen, "
     "and after your pleading he taught a flightless charybdis to fly.",
     ["M661i", "M762n", "M767e", "M767a", "M767f"]),
   P(X772, None, "main", "Emet-Selch",
     "An Ascian, long dead in your own age, whom you meet alive in Elpis as a member of the Convocation. He rejected your tale that he would raise Amaurot from memory and fill it with phantoms, and went back to his duty.",
     ["M661i", "M762n", "M772c", "M772d"]),
   P(X775, None, "main", "Emet-Selch",
     "An Ascian, long dead in your own age, whom you meet alive in Elpis as a member of the Convocation. He reached the same conclusions about Hermes as you did, "
     "yet is certain Hermes has no conscious wish for the world to end.",
     ["M661i", "M762n", "M775i", "M775g"]),
   P(X778, None, "main", "Emet-Selch",
     "An Ascian, long dead in your own age, whom you meet alive in Elpis as a member of the Convocation. He helped you corner Meteion and meant to take her to Amaurot, "
     "but Hermes fled with her.",
     ["M661i", "M762n", "M778g", "M778i"]),
   P(X779, None, "main", "Emet-Selch",
     "An Ascian, long dead in your own age, whom you meet alive in Elpis as a member of the Convocation. Holding Meteion a threat, he pursued Hermes into Ktisis Hyperboreia; "
     "breaking his chains he briefly showed his Ascian sigil, and he tore open a way for your escape. Kairos took his memories of your visit.",
     ["M661i", "M779b", "M779h", "M779o", "M779j"]),
 ],
 "char-hythlodaeus": [
   P(X762, None, "main", "Hythlodaeus",
     "A long-departed ancient whose shade you met in Amaurot. In Elpis, in the distant past, he is alive: chief of the Bureau of the Architect and Emet-Selch's companion, able to see souls. "
     "He finds yours almost identical in color to Azem's, and offered to guide you to Hermes.",
     ["M673l", "M762j", "M762k", "M762l", "M762o"]),
   P(X767, None, "main", "Hythlodaeus",
     "A long-departed ancient, whom you meet alive in Elpis as chief of the Bureau of the Architect. He declined a seat on the Convocation, saying his vision is exceptional but all else pedestrian, "
     "and recommended Emet-Selch in his stead.",
     ["M673l", "M762j", "M767d", "M767e"]),
   P(X776, None, "main", "Hythlodaeus",
     "A long-departed ancient, whom you meet alive in Elpis as chief of the Bureau of the Architect. Having heard your tale, he hopes the Emet-Selch who would raise Amaurot beneath the sea never comes to be.",
     ["M673l", "M762j", "M776d"]),
   P(X779, None, "main", "Hythlodaeus",
     "A long-departed ancient, whom you meet alive in Elpis as chief of the Bureau of the Architect. He helped you chase Hermes into Ktisis Hyperboreia, but Kairos took his memories of your visit.",
     ["M673l", "M762j", "M779a", "M779j"]),
 ],
 "char-doros": [
   P(X768, None, "main", "Doros",
     "An observer in Elpis who reverts and unmakes failed creations. Since even Kairos could not change the lykaones' behavior, he means to unmake them all.",
     ["M768a", "M768c", "M768d"]),
   P(X770, None, "main", "Doros",
     "An observer in Elpis who unmakes failed creations. Three lykaones escaped him, and Hermes, his chief, finds no fault in his judgment.",
     ["M768d", "M770k", "M770c"]),
 ],
 "org-convocation-of-fourteen": [
   P(X765, None, "main", "The Convocation of Fourteen",
     "The council of the ancients, whose seats are held by elected sages. Its members retire by returning to the star: their office becomes their lives. "
     "In Elpis's age, the present Fandaniel means to step down, and has named Hermes his successor.",
     ["M645f", "M765c", "M765a"]),
   P(X767, None, "main", "The Convocation of Fourteen",
     "The council of the ancients, whose members retire by returning to the star. Hythlodaeus declined a seat and recommended Emet-Selch; "
     "Emet-Selch would welcome Hermes, since none of the Fourteen specializes in the celestial.",
     ["M645f", "M765c", "M767d", "M767e", "M767a"]),
   P(X780, None, "main", "The Convocation of Fourteen",
     "The council of the ancients. Hermes vowed to bring honor to its seat of Fandaniel, and Venat, fearing the Meteia's report would spread, will work apart from the Convocation against the Final Days.",
     ["M645f", "M780e", "M780c"]),
 ],
 "char-venat": [
   P(X771, None, "main", "Venat",
     "An ancient whom records name as the leader of Hydaelyn's summoning. In Elpis, in the distant past, you met her as the previous Azem, the image of the figure who appeared to you on the voyage to Old Sharlayan. "
     "Unlike most of the Convocation, she did not return to the star when she stepped down. She recognized her own ward on you, and deduced that you come from the future.",
     ["M666c", "M771a", "M771c", "M771i", "M771b", "M771g"]),
   P(X772, None, "main", "Venat",
     "The previous Azem, met in Elpis in the distant past. Hearing of the Final Days, which would destroy all she holds dear, she wonders whether she is Hydaelyn, "
     "and why she would ever oppose the Fourteen. She concludes that only Hermes knows dynamis well.",
     ["M771a", "M772b", "M772e", "M772f", "M772g"]),
   P(X774, None, "main", "Venat",
     "The previous Azem, met in Elpis in the distant past, who is investigating Hermes with you and fears he may have a hand in the Final Days. "
     "To win over her familiar Argos she sparred with you, and judged you to have weathered more hardship than your tales suggest.",
     ["M771a", "M773d", "M774b", "M774d", "M774e"]),
   P(X775, None, "main", "Venat",
     "The previous Azem, met in Elpis in the distant past. Having reached the same conclusions about Hermes as Hythlodaeus and Emet-Selch, she proposes telling him your tale in hope of his help.",
     ["M771a", "M775i", "M775h"]),
   P(X779, None, "main", "Venat",
     "The previous Azem, met in Elpis in the distant past. When Hermes bound your company she broke free and chased Meteion into the sky, placing an enchantment on her that lets her trail be followed. "
     "Argos carried the two of you beyond Kairos, so you alone remember.",
     ["M771a", "M779n", "M779k", "M779i", "M779j"]),
   P(X780, None, "main", "Venat",
     "The previous Azem, whom you met in Elpis in the distant past. She sent you home to fight in your own age while she keeps the Meteia's report secret and works apart from the Convocation, "
     "to prove mankind worthy to exist. In a memory you saw her sunder the star so that man must walk.",
     ["M771a", "M780a", "M780c", "M780j", "M780g"]),
 ],
 "char-argos": [
   P(X774, None, "main", "Argos",
     "Venat's familiar in Elpis, who has traveled every corner of the star with her and is obstinate with strangers. After you sparred with Venat, he warmed to you.",
     ["M774b", "M774e"]),
   P(X779, None, "main", "Argos",
     "Venat's familiar in Elpis, who warmed to you after you sparred with her. He carried you and Venat through the portal, beyond the reach of Kairos.",
     ["M774b", "M774e", "M779i"]),
 ],
 "loc-ktisis-hyperboreia": [
   P(X775, None, "main", "Ktisis Hyperboreia",
     "The largest facility in Elpis, on its northern isle, where the chief overseer and most of its observers do their work.",
     ["M775c", "M775d"]),
   P(X779, None, "main", "Ktisis Hyperboreia",
     "The largest facility in Elpis, where Hermes took refuge with Meteion under a dampening field. At its summit he set Kairos to erase your company's memories.",
     ["M775c", "M779a", "M779c", "M779f"]),
 ],
 "char-hydaelyn": [
   P(X780, None, "main", "Hydaelyn",
     "A power created by dissenters among the ancients, an incarnation of their opposing belief. In Elpis, Venat wondered whether she herself is Hydaelyn; "
     "back in the Ocular, Venat's voice, speaking as Hydaelyn, says a conjunction has begun to form between your time and hers.",
     ["M646h", "M772e", "M780h"]),
 ],
}

# ---- Arc recaps (one per step: the story so far, standing on its own) ------------------------------------------------
N1, N2, N3, N4 = "The River of Time", "The Overseer's Doubts", "Venat's Inquiry", "Meteion's Report"
PRES.update({
 A1: [
   P(X761, None, "main", N1,
     "Seeking answers to the doom spreading on the Source, you returned to the Crystarium with G'raha Tia's empty spirit vessel, which can work the tower's systems, to find whatever remains of Elidibus. "
     "Lyna says the peace holds while the city debates its governance. Ryne, who felt her bond to Hydaelyn sever and saw a burning sky, knows the doom of Amaurot has come again.",
     ["M761a", "M761b", "M761d", "M761e", "M761h", "M761i"]),
   P(X762, None, "main", N1,
     "In the Umbilicus, G'raha's spirit vessel woke what remains of Elidibus. Learning that Zodiark has fallen, he told you that Fandaniel once shed light on the Final Days, and before that was Hermes, chief of Elpis. "
     "Elidibus spent the last of his essence sending you to that age. There Hythlodaeus and Emet-Selch, who can see souls, made you visible, and they too seek Hermes.",
     ["M762a", "M762b", "M762d", "M762e", "M762i", "M762k", "M762o"]),
   P(X763, None, "main", N1,
     "Elidibus sent you into the distant past, to Elpis, where Hermes, the man Fandaniel once was, serves as chief. Hythlodaeus and Emet-Selch, there on an errand of their own, made you visible. "
     "Hythlodaeus wove you a robe from two captured petaloudai, and since your unusual nature shows to anyone who looks, you will pass as the familiar of Azem, whose soul resembles yours.",
     ["M762i", "M762e", "M762k", "M763c", "M763d", "M763e", "M762l"]),
   P(X764, None, "main", N1,
     "Sent back to Elpis to learn about Hermes, the man Fandaniel once was, you travel as Azem's familiar with Hythlodaeus and Emet-Selch. "
     "In the gardens of Anagnorisis you found Hermes, its chief overseer, beside a winged girl he calls Meteion, a pet project. After you rescued a wayward creature from a tree, he welcomed you to Elpis.",
     ["M762e", "M763e", "M764b", "M764c", "M764f"]),
   P(X765, None, "main", N1,
     "In Elpis you have met Hermes, the man who will become Fandaniel, and Meteion, his creation, who shares the feelings of those around her. "
     "Emet-Selch has come to assess Hermes for the Convocation: the present Fandaniel will step down and return to the star, and named Hermes his successor. "
     "Hermes invited you to see the creations tested here for fitness to exist.",
     ["M764g", "M765d", "M765a", "M765b", "M765h", "M765f"]),
 ],
 A2: [
   P(X766, None, "main", N2,
     "Hermes, chief overseer of Elpis, took you on his rounds of the creations under test. He told you of dynamis, an energy far weaker than aether that beings like him cannot readily use, "
     "and said he made Meteion of it, the first entelechy with free will, to travel where aether is scarce. Whether she is a living being is for the Bureau of the Architect to decide.",
     ["M766a", "M766c", "M766d", "M766e", "M766f"]),
   P(X767, None, "main", N2,
     "On Hermes's rounds, a charybdis that could not fly faced reversion. Hermes offered to transform and fly beside it, though doing so before others is thought vainglorious, until Hythlodaeus had you badger Emet-Selch into teaching it instead. "
     "Emet-Selch would welcome Hermes into the Convocation, which has no master of the celestial, and Hythlodaeus revealed that he declined a seat himself.",
     ["M767c", "M767b", "M767f", "M767a", "M767d"]),
   P(X768, None, "main", N2,
     "Hermes has been showing you the creations of Elpis while Emet-Selch weighs him for the Convocation. Now a lykaon has slaughtered other creatures, and Doros means to unmake the whole kind, "
     "since even Kairos, a system that rewrites memories, could not change their behavior. Hermes, who abhors altering memories but prefers it to execution, asked that every option be exhausted first.",
     ["M767a", "M768a", "M768b", "M768c", "M768d", "M768e", "M768f"]),
   P(X769, None, "main", N2,
     "The lykaones of Elpis face unmaking, and the matter weighs on Hermes. Meteion asked your help finding an Elpis flower to cheer him, since such flowers, entelechies like her, darken with his pain. "
     "Hermes confided his doubts about how lightly man discards his creations, and told you that Meteion's many sisters, made to cross the void between stars, have already departed.",
     ["M769a", "M769b", "M769f", "M769g", "M769d", "M769e"]),
   P(X770, None, "main", N2,
     "It was decided that all seven lykaones must be unmade, and Hermes ended the last himself, bidding it not be forgotten. Emet-Selch urged him to join the Convocation, "
     "but Hermes fears that taking the seat of Fandaniel would approve his predecessor's death, doubts he is fit to represent mankind, and asks whether it is right to sacrifice lives for the star. He begged time to think.",
     ["M770a", "M770d", "M770j", "M770g", "M770e", "M770f", "M770i", "M770h"]),
 ],
 A3: [
   P(X771, None, "main", N3,
     "While Hermes weighs the Convocation's offer, Hythlodaeus took you to another isle of Elpis, where Venat, the previous Azem, knocked out a charging shark. "
     "She is the image of the figure who appeared to you on the voyage to Old Sharlayan, and she recognized her own ward on you and deduced that you come from the future. "
     "After you found a lost crystal for her, she asked to hear your tale.",
     ["M770h", "M771a", "M771c", "M771b", "M771j"]),
   P(X772, None, "main", N3,
     "Venat, the previous Azem, heard your account of the Final Days, which would destroy all she holds dear. Emet-Selch dismissed your tale of the phantom Amaurot he would raise, and left. "
     "Venat wonders whether she is Hydaelyn and why she would ever oppose the Fourteen, and after questioning Hermes's colleagues she judges that only Hermes himself knows dynamis well.",
     ["M772a", "M772b", "M772c", "M772d", "M772e", "M772f", "M772g"]),
   P(X773, None, "main", N3,
     "With Venat, the previous Azem, you are looking into Hermes and Meteion. At the archives you learned that a researcher saw Hermes send a host of Meteion into the night sky, "
     "and that he says he needs more tests before revealing his work. Venat fears that someone will misuse his discoveries, or that Hermes himself will have a hand in the Final Days.",
     ["M771a", "M773a", "M773b", "M773c", "M773d"]),
   P(X774, None, "main", N3,
     "Hermes was seen sending a host of Meteion into the sky, and Venat means to visit the isle they left from. Her familiar Argos would not carry a stranger, so she sparred with you to prove your worth, "
     "and judged you tougher than your tales suggest. Argos has warmed to you, and Venat hopes to find no wish for oblivion behind Hermes's work.",
     ["M773b", "M774a", "M774b", "M774d", "M774e", "M774f"]),
   P(X775, None, "main", N3,
     "On the isle the Meteia left from, a glimpse of the past showed Meteion telling Hermes that her sisters are on course to their stars. At Ktisis Hyperboreia, the largest facility in Elpis, "
     "you met Hythlodaeus and Emet-Selch, who had reached the same conclusions about Hermes. Emet-Selch is sure he has no conscious wish for the world to end, and you agreed to tell Hermes your tale.",
     ["M775a", "M775b", "M775c", "M775i", "M775g", "M775h"]),
 ],
 A4: [
   P(X776, None, "main", N4,
     "You, Venat, Hythlodaeus and Emet-Selch suspect that Hermes's research is bound up with the Final Days, and mean to ask his help. Hythlodaeus found him with Meteion in the Hungering Gardens, "
     "and Emet-Selch sent you in alone, since Hermes would think he had come to press the Fandaniel matter. Hermes agreed to meet once his work is done.",
     ["M775i", "M775h", "M776a", "M776f", "M776b", "M776c"]),
   P(X777, None, "main", N4,
     "Hermes heard your tale and told you how the Final Days differ: the first warped creation magicks, the second the people themselves, sundered and thin in aether. "
     "Venat believes someone or something is instigating the star's demise. Then Meteion cried out in pain and hatred and vanished, and since the Meteia share one mind, she is the only way to reach her sisters.",
     ["M777b", "M777c", "M777e", "M777f", "M777g"]),
   P(X778, None, "main", N4,
     "Meteion fled after crying out in pain and hatred. With Emet-Selch you cornered her, and she told of other stars whose peoples perished, one annihilated by weapons of mass destruction. "
     "Hermes had tasked her with asking what others live for. When Emet-Selch moved to take her to Amaurot, Hermes refused to give her up and flew off with her.",
     ["M777f", "M778c", "M778d", "M778g", "M778h"]),
   P(X779, None, "main", N4,
     "You chased Hermes into Ktisis Hyperboreia. Meteion declared she will free all life from existence, and Hermes, taking it as a test of man's fitness to exist, bound your company, "
     "bade her flee to the edge of the universe, and set Kairos to erase everyone's memories of your visit. Argos carried you and Venat out in time, but Hythlodaeus and Emet-Selch will forget.",
     ["M779a", "M779d", "M779e", "M779g", "M779f", "M779i", "M779j"]),
   P(X780, None, "main", N4,
     "Hermes erased the memories of your days in Elpis, and Meteion is free, so the Final Days are only a matter of time. Venat will keep their cause secret and work apart from the Convocation, "
     "and sent you home to fight in your own age. Passing through the rift, you saw Hermes swear to honor the seat of Fandaniel, and Venat sunder the star so that man must walk.",
     ["M779f", "M780b", "M780c", "M780a", "M780e", "M780g"]),
 ],
})

# ---- Relationships --------------------------------------------------------------------------------------------------
TYPES = [
 ("made-by", "made by", "maker of", False),                # as content_5_0_part3 defines it
 ("successor-of", "successor of", "predecessor of", False),  # new: Azem, Venat's successor in the seat
]

RELS = [
 # #762 the reveal and the ancients
 ("rel-fandaniel-revealed-as-hermes", "char-fandaniel", "revealed-as", "char-hermes", X762, None, "main", ["M762e"]),
 ("rel-fandaniel-member-of-convocation-of-fourteen", "char-fandaniel", "member-of", "org-convocation-of-fourteen", X762, None, "main", ["M762e"]),
 ("rel-hermes-leads-elpis", "char-hermes", "leads", "loc-elpis", X762, None, "main", ["M762e", "M762g"]),
 ("rel-hythlodaeus-leads-bureau-of-the-architect", "char-hythlodaeus", "leads", "org-bureau-of-the-architect", X762, None, "main", ["M762j"]),
 ("rel-emet-selch-member-of-convocation-of-fourteen", "char-emet-selch", "member-of", "org-convocation-of-fourteen", X762, None, "main", ["M762n"]),
 # Elpis
 ("rel-hermes-allied-with-hythlodaeus", "char-hermes", "allied-with", "char-hythlodaeus", X764, None, "main", ["M764a"]),
 ("rel-meteion-made-by-hermes", "char-meteion", "made-by", "char-hermes", X765, None, "main", ["M765d", "M764c"]),
 ("rel-meteia-made-by-hermes", "org-meteia", "made-by", "char-hermes", X769, None, "main", ["M769d", "M769e"]),
 ("rel-meteion-member-of-meteia", "char-meteion", "member-of", "org-meteia", X769, None, "main", ["M769e"]),
 ("rel-doros-serves-hermes", "char-doros", "serves", "char-hermes", X770, None, "main", ["M770c"]),
 # Venat
 ("rel-azem-successor-of-venat", "char-azem", "successor-of", "char-venat", X771, None, "main", ["M771e", "M771d"]),
 ("rel-azem-member-of-convocation-of-fourteen", "char-azem", "member-of", "org-convocation-of-fourteen", X771, None, "main", ["M771f", "M771i", "M673g"]),
 ("rel-argos-serves-venat", "char-argos", "serves", "char-venat", X774, None, "main", ["M774b", "M774e"]),
 ("rel-venat-allied-with-hythlodaeus", "char-venat", "allied-with", "char-hythlodaeus", X775, X779, "main", ["M775i", "M775h"], ["M779f", "M779j"]),
 ("rel-venat-allied-with-emet-selch", "char-venat", "allied-with", "char-emet-selch", X775, X779, "main", ["M775i", "M775h"], ["M779f", "M779j"]),
 # Meteion's flight
 ("rel-hermes-aids-meteion", "char-hermes", "aids", "char-meteion", X778, None, "main", ["M778h", "M778i"]),
 ("rel-emet-selch-opposes-hermes", "char-emet-selch", "opposes", "char-hermes", X778, X780, "main", ["M778g", "M778i"], ["M779f", "M779j"]),
 ("rel-hermes-opposes-venat", "char-hermes", "opposes", "char-venat", X779, None, "main", ["M779e", "M779f"]),
 ("rel-venat-opposes-meteion", "char-venat", "opposes", "char-meteion", X779, None, "main", ["M779n", "M779k"]),
 ("rel-emet-selch-opposes-meteion", "char-emet-selch", "opposes", "char-meteion", X779, X780, "main", ["M779b"]),  # lead: one-step edge, its end is told in the recap (end evidence must come after the start)
 ("rel-hermes-member-of-convocation-of-fourteen", "char-hermes", "member-of", "org-convocation-of-fourteen", X780, None, "main", ["M780e", "M779l"]),
]

ADJUST = {}

# ---- Arcs ------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-x1-the-river-of-time", A1, X761, X765),
 ("arc-x2-the-overseers-doubts", A2, X766, X770),
 ("arc-x3-venats-inquiry", A3, X771, X775),
 ("arc-x4-meteions-report", A4, X776, X780),
]

CASTS = {
 A1: [
   ("char-graha-tia", X761, ["M761a"]), ("char-ryne", X761, ["M761h"]), ("char-elidibus", X762, ["M762a"]),
   ("char-fandaniel", X762, ["M762e"]), ("char-hermes", X762, ["M762e"]), ("loc-elpis", X762, ["M762g"]),
   ("char-hythlodaeus", X762, ["M762k"]), ("char-emet-selch", X762, ["M762k"]), ("char-azem", X763, ["M763e"]),
   ("char-meteion", X764, ["M764c"]),
 ],
 A2: [
   ("char-hermes", X766, ["M766a"]), ("char-meteion", X766, ["M766d"]), ("org-bureau-of-the-architect", X766, ["M766f"]),
   ("loc-elpis", X766, ["M766a"]), ("char-emet-selch", X767, ["M767a"]), ("char-hythlodaeus", X767, ["M767d"]),
   ("org-convocation-of-fourteen", X767, ["M767a"]), ("char-doros", X768, ["M768a"]), ("org-meteia", X769, ["M769e"]),
 ],
 A3: [
   ("char-venat", X771, ["M771a"]), ("char-hythlodaeus", X771, ["M771i"]), ("char-emet-selch", X771, ["M771h"]),
   ("char-azem", X771, ["M771e"]), ("char-hydaelyn", X772, ["M772e"]), ("char-hermes", X772, ["M772g"]),
   ("char-meteion", X773, ["M773b"]), ("org-meteia", X774, ["M774a"]), ("char-argos", X774, ["M774b"]),
   ("loc-ktisis-hyperboreia", X775, ["M775c"]),
 ],
 A4: [
   ("char-hermes", X776, ["M776a"]), ("char-meteion", X776, ["M776a"]), ("char-hythlodaeus", X776, ["M776a"]),
   ("char-emet-selch", X776, ["M776b"]), ("char-venat", X776, ["M775h"]), ("org-meteia", X777, ["M777g"]),
   ("loc-ktisis-hyperboreia", X779, ["M779a"]), ("char-argos", X779, ["M779i"]), ("char-fandaniel", X779, ["M779l"]),
   ("char-hydaelyn", X780, ["M780h"]),
 ],
}

ARC_NOTES = {
 "arc-x1-the-river-of-time": "MSQ #761 *Return to the Crystarium* to #765 *Ponder, Warrant, Cherish, Welcome*: G'raha's spirit vessel and Ryne's severed bond (M761a, M761h), "
   "Elidibus's reveal and last act (M762e, M762i), the disguise as Azem's familiar (M763e) and the meeting with Hermes and Meteion (M764b, M764c), ending when Hermes's succession "
   "to the seat of Fandaniel is put to him and he invites you on his rounds (M765a, M765h). It starts where the 6.0 part 2 era hands over (the feast, #760). Lyna stays in the entity records: the cast is full.",
 "arc-x2-the-overseers-doubts": "MSQ #766 *Lives Apart* to #770 *Verdict and Execution*: Hermes's rounds through Elpis, dynamis and Meteion's nature (M766c, M766d), the charybdis (M767c), "
   "the lykaon case from report to unmaking (M768a, M770a) and Hermes's doubts, ending when he asks the Convocation for time (M770h). Its name avoids #766's common-word title.",
 "arc-x3-venats-inquiry": "MSQ #771 *Travelers at the Crossroads* to #775 *A Flower upon Your Return*: Venat's arrival and the investigation she leads (M771a, M772g, M773d), Argos (M774e), "
   "ending when the four of you agree to bring Hermes in (M775h). It starts at Venat, since from #771 the story turns from observing Hermes to suspecting him.",
 "arc-x4-meteions-report": "MSQ #776 *Hunger in the Garden* to #780 *Thou Must Live, Die, and Know*: Hermes heard out (M776c, M777b), Meteion's flight and report (M777f, M778c), "
   "the Kairos wipe at Ktisis Hyperboreia (M779f) and Venat sending you home (M780a). It ends where your time in Elpis does; the Baldesion Annex report (#780's last step) leads into the next era.",
}

DECISIONS = [
 "**Four arcs (x1–x4)**, five steps each, cover #761–#780 without sharing steps: the journey and first meeting, Hermes's doubts, Venat's investigation, and Meteion's report and the memory wipe.",
 "**Fandaniel → Hermes** follows Marques → Cid: `char-fandaniel` keeps its record (one new presentation at #762, where Elidibus and the Journal state the identity), "
   "`rel-fandaniel-revealed-as-hermes` runs from #762, and `char-hermes` carries \"Fandaniel\" as an alias throughout. The incumbent who holds the seat of Fandaniel in Elpis is a different person and stays text-only (\"the present Fandaniel\", \"his predecessor\").",
 "**The ancients appear as their past selves** under the accepted IDs: Emet-Selch, Hythlodaeus and Venat each open with who they are in your own age (dead, a shade, the leader of Hydaelyn's summoning), then what they are in Elpis.",
 "**Azem** (`char-azem`) is the seat's current holder, Venat's successor, visible from #762, where Hythlodaeus first likens your soul to Azem's; `successor-of` is a new type for it. Venat is \"the previous Azem\" in text only.",
 "**Meteion's sisters** are `org-meteia`, shown as \"Meteion's sisters\" from #769 (where Hermes says they exist) and \"The Meteia\" from #774 (where the name first appears), with the old name as an alias.",
 "**Argos** is declared here as `char-argos` (Venat's familiar, from #774); if the 6.0 part 2 era already made him an entry at the moon, the two merge. Nothing here states that the two are the same creature: only optional text does.",
 "**Emet-Selch's Ascian sigil** (#779) is told in his text, not as a new `member-of` edge to the Ascians: that edge ended with his death in 5.0 and the Atlas stays in your present.",
 "**Memory wipe:** Venat's alliances with Hythlodaeus and Emet-Selch, and Emet-Selch's opposition to Hermes and Meteion, end at #779/#780 with the Kairos claims (M779f, M779j).",
 "**Left out as entities** (text only, or not at all): Moren, Riqi-Tio, Eirwel, Arkil, Feo Ul (#761), the Propylaion guide, Memnon, Euanthe, Eukleides, the observers, Galene, Ismene, Timaios, "
   "Kairos (a system), Propylaion, Anagnorisis, Poieten Oikos and the Hungering Gardens; Krile appears only in the #780 claim and the next era.",
]

ALLOW = {}
