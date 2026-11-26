"""Atlas content for Heavensward 3.0, part 2: MSQ #292 A General Summons to #334 Fetters of Lament, then the
cp-hw-3-0 milestone (after #335, the patch's last quest). Arc tag f. Data only; see docs/atlas/era-modules.md.

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lane reports L16–L19). Spoiler rules this module
follows on top of the contract: the second Ascian at #313 and #335 is never named (her name is banned), Lucia's and
Livia's family name and every other surname stay out, and the patch's own title appears only from cp-hw-3-0 (ALLOW).
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

S = {n: f"cp-msq-{n}" for n in range(292, 335)}
HW = "cp-hw-3-0"

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #292 A General Summons
 "M292a": ("Raubahn believes the sultana lies alive, abed somewhere in the palace.", "A General Summons", "Her Grace is likely somewhere within the palace─abed but alive."),
 "M292b": ("Yugiri learns that Meriel, the sultana's former lady-in-waiting, is hiding in the Silver Bazaar.", "A General Summons", "the sultana's former lady-in-waiting, is hiding somewhere in the"),
 "M292c": ("Lolorito appears before Meriel can be questioned and reveals the assassination plot himself.", "A General Summons", "appears and proceeds to reveal the details of the assassination plot"),
 "M292d": ("Lolorito had Meriel give the sultana a sleeping potion in place of poison.", "A General Summons", "Thus did I employ young Meriel here to administer a potent sleeping potion in place of a poison."),
 "M292e": ("Lolorito had Ilberd lie about the assassination to turn Raubahn's rage on Teledji.", "A General Summons", "I had him lie about the assassination as a means to prime your rage against Teledji."),
 "M292f": ("Lolorito gives Raubahn the means to wake the sultana.", "A General Summons", "he then presents the Flame General with the means to rouse the sultana from her deathlike state"),
 "M292g": ("Raubahn is reinstated as general of the Immortal Flames.", "A General Summons", "you are hereby reinstated as general of the Immortal Flames!"),
 "M292h": ("Teledji's Carteneau Reclamation Bill was a facade for seizing the Allagan machine Omega.", "A General Summons", "Teledji Adeledji's Carteneau Reclamation Bill was no more than a facade"),
 "M292i": ("Raubahn executed Teledji without trial.", "A General Summons", "Or have you forgotten your ''own'' crime in executing Teledji Adeledji without trial!?"),
 # #293 Awakening in Ul'dah
 "M293a": ("The sultana is awake and none the worse for her sleep.", "Awakening in Ul'dah", "Her Grace is awoken. The palace physician assures me she is none the worse for her slumber."),
 "M293b": ("Nanamo will soon resume her plan to place Ul'dah's government in its citizens' hands.", "Awakening in Ul'dah", "I believe Her Grace will soon resume her plans to place the government of Ul'dah into the hands of its citizens."),
 "M293c": ("Lolorito reports that the Empire has built a warship to rival the Agrius.", "Awakening in Ul'dah", "has built a warship to rival the might of the legendary"),
 "M293d": ("Lolorito urges repairing Teledji's damage and preparing to repel the Empire.", "Awakening in Ul'dah", "I move that it is time to repair the damage caused by Teledji Adeledji, and prepare our great nation to repel the Empire once more."),
 "M293e": ("Alphinaud decides to disband the Crystal Braves.", "Awakening in Ul'dah", "I have decided to disband the Crystal Braves."),
 "M293f": ("Those who sided with Ilberd will be hunted down and held to account.", "Awakening in Ul'dah", "As for those who sided with the traitor, Ilberd, they shall be hunted down and held to account for their crimes."),
 "M293g": ("Alphinaud will henceforth be simply a member of the Scions.", "Awakening in Ul'dah", "Henceforth, I shall be no more or less than Alphinaud, proud member of the Scions."),
 "M293h": ("Alphinaud calls for the search for the missing comrades to resume.", "Awakening in Ul'dah", "Let us resume the search for our missing comrades"),
 # #294 A Brave Resolution
 "M294a": ("The 3rd Unit Braves abandoned Revenant's Toll when they learned of Ilberd's defeat.", "A Brave Resolution", "the 3rd Unit Braves abandoned Revenant's Toll when they learned of Captain Ilberd's defeat"),
 "M294b": ("Alphinaud means to thank the Braves and disband the company in person.", "A Brave Resolution", "Alphinaud declares his intention to thank these stalwart warriors, and disband the company in person."),
 "M294c": ("The Braves pledge their support to Alphinaud and the Scions, loyal to the company's ideals.", "A Brave Resolution", "pledge their undying support to both him and the"),
 "M294d": ("Alianne says the company's ideals live on.", "A Brave Resolution", "The Crystal Braves may be finished, but the ideals upon which the company was founded live on."),
 "M294e": ("Riol asks that the Braves help the Scions find Minfilia and the others.", "A Brave Resolution", "Let us help the Scions. Let us help you find Minfilia an' the others."),
 "M294f": ("Alphinaud is moved to tears by his comrades' support.", "A Brave Resolution", "Alphinaud is moved to tears by the unshakable support of his comrades"),
 # #295 Ready to Fly
 "M295a": ("Alphinaud sends you to Ishgard while he coordinates the search with the remaining Braves.", "Ready to Fly", "while he coordinates the ongoing search efforts with the remaining"),
 "M295b": ("Cid's manacutter completes its first successful test flight.", "Ready to Fly", "We have but this moment completed the manacutter's first successful test flight!"),
 "M295c": ("Nidhogg remains in the Aery, plotting revenge.", "Ready to Fly", "Nidhogg seems to content to remain in the Aery, plotting his revenge."),
 "M295d": ("The lord commander, Aymeric, offers his blade, and Estinien reminds him of his duty to protect the city.", "Ready to Fly", "the lord commander eagerly offers his own blade for the battle ahead, forcing Estinien to remind him of his duties as the city's protector"),
 "M295e": ("With Nidhogg's eye in his possession, Estinien can stifle the wyrm's strength.", "Ready to Fly", "But with his eye in my possession, I can stifle his strength at the source."),
 "M295f": ("Estinien refuses to take Alphinaud against Nidhogg.", "Ready to Fly", "But one does not ''practice'' on an adversary such as Nidhogg."),
 "M295g": ("Through an unlikely alliance with Lady Iceheart, the party came to speak with Hraesvelgr.", "Ready to Fly", "'twas through that most unlikely of alliances that we came to speak with Hraesvelgr."),
 # #296 Into the Aery
 "M296a": ("Estinien bids you fly with him to Nidhogg's lair.", "Into the Aery", "Estinien bids you fly with him to"),
 "M296b": ("The Azure Dragoon gouges out Nidhogg's remaining eye and the lifeless wyrm falls.", "Into the Aery", "Glorying in victory, the Azure Dragoon gouges out Nidhogg's remaining eye, and sends the lifeless wyrm tumbling into the clouds below."),
 "M296c": ("A vision shows Nidhogg's defeat long ago at the hands of Haldrath and his knights.", "Into the Aery", "a vision wherein you witness the truth of Nidhogg's defeat at the hands of"),
 "M296d": ("Estinien asks how the eye came to be in Nidhogg's skull if Haldrath took both.", "Into the Aery", "If Haldrath took both of Nidhogg's eyes, then how came this eye to be lodged in the wyrm's skull?"),
 "M296e": ("Only the truth from Hraesvelgr will complete the triumph.", "Into the Aery", "Only by wresting the truth from"),
 "M296f": ("In the vision, the founders keep Ishgard's throne empty and rule as stewards.", "Into the Aery", "We keep it empty. Until a king rises once more, we must assume the role of stewards."),
 # #297 The Song Begins
 "M297a": ("Estinien would have Lady Iceheart present when he prises the truth from Hraesvelgr.", "The Song Begins", "cannot rest until he has prised the truth from"),
 "M297b": ("Estinien tells Ysayle the Dragonsong War has consumed her life and claimed many followers.", "The Song Begins", "Lady Iceheart─the Dragonsong War has all but consumed your life and claimed many of your followers."),
 "M297c": ("Hraesvelgr yielded half his strength to the blinded Nidhogg.", "The Song Begins", "Unto the blinded Nidhogg did I yield one half of my strength..."),
 "M297d": ("In the vision, Hraesvelgr surrenders an eye to his vengeful brood-brother.", "The Song Begins", "Hraesvelgr surrenders an eye to his vengeful brood-brother, condemning the people of"),
 "M297e": ("Mortals took Ratatoskr's eyes and fed on her essence.", "The Song Begins", "They did take Ratatoskr's eyes...and glut their appetites upon her essence..."),
 "M297f": ("Human treachery took Hraesvelgr's brood-sister's life and his brood-brother's reason.", "The Song Begins", "Their treachery claimed my brood-sister's life and my brood-brother's reason!"),
 "M297g": ("Ysayle realizes it was Hraesvelgr's strength that sustained Nidhogg.", "The Song Begins", "It was yours... Your strength that sustained Nidhogg all these years..."),
 "M297h": ("Hraesvelgr sends the mortals away.", "The Song Begins", "Go, mortals! Take your unruly passions and leave this place..."),
 "M297i": ("You learn the truth of the Dragonsong War's beginnings.", "The Song Begins", "At last, you know the truth of the"),
 # #298 Unrest in Ishgard
 "M298a": ("Heretics rise up within Ishgard itself.", "Unrest in Ishgard", "It would seem that heretics have begun an uprising within the city itself."),
 "M298b": ("Ysayle declares the war ended and Nidhogg dead.", "Unrest in Ishgard", "The war is ended! Nidhogg is no more!"),
 "M298c": ("The heretics put up their arms and retreat at their mistress's command.", "Unrest in Ishgard", "The heretics are thus persuaded to put up their arms, and retreat from the conflict at their mistress's command."),
 "M298d": ("Zephirin says the unrest will feed the people's fear of heretics and dragons.", "Unrest in Ishgard", "This unrest shall serve to feed the people's fear of the heretics and the dragons both."),
 "M298e": ("The archbishop orders the intruders allowed to sow chaos, then crushed by the Temple Knights.", "Unrest in Ishgard", "Grant our guests what time they need to sow a measure of chaos, then order the Temple Knights to crush them."),
 "M298f": ("Lahabrea says the Bringer of Light must die.", "Unrest in Ishgard", "It is time for the Bringer of Light to die."),
 "M298g": ("Haurchefant says the knights must keep the peace if the heretics do.", "Unrest in Ishgard", "If the heretics mean to observe the peace, then it would be folly not to do the same!"),
 "M298h": ("Estinien lost his family to Nidhogg's flames.", "Unrest in Ishgard", "I lost my family to Nidhogg's flames."),
 "M298i": ("In the war-torn city you are reunited with Haurchefant.", "Unrest in Ishgard", "Upon entering the war-torn city, you are reunited with Lord"),
 "M298j": ("Ysayle tells her followers the cycle of violence was born of their forefathers' treachery.", "Unrest in Ishgard", "The endless cycle of violence between man and dragon was born of our forefathers' treachery."),
 # #299 He Who Would Not Be Denied
 "M299a": ("Count Edmont and the others are troubled to learn Ishgard's faith is built on a lie.", "He Who Would Not Be Denied", "and the others are deeply troubled by the revelation that the … ian faith is built upon a lie"),
 "M299b": ("Aymeric leaves to confront the archbishop with the truth.", "He Who Would Not Be Denied", "Ser Aymeric leaves to confront the archbishop with the truth"),
 "M299c": ("Lucia reveals that Aymeric is the archbishop's bastard son.", "He Who Would Not Be Denied", "That Ser Aymeric is the archbishop's bastard son."),
 "M299d": ("Lucia's loyalty is to the lord commander alone.", "He Who Would Not Be Denied", "My loyalty is to the lord commander alone."),
 "M299e": ("Lucia means to fetch Aymeric from the Vault if he does not return.", "He Who Would Not Be Denied", "If the lord commander does not return from the Vault at the appointed hour, I mean to go and fetch him."),
 "M299f": ("Haurchefant swears on his house's sigil to do what Aymeric asks.", "He Who Would Not Be Denied", "I swear to you, on the sigil of our house, that I shall do this and make you proud."),
 "M299g": ("Aymeric says man's treachery shattered the peace with the dragons.", "He Who Would Not Be Denied", "it was man's treachery which shattered the peace and plunged our peoples into war."),
 "M299h": ("Lucia's rescue will need more allies.", "He Who Would Not Be Denied", "To be assured of success, you will need to enlist the aid of others."),
 "M299i": ("Haurchefant brings the news to his father and Aymeric.", "He Who Would Not Be Denied", "Keen to break the news to his father and Ser"),
 # #300 Ill-weather Friends
 "M300a": ("Lucia hopes to enlist the revolutionaries hiding in the Brume.", "Ill-weather Friends", "were you to enlist the aid of the revolutionaries hiding in the"),
 "M300b": ("Lucia believes the revolutionaries opened the city's gates to the heretics.", "Ill-weather Friends", "'Twas these disgruntled Ishgardians who opened the gates of our city to the heretics, I believe."),
 "M300c": ("Tataru knows only that the revolutionaries are led by someone called the Mongrel.", "Ill-weather Friends", "led by someone called “the Mongrel.”"),
 "M300d": ("The people of the Brume shelter the revolutionaries.", "Ill-weather Friends", "the revolutionaries are being sheltered by the populace"),
 "M300e": ("As a Temple Knight sworn to the Holy See, Lucia cannot approach them herself.", "Ill-weather Friends", "As a Temple Knight and sworn servant of the Holy See, any overtures I make are doomed to fail."),
 "M300f": ("Estinien says the dragoons have no love for politics.", "Ill-weather Friends", "The dragoons have no love for politics, my lady."),
 # #301 The Spice of Life
 "M301a": ("Gibrillont, keeper of the Forgotten Knight, will divulge nothing of the Mongrel.", "The Spice of Life", "Gibrillont stresses that discretion is key to running a successful tavern"),
 "M301b": ("Gibrillont offers to point you the right way in exchange for a favor.", "The Spice of Life", "he offers to point you in the right direction in exchange for a small favor"),
 "M301c": ("Gibrillont brews mulled wine, which stirs men's hearts.", "The Spice of Life", "There are few things which stir the hearts of men like a sip of mulled wine."),
 # #302 Noble Indiscretions
 "M302a": ("Hierytha knows the wine's recipe from a young Hyuran girl decades ago.", "Noble Indiscretions", "recognizes the blend of herbs and spices to be the same as one used by a young"),
 "M302b": ("The baron the girl served cast her out when she became pregnant with his child.", "Noble Indiscretions", "the baron took advantage of the girl's affections, and cast her out onto the streets when she became pregnant with his child."),
 "M302c": ("The girl died after returning to the Brume and giving birth.", "Noble Indiscretions", "She passed away sometime later, after returning to the"),
 "M302d": ("The baron was an Elezen with striking red eyes.", "Noble Indiscretions", "baron with striking red eyes"),
 # #303 A Child Apart
 "M303a": ("Gerraldieux tends the poorest of the Brume.", "A Child Apart", "who tends to the poorest of the poor in the"),
 "M303b": ("The young mother toiled for her daughter and still helped Gerraldieux tend the poor.", "A Child Apart", "despite toiling tirelessly to feed and clothe her daughter, she took time to help Gerraldieux administer succor to the poor"),
 "M303c": ("Her raven-haired daughter would stand on the walls staring into the mists.", "A Child Apart", "her raven-black hair flowing in the wind as she stared out into the mists in silence"),
 "M303d": ("The mother held fast to hope for her daughter.", "A Child Apart", "she still held fast to hope—if not for herself, then for her beloved daughter."),
 # #304 Bloodlines
 "M304a": ("The Mongrel and her pups embrace the legacy of their parents.", "Bloodlines", "have chosen to embrace that inescapable truth"),
 "M304b": ("The Mongrel is the raven-haired, ruby-eyed child of the Elezen nobleman and the Hyuran woman.", "Bloodlines", "the raven-haired, ruby-eyed child born of the"),
 "M304c": ("Alphinaud: the Mongrel was born of an Elezen nobleman and a Hyuran maidservant.", "Bloodlines", "So our mongrel was born of an Elezen nobleman and a Hyuran maidservant."),
 "M304d": ("The Mongrel's whereabouts are still unknown.", "Bloodlines", "Though the whereabouts of the Mongrel are still unknown to you"),
 # #305 Fire and Blood
 "M305a": ("Alphinaud fears Tataru has run afoul of the revolutionaries.", "Fire and Blood", "Fearing that she may have run afoul of the revolutionaries"),
 "M305b": ("A raven-haired woman with ruby eyes, Hilda, stops Tataru's tormentors.", "Fire and Blood", "a raven-haired woman with ruby eyes appears, and commands Tataru's tormentors to desist. It would seem her name is"),
 "M305c": ("Ser Charibert of the Heavens' Ward accuses the party of plotting insurrection.", "Fire and Blood", "strides into the tavern, accusing you and the others of plotting insurrection"),
 "M305d": ("With Haurchefant and Lucia, you overwhelm Ser Charibert.", "Fire and Blood", "Joined by Lord [[Haurchefant]] and [[Lucia]], you manage to overwhelm Ser Charibert, who withdraws."),
 "M305e": ("Aymeric has been imprisoned, and the Heavens' Ward placed in command of the Temple Knights.", "Fire and Blood", "has been imprisoned, and the Heavens' Ward placed in command of"),
 "M305f": ("Hilda agrees to help rescue Aymeric.", "Fire and Blood", "Hilda agrees to assist with the rescue mission."),
 "M305g": ("Hilda calls herself the Mongrel out of pride in her mixed heritage.", "Fire and Blood", "she took to calling herself “the Mongrel” out of a newfound pride for her mixed heritage"),
 "M305h": ("Half the Temple Knights, who opposed Aymeric's promotion, have gathered at the Vault.", "Fire and Blood", "The other half, who opposed his promotion to lord commander, have gathered at the Vault as ordered."),
 "M305i": ("Hilda's followers are pledged to Aymeric's cause.", "Fire and Blood", "Thus united in purpose and pledged to Ser Aymeric's cause"),
 # #306 A Knight's Calling
 "M306a": ("Hilda's sympathizers spread word of a heretic army outside the gates to draw the High Houses away.", "A Knight's Calling", "spread word of a heretic army massing outside the"),
 "M306b": ("Your party draws the Heavens' Ward while Lucia's rescues Aymeric.", "A Knight's Calling", "and draw the attention of the Heavens' Ward, and hers to rescue Ser Aymeric during the ensuing chaos"),
 "M306c": ("A transformed Ser Zephirin takes aim with a spear of pure light.", "A Knight's Calling", "a transformed Ser Zephirin taking aim at you, a spear of pure light in his hand"),
 "M306d": ("Haurchefant raises his shield to save you, the spear finds its mark, and he dies.", "A Knight's Calling", "Lord Haurchefant bellows a warning and raises his shield in your defense, but the steel gives way, and the spear finds a mark … before the light leaves his eyes forever"),
 "M306e": ("The archbishop boards an airship and tells his knights Azys Lla awaits.", "A Knight's Calling", "finally catching up with him as he prepares to board an … Go. Azys Lla awaits."),
 "M306f": ("A wounded Aymeric rejoins you after his rescue.", "A Knight's Calling", "Rejoined by your companions and a wounded Ser Aymeric"),
 "M306g": ("Count Edmont says a knight lives to serve, protect and sacrifice.", "A Knight's Calling", "A knight lives to serve. To protect. To sacrifice. There is no greater calling."),
 "M306h": ("Alphinaud: Haurchefant took the Scions in when all others forsook them.", "A Knight's Calling", "When all others had forsaken us, Lord Haurchefant took us in."),
 "M306i": ("Ser Zephirin orders the retreat, and Ser Charibert obeys.", "A Knight's Calling", "gives the order to retreat, and Ser [[Charibert]] reluctantly obeys"),
 # #307 The Sins of Antiquity
 "M307a": ("King Thordan and his knights twelve slew Ratatoskr to partake of her eyes.", "The Sins of Antiquity", "entrapped and butchered the great wyrm Ratatoskr, that they might partake of her eyes"),
 "M307b": ("The blood of the knights twelve flows in all Ishgardians.", "The Sins of Antiquity", "for the blood of the knights twelve flows within ''all'' our veins!"),
 "M307c": ("Haldrath took one of Nidhogg's eyes and wielded its power to defend his people.", "The Sins of Antiquity", "Whilst Thordan's son Haldrath took one of Nidhogg's eyes and learned to wield its power in defense of his people"),
 "M307d": ("The Heavens' Ward use their bodies as vessels for the souls of King Thordan and his knights twelve.", "The Sins of Antiquity", "they are using their own bodies as vessels for the souls of the legendary King Thordan and his knights twelve"),
 "M307e": ("The archbishop had Aymeric arrested, revealing plans to free Ishgard from the sins of antiquity.", "The Sins of Antiquity", "has Ser Aymeric arrested—but not before revealing that he has plans of his own to free the people of Ishgard from the sins of antiquity."),
 "M307f": ("Aymeric asks your aid in bringing his father to justice.", "The Sins of Antiquity", "Your aid in bringing him to justice."),
 "M307g": ("Alphinaud says the Scions must oppose the Heavens' Ward if they wield primal power.", "The Sins of Antiquity", "it is the duty of the remaining Scions to oppose them"),
 "M307h": ("The archbishop's absence has thrown Ishgard's government into chaos.", "The Sins of Antiquity", "my father's absence has thrown our government into chaos."),
 "M307i": ("Lucia asks to help the Scions search for the archbishop.", "The Sins of Antiquity", "I would like to assist the Scions in their search for the archbishop."),
 # #308 In Search of the Soleil
 "M308a": ("The archbishop's airship vanished into the northern reaches near the Blue Window.", "In Search of the Soleil", "The airship has not been seen since it disappeared into the northern reaches near the Blue Window."),
 "M308b": ("That region is firmly held by the Vanu Vanu.", "In Search of the Soleil", "because the region is firmly held by the Vanu Vanu"),
 "M308c": ("Cid darkens on learning of Haurchefant's death and the archbishop's escape.", "In Search of the Soleil", "cheery demeanor soon darkens when he learns of Lord"),
 "M308d": ("Cid says the Ascians tried to tempt the archbishop as they tempted Gaius with the Ultima Weapon.", "In Search of the Soleil", "the Ascians tried to tempt him as they tempted Gaius with the Ultima Weapon."),
 "M308e": ("Cid guesses Azys Lla is a source of cosmic power the archbishop covets.", "In Search of the Soleil", "he surmises that it is the source of some phenomenal cosmic power which"),
 "M308f": ("Cid puts the Enterprise at your disposal.", "In Search of the Soleil", "is at your disposal. Come to the airship landing when you're ready to depart."),
 # #309 Into the Blue
 "M309a": ("There is no news of the missing Scions, but Urianger and Riol are pursuing leads.", "Into the Blue", "We still have no news of the missing Scions, but she assures me that Urianger and Riol are pursuing promising leads."),
 "M309b": ("Aboard the Enterprise you are haunted by the memory of a broken shield.", "Into the Blue", "only to be confronted with the memory of a broken shield..."),
 "M309c": ("No Vanu wait at the Blue Window, and Alphinaud is on edge.", "Into the Blue", "waiting to receive you. Nevertheless, Alphinaud appears to be on edge."),
 # #310 Familiar Faces
 "M310a": ("Imperial troops surround a terrified Vanu Vanu.", "Familiar Faces", "a unit of imperial troops surrounding a terrified"),
 "M310b": ("The imperials try to seize Ishgardians, who they think know where the archbishop is.", "Familiar Faces", "Ishgardians!? Seize them! They'll know where the archbishop is!"),
 "M310c": ("The rescued Vanu, Lonu Vanu, is profoundly grateful.", "Familiar Faces", "as he names himself, expresses his profound gratitude for your intervention"),
 "M310d": ("The Vanu here are not openly hostile to you.", "Familiar Faces", "the Vanu here are not openly hostile to you and Alphinaud"),
 # #311 Devourer of Worlds
 "M311a": ("Lonu Vanu invites you to his village.", "Devourer of Worlds", "invites you to his village"),
 "M311b": ("The imperials have engaged Bismarck.", "Devourer of Worlds", "he explains that the imperials have engaged"),
 "M311c": ("Bismarck swallows an island whole.", "Devourer of Worlds", "Bismarck opens wide its great maw and swallows an island whole."),
 "M311d": ("Lonu Vanu will not dwell on the deeds of an unfathomable god.", "Devourer of Worlds", "refuses to dwell on the actions of an unfathomable god"),
 "M311e": ("The archbishop and the Heavens' Ward seek the key to Azys Lla, which lay on the island Bismarck devoured.", "Devourer of Worlds", "are come to the Sea of Clouds in search of the key to … has devoured the island upon which the key was kept"),
 "M311f": ("Chief Sonu calls Azys Lla the ancient birthplace of sin.", "Devourer of Worlds", "There lies ancient birthplace of sin, home of forbidden secrets."),
 # #312 Black and the White
 "M312a": ("Alphinaud: unless you slay the whale and claim the key first, the Heavens' Ward will.", "Black and the White", "If we do not slay the whale and claim the key first, they surely will."),
 "M312b": ("Bismarck is the Vanu Vanu's patron deity.", "Black and the White", "'s patron deity, of course, it would only be prudent to learn more of its nature"),
 "M312c": ("Kunu Vali tells of Bismarck's death at his brothers' hands and his heavenly rebirth.", "Black and the White", "recounts the tale of Bismarck's death at the hands of his brothers and of his heavenly rebirth"),
 "M312d": ("The merciful Bismarck of the tales is at odds with his recent behavior.", "Black and the White", "a depiction wholly at odds with his recent behavior"),
 "M312e": ("Cid plans to tow an island through the Sea of Clouds to lure Bismarck.", "Black and the White", "By towing a small island through the Sea of Clouds, he hopes to lure the ravenous primal out of hiding"),
 # #313 Bolt, Chain, and Island
 "M313a": ("Chief Sonu gives you an island for bait.", "Bolt, Chain, and Island", "Chief Sonu declares that you will have your island"),
 "M313b": ("Bismarck, Lord of Mists, falls.", "Bolt, Chain, and Island", "the Lord of Mists falls like so many before Him"),
 "M313c": ("Hydaelyn's voice resounds in your mind again, faintly.", "Bolt, Chain, and Island", "resounds in your mind once more, though you must strain to make out Her words"),
 "M313d": ("An Ascian and the archbishop bar your path and wrest the key from you.", "Bolt, Chain, and Island", "barring your path. After wresting the key from your grasp"),
 "M313e": ("The Ascian says your blessing of Light has returned at a fraction of its strength.", "Bolt, Chain, and Island", "observes that you have regained the blessing of Light—albeit at a fraction of its former strength"),
 "M313f": ("The key's beam points the way to Azys Lla, and the pair depart aboard the Soleil.", "Bolt, Chain, and Island", "emits a beam of light pointing the way to … The pair then depart aboard the"),
 "M313g": ("The key unlocks Azys Lla and the secrets of Allag.", "Bolt, Chain, and Island", "The key to Azys Lla and the secrets of Allag."),
 # #314 A Difference of Opinion
 "M314a": ("The Zundu village is overrun with imperial troops.", "A Difference of Opinion", "village, only to find it overrun with imperial troops"),
 "M314b": ("Varis is the newly crowned Emperor of Garlemald.", "A Difference of Opinion", "the newly crowned Emperor of"),
 "M314c": ("Varis means to bring the eikons to heel, even by extermination.", "A Difference of Opinion", "'Tis my solemn charge as emperor to bring the eikons to heel. If this requires the extermination of certain elements, then so be it."),
 "M314d": ("Lucia, piloting magitek armor, breaks up the execution.", "A Difference of Opinion", "piloting a suit of magitek armor, rushes to your side"),
 "M314e": ("Alphinaud vows to keep opposing the Empire's attempts to claim Eorzea.", "A Difference of Opinion", "and that is why we will continue to oppose your every attempt to claim Eorzea!"),
 "M314f": ("Varis promises to meet you again.", "A Difference of Opinion", "We shall meet again, Warrior of Light. On that you have my word."),
 "M314g": ("Regula orders a withdrawal under the guns of an imperial battleship.", "A Difference of Opinion", "Regula orders an immediate withdrawal, covered by the guns of the imperial battleship overhead"),
 "M314h": ("No Zundu died in the raid.", "A Difference of Opinion", "miraculously, no Zundu died in the imperial raid"),
 "M314i": ("Alphinaud judges that Varis wants only to reach Azys Lla.", "A Difference of Opinion", "Plainly, Varis is only interested in reaching Azys Lla."),
 # #315 One Good Turn
 "M315a": ("Wedge works out the heading to Azys Lla from the key's beam.", "One Good Turn", "now knows the heading that will lead you to"),
 "M315b": ("Lucia is a Garlean defector and sister to Livia, whom you slew.", "One Good Turn", "defector, and sister to … whom you slew in battle"),
 "M315c": ("Lucia was sent to Ishgard to investigate Allagan relics thought to be in the Vault.", "One Good Turn", "'Twas believed that the Allagan relics of great worth were stored in the Vault, and I was sent to investigate."),
 "M315d": ("Aymeric accepted Lucia into his service.", "One Good Turn", "he was good enough to accept me into his service."),
 "M315e": ("Lucia holds no grudge, and Cid takes her at her word.", "One Good Turn", "Lucia claims to hold no grudge against you"),
 "M315f": ("Azys Lla is a floating isle behind an energy barrier that nearly tears the Enterprise apart.", "One Good Turn", "the clouds part to reveal the floating isle of Azys Lla … a powerful energy barrier which threatens to tear the"),
 "M315g": ("Cid turns back to Ishgard.", "One Good Turn", "Cid turns the airship around and sets course for"),
 "M315h": ("Cid presumes the Soleil passed through the barrier unscathed.", "One Good Turn", "I can only presume the ''Soleil'' passed through the barrier unscathed."),
 # #316 An Engineering Enterprise
 "M316a": ("Alphinaud calls a meeting on breaching Azys Lla's defenses.", "An Engineering Enterprise", "has called a meeting to discuss how"),
 "M316b": ("The barrier turns surrounding aether into a wall of lightning.", "An Engineering Enterprise", "polarizes its elemental aspect to produce what is, in effect, a wall of lightning."),
 "M316c": ("The archbishop and his cronies are on the isle.", "An Engineering Enterprise", "the archbishop and his cronies are enjoying the view from its top."),
 "M316d": ("Cid would pierce the barrier with a ram of condensed aether, but needs an authority such as an Archon to design it.", "An Engineering Enterprise", "by mounting a ram of condensed aether on the … an authority such as an"),
 "M316e": ("Tataru has a clue to the whereabouts of a missing comrade.", "An Engineering Enterprise", "she claimed to have acquired a clue pointing to the whereabouts of one of your missing comrades"),
 "M316f": ("Tataru has made progress in the search for the Archons.", "An Engineering Enterprise", "Tataru confirms that she has made progress in the search for the Archons."),
 # #317 Aetherial Trail
 "M317a": ("Tataru had Pipin search the watercourse beneath Ul'dah, where Minfilia, Thancred and Y'shtola were last seen.", "Aetherial Trail", "to conduct a search of the watercourse beneath"),
 "M317b": ("Your friends were not among the dead found there.", "Aetherial Trail", "Be at ease, Master Alphinaud - your friends were not among the deceased."),
 "M317c": ("From her wand, Urianger divines that Y'shtola used a forbidden teleportation magick.", "Aetherial Trail", "divines that Y'shtola invoked a forbidden teleportation magick and was sent to an unknown location"),
 "M317d": ("Sharlayan's scholars forbade the spell.", "Aetherial Trail", "Know that the scholars of Sharlayan forbade the use of this spell—and with good reason."),
 "M317e": ("Y'shtola likely remains adrift in the Lifestream beneath the Twelveswood.", "Aetherial Trail", "where she likely remains adrift in the Lifestream"),
 "M317f": ("Only the elementals can find her in the Lifestream.", "Aetherial Trail", "only the elementals will be able to find Y'shtola within the Lifestream."),
 "M317g": ("Alphinaud resolves to seek the Elder Seedseer's aid.", "Aetherial Trail", "resolves to petition the aid of the"),
 # #318 Lost in the Lifestream
 "M318a": ("Alphinaud arranges an audience with the Elder Seedseer.", "Lost in the Lifestream", "has arranged an audience with the [[Elder Seedseer]]"),
 "M318b": ("Kan-E-Senna agrees to seek the elementals' aid.", "Lost in the Lifestream", "Kan-E-Senna readily agrees to petition the elementals' aid in searching the"),
 "M318c": ("The elementals need aether akin to Y'shtola's.", "Lost in the Lifestream", "Nay, they must needs be presented with aether which is akin to hers."),
 "M318d": ("Y'shtola has a sister living in Gridania.", "Lost in the Lifestream", "Y'shtola has a sister who came to live in Gridania."),
 "M318e": ("Y'mhitra and Y'shtola share a father.", "Lost in the Lifestream", "Though we were born of different mothers, our veins course with the same father's blood."),
 "M318f": ("Y'shtola is drawn from the Lifestream, unconscious but alive.", "Lost in the Lifestream", "they succeed in plucking Y'shtola from the Lifestream, insensible but alive."),
 "M318g": ("Y'shtola is taken to the Roost.", "Lost in the Lifestream", "A room has been readied at the Roost. Pray bear her thither at once."),
 # #319 Tataru's Surprise
 "M319a": ("Tataru has prepared a surprise for Y'shtola's return.", "Tataru's Surprise", "has been preparing a surprise for"),
 "M319b": ("Y'shtola brought the tunnel down so Alphinaud and Minfilia could escape.", "Tataru's Surprise", "I brought the tunnel down that you and Minfilia might escape."),
 "M319c": ("Y'shtola tried to teleport Thancred away.", "Tataru's Surprise", "I invoked a teleportation magick in hopes of spiriting Thancred away, at least."),
 "M319d": ("The others remain unaccounted for.", "Tataru's Surprise", "They remain unaccounted for. You are the only one we have been able to find."),
 "M319e": ("Y'shtola cannot build an aetheric ram, but her former master Matoya could.", "Tataru's Surprise", "flatly states that she lacks the knowledge to build an aetheric ram … However, she knows someone who could: her former master,"),
 "M319f": ("Y'shtola senses the aether more keenly than before.", "Tataru's Surprise", "I seem to sense the aether around me more keenly than before."),
 "M319g": ("Matoya is a leading figure in aetheric research.", "Tataru's Surprise", "A leading figure in the field of aetheric research"),
 # #320 Onward to Sharlayan
 "M320a": ("Matoya lives as a hermit on the fringes of Sharlayan, in the Dravanian hinterlands.", "Onward to Sharlayan", "has been living as a hermit on the fringes of"),
 "M320b": ("Matoya refused to join the exodus.", "Onward to Sharlayan", "However, Matoya refused to join the exodus."),
 "M320c": ("Alphinaud and Alisaie were born in Sharlayan.", "Onward to Sharlayan", "Though Alisaie and I were born in Sharlayan, our days there were short."),
 "M320d": ("You and Alphinaud will accompany Y'shtola to Sharlayan.", "Onward to Sharlayan", "It is decided that you and Alphinaud will accompany Y'shtola on the expedition to Sharlayan."),
 # #321 A Great New Nation
 "M321a": ("Goblins mean to found a new nation in Sharlayan, aided by treasure hunters.", "A Great New Nation", "the goblins mean to found a new nation here in Sharlayan, aided by treasure hunters who have come seeking the city's artifacts"),
 "M321b": ("Alphinaud convinces the goblin leader, Slowfix, of your peaceful purpose.", "A Great New Nation", "manages to defuse the situation by convincing the goblin leader"),
 "M321c": ("Slowfix asks for help with Idyllshire's problems in exchange for passage.", "A Great New Nation", "In exchange for passage through the settlement, Slowfix asks that you help the denizens of"),
 "M321d": ("Sharlayans crossed the seas to Eorzea in search of knowledge.", "A Great New Nation", "men from the northern nation of Sharlayan journeyed across the seas to Eorzea in search of knowledge."),
 # #322 Golems Begone
 "M322a": ("The Sharlayans' golem sentinels can be unmade with a coded command.", "Golems Begone", "The automata were employed as sentinels, and by design can be unmade with a coded command."),
 "M322b": ("With the golems gone, Idyllshire can expand.", "Golems Begone", "The goblin is pleased to hear that the golems will no longer impede the expansion effort."),
 # #323 An Illuminati Incident
 "M323a": ("Slowfix asks you to rescue his friend from Illuminati territory.", "An Illuminati Incident", "rescue his friend who has ventured into"),
 "M323b": ("The Illuminati seek retribution on Brayflox for a stolen cheese recipe.", "An Illuminati Incident", "bent on bloody retribution for their stolen cheese recipe"),
 "M323c": ("You rout the Illuminati.", "An Illuminati Incident", "you succeed in putting the enemy to rout"),
 # #324 Leaving Idyllshire
 "M324a": ("Slowfix names you and your companions honored citizens, free to cross the Thaliak River.", "Leaving Idyllshire", "names you and your companions honored citizens of … thus according you the right to cross the"),
 "M324b": ("Y'shtola was upset at first that her home was occupied.", "Leaving Idyllshire", "I must confess, at first it upset me to learn that my home had been occupied by others."),
 "M324c": ("Matoya's dwelling is a short distance away.", "Leaving Idyllshire", "is but a short distance away. The end of your journey is in sight."),
 # #325 Matoya's Cave
 "M325a": ("Y'shtola learned from Matoya, and they reunite.", "Matoya's Cave", "I learned from the best. It has been too long, Master Matoya."),
 "M325b": ("Matoya and Louisoix were constantly at each other's throats.", "Matoya's Cave", "We were constantly at each other's throats."),
 "M325c": ("Azys Lla holds a research facility for mastering primals and dragons.", "Matoya's Cave", "The place is home to a research facility dedicated to finding ways of mastering mighty beings such as primals and dragons."),
 "M325d": ("Matoya warns Azys Lla's secrets are not fit to see the light of day.", "Matoya's Cave", "Such secrets as lie buried on Azys Lla aren't fit to see the light of day."),
 "M325e": ("Alphinaud says the Ascians have a hand in the plot.", "Matoya's Cave", "And to make matters worse, the Ascians have a hand in their plot."),
 "M325f": ("To Y'shtola's surprise, Matoya agrees to help build the ram.", "Matoya's Cave", "Much to Y'shtola's surprise, her ordinarily truculent master agrees to lend her aid to your cause."),
 # #326 Forbidden Knowledge
 "M326a": ("Matoya's aetheric converger led to a bitter falling-out with her peers.", "Forbidden Knowledge", "a device known as an aetheric converger, and how it led to a bitter falling-out between her and her peers"),
 "M326b": ("The Forum denounced the device as more likely to destroy Sharlayan than its enemies.", "Forbidden Knowledge", "it was denounced by the Forum, who claimed that my device was more likely to destroy us than our enemies"),
 "M326c": ("Her research lies sealed in a tome in the Great Gubal Library.", "Forbidden Knowledge", "compiled within a tome which now lies sealed within the"),
 "M326d": ("Your Crystal of Water regains the power of the Light.", "Forbidden Knowledge", "the Crystal of Water regains the power of the Light"),
 "M326e": ("You bring Matoya the correct tome.", "Forbidden Knowledge", "Matoya confirms that you have retrieved the correct tome."),
 # #327 An Eye for Aether
 "M327a": ("Matoya deciphers the tome so Cid can build the aetheric ram.", "An Eye for Aether", "might avail himself of her research and build the aetheric ram"),
 "M327b": ("Alphinaud proposes the Eye as the ram's power source.", "An Eye for Aether", "It has been drawing aether into itself for as long as the great wyrms have lived!"),
 "M327c": ("Minfilia is missing, and Moenbryda is gone.", "An Eye for Aether", "Alas, Minfilia is missing, along with both artifacts. And Moenbryda is gone..."),
 "M327d": ("Y'shtola's eyes have been this way since the Lifestream.", "An Eye for Aether", "It has been this way since I returned from the Lifestream."),
 "M327e": ("Matoya says the magick consumes Y'shtola's life force.", "An Eye for Aether", "I need not tell you that it consumes your very life force by sensing the aether around you."),
 "M327f": ("Estinien agrees to draw on the Eye.", "An Eye for Aether", "The power of the Eye is not to be drawn upon lightly, but I believe we have sufficient cause to do so."),
 "M327g": ("Cid sets to work building the ram.", "An Eye for Aether", "Cid sets to work with obvious relish"),
 # #328 Hour of Departure
 "M328a": ("Aymeric: by consorting with Ascians and primal powers, his father became an enemy of all that is good.", "Hour of Departure", "In consorting with the Ascians and availing himself of primal powers, my father made himself an enemy of all that is good and right in the world."),
 "M328b": ("Aymeric gives you his blessing to stop his father.", "Hour of Departure", "gives you his blessing to do whatever is necessary to stop"),
 "M328c": ("Aymeric's wounds keep him from the battle.", "Hour of Departure", "but with my wounds, I fear I would only be a burden to you."),
 "M328d": ("Hilda stays to keep the poor from storming the Pillars.", "Hour of Departure", "With the archbishop gone, some of the poor folk might get it in their heads to do somethin' stupid like stormin' the Pillars."),
 "M328e": ("Count Edmont gives you the shield his son used to save your life.", "Hour of Departure", "Lord Edmont bequeaths to you the shield that his son used to save your life."),
 "M328f": ("You renew your vow of vengeance on Ser Zephirin.", "Hour of Departure", "Inwardly, you reaffirm your vow to exact vengeance upon Ser"),
 "M328g": ("Tataru says the Scions have lost too many friends.", "Hour of Departure", "We've lost too many friends as it is."),
 # #329 The First Flight of the Excelsior
 "M329a": ("Y'shtola warns Estinien the Eye will consume him if he falters.", "The First Flight of the Excelsior", "Should you falter for so much as a moment, it will surely consume you."),
 "M329b": ("Urianger brings white auracite found among Moenbryda's last effects.", "The First Flight of the Excelsior", "arrives bearing a gift of … 's last effects"),
 "M329c": ("The ram breaks the barrier, but an imperial battleship opens fire.", "The First Flight of the Excelsior", "the newly installed aetheric ram makes short work of the … an imperial battleship appears in your wake and opens fire"),
 "M329d": ("Ysayle rides Hraesvelgr to the rescue, becomes Shiva and disables the battleship at the cost of her life.", "The First Flight of the Excelsior", "riding to the rescue upon … she engages the enemy battleship single-handed, and succeeds in incapacitating it at the cost of her own life."),
 "M329e": ("Ysayle admits she created a false cause for want of companionship.", "The First Flight of the Excelsior", "For a false cause that I created for want of the warmth of companionship."),
 "M329f": ("Y'shtola says Ysayle too was one of Hydaelyn's chosen.", "The First Flight of the Excelsior", "She, too, was one of Hydaelyn's chosen..."),
 "M329g": ("Cid's refit ship is the Enterprise Excelsior.", "The First Flight of the Excelsior", "The ''Enterprise Excelsior!'' Or simply the ''Excelsior'', if pressed for time."),
 "M329h": ("Count Edmont says his son's spirit goes with you.", "The First Flight of the Excelsior", "Yet know that wheresoever you may go, my son's spirit goes with you."),
 "M329i": ("Urianger warns that servants of Darkness lie in wait.", "The First Flight of the Excelsior", "In the place whither thou goest, servants of Darkness do lie in wait."),
 "M329j": ("You arrive in Azys Lla and pray for the allies who paid the ultimate price.", "The First Flight of the Excelsior", "When you subsequently arrive in Azys Lla, you say a silent prayer for the allies who have paid the ultimate price that you might fight on."),
 "M329k": ("Cid declares the area safe and calls a meeting.", "The First Flight of the Excelsior", "Cid declares the area safe, and calls a meeting to discuss the next step."),
 # #330 Systematic Exploration
 "M330a": ("Cid makes the landing a base to coordinate the search for the archbishop.", "Systematic Exploration", "We can coordinate the search for the archbishop from here."),
 "M330b": ("A guidance node gives you a destination: the Aetherochemical Research Facility on the Flagship.", "Systematic Exploration", "which furnishes you with a destination:"),
 "M330c": ("Someone recently reactivated Helix, this area.", "Systematic Exploration", "It appears someone recently reactivated"),
 "M330d": ("Cid wagers the archbishop woke the place with the Vanu's key.", "Systematic Exploration", "I daresay he woke the place up when he used the Vanu's key."),
 "M330e": ("Triad Control regulates the Warring Triad test subjects.", "Systematic Exploration", "a regulation facility for the 'Warring Triad' test subjects."),
 "M330f": ("Wedge calls the node Gilly.", "Systematic Exploration", "Gilly! You have to do what the chief says!"),
 # #331 In Node We Trust
 "M331a": ("You decide to trust the guidance node.", "In Node We Trust", "it is decided that you will trust the guidance node"),
 "M331b": ("The Excelsior is the only means of escape, and Cid stays to ready it.", "In Node We Trust", "Cid, the ''Excelsior'' is our sole means of escape."),
 "M331c": ("The matter conduit still works after over five millennia.", "In Node We Trust", "the guidance node expresses surprise that the conduit still functions correctly after over five millennia of disuse"),
 # #332 Chimerical Maintenance
 "M332a": ("The Beta Quadrant's labs produce chimerical life-forms.", "Chimerical Maintenance", "is home to laboratories which produce chimerical life-forms for both military and household applications."),
 "M332b": ("Chimeras siphon the energy the conduit needs.", "Chimerical Maintenance", "chimerical creatures nearby are siphoning away the energy necessary for activation"),
 "M332c": ("The Gamma Quadrant is crawling with Garlean soldiers.", "Chimerical Maintenance", "to find the place crawling with"),
 "M332d": ("Y'shtola expects the Garleans to strip the isle of its secrets.", "Chimerical Maintenance", "Nay, they will remain here long after they have stripped the isle of all its secrets."),
 # #333 Close Encounters of the VIth Kind
 "M333a": ("The Garlean force is the VIth Imperial Legion, first met at the Zundu village.", "Close Encounters of the VIth Kind", "The Garlean force present is revealed to be none other than the … which you first encountered at the"),
 "M333b": ("The legion seeks the knowledge to capture primals.", "Close Encounters of the VIth Kind", "Their purpose is to acquire the knowledge to capture"),
 "M333c": ("Regula says the Allagans found a way to capture eikons alive.", "Close Encounters of the VIth Kind", "the Allagans found a means to capture eikons alive, and their knowledge lies hid upon this isle."),
 "M333d": ("Regula, legatus of the VIth Legion, is overwhelmed but escapes by airship.", "Close Encounters of the VIth Kind", "legatus of the VIth Legion. Though you are able to overwhelm him, he sets his minions upon you and boards an"),
 "M333e": ("Alphinaud and the others hold the enemy while you press on with the Eye.", "Close Encounters of the VIth Kind", "bids you continue your pursuit of the archbishop while he and the others keep the enemy at bay. Having accepted the"),
 "M333f": ("Estinien hands you the Eye.", "Close Encounters of the VIth Kind", "Take the Eye. It should still hold enough energy to be of use to you."),
 "M333g": ("The Delta Quadrant is home to live dragons.", "Close Encounters of the VIth Kind", "where you now stand, is home to live dragons."),
 "M333h": ("Y'shtola warns a captive primal keeps nursing its hatred.", "Close Encounters of the VIth Kind", "Held in duress, a primal will continue to nurse its hatred for mankind."),
 # #334 Fetters of Lament
 "M334a": ("Midgardsormr manifests and sends you to one of his children, held in torment nearby.", "Fetters of Lament", "manifests and bids you seek out one of his children, who abides in torment nearby"),
 "M334b": ("Tiamat has been imprisoned in Azys Lla since before the Allagan Empire fell.", "Fetters of Lament", "who has been imprisoned in … since before the fall of the"),
 "M334c": ("In her grief, Tiamat accepted the Ascians' offer to resurrect Bahamut.", "Fetters of Lament", "They offered to resurrect Bahamut through their dark arts, and I, in my grief, accepted"),
 "M334d": ("The Ascians then gave Bahamut's murderers the means to entrap him.", "Fetters of Lament", "Worse, the Ascians gifted his murders the means to entrap him."),
 "M334e": ("Tiamat urges you to vanquish the Ascians.", "Fetters of Lament", "If thou wouldst end the conflict, vanquish thee the Ascians"),
 "M334f": ("Your Crystal of Fire regains its light, and you hear Hydaelyn again.", "Fetters of Lament", "your Crystal of Fire regains its light, and you find that you are able to hear"),
 "M334g": ("Midgardsormr offers to carry you to the Flagship to cast out the Darkness.", "Fetters of Lament", "Midgardsormr offers to carry you to the Flagship, that you might cast out the Darkness which lurks therein."),
 "M334h": ("Men of old devised a means to enslave dragonkind.", "Fetters of Lament", "they devised a means to enslave dragonkind..."),
 # #335 Heavensward (the cp-hw-3-0 milestone)
 "M335a": ("The guidance node opens the way and deactivates.", "Heavensward", "the guidance node bids you farewell and deactivates for what might very well be another five millennia"),
 "M335b": ("You face Lahabrea and a second Ascian, and destroy her with a blade of Light from the Eye.", "Heavensward", "you destroy her with a blade of Light forged from the Eye's remaining aether"),
 "M335c": ("The archbishop and his knights arrive bearing Haldrath's body and the Eye's twin.", "Heavensward", "the archbishop and his knights arrive, bearing the body of … ...and the Eye's long-lost twin"),
 "M335d": ("With King Thordan's soul in him, the archbishop executes Lahabrea with a divine blade.", "Heavensward", "the archbishop conjures a divine blade using the power of the second Eye, and summarily executes Lahabrea"),
 "M335e": ("You triumph over Thordan and his knights, ending their dream of a new world order.", "Heavensward", "and his knights, bringing to an end their deranged dream of founding a new world order"),
 "M335f": ("Estinien collects both Eyes and is claimed as a vessel for Nidhogg's rage.", "Heavensward", "who sullenly collects the Eye and its twin … 's lingering influence and is claimed as a vessel for the great wyrm's rage"),
 "M335g": ("Midgardsormr and Aymeric's meeting begins a journey toward peace between man and dragon.", "Heavensward", "their meeting marking the start of the journey towards peace between man and"),
 "M335h": ("The Holy See rejoins the Eorzean Alliance.", "Heavensward", "shall once more be counted a member of the Eorzean Alliance."),
 "M335i": ("Alphinaud is elated that his dream of a unified Eorzea is realized.", "Heavensward", "is elated that his dream of a unified"),
 "M335j": ("Midgardsormr says Nidhogg's rage has claimed the Azure Dragoon as its vessel.", "Heavensward", "His unbridled rage hath claimed for its vessel the one thou callest the Azure Dragoon."),
 "M335k": ("King Thordan calls himself a god sustained by a millennium of prayer and the Eye's aether.", "Heavensward", "A god who knows not cessation, whose being is sustained by a millennium of fervent prayer and the Eye's nigh-bottomless reservoir of aether."),
}

# ---- New entities (an id another era also defines, with the same category, is merged) ---------------------------
ARC1, ARC2, ARC3, ARC4, ARC5, ARC6 = ("evt-uldah-set-right", "evt-fall-of-nidhogg", "evt-ishgards-founding-lie",
                                      "evt-key-in-the-clouds", "evt-the-aetheric-ram", "evt-the-floating-isle")
ENTITIES = {
 ARC1: "event", ARC2: "event", ARC3: "event", ARC4: "event", ARC5: "event", ARC6: "event",
 "char-raubahn": "character", "char-nanamo": "character", "char-lolorito": "character", "char-ilberd": "character",
 "char-teledji": "character", "org-immortal-flames": "organization",
 "char-aymeric": "character", "char-estinien": "character", "char-ysayle": "character", "char-lucia": "character",
 "char-nidhogg": "character", "char-hraesvelgr": "character", "char-thordan": "character", "char-zephirin": "character",
 "char-edmont": "character", "char-hilda": "character",
 "org-heavens-ward": "organization", "org-temple-knights": "organization", "org-holy-see": "organization",
 "org-vanu-vanu": "organization", "char-bismarck": "character", "char-varis": "character", "char-regula": "character",
 "loc-azys-lla": "location", "org-ascians": "organization",
 "char-kan-e-senna": "character", "char-ymhitra": "character", "char-matoya": "character", "char-slowfix": "character",
 "loc-idyllshire": "location", "char-midgardsormr": "character", "char-tiamat": "character",
}

PRES = {
 # ---- Ul'dah ----
 "char-raubahn": [
   P(S[292], None, "main", "Raubahn",
     "Ul'dah's Flame General. He found that the sultana, whom the Scions were accused of poisoning, lies alive in a deathlike sleep in the palace. "
     "When Lord Lolorito confessed to the plot and handed him the means to wake her, Raubahn was reinstated as general of the Immortal Flames, "
     "though he had executed Teledji without trial.",
     ["M292a", "C50", "M292c", "M292f", "M292g", "M292i"], ["General Raubahn"]),
 ],
 "char-nanamo": [
   P(S[292], None, "main", "Nanamo",
     "The sultana of Ul'dah, whom the Scions were accused of poisoning at a royal banquet. She was given a sleeping potion in place of poison, "
     "and lies alive in a deathlike sleep in the palace. Lord Lolorito, who arranged it, has handed over the means to wake her.",
     ["C50", "M292a", "M292d", "M292f"], ["Sultana Nanamo"]),
   P(S[293], None, "main", "Nanamo",
     "The sultana of Ul'dah. Lord Lolorito had her given a sleeping potion in place of the poison the Scions were accused of using, "
     "and she has now woken, none the worse for her sleep. Raubahn believes she will soon resume her plan to place Ul'dah's government in its citizens' hands.",
     ["C50", "M292d", "M293a", "M293b"], ["Sultana Nanamo"]),
 ],
 "char-lolorito": [
   P(S[292], None, "main", "Lolorito",
     "A lord of Ul'dah who stepped in and revealed the plot against the sultana himself: he had her lady-in-waiting give her a sleeping potion in place of poison, "
     "and had Captain Ilberd lie about the assassination to turn Raubahn's rage on Teledji. He then handed over the means to wake her.",
     ["M292c", "M292d", "M292e", "M292f"]),
   P(S[293], None, "main", "Lolorito",
     "A lord of Ul'dah who arranged the sultana's false poisoning, using Captain Ilberd's lie to turn Raubahn against Teledji, then handed over the means to wake her. "
     "With the sultana awake, he warns that the Empire has built a warship to rival the Agrius, and urges repairing Teledji's damage and preparing to repel the Empire.",
     ["M292d", "M292e", "M292f", "M293c", "M293d"]),
 ],
 "char-ilberd": [
   P(S[292], None, "main", "Ilberd",
     "A captain of the Crystal Braves. Lord Lolorito says he had Ilberd lie about the assassination of the sultana, to turn Raubahn's rage against Teledji.",
     ["M292e", "C16"], ["Captain Ilberd"]),
   P(S[294], None, "main", "Ilberd",
     "A captain of the Crystal Braves who turned on Alphinaud. Lord Lolorito says he had Ilberd lie about the sultana's assassination. "
     "Ilberd has been defeated, and the 3rd Unit Braves abandoned Revenant's Toll when they learned of it. Alphinaud vows that those who sided with him will be held to account.",
     ["C16", "M292e", "M294a", "M293f"], ["Captain Ilberd"]),
 ],
 "char-teledji": [
   P(S[292], None, "main", "Teledji",
     "A wealthy man of Ul'dah. Lord Lolorito says his Carteneau Reclamation Bill was a facade to seize the Allagan machine Omega, and arranged for Raubahn's rage to fall on him. "
     "Raubahn executed him without trial.",
     ["M292h", "M292e", "M292i"]),
 ],
 "org-immortal-flames": [
   P(S[292], None, "main", "The Immortal Flames",
     "Ul'dah's army. Raubahn has been reinstated as its general.",
     ["M292g"]),
 ],
 "org-crystal-braves": [
   P(S[293], None, "main", "The Crystal Braves",
     "A company Alphinaud founded for the sake of a united Eorzea. At the royal banquet in Ul'dah it turned on the Scions, at the word of Captain Ilberd, who lied about the sultana's assassination. "
     "With the sultana awake, Alphinaud has decided to disband it, and those who sided with Ilberd will be hunted down.",
     ["C48", "C19", "M292e", "M293e", "M293f"]),
   P(S[294], None, "main", "The Crystal Braves",
     "A company Alphinaud founded for the sake of a united Eorzea, which turned on the Scions under Captain Ilberd. After Ilberd's defeat the 3rd Unit Braves abandoned Revenant's Toll, "
     "and only loyalists remain. When Alphinaud tried to disband them, they refused: the company's ideals live on, and they pledged to help the Scions find Minfilia and the others.",
     ["C48", "C19", "M294a", "M294c", "M294d", "M294e"]),
 ],
 "loc-rising-stones": [
   P(S[294], None, "main", "The Rising Stones",
     "The Scions' headquarters in Revenant's Toll, Mor Dhona, seized by the Crystal Braves after the royal banquet in Ul'dah. "
     "Since Captain Ilberd's defeat the 3rd Unit Braves have abandoned the Toll, and the Braves who remain are loyal to Alphinaud and have pledged to help the Scions.",
     ["C14", "C19", "M294a", "M294c"]),
 ],
 "char-alphinaud": [
   P(S[293], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who founded and commanded the Crystal Braves until they turned on him at the royal banquet in Ul'dah. "
     "With the sultana awake and the Scions' names cleared, he has decided to disband the Braves and be simply a member of the Scions, and he means to resume the search for his missing comrades.",
     ["C10", "C16", "C52", "M293a", "M293e", "M293g", "M293h"]),
   P(S[294], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother. He gave up command of the Crystal Braves and tried to disband them, but the loyal Braves refused and pledged to help him and the Scions. "
     "Moved to tears, he vows to earn their loyalty, and coordinates their search for the missing Scions.",
     ["C10", "M293g", "M294b", "M294c", "M294f"]),
   P(S[307], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother. In Ishgard he has stood with Ser Aymeric against the archbishop, and he has lost Lord Haurchefant, who took the Scions in when all others forsook them. "
     "He holds that if the Heavens' Ward wield primal power, the Scions must oppose them, and he is hunting the archbishop with you.",
     ["C10", "M299b", "M306h", "M307g", "M307f"]),
   P(S[320], None, "main", "Alphinaud",
     "A young Scion. He and his twin, Alisaie, were born in Sharlayan, though their days there were short. "
     "Leading the hunt for the archbishop, he goes with you and Y'shtola to the abandoned city of Sharlayan, to seek Matoya's help in breaching Azys Lla's barrier.",
     ["M320c", "M320d", "M316a", "M319e"]),
   P(HW, None, "main", "Alphinaud",
     "A young Scion who leads the Scions' efforts in Ishgard. He went with you to Azys Lla and held back the VIth Legion while you pressed on after the archbishop. "
     "With the Holy See back in the Eorzean Alliance, he is elated that his dream of a unified Eorzea is realized.",
     ["M320c", "M333e", "M335h", "M335i"]),
 ],
 # ---- Ishgard: the wyrm and the war ----
 "char-aymeric": [
   P(S[295], None, "main", "Aymeric",
     "Ser Aymeric, lord commander in Ishgard. When you laid out the plan to strike at Nidhogg in his lair, he offered his own blade, and Estinien reminded him that he must stay to protect the city.",
     ["M295d", "M295c"], ["Ser Aymeric"]),
   P(S[299], None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander. Learning that man's treachery began the war with the dragons, and that Ishgard's faith rests on a lie, he has gone to confront the archbishop with the truth. "
     "Lucia reveals that he is the archbishop's bastard son. She, Haurchefant and you stand ready to fetch him from the Vault if he does not return.",
     ["M299g", "M299a", "M299b", "M299c", "M299e"], ["Ser Aymeric"]),
   P(S[305], None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander and, Lucia says, the archbishop's bastard son. He went to confront his father with the truth about the war, and has been imprisoned, "
     "with the Heavens' Ward placed in command of the Temple Knights. Hilda's revolutionaries have joined the plan to rescue him.",
     ["M299c", "M299b", "M305e", "M305f"], ["Ser Aymeric"]),
   P(S[306], None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander and the archbishop's son. He was rescued from the Vault, wounded, and joined the chase as his father fled by airship. "
     "He cradled Lord Haurchefant as he died.",
     ["M299c", "M306f", "M306e", "M306d"], ["Ser Aymeric"]),
   P(S[307], None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander. Through the Echo you saw him confront his father, the archbishop, who admitted the church hides how the war began, and had him arrested. "
     "Now freed, he asks you and the Scions to bring his father to justice, while he stays to hold together a government his father's absence has thrown into chaos.",
     ["M307e", "M299c", "M307f", "M307h"], ["Ser Aymeric"]),
   P(S[328], None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander. He says his father, the archbishop, made himself an enemy of all that is good by consorting with the Ascians and using primal powers. "
     "Still wounded, he cannot join you, but he gives you his blessing to do whatever is needed to stop his father.",
     ["M328a", "M328c", "M328b"], ["Ser Aymeric"]),
   P(HW, None, "main", "Aymeric",
     "Ser Aymeric, Ishgard's lord commander. After his father, the archbishop, fell on Azys Lla, Aymeric met Midgardsormr at the airship landing, beginning a journey toward peace between man and dragon. "
     "The Holy See has since rejoined the Eorzean Alliance.",
     ["M328a", "M335e", "M335g", "M335h"], ["Ser Aymeric"]),
 ],
 "char-estinien": [
   P(S[295], None, "main", "Estinien",
     "A dragoon of Ishgard. With Nidhogg's eye in his possession, he believes he can stifle the wyrm's strength, and he means to strike at Nidhogg in the Aery with you alone: "
     "he told Ser Aymeric to stay and protect the city, and refused to take Alphinaud.",
     ["M295e", "M295c", "M295d", "M295f"], ["the Azure Dragoon"]),
   P(S[296], None, "main", "Estinien",
     "The Azure Dragoon of Ishgard. He flew with you to the Aery, where you brought Nidhogg down, and he gouged out the wyrm's remaining eye. "
     "A vision showed that Haldrath took both of Nidhogg's eyes long ago, so Estinien is perplexed: whence came this one? He means to wrest the truth from Hraesvelgr.",
     ["M296a", "M296b", "M296c", "M296d", "M296e"], ["the Azure Dragoon"]),
   P(S[298], None, "main", "Estinien",
     "The Azure Dragoon, who lost his family to Nidhogg's flames and took vengeance with you in the Aery. At Zenith, Hraesvelgr admitted he gave the blinded Nidhogg half his strength. "
     "Back in Ishgard, he and Ysayle helped end a heretic uprising.",
     ["M298h", "M296b", "M297c", "M298a", "M298b"], ["the Azure Dragoon"]),
   P(S[327], None, "main", "Estinien",
     "The Azure Dragoon, who slew Nidhogg with you and holds the wyrm's Eye, a boundless store of aether. "
     "Though its power is not to be drawn on lightly, he has agreed to let it power the aetheric ram that will breach Azys Lla's barrier.",
     ["M296b", "M327b", "M327f"], ["the Azure Dragoon"]),
   P(S[333], None, "main", "Estinien",
     "The Azure Dragoon, who lent the Eye to power the aetheric ram. Y'shtola warned him it will consume him if he falters, and he would have none of it. "
     "On Azys Lla he handed the Eye to you, saying it still holds enough energy to be of use.",
     ["M327f", "M329a", "M333f"], ["the Azure Dragoon"]),
   P(HW, None, "main", "Estinien",
     "The Azure Dragoon. After you defeated the archbishop on Azys Lla, Estinien collected the Eye and its twin, and was claimed as a vessel for Nidhogg's lingering rage. "
     "Midgardsormr says Nidhogg's soul lives on in him.",
     ["M335f", "M335j"], ["the Azure Dragoon"]),
 ],
 "char-nidhogg": [
   P(S[295], None, "main", "Nidhogg",
     "A great wyrm who remains in his lair, the Aery, plotting revenge. Estinien holds one of his eyes, and believes he can use it to stifle Nidhogg's strength.",
     ["M295c", "M295e"]),
   P(S[296], None, "main", "Nidhogg",
     "A great wyrm. You and Estinien brought him down in the Aery, and Estinien gouged out his remaining eye before he fell, lifeless, into the clouds. "
     "A vision showed Haldrath and his knights taking both his eyes long ago, so how he came to have this one is a mystery.",
     ["M296b", "M296c", "M296d"]),
   P(S[297], None, "main", "Nidhogg",
     "A great wyrm, slain in the Aery by you and Estinien. Long ago, after mortals took the eyes of his brood-sister Ratatoskr, he demanded an eye from his brother Hraesvelgr, "
     "to torment Ishgard's people; Hraesvelgr gave the blinded Nidhogg half his strength, which sustained him all these years.",
     ["M296b", "M297e", "M297d", "M297c", "M297g"]),
   P(HW, None, "main", "Nidhogg",
     "A great wyrm, slain in the Aery by you and Estinien. His soul lives on: when Estinien took up the Eye and its twin, Nidhogg's lingering rage claimed him as its vessel.",
     ["M296b", "M335f", "M335j"]),
 ],
 "char-hraesvelgr": [
   P(S[295], None, "main", "Hraesvelgr",
     "A great wyrm. On Alphinaud's proposal, and through an unlikely alliance with the heretics' leader, you came to speak with him.",
     ["M295g"]),
   P(S[297], None, "main", "Hraesvelgr",
     "A great wyrm, Nidhogg's brother. At Zenith he admitted that, long ago, he yielded half his strength to the blinded Nidhogg, and a vision showed him surrendering an eye. "
     "Human treachery took his brood-sister's life and his brother's reason, and he sent you, Estinien and Ysayle away.",
     ["M297c", "M297d", "M297f", "M297h"]),
   P(S[329], None, "main", "Hraesvelgr",
     "A great wyrm, Nidhogg's brother, who once gave the blinded Nidhogg half his strength. When an imperial battleship caught your airship at Azys Lla, he carried Ysayle to the rescue.",
     ["M297c", "M329d"]),
 ],
 "char-ysayle": [
   P(S[297], None, "main", "Ysayle",
     "Lady Iceheart, whose followers fight in the Dragonsong War, which Estinien says has all but consumed her life. "
     "At Zenith she heard Hraesvelgr admit that his strength sustained Nidhogg all these years.",
     ["M297a", "M297b", "M297c", "M297g"], ["Iceheart", "Lady Iceheart"]),
   P(S[298], None, "main", "Ysayle",
     "Lady Iceheart, mistress of the heretics. When they rose up in Ishgard, she told them Nidhogg is dead and the Dragonsong War is over, that the cycle of violence was born of their forefathers' treachery, "
     "and they laid down their arms at her command.",
     ["M298a", "M298b", "M298j", "M298c"], ["Iceheart", "Lady Iceheart"]),
   P(S[329], None, "main", "Ysayle",
     "Lady Iceheart, who led the heretics and ended their uprising. When an imperial battleship caught your airship at Azys Lla, she rode to the rescue on Hraesvelgr, transformed into Shiva, "
     "and disabled the battleship at the cost of her own life. She admitted that her cause was false, and Y'shtola says she too was one of Hydaelyn's chosen.",
     ["M298c", "M329d", "M329e", "M329f"], ["Iceheart", "Lady Iceheart"]),
 ],
 "char-lahabrea": [
   P(S[298], None, "main", "Lahabrea",
     "An Ascian, who once possessed Thancred and came for you when the Ultima Weapon fell. During the uprising in Ishgard he declared that it is time for the Bringer of Light to die.",
     ["C37", "C09", "M298f"]),
   P(HW, None, "main", "Lahabrea",
     "An Ascian, who once possessed Thancred. In Azys Lla's research facility he and a second Ascian fought you, and when you destroyed her he was left exposed; "
     "the archbishop, bearing King Thordan's soul, executed him with a divine blade.",
     ["C37", "M335b", "M335d"]),
 ],
 "char-thordan": [
   P(S[298], None, "main", "Thordan VII",
     "Ishgard's archbishop. When heretics rose up in the city, he ordered that the intruders be given time to sow chaos and then be crushed by the Temple Knights, "
     "so that the unrest would feed the people's fear of heretics and dragons alike.",
     ["M298e", "M298d", "M298a"], ["Archbishop Thordan VII", "Archbishop Thordan"]),
   P(S[299], None, "main", "Thordan VII",
     "Ishgard's archbishop, who used a heretic uprising to feed the people's fear of heretics and dragons. Ser Aymeric, his bastard son, has gone to confront him with the truth that the faith rests on a lie.",
     ["M298e", "M298d", "M299c", "M299b", "M299a"], ["Archbishop Thordan VII", "Archbishop Thordan"]),
   P(S[306], None, "main", "Thordan VII",
     "Ishgard's archbishop and Ser Aymeric's father. He imprisoned Aymeric and put the Heavens' Ward in command of the Temple Knights. "
     "When you stormed the Vault, he fled by airship, telling his knights that Azys Lla awaits, and Ser Zephirin's spear killed Lord Haurchefant.",
     ["M299c", "M305e", "M306e", "M306d"], ["Archbishop Thordan VII", "Archbishop Thordan"]),
   P(S[307], None, "main", "Thordan VII",
     "Ishgard's archbishop and Ser Aymeric's father. He admits the church hides the truth: King Thordan and his knights twelve slew the wyrm Ratatoskr for her eyes, and Ishgard's people must still fight and die for the lie. "
     "He has plans of his own to free them from the sins of antiquity, and has fled with the Heavens' Ward, who channel the souls of King Thordan and his knights.",
     ["M307e", "M307a", "M307d", "M306e"], ["Archbishop Thordan VII", "Archbishop Thordan"]),
   P(S[313], None, "main", "Thordan VII",
     "Ishgard's fugitive archbishop. Cid believes the Ascians tempted him as they tempted Gaius. In the Sea of Clouds, he and an Ascian took from you the key to Azys Lla and the secrets of Allag, "
     "whose beam showed the way, and departed aboard his airship, the Soleil.",
     ["M308d", "M313d", "M313g", "M313f"], ["Archbishop Thordan VII", "Archbishop Thordan"]),
   P(S[316], None, "main", "Thordan VII",
     "Ishgard's fugitive archbishop, who took the key to Azys Lla with an Ascian's help. His airship passed the isle's Allagan barrier unscathed, and he and his knights now hold the floating isle.",
     ["M313d", "M315h", "M316c"], ["Archbishop Thordan VII", "Archbishop Thordan"]),
   P(HW, None, "main", "Thordan VII",
     "Ishgard's archbishop, Ser Aymeric's father, who consorted with the Ascians. On Azys Lla he took King Thordan's soul into himself, executed Lahabrea with a blade forged from the Eye's twin, "
     "and called himself a god. You triumphed over him and his knights, ending their dream of a new world order.",
     ["M328a", "M335c", "M335d", "M335k", "M335e"], ["Archbishop Thordan VII", "Archbishop Thordan"]),
 ],
 "char-zephirin": [
   P(S[298], None, "main", "Zephirin",
     "A churchman of Ishgard who planned with the archbishop to let a heretic uprising run its course, so that it would feed the people's fear of heretics and dragons.",
     ["M298d", "M298e"], ["Ser Zephirin"]),
   P(S[306], None, "main", "Zephirin",
     "Ser Zephirin, a knight of the Heavens' Ward who serves the archbishop. When you stormed the Vault he ordered the retreat, and then, transformed, he hurled a spear of pure light at you. "
     "Lord Haurchefant took it on his shield and died.",
     ["M306i", "M306b", "M306c", "M306d"], ["Ser Zephirin"]),
   P(HW, None, "main", "Zephirin",
     "Ser Zephirin, a knight of the Heavens' Ward, whose spear killed Lord Haurchefant and on whom you vowed vengeance. On Azys Lla you triumphed over the archbishop and his knights.",
     ["M306c", "M306d", "M328f", "M335e"], ["Ser Zephirin"]),
 ],
 "org-heavens-ward": [
   P(S[305], None, "main", "The Heavens' Ward",
     "Knights of Ishgard. With Ser Aymeric imprisoned, they have been placed in command of the Temple Knights, and Ser Charibert of the Ward has accused you of plotting insurrection.",
     ["M305e", "M305c"]),
   P(S[306], None, "main", "The Heavens' Ward",
     "The archbishop's knights, who command the Temple Knights while Ser Aymeric is imprisoned. When you stormed the Vault they showed unnatural powers: a transformed Ser Zephirin killed Lord Haurchefant. "
     "They have gone with the archbishop, who told them Azys Lla awaits.",
     ["M305e", "M306b", "M306c", "M306d", "M306e"]),
   P(S[307], None, "main", "The Heavens' Ward",
     "The archbishop's knights. Your companions conclude that they use their own bodies as vessels for the souls of King Thordan and his knights twelve, and Alphinaud holds that the Scions must oppose them.",
     ["M307d", "M307g", "M306e"]),
   P(S[311], None, "main", "The Heavens' Ward",
     "The archbishop's knights, who channel the souls of King Thordan and his knights twelve. They have come with the archbishop to the Sea of Clouds in search of the key to Azys Lla.",
     ["M307d", "M311e"]),
   P(HW, None, "main", "The Heavens' Ward",
     "The archbishop's knights, who channeled the souls of King Thordan and his knights twelve. On Azys Lla you triumphed over the archbishop and his knights, ending their dream of a new world order.",
     ["M307d", "M335e"]),
 ],
 "org-temple-knights": [
   P(S[305], None, "main", "The Temple Knights",
     "Ishgard's knights, sworn to the Holy See. With their lord commander, Ser Aymeric, imprisoned, the Heavens' Ward has been put in command of them. "
     "Half stay loyal to Aymeric; the other half, who opposed his promotion, have gathered at the Vault.",
     ["M300e", "M305e", "M305h"]),
 ],
 "org-holy-see": [
   P(S[307], None, "main", "The Holy See",
     "Ishgard's church, whose faith rests on a lie: its founders, King Thordan and his knights twelve, slew the wyrm Ratatoskr for her eyes. "
     "Its archbishop has fled, and his absence has thrown the government into chaos.",
     ["M300e", "M299a", "M307a", "M307h"]),
   P(HW, None, "main", "The Holy See",
     "Ishgard's church, whose archbishop fell on Azys Lla. The Holy See has rejoined the Eorzean Alliance.",
     ["M335e", "M335h"]),
 ],
 "char-haurchefant": [
   P(S[298], None, "main", "Haurchefant",
     "A lord of House Fortemps who defended Lord Francel at his heresy trial. He met you in war-torn Ishgard during a heretic uprising, and when the heretics laid down their arms "
     "he persuaded the knights to keep the peace too.",
     ["E120e", "M298i", "M298c", "M298g"]),
   P(S[299], None, "main", "Haurchefant",
     "A lord of House Fortemps and Count Edmont's son. He brought word of Nidhogg's death and the heretics' peace to his father and Ser Aymeric, "
     "and swore on his house's sigil to stand with Aymeric, who has gone to confront the archbishop.",
     ["M299i", "M299b", "M299f"]),
   P(S[306], None, "main", "Haurchefant",
     "A lord of House Fortemps and Count Edmont's son, who took the Scions in when all others forsook them. As the archbishop fled the Vault, a transformed Ser Zephirin hurled a spear of light at you. "
     "Haurchefant raised his shield in your defense, but it gave way, and he died.",
     ["M299i", "M306h", "M306c", "M306d"]),
 ],
 "char-edmont": [
   P(S[299], None, "main", "Edmont",
     "Count Edmont, Lord Haurchefant's father. He is deeply troubled to learn that Ishgard's faith is built on a lie.",
     ["M299i", "M299a"], ["Count Edmont"]),
   P(S[306], None, "main", "Edmont",
     "Count Edmont, whose son, Lord Haurchefant, died shielding you from Ser Zephirin's spear. A knight lives to serve, to protect and to sacrifice, he tells himself, and he mourns in private.",
     ["M299i", "M306d", "M306g"], ["Count Edmont"]),
   P(S[328], None, "main", "Edmont",
     "Count Edmont, whose son, Lord Haurchefant, died saving your life. Before you left for Azys Lla, he gave you the shield his son used to save you.",
     ["M306d", "M328e"], ["Count Edmont"]),
 ],
 "char-lucia": [
   P(S[299], None, "main", "Lucia",
     "A knight whose loyalty is to Ser Aymeric alone. She revealed that he is the archbishop's bastard son, and means to fetch him from the Vault if he does not return, "
     "though she will need more allies.",
     ["M299d", "M299c", "M299e", "M299h"]),
   P(S[306], None, "main", "Lucia",
     "A Temple Knight loyal to Ser Aymeric alone. To free him from the Vault, she enlisted Hilda's revolutionaries to draw the High Houses' forces out of the city, "
     "and while you drew the Heavens' Ward away, her party rescued him.",
     ["M300e", "M299d", "M306a", "M306b", "M306f"]),
   P(S[307], None, "main", "Lucia",
     "A Temple Knight loyal to Ser Aymeric, whom she helped rescue from the Vault. With the archbishop fled, she has asked to help the Scions search for him.",
     ["M299d", "M306b", "M307i"]),
   P(S[314], None, "main", "Lucia",
     "A Temple Knight loyal to Ser Aymeric, who joined the Scions' hunt for the archbishop. In the Zundu village she broke up the Emperor's order to execute the captive Vanu, piloting a suit of magitek armor.",
     ["M299d", "M307i", "M314d"]),
   P(S[315], None, "main", "Lucia",
     "A Garlean defector, and sister to Livia, the tribunus you slew. She was sent to Ishgard to investigate Allagan relics thought to lie in the Vault, but Ser Aymeric took her into his service, "
     "and she is loyal to him alone. She holds no grudge against you, and Cid takes her at her word.",
     ["M315b", "M315c", "M315d", "M299d", "M315e"]),
 ],
 "char-livia": [
   P(S[315], None, "main", "Livia",
     "An imperial tribunus who captured the Scions in the raid on the Waking Sands, fought you in Castrum Meridianum and died. "
     "Lucia, who serves Ser Aymeric in Ishgard, has revealed herself to be Livia's sister and a Garlean defector.",
     ["K01", "K62", "M315b"]),
 ],
 "char-hilda": [
   P(S[300], None, "main", "The Mongrel",
     "The leader of revolutionaries rumored to hide in Ishgard's Brume, whom Lucia believes opened the city's gates to the heretics. "
     "Tataru knows only the name, and the people of the Brume shelter the gang and will not talk.",
     ["M300a", "M300b", "M300c", "M300d"]),
   P(S[304], None, "main", "The Mongrel",
     "The leader of revolutionaries hiding in Ishgard's Brume. She is the raven-haired, ruby-eyed child of an Elezen nobleman and the Hyuran maidservant he cast out when she became pregnant; "
     "her mother died in the Brume after giving birth. She and her followers embrace their parentage. Where she hides is still unknown.",
     ["M300a", "M304b", "M304c", "M302b", "M302c", "M304a", "M304d"]),
   P(S[305], None, "main", "Hilda",
     "The leader of the Brume's revolutionaries, who calls herself the Mongrel out of pride in her mixed heritage: the child of an Elezen nobleman and a Hyuran maidservant. "
     "She rescued Tataru from two men, and when Ser Aymeric was imprisoned, she agreed to help rescue him; her followers are pledged to his cause.",
     ["M305b", "M305g", "M304c", "M305e", "M305f", "M305i"], ["The Mongrel"]),
   P(S[306], None, "main", "Hilda",
     "The leader of the Brume's revolutionaries, who calls herself the Mongrel. Her sympathizers among the High Houses' knights spread word of a heretic army outside the gates, "
     "drawing the city's defenders away so that Ser Aymeric could be rescued from the Vault.",
     ["M305b", "M305g", "M306a", "M306f"], ["The Mongrel"]),
   P(S[328], None, "main", "Hilda",
     "The leader of the Brume's revolutionaries, who calls herself the Mongrel and helped rescue Ser Aymeric. With the archbishop gone, she stays in Ishgard, fearing the poor may try to storm the Pillars.",
     ["M305b", "M305g", "M306a", "M328d"], ["The Mongrel"]),
 ],
 "char-tataru": [
   P(S[300], None, "main", "Tataru",
     "The Scions' receptionist, who was rescued from the Crystal Braves after the royal banquet. She is gathering word in Ishgard's Forgotten Knight tavern, "
     "but knows only that the Brume's revolutionaries are led by someone called the Mongrel.",
     ["C15", "C53", "M300c"]),
   P(S[305], None, "main", "Tataru",
     "The Scions' receptionist. Searching the Brume alone for its revolutionaries, she was chased by two men until their leader, Hilda, called them off.",
     ["C15", "M305a", "M305b"]),
   P(S[317], None, "main", "Tataru",
     "The Scions' receptionist, who keeps searching for the missing Scions. She has a clue to one of them, and had Pipin search the watercourse beneath Ul'dah, "
     "where Minfilia, Thancred and Y'shtola were last seen: he found Y'shtola's wand.",
     ["C15", "M316e", "M316f", "M317a", "M317c"]),
   P(S[319], None, "main", "Tataru",
     "The Scions' receptionist, who had Pipin search the watercourse beneath Ul'dah and so set the Scions on Y'shtola's trail. "
     "With Y'shtola drawn from the Lifestream alive, Tataru gave her the surprise she had prepared for her return.",
     ["C15", "M317a", "M318f", "M319a"]),
 ],
 # ---- Sea of Clouds ----
 "char-cid": [
   P(S[295], None, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. At Ishgard's Skysteel Manufactory he has built the manacutter, which has just made its first successful test flight.",
     ["M295b", "M295a"]),
   P(S[308], None, "main", "Cid",
     "A brilliant engineer who built the Ironworks. Shaken by Lord Haurchefant's death and the archbishop's escape, he has put his airship, the Enterprise, at your disposal for the chase. "
     "He believes the Ascians tempted the archbishop as they tempted Gaius with the Ultima Weapon, and that Azys Lla is a source of cosmic power.",
     ["M308c", "M308f", "M308d", "M308e"]),
   P(S[312], None, "main", "Cid",
     "A brilliant engineer, captain of the Enterprise. To beat the Heavens' Ward to the key in Bismarck's belly, he plans to tow an island through the Sea of Clouds to lure the primal close.",
     ["M308f", "M312a", "M312e"]),
   P(S[316], None, "main", "Cid",
     "A brilliant engineer, captain of the Enterprise. Azys Lla's barrier turns aether into a wall of lightning and nearly tore his ship apart. "
     "He would pierce it with a ram of condensed aether mounted on the Enterprise, but designing one needs an authority such as an Archon.",
     ["M315f", "M316b", "M316d"]),
   P(S[327], None, "main", "Cid",
     "A brilliant engineer, captain of the Enterprise. Matoya has deciphered her research so he can build the aetheric ram to breach Azys Lla's barrier, "
     "and with the Eye as its power source, he has set to work.",
     ["M327a", "M327b", "M327g"]),
   P(S[329], None, "main", "Cid",
     "A brilliant engineer. His refit airship, the Enterprise Excelsior, broke through Azys Lla's barrier with the aetheric ram and carried you onto the floating isle, "
     "where he has declared the area safe and called a meeting on the next step.",
     ["M329g", "M329c", "M329j", "M329k"]),
 ],
 "char-urianger": [
   P(S[309], None, "main", "Urianger",
     "A learned Sharlayan Scion who studied under Louisoix and keeps the Waking Sands. With no news yet of the missing Scions, he is pursuing promising leads.",
     ["C54", "C21", "M309a"]),
   P(S[317], None, "main", "Urianger",
     "A learned Sharlayan Scion. From Y'shtola's wand, found beneath Ul'dah, he divined that she used a teleportation magick Sharlayan's scholars forbade, and that she is adrift in the Lifestream.",
     ["C54", "M317c", "M317d", "M317e"]),
   P(S[329], None, "main", "Urianger",
     "A learned Sharlayan Scion who traced Y'shtola into the Lifestream. Before you left for Azys Lla, he brought you white auracite from Moenbryda's last effects, and warned that servants of Darkness lie in wait.",
     ["C54", "M317c", "M329b", "M329i"]),
 ],
 "org-vanu-vanu": [
   P(S[308], None, "main", "The Vanu Vanu",
     "A beast tribe of the Sea of Clouds, who firmly hold the northern reaches where the archbishop's airship vanished.",
     ["M308a", "M308b"]),
   P(S[311], None, "main", "The Vanu Vanu",
     "A beast tribe of the Sea of Clouds. Those of the Zundu village are not openly hostile to you. Imperial troops have been hunting them, "
     "and their god, the primal Bismarck, has swallowed the island that held the key to Azys Lla.",
     ["M310d", "M310a", "M311c", "M311d", "M311e"]),
   P(S[313], None, "main", "The Vanu Vanu",
     "A beast tribe of the Sea of Clouds. Swayed by Alphinaud's denunciation of their patron deity, Bismarck, as a false savior, Chief Sonu of the Zundu gave you an island for bait, and you slew the primal.",
     ["M312b", "M313a", "M313b"]),
   P(S[314], None, "main", "The Vanu Vanu",
     "A beast tribe of the Sea of Clouds, whose god Bismarck you slew. Imperial troops overran the Zundu village and the Emperor ordered the captives executed, but Lucia broke it up, and no Zundu died.",
     ["M313b", "M314a", "M314d", "M314h"]),
 ],
 "char-bismarck": [
   P(S[311], None, "main", "Bismarck",
     "A primal, the god of the Vanu Vanu, who swallows islands whole in the Sea of Clouds. Imperial troops have engaged him, and the key to Azys Lla lay on an island he devoured.",
     ["M311c", "M311d", "M311b", "M311e"], ["Lord of the Mists"]),
   P(S[312], None, "main", "Bismarck",
     "A primal, patron deity of the Vanu Vanu, who swallows islands whole. The keeper of tales says he was slain by his brothers and reborn in the heavens, "
     "a merciful being at odds with his recent rampage. The key to Azys Lla lies in his belly.",
     ["M312b", "M311c", "M312c", "M312d", "M311e"], ["Lord of the Mists"]),
   P(S[313], None, "main", "Bismarck",
     "A primal, patron deity of the Vanu Vanu. You lured him with an island the Zundu gave as bait and slew him, but the key to Azys Lla he swallowed was taken from you.",
     ["M312b", "M313a", "M313b", "M313d"], ["Lord of the Mists"]),
 ],
 "loc-azys-lla": [
   P(S[306], None, "main", "Azys Lla",
     "A place the archbishop named as he fled the Vault by airship, telling his knights that Azys Lla awaits.",
     ["M306e"]),
   P(S[308], None, "main", "Azys Lla",
     "A place the archbishop and his knights are bound for. Cid guesses it is a source of cosmic power he covets.",
     ["M306e", "M308e"]),
   P(S[311], None, "main", "Azys Lla",
     "A land of forbidden secrets, which the Vanu Vanu call the ancient birthplace of sin. The archbishop and the Heavens' Ward seek the key to it, which lay on an island the primal Bismarck swallowed.",
     ["M311f", "M311e"]),
   P(S[313], None, "main", "Azys Lla",
     "A land of forbidden secrets holding the secrets of Allag. The archbishop and an Ascian took its key from you, and its beam pointed the way there.",
     ["M311f", "M313g", "M313d", "M313f"]),
   P(S[315], None, "main", "Azys Lla",
     "A floating isle that holds the secrets of Allag, guarded by an Allagan energy barrier that nearly tore the Enterprise apart. The archbishop's airship, carrying the key, passed through unscathed.",
     ["M313g", "M315f", "M315h"]),
   P(S[316], None, "main", "Azys Lla",
     "A floating Allagan isle, held by the archbishop and his knights. Its barrier turns surrounding aether into a wall of lightning; without the key, only a ram of condensed aether might pierce it.",
     ["M316c", "M316b", "M316d"]),
   P(S[325], None, "main", "Azys Lla",
     "A floating Allagan isle, held by the archbishop and guarded by a barrier of lightning. Matoya says it holds a research facility for mastering primals and dragons, whose secrets are not fit to see the light of day.",
     ["M316c", "M316b", "M325c", "M325d"]),
   P(S[329], None, "main", "Azys Lla",
     "A floating Allagan isle with a research facility for mastering primals and dragons. The aetheric ram broke its barrier, and you have landed there in pursuit of the archbishop.",
     ["M325c", "M329c", "M329j"]),
   P(S[330], None, "main", "Azys Lla",
     "A floating Allagan isle where you pursue the archbishop. Someone has recently reactivated it, likely with the key, and a guidance node points you to the Aetherochemical Research Facility on the Flagship, "
     "where Triad Control regulates test subjects called the Warring Triad.",
     ["M330c", "M330d", "M330b", "M330e"]),
   P(S[333], None, "main", "Azys Lla",
     "A floating Allagan isle. Its labs bred chimeras, and the Delta Quadrant is home to live dragons. The VIth Imperial Legion is there too, seeking the Allagans' means of capturing primals.",
     ["M332a", "M333g", "M333a", "M333c"]),
   P(S[334], None, "main", "Azys Lla",
     "A floating Allagan isle, where men of old devised a means to enslave dragonkind. The great wyrm Tiamat has been imprisoned there since before the Allagan Empire fell.",
     ["M334h", "M334b"]),
   P(HW, None, "main", "Azys Lla",
     "A floating Allagan isle. In its Aetherochemical Research Facility you destroyed one Ascian, saw the archbishop execute Lahabrea, and defeated him and his knights; then the facility began to collapse.",
     ["M335a", "M335b", "M335d", "M335e"]),
 ],
 "org-ascians": [
   P(S[308], None, "main", "The Ascians",
     "Elusive beings who, Cid believes, have tried to tempt Ishgard's archbishop as they once tempted Gaius with the Ultima Weapon.",
     ["M308d"]),
   P(S[313], None, "main", "The Ascians",
     "Elusive beings who tempted Gaius with the Ultima Weapon. One of them stood with Ishgard's archbishop in the Sea of Clouds and took the key to Azys Lla from you, "
     "noting that your blessing of Light has returned at a fraction of its strength.",
     ["M308d", "M313d", "M313e"]),
   P(S[334], None, "main", "The Ascians",
     "Elusive beings who aid Ishgard's archbishop. Tiamat says they offered to resurrect Bahamut for her, then gave his murderers the means to trap him, and she urges you to vanquish them.",
     ["M328a", "M334c", "M334d", "M334e"]),
   P(HW, None, "main", "The Ascians",
     "Elusive beings who aided Ishgard's archbishop. In Azys Lla's research facility Lahabrea and a second Ascian fought you: you destroyed her, and the archbishop executed Lahabrea.",
     ["M328a", "M335b", "M335d"]),
 ],
 "char-varis": [
   P(S[314], None, "main", "Varis",
     "The newly crowned Emperor of Garlemald, who came in person to the Sea of Clouds. He believes it his charge to bring the eikons to heel, even by extermination, "
     "and ordered captive Vanu executed. Alphinaud judges that he seeks Azys Lla, and Varis has promised to meet you again.",
     ["M314b", "M314c", "M314i", "M314f"], ["Emperor Varis"]),
 ],
 "char-regula": [
   P(S[314], None, "main", "Regula",
     "An imperial commander whose troops overran the Zundu village in the Sea of Clouds. He withdrew under the guns of an imperial battleship when Lucia attacked.",
     ["M314a", "M314g"]),
   P(S[333], None, "main", "Regula",
     "Legatus of the VIth Imperial Legion, whose troops raided the Zundu village. On Azys Lla he seeks the Allagans' means of capturing eikons alive. "
     "You overwhelmed him, but he escaped by airship toward the research facility.",
     ["M333d", "M333a", "M333c"]),
 ],
 "org-garlean-empire": [
   P(S[293], None, "main", "The Garlean Empire",
     "An empire that tried to conquer Eorzea, whose legatus Gaius was slain with the Ultima Weapon. It has built a new warship to rival the Agrius.",
     ["K73", "M293c"]),
   P(S[314], None, "main", "The Garlean Empire",
     "An empire that has tried to conquer Eorzea. Its newly crowned Emperor, Varis, came to the Sea of Clouds in person, seeking Azys Lla, and means to bring the eikons to heel even by extermination.",
     ["M314b", "M314i", "M314c", "M314e"]),
   P(S[333], None, "main", "The Garlean Empire",
     "An empire ruled by the newly crowned Emperor Varis. Its VIth Imperial Legion, under Regula, is on Azys Lla seeking the Allagans' means of capturing primals.",
     ["M314b", "M333a", "M333b", "M333c"]),
 ],
 # ---- The road to Matoya ----
 "char-yshtola": [
   P(S[317], None, "main", "Y'shtola",
     "A Sharlayan Scion, last seen beneath Ul'dah after the royal banquet. Her wand was found in the collapsed watercourse: she invoked a teleportation magick that Sharlayan's scholars forbade, "
     "and Urianger believes she is adrift in the Lifestream beneath the Twelveswood, where no soul survives for long.",
     ["M317a", "M317c", "M317d", "M317e"]),
   P(S[318], None, "main", "Y'shtola",
     "A Sharlayan Scion, lost in the Lifestream after a forbidden teleportation magick. With her sister Y'mhitra's help, the Seedseers and the elementals drew her out, unconscious but alive, "
     "and she is recovering at the Roost.",
     ["M317c", "M318e", "M318f", "M318g"]),
   P(S[319], None, "main", "Y'shtola",
     "A Sharlayan Scion, back from the Lifestream. She brought the tunnel beneath Ul'dah down so Alphinaud and Minfilia could escape, and tried to teleport Thancred away. "
     "She now senses the aether more keenly. She cannot build an aetheric ram, but her former master, Matoya, could.",
     ["M318f", "M319b", "M319c", "M319f", "M319e"]),
   P(S[327], None, "main", "Y'shtola",
     "A Sharlayan Scion, Matoya's former student, who led you to her master. Her eyes have lost their light since the Lifestream, and Matoya warns that the magick she now uses to sense the aether consumes her life force.",
     ["M325a", "M327d", "M327e"]),
 ],
 "char-minfilia": [
   P(S[317], None, "main", "Minfilia",
     "Leader of the Scions, who stayed behind during the escape from the royal banquet in Ul'dah, saying that Hydaelyn was speaking to her. "
     "A search of the watercourse beneath Ul'dah, where she was last seen, did not find her among the dead. She is still missing.",
     ["C17", "M317a", "M317b"]),
 ],
 "char-thancred": [
   P(S[319], None, "main", "Thancred",
     "A Scion and bard who stayed behind with Y'shtola to stop the pursuit after the royal banquet in Ul'dah. Y'shtola tried to teleport him away, but he remains unaccounted for.",
     ["C18", "M319c", "M319d"]),
 ],
 "char-kan-e-senna": [
   P(S[318], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania. At Alphinaud's request she petitioned the elementals, who could find Y'shtola in the Lifestream only by aether akin to hers, "
     "and with the Seedseers drew Y'shtola out alive.",
     ["M318a", "M318b", "M318c", "M318f"], ["the Elder Seedseer"]),
 ],
 "char-ymhitra": [
   P(S[318], None, "main", "Y'mhitra",
     "Y'shtola's sister, who lives in Gridania; they have different mothers but the same father. Her aether, akin to her sister's, let the elementals find Y'shtola in the Lifestream.",
     ["M318d", "M318e", "M318c", "M318f"]),
 ],
 "char-matoya": [
   P(S[319], None, "main", "Matoya",
     "Y'shtola's former master, a leading figure in aetheric research. Y'shtola says she could build the aetheric ram needed to breach Azys Lla's barrier.",
     ["M319e", "M319g"]),
   P(S[320], None, "main", "Matoya",
     "Y'shtola's former master, without rival in aetheric research. She refused to join the Sharlayan exodus, and lives as a hermit on the fringes of Sharlayan, in the Dravanian hinterlands.",
     ["M319e", "M320b", "M320a"]),
   P(S[325], None, "main", "Matoya",
     "A Sharlayan hermit and master of aetheric research, who taught Y'shtola and was constantly at odds with Louisoix. She warns that Azys Lla's secrets are not fit to see the light of day, "
     "but to Y'shtola's surprise she agreed to help build the aetheric ram.",
     ["M325a", "M325b", "M325d", "M325f"]),
   P(S[326], None, "main", "Matoya",
     "A Sharlayan hermit who taught Y'shtola. Her aetheric converger set her against her peers: the Forum denounced it as more likely to destroy Sharlayan than its enemies, "
     "and she sealed her research in a tome in the Great Gubal Library, which you have now brought back.",
     ["M325a", "M326a", "M326b", "M326c", "M326e"]),
   P(S[327], None, "main", "Matoya",
     "A Sharlayan hermit who taught Y'shtola. She deciphered her sealed tome so that Cid can build the aetheric ram, and warns Y'shtola that the magick she uses to sense the aether consumes her life force.",
     ["M325a", "M327a", "M327e"]),
 ],
 "char-slowfix": [
   P(S[321], None, "main", "Slowfix",
     "A goblin who leads Idyllshire, a new nation goblins and treasure hunters are founding in the ruins of Sharlayan. Alphinaud convinced him of your peaceful purpose, "
     "and he offers passage across the river if you help with the settlement's problems.",
     ["M321a", "M321b", "M321c"]),
   P(S[324], None, "main", "Slowfix",
     "The goblin leader of Idyllshire. After you cleared its golems and rescued his friend Brayflox from the Illuminati, he named you and your companions honored citizens, free to cross the Thaliak River.",
     ["M321b", "M322b", "M323a", "M323c", "M324a"]),
 ],
 "loc-idyllshire": [
   P(S[321], None, "main", "Idyllshire",
     "A settlement in the ruins of Sharlayan, where goblins mean to found a new nation, aided by treasure hunters who came for the city's artifacts. Its leader is the goblin Slowfix.",
     ["M321a", "M321b", "M321d"]),
   P(S[324], None, "main", "Idyllshire",
     "A goblin settlement in the ruins of Sharlayan, led by Slowfix. You cleared the Sharlayans' sentinel golems so it can expand and routed the Illuminati, "
     "and its people have made you honored citizens. Y'shtola, upset at first that her home was occupied, now believes it is in good hands.",
     ["M322a", "M322b", "M323c", "M324a", "M324b"]),
 ],
 # ---- Azys Lla ----
 "char-midgardsormr": [
   P(S[334], None, "main", "Midgardsormr",
     "A great wyrm who manifested in Azys Lla's Delta Quadrant and sent you to one of his children, Tiamat, held in torment there. "
     "Convinced at last of your worth, he offered to carry you to the Flagship to cast out the Darkness within.",
     ["M334a", "M334b", "M334g"]),
   P(HW, None, "main", "Midgardsormr",
     "A great wyrm who carried you to Azys Lla's Flagship. After the archbishop's fall he bore you away from the collapsing facility, and in Ishgard he met Ser Aymeric, "
     "beginning a journey toward peace between man and dragon. He warns that Nidhogg's rage has claimed Estinien.",
     ["M334g", "M335g", "M335j"]),
 ],
 "char-tiamat": [
   P(S[334], None, "main", "Tiamat",
     "A great wyrm, one of Midgardsormr's children, imprisoned in Azys Lla since before the Allagan Empire fell. In her grief she accepted the Ascians' offer to resurrect Bahamut, "
     "and they then gave his murderers the means to trap him. She urges you to vanquish the Ascians.",
     ["M334a", "M334b", "M334c", "M334d", "M334e"]),
 ],
 "org-scions": [
   P(S[307], None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, scattered since the royal banquet in Ul'dah, when its members were branded fugitives. The Crystal Braves have returned to its side, "
     "and in Ishgard Alphinaud and you have joined Ser Aymeric against the archbishop: if the Heavens' Ward wield primal power, the Scions must oppose them.",
     ["C50", "C22", "M294c", "M307f", "M307g"]),
   P(HW, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future. Alphinaud, Y'shtola and you followed Ishgard's archbishop to Azys Lla and ended his plans, and the Holy See has rejoined the Eorzean Alliance. "
     "Minfilia is still missing.",
     ["M329c", "M335e", "M335h", "M327c"]),
 ],
 "org-eorzean-alliance": [
   P(HW, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states, whose Operation Archon ended Gaius and the Ultima Weapon. The Holy See of Ishgard has rejoined it, fulfilling Alphinaud's dream of a unified Eorzea.",
     ["K73", "M335h", "M335i"]),
 ],
}

# ---- Arc recaps: one presentation per step, each standing on its own ---------------------------------------------
N1, N2, N3, N4, N5, N6 = ("Ul'dah Set Right", "The Fall of Nidhogg", "Ishgard's Founding Lie", "The Key in the Clouds",
                          "The Aetheric Ram", "The Floating Isle")
L1 = "The Scions were branded fugitives after the sultana's apparent poisoning at a royal banquet in Ul'dah. "
L3 = "Ser Aymeric learned that Ishgard's faith rests on a lie: man's treachery began the war with the dragons. "
L4 = "Archbishop Thordan fled Ishgard by airship for a place called Azys Lla, and you and Alphinaud are hunting him. "
L5 = "The archbishop holds Azys Lla, a floating Allagan isle behind a barrier that only a ram of condensed aether might pierce. "
L6 = "Cid's aetheric ram, powered by Nidhogg's Eye, broke Azys Lla's barrier, and you have followed the archbishop onto the isle. "

PRES.update({
 ARC1: [
   P(S[292], None, "main", N1,
     L1 + "Raubahn has found she lies alive in a deathlike sleep. Yugiri traced her former lady-in-waiting, Meriel, "
     "but Lord Lolorito stepped in and confessed: he had Meriel give the sultana a sleeping potion instead of poison, and had Ilberd lie about the assassination to turn Raubahn's rage on Teledji. "
     "He handed over the means to wake her, and Raubahn was reinstated as Flame General.",
     ["C50", "M292a", "M292b", "M292c", "M292d", "M292e", "M292f", "M292g"]),
   P(S[293], None, "main", N1,
     L1 + "In truth Lord Lolorito had her given a sleeping potion, and she has woken, none the worse; she means to resume placing Ul'dah's government in its citizens' hands. "
     "Lolorito warns of a new imperial warship to rival the Agrius. Alphinaud will disband the Crystal Braves, whose captain lied about the assassination, "
     "and search for his missing comrades as simply a Scion.",
     ["C50", "M292d", "M293a", "M293b", "M293c", "M292e", "M293e", "M293g"]),
   P(S[294], None, "main", N1,
     L1 + "The sultana is awake, the plot exposed, and Ilberd, who lied about the assassination, defeated: the 3rd Unit Braves have abandoned Revenant's Toll. "
     "Alphinaud went to the Rising Stones to disband the Crystal Braves in person, but the loyal Braves refused, saying the company's ideals live on, and pledged to help the Scions find Minfilia and the others. "
     "Alphinaud was moved to tears.",
     ["C50", "M293a", "M292e", "M294a", "M294b", "M294c", "M294d", "M294e"]),
   P(S[295], None, "main", N1,
     "The sultana Nanamo is awake, Lord Lolorito's plot against her is exposed, and Captain Ilberd, who lied about it, has been defeated. "
     "The Crystal Braves refused to disband and pledged to help the Scions, and Alphinaud now coordinates their search for the missing Scions while he sends you back to Ishgard, where Cid's manacutter is ready to fly.",
     ["M293a", "M292c", "M294a", "M294c", "M295a", "M295b"]),
 ],
 ARC2: [
   P(S[295], None, "main", N2,
     "The great wyrm Nidhogg waits in his lair, the Aery, plotting revenge. Alphinaud's proposal led you to parley with Hraesvelgr, through an unlikely alliance with the heretics' leader, "
     "and now Cid's manacutter has made its first successful flight. Estinien, who holds Nidhogg's eye, means to stifle the wyrm's strength and strike with you alone: "
     "he told Ser Aymeric to stay and protect the city, and refused to take Alphinaud.",
     ["M295c", "M295g", "M295b", "M295e", "M295d", "M295f"]),
   P(S[296], None, "main", N2,
     "You and Estinien flew to the Aery on Cid's manacutters and brought Nidhogg down, and Estinien gouged out the wyrm's remaining eye. "
     "A vision showed Haldrath and his knights taking both of Nidhogg's eyes long ago, and Ishgard's founders keeping its throne empty as stewards. "
     "Whence came this eye, then? Only Hraesvelgr can tell.",
     ["M296a", "M296b", "M296c", "M296f", "M296d", "M296e"]),
   P(S[297], None, "main", N2,
     "You and Estinien slew Nidhogg in the Aery. With Ysayle, called Lady Iceheart, you returned to Zenith, and Hraesvelgr admitted that he yielded half his strength to the blinded Nidhogg. "
     "A vision showed the truth of the Dragonsong War's beginning: mortals took the eyes of Ratatoskr, the wyrms' brood-sister, and Nidhogg demanded an eye from Hraesvelgr to torment Ishgard's people. "
     "Hraesvelgr sent you away.",
     ["M296b", "M297a", "M297c", "M297i", "M297e", "M297d", "M297h"]),
   P(S[298], None, "main", N2,
     "You and Estinien slew Nidhogg, and Hraesvelgr revealed that the Dragonsong War began with mortals' treachery. Back in Ishgard, heretics had risen up. "
     "Ysayle told them Nidhogg is dead and the war has ended, and they laid down their arms; Lord Haurchefant persuaded the knights to keep the peace. "
     "But the archbishop and Zephirin had let the uprising run to feed the people's fear, and Lahabrea declares that the Bringer of Light must die.",
     ["M296b", "M297f", "M298a", "M298b", "M298c", "M298g", "M298e", "M298f"]),
 ],
 ARC3: [
   P(S[299], None, "main", N3,
     "Nidhogg is dead and the heretics have left Ishgard in peace, but at Fortemps Manor, Count Edmont and the others were troubled to learn the faith is built on a lie: man's treachery began the war. "
     "Ser Aymeric has gone to confront the archbishop with the truth. Lucia revealed he is the archbishop's bastard son, and will fetch him from the Vault if he does not return. "
     "Haurchefant, Alphinaud and you stand with her, but she needs more allies.",
     ["M299i", "M299a", "M299g", "M299b", "M299c", "M299e", "M299h"]),
   P(S[300], None, "main", N3,
     L3 + "He has gone to confront the archbishop, his father, and Lucia means to rescue him from the Vault if need be. For allies, she looks to the revolutionaries hiding in the Brume, "
     "who she believes opened the gates to the heretics. Tataru knows only that their leader is called the Mongrel, and the Brume's people shelter them and will not talk.",
     ["M299g", "M299b", "M299c", "M300a", "M300b", "M300c", "M300d"]),
   P(S[301], None, "main", N3,
     L3 + "To rescue him from the archbishop if need be, Lucia seeks the Brume's revolutionaries, led by someone called the Mongrel. "
     "Gibrillont, keeper of the Forgotten Knight, will tell you nothing outright, but for a favor he brewed a mulled wine that might loosen the right tongues.",
     ["M299g", "M299e", "M300a", "M300c", "M301a", "M301b", "M301c"]),
   P(S[302], None, "main", N3,
     L3 + "To rescue him if need be, Lucia seeks the Brume's revolutionaries and their leader, the Mongrel. Gibrillont sent you with his mulled wine to Hierytha, a maidservant, "
     "who knew the recipe from a young Hyuran girl decades ago: the red-eyed Elezen baron she served cast her out when she became pregnant, and she died in the Brume after giving birth.",
     ["M299g", "M300a", "M300c", "M302a", "M302d", "M302b", "M302c"]),
   P(S[303], None, "main", N3,
     L3 + "Lucia seeks the Brume's revolutionaries to help rescue him, but their leader, the Mongrel, is hidden. Gibrillont's wine led you to a maidservant cast out by an Elezen baron, "
     "who died in the Brume after giving birth. The monk Gerraldieux remembers her toiling for her daughter, a raven-haired girl who would stand on the walls staring into the mists.",
     ["M299g", "M300a", "M300c", "M302b", "M302c", "M303a", "M303b", "M303c"]),
   P(S[304], None, "main", N3,
     L3 + "Lucia seeks the Brume's revolutionaries to help rescue him. Gibrillont's errands revealed who their leader, the Mongrel, is: the raven-haired, ruby-eyed child of an Elezen nobleman "
     "and the Hyuran maidservant he cast out. She and her followers embrace their parentage, but where she hides is still unknown.",
     ["M299g", "M300a", "M302b", "M304b", "M304c", "M304a", "M304d"]),
   P(S[305], None, "main", N3,
     L3 + "Searching the Brume alone, Tataru was chased by two men until Hilda, the Mongrel, called them off. At the Forgotten Knight, Ser Charibert of the Heavens' Ward accused you of insurrection, "
     "and you drove him off with Haurchefant and Lucia. Now Aymeric is imprisoned, the Heavens' Ward command the Temple Knights, and Hilda has agreed to help rescue him.",
     ["M299g", "M305a", "M305b", "M305c", "M305d", "M305e", "M305f"]),
   P(S[306], None, "main", N3,
     L3 + "Imprisoned for confronting his father, the archbishop, he was rescued by Lucia's party while you stormed the Vault and Hilda's sympathizers drew off the defenders. "
     "The archbishop fled by airship, telling his knights that Azys Lla awaits, and a transformed Ser Zephirin hurled a spear of light at you. "
     "Lord Haurchefant shielded you and died, and Count Edmont mourns his son.",
     ["M299g", "M305e", "M306a", "M306b", "M306e", "M306c", "M306d", "M306g"]),
   P(S[307], None, "main", N3,
     "Through the Echo you saw Ser Aymeric confront his father, Archbishop Thordan, who admitted the truth: King Thordan and his knights twelve slew the wyrm Ratatoskr for her eyes, and Ishgard still fights and dies for the lie. "
     "Planning to free Ishgard from the sins of antiquity, the archbishop fled with the Heavens' Ward, who channel the souls of King Thordan and his knights. "
     "Mourning Haurchefant, Aymeric asks you to bring his father to justice, and Lucia joins the search.",
     ["M307e", "M307a", "M307d", "M306e", "M306d", "M307f", "M307i"]),
 ],
 ARC4: [
   P(S[308], None, "main", N4,
     L4 + "His airship, the Soleil, vanished into the northern Sea of Clouds, which the Vanu Vanu firmly hold. Cid, shaken by Lord Haurchefant's death, has lent you the Enterprise. "
     "He believes the Ascians tempted the archbishop as they tempted Gaius, and that Azys Lla is a source of cosmic power.",
     ["M306e", "M308a", "M308b", "M308c", "M308f", "M308d", "M308e"]),
   P(S[309], None, "main", N4,
     L4 + "Cid's Enterprise carried you into the Sea of Clouds, where the archbishop's airship vanished in Vanu Vanu territory. Haunted by the memory of Lord Haurchefant's broken shield, "
     "you reached the Blue Window, where no Vanu wait, and Alphinaud is on edge. Of the missing Scions there is no news, though Urianger is pursuing leads.",
     ["M306e", "M308f", "M308a", "M309b", "M309c", "M309a"]),
   P(S[310], None, "main", N4,
     L4 + "Searching the isles of the Sea of Clouds for his airship, you found imperial troops seizing a terrified Vanu, and they tried to seize you too, taking you for Ishgardians "
     "who would know where the archbishop is. You drove them off, and the rescued Lonu Vanu is grateful: the Vanu here are not openly hostile.",
     ["M306e", "M308a", "M310a", "M310b", "M310c", "M310d"]),
   P(S[311], None, "main", N4,
     L4 + "In the Sea of Clouds, Lonu Vanu led you to his village, where you watched the primal Bismarck, the Vanu Vanu's god, swallow an island whole as imperials engaged him. "
     "Chief Sonu says the archbishop and the Heavens' Ward seek the key to Azys Lla, a land of forbidden secrets, and it lay on the island Bismarck devoured.",
     ["M306e", "M311a", "M311b", "M311c", "M311d", "M311e", "M311f"]),
   P(S[312], None, "main", N4,
     L4 + "The key to Azys Lla lies in the belly of Bismarck, the Vanu Vanu's patron deity, and you must slay him for it before the Heavens' Ward do. "
     "The keeper of tales says Bismarck was slain by his brothers and reborn, a merciful god at odds with his rampage. Cid plans to tow an island through the clouds to lure him.",
     ["M306e", "M311e", "M312a", "M312b", "M312c", "M312d", "M312e"]),
   P(S[313], None, "main", N4,
     L4 + "Chief Sonu of the Zundu gave you an island for bait, and you slew Bismarck, and for a moment Hydaelyn's voice resounded in your mind. But the archbishop and an Ascian took the key from you, "
     "and its beam pointed the way to Azys Lla and the secrets of Allag. They departed aboard his airship, the Soleil.",
     ["M306e", "M313a", "M313b", "M313c", "M313d", "M313g", "M313f"]),
   P(S[314], None, "main", N4,
     L4 + "After you slew Bismarck, the archbishop took the key to Azys Lla from you. At the Zundu village you found imperial troops under Regula, and Varis, the newly crowned Emperor of Garlemald, "
     "who would bring the eikons to heel even by extermination; Lucia, in magitek armor, broke up his execution of the Vanu. "
     "Alphinaud judges that Varis seeks only Azys Lla.",
     ["M306e", "M313d", "M314a", "M314g", "M314b", "M314c", "M314d", "M314i"]),
   P(S[315], None, "main", N4,
     L4 + "Following the stolen key's beam, the Enterprise found the floating isle of Azys Lla, but an Allagan barrier the archbishop's airship passed unscathed nearly tore yours apart, and Cid turned back. "
     "On the way, Lucia revealed she is a Garlean defector and sister of Livia, whom you slew; she came to Ishgard as a spy, but now serves Ser Aymeric.",
     ["M306e", "M315a", "M315f", "M315h", "M315g", "M315b", "M315c", "M315d"]),
 ],
 ARC5: [
   P(S[316], None, "main", N5,
     L5 + "The barrier turns surrounding aether into a wall of lightning. Cid would mount such a ram on the Enterprise, but designing one needs an authority such as an Archon. "
     "Tataru, meanwhile, has made progress in the search for the missing Scions.",
     ["M316c", "M316b", "M316a", "M316d", "M316e", "M316f"]),
   P(S[317], None, "main", N5,
     L5 + "Tataru had Pipin search the watercourse beneath Ul'dah, where Minfilia, Thancred and Y'shtola were last seen; they were not among the dead, but he found Y'shtola's wand. "
     "Urianger divined that she used a forbidden teleportation magick and is adrift in the Lifestream beneath the Twelveswood, and only the elementals can find her, so Alphinaud will petition Gridania's Elder Seedseer.",
     ["M316c", "M316d", "M317a", "M317b", "M317c", "M317e", "M317f", "M317g"]),
   P(S[318], None, "main", N5,
     L5 + "Designing one needs an expert, and the search for the missing Scions has found Y'shtola, adrift in the Lifestream. Kan-E-Senna, the Elder Seedseer, petitioned the elementals, "
     "who needed aether akin to Y'shtola's; her sister Y'mhitra lent hers, and the Seedseers drew Y'shtola out, unconscious but alive.",
     ["M316c", "M316d", "M317e", "M318b", "M318c", "M318e", "M318f"]),
   P(S[319], None, "main", N5,
     L5 + "Y'shtola, drawn from the Lifestream alive, is awake and senses the aether more keenly. She brought the tunnel beneath Ul'dah down so Alphinaud and Minfilia could escape, "
     "and tried to teleport Thancred away; the others are still unaccounted for. She cannot build the ram, but her former master, Matoya, could.",
     ["M316c", "M316d", "M318f", "M319f", "M319b", "M319c", "M319d", "M319e"]),
   P(S[320], None, "main", N5,
     L5 + "Y'shtola's former master, Matoya, without rival in aetheric research, could build it. She refused the Sharlayan exodus and lives as a hermit on the fringes of Sharlayan, in the Dravanian hinterlands, "
     "and you, Alphinaud and Y'shtola have set out west to find her, while Tataru keeps searching for the others.",
     ["M316c", "M316d", "M319e", "M320a", "M320b", "M320d"]),
   P(S[321], None, "main", N5,
     L5 + "To find Y'shtola's former master, Matoya, who could build it, you travelled through Gnath territory to the ruins of Sharlayan, where goblins and treasure hunters are founding a new nation, Idyllshire. "
     "Alphinaud talked down their leader, Slowfix, who will give you passage across the river if you help with the settlement's troubles.",
     ["M316c", "M316d", "M319e", "M321a", "M321b", "M321c"]),
   P(S[322], None, "main", N5,
     L5 + "Seeking Matoya, who could build it, you reached Idyllshire, a goblin settlement in the ruins of Sharlayan. For passage, its leader Slowfix asked for help, "
     "and you unmade the Sharlayans' sentinel golems with the coded command Y'shtola knew, so the settlement can expand.",
     ["M316c", "M319e", "M321a", "M321c", "M322a", "M322b"]),
   P(S[323], None, "main", N5,
     L5 + "Seeking Matoya, who could build it, you are helping Idyllshire, a goblin settlement in the ruins of Sharlayan, in exchange for passage. "
     "After you cleared its golems, Slowfix asked you to rescue his friend Brayflox from the Illuminati, who want revenge for a stolen cheese recipe, and you routed them.",
     ["M316c", "M319e", "M321c", "M322b", "M323a", "M323b", "M323c"]),
   P(S[324], None, "main", N5,
     L5 + "Seeking Matoya, who could build it, you helped Idyllshire, the goblin settlement in the ruins of Sharlayan, and Slowfix has named you honored citizens, free to cross the Thaliak River. "
     "Y'shtola, upset at first that her home was occupied, believes it is in good hands, and Matoya's dwelling is a short distance away.",
     ["M316c", "M319e", "M321a", "M324a", "M324b", "M324c"]),
   P(S[325], None, "main", N5,
     L5 + "In her hidden cave, Y'shtola was reunited with her former master, Matoya, who often clashed with Louisoix. She says Azys Lla holds a research facility for mastering primals and dragons, "
     "whose secrets are not fit to see the light of day. Hearing the Ascians have a hand in the archbishop's plot, she surprised Y'shtola by agreeing to help.",
     ["M316c", "M316d", "M325a", "M325b", "M325c", "M325d", "M325e", "M325f"]),
   P(S[326], None, "main", N5,
     L5 + "Matoya has agreed to help. Long ago her aetheric converger set her against her peers: the Forum denounced it, and she sealed her research in a tome in the Great Gubal Library. "
     "You braved the library, your Crystal of Water regained the Light, and you brought her the tome.",
     ["M316c", "M325f", "M326a", "M326b", "M326c", "M326d", "M326e"]),
   P(S[327], None, "main", N5,
     L5 + "Matoya deciphered her sealed research for Cid, and Alphinaud proposed Nidhogg's Eye as the ram's power source. Through Ser Aymeric, Estinien agreed to lend it, and Cid has set to work. "
     "But Y'shtola's eyes have lost their light since the Lifestream, and Matoya warns that the magick she uses to sense the aether consumes her life force.",
     ["M316c", "M327a", "M327b", "M327f", "M327g", "M327d", "M327e"]),
   P(S[328], None, "main", N5,
     L5 + "Cid is building the ram around Nidhogg's Eye. In Ishgard you said your farewells: wounded Ser Aymeric gave you his blessing to stop his father, who consorted with the Ascians; "
     "Hilda stays to keep the peace; and Count Edmont gave you the shield Haurchefant used to save your life. You renewed your vow of vengeance on Ser Zephirin.",
     ["M316c", "M327g", "M328a", "M328b", "M328c", "M328d", "M328e", "M328f"]),
 ],
 ARC6: [
   P(S[329], None, "main", N6,
     "Aboard Cid's refit Enterprise Excelsior, the aetheric ram powered by Nidhogg's Eye broke Azys Lla's barrier, but an imperial battleship opened fire. "
     "Ysayle rode to the rescue on Hraesvelgr, transformed into Shiva and disabled the battleship at the cost of her own life. You have landed on the floating isle in pursuit of the archbishop, "
     "where Urianger warns that servants of Darkness lie in wait.",
     ["M329g", "M327b", "M329c", "M329d", "M329j", "M329i"]),
   P(S[330], None, "main", N6,
     L6 + "Ysayle gave her life to get you there. From a base camp at the landing, you found a guidance node Wedge calls Gilly. Someone recently reactivated the isle, likely the archbishop with the key, "
     "and the node points you to the Aetherochemical Research Facility on the Flagship, where Triad Control regulates the Warring Triad.",
     ["M329c", "M329d", "M330a", "M330f", "M330c", "M330d", "M330b", "M330e"]),
   P(S[331], None, "main", N6,
     L6 + "Ysayle gave her life to get you there. With no surer way to the research facility on the Flagship, where the archbishop is likely bound, you are trusting a guidance node. "
     "Cid stays to ready the Excelsior, your only way off the isle, and an Allagan matter conduit carried you onward after five millennia of disuse.",
     ["M329c", "M329d", "M330b", "M331a", "M331b", "M331c"]),
   P(S[332], None, "main", N6,
     L6 + "Following a guidance node toward the research facility on the Flagship, you crossed the Beta Quadrant, where Allagan labs bred chimeras that were siphoning the next conduit's energy. "
     "Beyond it, the Gamma Quadrant is crawling with Garlean soldiers, and Y'shtola expects them to strip the isle of its secrets.",
     ["M329c", "M330b", "M332a", "M332b", "M332c", "M332d"]),
   P(S[333], None, "main", N6,
     L6 + "The Garleans on the isle are the VIth Imperial Legion under Regula, who say the Allagans found a way to capture eikons alive. You overwhelmed Regula, but he escaped toward the research facility. "
     "Alphinaud and the others hold the legion back while you press on with the Eye, which Estinien handed you, into the Delta Quadrant, home to live dragons.",
     ["M329c", "M333a", "M333c", "M333d", "M333e", "M333f", "M333g"]),
   P(S[334], None, "main", N6,
     L6 + "With the way to the Flagship destroyed, Midgardsormr sent you to his child Tiamat, imprisoned there since before the Allagan Empire fell. "
     "She said the Ascians offered to resurrect Bahamut, then helped his murderers trap him, and urged you to vanquish them. "
     "Your Crystal of Fire regained its light, and Midgardsormr will carry you to the Flagship.",
     ["M329c", "M334a", "M334b", "M334c", "M334d", "M334e", "M334f", "M334g"]),
   P(HW, None, "main", N6,
     "On Azys Lla's Flagship you destroyed an Ascian, and the archbishop, bearing King Thordan's soul, executed Lahabrea with a blade forged from the Eye's twin. You triumphed over him and his knights, "
     "but Estinien took up both Eyes and was claimed by Nidhogg's lingering rage. Midgardsormr bore you away and met Ser Aymeric in Ishgard, beginning a journey toward peace between man and dragon, "
     "and the Holy See rejoined the Eorzean Alliance.",
     ["M335b", "M335d", "M335e", "M335f", "M335g", "M335h"]),
 ],
})

# ---- Relationship types and relationships -------------------------------------------------------------------------
TYPES = [
 ("child-of", "child of", "parent of", False),
 ("sibling-of", "sibling of", "sibling of", True),
 ("student-of", "student of", "teacher of", False),
]

# (id, source, type, target, from, until, scope, claims[, end claims]). End claims can't sit on a milestone, so
# relationships that end with the 3.0 finale end on cp-hw-3-0 without them.
RELS = [
 # Ul'dah
 ("rel-ilberd-serves-lolorito", "char-ilberd", "serves", "char-lolorito", S[292], S[294], "main", ["M292e"], ["M294a"]),
 ("rel-crystal-braves-aids-scions", "org-crystal-braves", "aids", "org-scions", S[294], None, "main", ["M294c", "M294e"]),
 # Ishgard
 ("rel-estinien-possessed-by-nidhogg", "char-estinien", "possessed-by", "char-nidhogg", HW, None, "main", ["M335f", "M335j"]),
  ("rel-aymeric-child-of-thordan", "char-aymeric", "child-of", "char-thordan", S[299], None, "main", ["M299c"]),
 ("rel-aymeric-opposes-thordan", "char-aymeric", "opposes", "char-thordan", S[299], HW, "main", ["M299b"]),
 ("rel-haurchefant-aids-aymeric", "char-haurchefant", "aids", "char-aymeric", S[299], S[306], "main", ["M299f"], ["M306d"]),
 ("rel-hilda-aids-aymeric", "char-hilda", "aids", "char-aymeric", S[305], None, "main", ["M305f", "M305i"]),
 ("rel-aymeric-prisoner-of-thordan", "char-aymeric", "prisoner-of", "char-thordan", S[305], S[306], "main", ["M305e", "M299b"], ["M306f"]),
 ("rel-heavens-ward-controls-temple-knights", "org-heavens-ward", "controls", "org-temple-knights", S[305], S[306], "main", ["M305e"], ["M306f", "M306i"]),
 ("rel-lucia-aids-scions", "char-lucia", "aids", "org-scions", S[307], None, "main", ["M307i"]),
 ("rel-scions-opposes-heavens-ward", "org-scions", "opposes", "org-heavens-ward", S[307], HW, "main", ["M307g"]),
 # The hunt
 ("rel-thordan-allied-ascians", "char-thordan", "allied-with", "org-ascians", S[313], HW, "main", ["M313d", "M308d"]),
 ("rel-garlean-empire-opposes-vanu-vanu", "org-garlean-empire", "opposes", "org-vanu-vanu", S[310], None, "main", ["M310a", "M310b"]),
 ("rel-vanu-vanu-aids-scions", "org-vanu-vanu", "aids", "org-scions", S[313], None, "main", ["M313a"]),
 ("rel-regula-member-garlean-empire", "char-regula", "member-of", "org-garlean-empire", S[314], None, "main", ["M314a", "M314g"]),
 ("rel-alphinaud-opposes-varis", "char-alphinaud", "opposes", "char-varis", S[314], None, "main", ["M314e"]),
 ("rel-lucia-sibling-of-livia", "char-lucia", "sibling-of", "char-livia", S[315], None, "main", ["M315b"]),
 ("rel-lucia-turned-against-garlean-empire", "char-lucia", "turned-against", "org-garlean-empire", S[315], None, "main", ["M315b", "M315c"]),
 ("rel-thordan-controls-azys-lla", "char-thordan", "controls", "loc-azys-lla", S[316], HW, "main", ["M316c"]),
 ("rel-ymhitra-sibling-of-yshtola", "char-ymhitra", "sibling-of", "char-yshtola", S[318], None, "main", ["M318d", "M318e"]),
 ("rel-yshtola-student-of-matoya", "char-yshtola", "student-of", "char-matoya", S[319], None, "main", ["M319e"]),
 ("rel-slowfix-leads-idyllshire", "char-slowfix", "leads", "loc-idyllshire", S[321], None, "main", ["M321a", "M321b"]),
 ("rel-matoya-aids-scions", "char-matoya", "aids", "org-scions", S[325], None, "main", ["M325f"]),
 ("rel-regula-opposes-scions", "char-regula", "opposes", "org-scions", S[333], None, "main", ["M333d", "M333e"]),
 ("rel-tiamat-child-of-midgardsormr", "char-tiamat", "child-of", "char-midgardsormr", S[334], None, "main", ["M334a"]),
 ("rel-tiamat-held-at-azys-lla", "char-tiamat", "held-at", "loc-azys-lla", S[334], None, "main", ["M334b"]),
 ("rel-midgardsormr-aids-scions", "char-midgardsormr", "aids", "org-scions", S[334], None, "main", ["M334g"]),
 ("rel-holy-see-member-eorzean-alliance", "org-holy-see", "member-of", "org-eorzean-alliance", HW, None, "main", ["M335h"]),
]

# Relationships from the accepted content that end in this era.
ADJUST = {
 "rel-braves-turned-against-scions": {"until": S[294], "end": ["M294c", "M294e"]},  # the loyal Braves pledge to the Scions
 "rel-haurchefant-aids-francel": {"until": S[306], "end": ["M306d"]},  # Haurchefant dies
 "rel-lahabrea-allied-empire": {"until": HW},  # Lahabrea is executed in the finale (no end claims on a milestone)
 # Defined by content_2_1_to_2_3:
 "rel-ilberd-member-crystal-braves": {"until": S[294], "end": ["M294a"]},  # Ilberd is defeated; his followers scatter
 "rel-lahabrea-member-ascians": {"until": HW},  # executed by the archbishop in the finale
 "rel-haurchefant-aids-scions": {"until": S[306], "end": ["M306d", "M306h"]},  # Haurchefant dies (the id is defined twice; see report)
 # Defined by content_2_4_to_2_55:
 "rel-ilberd-opposes-raubahn": {"until": S[294], "end": ["M294a"]},
 "rel-crystal-braves-turned-against-alphinaud": {"until": S[294], "end": ["M294c", "M294f"]},  # the loyal Braves stand by him
 "rel-heretics-opposes-temple-knights": {"until": S[298], "end": ["M298c", "M298g"]},  # the heretics lay down their arms
 "rel-iceheart-opposes-holy-see": {"until": S[298], "end": ["M298b", "M298c"]},  # Ysayle declares the war over
 "rel-iceheart-leads-heretics": {"until": S[329], "end": ["M329d"]},  # Ysayle dies
 "rel-shiva-summoned-iceheart": {"until": S[329], "end": ["M329d"]},
 # Defined by content_3_0_part1:
 "rel-estinien-opposes-nidhogg": {"until": S[296], "end": ["M296b"]},  # Nidhogg is slain in the Aery
 "rel-nidhogg-leads-dravanian-horde": {"until": S[296], "end": ["M296b"]},
 "rel-nidhogg-headquartered-at-aery": {"until": S[296], "end": ["M296b"]},
 "rel-bismarck-summoned-by-vanu-vanu": {"until": S[313], "end": ["M313b"]},  # Bismarck is slain
 "rel-ysayle-aids-scions": {"until": S[329], "end": ["M329d"]},  # Ysayle dies disabling the battleship
 "rel-thordan-leads-holy-see": {"until": HW},  # the archbishop falls on Azys Lla
 "rel-heavens-ward-serves-thordan": {"until": HW},
 "rel-zephirin-member-of-heavens-ward": {"until": HW},
 "rel-zephirin-serves-thordan": {"until": HW},
 "rel-estinien-aids-scions": {"until": HW},  # claimed by Nidhogg's rage in the finale
}

# ---- Arcs -----------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-f1-uldah-set-right", ARC1, S[292], S[295]),
 ("arc-f2-fall-of-nidhogg", ARC2, S[295], S[298]),
 ("arc-f3-ishgards-founding-lie", ARC3, S[299], S[307]),
 ("arc-f4-key-in-the-clouds", ARC4, S[308], S[315]),
 ("arc-f5-the-aetheric-ram", ARC5, S[316], S[328]),
 ("arc-f6-the-floating-isle", ARC6, S[329], HW),
]

CASTS = {
 ARC1: [("char-raubahn", S[292], ["M292a"]), ("char-nanamo", S[292], ["M292a"]), ("char-lolorito", S[292], ["M292c"]),
        ("char-ilberd", S[292], ["M292e"]), ("char-teledji", S[292], ["M292e"]), ("org-immortal-flames", S[292], ["M292g"]),
        ("char-alphinaud", S[293], ["M293e"]), ("org-crystal-braves", S[293], ["M293e"]), ("char-cid", S[295], ["M295b"])],
 ARC2: [("char-nidhogg", S[295], ["M295c"]), ("char-estinien", S[295], ["M295e"]), ("char-aymeric", S[295], ["M295d"]),
        ("char-hraesvelgr", S[295], ["M295g"]), ("char-cid", S[295], ["M295b"]), ("char-ysayle", S[297], ["M297a"]),
        ("char-haurchefant", S[298], ["M298i"]), ("char-thordan", S[298], ["M298e"]), ("char-zephirin", S[298], ["M298d"]),
        ("char-lahabrea", S[298], ["M298f"])],
 ARC3: [("char-aymeric", S[299], ["M299b"]), ("char-lucia", S[299], ["M299e"]), ("char-haurchefant", S[299], ["M299f"]),
        ("char-edmont", S[299], ["M299a"]), ("char-thordan", S[299], ["M299c"]), ("char-hilda", S[300], ["M300c"]),
        ("char-tataru", S[300], ["M300c"]), ("org-heavens-ward", S[305], ["M305e"]), ("char-zephirin", S[306], ["M306c"]),
        ("char-alphinaud", S[306], ["M306h"])],
 ARC4: [("char-thordan", S[308], ["M308d"]), ("char-cid", S[308], ["M308f"]), ("loc-azys-lla", S[308], ["M308e"]),
        ("org-vanu-vanu", S[308], ["M308b"]), ("char-alphinaud", S[309], ["M309c"]), ("char-bismarck", S[311], ["M311c"]),
        ("org-ascians", S[313], ["M313d"]), ("char-varis", S[314], ["M314b"]), ("char-regula", S[314], ["M314g"]),
        ("char-lucia", S[314], ["M314d"])],
 ARC5: [("char-cid", S[316], ["M316d"]), ("char-tataru", S[316], ["M316f"]), ("char-yshtola", S[317], ["M317c"]),
        ("char-urianger", S[317], ["M317c"]), ("char-kan-e-senna", S[318], ["M318b"]), ("char-ymhitra", S[318], ["M318e"]),
        ("char-matoya", S[319], ["M319e"]), ("char-slowfix", S[321], ["M321c"]), ("char-estinien", S[327], ["M327f"]),
        ("char-aymeric", S[328], ["M328b"])],
 ARC6: [("char-ysayle", S[329], ["M329d"]), ("char-hraesvelgr", S[329], ["M329d"]), ("char-cid", S[329], ["M329g"]),
        ("loc-azys-lla", S[329], ["M329c"]), ("char-regula", S[333], ["M333d"]), ("char-estinien", S[333], ["M333f"]),
        ("char-midgardsormr", S[334], ["M334a"]), ("char-tiamat", S[334], ["M334b"]), ("char-thordan", HW, ["M335d"]),
        ("char-nidhogg", HW, ["M335f"])],
}

ARC_NOTES = {
 "arc-f1-uldah-set-right": "MSQ #292 *A General Summons* to #295 *Ready to Fly*. The Ul'dah threads closed out: Lolorito's confession, the sultana woken, "
   "Raubahn reinstated and the Crystal Braves refusing to disband (M292c, M293a, M294c). It ends on #295, where Alphinaud keeps the Braves on the search and sends you back to Ishgard (M295a), "
   "sharing that step with the next arc so the Ul'dah thread has four steps.",
 "arc-f2-fall-of-nidhogg": "MSQ #295 *Ready to Fly* to #298 *Unrest in Ishgard*: the manacutter, Nidhogg's death in the Aery, Hraesvelgr's account of the war's origin, "
   "and Ysayle ending the heretic uprising (M296b, M297d, M298b). It ends where the Holy See's own plot surfaces (M298e), which the next arc takes up.",
 "arc-f3-ishgards-founding-lie": "MSQ #299 *He Who Would Not Be Denied* to #307 *The Sins of Antiquity*: Aymeric's confrontation, the search for the Mongrel, the Vault, "
   "Haurchefant's death and the archbishop's admission (M299b, M305f, M306d, M307a). It ends when Aymeric asks the Scions to hunt his father.",
 "arc-f4-key-in-the-clouds": "MSQ #308 *In Search of the Soleil* to #315 *One Good Turn*: the Sea of Clouds, Bismarck and the key, Varis at the Zundu village, "
   "and the first sight of Azys Lla's barrier, with Lucia's reveal (M313d, M314b, M315b, M315f).",
 "arc-f5-the-aetheric-ram": "MSQ #316 *An Engineering Enterprise* to #328 *Hour of Departure*: the ram plan, Y'shtola's rescue from the Lifestream, the road through Idyllshire to Matoya, "
   "the Eye as power source, and the farewells (M316d, M318f, M325f, M327f, M328e). 13 steps.",
 "arc-f6-the-floating-isle": "MSQ #329 *The First Flight of the Excelsior* to the `cp-hw-3-0` milestone (after #335): Ysayle's sacrifice, Azys Lla's quadrants, Tiamat, "
   "the archbishop's fall, Estinien's possession and the Holy See's return to the Alliance (M329d, M334c, M335e, M335f, M335h). The era's last arc ends on its milestone.",
}

DECISIONS = [
 "The Ascian beside the archbishop at #313 and #335 is never named (her name is banned in `RealDataTests`); she is \"an Ascian\" / \"a second Ascian\".",
 "Lucia's reveal at #315 gives no family name (banned surname); she is \"a Garlean defector, and sister to Livia\". Livia gets one new presentation at #315 for the same fact.",
 "Hilda is one entry (`char-hilda`) named \"The Mongrel\" from #300 to #304 and \"Hilda\" from #305, keeping \"The Mongrel\" as an alias; a self-chosen moniker is not a second identity, so there is no `revealed-as` edge.",
 "Regula appears only from #314, where the journal first gives his name; at #310 the troops' commander is left unnamed (the page gives only \"Lord van Hydrus\", a family name).",
 "Archbishop Thordan VII is `char-thordan`, named \"Thordan VII\" as in 3.0 part 1. King Thordan is named in text only, not an entry.",
 "Relationships that other eras already define (Lucia serves Aymeric, Varis leads the Empire, Raubahn leads the Immortal Flames, Haurchefant child of Edmont, Zephirin and the Heavens' Ward serving Thordan, Kan-E-Senna aids the Scions) are not repeated; deaths and endings in this era close them through ADJUST.",
 "Three new relationship types: `child-of` (child of / parent of), `sibling-of` (symmetric) and `student-of` (student of / teacher of).",
 "Relationships that end with the 3.0 finale end on `cp-hw-3-0` without end claims, since end claims cannot sit on a milestone.",
]

# The quest "Heavensward" (#335) is the 3.0 milestone's own source: its title is shown wherever it is cited. (The lint
# now exempts citation titles, so this is only needed if displayed text should ever use the word from the milestone.)
ALLOW = {"Heavensward": HW}
