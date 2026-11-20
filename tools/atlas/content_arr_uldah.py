"""Atlas content for A Realm Reborn 2.0, the Ul'dah starting-city chain: MSQ #1 Close to Home (Ul'dah) to #24 Call of
the Sea (Ul'dah) (steps cp-msq-1c … cp-msq-22c, cp-msq-23b, cp-msq-24). Era tag s.

Data only, per docs/atlas/era-modules.md. Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes
A05–A07); every locator is an exact substring of the quest's saved page (Journal, Steps or main dialogue).

The three starting cities are mutually exclusive in game and run one after another in the timeline, so a Gridania or
Limsa starter also sees these records later on. Arc recaps may say "you"; the presentations of entities that other
chains and later eras share (Ul'dah, Thancred, Nanamo, Raubahn, Lolorito, the Syndicate, the Immortal Flames, the
Alliance, its leaders, Gaius and the Empire, the Ascians, Baderon) state facts about the entity instead.

Spoiler handling:
  - first names only (Nanamo, Raubahn, Merlwyb, Kan-E-Senna, Gaius); no "Ul Namo", "Aldynn", "Bloefhiswyn" or
    "Baelsar" in displayed text, and Nero stays out entirely;
  - the sultana's feast is a "feast" ("banquet" is reserved for 2.55);
  - the voice in the Carteneau vision is not named (the page tags it "???"), nor is the masked mage;
  - the Scions are not named: the chain only hints at them before #30, whose title is their name.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

U = {n: f"cp-msq-{n}c" for n in range(1, 23)}
U[23] = "cp-msq-23b"   # The Ul'dahn Envoy
U[24] = "cp-msq-24"    # Call of the Sea (Ul'dah)
SULTANA = ["the sultana", "Sultana Nanamo"]
GENERAL = ["General Raubahn"]
EMPIRE = ["the Empire"]

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #1 Close to Home (Ul'dah)
 "M1ca": ("Momodi, proprietress of the Quicksand, sets you three tasks to learn the basics of adventuring.", "Close to Home (Ul'dah)", "[[Momodi]], the proprietress of [[the Quicksand]], wants you to perform three tasks that will help you learn the fundamentals of [[adventurer|adventuring]]."),
 "M1cb": ("The Sapphire Avenue Exchange is the sultanate's busiest and most profitable market.", "Close to Home (Ul'dah)", "You stand in the Sapphire Avenue Exchange, the busiest and most profitable marketplace in the sultanate."),
 "M1cc": ("Countless companies and consortia have made Ul'dah their base.", "Close to Home (Ul'dah)", "Because of this, countless companies and consortia have chosen Ul'dah as their base of operations."),
 "M1cd": ("Momodi tells you to explore with a purpose.", "Close to Home (Ul'dah)", "So when you go explorin', explore like you've got a purpose, eh?"),
 # #2 We Must Rebuild
 "M2ca": ("Momodi sends you to Papashan, who may have work for a new adventurer.", "We Must Rebuild", "According to Momodi, a [[Lalafell]] named [[Papashan]] may have some work for a burgeoning [[adventurer]]."),
 "M2cb": ("Papashan is stationmaster of the Ul'dah Dispatch Yard.", "We Must Rebuild", "I am Papashan, stationmaster of this humble Dispatch Yard."),
 "M2cc": ("Five years after the Calamity, its devastation was vast.", "We Must Rebuild", "Twelve know there have been plenty of both these last five years since the Calamity struck. The devastation...was vast."),
 "M2cd": ("Isolated places beyond the lines of supply still want for relief.", "We Must Rebuild", "Isolated areas beyond our lines of supply remain, and there are places yet wanting for relief and restoration."),
 "M2ce": ("Papashan has work suited to your ability.", "We Must Rebuild", "I do believe I may have some work suited to one of your ability."),
 "M2cf": ("Momodi warns of the dangers beyond the city wall.", "We Must Rebuild", "There's dangers beyond the wall, though. More than I'd care to count."),
 # #3 Nothing to See Here
 "M3ca": ("Papashan sends you with twilight pretzels to the Sultansworn sentries posted to guard the area.", "Nothing to See Here", "It isn't much, but go and give them these twilight pretzels, would you?"),
 "M3cb": ("Sentries have been sent to guard the Dispatch Yard's area.", "Nothing to See Here", "It just so happens a number of sentries have been sent to guard the area."),
 "M3cc": ("Papashan seems to have something else on his mind.", "Nothing to See Here", "While Papashan is grateful for your assistance, there appears to be something else on his mind."),
 "M3cd": ("The sentries' empty report alarms Papashan.", "Nothing to See Here", "What? Nothing? Are you sure? I...oh, oh dear."),
 "M3ce": ("Papashan asks you to stay, for he has more to ask of you.", "Nothing to See Here", "And stay a moment─there is more I would ask of you."),
 # #4 Underneath the Sultantree
 "M4ca": ("Papashan and the Sultansworn are searching for Lady Lilira, a young noblewoman who ran away from home.", "Underneath the Sultantree", "The stationmaster explains that he and the [[Sultansworn]] are in fact searching for Lady [[Lilira]], a young noblewoman who has run away from home."),
 "M4cb": ("Papashan's errand to the sentries was a cover for the search.", "Underneath the Sultantree", "Which is the ''real'' reason I sent you to meet those Sultansworn."),
 "M4cc": ("Papashan keeps the search quiet, fearing others with less honorable motives would join the hunt.", "Underneath the Sultantree", "should word of her disappearance spread, I fear others with less honorable motives may join the hunt."),
 "M4cd": ("At the Sultantree voidsent attack, and you and a stranger protect Lilira together.", "Underneath the Sultantree", "Moments later, voidsent attack, forcing you to work together to protect Lady Lilira."),
 "M4ce": ("A vision says the power to banish the Darkness lies in the Crystals of Light, and bids you claim them.", "Underneath the Sultantree", "The power to banish the Darkness dwelleth in the Crystals of Light. Journey forth, and lay claim to them."),
 "M4cf": ("The stranger blames an aetheric disturbance, as though the dead were watching.", "Underneath the Sultantree", "It isn't safe for anyone─not with this aetheric disturbance... It's as though the dead are watching us..."),
 "M4cg": ("Papashan names the stranger as Thancred, a scholar researching the aether.", "Underneath the Sultantree", "Papashan explains that the young man was most likely [[Thancred]], a scholar conducting research on aether-related subjects."),
 "M4ch": ("Lilira promises not to travel unescorted again.", "Underneath the Sultantree", "I shall refrain from traveling unescorted in future."),
 # #5 Step Nine
 "M5ca": ("Cicidoa sends a pumpkin to Roger at the Coffer & Coffin to repay a debt of gratitude.", "Step Nine", "To repay a debt of gratitude, Cicidoa wishes to give [[Roger]] a [[Plantation Pumpkin|pumpkin]], which he has purchased from [[the Royal Plantations]]."),
 "M5cb": ("Cicidoa is waiting on a late shipment from the Nanawa Mines.", "Step Nine", "the scheduled shipment from the Nanawa Mines, for which I wait, is late."),
 # #6 Prudence at This Junction
 "M6ca": ("Roger sends you to Warin of the Stone Torches, who needs help.", "Prudence at This Junction", "He suggests that you speak with [[Warin]] of the [[Stone Torches]], who is in need of assistance of some description."),
 "M6cb": ("The Stone Torches are sellswords hired by Amajina & Sons Mineral Concern.", "Prudence at This Junction", "We Stone Torches are sellswords hired by Amajina & Sons Mineral Concern to protect its interests."),
 "M6cc": ("The Stone Torches keep the tracks clear of pests.", "Prudence at This Junction", "Our primary duty here is to keep the tracks clear of pests, and it is for this purpose that we require your aid."),
 # #7 Out of House and Home
 "M7ca": ("Warin wants the coblyns that attack ore wagons exterminated.", "Out of House and Home", "[[Warin]] has work for an [[adventurer]] willing to exterminate the [[Silver Coblyn|coblyns]] attacking ore wagons."),
 "M7cb": ("You purge the tunnel of coblyns, securing future shipments.", "Out of House and Home", "You have purged the tunnel of coblyn presence, thus ensuring the security of future shipments."),
 "M7cc": ("Disrupted ore shipments threaten Ul'dah itself.", "Out of House and Home", "Disruptions to ore shipments threaten not only the interests of Amajina & Sons Mineral Concern, but of Ul'dah herself."),
 "M7cd": ("Warin likens the tracks to veins bearing the nation's lifeblood.", "Out of House and Home", "One might liken these train tracks to veins that bear our nation's lifeblood."),
 # #8 Way Down in the Hole
 "M8ca": ("Wystan, a self-made merchant from Stonesthrow, is moving to claim an ore vein.", "Way Down in the Hole", "And even as we speak, a young upstart─a self-made merchant from ''Stonesthrow'' of all places─is moving to claim it!"),
 "M8cl": ("Rumor says a vast, untapped vein of ore lies beneath the ruins of Sil'dih.", "Way Down in the Hole", "Rumor has it that there is a vast, untapped vein of ore beneath the ruins of Sil'dih."),
 "M8cb": ("Lolorito has long lavished gil on the thaumaturges, and some claim he devises laws to ruin his competitors.", "Way Down in the Hole", "He has long lavished gil upon the thaumaturges, and some claim that he devises new laws with the express intention of ruining his competitors while protecting his own interests."),
 "M8cc": ("At the ruins the Brass Blades turn on Wystan, saying no one crosses the Syndicate.", "Way Down in the Hole", "''No one'' crosses the Syndicate!"),
 "M8cd": ("A masked mage looses a clay golem on you, and you slay it just before Thancred arrives.", "Way Down in the Hole", "Your confrontation with the Brass Blades is interrupted by a mysterious masked mage, who unleashes a [[Clay Golem|clay golem]] upon you. In the chaotic battle that ensues, you somehow slay the rampaging construct moments before [[Thancred]] arrives."),
 "M8ce": ("Lolorito marked Wystan for death; the vein, the Brass Blades and the golem were all part of the trap.", "Way Down in the Hole", "Wystan now understands that he has been marked for death by Lord [[Lolorito]]. The ore vein, the Brass Blades, and the golem all appear to have been part of the trap."),
 "M8cf": ("Lolorito owns the Brass Blades.", "Way Down in the Hole", "Lolorito ''owns'' the godsdamned Brass Blades."),
 "M8cg": ("Lolorito chairs a trading company, gives generously to the Order of Nald'thal, and sits on the Syndicate.", "Way Down in the Hole", "''Lord'' Lolorito: chairman of the East Aldenard Trading Company, generous contributor to the Order of Nald'thal, ''and'' member of the Syndicate."),
 "M8ch": ("Thancred calls himself a scholar surveying the flow of aether in Thanalan.", "Way Down in the Hole", "I am Thancred, a humble scholar surveying the flow of aether in Thanalan."),
 "M8ci": ("Thancred warns that Lolorito sanctioned the trap and is not to be trifled with.", "Way Down in the Hole", "The carefully laid trap you dismantled was clearly sanctioned by Lord Lolorito. … Believe me when I tell you that he is not a man to be trifled with."),
 "M8cj": ("Momodi confirms Wystan is finished in Ul'dah, but no one knows your part.", "Way Down in the Hole", "Momodi confirms that Wystan is finished in [[Ul'dah]], but assures you that no one knows of your deeds."),
 "M8ck": ("Thancred's detectors find aetheric disturbances, and you are always in the middle of them.", "Way Down in the Hole", "My colleagues went to great lengths to provide me with the means to detect aetheric disturbances, but every time I find one, you seem to be in the middle of it."),
 # #9 Takin' What They're Givin'
 "M9cc": ("Dadanen has asked Momodi to send him anyone looking for work.", "Takin' What They're Givin'", "And that's why I've asked Momodi to send me any souls looking for work."),
 "M9ca": ("Momodi sends you to Dadanen, a merchant who needs a hand.", "Takin' What They're Givin'", "So happens I know a fella by the name of [[Dadanen]] who needs a hand."),
 "M9cb": ("Horizon is a trading settlement that takes in goods from the port of Vesper Bay.", "Takin' What They're Givin'", "Ours is a trading settlement that sees goods in from the port of Vesper Bay to the west─and trade we do."),
 # #10 Supply and Demands
 "M10ca": ("Dadanen is out of premium product and his latest order is late.", "Supply and Demands", "I'm plumb out of premium product, and my latest order has yet to arrive!"),
 "M10cb": ("Dadanen has heard nothing from his man since he left for Copperbell Mines.", "Supply and Demands", "I've heard nothing since he departed for Copperbell Mines days ago."),
 "M10cc": ("The mines have been closed after an incident in the depths, so Drunken Stag can do nothing.", "Supply and Demands", "Drunken Stag is powerless to act, as the mines have been closed due to an incident in the depths."),
 # #11 Give It to Me Raw
 "M11ca": ("Strange coblyns, hungry only for good stone, drove Drunken Stag off his haul.", "Give It to Me Raw", "Not like any coblyns I'd seen before, and hungry only for the good rocks."),
 "M11cb": ("The coblyns ate most of the haul.", "Give It to Me Raw", "I reckon those coblyns made a meal of the stuff."),
 "M11cc": ("A timely delivery may keep Dadanen from destitution.", "Give It to Me Raw", "a timely delivery to [[Dadanen]] may prevent his impending fall into destitution."),
 # #12 The Perfect Swarm
 "M12ca": ("The Brass Blades pay people to keep the roads clear of sun midges.", "The Perfect Swarm", "It's gotten so bad that the Brass Blades have started paying folks to keep the roads clear."),
 "M12cb": ("Fufulupa thanks you, as the Brass Blades have struggled with the swarms.", "The Perfect Swarm", "The Brass Blades have been struggling to keep them in check, so your assistance is greatly appreciated."),
 "M12cc": ("Fufulupa's letters to Captain Leofric at Lost Hope have gone unanswered.", "The Perfect Swarm", "Captain Leofric is stationed there. Ever since he was transferred, we've exchanged letters, but never before has it taken this long to receive a reply."),
 # #13 Last Letter to Lost Hope
 "M13ca": ("The courier is unharmed, but her chocobo is hurt.", "Last Letter to Lost Hope", "You find the courier unharmed, but her [[chocobo]] did not fare as well."),
 "M13cb": ("Leofric has been demoted, though Fufulupa still calls him Captain.", "Last Letter to Lost Hope", "Despite my demotion, he continues to call me Captain."),
 "M13cc": ("Leofric says everyone at Lost Hope has been forsaken.", "Last Letter to Lost Hope", "All here have been forsaken, adventurer."),
 "M13cd": ("Leofric, a crestfallen Brass Blade, warns you not to linger with Ul'dah's unwanted.", "Last Letter to Lost Hope", "Leofric thanks you for the letter and suggests that you do not linger in Lost Hope, lest you become associated with [[Ul'dah]]'s unwanted. Despite what the crestfallen [[The Brass Blades|Brass Blade]] says"),
 # #14 Heir Today, Gone Tomorrow
 "M14ca": ("Outlaws have taken over the Quiveron Manse.", "Heir Today, Gone Tomorrow", "A band of outlaws has taken up residence at the Quiveron Manse on the ridge to the south."),
 "M14cb": ("Their leader styles himself heir to Eolande Quiveron, a Syndicate member who died in the Calamity.", "Heir Today, Gone Tomorrow", "Their leader has styled himself heir to Eolande Quiveron, the Syndicate member who died in the Calamity."),
 "M14cc": ("The self-styled baron is dead.", "Heir Today, Gone Tomorrow", "[[Baron von Quiveron III Esquire]] is no more."),
 "M14cd": ("Lost Hope suffers despite Ul'dah's prosperity, and Leofric says the Brass Blades of the Rose must look to others.", "Heir Today, Gone Tomorrow", "Leofric thanks you for aiding the people of [[Lost Hope]], who continue to suffer in spite of [[Ul'dah]]'s growing prosperity. Reflecting on his downfall, the captain concludes that [[the Brass Blades of the Rose]] must look to others for guidance."),
 # #15 Passing the Blade
 "M15ca": ("Leofric, too hurt to travel, sends an antique dagger to Fufulupa.", "Passing the Blade", "Leofric wishes to give an antique dagger to [[Fufulupa]], but is in no shape to travel due to his injuries."),
 "M15cb": ("Only a captain of the Brass Blades of the Rose may carry the dagger; Fufulupa keeps it until Leofric reclaims it.", "Passing the Blade", "explaining that only captains of [[the Brass Blades of the Rose]] are permitted to carry it. Nevertheless, he takes it into safekeeping until Leofric comes to reclaim it."),
 "M15cc": ("Fufulupa thinks himself unworthy of the dagger.", "Passing the Blade", "I am not worthy to wield it."),
 # #16 Following Footfalls
 "M16ca": ("Fufulupa's fellow Brass Blades guard thaumaturges surveying the Footfalls.", "Following Footfalls", "[[Fufulupa]] needs you to assist his fellow [[The Brass Blades|Brass Blades]]."),
 "M16cb": ("Thaumaturges from the Ossuary are surveying the Footfalls for ancient relics.", "Following Footfalls", "Thaumaturges from the Ossuary are presently surveying the Footfalls for ancient relics."),
 "M16cc": ("Captain Baldewyn sent only a handful of Brass Blades to guard them.", "Following Footfalls", "But Captain Baldewyn sent only a handful of Brass Blades!"),
 "M16cd": ("Baldewyn said only trusted men would be on the operation.", "Following Footfalls", "I ain't heard nothin' from Cap'n Baldewyn 'bout this. He said trusted men only..."),
 "M16ce": ("Totoruna refuses help: the operation has nothing to do with Fufulupa.", "Following Footfalls", "we've got this under control─an' besides, this operation ain't got nothin' to do with Fufulupa."),
 # #17 Storms on the Horizon
 "M17ca": ("Captain Baldewyn is planning festivities for the thaumaturges.", "Storms on the Horizon", "Captain Baldewyn's plannin' some festivities for the thaumaturges, see, and he wants 'em treated to the finest food and drink."),
 "M17cb": ("The fisherman Raffe reacts nervously to Baldewyn's request.", "Storms on the Horizon", "Raffe's nervous reaction to Captain Baldewyn's request lingers in your mind."),
 # #18 Oh Captain, My Captain
 "M18ca": ("Bandits plan to collect Nashachite stolen from Copperbell Mines.", "Oh Captain, My Captain", "[[Fufulupa]] has accidentally overheard Merilda's tale regarding the bandits and their plans to obtain [[Raw Nashachite|Nashachite]] stolen from [[Copperbell Mines]]."),
 "M18cb": ("Fufulupa's supervising officer is secretly cooperating with the bandits.", "Oh Captain, My Captain", "runs to tell his supervising officer─who, unbeknownst to Fufulupa, is cooperating with the bandits."),
 "M18cc": ("Baldewyn claims to act under Lolorito's authority.", "Oh Captain, My Captain", "I am acting under the authority of Lord Lolorito himself!"),
 "M18cd": ("Quiveron IV says you killed his brother and vows revenge.", "Oh Captain, My Captain", "You killed my brother, and now I'm going to return the favor!"),
 "M18ce": ("Leofric reveals Baldewyn acted without Lolorito's knowledge.", "Oh Captain, My Captain", "Baldewyn was in fact operating without Lord [[Lolorito]]'s knowledge"),
 "M18cf": ("Baldewyn is stripped of rank, and Fufulupa is acting captain of the Horizon garrison.", "Oh Captain, My Captain", "Baldewyn has been stripped of his rank, leaving [[the Brass Blades of the Rose]] without a captain. For now, Fufulupa will serve as acting captain of the Horizon garrison."),
 "M18cg": ("Leofric calls Fufulupa the most honorable man he knows.", "Oh Captain, My Captain", "The Brass Blades of the Rose need a leader with honor, and you're the most honorable man I know."),
 # #19 Secrets and Lies
 "M19ca": ("Fufulupa finds a sealed letter to Sultansworn Owyne among his predecessor's belongings.", "Secrets and Lies", "Fufulupa reveals that he has found a [[Letter to Owyne|sealed letter]] addressed to [[Sultansworn]] [[Owyne]] among his disgraced predecessor's belongings."),
 "M19cb": ("Momodi is a steadfast supporter of the royal family.", "Secrets and Lies", "he bids you deliver the letter to [[Momodi]] of [[the Quicksand]], a steadfast supporter of the royal family."),
 "M19cc": ("Momodi insists Owyne is loyal, but has suspicions about the letter.", "Secrets and Lies", "However, she has her own suspicions regarding the letter..."),
 "M19cd": ("Momodi asks you to swear secrecy before she explains.", "Secrets and Lies", "Listen, [Forename]─I think I know what this is all about, but I need you to swear to keep it quiet."),
 # #20 Duty, Honor, Country
 "M20ca": ("Momodi reveals that the royal crown has been stolen.", "Duty, Honor, Country", "Having sworn you to secrecy, Momodi reveals that the royal crown has been stolen."),
 "M20cb": ("Outsiders think Ul'dah a sultanate ruled by its sultana, but its six wealthiest citizens, the Syndicate, hold the most sway.", "Duty, Honor, Country", "The outside world believes Ul'dah to be a sultanate, ruled by Sultana Nanamo Ul Namo. Truth is, though, it's the six wealthiest citizens that hold the most sway─the Syndicate."),
 "M20cc": ("The sultana keeps the people's support, which the theft could cost her.", "Duty, Honor, Country", "Be that as it may, the sultana's still got the support of the people..."),
 "M20cd": ("Owyne, the Sultansworn who was guarding the crown, decides to pay the thieves' ransom.", "Duty, Honor, Country", "And Owyne...Owyne's the Sultansworn who was charged with guardin' it that night. … Believing there to be no other way, the guilt-ridden Sultansworn decides to give the criminals what they want."),
 "M20ce": ("The crown is the sultana's birthright and marks her as custodian of the Ul legacy.", "Duty, Honor, Country", "The crown symbolizes Her Grace's birthright, and identifies her as the custodian of the Ul legacy."),
 "M20cf": ("The ransom was the Traders' Spurn, which the thieves call the power to raise an army of undying soldiers.", "Duty, Honor, Country", "The power to create an army of undying soldiers─''The Traders' Spurn''!"),
 "M20cg": ("With Papashan and a band of Sultansworn, you defeat the thieves.", "Duty, Honor, Country", "with the aid of [[Papashan]] and a band of Sultansworn, you defeat them."),
 "M20ch": ("Raubahn saw Owyne sneak into the vaults and had him watched.", "Duty, Honor, Country", "The General saw you sneak into the vaults, Owyne. … He suspected something was afoot and ordered us to keep an eye on you."),
 "M20ci": ("With Thancred's help you defeat the masked mage behind the theft, whom the Journal calls an Ascian.", "Duty, Honor, Country", "Soon after, you find yourself alone with the masked mage who orchestrated the theft, and another battle ensues. Fortunately, [[Thancred]] comes to your aid, and together you emerge triumphant. Though the motives of this “[[Ascian]]” remain a mystery, his schemes now lie in ruin."),
 "M20cj": ("Thancred says they long suspected the Bringers of Chaos, whose true name is Ascians.", "Duty, Honor, Country", "We had long suspected the involvement of the Bringers of Chaos─''Ascians'', to give them their true name."),
 "M20cp": ("Thancred says they could not be sure the Ascians were behind the recent disturbances until now.", "Duty, Honor, Country", "But we could not be sure they were responsible for the recent disturbances until now."),
 "M20ck": ("Thancred is a Sharlayan.", "Duty, Honor, Country", "Have we Sharlayans crossed paths with Ascians before? Well, we've certainly─ Wait. I don't recall telling you about my homeland."),
 "M20cl": ("Papashan was a Sultansworn until fifteen years ago, and still protects the sultana outside the gates.", "Duty, Honor, Country", "I was once a Sultansworn, you know, though it's been fifteen years since I put down my sword, and took up the role of stationmaster. … Whenever Her Grace ventures outside the gates, I have the honor of protecting her person."),
 "M20cm": ("Nanamo, seventeenth to rule Ul'dah, thanks you and makes you her guest of honor at a coming feast.", "Duty, Honor, Country", "seventeenth ascendant to the throne of Ul'dah, Her Royal Majesty Nanamo Ul Namo presides! … See to it that our champion is my personal guest at the banquet."),
 "M20cn": ("Raubahn oversees the sultanate's affairs with the sultana's consent.", "Duty, Honor, Country", "With the consent of Her Grace, I oversee the affairs of the sultanate."),
 "M20co": ("The Sultansworn's duty is to serve the sultana.", "Duty, Honor, Country", "It's your duty to serve the sultana, lad─and you'll be doing it for a good while yet!"),
 # #21 A Matter of Tradition
 "M21ca": ("Owyne calls the sultana's personal invitation to an adventurer unprecedented.", "A Matter of Tradition", "For an adventurer to receive a personal invitation from Her Grace is unprecedented!"),
 "M21cb": ("The ceremonial earrings, unique to the occasion, serve as a security measure.", "A Matter of Tradition", "Bein' of a design unique to the occasion, the earrin's serve as a security measure."),
 "M21cd": ("You now have the earrings needed to enter the feast.", "A Matter of Tradition", "You now have the ceremonial earrings needed to gain entry to the banquet."),
 # #22 A Royal Reception
 "M22ca": ("Nanamo presents you to her guests as Ul'dah's champion.", "A Royal Reception", "Honored guests, I give you our champion!"),
 "M22cb": ("Raubahn says children starve in Ul'dah's streets while the rich feast.", "A Royal Reception", "While we gorge ourselves, children starve in the streets."),
 "M22cc": ("Members of the Syndicate who profit from the workers' poverty thwart the sultana at every turn.", "A Royal Reception", "She is thwarted at every turn by those on the Syndicate who derive their wealth from the workers' poverty."),
 "M22cd": ("Raubahn says there is no hope for the masses until the crown is restored to power.", "A Royal Reception", "But there will be no hope for the masses until the crown is restored to power."),
 "M22cf": ("Those heroes were lost at Carteneau five years ago; their names are forgotten, so they are called the Warriors of Light.", "A Royal Reception", "And they stood with us at Carteneau, that fateful day five years ago... … But the names of these heroes come not to our lips. … It is for this reason that we have come to call them the Warriors of Light."),
 "M22ch": ("The tale brings a vision of the last moments of the Battle of Carteneau, and you wake at the Hourglass.", "A Royal Reception", "The tale triggers inside your mind a vision of the final moments of the [[Battle of Carteneau]]. When you subsequently come to your senses, you are surprised to find yourself in a room at [[the Hourglass]], with no idea how you got there."),
 "M22ci": ("The Flame General says there is work to be done, and he would have you do it.", "A Royal Reception", "The Flame General declares that there is work to be done─and that he would have you do it."),
 # #23 The Ul'dahn Envoy
 "M23ba": ("Raubahn makes you his personal envoy to the other two leaders of the Eorzean Alliance.", "The Ul'dahn Envoy", "Appointing you his personal envoy, Raubahn bids you deliver a missive to the other two leaders of the [[Eorzean Alliance]]."),
 "M23bb": ("Raubahn means to mark the fifth anniversary of Carteneau with a memorial service.", "The Ul'dahn Envoy", "And so I mean to mark the fifth anniversary of the Battle of Carteneau with a memorial service honoring the fallen."),
 "M23bc": ("The Eorzean Alliance joins Ul'dah, Gridania and Limsa Lominsa.", "The Ul'dahn Envoy", "In addition to [[Ul'dah]], the Eorzean Alliance encompasses the city–states of [[Gridania]] and [[Limsa Lominsa]]."),
 "M23bd": ("The threat of imperial attack has forced strict limits on airship travel.", "The Ul'dahn Envoy", "The ever-present threat of imperial attack has forced us to impose drastic restrictions out of concern for public safety."),
 "M23be": ("Raubahn bears the seal of the supreme commander of the Immortal Flames.", "The Ul'dahn Envoy", "Verily, this is the seal of the supreme commander of the Immortal Flames."),
 "M23bf": ("In an imperial castrum, the Empire's legatus declares that only Garlean rule can bring order to Eorzea.", "The Ul'dahn Envoy", "Only Garlean rule can bring order to Eorzea. It falls to us to deliver the misguided masses from their ignorance."),
 "M23bg": ("The XIVth Imperial Legion under Legatus Gaius is entrenched in the border regions.", "The Ul'dahn Envoy", "with the [[XIVth Imperial Legion]], led by Legatus [[Gaius van Baelsar]], deeply entrenched in the border regions."),
 "M23bh": ("Merlwyb is Admiral of Limsa Lominsa and commander of its Grand Company.", "The Ul'dahn Envoy", "Admiral of Limsa Lominsa, and commander of the Maelstrom."),
 "M23bi": ("The city-states formed the Grand Companies and remade the Alliance to answer the Empire.", "The Ul'dahn Envoy", "It was in answer to the imperial threat that the city–states formed the Grand Companies, and forged the Eorzean Alliance anew."),
 "M23bj": ("Merlwyb warns that the imperials crowd Eorzea's borders.", "The Ul'dahn Envoy", "Do not imagine that the Empire has forsaken its claim on Eorzea. The imperials crowd our borders, waiting to strike."),
 "M23bk": ("Merlwyb accepts Raubahn's proposal.", "The Ul'dahn Envoy", "Aye, Raubahn has the right of it. I accept his proposal."),
 "M23bl": ("Kan-E-Senna is Elder Seedseer of Gridania and leads its Grand Company.", "The Ul'dahn Envoy", "Elder Seedseer of Gridania, and leader of the Order of the Twin Adder, our nation's Grand Company."),
 "M23bm": ("Kan-E-Senna says none may sleep easy while Gaius breathes Eorzean air.", "The Ul'dahn Envoy", "a man whose ambitions are well known to us. So long as he breathes Eorzean air, none of us may sleep easy."),
 "M23bn": ("The beast tribes still summon their primals.", "The Ul'dahn Envoy", "To add to our woes, the beast tribes continue to summon their primals, whose very existence is a bane upon the land."),
 "M23bo": ("Kan-E-Senna approves the memorial and will hold a service in Gridania.", "The Ul'dahn Envoy", "The Flame General was wise to make his proposal, and I wholeheartedly approve of it. The necessary provisions shall be made for a service here in Gridania."),
 "M23bp": ("Kan-E-Senna says Eorzea must stand united again to weather the gathering storm.", "The Ul'dahn Envoy", "A storm gathers upon the horizon. If we are to weather it, we must needs stand united once more."),
 # #24 Call of the Sea (Ul'dah)
 "M24a": ("Baderon, proprietor of the Drowning Wench in Limsa Lominsa, needs a capable adventurer.", "Call of the Sea (Ul'dah)", "[[Baderon]], the proprietor of [[the Drowning Wench]] in [[Limsa Lominsa]], has need of a capable [[adventurer]]."),
 "M24b": ("A Serpent officer thinks the Flame General's envoy would make a fine candidate.", "Call of the Sea (Ul'dah)", "I know not what the task entails, but I daresay the Flame General's personal envoy would make a fine candidate."),
 "M24c": ("Baderon warns that the job will be dangerous.", "Call of the Sea (Ul'dah)", "Baderon warns you that the job will entail considerable danger."),
}

# ---- Entities this era introduces (shared ones repeat the existing ID, so the module lints on its own) ------------
ARC1, ARC2, ARC3, ARC4 = ("evt-a-newcomer-in-uldah", "evt-ore-and-gil", "evt-the-sultanas-crown", "evt-the-flame-generals-envoy")
ENTITIES = {
 ARC1: "event", ARC2: "event", ARC3: "event", ARC4: "event",
 "loc-uldah": "location", "char-momodi": "character", "char-papashan": "character", "char-lilira": "character",
 "org-sultansworn": "organization", "char-wystan": "character", "org-brass-blades": "organization",
 "char-dadanen": "character", "char-fufulupa": "character", "char-leofric": "character", "char-baldewyn": "character",
 "char-owyne": "character", "char-baderon": "character",
 # already in the Atlas from later eras (or likely from the other starting chains)
 "char-thancred": "character", "char-lolorito": "character", "org-syndicate": "organization",
 "char-nanamo": "character", "char-raubahn": "character", "org-ascians": "organization",
 "org-immortal-flames": "organization", "org-eorzean-alliance": "organization", "char-merlwyb": "character",
 "char-kan-e-senna": "character", "char-gaius": "character", "org-garlean-empire": "organization",
}

N1, N2, N3, N4 = "A Newcomer in Ul'dah", "Ore and Gil", "The Sultana's Crown", "The Flame General's Envoy"
HOR = "In Horizon, a trading settlement in Thanalan, "
CROWN = "Ul'dah's royal crown was stolen, and Owyne, the Sultansworn who guarded it, paid the thieves' ransom. "

PRES = {
 # ---- Arc recaps ----
 ARC1: [
   P(U[1], None, "main", N1,
     "You have arrived in Ul'dah, where countless companies and consortia keep their base. Momodi, proprietress of the Quicksand, set you three tasks to learn the basics of adventuring, "
     "among them a visit to the Sapphire Avenue Exchange, Ul'dah's busiest and most profitable market. Her parting advice: explore with a purpose.",
     ["M1cc", "M1ca", "M1cb", "M1cd"]),
   P(U[2], None, "main", N1,
     "Momodi of the Quicksand sent you beyond Ul'dah's wall, warning of the dangers there, to Papashan, stationmaster of the Ul'dah Dispatch Yard. "
     "Five years after the Calamity, he says, places beyond the lines of supply still want for relief, and he has work suited to your ability.",
     ["M2ca", "M2cf", "M2cb", "M2cc", "M2cd", "M2ce"]),
   P(U[3], None, "main", N1,
     "Papashan, stationmaster of the Ul'dah Dispatch Yard, sent you with twilight pretzels for the Sultansworn sentries posted to guard the area. "
     "Each had nothing to report, and that news alarmed him. Something else is plainly on his mind, and he has asked you to stay, for there is more he would ask of you.",
     ["M2cb", "M3ca", "M3cb", "M3cd", "M3cc", "M3ce"]),
   P(U[4], None, "main", N1,
     "Papashan's errand was a cover: he and the Sultansworn were quietly searching for Lady Lilira, a young noblewoman who ran away from home. "
     "You found her at the Sultantree, where voidsent attacked and a stranger helped you protect her. A vision followed, bidding you claim the Crystals of Light. "
     "Papashan named the stranger as Thancred, a scholar of the aether.",
     ["M4cb", "M4ca", "M4cd", "M4ce", "M4cg"]),
   P(U[5], None, "main", N1,
     "Thancred, a scholar of the aether, helped you protect the runaway Lady Lilira from voidsent at the Sultantree, and a vision bade you claim the Crystals of Light. "
     "Back at work in Thanalan, you carried a pumpkin from Cicidoa, who is waiting on a late shipment from the Nanawa Mines, to Roger of the Coffer & Coffin, settling an old debt of gratitude.",
     ["M4cd", "M4cg", "M4ce", "M5ca", "M5cb"]),
   P(U[6], None, "main", N1,
     "Taking work around Thanalan, you carried a pumpkin to Roger of the Coffer & Coffin, repaying an old debt of gratitude, and Roger sent you on to Warin of the Stone Torches. "
     "They are sellswords hired by Amajina & Sons Mineral Concern, and their main duty is to keep its tracks clear of pests.",
     ["M5ca", "M6ca", "M6cb", "M6cc"]),
   P(U[7], None, "main", N1,
     "For Warin of the Stone Torches, sellswords who guard Amajina & Sons Mineral Concern, you purged a tunnel of the coblyns that were attacking ore wagons. "
     "Disrupted shipments, he says, threaten Ul'dah itself: he likens the tracks to veins that bear the nation's lifeblood.",
     ["M6cb", "M7ca", "M7cb", "M7cc", "M7cd"]),
 ],
 ARC2: [
   P(U[8], None, "main", N2,
     "Wystan, a self-made merchant from Stonesthrow, took Brass Blades along to claim a rumored ore vein under the ruins of Sil'dih, but the vein was a trap set by Lord Lolorito of the Syndicate. "
     "The Brass Blades turned on him, a masked mage loosed a clay golem, and you slew it just before Thancred arrived. Wystan is finished in Ul'dah, but Momodi says no one knows your part.",
     ["M8ca", "M8cl", "M8ce", "M8cc", "M8cd", "M8cj"]),
   P(U[9], None, "main", N2,
     "Lord Lolorito, who owns the Brass Blades and sits on the Syndicate, set a deadly trap for Wystan, a rival merchant, and Wystan is finished in Ul'dah. "
     "Momodi, who keeps your part in it quiet, has sent you to Dadanen, a merchant in Horizon, a trading settlement that takes in goods from Vesper Bay.",
     ["M8cf", "M8cg", "M8ce", "M8cj", "M9ca", "M9cb"]),
   P(U[10], None, "main", N2,
     HOR + "the merchant Dadanen is out of premium stock, and his man Drunken Stag went silent after leaving for Copperbell Mines. "
     "You found him there: the mines are closed after an incident in the depths, and he can do nothing.",
     ["M9cb", "M10ca", "M10cb", "M10cc"]),
   P(U[11], None, "main", N2,
     HOR + "the merchant Dadanen faces ruin for want of stock, because Copperbell Mines closed after an incident in the depths. "
     "Strange coblyns, hungry only for good stone, drove his man Drunken Stag off his haul of Nashachite, and you won back what little they had not eaten.",
     ["M9cb", "M11cc", "M10cc", "M11ca", "M11cb"]),
   P(U[12], None, "main", N2,
     HOR + "the Brass Blades pay for help keeping the roads clear, and you thinned the sun midge swarms for them. "
     "Fufulupa, a Brass Blade there, thanked you and asked you to trace his letter to Captain Leofric at Lost Hope: never before has a reply taken so long.",
     ["M9cb", "M12ca", "M12cb", "M12cc"]),
   P(U[13], None, "main", N2,
     "Carrying Fufulupa's letter from Horizon in place of a courier whose chocobo was hurt, you reached Lost Hope. "
     "There Leofric, a Brass Blade demoted though Fufulupa still calls him Captain, says everyone at Lost Hope has been forsaken, and warned you not to linger with Ul'dah's unwanted.",
     ["M12cc", "M13ca", "M13cb", "M13cc", "M13cd"]),
   P(U[14], None, "main", N2,
     "At Lost Hope, which suffers despite Ul'dah's growing prosperity, the demoted Brass Blade Leofric sent you against outlaws in the Quiveron Manse. "
     "Their leader styled himself heir to Eolande Quiveron, a Syndicate member who died in the Calamity, and he is now dead. Leofric says the Brass Blades of the Rose must look to others.",
     ["M13cb", "M14cd", "M14ca", "M14cb", "M14cc"]),
   P(U[15], None, "main", N2,
     "Leofric of Lost Hope, too hurt to travel, sent an antique dagger to Fufulupa in Horizon by your hand, after saying the Brass Blades of the Rose must look to others. "
     "Only a captain may carry it, and Fufulupa, thinking himself unworthy, keeps it safe until Leofric reclaims it.",
     ["M15ca", "M14cd", "M15cb", "M15cc"]),
   P(U[16], None, "main", N2,
     "Fufulupa, the Horizon Brass Blade who keeps Leofric's captain's dagger, worries for thaumaturges from the Ossuary surveying the Footfalls for relics: Captain Baldewyn sent only a handful of guards. "
     "At the ruins Totoruna turned your help away, saying Baldewyn wants trusted men only, and that the work has nothing to do with Fufulupa.",
     ["M15cb", "M16ca", "M16cb", "M16cc", "M16cd", "M16ce"]),
   P(U[17], None, "main", N2,
     "Captain Baldewyn of Horizon keeps his Footfalls survey to trusted men, and turned away Fufulupa's offer of help. "
     "Now he is planning festivities for the visiting thaumaturges, but Raffe, the fisherman you asked for their fish, was oddly nervous about the captain's request.",
     ["M16cc", "M16cd", "M17ca", "M17cb"]),
   P(U[18], None, "main", N2,
     "Bandits from the Quiveron Manse came to the Footfalls for Nashachite stolen from Copperbell Mines, and their partner was Captain Baldewyn, who claimed Lord Lolorito's authority. "
     "You defeated him and the new self-styled baron, who vowed revenge for his brother. Leofric says Baldewyn acted alone, and Fufulupa is now acting captain.",
     ["M18ca", "M18cb", "M18cc", "M18cd", "M18ce", "M18cf"]),
   P(U[19], None, "main", N2,
     "Captain Baldewyn of Horizon, caught dealing with bandits in stolen Nashachite, has been stripped of his rank, and Fufulupa is acting captain. "
     "Among Baldewyn's papers Fufulupa found a sealed letter to Owyne of the Sultansworn. Momodi swears Owyne is loyal, yet she has her own suspicions, and asked you to swear secrecy.",
     ["M18cf", "M18ca", "M19ca", "M19cc", "M19cd"]),
 ],
 ARC3: [
   P(U[20], None, "main", N3,
     CROWN + "It was the Traders' Spurn, which the thieves called the power to raise an army of undying soldiers. With Papashan and the Sultansworn you beat them, "
     "and Thancred helped you defeat their master, a masked mage called an Ascian. Sultana Nanamo thanked you in person and invited you to her feast as her guest of honor.",
     ["M20ca", "M20cd", "M20cf", "M20cg", "M20ci", "M20cm"]),
   P(U[21], None, "main", N3,
     "With Papashan, Thancred and the Sultansworn, you recovered Ul'dah's stolen crown and defeated the masked mage behind the theft, called an Ascian. "
     "Owyne calls Sultana Nanamo's invitation to her feast unprecedented for an adventurer, and Momodi has entrusted you with the ceremonial earrings that guests must wear to enter.",
     ["M20cg", "M20ci", "M20cm", "M21ca", "M21cb", "M21cd"]),
   P(U[22], None, "main", N3,
     "At her feast, Sultana Nanamo named you Ul'dah's champion. Raubahn spoke of children starving under the Syndicate's grip, and of the Warriors of Light, lost at Carteneau five years ago, "
     "whom you resemble. His tale brought on a vision of that battle's last moments. You woke at the Hourglass, and the Flame General has work for you.",
     ["M22ca", "M22cb", "M22cc", "M22cf", "M22ch", "M22ci"]),
 ],
 ARC4: [
   P(U[23], None, "main", N4,
     "Raubahn made you his envoy to the other leaders of the Eorzean Alliance, proposing a memorial for the fifth anniversary of Carteneau. Admiral Merlwyb of Limsa Lominsa "
     "and Elder Seedseer Kan-E-Senna of Gridania agreed. Both warn that the Empire's XIVth Legion under Gaius is entrenched at Eorzea's borders, and that the beast tribes still summon primals.",
     ["M23ba", "M23bb", "M23bk", "M23bo", "M23bg", "M23bj", "M23bn"]),
   P(U[24], None, "main", N4,
     "As the Flame General's envoy you carried his proposal of a Carteneau memorial to Limsa Lominsa and Gridania, and both leaders agreed. "
     "Now a Serpent officer has sent you on to Baderon, proprietor of the Drowning Wench in Limsa Lominsa, who needs a capable adventurer and warns the job is dangerous.",
     ["M23ba", "M23bk", "M23bo", "M24b", "M24a", "M24c"]),
 ],

 # ---- Places and organizations ----
 "loc-uldah": [
   P(U[1], None, "main", "Ul'dah",
     "A city where countless companies and consortia keep their base. Its Sapphire Avenue Exchange is its busiest and most profitable marketplace.",
     ["M1cc", "M1cb"]),
   P(U[20], None, "main", "Ul'dah",
     "A sultanate in Thanalan whose markets draw countless companies and consortia. The outside world believes it ruled by its sultana, Nanamo, but its six wealthiest citizens, the Syndicate, hold the most sway.",
     ["M1cc", "M20cb"]),
   P(U[23], None, "main", "Ul'dah",
     "A sultanate whose six wealthiest citizens, the Syndicate, hold more sway than its sultana, Nanamo. With Gridania and Limsa Lominsa it makes up the Eorzean Alliance.",
     ["M20cb", "M23bc"]),
 ],
 "org-sultansworn": [
   P(U[3], None, "main", "The Sultansworn",
     "Ul'dah's guards, whose sentries watch over the Ul'dah Dispatch Yard.",
     ["M3ca", "M3cb"]),
   P(U[20], None, "main", "The Sultansworn",
     "The guards sworn to serve Ul'dah's sultana. One of their number, Owyne, lost the royal crown to thieves, and with the former Sultansworn Papashan at their head they won it back.",
     ["M20co", "M20cd", "M20cg", "M20cl"]),
 ],
 "org-brass-blades": [
   P(U[8], None, "main", "The Brass Blades",
     "An armed company of Ul'dah, owned by Lord Lolorito. Brass Blades who joined the merchant Wystan's expedition turned on him at the ruins of Sil'dih, as part of a trap Lolorito had set.",
     ["M8cf", "M8ce", "M8cc"]),
   P(U[12], None, "main", "The Brass Blades",
     "An armed company of Ul'dah, owned by Lord Lolorito, that also keeps Thanalan's roads: in Horizon it pays others to help clear them of pests.",
     ["M8cf", "M12ca", "M12cb"]),
   P(U[18], None, "main", "The Brass Blades",
     "An armed company of Ul'dah, owned by Lord Lolorito, that keeps Thanalan's roads. Its Horizon garrison, the Brass Blades of the Rose, lost its captain, Baldewyn, after he was caught dealing with bandits, and Fufulupa is acting captain.",
     ["M8cf", "M12ca", "M18cb", "M18cf"]),
 ],
 "org-syndicate": [
   P(U[8], None, "main", "The Syndicate",
     "A powerful body of Ul'dah. Lord Lolorito is a member, and Brass Blades who turned on a rival merchant warned that no one crosses the Syndicate.",
     ["M8cg", "M8cc"]),
   P(U[20], None, "main", "The Syndicate",
     "Ul'dah's six wealthiest citizens, who hold more sway in the sultanate than its sultana, Nanamo. Lord Lolorito is a member.",
     ["M20cb", "M8cg"]),
   P(U[22], None, "main", "The Syndicate",
     "Ul'dah's six wealthiest citizens, who hold more sway in the sultanate than its sultana, Nanamo. Raubahn says those among them who profit from the workers' poverty thwart her at every turn, while children starve in the streets.",
     ["M20cb", "M22cc", "M22cb"]),
 ],
 "org-ascians": [
   P(U[20], None, "main", "The Ascians",
     "Also called the Bringers of Chaos. Thancred, a Sharlayan, says his people had long suspected their involvement in recent disturbances, and a masked mage called an Ascian was behind the theft of Ul'dah's royal crown.",
     ["M20cj", "M20cp", "M20ck", "M20ci"], ["the Bringers of Chaos"]),
 ],
 "org-immortal-flames": [
   P(U[23], None, "main", "The Immortal Flames",
     "Ul'dah's Grand Company, whose supreme commander is Raubahn, the Flame General. The city-states formed their Grand Companies in answer to the Empire.",
     ["M23be", "M23bi"]),
 ],
 "org-eorzean-alliance": [
   P(U[23], None, "main", "The Eorzean Alliance",
     "The alliance of Ul'dah, Gridania and Limsa Lominsa, forged anew in answer to the Empire. Raubahn proposed that its nations mark the fifth anniversary of the Battle of Carteneau with a memorial, "
     "and the Admiral and the Elder Seedseer agreed.",
     ["M23bc", "M23bi", "M23bb", "M23bk", "M23bo"]),
 ],
 "org-garlean-empire": [
   P(U[23], None, "main", "The Garlean Empire",
     "An empire that threatens Eorzea. Its XIVth Imperial Legion, led by Legatus Gaius, is entrenched in Eorzea's border regions, and the threat of imperial attack has forced strict limits on airship travel.",
     ["M23bg", "M23bj", "M23bd"], EMPIRE),
 ],

 # ---- People of Ul'dah ----
 "char-momodi": [
   P(U[1], None, "main", "Momodi",
     "Proprietress of the Quicksand in Ul'dah, who sets new adventurers their first tasks.",
     ["M1ca"]),
   P(U[8], None, "main", "Momodi",
     "Proprietress of the Quicksand in Ul'dah, who finds work for adventurers. She keeps quiet the part an adventurer played in surviving Lord Lolorito's trap for the merchant Wystan.",
     ["M1ca", "M8cj", "M8ce"]),
   P(U[19], None, "main", "Momodi",
     "Proprietress of the Quicksand in Ul'dah, who finds work for adventurers, and a steadfast supporter of the royal family. She swears that Owyne of the Sultansworn is loyal, but suspects what his letter means.",
     ["M1ca", "M19cb", "M19cc"]),
 ],
 "char-papashan": [
   P(U[2], None, "main", "Papashan",
     "Stationmaster of the Ul'dah Dispatch Yard, who has work for adventurers in the Calamity's long aftermath.",
     ["M2cb", "M2cd", "M2ce"]),
   P(U[4], None, "main", "Papashan",
     "Stationmaster of the Ul'dah Dispatch Yard. With the Sultansworn he quietly searched for the runaway Lady Lilira, fearing that others with less honorable motives would join the hunt.",
     ["M2cb", "M4ca", "M4cc"]),
   P(U[20], None, "main", "Papashan",
     "Stationmaster of the Ul'dah Dispatch Yard, and a Sultansworn until fifteen years ago; he still protects the sultana outside the gates. "
     "On Raubahn's orders he watched over Owyne, and led the Sultansworn who beat the crown thieves.",
     ["M2cb", "M20cl", "M20ch", "M20cg"]),
 ],
 "char-lilira": [
   P(U[4], None, "main", "Lilira",
     "A young noblewoman of Ul'dah who ran away from home. Found at the Sultantree and kept safe from voidsent, she has promised not to travel unescorted again.",
     ["M4ca", "M4cd", "M4ch"], ["Lady Lilira"]),
 ],
 "char-thancred": [
   P(U[4], None, "main", "Thancred",
     "A scholar who researches the aether, and who helped protect Lady Lilira when voidsent attacked at the Sultantree. He blames an aetheric disturbance.",
     ["M4cg", "M4cd", "M4cf"]),
   P(U[8], None, "main", "Thancred",
     "A scholar surveying the flow of aether in Thanalan, whose colleagues gave him the means to detect aetheric disturbances. "
     "He warns that Lord Lolorito, who sanctioned a deadly trap for the merchant Wystan, is not a man to be trifled with.",
     ["M8ch", "M8ck", "M8ci"]),
   P(U[20], None, "main", "Thancred",
     "A Sharlayan scholar surveying the flow of aether in Thanalan. He helped defeat the masked mage behind the theft of Ul'dah's royal crown, and says he and his fellows had long suspected the Bringers of Chaos, the Ascians.",
     ["M8ch", "M20ck", "M20ci", "M20cj"]),
 ],
 "char-lolorito": [
   P(U[8], None, "main", "Lolorito",
     "A lord of Ul'dah and member of the Syndicate, who chairs a trading company, gives generously to the Order of Nald'thal and owns the Brass Blades. "
     "Some claim he devises laws to ruin his competitors, and he set a deadly trap for the rival merchant Wystan.",
     ["M8cg", "M8cf", "M8cb", "M8ce"], ["Lord Lolorito"]),
 ],
 "char-wystan": [
   P(U[8], None, "main", "Wystan",
     "A self-made merchant from Stonesthrow who tried to claim an ore vein under Sil'dih. The vein was a trap: Lord Lolorito marked him for death, and he is finished in Ul'dah.",
     ["M8ca", "M8ce", "M8cj"]),
 ],
 "char-dadanen": [
   P(U[9], None, "main", "Dadanen",
     "A merchant in Horizon, a trading settlement in Thanalan, who asked Momodi to send him anyone looking for work.",
     ["M9ca", "M9cb", "M9cc"]),
   P(U[11], None, "main", "Dadanen",
     "A merchant in Horizon who ran out of stock when Copperbell Mines closed. A small delivery of Nashachite, most of it eaten by coblyns, may keep him from destitution.",
     ["M10ca", "M10cc", "M11cb", "M11cc"]),
 ],
 "char-fufulupa": [
   P(U[12], None, "main", "Fufulupa",
     "A man of Horizon who thanks those who help the Brass Blades keep its roads clear, and who writes to Captain Leofric at Lost Hope.",
     ["M12cb", "M12cc"]),
   P(U[15], None, "main", "Fufulupa",
     "A man of Horizon, and a friend of Captain Leofric. Leofric sent him the dagger that only a captain of the Brass Blades of the Rose may carry; thinking himself unworthy, he keeps it safe until Leofric reclaims it.",
     ["M12cb", "M15ca", "M15cb", "M15cc"]),
   P(U[18], None, "main", "Fufulupa",
     "Acting captain of the Brass Blades of the Rose, the Horizon garrison, after his captain, Baldewyn, was caught dealing with bandits. Leofric calls him the most honorable man he knows.",
     ["M18cf", "M18cb", "M18cg"]),
 ],
 "char-leofric": [
   P(U[12], None, "main", "Leofric",
     "A captain stationed at Lost Hope since his transfer, who exchanges letters with Fufulupa in Horizon.",
     ["M12cc"]),
   P(U[13], None, "main", "Leofric",
     "A demoted Brass Blade at Lost Hope, though Fufulupa still calls him Captain. He says everyone there has been forsaken.",
     ["M13cb", "M13cc", "M13cd"]),
   P(U[14], None, "main", "Leofric",
     "A demoted Brass Blade at Lost Hope, which suffers despite Ul'dah's growing prosperity. He had the outlaws of the Quiveron Manse dealt with, and says the Brass Blades of the Rose must look to others.",
     ["M13cb", "M14cd", "M14cc"]),
   P(U[18], None, "main", "Leofric",
     "A demoted Brass Blade at Lost Hope, who passed his captain's dagger to Fufulupa as the most honorable man he knows. "
     "He revealed that Captain Baldewyn's dealings with bandits were made without Lord Lolorito's knowledge.",
     ["M13cb", "M18cg", "M18ce"]),
 ],
 "char-baldewyn": [
   P(U[16], None, "main", "Baldewyn",
     "Captain of the Brass Blades in Horizon. He sent only a handful of guards with the thaumaturges surveying the Footfalls, and wants trusted men only on the work.",
     ["M16cc", "M16cd"], ["Captain Baldewyn"]),
   P(U[18], None, "main", "Baldewyn",
     "The former captain of the Brass Blades of the Rose in Horizon. He partnered with bandits dealing in Nashachite stolen from Copperbell Mines, claiming Lord Lolorito's authority, "
     "but acted without Lolorito's knowledge, and has been stripped of his rank.",
     ["M18cb", "M18ca", "M18cc", "M18ce", "M18cf"]),
 ],
 "char-owyne": [
   P(U[19], None, "main", "Owyne",
     "A Sultansworn of Ul'dah. A sealed letter to him turned up among the papers of a captain caught dealing with bandits; Momodi swears he is loyal.",
     ["M19ca", "M19cc"]),
   P(U[20], None, "main", "Owyne",
     "The Sultansworn who was guarding Ul'dah's royal crown when it was stolen. Guilt-ridden, he paid the thieves' ransom, the Traders' Spurn, before the crown was won back.",
     ["M20cd", "M20cf", "M20cg"]),
 ],

 # ---- Ul'dah's rulers ----
 "char-nanamo": [
   P(U[20], None, "main", "Nanamo",
     "The sultana of Ul'dah, seventeenth to ascend its throne. Her crown is her birthright and marks her as custodian of the Ul legacy. "
     "She keeps the support of the people, but the six wealthiest citizens, the Syndicate, hold the most sway.",
     ["M20cm", "M20ce", "M20cc", "M20cb"], SULTANA),
   P(U[22], None, "main", "Nanamo",
     "The sultana of Ul'dah, seventeenth to ascend its throne. Raubahn says she is aghast at her subjects' plight, but the members of the Syndicate who profit from the workers' poverty thwart her at every turn.",
     ["M20cm", "M22cc", "M22cd"], SULTANA),
 ],
 "char-raubahn": [
   P(U[20], None, "main", "Raubahn",
     "A general of Ul'dah who oversees the sultanate's affairs with Sultana Nanamo's consent. He suspected Owyne after seeing him sneak into the vaults, and had him watched.",
     ["M20cn", "M20ch"], GENERAL),
   P(U[22], None, "main", "Raubahn",
     "The Flame General, who oversees Ul'dah's affairs with Sultana Nanamo's consent. He says there is no hope for the masses until the crown is restored to power, "
     "and remembers the Warriors of Light, the forgotten heroes lost at Carteneau five years ago.",
     ["M20cn", "M22ci", "M22cd", "M22cf"], GENERAL),
   P(U[23], None, "main", "Raubahn",
     "The Flame General: supreme commander of the Immortal Flames, Ul'dah's Grand Company, who oversees the sultanate's affairs with Sultana Nanamo's consent. "
     "He proposed that the Eorzean Alliance mark the fifth anniversary of Carteneau with a memorial, and the Admiral and the Elder Seedseer agreed.",
     ["M23be", "M20cn", "M23bb", "M23bk", "M23bo"], GENERAL),
 ],

 # ---- The Alliance and the Empire ----
 "char-merlwyb": [
   P(U[23], None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa and commander of its Grand Company. She accepted Raubahn's proposal of a memorial for Carteneau, and warns that the imperials crowd Eorzea's borders.",
     ["M23bh", "M23bk", "M23bj"], ["Admiral Merlwyb", "the Admiral"]),
 ],
 "char-kan-e-senna": [
   P(U[23], None, "main", "Kan-E-Senna",
     "Elder Seedseer of Gridania and leader of its Grand Company. She approved Raubahn's memorial for Carteneau, and says Eorzea must stand united again, for none may sleep easy while Gaius breathes Eorzean air.",
     ["M23bl", "M23bo", "M23bp", "M23bm"], ["the Elder Seedseer"]),
 ],
 "char-gaius": [
   P(U[23], None, "main", "Gaius",
     "Legatus of the XIVth Imperial Legion, entrenched in Eorzea's border regions. He holds that only Garlean rule can bring order to Eorzea, and the Elder Seedseer says none may sleep easy while he breathes its air.",
     ["M23bg", "M23bf", "M23bm"]),
 ],
 "char-baderon": [
   P(U[24], None, "main", "Baderon",
     "Proprietor of the Drowning Wench in Limsa Lominsa, who needs a capable adventurer for a dangerous job.",
     ["M24a", "M24c"]),
 ],
}

# ---- Relationships ------------------------------------------------------------------------------------------------
# Backfills ("-arr") repeat a later era's triple for the steps before it, ending exactly where that record begins,
# because its claims come from later quests (an ADJUST would cite them early).
RELS = [
 ("rel-papashan-aids-sultansworn", "char-papashan", "aids", "org-sultansworn", U[4], None, "main", ["M4ca"]),
 ("rel-lolorito-member-syndicate-arr", "char-lolorito", "member-of", "org-syndicate", U[8], "cp-msq-174", "main", ["M8cg"]),
 ("rel-lolorito-controls-brass-blades", "char-lolorito", "controls", "org-brass-blades", U[8], None, "main", ["M8cf"]),
 ("rel-lolorito-opposes-wystan", "char-lolorito", "opposes", "char-wystan", U[8], None, "main", ["M8ce"]),
 ("rel-leofric-member-brass-blades", "char-leofric", "member-of", "org-brass-blades", U[13], None, "main", ["M13cd"]),
 ("rel-baldewyn-member-brass-blades", "char-baldewyn", "member-of", "org-brass-blades", U[16], U[18], "main", ["M16cc"], ["M18cf"]),
 ("rel-fufulupa-member-brass-blades", "char-fufulupa", "member-of", "org-brass-blades", U[16], None, "main", ["M16ca"]),
 ("rel-owyne-member-sultansworn", "char-owyne", "member-of", "org-sultansworn", U[19], None, "main", ["M19ca"]),
 ("rel-sultansworn-serves-nanamo", "org-sultansworn", "serves", "char-nanamo", U[20], None, "main", ["M20co"]),
 ("rel-raubahn-serves-nanamo-arr", "char-raubahn", "serves", "char-nanamo", U[20], "cp-msq-217", "main", ["M20cn"]),
 ("rel-momodi-aids-nanamo", "char-momodi", "aids", "char-nanamo", U[20], None, "main", ["M19cb", "M20ca"]),
 ("rel-raubahn-leads-immortal-flames-arr", "char-raubahn", "leads", "org-immortal-flames", U[23], "cp-msq-200", "main", ["M23be"]),
 ("rel-gaius-member-empire-arr", "char-gaius", "member-of", "org-garlean-empire", U[23], "cp-msq-141", "main", ["M23bg"]),
]

# Arc casts: (member, from step, claims). At most 10 per arc.
CASTS = {
 ARC1: [("loc-uldah", U[1], ["M1cc"]), ("char-momodi", U[1], ["M1ca"]), ("char-papashan", U[2], ["M2cb"]),
        ("org-sultansworn", U[3], ["M3ca"]), ("char-lilira", U[4], ["M4ca"]), ("char-thancred", U[4], ["M4cg"])],
 ARC2: [("char-wystan", U[8], ["M8ca"]), ("char-lolorito", U[8], ["M8ce"]), ("org-brass-blades", U[8], ["M8cc"]),
        ("org-syndicate", U[8], ["M8cc"]), ("char-momodi", U[8], ["M8cj"]), ("char-dadanen", U[9], ["M9ca"]),
        ("char-fufulupa", U[12], ["M12cb"]), ("char-leofric", U[12], ["M12cc"]), ("char-baldewyn", U[16], ["M16cc"]),
        ("char-owyne", U[19], ["M19ca"])],
 ARC3: [("char-owyne", U[20], ["M20cd"]), ("char-momodi", U[20], ["M20ca"]), ("char-papashan", U[20], ["M20cg"]),
        ("org-sultansworn", U[20], ["M20cg"]), ("org-ascians", U[20], ["M20ci"]), ("char-thancred", U[20], ["M20ci"]),
        ("char-nanamo", U[20], ["M20cm"]), ("char-raubahn", U[20], ["M20ch"]), ("org-syndicate", U[22], ["M22cc"])],
 ARC4: [("char-raubahn", U[23], ["M23ba"]), ("org-eorzean-alliance", U[23], ["M23ba"]), ("char-merlwyb", U[23], ["M23bk"]),
        ("char-kan-e-senna", U[23], ["M23bo"]), ("char-gaius", U[23], ["M23bg"]), ("org-garlean-empire", U[23], ["M23bg"]),
        ("org-immortal-flames", U[23], ["M23be"]), ("char-baderon", U[24], ["M24a"])],
}

ARCS = [
 ("arc-s1-a-newcomer-in-uldah", ARC1, U[1], U[7]),
 ("arc-s2-ore-and-gil", ARC2, U[8], U[19]),
 ("arc-s3-the-sultanas-crown", ARC3, U[20], U[22]),
 ("arc-s4-the-flame-generals-envoy", ARC4, U[23], U[24]),
]
ARC_NOTES = {
 "arc-s1-a-newcomer-in-uldah": "Ul'dah MSQ #1 *Close to Home (Ul'dah)* to #7 *Out of House and Home*: Momodi's first tasks, Papashan's Dispatch Yard, "
   "the runaway Lady Lilira at the Sultantree (where Thancred and the Crystal vision first appear) and the Stone Torches' ore route (M7cb). "
   "It stops before #8, where Lolorito's trap opens the chain's first real conflict.",
 "arc-s2-ore-and-gil": "Ul'dah MSQ #8 *Way Down in the Hole* to #19 *Secrets and Lies*: Lolorito's trap for Wystan, Dadanen's lost Nashachite, Lost Hope and the "
   "Brass Blades of the Rose, ending when Baldewyn's papers yield the letter to Owyne (M19ca). Ore and gems run through it, from the Sil'dih vein to the stolen Nashachite. "
   "#19 belongs here rather than to the crown arc, whose name would reveal #20's theft a step early.",
 "arc-s3-the-sultanas-crown": "Ul'dah MSQ #20 *Duty, Honor, Country* to #22 *A Royal Reception*: the stolen crown, the Ascian mage, Nanamo's invitation and the feast, "
   "ending when Raubahn says he has work for you (M22ci). The page's \"banquet\" is called a feast (reserved term).",
 "arc-s4-the-flame-generals-envoy": "Ul'dah MSQ #23 *The Ul'dahn Envoy* and #24 *Call of the Sea (Ul'dah)*: Raubahn's envoy to Merlwyb and Kan-E-Senna, and the handoff to "
   "Baderon (M24a), where the three chains converge on *It's Probably Pirates*. Named so as not to reuse #23's title.",
}

DECISIONS = [
 "**Shared entities speak in facts.** Ul'dah, Thancred, Lolorito, the Syndicate, Nanamo, Raubahn, the Immortal Flames, the Alliance, Merlwyb, Kan-E-Senna, Gaius, the Empire, the Ascians and Baderon "
 "are described by what the pages say about them, not by the Ul'dah starter's deeds, so they read true for every starting city. Only the arc recaps say \"you\".",
 "**Backfills, not ADJUSTs, for later eras' relationships.** Lolorito in the Syndicate (from #8), Raubahn serving Nanamo (#20) and leading the Immortal Flames (#23), and Gaius in the Empire (#23) "
 "each get an `-arr` record that ends where the later era's record begins (#174, #217, #200, #141), because those records cite later quests.",
 "**Unnamed figures stay unnamed.** The masked mage (#8, #20) is \"a masked mage called an Ascian\", and the voice in the Carteneau vision (#22, tagged \"???\") is left out, as is the castrum cutscene's second officer.",
 "**Minor helpers live in recaps only:** Cicidoa, Roger, Warin and the Stone Torches, Drunken Stag, Totoruna, Raffe, Merilda, Garibald and the two self-styled barons have no entries.",
 "**No Scions yet.** Thancred's Echo memory at #8 mentions the Scions, but the chain never introduces them; he stays a Sharlayan scholar of the aether until the later eras.",
]
