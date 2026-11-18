"""Atlas content for A Realm Reborn 2.0, MSQ #102–#154 (NDL-012): five arcs before the Black Wolf's Challenge.

Imported by build_pilot_content.py, which owns the timeline, sources, review status and every generated file. This
module holds only data: the early timeline steps, the claims (own words, source quest, verbatim locator), the
presentations and relationships, and the arcs. Researched 2026-11-17 from raw Console Games Wiki wikitext in six
parallel lanes (Claude Haiku 5.5); the lead checked every locator against the saved pages. See
docs/atlas/ndl-012-discovery.md for the method, the quest inventory, the arc map and the decisions.

Every presentation and relationship here is new, so the generator emits it "pending" until the user accepts it.
Each step means "after this quest". Spoiler rules this content follows (and the host tests enforce):
  - no text names a quest past its step, or an entity that is not yet visible;
  - first names only; Nero stays out of displayed text (NDL-009 decision 9), as do surnames;
  - "banquet" is reserved for the 2.55 story (RealDataTests), so the Company of Heroes holds a "feast";
  - Cid lived as "Marques" until #110. Marques is his own entry (no portrait), because Cid's approved portrait shows
    his later look; from #110 Marques is "revealed as" Cid, and Cid carries "Marques" as an alias.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

# ---- Timeline -----------------------------------------------------------------------------------------------------
# (checkpoint id, MSQ index, quest title, game quest id). #102 is the new first step: the baseline before the first
# arc. After #149 the main scenario splits into two paths that rejoin at #153 (there is no #152): Drowning Out the
# Voices (#150), and Acting the Part (#150) → Dressed for Conquest (#151). Both are needed for #153 (its prev-quest
# lists both). Ordering rule: MSQ index, then authored order; Acting the Part is not contiguous with the step before it.
EARLY_SLICE = [
    ("cp-msq-102", 102, "It Was a Very Good Year", 66386),
    ("cp-msq-103", 103, "In the Company of Heroes", 66391),
    ("cp-msq-104", 104, "As You Wish", 66392),
    ("cp-msq-105", 105, "Lord of Crags", 66393),
    ("cp-msq-106", 106, "All Good Things", 66053),
    ("cp-msq-107", 107, "You Can't Take It with You", 69403),
    ("cp-msq-108", 108, "Bringing out the Dead", 66412),
    ("cp-msq-109", 109, "Bury Me Not on the Lone Prairie", 66414),
    ("cp-msq-110", 110, "Eyes on Me", 66054),
    ("cp-msq-111", 111, "He Who Waited Behind", 66419),
    ("cp-msq-112", 112, "Cold Reception", 66420),
    ("cp-msq-113", 113, "The Unending War", 66422),
    ("cp-msq-114", 114, "Men of Honor", 66423),
    ("cp-msq-115", 115, "Three for Three", 66425),
    ("cp-msq-116", 116, "The Rose and the Unicorn", 66426),
    ("cp-msq-117", 117, "The Talk of Coerthas", 66433),
    ("cp-msq-118", 118, "Road to Redemption", 66446),
    ("cp-msq-119", 119, "Following the Evidence", 66447),
    ("cp-msq-120", 120, "In the Eyes of Gods and Men", 66448),
    ("cp-msq-121", 121, "The Final Flight of the Enterprise", 69404),
    ("cp-msq-122", 122, "Ye of Little Faith", 66460),
    ("cp-msq-123", 123, "Factual Folklore", 66463),
    ("cp-msq-124", 124, "The Best Inventions", 69405),
    ("cp-msq-125", 125, "Influencing Inquisitors", 66474),
    ("cp-msq-126", 126, "By the Lights of Ishgard", 66475),
    ("cp-msq-127", 127, "Blood for Blood", 66476),
    ("cp-msq-128", 128, "The Heretic among Us", 66477),
    ("cp-msq-129", 129, "In Pursuit of the Past", 66488),
    ("cp-msq-130", 130, "Into the Eye of the Storm", 66489),
    ("cp-msq-131", 131, "Sealed with Science", 66491),
    ("cp-msq-132", 132, "With the Utmost Care", 66492),
    ("cp-msq-133", 133, "A Promising Prospect", 66495),
    ("cp-msq-134", 134, "It's Probably Not Pirates", 66496),
    ("cp-msq-135", 135, "Representing the Representative", 66497),
    ("cp-msq-136", 136, "The Reluctant Researcher", 66498),
    ("cp-msq-137", 137, "Sweet Somethings", 66499),
    ("cp-msq-138", 138, "History Repeating", 66503),
    ("cp-msq-139", 139, "The Curious Case of Giggity", 69406),
    ("cp-msq-140", 140, "Better Late than Never", 66511),
    ("cp-msq-141", 141, "Lady of the Vortex", 66055),
    ("cp-msq-142", 142, "Reclamation", 66056),
    ("cp-msq-143", 143, "Casing the Castrum", 66514),
    ("cp-msq-144", 144, "Eyes on the Empire", 66516),
    ("cp-msq-145", 145, "Footprints in the Snow", 66517),
    ("cp-msq-146", 146, "Monumental Hopes", 66518),
    ("cp-msq-147", 147, "Notorious Biggs", 66519),
    ("cp-msq-148", 148, "Come-Into-My-Castrum", 66520),
    ("cp-msq-149", 149, "Getting Even with Garlemald", 66522),
    ("cp-msq-150", 150, "Drowning Out the Voices", 66537),
    ("cp-msq-150b", 150, "Acting the Part", 66538),
    ("cp-msq-151", 151, "Dressed for Conquest", 69407),
    ("cp-msq-153", 153, "Fool Me Twice", 66540),
]
NOT_CONTIGUOUS = {"cp-msq-150b"}  # follows the other #150 path, not its own prerequisite (#149)
SHORT = {"cp-msq-150b": "#150b"}
PAGES = {"Fool Me Twice": "Fool Me Twice (Quest)"}  # wiki page titles that differ from the quest title
EXTRA_SOURCES = ["That Weight"]  # MSQ #100, before the first step: it counts from the baseline

(Q102, Q103, Q104, Q105, Q106, Q107, Q108, Q109, Q110, Q111, Q112, Q113, Q114, Q115, Q116, Q117, Q118, Q119, Q120,
 Q121, Q122, Q123, Q124, Q125, Q126, Q127, Q128, Q129, Q130, Q131, Q132, Q133, Q134, Q135, Q136, Q137, Q138, Q139,
 Q140, Q141, Q142, Q143, Q144, Q145, Q146, Q147, Q148, Q149, Q150, Q150B, Q151, Q153) = (c for c, _, _, _ in EARLY_SLICE)
Q154, Q155, Q157, Q160, A = "cp-msq-154", "cp-msq-155", "cp-msq-157", "cp-msq-160", "cp-arr-2-0"

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
# Locators quote the saved wikitext exactly, markup included; " … " joins two exact fragments of one page.
CLAIMS = {
 "E100a": ("The Empire conquered the lands of the deserter Drest, as it tried to conquer Eorzea.", "That Weight", "They conquered my lands just like they tried to conquer yours!"),
 # #103 In the Company of Heroes
 "E103a": ("The feast was a pretext for the Company of Heroes to judge whether you are worthy to face Titan.", "In the Company of Heroes", "the banquet preparations were but an excuse for his comrades to evaluate your worthiness to face"),
 "E103b": ("Five members of the Company of Heroes judge you a worthy challenger.", "In the Company of Heroes", "We five of the Company of Heroes hereby judge you a worthy challenger."),
 "E103c": ("The Company weighs anyone who would follow in its footsteps by deeds, not reputation.", "In the Company of Heroes", "That any who would follow in our footsteps must be weighed and measured─not by their reputation, but by their deeds."),
 "E103d": ("Y'shtola, with you at the feast, says the battle with Titan has yet to begin.", "In the Company of Heroes", "the battle with Titan has yet to begin."),
 "E103e": ("Wheiskaet can now tell you how to reach Titan's lair.", "In the Company of Heroes", "may now ask him how to reach Titan's lair"),
 "E103f": ("The five were chosen by their comrades before the Company of Heroes disbanded.", "In the Company of Heroes", "We five were chosen by our brothers and sisters, and before the Company of Heroes disbanded"),
 # #104 As You Wish
 "E104a": ("Wheiskaet sends you to Bronze Lake to meet Riol, another former member of the Company.", "As You Wish", "There you will meet with Riol, another man who once served with the Company."),
 "E104b": ("Riol guards the Company's knowledge and stays hidden until he hears the right signal.", "As You Wish", "To ensure that this knowledge does not fall into the wrong hands, he will remain in hiding until you have given the correct signal."),
 # #105 Lord of Crags
 "E105a": ("The Company of Heroes reached Titan through a beastman aetheryte, not the kobold mines.", "Lord of Crags", "Riol reveals that the [[Company of Heroes]] reached [[Titan]] not by fighting their way through the mines of [[O'Ghomoro]], but by using a beastman [[aetheryte]]."),
 "E105b": ("Y'shtola stays behind at the aetheryte, so you go on alone.", "Lord of Crags", "It seems you will have to proceed without me, [Forename]."),
 "E105c": ("Titan, whom the kobolds call Great Father and the Lord of Crags, falls.", "Lord of Crags", "The Lord of Crags, Great Father Titan has fallen!"),
 "E105d": ("Rhitahtyn, an imperial officer at the Navel, refuses to endorse his comrade's plan.", "Lord of Crags", "I cannot endorse this course of action."),
 "E105e": ("Lahabrea urges you on, saying your work is far from done.", "Lord of Crags", "Carry on, crystal bearer. Far though you have come, your work is far from done."),
 "E105f": ("Y'shtola stays behind to investigate something before she leaves.", "Lord of Crags", "There is something I must investigate before I depart."),
 # #106 All Good Things
 "E106a": ("Minfilia calls you back to the Waking Sands.", "All Good Things", "We'll be awaiting your return at the Waking Sands. There is much to discuss."),
 "E106b": ("Imperial forces raided the Waking Sands, slaughtered many Scions and left with prisoners.", "All Good Things", "the Waking Sands was raided by imperial forces, who slaughtered countless Scions before departing─with prisoners."),
 "E106c": ("The raiders came for the one who slew Ifrit and Titan.", "All Good Things", "We have come for the one who slayed Ifrit and Titan!"),
 "E106d": ("Minfilia offered to surrender if the innocents were spared.", "All Good Things", "I surrender myself, on the condition you spare the innocents."),
 "E106e": ("The dying sylph Noraxia sends you to the church in eastern Thanalan.", "All Good Things", "At church in eastern Thanalan...walking one must claim sanctuary..."),
 "E106f": ("Father Iliud has known Minfilia since childhood, swore to support her, and offers the same to her fellow Scions.", "All Good Things", "I have known her since she was but a child... … I swore then to do everything in my power to support her, and I will gladly offer the selfsame service to her brother and sister Scions."),
 "E106g": ("Marques, a survivor of Carteneau whom the church took in, is set to look after you.", "All Good Things", "Marques is a survivor of the battle of Carteneau. … Had we not taken him into our care, he would surely have perished in the desert. … Marques, I want you to look after [Forename]."),
 # #107 You Can't Take It with You
 "E107a": ("Marques mended a broken horologe as though he had done it countless times.", "You Can't Take It with You", "I knew exactly what to do, as though I had performed the same motions countless times before..."),
 "E107b": ("Sister Eluned wonders whether the horologe's dead owner was a Garlean spy.", "You Can't Take It with You", "You don't suppose that the owner might have been a Garlean spy?"),
 # #108 Bringing out the Dead
 "E108a": ("The fallen Scions are carried from the Waking Sands for their rites.", "Bringing out the Dead", "the bodies of your comrades are presently being removed from the Waking Sands and prepared for transport here."),
 "E108b": ("The church will do all it can to see the dead to Thal's realm.", "Bringing out the Dead", "do everything we can to shepherd them to Thal's realm."),
 # #109 Bury Me Not on the Lone Prairie
 "E109a": ("Noraxia's body is returned to her home in the Black Shroud.", "Bury Me Not on the Lone Prairie", "Sister Eluned believes that it would be best if the [[Noraxia's Corpse|sylph's body]] was returned to her home in [[the Black Shroud]]"),
 "E109b": ("You were with Noraxia at the end, and her people ask that you tell them she was brave.", "Bury Me Not on the Lone Prairie", "Walking one was with Noraxia at the end... Tell this one that Noraxia was brave."),
 "E109c": ("The sylph Komuxio demands vengeance on the imperials.", "Bury Me Not on the Lone Prairie", "This one demands vengeance! Imperial ones must pay! Imperial ones must suffer!"),
 "E109d": ("The remaining Scions are buried in the church's lichyard.", "Bury Me Not on the Lone Prairie", "in your absence, we interred the remaining Scions in the lichyard."),
 # #110 Eyes on Me
 "E110a": ("A stranger attacks you in the lichyard, and you kill him in self-defense.", "Eyes on Me", "you come under attack from an unknown assailant … After slaying the man in self-defense, you note that his sword is unlike any you have seen before"),
 "E110b": ("Iliud knows the sword for Garlean steel: an imperial soldier was watching Marques.", "Eyes on Me", "Recognizing the sword you found to be Garlean steel, Father Iliud concludes that the man observing Marques was an imperial soldier."),
 "E110c": ("Alphinaud declares Marques to be Cid, missing since the Calamity five years ago.", "Eyes on Me", "declares Marques to be none other than Master Cid … who has been missing since the Calamity five years ago."),
 "E110d": ("Cid has not recovered his memories, but believes Alphinaud and joins him.", "Eyes on Me", "While he has yet to recover his lost memories, Cid senses that the boy speaks the truth, and decides to join him."),
 "E110e": ("The Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her.", "Eyes on Me", "that the Ixal have summoned Garuda, and that Cid's lost airship, the ''Enterprise'', will be required if the surviving Scions are to reach the primal."),
 "E110f": ("The Enterprise was last seen over Gridania.", "Eyes on Me", "Together with Cid and Alphinaud, make for Gridania, where the ''Enterprise'' was last seen."),
 # #111 He Who Waited Behind
 "E111a": ("A tale says the Enterprise flew northwest from Gridania toward Coerthas.", "He Who Waited Behind", "It states that the ''Enterprise'' flew northwest from Gridania towards Coerthas."),
 "E111b": ("Vortefaurt saw the airship pass.", "He Who Waited Behind", "Vortefaurt confirms that he bore witness to the vessel's passing."),
 # #112 Cold Reception
 "E112a": ("The Enterprise vanished over the mountains of Coerthas to the northwest.", "Cold Reception", "According to Vortefaurt, the ''Enterprise'' disappeared over the mountains of [[Coerthas]] to the northwest."),
 "E112b": ("Ser Ludovoix will not let an outsider read the Observatorium's records.", "Cold Reception", "Hah, how absurd! As if we would permit an outsider to peruse the records of the Observatorium."),
 "E112c": ("Ishgard lets foreigners travel but offers strangers no help.", "Cold Reception", "The Holy See of Ishgard may allow foreigners to travel freely within these lands, but we do not intend to offer succor to strangers."),
 # #113 The Unending War
 "E113a": ("The knight's attackers were heretics sworn to the dragons.", "The Unending War", "the [[Ishgard]]ian names the attackers as heretics─those who have pledged their allegiance to the [[dragon]]s."),
 "E113b": ("The records bear on a war that has raged for generations.", "The Unending War", "Were our records to fall into the wrong hands, it could change the course of a war which has raged for generations!"),
 "E113c": ("Inquisitor Guillaime subtly warns you away from Ishgard's affairs.", "The Unending War", "subtly cautioning you against becoming involved in Ishgardian affairs"),
 # #114 Men of Honor
 "E114a": ("House Durendaire will still not open the Observatorium's records to you.", "Men of Honor", "Even so, they will ''not'' grant you access to the Observatorium's records."),
 "E114b": ("You must petition Lord Portelaine for introductions to the other High Houses.", "Men of Honor", "Approach Lord [[Portelaine]] and petition him for formal introductions to the other [[High Houses]]"),
 "E114c": ("Portelaine wants a third deed before he endorses you to three High Houses.", "Men of Honor", "But while you have performed ''two'' acts, you would have me endorse you to ''three'' High Houses."),
 # #115 Three for Three
 "E115a": ("A draconian rosary turns up in a chest belonging to Lord Francel of House Haillenarte.", "Three for Three", "a draconian rosary in a chest belonging to Lord [[Francel]] of [[House Haillenarte]]."),
 "E115b": ("House Haillenarte is whispered to be full of heretics.", "Three for Three", "House Haillenarte is whispered to be infested with heretics..."),
 "E115c": ("Portelaine informs the inquisitors and warns you away from House Haillenarte.", "Three for Three", "I shall inform the inquisitors immediately. Under these circumstances, I must strongly advise against associating with House Haillenarte."),
 # #116 The Rose and the Unicorn
 "E116a": ("Francel's former servant swears he is no heretic.", "The Rose and the Unicorn", "Lord Francel is no heretic. He is a goodly, righteous man, wholly dedicated to the cause."),
 "E116b": ("Francel fears the rosary will still be taken as proof against him.", "The Rose and the Unicorn", "Although the draconian rosary was not found in my possession, it will still be considered by many to be proof of my"),
 "E116c": ("Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead.", "The Rose and the Unicorn", "Lord Haurchefant of House Fortemps commands the garrison at Camp Dragonhead."),
 "E116d": ("Francel gives you a letter of introduction to House Fortemps.", "The Rose and the Unicorn", "he furnishes you with a [[Letter to Haurchefant|letter of introduction]] to [[House Fortemps]]"),
 "E116e": ("Haurchefant promises to make inquiries for you.", "The Rose and the Unicorn", "Nevertheless, I will make inquiries on your behalf and share with you my findings in the future."),
 # #117 The Talk of Coerthas
 "E117a": ("Since Inquisitor Guillaime arrived, countless heretics have been found, even among Ishgard's elite.", "The Talk of Coerthas", "Why, in the short time since Inquisitor Guillaime arrived in Coerthas, countless heretics have been discovered, even amongst the elite of Ishgardian society!"),
 "E117b": ("The heresy accusations have thrown House Haillenarte into chaos.", "The Talk of Coerthas", "But these accusations of heresy have thrown House Haillenarte into chaos."),
 "E117c": ("All of Coerthas is consumed by talk of heretics in the High Houses.", "The Talk of Coerthas", "It seems the whole of Coerthas is consumed by this talk of heretics in the High Houses."),
 # #118 Road to Redemption
 "E118a": ("Francel went to the Steel Vigil hoping to show his devotion by slaying scalekin.", "Road to Redemption", "I had hoped we might demonstrate our devotion by slaying a number of the scalekin."),
 "E118b": ("Francel's trial approaches.", "Road to Redemption", "The day of my trial approaches."),
 "E118c": ("A witness to the Enterprise's flight has been found, but is reluctant to meet you.", "Road to Redemption", "the witness became understandably reticent to make your acquaintance"),
 "E118d": ("Francel's name, and so yours, must be cleared first.", "Road to Redemption", "we must first clear Lord Francel's name─and, by association, yours."),
 # #119 Following the Evidence
 "E119a": ("Haurchefant believes the rosary was planted.", "Following the Evidence", "If the rosary was not his, then someone else with access ''must'' have planted it."),
 "E119b": ("Two parcels bound for Skyfire Locks each held a draconian rosary.", "Following the Evidence", "the two parcels bound for [[Skyfire Locks]] both contained a draconian rosary!"),
 "E119c": ("Haurchefant calls it a crass attempt to sully House Haillenarte.", "Following the Evidence", "Even the inquisitors must acknowledge that this is no more than a crass attempt to sully House Haillenarte's reputation."),
 "E119d": ("Francel's trial is at hand.", "Following the Evidence", "Lord Francel's trial is upon us, and we must act now if we are to clear his name!"),
 # #120 In the Eyes of Gods and Men
 "E120a": ("Inquisitor Guillaime presides over Francel's trial at Witchdrop.", "In the Eyes of Gods and Men", "Inquisitor Guillaime presides over Lord Francel's trial at Witchdrop even as we speak."),
 "E120b": ("Guillaime orders Francel to prove his innocence by leaping from the cliff.", "In the Eyes of Gods and Men", "Leap from the cliff and entrust your fate to the Fury."),
 "E120c": ("A heretic among the Temple Knights summoned the wyvern.", "In the Eyes of Gods and Men", "it was ''he'' who summoned the wyvern!"),
 "E120d": ("Guillaime withdraws the charges against Francel, pending investigation.", "In the Eyes of Gods and Men", "I shall withdraw my charges against Lord Francel, pending further investigation."),
 "E120e": ("Haurchefant says someone has used the trials to sow discord between the houses.", "In the Eyes of Gods and Men", "They have used you and your fellows to sow discord, Inquisitor─to set brother against brother"),
 # #121 The Final Flight of the Enterprise
 "E121a": ("The Enterprise landed near the Stone Vigil days before the Calamity.", "The Final Flight of the Enterprise", "he saw the ''Enterprise'' land near [[the Stone Vigil]] several days before [[the Calamity]]"),
 "E121b": ("The Stone Vigil is now held by Dravanian forces.", "The Final Flight of the Enterprise", "the Stone Vigil is currently held by [[Dravanian Horde|Dravanian forces]]"),
 "E121c": ("Haurchefant writes to Lord Drillemont of Whitebrim Front to ask that you be let in.", "The Final Flight of the Enterprise", "I will write a letter to Lord Drillemont of Whitebrim Front and request that he grant you permission to enter."),
 "E121d": ("Those who tried to destroy House Haillenarte are still unmasked.", "The Final Flight of the Enterprise", "the cravens who attempted to destroy House Haillenarte have yet to be unmasked"),
 # #122 Ye of Little Faith
 "E122a": ("Alphinaud tells Drillemont you came to slay Garuda and seek the Enterprise.", "Ye of Little Faith", "We are come to Coerthas to slay Garuda, Lady of the Vortex. To that end, we seek the ''Enterprise''"),
 "E122b": ("Drillemont is astonished that Cid is alive.", "Ye of Little Faith", "you're ''alive''!? But that's impossible!"),
 "E122c": ("Guillaime calls Cid presumed dead and the Scions a defunct band the Empire exterminated.", "Ye of Little Faith", "missing and presumed dead since before the Calamity, and two Scions of the Seventh Dawn─a defunct band of misfits recently exterminated by the Empire."),
 "E122d": ("Guillaime insists you must not be let through to the Stone Vigil.", "Ye of Little Faith", "I know not why these three seek the Stone Vigil, but I know that we cannot permit them to pass."),
 "E122e": ("Drillemont bars you until the outpost is retaken and you declare your true intentions.", "Ye of Little Faith", "You three will not enter the outpost until we have reclaimed it─and until you declare your ''true'' intentions as well."),
 "E122f": ("Alphinaud means to earn Drillemont's trust.", "Ye of Little Faith", "we must do whatever it takes to earn Lord Drillemont's trust. Understood?"),
 # #123 Factual Folklore
 "E123a": ("The cook says winning over the barracks will catch Drillemont's notice.", "Factual Folklore", "Win over the barracks, and he's sure to take notice."),
 # #124 The Best Inventions
 "E124a": ("Cid builds the infirmary a better alembic from its broken equipment.", "The Best Inventions", "So I used some of their broken equipment to craft a more advanced alembic─both as a gesture of goodwill"),
 "E124b": ("Working with his hands kindles familiar feelings in Cid.", "The Best Inventions", "since working with my hands kindles familiar feelings."),
 "E124c": ("Guillaime warns that your efforts serve an unknown end.", "The Best Inventions", "Their earnest efforts are but a means to an as-yet-unknown end."),
 "E124d": ("The inquisitor seems to hate you and your companions.", "The Best Inventions", "The inquisitor appears to have developed a hatred for you and your associates"),
 # #125 Influencing Inquisitors
 "E125a": ("The knight Joellaut says Guillaime carried him to the gates when he fell.", "Influencing Inquisitors", "Inquisitor Guillaime rescued ''me'', carrying my unconscious body to the gates."),
 "E125b": ("Alphinaud suspects Guillaime has other reasons for hindering you.", "Influencing Inquisitors", "I am beginning to suspect he has other reasons for hindering us now."),
 "E125c": ("Guillaime is credited with unmasking unprecedented numbers of heretics.", "Influencing Inquisitors", "Under Inquisitor Guillaime's watchful gaze, unprecedented numbers of heretics have been unmasked and brought to justice."),
 # #126 By the Lights of Ishgard
 "E126a": ("A frozen corpse in the chasm closely resembles Guillaime.", "By the Lights of Ishgard", "a frozen corpse in the chasm which bears a striking resemblance to Inquisitor Guillaime"),
 "E126b": ("The real inquisitor was murdered on the day he arrived in Coerthas.", "By the Lights of Ishgard", "Newly come to Coerthas and murdered on the day of his arrival..."),
 "E126c": ("The corpse is the real Inquisitor Guillaime.", "By the Lights of Ishgard", "I believe you have just made the acquaintance of the ''real'' Inquisitor Guillaime."),
 "E126d": ("The impostor's identity and reasons for opposing you are unknown.", "By the Lights of Ishgard", "we have yet to discern his true identity, or why he has decided to oppose us."),
 # #127 Blood for Blood
 "E127a": ("The impostor coerced Prunilla with threats against her loved ones.", "Blood for Blood", "if I defied him...everyone I loved would suffer unimaginable horrors before they died."),
 "E127b": ("The impostor condemned innocent people found carrying draconian rosaries.", "Blood for Blood", "countless men and women of good moral standing, seized whilst in possession of draconian rosaries."),
 "E127c": ("Prunilla planted rosaries from his chest in shipments bound for Skyfire Locks.", "Blood for Blood", "I took several from his chest and planted them in shipments bound for Skyfire Locks."),
 "E127d": ("Drillemont is convinced the inquisitor is a heretic.", "Blood for Blood", "Fury take me, the inquisitor is a ''heretic''!?"),
 "E127e": ("Drillemont will let you into the outpost, but first asks your help.", "Blood for Blood", "I will permit you to enter the outpost─but first, I must needs beg your assistance."),
 # #128 The Heretic among Us
 "E128a": ("Drillemont names the impostor a heretic and the murderer of Inquisitor Guillaime.", "The Heretic among Us", "I name thee ''heretic'', murderer of Inquisitor Guillaime and countless innocents!"),
 "E128b": ("The impostor calls all Ishgard complicit in the archbishop's lies.", "The Heretic among Us", "''All'' are complicit in these crimes, for ''all'' live their lives by the archbishop's lies."),
 "E128c": ("He summons his Dravanian allies and takes the form of a dragon.", "The Heretic among Us", "he summons his [[Dravanian Horde|Dravanian allies]] and endeavors to defend himself, going so far as to use his magicks to assume the form of a [[dragon]]."),
 "E128d": ("He warns that the dragons in the Stone Vigil will tear you apart.", "The Heretic among Us", "The dragons within the Stone Vigil will rend you asunder."),
 "E128e": ("Drillemont says it is time you were reunited with your airship.", "The Heretic among Us", "It is past time that you were reunited with your airship."),
 "E128f": ("You defeat the false inquisitor.", "The Heretic among Us", "Alphinaud refuses to revel in your victory over the false inquisitor"),
 # #129 In Pursuit of the Past
 "E129a": ("Drillemont cannot say whether the Enterprise survived the outpost's fall.", "In Pursuit of the Past", "Whether it was damaged or destroyed during the battle, I cannot say"),
 "E129b": ("Lahabrea taunts that Garuda is stronger than any primal you have faced.", "In Pursuit of the Past", "And you are aware that her strength greatly exceeds that of your previous primal conquests?"),
 "E129c": ("Alphinaud and Cid slip aboard the Enterprise while you hold off the dragon.", "In Pursuit of the Past", "Cid─you and I will sneak aboard the ''Enterprise'' and prepare it for launch."),
 "E129d": ("Cid knows the airship, though he cannot say more.", "In Pursuit of the Past", "I...I ''know'' this airship."),
 "E129e": ("The Enterprise is in no condition to weather Garuda's storm.", "In Pursuit of the Past", "it is plain the ''Enterprise'' is in no condition to weather the storm"),
 # #130 Into the Eye of the Storm
 "E130a": ("The battered Enterprise cannot survive the winds around the Howling Eye, Garuda's sanctuary.", "Into the Eye of the Storm", "In its current condition, the ''Enterprise'' cannot endure the tumultuous winds which encircle [[the Howling Eye]], [[Garuda]]'s sanctuary."),
 "E130b": ("Cid would use a corrupted crystal to change the aspect of Garuda's wind barrier.", "Into the Eye of the Storm", "we could theoretically use a corrupted crystal to convert the wind-aspected aether comprising Garuda's barrier into aether of another aspect"),
 "E130c": ("Cid knows of a scholar, Lamberteint, in Camp Drybone.", "Into the Eye of the Storm", "A scholar by the name of Lamberteint, who resides in Camp Drybone."),
 "E130d": ("Cid met Lamberteint while he lived as Marques at the church.", "Into the Eye of the Storm", "Strange as it may sound, I met him during my time at the church. Well, ''Marques'' met him, I suppose."),
 "E130e": ("The Seedseers house the Enterprise for its repairs.", "Into the Eye of the Storm", "The Seedseers have granted our request to house the ''Enterprise''."),
 # #131 Sealed with Science
 "E131a": ("Lamberteint lends you a warded pot and sends you to his pupil Hahasako at Highbridge.", "Sealed with Science", "take the pot to Hahasako, a student of mine monitoring the flow of aether at Highbridge."),
 # #132 With the Utmost Care
 "E132a": ("The crystal from the Burning Wall is wind-aspected and would only strengthen the barrier.", "With the Utmost Care", "A corrupted crystal overflowing with wind-aspected aether. … this crystal would only serve to ''strengthen'' the barrier."),
 # #133 A Promising Prospect
 "E133a": ("Another pupil, Ceana, has found a promising site at Pharos Sirius on the Isles of Umbra.", "A Promising Prospect", "It was ''western'' La Noscea─Pharos Sirius, on the Isles of Umbra, to be precise."),
 # #134 It's Probably Not Pirates
 "E134a": ("Access to the isles is prohibited.", "It's Probably Not Pirates", "all access to the isles is prohibited at present"),
 "E134b": ("The Yellowjackets speak of spirits and undead on the isles.", "It's Probably Not Pirates", "The three Yellowjackets you elect to question speak of spirits and undead infesting the Isles of Umbra."),
 # #135 Representing the Representative
 "E135a": ("Mimidoa gives you a writ of passage if you look into the rumors for him.", "Representing the Representative", "Mimidoa offers you a [[Permission for Passage|writ of passage]], on the condition that you look into the rumors on his behalf."),
 "E135b": ("Skyfryn, back from the isles, says a woman calls and sings to him.", "Representing the Representative", "I...I have to go back. She calls to me...''sings'' to me..."),
 # #136 The Reluctant Researcher
 "E136a": ("Ceana flees back to the mainland in fear.", "The Reluctant Researcher", "In the end, Ceana succumbs to her fear and flees back to the mainland"),
 "E136b": ("The gate guard, Davyd, cannot give you a crystal.", "The Reluctant Researcher", "Though [[Davyd]] understands your intent, he is nevertheless unable to oblige you."),
 # #137 Sweet Somethings
 "E137a": ("Davyd will bring you a crystal if you help solve the mystery.", "Sweet Somethings", "help me unravel this mystery, and I'll bring you your corrupted crystal."),
 "E137b": ("Adventurers speak of an irresistible voice at the Ship Graveyard.", "Sweet Somethings", "The adventurers speak of a beautiful, irresistible voice heard at [[the Ship Graveyard]], which may be connected to the undead."),
 # #138 History Repeating
 "E138a": ("Mimidoa is sure a siren is behind the trouble.", "History Repeating", "Aye...I'd bet me bum ear a siren's behind all this."),
 "E138b": ("The siren retreats into the depths.", "History Repeating", "before at last relenting and retreating to the depths whence she came."),
 "E138c": ("Davyd gives you the corrupted crystal as promised.", "History Repeating", "the corrupted crystal you wanted, safely sealed within the pot, just as you requested."),
 "E138d": ("The crystal is fire-aspected, so it won't help against the wind.", "History Repeating", "the corrupted shard is the manifestation of an over-abundance of the element of fire"),
 # #139 The Curious Case of Giggity
 "E139a": ("A spriggan has devoured every corrupted crystal in the Twelveswood.", "The Curious Case of Giggity", "one such creature with an infamously insatiable appetite has single-handedly devoured every corrupted crystal in the Twelveswood."),
 "E139b": ("You cut the crystal from the spriggan's gut.", "The Curious Case of Giggity", "you rip and tear open the spriggan's huge guts and claim the corrupted crystal nestled deep within."),
 "E139c": ("Hedyn confirms the crystal is ice-aspected.", "The Curious Case of Giggity", "Hedyn confirms that the foul-smelling, offal-laden crystal is comprised of ice-aspected aether."),
 # #140 Better Late than Never
 "E140a": ("Cid's work on the Enterprise is nearly done; only the crystal remains to be tested.", "Better Late than Never", "Cid's work on the ''Enterprise'' is nearly complete, and all that remains is for him to test the crystal you have brought."),
 "E140b": ("Cid says nothing will stand between you and Garuda.", "Better Late than Never", "Once you bring me that crystal, nothing will stand between us and Garuda."),
 "E140c": ("Cid says this is what he was born to do.", "Better Late than Never", "This...this is me. This is what I was born to do."),
 # #141 Lady of the Vortex
 "E141a": ("The Enterprise is ready to fly to the Howling Eye.", "Lady of the Vortex", "the ''Enterprise'' is finally ready to make the journey to [[the Howling Eye]]."),
 "E141b": ("With the Echo you guide Cid through his lost memories of leaving Garlemald for Eorzea.", "Lady of the Vortex", "you guide him through a series of forgotten memories, detailing the path that led the once-loyal engineer to turn his back on [[Garlemald]] and flee to [[Eorzea]]."),
 "E141c": ("You strike Garuda down, but her Ixali worshippers' belief raises her again.", "Lady of the Vortex", "only to see her rise once more, reinvigorated by the belief of her [[Ixal]]i disciples."),
 "E141d": ("Garuda's dying kobold and Amalj'aa captives cry out and summon their own gods.", "Lady of the Vortex", "slaughtering her captive [[kobold]]s and [[Amalj'aa]], whose cries of agony serve to summon their own patron deities."),
 "E141e": ("All efforts now turn to destroying the Empire's weapon.", "Lady of the Vortex", "all efforts must now be focused upon destroying [[Garlean Empire|the Empire]]'s [[The Ultima Weapon|ultimate weapon]]."),
 "E141f": ("Cid and Alphinaud resolve to re-form the Scions at the Waking Sands.", "Lady of the Vortex", "Believing the best course of action is to reform [[the Scions of the Seventh Dawn]], they decide to return to [[the Waking Sands]]."),
 # #142 Reclamation
 "E142a": ("Alphinaud brings you back to the Waking Sands.", "Reclamation", "It is past time that we return to the Waking Sands."),
 "E142b": ("Yda learns that Papalymo and Minfilia were not among the dead.", "Reclamation", "Papalymo and Minfilia weren't among the dead, according to the church."),
 "E142c": ("Alphinaud believes Gaius means to use Minfilia to understand the Echo.", "Reclamation", "He means to use Minfilia to gain an understanding of the Echo."),
 "E142d": ("The captured Scions are held at Castrum Centri, an imperial stronghold in Mor Dhona.", "Reclamation", "your comrades are being held at [[Castrum Centri]], an imperial stronghold in [[Mor Dhona]]."),
 # #143 Casing the Castrum
 "E143a": ("Y'shtola wants intelligence first, from Lord Portelaine at the Observatorium.", "Casing the Castrum", "she suggests traveling to [[the Observatorium]] in [[Coerthas]], and there petitioning Lord [[Portelaine]] for aid."),
 "E143b": ("Four prisoners matching Minfilia, Urianger, Papalymo and Tataru were seen led into Castrum Centri.", "Casing the Castrum", "matching the descriptions of [[Minfilia Warde|Minfilia]], [[Urianger]], [[Papalymo]], and [[Tataru]] were observed being led into Castrum Centri."),
 "E143c": ("Two men, likely Biggs and Wedge, escaped a downed imperial airship.", "Casing the Castrum", "two men─likely [[Biggs]] and [[Wedge]]─escaped from a downed imperial airship not long ago."),
 "E143d": ("Y'shtola reasons the captives will not be executed until the study is complete.", "Casing the Castrum", "they will not be executed until such time as the study is complete."),
 "E143e": ("Gaius sends Rhitahtyn to Castrum Occidens.", "Casing the Castrum", "Rhitahtyn. You depart for Castrum Occidens at midnight."),
 # #144 Eyes on the Empire
 "E144a": ("Imperial soldiers are hunting the escapees.", "Eyes on the Empire", "Imperial soldiers have since been sighted in the area, seeking to recapture them."),
 # #145 Footprints in the Snow
 "E145a": ("Wedge says Biggs went another way to lure their pursuers off.", "Footprints in the Snow", "He went off in a different direction to lure our pursuers away."),
 "E145b": ("Biggs headed west.", "Footprints in the Snow", "At any rate, we know for a fact that Biggs headed west."),
 "E145c": ("Wedge recognizes Cid, alive after five years.", "Footprints in the Snow", "Dare I hope...? Was that...Master"),
 "E145d": ("Cid says Biggs has always taken care of Wedge.", "Footprints in the Snow", "For all the tongue-lashings he gives Wedge, he's always taken care of him."),
 # #146 Monumental Hopes
 "E146a": ("The Fury's Gaze holds only vengeful ghosts.", "Monumental Hopes", "Your search of the Fury's Gaze yields nothing but a confrontation with vengeful ghosts."),
 "E146b": ("Wedge is still determined to find Biggs.", "Monumental Hopes", "is no less determined to find his companion."),
 # #147 Notorious Biggs
 "E147a": ("With Yda and Y'shtola you rescue Biggs from imperial troops.", "Notorious Biggs", "With the aid of [[Yda]] and [[Y'shtola]], you succeed in rescuing Biggs from a detachment of imperial troops."),
 "E147b": ("Y'shtola believes the raiders arrived by teleportation of the kind the Ascians use.", "Notorious Biggs", "they were borne there by potent teleportation magicks─magicks of the kind used by the Ascians."),
 "E147c": ("Biggs and Wedge were held at Castrum Centri apart from Minfilia and the others.", "Notorious Biggs", "we found ourselves in the midst of an imperial stronghold─Castrum Centri. … Biggs and I were thrown into a detainment cell together, while Minfilia and the others were taken elsewhere."),
 "E147d": ("They escaped by sabotaging an airship's altitude control.", "Notorious Biggs", "we sabotaged the ship's altitude control and thereby forced an emergency landing."),
 "E147e": ("Cid and his two core Ironworks members are together again.", "Notorious Biggs", "the three core members of [[Garlond Ironworks]] are together again"),
 # #148 Come-Into-My-Castrum
 "E148a": ("Cid means to march in disguised as imperial troops.", "Come-Into-My-Castrum", "Aye, we'll disguise ourselves as imperial troops and march right in."),
 "E148b": ("Castrum Centri is on high alert.", "Come-Into-My-Castrum", "Not even a fly could get within a hundred yalms of the walls undetected."),
 "E148c": ("Glaumunt has a grudge against the Empire and knows Castrum Centri.", "Come-Into-My-Castrum", "The fellow's got a personal grudge against the Empire, and happens to know a deal about Castrum Centri besides."),
 "E148d": ("Y'shtola and Yda go to scout the stronghold.", "Come-Into-My-Castrum", "Yda and I shall go to reconnoiter Garlean activity at the stronghold."),
 "E148e": ("Glaumunt will help you.", "Come-Into-My-Castrum", "If his response is any indication, it would seem you can indeed expect his aid."),
 # #149 Getting Even with Garlemald
 "E149a": ("A guard wonders why the tribunus is so obsessed with Minfilia.", "Getting Even with Garlemald", "I do wonder, why is the tribunus so obsessed with this Minfilia woman?"),
 "E149b": ("The guards say Minfilia has a mystical power the Garleans lack.", "Getting Even with Garlemald", "They say she possesses some mystical power. Something we Garleans don't have."),
 "E149c": ("Alphinaud is sure the captives are inside Castrum Centri.", "Getting Even with Garlemald", "So Minfilia and the others are indeed at Castrum Centri!"),
 "E149d": ("Glaumunt is seeking a suit of magitek armor.", "Getting Even with Garlemald", "Glaumunt is looking into ways to procure a suit of magitek armor."),
 "E149e": ("Glaumunt shows you a drainage pipe from the command tower for listening in.", "Getting Even with Garlemald", "He tells you of a drainage pipe that leads from the stronghold's command tower"),
 # #150 Drowning Out the Voices / #150 Acting the Part / #151 Dressed for Conquest / #153 Fool Me Twice
 "E150a": ("Cid prepares to jam imperial communications using crystals that amplify their energy, though he is reluctant to use them.", "Drowning Out the Voices", "Cid is satisfied that the crystals will suit his needs, though he expresses his reluctance to harness their power."),
 "E150c": ("Glaumunt's plan is to send you into Castrum Centri in imperial dress.", "Acting the Part", "The plan's to have you enter Castrum Centri all decked out in imperial duds"),
 "E150d": ("You learn the imperial salute by watching patrols.", "Acting the Part", "You have committed the imperial salute to your memory."),
 "E151a": ("Three sets of imperial gear are needed: for Biggs, Wedge and you.", "Dressed for Conquest", "three sets of gear, one for each member of the infiltration team─Biggs, Wedge, and yourself."),
 "E151b": ("Sark Malark, a friend of Glaumunt's, helps with the disguises, and Eginolf repairs the gear.", "Dressed for Conquest", "I have heard of your plight from my friend Glaumunt. … Yes, these will serve beautifully. The great Eginolf never fails to impress."),
 "E153a": ("Glaumunt fed the imperials false intelligence to draw out a patrol.", "Fool Me Twice", "I took the liberty o' feedin' 'em a bit o' the old false intelligence"),
 "E153b": ("You seize a magitek reaper, which needs repairs.", "Fool Me Twice", "You have succeeded in acquiring a magitek reaper, though some repairs will be required before it can be put to use."),
 "E153c": ("Biggs and Wedge repair the reaper at Cid's workshop.", "Fool Me Twice", "have already set about repairing the magitek reaper."),
 # #155 Escape from Castrum Centri (for the existing slice): what the wider cast does in the rescue
 "E155a": ("Y'shtola and Yda confront Livia, who led the raid on the Waking Sands.", "Escape from Castrum Centri", "'Twas you who led the raid on the Waking Sands─you who butchered unarmed men and women for the crime of being unworthy of capture."),
 "E155b": ("Y'shtola and Yda rode into the castrum aboard your vehicle.", "Escape from Castrum Centri", "There chanced to be a commotion outside the castrum's walls which allowed us to avail ourselves of the comforts of your vehicle."),
}

# ---- Presentations for entities the Atlas already has ------------------------------------------------------------
# Each starts at the entity's first step in the extended timeline and ends where the existing record begins, so the
# accepted records are unchanged. Where the story adds nothing new before the A4 baseline, the text repeats the
# accepted #154 text, so the Changes lens shows no false "description updated" at #154.
EARLY_PRES = {
 "char-minfilia": [
   P(Q102, Q106, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who welcomed you at the Waking Sands. Like you, she has the Echo.",
     ["C01", "C33"]),
   P(Q106, Q142, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. When imperial forces under Livia raided the Waking Sands, she offered to surrender if the innocents were spared. "
     "Livia refused, and took her prisoner, wanting her for the Echo.",
     ["C01", "C33", "E106d", "K01", "K02"]),
   P(Q142, Q149, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, taken prisoner when imperial forces under Livia raided the Waking Sands. "
     "She is held at Castrum Centri, an imperial stronghold in Mor Dhona, and Alphinaud believes Gaius means to use her to understand the Echo.",
     ["C01", "K01", "E142d", "E142c"]),
   P(Q149, Q154, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, taken prisoner when imperial forces under Livia raided the Waking Sands, and held at Castrum Centri. "
     "Guards there say the tribunus is obsessed with her, and that she has a mystical power the Garleans lack.",
     ["C01", "K01", "E142d", "E149a", "E149b"]),
 ],
 "char-thancred": [
   P(Q102, Q154, "main", "Thancred",
     "A Scion who serves as the order's man in Ul'dah, and who briefed your first investigation.",
     ["C31", "C39"]),
 ],
 "char-yshtola": [
   P(Q102, Q103, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order, and who told you how the Scions were founded.",
     ["C31", "C40"]),
   P(Q103, Q105, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order. She stood with you when the Company of Heroes judged you worthy to challenge Titan, and warns that the battle has yet to begin.",
     ["C40", "E103b", "E103d"]),
   P(Q105, Q142, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order. On the way to Titan she stayed behind to keep the aetheryte working while you went on alone. "
     "Afterwards, troubled that the elusive Ascians would consort with the Empire, she stayed behind to investigate.",
     ["C40", "E105b", "K14", "E105f"]),
   P(Q142, Q143, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order. She has learned that the Scions captured in the raid on the Waking Sands are held at Castrum Centri, an imperial stronghold in Mor Dhona.",
     ["C40", "E142d"]),
   P(Q143, Q147, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order. She found where the captured Scions are held, and insisted on gathering intelligence before any rescue. "
     "She reasons that the captives will be kept alive until the Empire finishes studying the Echo.",
     ["C40", "E142d", "E143a", "E143d"]),
   P(Q147, Q155, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order. With Yda she helped you rescue Biggs from imperial troops, and she believes the raiders reached the Waking Sands by teleportation of the kind the Ascians use.",
     ["C40", "E147a", "E147b"]),
   P(Q155, A, "main", "Y'shtola",
     "A Scion who looks after Limsa Lominsa for the order. During the rescue at Castrum Centri she and Yda rode in aboard your vehicle and confronted Livia, who led the raid on the Waking Sands.",
     ["C40", "E155b", "E155a"]),
 ],
 "char-urianger": [
   P(Q102, Q143, "main", "Urianger",
     "A Scion who presides over the affairs of the Waking Sands.",
     ["C31", "C41"]),
   P(Q143, Q155, "main", "Urianger",
     "A Scion who presides over the affairs of the Waking Sands. Scouts saw him among four prisoners led into Castrum Centri.",
     ["C41", "E143b"]),
   P(Q155, A, "main", "Urianger",
     "A Scion who presides over the affairs of the Waking Sands. He was among the prisoners held at Castrum Centri, and was freed in the rescue.",
     ["C41", "E143b", "K20"]),
 ],
 "char-tataru": [
   P(Q102, Q143, "main", "Tataru",
     "The Scions' clerk, who makes sure everything runs smoothly.",
     ["C32"]),
   P(Q143, Q155, "main", "Tataru",
     "The Scions' clerk. Scouts saw her among four prisoners led into Castrum Centri.",
     ["C32", "E143b"]),
   P(Q155, A, "main", "Tataru",
     "The Scions' clerk. She was among the prisoners held at Castrum Centri, and was freed in the rescue.",
     ["C32", "E143b", "K20"]),
 ],
 "char-alphinaud": [
   P(Q102, Q110, "main", "Alphinaud",
     "A young traveler who, with his twin sister, calls himself a student of history.",
     ["C10", "C42"]),
   P(Q110, Q129, "main", "Alphinaud",
     "A young Scion who stands against the primals and the Empire, as his grandfather once did. He recognized Marques as Cid, an engineer missing since the Calamity, "
     "and enlisted him to find his lost airship, the Enterprise: the Ixal have summoned Garuda, and the surviving Scions need the ship to reach her.",
     ["C25", "E110c", "E110e"]),
   P(Q129, Q141, "main", "Alphinaud",
     "A young Scion who stands against the primals and the Empire, as his grandfather once did. He and Cid recovered the Enterprise from the Stone Vigil, "
     "and it must now be repaired to brave the storm around Garuda.",
     ["C25", "E129c", "E129e"]),
   P(Q141, Q142, "main", "Alphinaud",
     "A young Scion who stands against the primals and the Empire, as his grandfather once did. After the Empire's weapon seemingly absorbed the primals at the Howling Eye, "
     "he turned the Scions' efforts to destroying it, and resolved to re-form the order at the Waking Sands.",
     ["C25", "K11", "E141e", "E141f"]),
   P(Q142, Q154, "main", "Alphinaud",
     "A young Scion who stands against the primals and the Empire, as his grandfather once did. He has brought the survivors back to the Waking Sands to rebuild the order, "
     "and is working to rescue the Scions held at Castrum Centri.",
     ["C25", "K16", "E142a", "E142d"]),
 ],
 "org-scions": [
   P(Q102, Q106, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. It stands above politics, and its headquarters is the Waking Sands in Vesper Bay, western Thanalan.",
     ["C34", "C01", "C02"]),
   P(Q106, Q110, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. Imperial forces raided its headquarters at the Waking Sands, slaughtered many of its members and took prisoners, Minfilia among them. "
     "Father Iliud, an old friend of Minfilia's, has given the survivors sanctuary at his church in eastern Thanalan.",
     ["C34", "C01", "E106b", "K01", "E106f"]),
   P(Q110, Q141, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia, who was taken prisoner when imperial forces raided its headquarters at the Waking Sands. "
     "The surviving Scions, with Alphinaud, are seeking Cid's lost airship to reach the primal Garuda.",
     ["C34", "C01", "E106b", "K01", "E110e"]),
   P(Q141, Q142, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia, who was taken prisoner when imperial forces raided its headquarters. "
     "After the Empire's weapon seemingly absorbed the primals at the Howling Eye, the survivors resolved to re-form the order at the Waking Sands.",
     ["C34", "C01", "K01", "K11", "E141f"]),
   P(Q142, Q154, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. Its captured members, Minfilia among them, are held at Castrum Centri. "
     "Alphinaud is rebuilding the order at its damaged headquarters, the Waking Sands, and its free members are preparing a rescue.",
     ["C34", "C01", "E142d", "K16", "C38"]),
 ],
 "loc-waking-sands": [
   P(Q102, Q106, "main", "The Waking Sands",
     "The Scions' headquarters in Vesper Bay, western Thanalan, where Urianger presides over the order's affairs.",
     ["C02", "C41"]),
   P(Q106, Q142, "main", "The Waking Sands",
     "The Scions' headquarters in Vesper Bay, western Thanalan. Imperial forces raided it, slaughtering many Scions and taking prisoners.",
     ["C02", "E106b"]),
   P(Q142, A, "main", "The Waking Sands",
     "The Scions' headquarters in Vesper Bay, western Thanalan, damaged in the imperial raid. Alphinaud has brought the surviving Scions back to restore it and rebuild the order.",
     ["C02", "E106b", "E142a", "C38"]),
 ],
 "char-livia": [
   P(Q106, Q154, "main", "Livia",
     "An imperial officer who led the raid on the Waking Sands. She refused Minfilia's surrender, took her prisoner, and is eager to learn about the Echo.",
     ["K01", "K02"]),
 ],
 "char-gaius": [
   P(Q141, Q143, "main", "Gaius",
     "The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. "
     "At the Howling Eye he called forth an imperial weapon that overpowered and seemingly absorbed three primals. He knows Cid, and scorned him for forsaking kin and country.",
     ["K10", "K11", "K08"], ["the Black Wolf"]),
   P(Q143, Q154, "main", "Gaius",
     "The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. "
     "He called forth an imperial weapon that overpowered and seemingly absorbed three primals, and he means to purge the land of its false gods.",
     ["K10", "K11", "K12"], ["the Black Wolf"]),
 ],
 "char-lahabrea": [
   P(Q105, Q129, "main", "Lahabrea",
     "A figure who appeared with imperial officers at the Navel after Titan fell, and urged you on, saying your work is far from done. "
     "Y'shtola is troubled that the elusive Ascians would consort with the Empire.",
     ["E105e", "K14"]),
   P(Q129, Q141, "main", "Lahabrea",
     "An Ascian, one of an elusive kind that the Scions are troubled to find consorting with the Empire. In the Stone Vigil he woke the dragon that guarded the Enterprise, "
     "taunting that Garuda is stronger than any primal you have faced.",
     ["K13", "K14", "E129b"]),
   P(Q141, Q154, "main", "Lahabrea",
     "An Ascian, one of an elusive kind that the Scions are troubled to find consorting with the Empire. He marveled as the Empire's weapon grew stronger with each primal it consumed.",
     ["K13", "K14", "K15"]),
 ],
 "char-cid": [
   P(Q110, Q129, "main", "Cid",
     "An engineer, missing since the Calamity, who lived as Marques at the church in eastern Thanalan with no memory of his past. "
     "Alphinaud recognized him, and he has joined the search for his lost airship, the Enterprise, which the Scions need to reach Garuda.",
     ["E110c", "E110d", "E110e"], ["Marques"]),
   P(Q129, Q130, "main", "Cid",
     "An engineer, missing since the Calamity, who lived as Marques with no memory of his past. He has his airship, the Enterprise, back from the Stone Vigil, and he knows it, "
     "though he can't recall more. It must be repaired before it can brave the storm around Garuda.",
     ["E110c", "E129d", "E129e"], ["Marques"]),
   P(Q130, Q141, "main", "Cid",
     "An engineer, missing since the Calamity, who lived as Marques with no memory of his past. He is repairing his airship, the Enterprise, "
     "and plans to use a corrupted crystal to change the aspect of Garuda's wind barrier so the ship can pass.",
     ["E110c", "E130a", "E130b"], ["Marques"]),
   P(Q141, Q147, "main", "Cid",
     "A brilliant engineer, born and raised in Garlemald, who left the Empire for Eorzea and built the Ironworks. With the Echo you guided him through the memories he had lost, "
     "and he flew the Enterprise to the Howling Eye, where Gaius, who knows him, scorned him for forsaking kin and country.",
     ["K07", "E141b", "E141a", "K08"], ["Marques"]),
   P(Q147, Q148, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. Gaius knows him and scorns him for forsaking kin and country. "
     "His Ironworks crew, Biggs and Wedge, are back with him.",
     ["K07", "K08", "E147e"], ["Marques"]),
   P(Q148, Q154, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. Gaius knows him and scorns him for forsaking kin and country. "
     "With his crew back, he means to break into Castrum Centri disguised as imperial troops and rescue the captive Scions.",
     ["K07", "K08", "E147e", "E148a"], ["Marques"]),
 ],
}

# ---- New entities --------------------------------------------------------------------------------------------------
# Arc entries (category event) first, then the new cast. Every new entity keeps a presentation through the milestones
# (v2 plan, baseline rule); after its last change the text simply stays as it was, adding nothing later.
ARC_TITAN, ARC_RAID, ARC_ENTERPRISE, ARC_BARRIER, ARC_RESCUE = (
    "evt-road-to-titan", "evt-fall-of-the-waking-sands", "evt-search-for-the-enterprise", "evt-garudas-barrier", "evt-road-to-castrum-centri")

N_TITAN = "The Road to Titan"
N_RAID = "The Fall of the Waking Sands"
N_ENT = "The Search for the Enterprise"
N_BAR = "Garuda's Barrier"
N_RES = "The Road to Castrum Centri"

# Shared openings, so each step's recap reads on its own.
RAID_LEAD = "Imperial forces under Livia raided the Waking Sands, slaughtered many Scions and took Minfilia prisoner. "
ENT_LEAD = "You are searching Coerthas for Cid's lost airship, the Enterprise, which the Scions need to reach Garuda, the primal the Ixal have summoned. "
BAR_LEAD = "Cid is repairing the Enterprise to reach Garuda, but it can't pass her wind barrier unless a corrupted crystal can change its aspect. "
RES_LEAD = "Alphinaud is rebuilding the Scions, and Minfilia, Urianger, Papalymo and Tataru are held at Castrum Centri, an imperial stronghold in Mor Dhona. "

NEW_ENT = [
 (ARC_TITAN, "event", [
   P(Q103, Q104, "main", N_TITAN,
     "The Company of Heroes turned a feast at Costa del Sol into a test, weighing you by deeds rather than reputation. "
     "Its five chosen members have judged you a worthy challenger for the primal Titan, and Y'shtola, at your side, warns that the battle has yet to begin. "
     "Wheiskaet can tell you how to reach Titan's lair.",
     ["E103a", "E103c", "E103b", "E103d", "E103e"]),
   P(Q104, Q105, "main", N_TITAN,
     "Five members of the Company of Heroes judged you worthy to challenge the primal Titan. Wheiskaet sent you to Bronze Lake to find Riol, another former member, "
     "who guards the secret of how to reach Titan and stays hidden until he hears the right signal. He has answered yours.",
     ["E103b", "E104a", "E104b"]),
   P(Q105, None, "main", N_TITAN,
     "Riol revealed that the Company of Heroes reached Titan through a beastman aetheryte. Y'shtola stayed behind to keep it working, and you went on alone and struck Titan down in the Navel. "
     "Then imperial officers, Rhitahtyn among them, appeared with a figure called Lahabrea, who urged you on: your work is far from done. "
     "Y'shtola, troubled that the elusive Ascians would consort with the Empire, stayed behind to investigate.",
     ["E105a", "E105b", "E105c", "E105d", "E105e", "K14", "E105f"]),
 ]),
 (ARC_RAID, "event", [
   P(Q106, Q107, "main", N_RAID,
     "After Titan fell, Minfilia called you back to the Waking Sands, but imperial forces under Livia got there first. They came for the one who slew Ifrit and Titan, "
     "slaughtered many Scions, refused Minfilia's offer to surrender if the innocents were spared, and took her prisoner. "
     "The dying sylph Noraxia sent you to the church in eastern Thanalan, where Father Iliud took you in.",
     ["E106a", "E106b", "E106c", "E106d", "K01", "E106e", "E106f"]),
   P(Q107, Q108, "main", N_RAID,
     RAID_LEAD + "You have taken sanctuary at the church in eastern Thanalan with Father Iliud. There Marques, a survivor of Carteneau, mended a dead man's broken horologe "
     "as though his hands remembered the work, and Sister Eluned wondered whether its owner was a Garlean spy.",
     ["E106b", "K01", "E106f", "E106g", "E107a", "E107b"]),
   P(Q108, Q109, "main", N_RAID,
     RAID_LEAD + "From the church in eastern Thanalan, where Father Iliud gave you sanctuary, you helped carry the fallen from the Waking Sands for their rites, "
     "and the church will see them to Thal's realm.",
     ["E106b", "K01", "E106f", "E108a", "E108b"]),
   P(Q109, Q110, "main", N_RAID,
     RAID_LEAD + "You returned the body of Noraxia, the sylph who died there, to her people in the Black Shroud, who mourned her as brave; Komuxio vowed vengeance on the imperials. "
     "The other fallen Scions now rest in the church's lichyard.",
     ["E106b", "K01", "E109a", "E109b", "E109c", "E109d"]),
   P(Q110, None, "main", N_RAID,
     RAID_LEAD + "At the church that sheltered you, Marques felt watched, and a stranger attacked you in the lichyard; Father Iliud knew his sword for Garlean steel. "
     "Then Alphinaud arrived and named Marques as Cid, an engineer missing since the Calamity. Cid has no memory of his past, but he has joined Alphinaud.",
     ["E106b", "K01", "E110a", "E110b", "E110c", "E110d"]),
 ]),
 (ARC_ENTERPRISE, "event", [
   P(Q110, Q111, "main", N_ENT,
     "At the church in eastern Thanalan, Alphinaud recognized Marques as Cid, an engineer missing since the Calamity. Cid has no memory of his past, but he has joined Alphinaud: "
     "the Ixal have summoned Garuda, and the surviving Scions need Cid's lost airship, the Enterprise, to reach her. It was last seen over Gridania.",
     ["E110c", "E110d", "E110e", "E110f"]),
   P(Q111, Q112, "main", N_ENT,
     ENT_LEAD + "Cid still remembers nothing of his past. A tale says the ship flew northwest from Gridania toward Coerthas, and at Florentel's Spire you found Vortefaurt, who saw it pass.",
     ["E110e", "E110d", "E111a", "E111b"]),
   P(Q112, Q113, "main", N_ENT,
     ENT_LEAD + "Vortefaurt saw the ship vanish over the mountains of Coerthas. The astrologers of Ishgard's Observatorium may have records, "
     "but Ser Ludovoix will not let an outsider read them, and Ishgard offers strangers no help.",
     ["E110e", "E112a", "E112b", "E112c"]),
   P(Q113, Q114, "main", N_ENT,
     ENT_LEAD + "The Observatorium's records may tell where it went, but they chart a war with the dragons that has raged for generations, and even after you saved a knight from heretics "
     "sworn to the dragons, they stay closed. An inquisitor, Guillaime, warned you to keep out of Ishgard's affairs.",
     ["E110e", "E112b", "E113a", "E113b", "E113c"]),
   P(Q114, Q115, "main", N_ENT,
     ENT_LEAD + "Ishgard's Observatorium won't open its records to an outsider, and Inquisitor Guillaime has warned you off. "
     "House Durendaire owes you for two good deeds, but Lord Portelaine will introduce you to the other High Houses only after a third.",
     ["E110e", "E114a", "E113c", "E114b", "E114c"]),
   P(Q115, Q116, "main", N_ENT,
     ENT_LEAD + "Seeking help from Ishgard's High Houses, you recovered a porter's stolen wares, and among them was a draconian rosary in a chest belonging to Lord Francel of House Haillenarte, "
     "a house whispered to be full of heretics. Lord Portelaine has told the inquisitors and warned you away from the house.",
     ["E110e", "E114b", "E115a", "E115b", "E115c"]),
   P(Q116, Q117, "main", N_ENT,
     ENT_LEAD + "A draconian rosary found among Lord Francel's belongings has put him under suspicion of heresy, though his former servant swears he is innocent. "
     "Francel sent you with a letter to Lord Haurchefant of House Fortemps at Camp Dragonhead, who has promised to make inquiries about the ship.",
     ["E110e", "E115a", "E116a", "E116b", "E116c", "E116e"]),
   P(Q117, Q118, "main", N_ENT,
     ENT_LEAD + "Lord Haurchefant of House Fortemps is making inquiries for you, but the High Houses have nothing to offer: all of Coerthas talks only of heretics. "
     "Since Inquisitor Guillaime arrived, countless have been found, even among Ishgard's elite, and the charge against Lord Francel has thrown House Haillenarte into chaos.",
     ["E110e", "E116e", "E117c", "E117a", "E117b"]),
   P(Q118, Q119, "main", N_ENT,
     ENT_LEAD + "Lord Haurchefant has found a witness to its flight, but he won't speak to anyone tied to an accused heretic. "
     "You saved Lord Francel at the Steel Vigil, where he hoped to prove his devotion. His heresy trial approaches, and his name, and yours with it, must be cleared first.",
     ["E110e", "E118c", "E118a", "E118b", "E118d"]),
   P(Q119, Q120, "main", N_ENT,
     ENT_LEAD + "A witness to its flight won't talk until Lord Francel is cleared of heresy. Haurchefant believes the rosary against Francel was planted, "
     "and two parcels bound for Skyfire Locks each held another: a crude attempt to smear House Haillenarte. Francel's trial is at hand.",
     ["E110e", "E118c", "E119a", "E119b", "E119c", "E119d"]),
   P(Q120, Q121, "main", N_ENT,
     ENT_LEAD + "At Witchdrop, Inquisitor Guillaime ordered Lord Francel to prove his innocence by leaping from the cliff. You protected him, Haurchefant argued that someone was using the trials "
     "to set the houses against each other, and a heretic among the Temple Knights was exposed. Guillaime withdrew the charges, pending investigation.",
     ["E110e", "E120a", "E120b", "E120e", "E120c", "E120d"]),
   P(Q121, Q122, "main", N_ENT,
     ENT_LEAD + "With Lord Francel cleared, the witness spoke: the ship landed near the Stone Vigil before the Calamity, and the outpost is now held by Dravanian forces. "
     "Haurchefant has written to Lord Drillemont of Whitebrim Front to ask that you be let in, and Francel warns that those who tried to destroy his house are still unknown.",
     ["E110e", "E120d", "E121a", "E121b", "E121c", "E121d"]),
   P(Q122, Q123, "main", N_ENT,
     ENT_LEAD + "It landed near the Stone Vigil, now held by Dravanian forces. At Whitebrim Front, Inquisitor Guillaime branded you untrustworthy and the Scions a defunct band the Empire had exterminated, "
     "and Lord Drillemont barred the way until the outpost is retaken and you declare your true intentions. Alphinaud means to earn his trust.",
     ["E110e", "E121a", "E122a", "E122c", "E122d", "E122e", "E122f"]),
   P(Q123, Q124, "main", N_ENT,
     ENT_LEAD + "It landed near the Stone Vigil, but Lord Drillemont of Whitebrim Front won't let you in, and Inquisitor Guillaime calls you untrustworthy. "
     "To win Drillemont's notice through his knights, you helped the cook feed the hungry barracks.",
     ["E110e", "E121a", "E122e", "E122c", "E123a"]),
   P(Q124, Q125, "main", N_ENT,
     ENT_LEAD + "It landed near the Stone Vigil, but Lord Drillemont of Whitebrim Front won't let you in. Cid built the infirmary a better alembic, but Inquisitor Guillaime warned the chirurgeons "
     "that your gifts serve an unknown end, and he seems to hate you and your companions.",
     ["E110e", "E121a", "E122e", "E124a", "E124c", "E124d"]),
   P(Q125, Q126, "main", N_ENT,
     ENT_LEAD + "It landed near the Stone Vigil, but Lord Drillemont won't let you in, and Inquisitor Guillaime works against you. "
     "You heard he carried an injured knight, Joellaut, to the gates on the night he arrived, and Alphinaud suspects he has other reasons for hindering you.",
     ["E110e", "E121a", "E122e", "E125a", "E125b"]),
   P(Q126, Q127, "main", N_ENT,
     ENT_LEAD + "It landed near the Stone Vigil, but Lord Drillemont won't let you in. Retracing Joellaut's story of the inquisitor's first night, you found a frozen corpse in a chasm: "
     "the real Inquisitor Guillaime, murdered the day he arrived. The man you know by that name is an impostor, and his true identity and motives are unknown.",
     ["E110e", "E121a", "E122e", "E126a", "E126b", "E126c", "E126d"]),
   P(Q127, Q128, "main", N_ENT,
     ENT_LEAD + "It landed near the Stone Vigil. The inquisitor who works against you is an impostor: Prunilla confessed he coerced her and condemned innocent people for carrying draconian rosaries, "
     "and that she planted some of his rosaries in shipments to Skyfire Locks. Convinced, Lord Drillemont will let you into the Stone Vigil once the impostor faces justice.",
     ["E110e", "E121a", "E126c", "E127a", "E127b", "E127c", "E127d", "E127e"]),
   P(Q128, Q129, "main", N_ENT,
     ENT_LEAD + "At Snowcloak, Lord Drillemont named the false inquisitor the murderer of the real Guillaime. "
     "The impostor called all Ishgard complicit in the archbishop's lies, took the form of a dragon beside his Dravanian allies, and was defeated, "
     "warning that the dragons in the Stone Vigil, where the ship landed, would tear you apart.",
     ["E110e", "E121a", "E128a", "E128b", "E128c", "E128f", "E128d"]),
   P(Q129, None, "main", N_ENT,
     "Cid and Alphinaud need Cid's airship, the Enterprise, to reach Garuda, the primal the Ixal have summoned. In the Stone Vigil you found it beside a sleeping dragon, "
     "and the Ascian Lahabrea woke the beast, taunting that Garuda is stronger than any primal you have faced. While you held off the dragon, Alphinaud and Cid slipped aboard. "
     "Cid knows the ship, though he can't recall more, and it is in no state to weather Garuda's storm.",
     ["E110e", "K13", "E129b", "E129c", "E129d", "E129e"]),
 ]),
 (ARC_BARRIER, "event", [
   P(Q130, Q131, "main", N_BAR,
     "The Enterprise is back in Cid's hands, but battered as it is, it can't survive the winds around the Howling Eye, Garuda's sanctuary. "
     "While the Seedseers house it for repairs, Cid plans to use a corrupted crystal to change the aspect of Garuda's wind barrier, "
     "and he has sent you to Lamberteint, a scholar he met while he lived as Marques.",
     ["E130a", "E130e", "E130b", "E130c", "E130d"]),
   P(Q131, Q132, "main", N_BAR,
     BAR_LEAD + "The scholar Lamberteint lent you a warded pot to carry such a crystal safely, and sent you to his pupil Hahasako at Highbridge.",
     ["E130a", "E130b", "E131a"]),
   P(Q132, Q133, "main", N_BAR,
     BAR_LEAD + "The crystal you broke from the Burning Wall, with Hahasako's help, is wind-aspected, so it would only strengthen the barrier.",
     ["E130a", "E130b", "E131a", "E132a"]),
   P(Q133, Q134, "main", N_BAR,
     BAR_LEAD + "The first crystal you found was wind-aspected and useless. Lamberteint's pupil Ceana has found a promising site at Pharos Sirius on the Isles of Umbra, and you found her in Aleport.",
     ["E130a", "E130b", "E132a", "E133a"]),
   P(Q134, Q135, "main", N_BAR,
     BAR_LEAD + "Lamberteint's pupil Ceana believes the Isles of Umbra hold such crystals, but the isles are closed, and the Yellowjackets speak of spirits and undead there.",
     ["E130a", "E130b", "E133a", "E134a", "E134b"]),
   P(Q135, Q136, "main", N_BAR,
     BAR_LEAD + "The scholar Ceana believes the Isles of Umbra hold such crystals, and the isles are said to be haunted. Mimidoa gave you a writ of passage there in return for looking into the rumors, "
     "and Skyfryn, back from the isles, raves of a woman singing to him.",
     ["E130a", "E130b", "E133a", "E134b", "E135a", "E135b"]),
   P(Q136, Q137, "main", N_BAR,
     BAR_LEAD + "You crossed to the Isles of Umbra with a writ of passage, but the scholar Ceana fled back to the mainland in fear, and the gate guard, Davyd, can't give you a crystal.",
     ["E130a", "E130b", "E135a", "E136a", "E136b"]),
   P(Q137, Q138, "main", N_BAR,
     BAR_LEAD + "On the Isles of Umbra, the guard Davyd will find you one if you help solve the island's mystery, and adventurers speak of an irresistible voice at the Ship Graveyard.",
     ["E130a", "E130b", "E136b", "E137a", "E137b"]),
   P(Q138, Q139, "main", N_BAR,
     BAR_LEAD + "On the Isles of Umbra, Mimidoa lured a siren ashore and you drove her back into the depths. Davyd kept his word, but the crystal he gave you is fire-aspected and won't help against the wind.",
     ["E130a", "E130b", "E138a", "E138b", "E138c", "E138d"]),
   P(Q139, Q140, "main", N_BAR,
     BAR_LEAD + "Two crystals proved the wrong aspect. In Gridania, Hedyn told you a spriggan had devoured every corrupted crystal in the Twelveswood; you cut the last one from its gut, and it is ice-aspected.",
     ["E130a", "E130b", "E138d", "E139a", "E139b", "E139c"]),
   P(Q140, Q141, "main", N_BAR,
     "Cid has been repairing the Enterprise to pass Garuda's wind barrier. You brought him an ice-aspected corrupted crystal, his work is nearly done, "
     "and once it passes his tests, he says, nothing will stand between you and Garuda. This, he says, is what he was born to do.",
     ["E130b", "E139c", "E140a", "E140b", "E140c"]),
   P(Q141, None, "main", N_BAR,
     "The Enterprise carried you to the Howling Eye, and on the way the Echo let you guide Cid through his lost memories of leaving Garlemald for Eorzea. "
     "You struck Garuda down, but her Ixali worshippers' belief raised her again, and her dying captives' cries summoned their own gods. "
     "Then Gaius, the Black Wolf, called forth an imperial weapon that seemingly absorbed all three primals. The Scions mean to re-form, and to destroy that weapon.",
     ["E141a", "E141b", "E141c", "E141d", "K11", "K10", "E141e", "E141f"]),
 ]),
 (ARC_RESCUE, "event", [
   P(Q142, Q143, "main", N_RES,
     "After the Empire's weapon seemingly absorbed the primals, Alphinaud brought you and Cid back to the ruined Waking Sands to rebuild the Scions. "
     "Yda, who was away during the raid, learned that Papalymo and Minfilia were not among the dead, and Y'shtola has found that the captured Scions are held at Castrum Centri, "
     "an imperial stronghold in Mor Dhona. Alphinaud believes Gaius means to use Minfilia to understand the Echo.",
     ["K11", "E142a", "K16", "E142b", "E142d", "E142c"]),
   P(Q143, Q144, "main", N_RES,
     RES_LEAD + "Y'shtola reasons they will be kept alive until the Empire finishes studying the Echo, so you are first going after two escapees, likely Biggs and Wedge, "
     "who fled a downed imperial airship and are being hunted in Coerthas. Meanwhile Gaius readies his weapon to purge the land of its gods.",
     ["K16", "E143b", "E143d", "E143c", "K12"]),
   P(Q144, Q145, "main", N_RES,
     RES_LEAD + "First you are tracking two escapees, likely Biggs and Wedge, who fled a downed imperial airship in Coerthas. Imperial soldiers are hunting them too.",
     ["K16", "E143b", "E143c", "E144a"]),
   P(Q145, Q146, "main", N_RES,
     RES_LEAD + "In the snows of Coerthas you found Wedge, one of two escapees from an imperial airship. Biggs went another way to draw their pursuers off and was last seen heading west.",
     ["K16", "E143b", "E143c", "E145a", "E145b"]),
   P(Q146, Q147, "main", N_RES,
     RES_LEAD + "In Coerthas you found Wedge, who escaped from the Empire, but Biggs drew their pursuers away and is still missing. He wasn't in the Fury's Gaze, and Wedge is still determined to find him.",
     ["K16", "E143b", "E145a", "E146a", "E146b"]),
   P(Q147, Q148, "main", N_RES,
     RES_LEAD + "Yda and Y'shtola helped you rescue Biggs from imperial troops, so Cid's Ironworks crew is together again. "
     "Biggs and Wedge were taken to Castrum Centri too, and escaped by sabotaging an airship. Y'shtola suspects the raiders reached the Waking Sands by teleportation of the kind the Ascians use.",
     ["K16", "E143b", "E147a", "E147e", "E147c", "E147d", "E147b"]),
   P(Q148, Q149, "main", N_RES,
     RES_LEAD + "The stronghold is on high alert, so Cid means to march in disguised as imperial troops. At Revenant's Toll you recruited Glaumunt, "
     "who bears a grudge against the Empire and knows the castrum, while Y'shtola and Yda scout it.",
     ["K16", "E143b", "E148b", "E148a", "E148c", "E148e", "E148d"]),
   P(Q149, Q150, "main", N_RES,
     RES_LEAD + "Cid means to march in disguised as imperial troops. Through a drainage pipe, you overheard guards say the tribunus is obsessed with Minfilia, who they believe has a mystical power. "
     "Alphinaud is sure the captives are inside, and Glaumunt is seeking a suit of magitek armor.",
     ["K16", "E143b", "E148a", "E149e", "E149a", "E149b", "E149c", "E149d"]),
   P(Q150, Q150B, "main", N_RES,
     RES_LEAD + "Cid and Glaumunt are preparing to march in disguised as imperial troops, with a suit of magitek armor if one can be found. "
     "For Cid you took readings at a crystal cluster near Revenant's Toll, so that he can jam imperial communications, though he is reluctant to use the crystals' power.",
     ["K16", "E143b", "E148a", "E149d", "E150a"]),
   P(Q150B, Q151, "main", N_RES,
     RES_LEAD + "Glaumunt's plan is to send you into the castrum dressed as an imperial soldier, so you learned the imperial salute by watching the patrols. "
     "Cid is ready to jam imperial communications, and a suit of magitek armor is still needed.",
     ["K16", "E143b", "E150c", "E150d", "E150a", "E149d"]),
   P(Q151, Q153, "main", N_RES,
     RES_LEAD + "You, Biggs and Wedge will go in disguised as imperial soldiers. Sark Malark, a friend of Glaumunt's, had you take three sets of imperial gear for the three of you, "
     "and the smith Eginolf repaired them. All that's still missing is a suit of magitek armor.",
     ["K16", "E143b", "E150c", "E151a", "E151b", "E149d"]),
   P(Q153, Q154, "main", N_RES,
     RES_LEAD + "You, Biggs and Wedge will go in disguised as imperial soldiers. Glaumunt fed the imperials false word of insurgents to draw out a patrol, "
     "and with Cid's help you seized a magitek reaper. Biggs and Wedge are repairing it at Cid's workshop.",
     ["K16", "E143b", "E151a", "E153a", "E153b", "E153c"]),
   P(Q154, None, "main", N_RES,
     RES_LEAD + "You, Biggs and Wedge will go in disguised as imperial soldiers. Cid's crew restored the magitek reaper you seized, and after you fought off imperial troops sent to reclaim it, "
     "the armor works. The time has come to infiltrate Castrum Centri and rescue the imprisoned Scions.",
     ["K16", "E143b", "E151a", "E153b", "K09"]),
 ]),
 # ---- Characters ----
 ("char-yda", "character", [
   P(Q102, Q142, "main", "Yda",
     "A Scion, one of the friends Minfilia introduced you to in the order.",
     ["C31"]),
   P(Q142, Q147, "main", "Yda",
     "A Scion who was away when the Waking Sands was raided. She learned that Papalymo and Minfilia were not among the dead.",
     ["C31", "E142b"]),
   P(Q147, Q155, "main", "Yda",
     "A Scion who was away when the Waking Sands was raided. With Y'shtola she helped you rescue Biggs from imperial troops.",
     ["C31", "E142b", "E147a"]),
   P(Q155, None, "main", "Yda",
     "A Scion who was away when the Waking Sands was raided. During the rescue at Castrum Centri she and Y'shtola rode in aboard your vehicle and confronted Livia, who led the raid.",
     ["C31", "E142b", "E155b", "E155a"]),
 ]),
 ("char-papalymo", "character", [
   P(Q102, Q142, "main", "Papalymo",
     "A Scion, one of the friends Minfilia introduced you to in the order.",
     ["C31"]),
   P(Q142, Q143, "main", "Papalymo",
     "A Scion. After the raid on the Waking Sands, Yda learned that he was not among the dead.",
     ["C31", "E142b"]),
   P(Q143, Q155, "main", "Papalymo",
     "A Scion taken in the raid on the Waking Sands. Scouts saw him among four prisoners led into Castrum Centri.",
     ["C31", "E142b", "E143b"]),
   P(Q155, None, "main", "Papalymo",
     "A Scion taken in the raid on the Waking Sands. He was among the prisoners held at Castrum Centri, and was freed in the rescue.",
     ["C31", "E143b", "K20"]),
 ]),
 ("char-titan", "character", [
   P(Q103, Q105, "main", "Titan",
     "A primal. The Company of Heroes has judged you worthy to challenge him.",
     ["E103b", "E103e"]),
   P(Q105, Q141, "main", "Titan",
     "The primal the kobolds call their Great Father, the Lord of Crags. The Company of Heroes once reached him through a beastman aetheryte, and you struck him down in the Navel.",
     ["E105c", "E105a"], ["the Lord of Crags"]),
   P(Q141, None, "main", "Titan",
     "The primal the kobolds call their Great Father, the Lord of Crags. You struck him down in the Navel. At the Howling Eye, the dying cries of Garuda's captives summoned their own gods, "
     "and the Empire's weapon seemingly absorbed all three primals.",
     ["E105c", "E141d", "K11"], ["the Lord of Crags"]),
 ]),
 ("char-rhitahtyn", "character", [
   P(Q105, Q143, "main", "Rhitahtyn",
     "An imperial officer who appeared at the Navel after Titan fell, and refused to endorse his comrade's plan.",
     ["E105d"]),
   P(Q143, Q157, "main", "Rhitahtyn",
     "An imperial officer who serves Gaius. After Titan fell he refused to endorse a comrade's plan, and Gaius has sent him to Castrum Occidens.",
     ["E105d", "E143e"]),
   P(Q157, None, "main", "Rhitahtyn",
     "An imperial officer who served Gaius as one of the Black Wolf's most trusted lieutenants, sent to Castrum Occidens. You slew him in the first phase of Operation Archon.",
     ["E143e", "K42"]),
 ]),
 ("char-noraxia", "character", [
   P(Q106, Q109, "main", "Noraxia",
     "A sylph you found dying at the Waking Sands after the imperial raid. With her last words she sent you to the church in eastern Thanalan.",
     ["E106e"]),
   P(Q109, None, "main", "Noraxia",
     "A sylph who died in the imperial raid on the Waking Sands, after sending you to the church in eastern Thanalan. You returned her body to her people in the Black Shroud, who mourned her as brave.",
     ["E106e", "E109a", "E109b"]),
 ]),
 ("char-iliud", "character", [
   P(Q106, Q110, "main", "Iliud",
     "A priest at the church in eastern Thanalan who has known Minfilia since she was a child, and has sworn to support her and her fellow Scions. "
     "He gave you sanctuary after the raid on the Waking Sands.",
     ["E106f", "E106g"], ["Father Iliud"]),
   P(Q110, None, "main", "Iliud",
     "A priest at the church in eastern Thanalan who has known Minfilia since she was a child, and has sworn to support her and her fellow Scions. "
     "He sheltered you after the raid on the Waking Sands, and knew the sword of the man watching Marques for Garlean steel.",
     ["E106f", "E110b"], ["Father Iliud"]),
 ]),
 ("char-marques", "character", [
   P(Q106, Q107, "main", "Marques",
     "A survivor of the battle of Carteneau whom the church in eastern Thanalan took in. Father Iliud has asked him to look after you.",
     ["E106g"]),
   P(Q107, Q110, "main", "Marques",
     "A survivor of the battle of Carteneau whom the church in eastern Thanalan took in. He mended a dead man's broken horologe as though his hands remembered the work.",
     ["E106g", "E107a"]),
   P(Q110, None, "main", "Marques",
     "The name of a survivor of Carteneau whom the church in eastern Thanalan sheltered. Alphinaud recognized him as Cid, an engineer missing since the Calamity.",
     ["E106g", "E110c"]),
 ]),
 ("char-garuda", "character", [
   P(Q110, Q129, "main", "Garuda",
     "A primal summoned by the Ixal. The Scions need Cid's lost airship, the Enterprise, to reach her.",
     ["E110e"]),
   P(Q129, Q130, "main", "Garuda",
     "A primal summoned by the Ixal. The Ascian Lahabrea taunts that she is stronger than any primal you have faced, and the Enterprise must be repaired to brave her storm.",
     ["E110e", "E129b", "E129e"]),
   P(Q130, Q141, "main", "Garuda",
     "A primal summoned by the Ixal. Her sanctuary, the Howling Eye, is ringed by winds the battered Enterprise can't survive, and her barrier is wind-aspected aether. "
     "The Ascian Lahabrea taunts that she is stronger than any primal you have faced.",
     ["E110e", "E130a", "E130b", "E129b"]),
   P(Q141, None, "main", "Garuda",
     "A primal summoned by the Ixal. At the Howling Eye you struck her down, but her Ixali worshippers' belief raised her again; "
     "then Gaius's imperial weapon seemingly absorbed her, along with the gods her dying captives summoned.",
     ["E110e", "E141c", "E141d", "K11"], ["the Lady of the Vortex"]),
 ]),
 ("char-francel", "character", [
   P(Q115, Q116, "main", "Francel",
     "A lord of House Haillenarte. A draconian rosary has turned up in a chest belonging to him.",
     ["E115a"]),
   P(Q116, Q118, "main", "Francel",
     "A lord of House Haillenarte. A draconian rosary turned up among his belongings, and he fears many will take it as proof of heresy, though his former servant swears he is no heretic. "
     "He sent you with a letter to Lord Haurchefant.",
     ["E115a", "E116b", "E116a", "E116d"]),
   P(Q118, Q120, "main", "Francel",
     "A lord of House Haillenarte suspected of heresy over a draconian rosary found among his belongings. You saved him at the Steel Vigil, where he hoped to prove his devotion, "
     "and his trial approaches.",
     ["E115a", "E118a", "E118b"]),
   P(Q120, None, "main", "Francel",
     "A lord of House Haillenarte tried for heresy over a draconian rosary found among his belongings. At Witchdrop, Inquisitor Guillaime ordered him to prove his innocence by leaping from the cliff. "
     "You protected him, and the charges were withdrawn pending investigation.",
     ["E115a", "E120a", "E120b", "E120d"]),
 ]),
 ("char-haurchefant", "character", [
   P(Q116, Q118, "main", "Haurchefant",
     "A lord of House Fortemps who commands the garrison at Camp Dragonhead. Lord Francel sent you to him, and he has promised to make inquiries for you.",
     ["E116c", "E116d", "E116e"]),
   P(Q118, Q120, "main", "Haurchefant",
     "A lord of House Fortemps who commands the garrison at Camp Dragonhead. He has found a witness to the Enterprise's flight, but first means to clear Lord Francel's name, and yours with it.",
     ["E116c", "E118c", "E118d"]),
   P(Q120, Q121, "main", "Haurchefant",
     "A lord of House Fortemps who commands the garrison at Camp Dragonhead. He believes the rosaries against Lord Francel were planted, and at the trial argued that someone was using the trials to set the houses against each other.",
     ["E116c", "E119a", "E120e"]),
   P(Q121, None, "main", "Haurchefant",
     "A lord of House Fortemps who commands the garrison at Camp Dragonhead. He defended Lord Francel at his heresy trial, and wrote to Lord Drillemont of Whitebrim Front asking that you be let into the Stone Vigil.",
     ["E116c", "E120e", "E121c"]),
 ]),
 ("char-guillaime", "character", [
   P(Q113, Q117, "main", "Guillaime",
     "An Ishgardian inquisitor who subtly warned you to stay out of Ishgard's affairs.",
     ["E113c"], ["Inquisitor Guillaime"]),
   P(Q117, Q120, "main", "Guillaime",
     "An Ishgardian inquisitor who warned you to stay out of Ishgard's affairs. Since he arrived in Coerthas, countless heretics have been found, even among Ishgard's elite.",
     ["E113c", "E117a"], ["Inquisitor Guillaime"]),
   P(Q120, Q122, "main", "Guillaime",
     "An Ishgardian inquisitor under whom countless heretics have been found. He tried Lord Francel at Witchdrop and ordered him to leap from the cliff to prove his innocence, "
     "then withdrew the charges pending investigation.",
     ["E117a", "E120a", "E120b", "E120d"], ["Inquisitor Guillaime"]),
   P(Q122, Q124, "main", "Guillaime",
     "An Ishgardian inquisitor under whom countless heretics have been found. At Whitebrim Front he branded you untrustworthy and the Scions a defunct band the Empire had exterminated, "
     "and insists you must not reach the Stone Vigil.",
     ["E117a", "E122c", "E122d"], ["Inquisitor Guillaime"]),
   P(Q124, Q126, "main", "Guillaime",
     "An Ishgardian inquisitor under whom countless heretics have been found. He insists you must not reach the Stone Vigil, warned the chirurgeons that your gifts serve an unknown end, "
     "and seems to hate you and your companions.",
     ["E117a", "E122d", "E124c", "E124d"], ["Inquisitor Guillaime"]),
   P(Q126, Q127, "main", "The false Guillaime",
     "An impostor posing as Inquisitor Guillaime. The real inquisitor was murdered on the day he arrived in Coerthas. "
     "The impostor has worked to keep you from the Stone Vigil, and his true identity and motives are unknown.",
     ["E126b", "E126c", "E126d", "E122d"], ["Guillaime", "Inquisitor Guillaime"]),
   P(Q127, Q128, "main", "The false Guillaime",
     "An impostor posing as Inquisitor Guillaime, whose namesake was murdered on arriving in Coerthas. He coerced Prunilla with threats against her loved ones, "
     "and condemned innocent people for carrying draconian rosaries. His true identity is unknown.",
     ["E126b", "E126c", "E127a", "E127b", "E126d"], ["Guillaime", "Inquisitor Guillaime"]),
   P(Q128, None, "main", "The false Guillaime",
     "An impostor who posed as Inquisitor Guillaime after the real inquisitor was murdered. Unmasked at Snowcloak, he called all Ishgard complicit in the archbishop's lies, "
     "summoned his Dravanian allies and took the form of a dragon, and you defeated him.",
     ["E126c", "E128a", "E128b", "E128c", "E128f"], ["Guillaime", "Inquisitor Guillaime"]),
 ]),
 ("char-drillemont", "character", [
   P(Q121, Q122, "main", "Drillemont",
     "Lord of Whitebrim Front, whose leave you need to enter the Stone Vigil. Lord Haurchefant has written to him on your behalf.",
     ["E121c"]),
   P(Q122, Q127, "main", "Drillemont",
     "Lord of Whitebrim Front. He was astonished to find Cid alive, but bars you from the Stone Vigil until it is retaken and you declare your true intentions.",
     ["E121c", "E122b", "E122e"]),
   P(Q127, Q128, "main", "Drillemont",
     "Lord of Whitebrim Front. Convinced that the inquisitor who opposed you is a heretic, he will let you into the Stone Vigil once the impostor is brought to justice.",
     ["E122b", "E127d", "E127e"]),
   P(Q128, None, "main", "Drillemont",
     "Lord of Whitebrim Front. He confronted the false inquisitor at Snowcloak, naming him the murderer of Inquisitor Guillaime, and opened the way to the Stone Vigil and your airship.",
     ["E127e", "E128a", "E128e"]),
 ]),
 ("char-biggs", "character", [
   P(Q143, Q145, "main", "Biggs",
     "One of two men, likely Biggs and Wedge, who escaped from a downed imperial airship in Coerthas and are being hunted.",
     ["E143c"]),
   P(Q145, Q147, "main", "Biggs",
     "One of two escapees from a downed imperial airship in Coerthas. He drew the pursuers away from Wedge and was last seen heading west. Cid says he has always looked after Wedge.",
     ["E143c", "E145a", "E145b", "E145d"]),
   P(Q147, Q153, "main", "Biggs",
     "A member of Cid's Ironworks crew. The imperials took him and Wedge from the Waking Sands to Castrum Centri, and they escaped by sabotaging an airship. "
     "Yda and Y'shtola helped you rescue him from imperial troops.",
     ["E147e", "E147c", "E147d", "E147a"]),
   P(Q153, None, "main", "Biggs",
     "A member of Cid's Ironworks crew who escaped from Castrum Centri. He is to go back in with Wedge and you, disguised as imperial soldiers, and he and Wedge repaired the magitek reaper you seized.",
     ["E147e", "E147c", "E151a", "E153c"]),
 ]),
 ("char-wedge", "character", [
   P(Q143, Q145, "main", "Wedge",
     "One of two men, likely Biggs and Wedge, who escaped from a downed imperial airship in Coerthas and are being hunted.",
     ["E143c"]),
   P(Q145, Q147, "main", "Wedge",
     "One of two escapees from a downed imperial airship in Coerthas. You found him hiding under a bridge after Biggs drew off their pursuers, and he was overjoyed to find Cid alive.",
     ["E143c", "E145a", "E145c"]),
   P(Q147, Q153, "main", "Wedge",
     "A member of Cid's Ironworks crew. The imperials took him and Biggs from the Waking Sands to Castrum Centri, and they escaped by sabotaging an airship.",
     ["E147e", "E147c", "E147d"]),
   P(Q153, None, "main", "Wedge",
     "A member of Cid's Ironworks crew who escaped from Castrum Centri. He is to go back in with Biggs and you, disguised as imperial soldiers, and he and Biggs repaired the magitek reaper you seized.",
     ["E147e", "E147c", "E151a", "E153c"]),
 ]),
 ("char-glaumunt", "character", [
   P(Q148, Q149, "main", "Glaumunt",
     "A man at Revenant's Toll with a personal grudge against the Empire, who knows a great deal about Castrum Centri. He has agreed to help you get inside.",
     ["E148c", "E148e"]),
   P(Q149, Q153, "main", "Glaumunt",
     "A man at Revenant's Toll with a grudge against the Empire, who knows a great deal about Castrum Centri. He showed you a drainage pipe for listening in on the castrum, "
     "and is seeking a suit of magitek armor for the infiltration.",
     ["E148c", "E149e", "E149d"]),
   P(Q153, None, "main", "Glaumunt",
     "A man at Revenant's Toll with a grudge against the Empire, who knows a great deal about Castrum Centri. He planned your disguise, and fed the imperials false word of insurgents so you could seize a magitek reaper.",
     ["E148c", "E150c", "E153a", "E153b"]),
 ]),
 # ---- Organizations and places ----
 ("org-company-of-heroes", "organization", [
   P(Q103, Q105, "main", "The Company of Heroes",
     "A disbanded company whose five chosen members judged you worthy to challenge Titan, weighing you by deeds rather than reputation.",
     ["E103f", "E103b", "E103c"]),
   P(Q105, None, "main", "The Company of Heroes",
     "A disbanded company whose five chosen members judged you worthy to challenge Titan. Riol, another former member, revealed that the Company once reached Titan through a beastman aetheryte.",
     ["E103f", "E103b", "E104a", "E105a"]),
 ]),
 ("org-garlean-empire", "organization", [
   P(Q102, Q105, "main", "The Garlean Empire",
     "An empire that conquers other lands, and has tried to conquer Eorzea.",
     ["E100a"], ["the Empire"]),
   P(Q105, Q106, "main", "The Garlean Empire",
     "An empire that conquers other lands, and has tried to conquer Eorzea. After Titan fell, its officers appeared at the Navel with a figure called Lahabrea, "
     "and Y'shtola is troubled that the Ascians would consort with the Empire.",
     ["E100a", "E105d", "K14"], ["the Empire"]),
   P(Q106, Q141, "main", "The Garlean Empire",
     "An empire that conquers other lands, and has tried to conquer Eorzea. Its forces, led by Livia, raided the Waking Sands, slaughtered many Scions and took prisoners, Minfilia among them.",
     ["E100a", "E106b", "K01"], ["the Empire"]),
   P(Q141, None, "main", "The Garlean Empire",
     "An empire that has tried to conquer Eorzea. Its forces under Livia raided the Waking Sands and took the Scions' leader prisoner, and at the Howling Eye Gaius, the Black Wolf, "
     "called forth a weapon that seemingly absorbed three primals.",
     ["E100a", "K01", "K10", "K11"], ["the Empire"]),
 ]),
 ("org-house-haillenarte", "organization", [
   P(Q115, Q117, "main", "House Haillenarte",
     "One of Ishgard's High Houses, whispered to be full of heretics. A draconian rosary turned up in a chest belonging to its Lord Francel.",
     ["E115a", "E115b"]),
   P(Q117, Q119, "main", "House Haillenarte",
     "One of Ishgard's High Houses, whispered to be full of heretics. Accusations of heresy against its Lord Francel have thrown the house into chaos.",
     ["E115a", "E115b", "E117b"]),
   P(Q119, Q121, "main", "House Haillenarte",
     "One of Ishgard's High Houses, accused of harboring heretics. Draconian rosaries planted in shipments to Skyfire Locks look like a crude attempt to smear the house.",
     ["E115b", "E119b", "E119c"]),
   P(Q121, Q127, "main", "House Haillenarte",
     "One of Ishgard's High Houses, accused of harboring heretics. Its Lord Francel was cleared of heresy at his trial, but those who tried to destroy the house are still unknown.",
     ["E115b", "E120d", "E121d"]),
   P(Q127, None, "main", "House Haillenarte",
     "One of Ishgard's High Houses, accused of harboring heretics. Its Lord Francel was cleared of heresy at his trial, and Prunilla has confessed that she planted rosaries from the false inquisitor's chest in shipments to Skyfire Locks.",
     ["E115b", "E120d", "E127c"]),
 ]),
 ("org-ixal", "organization", [
   P(Q110, Q141, "main", "The Ixal",
     "A beast tribe that has summoned the primal Garuda.",
     ["E110e"]),
   P(Q141, None, "main", "The Ixal",
     "A beast tribe that summoned the primal Garuda. When you struck her down at the Howling Eye, their belief raised her again.",
     ["E110e", "E141c"]),
 ]),
 ("loc-castrum-centri", "location", [
   P(Q142, Q143, "main", "Castrum Centri",
     "An imperial stronghold in Mor Dhona, where the Scions captured in the raid on the Waking Sands are held.",
     ["E142d"]),
   P(Q143, Q148, "main", "Castrum Centri",
     "An imperial stronghold in Mor Dhona. Scouts saw four prisoners matching Minfilia, Urianger, Papalymo and Tataru led inside.",
     ["E142d", "E143b"]),
   P(Q148, Q155, "main", "Castrum Centri",
     "An imperial stronghold in Mor Dhona, where Minfilia, Urianger, Papalymo and Tataru are held. It is on such high alert that you must go in disguised as imperial troops.",
     ["E142d", "E143b", "E148b", "E148a"]),
   P(Q155, None, "main", "Castrum Centri",
     "An imperial stronghold in Mor Dhona where the captured Scions were held, until a rescue freed them from its storage tower.",
     ["E142d", "K20"]),
 ]),
]

# ---- Relationship types and relationships -------------------------------------------------------------------------
TYPES = [
 ("aids", "aids", "aided by", False),
 ("opposes", "opposes", "opposed by", False),
 ("summoned-by", "summoned by", "summoned", False),
 ("allied-with", "allied with", "allied with", True),
 ("revealed-as", "revealed as", "formerly known as", False),
 ("held-at", "held at", "holds", False),
]

# (id, source, type, target, from, until, scope, claims, review-sheet label[, end claims]). Backfills repeat an
# existing triple for the steps before it, ending exactly where the accepted record begins, so nothing "changes".
RELS = [
 # Backfills
 ("rel-minfilia-leads-scions-arr", "char-minfilia", "leads", "org-scions", Q102, Q154, "main", ["C01"], "R24"),
 ("rel-thancred-member-scions-arr", "char-thancred", "member-of", "org-scions", Q102, Q154, "main", ["C31"], "R25"),
 ("rel-yshtola-member-scions-arr", "char-yshtola", "member-of", "org-scions", Q102, A, "main", ["C31", "C40"], "R26"),
 ("rel-urianger-member-scions-arr", "char-urianger", "member-of", "org-scions", Q102, A, "main", ["C31"], "R27"),
 ("rel-tataru-member-scions-arr", "char-tataru", "member-of", "org-scions", Q102, A, "main", ["C32"], "R28"),
 ("rel-alphinaud-member-scions-arr", "char-alphinaud", "member-of", "org-scions", Q110, Q154, "main", ["C25"], "R29"),
 ("rel-scions-hq-waking-sands-arr", "org-scions", "headquartered-at", "loc-waking-sands", Q102, A, "main", ["C02"], "R30"),
 ("rel-minfilia-prisoner-livia-arr", "char-minfilia", "prisoner-of", "char-livia", Q106, Q154, "main", ["K01", "E106d"], "R31"),
 # New
 ("rel-yda-member-scions", "char-yda", "member-of", "org-scions", Q102, None, "main", ["C31"], "R32"),
 ("rel-papalymo-member-scions", "char-papalymo", "member-of", "org-scions", Q102, None, "main", ["C31"], "R33"),
 ("rel-lahabrea-allied-empire", "char-lahabrea", "allied-with", "org-garlean-empire", Q105, None, "main", ["K14"], "R34"),
 ("rel-livia-member-empire", "char-livia", "member-of", "org-garlean-empire", Q106, Q160, "main", ["K01", "E106b"], "R35", ["K62"]),
 ("rel-iliud-aids-scions", "char-iliud", "aids", "org-scions", Q106, None, "main", ["E106f"], "R36"),
 ("rel-marques-revealed-cid", "char-marques", "revealed-as", "char-cid", Q110, None, "main", ["E110c"], "R37"),
 ("rel-garuda-summoned-ixal", "char-garuda", "summoned-by", "org-ixal", Q110, None, "main", ["E110e"], "R38"),
 ("rel-francel-member-haillenarte", "char-francel", "member-of", "org-house-haillenarte", Q115, None, "main", ["E115a"], "R39"),
 ("rel-haurchefant-aids-francel", "char-haurchefant", "aids", "char-francel", Q118, None, "main", ["E118d"], "R40"),
 ("rel-guillaime-opposes-alphinaud", "char-guillaime", "opposes", "char-alphinaud", Q122, Q128, "main", ["E122d", "E122c"], "R41", ["E128f"]),
 ("rel-drillemont-aids-alphinaud", "char-drillemont", "aids", "char-alphinaud", Q127, None, "main", ["E127e"], "R42"),
 ("rel-gaius-member-empire", "char-gaius", "member-of", "org-garlean-empire", Q141, A, "main", ["K10"], "R43"),
 ("rel-minfilia-held-castrum-centri", "char-minfilia", "held-at", "loc-castrum-centri", Q142, Q155, "main", ["E142d"], "R44", ["K20"]),
 ("rel-urianger-held-castrum-centri", "char-urianger", "held-at", "loc-castrum-centri", Q143, Q155, "main", ["E143b"], "R45", ["K20"]),
 ("rel-papalymo-held-castrum-centri", "char-papalymo", "held-at", "loc-castrum-centri", Q143, Q155, "main", ["E143b"], "R46", ["K20"]),
 ("rel-tataru-held-castrum-centri", "char-tataru", "held-at", "loc-castrum-centri", Q143, Q155, "main", ["E143b"], "R47", ["K20"]),
 ("rel-rhitahtyn-serves-gaius", "char-rhitahtyn", "serves", "char-gaius", Q143, Q157, "main", ["E143e"], "R48", ["K42"]),
 ("rel-biggs-serves-cid", "char-biggs", "serves", "char-cid", Q147, None, "main", ["E147e"], "R49"),
 ("rel-wedge-serves-cid", "char-wedge", "serves", "char-cid", Q147, None, "main", ["E147e"], "R50"),
 ("rel-glaumunt-aids-scions", "char-glaumunt", "aids", "org-scions", Q148, None, "main", ["E148c", "E148e"], "R51"),
]

# Arc casts: each member's participant-in edge to its arc entry, from the step it enters the arc. They never end.
CASTS = {
 ARC_TITAN: [("char-yshtola", Q103, ["E103d"]), ("org-company-of-heroes", Q103, ["E103b"]), ("char-titan", Q103, ["E103b"]),
             ("char-rhitahtyn", Q105, ["E105d"]), ("char-lahabrea", Q105, ["E105e"]), ("org-garlean-empire", Q105, ["K14"])],
 ARC_RAID: [("char-minfilia", Q106, ["K01"]), ("org-scions", Q106, ["E106b"]), ("loc-waking-sands", Q106, ["E106b"]),
            ("char-livia", Q106, ["K01"]), ("org-garlean-empire", Q106, ["E106b"]), ("char-noraxia", Q106, ["E106e"]),
            ("char-iliud", Q106, ["E106f"]), ("char-marques", Q106, ["E106g"]), ("char-alphinaud", Q110, ["E110c"]),
            ("char-cid", Q110, ["E110c"])],
 ARC_ENTERPRISE: [("char-alphinaud", Q110, ["E110c"]), ("char-cid", Q110, ["E110d"]), ("char-garuda", Q110, ["E110e"]),
                  ("org-ixal", Q110, ["E110e"]), ("char-guillaime", Q113, ["E113c"]), ("char-francel", Q115, ["E115a"]),
                  ("org-house-haillenarte", Q115, ["E115a"]), ("char-haurchefant", Q116, ["E116e"]),
                  ("char-drillemont", Q121, ["E121c"]), ("char-lahabrea", Q129, ["E129b"])],
 ARC_BARRIER: [("char-cid", Q130, ["E130b"]), ("char-alphinaud", Q130, ["E130e"]), ("char-garuda", Q130, ["E130a"]),
               ("org-ixal", Q141, ["E141c"]), ("char-titan", Q141, ["E141d"]), ("char-gaius", Q141, ["K11"]),
               ("org-garlean-empire", Q141, ["E141e"]), ("org-scions", Q141, ["E141f"])],
 ARC_RESCUE: [("char-alphinaud", Q142, ["E142a"]), ("char-cid", Q142, ["E142a"]), ("char-yda", Q142, ["E142b"]),
              ("char-yshtola", Q142, ["E142d"]), ("char-minfilia", Q142, ["E142d"]), ("org-scions", Q142, ["K16"]),
              ("loc-castrum-centri", Q142, ["E142d"]), ("char-biggs", Q143, ["E143c"]), ("char-wedge", Q143, ["E143c"]),
              ("char-glaumunt", Q148, ["E148c"])],
}

# Arcs, in authored order: (arc id, entry, first step, last step).
ARCS = [
 ("arc-b1-road-to-titan", ARC_TITAN, Q103, Q105),
 ("arc-b2-fall-of-the-waking-sands", ARC_RAID, Q106, Q110),
 ("arc-b3-search-for-the-enterprise", ARC_ENTERPRISE, Q110, Q129),
 ("arc-b4-garudas-barrier", ARC_BARRIER, Q130, Q141),
 ("arc-b5-road-to-castrum-centri", ARC_RESCUE, Q142, Q154),
]
ARC_NOTES = {
 "arc-b1-road-to-titan": "MSQ #103 *In the Company of Heroes* to #105 *Lord of Crags*, with #102 as the baseline (the first timeline step). "
   "The Company of Heroes' test, Riol's secret and Titan's fall, ending with the first sight of Lahabrea beside imperial officers (E105e, K14). "
   "The Titan storyline starts before #102; the Atlas does not cover those quests.",
 "arc-b2-fall-of-the-waking-sands": "MSQ #106 *All Good Things* to #110 *Eyes on Me*. The raid, Minfilia's capture and the church's sanctuary (E106b, K01), "
   "ending when Alphinaud names Marques as Cid (E110c). It shares #110 with the next arc, so overlapping arcs are proven in real content: "
   "at #110 the default is this arc (earliest started), and the picker offers both.",
 "arc-b3-search-for-the-enterprise": "MSQ #110 *Eyes on Me* to #129 *In Pursuit of the Past*: the hunt for Cid's airship through Coerthas and Ishgard's heresy "
   "crisis, ending when the Enterprise is found in the Stone Vigil (E129d). 20 steps.",
 "arc-b4-garudas-barrier": "MSQ #130 *Into the Eye of the Storm* to #141 *Lady of the Vortex*: the corrupted-crystal hunt and Garuda, ending when the Empire's "
   "weapon absorbs the primals and the Scions resolve to re-form (K11, E141f). Its name avoids #141's title, which may not appear before #141.",
 "arc-b5-road-to-castrum-centri": "MSQ #142 *Reclamation* to #154 *Every Little Thing She Does Is Magitek*, including both #150 paths: rebuilding the Scions, "
   "finding Biggs and Wedge, and preparing the infiltration, ending when the armor is ready (K09). It stops before #155 so that the accepted "
   "Black Wolf's Challenge stays the default arc at #155 (see the discovery doc for the trade-off).",
}
