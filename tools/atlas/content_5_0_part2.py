"""Atlas content for Shadowbringers 5.0, part 2: MSQ #580 The Elder's Answer to #620 Crossing Paths. Arc tag m.
Data only (docs/atlas/era-modules.md is the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes B06–B10, with B05 for context); every locator is an
exact substring of a quest's Journal, Steps or main dialogue (stage directions inside cutscenes included). Spoiler rules
this module follows:
  - the Shadowbringers cast reuses the contract's conventional IDs (char-crystal-exarch, char-emet-selch, char-ryne,
    char-ardbert, char-lyna, loc-crystarium, org-lightwardens, char-ranjit, char-vauthry, loc-eulmore, char-feo-ul,
    char-titania), listed in ENTITIES so this era lints alone; each first presentation here stands on its own as of its
    step and cites only this era's claims or accepted ones;
  - the girl who goes by Minfilia is `char-ryne`, shown as "Minfilia of the First" (part1's name) until #620, where
    Thancred names her Ryne; the Source's Minfilia (`char-minfilia`) is the Oracle of Light, named so in her text only
    (an alias would collide with the title of #568, The Oracle of Light);
  - Solus → Emet-Selch is a reveal (#584): he introduces himself as Solus, founding father of the Empire, then as the Ascian
    Emet-Selch; `char-solus` is `revealed-as` `char-emet-selch` from #584, which carries "Solus" as an alias;
  - first names and titles only ("zos Galvus" and "Warde" stay in locators); "the First" appears only in Ryne's
    name (the world is "Norvrandt" or "this world"); Y'shtola's "Master Matoya" stays in text, not an alias, since
    the Source's Matoya is already "Master Matoya" in accepted text.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

(S580, S581, S582, S583, S584, S585, S586, S587, S588, S589, S590, S591, S592, S593, S594, S595, S596, S597, S598, S599,
 S600, S601, S602, S603, S604, S605, S606, S607, S608, S609, S610, S611, S612, S613, S614, S615, S616, S617, S618, S619,
 S620) = (f"cp-msq-{n}" for n in range(580, 621))

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #580 The Elder's Answer
 "M580a": ("The Nu Mou, unable to deal with their fallen monarch, entrust you with the stone scepter.", "The Elder's Answer", "Acknowledging that they do not have the power to deal with their fallen monarch, the Nu Mou have decided to entrust the relic to you."),
 "M580b": ("Titania is a title, not a name, given to the one chosen to lead the pixies.", "The Elder's Answer", "Know that Titania is not a name, but a title bestowed upon one chosen to lead the pixies by the grace of nature."),
 "M580c": ("The fallen Titania has become a sin eater, with powers unchanged.", "The Elder's Answer", "Though they are become a sin eater, their powers remain unchanged."),
 "M580d": ("Seto, the largest of the amaro, leads them and bears the last relic.", "The Elder's Answer", "When you arrive in Wolekdorf, seek out the largest of the amaro. His name is Seto, and he is their leader and the bearer of the relic."),
 "M580e": ("Seto thinks facing the faerie king is folly and refuses you the crystal shoes.", "The Elder's Answer", "Though Seto receives you warmly, he believes that facing the faerie king is folly, and refuses to give you the crystal shoes."),
 "M580f": ("The amaro Rispa's master, a knight, died fighting the sin eaters.", "The Elder's Answer", "But like so many others, he died fighting the sin eaters."),
 "M580g": ("Urianger concludes that Seto refused out of concern for you.", "The Elder's Answer", "concludes that it is out of genuine concern for your welfare that Seto sought to prevent your confrontation with the faerie king"),
 "M580h": ("A mage of Ronka gave the amaro intelligence.", "The Elder's Answer", "But then a mage of Ronka gave us the gift of intelligence, that we might better serve our masters."),
 # #581 A Resounding Roar
 "M581a": ("Seto can no longer bear to see men fight and die.", "A Resounding Roar", "I simply cannot bear to see men fight and die. Not anymore. None of us can."),
 "M581b": ("Seto says the land is no longer man's to fight for.", "A Resounding Roar", "This land is no longer man's to fight for, nor will your doing so compel the fae folk to change."),
 "M581c": ("Seto will consider giving you the relic if you prove yourself against sin eaters.", "A Resounding Roar", "Sin eaters have been prowling the area of late. Prove yourself against them, and I will consider giving you the relic."),
 "M581d": ("Seto lures sin eaters with his voice, as he once did hunting with an old friend.", "A Resounding Roar", "I will use my voice to lure out the sin eaters, as I once did when I hunted with an old friend."),
 "M581e": ("Seto still needs time to think, and asks a favor of you.", "A Resounding Roar", "However, I still require time to think. And if you should be willing, there is a favor I would ask of you."),
 # #582 Memento of a Friend
 "M582a": ("Seto asks you to search for his lost medallion.", "Memento of a Friend", "While I ponder your request for the shoes, will you not go and search for my medallion?"),
 "M582b": ("The medallion was a gift from Ardbert, Seto's friend.", "Memento of a Friend", "His name was Ardbert, and he was my friend."),
 "M582c": ("Everyone blamed Ardbert and his comrades for the Flood.", "Memento of a Friend", "Everyone blamed him for the Flood. Him and his comrades."),
 "M582d": ("Seto says your soul strongly resembles Ardbert's.", "Memento of a Friend", "It is reminiscent of Ardbert's. Strikingly so."),
 "M582e": ("Seto places his faith in you and gives you the relic.", "Memento of a Friend", "Which is why I will place my faith in you. The relic─it is yours."),
 "M582f": ("The pixies report an old mortal who has spoiled their tricks.", "Memento of a Friend", "But then a scary, bony, ''wrinkly'' old mortal came along and spoiled everything!"),
 "M582g": ("Urianger and the others go to obstruct the trespassers while you face the Lightwarden.", "Memento of a Friend", "Whilst thou salliest forth to meet with the Lightwarden, we shall join in the effort to obstruct the trespassers."),
 "M582h": ("Thancred names the old mortal as Ran'jit, who could undo their efforts.", "Memento of a Friend", "Ran'jit. If he manages to find his way in, all our efforts will have been for naught."),
 # #583 Acht-la Ormh Inn
 "M583a": ("The bearer of all four relics breaks the seal on the castle.", "Acht-la Ormh Inn", "At the arrival of the bearer of all four relics, the seal protecting the castle is broken."),
 "M583b": ("Feo Ul calls Titania a being bereft of reason and mercy.", "Acht-la Ormh Inn", "All that remains is to enter the castle and confront Titania─a being bereft of reason and mercy."),
 "M583c": ("You defeat the Lightwarden and restore night to Il Mheg.", "Acht-la Ormh Inn", "At the end of a frenzied struggle, you emerge victorious over the Lightwarden, thereby restoring night to Il Mheg."),
 "M583d": ("By Il Mheg's laws you should take the defeated king's place.", "Acht-la Ormh Inn", "Feo Ul declares that, by the laws of Il Mheg, you should rightly take your defeated foe's place as king."),
 "M583e": ("Feo Ul takes the burden instead, and leads an army that repels the Eulmorans.", "Acht-la Ormh Inn", "your beautiful branch shoulders this burden in your stead. Thus empowered, the pixie leads an army to Lydha Lran and repels the invading Eulmoran forces."),
 "M583f": ("Ran'jit comes in pursuit of villains who fled to Il Mheg.", "Acht-la Ormh Inn", "We come in pursuit of villains who have fled to this land."),
 "M583g": ("Ran'jit trained Minfilia as an Oracle.", "Acht-la Ormh Inn", "No Oracle I trained would make such an unseemly show of herself!"),
 "M583h": ("Minfilia refuses to return to Eulmore.", "Acht-la Ormh Inn", "I won't return to Eulmore! And I won't let you hurt my friends!"),
 "M583i": ("Ran'jit vows that all who stand with the Warrior of Darkness will face justice, as his master demands.", "Acht-la Ormh Inn", "All who stand with the Warrior of Darkness shall face justice! My master demands it."),
 "M583j": ("Ran'jit's adjutant addresses him as general.", "Acht-la Ormh Inn", "General, they come in greater numbers!"),
 "M583k": ("The Eulmoran army is fast approaching Il Mheg.", "Acht-la Ormh Inn", "With the Eulmoran Army fast approaching, there isn't a moment to waste."),
 # #584 The Wheel Turns
 "M584a": ("With the Warden defeated, Thancred considers the work in Il Mheg done.", "The Wheel Turns", "With the Warden defeated, I believe our work here is done."),
 "M584b": ("He introduces himself as Solus, founding father of the Garlean Empire.", "The Wheel Turns", "I am Solus zos Galvus, founding father of the Garlean Empire."),
 "M584c": ("He reveals his true identity: Emet-Selch, an Ascian.", "The Wheel Turns", "As for my true identity... … I am Emet-Selch. Ascian."),
 "M584d": ("Alphinaud says the Ascians have labored since time immemorial to rejoin the thirteen shards.", "The Wheel Turns", "Since time immemorial, you and yours have labored to rejoin the thirteen shards, at the cost of countless lives."),
 "M584e": ("Emet-Selch blames you for putting his plans in tatters.", "The Wheel Turns", "Thanks to your meddling, Light's supremacy is in doubt, and our painstakingly laid plans are in tatters!"),
 "M584f": ("Emet-Selch proposes cooperation and swears not to hinder the hunt for the Lightwardens.", "The Wheel Turns", "Cooperation! … I will not raise a hand to hinder your hunt for the Lightwardens."),
 "M584g": ("Ardbert says an Ascian in white urged his world to bring about the Rejoining.", "The Wheel Turns", "When our world was about to be consumed by Light, the Ascian in white appeared before us. He said that the only way for us to live on was to bring about the Rejoining."),
 "M584h": ("Ardbert says the Flood was of the Ascians' own making.", "The Wheel Turns", "Desperate as we were, we heeded his words, not realizing that the Flood was of the Ascians' own making."),
 "M584i": ("Ardbert's shade appears to you in your room.", "The Wheel Turns", "Ardbert's shade appears."),
 "M584j": ("Urianger tells Emet-Selch that making his case through an illusion reflects poorly on his sincerity.", "The Wheel Turns", "to make thy case via an illusion reflecteth poorly upon thy sincerity."),
 # #585 A Party Soon Divided
 "M585a": ("Emet-Selch again offers partnership, claiming only to observe.", "A Party Soon Divided", "He continues to cling to the claim that he comes only to observe your efforts in defeating the Lightwardens, once more offering his hand in partnership."),
 "M585b": ("Alphinaud says an alliance with the Ascians is out of the question.", "A Party Soon Divided", "It goes without saying that an alliance with the Ascians is out of the question."),
 "M585c": ("The Exarch proposes dividing forces to survey each region.", "A Party Soon Divided", "Which is why I propose we divide our forces and conduct a systematic survey of each region."),
 "M585d": ("The Wardens of Kholusia, Amh Araeng and Rak'tika remain.", "A Party Soon Divided", "That may be, but the Wardens of Kholusia, Amh Araeng, and Rak'tika remain."),
 "M585e": ("You, Thancred, Minfilia and Urianger are to seek out Y'shtola in the Rak'tika Greatwood.", "A Party Soon Divided", "You, along with Thancred, Minfilia, and Urianger, have been tasked with seeking out Y'shtola in the Rak'tika Greatwood."),
 "M585f": ("The Exarch wants a holy text for Y'shtola, who lives with the Night's Blessed.", "A Party Soon Divided", "It is a holy text he believes may be of interest to Y'shtola, who presently resides with worshipers of the Dark─the Night's Blessed."),
 "M585g": ("Lord Vauthry invites the Exarch to Eulmore.", "A Party Soon Divided", "A missive from Lord Vauthry. He invites me to join him in Eulmore to discuss the recent conflict at Lydha Lran."),
 "M585h": ("The Exarch's power will be diminished far from the tower, but he will go.", "A Party Soon Divided", "Though my power will be much diminished so far from the tower, it is a risk I am willing to take."),
 "M585i": ("Alisaie takes Amh Araeng.", "A Party Soon Divided", "I'll take Amh Araeng, in that case. I know the lie of the land well enough."),
 "M585j": ("The Exarch asks Alphinaud to accompany him to Eulmore.", "A Party Soon Divided", "Master Alphinaud─might I impose upon you to accompany me to Eulmore, prior to beginning your reconnaissance?"),
 "M585k": ("Y'shtola is disinclined to speak with the Exarch.", "A Party Soon Divided", "she is...disinclined to speak with me."),
 "M585l": ("The Lightwardens of Lakeland and Il Mheg have been struck down.", "A Party Soon Divided", "In striking down the Lightwardens of Lakeland and Il Mheg, you have accomplished more in your short time here than all of our forces managed in the last century."),
 "M585m": ("Alphinaud will make for Kholusia.", "A Party Soon Divided", "If there are no objections, I will make for Kholusia."),
 # #586 A Little Faith
 "M586a": ("The creatures that rose from the Flood were taken as agents of divine punishment.", "A Little Faith", "For the creatures which then did rise from that fulgent deluge were seen as agents of divine punishment, sent to devour sin and sinner both"),
 "M586b": ("The most devout worshipers of shadow migrated to the Rak'tika Greatwood.", "A Little Faith", "The most devout of these worshipers of shadow did then migrate to the Rak'tika Greatwood."),
 "M586c": ("The church's standards belong to the Night's Blessed, worshipers of the Dark.", "A Little Faith", "To be plain, the standards which do adorn these walls belong not to those who built them, but to worshipers of the Dark─the Night's Blessed."),
 "M586d": ("The Exarch knows Y'shtola studies the Blessed and their past.", "A Little Faith", "The Exarch knoweth full well that Y'shtola, in her seclusion, doth labor to learn all she may of the Blessed and their past."),
 "M586e": ("The tablet is written in the script of Ronka, whose capital stood in Rak'tika.", "A Little Faith", "If I am not mistaken, they are writ in the script of the ancient empire of Ronka, whose capital once stood in the midst of what is now Rak'tika."),
 "M586f": ("You find the tablet.", "A Little Faith", "Naught escapeth thine eye, 'twould seem. This is indeed the tablet we seek."),
 # #587 Into the Dark
 "M587a": ("Y'shtola has taken the name Master Matoya.", "Into the Dark", "So it is that Y'shtola hath taken the name of Master Matoya."),
 "M587b": ("The Night's Blessed take their forebears' names to protect themselves from the Light.", "Into the Dark", "it is their custom to adopt the names of their forebears. They do this, he explains, in the belief that it will protect their true selves from the blighted touch of the Light."),
 "M587c": ("Two years ago sin eaters razed the Blessed's largest settlement and killed many priests.", "Into the Dark", "Two years past, a swarm of sin eaters did lay waste unto their largest settlement, killing a great many of their priests in so doing."),
 "M587d": ("Y'shtola has assumed a commanding role among the Blessed.", "Into the Dark", "Since Y'shtola's arrival, she has assumed a commanding role among their people, and has helped them begin to rebuild."),
 "M587e": ("The Exarch's secrecy and half-truths lost him Y'shtola's trust.", "Into the Dark", "But his penchant for secrecy and the telling of half-truths soon lost him my trust."),
 "M587f": ("The Light suffusing you made you a stranger to Y'shtola's sight.", "Into the Dark", "The abundance of Light that suffuses your being has made you a stranger to her."),
 "M587g": ("Y'shtola finds the tablet's discovery suspiciously convenient.", "Into the Dark", "I find the timing of its discovery suspiciously convenient."),
 "M587h": ("Emet-Selch says he is only an observer.", "Into the Dark", "I am an observer─nothing more."),
 "M587i": ("Minfilia says Thancred understands she is not the one he lost.", "Into the Dark", "He understands that I'm not the same. That I'm not her."),
 "M587j": ("Yx'Maja's guardians meet intruders with lethal force.", "Into the Dark", "Any attempt to enter their territory is met with lethal force."),
 "M587k": ("Y'shtola can narrow the search for the Lightwarden.", "Into the Dark", "I cannot say with certainty where your quarry is hiding, but I am confident I can narrow the search."),
 # #588 A Day in the Neighborhood
 "M588a": ("Runar credits Master Matoya with driving back the sin eaters.", "A Day in the Neighborhood", "It was she who drove them back."),
 "M588b": ("With their priests slain, the Blessed were at the sin eaters' mercy.", "A Day in the Neighborhood", "With our priests slain and our home in ruins, we were at the mercy of the sin eaters."),
 "M588c": ("Runar cleanses you with water stored against the Light's impurity.", "A Day in the Neighborhood", "We use the water stored here to cleanse ourselves of the Light's impurity."),
 "M588d": ("Runar teaches the Ronkan greeting allin tuta.", "A Day in the Neighborhood", "Allin tuta. In the language of Ronka, it is one of several ways one might say"),
 "M588e": ("Minfilia is starting to feel at home among the Blessed.", "A Day in the Neighborhood", "I was nervous at first, but already I'm starting to feel at home."),
 "M588f": ("Y'shtola must begin deciphering the tablet.", "A Day in the Neighborhood", "I really must begin work on deciphering this tablet."),
 # #589 A Helping Hand
 "M589a": ("Runar asks you to water the crops in return for lodging.", "A Helping Hand", "All I ask is that you take a jug and water the crops in the square."),
 "M589b": ("Watering the crops was Toddia's duty, but she is gone.", "A Helping Hand", "Watering the crops was always Toddia's duty, but she...she is no longer with us."),
 "M589c": ("The Night's Blessed began with those left homeless by the Flood.", "A Helping Hand", "The Night's Blessed was initially formed by those who lost their homes in the wake of the Flood."),
 "M589d": ("No one could say where the souls of those reborn as sin eaters went.", "A Helping Hand", "To make matters worse, none could say what became of the souls of those lost to the Flood when their bodies were reborn as sin eaters."),
 "M589e": ("The Blessed believe the souls of the dead find peace in the sunless sea above.", "A Helping Hand", "a belief that the souls of the departed could yet find peace beyond these burning skies, in the sunless sea above."),
 # #590 Lost but Not Forgotten
 "M590a": ("Toddia, a child of the Night's Blessed, was slain by sin eaters.", "Lost but Not Forgotten", "A few days past, Toddia, a child of the Night's Blessed, was slain by the sin eaters."),
 "M590b": ("Every one of the Blessed is given a heartstone at birth.", "Lost but Not Forgotten", "All of the Night's Blessed are given such a stone at birth."),
 "M590c": ("Runar will not risk his people being corrupted by the sin eaters.", "Lost but Not Forgotten", "But if they indeed have the touch, I will not risk them corrupting one of our own."),
 "M590d": ("The Light's corruption does not touch Minfilia as it does others.", "Lost but Not Forgotten", "I have experience fighting sin eaters. And the Light's...corruption does not touch me like it does others."),
 "M590e": ("Runar asks whether she is truly the Minfilia, descended from the Oracle.", "Lost but Not Forgotten", "Are you truly ''the'' Minfilia? Descended from the Oracle?"),
 "M590f": ("Recovered heartstones ensure the souls of the dead peace in the dark.", "Lost but Not Forgotten", "Even should we be felled by the sin eaters, so long as these gems are recovered, our souls are ensured peace in the dark."),
 # #591 Saying Good-bye
 "M591a": ("Runar insists you attend Toddia's service as honored guests.", "Saying Good-bye", "I must insist you and your friends attend Toddia's service as honored guests."),
 "M591b": ("In the dark, Toddia will be remembered as Minnine.", "Saying Good-bye", "In the light, she was known as Toddia. But in the dark, we shall remember her always as Minnine."),
 "M591c": ("The legend of the Warrior of Darkness owes much to the Blessed's traditions.", "Saying Good-bye", "The enduring legend of the Warrior of Darkness owes much to the traditions of these people."),
 "M591d": ("Minfilia says the dark must be brought back.", "Saying Good-bye", "We cannot allow their hopes and dreams to drown in the light. … We have to bring back the dark."),
 "M591e": ("Thancred agrees they will bring back the dark.", "Saying Good-bye", "No, it's all right. We ''will'' bring back the dark."),
 "M591f": ("Y'shtola and Urianger have finished deciphering the tablet.", "Saying Good-bye", "Urianger and I have finished deciphering the tablet, and its contents were most illuminating."),
 "M591g": ("Thanks to the Exarch's gift, the next course is clear.", "Saying Good-bye", "Thanks to the Exarch's ''gift'', our next course of action is now clear."),
 # #592 Stirring up Trouble
 "M592a": ("The tablet dates from the end of the Ronkan Empire.", "Stirring up Trouble", "Much to my surprise, it dates back to the end of the Ronkan Empire, and was likely written under the direction of the reigning ruler."),
 "M592b": ("The tablet tells how to prove oneself an ally of the Ronkan Empire.", "Stirring up Trouble", "For etched into this tablet is a method by which one may prove themself an ally of the Ronkan Empire."),
 "M592c": ("The monolith Y'shtola needs is held by the Children of the Everlasting Dark, a radical faction.", "Stirring up Trouble", "it is in the possession of a rather radical faction of Dark worshipers─the Children of the Everlasting Dark."),
 "M592d": ("The Children kill, claiming to cleanse their victims of sin.", "Stirring up Trouble", "They rejoice in dealing death to others, claiming that in doing so they cleanse their victims of sin and usher them unto the sunless sea."),
 "M592e": ("The Children have been breeding venomous spiders in greater numbers.", "Stirring up Trouble", "But then I took notice of their venomous spiders. They've been breeding them in much greater numbers."),
 "M592f": ("Y'shtola plans to use bees against the spiders.", "Stirring up Trouble", "Bees, for example, are a natural predator of spiders."),
 # #593 A Beeautiful Plan
 "M593a": ("The Children's settlement is Woven Oath.", "A Beeautiful Plan", "The Children's settlement is to the west, a place they call Woven Oath."),
 "M593b": ("The bees send the Children into a panic.", "A Beeautiful Plan", "What is that!? … By the abyss, they're everywhere!"),
 "M593c": ("Murals depict heroes from the age of gods to just before the Flood.", "A Beeautiful Plan", "Depictions of heroes? From the age of gods, the Ronkan Empire, and immediately before the Flood."),
 "M593d": ("Ardbert recalls the researcher who dated the first painting to an age of myth.", "A Beeautiful Plan", "He believed this first painting dated back to a time of myth and legends."),
 "M593e": ("Ardbert wonders who tried to scrape a mural off the wall.", "A Beeautiful Plan", "Or did someone try to scrape it off the wall? Maybe the man himself, once he came to his senses..."),
 "M593f": ("Y'shtola has all she needs to finish deciphering the tablet.", "A Beeautiful Plan", "I believe I now have everything needed to finish deciphering the tablet."),
 # #594 An Unwanted Proposal
 "M594a": ("Y'shtola confronts Urianger about the Eighth Umbral Calamity he claimed to have seen.", "An Unwanted Proposal", "The Eighth Umbral Calamity and all that followed; everything you claimed to have seen─did you?"),
 "M594b": ("Y'shtola has grown exasperated with Urianger's secrets.", "An Unwanted Proposal", "It would seem she has grown exasperated with Urianger's penchant for secrets."),
 "M594c": ("By Lord Vauthry's decree, Rak'tika now falls under Eulmore.", "An Unwanted Proposal", "By Lord Vauthry's decree, Rak'tika now falls under the governance of Eulmore."),
 "M594d": ("Vauthry says the sin eaters exist to unite the world under his dominion.", "An Unwanted Proposal", "That is why the sin eaters exist. To unite the world under ''my'' dominion!"),
 "M594e": ("Vauthry tries to enthrall the Exarch, who vanishes.", "An Unwanted Proposal", "Vauthry attempts to enthrall the Exarch, but he vanishes."),
 "M594f": ("Vauthry gives the Children of the Everlasting Dark authority over the forest.", "An Unwanted Proposal", "Therefore his lordship has claimed dominion over this forest, and bestowed executive authority upon the Children of the Everlasting Dark."),
 "M594g": ("Any Blessed found in Rak'tika on the Eulmorans' return will be treated as traitors.", "An Unwanted Proposal", "Anyone found here upon our return will be considered a traitor to Eulmore, and dealt with as such."),
 "M594h": ("The Blessed must join the Children and swear to Eulmore, or face retribution.", "An Unwanted Proposal", "The Night's Blessed have been given a choice: join the Children of the Everlasting Dark and swear allegiance to Eulmore, or face their retribution."),
 "M594i": ("A Blessed guard has been poisoned.", "An Unwanted Proposal", "The guard hath been afflicted with a most terrible and efficacious poison."),
 "M594j": ("Y'shtola fears the light from the Wardens was not negated at all.", "An Unwanted Proposal", "Though I have no proof, I fear that the light which poured forth from the Wardens was not negated at all."),
 "M594k": ("Eulmoran soldiers arrive at Slitherbough.", "An Unwanted Proposal", "Eulmoran soldiers have arrived, and one of the Blessed's guards has been felled by poison."),
 # #595 Put to the Proof
 "M595a": ("Y'shtola believes the Eulmorans are in the woods to protect the Lightwarden.", "Put to the Proof", "The Eulmorans' presence here plainly stems from a desire to protect the Lightwarden."),
 "M595b": ("The tablet calls for a seal that identified Ronka's allies.", "Put to the Proof", "According to the tablet, we will first need to obtain a seal used to identify the allies of Ronka in times past."),
 "M595c": ("Runar swears to keep the Blessed safe.", "Put to the Proof", "By all that is dark, I swear to keep the Blessed safe."),
 "M595d": ("A hidden door reveals a medallion.", "Put to the Proof", "A door opens to reveal a pedestal upon which rests a medallion."),
 "M595e": ("The medallion bears the empire's owl insignia.", "Put to the Proof", "This medallion... It bears the owl insignia of the empire."),
 "M595f": ("Preparations to enter Yx'Maja can begin.", "Put to the Proof", "We can begin our preparations to enter Yx'Maja in earnest."),
 # #596 Into the Wood
 "M596a": ("The Lightwarden presumably lies beyond, in Yx'Maja.", "Into the Wood", "Beyond lies Yx'Maja, and presumably the Lightwarden."),
 "M596b": ("Arrows rain on you from the trees.", "Into the Wood", "you are suddenly assailed by arrows from the trees."),
 "M596c": ("Almet recognizes the seal and welcomes you as allies of Ronka.", "Into the Wood", "Upon closer examination, their leader, Almet, recognizes the authenticity of your seal and welcomes you as allies of Ronka."),
 "M596d": ("The sentinels have waited three thousand years for Ronka's allies.", "Into the Wood", "For three thousand years we have waited for this moment, and now you are finally here. I bid you welcome, allies of Ronka."),
 "M596e": ("Almet is chieftainess of Fanow.", "Into the Wood", "I am Almet, chieftainess of Fanow."),
 "M596f": ("Almet's people are in troubled times.", "Into the Wood", "These are troubled times for my people."),
 # #597 Top of the Tree
 "M597a": ("The Viis descend from the palace guard of the last emperor.", "Top of the Tree", "We are descendants of the palace guard which served under the last emperor."),
 "M597b": ("The emperor's last decree bade them keep Ronka's secrets and await allies.", "Top of the Tree", "Keep it secret. Keep it safe. And look to the coming of our allies."),
 "M597c": ("Almet does not know where the Lightwarden lairs.", "Top of the Tree", "My apologies, but I do not know where it makes its lair."),
 "M597d": ("Korille's mother saw a sin eater the others seemed to revere.", "Top of the Tree", "It was larger, for one thing, but what struck her was the way its fellows seemed to revere it."),
 "M597e": ("The tunnel to the falls collapsed after a battle with the eaters.", "Top of the Tree", "But the tunnel which leads there collapsed after a rather bloody battle with the eaters"),
 "M597f": ("The way lies through the Qitana Ravel, once the K'mul Astropolis is restored.", "Top of the Tree", "First we must go to the K'mul Astropolis. Once the flow of magic is restored there, the path through the Qitana Ravel can be opened."),
 "M597g": ("The Qitana Ravel is a temple to the northeast.", "Top of the Tree", "The Qitana Ravel, a temple to the northeast."),
 # #598 Look to the Stars
 "M598a": ("The Morning Stars are four monuments to Rak'tika's guardians.", "Look to the Stars", "Ahead lie the Morning Stars, four monuments built in tribute to the guardians of Rak'tika."),
 "M598b": ("The monuments are said to be the keys to the pyramid.", "Look to the Stars", "It is said that the monuments are themselves the keys to opening the pyramid."),
 "M598c": ("The riddle calls for suffusing one statue with aether.", "Look to the Stars", "it is but a matter of suffusing one of the statues with aether."),
 "M598d": ("Eulmoran soldiers have entered Yx'Maja.", "Look to the Stars", "Eulmoran soldiers. They have entered Yx'Maja!"),
 "M598e": ("Thancred and Uimet are fighting them at the border.", "Look to the Stars", "Together with Thancred, Uimet and some few others have engaged them at the border."),
 # #599 Mi Casa, Toupasa
 "M599a": ("Almet says time is against you.", "Mi Casa, Toupasa", "Time is against us, friend."),
 "M599b": ("Magic is blocked before the sealed door.", "Mi Casa, Toupasa", "Magic appears to be flowing through the walls, but it's being obstructed as it approaches the door."),
 "M599c": ("Only one pedestal bears an owl statue.", "Mi Casa, Toupasa", "Is it not strange that only one of these pedestals bears an owl statue?"),
 "M599d": ("With the statuette returned, aether flows to the door.", "Mi Casa, Toupasa", "I can see aether flowing to the door now."),
 "M599e": ("Almet warns the last step is the most perilous.", "Mi Casa, Toupasa", "this last step is without question the most perilous."),
 # #600 Legend of the Not-so-hidden Temple
 "M600a": ("General Ran'jit bars the way in the final chamber.", "Legend of the Not-so-hidden Temple", "you encounter a most unexpected obstacle: General Ran'jit."),
 "M600b": ("The Viis sisters hold him while you restore the aether and open the Qitana Ravel.", "Legend of the Not-so-hidden Temple", "hold him off long enough for you to activate the final switch restoring the flow of aether through the whole of the pyramid, thus opening the path through the Qitana Ravel."),
 "M600c": ("The Eulmorans poisoned Blessed villagers with a toxin brewed by the Children.", "Legend of the Not-so-hidden Temple", "We poisoned a number of villagers in Slitherbough with a toxin brewed for us by the Children."),
 "M600d": ("Ran'jit refuses to bargain for the antidote.", "Legend of the Not-so-hidden Temple", "We do not negotiate with the enemy. The villagers' lives are forfeit."),
 "M600e": ("Y'shtola leaps into the void for the antidote and vanishes.", "Legend of the Not-so-hidden Temple", "Y'shtola leaps into the void, grabs hold of the antidote, and tosses it to you before disappearing into the dark."),
 "M600f": ("Thancred strikes Ran'jit down into the depths.", "Legend of the Not-so-hidden Temple", "sent down into the depths with a swift strike from Thancred's gunblade."),
 "M600g": ("Ran'jit kicks his adjutant into the chasm along with the antidote.", "Legend of the Not-so-hidden Temple", "choosing to rid himself of the adjutant and any hope of saving the Blessed by kicking him into the chasm along with the antidote."),
 "M600h": ("Minfilia arrives asking for Y'shtola.", "Legend of the Not-so-hidden Temple", "Where...where is Y'shtola?"),
 # #601 The Aftermath
 "M601a": ("The Viis have never been able to measure the pit's depth.", "The Aftermath", "we have tried to mark the depth of the pit. And failed."),
 "M601b": ("The Eulmorans and the Children have fled Yx'Maja.", "The Aftermath", "The Eulmoran soldiers and the Children have fled Yx'Maja."),
 "M601c": ("They remain in the swamps near Lakeland.", "The Aftermath", "though they yet remain in the swamps near Lakeland."),
 "M601d": ("The wounded Blessed man held up the Eulmorans' procession.", "The Aftermath", "'Twas he who forestalled the Eulmorans' procession."),
 "M601e": ("Thancred and Minfilia take the antidote to Slitherbough.", "The Aftermath", "If you've a spare vial, Minfilia and I can deliver it to the Blessed at Slitherbough."),
 "M601f": ("Thancred says Y'shtola leapt into the pit for a reason.", "The Aftermath", "I know it seems callous of us to leave, but she leapt into that hole for a reason."),
 "M601g": ("You treat Runar with the antidote.", "The Aftermath", "Use the [[Bottle of Antidote|antidote]] to treat [[Runar]]'s poison."),
 "M601h": ("The antidote takes effect.", "The Aftermath", "The medicine seems to take effect as the color slowly creeps back to his cheeks."),
 # #602 In Good Faith
 "M602a": ("The Viis scouts have caught an intruder.", "In Good Faith", "our scouts have apprehended an intruder."),
 "M602b": ("Emet-Selch is embarrassed to be caught.", "In Good Faith", "Well...this is embarrassing."),
 "M602c": ("Emet-Selch plucked Y'shtola from the Lifestream.", "In Good Faith", "Emet-Selch, the Ascian of whom I spoke. 'Twas he who plucked thee from the Lifestream."),
 "M602d": ("Emet-Selch lends you an aetherial lamp to search the woods.", "In Good Faith", "Keep it close as you venture out into the woods."),
 "M602e": ("Y'shtola invoked Flow, which carried her soul into the Lifestream.", "In Good Faith", "Thou didst invoke the power of Flow, which thence did usher thy soul unto the Lifestream."),
 "M602f": ("Y'shtola admits she did something reckless.", "In Good Faith", "I did something exceedingly reckless."),
 "M602g": ("Emet-Selch says the Ascians act for the greater good.", "In Good Faith", "we Ascians do what we do for the greater good."),
 "M602h": ("Y'shtola would make ready to enter the Qitana Ravel and slay the Lightwarden.", "In Good Faith", "We must make ready to enter the Qitana Ravel, and put the Lightwarden to the sword."),
 # #603 The Burden of Knowledge
 "M603a": ("The Qitana Ravel is said to hold the empire's accumulated knowledge.", "The Burden of Knowledge", "The accumulated knowledge of the empire is said to reside within."),
 "M603b": ("Emet-Selch says the world was divided across thirteen reflections.", "The Burden of Knowledge", "the world was divided across ten and three reflections, sundering the land and all who dwelled upon it."),
 "M603c": ("Emet-Selch says Hydaelyn rose to serve as Zodiark's shackles.", "The Burden of Knowledge", "From the fears of these naysayers would rise Hydaelyn─She who was to serve as His shackles."),
 "M603d": ("Emet-Selch says the Ascians summoned Zodiark.", "The Burden of Knowledge", "It was we who summoned Zodiark─we natives of that sundered paradise."),
 "M603e": ("Emet-Selch's tale makes Zodiark and Hydaelyn the eldest of primals, conjured by the Ascians.", "The Burden of Knowledge", "that Zodiark and Hydaelyn are the eldest of primals, and that it was the Ascians who first conjured them into being."),
 "M603f": ("The Lightwarden falls at Rak'tika Falls, and the night sky returns.", "The Burden of Knowledge", "the primordial Light of the firmament at last gives way to a breathtaking night sky."),
 "M603g": ("Y'shtola warns that though you show no corruption, the danger remains.", "The Burden of Knowledge", "shows no immediate signs of corruption, the danger remains."),
 "M603h": ("Y'shtola asks whether there is truth in Emet-Selch's claims.", "The Burden of Knowledge", "Do you suppose there is any truth in Emet-Selch's claims?"),
 # #604 Bearing With It
 "M604a": ("Y'shtola reports that the Lightwarden is no more.", "Bearing With It", "I am pleased to report that the Lightwarden is no more, thanks in large part to you."),
 "M604b": ("The Viis must keep Ronka's secrets from the wrong hands.", "Bearing With It", "So long as we live here in these woods, the secrets of Ronka must not fall into the wrong hands."),
 "M604c": ("The Eulmorans fled at the night sky, and the Children retreated to Woven Oath.", "Bearing With It", "They turned tail and fled at the sight of the night sky. … The Children of the Everlasting Dark have also retreated back to Woven Oath."),
 "M604d": ("Runar hails the Scions as the Bringers of Shadow and the Warriors of Darkness.", "Bearing With It", "You are the Bringers of Shadow. The Warriors of Darkness."),
 "M604e": ("Y'shtola refuses to be worshipped.", "Bearing With It", "But we are not worthy of your reverence, nor have we any desire to be worshipped."),
 "M604f": ("Y'shtola says the Scions must all go, sharing the same path.", "Bearing With It", "We must go─all of us. For we share the same path and the same fate."),
 "M604g": ("Runar swears to hold the Scions in his heart.", "Bearing With It", "By the boundless dark, this I swear."),
 "M604h": ("Ardbert's shade watches.", "Bearing With It", "Ardbert's shade observes."),
 # #605 Out of the Wood
 "M605a": ("Y'shtola fears the Lightwarden's light was not negated by Hydaelyn's blessing.", "Out of the Wood", "When you defeated the Lightwarden, I fear the light which poured forth from it was not negated by Hydaelyn's blessing."),
 "M605b": ("Your aether is suffused with light like the sin eaters'.", "Out of the Wood", "Suffused with an overabundance of light not unlike the sin eaters."),
 "M605c": ("With every Warden you defeat, the danger to you grows.", "Out of the Wood", "with every Warden you defeat, the danger to you grows greater."),
 "M605d": ("Alphinaud hears the Rak'tika Warden is slain.", "Out of the Wood", "Found and slain, you say? I should have known."),
 "M605e": ("The Exarch's time away from the tower has taken its toll.", "Out of the Wood", "Exarch, you mustn't push yourself. Your time away from the tower has clearly taken its toll."),
 "M605f": ("Ardbert sees a light sealed inside you.", "Out of the Wood", "So there's a light sealed inside you, is there? You wouldn't know it from the outside."),
 "M605g": ("Ardbert doubts Emet-Selch's talk of Hydaelyn as just another primal.", "Out of the Wood", "All that rot about Hydaelyn being no different from any other primal..."),
 "M605h": ("A general vanished from the Ghimlyt Dark.", "Out of the Wood", "One of our generals posted to the Ala Mhigan front recently disappeared without trace from the battlefield at the Ghimlyt Dark."),
 "M605i": ("Gaius reasons that Elidibus needs no new host, so asks who would.", "Out of the Wood", "Elidibus plainly has no need of a new host, so the question becomes, who?"),
 "M605j": ("Y'shtola lived two years among the Blessed under Master Matoya's name.", "Out of the Wood", "For two years I have lived with the Blessed, learned their culture, even going so far as to adopt Master Matoya's name as my own."),
 "M605k": ("Estinien and Gaius search for their next target.", "Out of the Wood", "All the more reason to hasten our search. How close are your people to identifying our next target?"),
 "M605l": ("The scene shifts to Garlemald.", "Out of the Wood", "Meanwhile, in Garlemald..."),
 "M605m": ("Eulmore has sent soldiers to all corners of Norvrandt to defend the Wardens.", "Out of the Wood", "Eulmore has but recently dispatched soldiers to all corners of Norvrandt to defend them."),
 # #606 When It Rains
 "M606a": ("A host of sin eaters advances on the Crystarium.", "When It Rains", "An entire host of sin eaters appears to be advancing upon the Crystarium."),
 "M606b": ("Alisaie cannot see how the sin eaters came, with the darkness restored.", "When It Rains", "Where are they coming from? This shouldn't be possible─we restored the darkness!"),
 "M606c": ("The Exarch prepares a barrier around the Crystarium.", "When It Rains", "The Crystal Exarch is preparing to deploy a barrier around the Crystarium as we speak."),
 "M606d": ("The barrier holds.", "When It Rains", "Excellent. The barrier is holding."),
 "M606e": ("Crystarium guards turned into sin eaters and attacked Lyna.", "When It Rains", "Minfilia notices that Lyna was attacked by Crystarium Guard who turned into sin eaters."),
 "M606f": ("Lyna says her own soldiers turned on her.", "When It Rains", "They...they turned on me..."),
 "M606g": ("Thancred is injured protecting Lyna.", "When It Rains", "Thancred protects her from a sin eater attack, but is injured."),
 "M606h": ("Y'shtola finds the eaters too organized for instinct alone.", "When It Rains", "These eaters are too organized. They cannot merely be acting on instinct."),
 "M606i": ("Lyna and her people engage the eater host in Lakeland.", "When It Rains", "where Lyna and her people are already engaging the eater host."),
 "M606j": ("You and Alisaie activate the barrier's anchors.", "When It Rains", "several anchors around the city must activated before the protective barrier that serves as its primary defense can take effect."),
 # #607 Word from On High
 "M607a": ("Alisaie helps move the wounded.", "Word from On High", "I'm planning to assist in moving them, but even so, we simply don't have enough hands."),
 "M607b": ("A wounded guard, fearing he will turn, begs to be killed if he does.", "Word from On High", "If I turn, please... Please, kill me, I beg you."),
 "M607c": ("Lyna says the war is far from over.", "Word from On High", "Unfortunately, this war is far from over."),
 "M607d": ("Lyna blames herself for those she failed to protect.", "Word from On High", "Who I failed to protect when they needed me most."),
 "M607e": ("Lyna walks away and collapses.", "Word from On High", "Lyna walks away but collapses."),
 "M607f": ("Vauthry calls the tragedy divine retribution for the Crystarium's defiance.", "Word from On High", "Divine retribution for your defiance."),
 "M607g": ("Vauthry offers himself as a benevolent savior.", "Word from On High", "The heavens have bequeathed to you a benevolent savior─me!"),
 "M607h": ("Vauthry says the sin eaters regard him and his as kin.", "Word from On High", "Why, already our winged brothers and sisters regard me and mine as kin, alike to them in beauty and purity!"),
 "M607i": ("Lyna is the guard's captain.", "Word from On High", "Captain Lyna is about somewhere"),
 # #608 Small Favors
 "M608a": ("Lyna asks you to check on Thancred and Minfilia, who risked themselves for her.", "Small Favors", "They endangered themselves on my behalf, and I would feel better knowing that they are well looked after."),
 "M608b": ("Thancred was badly hurt by a sin eater.", "Small Favors", "Thancred, in particular, sustained quite an injury from that sin eater."),
 "M608c": ("Minfilia blames her own carelessness.", "Small Favors", "It's my fault, you know. I jumped at the chance to help Lyna, but I was careless."),
 "M608d": ("The healers struggle to keep up with the wounded.", "Small Favors", "We're struggling to keep up with the number of wounded that are being brought in."),
 "M608e": ("Thancred says the healers have done wonders.", "Small Favors", "The eater landed an unfortunately solid blow, but the healers here have done wonders."),
 "M608f": ("A wounded guard still believes in the Warrior of Darkness and the Exarch.", "Small Favors", "But I ''believe'' in the Warrior of Darkness. In the Crystal Exarch."),
 "M608g": ("Thancred promises to tell the Exarch.", "Small Favors", "We'll tell him. You have my word."),
 # #609 The Best Way Out
 "M609a": ("You deliver the soldier's message of support to the Exarch.", "The Best Way Out", "he reminds you to deliver the soldier's message of support to the Exarch"),
 "M609b": ("The Exarch says Vauthry can enslave the minds of others.", "The Best Way Out", "It appears he has mastered a technique which allows him to enslave the minds of others."),
 "M609c": ("The sin eaters are Vauthry's to command.", "The Best Way Out", "The sin eaters are his to command."),
 "M609d": ("Minfilia proposes going to Amh Araeng to become one with the Oracle of Light.", "The Best Way Out", "Minfilia suggests that you travel to Amh Araeng, where she may become one with the Oracle of Light"),
 "M609e": ("Emet-Selch calls Minfilia a reincarnation.", "The Best Way Out", "I thought you were a rather underwhelming reincarnation, but it all makes sense now."),
 "M609f": ("Emet-Selch says one of them must consume the other.", "The Best Way Out", "To wit, one being must consume the other. Who shall be the lucky winner?"),
 "M609g": ("Alisaie, Alphinaud and Y'shtola go east to distract the Eulmoran army while the rest take the western route.", "The Best Way Out", "sending her, Alphinaud, and Y'shtola to the east to distract the Eulmoran Army while the rest of you take the western route to Nabaath Areng."),
 "M609h": ("Minfilia wants to be strong enough to face her destiny.", "The Best Way Out", "I want to be stronger─strong enough to face my destiny."),
 "M609i": ("The Exarch is burdened by the sacrifices made to restore balance.", "The Best Way Out", "the Exarch is plainly burdened by the sacrifices made in the name of restoring balance to the First."),
 # #610 Free Trade
 "M610a": ("Garik was a mining village before the Flood.", "Free Trade", "This place is Garik. Before the Flood, it was home to many miners."),
 "M610b": ("The Flood crushed the mines around Nabaath Areng.", "Free Trade", "The Flood rent the stone and crushed the mines surrounding Nabaath Areng."),
 "M610c": ("Minfilia is bound for Nabaath Areng.", "Free Trade", "We're on our way to Nabaath Areng, ourselves."),
 "M610d": ("The trolley is locked behind a gate.", "Free Trade", "It is locked behind a gate, however."),
 "M610e": ("The Eulmorans have an airship.", "Free Trade", "The Eulmorans have one, I hear."),
 "M610f": ("There are no Eulmorans in the Hills of Amber.", "Free Trade", "there have been no sightings of Eulmorans at all in the Hills of Amber."),
 # #611 The Trolley Problem
 "M611a": ("The trolley controls stand at Mount Biran Mines.", "The Trolley Problem", "You should travel east to Mount Biran Mines! That is where the trolley controls stand."),
 "M611b": ("A stone Talos once opened the gate.", "The Trolley Problem", "Before, there was a hulking thing of stone─the Talos. It opened the gate, they say."),
 "M611c": ("No one operates a Talos now.", "The Trolley Problem", "But none operate such a thing now."),
 "M611d": ("Someone is maintaining the cars and rails.", "The Trolley Problem", "Whoever is maintaining the cars and rails must know something that we don't."),
 "M611e": ("Only Magnus knows the trolley's full operation.", "The Trolley Problem", "If you spoke with Magnus, you'd understand. He's the only one with full knowledge of the trolley's operation."),
 "M611f": ("The engineers lead you to Twine.", "The Trolley Problem", "Right. It looks like you'll be following us back to Twine, then!"),
 # #612 Rust and Ruin
 "M612a": ("The trolley brought Twine its people.", "Rust and Ruin", "But it was still the trolley that brought them here."),
 "M612b": ("Twine's remaining residents are the destitute and those with nowhere else to go.", "Rust and Ruin", "The only residents that remain are the destitute, the delusional, and those with nowhere else to go."),
 "M612c": ("Magnus says there is nothing left in Nabaath Areng.", "Rust and Ruin", "What? There's nothing in Nabaath Areng. Not anymore."),
 "M612d": ("Magnus refuses to talk about the trolley.", "Rust and Ruin", "No. I'm sick of people asking me about the blasted thing. Leave me be."),
 "M612e": ("Minfilia thinks Magnus believes her weak.", "Rust and Ruin", "He only said that because...because he thinks I'm weak."),
 "M612f": ("Magnus calls the journey fruitless and the trolley impossible.", "Rust and Ruin", "He seems unwilling to discuss your request for help beyond saying that to travel to Nabaath Areng is fruitless, and to use the trolley to do so, impossible."),
 # #613 On Track
 "M613a": ("Minfilia is lost in thought.", "On Track", "Minfilia remains adrift in the turbulent sea of thought."),
 "M613b": ("Minfilia proposes asking Twine's other residents.", "On Track", "It's clear that Magnus has no intention of helping us, but perhaps we should ask the other residents?"),
 "M613e": ("Magnus and his wife returned to Twine seven years ago.", "On Track", "But then, about seven years past, Magnus and his wife returned to us."),
 "M613f": ("Sin eaters killed Magnus's son.", "On Track", "It didn't help, in the end. The sin eaters got the boy."),
 "M613g": ("Thancred keeps his hopes for Minfilia to himself.", "On Track", "I would not shackle her again by making my hopes known."),
 # #614 Down for Maintenance
 "M614a": ("Twine has a Talos it meant to repair.", "Down for Maintenance", "Not that it'll do you any good, but we do have a Talos we've been meaning to repair."),
 "M614b": ("Fractures in the Talos impede its aether.", "Down for Maintenance", "Or so it would, were it not for several fractures which now impede said flow."),
 "M614c": ("Urianger needs three stones from the debitage.", "Down for Maintenance", "I spied but three obstructions to the flow of aether in the Talos, and thus would I ask you provide three stones of the debitage."),
 "M614d": ("The core still will not stir.", "Down for Maintenance", "Strange... The core refuseth to stir."),
 "M614e": ("Without its core repaired or replaced, the Talos cannot be restored.", "Down for Maintenance", "Failing its repair or replacement, the Talos cannot be restored."),
 "M614f": ("Twine tried to find a replacement before.", "Down for Maintenance", "We tried to find another. In case things turned out as they are now, but..."),
 "M614g": ("Jeryk agrees to tell you what happened.", "Down for Maintenance", "After all you lot have done for me, I suppose it's the least I can do."),
 # #615 The Truth Hurts
 "M615a": ("A Talos heart needs special stone with aetherial conductivity.", "The Truth Hurts", "their hearts cannot be made of just any stone. You need a special sort with sufficient aetherial conductivity."),
 "M615b": ("Magnus's wife kept digging deeper until her mine collapsed.", "The Truth Hurts", "She just kept digging deeper and deeper. And then the mine collapsed."),
 "M615c": ("Magnus has never been the same since.", "The Truth Hurts", "Magnus has never been the same since."),
 "M615d": ("Magnus's son was Skuli and his wife Agna.", "The Truth Hurts", "My son was named Skuli. My wife, Agna."),
 "M615e": ("Thancred robbed a young girl of her family.", "The Truth Hurts", "But I finally had a family. And then...and then I robbed a young girl of hers."),
 "M615f": ("Thancred refuses to let her legacy die.", "The Truth Hurts", "That is why I refuse to let her legacy die."),
 "M615g": ("You may find stone at Nuvy's Leavings.", "The Truth Hurts", "Though I suppose, if you really wanted to try, you may find something at Nuvy's Leavings."),
 "M615h": ("Urianger says Thancred's heart is in turmoil.", "The Truth Hurts", "Though he wouldst be quick to deny it, his heart is in turmoil, and his thoughts clouded."),
 # #616 A Convenient Distraction
 "M616a": ("The stone is leonine, which powers every Talos in the Hills of Amber.", "A Convenient Distraction", "The stone you're looking for is leonine. All the Talos in the Hills of Amber are powered using them."),
 "M616b": ("The deepest reaches of the mine were held up by Talos.", "A Convenient Distraction", "In the deepest reaches of the mine, we used Talos to keep the pathways from collapsing."),
 "M616c": ("Guthjon wants his lost Voeburt gold piece in exchange.", "A Convenient Distraction", "he asks a favor of you─to retrieve a Voeburt gold piece he dropped somewhere in the mine."),
 "M616d": ("Thancred's sundrops help the eye take in more light.", "A Convenient Distraction", "That's why I propose we use these─sundrops. They help the eye take in more light."),
 "M616e": ("Thancred compensates for a condition.", "A Convenient Distraction", "It hasn't been easy finding ways to compensate for my...condition."),
 "M616f": ("You find the coin.", "A Convenient Distraction", "I'll be damned. You actually found it!"),
 "M616g": ("Guthjon warns the find does not ensure success.", "A Convenient Distraction", "Well, a deal's a deal. But don't think this means you'll find what you're after."),
 # #617 A Dirty Job
 "M617a": ("Knockers fit through cracks miners cannot reach.", "A Dirty Job", "They can fit through cracks and crevices down where we could never hope to reach."),
 "M617b": ("Smoke bombs flush the knockers out.", "A Dirty Job", "Set off a few in the mines and you'll flush them out in no time."),
 "M617c": ("Minfilia was a miner before founding the Path of the Twelve.", "A Dirty Job", "prior to founding the Path of the Twelve, long before the Scions, she was something of a miner."),
 "M617d": ("F'lhaminn took Minfilia in after her father died.", "A Dirty Job", "After her father died, F'lhaminn took her in and taught her the trade."),
 "M617e": ("The find is the largest in decades.", "A Dirty Job", "It's been decades since we've found anything approaching this big!"),
 "M617f": ("The stone is engraved to Magnus and Skuli.", "A Dirty Job", "To my beloved Magnus and Skuli."),
 "M617g": ("It was a gift to Magnus from his wife.", "A Dirty Job", "It was a gift to Magnus from his wife!"),
 "M617h": ("Knockers carried it off before anyone reached her.", "A Dirty Job", "Those rock-backed bastards must've made off with it before we could clear a path to her."),
 # #618 Have a Heart
 "M618a": ("Thancred tells Magnus the stone was Agna's gift.", "Have a Heart", "Your name is engraved on it, along with your son's. It was a gift from your wife, Magnus. From Agna."),
 "M618b": ("Magnus gives up the stone.", "Have a Heart", "Take it. Do with it what you will."),
 "M618c": ("The Talos works.", "Have a Heart", "''The Talos activates.'' … It's working! It's working!"),
 "M618d": ("Minfilia believes Thancred wishes her dead so another could return.", "Have a Heart", "I wish he'd just say it─just say that he hates me! That he wishes I was dead so that she could return..."),
 "M618e": ("Urianger confesses he set the Oracle on her path.", "Have a Heart", "'Twas ''I'' who set the Oracle on her path unto the First."),
 "M618f": ("Emet-Selch says he shaped the nation that built the tower.", "Have a Heart", "The once-great nation whose ingenuity gave birth to this tower was shaped by my hand."),
 "M618g": ("The Exarch calls himself the adjudicator of the history Emet-Selch trifled with.", "Have a Heart", "I am the adjudicator of the sacred history with which you dared trifle."),
 "M618h": ("The Exarch says Emet-Selch had a hand in Allag.", "Have a Heart", "You had a hand in Allag as well."),
 "M618i": ("The Exarch vows the history that led here will be unwritten.", "Have a Heart", "The history which led us here ''will'' be unwritten."),
 # #619 Full Steam Ahead
 "M619a": ("The gate opens at the Talos's approach.", "Full Steam Ahead", "It's designed to open at the Talos's approach."),
 "M619b": ("Urianger stays to apprise Alisaie and the others.", "Full Steam Ahead", "I would apprise Mistress Alisaie and the others of our progress."),
 "M619c": ("Minfilia will meet the original Oracle, the real Minfilia.", "Full Steam Ahead", "Before long, Minfilia will come face-to-face with the original Oracle–the real Minfilia."),
 "M619d": ("Ran'jit serves Lord Vauthry.", "Full Steam Ahead", "Had you only sworn fealty to Lord Vauthry, you would have no cause to skulk about like frightened animals."),
 "M619e": ("Ran'jit claims to seek peace.", "Full Steam Ahead", "We seek to bring peace to what is left of this shattered land, while these mad fools would only bring further chaos down upon us!"),
 "M619f": ("Ran'jit sought out Minfilia's successors again and again.", "Full Steam Ahead", "who sought out your successor to carry on the futile struggle again and again!?"),
 "M619g": ("The Scions are everything to Minfilia.", "Full Steam Ahead", "They're everything to me. All I have and all I need."),
 "M619h": ("Thancred leaves Minfilia in your hands.", "Full Steam Ahead", "I leave her in your hands. Hurry!"),
 "M619i": ("Ran'jit retreats and Thancred collapses, injured.", "Full Steam Ahead", "''Ran'jit retreats. Thancred, injured, collapses on the ground.''"),
 "M619j": ("Nabaath Areng is where the Oracle stopped the Flood.", "Full Steam Ahead", "This is where she stopped the Flood."),
 "M619k": ("Ran'jit topples the trolley.", "Full Steam Ahead", "With a single blow, Ran'jit topples the trolley"),
 # #620 Crossing Paths
 "M620a": ("Minfilia senses the Oracle's presence.", "Crossing Paths", "I can sense her presence, albeit faintly."),
 "M620b": ("In an echo, the Oracle of Light stays the Flood.", "Crossing Paths", "No. Stand back. … We shall stay the Flood."),
 "M620c": ("Ardbert wanted to make the sacrifice himself.", "Crossing Paths", "But this is what I want! It's my sacrifice to make!"),
 "M620d": ("The Oracle tells Ardbert he must give them hope when all hangs in the balance.", "Crossing Paths", "When all hangs in the balance, ''you'' must give them hope."),
 "M620e": ("The Oracle warns the power Minfilia seeks has a price.", "Crossing Paths", "But know, my child, that the power you seek will come at a price."),
 "M620f": ("The Oracle spent her power staying the Flood.", "Crossing Paths", "Though my power was all but spent in staying the Flood, I prayed this final act would give hope to those who survived."),
 "M620g": ("The girl thanks the Oracle, whom she calls Minfilia.", "Crossing Paths", "Thank you, Minfilia, for believing in us. For believing in me."),
 "M620h": ("The Oracle has given her a new path of her own.", "Crossing Paths", "But she's given me a new path─a new life─that I can call my own."),
 "M620i": ("She can feel the Lightwardens, one of them in Amh Araeng.", "Crossing Paths", "And the Lightwardens. There's one here in Amh Araeng."),
 "M620j": ("She can now track the Lightwardens.", "Crossing Paths", "I can track the Lightwardens now. Maybe even help you fight them."),
 "M620k": ("Thancred tells her she is family.", "Crossing Paths", "But I want to. You're family. How else would I feel?"),
 "M620l": ("Y'shtola wants her to have a name of her own.", "Crossing Paths", "A name of her own. I would not have her walk in the shadow of another any longer."),
 "M620m": ("Thancred suggests Ryne, which Urianger knows as \"blessing\" in Fae.", "Crossing Paths", "What about... Ryne? … Ah. “Blessing” in Fae..."),
 "M620n": ("She accepts the name, and Thancred welcomes Ryne aboard.", "Crossing Paths", "Ryne... Yes, I rather like the sound of it. … That settles it, then. Welcome aboard, Ryne!"),
 "M620o": ("The others found Thancred at death's door after Urianger called them.", "Crossing Paths", "It's a good thing Urianger called on us when he did. You were at death's door when we found you."),
 "M620p": ("The Oracle says they stand at a crossroads.", "Crossing Paths", "We stand now at the crossroads. A decision must be made."),
 "M620q": ("The Oracle is gone, though the girl still feels her.", "Crossing Paths", "And even though she's gone, I can still feel her...warm and calm and gentle."),
}

# ---- Entities ------------------------------------------------------------------------------------------------------
ENTITIES = {
 # recurring from accepted content or earlier eras (same id and category merge)
 "char-thancred": "character", "char-urianger": "character", "char-yshtola": "character", "char-alphinaud": "character",
 "char-alisaie": "character", "char-minfilia": "character", "char-solus": "character",
 "char-gaius": "character", "char-estinien": "character", "org-ascians": "organization", "org-scions": "organization",
 # the Shadowbringers cast (content_5_0_part1 creates these under the same ids)
 "char-crystal-exarch": "character", "char-emet-selch": "character", "char-ryne": "character", "char-ardbert": "character",
 "char-lyna": "character", "loc-crystarium": "location", "org-lightwardens": "organization", "char-ranjit": "character",
 "char-vauthry": "character", "loc-eulmore": "location", "char-feo-ul": "character", "char-titania": "character",
 "org-pixies": "organization", "char-zodiark": "character",  # content_5_0_part1, content_5_0_part3
 # new in this era
 "char-seto": "character", "char-runar": "character", "org-nights-blessed": "organization",
 "org-children-of-the-everlasting-dark": "organization", "org-viis": "organization", "char-almet": "character",
 "char-magnus": "character",
 "evt-the-throne-of-lyhe-ghiah": "event", "evt-the-ascians-offer": "event", "evt-darkness-in-the-greatwood": "event",
 "evt-allies-of-ronka": "event", "evt-the-warden-of-the-greatwood": "event", "evt-the-siege-of-the-crystarium": "event",
 "evt-the-road-to-nabaath-areng": "event", "evt-the-oracles-crossroads": "event",
}

# ---- Presentations ---------------------------------------------------------------------------------------------------
PRES = {
 # -- Il Mheg
 "char-seto": [
   P(S580, None, "main", "Seto",
     "The largest of the amaro of Wolekdorf in Il Mheg, their leader and bearer of the crystal shoes, last of the four relics. He welcomed you warmly, "
     "but thinks facing the faerie king folly and refuses you the shoes; Urianger concludes he does so out of concern for you.",
     ["M580d", "M580e", "M580g"]),
   P(S581, None, "main", "Seto",
     "Leader of the amaro of Wolekdorf, who keeps the crystal shoes. He can no longer bear to see men fight and die. As a trial he lured sin eaters out with his voice, "
     "as he once did hunting with an old friend, and though you prevailed, he still needs time and asks a favor.",
     ["M580d", "M581a", "M581c", "M581d", "M581e"]),
   P(S582, None, "main", "Seto",
     "Leader of the amaro of Wolekdorf. You recovered his medallion, a gift from his old friend Ardbert, whom everyone blamed for the Flood. "
     "Seto says your soul strongly resembles Ardbert's, and has placed his faith in you with the crystal shoes.",
     ["M580d", "M582a", "M582b", "M582c", "M582d", "M582e"]),
 ],
 "char-titania": [
   P(S580, None, "main", "Titania",
     "The faerie king sealed in Lyhe Ghiah. Titania is a title, not a name, borne by the one chosen to lead the pixies, and this Titania has become a sin eater, "
     "its powers unchanged. The Nu Mou, unable to deal with their fallen monarch, gave you the stone scepter to break the seal.",
     ["M580b", "M580c", "M580a"]),
   P(S583, None, "main", "Titania",
     "The Light-corrupted king of Il Mheg, bereft of reason and mercy. Bearing all four relics, you broke the seal on Lyhe Ghiah and defeated this Lightwarden, restoring night to Il Mheg.",
     ["M583a", "M583b", "M583c"]),
 ],
 "char-feo-ul": [
   P(S583, None, "main", "Feo Ul",
     "A pixie of Il Mheg who stood with you in Lyhe Ghiah. By Il Mheg's laws the one who defeats the king should take the throne, but Feo Ul took that burden in your stead, "
     "becoming the new Titania, and led an army that drove the Eulmorans from Lydha Lran.",
     ["M583d", "M583e", "M580b"], ["Titania"]),
 ],
 "org-pixies": [
   P(S583, None, "main", "The pixies",
     "Fae of Il Mheg, led by the one who bears the title Titania. You defeated their Light-corrupted king, and Feo Ul took the throne as the new Titania and led them to repel the Eulmoran army at Lydha Lran.",
     ["M580b", "M583c", "M583e"]),
 ],
 "char-zodiark": [
   P(S603, None, "main", "Zodiark",
     "The eldest and most powerful of primals, Emet-Selch claims, summoned by the Ascians before the world was sundered into thirteen reflections. Hydaelyn, he says, rose to serve as his shackles.",
     ["M603d", "M603e", "M603b", "M603c"]),
 ],
 "char-ranjit": [
   P(S582, None, "main", "Ran'jit",
     "An old mortal, as the pixies describe him, who has spoiled their tricks and is closing in on Il Mheg. Thancred fears that if Ran'jit finds his way in, all their efforts will be for naught.",
     ["M582f", "M582h"]),
   P(S583, None, "main", "Ran'jit",
     "General of the Eulmoran army, who pursued you into Il Mheg after villains he says fled there. He trained the girl Minfilia as an Oracle and wants her back. "
     "When the fae turned his soldiers, he withdrew, vowing that all who stand with the Warrior of Darkness will face justice, as his master demands.",
     ["M583f", "M583j", "M583g", "M583h", "M583e", "M583i"], ["General Ran'jit"]),
   P(S594, None, "main", "Ran'jit",
     "General of the Eulmoran army. By Lord Vauthry's decree he proclaimed Rak'tika under Eulmore's rule, gave the Children of the Everlasting Dark authority over the forest, "
     "and warned the Night's Blessed that any found there on his return will be treated as traitors.",
     ["M583f", "M594c", "M594f", "M594g"], ["General Ran'jit"]),
   P(S600, None, "main", "Ran'jit",
     "General of the Eulmoran army. In the Great Pyramid of Ux'ner he barred your way, refused to trade the antidote for the poisoned Blessed, and kicked his own adjutant into a chasm. "
     "Thancred struck him down into the depths.",
     ["M600a", "M600d", "M600g", "M600f"], ["General Ran'jit"]),
   P(S619, None, "main", "Ran'jit",
     "General of the Eulmoran army, sworn to Lord Vauthry, who claims to seek peace. He waited past the gate to Nabaath Areng, toppled your trolley, and raged that he trained Minfilia "
     "and sought out her successors again and again. Thancred held him off until he retreated.",
     ["M619d", "M619e", "M619k", "M619f", "M619i"], ["General Ran'jit"]),
 ],
 "loc-eulmore": [
   P(S583, None, "main", "Eulmore",
     "Home of the Eulmoran army, which under General Ran'jit marched on Il Mheg and was repelled by the fae. The girl Minfilia, whom Ran'jit trained as an Oracle, refuses to return there.",
     ["M583k", "M583e", "M583j", "M583g", "M583h"]),
   P(S594, None, "main", "Eulmore",
     "A city ruled by Lord Vauthry, who would unite the world under his dominion through the sin eaters. By his decree Rak'tika now falls under Eulmore's governance.",
     ["M594c", "M594d", "M594f"]),
   P(S605, None, "main", "Eulmore",
     "A city ruled by Lord Vauthry, who claims Rak'tika and would rule the world through the sin eaters. It has sent soldiers to all corners of Norvrandt to defend the Wardens.",
     ["M594c", "M594d", "M605m"]),
   P(S609, None, "main", "Eulmore",
     "A city ruled by Lord Vauthry, who the Crystal Exarch says can enslave minds and commands the sin eaters. Its army hunts the Scions across Norvrandt.",
     ["M609b", "M609c", "M609g"]),
 ],
 # -- The Ascians
 "char-solus": [
   P(S584, None, "main", "Solus",
     "A former emperor of Garlemald and an Ascian. In the Crystarium a man introduced himself as Solus, founding father of the Garlean Empire, then revealed his true identity: the Ascian Emet-Selch.",
     ["M584b", "M584c"], ["Emperor Solus"]),
 ],
 "char-emet-selch": [
   P(S584, None, "main", "Emet-Selch",
     "An Ascian, who first named himself Solus, founding father of the Garlean Empire. He blames you for upsetting the Rejoining his kind has labored for, and offers cooperation, "
     "swearing not to hinder your hunt for the Lightwardens. Urianger told him that making his case through an illusion reflects poorly on his sincerity.",
     ["M584b", "M584c", "M584d", "M584e", "M584f", "M584j"], ["Solus"]),
   P(S585, None, "main", "Emet-Selch",
     "An Ascian, once known as Solus, founding father of the Garlean Empire. He renewed his offer of partnership, claiming only to observe your hunt for the Lightwardens, and the Scions refused an Ascian alliance.",
     ["M584b", "M584c", "M585a", "M585b"], ["Solus"]),
   P(S587, None, "main", "Emet-Selch",
     "An Ascian, once known as Solus, who offers you cooperation. He tags along on your travels in the Rak'tika Greatwood, refusing to help as a mere observer.",
     ["M584c", "M584f", "M587h"], ["Solus"]),
   P(S602, None, "main", "Emet-Selch",
     "An Ascian, once known as Solus, who follows the Scions as an observer. Caught by the Viis, he revealed that he plucked Y'shtola from the Lifestream, and with his help she returned. "
     "The Ascians, he says, act for the greater good.",
     ["M584c", "M587h", "M602a", "M602c", "M602g"], ["Solus"]),
   P(S603, None, "main", "Emet-Selch",
     "An Ascian, once known as Solus, who saved Y'shtola from the Lifestream. In the Qitana Ravel he claimed that the world was sundered into thirteen reflections, that the Ascians summoned Zodiark, "
     "and that Hydaelyn rose to be his shackles, the eldest primals both. Y'shtola wonders if it is true.",
     ["M584c", "M602c", "M603b", "M603d", "M603c", "M603h"], ["Solus"]),
   P(S609, None, "main", "Emet-Selch",
     "An Ascian, once known as Solus, who claims the Ascians summoned Zodiark. Hearing Minfilia's plan to become one with the Oracle, he called her a reincarnation, and said one of them must consume the other.",
     ["M584c", "M603d", "M609d", "M609e", "M609f"], ["Solus"]),
   P(S618, None, "main", "Emet-Selch",
     "An Ascian, once known as Solus. He told the Crystal Exarch that he shaped the nation that built the Exarch's tower, and the Exarch says he had a hand in Allag as well.",
     ["M584c", "M618f", "M618h"], ["Solus"]),
 ],
 "org-ascians": [
   P(S584, None, "main", "The Ascians",
     "A group who sow strife and founded the Garlean Empire. One of them, Emet-Selch, admits they have labored for ages to rejoin the thirteen shards, and Ardbert says an Ascian in white urged his world "
     "toward the Rejoining, though the Flood was the Ascians' own making.",
     ["M584c", "M584d", "M584g", "M584h"]),
   P(S603, None, "main", "The Ascians",
     "A group who have labored for ages to rejoin the thirteen shards, and who, Emet-Selch says, act for the greater good. He claims they summoned Zodiark, eldest of primals, before the world was sundered.",
     ["M584d", "M602g", "M603d", "M603e"]),
 ],
 # -- Ardbert
 "char-ardbert": [
   P(S582, None, "main", "Ardbert",
     "Seto's old friend, who gave him the medallion he treasures. Everyone blamed Ardbert and his comrades for the Flood, and Seto says your soul strongly resembles his.",
     ["M582b", "M582c", "M582d"]),
   P(S584, None, "main", "Ardbert",
     "Seto's old friend, blamed with his comrades for the Flood, whose soul Seto says resembles yours. His shade appears to you, saying an Ascian in white urged his world toward the Rejoining, "
     "not knowing the Flood was the Ascians' own making.",
     ["M582c", "M582d", "M584i", "M584g", "M584h"]),
   P(S593, None, "main", "Ardbert",
     "A shade who walks with you, blamed in life for the Flood. Among the murals at Woven Oath he recalled the researcher who believed the first painting dated to an age of myth, and wondered who tried to scrape another off the wall.",
     ["M582c", "M584i", "M593d", "M593e"]),
   P(S605, None, "main", "Ardbert",
     "A shade who walks with you, blamed in life for the Flood. He sees the light sealed inside you, and doubts Emet-Selch's talk of Hydaelyn as just another primal.",
     ["M582c", "M604h", "M605f", "M605g"]),
   P(S620, None, "main", "Ardbert",
     "A shade who walks with you. An echo at Nabaath Areng showed him begging to make the sacrifice himself as the Flood came; the Oracle told him his time had not come, and that when all hangs in the balance he must give them hope.",
     ["M582c", "M620b", "M620c", "M620d"]),
 ],
 # -- The Crystarium
 "char-crystal-exarch": [
   P(S585, None, "main", "The Crystal Exarch",
     "The master of the Crystarium's tower. With the Lightwardens of Lakeland and Il Mheg struck down, he divided your forces to find the rest, and sent you after Y'shtola, who will not speak with him. "
     "Invited to Eulmore by Lord Vauthry, he goes with Alphinaud, though his power wanes far from the tower.",
     ["M585l", "M585c", "M585e", "M585k", "M585g", "M585h", "M585j"], ["The Exarch", "The enigmatic figure"]),
   P(S587, None, "main", "The Crystal Exarch",
     "The master of the Crystarium's tower, who has gone to Eulmore at Lord Vauthry's invitation. He sent you to find a tablet for Y'shtola, but she lost her trust in him over his secrecy and half-truths, "
     "and finds the tablet's discovery suspiciously convenient.",
     ["M585g", "M586d", "M587e", "M587g"], ["The Exarch", "The enigmatic figure"]),
   P(S594, None, "main", "The Crystal Exarch",
     "The master of the Crystarium's tower, whose gift of a tablet has shown the Scions their course. In Eulmore he confronted Lord Vauthry, who tried to enthrall him; the Exarch vanished.",
     ["M585h", "M591g", "M594d", "M594e"], ["The Exarch", "The enigmatic figure"]),
   P(S605, None, "main", "The Crystal Exarch",
     "The master of the Crystarium's tower. Back from Eulmore, he is plainly shaken by his time away from the tower and could not describe his meeting with Vauthry.",
     ["M585h", "M594e", "M605e"], ["The Exarch", "The enigmatic figure"]),
   P(S606, None, "main", "The Crystal Exarch",
     "The master of the Crystarium's tower. When a host of sin eaters advanced on the city, he raised a barrier around it, and it held.",
     ["M606a", "M606c", "M606d"], ["The Exarch", "The enigmatic figure"]),
   P(S609, None, "main", "The Crystal Exarch",
     "The master of the Crystarium's tower, plainly burdened by the sacrifices made to restore the balance. He believes Vauthry has mastered a way to enslave minds, and that the sin eaters are his to command.",
     ["M609i", "M609b", "M609c", "M609a"], ["The Exarch", "The enigmatic figure"]),
   P(S618, None, "main", "The Crystal Exarch",
     "The master of the Crystarium's tower. To Emet-Selch, who claims to have shaped the nation that built it and had a hand in Allag, he declared himself the adjudicator of the history the Ascian trifled with, "
     "and vowed that the history which led here will be unwritten.",
     ["M618f", "M618h", "M618g", "M618i"], ["The Exarch", "The enigmatic figure"]),
 ],
 "loc-crystarium": [
   P(S606, None, "main", "The Crystarium",
     "A city under the Crystal Exarch's protection. A host of sin eaters advanced on it, and his barrier held, but in Lakeland its own guards turned into sin eaters and attacked Lyna and her people.",
     ["M606a", "M606c", "M606d", "M606e", "M606i"]),
   P(S607, None, "main", "The Crystarium",
     "A city under the Crystal Exarch's protection, which held against a host of sin eaters at grievous cost. Its healers struggle with the wounded, and from Eulmoran airships Lord Vauthry called its losses divine retribution for its defiance.",
     ["M606c", "M606d", "M607a", "M607f"]),
 ],
 "char-lyna": [
   P(S606, None, "main", "Lyna",
     "A leader of the Crystarium's forces, who fought the sin eaters' host in Lakeland with her people. Her own guards turned into sin eaters and turned on her, and Thancred was injured protecting her.",
     ["M606i", "M606e", "M606f", "M606g"], ["Captain Lyna"]),
   P(S607, None, "main", "Lyna",
     "Captain of the Crystarium's guard. After her own soldiers turned into sin eaters in Lakeland, she blames herself for those she failed to protect; she says the war is far from over, then collapsed.",
     ["M607i", "M606f", "M607d", "M607c", "M607e"], ["Captain Lyna"]),
   P(S608, None, "main", "Lyna",
     "Captain of the Crystarium's guard, who collapsed after the sin eaters' assault. She asked you to look in on Thancred and Minfilia, who risked themselves for her.",
     ["M607i", "M607e", "M608a"], ["Captain Lyna"]),
 ],
 "char-vauthry": [
   P(S585, None, "main", "Vauthry",
     "A lord of Eulmore, who has invited the Crystal Exarch there to discuss the recent conflict at Lydha Lran. Alisaie calls it obviously a trap.",
     ["M585g"], ["Lord Vauthry"]),
   P(S594, None, "main", "Vauthry",
     "The lord of Eulmore. He told the Crystal Exarch that the sin eaters exist to unite the world under his dominion, and tried to enthrall him. "
     "By his decree Rak'tika falls under Eulmore, with the Children of the Everlasting Dark given authority over the forest.",
     ["M594d", "M594e", "M594c", "M594f"], ["Lord Vauthry"]),
   P(S607, None, "main", "Vauthry",
     "The lord of Eulmore, who would unite the world under his dominion through the sin eaters. After their assault on the Crystarium he called its losses divine retribution, "
     "offering himself as a benevolent savior and claiming the sin eaters regard him and his as kin.",
     ["M594d", "M607f", "M607g", "M607h"], ["Lord Vauthry"]),
   P(S609, None, "main", "Vauthry",
     "The lord of Eulmore. The Crystal Exarch believes he has mastered a technique to enslave the minds of others, which he tried on the Exarch, and that the sin eaters are his to command.",
     ["M594e", "M609b", "M609c"], ["Lord Vauthry"]),
 ],
 "org-lightwardens": [
   P(S585, None, "main", "The Lightwardens",
     "Wardens of the Light. You struck down those of Lakeland and Il Mheg; the Wardens of Kholusia, Amh Araeng and Rak'tika remain, their whereabouts unknown.",
     ["M583c", "M585l", "M585d"]),
   P(S595, None, "main", "The Lightwardens",
     "Wardens of the Light. Those of Lakeland and Il Mheg are slain; Kholusia's, Amh Araeng's and Rak'tika's remain. Y'shtola believes Eulmore's soldiers are in Rak'tika to protect its Lightwarden.",
     ["M585l", "M585d", "M595a"]),
   P(S605, None, "main", "The Lightwardens",
     "Wardens of the Light, of which Lakeland's, Il Mheg's and Rak'tika's are slain. Their light was not negated but absorbed into you, and with each Warden you defeat the danger grows. Eulmore has sent soldiers to defend the rest.",
     ["M603f", "M605a", "M605c", "M605m"]),
   P(S620, None, "main", "The Lightwardens",
     "Wardens of the Light, three of them slain, whose light is absorbed into you. Ryne, with the Oracle's power, can now track them, and senses one in Amh Araeng.",
     ["M605a", "M620i", "M620j"]),
 ],
 # -- The Scions
 "char-thancred": [
   P(S587, None, "main", "Thancred",
     "A Scion who travels with you and the girl Minfilia in Norvrandt. He struggles to accept, she says, that she is not the Minfilia he lost.",
     ["C31", "M585e", "M587i"]),
   P(S600, None, "main", "Thancred",
     "A Scion who travels with the girl Minfilia. He fought Eulmoran soldiers at the border of Yx'Maja, then struck General Ran'jit down into the depths of the Great Pyramid of Ux'ner.",
     ["C31", "M598e", "M600f"]),
   P(S606, None, "main", "Thancred",
     "A Scion who watches over the girl Minfilia. When the Crystarium's guards turned into sin eaters in Lakeland, he was injured protecting Lyna.",
     ["C31", "M606e", "M606g"]),
   P(S608, None, "main", "Thancred",
     "A Scion who watches over the girl Minfilia. A sin eater dealt him a serious injury as he protected Lyna, but the healers have done wonders, and he promised a wounded guard to carry his message to the Crystal Exarch.",
     ["C31", "M608b", "M608e", "M608g"]),
   P(S613, None, "main", "Thancred",
     "A Scion escorting the girl Minfilia to Nabaath Areng. He keeps his hopes for her to himself, unwilling to shackle her again.",
     ["C31", "M610c", "M613g"]),
   P(S615, None, "main", "Thancred",
     "A Scion escorting the girl Minfilia. He told Magnus that he once robbed a young girl of her family, and refuses to let her legacy die; Urianger says his heart is in turmoil.",
     ["C31", "M615e", "M615f", "M615h"]),
   P(S616, None, "main", "Thancred",
     "A Scion who carries the girl Minfilia's hopes and his own guilt. He relies on preparation and tools such as sundrops to compensate for a condition.",
     ["C31", "M615f", "M616d", "M616e"]),
   P(S619, None, "main", "Thancred",
     "A Scion who watches over the girl Minfilia. When Ran'jit toppled your trolley, he left her in your hands and held the general off until he retreated, then collapsed, injured.",
     ["C31", "M619k", "M619h", "M619i"]),
   P(S620, None, "main", "Thancred",
     "A Scion, found at death's door after holding off Ran'jit. He told the girl who went by Minfilia that she is family, and gave her a name of her own: Ryne.",
     ["C31", "M620o", "M620k", "M620m", "M620n"]),
 ],
 "char-urianger": [
   P(S582, None, "main", "Urianger",
     "A Scion with you in Il Mheg. While you go to face its Lightwarden, he and the others mean to obstruct the trespassers closing in.",
     ["C31", "M580g", "M582g"]),
   P(S586, None, "main", "Urianger",
     "A Scion bound with you for the Rak'tika Greatwood. At Fort Jobb he found the tablet the Crystal Exarch sought for Y'shtola, written in the script of Ronka.",
     ["C31", "M585e", "M586e", "M586f"]),
   P(S594, None, "main", "Urianger",
     "A Scion who has deciphered the tablet with Y'shtola. She has grown exasperated with his secrets, and confronted him over the Eighth Umbral Calamity he claimed to have seen.",
     ["C31", "M591f", "M594b", "M594a"]),
   P(S614, None, "main", "Urianger",
     "A Scion escorting the girl Minfilia. In Twine he mended the cracks in a Talos's aether network, but found its core will not stir.",
     ["C31", "M614b", "M614c", "M614d"]),
   P(S618, None, "main", "Urianger",
     "A Scion who readied Twine's Talos. When the girl Minfilia broke down, he confessed that it was he who set the Oracle on her path to this world.",
     ["C31", "M618c", "M618d", "M618e"]),
   P(S619, None, "main", "Urianger",
     "A Scion who confessed he set the Oracle on her path. He stayed behind in the Hills of Amber to tell Alisaie and the others of your progress.",
     ["C31", "M618e", "M619b"]),
   P(S620, None, "main", "Urianger",
     "A Scion who confessed he set the Oracle on the girl's path. He called Alisaie and the others in time to find Thancred at death's door, and knew the name Thancred chose for her, Ryne, as \"blessing\" in Fae.",
     ["C31", "M618e", "M620o", "M620m"]),
 ],
 "char-yshtola": [
   P(S587, None, "main", "Y'shtola",
     "A Scion living in the Rak'tika Greatwood as Master Matoya, after the custom of the Night's Blessed. She leads them since sin eaters razed their largest settlement. "
     "She lost her trust in the Crystal Exarch, and the Light suffusing you made you a stranger to her sight.",
     ["C31", "M587a", "M587b", "M587d", "M587c", "M587e", "M587f"]),
   P(S591, None, "main", "Y'shtola",
     "A Scion who lives among the Night's Blessed as Master Matoya and drove back the sin eaters. With Urianger she has deciphered the tablet, which makes the Scions' next course clear.",
     ["C31", "M587a", "M588a", "M591f", "M591g"]),
   P(S594, None, "main", "Y'shtola",
     "A Scion who leads the Night's Blessed as Master Matoya. Exasperated by Urianger's secrets, she confronted him, fearing the light from the Wardens was not negated at all. Eulmore now claims the forest.",
     ["C31", "M587d", "M594b", "M594a", "M594j", "M594c"]),
   P(S600, None, "main", "Y'shtola",
     "A Scion who lived among the Night's Blessed as Master Matoya. In the Great Pyramid of Ux'ner she leapt into the void after the antidote for the poisoned Blessed, tossed it to you, and vanished into the dark.",
     ["C31", "M587a", "M600c", "M600e"]),
   P(S602, None, "main", "Y'shtola",
     "A Scion who lived among the Night's Blessed as Master Matoya. Leaping after an antidote, she invoked Flow, which carried her soul into the Lifestream; Emet-Selch plucked her out, and she admits it was reckless.",
     ["C31", "M587a", "M600e", "M602e", "M602c", "M602f"]),
   P(S604, None, "main", "Y'shtola",
     "A Scion who lived among the Night's Blessed as Master Matoya. With the Lightwarden of Rak'tika slain, she refused the Blessed's worship and told them the Scions must all go on together.",
     ["C31", "M587a", "M604a", "M604e", "M604f"]),
   P(S605, None, "main", "Y'shtola",
     "A Scion who lived two years among the Night's Blessed as Master Matoya. She warned you that the Lightwarden's light was absorbed into you rather than negated, and that each Warden you defeat raises the danger.",
     ["C31", "M605j", "M605a", "M605b", "M605c"]),
   P(S609, None, "main", "Y'shtola",
     "A Scion who sees the Lightwardens' light gathering in you. She has gone east with Alisaie and Alphinaud to draw the Eulmoran army away from Amh Araeng's western route.",
     ["C31", "M605a", "M609g"]),
   P(S620, None, "main", "Y'shtola",
     "A Scion who sees the Lightwardens' light gathering in you. She would not have the girl who went by Minfilia walk in another's shadow, and called for a name of her own.",
     ["C31", "M605a", "M620l"]),
 ],
 "char-alphinaud": [
   P(S584, None, "main", "Alphinaud",
     "A young Scion, back in the Crystarium after Il Mheg. He confronted Emet-Selch: the Ascians have labored since time immemorial to rejoin the thirteen shards, at the cost of countless lives.",
     ["C31", "M584a", "M584d"]),
   P(S585, None, "main", "Alphinaud",
     "A young Scion who rules out any alliance with the Ascians. He will hunt Kholusia's Lightwarden, first escorting the Crystal Exarch to Eulmore.",
     ["C31", "M585b", "M585m", "M585j"]),
   P(S605, None, "main", "Alphinaud",
     "A young Scion who escorted the Crystal Exarch to Eulmore and back. Reunited with the others, he heard the Rak'tika Warden is slain, and worries for the shaken Exarch.",
     ["C31", "M585j", "M605d", "M605e"]),
   P(S609, None, "main", "Alphinaud",
     "A young Scion. With Alisaie and Y'shtola he has gone east to draw the Eulmoran army away while you take the western route through Amh Araeng.",
     ["C31", "M609g"]),
 ],
 "char-alisaie": [
   P(S585, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. She has taken on the search for Amh Araeng's Lightwarden, knowing the lie of the land, and suspects Lord Vauthry's invitation of a trap.",
     ["C31", "M585i", "M585g"]),
   P(S606, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion, back from Amh Araeng. When sin eaters advanced on the Crystarium, she helped you activate the anchors of its barrier, unsettled that they came at all with the darkness restored.",
     ["C31", "M606b", "M606j", "M606d"]),
   P(S607, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. After the sin eaters' assault on the Crystarium, she has been helping move the wounded.",
     ["C31", "M606a", "M607a"]),
   P(S609, None, "main", "Alisaie",
     "Alphinaud's twin and a Scion. She proposed the plan by which she, her brother and Y'shtola went east to draw off the Eulmoran army while you take the western route to Nabaath Areng.",
     ["C31", "M609g"]),
 ],
 "char-ryne": [
   P(S583, None, "main", "Minfilia of the First",
     "A girl who goes by Minfilia and travels with Thancred and the Scions. General Ran'jit trained her as an Oracle in Eulmore and wants her back, but she refuses to return and drew her weapons to protect her friends.",
     ["M583g", "M583h"], ["Minfilia"]),
   P(S587, None, "main", "Minfilia of the First",
     "A girl who goes by Minfilia, trained as an Oracle in Eulmore by Ran'jit, who now travels with the Scions. She tells Thancred again that she is not the Minfilia he lost.",
     ["M583g", "M583h", "M587i"], ["Minfilia"]),
   P(S590, None, "main", "Minfilia of the First",
     "A girl who goes by Minfilia, trained as an Oracle in Eulmore, and not the Minfilia Thancred lost. The Light's corruption does not touch her as it does others, and Runar wonders if she is the Minfilia descended from the Oracle.",
     ["M583g", "M587i", "M590d", "M590e"], ["Minfilia"]),
   P(S591, None, "main", "Minfilia of the First",
     "A girl who goes by Minfilia, trained as an Oracle and untouched by the Light's corruption. Moved by the Night's Blessed, she vowed to bring back the dark.",
     ["M583g", "M590d", "M588e", "M591d"], ["Minfilia"]),
   P(S608, None, "main", "Minfilia of the First",
     "A girl who goes by Minfilia, trained as an Oracle in Eulmore. She blames her own carelessness for Thancred's injury when the Crystarium's guards turned into sin eaters.",
     ["M583g", "M606e", "M608c"], ["Minfilia"]),
   P(S609, None, "main", "Minfilia of the First",
     "A girl who goes by Minfilia, trained as an Oracle. She means to travel to Amh Araeng to become one with the Oracle of Light and find the Lightwardens; Emet-Selch calls her a reincarnation, "
     "and says one of them must consume the other. She wants to be strong enough to face her destiny.",
     ["M583g", "M609d", "M609e", "M609f", "M609h"], ["Minfilia"]),
   P(S612, None, "main", "Minfilia of the First",
     "A girl who goes by Minfilia, bound for Nabaath Areng to become one with the Oracle. Magnus of Twine called the journey fruitless, and she believes he thinks her weak.",
     ["M609d", "M610c", "M612f", "M612e"], ["Minfilia"]),
   P(S618, None, "main", "Minfilia of the First",
     "A girl who goes by Minfilia, bound for Nabaath Areng to become one with the Oracle. She broke down, sure that Thancred wishes her dead so the other could return, and Urianger confessed he set the Oracle on her path.",
     ["M609d", "M610c", "M618d", "M618e"], ["Minfilia"]),
   P(S619, None, "main", "Minfilia of the First",
     "A girl who goes by Minfilia, about to meet the original Oracle. Ran'jit, who trained her, raged that he sought out her successors again and again; she answered that the Scions are everything to her.",
     ["M619c", "M619f", "M619g", "M619j"], ["Minfilia"]),
   P(S620, None, "main", "Ryne",
     "The girl who went by Minfilia. At Nabaath Areng the Oracle warned that the power she sought has a price, then gave her a new path of her own; she can now track the Lightwardens. "
     "Thancred, who calls her family, named her Ryne, \"blessing\" in Fae, and the Scions welcomed her aboard.",
     ["M620e", "M620h", "M620j", "M620k", "M620m", "M620n"], ["Minfilia"]),
 ],
 "char-minfilia": [
   P(S619, None, "main", "Minfilia",
     "Once leader of the Scions, revered in this world as the Oracle of Light, who stopped the Flood at Nabaath Areng. "
     "Urianger confesses he set her on her path here, and the girl who bears her name is about to meet her: the original Oracle, the real Minfilia.",
     ["M609d", "M618e", "M619c", "M619j"], ["the Antecedent", "the Word of the Mother"]),
   P(S620, None, "main", "Minfilia",
     "Once leader of the Scions, revered in this world as the Oracle of Light. An echo at Nabaath Areng showed her staying the Flood, her power all but spent. Meeting the girl who bears her name, she warned of the power's price "
     "and gave her a new path of her own; then she was gone, though the girl still feels her.",
     ["M620b", "M620f", "M620g", "M620e", "M620h", "M620q"], ["the Antecedent", "the Word of the Mother"]),
 ],
 # -- Rak'tika
 "org-nights-blessed": [
   P(S586, None, "main", "The Night's Blessed",
     "Worshipers of the Dark, whose most devout fled to the Rak'tika Greatwood as the faith of the Light waned. Their standards hang in the ruined church at Fort Jobb, and Y'shtola lives among them.",
     ["M585f", "M586b", "M586c"]),
   P(S587, None, "main", "The Night's Blessed",
     "Worshipers of the Dark in the Rak'tika Greatwood, who take their forebears' names to shield their true selves from the Light. Two years ago sin eaters razed their largest settlement and killed many priests; "
     "Y'shtola, as Master Matoya, now leads them.",
     ["M586b", "M587b", "M587c", "M587d"]),
   P(S589, None, "main", "The Night's Blessed",
     "Worshipers of the Dark in Slitherbough, led by Y'shtola as Master Matoya. They began with those left homeless by the Flood, and found faith that the souls of the dead may find peace in the sunless sea above.",
     ["M587d", "M589c", "M589d", "M589e"]),
   P(S594, None, "main", "The Night's Blessed",
     "Worshipers of the Dark in Slitherbough. Eulmore has claimed their forest: they must join the Children of the Everlasting Dark and swear to Eulmore, or be treated as traitors.",
     ["M589c", "M594c", "M594h", "M594g"]),
   P(S604, None, "main", "The Night's Blessed",
     "Worshipers of the Dark in Slitherbough. Poisoned by Eulmore, they were saved by the antidote; when the night sky returned, the Eulmorans fled and the Children retreated. Runar hails the Scions as the Warriors of Darkness.",
     ["M600c", "M601e", "M604c", "M604d"]),
 ],
 "char-runar": [
   P(S588, None, "main", "Runar",
     "One of the Night's Blessed in Slitherbough, who keeps their rites. He credits Master Matoya with driving the sin eaters back after their priests were slain, and cleansed you of the Light's impurity.",
     ["M588a", "M588b", "M588c", "M588d"]),
   P(S590, None, "main", "Runar",
     "One of the Night's Blessed in Slitherbough. He would not send his people after the heartstone of Toddia, slain by sin eaters, for fear of corruption, and wonders if Minfilia is the one descended from the Oracle.",
     ["M588c", "M590a", "M590c", "M590e"]),
   P(S595, None, "main", "Runar",
     "One of the Night's Blessed in Slitherbough, who held Toddia's funeral. With Eulmore claiming the forest, he swore to keep the Blessed safe while the Scions are away.",
     ["M591a", "M594h", "M595c"]),
   P(S601, None, "main", "Runar",
     "One of the Night's Blessed, who held up the Eulmorans' procession through Yx'Maja. Found wounded and poisoned, he was cured in Fanow with the antidote.",
     ["M601d", "M601g", "M601h"]),
   P(S604, None, "main", "Runar",
     "One of the Night's Blessed, who held up the Eulmorans in Yx'Maja. He hailed the Scions as the Bringers of Shadow and the Warriors of Darkness, and swore to hold them in his heart.",
     ["M601d", "M604d", "M604g"]),
 ],
 "org-children-of-the-everlasting-dark": [
   P(S592, None, "main", "The Children of the Everlasting Dark",
     "A radical faction of Dark worshipers who kill, claiming to cleanse their victims of sin. They hold a monolith Y'shtola needs, and have been breeding venomous spiders in greater numbers.",
     ["M592c", "M592d", "M592e"]),
   P(S594, None, "main", "The Children of the Everlasting Dark",
     "A radical faction of Dark worshipers based at Woven Oath. Lord Vauthry has given them authority over the forest, and the Night's Blessed must join them or be treated as traitors.",
     ["M592d", "M593a", "M594f", "M594h"]),
   P(S600, None, "main", "The Children of the Everlasting Dark",
     "A radical faction of Dark worshipers, given authority over the forest by Lord Vauthry. They brewed the toxin with which Eulmore's soldiers poisoned the Blessed.",
     ["M592d", "M594f", "M600c"]),
   P(S604, None, "main", "The Children of the Everlasting Dark",
     "A radical faction of Dark worshipers who served Eulmore in the Greatwood. With the night sky restored they have retreated to Woven Oath.",
     ["M592d", "M594f", "M604c"]),
 ],
 "char-almet": [
   P(S596, None, "main", "Almet",
     "Chieftainess of Fanow in Yx'Maja. Recognizing the seal of Ronka, she welcomed you as allies of Ronka, whom her people have awaited for three thousand years. These are troubled times for them.",
     ["M596e", "M596c", "M596d", "M596f"]),
   P(S597, None, "main", "Almet",
     "Chieftainess of the Viis of Fanow. She does not know the Lightwarden's lair, but will open the way to Rak'tika Falls through the Qitana Ravel, starting at the K'mul Astropolis.",
     ["M596e", "M597c", "M597f"]),
 ],
 "org-viis": [
   P(S597, None, "main", "The Viis",
     "The people of Fanow in Yx'Maja, descendants of the palace guard of Ronka's last emperor. Bidden to keep Ronka's secrets and await its allies, they take the Scions for those allies.",
     ["M597a", "M597b", "M596c"]),
   P(S600, None, "main", "The Viis",
     "Descendants of the palace guard of Ronka's last emperor, allies of the Scions. Almet's sisters held off General Ran'jit while you opened the Qitana Ravel.",
     ["M597a", "M596c", "M600b"]),
   P(S604, None, "main", "The Viis",
     "Descendants of the palace guard of Ronka's last emperor, who helped the Scions reach the Lightwarden of Rak'tika. They remain to guard Ronka's ruins, so its secrets stay from the wrong hands.",
     ["M597a", "M604a", "M604b"]),
 ],
 # -- Amh Araeng
 "char-magnus": [
   P(S611, None, "main", "Magnus",
     "A man of Twine, the only one with full knowledge of the trolley that once ran through the Hills of Amber.",
     ["M611e", "M611f"]),
   P(S612, None, "main", "Magnus",
     "The man of Twine who knows the trolley best. He told you there is nothing left in Nabaath Areng, called the journey fruitless and the trolley impossible, and refused to say more.",
     ["M611e", "M612c", "M612f", "M612d"]),
   P(S615, None, "main", "Magnus",
     "The man of Twine who knows the trolley best. He returned seven years ago with his wife, Agna, after sin eaters killed their son, Skuli; Agna died when her mine collapsed as she dug for Talos stone, "
     "and Magnus has not been the same since.",
     ["M611e", "M613e", "M613f", "M615d", "M615b", "M615c"]),
   P(S618, None, "main", "Magnus",
     "The man of Twine who knows the trolley best, widowed when his wife, Agna, died in a mine. Shown the leonine she engraved for him and their son, he gave it up for the Talos, which now works.",
     ["M615b", "M617f", "M618a", "M618b", "M618c"]),
 ],
 # -- Garlemald
 "char-gaius": [
   P(S605, None, "main", "Gaius",
     "The Black Wolf, a former imperial legatus who now hunts Ascians. In Garlemald, he and Estinien seek their next target; he has learned that a general vanished from the Ghimlyt Dark, "
     "and since Elidibus needs no new host, he asks who would.",
     ["M605l", "M605k", "M605h", "M605i"], ["the Black Wolf", "Shadowhunter"]),
 ],
 "char-estinien": [
   P(S605, None, "main", "Estinien",
     "A dragoon who saved you at the front and now works with Gaius in Garlemald, urging him to hasten their search for their next target.",
     ["M605l", "M605k"]),
 ],
}

# ---- Arc recaps ---------------------------------------------------------------------------------------------------
N1, N2, N3, N4, N5, N6, N7, N8 = ("The Throne of Lyhe Ghiah", "The Ascian's Offer", "Darkness in the Greatwood",
                                  "Allies of Ronka", "The Warden of the Greatwood", "The Siege of the Crystarium",
                                  "The Road to Nabaath Areng", "The Oracle's Crossroads")
PRES.update({
 "evt-the-throne-of-lyhe-ghiah": [
   P(S580, None, "main", N1,
     "To break the seal on Lyhe Ghiah, the castle in Il Mheg's lake, you need four relics. The Nu Mou, unable to deal with their fallen monarch, entrusted you with the stone scepter; "
     "Titania, they say, is a title, and its bearer has become a sin eater. Only the crystal shoes remain, and Seto, leader of the amaro, refuses them out of concern for you.",
     ["M580a", "M580b", "M580c", "M580d", "M580e", "M580g"]),
   P(S581, None, "main", N1,
     "You hold three of the four relics needed to enter Lyhe Ghiah and face its fallen king. Seto, leader of the amaro, keeps the crystal shoes, for he can no longer bear to see men fight and die. "
     "As a trial he lured sin eaters out with his voice, as he once did with an old friend, and you prevailed, but he asks a favor first.",
     ["M580a", "M580d", "M581a", "M581c", "M581d", "M581e"]),
   P(S582, None, "main", N1,
     "Seto, leader of the amaro, gave you the crystal shoes, the last relic for Lyhe Ghiah, after you recovered his medallion. It was a gift from his old friend Ardbert, blamed for the Flood, "
     "and Seto says your soul strongly resembles his. Now an old mortal, Ran'jit, closes on Il Mheg, and the others go to delay him while you face the Lightwarden.",
     ["M582a", "M582b", "M582c", "M582d", "M582e", "M582h", "M582g"]),
   P(S583, None, "main", N1,
     "With all four relics you broke the seal on Lyhe Ghiah and defeated Titania, the Lightwarden of Il Mheg, restoring night to the land. Feo Ul took the throne in your stead and drove the Eulmoran army from Lydha Lran. "
     "Its general, Ran'jit, who trained Minfilia as an Oracle, withdrew, vowing that all who stand with the Warrior of Darkness will face justice.",
     ["M583a", "M583c", "M583e", "M583g", "M583i"]),
 ],
 "evt-the-ascians-offer": [
   P(S584, None, "main", N2,
     "Back in the Crystarium after Il Mheg, a man introduced himself as Solus, founding father of the Garlean Empire, then as Emet-Selch, an Ascian. He blames you for upsetting a Rejoining, "
     "and offers cooperation in your hunt for the Lightwardens. Later Ardbert's shade told you an Ascian in white had urged his world toward the Rejoining, though the Flood was the Ascians' own making.",
     ["M584a", "M584b", "M584c", "M584e", "M584f", "M584g", "M584h"]),
   P(S585, None, "main", N2,
     "Emet-Selch, the Ascian who revealed himself in the Crystarium, renewed his offer of partnership, and the Scions refused it. Three Lightwardens remain, so the Crystal Exarch divided your forces: "
     "Alisaie takes Amh Araeng, and Alphinaud escorts the Exarch to Eulmore at Lord Vauthry's invitation. You, Thancred, Minfilia and Urianger go to find Y'shtola in the Rak'tika Greatwood.",
     ["M585a", "M585b", "M585d", "M585c", "M585i", "M585j", "M585e"]),
   P(S586, None, "main", N2,
     "The Scions split up to hunt the three remaining Lightwardens, and the Crystal Exarch, bound for Eulmore, asked you to find a tablet at Fort Jobb for Y'shtola. In a ruined church hung with the standards of the Night's Blessed, "
     "worshipers of the Dark, you found it hidden in the altar. Urianger reads its engravings as the script of Ronka, whose capital stood in Rak'tika.",
     ["M585d", "M585f", "M586c", "M586f", "M586e"]),
   P(S587, None, "main", N2,
     "In the Rak'tika Greatwood you found Y'shtola living as Master Matoya among the Night's Blessed, who take their forebears' names to shield themselves from the Light. "
     "She has led them since sin eaters razed their largest settlement, and she lost her trust in the Crystal Exarch. Emet-Selch tags along as a mere observer, and Minfilia insists she is not the one Thancred lost.",
     ["M587a", "M587b", "M587c", "M587d", "M587e", "M587h", "M587i"]),
 ],
 "evt-darkness-in-the-greatwood": [
   P(S588, None, "main", N3,
     "In Slitherbough, home of the Night's Blessed, Y'shtola is deciphering the tablet from Fort Jobb. Runar says Master Matoya, as Y'shtola is known there, drove back the sin eaters after their priests were slain. "
     "He cleansed you and Minfilia of the Light's impurity and taught you their greeting, and Minfilia is starting to feel at home.",
     ["M588f", "M588a", "M588b", "M588c", "M588d", "M588e"]),
   P(S589, None, "main", N3,
     "While Y'shtola deciphers the tablet from Fort Jobb, you and Minfilia are earning your keep in Slitherbough. Watering its crops, you learned that the Night's Blessed began with those left homeless by the Flood. "
     "When no one could say where the souls of those reborn as sin eaters went, they found faith that the dead may find peace in the sunless sea above.",
     ["M588f", "M589a", "M589c", "M589d", "M589e"]),
   P(S590, None, "main", N3,
     "In Slitherbough the Night's Blessed mourn Toddia, a child slain by sin eaters, whose jade heartstone was lost; such stones guide the souls of the dead to peace in the dark. "
     "Minfilia, untouched by the Light's corruption as others are, helped you recover it. Runar wonders whether she is truly the Minfilia descended from the Oracle.",
     ["M590a", "M590b", "M590f", "M590d", "M590e"]),
   P(S591, None, "main", N3,
     "With Toddia's heartstone recovered, the Night's Blessed held her funeral, and you attended as honored guests. Moved by their hopes, Minfilia vowed to bring back the dark, and Thancred agreed. "
     "Afterwards Y'shtola and Urianger revealed that they have deciphered the Crystal Exarch's tablet, and that his gift makes the Scions' next course clear.",
     ["M591a", "M591b", "M591d", "M591e", "M591f", "M591g"]),
   P(S592, None, "main", N3,
     "Y'shtola has deciphered most of the tablet from Fort Jobb: written at the end of the Ronkan Empire, it tells how to prove oneself Ronka's ally. To finish it she needs a monolith held by the Children of the Everlasting Dark, "
     "radical Dark worshipers who kill to cleanse their victims of sin. You gathered bees and smoke bombs to lure them from their camp.",
     ["M592a", "M592b", "M592c", "M592d", "M592f"]),
   P(S593, None, "main", N3,
     "To finish the tablet, Y'shtola needed a monolith in Woven Oath, the settlement of the Children of the Everlasting Dark. Thancred's bees sent the Children running to save their spiders, "
     "and inside you found murals of heroes from the age of gods to the eve of the Flood. Ardbert recalled the researcher behind them, and Y'shtola now has all she needs.",
     ["M593a", "M593b", "M592e", "M593c", "M593d", "M593f"]),
   P(S594, None, "main", N3,
     "Back in Slitherbough, Y'shtola confronted Urianger over his secrets, fearing the Wardens' light was not negated at all. Then Eulmoran soldiers came, and a guard fell to poison. "
     "In Eulmore, Lord Vauthry tried to enthrall the Crystal Exarch, who vanished. Ran'jit proclaimed Rak'tika Eulmore's, gave the Children authority over the forest, and told the Night's Blessed to join them or be traitors.",
     ["M594b", "M594j", "M594k", "M594e", "M594c", "M594f", "M594h"]),
 ],
 "evt-allies-of-ronka": [
   P(S595, None, "main", N4,
     "Eulmore has claimed Rak'tika and given the Children of the Everlasting Dark authority over the forest, and Y'shtola believes its soldiers are there to protect the Lightwarden, so she means to slay it first. "
     "Following the tablet, you found the seal of Ronka beneath Lake Tusi Mek'ta, a medallion with the empire's owl insignia, while Runar swore to keep the Blessed safe.",
     ["M594c", "M594f", "M595a", "M595b", "M595e", "M595c"]),
   P(S596, None, "main", N4,
     "Bearing the seal of Ronka, which marks the allies of that ancient empire, you and the Scions entered Yx'Maja, where the Lightwarden presumably hides. Its guardians shot at you from the trees until Y'shtola showed the seal. "
     "In their village of Fanow, the chieftainess, Almet, welcomed you as allies of Ronka, awaited for three thousand years.",
     ["M595b", "M596a", "M596b", "M596c", "M596e", "M596d"]),
   P(S597, None, "main", N4,
     "In Fanow, the Viis, descendants of the palace guard of Ronka's last emperor, hail the Scions as the allies they were bidden to await. None of them knows the Lightwarden's lair, but Korille's mother once saw a sin eater the others revered. "
     "The tunnel to Rak'tika Falls has collapsed, so Almet will open a way through the Qitana Ravel, starting at the K'mul Astropolis.",
     ["M597a", "M597b", "M597c", "M597d", "M597e", "M597f"]),
   P(S598, None, "main", N4,
     "Almet of the Viis is opening the sealed way to Rak'tika Falls, where the Lightwarden may lair. At the Morning Stars, four monuments said to be keys to the Great Pyramid of Ux'ner, Y'shtola decoded a riddle calling for one statue to be suffused with aether. "
     "Then Cymet brought word that Eulmoran soldiers have entered Yx'Maja, and Thancred and Uimet are fighting them at the border.",
     ["M597f", "M598a", "M598b", "M598c", "M598d", "M598e"]),
   P(S599, None, "main", N4,
     "With Eulmoran soldiers in Yx'Maja, Almet and Y'shtola hurried you into the Great Pyramid of Ux'ner to open the way to the Qitana Ravel. Magic was blocked short of a sealed door until you returned a missing owl statuette to its altar. "
     "Almet warns that the last step is the most perilous.",
     ["M598d", "M599a", "M599b", "M599c", "M599d", "M599e"]),
   P(S600, None, "main", N4,
     "In the pyramid's final chamber Ran'jit barred the way, and the Viis sisters held him while you opened the Qitana Ravel. His adjutant offered an antidote for the Blessed their men had poisoned, but Ran'jit kicked him into a chasm. "
     "Y'shtola leapt after the antidote, tossed it to you and vanished into the dark, and Thancred struck Ran'jit down into the depths.",
     ["M600a", "M600b", "M600c", "M600g", "M600e", "M600f"]),
 ],
 "evt-the-warden-of-the-greatwood": [
   P(S601, None, "main", N5,
     "Y'shtola vanished into a pit whose depth the Viis have never measured, saving an antidote for the Night's Blessed poisoned by Eulmore. The Eulmorans and the Children have fled Yx'Maja. "
     "Thancred and Minfilia took the antidote to Slitherbough, and in Fanow you cured Runar, who had held up the Eulmorans' procession.",
     ["M600e", "M601a", "M601b", "M601e", "M601d", "M601h"]),
   P(S602, None, "main", N5,
     "The Viis caught Emet-Selch, the Ascian who has followed you, and learned he had plucked Y'shtola from the Lifestream, where her spell had carried her soul. With his aetherial lamp you found a spot that resonates with it, "
     "and he brought her back. The Ascians act for the greater good, he says, and Y'shtola would make ready to face the Lightwarden.",
     ["M602a", "M602c", "M602e", "M602d", "M602g", "M602h"]),
   P(S603, None, "main", N5,
     "Through the Qitana Ravel you reached Rak'tika Falls and slew its Lightwarden, and night returned to the Greatwood. In the Ravel, Emet-Selch claimed the world was sundered into thirteen reflections, "
     "the Ascians summoned Zodiark, and Hydaelyn rose to be his shackles. Y'shtola wonders whether it is true, and warns that your danger remains though you show no corruption.",
     ["M603f", "M603b", "M603d", "M603c", "M603h", "M603g"]),
   P(S604, None, "main", N5,
     "With the Lightwarden of Rak'tika slain, the Viis keep guarding Ronka's ruins, and the Eulmorans and the Children fled at the sight of the night sky. In Slitherbough, Runar hailed the Scions as the Warriors of Darkness. "
     "Y'shtola refused the Blessed's worship and said the Scions must all go on together, as Ardbert's shade watched.",
     ["M604a", "M604b", "M604c", "M604d", "M604e", "M604f", "M604h"]),
   P(S605, None, "main", N5,
     "Back at the Crystarium, Y'shtola warned you that the Lightwarden's light was not negated but absorbed into you, a danger that grows with each one. The Crystal Exarch, shaken by his time in Eulmore, could not describe his meeting with Vauthry. "
     "Meanwhile, in Garlemald, Gaius and Estinien learned that a general vanished from the Ghimlyt Dark.",
     ["M605a", "M605c", "M605e", "M605l", "M605h", "M605k"]),
 ],
 "evt-the-siege-of-the-crystarium": [
   P(S606, None, "main", N6,
     "A host of sin eaters advanced on the Crystarium, and you and Alisaie activated the anchors of the Crystal Exarch's barrier, which held. In Lakeland, Lyna's own guards turned into sin eaters, and Thancred was wounded protecting her. "
     "The battle was won, but Y'shtola finds the eaters too organized to act on instinct alone.",
     ["M606a", "M606j", "M606d", "M606e", "M606g", "M606h"]),
   P(S607, None, "main", N6,
     "The Crystarium held against a host of sin eaters, but its guards turned into eaters in Lakeland, and many died. As you helped Alisaie with the wounded, Captain Lyna blamed herself for those she failed, and collapsed. "
     "From Eulmoran airships Lord Vauthry called the tragedy divine retribution, offering himself as a benevolent savior.",
     ["M606d", "M606e", "M607a", "M607i", "M607d", "M607e", "M607f", "M607g"]),
   P(S608, None, "main", N6,
     "After the sin eaters' assault on the Crystarium, Lyna asked you to look in on Thancred, badly hurt by an eater, and Minfilia, who blames her own carelessness. The healers can barely keep up. "
     "A wounded guard asked that the Crystal Exarch hear he still believes in the Warrior of Darkness and in the Exarch, and Thancred gave his word.",
     ["M608a", "M608b", "M608c", "M608d", "M608f", "M608g"]),
   P(S609, None, "main", N6,
     "The Crystal Exarch believes Vauthry can enslave minds and commands the sin eaters. With the Lightwardens unfound, Minfilia means to go to Amh Araeng to become one with the Oracle of Light, and Emet-Selch says one must consume the other. "
     "Alisaie, Alphinaud and Y'shtola went east to draw off the Eulmorans while the rest of you take the western route.",
     ["M609b", "M609c", "M609d", "M609e", "M609f", "M609g"]),
 ],
 "evt-the-road-to-nabaath-areng": [
   P(S610, None, "main", N7,
     "Minfilia is bound for Nabaath Areng to become one with the Oracle of Light, with you, Thancred and Urianger. At Garik in the Hills of Amber you learned that the Flood crushed the mines around it. "
     "The ways down are a ruined gondola, a trolley locked behind a gate, or Eulmore's airship, and Thancred has seen no Eulmorans in the hills.",
     ["M609d", "M610c", "M610a", "M610b", "M610d", "M610e", "M610f"]),
   P(S611, None, "main", N7,
     "To reach Nabaath Areng, the Scions seek the trolley that ran through the Hills of Amber, but its gate opened only for the Talos, a hulking thing of stone that no one now operates. "
     "At the rail yard you caught two engineers who keep the trolley maintained. They say only Magnus knows its full workings, and lead you to Twine to meet him.",
     ["M610c", "M611a", "M611b", "M611c", "M611d", "M611e", "M611f"]),
   P(S612, None, "main", N7,
     "Minfilia needs the trolley to reach Nabaath Areng, and only Magnus of Twine knows it fully. Twine, which the trolley once filled with workers, now holds only the destitute and those with nowhere else to go. "
     "Magnus told you nothing is left in Nabaath Areng and refused to discuss the trolley, and Minfilia believes he thinks her weak.",
     ["M611e", "M612a", "M612b", "M612c", "M612d", "M612e"]),
   P(S613, None, "main", N7,
     "Magnus will not help Minfilia reach Nabaath Areng by trolley, so you asked the rest of Twine. Jeryk, repairing the rails, explained that no one now operates the Talos that once opened the gate. "
     "Magnus came back seven years ago with his wife, after sin eaters killed their son. Thancred, meanwhile, keeps his hopes for Minfilia to himself.",
     ["M613b", "M611b", "M611c", "M613e", "M613f", "M613g"]),
   P(S614, None, "main", N7,
     "The trolley to Nabaath Areng needs a working Talos to open its gate, and Jeryk showed you one Twine meant to repair. Urianger mended the cracks in its aether network with stones from the debitage, but its core will not stir. "
     "Twine once tried and failed to replace it, and Jeryk agreed to tell you why.",
     ["M611b", "M614a", "M614b", "M614c", "M614d", "M614f", "M614g"]),
   P(S615, None, "main", N7,
     "Twine's Talos needs a heart of special aether-conducting stone from the mines of the Hills of Amber. Magnus's wife, Agna, kept digging for it until her mine collapsed, and Magnus, who lost his son Skuli too, has not been the same. "
     "Thancred told him of a girl he once robbed of her family, and the two of you head for Nuvy's Leavings.",
     ["M614e", "M615a", "M615b", "M615c", "M615d", "M615e", "M615g"]),
 ],
 "evt-the-oracles-crossroads": [
   P(S616, None, "main", N8,
     "Twine's Talos needs a heart of rare stone if Minfilia is to reach Nabaath Areng, so you and Thancred went to the mine at Nuvy's Leavings. Guthjon named the stone leonine, but what remains lies too deep to dig. "
     "With Thancred's sundrops, you found the gold piece Guthjon lost, and he agreed to share a trade secret.",
     ["M615a", "M616a", "M616b", "M616c", "M616d", "M616f"]),
   P(S617, None, "main", N8,
     "Seeking leonine for Twine's Talos, you flushed rockworms called knockers from the mine at Nuvy's Leavings, since they reach crevices miners cannot. Thancred told you the Scions' Minfilia was a miner before she founded the Path of the Twelve. "
     "Then Guthjon found a large leonine engraved by Agna to Magnus and Skuli, carried off by knockers before anyone could reach her.",
     ["M616a", "M617a", "M617b", "M617c", "M617e", "M617f", "M617h"]),
   P(S618, None, "main", N8,
     "Thancred brought Magnus the leonine his late wife had engraved, Magnus gave it up, and Twine's Talos stirred to life. Minfilia broke down, sure Thancred wishes her dead so the other could return, and Urianger confessed he set the Oracle on her path. "
     "In the Crystarium, the Crystal Exarch told Emet-Selch that the history which led here will be unwritten.",
     ["M618a", "M618b", "M618c", "M618d", "M618e", "M618i"]),
   P(S619, None, "main", N8,
     "With the Talos repaired, Magnus sent you by trolley toward Nabaath Areng, while Urianger stayed to tell Alisaie and the others. Past the gate, Ran'jit toppled the trolley, raging that he trained Minfilia and sought out her successors. "
     "Thancred held him off, then collapsed as he retreated. Ahead waits the original Oracle, the real Minfilia.",
     ["M619a", "M619b", "M619k", "M619f", "M619h", "M619i", "M619c"]),
   P(S620, None, "main", N8,
     "At Nabaath Areng an echo showed the Oracle of Light staying the Flood and telling Ardbert his time had not come. She warned the girl that the power she seeks has a price, then gave her a new path of her own. "
     "Changed, she can track the Lightwardens, one of them in Amh Araeng, and Thancred named her Ryne, \"blessing\" in Fae.",
     ["M620b", "M620c", "M620e", "M620h", "M620i", "M620m", "M620n"]),
 ],
})

# ---- Relationships --------------------------------------------------------------------------------------------------
RELS = [
 ("rel-solus-revealed-as-emet-selch", "char-solus", "revealed-as", "char-emet-selch", S584, None, "main", ["M584b", "M584c"]),
 ("rel-emet-selch-member-of-ascians", "char-emet-selch", "member-of", "org-ascians", S584, None, "main", ["M584c", "M584d"]),
 ("rel-ranjit-opposes-scions", "char-ranjit", "opposes", "org-scions", S583, None, "main", ["M583f", "M583i"]),
 ("rel-ranjit-serves-vauthry", "char-ranjit", "serves", "char-vauthry", S594, None, "main", ["M594c", "M594f"]),
 ("rel-vauthry-controls-eulmore", "char-vauthry", "controls", "loc-eulmore", S594, None, "main", ["M594c", "M594d"]),
 ("rel-crystal-exarch-opposes-vauthry", "char-crystal-exarch", "opposes", "char-vauthry", S594, None, "main", ["M594d", "M594e"]),
 ("rel-children-of-the-everlasting-dark-serves-vauthry", "org-children-of-the-everlasting-dark", "serves", "char-vauthry", S594, None, "main", ["M594f", "M594h"]),
 ("rel-children-of-the-everlasting-dark-opposes-nights-blessed", "org-children-of-the-everlasting-dark", "opposes", "org-nights-blessed", S594, None, "main", ["M594h", "M594g"]),
 ("rel-yshtola-leads-nights-blessed", "char-yshtola", "leads", "org-nights-blessed", S587, S605, "main", ["M587d", "M587a"], ["M604f"]),
 ("rel-runar-member-of-nights-blessed", "char-runar", "member-of", "org-nights-blessed", S588, None, "main", ["M588c", "M588b"]),
 ("rel-almet-leads-viis", "char-almet", "leads", "org-viis", S597, None, "main", ["M596e", "M597a"]),
 ("rel-viis-allied-with-scions", "org-viis", "allied-with", "org-scions", S597, None, "main", ["M596c", "M597b"]),
 ("rel-estinien-allied-with-gaius", "char-estinien", "allied-with", "char-gaius", S605, None, "main", ["M605k", "M605h"]),
 ("rel-magnus-aids-scions", "char-magnus", "aids", "org-scions", S618, None, "main", ["M618b", "M618c"]),
 ("rel-feo-ul-leads-pixies", "char-feo-ul", "leads", "org-pixies", S583, None, "main", ["M583e", "M580b"]),
 ("rel-ryne-member-of-scions", "char-ryne", "member-of", "org-scions", S620, None, "main", ["M620k", "M620n"]),
]

ADJUST = {  # content_5_0_part1's relationships, ended here (unknown when this era lints alone)
 "rel-titania-member-of-sin-eaters": {"until": S583, "end": ["M583c"]},     # the Lightwarden is defeated
 "rel-titania-prisoner-of-pixies": {"until": S583, "end": ["M583a", "M583c"]},  # the seal is broken and Titania falls
 "rel-ryne-possessed-by-minfilia": {"until": S620, "end": ["M620h", "M620q"]},  # the Oracle gives her a path of her own and is gone
}

# ---- Arcs ------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-m1-the-throne-of-lyhe-ghiah", "evt-the-throne-of-lyhe-ghiah", S580, S583),
 ("arc-m2-the-ascians-offer", "evt-the-ascians-offer", S584, S587),
 ("arc-m3-darkness-in-the-greatwood", "evt-darkness-in-the-greatwood", S588, S594),
 ("arc-m4-allies-of-ronka", "evt-allies-of-ronka", S595, S600),
 ("arc-m5-the-warden-of-the-greatwood", "evt-the-warden-of-the-greatwood", S601, S605),
 ("arc-m6-the-siege-of-the-crystarium", "evt-the-siege-of-the-crystarium", S606, S609),
 ("arc-m7-the-road-to-nabaath-areng", "evt-the-road-to-nabaath-areng", S610, S615),
 ("arc-m8-the-oracles-crossroads", "evt-the-oracles-crossroads", S616, S620),
]

CASTS = {
 "evt-the-throne-of-lyhe-ghiah": [
   ("char-urianger", S580, ["M580g"]), ("char-seto", S580, ["M580d"]), ("char-titania", S580, ["M580b"]),
   ("char-ardbert", S582, ["M582b"]), ("char-thancred", S582, ["M582h"]), ("char-ranjit", S582, ["M582h"]),
   ("char-feo-ul", S583, ["M583e"]), ("char-ryne", S583, ["M583h"]), ("loc-eulmore", S583, ["M583h"]),
 ],
 "evt-the-ascians-offer": [
   ("char-emet-selch", S584, ["M584c"]), ("char-solus", S584, ["M584b"]), ("char-ardbert", S584, ["M584g"]),
   ("char-alphinaud", S584, ["M584d"]), ("char-crystal-exarch", S585, ["M585c"]), ("char-alisaie", S585, ["M585i"]),
   ("char-urianger", S586, ["M586e"]), ("org-nights-blessed", S586, ["M586c"]), ("char-yshtola", S587, ["M587a"]),
   ("char-ryne", S587, ["M587i"]),
 ],
 "evt-darkness-in-the-greatwood": [
   ("char-yshtola", S588, ["M588f"]), ("char-ryne", S588, ["M588e"]), ("char-runar", S588, ["M588c"]),
   ("org-nights-blessed", S588, ["M588b"]), ("char-thancred", S591, ["M591e"]), ("char-urianger", S591, ["M591f"]),
   ("org-children-of-the-everlasting-dark", S592, ["M592c"]), ("char-crystal-exarch", S594, ["M594e"]),
   ("char-vauthry", S594, ["M594d"]), ("char-ranjit", S594, ["M594c"]),
 ],
 "evt-allies-of-ronka": [
   ("char-yshtola", S595, ["M595a"]), ("char-runar", S595, ["M595c"]), ("org-children-of-the-everlasting-dark", S595, ["M594f"]),
   ("char-almet", S596, ["M596e"]), ("org-viis", S597, ["M597a"]), ("char-thancred", S598, ["M598e"]),
   ("char-ranjit", S600, ["M600a"]),
 ],
 "evt-the-warden-of-the-greatwood": [
   ("char-yshtola", S601, ["M601f"]), ("char-thancred", S601, ["M601e"]), ("char-ryne", S601, ["M601e"]),
   ("char-runar", S601, ["M601d"]), ("char-emet-selch", S602, ["M602c"]), ("org-ascians", S603, ["M603d"]),
   ("org-lightwardens", S603, ["M603f"]), ("org-viis", S604, ["M604b"]), ("char-crystal-exarch", S605, ["M605e"]),
   ("char-gaius", S605, ["M605i"]),
 ],
 "evt-the-siege-of-the-crystarium": [
   ("loc-crystarium", S606, ["M606a"]), ("char-alisaie", S606, ["M606b"]), ("char-crystal-exarch", S606, ["M606c"]),
   ("char-lyna", S606, ["M606e"]), ("char-thancred", S606, ["M606g"]), ("char-yshtola", S606, ["M606h"]),
   ("char-vauthry", S607, ["M607f"]), ("char-ryne", S608, ["M608c"]), ("char-emet-selch", S609, ["M609e"]),
   ("char-alphinaud", S609, ["M609g"]),
 ],
 "evt-the-road-to-nabaath-areng": [
   ("char-ryne", S610, ["M610c"]), ("char-thancred", S610, ["M610f"]), ("char-urianger", S614, ["M614c"]),
   ("char-magnus", S611, ["M611e"]),
 ],
 "evt-the-oracles-crossroads": [
   ("char-thancred", S616, ["M616d"]), ("char-magnus", S617, ["M617f"]), ("char-ryne", S618, ["M618d"]),
   ("char-urianger", S618, ["M618e"]), ("char-emet-selch", S618, ["M618f"]), ("char-crystal-exarch", S618, ["M618i"]),
   ("char-ranjit", S619, ["M619f"]), ("char-minfilia", S619, ["M619c"]), ("char-ardbert", S620, ["M620c"]),
   ("org-lightwardens", S620, ["M620i"]),
 ],
}

ARC_NOTES = {
 "arc-m1-the-throne-of-lyhe-ghiah": "MSQ #580 *The Elder's Answer* to #583 *Acht-la Ormh Inn*: the last two relics (the Nu Mou's scepter, M580a; Seto's crystal shoes, M582e), "
   "Titania's defeat and Feo Ul's succession (M583c, M583e), ending as Ran'jit withdraws from Il Mheg (M583i). It opens on the era's first step, so its first recap restates the relic hunt the previous era began.",
 "arc-m2-the-ascians-offer": "MSQ #584 *The Wheel Turns* to #587 *Into the Dark*: Emet-Selch's reveal and offer (M584c, M585a), the Exarch's division of forces (M585c), "
   "the Fort Jobb tablet (M586f) and the reunion with Y'shtola as Master Matoya (M587a). Ends where the Rak'tika story settles into Slitherbough.",
 "arc-m3-darkness-in-the-greatwood": "MSQ #588 *A Day in the Neighborhood* to #594 *An Unwanted Proposal*: life among the Night's Blessed, Toddia's funeral (M591a), the tablet and Woven Oath (M591f, M593f), "
   "ending on Eulmore's claim to Rak'tika and Vauthry's attempt on the Exarch (M594c, M594e).",
 "arc-m4-allies-of-ronka": "MSQ #595 *Put to the Proof* to #600 *Legend of the Not-so-hidden Temple*: the seal of Ronka (M595e), the Viis (M596c, M597a) and the pyramid (M598b), "
   "ending with Y'shtola's fall and Ran'jit's (M600e, M600f).",
 "arc-m5-the-warden-of-the-greatwood": "MSQ #601 *The Aftermath* to #605 *Out of the Wood*: Runar's cure (M601h), Y'shtola's rescue (M602c), the Lightwarden of Rak'tika and Emet-Selch's tale (M603f, M603d), "
   "the Blessed's farewell (M604f), ending on the absorbed-light warning and the Garlemald scene (M605a, M605h). Estinien, who appears only at #605, is in the entity records.",
 "arc-m6-the-siege-of-the-crystarium": "MSQ #606 *When It Rains* to #609 *The Best Way Out*: the sin eaters' assault and the turned guards (M606e), Vauthry's broadcast (M607f), "
   "ending on the Oracle plan and the party's split for Amh Araeng (M609d, M609g).",
 "arc-m7-the-road-to-nabaath-areng": "MSQ #610 *Free Trade* to #615 *The Truth Hurts*: Garik, the trolley and the Talos (M610d, M611b), Magnus's refusal (M612d) and grief (M615b), "
   "ending as you and Thancred set out for Nuvy's Leavings. Its name avoids the later quest titles of Amh Araeng.",
 "arc-m8-the-oracles-crossroads": "MSQ #616 *A Convenient Distraction* to #620 *Crossing Paths*: the leonine (M617f), the Talos and Urianger's confession (M618c, M618e), Ran'jit at the gate (M619k), "
   "and the Oracle's echo and the naming of Ryne (M620h, M620n). Its name keeps clear of #620's title.",
}

DECISIONS = [
 "**Eight arcs (m1–m8)** cover every step from #580 to #620 without sharing steps; each is 4–7 steps long.",
 "**Solus → Emet-Selch** follows the Marques → Cid pattern: `char-solus` gets a closing presentation at #584, `rel-solus-revealed-as-emet-selch` from #584, and `char-emet-selch` carries \"Solus\" as an alias. "
 "\"Emet-Selch\" appears only from #584, the first quest where the name is spoken (earlier pages show it only in speaker tags).",
 "**The girl called Minfilia** is `char-ryne`, displayed as \"Minfilia of the First\" (as content_5_0_part1 names her) with alias \"Minfilia\" until #620, then as \"Ryne\" with \"Minfilia\" as an alias; texts say \"the girl Minfilia\" to keep her apart from `char-minfilia`.",
 "**The Oracle of Light** is `char-minfilia`, as in content_5_0_part1 (`rel-ryne-possessed-by-minfilia`, ended here at #620, where the Oracle gives the girl her own path and is gone); no alias, since \"The Oracle of Light\" is #568's title.",
 "**Leaders as relationships:** Y'shtola `leads` the Night's Blessed from #587 (commanding role) until #605 (she leaves with the Scions, M604f); Almet `leads` the Viis; Ran'jit `serves` Vauthry from #594 (his decree).",
 "**Left out as entities** (named in text only): the Nu Mou and Wyd Aenc, Rispa and the amaro, Oul Sigun, Toddia, Korille, Uimet and Cymet, Jeryk, Thaffe, Guthjon, Agna and Skuli, the Mord of Garik, Hardyss, "
 "the researcher of the murals, the missing general and the katana-bearing centurion.",
 "**Surnames and later names out:** \"zos Galvus\" and \"Warde\" stay in locators; \"the First\" appears only in Ryne's name; Eros, the Lightwarden of Rak'tika's System-text name, is left out.",
]

# Banned terms this era's text needs, each from the first step in this era where the pages speak it (an earlier era's
# accepted step wins; the lead reconciles).
ALLOW = {
 "Lightwarden": S580,      # The Elder's Answer and on (the Lightwarden of Il Mheg); earlier pages use it from #553
 "Exarch": S584,           # The Wheel Turns (Ardbert on the Exarch); earlier pages use it from #542
 "Emet-Selch": S584,       # The Wheel Turns: "I am Emet-Selch. Ascian." (only a speaker tag before)
 "Zodiark": S603,          # The Burden of Knowledge: "It was we who summoned Zodiark"
 "Oracle of Light": S609,  # The Best Way Out (journal); earlier pages use it from #542
 "Ryne": S620,             # Crossing Paths: Thancred names her
 "The First": S583,        # only in "Minfilia of the First" (part1's display name for her); earlier pages from #542
}

# Not loaded by the builder: Hydaelyn's records for this era, for the lead to merge. char-hydaelyn is defined by
# content_2_1_to_2_3, so with only this era loaded, accepted text that names her fails the lint (her entity starts here).
HYDAELYN_DRAFT = {
  "char-hydaelyn": [
   P(S603, None, "main", "Hydaelyn",
     "The power whose blessing you bear. Emet-Selch claims she rose to serve as the shackles of Zodiark, whom the Ascians summoned, and that the two are the eldest of primals.",
     ["M603c", "M603d", "M603e"]),
   P(S605, None, "main", "Hydaelyn",
     "The power whose blessing you bear, which Emet-Selch calls the eldest of primals alongside Zodiark. Y'shtola fears her blessing did not negate the Lightwarden's light within you, and Ardbert wonders what Her blessing makes of you.",
     ["M603e", "M605a", "M605g"]),
 ]
}
