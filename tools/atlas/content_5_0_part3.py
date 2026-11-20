"""Atlas content for patch 5.0, part 3: MSQ #621 A Fresh Start to #646 A Greater Purpose, and the cp-shb-5-0 milestone
(after the 5.0 finale). Arc tag n. Data only (docs/atlas/era-modules.md is the contract).

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes B11–B15); every locator is an exact substring of a
quest's Journal, Steps or main dialogue (stage directions inside cutscenes included), outside optional blocks and choice
branches. Spoiler rules this module follows:
  - the 5.0 cast reuses the contract's conventional IDs (char-crystal-exarch, char-emet-selch, char-ryne, char-ardbert,
    char-lyna, loc-the-first, loc-crystarium, org-lightwardens …); each first presentation here stands on its own as of
    its step, because parts 1 and 2 of 5.0 are written in parallel;
  - first names and titles only: no "zos Galvus", "yae Galvus" or "Garlond"; the Exarch is "the Crystal Exarch" until the
    pages name him;
  - two reveals follow the Marques → Cid pattern: the Crystal Exarch → G'raha Tia at #639 (the Journal and Urianger name
    him; #636 only unveils his face, in a stage direction), and Emet-Selch → Hades at the milestone (he names himself);
  - "Amaurot", "the Convocation of Fourteen" and "Hythlodaeus" appear only from the step that introduces them; the arc names
    avoid every later quest title;
  - ALLOW proposes each banned term this era needs from the first step in this era whose main text establishes it.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

(N621, N622, N623, N624, N625, N626, N627, N628, N629, N630, N631, N632, N633, N634, N635, N636, N637, N638, N639,
 N640, N641, N642, N643, N644, N645, N646) = (f"cp-msq-{n}" for n in range(621, 647))
MS = "cp-shb-5-0"

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #621 A Fresh Start
 "M621a": ("You left for Nabaath Areng with a girl named Minfilia and came back with one named Ryne, whom the Scions welcome.", "A Fresh Start", "You left for Nabaath Areng with a girl named Minfilia, and return with one named Ryne, whom your fellow Scions welcome with open arms."),
 "M621b": ("Ryne senses a Lightwarden in Amh Araeng, to the west, perhaps hiding underground.", "A Fresh Start", "In fact, I sense one here in Amh Araeng, to the west. I think it might be hiding underground."),
 "M621c": ("The Lightwardens' presence is now unmistakable to Ryne.", "A Fresh Start", "Maybe not, but the presence of the Lightwardens is unmistakable to me now."),
 "M621d": ("Malikah's Well fell into disuse after the Flood, and miners turned part of it into a dig.", "A Fresh Start", "It fell into disuse after the Flood, whereupon the miners of Amh Araeng thought to turn part of it into an excavation site."),
 "M621e": ("You face the Lightwarden in the well and lay it low.", "A Fresh Start", "until you come face-to-face with the Lightwarden. … after a drawn-out struggle, the beast is laid low."),
 "M621f": ("You emerge beneath a night sky, and Alisaie is especially moved by it.", "A Fresh Start", "soon you emerge beneath a spectacular night sky. The sight of it leaves your fellow Scions in awe, Alisaie seeming especially affected by the view."),
 "M621g": ("With each victory the Light's grip on Norvrandt loosens, and Kholusia is its last foothold.", "A Fresh Start", "With each hard-fought victory, the Light's grip over Norvrandt loosens, Kholusia now serving as its final foothold."),
 "M621h": ("The salvation of the First seems within reach.", "A Fresh Start", "Could the salvation of the First at last be within reach?"),
 "M621i": ("Thancred expects Lord Vauthry, in Kholusia, to do everything he can to thwart them.", "A Fresh Start", "Home to our dear Lord Vauthry─who will no doubt do everything in his power to thwart us."),
 "M621j": ("Y'shtola calls Kholusia the last refuge of Light.", "A Fresh Start", "Back to Kholusia. The last refuge of Light."),
 "M621l": ("Y'shtola had surveyed a site called Malikah's Well and suspected the Warden hid there.", "A Fresh Start", "This coincides with Y'shtola's own suspicions after surveying a site known as Malikah's Well."),
 "M621k": ("Alisaie wonders whether Ryne can wield the Oracle's power so soon.", "A Fresh Start", "I can't imagine the power of the Oracle is something one learns to wield in the space of a few hours."),
 # #622 More than a Hunch
 "M622a": ("Ryne sees that you absorbed the Warden's aether, and the Light within you has grown monstrous.", "More than a Hunch", "You've absorbed its aether, [Forename]. And the Light within you has grown monstrous."),
 "M622b": ("Y'shtola warns it will only get worse if nothing is done.", "More than a Hunch", "If naught is done, this will only get worse."),
 "M622c": ("Ryne cannot extinguish the Light; even Minfilia could only hold it back.", "More than a Hunch", "Extinguishing it is out of the question. Even at her strongest, Minfilia could only hold back the Light."),
 "M622d": ("Y'shtola says they must rely on Urianger and his secrets.", "More than a Hunch", "Then we have no choice but to rely on Urianger and his secrets."),
 "M622e": ("Ardbert's shade lingers in your room.", "More than a Hunch", "The player sees Ardbert's shade looking out the window in their room."),
 "M622f": ("With Minfilia gone, Ardbert says, the reason for his purgatory will stay a mystery.", "More than a Hunch", "Which means the reason I must suffer this purgatory shall forever remain a mystery."),
 "M622g": ("Minfilia told Ardbert his time had not yet come and he still had a role to play.", "More than a Hunch", "Minfilia said my time had not yet come. That I still had a role to play."),
 "M622h": ("The Crystal Exarch asks you to survive, no matter what, and then return to your world.", "More than a Hunch", "That you survive this, no matter what. … When the dust settles, you ''must'' return to your world."),
 "M622i": ("The Exarch says only the final Lightwarden stands between them and victory.", "More than a Hunch", "The final Lightwarden is all that stands between us and victory."),
 "M622j": ("The Exarch will look for a remedy for your affliction.", "More than a Hunch", "I will see if there is aught that may remedy the strange affliction which plagues you."),
 # #623 Return to Eulmore
 "M623a": ("The Crystal Exarch calls you to the Ocular.", "Return to Eulmore", "the Crystal Exarch has requested your presence in the Ocular"),
 "M623b": ("Four Lightwardens have been vanquished, returning night to much of Norvrandt.", "Return to Eulmore", "Thus far, we have vanquished four Lightwardens, restoring night to much of Norvrandt."),
 "M623c": ("Emet-Selch declares that driving back the Light will not save the world.", "Return to Eulmore", "Emet-Selch sours the mood with the declaration that driving back the Light will not serve to save the world"),
 "M623d": ("As Zodiark and Hydaelyn warred, Her blow sundered Him and all creation into fourteen fragments.", "Return to Eulmore", "as Zodiark and Hydaelyn warred, the latter struck a devastating blow which sundered not only Her foe, but all of creation, into fourteen fragments"),
 "M623e": ("Looking on their shattered home, the Ascians resolved to rejoin the worlds.", "Return to Eulmore", "looking upon the shattered remains of their home, that the Ascians resolved to rejoin the worlds"),
 "M623f": ("Emet-Selch admits the Ascians erred and made a useless void of the Thirteenth.", "Return to Eulmore", "But in our eagerness─and, I confess, our ignorance─we erred, and made a useless void of the Thirteenth."),
 "M623g": ("Emet-Selch calls you a hero of the Source, seven times rejoined.", "Return to Eulmore", "A vaunted hero of the Source, seven times rejoined."),
 "M623h": ("Lyna's informant in Kholusia reports Eulmore's forces entrenching themselves.", "Return to Eulmore", "Our informant in Kholusia sends word of unusual activity in Eulmore. … It appears their forces are entrenching themselves at key points throughout the city."),
 "M623i": ("The Lightwarden likely hides inside Eulmore.", "Return to Eulmore", "suggesting that the Lightwarden likely hides therein"),
 "M623j": ("Alphinaud saw a reflection of himself in Vauthry's self-righteousness.", "Return to Eulmore", "In Vauthry's self-righteousness─in his absolute belief that he, and he alone, is the cure to the world's ills─I saw a reflection of myself."),
 "M623k": ("On the road to Gatetown you meet civilians acting as if in a trance.", "Return to Eulmore", "On the way to Gatetown, you encounter civilians behaving strangely, as if in a trance"),
 "M623l": ("The Scions agree to meet in Wright, in Kholusia.", "Return to Eulmore", "So it is that you and your comrades depart for Kholusia, having agreed to rendezvous in the village of Wright."),
 "M623m": ("The Exarch addresses Lyna as Captain.", "Return to Eulmore", "Speak freely, Captain."),
 "M623o": ("Y'shtola tells how Hydaelyn unmade Zodiark with a single blow.", "Return to Eulmore", "with a single, devastating blow, Hydaelyn unmade Zodiark, scattering his being across space and time."),
 # #624 A Feast of Lies
 "M624a": ("Gatetown's residents are under Vauthry's mind control.", "A Feast of Lies", "By all indications, the residents of Gatetown are under Vauthry's mind control"),
 "M624b": ("Ryne recognizes meol as sin eater flesh, which leaves those who eat it open to Vauthry's influence.", "A Feast of Lies", "Ryne immediately recognizes the Eulmoran staple for what it is: sin eater flesh, the consumption of which apparently renders one susceptible to Vauthry's influence."),
 "M624c": ("Alphinaud suspects citizens who outlive their usefulness are deliberately turned into sin eaters.", "A Feast of Lies", "Alphinaud shares his suspicion that citizens who have outlived their usefulness are being deliberately turned into sin eaters."),
 "M624d": ("Your old friend Kai-Shirr is the informant who has been feeding secrets to the Crystarium.", "A Feast of Lies", "Alisaie arrives with your old friend Kai-Shirr in tow … that informant who's been feeding secrets to the Crystarium...it's me."),
 "M624e": ("A lone Ran'jit confronts you in the Canopy, and you strike him down.", "A Feast of Lies", "you are confronted by a lone Ran'jit. … striking him down once and for all."),
 "M624f": ("Ran'jit says he has been only a weapon since he submitted to his master.", "A Feast of Lies", "Ever since I submitted to my master's authority, I have been naught but a weapon."),
 "M624g": ("Ryne realizes Vauthry is the Lightwarden, a mixture of man and sin eater.", "A Feast of Lies", "Ryne finally realizes that he is the Lightwarden, being an unholy mixture of man and sin eater."),
 "M624h": ("Vauthry sprouts wings and flees to the peak of Mt. Gulg, torn from the earth and floating.", "A Feast of Lies", "Vauthry sprouts wings and takes to the skies. … the peak of Mt. Gulg, torn from the earth and floating in the heavens. It is there that Vauthry appears to have fled."),
 "M624i": ("Ryne can counteract Vauthry's mind control, and tends the afflicted one by one.", "A Feast of Lies", "Ryne is able to counteract the effects of Vauthry's mind control, and is busy tending to the afflicted one by one."),
 "M624j": ("Vauthry declares there is no justice, future or will but his.", "A Feast of Lies", "There is no justice but mine. No future but mine. No will but mine."),
 # #625 Paradise Fallen
 "M625a": ("Thancred has the enthralled dosed with dream powder to keep them calm.", "Paradise Fallen", "We're administering it to the enthralled to keep them calm until they can receive proper attention."),
 "M625b": ("Ryne heals with the power Minfilia entrusted to her.", "Paradise Fallen", "But Minfilia entrusted this power to me."),
 "M625c": ("Alphinaud tells the Eulmorans that Vauthry is a sin eater and his promises were lies.", "Paradise Fallen", "Vauthry is a sin eater. Everything he offered, everything he promised, was a lie..."),
 "M625d": ("Alphinaud reminds the Eulmorans they gave themselves to the city's pleasures of their own free will.", "Paradise Fallen", "Of your own free will, you came to this city and gave yourselves over to its pleasures."),
 "M625e": ("The Ladder is the only way up and down the cliff, and has not moved in a long time.", "Paradise Fallen", "The Ladder is the only way up and down the cliff, but it hasn't moved in a long time."),
 "M625f": ("Dulia-Chai's husband, Chai-Nuzz, is heir to Daedalus Stoneworks, foremost makers of Talos.", "Paradise Fallen", "For he happens to be the heir to Daedalus Stoneworks, foremost makers of Talos,"),
 "M625g": ("Chai-Nuzz will look at the Talos, but promises nothing.", "Paradise Fallen", "I will take a look at the Talos, but beyond that, I make no promises!"),
 "M625h": ("The only way to Mt. Gulg is over the Bright Cliff.", "Paradise Fallen", "The only way to Mt. Gulg is over the Bright Cliff."),
 # #626 The Ladder
 "M626a": ("The Ladder needs extensive maintenance and materials before it can move again.", "The Ladder", "Extensive maintenance will be needed ere it can move again, as well as myriad materials with which to perform it."),
 "M626b": ("Urianger sends you to Venmont Yards, a dry dock to the south.", "The Ladder", "Directly to the south thou wilt find a dry dock─Venmont Yards."),
 "M626c": ("Irvithe will give lumber if your count of the yard's supply matches his.", "The Ladder", "I want you to do the counting instead, and we'll see if your total matches mine."),
 "M626d": ("You secure the lumber and the shipwrights' eager cooperation.", "The Ladder", "to secure not only the material, but the eager cooperation of the shipwrights besides"),
 "M626e": ("Urianger says the people now stand united against the world's fate.", "The Ladder", "at long last do the people stand united in defiance of the world's fate"),
 # #627 The View from Above
 "M627a": ("The Ladder lives again, and you and the twins are its first riders in twenty years.", "The View from Above", "The Ladder lives again, and you join the twins as the first souls to ride the lift in twenty years."),
 "M627b": ("Emet-Selch raises the prospect of your joining him as an equal.", "The View from Above", "he raises the prospect of you joining him as an equal─a complete existence in a complete world."),
 "M627c": ("Emet-Selch reminds you that you are of the Source, unlike the halfmen here.", "The View from Above", "Remember, you are of the Source. Unlike the halfmen here, you stand only to gain."),
 "M627d": ("Emet-Selch recalls when the world was whole, and his people had family, friends and loves.", "The View from Above", "Back when the world was whole, we had family, friends, loves..."),
 "M627e": ("Emet-Selch asks whether the Exarch has ever shown what hides beneath his cowl.", "The View from Above", "How well do you know the Exarch? Has he ever deigned to show you what hides beneath the cowl?"),
 "M627f": ("Ardbert speaks of his struggles against solitude and warns you against a choice that leaves you alone.", "The View from Above", "he speaks to you of his struggles against solitude, and warns you against making a choice that leaves you alone"),
 "M627g": ("Ardbert carries the guilt of causing the Flood.", "The View from Above", "The guilt of causing the Flood... Knowing everyone hated me..."),
 "M627h": ("Alisaie saw someone come out of a village thought abandoned.", "The View from Above", "she witnessed someone emerge from the village to the northeast, even though the area is believed to have been abandoned"),
 "M627i": ("Tristol, the artist you saved, says Amity is a settlement of Eulmore's exiles, and promises aid.", "The View from Above", "It is revealed to belong to none other than Tristol, the young artist whose life you saved in Kholusia. He informs you that the village, Amity, is a settlement for those who survived being exiled from Eulmore, and upon learning that you are in pursuit of Vauthry, promises to aid you in your quest."),
 "M627j": ("A local led Tristol through a secret tunnel to the top of the Bright Cliff.", "The View from Above", "He took me through a secret tunnel which led to the top of the Bright Cliff."),
 "M627k": ("Ardbert once rode the Ladder with his comrades, and no one but him remembers it.", "The View from Above", "We rode the Ladder too, my comrades and I. Once upon a time. … No one but me remembers that day."),
 # #628 In Mt. Gulg's Shadow
 "M628a": ("Alisaie judges that Vauthry is massing sin eaters around the volcano.", "In Mt. Gulg's Shadow", "And judging by the number we've already faced, his lordship is of the same mind."),
 "M628b": ("Allagan drones fly toward Mt. Gulg, and flight is ruled out.", "In Mt. Gulg's Shadow", "Three Allagan drones fly overhead towards Mt. Gulg. … Well, it seems flying is off the table."),
 "M628c": ("The Exarch says the machina served their purpose.", "In Mt. Gulg's Shadow", "If we have learned that much, then the machina have served their purpose."),
 "M628d": ("The Exarch wants to observe the final struggle with his own eyes.", "In Mt. Gulg's Shadow", "I wish to observe the final struggle with my own eyes."),
 "M628e": ("Urianger concludes the foe cannot be reached by land or air.", "In Mt. Gulg's Shadow", "'Twould seem our foe will not be reached by land or air."),
 # #629 A Gigantic Undertaking
 "M629a": ("Y'shtola proposes a Talos large enough to take the volcano in its grasp.", "A Gigantic Undertaking", "In the form of a Talos. A Talos large enough to reach out and take the volcano in its grasp."),
 "M629b": ("Y'shtola tells Chai-Nuzz that Norvrandt is counting on him as heir to Daedalus Stoneworks.", "A Gigantic Undertaking", "Norvrandt is counting on you...heir to Daedalus Stoneworks."),
 "M629c": ("Chai-Nuzz admits Eulmore essentially sent Tristol to his death.", "A Gigantic Undertaking", "Lest you've forgotten, we essentially sent him to his death!"),
 "M629d": ("Tristol reminds Chai-Nuzz that Eulmore ignored his pleas and cast him out.", "A Gigantic Undertaking", "After you ignored my desperate pleas and cast me out, you have the gall to come here and ask for my cooperation?"),
 "M629e": ("Chai-Nuzz says what Eulmore did to Tristol and many others was terribly wrong.", "A Gigantic Undertaking", "But we know now that what we did to you─to full many─was wrong. Terribly wrong."),
 "M629f": ("Tristol agrees to cooperate.", "A Gigantic Undertaking", "And so...I will cooperate with you. Please see our friends to Mt. Gulg."),
 "M629g": ("Thancred will ask the miners of Amh Araeng for aid.", "A Gigantic Undertaking", "We have friends amongst the miners of Amh Araeng. I will go and petition their aid."),
 "M629h": ("Waking a Talos this size needs a whole congregation of mages.", "A Gigantic Undertaking", "To awaken a Talos of this size would require an entire congregation of mages."),
 "M629i": ("Chai-Nuzz forgot one important item needed to bring a Talos to life.", "A Gigantic Undertaking", "But I forgot about one rather important item needed to bring a Talos to life..."),
 # #630 Meet the Tholls
 "M630a": ("The Tholls, a dwarven family, have long mined this land.", "Meet the Tholls", "a dwarven family known as the Tholls have long mined this land"),
 "M630b": ("You and the Exarch set out for Tomra to see its chief, Xamott.", "Meet the Tholls", "Thus do you and the Exarch set out for the village of Tomra to seek an audience with its chief, a dwarf named Xamott."),
 "M630c": ("Xamott will help only if sure you will put the ore to good use, so he sets a trial.", "Meet the Tholls", "he will only help you find the ore if he is certain you will put it to good use. To that end, he requires that you undertake a trial most tricksy"),
 "M630d": ("Xamott places his faith in you and will help you find ore for the Talos heart.", "Meet the Tholls", "Xamott declares that he will place his faith in you and help you to find the ore you seek for the Talos heart."),
 "M630e": ("A Tholl showed Tristol the secret tunnel to the clifftop.", "Meet the Tholls", "'twas one of them that showed me the secret tunnel to the top of the cliff."),
 "M630f": ("The Tholls don't know how to deal with the floating volcano or the sin eaters either.", "Meet the Tholls", "Havin' said that, it's not like we know how to deal with that floatin' volcano and all them sin eaters neither."),
 # #631 A-Digging We Will Go
 "M631a": ("Earthseed is a rare ore steeped in magick.", "A-Digging We Will Go", "every so often, the selfsame veins yield what's called earthseed, a rare ore steeped in magick."),
 "M631b": ("The Duergar's Tewel is the surest place for earthseed, but the Tholls' rivals, the Goggs, hold it.", "A-Digging We Will Go", "And no place is surer'n the Duergar's Tewel. … Problem is, the site's occupied by our age-old rivals─the Goggs."),
 "M631c": ("Korutt volunteers to go with you.", "A-Digging We Will Go", "I'll do it! I'll go with them!"),
 "M631d": ("Korutt is one of Tomra's finest miners, but hopeless in a fight.", "A-Digging We Will Go", "Young as he is, he's one of the village's finest miners. … It's true... I'm hopeless in a fight..."),
 "M631e": ("Korutt is shocked that the last Lightwarden hides up on the volcano.", "A-Digging We Will Go", "To think the last Lightwarden's hiding up there..."),
 "M631f": ("Korutt reaches the cave and urges everyone inside.", "A-Digging We Will Go", "Let's hurry inside before any more sin eaters come!"),
 # #632 The Duergar's Tewel
 "M632a": ("The Exarch renders Korutt invisible with an enchantment.", "The Duergar's Tewel", "I will use an enchantment to render you invisible."),
 "M632b": ("The Exarch brings dream powder, as used in the rescue at Laxan Loft.", "The Duergar's Tewel", "Dream powder. As you may recall, we used it for the rescue mission at Laxan Loft."),
 "M632c": ("Glagg, chief of the Goggs, arrives.", "The Duergar's Tewel", "Th-That's Glagg, chief of the Goggs!"),
 "M632d": ("Glagg accuses Tholl scum of skulking about his site.", "The Duergar's Tewel", "And what should I find here but Tholl scum skulkin' about!"),
 "M632e": ("The Exarch weakens after so long away from the Crystarium.", "The Duergar's Tewel", "Long as I have been away from the Crystarium, a little weakness is to be expected."),
 "M632f": ("With the ore in hand, the Exarch says the Talos awaits its heart.", "The Duergar's Tewel", "Now that we have what we came for, however, it is time to take our leave. The Talos awaits its heart!"),
 # #633 Rich Veins of Hope
 "M633a": ("The Exarch carries the earthseed to Chai-Nuzz in Amity, and asks you to take Korutt home.", "Rich Veins of Hope", "While he transports the earthseed to Chai-Nuzz in Amity, he asks that you see your young dwarven companion, Korutt, safely back to Tomra."),
 "M633b": ("The Tholls modified their spare pickaxes for bigger folk.", "Rich Veins of Hope", "they have modified their spare pickaxes for use by bigger folk"),
 "M633c": ("Volunteers recruited by Thancred and Ryne arrive under escort of Crystarium and Eulmoran soldiers.", "Rich Veins of Hope", "the volunteers Thancred and Ryne recruited are being escorted to the work site─and by both Crystarium and Eulmoran soldiers, no less."),
 "M633d": ("All the volunteers want to do their part for Norvrandt.", "Rich Veins of Hope", "all are united in their desire to do their part for Norvrandt"),
 "M633e": ("Alisaie sought the aid of those who believe in the Warrior of Darkness.", "Rich Veins of Hope", "She said that she sought the aid of those who believed in the Warrior of Darkness."),
 "M633f": ("Kai-Shirr has yet to repay you and Alphinaud for saving him.", "Rich Veins of Hope", "I still haven't repaid you and Alphinaud for saving me, and I'm not sure I ever could."),
 "M633g": ("Alisaie joins the soldiers guarding the volunteers.", "Rich Veins of Hope", "I think I'll go and join the soldiers standing guard over the volunteers."),
 "M633h": ("After night returned to Amh Araeng, the patients' transformation halted.", "Rich Veins of Hope", "After night returned to Amh Araeng, we noticed a change in our patients. The transformation had halted in every one of them."),
 # #634 That None Shall Ever Again
 "M634a": ("In Amity, Y'shtola oversees those who will imbue the Talos.", "That None Shall Ever Again", "There, Y'shtola is overseeing those who will imbue the Talos with magicks."),
 "M634b": ("There is not enough ore for the Talos's purpose.", "That None Shall Ever Again", "However, we don't have enough ore for this purpose."),
 "M634c": ("The heartstones are the Night's Blessed's most prized possession.", "That None Shall Ever Again", "The most prized possession of we of the Night's Blessed."),
 "M634d": ("A heartstone bears the Night's Blessed's hope that none shall again be sacrificed to sin eaters.", "That None Shall Ever Again", "It bears the collective hope of the Night's Blessed─the hope that none shall ever again be sacrificed to sin eaters."),
 "M634e": ("Urianger has measures ready in case you fail to contain the Light.", "That None Shall Ever Again", "You said that you would have measures ready in the event that our friend fails to contain the Light."),
 "M634f": ("Once the Talos wakes and the way to Mt. Gulg is secured, they will sally forth.", "That None Shall Ever Again", "When the Talos awakens and the way to Mt. Gulg is secured, we shall sally forth."),
 "M634g": ("Nigh everyone in Norvrandt rallied for the endeavor.", "That None Shall Ever Again", "We managed to rally nigh everyone in Norvrandt for this endeavor."),
 # #635 A Breath of Respite
 "M635a": ("The Exarch excused himself for a breath of fresh air.", "A Breath of Respite", "Anyway, he excused himself, saying that he needed a breath of fresh air."),
 "M635b": ("The Exarch made himself one with the Crystal Tower so he might live indefinitely.", "A Breath of Respite", "And so I made myself one with the Crystal Tower, that I might live indefinitely."),
 "M635c": ("He is an extension of the tower, so he weakens the farther and longer he is away.", "A Breath of Respite", "I am but an extension of it now. Hence my weakness the farther I travel, and the longer I am away."),
 "M635d": ("In the Source, Zenos's body reports that the Scions are no longer in the Source.", "A Breath of Respite", "It is because they are no longer in the Source."),
 "M635e": ("The plan is to defeat the Alliance before the Scions return.", "A Breath of Respite", "If we can defeat the Alliance prior to the Scions' return, we may eliminate their order at a stroke."),
 "M635f": ("Emet-Selch has gone to the First to usher that world to its end.", "A Breath of Respite", "He has taken himself to the First, to usher that world to its end."),
 "M635g": ("A katana-bearing centurion calls the one in Zenos's body Elidibus, and draws his weapon.", "A Breath of Respite", "Or would you rather I called you Elidibus? … The katana-bearing centurion draws his weapon."),
 "M635i": ("Emperor Varis asks after Emet-Selch.", "A Breath of Respite", "And what of Emet-Selch?"),
 "M635j": ("The scene shifts to the imperial palace in the Source.", "A Breath of Respite", "Meanwhile, in the imperial palace in the Source..."),
 "M635h": ("The centurion cares nothing for Zenos's name, but is rather fond of the body.", "A Breath of Respite", "I have no particular attachment to that name─but I ''am'' rather fond of that body."),
 # #636 Extinguishing the Last Light
 "M636a": ("The fae folk drive the sin eaters off the Talos's hands, and it completes its task.", "Extinguishing the Last Light", "help then arrives in the unexpected form of the fae folk, who engage the sin eaters from the air and allow the Talos to safely complete its task"),
 "M636b": ("You lay low Vauthry's ultimate incarnation, Innocence.", "Extinguishing the Last Light", "you succeed in laying low Vauthry's ultimate incarnation, Innocence"),
 "M636c": ("Vauthry dissolves into light, which you take into yourself, and the night sky returns.", "Extinguishing the Last Light", "Vauthry's body dissolves into innumerable motes of light, which you stoically take unto yourself. At that instant, the blazing shroud covering the firmament falls away to reveal a peaceful night sky."),
 "M636d": ("Vauthry was a pawn of the Ascians, born man and sin eater both to bring about the First's Rejoining.", "Extinguishing the Last Light", "He too, you discover, was a pawn of the Ascians, born as man and sin eater both to bring about the First's Rejoining."),
 "M636e": ("Emet-Selch offered Eulmore's former mayor to give a Lightwarden's power to his unborn child.", "Extinguishing the Last Light", "By giving its power to the babe within your lady wife's womb, we shall create a transcendent being─a king to rule over all."),
 "M636f": ("You cannot contain the combined power of all the Wardens.", "Extinguishing the Last Light", "you are unable to contain the combined power of all the Wardens"),
 "M636g": ("The Exarch meant all along to take your burden on himself and teleport into the rift as a sacrifice.", "Extinguishing the Last Light", "From the beginning, it was his intent to take your unbearable burden upon himself, and teleport into the rift in a final act of sacrifice."),
 "M636h": ("Emet-Selch shoots the Exarch before he can finish.", "Extinguishing the Last Light", "But before he can complete his ritual, a shot rings out and he crumples to the floor. Holding the smoking gun is none other than Emet-Selch"),
 "M636i": ("Emet-Selch declares you unworthy, leaves with the wounded Exarch, and invites you to his abode in the Tempest.", "Extinguishing the Last Light", "Declaring you unworthy to be his ally, the Ascian leaves with the wounded Exarch, though not before inviting you to seek him out at his abode, in the dark depths of the Tempest."),
 "M636j": ("Emet-Selch, an Ascian seeking the Great Rejoining, created Vauthry.", "Extinguishing the Last Light", "I am an Ascian. My heart's sole desire is to usher in the Great Rejoining. … When that failed to achieve the desired result, I created Vauthry."),
 "M636k": ("Only Ryne's powers keep you from becoming a sin eater, and only for a time.", "Extinguishing the Last Light", "it is only thanks to Ryne's powers that you have not yet turned into a sin eater, but that it is only a matter of time"),
 "M636l": ("The land is shrouded in Light once more.", "Extinguishing the Last Light", "look out upon a land shrouded in Light once more"),
 "M636m": ("Norvrandt is shrouded in Light again because of the power you absorbed, and only your friends know it.", "Extinguishing the Last Light", "And it's because of you and the power you absorbed from the Wardens. … No one knows but your friends."),
 "M636n": ("Emet-Selch says only those with the Royal Eye of the Allagan line can control the Crystal Tower.", "Extinguishing the Last Light", "Only those who possess the Royal Eye of the Allagan imperial line are capable of controlling the Crystal Tower."),
 "M636o": ("The Exarch is still alive, and Emet-Selch says his survival depends on you.", "Extinguishing the Last Light", "Your friend is still alive, but whether he remains so depends on you."),
 "M636p": ("The Exarch's hood falls back, unveiling his face.", "Extinguishing the Last Light", "The Exarch's hood unveils"),
 "M636q": ("Y'shtola sees that the Exarch means to take the Light into the rift and die there.", "Extinguishing the Last Light", "He means to take the Light with him into the rift...where he will die."),
 "M636r": ("Urianger knew of the Exarch's plan and begs the others not to interfere.", "Extinguishing the Last Light", "Do not interfere! … You knew of this, Urianger."),
 "M636s": ("Emet-Selch says you have all but become a sin eater.", "Extinguishing the Last Light", "Hm, you still retain your form and your senses...but you have all but become a sin eater."),
 "M636t": ("Ryne promised to keep the legacy a noble woman entrusted to her.", "Extinguishing the Last Light", "I made a promise to a noble soul─a woman who saw fit to entrust me with her legacy─and I mean to keep it."),
 "M636u": ("Dying, Innocence says he was born man and sin eater both, and told he was a god.", "Extinguishing the Last Light", "Father told me...that I am hope. I am righteousness. That I am...a ''god''... … That is why I was born...as man and sin eater both..."),
 "M636v": ("You wake with Ardbert watching over you.", "Extinguishing the Last Light", "you awaken in your chambers with Ardbert watching over you"),
 "M636w": ("Emet-Selch tells you your friends are now your foes.", "Extinguishing the Last Light", "Your friends are now your foes. If you do not kill them, they will kill you."),
 # #637 Reassuring the Masses
 "M637a": ("You are asked to walk the city and reassure its anxious citizens.", "Reassuring the Masses", "would you mayhap consider a stroll around the city to reassure our anxious citizens?"),
 "M637b": ("Trade with Eulmore is back on the table.", "Reassuring the Masses", "Trade with Eulmore is back on the table."),
 "M637c": ("Moren wonders why the Light has returned with every Lightwarden defeated.", "Reassuring the Masses", "why, with all the Lightwardens defeated, has the Light returned to obscure the sky?"),
 "M637d": ("With you awake, Moren hopes the search for their stolen steward can begin in earnest.", "Reassuring the Masses", "Now that you are awake, however, I am hopeful the search for our stolen steward might begin in earnest."),
 "M637e": ("Katliss readies the Crystalline Mean for battle against an unknown foe.", "Reassuring the Masses", "Katliss, meanwhile, leads the Crystalline Mean in preparations for battle...though against what foe, we are as yet uncertain."),
 "M637f": ("Ryne told Chessamile your symptoms resemble eater corruption.", "Reassuring the Masses", "Ryne ''was'' kind enough to tell me you were showing symptoms similar to eater corruption"),
 "M637g": ("No one has seen the craftsman Grenoldt since he wandered off years ago.", "Reassuring the Masses", "No one's seen hide nor hair of Grenoldt since he wandered off some years ago."),
 # #638 In His Garden
 "M638a": ("Ardbert and his comrades, realizing they caused the Flood, resolved to journey to the Source by taking their own lives.", "In His Garden", "It was after we realized we were responsible for the Flood. When we resolved to journey to the Source by taking our own lives."),
 "M638b": ("Ardbert casts his lot with yours.", "In His Garden", "For what it's worth, I cast my lot with yours."),
 "M638c": ("If you lose control, Ardbert will do his best to stop you.", "In His Garden", "if you lose control, I'll do my best to stop you"),
 "M638d": ("Feo Ul bids you ask his flowers what they know.", "In His Garden", "Ask his flowers what they know, and you will surely find an answer."),
 "M638e": ("No one but the Exarch may dwell within the spire.", "In His Garden", "no one except the Exarch is permitted to dwell within the spire"),
 "M638f": ("The Exarch said the Crystal Tower may one day vanish as suddenly as it came.", "In His Garden", "Because one day, the Crystal Tower may vanish as suddenly as it arrived."),
 "M638g": ("Lyna lost her parents to eaters as a baby, and the Exarch raised her.", "In His Garden", "She lost her parents to an eater attack not long after she was born, and the Exarch saw to her upbringing."),
 "M638h": ("The Crystal Tower appeared less than a decade after the Flood, and its summoner, the Exarch, became known to the Lakeland refugees soon after.", "In His Garden", "Less than a decade had passed since the coming of the Flood when the Crystal Tower first flashed into existence. Its summoner─the Exarch himself─became known to the refugees in Lakeland soon thereafter."),
 "M638i": ("The Exarch's true name remains an unsolved mystery.", "In His Garden", "'twould seem that is a mystery that remains unsolved to this day."),
 "M638j": ("The Exarch left Lyna access to the Umbilicus, to wake the city's barrier if eaters attack.", "In His Garden", "Only in the event that an army of eaters descended upon the city was I to access the Umbilicus and awaken the defensive barrier."),
 "M638k": ("Lyna believes the Exarch knew a terrible fate awaited him.", "In His Garden", "He ''knew'' that some terrible fate awaited him."),
 # #639 The Unbroken Thread
 "M639a": ("An Echo shows the Exarch, whose true identity is G'raha Tia, telling Urianger of an apocalyptic future in the Source and of efforts across time to spare your life and countless others.", "The Unbroken Thread", "G'raha Tia─for that is the steward's true identity─speaks of an apocalyptic future in the Source, and of a determined group's efforts to bend time and space so that your life, and the lives of countless others, might be spared."),
 "M639b": ("Urianger agreed to hide the truth from the other Scions and keep them from interfering with the Exarch's self-sacrifice.", "The Unbroken Thread", "Urianger grimly agrees to conceal the truth from his fellow Scions, and to prevent them from interfering with the Exarch's planned act of self-sacrifice."),
 "M639c": ("Urianger names him: G'raha Tia.", "The Unbroken Thread", "Thy true name is G'raha Tia, then."),
 "M639d": ("G'raha Tia is a native of the Source in a later age, after the Eighth Umbral Calamity.", "The Unbroken Thread", "By thy claims, thou too art a native of the Source, though from an age beyond our own, when the Eighth Umbral Calamity hath visited devastation upon our star."),
 "M639e": ("Generations later, his people woke the Crystal Tower and roused its caretaker, himself.", "The Unbroken Thread", "After two centuries of labor, their descendants finally succeeded in awakening the Crystal Tower─an integral part of the process─and in doing so roused its caretaker. Me."),
 "M639f": ("They missed their mark in the First by almost a century.", "The Unbroken Thread", "we missed our mark by almost an entire century"),
 "M639g": ("Once the last Lightwarden is slain, he will absorb their aether and die.", "The Unbroken Thread", "When all is said and done, and the last of the Lightwardens lies slain, I will absorb their corrupted aether. And then I will die."),
 "M639h": ("The Warrior of Light's tale held the plan together.", "The Unbroken Thread", "The Warrior of Light has been our unbroken thread."),
 "M639i": ("Urianger convinced the Exarch he could be trusted when he spoke of arranging Minfilia's journey to the First.", "The Unbroken Thread", "'Twas you yourself who convinced me of your suitability when you spoke of how you learned of the Flood, and of your part in arranging Minfilia's journey to the First."),
 "M639j": ("Lyna resolves to unlock the door to the Umbilicus.", "The Unbroken Thread", "Lyna is resolved to unlock the door to the Umbilicus."),
 "M639k": ("Ardbert helps guide you toward a course of action.", "The Unbroken Thread", "Ardbert appears and helps guide you towards a possible course of action"),
 "M639l": ("Lyna directs you to the tamers at the Amaro Launch to reach the Tempest.", "The Unbroken Thread", "ask for the most direct means of reaching the Tempest. Somewhat taken aback by the request, the guard captain directs you to the tamers at the Amaro Launch."),
 "M639m": ("Over Ryne's objections and with Alisaie's argument, your companions agree to go with you, and the Crystarium, long suspecting you the Warrior of Darkness, backs you.", "The Unbroken Thread", "the objections raised by Ryne are met with an impassioned argument from Alisaie. In the end, your companions agree to accompany you to the Tempest─an endeavor which gains the unexpected support of the Crystarium citizenry. They have long suspected your role as the Warrior of Darkness"),
 "M639n": ("Urianger has told the Scions the Exarch's true identity and purpose.", "The Unbroken Thread", "Urianger has shared everything with us─the Exarch's true identity and purpose."),
 "M639o": ("Ryne warns that what she did for you won't last forever.", "The Unbroken Thread", "What I did for you won't last forever. There's no telling when the Light will break free again."),
 "M639p": ("Ardbert thinks the Ascian's lair lies beneath the Tempest's waves.", "The Unbroken Thread", "His lair must be down there somewhere, hidden beneath the waves."),
 "M639q": ("Urianger hints at an easier way to reach the ocean floor.", "The Unbroken Thread", "Urianger hints that he may have a less strenuous way of reaching the ocean floor."),
 # #640 To Storm-tossed Seas
 "M640a": ("The Isle of Ken is an ancient fae being named Bismarck.", "To Storm-tossed Seas", "The Isle of Ken is, as it turns out, an ancient fae being by the name of Bismarck."),
 "M640b": ("Feo Ul convinces Bismarck to carry you to the ocean's depths.", "To Storm-tossed Seas", "it takes the intervention of Feo Ul to convince Bismarck to bear you to the ocean's depths"),
 "M640c": ("Bismarck sets you on the sea floor within a dome of air made by its breath.", "To Storm-tossed Seas", "Bismarck deposits you on the sea floor, secure within an enormous dome of air created by its mighty breath."),
 "M640d": ("Urianger reasons Emet-Selch cannot risk the rift with the Exarch as prisoner, so he is in the Tempest.", "To Storm-tossed Seas", "Suspecting that Emet-Selch cannot risk fleeing into the rift while the Exarch is his prisoner, he seems confident that the Ascian is to be found somewhere within this underwater realm."),
 "M640e": ("The Exarch's body is the key to the Crystal Tower and its power to travel through time.", "To Storm-tossed Seas", "the Exarch's very body serveth as the key to the Crystal Tower and its powers of temporal transportation"),
 "M640f": ("Feo Ul commands Bismarck as king.", "To Storm-tossed Seas", "[Let their wish be the king's command.]"),
 "M640h": ("Ardbert calls the Tempest's floor the last refuge of he who denies the Light.", "To Storm-tossed Seas", "The last refuge of he who denies the Light with every fiber of his being."),
 "M640g": ("Urianger seeks the aid of a fae being he has never met.", "To Storm-tossed Seas", "Thus would I petition the aid of one of the fae─a being with whom I have yet to meet face-to-face."),
 # #641 Waiting in the Depths
 "M641a": ("Thancred leads the search down the slope for a formation big enough to house a stronghold.", "Waiting in the Depths", "I propose we follow the slope down towards the deeper trenches, and keep an eye out for rock formations large enough to house a stronghold."),
 "M641b": ("The Scions did not know the Ondo lived in the Tempest.", "Waiting in the Depths", "we were not aware your people lived here in the Tempest."),
 "M641c": ("The Ondo have seen an illuminated land shining through the abyss.", "Waiting in the Depths", "We have ssseen the illuminated land shhhining through the gloom of the abyss..."),
 "M641d": ("Tolshs Aath will welcome you only if you are the chosen emissaries.", "Waiting in the Depths", "If you are the emissaries─the chosen─I bid you welcome. If you are not, I bid you leave."),
 "M641e": ("Y'shtola senses the Ondo have a deeper tie to the Ascians.", "Waiting in the Depths", "I sense this tribe has a deeper connection to the Ascians than first meets the eye."),
 "M641f": ("Paushs Ooan is the Ondo Alphinaud did business with before Eulmore.", "Waiting in the Depths", "This is Paushs Ooan, the very fellow I did business with prior to our ill-fated stay in Eulmore!"),
 "M641g": ("The Ondo believe the ancients chose them as caretakers of their sanctuary.", "Waiting in the Depths", "That the ancients had chosen us to ssserve as caretakers of their eternal sssanctuary, until sssuch time as they returned."),
 "M641h": ("Alphinaud admits the lack of water is the Scions' doing.", "Waiting in the Depths", "the lack of water is ''our'' doing, for which we must also make amends."),
 # #642 City of the Ancients
 "M642a": ("Your knife cannot scrape so much as a flake from the remnant wall.", "City of the Ancients", "you cannot remove so much as a flake of stone."),
 "M642b": ("Even the Ronkan Empire produced nothing to compare.", "City of the Ancients", "Even the Ronkan Empire, once the greatest power in Norvrandt, produced nothing which compares to this level of perfection."),
 "M642c": ("Emet-Selch said the Qitana Ravel mural depicts a city of eons past and its disaster.", "City of the Ancients", "By Emet-Selch's own words, it depicts a city of eons past and the disaster which befell it."),
 "M642d": ("Y'shtola thinks Emet-Selch's choice of stronghold serves the Ascian agenda.", "City of the Ancients", "Emet-Selch is devoted to his role, and thus we might assume his choice of stronghold somehow serves the Ascian agenda."),
 "M642e": ("Y'shtola is almost certain Emet-Selch lit the illuminated land and is there.", "City of the Ancients", "And who else would “light the lanterns” as Ryne put it, than Emet-Selch himself? 'Tis almost certain he is there!"),
 "M642f": ("Gaining the Ondo's trust is the swiftest way to the stronghold.", "City of the Ancients", "But if we are to find this stronghold in a timely manner, it seems gaining the Ondo's trust remains our swiftest path forward."),
 # #643 The Light of Inspiration
 "M643a": ("The Ondo plan to light the Walls to answer the illuminated land.", "The Light of Inspiration", "our plans to bring light to the Walls, that we might answer the shining call of the illuminated land."),
 "M643b": ("The Ondo asked a finless craftsman for a sacred lamp.", "The Light of Inspiration", "We have requested a finless craftsman to shape for us a sssacred lamp."),
 "M643c": ("Grenoldt's delivery date is long past and his bench untouched.", "The Light of Inspiration", "Me delivery date's long past, me workbench is untouched..."),
 "M643d": ("You show Grenoldt a crystal that belonged to one of Ardbert's companions.", "The Light of Inspiration", "Show Grenoldt a crystal which once belonged to one of Ardbert's companions?"),
 "M643e": ("You must present something inspiring to Grenoldt.", "The Light of Inspiration", "Present something inspiring to Grenoldt."),
 # #644 The Illuminated Land
 "M644a": ("Grenoldt crafts a splendid lamp for the Ondo's devotions.", "The Illuminated Land", "Grenoldt channels his newfound inspiration into crafting a suitably splendid lamp for the Ondo's planned devotions."),
 "M644b": ("The perfection of the ancients' works had stolen Grenoldt's will to craft.", "The Illuminated Land", "explaining how the perfection of the ancients' works had stolen his will to craft"),
 "M644c": ("Grenoldt offers to weave bittersweet sagas into armaments for you.", "The Illuminated Land", "enough to weave the strength of bittersweet sagas into armaments you can use"),
 "M644d": ("Tolshs Aath recognizes you as the sign the Ondo have awaited.", "The Illuminated Land", "the grateful chieftain recognizes you and your companions as the sign they have been waiting for"),
 "M644e": ("Tolshs Aath appoints a guide to the illuminated land.", "The Illuminated Land", "Tolshs Aath appoints a guide to show you the way to the “illuminated land.”"),
 "M644f": ("The Ondo saw a light, believed the ancients had risen, and found a whole city in the depths.", "The Illuminated Land", "We understood at once─the ancients had risen. There could be no doubt. … and discovered in the depths an entire city."),
 "M644g": ("You dispel the Ondo's barrier at the Caliban Gap.", "The Illuminated Land", "Alphinaud bids you dispel the Ondo's barrier."),
 "M644h": ("Past the Caliban Gap lies a vast city.", "The Illuminated Land", "As you exit the Caliban Gap, you are greeted by the spectacle of a vast city."),
 "M644i": ("Emet-Selch has draped the semblance of a city over ancient ruins, and holds the Exarch somewhere within.", "The Illuminated Land", "upon the ruins has been draped the semblance of the city which once stood there. And somewhere, hidden within this enchanted metropolis, awaits Emet-Selch and the captive Exarch..."),
 "M644j": ("Alisaie never quite believed Emet-Selch was telling the truth.", "The Illuminated Land", "Despite his many protestations, I never quite believed Emet-Selch was telling the truth."),
 # #645 The End of a World
 "M645a": ("Urianger recalls that Emet-Selch invited you to his abode.", "The End of a World", "Did Emet-Selch not invite [Forename] to visit his abode?"),
 "M645b": ("To Y'shtola, the city's people appear as arcane entities.", "The End of a World", "To my eyes, these people appear as arcane entities."),
 "M645c": ("The Final Days were a catastrophe that set in motion the summoning of Zodiark, then Hydaelyn.", "The End of a World", "A catastrophe of unprecedented scale, which did set in motion the summoning of Zodiark...and thence Hydaelyn Herself."),
 "M645d": ("Emet-Selch has resurrected a moment from before the star was sundered.", "The End of a World", "Emet-Selch hath resurrected a memory─a moment in time from before the star was sundered."),
 "M645e": ("A resident says a terrible phenomenon afflicts their star.", "The End of a World", "a terrible phenomenon afflicts our star."),
 "M645f": ("Lahabrea is the Convocation's speaker and Elidibus its emissary; each seat is held by an elected sage.", "The End of a World", "Be it the speaker, Lahabrea, or the emissary, Elidibus, each seat is occupied by an elected sage of surpassing intellect."),
 "M645g": ("Rumor says the Fourteen will invoke their mightiest spells of creation.", "The End of a World", "They will invoke our mightiest spells of creation to birth an antity of all-encompassing magnificence"),
 "M645h": ("The city's people believe they face the end of the world, and Alphinaud wonders why Emet-Selch recreated it.", "The End of a World", "the people of this city believe they face the end of the world. … I cannot imagine what purpose compelled Emet-Selch to recreate this ancient"),
 "M645i": ("Thancred sends the group to learn where their quarry is.", "The End of a World", "see if we can't learn the location of our quarry."),
 "M645j": ("The city is Amaurot.", "The End of a World", "Amaurot"),
 # #646 A Greater Purpose
 "M646a": ("The Capitol's attendant will not let anyone through without a writ.", "A Greater Purpose", "the attendant wouldn't let us through without a writ of permission..."),
 "M646b": ("Emet-Selch himself approved your residency.", "A Greater Purpose", "As your residency was approved by Emet-Selch himself, further forms of identification will not be required."),
 "M646c": ("Hythlodaeus knows only his name, and that the city is a recreation.", "A Greater Purpose", "I know only that my name is Hythlodaeus, and that this city is a recreation"),
 "M646d": ("Hythlodaeus and Emet-Selch were close friends once.", "A Greater Purpose", "We were... close friends once, you see..."),
 "M646e": ("The Convocation set out to create a will for the star.", "A Greater Purpose", "endeavored to create a will for our star"),
 "M646f": ("Nearly half the living gave their lives, and from their sacrifice Zodiark was born.", "A Greater Purpose", "Of those of us who still lived, nearly half offered up their lives in the name of salvation. … And from their sacrifice, Zodiark was born."),
 "M646g": ("Zodiark would restore the brethren whose souls fed His strength.", "A Greater Purpose", "In return, He would restore to us those brethren whose souls had fed His strength"),
 "M646h": ("Dissidents gave their life energies to create Hydaelyn.", "A Greater Purpose", "These dissidents surrendered their life energies in the creation of Hydaelyn, an incarnation of their opposing belief."),
 "M646i": ("Emet-Selch has ever championed the will of Zodiark, and will pay any price for their return.", "A Greater Purpose", "Emet-Selch has ever been a champion for the will of Zodiark. … He will pay the price for our return by whatever means necessary."),
 "M646j": ("Ardbert's shade appears, and Hythlodaeus says you and he were once one.", "A Greater Purpose", "Ardbert's shade appears. … In our time, the two of you were one - the color of your souls tells the tale."),
 "M646k": ("Y'shtola reasons the Ascians mean to sacrifice the Source's lives to Zodiark after the final Rejoining.", "A Greater Purpose", "following the final Rejoining, the Ascians mean to draw on the lives of the Source to make their sacrifice to Zodiark."),
 "M646l": ("Alisaie says they need to find Emet-Selch.", "A Greater Purpose", "We need to find him, [Forename]."),
 # cp-shb-5-0, after the 5.0 finale (MSQ #647)
 "M647a": ("Alisaie vows to press on, however long and however much it hurts.", "Shadowbringers", "Alisaie vows to press on, no matter how long it takes or how much it hurts."),
 "M647b": ("Alisaie believes that if they keep going, they may find a way to save you.", "Shadowbringers", "If we keep taking that next step forward, there's a chance we'll find a way to save you."),
 "M647c": ("Ryne, gripped by doubt, is convinced to trust her chosen path.", "Shadowbringers", "Unlike your fellow Scions, Ryne seems gripped by doubt and feelings of powerlessness. After some encouragement, however, you convince her to trust in the path she has chosen."),
 "M647d": ("Emet-Selch belittles the fragmentary lives of the Source and challenges you to prove yourself worthy of his people's legacy.", "Shadowbringers", "The Ascian belittles the value of the fragmentary lives which now populate the Source and its reflections, challenging you to prove yourself worthy of his people's legacy."),
 "M647e": ("You wade into the flames of the Final Days of Amaurot.", "Shadowbringers", "you steel yourself to wade into the infernal flames of the Final Days of Amaurot"),
 "M647f": ("The Light within you breaks its bonds, and Emet-Selch seems to have won.", "Shadowbringers", "you are powerless to prevent the Light within from breaking its bonds, and you slump to the ground in agony. Emet-Selch has won."),
 "M647g": ("Ardbert lends you strength, and the Exarch appears and summons reinforcements.", "Shadowbringers", "But then Ardbert is there at your side, and with his hand at your back, you find the strength to take another step. Emet-Selch's disbelief is compounded as the Exarch appears and intones a spell to bring you further reinforcements."),
 "M647h": ("Emet-Selch casts aside his mortal form and reveals his true name, Hades.", "Shadowbringers", "the Ascian casts aside his mortal form, and reveals to you his true name─Hades"),
 "M647i": ("He proclaims himself Hades, who shall wake his brethren from their slumber.", "Shadowbringers", "I am Hades! He who shall awaken our brethren from their dark slumber!"),
 "M647j": ("Your axe of Light shatters Emet-Selch's bound soul.", "Shadowbringers", "the axe of incandescent Light shatters the bound soul of Emet-Selch"),
 "M647k": ("His last words ask you to remember that they once lived.", "Shadowbringers", "Remember...that we once lived..."),
 "M647l": ("Y'shtola and Ryne declare your soul free of the Wardens' taint.", "Shadowbringers", "both Y'shtola and Ryne declare your soul free of the Wardens' taint"),
 "M647m": ("The Exarch proclaims the First saved, and the Eighth Umbral Calamity no longer threatens the Source.", "Shadowbringers", "the Exarch proclaims that the First is saved, and that the Eighth Umbral Calamity no longer threatens the Source"),
 "M647n": ("With the Exarch alive, the summoned Scions are stuck in the First.", "Shadowbringers", "it would seem the summoned Scions are stuck in the First"),
 "M647o": ("Your comrades urge you to go back alone, and you step through to bring word to Tataru.", "Shadowbringers", "your comrades urge you to head back alone. Once the portal is prepared, you step through without further hesitation, eager to bring word of your success to Tataru."),
 "M647p": ("Your early return surprises Tataru, who bids you rest while she checks the front and contacts a surprise helper.", "Shadowbringers", "your unexpectedly early return catches Tataru entirely off guard. … Wishing to confirm the current news from the front line, as well as contact her “surprise” helper, Tataru bids you take your ease for the moment"),
 "M647q": ("Emet-Selch says that once the worlds are rejoined, Zodiark will regain His strength and shatter His prison.", "Shadowbringers", "Once the rejoining of worlds is complete, Zodiark will regain His full strength and shatter His prison."),
 "M647r": ("On the moon, Elidibus says Emet-Selch and Lahabrea are gone and he alone remains.", "Shadowbringers", "Emet-Selch...gone. Lahabrea...gone. I alone remain─the last of the unbroken."),
 "M647s": ("Elidibus means to keep the heroes mired in the First.", "Shadowbringers", "I will keep these “heroes” mired in the First, and victory will be ours at the last."),
 "M647t": ("Elidibus admits Zenos overpowered him, though he wore Zenos's body.", "Shadowbringers", "Ah, Zenos. Never did I dream you could overpower me so completely, possessed as I was of your body"),
 "M647u": ("Estinien and Gaius slip into the imperial palace with the Shadowhunters.", "Shadowbringers", "Estinien, Gaius, and the Shadowhunters notice several dead guards in the palace hallway."),
 "M647v": ("Zenos says the Ascian shed his skin and fled, and his body and soul are reunited.", "Shadowbringers", "The craven shed this skin and fled rather than face me. … Body and soul, reunited at last!"),
 "M647w": ("Zenos kills Emperor Varis for interfering with his hunt.", "Shadowbringers", "Any and all who interfere with my hunt... … Zenos kills Varis"),
 "M647x": ("Gaius charges at Zenos.", "Shadowbringers", "Gaius charges at Zenos."),
 "M647y": ("The Exarch is alive, and the Scions are still stuck in the First.", "Shadowbringers", "Yet I am very much alive, and you are still stuck here in the First."),
 "M647z": ("Zenos has no wish to rule; he came to remove what spoils his sport.", "Shadowbringers", "I came only to remove that which ruins my sport."),
 "M647aa": ("Alphinaud is eager to go on at your side.", "Shadowbringers", "Alphinaud is eager to continue along the road, and behold more miracles at your side."),
 "M647ab": ("Thancred promises to guard your back.", "Shadowbringers", "Thancred seizes upon the chance to express his appreciation for all you have done, and promises to guard your back during the coming battle."),
 "M647ac": ("Y'shtola implores you to do as your heart decrees.", "Shadowbringers", "Y'shtola would repay you for all the support you have given her, and implores you to do as your heart decrees."),
 "M647ad": ("Urianger would go with you into peril and see you survive.", "Shadowbringers", "Urianger would sally forth with you into the jaws of peril, and see you survive “unto the morrow.”"),
 "M647ae": ("Ardbert asks whether you could take another step and save your worlds.", "Shadowbringers", "If you had the strength to take another step, could you do it? … Could you save our worlds?"),
 "M647af": ("Norvrandt hails you as heroes, and the Crystarium celebrates beneath a clear sky.", "Shadowbringers", "you and your companions are given a hero's welcome by the people of Norvrandt. The Crystarium erupts in celebration, and you enter the city beneath a blessedly clear sky."),
 "M647ag": ("Varis says Elidibus is gone, having torn a hole into the rift.", "Shadowbringers", "Elidibus is gone... Tore a hole into the rift..."),
}

# ---- Entities: the 5.0 cast under the contract's IDs (merged by id with parts 1 and 2), plus this era's own --------
ENTITIES = {
 # recurring from earlier eras (same id and category merge)
 "char-alphinaud": "character", "char-alisaie": "character", "char-thancred": "character", "char-urianger": "character",
 "char-yshtola": "character", "char-elidibus": "character", "char-zenos": "character", "char-varis": "character",
 "char-gaius": "character", "char-estinien": "character", "char-tataru": "character", "char-lahabrea": "character", "org-scions": "organization", "org-ascians": "organization",
 # the 5.0 cast (parts 1 and 2 may also define these, under the same ids)
 "char-ryne": "character", "char-crystal-exarch": "character", "char-emet-selch": "character", "char-ardbert": "character",
 "char-lyna": "character", "char-vauthry": "character", "char-ranjit": "character", "char-kai-shirr": "character",
 "char-tristol": "character", "char-chai-nuzz": "character", "char-dulia-chai": "character", "char-feo-ul": "character",
 "loc-the-first": "location", "loc-crystarium": "location", "loc-eulmore": "location", "loc-crystal-tower": "location",
 "org-lightwardens": "organization", "char-zodiark": "character",
 # new in this era
 "char-xamott": "character", "char-korutt": "character", "char-grenoldt": "character", "char-tolshs-aath": "character",
 "char-hythlodaeus": "character", "char-graha-tia": "character", "char-hades": "character",
 "loc-the-tempest": "location", "loc-amaurot": "location", "org-convocation-of-fourteen": "organization",
 "evt-the-last-foothold": "event", "evt-a-talos-for-mt-gulg": "event", "evt-the-final-warden": "event",
 "evt-beneath-the-tempest": "event", "evt-amaurot": "event",
}

# ---- Presentations ---------------------------------------------------------------------------------------------------
PRES = {
 # -- The Scions
 "char-ryne": [
   P(N621, None, "main", "Ryne",
     "A girl who left for Nabaath Areng as Minfilia and came back as Ryne, welcomed by the Scions as one of their own. "
     "Alisaie wonders how she can wield the Oracle's power so soon, but the Lightwardens' presence is now unmistakable to her, and she led you to the one hiding beneath Malikah's Well.",
     ["M621a", "M621k", "M621c", "M621b"], ["Minfilia"]),
   P(N622, None, "main", "Ryne",
     "A Scion who carries the Oracle's power. She saw that you absorbed the slain Warden's aether, and that the Light within you has grown monstrous. "
     "She can hold it back but not put it out: even Minfilia, at her strongest, could only hold it back.",
     ["M621a", "M621k", "M622a", "M622c"], ["Minfilia"]),
   P(N624, None, "main", "Ryne",
     "A Scion who carries the Oracle's power. In Gatetown she recognized meol as sin eater flesh, and in Eulmore she saw that Lord Vauthry himself is the last Lightwarden, part man and part sin eater. "
     "She alone can undo his hold over the enthralled, and is tending them one by one.",
     ["M624b", "M624g", "M624i"], ["Minfilia"]),
   P(N636, None, "main", "Ryne",
     "A Scion who carries the power Minfilia entrusted to her, and who has promised to keep that legacy. When you could not contain the Wardens' combined Light, she stayed its raging. "
     "Only her power keeps you from turning into a sin eater, and only for a time.",
     ["M625b", "M636t", "M636f", "M636k"], ["Minfilia"]),
   P(N639, None, "main", "Ryne",
     "A Scion who carries Minfilia's legacy and holds back the Light within you, though she warns it won't last forever. She objected to your going on to the Tempest in your condition, "
     "but in the end she and the others are going with you.",
     ["M625b", "M639o", "M639m"], ["Minfilia"]),
   P(MS, None, "main", "Ryne",
     "A Scion who carries Minfilia's legacy. Gripped by doubt before the Capitol, she chose to trust her path, and after the battle she and Y'shtola declared your soul free of the Wardens' taint. "
     "With the Exarch alive, she and the other Scions remain in the First.",
     ["M625b", "M647c", "M647l", "M647n"], ["Minfilia"]),
 ],
 "char-alisaie": [
   P(N621, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion fighting the Light in Norvrandt. She was with you and Ryne when the Lightwarden beneath Malikah's Well fell, and of all the Scions was the most moved when the night sky returned.",
     ["M621a", "M621e", "M621f"]),
   P(N627, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion. She rode the restored Ladder with her brother and you, its first riders in twenty years, and then spotted someone slipping out of a village thought abandoned, which led you to Amity.",
     ["M627a", "M627h", "M627i"]),
   P(N633, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion. To raise workers for the giant Talos she called on those who believe in the Warrior of Darkness, and now stands guard with the soldiers over the volunteers at Top Rung.",
     ["M629a", "M633e", "M633g"]),
   P(N639, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion. When Ryne objected to your going on to the Tempest in your condition, Alisaie argued passionately for it, and the Scions are going with you.",
     ["M639m", "M639n"]),
   P(N644, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion who never quite believed Emet-Selch's tales. In the vast enchanted city beneath the Tempest she sees their proof.",
     ["M644h", "M644i", "M644j"]),
   P(MS, None, "main", "Alisaie",
     "Alphinaud's twin, a Scion who vowed to keep going, however long it takes, until a way to save you is found. With the Exarch alive, she and the other Scions remain in the First.",
     ["M647a", "M647b", "M647n"]),
 ],
 "char-alphinaud": [
   P(N623, None, "main", "Alphinaud",
     "A young Scion, Alisaie's twin, fighting the Light in Norvrandt. He saw a reflection of himself in Lord Vauthry's self-righteousness, and the Scions gathered in Wright before the push into Kholusia.",
     ["M623j", "M623l"]),
   P(N625, None, "main", "Alphinaud",
     "A young Scion. He suspected Eulmore deliberately turns citizens who outlive their usefulness into sin eaters, and he told the freed Eulmorans the truth: Vauthry is a sin eater, his promises were lies, "
     "and they gave themselves to his city's pleasures of their own free will.",
     ["M624c", "M625c", "M625d"]),
   P(N641, None, "main", "Alphinaud",
     "A young Scion. Beneath the Tempest he met the Ondo, whom the Scions had not known lived there, and found his old trading partner, Paushs Ooan. "
     "The water the Scions drove off was the Ondo's, and he means to make amends.",
     ["M641b", "M641f", "M641h"]),
   P(MS, None, "main", "Alphinaud",
     "A young Scion, eager to go on at your side. With the Exarch alive, he and the other Scions remain in the First.",
     ["M647aa", "M647n"]),
 ],
 "char-thancred": [
   P(N621, None, "main", "Thancred",
     "A Scion who went with Ryne and the others to slay the Lightwarden beneath Malikah's Well. With Kholusia now the Light's last foothold, he expects Lord Vauthry, who waits there, to do everything in his power to thwart them.",
     ["M621a", "M621g", "M621i"]),
   P(N625, None, "main", "Thancred",
     "A Scion who, after the battle in Eulmore, had the enthralled dosed with dream powder to keep them calm while Ryne undoes Vauthry's hold.",
     ["M624i", "M625a"]),
   P(N629, None, "main", "Thancred",
     "A Scion. To build the giant Talos that will seize the floating volcano, he went to ask the miners of Amh Araeng for help, to recruit help.",
     ["M629a", "M629g"]),
   P(N641, None, "main", "Thancred",
     "A Scion who leads the search across the Tempest's drained sea floor, following the slope down toward the trenches for a formation big enough to house Emet-Selch's stronghold.",
     ["M640d", "M641a"]),
   P(MS, None, "main", "Thancred",
     "A Scion who promised to guard your back in the battle with Emet-Selch. With the Exarch alive, he and the other Scions remain in the First.",
     ["M647ab", "M647n"]),
 ],
 "char-yshtola": [
   P(N621, None, "main", "Y'shtola",
     "A Scion who surveyed Malikah's Well, a site abandoned after the Flood, and suspected the Lightwarden hid there; you slew it in the well's depths. Kholusia, she says, is the last refuge of Light.",
     ["M621l", "M621d", "M621e", "M621j"]),
   P(N622, None, "main", "Y'shtola",
     "A Scion. The Light within you has grown, and she warns it will only get worse if nothing is done; for that, the Scions must rely on Urianger and his secrets.",
     ["M622a", "M622b", "M622d"]),
   P(N629, None, "main", "Y'shtola",
     "A Scion. Since the floating volcano will not come down, she proposed a Talos large enough to seize it, and told Chai-Nuzz that Norvrandt is counting on him.",
     ["M629a", "M629b"]),
   P(N634, None, "main", "Y'shtola",
     "A Scion who oversees the imbuing of the giant Talos in Amity. When the ore fell short, the Night's Blessed gave their heartstones, bearing their hope that none shall be sacrificed to sin eaters again. "
     "She reminded Urianger of his promise to have measures ready if you cannot contain the Light.",
     ["M634a", "M634c", "M634d", "M634e"]),
   P(N636, None, "main", "Y'shtola",
     "A Scion who saw through the Exarch's claim that he would carry your Light to another world: he meant to take it into the rift and die there, and Urianger knew.",
     ["M636g", "M636q", "M636r"]),
   P(N642, None, "main", "Y'shtola",
     "A Scion. She found ruins beneath the Tempest finer than anything the Ronkan Empire made, and believes Emet-Selch chose them for the Ascian agenda. "
     "She is almost certain he lit the illuminated land the Ondo speak of, and that winning the Ondo's trust is the swiftest way there.",
     ["M642b", "M642d", "M642e", "M642f"]),
   P(N646, None, "main", "Y'shtola",
     "A Scion. From what you learned in Amaurot she reasons that, after the final Rejoining, the Ascians mean to sacrifice the lives of the Source to Zodiark.",
     ["M646f", "M646k"]),
   P(MS, None, "main", "Y'shtola",
     "A Scion who implored you to do as your heart decrees, and who, with Ryne, declared your soul free of the Wardens' taint. With the Exarch alive, she and the other Scions remain in the First.",
     ["M647ac", "M647l", "M647n"]),
 ],
 "char-urianger": [
   P(N626, None, "main", "Urianger",
     "A Scion with secrets of his own, on whom the others must rely to deal with the Light within you. He oversees the Ladder's repair, and says the people now stand united against the world's fate.",
     ["M622d", "M626a", "M626e"]),
   P(N634, None, "main", "Urianger",
     "A Scion who has measures ready in case you cannot contain the Light, though he will not say what they are.",
     ["M622d", "M634e"]),
   P(N636, None, "main", "Urianger",
     "A Scion who knew the Exarch meant to take your Light into the rift and die, and begged the others not to interfere.",
     ["M636g", "M636r"]),
   P(N639, None, "main", "Urianger",
     "A Scion. An Echo showed him agreeing to be the Exarch's accomplice: to hide the truth from the other Scions and keep them from stopping his self-sacrifice. "
     "Urianger has now told them everything, and hints at an easier way to the ocean floor.",
     ["M639b", "M639i", "M639n", "M639q"]),
   P(N640, None, "main", "Urianger",
     "A Scion who sought the aid of a fae being he had never met: Bismarck, the Isle of Ken, which carried you to the ocean floor. He reasons that Emet-Selch is still in the Tempest, since the Exarch's body is the key to the Crystal Tower's power over time.",
     ["M640g", "M640a", "M640d", "M640e"]),
   P(N645, None, "main", "Urianger",
     "A Scion who sees the city in the trench as a memory Emet-Selch has raised from before the star was sundered, its people facing the Final Days that set Zodiark's and Hydaelyn's summoning in motion.",
     ["M645c", "M645d"]),
   P(MS, None, "main", "Urianger",
     "A Scion who went with you into the jaws of peril. With the Exarch alive, he and the other Scions remain in the First.",
     ["M647ad", "M647n"]),
 ],
 "org-scions": [
   P(N621, None, "main", "The Scions of the Seventh Dawn",
     "An order whose members fight the Light in Norvrandt. They welcomed Ryne, who left as Minfilia, into their ranks, and with her slew the Lightwarden of Amh Araeng.",
     ["M621a", "M621e"]),
   P(N635, None, "main", "The Scions of the Seventh Dawn",
     "An order whose members are no longer in the Source. In the imperial palace, the one wearing Zenos's body plans to defeat the Alliance before they return.",
     ["M635j", "M635d", "M635e"]),
   P(MS, None, "main", "The Scions of the Seventh Dawn",
     "An order whose members saved the First beside you. Because the Exarch lives, those he summoned are stuck there, and they urged you to go home alone.",
     ["M647m", "M647n", "M647o"]),
 ],
 # -- The Crystarium and its steward
 "char-crystal-exarch": [
   P(N622, None, "main", "The Crystal Exarch",
     "The Crystal Exarch, who asks one thing of you: survive what is to come, no matter what, and when the dust settles return to your own world. "
     "Only the final Lightwarden, he says, stands between them and victory, and he will look for a remedy for your affliction.",
     ["M622h", "M622i", "M622j"], ["The Exarch", "The enigmatic figure"]),
   P(N623, None, "main", "The Crystal Exarch",
     "The Crystal Exarch, who called you to the Ocular to plan the hunt for Kholusia's Lightwarden: four have been vanquished, returning night to much of Norvrandt. Lyna, his captain, brought word of Eulmore entrenching.",
     ["M623a", "M623b", "M623h", "M623m"], ["The Exarch", "The enigmatic figure"]),
   P(N628, None, "main", "The Crystal Exarch",
     "The Crystal Exarch, who came to Kholusia to observe the final struggle with his own eyes. The Allagan drones lost over the floating volcano, he says, served their purpose. Emet-Selch wonders why he never shows what hides beneath his cowl.",
     ["M627e", "M628b", "M628c", "M628d"], ["The Exarch", "The enigmatic figure"]),
   P(N632, None, "main", "The Crystal Exarch",
     "The Crystal Exarch, who went with you to the Tholls for the giant Talos's heart. In the Duergar's Tewel he made Korutt invisible and put the Goggs to sleep, but he grows weak this long away from the Crystarium.",
     ["M630b", "M632a", "M632b", "M632e"], ["The Exarch", "The enigmatic figure"]),
   P(N635, None, "main", "The Crystal Exarch",
     "The Crystal Exarch, who made himself one with the Crystal Tower so that he might live indefinitely. As an extension of the tower, he weakens the farther he travels and the longer he is away.",
     ["M635a", "M635b", "M635c"], ["The Exarch", "The enigmatic figure"]),
   P(N636, None, "main", "The Crystal Exarch",
     "The Crystal Exarch, who meant all along to take the Wardens' Light from you and carry it into the rift, dying in your place. His hood fell back, and then Emet-Selch shot him "
     "and left with him, still alive, inviting you to the Tempest. Only one of the Allagan royal line, Emet-Selch says, can control the Crystal Tower.",
     ["M636g", "M636p", "M636h", "M636i", "M636o", "M636n"], ["The Exarch", "The enigmatic figure"]),
   P(N637, None, "main", "The Crystal Exarch",
     "The Crystal Exarch, the Crystarium's steward, whom Emet-Selch shot and carried off. With you awake, the city hopes the search for him can begin in earnest.",
     ["M636i", "M637d"], ["The Exarch", "The enigmatic figure"]),
   P(N638, None, "main", "The Crystal Exarch",
     "The Crystarium's stolen steward, who became known to the refugees in Lakeland soon after the Crystal Tower appeared. He raised Lyna after eaters killed her parents, lets no one else dwell in the spire, "
     "and no one knows his true name. Lyna believes he knew a terrible fate awaited him.",
     ["M637d", "M638h", "M638g", "M638e", "M638i", "M638k"], ["The Exarch", "The enigmatic figure"]),
   P(N639, None, "main", "The Crystal Exarch",
     "The Crystarium's steward, held by Emet-Selch. He is G'raha Tia, who came from the Source of a later age to unmake the Calamity that devastated it.",
     ["M639a", "M639c", "M639d"], ["The Exarch", "The enigmatic figure"]),
 ],
 "char-graha-tia": [
   P(N639, None, "main", "G'raha Tia",
     "The Crystal Exarch's true name. He is a native of the Source in an age beyond yours, after the Eighth Umbral Calamity devastated the star; generations later his people woke the Crystal Tower and roused him, its caretaker, "
     "and he crossed to the First, almost a century early, to unmake that Calamity and spare your life. He meant to absorb the Lightwardens' aether and die. Emet-Selch shot him and holds him prisoner.",
     ["M639a", "M639c", "M639d", "M639e", "M639f", "M639g", "M636i"], ["The Crystal Exarch", "The Exarch"]),
   P(N640, None, "main", "G'raha Tia",
     "The Crystal Exarch, a native of the Source's future who came to the First to save you. Emet-Selch holds him in the Tempest, Urianger reasons, because his body is the key to the Crystal Tower and its power to travel through time.",
     ["M639a", "M639d", "M640d", "M640e"], ["The Crystal Exarch", "The Exarch"]),
   P(N644, None, "main", "G'raha Tia",
     "The Crystal Exarch, a native of the Source's future who came to the First to save you. Emet-Selch holds him captive somewhere in the enchanted city beneath the Tempest.",
     ["M639a", "M639d", "M644i"], ["The Crystal Exarch", "The Exarch"]),
   P(MS, None, "main", "G'raha Tia",
     "The Crystal Exarch, a native of the Source's future. He appeared, alive, at the height of the battle with Emet-Selch and summoned reinforcements to your side. "
     "Back in the Crystarium he proclaimed the First saved and the Eighth Umbral Calamity averted, but his survival leaves the Scions stuck in the First.",
     ["M639d", "M647g", "M647m", "M647n", "M647y"], ["The Crystal Exarch", "The Exarch"]),
 ],
 "char-lyna": [
   P(N623, None, "main", "Lyna",
     "The Crystal Exarch's captain. Her informant in Kholusia reports Eulmore's forces entrenching at key points throughout the city.",
     ["M623m", "M623h"], ["Captain Lyna"]),
   P(N638, None, "main", "Lyna",
     "Captain under the Crystal Exarch, who raised her after eaters killed her parents when she was a baby. He left her access to the Umbilicus, to wake the city's barrier if eaters ever attacked, "
     "and she believes he knew a terrible fate awaited him.",
     ["M623m", "M638g", "M638j", "M638k"], ["Captain Lyna"]),
   P(N639, None, "main", "Lyna",
     "The guard captain raised by the Exarch. She unlocked the Umbilicus for you, and when you asked the most direct way to the Tempest, she sent you to the tamers at the Amaro Launch.",
     ["M638g", "M639j", "M639l"], ["Captain Lyna"]),
 ],
 "loc-crystarium": [
   P(N624, None, "main", "The Crystarium",
     "The Crystal Exarch's city, whose informant in Gatetown, feeding it secrets, turns out to be your old friend Kai-Shirr.",
     ["M624d", "M623h"]),
   P(N637, None, "main", "The Crystarium",
     "A city whose steward, the Crystal Exarch, has been stolen away. Its citizens are anxious about the Light's return, its Crystalline Mean prepares for battle against an unknown foe, and trade with Eulmore has resumed.",
     ["M637a", "M637d", "M637e", "M637b"]),
   P(N639, None, "main", "The Crystarium",
     "A city around the Crystal Tower, whose stolen steward is G'raha Tia. Its citizens have long suspected you are the Warrior of Darkness, and they back your journey to the Tempest.",
     ["M637d", "M639a", "M639m"]),
   P(MS, None, "main", "The Crystarium",
     "A city around the Crystal Tower. It erupted in celebration when you returned beneath a clear sky, and there the Exarch proclaimed the First saved.",
     ["M647af", "M647m"]),
 ],
 "loc-crystal-tower": [
   P(N635, None, "main", "The Crystal Tower",
     "A tower with which the Crystal Exarch made himself one, so that he might live indefinitely; he weakens the farther he goes from it.",
     ["M635b", "M635c"]),
   P(N638, None, "main", "The Crystal Tower",
     "A tower that appeared less than a decade after the Flood, summoned by the Crystal Exarch, who lets no one else dwell in its spire. He once said it might vanish as suddenly as it came. "
     "Only one of the Allagan royal line, Emet-Selch says, can control it.",
     ["M638h", "M638e", "M638f", "M636n"]),
   P(N639, None, "main", "The Crystal Tower",
     "A tower woken in the Source of a later age and sent back to the First, with its caretaker, G'raha Tia, to unmake the Eighth Umbral Calamity. Its heart is the Umbilicus.",
     ["M639d", "M639e", "M639j"]),
 ],
 "char-kai-shirr": [
   P(N624, None, "main", "Kai-Shirr",
     "An old friend of yours from Gatetown, who has been the informant feeding secrets to the Crystarium.",
     ["M624d"]),
   P(N633, None, "main", "Kai-Shirr",
     "An old friend from Gatetown, and the Crystarium's informant there. He has yet to repay you and Alphinaud for saving him, and came to Top Rung to work on the giant Talos.",
     ["M624d", "M633f", "M633d"]),
 ],
 # -- Eulmore and its lord
 "char-vauthry": [
   P(N621, None, "main", "Vauthry",
     "Lord Vauthry, of Kholusia, the last land where the Light holds sway. Thancred expects him to do everything in his power to thwart the Scions.",
     ["M621g", "M621i"], ["Lord Vauthry"]),
   P(N623, None, "main", "Vauthry",
     "Lord Vauthry of Eulmore, whose forces are entrenching in the city where the last Lightwarden likely hides. Alphinaud saw a reflection of himself in his self-righteousness, and on the road to Gatetown people move as if in a trance.",
     ["M623h", "M623i", "M623j", "M623k"], ["Lord Vauthry"]),
   P(N624, None, "main", "Vauthry",
     "Lord Vauthry of Eulmore, who controls his people's minds through meol made of sin eater flesh. He is the last Lightwarden, part man and part sin eater, and admits no justice, future or will but his. "
     "When you reached his chamber he sprouted wings and fled to the floating peak of Mt. Gulg.",
     ["M624a", "M624b", "M624g", "M624j", "M624h"], ["Lord Vauthry"]),
   P(N625, None, "main", "Vauthry",
     "Lord Vauthry, the last Lightwarden, who has fled to the floating peak of Mt. Gulg. Alphinaud has told the Eulmorans freed from his hold that he is a sin eater, and that everything he promised was a lie.",
     ["M624g", "M624h", "M625c", "M625h"], ["Lord Vauthry"]),
   P(N636, None, "main", "Vauthry",
     "Lord Vauthry, the last Lightwarden, whom you slew atop the volcano in his final form, Innocence; you took his light into yourself. He was an Ascian pawn: "
     "Emet-Selch gave a Lightwarden's power to him in his mother's womb, born man and sin eater both, a king to rule over all.",
     ["M636b", "M636c", "M636d", "M636e", "M636j", "M636u"], ["Lord Vauthry", "Innocence"]),
 ],
 "char-ranjit": [
   P(N624, None, "main", "Ran'jit",
     "An old Eulmoran soldier who said he had been nothing but a weapon since he submitted to his master's authority. He confronted you alone in Eulmore's Canopy, and you struck him down.",
     ["M624e", "M624f"], ["General Ran'jit"]),
 ],
 "loc-eulmore": [
   P(N623, None, "main", "Eulmore",
     "Lord Vauthry's city in Kholusia, where his forces are entrenching and the last Lightwarden likely hides.",
     ["M623h", "M623i"]),
   P(N624, None, "main", "Eulmore",
     "Lord Vauthry's city in Kholusia, whose staple, meol, is sin eater flesh that leaves its eaters open to his control. You stormed it, and he fled to the floating peak of Mt. Gulg.",
     ["M624b", "M624a", "M624h"]),
   P(N625, None, "main", "Eulmore",
     "A city freed from Lord Vauthry's hold, whose people Alphinaud told the truth: their lord is a sin eater, and they gave themselves to his pleasures of their own free will.",
     ["M624i", "M625c", "M625d"]),
   P(N637, None, "main", "Eulmore",
     "A city freed from Lord Vauthry, now trading with the Crystarium again.",
     ["M625c", "M637b"]),
 ],
 "char-chai-nuzz": [
   P(N625, None, "main", "Chai-Nuzz",
     "Dulia-Chai's husband, heir to Daedalus Stoneworks, foremost makers of Talos. He agreed to look at the Talos that drives the Ladder, but promises nothing.",
     ["M625f", "M625g"]),
   P(N629, None, "main", "Chai-Nuzz",
     "Heir to Daedalus Stoneworks, on whom Norvrandt counts to build a Talos big enough to seize the floating volcano. In Amity he admitted that Eulmore wronged Tristol terribly, and won his help; "
     "the Talos still needs a heart, and a congregation of mages to wake it.",
     ["M629b", "M629e", "M629f", "M629h", "M629i"]),
   P(N634, None, "main", "Chai-Nuzz",
     "Heir to Daedalus Stoneworks, building the giant Talos. Nigh everyone in Norvrandt rallied to the work, and when the Exarch's ore fell short, the Night's Blessed gave their heartstones.",
     ["M629b", "M633a", "M634b", "M634g"]),
 ],
 "char-dulia-chai": [
   P(N625, None, "main", "Dulia-Chai",
     "A Eulmoran whose husband, Chai-Nuzz, is heir to Daedalus Stoneworks. She urged him to look at the Talos that drives the Ladder.",
     ["M625f", "M625g"]),
 ],
 # -- Kholusia
 "char-tristol": [
   P(N627, None, "main", "Tristol",
     "The young artist whose life you saved in Kholusia. A local led him through a secret tunnel to the top of the Bright Cliff, where he lives in Amity among Eulmore's exiles, and he has promised to help you reach Vauthry.",
     ["M627i", "M627j"]),
   P(N629, None, "main", "Tristol",
     "An artist of Amity, a settlement of Eulmore's exiles. Eulmore ignored his pleas and cast him out, and Chai-Nuzz admits it all but sent him to his death; once Chai-Nuzz owned the wrong, Tristol agreed to cooperate.",
     ["M627i", "M629c", "M629d", "M629e", "M629f"]),
   P(N630, None, "main", "Tristol",
     "An artist of Amity who is helping you reach Vauthry. A Tholl showed him the secret tunnel to the clifftop, and he sent you and the Exarch to their village, Tomra, for ore.",
     ["M627i", "M630e", "M630b"]),
 ],
 "char-xamott": [
   P(N630, None, "main", "Xamott",
     "Chief of the Tholls, a dwarven family who have long mined this land, at Tomra. He made you pass a trial before placing his faith in you, and will help you find ore for the giant Talos's heart, "
     "though the Tholls know no better than you how to deal with the floating volcano.",
     ["M630a", "M630b", "M630c", "M630d", "M630f"], ["Chief Xamott"]),
   P(N631, None, "main", "Xamott",
     "Chief of the Tholls. He told you the ore you need is earthseed, steeped in magick, surest found in the Duergar's Tewel, held by the Tholls' age-old rivals, the Goggs.",
     ["M630d", "M631a", "M631b"], ["Chief Xamott"]),
   P(N633, None, "main", "Xamott",
     "Chief of the Tholls, who helped you find earthseed for the giant Talos. His dwarves modified their spare pickaxes for bigger folk, for the volunteers at Top Rung.",
     ["M630d", "M633b"], ["Chief Xamott"]),
 ],
 "char-korutt": [
   P(N631, None, "main", "Korutt",
     "A young Tholl miner, one of Tomra's finest though hopeless in a fight, who volunteered to guide you to the Duergar's Tewel for earthseed.",
     ["M631c", "M631d", "M631f"]),
   P(N632, None, "main", "Korutt",
     "A young Tholl miner who, made invisible by the Exarch, dug the earthseed from the Goggs' cave. Glagg, chief of the Goggs, caught him there and accused the Tholls.",
     ["M632a", "M632c", "M632d"]),
   P(N633, None, "main", "Korutt",
     "A young Tholl miner who helped you win the earthseed, and whom you saw safely home to Tomra.",
     ["M633a"]),
 ],
 # -- The fae and the Tempest
 "char-feo-ul": [
   P(N638, None, "main", "Feo Ul",
     "A fae, who bade you ask the Exarch's flowers what they know if you seek word of him.",
     ["M638d"], ["Titania"]),
   P(N640, None, "main", "Feo Ul",
     "A fae whom Bismarck, an ancient fae being, obeys as king. Feo Ul persuaded it to carry you to the bottom of the Tempest.",
     ["M640a", "M640b", "M640f"], ["Titania"]),
 ],
 "loc-the-tempest": [
   P(N636, None, "main", "The Tempest",
     "A realm of dark depths, where Emet-Selch keeps his abode and has invited you to seek him out.",
     ["M636i"]),
   P(N640, None, "main", "The Tempest",
     "An undersea realm where Emet-Selch likely hides with the Exarch. Bismarck carried you to its floor and left you within a dome of air.",
     ["M640c", "M640d"]),
   P(N641, None, "main", "The Tempest",
     "An undersea realm whose waters the Scions' coming drove back, where the Ondo live, believing the ancients made them caretakers of a sanctuary. They have seen an illuminated land shining through the abyss.",
     ["M641b", "M641g", "M641h", "M641c"]),
 ],
 "char-tolshs-aath": [
   P(N641, None, "main", "Tolshs Aath",
     "Chieftain of the Ondo, who live in the Tempest. He has seen an illuminated land shining in the abyss, and will welcome you only if you are the ancients' chosen.",
     ["M641b", "M641c", "M641d"]),
   P(N644, None, "main", "Tolshs Aath",
     "Chieftain of the Ondo, who believe the ancients have risen in a city in the depths. Given Grenoldt's lamp, he named you the sign his people awaited, and lent you a guide to the illuminated land.",
     ["M644d", "M644e", "M644f"]),
 ],
 "char-grenoldt": [
   P(N637, None, "main", "Grenoldt",
     "A craftsman of the Crystarium, unseen since he wandered off some years ago.",
     ["M637g"]),
   P(N643, None, "main", "Grenoldt",
     "A craftsman, long missing from the Crystarium, living in the Tempest. The Ondo asked him for a sacred lamp, but his deadline is long past and his bench untouched. What he needed was inspiration, and you showed him a crystal that belonged to one of Ardbert's companions.",
     ["M637g", "M643b", "M643c", "M643d", "M643e"]),
   P(N644, None, "main", "Grenoldt",
     "A craftsman in the Tempest, whose will to work had been stolen by the perfection of the ancients' works. Inspired again, he made the Ondo's lamp, and offers to weave bittersweet sagas into armaments for you.",
     ["M644a", "M644b", "M644c"]),
 ],
 # -- Ascians, ghosts and gods
 "char-emet-selch": [
   P(N623, None, "main", "Emet-Selch",
     "An Ascian, who declares that driving back the Light will not save the world. As Zodiark and Hydaelyn warred, he says, Her blow sundered all creation into fourteen fragments, and the Ascians resolved to rejoin them, "
     "though their haste made a useless void of the Thirteenth. He calls you a hero of the Source, seven times rejoined.",
     ["M623c", "M623d", "M623e", "M623f", "M623g"], ["Solus"]),
   P(N627, None, "main", "Emet-Selch",
     "An Ascian who longs for the time when the world was whole. He offered you a place as his equal, reminding you that you are of the Source, unlike the halfmen here, "
     "and asked whether the Exarch has ever shown what hides beneath his cowl.",
     ["M627b", "M627c", "M627d", "M627e"], ["Solus"]),
   P(N635, None, "main", "Emet-Selch",
     "An Ascian, who, Elidibus tells Emperor Varis, has gone to the First to usher that world to its end.",
     ["M635f", "M635g"], ["Solus"]),
   P(N636, None, "main", "Emet-Selch",
     "An Ascian who seeks the Great Rejoining. He gave a Lightwarden's power to Vauthry in the womb, and when you could not contain the Wardens' Light he shot the Exarch, who meant to carry it away, "
     "and took him, still alive. He declared you unworthy, all but a sin eater, and invited you to his abode in the Tempest.",
     ["M636j", "M636e", "M636h", "M636o", "M636s", "M636i"], ["Solus"]),
   P(N640, None, "main", "Emet-Selch",
     "An Ascian who holds the Exarch prisoner. Unable to risk the rift with his captive, he is likely somewhere in the Tempest, the last refuge, Ardbert says, of he who denies the Light.",
     ["M636i", "M640d", "M640e", "M640h"], ["Solus"]),
   P(N644, None, "main", "Emet-Selch",
     "An Ascian who holds the Exarch captive in a vast city he has layered over ancient ruins beneath the Tempest: the illuminated land the Ondo saw.",
     ["M642e", "M644h", "M644i"], ["Solus"]),
   P(N646, None, "main", "Emet-Selch",
     "An Ascian who raised Amaurot from memory and approved your residency himself. His old friend Hythlodaeus says he has ever championed the will of Zodiark and will pay any price for his people's return.",
     ["M645d", "M646b", "M646d", "M646i"], ["Solus"]),
   P(MS, None, "main", "Emet-Selch",
     "An Ascian who challenged you to prove yourself worthy of his people's legacy. In the battle that followed he cast aside his mortal form: he is Hades.",
     ["M647d", "M647h"], ["Solus"]),
 ],
 "char-hades": [
   P(MS, None, "main", "Hades",
     "The true name of the Ascian Emet-Selch, who would wake his brethren from their slumber. He nearly won, as the Light within you broke its bonds, until Ardbert and the Exarch turned the fight. "
     "Your axe of Light shattered his bound soul, and his last words asked you to remember that they once lived.",
     ["M647h", "M647i", "M647f", "M647g", "M647j", "M647k"], ["Emet-Selch", "Solus"]),
 ],
 "char-ardbert": [
   P(N622, None, "main", "Ardbert",
     "A shade who lingers in your room. With Minfilia gone, he says, the reason he must suffer this purgatory will forever remain a mystery, though she told him his time had not yet come and he still had a role to play.",
     ["M622e", "M622f", "M622g"]),
   P(N627, None, "main", "Ardbert",
     "A shade who carries the guilt of causing the Flood. Solitude nearly finished him, and he warns you against any choice that leaves you alone. He once rode the Ladder with his comrades, a day no one but he remembers.",
     ["M627f", "M627g", "M627k"]),
   P(N636, None, "main", "Ardbert",
     "A shade who watched over you after you collapsed. He told you why Light shrouds Norvrandt again: the power you absorbed from the Wardens. Only your friends know.",
     ["M636v", "M636m"]),
   P(N638, None, "main", "Ardbert",
     "A shade who, with his comrades, caused the Flood, and who resolved with them to journey to the Source by taking their own lives. He has cast his lot with yours, and if you lose control, he will do his best to stop you.",
     ["M638a", "M638b", "M638c"]),
   P(N646, None, "main", "Ardbert",
     "A shade who has cast his lot with yours. In Amaurot, Hythlodaeus saw him beside you, and said that in his time, the two of you were one.",
     ["M638b", "M646j"]),
   P(MS, None, "main", "Ardbert",
     "A shade who was once one with you. When the Light broke loose and Emet-Selch had all but won, Ardbert was at your side, and with his hand at your back you found the strength to take another step.",
     ["M646j", "M647ae", "M647g"]),
 ],
 "char-hythlodaeus": [
   P(N646, None, "main", "Hythlodaeus",
     "A shade in Amaurot who knows he is part of a recreation, and was once Emet-Selch's close friend. He told you how half his people gave their lives to create Zodiark and dissenters made Hydaelyn, "
     "and that you and Ardbert were once one.",
     ["M646c", "M646d", "M646f", "M646h", "M646j"]),
 ],
 "loc-amaurot": [
   P(N645, None, "main", "Amaurot",
     "A city in the depths of the Tempest, a memory Emet-Selch has raised from before the star was sundered, whose people, arcane entities to Y'shtola's eyes, believe they face the end of the world.",
     ["M645j", "M645d", "M645b", "M645h"]),
   P(N646, None, "main", "Amaurot",
     "A city Emet-Selch has recreated from memory, where he approved your residency himself. Its Convocation is sequestered in the Capitol, admitting no one without a writ.",
     ["M645d", "M646b", "M646a"]),
   P(MS, None, "main", "Amaurot",
     "A recreated city, where you passed through the flames of its Final Days to face Emet-Selch.",
     ["M645d", "M647e"]),
 ],
 "org-convocation-of-fourteen": [
   P(N645, None, "main", "The Convocation of Fourteen",
     "The council of Amaurot, whose seats are held by elected sages, among them its speaker, Lahabrea, and its emissary, Elidibus. Rumor says it will invoke its mightiest spells of creation.",
     ["M645f", "M645g"]),
   P(N646, None, "main", "The Convocation of Fourteen",
     "The council of Amaurot. When the Final Days came, it set out to create a will for the star, and nearly half the living gave their lives to make Zodiark.",
     ["M645f", "M646e", "M646f"]),
 ],
 "org-ascians": [
   P(N623, None, "main", "The Ascians",
     "A group who, looking on the shattered remains of their home after Hydaelyn's blow sundered creation, resolved to rejoin the worlds.",
     ["M623d", "M623e", "M623f"]),
   P(N636, None, "main", "The Ascians",
     "A group who seek the Great Rejoining. Lord Vauthry was their pawn, born man and sin eater both to bring it about in the First.",
     ["M636d", "M636j"]),
   P(N646, None, "main", "The Ascians",
     "A group who, Y'shtola reasons, mean to sacrifice the lives of the Source to Zodiark once the worlds are rejoined.",
     ["M646i", "M646k"]),
   P(MS, None, "main", "The Ascians",
     "A group whose last unbroken member, Elidibus, says Emet-Selch and Lahabrea are gone.",
     ["M647r"]),
 ],
 "char-zodiark": [
   P(N623, None, "main", "Zodiark",
     "A power that warred with Hydaelyn, who unmade Him with a single blow and sundered all creation into fourteen fragments.",
     ["M623o", "M623d"]),
   P(N645, None, "main", "Zodiark",
     "A power whose summoning was set in motion by a catastrophe called the Final Days, and who was sundered by Hydaelyn's blow.",
     ["M645c", "M623d"]),
   P(N646, None, "main", "Zodiark",
     "A power born when nearly half of the ancients who still lived gave their lives for salvation. He was to restore the souls that fed Him, and Emet-Selch has ever championed His will.",
     ["M646f", "M646g", "M646i"]),
   P(MS, None, "main", "Zodiark",
     "A power born of the ancients' sacrifice. Once the worlds are rejoined, Emet-Selch said, He will regain His full strength and shatter His prison.",
     ["M646f", "M647q"]),
 ],
 "char-lahabrea": [
   P(N645, None, "main", "Lahabrea",
     "An Ascian, named by Amaurot's residents as the speaker of the Convocation of Fourteen.",
     ["M645f"]),
   P(MS, None, "main", "Lahabrea",
     "An Ascian, once the Convocation's speaker, whom Elidibus counts among the gone.",
     ["M645f", "M647r"]),
 ],
 "char-elidibus": [
   P(N635, None, "main", "Elidibus",
     "An Ascian who wears Zenos's body. Reporting to Emperor Varis, he said the Scions are gone from the Source, and that Emet-Selch has gone to end the First; a centurion with a katana called him by his name.",
     ["M635d", "M635f", "M635g", "M635h"]),
   P(N645, None, "main", "Elidibus",
     "An Ascian who wears Zenos's body, and who, Amaurot's residents say, is the Convocation of Fourteen's emissary.",
     ["M635g", "M645f"]),
   P(MS, None, "main", "Elidibus",
     "An Ascian, the last of the unbroken now that Emet-Selch and Lahabrea are gone. Zenos overpowered him and took back his body, and Elidibus means to keep the heroes mired in the First.",
     ["M647r", "M647t", "M647s", "M647ag"]),
 ],
 "char-zenos": [
   P(N635, None, "main", "Zenos",
     "The crown prince, whose body Elidibus wears. A centurion bearing a katana said he cares nothing for Zenos's name, but is rather fond of the body.",
     ["M635g", "M635h"]),
   P(MS, None, "main", "Zenos",
     "The crown prince, his body and soul reunited after the Ascian who wore him fled. He killed his father, Emperor Varis, for interfering with his hunt; he came, he said, only to remove what ruins his sport. Gaius charged him.",
     ["M647v", "M647w", "M647z", "M647x"]),
 ],
 "char-varis": [
   P(N635, None, "main", "Varis",
     "The Emperor of Garlemald. The one wearing Zenos's body reports to him that the Scions are gone from the Source and plans to beat the Alliance before they return; Varis asked after Emet-Selch.",
     ["M635d", "M635e", "M635i"], ["Emperor Varis"]),
   P(MS, None, "main", "Varis",
     "The Emperor of Garlemald, killed by his son Zenos with a katana for interfering with his hunt. Dying, he told Gaius that Elidibus is gone.",
     ["M647w", "M647ag"], ["Emperor Varis"]),
 ],
 "char-gaius": [
   P(MS, None, "main", "Gaius",
     "The Black Wolf, who slipped into the imperial palace with Estinien and the Shadowhunters, found Zenos killing Emperor Varis, and charged at him.",
     ["M647u", "M647w", "M647x"], ["the Black Wolf", "Shadowhunter"]),
 ],
 "char-estinien": [
   P(MS, None, "main", "Estinien",
     "A dragoon who entered the imperial palace with Gaius and the Shadowhunters, and found Zenos had killed Emperor Varis.",
     ["M647u", "M647w"]),
 ],
 "char-tataru": [
   P(MS, None, "main", "Tataru",
     "The Scions' receptionist, caught off guard by your early return. She bids you rest while she confirms news from the front and contacts a surprise helper.",
     ["M647o", "M647p"]),
 ],
 "org-lightwardens": [
   P(N621, None, "main", "The Lightwardens",
     "Beings whose Light grips Norvrandt. With each one slain the grip loosens, and since you killed the one beneath Malikah's Well, Kholusia is the Light's last foothold.",
     ["M621e", "M621g"]),
   P(N623, None, "main", "The Lightwardens",
     "Beings whose Light grips Norvrandt. Four have been vanquished, returning night to much of the land, and the last likely hides in Eulmore.",
     ["M623b", "M623i"]),
   P(N624, None, "main", "The Lightwardens",
     "Beings whose Light grips Norvrandt. The last is Lord Vauthry himself, part man and part sin eater, now on the floating peak of Mt. Gulg.",
     ["M623b", "M624g", "M624h"]),
   P(N636, None, "main", "The Lightwardens",
     "Beings whose Light gripped Norvrandt. You slew the last, Lord Vauthry, but could not contain the Wardens' combined power, and the Light shrouds the land again because of what you absorbed.",
     ["M636b", "M636f", "M636m"]),
 ],
 "loc-the-first": [
   P(N621, None, "main", "The world of the First",
     "A world gripped by Light, where the Scions fight on in Norvrandt. With Kholusia the Light's last foothold, its salvation seems within reach.",
     ["M621g", "M621h"]),
   P(N635, None, "main", "The world of the First",
     "A world gripped by Light, where the Scions have gone and to which Emet-Selch has taken himself, to usher it to its end.",
     ["M635d", "M635f"]),
   P(MS, None, "main", "The world of the First",
     "A world saved from the Light, the Exarch proclaims. The Scions he summoned are stuck there, and Elidibus means to keep them mired in it.",
     ["M647m", "M647n", "M647s"]),
 ],
}

# ---- Arc recaps ---------------------------------------------------------------------------------------------------
NA1, NA2, NA3, NA4, NA5 = ("The Last Foothold", "A Talos for Mt. Gulg", "The Final Warden", "Beneath the Tempest", "Amaurot")
PRES.update({
 "evt-the-last-foothold": [
   P(N621, None, "main", NA1,
     "Ryne, who left for Nabaath Areng as Minfilia, has joined the Scions and now senses the Lightwardens plainly. She led you to Malikah's Well, where you slew the Warden and brought night back to Amh Araeng. "
     "Kholusia is the Light's last foothold, and there Lord Vauthry waits to thwart you.",
     ["M621a", "M621c", "M621e", "M621f", "M621g", "M621i"]),
   P(N622, None, "main", NA1,
     "With Amh Araeng's Warden slain, only Kholusia's remains. Ryne found that you absorbed the Warden's aether and the Light within you has grown monstrous; she can hold it back, but not put it out. "
     "A shade, Ardbert, haunts your room, and the Exarch begs you to survive.",
     ["M621g", "M622a", "M622c", "M622e", "M622h", "M622i"]),
   P(N623, None, "main", NA1,
     "Only Kholusia's Lightwarden remains, and Eulmore is digging in, so it likely hides there. In the Ocular, Emet-Selch told how Hydaelyn's blow sundered creation into fourteen fragments, and the Ascians resolved to rejoin them. "
     "On the road to Gatetown, people move as if in a trance.",
     ["M623b", "M623h", "M623i", "M623c", "M623d", "M623e", "M623k"]),
   P(N624, None, "main", NA1,
     "Gatetown's people were under Lord Vauthry's control, through meol made of sin eater flesh. You stormed Eulmore and struck down Ran'jit in the Canopy, and Ryne saw that Vauthry himself is the last Lightwarden, part man and part sin eater. "
     "He sprouted wings and fled to the floating peak of Mt. Gulg.",
     ["M624a", "M624b", "M624e", "M624g", "M624h"]),
   P(N625, None, "main", NA1,
     "Lord Vauthry, the last Lightwarden, has fled to a floating mountain peak. While Ryne undid his hold on the enthralled, Alphinaud told the Eulmorans the truth about their lord. "
     "The only way up the Bright Cliff toward the peak is the Ladder, unmoving for years, and Chai-Nuzz has agreed to look at its Talos.",
     ["M624h", "M624i", "M625c", "M625e", "M625h", "M625g"]),
   P(N626, None, "main", NA1,
     "To reach Lord Vauthry on his floating mountain, the Scions are restoring the Ladder, the only way up the Bright Cliff. Urianger sent you to Venmont Yards for lumber, and once you had counted its supply, its shipwrights eagerly joined the work. "
     "The people, Urianger says, stand united against the world's fate.",
     ["M625e", "M626a", "M626b", "M626c", "M626d", "M626e"]),
 ],
 "evt-a-talos-for-mt-gulg": [
   P(N627, None, "main", NA2,
     "The Ladder runs again, and you rode it with the twins as its first passengers in twenty years. Emet-Selch dropped by to offer you a place as his equal, and Ardbert warned you against a choice that leaves you alone. "
     "Atop the Bright Cliff you found Amity, a refuge of Eulmore's exiles, where Tristol promised his help.",
     ["M627a", "M627b", "M627f", "M627h", "M627i"]),
   P(N628, None, "main", NA2,
     "From Amity you scouted toward the floating volcano where Lord Vauthry hides, and found sin eaters massing on its slopes. Allagan drones sent toward it showed flight is off the table, and Urianger arrived with the Exarch, who wishes to witness the final struggle himself. "
     "Neither land nor air will reach the foe.",
     ["M628a", "M628b", "M628c", "M628d", "M628e"]),
   P(N629, None, "main", NA2,
     "Since the volcano will not come down, Y'shtola proposed a Talos big enough to seize it, and Chai-Nuzz, heir to Daedalus Stoneworks, must build it. Thancred and the others set out to recruit help. "
     "In Amity, Chai-Nuzz owned the wrong Eulmore did Tristol, who agreed to cooperate, but the Talos still needs a heart.",
     ["M629a", "M629b", "M629g", "M629e", "M629f", "M629i"]),
   P(N630, None, "main", NA2,
     "The giant Talos still needs ore for its heart. Tristol sent you and the Exarch to Tomra, home of the Tholls, a dwarven family who have long mined the land. "
     "Their chief, Xamott, made you pass a trial, then agreed to help you find the ore.",
     ["M629i", "M630a", "M630b", "M630c", "M630d"]),
   P(N631, None, "main", NA2,
     "To make the giant Talos's heart, you need earthseed, a rare ore steeped in magick. Xamott says the surest place to find it is the Duergar's Tewel, a cave held by the Tholls' age-old rivals, the Goggs. "
     "With the Exarch, you escorted young Korutt through sin eaters to its mouth.",
     ["M630d", "M631a", "M631b", "M631c", "M631f"]),
   P(N632, None, "main", NA2,
     "In the Duergar's Tewel, the Exarch made Korutt invisible while you put the Gogg miners to sleep with dream powder, and Korutt dug out the earthseed. "
     "When Glagg, chief of the Goggs, caught you and accused the Tholls, the Exarch put him to sleep too. The Exarch grows weak this far from the Crystarium.",
     ["M632a", "M632b", "M632c", "M632d", "M632e", "M632f"]),
   P(N633, None, "main", NA2,
     "The Exarch is carrying the earthseed to Chai-Nuzz in Amity, and the Tholls lent pickaxes sized for bigger folk. At Top Rung you handed them out to volunteers escorted by Crystarium and Eulmoran soldiers, all eager to do their part for Norvrandt. "
     "Alisaie joined the soldiers guarding them.",
     ["M633a", "M633b", "M633c", "M633d", "M633g"]),
 ],
 "evt-the-final-warden": [
   P(N634, None, "main", NA3,
     "The giant Talos is nearly ready to seize Lord Vauthry's floating volcano. In Amity, Y'shtola oversees its imbuing, and when the ore fell short, the Night's Blessed gave their heartstones, hoping none will ever again be sacrificed to sin eaters. "
     "Urianger has measures ready in case you cannot contain the Light.",
     ["M634a", "M634b", "M634c", "M634d", "M634e", "M634f"]),
   P(N635, None, "main", NA3,
     "On the eve of the assault, the Exarch confided that he made himself one with the Crystal Tower to live indefinitely, so he weakens the farther he goes from it. "
     "In the imperial palace, Elidibus, wearing Zenos's body, told Emperor Varis that the Scions have left the Source, and that Emet-Selch means to end their world.",
     ["M635b", "M635c", "M635j", "M635d", "M635f", "M635g"]),
   P(N636, None, "main", NA3,
     "The Talos seized the volcano, and at its summit you slew Lord Vauthry, born part sin eater as an Ascian pawn. You could not hold the Wardens' combined Light, and the Exarch tried to carry it into the rift and die in your place, "
     "until Emet-Selch shot him and took him away. Only Ryne's power keeps you from becoming a sin eater.",
     ["M636a", "M636b", "M636d", "M636f", "M636g", "M636h", "M636i", "M636k"]),
   P(N637, None, "main", NA3,
     "Light shrouds Norvrandt again because of the power you took from the Wardens, and only your friends know it; Ryne's power holds off your turning, for now. "
     "You woke in the Crystarium and walked its streets to calm the anxious citizens, who mean to search for their stolen steward.",
     ["M636m", "M636k", "M637a", "M637c", "M637d"]),
   P(N638, None, "main", NA3,
     "Emet-Selch holds the wounded Exarch, and Light again shrouds the sky. Seeking word of him, you learned he raised Lyna, lets no one else live in the tower, and that no one knows his true name. "
     "Ardbert has cast his lot with yours, and Lyna holds the key to the tower's heart.",
     ["M636i", "M638g", "M638e", "M638i", "M638b", "M638j"]),
 ],
 "evt-beneath-the-tempest": [
   P(N639, None, "main", NA4,
     "In the Crystal Tower's heart, an Echo showed the Exarch, whose true name is G'raha Tia, telling Urianger he came from a future Source ravaged by Calamity to save you, and meant to die doing it. "
     "Urianger kept his secret, but has now told the Scions. They and the Crystarium back your descent to Emet-Selch's lair in the Tempest.",
     ["M639a", "M639c", "M639d", "M639g", "M639b", "M639n", "M639m"]),
   P(N640, None, "main", NA4,
     "Emet-Selch holds G'raha Tia, whose body is the key to the Crystal Tower's power over time, so he is likely still in the Tempest. "
     "Urianger's way down was the Isle of Ken, an ancient fae being called Bismarck, which Feo Ul persuaded to carry you to the sea floor in a dome of air.",
     ["M640d", "M640e", "M640a", "M640b", "M640c"]),
   P(N641, None, "main", NA4,
     "On the Tempest's drained sea floor, the Scions search for Emet-Selch's stronghold. They found the Ondo, whose chieftain Tolshs Aath will welcome them only if they are the ancients' chosen, and who have seen an illuminated land shining in the abyss. "
     "Alphinaud means to make amends for their lost water.",
     ["M641a", "M641b", "M641c", "M641d", "M641h"]),
   P(N642, None, "main", NA4,
     "Searching the Tempest for Emet-Selch, you found ruins no knife can scratch, finer than anything the Ronkan Empire made. Y'shtola believes he chose them for the Ascian agenda, and that he lit the illuminated land the Ondo speak of. "
     "Winning the Ondo's trust is the swiftest way to find it.",
     ["M642a", "M642b", "M642d", "M642e", "M642f"]),
   P(N643, None, "main", NA4,
     "The Ondo would light their Walls to answer the illuminated land, where Emet-Selch likely hides, and need a sacred lamp to do it. "
     "Grenoldt, the craftsman who vanished from the Crystarium years ago, had not begun it for want of inspiration, so you showed him a crystal that belonged to one of Ardbert's companions.",
     ["M642e", "M643a", "M643b", "M643c", "M643d", "M643e"]),
   P(N644, None, "main", NA4,
     "Grenoldt made the Ondo's lamp, and Tolshs Aath named you the sign his people awaited. An Ondo guide sent you down through the trench, and past the Caliban Gap you found a vast city that Emet-Selch has layered over ancient ruins. "
     "Somewhere inside, he holds G'raha Tia captive.",
     ["M644a", "M644d", "M644e", "M644g", "M644h", "M644i"]),
 ],
 "evt-amaurot": [
   P(N645, None, "main", NA5,
     "In the trench stands Amaurot, a memory Emet-Selch has raised from before the star was sundered, whose people, arcane entities to Y'shtola's eyes, believe their world is ending. "
     "They speak of the Convocation of Fourteen, whose seats include Lahabrea and Elidibus. The Scions spread out to learn where Emet-Selch hides.",
     ["M645j", "M645d", "M645b", "M645h", "M645f", "M645i"]),
   P(N646, None, "main", NA5,
     "In Amaurot you learned that Emet-Selch himself approved your residency. A shade named Hythlodaeus told you that half his people died to create Zodiark, dissenters made Hydaelyn, and Emet-Selch will pay any price to restore the lost; "
     "you and Ardbert, he said, were once one soul. The Ascians mean to sacrifice the Source's lives.",
     ["M646b", "M646c", "M646f", "M646h", "M646i", "M646j", "M646k"]),
   P(MS, None, "main", NA5,
     "In the Capitol, Emet-Selch challenged you to prove yourself worthy of his people's legacy, and nearly broke you as the Light burst its bonds. Ardbert and the living Exarch turned the fight, and Emet-Selch, revealed as Hades, fell to your axe of Light. "
     "With that world saved, the Scions are stuck there, and you returned home alone.",
     ["M647d", "M647f", "M647g", "M647h", "M647j", "M647m", "M647n", "M647o"]),
 ],
})

# ---- Relationships --------------------------------------------------------------------------------------------------
TYPES = [
 ("raised", "raised", "raised by", False),             # as content_2_1_to_2_3 defines it (listed so this era lints alone)
 ("made-by", "made by", "maker of", False),            # new: Vauthry, made by Emet-Selch
 ("spouse-of", "spouse of", "spouse of", True),        # new: Dulia-Chai and Chai-Nuzz
]

RELS = [
 ("rel-vauthry-member-of-lightwardens", "char-vauthry", "member-of", "org-lightwardens", N624, None, "main", ["M624g"]),
 ("rel-vauthry-made-by-emet-selch", "char-vauthry", "made-by", "char-emet-selch", N636, None, "main", ["M636e", "M636j"]),
 ("rel-dulia-chai-spouse-of-chai-nuzz", "char-dulia-chai", "spouse-of", "char-chai-nuzz", N625, None, "main", ["M625f"]),
 ("rel-chai-nuzz-aids-scions", "char-chai-nuzz", "aids", "org-scions", N629, None, "main", ["M629b", "M629h"]),
 ("rel-tristol-aids-scions", "char-tristol", "aids", "org-scions", N627, None, "main", ["M627i"]),
 ("rel-xamott-aids-scions", "char-xamott", "aids", "org-scions", N630, None, "main", ["M630d"]),
 ("rel-korutt-aids-scions", "char-korutt", "aids", "org-scions", N631, None, "main", ["M631c", "M631d"]),
 ("rel-kai-shirr-aids-scions", "char-kai-shirr", "aids", "org-scions", N633, None, "main", ["M633f"]),
 ("rel-crystal-exarch-raised-lyna", "char-crystal-exarch", "raised", "char-lyna", N638, N639, "main", ["M638g"], ["M639a"]),
 ("rel-crystal-exarch-prisoner-of-emet-selch", "char-crystal-exarch", "prisoner-of", "char-emet-selch", N636, N639, "main", ["M636h", "M636i", "M636o"], ["M639a"]),
 ("rel-crystal-exarch-revealed-as-graha-tia", "char-crystal-exarch", "revealed-as", "char-graha-tia", N639, None, "main", ["M639a", "M639c"]),
 ("rel-graha-tia-prisoner-of-emet-selch", "char-graha-tia", "prisoner-of", "char-emet-selch", N639, MS, "main", ["M636i", "M636o", "M639a"]),
 ("rel-lyna-serves-graha-tia", "char-lyna", "serves", "char-graha-tia", N639, None, "main", ["M623m", "M639a"]),
 ("rel-graha-tia-raised-lyna", "char-graha-tia", "raised", "char-lyna", N639, None, "main", ["M638g", "M639a"]),
 ("rel-graha-tia-leads-crystarium", "char-graha-tia", "leads", "loc-crystarium", N639, None, "main", ["M637d", "M639a"]),
 ("rel-urianger-allied-with-graha-tia", "char-urianger", "allied-with", "char-graha-tia", N639, None, "main", ["M639b", "M639i"]),
 ("rel-emet-selch-opposes-scions", "char-emet-selch", "opposes", "org-scions", N636, MS, "main", ["M636i", "M636w"]),
 ("rel-feo-ul-aids-scions", "char-feo-ul", "aids", "org-scions", N640, None, "main", ["M640b"]),
 ("rel-tolshs-aath-aids-scions", "char-tolshs-aath", "aids", "org-scions", N644, None, "main", ["M644d", "M644e"]),
 ("rel-grenoldt-aids-scions", "char-grenoldt", "aids", "org-scions", N644, None, "main", ["M644a", "M644c"]),
 ("rel-lahabrea-member-of-convocation-of-fourteen", "char-lahabrea", "member-of", "org-convocation-of-fourteen", N645, None, "main", ["M645f"]),
 ("rel-elidibus-member-of-convocation-of-fourteen", "char-elidibus", "member-of", "org-convocation-of-fourteen", N645, None, "main", ["M645f"]),
 ("rel-emet-selch-serves-zodiark", "char-emet-selch", "serves", "char-zodiark", N646, MS, "main", ["M646i"]),
 ("rel-emet-selch-revealed-as-hades", "char-emet-selch", "revealed-as", "char-hades", MS, None, "main", ["M647h", "M647i"]),
 ("rel-elidibus-opposes-scions", "char-elidibus", "opposes", "org-scions", MS, None, "main", ["M647s"]),
 ("rel-gaius-opposes-zenos", "char-gaius", "opposes", "char-zenos", MS, None, "main", ["M647x"]),
]

# Relationships the accepted content or an earlier era defined, ended here. The milestone offers no Changes row, so these
# end without end claims (the reason is in the milestone's records: M647v, M647w).
ADJUST = {
 "rel-ranjit-serves-vauthry": {"until": N624, "end": ["M624e"]},                    # content_5_0_part1/part2: you strike him down
 "rel-ranjit-opposes-scions": {"until": N624, "end": ["M624e"]},                    # content_5_0_part2
 "rel-eulmore-opposes-crystarium": {"until": N633, "end": ["M633c"]},               # content_5_0_part1: their soldiers guard the volunteers together
 "rel-crystarium-opposes-eulmore": {"until": N633, "end": ["M633c"]},               # content_5_0_part1
 "rel-vauthry-controls-eulmore": {"until": N636, "end": ["M636b", "M636c"]},        # content_5_0_part1/part2: Vauthry dies
 "rel-vauthry-controls-sin-eaters": {"until": N636, "end": ["M636b", "M636c"]},     # content_5_0_part1
 "rel-vauthry-opposes-alphinaud": {"until": N636, "end": ["M636b", "M636c"]},       # content_5_0_part1
 "rel-crystal-exarch-opposes-vauthry": {"until": N636, "end": ["M636b", "M636c"]},  # content_5_0_part2
 "rel-children-of-the-everlasting-dark-serves-vauthry": {"until": N636, "end": ["M636b", "M636c"]},  # content_5_0_part2
 "rel-crystal-exarch-leads-crystarium": {"until": N639, "end": ["M639a"]},          # content_5_0_part1: continues as rel-graha-tia-leads-crystarium
 "rel-lyna-serves-crystal-exarch": {"until": N639, "end": ["M639a"]},               # content_5_0_part1: continues as rel-lyna-serves-graha-tia
 "rel-emet-selch-member-of-ascians": {"until": MS},                                 # content_5_0_part2: revealed as Hades, destroyed
 "rel-zenos-possessed-by-elidibus": {"until": MS},       # content_4_1_to_4_56: Zenos takes his body back
 "rel-varis-leads-garlean-empire": {"until": MS},        # content_2_4_to_2_55: Zenos kills him
 "rel-varis-opposes-eorzean-alliance": {"until": MS},    # content_4_1_to_4_56
}

# ---- Arcs ------------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-n1-the-last-foothold", "evt-the-last-foothold", N621, N626),
 ("arc-n2-a-talos-for-mt-gulg", "evt-a-talos-for-mt-gulg", N627, N633),
 ("arc-n3-the-final-warden", "evt-the-final-warden", N634, N638),
 ("arc-n4-beneath-the-tempest", "evt-beneath-the-tempest", N639, N644),
 ("arc-n5-amaurot", "evt-amaurot", N645, MS),
]

CASTS = {
 "evt-the-last-foothold": [
   ("char-ryne", N621, ["M621a"]), ("char-alisaie", N621, ["M621f"]), ("char-thancred", N621, ["M621i"]),
   ("char-yshtola", N621, ["M621d"]), ("char-crystal-exarch", N622, ["M622h"]), ("char-ardbert", N622, ["M622e"]),
   ("char-emet-selch", N623, ["M623c"]), ("char-alphinaud", N623, ["M623j"]), ("char-vauthry", N624, ["M624g"]),
   ("char-urianger", N626, ["M626a"]),
 ],
 "evt-a-talos-for-mt-gulg": [
   ("char-alisaie", N627, ["M627h"]), ("char-emet-selch", N627, ["M627b"]), ("char-ardbert", N627, ["M627f"]),
   ("char-tristol", N627, ["M627i"]), ("char-crystal-exarch", N628, ["M628d"]), ("char-yshtola", N629, ["M629a"]),
   ("char-chai-nuzz", N629, ["M629b"]), ("char-xamott", N630, ["M630b"]), ("char-korutt", N631, ["M631c"]),
   ("char-urianger", N628, ["M628e"]),
 ],
 "evt-the-final-warden": [
   ("char-yshtola", N634, ["M634a"]), ("char-urianger", N634, ["M634e"]), ("char-chai-nuzz", N634, ["M634b"]),
   ("char-crystal-exarch", N635, ["M635b"]), ("char-elidibus", N635, ["M635g"]), ("char-vauthry", N636, ["M636b"]),
   ("char-emet-selch", N636, ["M636h"]), ("char-ryne", N636, ["M636k"]), ("char-ardbert", N636, ["M636v"]),
   ("char-lyna", N638, ["M638j"]),
 ],
 "evt-beneath-the-tempest": [
   ("char-graha-tia", N639, ["M639a"]), ("char-urianger", N639, ["M639b"]), ("char-lyna", N639, ["M639j"]),
   ("char-ardbert", N639, ["M639k"]), ("char-ryne", N639, ["M639o"]), ("char-feo-ul", N640, ["M640b"]),
   ("char-alphinaud", N641, ["M641f"]), ("char-tolshs-aath", N641, ["M641d"]), ("char-yshtola", N642, ["M642e"]),
   ("char-grenoldt", N643, ["M643b"]),
 ],
 "evt-amaurot": [
   ("char-alisaie", N645, ["M645h"]), ("char-alphinaud", N645, ["M645h"]), ("char-urianger", N645, ["M645d"]),
   ("char-yshtola", N645, ["M645b"]), ("char-thancred", N645, ["M645i"]), ("char-ryne", N646, ["M646a"]),
   ("char-hythlodaeus", N646, ["M646c"]), ("char-ardbert", N646, ["M646j"]), ("char-emet-selch", N646, ["M646b"]),
   ("char-graha-tia", MS, ["M647g"]),
 ],
}

ARC_NOTES = {
 "arc-n1-the-last-foothold": "MSQ #621 *A Fresh Start* to #626 *The Ladder* (5.0): the hunt for Kholusia's Lightwarden, from Ryne's first Warden (M621e) and Thancred naming Vauthry (M621i) "
   "through the storming of Eulmore and Vauthry's flight (M624g, M624h), ending as the Ladder is restored (M626e). The next quest opens the Bright Cliff, so the arc closes there.",
 "arc-n2-a-talos-for-mt-gulg": "MSQ #627 *The View from Above* to #633 *Rich Veins of Hope* (5.0): Amity and Tristol (M627i), the failed scouting (M628e), the giant Talos plan (M629a), "
   "and the Tholls' earthseed (M630d, M632f), ending as Norvrandt's volunteers start work (M633d). Its name avoids the later titles.",
 "arc-n3-the-final-warden": "MSQ #634 *That None Shall Ever Again* to #638 *In His Garden* (5.0): the heartstones (M634d), the Exarch's bond to the tower (M635b), the assault and Vauthry's death, "
   "the Exarch's sacrifice and capture (M636g, M636h), and the Crystarium's search, ending as Lyna readies the tower's heart (M638j). Dulia-Chai, Feo Ul and the Night's Blessed live in the entity records.",
 "arc-n4-beneath-the-tempest": "MSQ #639 *The Unbroken Thread* to #644 *The Illuminated Land* (5.0): the Echo that names G'raha Tia (M639a) opens the arc; Bismarck (M640a), the Ondo (M641d), "
   "the ruins (M642e) and Grenoldt's lamp (M643d) lead to the city beneath the Tempest (M644h). The arc ends before the city is named.",
 "arc-n5-amaurot": "MSQ #645 *The End of a World*, #646 *A Greater Purpose* and the cp-shb-5-0 milestone (the 5.0 finale): Amaurot (M645d), Hythlodaeus (M646c), and Emet-Selch's defeat as Hades (M647h). "
   "The Source coda (Zenos, Varis, Gaius, Estinien, Tataru, Elidibus) lives in the entity records, because the cast is full.",
}

DECISIONS = [
 "**Five arcs (n1–n5)** cover every step from #621 to cp-shb-5-0 without sharing steps; n5 is three steps long, because Amaurot opens at #645.",
 "**The Crystal Exarch → G'raha Tia** follows the Marques → Cid pattern at #639, where the Journal and Urianger name him. At #636 only a stage direction names him as his hood falls; "
 "the text there says only that his hood fell back. The Exarch's own relationships end at #639 (M639a) and continue on `char-graha-tia`, which carries \"The Crystal Exarch\" and \"The Exarch\" as aliases.",
 "**Emet-Selch → Hades** at the milestone, where he casts aside his mortal form and names himself (M647h, M647i). `char-hades` carries \"Emet-Selch\" as an alias; the milestone offers no Changes row, so his ended relationships carry no end claims.",
 "**Ryne** is `char-ryne` from #621, whose Journal says you left with a girl named Minfilia and came back with one named Ryne. Her presentations name Minfilia (`char-minfilia`) only as the one who entrusted her power.",
 "**Continuity with 5.0 parts 1 and 2:** the same names and aliases as their last records (`loc-the-first` is \"The world of the First\", so citation titles such as *The First of Many* never match it; Emet-Selch keeps \"Solus\", Ryne \"Minfilia\", Y'shtola \"Master Matoya\", Lyna \"Captain Lyna\", Feo Ul \"Titania\"). Their `rel-ryne-member-of-scions` and `rel-estinien-allied-with-gaius` already cover this era, so they are not repeated here.",
 "**Endings (ADJUST):** Ran'jit's ties end at #624, where you strike him down; Eulmore and the Crystarium stop opposing each other at #633, where their soldiers guard the volunteers together; Vauthry's ties, and the Exarch's opposition to him, end at #636 with his death; the Exarch's leadership of the Crystarium and Lyna's service move to `char-graha-tia` at #639.",
 "**Zenos's body:** ADJUST ends `rel-zenos-possessed-by-elidibus` at the milestone, where Zenos says the Ascian shed his skin (M647v); Varis's leadership and opposition end there too (M647w).",
 "**Left out as entities** (named in text only, or not at all): Ran'jit's \"master\", Gatetown, Wright, Amity, Tomra, the Goggs and Glagg, Bismarck of the First (the existing `char-bismarck` is the Vanu Vanu primal, so the fae is described in text), "
 "Paushs Ooan, the Ondo, the Night's Blessed and Runar, Irvithe and the shipwrights, Katliss, Moren and the Crystarium's citizens, Innocence (an alias of Vauthry), Loghrif, Tesleen and Magnus.",
]

ALLOW = {
 "Ryne": N621,          # A Fresh Start, Journal: "return with one named Ryne"
 "Lightwarden": N621,   # A Fresh Start, Journal: "face-to-face with the Lightwarden"
 "Exarch": N622,        # More than a Hunch, main dialogue: the Crystal Exarch at your door
 "Emet-Selch": N623,    # Return to Eulmore, Journal: "Emet-Selch sours the mood"
 "Zodiark": N623,       # Return to Eulmore, Journal: "as Zodiark and Hydaelyn warred"
 "Hythlodaeus": N646,   # A Greater Purpose: "my name is Hythlodaeus"
 "Hades": MS,           # Shadowbringers, Journal: "his true name─Hades"
}

# Not loaded by the builder: Hydaelyn's records for this era, for the lead to merge. char-hydaelyn lives in an earlier
# era module, so loading these alone makes the accepted text that names Hydaelyn fail "visible" checks in a one-era lint.
HYDAELYN_DRAFT = {
 "PRES": {
 "char-hydaelyn": [
   P(N623, None, "main", "Hydaelyn",
     "A power who warred with Zodiark and unmade Him with a single blow, sundering all creation into fourteen fragments.",
     ["M623o", "M623d"]),
   P(N646, None, "main", "Hydaelyn",
     "A power created by dissenters among the ancients, who gave their life energies to make Her an incarnation of their opposing belief.",
     ["M646h", "M645c"]),
 ],
 },
 "RELS": [("rel-hydaelyn-opposes-zodiark", "char-hydaelyn", "opposes", "char-zodiark", N623, None, "main", ["M623d", "M623o"])],
}
