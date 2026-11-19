"""Atlas content for patches 2.4–2.55: MSQ #200 Traitor in the Midst to #240 The Parting Glass, and the 2.55
milestone (cp-arr-2-55, after Before the Dawn). Arc tag d. Data only; see docs/atlas/era-modules.md for the contract.

Researched 2026-11-19 from the saved Console Games Wiki wikitext (lanes L06–L10); every locator is an exact substring
of the quest's saved page. Spoiler choices this era makes:
  - first names only: Eline (never her surname), Teledji, Nanamo, Varis, Pipin; Estinien without his epithet;
  - Nanamo is never stated dead: she collapses, Teledji proclaims her murdered and Ilberd claims credit;
  - the Ivy is its own entry until #210, then "revealed as" Eline (the Marques → Cid pattern);
  - Iceheart keeps her entry and takes "Ysayle" as an alias from #207, where she gives that name herself;
  - Nabriales is named only from #224, where he names himself (ALLOW below; the lead must accept it). At #213 he is
    "an unseen figure";
  - the accepted cp-arr-2-55 records for the Scions' core cast are left alone; this module closes them only from earlier.
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

def S(n):
    return f"cp-msq-{n}"

B = "cp-arr-2-55"
S234B, S235B = "cp-msq-234b", "cp-msq-235b"

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #200 Traitor in the Midst
 "M200a": ("Minfilia asks you to help Alphinaud run the newly formed Crystal Braves.", "Traitor in the Midst", "Conscious of the many practical difficulties facing the newly formed Crystal Braves, Minfilia asks that you place yourself at Alphinaud's disposal."),
 "M200b": ("Ilberd reveals that a Garlean spy known as the Ivy has infiltrated one of the Grand Companies.", "Traitor in the Midst", "Ilberd reveals that a [[Garlean]] spy known as [[the Ivy]] has infiltrated one of the [[Grand Companies]]."),
 "M200c": ("A suspect in the Immortal Flames proved to be only one of the many in the spy's employ.", "Traitor in the Midst", "A suspect was identified among [[the Immortal Flames]], but the man proved to be but one of many in the agent's employ."),
 "M200d": ("The Ivy's conspirators are the vines by which the spy learns secrets without being exposed.", "Traitor in the Midst", "These conspirators are the vines by which he learns our secrets, all without exposing himself."),
 "M200e": ("Raubahn and Ilberd have been friends and rivals since before the fall of Ala Mhigo.", "Traitor in the Midst", "You learn that Raubahn and Ilberd have been friends and rivals since before the fall of [[Ala Mhigo]]."),
 "M200f": ("Raubahn is a Flame General.", "Traitor in the Midst", "Flame General... You wear the mantle well, old friend."),
 "M200g": ("Raubahn wonders whether the Monetarists have been in league with the Empire from the first.", "Traitor in the Midst", "Could it be that the Monetarists have been in league with the Empire from the first?"),
 "M200h": ("Ilberd fears the Empire will soon resume its march on Eorzea.", "Traitor in the Midst", "Garlemald's war of succession nears its end, and it is feared that the Empire will soon resume its march on Eorzea."),
 # #201 Back and Fourth
 "M201a": ("A unit of Crystal Braves was ambushed by Garlean forces.", "Back and Fourth", "a unit of [[Crystal Braves]] was ambushed by Garlean forces during your absence."),
 "M201b": ("The captured Brave is rescued with no further losses.", "Back and Fourth", "Thanks to your aid, our comrade Rhesh is safe, and we suffered no further casualties."),
 "M201c": ("An Ishgardian dignitary has granted Alphinaud an audience and asked for you.", "Back and Fourth", "I have been granted an audience with an Ishgardian dignitary, you see, and the man expressly requested your presence."),
 "M201d": ("Ilberd vows not to rest until the Ivy is caught.", "Back and Fourth", "And it may yet take time, but I will not rest until we have identified and apprehended the Ivy."),
 "M201e": ("Alianne of the 4th Unit waits near Castrum Centri.", "Back and Fourth", "Alianne of the 4th lies in wait in the Tangle, near the entrance to Castrum Centri."),
 "M201f": ("One of the ambushed unit's members was taken to Castrum Centri.", "Back and Fourth", "one of the unit's members was captured and taken to [[Castrum Centri]]"),
 # #202 Coming to Terms
 "M202a": ("Ser Aymeric, lord commander of the Temple Knights, represents the Holy See.", "Coming to Terms", "Alphinaud has been granted an audience with Ser Aymeric, lord commander of the [[Ishgard]]ian [[Temple Knights]], who will be acting as a representative of the [[Holy See]]."),
 "M202b": ("The Holy See has no intention of rejoining the Eorzean Alliance.", "Coming to Terms", "it becomes apparent that the Holy See has no intention of rejoining the [[Eorzean Alliance]]"),
 "M202c": ("Ishgard's astrologians foretell Midgardsormr's return, and Aymeric wants the Scions to help watch the great wyrm's remains.", "Coming to Terms", "You learn that the [[astrologian]]s of Ishgard have foretold the return of [[Midgardsormr]]─the fallen guardian of [[Silvertear Falls]]─and that Ser Aymeric wishes to enlist [[the Scions]]' aid in keeping watch over the great wyrm's remains."),
 "M202d": ("In exchange, Aymeric will keep House Fortemps' aid shipments flowing to Revenant's Toll.", "Coming to Terms", "In exchange, he will ensure that the shipments of aid from [[House Fortemps]] to [[Revenant's Toll]] will continue unabated."),
 "M202e": ("Iceheart and her followers waylay the latest shipment.", "Coming to Terms", "only to learn moments after that the latest shipment has been waylaid by [[Iceheart]] and her followers..."),
 "M202f": ("Ishgard's forces are wholly committed to the conflict with the Dravanians.", "Coming to Terms", "Even were that not the case, our forces are wholly committed to the Dravanian conflict."),
 "M202h": ("The dragon star waxes bright, and there are whispers that it portends Midgardsormr's resurrection.", "Coming to Terms", "The dragon star waxes unnaturally bright, and there are whispers that it portends the resurrection of Midgardsormr."),
 "M202i": ("Since the Battle of Silvertear Skies, Ishgard has kept her neighbors at arm's length.", "Coming to Terms", "Ever since the [[Battle of Silvertear Skies]], the city–state of Ishgard has kept her neighbors at arm's length."),
 # #203 The Intercession of Saints
 "M203a": ("In the ambush every knight was slain and every crate seized.", "The Intercession of Saints", "'Twas an ambush─swift and ruthless. In an instant, every knight was slain, every crate seized."),
 "M203b": ("Disguised as pilgrims, Iceheart and her brethren slaughtered the caravan's guards.", "The Intercession of Saints", "Disguised as pilgrims, Iceheart and her brethren slaughtered the caravan's guards, and the young man only survived by feigning his own death."),
 "M203c": ("Iceheart's people spoke of deliverance and resurrection.", "The Intercession of Saints", "Iceheart's people spoke of deliverance and resurrection."),
 "M203d": ("Ishgard calls Shiva a traitor to kith and kin who lay down with dragons.", "The Intercession of Saints", "Shiva was a traitor to kith and kin─an apostate who ''lay down with dragons''."),
 "M203e": ("Alphinaud concludes that Iceheart and her followers mean to summon Shiva as a beast tribe would a primal.", "The Intercession of Saints", "Iceheart and her followers intend to ''summon'' Shiva, as a beast tribe would a primal!"),
 "M203f": ("Alphinaud turns the whole order to preventing the summoning.", "The Intercession of Saints", "Our entire order must turn its efforts to the prevention of this summoning."),
 "M203g": ("Shiva is the heretics' patron saint.", "The Intercession of Saints", "Wait─you say she is their ''patron'' saint?"),
 "M203h": ("Iceheart is a silver-haired woman.", "The Intercession of Saints", "Slowly she approached, her silver hair flowing in the wind like melting snow."),
 # #204 Strength in Unity
 "M204a": ("Drillemont's scouts lost the heretic pilgrims at Snowcloak.", "Strength in Unity", "Alas, our scouts lost track of them at Snowcloak─that selfsame frozen wall which we speculated might conceal the heretics' hideaway."),
 "M204b": ("Aymeric's knights join the hunt.", "Strength in Unity", "I have heard enough. My knights will join the hunt."),
 "M204c": ("Alphinaud summons a unit of Crystal Braves to Whitebrim Front.", "Strength in Unity", "I took the liberty of summoning a unit of Crystal Braves to Whitebrim Front."),
 "M204d": ("The Scions join the hunt for Iceheart.", "Strength in Unity", "The Scions of the Seventh Dawn wish to join in the hunt for Iceheart?"),
 # #205 Dark Words, Dark Deeds
 "M205a": ("A covert check of Whitebrim Front finds one possible heretic.", "Dark Words, Dark Deeds", "we identified only one possible heretic."),
 "M205b": ("The heretics already know the movements of the Temple Knights and the Crystal Braves.", "Dark Words, Dark Deeds", "the movements of the [[Temple Knights]] and the [[Crystal Braves]] are already known to them."),
 "M205c": ("The suspect is detained.", "Dark Words, Dark Deeds", "I shall have the man detained at once. His guilt is plain."),
 "M205d": ("Drillemont means to root out the heretics.", "Dark Words, Dark Deeds", "which means it is key to ''our'' plans that they be rooted out and put to the sword."),
 # #206 First Blood
 "M206a": ("The knights of House Durendaire lie slain in Boulder Downs.", "First Blood", "the knights of House Durendaire slain after what must have been a desperate battle with"),
 "M206b": ("A recovered parchment is a timetable of the watches at Snowcloak.", "First Blood", "The parchment you recovered is a timetable of the guardsmen's watches at our outpost in Snowcloak."),
 "M206c": ("The traitor passed the heretics something of value.", "First Blood", "it seems the traitor you followed managed to pass the heretics something of value after all"),
 "M206d": ("The heretics may already be in position.", "First Blood", "Of course, it will be changed ''now'', but the heretics may already be in position."),
 # #207 The Path of the Righteous
 "M207a": ("Aymeric had suspected the heretics were plotting an attack.", "The Path of the Righteous", "Truth be told, we suspected the heretics might be plotting such an attack."),
 "M207b": ("Alphinaud finds the entrance to Iceheart's lair among the tunnels.", "The Path of the Righteous", "Amongst this warren of tunnels lies the entrance to Iceheart's lair!"),
 "M207c": ("Iceheart was given the name Ysayle but earned the name Iceheart.", "The Path of the Righteous", "I was given the name Ysayle, but I earned the name Iceheart."),
 "M207d": ("Iceheart vows to end the war between dragon and man, no matter the cost.", "The Path of the Righteous", "I will bring an end to this war between dragon and man─no matter the cost."),
 "M207e": ("Iceheart escapes, but you drive the heretics from their lair.", "The Path of the Righteous", "Though you failed to apprehend Iceheart, you have driven the heretics from their lair."),
 "M207f": ("Minfilia and Urianger search House Fortemps' archives for word of Shiva.", "The Path of the Righteous", "Minfilia and Urianger have been busy perusing the archives of House Fortemps, gathering what information they can on Shiva."),
 # #208 For the Greater Good
 "M208a": ("Minfilia is certain Shiva was a real, living woman.", "For the Greater Good", "Shiva was real─a living, breathing woman─of that there can be no doubt."),
 "M208b": ("Iceheart likely had the second aetheryte destroyed to keep anyone from following.", "For the Greater Good", "I can only presume she had it destroyed to prevent us from following her."),
 "M208c": ("The Garlean spy may have been helping Iceheart.", "For the Greater Good", "it seems our favorite Garlean spy may have been providing assistance to Iceheart."),
 "M208d": ("Ilberd and Alphinaud had sought the captured merchant in their hunt for the Ivy.", "For the Greater Good", "they had been seeking the merchant in connection with their investigation into"),
 "M208e": ("Yugiri offers to accompany the Scions until the investigation is complete.", "For the Greater Good", "If you will allow it, I would accompany you until the investigation is complete."),
 "M208f": ("Yugiri and her shinobi helped uncover the merchant's link to the heretics.", "For the Greater Good", "Were it not for the efforts of Lady Yugiri and her shinobi, we might never have discovered this connection."),
 "M208g": ("Yugiri's people long to strike back against the Empire.", "For the Greater Good", "We long to strike back against the Empire and weaken their influence in this land─"),
 "M208h": ("Yuyuhase leads the 3rd Unit Braves in pursuit of the heretics.", "For the Greater Good", "the 3rd Unit Braves are already in pursuit. Yuyuhase leaves to join them"),
 "M208i": ("A dead heretic's plan has them withdraw to the Observatorium.", "For the Greater Good", "Withdraw in groups of three or less to the Observatorium."),
 # #209 Tendrils of Intrigue
 "M209a": ("A Flame at Revenant's Toll sold secrets to the merchant, who passed them to the heretics.", "Tendrils of Intrigue", "had been selling secrets to the merchant you apprehended, who had in turn been passing information to the heretics."),
 "M209b": ("The Ivy covered the trail with powers held only by high-ranking Flames.", "Tendrils of Intrigue", "In a desperate bid to cover his tracks, the Ivy resorted to exercising certain administrative powers available only to high-ranking members of the Immortal Flames."),
 "M209c": ("The Garlean war of succession ends with Varis, the late emperor's grandson, crowned.", "Tendrils of Intrigue", "the crowning of [[Varis zos Galvus]], the [[Solus zos Galvus|late emperor]]'s grandson."),
 "M209d": ("Varis tore the crown from his uncle's grasp.", "Tendrils of Intrigue", "So, young Varis has torn the crown from his uncle's grasp, and taken his place at the head of the Empire."),
 "M209e": ("Until another path is found, Iceheart's sanctum is out of reach.", "Tendrils of Intrigue", "until another path to her sanctum is found, she will remain beyond our reach."),
 "M209f": ("Ilberd says the Ivy has been unmasked.", "Tendrils of Intrigue", "Doubtless the commander has informed you, but we have unmasked the Ivy."),
 "M209g": ("The Alliance must entice Ishgard back into the fold.", "Tendrils of Intrigue", "find a way to entice the long-estranged [[Ishgard]]ians back into the fold"),
 "M209h": ("Kan-E-Senna opens the council on the change in the Garlean Empire.", "Tendrils of Intrigue", "Change has come to the Garlean Empire, and we must discuss the implications."),
 "M209i": ("The Alliance leaders convene at the Lotus Stand in Old Gridania.", "Tendrils of Intrigue", "The council of Alliance leaders will convene at [[the Lotus Stand]] in [[Old Gridania]]."),
 # #210 Chasing Ivy
 "M210a": ("Ilberd names Flame Marshal Eline, Raubahn's second-in-command, as the spy.", "Chasing Ivy", "The spy we have been seeking all this time is none other than Flame Marshal Eline Roaille, Raubahn's second-in-command."),
 "M210b": ("Eline is of Ishgardian birth, the highest-ranked foreigner in the Immortal Flames.", "Chasing Ivy", "Of Ishgardian birth, she is the highest-ranked foreigner in the Immortal Flames"),
 "M210c": ("Ilberd wonders whether the Ivy has a hold over the Monetarists.", "Chasing Ivy", "Could it be that the Ivy has some hold over the Monetarists?"),
 "M210d": ("Eline should have stayed at the Hall of Flames while Raubahn attended the council.", "Chasing Ivy", "While Raubahn attended the council of Alliance leaders, she ''should'' have remained in the Hall of Flames."),
 "M210e": ("A Doman shinobi saw through Eline's merchant disguise.", "Chasing Ivy", "She was attired as a merchant, but these eyes are not so easily deceived."),
 # #211 In Flagrante Delicto
 "M211a": ("Devices from the Ironworks disrupt Garlean communications.", "In Flagrante Delicto", "our ingenious friends at Garlond Ironworks have provided us with devices which disrupt these communications"),
 "M211b": ("The Garleans send agents to destroy the devices.", "In Flagrante Delicto", "the Garleans have sent agents with a mind to destroy the devices and render such direct contact unnecessary."),
 "M211c": ("Ilberd arrests Eline for treason and espionage.", "In Flagrante Delicto", "Flame Marshal Eline Roaille! You are under arrest for treason and espionage!"),
 "M211d": ("Eline offers no struggle, saying she has nothing to hide.", "In Flagrante Delicto", "I will offer you no struggle. After all, I have naught to hide."),
 "M211e": ("Yugiri reads Eline's surrender as knowing her position is untenable, not as innocence.", "In Flagrante Delicto", "Despite her claims, her surrender does not bespeak innocence, but an awareness that her position is untenable."),
 "M211f": ("Minfilia reports progress toward a way into Iceheart's sanctum.", "In Flagrante Delicto", "I am pleased to report that we have made progress in our efforts to find a way into Iceheart's sanctum"),
 # #212 A Simple Plan
 "M212a": ("Iceheart means to summon Shiva with the crystals stolen from the House Fortemps caravan.", "A Simple Plan", "It is there that we suspect she means to summon Shiva using the crystals she stole from the House Fortemps caravan."),
 "M212b": ("Minfilia expects the result to be something more akin to a primal.", "A Simple Plan", "it seems likely that the result will be something more akin to a primal."),
 "M212c": ("Moenbryda is an accomplished Sharlayan scholar and an authority on aetheryte technologies.", "A Simple Plan", "Moenbryda is an accomplished Sharlayan scholar and an authority on aetheryte technologies."),
 "M212d": ("Moenbryda has been researching white auracite to capture Ascian souls.", "A Simple Plan", "a material she has been researching for the purpose of capturing [[Ascian]] souls."),
 "M212e": ("Moenbryda proposes using an aetherial current to recreate the beacon.", "A Simple Plan", "We use the current to recreate the beacon."),
 "M212f": ("Everyone who has tried to teleport this way has died.", "A Simple Plan", "Every person who has attempted to teleport in this fashion has died in the process."),
 # #213 The Instruments of Our Deliverance
 "M213a": ("Through Moenbryda's white auracite the aetheryte wakes, opening a path to Iceheart's sanctuary.", "The Instruments of Our Deliverance", "you attune to the giant crystal, opening a path to [[Iceheart]]'s sanctuary...probably."),
 "M213b": ("Iceheart offers her own body as a vessel for Shiva's soul.", "The Instruments of Our Deliverance", "Iceheart offers her own body as a vessel for Shiva's soul."),
 "M213c": ("The battle ends with the maiden kneeling in the snow, cursing your ignorance.", "The Instruments of Our Deliverance", "the battle ends as it began, with the young maiden kneeling in the snow, cursing your ignorance."),
 "M213d": ("Iceheart tells you to seek the Keeper of the Lake and see with eyes unclouded.", "The Instruments of Our Deliverance", "Seek the Keeper of the Lake. See with eyes unclouded."),
 "M213e": ("An unseen figure remarks that Lahabrea will be pleased.", "The Instruments of Our Deliverance", "Nevertheless, Lahabrea will be pleased."),
 "M213f": ("You wonder whether Hydaelyn speaks to your enemy too.", "The Instruments of Our Deliverance", "Could it be that [[Hydaelyn]] speaks to your enemy too?"),
 # #214 The Road Less Traveled
 "M214a": ("The Holy See ordered its knights to observe and act only in self-defense.", "The Road Less Traveled", "the Holy See decreed that we were to observe, and that military action should be taken only in self-defense."),
 "M214b": ("Ishgard wants Revenant's Toll to flourish as an obstacle to its enemies from the south.", "The Road Less Traveled", "Ishgard desires to see Revenant's Toll flourish, as it would present a troublesome obstacle to our enemies from the south."),
 "M214c": ("Aymeric introduces Lucia, his second-in-command, who will represent him.", "The Road Less Traveled", "Ser Aymeric then formally introduces his second-in-command, [[Lucia]], who will act as his representative when he is otherwise indisposed."),
 "M214d": ("Lucia, not of Ishgardian birth, owes no allegiance to any noble house.", "The Road Less Traveled", "Not being of Ishgardian birth, she owes no allegiance to any noble house, making her as near to incorruptible as one can find in my homeland."),
 "M214e": ("Haurchefant is distressed that you did not involve him.", "The Road Less Traveled", "Lord [[Haurchefant]] is more than a little distressed that you did not think to involve him in your daring endeavor."),
 "M214f": ("Iceheart has escaped, but Aymeric says she cannot run forever.", "The Road Less Traveled", "Aye, there is the matter of Iceheart's escape, but she cannot run forever."),
 "M214g": ("Alphinaud suspects Ishgard of manipulating its neighbors.", "The Road Less Traveled", "Ishgard is not wont to aid its neighbors, but that does not preclude it from manipulating them to serve its own interests."),
 "M214h": ("Ishgard shares what it learned from the heretics' attacks and the captured merchant.", "The Road Less Traveled", "The results of our investigation into the heretics' recent attacks, as well as our interrogation of the merchant you detained."),
 "M214i": ("Aymeric calls the arrangement mutually beneficial, born of necessity.", "The Road Less Traveled", "Ours is a mutually beneficial arrangement, lest we forget. One born of necessity."),
 # #215 Eyes Unclouded
 "M215a": ("Not only beast tribes but civilized peoples can summon primals.", "Eyes Unclouded", "it was not only the beast tribes of Eorzea that could summon primals, but her civilized peoples as well"),
 "M215b": ("The Alliance could face the combined might of all Garlemald.", "Eyes Unclouded", "we could well find ourselves facing the combined might of ''all Garlemald''"),
 "M215c": ("Minfilia wonders whether Iceheart has the Echo.", "Eyes Unclouded", "If Iceheart is blessed with the power of the Echo, she will doubtless have used it to further her goals."),
 "M215d": ("Moenbryda says what Iceheart summoned was a primal.", "Eyes Unclouded", "but I ''will'' say that what she summoned was a primal."),
 "M215e": ("Midgardsormr was a king amongst kings who reigned for centuries.", "Eyes Unclouded", "Midgardsormr was a king amongst kings who reigned for centuries on end"),
 "M215f": ("Ishgard's astrologians fear Midgardsormr may soon rise from the dead.", "Eyes Unclouded", "that [[Ishgard]]ian [[astrologian]]s fear may soon rise from the dead"),
 "M215g": ("The Scions have another reason to watch the Keeper of the Lake.", "Eyes Unclouded", "It would seem we have yet another reason to stand watch over the Keeper of the Lake."),
 "M215h": ("Urianger notes that few know the secrets of summoning, and a single party profits from spreading them.", "Eyes Unclouded", "Few are privy to the secrets of summoning, and but a single party standeth to profit from their dissemination."),
 # #216 The Reason Roaille
 "M216a": ("The turnkey and two guards are found slain after Eline's escape.", "The Reason Roaille", "The turnkey was found slain along with two guards."),
 "M216b": ("Eline had inside help.", "The Reason Roaille", "'Tis plain she received inside help."),
 "M216c": ("Eline makes for Castrum Meridianum.", "The Reason Roaille", "She makes for Castrum Meridianum, I am certain of it."),
 "M216d": ("Ilberd's men bind the recaptured Eline.", "The Reason Roaille", "Bind her! And do it ''tight''!"),
 "M216e": ("Eline speaks of the injustice lowborn Ishgardians endure.", "The Reason Roaille", "the injustice that we lowborn Ishgardians must endure!"),
 "M216f": ("Ilberd tells Eline that he sold his sword, but she sold her comrades.", "The Reason Roaille", "But whereas I sold my sword, you, Marshal─you sold your comrades."),
 "M216g": ("Eline is sent back to Ul'dah to face justice.", "The Reason Roaille", "You will return to Ul'dah to face justice"),
 "M216h": ("Teledji has the Blades watch Raubahn and the Flames day and night.", "The Reason Roaille", "Have the Blades watch him and the Flames day and night."),
 "M216i": ("Teledji orders an East Aldenard trade route severed to keep Lolorito occupied.", "The Reason Roaille", "Sever one of the East Aldenard trade routes. That ought to keep Lolorito occupied for a while."),
 # #217 Let Us Cling Together
 "M217a": ("Eline aided the Scions at the time of the order's founding.", "Let Us Cling Together", "Together with Raubahn, Eline lent us much-needed aid at the time of our order's founding."),
 "M217b": ("White auracite holds aether only for a short while.", "Let Us Cling Together", "The stone can only store aether for a short while before expelling its contents."),
 "M217c": ("An Ascian soul may be undone by a concentrated burst of pure aether.", "Let Us Cling Together", "'Tis our belief that an Ascian soul may be permanently undone if smitten by a sufficiently concentrated burst of pure aether."),
 "M217d": ("The Isle of Val has been erased from existence.", "Let Us Cling Together", "According to the report, the isle has been erased from existence."),
 "M217e": ("Even as she served the Empire, Eline sold imperial secrets to a faction in Eorzea.", "Let Us Cling Together", "We've learned that even as Roaille served the Empire's interests, she sold imperial secrets to a certain faction in Eorzea."),
 "M217f": ("Raubahn concludes that Emperor Varis was Eline's true master.", "Let Us Cling Together", "This could only be the former high legatus of the Garlean Army, now known as Emperor Varis zos Galvus."),
 "M217g": ("Ilberd calls Eline a triple agent.", "Let Us Cling Together", "Triple, if you consider her services to van Baelsar and the new emperor as separate."),
 "M217h": ("Nanamo declares that Ul'dah will become a true republic, ending Royalists and Monetarists alike.", "Let Us Cling Together", "When the time is ripe, the nation shall become a true republic. Both Royalists and Monetarists shall cease to be."),
 "M217i": ("Nanamo asks Raubahn's forgiveness for casting aside all he has toiled for in her name.", "Let Us Cling Together", "Raubahn... Forgive me for casting aside all that you have toiled for in my name..."),
 "M217j": ("Raubahn swears to purge the land of the Monetarists.", "Let Us Cling Together", "One day, I will purge this land of your sickness! Before the eyes of the Twelve, I swear it!"),
 "M217k": ("Nanamo asks the Alliance leaders to help Raubahn preserve order.", "Let Us Cling Together", "Help Raubahn to preserve order, and protect the people."),
 "M217l": ("Nanamo is the last monarch in the line of Ul.", "Let Us Cling Together", "As the last monarch in the line of Ul, I make unto you this request."),
 # #218 Good Intentions
 "M218a": ("The Immortal Flames struggle after one of their highest-ranking officers proved a Garlean agent.", "Good Intentions", "As expected, the Immortal Flames have been struggling to cope with the revelation that one of their highest-ranking officers was a Garlean agent."),
 "M218b": ("Shiva will not be the last primal, and ties with Ishgard are tenuous.", "Good Intentions", "We both know full well that Saint Shiva will not be the last primal we face...and our relationship with Ishgard is still tenuous at best."),
 "M218c": ("How to form an aetherial blade at will remains unsolved.", "Good Intentions", "Alas, the key problem─how to form an aetherial blade at will─remains unsolved."),
 "M218d": ("Riol, tracing weapons used by disgruntled refugees, learns of a large shipment.", "Good Intentions", "Riol, who has been attempting to trace the source of some weapons wielded by disgruntled refugees, has learned of a large shipment which may be intended for the same purpose."),
 "M218e": ("Alphinaud sends you to meet Captain Ilberd at Highbridge.", "Good Intentions", "Then it is settled. Rendezvous with Captain Ilberd at Highbridge and intervene when the exchange takes place."),
 "M218f": ("Teledji and his Monetarist ilk turn the situation to their advantage.", "Good Intentions", "Teledji Adeledji and his Monetarist ilk have wasted no time in attempting to turn the situation to their advantage."),
 # #219 Bait and Switch
 "M219a": ("Ilberd's 1st Unit is to block the clients' escape.", "Bait and Switch", "Ilberd states that the 1st Unit will establish a perimeter, preventing the clients' escape, while you and he seize the black marketeer and his weapons."),
 "M219b": ("The black marketeer fought back and one of Ilberd's men killed him.", "Bait and Switch", "The captain explains that the black marketeer fought back with a hidden blade, and that one of his subordinates, fearing for his safety, slew the man."),
 "M219c": ("The clients slipped past the perimeter.", "Bait and Switch", "though we know not how, they slipped past our perimeter."),
 "M219d": ("The promised massive shipment turns out to be one crate.", "Bait and Switch", "the information we received indicated a massive shipment, and this is anything but..."),
 # #220 Best-laid Schemes
 "M220a": ("Yuyuhase blames Riol's intelligence.", "Best-laid Schemes", "Clearly, Riol is unfamiliar with the ways of Ul'dahn merchants, who ever strive to present themselves as greater than they are."),
 "M220b": ("Riol insists his information was reliable.", "Best-laid Schemes", "Our information was reliable, godsdammit! I ''know'' he purchased those weapons!"),
 "M220c": ("Riol notes the 1st and 3rd Units now spend freely.", "Best-laid Schemes", "'Course these days the money flows like water, an' the 1st an' 3rd get the shiniest new toys..."),
 "M220d": ("A guest from Ishgard asks to see you.", "Best-laid Schemes", "a guest from [[Ishgard]] has requested your presence."),
 # #221 The Rising Chorus
 "M221a": ("Lucia comes on Aymeric's behalf to ask your help.", "The Rising Chorus", "Waiting for you in the solar is [[Lucia]], Ser [[Aymeric]]'s second-in-command, who has come on his behalf to request your assistance with a matter of grave import."),
 "M221b": ("The Observatorium's astrologians read the signs as Midgardsormr's imminent resurrection.", "The Rising Chorus", "The [[astrologian]]s of [[the Observatorium]] have interpreted recent signs as an indication of [[Midgardsormr]]'s imminent resurrection."),
 "M221c": ("The explosion that followed Eorzea's victory claimed the great wyrm's life.", "The Rising Chorus", "Yet this victory came at a great cost, for the explosion which followed claimed the life of the great wyrm as well."),
 "M221d": ("Atop the wreck of the Agrius you confront the fallen guardian of Silvertear Falls.", "The Rising Chorus", "atop the wreckage of the ''Agrius'' you confront the fallen guardian of [[Silvertear Falls]]"),
 "M221e": ("Hydaelyn marks you as Her chosen, and Midgardsormr strips you of the Mothercrystal's blessing.", "The Rising Chorus", "only to hesitate when [[Hydaelyn]] intervenes and marks you as one of Her chosen. Midgardsormr then relents─but not before somehow stripping you of [[the Mothercrystal]]'s blessing."),
 "M221f": ("A covenant binds Midgardsormr to you.", "The Rising Chorus", "Revealing that a covenant binds him to you"),
 "M221g": ("Midgardsormr says his children now sing of Ishgard's destruction.", "The Rising Chorus", "the wyrm lord flatly states that his children now sing of Ishgard's imminent destruction"),
 "M221h": ("The Scions keep most of the conversation with Midgardsormr secret.", "The Rising Chorus", "it would be best to keep the majority of your conversation with Midgardsormr a secret"),
 "M221i": ("Lucia thanks you for confirming that a Dravanian attack is coming.", "The Rising Chorus", "for bringing confirmation of the impending [[Dravanian]] attack"),
 "M221j": ("Until Ishgard asks for aid, the Scions can only watch and wait.", "The Rising Chorus", "Until such time as they choose to request aid, you and the others have no choice but to watch and wait."),
 # #222 Aether on Demand
 "M222a": ("An Ascian is immortal because its soul does not return to the aetherial realm when its host falls.", "Aether on Demand", "An Ascian is an immortal because its soul doesn't return to the aetherial realm when its host is defeated."),
 "M222b": ("Moenbryda plans to siphon energy from corrupted crystals across Eorzea.", "Aether on Demand", "by siphoning energy from the corrupted crystals found across [[Eorzea]]."),
 "M222c": ("The XIVth Legion lost the Empire's support, but was replenished from Castrum Centri.", "Aether on Demand", "Having lost the Empire's support, the XIVth Legion lacks the resources to sustain itself. … Not long after our forces withdrew, however, their ranks were replenished by reinforcements from Castrum Centri."),
 "M222d": ("Minfilia sends Alphinaud, with Thancred and Papalymo, to support the Crystal Braves.", "Aether on Demand", "Pray join the Crystal Braves and lend them your support. Thancred and Papalymo shall accompany you."),
 "M222e": ("Crates at the plant hold explosives of imperial design.", "Aether on Demand", "these boxes contain powerful explosive devices. Devices of imperial design, no less."),
 # #223 On the Counteroffensive
 "M223a": ("The imperial squads are too few to take and hold the plant.", "On the Counteroffensive", "According to the reconnaissance report that just came in, the squads seen leaving the castrum are too few in number to effectively take and hold our position."),
 "M223b": ("Ilberd marches the 3rd Unit out of Ul'dah to the plant.", "On the Counteroffensive", "The 3rd was getting restless holed up in Ul'dah, so I marched them out here to fill any holes in the plant's defenses and add their numbers to your counterattack."),
 "M223c": ("The plant is no longer in immediate danger.", "On the Counteroffensive", "The Amajina engineers will be most relieved to hear that the plant is no longer in any immediate danger."),
 "M223d": ("Yuyuhase reports that many Garleans won't make it back to the castrum.", "On the Counteroffensive", "I'll take that to mean that, between us, more than a few Garleans won't be making it back to the castrum."),
 # #224 An Uninvited Ascian
 "M224a": ("An Ascian introduces himself as Nabriales.", "An Uninvited Ascian", "We meet at last, Warrior of Light. I am Nabriales..."),
 "M224b": ("The blessing of Light had kept the Ascians out of the Scions' domain.", "An Uninvited Ascian", "The blessing of Light kept you and your fellow meddlers safe. It was that which prevented my kind from entering your domain."),
 "M224c": ("The staff Nabriales seeks is Tupsimati, the relic Louisoix once wielded.", "An Uninvited Ascian", "Moenbryda realizes that the staff Nabriales spoke of is likely [[Tupsimati]], the relic once wielded by [[Louisoix]] himself."),
 "M224d": ("Nabriales escapes through a rift with Minfilia and the relic.", "An Uninvited Ascian", "He then tears open a dimensional rift, through which he escapes with both Minfilia and the relic she holds."),
 "M224e": ("Minfilia realizes the Isle of Val and the scholars' fate were Nabriales's doing.", "An Uninvited Ascian", "Then it was ''your'' doing! The Isle of Val, the scholars─all of it!"),
 "M224f": ("You defeat Nabriales and rescue Minfilia.", "An Uninvited Ascian", "You have defeated Nabriales and rescued Minfilia."),
 "M224g": ("Minfilia traps the weakened Ascian's soul in white auracite.", "An Uninvited Ascian", "Minfilia succeeds in trapping the soul of the weakened Ascian within the chunk of [[White Auracite|white auracite]]."),
 "M224h": ("Moenbryda spends her own life energy so your blade can pierce Nabriales.", "An Uninvited Ascian", "The wounded scholar then expends her own life energy in a brilliant burst of aether, allowing your glowing blade to at last pierce Nabriales's essence."),
 "M224i": ("Nabriales means to use the staff's power to bring about a new Rejoining.", "An Uninvited Ascian", "the Ascian reveals his plans to use the power yet hidden within the staff to bring about a new [[Rejoining]]"),
 "M224j": ("Minfilia keeps a device left by Moenbryda.", "An Uninvited Ascian", "This device is a legacy of Moenbryda's toils and sacrifice."),
 "M224k": ("Nabriales reaches the Rising Stones' solar, where Minfilia holds the broken Tupsimati.", "An Uninvited Ascian", "You return to the Rising Stones to find Nabriales already in [[The Solar|the solar]] with Minfilia, the Antecedent clutching the shards of the broken Tupsimati."),
 "M224l": ("Louisoix was branded a pariah in his own land.", "An Uninvited Ascian", "Yet this great soul, whom all should rightly have honored, was branded a pariah in his own land."),
 # #225 In Memory of Moenbryda
 "M225a": ("Moenbryda was a native of Sharlayan, so the Scions gather at the mark of the Scholar.", "In Memory of Moenbryda", "As Moenbryda was a native of Sharlayan, I feel it is only fitting that we gather before the mark of the Scholar."),
 "M225b": ("Midgardsormr's voice calls it life for death, a fair exchange, and promises other bargains.", "In Memory of Moenbryda", "Life for death. A fair exchange. … Other bargains will be struck."),
 "M225c": ("Minfilia names the dead: Louisoix, Moenbryda and the Scions at the Waking Sands.", "In Memory of Moenbryda", "The battles we have fought have taken the lives of so many. Louisoix. Moenbryda. Our fellows at the Waking Sands."),
 "M225d": ("Minfilia calls you her pillar of strength.", "In Memory of Moenbryda", "You are ''my'' pillar of strength, and I fear I shall have need of your steadfast presence in the days to come..."),
 # #226 Mask of Grief
 "M226a": ("Minfilia is concerned for Yda after Moenbryda's death.", "Mask of Grief", "Minfilia expresses concern over [[Yda]]'s emotional state following the loss of [[Moenbryda]]."),
 "M226b": ("Yda ordered a rare flower in memory of her friend.", "Mask of Grief", "You learn that she has ordered a [[Moon Daisy|rare flower]] in memory of her friend"),
 "M226c": ("As Yda lays the flower at the mark of the Scholar, Dravanian wings darken the sky.", "Mask of Grief", "As Yda places the moon daisy before the mark of the Scholar, the skies over Rathefrost are suddenly darkened by the passing of [[Dravanian]] wings."),
 "M226d": ("An envoy from the Holy See is on the way with an urgent report.", "Mask of Grief", "an envoy from the [[Holy See]] is already en route to [[the Scions]]' headquarters, bearing an urgent report..."),
 # #227 Defenders for Ishgard
 "M227a": ("The envoy from Ishgard is Lucia, Aymeric's second-in-command.", "Defenders for Ishgard", "The envoy from Ishgard turns out to be [[Lucia]], Ser [[Aymeric]]'s second-in-command."),
 "M227b": ("The Dravanians were forced back, at the cost of many Ishgardian lives.", "Defenders for Ishgard", "Though the beasts were ultimately forced into retreat, our victory─if such it may be called─came at the cost of many of our own."),
 "M227c": ("Lucia seeks the aid of the Crystal Braves and the Grand Companies.", "Defenders for Ishgard", "has come to seek the aid of the [[Crystal Braves]] and the [[Grand Companies]] in bolstering her city's defenses."),
 "M227d": ("Minfilia warns that any support will be conditional.", "Defenders for Ishgard", "In the event that your plea does receive a favorable answer, know that any support is certain to be conditional."),
 "M227e": ("Alphinaud warns the Braves' commitment to Ul'dah must come first.", "Defenders for Ishgard", "I must warn you, however, that the involvement of the Crystal Braves is by no means assured─our commitment to quelling the unrest in Ul'dah must take precedence."),
 "M227f": ("A heretic force broke the outer defenses and dispelled the first of Ishgard's wards.", "Defenders for Ishgard", "a heretic force has broken through the outer defenses and dispelled the first layer of arcane wards protecting the city of Ishgard."),
 "M227g": ("Lady Iceheart and her followers attacked the knights at the Gates of Judgement.", "Defenders for Ishgard", "You learn from the knights stationed at the Gates of Judgement that they were attacked by Lady [[Iceheart]] and her followers."),
 "M227h": ("Iceheart says the sons must answer for their fathers' misdeeds.", "Defenders for Ishgard", "The sons must answer for their fathers' misdeeds."),
 # #228 The Wyrm's Roar
 "M228a": ("Iceheart and the Dravanians share one goal: reclaiming Nidhogg's stolen eye.", "The Wyrm's Roar", "'Twould seem that Lady Iceheart and the Dravanians share a common goal─the reclamation of Nidhogg's stolen eye."),
 "M228b": ("Haldrath took the Eye from Nidhogg's skull, and it is a treasured relic of Ishgard.", "The Wyrm's Roar", "The trophy Haldrath plucked from the bested wyrm's skull─known simply as “the Eye”─is a treasured relic of Ishgard, and one possessed of untold power."),
 "M228c": ("Nidhogg has terrorized Coerthas since Ishgard's founding.", "The Wyrm's Roar", "Though once defeated by the hero Haldrath, the beast is said to have terrorized Coerthas since Ishgard's founding."),
 "M228d": ("Aymeric presents Ishgard's Azure Dragoon, Estinien.", "The Wyrm's Roar", "May I present to you Ishgard's Azure Dragoon."),
 "M228e": ("Through the Eye, Estinien has become the vessel of Nidhogg's strength.", "The Wyrm's Roar", "Through the power of the Eye, I have become the vessel of Nidhogg's strength."),
 "M228f": ("Nidhogg means to hurl his Horde against Daniffen's Collar and shatter the remaining wards.", "The Wyrm's Roar", "He means to hurl his Horde against Daniffen's Collar, and shatter the remaining wards that protect the city."),
 "M228g": ("If Ishgard falls, the Empire would claim Coerthas.", "The Wyrm's Roar", "Until the Garleans' arrival, that is─for you may be certain that the Empire would not hesitate to claim Coerthas."),
 "M228h": ("Alphinaud pledges that Eorzea will not leave Ishgard to face the Horde alone.", "The Wyrm's Roar", "we of Eorzea will not abandon our Ishgardian brothers to face the coming Horde alone."),
 # #229 Committed to the Cause
 "M229a": ("The main Dravanian host advances on Ishgard.", "Committed to the Cause", "Indeed. The main host advances upon Ishgard as we speak."),
 "M229b": ("Ishgard's defenses have been nullified.", "Committed to the Cause", "Whose vaunted defenses have been nullified."),
 "M229c": ("The Scions and the Crystal Braves commit to the defense of Ishgard.", "Committed to the Cause", "Along with the [[Crystal Braves]], [[the Scions of the Seventh Dawn]] have committed themselves to the defense of Ishgard."),
 "M229d": ("Minfilia makes plain that the Scions would be directly intervening in the war.", "Committed to the Cause", "Let there be no ambiguity about what has been proposed. We would be directly intervening in the war."),
 "M229e": ("Riol is uneasy about private words between Ilberd and Yuyuhase.", "Committed to the Cause", "it appears that [[Riol]] is more concerned by the private words passing between [[Ilberd]] and [[Yuyuhase]]"),
 "M229f": ("Alphinaud will ask the Alliance council to contribute forces.", "Committed to the Cause", "I shall inform the council of our intentions, and request that they contribute their own forces to the defense of Ishgard."),
 # #230 Volunteer Dragonslayers
 "M230a": ("Minfilia asks you to gather adventurers for the coming siege.", "Volunteer Dragonslayers", "I would have you reach out to your fellow adventurers, and gather what allies you may for the coming siege."),
 "M230b": ("The Adventurers' Guild will have no official presence at the siege.", "Volunteer Dragonslayers", "There will be no official Adventurers' Guild presence at this siege."),
 "M230c": ("Wilred, the youth from Little Ala Mhigo, has disappeared.", "Volunteer Dragonslayers", "the disappearance of [[Wilred]], the youth from [[Little Ala Mhigo]]."),
 "M230d": ("Black-market weapons went missing from the Braves' vault when Wilred stopped turning up for duty.", "Volunteer Dragonslayers", "Around the time Wilred stopped turnin' up for duty, them black market weapons went missin' from our vault in Ul'dah..."),
 "M230e": ("Riol believes a villain other than Wilred is behind it.", "Volunteer Dragonslayers", "Aye, there's a villain at the end o' this trail I've stumbled on, an' I'll bet me good eye it ain't young Wilred."),
 "M230f": ("Wilred had reported that the Braves' numbers did not add up.", "Volunteer Dragonslayers", "Somethin' about the Braves' numbers not addin' up..."),
 "M230g": ("Only three or four volunteers come forward.", "Volunteer Dragonslayers", "One or two, eh? Well, added to mine, that makes three or four, not including Slafborn's friends!"),
 # #231 An Allied Perspective
 "M231a": ("The Alliance leaders refuse meaningful assistance and suggest hiring elite adventurers.", "An Allied Perspective", "the leaders refuse to provide meaningful assistance, and suggest instead that you assemble a contingent of elite [[adventurer]]s"),
 "M231b": ("Merlwyb puts Limsa first, then the Alliance, then Ishgard.", "An Allied Perspective", "Lest you doubt, Limsa comes first, then the Alliance, and finally─circumstances permitting─Ishgard and the rest."),
 "M231c": ("Raubahn proposes leaving Ul'dah's security to the Brass Blades to send a larger force.", "An Allied Perspective", "If we entrust the security of Ul'dah to the Brass Blades for a time, we can dispatch a larger force to Ishgard."),
 "M231d": ("Merlwyb gives Alphinaud the Crystal Braves to command.", "An Allied Perspective", "The Crystal Braves are yours to command, Alphinaud. Do what you will."),
 "M231e": ("The Dravanians have begun their assault on Coerthas.", "An Allied Perspective", "It would seem the [[Dravanians]] have begun their assault on [[Coerthas]]."),
 "M231f": ("Alphinaud sends the Braves to join House Durendaire at the Steel Vigil.", "An Allied Perspective", "Move our forces into position. Your unit will join House Durendaire at the Steel Vigil."),
 "M231g": ("The adventurer reinforcements are decimated.", "An Allied Perspective", "''Decimated'', you say? Dravanian devils! Damn their scaly hides!"),
 "M231h": ("Kan-E-Senna fears Teledji and his ilk would seize Gridania's territories in Carteneau.", "An Allied Perspective", "We dare not leave our interests in Carteneau undefended as well. Teledji Adeledji and his ilk would seize control of the territories in our absence."),
 "M231j": ("Kan-E-Senna speaks for Gridania at the council.", "An Allied Perspective", "Gridania does not object."),
 "M231i": ("Kan-E-Senna can commit only a token force.", "An Allied Perspective", "Would that we could commit more than a token force to this cause."),
 # #232 The Steps of Faith
 "M232a": ("Iceheart's damage to Ishgard's barrier lets the dragons land on the Steps of Faith.", "The Steps of Faith", "the damage [[Iceheart]] inflicted on Ishgard's arcane barrier has allowed the [[dragon]]s to land directly upon [[the Steps of Faith]]"),
 "M232b": ("The bridge is the foundation of the wards of Daniffen's Collar.", "The Steps of Faith", "More than simply a means to cross the Sea of Clouds, the bridge serves as a foundation for the arcane wards that form the barrier we call Daniffen's Collar."),
 "M232c": ("Estinien sees one of Nidhogg's greatest champions slain.", "The Steps of Faith", "One of Nidhogg's greatest champions...slain."),
 "M232d": ("You drive the Dravanian Horde from the Steps of Faith.", "The Steps of Faith", "You have succeeded in driving the Dravanian Horde from the Steps of Faith."),
 "M232e": ("Alphinaud declares the stage set for Ishgard's return to the Alliance.", "The Steps of Faith", "Alphinaud triumphantly declares that the stage has been set for Ishgard's return to the [[Eorzean Alliance]]"),
 "M232f": ("Aymeric thanks you on behalf of the Holy See and the people of Ishgard.", "The Steps of Faith", "On behalf of the Holy See and the people of Ishgard, I offer you my humble thanks."),
 "M232g": ("The siege is ended.", "The Steps of Faith", "Ishgard's weary defenders breathe a sigh of relief. The siege is ended."),
 "M232h": ("Papalymo and Yda join the rearguard.", "The Steps of Faith", "I think it prudent we divide into two groups. Yda and I will join the rearguard."),
 "M232i": ("You aid the Temple Knights in defending the bridge against the Dravanian Horde.", "The Steps of Faith", "aid the [[Temple Knights]] in defending the vital structure against the [[Dravanian Horde]]"),
 # #233 Administrative Decision
 "M233a": ("A royal invitation asks the Scions to a feast at Ul'dah's Royal Palace in honor of Ishgard's victory.", "Administrative Decision", "invites the Scions of the Seventh Dawn to attend a feast at the Royal Palace of Ul'dah...in honor of Ishgard's recent victory."),
 "M233b": ("The Alliance leaders sent sellswords, many of whom died before the siege began.", "Administrative Decision", "All three refused to deploy their standing armies, preferring to send hastily assembled companies of sellswords, many of whom perished ere the siege began."),
 "M233c": ("Minfilia suspects the feast is a chance to press for Ishgard's return to the Alliance.", "Administrative Decision", "Such an occasion would present a fine opportunity to press for Ishgard's return to the Eorzean Alliance."),
 "M233d": ("Tataru asks for leave to study a fighting discipline.", "Administrative Decision", "Citing a need for some measure of martial prowess, Tataru requests a leave of absence to study her chosen discipline."),
 "M233e": ("Tataru wants the power to defend herself.", "Administrative Decision", "And so it seems only right that I, too, should acquire the power to defend myself!"),
 "M233f": ("Minfilia is in no mood to celebrate so soon after Moenbryda's death.", "Administrative Decision", "We have scarce had time to mourn Moenbryda, and I, for one, am in no mood to carouse."),
 # #234 An Unexpected Ambition
 "M234a": ("Minfilia suspects Tataru has taken up arcanima.", "An Unexpected Ambition", "Minfilia surmises that [[Tataru]] may have taken up the [[Arcanist|study of arcanima]]."),
 "M234b": ("Tataru's Carbuncle abandons her to wild beasts.", "An Unexpected Ambition", "Wild beasts soon approach, and she steels herself for battle─only to be abandoned by her [[Carbuncle]]."),
 "M234c": ("Tataru admits she will never be a warrior.", "An Unexpected Ambition", "I'll never be a warrior like you or the others."),
 # #235 Ancient Ways, Timeless Wants
 "M235a": ("Tataru means to make charms for the Scions from the blood pearls she harvested.", "Ancient Ways, Timeless Wants", "Tataru reveals her intent to use the blood pearls she has harvested to fashion charms for her fellow [[Scions]]."),
 "M235b": ("Tataru hopes the charms will bring everyone home.", "Ancient Ways, Timeless Wants", "I thought I might make charms for everyone...so that no matter where they go, they will always come home."),
 "M235c": ("Minfilia concludes Tataru benefited from the attempt.", "Ancient Ways, Timeless Wants", "Minfilia concludes that despite Tataru's failure to become an [[arcanist]], she nevertheless benefited from the experience."),
 # #234 Where We Are Needed (the other path)
 "M234ba": ("The Scions employ scholars to take aetheric readings across Eorzea.", "Where We Are Needed", "employ [[scholar]]s to travel across [[Eorzea]] taking [[aether]]ic readings"),
 "M234bb": ("A scholar finds that ambient aether has decreased since the Calamity.", "Where We Are Needed", "there has been a widespread decrease in ambient aether concentrations following [[the Calamity]]"),
 "M234bc": ("The scholar wants more measurements.", "Where We Are Needed", "We must take additional measurements to confirm my assessment."),
 # #235 The Least among Us
 "M235ba": ("The scholar finds the body of Wilred, the young Ala Mhigan you recruited to the Crystal Braves.", "The Least among Us", "the young [[Ala Mhigan]] whom you personally recruited to the [[Crystal Braves]]"),
 "M235bb": ("Wilred was murdered, by whom and why no one knows.", "The Least among Us", "they conclude that the boy was murdered─though by whom and for what reason they can only speculate"),
 "M235bc": ("No Crystal Brave operation was known in the area.", "The Least among Us", "I've heard nothing of any Crystal Brave operations in this area."),
 "M235bd": ("Minfilia will send word to Alphinaud.", "The Least among Us", "I will send word to Alphinaud at once."),
 # #238 A Time to Every Purpose
 "M238a": ("Minfilia leaves for Ul'dah to meet the other Scions.", "A Time to Every Purpose", "And so she departs for [[Ul'dah]] to rendezvous with the other Scions, instructing you to follow when you are ready."),
 "M238b": ("Riol has evidence that Teledji bribed members of the Braves' 1st and 3rd Units.", "A Time to Every Purpose", "uncovered evidence that [[Teledji Adeledji]] has bribed members of the 1st and 3rd Units"),
 "M238c": ("The Braves' donors were fronts owned by the Mirage Trust.", "A Time to Every Purpose", "all were owned by the Mirage Trust."),
 "M238d": ("Riol believes the bribed Braves killed Wilred.", "A Time to Every Purpose", "I'd wager me right eye they're the ones what did for Wilred."),
 "M238e": ("Riol vows to purge the traitors from the Braves.", "A Time to Every Purpose", "We'll purge every one o' them traitorous bastards from our ranks!"),
 "M238f": ("Four nations prepare to celebrate Ishgard's defense.", "A Time to Every Purpose", "As four great nations stand poised to commemorate the successful defense of [[Ishgard]]"),
 "M238g": ("You are needed at the Quicksand.", "A Time to Every Purpose", "It would seem that your presence is required at [[the Quicksand]]"),
 # #239 Come, but Not Gone
 "M239a": ("Alianne of the 4th asks for a private meeting to show you something.", "Come, but Not Gone", "[[Alianne]] of the 4th has requested a private meeting so that she might show you something of importance."),
 "M239b": ("Alianne never comes, and you find a vial at your feet.", "Come, but Not Gone", "you chance to catch sight of [[Clouded Vial|a vial]] at your feet"),
 "M239c": ("Another Brave has seen no sign of Alianne.", "Come, but Not Gone", "He tells you that he has seen no sign of Alianne on his patrol"),
 "M239e": ("Another Brave knows her as Lieutenant Alianne.", "Come, but Not Gone", "Lieutenant Alianne? Why no, I haven't seen her about..."),
 "M239d": ("Nanamo laments that through her weakness the House of Ul has all but vanished.", "Come, but Not Gone", "Through my weakness, the glorious House of Ul has all but disappeared beneath the sands."),
 # #240 The Parting Glass
 "M240a": ("Nanamo tells you she means to abdicate and establish a republic.", "The Parting Glass", "In private, [[Nanamo|the sultana]] reveals to you her intent to abdicate the throne and establish a fair and equitable republic."),
 "M240b": ("Nanamo asks you to support Raubahn in the days ahead.", "The Parting Glass", "she asks that you support [[Raubahn]] however you can in the days ahead"),
 "M240c": ("Nanamo drinks the wine and collapses.", "The Parting Glass", "Nanamo drinks the wine and collapses."),
 "M240d": ("Teledji proclaims the sultana murdered with poison.", "The Parting Glass", "[[Teledji]] proclaims to all and sundry that Her Royal Majesty Nanamo Ul Namo has been murdered with poison"),
 "M240e": ("Captain Ilberd delivers you bound, accused of regicide.", "The Parting Glass", "Captain [[Ilberd]] of the [[Crystal Braves]] delivers you bound into [[the Fragrant Chamber]] and declares that you stand accused of regicide."),
 "M240f": ("Yuyuhase tells Alphinaud the Braves strive for the salvation of Eorzea.", "The Parting Glass", "Why, that which we have striven for all along, Commander: the salvation of Eorzea."),
 "M240g": ("An urgent message from the Holy See arrives.", "The Parting Glass", "We have received an urgent message from the Holy See."),
 "M240h": ("Teledji goads Raubahn, who cuts him down.", "The Parting Glass", "Unable to resist, he goads the Bull of Ala Mhigo into action, and is cleft in twain for his troubles"),
 "M240i": ("When Raubahn advances on Lolorito, Ilberd severs his arm.", "The Parting Glass", "Raubahn then advances upon [[Lolorito]]─only to be taken unawares by Ilberd, who severs his arm with a single practiced stroke."),
 "M240j": ("Ilberd claims credit for the sultana's murder.", "The Parting Glass", "going so far as to claim credit for Nanamo's murder"),
 "M240k": ("Raubahn bids you find out who is behind the plot.", "The Parting Glass", "Find out who is behind this plot! It is the only way! Now go!"),
 "M240l": ("Pipin is Vice Marshal of the Immortal Flames and Raubahn's adopted son.", "The Parting Glass", "Together with [[Pipin Tarupin]]─Vice Marshal of [[the Immortal Flames]], and Raubahn's adopted son─you flee to [[Black Brush]]"),
 "M240m": ("Cid comes to spirit you away aboard the Enterprise.", "The Parting Glass", "who is prepared to spirit you away from [[Thanalan]] aboard the ''Enterprise''"),
 "M240n": ("You land near Camp Dragonhead, and Alphinaud proposes seeking Haurchefant's counsel.", "The Parting Glass", "you disembark near [[Camp Dragonhead]], where a downcast Alphinaud proposes you seek Lord [[Haurchefant]]'s counsel."),
 "M240o": ("Pipin swears to do what he can to clear your names.", "The Parting Glass", "who swears to do what he can to clear your names"),
 "M240q": ("Raubahn bids you and the Scions escape and clear your names.", "The Parting Glass", "Raubahn bids you and [[the Scions]] escape─to clear your names and see justice done"),
 "M240r": ("One by one, your comrades stay behind to hold back the pursuit.", "The Parting Glass", "One by one, your comrades choose to remain and hold back the tide of pursuers"),
 "M240s": ("Pipin is Raubahn's adopted son.", "The Parting Glass", "Yes, I am his son. Adopted, of course."),
 "M240t": ("Yda stays to hold off the pursuers.", "The Parting Glass", "The rest of you go on ahead. I'll handle this lot!"),
 "M240u": ("Papalymo stays with Yda to hold the pursuers.", "The Parting Glass", "We will hold our pursuers here. Hurry, now! Find this tunnel of Thancred's!"),
 "M240v": ("Y'shtola means to bring the tunnel down on the pursuers.", "The Parting Glass", "Numbers will count for little when I bring the tunnel down upon their heads."),
 # Before the Dawn (MSQ #241, the cp-arr-2-55 milestone)
 "M241a": ("The Dravanians renewed their assault on Ishgard, and wyverns broke into the city.", "Before the Dawn", "the [[Dravanian]]s renewed their assault on [[Ishgard]] in your absence, and that several [[wyvern]]s broke free into the city proper"),
 "M241b": ("Your petition for asylum will wait until the threat to Ishgard diminishes.", "Before the Dawn", "your petition for asylum will not be heard until the threat to Ishgard has diminished"),
 "M241c": ("Aymeric is back from Ul'dah and again leads Ishgard's defense.", "Before the Dawn", "Ser Aymeric is safely returned from Ul'dah and once more leads the defense of Ishgard."),
 "M241d": ("House Fortemps will aid no one who comes searching for you.", "Before the Dawn", "any who come here in search of you will receive no aid from House Fortemps."),
 "M241e": ("Raubahn is shown in a prison cell.", "Before the Dawn", "A short scene plays of Raubahn in a prison cell."),
 "M241f": ("Elidibus says Nabriales is no more.", "Before the Dawn", "Nabriales is no more."),
 "M241g": ("Lahabrea says the Ardor was not Nabriales's to invoke, and his demise was his own making.", "Before the Dawn", "The Ardor was not his to invoke. His demise was of his own making."),
 "M241h": ("Elidibus turns their thoughts to the northern lands.", "Before the Dawn", "The northern lands, then?"),
 "M241i": ("At Ishgard's gates Midgardsormr says you will find only delusion, despair and death.", "Before the Dawn", "Delusion. Despair. Death. Thou shalt find naught else here."),
 "M241j": ("The Temple Knights slew the wyverns.", "Before the Dawn", "The Temple Knights succeeded in slaying the beasts"),
}

# ---- New entities --------------------------------------------------------------------------------------------------
ARC1, ARC2, ARC3, ARC4, ARC5 = (
    "evt-spies-and-heretics", "evt-saint-of-the-heretics", "evt-blade-for-the-ascians", "evt-horde-at-the-gates", "evt-royal-banquet")
N1, N2, N3, N4, N5 = "Spies and Heretics", "The Saint of the Heretics", "A Blade for the Ascians", "The Horde at the Gates", "The Royal Banquet"

ENTITIES = {
 ARC1: "event", ARC2: "event", ARC3: "event", ARC4: "event", ARC5: "event",
 # Characters (several may already exist from 2.1–2.3; the IDs follow the contract so they merge)
 "char-ilberd": "character", "char-raubahn": "character", "char-nanamo": "character", "char-teledji": "character",
 "char-lolorito": "character", "char-kan-e-senna": "character", "char-merlwyb": "character", "char-yugiri": "character",
 "char-aymeric": "character", "char-lucia": "character", "char-estinien": "character", "char-iceheart": "character",
 "char-shiva": "character", "char-eline": "character", "char-ivy": "character", "char-varis": "character",
 "char-moenbryda": "character", "char-midgardsormr": "character", "char-nidhogg": "character", "char-nabriales": "character",
 "char-elidibus": "character", "char-yuyuhase": "character", "char-alianne": "character",
 "char-wilred": "character", "char-pipin": "character",
 # Groups and places
 "org-immortal-flames": "organization", "org-monetarists": "organization", "org-heretics": "organization",
 "org-temple-knights": "organization", "org-dravanian-horde": "organization", "org-holy-see": "organization",
}

LEAD1 = "Alphinaud commands the newly formed Crystal Braves, with Captain Ilberd as his second-in-command. "
LEAD1B = "Iceheart's heretics seized a House Fortemps caravan's crystals, and Alphinaud believes they mean to summon Shiva, their patron saint, as a beast tribe would a primal. "
LEAD5 = "The Scions are invited to a royal feast in Ul'dah in honor of Ishgard's victory. "

PRES = {
 # ---- Arc entries: one recap per step ----
 ARC1: [
   P(S(200), None, "main", N1,
     LEAD1 + "Ilberd revealed that a Garlean spy known as the Ivy has planted conspirators in the Immortal Flames, and took you to his old friend and rival Raubahn, a Flame General, "
     "who wonders whether the Monetarists have long been in league with the Empire. Both men will keep digging, for Ilberd fears the Empire will soon march on Eorzea again.",
     ["C16", "M200b", "M200d", "M200e", "M200f", "M200g", "M200h"]),
   P(S(201), None, "main", N1,
     LEAD1 + "Their hunt for the Ivy, a Garlean spy in the Immortal Flames, has begun. When Garleans ambushed a unit of Braves, you helped Alianne of the 4th Unit free its captured comrade from Castrum Centri. "
     "Now Alphinaud has an audience with an Ishgardian dignitary who asked for you.",
     ["C16", "M200b", "M201a", "M201f", "M201e", "M201b", "M201c"]),
   P(S(202), None, "main", N1,
     "With Alphinaud you met Ser Aymeric, lord commander of Ishgard's Temple Knights, at Camp Dragonhead. The Holy See will not rejoin the Eorzean Alliance, but Aymeric will keep House Fortemps' aid flowing to Revenant's Toll "
     "if the Scions help watch the remains of Midgardsormr, whose return Ishgard's astrologians foretell. Then word came that Iceheart and her heretics had waylaid the latest shipment. "
     "Meanwhile Captain Ilberd hunts the Ivy, a Garlean spy in the Immortal Flames.",
     ["M202a", "M202b", "M202d", "M202c", "M202e", "M200b", "M201d"]),
   P(S(203), None, "main", N1,
     "Disguised as pilgrims, Iceheart's heretics slaughtered a House Fortemps caravan's guards and seized every crate of crystals. A survivor heard them speak of deliverance and resurrection, "
     "and Alphinaud believes they mean to summon Shiva, their patron saint, as a beast tribe would a primal. He has turned the whole order to preventing it. Captain Ilberd still hunts the Ivy, a Garlean spy.",
     ["M203a", "M203b", "M203c", "M203g", "M203e", "M203f", "M200b"]),
   P(S(204), None, "main", N1,
     LEAD1B + "At Whitebrim Front, Lord Drillemont reported that his scouts lost a band of heretic pilgrims at Snowcloak. Ser Aymeric's knights have joined the hunt for Iceheart, "
     "Alphinaud summoned a unit of Crystal Braves, and the Scions are helping.",
     ["M203a", "M203e", "M204a", "M204b", "M204c", "M204d"]),
   P(S(205), None, "main", N1,
     LEAD1B + "Lord Drillemont's covert check of Whitebrim Front turned up one possible heretic. You shadowed him to a meeting with a heretic who knew the movements of the Temple Knights and the Crystal Braves "
     "and spoke of tunnels in Boulder Downs. The traitor is detained, and Drillemont means to root out the heretics there.",
     ["M203e", "M205a", "M205b", "M205c", "M205d"]),
   P(S(206), None, "main", N1,
     LEAD1B + "In Boulder Downs you found House Durendaire's knights slain and the heretics waiting. A timetable of the watches at Snowcloak, found on one of them, shows the heretics may already be in position to strike, "
     "and Lord Drillemont is sending reinforcements.",
     ["M203e", "M205c", "M206a", "M206b", "M206c", "M206d"]),
   P(S(207), None, "main", N1,
     "Iceheart's heretics mean to summon Shiva, their patron saint, as a primal. At Snowcloak Ser Aymeric was ready for them, and Alphinaud found a tunnel to Iceheart's lair. "
     "There she told you she was given the name Ysayle but earned the name Iceheart, and vowed to end the war between dragon and man at any cost. "
     "She escaped by aetheryte, but you drove her heretics out, and Minfilia and Urianger are searching House Fortemps' archives for word of Shiva.",
     ["M203e", "M207a", "M207b", "M207c", "M207d", "M207e", "M207f"]),
   P(S(208), None, "main", N1,
     "Iceheart, once known as Ysayle, escaped Snowcloak by aetheryte and likely destroyed the second one behind her. Minfilia is sure Shiva, whom the heretics would summon, was a living woman. "
     "Chasing the heretics with Yuyuhase of the Braves' 3rd Unit led to a merchant caught outside the Observatorium, whom Ilberd and Alphinaud had sought in their hunt for the Ivy: the Garlean spy may have aided Iceheart. "
     "Yugiri, a Doman whose shinobi helped uncover the link, has joined the search.",
     ["M207c", "M208b", "M208a", "M208h", "M208d", "M208c", "M208f", "M208e"]),
   P(S(209), None, "main", N1,
     "A Flame at Revenant's Toll sold caravan routes to a merchant who passed them to Iceheart's heretics, and the Ivy, the Garlean spy behind it, covered the trail with powers held only by high-ranking Flames. "
     "At an emergency Alliance council in Gridania you learned that Varis has seized the Garlean throne, and the Alliance fears a new march on Eorzea. Iceheart's sanctum is still out of reach. "
     "Now Captain Ilberd says the Ivy is unmasked.",
     ["M209a", "M209b", "M209i", "M209c", "M209d", "M209e", "M209f"]),
   P(S(210), None, "main", N1,
     "Captain Ilberd named the Ivy, the Garlean spy in the Immortal Flames, as Flame Marshal Eline, Raubahn's second-in-command and the highest-ranked foreigner in the company. "
     "She was in Gridania when she should have been at the Hall of Flames, and while you shadowed her she slipped out disguised as a merchant, though a Doman shinobi saw through it. "
     "Ilberd wonders whether the Ivy has some hold over the Monetarists.",
     ["M210a", "M210b", "M210d", "M210e", "M210c"]),
   P(S(211), None, "main", N1,
     "Alliance jamming devices from the Ironworks force imperial agents to meet in person, and Yugiri's shinobi guard them. In the East Shroud, Captain Ilberd arrested Flame Marshal Eline, the Ivy, for treason and espionage "
     "as she met an imperial intermediary. She offered no struggle, but Yugiri reads that as knowing her position was untenable. Meanwhile Minfilia reports progress toward a way into Iceheart's sanctum.",
     ["M211a", "M211b", "M211c", "M211d", "M211e", "M211f"]),
 ],
 ARC2: [
   P(S(212), None, "main", N2,
     "Iceheart, the heretic leader once known as Ysayle, means to summon Shiva with crystals stolen from House Fortemps, at a sanctuary she reached by aetheryte. Minfilia expects something more akin to a primal than a saint. "
     "She called in Moenbryda, a Sharlayan scholar and authority on aetherytes, who proposes recreating the lost beacon, though everyone who has teleported that way has died. "
     "Flame Marshal Eline, the Garlean spy, is under arrest.",
     ["M207c", "M212a", "M212b", "M212c", "M212e", "M212f", "M211c"]),
   P(S(213), None, "main", N2,
     "Through Moenbryda's white auracite the Scions woke the aetheryte at Snowcloak, opening a path to Iceheart's sanctuary. There Iceheart offered her own body as a vessel for Shiva's soul. "
     "You defeated the primal, and Iceheart withdrew, telling you to seek the Keeper of the Lake and see with eyes unclouded. An unseen figure remarked that Lahabrea will be pleased, "
     "and you wonder whether Hydaelyn speaks to your enemy too.",
     ["M213a", "M213b", "M213c", "M213d", "M213e", "M213f"]),
   P(S(214), None, "main", N2,
     "You defeated Shiva, whom Iceheart summoned into her own body, but Iceheart escaped. Ishgard has shared what it learned from the heretics and the captured merchant, and Ser Aymeric formally introduced his second-in-command, "
     "Lucia, who owes no allegiance to any noble house. He calls Ishgard's arrangement with Revenant's Toll mutually beneficial; Alphinaud suspects Ishgard of manipulating its neighbors.",
     ["M213b", "M214f", "M214h", "M214c", "M214d", "M214i", "M214g"]),
   P(S(215), None, "main", N2,
     "Iceheart summoned Shiva into her own body; you defeated the primal, and she escaped. Alphinaud warns that if civilized peoples can summon primals, the Alliance could face all Garlemald. "
     "At the Rising Stones, Moenbryda confirmed it was a primal, Minfilia wondered whether Iceheart has the Echo, and Urianger noted how few know the secrets of summoning. "
     "Iceheart's parting words give the Scions another reason to watch the Keeper of the Lake.",
     ["M213b", "M215a", "M215b", "M215d", "M215c", "M215h", "M215g"]),
   P(S(216), None, "main", N2,
     "Flame Marshal Eline, the Garlean spy, escaped her cell in Ul'dah with inside help, leaving the turnkey and two guards dead, and fled for Castrum Meridianum. "
     "Captain Ilberd's Braves and you ran her down, and Ilberd sent her back to Ul'dah for trial, telling her that he sold his sword but she sold her comrades. "
     "Meanwhile, in Ul'dah, Teledji has ordered the Blades to watch Raubahn and the Flames day and night.",
     ["M216a", "M216b", "M216c", "M216d", "M216f", "M216g", "M216h"]),
   P(S(217), None, "main", N2,
     "Eline, the captured spy, once aided the Scions at their founding; Raubahn names Emperor Varis her true master, and she also sold imperial secrets to a faction in Eorzea. "
     "Moenbryda and Urianger believe a burst of pure aether can undo an Ascian soul, but white auracite holds aether only briefly. The Isle of Val has been erased from existence. "
     "Sultana Nanamo told the Alliance leaders that Ul'dah will become a republic, asking them to help Raubahn keep order.",
     ["M217a", "M217f", "M217e", "M217c", "M217b", "M217d", "M217h", "M217k"]),
 ],
 ARC3: [
   P(S(218), None, "main", N3,
     "The Scions want an aetherial blade that can destroy an Ascian's soul, but Moenbryda and Urianger still cannot form one at will, and Minfilia knows Shiva will not be the last primal. "
     "Alphinaud is staying in Ul'dah, where his Crystal Braves support the Immortal Flames, shaken by the spy found among their officers. "
     "Riol traced a large weapons purchase to a black marketeer, and you are to meet Captain Ilberd at Highbridge to stop the deal.",
     ["M218c", "M218b", "M218a", "M218d", "M218e"]),
   P(S(219), None, "main", N3,
     "Moenbryda and Urianger are still working on an aetherial blade against the Ascians. Riol's tip led you and Captain Ilberd to a black marketeer's deal at the Burning Wall, but it went wrong: "
     "one of Ilberd's men killed the seller, the buyers slipped past the 1st Unit's perimeter, and only a single crate of weapons was found.",
     ["M218c", "M218d", "M219a", "M219b", "M219c", "M219d"]),
   P(S(220), None, "main", N3,
     "Moenbryda and Urianger are still working on an aetherial blade against the Ascians. You delivered the one crate from Captain Ilberd's failed raid to Yuyuhase of the 3rd Unit, who blamed Riol's intelligence. "
     "Riol insists the buyer did purchase the weapons, and notes that the Braves' 1st and 3rd Units now spend freely. Tataru has called you back: a guest from Ishgard wants to see you.",
     ["M218c", "M219d", "M220a", "M220b", "M220c", "M220d"]),
   P(S(221), None, "main", N3,
     "Lucia, Ser Aymeric's second-in-command, asked you to examine the Keeper of the Lake, for Ishgard's astrologians foresee Midgardsormr's return, a great wyrm slain in the explosion after Eorzea's victory there. "
     "Atop the wreck you fought him; when Hydaelyn marked you as Her chosen he relented, but stripped you of the Mothercrystal's blessing. A covenant binds him to you, and he says his children sing of Ishgard's destruction. "
     "The Scions can only wait for Ishgard to ask for aid.",
     ["M221a", "M221b", "M221c", "M221d", "M221e", "M221f", "M221g", "M221j"]),
   P(S(222), None, "main", N3,
     "Midgardsormr stripped you of the Mothercrystal's blessing. An Ascian's soul does not return to the aetherial realm when its host falls, so Moenbryda plans to forge a blade against them by siphoning aether "
     "from corrupted crystals across Eorzea. Meanwhile the XIVth Legion, cut off from the Empire, has been reinforced from Castrum Centri; Minfilia sent Alphinaud, Thancred and Papalymo to back the Crystal Braves "
     "at the Ceruleum Processing Plant, where explosives of imperial design were found hidden.",
     ["M221e", "M222a", "M222b", "M222c", "M222d", "M222e"]),
   P(S(223), None, "main", N3,
     "Moenbryda is testing her plan to siphon aether for a blade against the Ascians. At the Ceruleum Processing Plant, small imperial squads struck from Castrum Meridianum; Captain Ilberd brought the 3rd Unit out of Ul'dah, "
     "and with Yuyuhase you destroyed the squads on the western approach. The plant is safe.",
     ["M222b", "M223a", "M223b", "M223d", "M223c"]),
   P(S(224), None, "main", N3,
     "Without your blessing of Light, nothing kept the Ascians out of the Scions' domain. The Ascian Nabriales came for Tupsimati, Louisoix's staff, to fuel a new Rejoining, and Minfilia saw that the Isle of Val was his doing. "
     "He carried her off through a rift; you followed and defeated him, Minfilia trapped his soul in white auracite, and Moenbryda spent her own life energy so that your blade could pierce him. Moenbryda is dead.",
     ["M224b", "M224c", "M224i", "M224e", "M224d", "M224f", "M224g", "M224h"]),
   P(S(225), None, "main", N3,
     "Moenbryda gave her life so that your blade could destroy the Ascian Nabriales. The Scions prayed for her at the mark of the Scholar, a Sharlayan monument at Rathefrost, where Midgardsormr's voice called it life for death, "
     "a fair exchange, and promised other bargains. Minfilia mourns Louisoix, Moenbryda and the Scions lost at the Waking Sands, and leans on you as her pillar of strength.",
     ["M224h", "M225a", "M225b", "M225c", "M225d"]),
 ],
 ARC4: [
   P(S(226), None, "main", N4,
     "The Scions mourn Moenbryda, who died destroying an Ascian. Yda ordered a rare flower in her friend's memory, and as she laid it at the mark of the Scholar at Rathefrost, Dravanian wings darkened the sky. "
     "An envoy from the Holy See is on the way with an urgent report from Ishgard.",
     ["M224h", "M226a", "M226b", "M226c", "M226d"]),
   P(S(227), None, "main", N4,
     "The envoy from Ishgard is Lucia, Ser Aymeric's second-in-command. A first Dravanian wave was beaten back at great cost, and she asks the Crystal Braves and the Grand Companies to help defend the city; "
     "Minfilia warns that any aid will be conditional, and Alphinaud that the Braves are committed in Ul'dah. At the Gates of Judgement, knights told you Lady Iceheart and her followers attacked, "
     "and the heretics have dispelled the first of Ishgard's wards.",
     ["M227a", "M227b", "M227c", "M227d", "M227e", "M227g", "M227f"]),
   P(S(228), None, "main", N4,
     "Iceheart's heretics dispelled one of Ishgard's wards. Ser Aymeric told you she and the Dravanians share one goal: Nidhogg's stolen Eye, a relic the hero Haldrath took from the wyrm's skull. "
     "Estinien, Ishgard's Azure Dragoon, has become the vessel of Nidhogg's strength through the Eye, and warns that the wyrm will hurl his Horde against the remaining wards. "
     "If Ishgard falls the Empire would claim Coerthas, and Alphinaud pledged that Eorzea will not leave Ishgard alone.",
     ["M227f", "M228a", "M228b", "M228d", "M228e", "M228f", "M228g", "M228h"]),
   P(S(229), None, "main", N4,
     "Nidhogg's Horde advances on Ishgard, whose wards have been nullified. At the Rising Stones, Minfilia agreed that the Scions will directly intervene in the war alongside the Crystal Braves, "
     "and Alphinaud will ask the Alliance council for forces. Riol noticed Captain Ilberd and Yuyuhase speaking privately.",
     ["M228f", "M229a", "M229b", "M229c", "M229d", "M229f", "M229e"]),
   P(S(230), None, "main", N4,
     "The Scions and the Crystal Braves have committed to defending Ishgard against Nidhogg's Horde. Minfilia sent you to recruit adventurers at Revenant's Toll, but the Adventurers' Guild will send no official presence, "
     "and only a handful volunteered. Riol told you that Wilred, a young Brave, vanished around the time black-market weapons went missing from the Braves' vault, and suspects a villain is behind it.",
     ["M229c", "M230a", "M230b", "M230g", "M230c", "M230d", "M230e"]),
   P(S(231), None, "main", N4,
     "At the Alliance council in Ul'dah, Eorzea's leaders refused meaningful aid to Ishgard: Admiral Merlwyb puts Limsa first, and Kan-E-Senna fears Teledji would seize Gridania's interests in Carteneau. "
     "Merlwyb gave Alphinaud the Crystal Braves to command, and as the Dravanians began their assault on Coerthas he sent them to the Steel Vigil. "
     "Near the Gates of Judgement you fought Dravanian skirmishers, and the adventurer reinforcements were decimated.",
     ["M231a", "M231b", "M231h", "M231d", "M231e", "M231f", "M231g"]),
   P(S(232), None, "main", N4,
     "The damage Iceheart did to Ishgard's barrier let the dragons land on the Steps of Faith, the bridge that anchors the wards of Daniffen's Collar. With the Scions and the Temple Knights you held it; "
     "one of Nidhogg's greatest champions fell, and the Horde was driven off. The siege is ended. Ser Aymeric thanked the Scions on behalf of the Holy See, "
     "and Alphinaud believes the stage is set for Ishgard's return to the Alliance.",
     ["M232a", "M232b", "M232i", "M232c", "M232d", "M232g", "M232f", "M232e"]),
   P(S(233), None, "main", N4,
     "Ishgard's defenders drove off the Dravanian Horde. Sultana Nanamo has invited the Scions to a feast at Ul'dah's Royal Palace in honor of the victory, though the Alliance leaders sent only sellswords, many of whom died "
     "before the siege began. Minfilia, still mourning Moenbryda, suspects the feast is a chance to press Ishgard to rejoin the Alliance. Tataru, troubled, has taken leave to learn to fight.",
     ["M232d", "M233a", "M233b", "M233f", "M233c", "M233d"]),
 ],
 ARC5: [
   P(S(234), None, "main", N5,
     LEAD5 + "Tataru, wanting the power to defend herself, took up arcanima, but in her first trial her Carbuncle abandoned her to wild beasts. She renounced it, admitting she will never be a warrior.",
     ["M233a", "M233e", "M234a", "M234b", "C47b", "M234c"]),
   P(S(235), None, "main", N5,
     LEAD5 + "Tataru gave up arcanima after her Carbuncle abandoned her in her first trial. Instead she harvested blood pearls to make charms for the Scions, so that wherever they go they will always come home, "
     "and Minfilia judges she gained from the attempt.",
     ["M233a", "C47b", "M234b", "M235a", "M235b", "M235c"]),
   P(S234B, None, "main", N5,
     LEAD5 + "Meanwhile the Scions send scholars across Eorzea to take aetheric readings. Guarding one in the South Shroud, you heard him conclude that ambient aether has fallen since the Calamity, though he wants more measurements. "
     "Riol still suspects a villain is behind the weapons missing from the Crystal Braves' vault and the vanished Brave, Wilred.",
     ["M233a", "M234ba", "M234bb", "M234bc", "M230e", "M230c"]),
   P(S235B, None, "main", N5,
     LEAD5 + "At Urth's Fount, a scholar's survey found the body of Wilred, the young Ala Mhigan you recruited to the Crystal Braves, who had vanished after reporting that the Braves' numbers did not add up. "
     "He was murdered, by whom no one knows, and no Brave operation was known there. Minfilia is sending word to Alphinaud.",
     ["M233a", "M235ba", "M230f", "M235bb", "M235bc", "M235bd"]),
   P(S(238), None, "main", N5,
     "Four nations are to celebrate Ishgard's defense at a royal banquet in Ul'dah, and Minfilia has gone ahead to meet the other Scions. Riol has evidence that Teledji bribed members of the Crystal Braves' 1st and 3rd Units "
     "through front companies of the Mirage Trust, and believes those Braves killed Wilred for asking pointed questions. He vows to purge them. Before you could make your entrance, you were called to the Quicksand.",
     ["M238f", "M238a", "M238b", "M238c", "M238d", "M238e", "M238g"]),
   P(S(239), None, "main", N5,
     "The Scions are gathering for the royal banquet in Ul'dah, and Riol believes Braves bribed by Teledji murdered Wilred. Lieutenant Alianne of the 4th asked to meet you privately to show you something, but she never came: "
     "you found a vial at your feet, and another Brave has seen no sign of her. Alone, Sultana Nanamo laments that through her weakness the House of Ul has all but vanished.",
     ["M238a", "M238d", "M239a", "M239e", "M239b", "M239c", "M239d"]),
   P(S(240), None, "main", N5,
     "Before the banquet, Sultana Nanamo told you she means to abdicate and found a republic, and asked you to support Raubahn. She drank wine and collapsed, Teledji proclaimed her poisoned and you the assassin, "
     "Ilberd delivered you bound, and the Crystal Braves turned on Alphinaud. Raubahn cut down the gloating Teledji; Ilberd severed Raubahn's arm and claimed credit for the murder. "
     "The Scions fled, comrades staying behind one by one, until Cid's Enterprise carried you and Alphinaud to Camp Dragonhead.",
     ["M240a", "M240b", "M240c", "M240d", "M240e", "C52", "M240h", "M240j", "M240r", "M240m"]),
   P(B, None, "main", N5,
     "At the banquet in Ul'dah the Scions were accused of poisoning the sultana and branded fugitives, and the Crystal Braves turned on them. Every Scion who attended but you and Alphinaud is unaccounted for, "
     "Raubahn sits in prison, and Alphinaud blames himself. In Coerthas, Lord Haurchefant shelters you while your petition for asylum waits on a renewed Dravanian assault on Ishgard. "
     "Tataru, rescued by Yugiri, has rejoined you, and Urianger has hidden the Waking Sands behind a glamour.",
     ["C50", "C20", "C22", "M241e", "M241a", "M241b", "C53", "C21", "C52b"]),
 ],

 # ---- Characters this era introduces or continues ----
 "char-ilberd": [
   P(S(200), None, "main", "Ilberd",
     "Captain of the Crystal Braves and Alphinaud's second-in-command. He and Raubahn have been friends and rivals since before the fall of Ala Mhigo. "
     "He is hunting the Ivy, a Garlean spy who has planted conspirators in the Immortal Flames, and fears the Empire will soon march on Eorzea again.",
     ["C16", "M200e", "M200b", "M200d", "M200h"], ["Captain Ilberd"]),
   P(S(209), None, "main", "Ilberd",
     "Captain of the Crystal Braves and Alphinaud's second-in-command, and Raubahn's friend and rival since before the fall of Ala Mhigo. His hunt for the Ivy, the Garlean spy in the Immortal Flames, "
     "traced a leak to a Flame at Revenant's Toll and narrowed the spy to someone of high rank. He says the Ivy is now unmasked.",
     ["C16", "M200e", "M209a", "M209b", "M209f"], ["Captain Ilberd"]),
   P(S(211), None, "main", "Ilberd",
     "Captain of the Crystal Braves and Alphinaud's second-in-command, and Raubahn's friend and rival since before the fall of Ala Mhigo. He named Flame Marshal Eline, Raubahn's own second-in-command, as the Ivy, "
     "the Garlean spy in the Immortal Flames, and arrested her for treason and espionage.",
     ["C16", "M200e", "M210a", "M211c"], ["Captain Ilberd"]),
   P(S(216), None, "main", "Ilberd",
     "Captain of the Crystal Braves and Alphinaud's second-in-command, and Raubahn's friend and rival since before the fall of Ala Mhigo. He unmasked and arrested the Garlean spy Eline, and when she escaped "
     "he ran her down and sent her back to Ul'dah for trial, telling her that he sold his sword but she sold her comrades.",
     ["C16", "M200e", "M210a", "M216d", "M216f", "M216g"], ["Captain Ilberd"]),
   P(S(219), None, "main", "Ilberd",
     "Captain of the Crystal Braves and Alphinaud's second-in-command, and Raubahn's friend and rival since before the fall of Ala Mhigo. He unmasked the Garlean spy Eline. "
     "His raid on a black marketeer at the Burning Wall went wrong: one of his men killed the seller, the buyers slipped away, and only one crate of weapons was found.",
     ["C16", "M200e", "M210a", "M219b", "M219c", "M219d"], ["Captain Ilberd"]),
   P(S(229), None, "main", "Ilberd",
     "Captain of the Crystal Braves and Alphinaud's second-in-command, and Raubahn's friend and rival since before the fall of Ala Mhigo. He unmasked the Garlean spy Eline and leads the Braves in the field. "
     "As the Braves committed to Ishgard's defense, Riol grew uneasy at private words between Ilberd and Yuyuhase.",
     ["C16", "M200e", "M210a", "M223b", "M229c", "M229e"], ["Captain Ilberd"]),
   P(S(240), None, "main", "Ilberd",
     "Captain of the Crystal Braves, once Alphinaud's second-in-command and Raubahn's friend and rival since before the fall of Ala Mhigo. At the royal banquet in Ul'dah he delivered you bound and accused of regicide. "
     "When Raubahn went for Lolorito, Ilberd severed the general's arm, and he claimed credit for the sultana's murder.",
     ["C16", "M200e", "M240e", "M240i", "M240j"], ["Captain Ilberd"]),
 ],
 "char-raubahn": [
   P(S(200), None, "main", "Raubahn",
     "A Flame General of Ul'dah's Immortal Flames. He and Captain Ilberd have been friends and rivals since before the fall of Ala Mhigo. "
     "He is looking into the Garlean spy in his company, and wonders whether the Monetarists have been in league with the Empire from the first.",
     ["M200f", "M200e", "M200c", "M200g"]),
   P(S(210), None, "main", "Raubahn",
     "A Flame General of Ul'dah's Immortal Flames, and Captain Ilberd's friend and rival since before the fall of Ala Mhigo. Ilberd has named Raubahn's own second-in-command, Flame Marshal Eline, as the Garlean spy in the company.",
     ["M200f", "M200e", "M210a"]),
   P(S(216), None, "main", "Raubahn",
     "A Flame General of Ul'dah's Immortal Flames, whose second-in-command, Eline, proved to be a Garlean spy. Teledji has ordered the Blades to watch him and the Flames day and night.",
     ["M200f", "M210a", "M216h"]),
   P(S(217), None, "main", "Raubahn",
     "A Flame General of Ul'dah's Immortal Flames, who serves Sultana Nanamo. He concluded that his former second-in-command, the spy Eline, truly served Emperor Varis, and he has sworn to purge the land of the Monetarists. "
     "Nanamo has asked the Alliance leaders to help him keep order.",
     ["M200f", "M217i", "M217f", "M217j", "M217k"]),
   P(S(231), None, "main", "Raubahn",
     "A Flame General of Ul'dah's Immortal Flames, who serves Sultana Nanamo and has sworn to purge the land of the Monetarists. At the Alliance council on Ishgard's plight he proposed leaving Ul'dah's security to the Brass Blades "
     "so that a larger force could go to Ishgard.",
     ["M200f", "M217i", "M217j", "M231c"]),
   P(S(240), None, "main", "Raubahn",
     "A general of Ul'dah who served Sultana Nanamo, and Captain Ilberd's friend and rival since before the fall of Ala Mhigo. At the royal banquet, when Teledji gloated at being rid of the sultana, Raubahn cut him down; "
     "then Ilberd severed his arm. He bade you and the Scions flee, clear your names and find out who is behind the plot.",
     ["M200e", "M217i", "M240h", "M240i", "M240q", "M240k"], ["the Bull of Ala Mhigo"]),
   P(B, None, "main", "Raubahn",
     "A general of Ul'dah who served Sultana Nanamo. At the royal banquet he cut down Teledji, lost his arm to Captain Ilberd, and bade you and the Scions flee and find out who is behind the plot. He is now held in a prison cell.",
     ["M217i", "M240h", "M240i", "M240k", "M241e"], ["the Bull of Ala Mhigo"]),
 ],
 "char-nanamo": [
   P(S(217), None, "main", "Nanamo",
     "The sultana of Ul'dah, last monarch in the line of Ul. She told the Alliance leaders that Ul'dah will one day become a true republic, ending both Royalists and Monetarists, "
     "and asked them to help Raubahn preserve order.",
     ["M217l", "M217h", "M217k"], ["Sultana Nanamo"]),
   P(S(233), None, "main", "Nanamo",
     "The sultana of Ul'dah, last monarch in the line of Ul, who means to make Ul'dah a republic. She has invited the Scions to a feast at the Royal Palace in honor of Ishgard's victory.",
     ["M217l", "M217h", "M233a"], ["Sultana Nanamo"]),
   P(S(240), None, "main", "Nanamo",
     "The sultana of Ul'dah, last monarch in the line of Ul. Before the royal banquet she told you she means to abdicate and found a republic, and asked you to support Raubahn. "
     "Then she drank wine and collapsed, and Teledji proclaimed her murdered with poison, naming you the assassin; Captain Ilberd later claimed credit for her murder.",
     ["M217l", "M240a", "M240b", "M240c", "M240d", "M240j"], ["Sultana Nanamo"]),
 ],
 "char-teledji": [
   P(S(216), None, "main", "Teledji",
     "A powerful man in Ul'dah. He has ordered the Blades to watch Raubahn and the Flames day and night, and to sever an East Aldenard trade route to keep Lolorito busy.",
     ["M216h", "M216i"]),
   P(S(218), None, "main", "Teledji",
     "A Monetarist of Ul'dah who is quick to turn the Immortal Flames' troubles to his advantage. He has ordered the Blades to watch Raubahn day and night.",
     ["M218f", "M216h"]),
   P(S(238), None, "main", "Teledji",
     "A Monetarist of Ul'dah who has had Raubahn watched. Riol has evidence that he bribed members of the Crystal Braves' 1st and 3rd Units, through front companies owned by the Mirage Trust.",
     ["M218f", "M216h", "M238b", "M238c"]),
   P(S(240), None, "main", "Teledji",
     "A Monetarist of Ul'dah who bribed members of the Crystal Braves. At the royal banquet he proclaimed the sultana murdered with poison and accused you and the Scions. When he gloated at being rid of her, Raubahn cut him down.",
     ["M218f", "M238b", "M240d", "M240h"]),
 ],
 "char-lolorito": [
   P(S(216), None, "main", "Lolorito",
     "A rival of Teledji in Ul'dah, whom Teledji means to keep busy by severing an East Aldenard trade route.",
     ["M216i"]),
   P(S(240), None, "main", "Lolorito",
     "A rival of Teledji in Ul'dah. At the royal banquet, after cutting Teledji down, Raubahn went for Lolorito, and Captain Ilberd stopped him by severing his arm.",
     ["M216i", "M240i"]),
 ],
 "char-kan-e-senna": [
   P(S(209), None, "main", "Kan-E-Senna",
     "One of the leaders of the Eorzean Alliance, who opened an emergency council at the Lotus Stand in Old Gridania on the change in the Garlean Empire.",
     ["M209h", "M209i"]),
   P(S(231), None, "main", "Kan-E-Senna",
     "The leader who speaks for Gridania in the Eorzean Alliance. At the council on Ishgard's plight Kan-E-Senna could commit only a token force, fearing that Teledji and his ilk would seize Gridania's territories in Carteneau.",
     ["M209h", "M231j", "M231i", "M231h"]),
 ],
 "char-merlwyb": [
   P(S(209), None, "main", "Merlwyb",
     "One of the leaders of the Eorzean Alliance. At its council in Old Gridania she observed that young Varis has torn the Garlean crown from his uncle's grasp.",
     ["M209i", "M209d"]),
   P(S(231), None, "main", "Merlwyb",
     "A leader of Limsa Lominsa in the Eorzean Alliance. At the council on Ishgard's plight she put Limsa first, then the Alliance, then Ishgard, and gave Alphinaud the Crystal Braves to command.",
     ["M209i", "M231b", "M231d"], ["Admiral Merlwyb"]),
 ],
 "char-yugiri": [
   P(S(208), None, "main", "Yugiri",
     "A Doman whose shinobi helped uncover a merchant's link to the heretics of Coerthas. Her people long to strike back against the Empire, and she has offered to accompany the Scions until the investigation is complete.",
     ["M208f", "M208g", "M208e"], ["Lady Yugiri"]),
   P(S(211), None, "main", "Yugiri",
     "A Doman who leads shinobi aiding the Scions. Her people long to strike back against the Empire, and her shinobi have stopped Garlean agents sent to destroy the Alliance's jamming devices. "
     "She judged the spy Eline's surrender a sign that her position was untenable, not of innocence.",
     ["M208f", "M208g", "M211b", "M211e"], ["Lady Yugiri"]),
   P(B, None, "main", "Yugiri",
     "A Doman who leads shinobi aiding the Scions. After the royal banquet in Ul'dah she rescued Tataru from the Crystal Braves in Limsa Lominsa, and the two found shelter at the Waking Sands before joining you in Coerthas.",
     ["M208f", "C53", "C21"], ["Lady Yugiri"]),
 ],
 "char-aymeric": [
   P(S(202), None, "main", "Aymeric",
     "Lord commander of Ishgard's Temple Knights, who speaks for the Holy See. He will not bring Ishgard back into the Eorzean Alliance, but he will keep House Fortemps' aid flowing to Revenant's Toll "
     "if the Scions help watch over the remains of Midgardsormr, whose return Ishgard's astrologians foretell.",
     ["M202a", "M202b", "M202d", "M202c"], ["Ser Aymeric"]),
   P(S(214), None, "main", "Aymeric",
     "Lord commander of Ishgard's Temple Knights, who speaks for the Holy See. His knights joined the hunt for Iceheart. He has formally introduced his second-in-command, Lucia, "
     "and calls Ishgard's arrangement with Revenant's Toll mutually beneficial, born of necessity.",
     ["M202a", "M204b", "M214c", "M214i"], ["Ser Aymeric"]),
   P(S(228), None, "main", "Aymeric",
     "Lord commander of Ishgard's Temple Knights, who speaks for the Holy See. He told you that Iceheart and the Dravanians share one goal, the reclamation of Nidhogg's stolen Eye, "
     "and introduced Ishgard's Azure Dragoon, Estinien.",
     ["M202a", "M228a", "M228b", "M228d"], ["Ser Aymeric"]),
   P(S(232), None, "main", "Aymeric",
     "Lord commander of Ishgard's Temple Knights, who speaks for the Holy See. After the Dravanian Horde was driven from the Steps of Faith, he thanked the Scions on behalf of the Holy See and the people of Ishgard.",
     ["M202a", "M232d", "M232f"], ["Ser Aymeric"]),
   P(S(240), None, "main", "Aymeric",
     "Lord commander of Ishgard's Temple Knights, who speaks for the Holy See. He was at the royal banquet in Ul'dah when an urgent message from the Holy See called him home.",
     ["M202a", "M232f", "M240g"], ["Ser Aymeric"]),
   P(B, None, "main", "Aymeric",
     "Lord commander of Ishgard's Temple Knights, who speaks for the Holy See. He is safely back from Ul'dah and again leads the defense of Ishgard against the Dravanians.",
     ["M202a", "M241c", "M241a"], ["Ser Aymeric"]),
 ],
 "char-lucia": [
   P(S(214), None, "main", "Lucia",
     "Ser Aymeric's second-in-command, who represents him when he is otherwise engaged. Not of Ishgardian birth, she owes no allegiance to any noble house, and Aymeric counts her as near incorruptible.",
     ["M214c", "M214d"]),
   P(S(221), None, "main", "Lucia",
     "Ser Aymeric's second-in-command, who owes no allegiance to any noble house. She brought his request that you examine the Keeper of the Lake, and thanked you for confirming that a Dravanian attack is coming.",
     ["M214c", "M214d", "M221a", "M221i"]),
   P(S(227), None, "main", "Lucia",
     "Ser Aymeric's second-in-command. After a first Dravanian wave struck Ishgard at heavy cost, she came to ask the Crystal Braves and the Grand Companies for help, "
     "and confirmed that a heretic force had dispelled the first of the city's wards.",
     ["M214c", "M227b", "M227c", "M227f"]),
   P(S(240), None, "main", "Lucia",
     "Ser Aymeric's second-in-command, who sought Eorzea's help for Ishgard against the Dravanians. She was at the royal banquet in Ul'dah when an urgent message from the Holy See called her and Aymeric home.",
     ["M214c", "M227c", "M240g"]),
 ],
 "char-estinien": [
   P(S(228), None, "main", "Estinien",
     "Ishgard's Azure Dragoon. Through the power of Nidhogg's Eye he has become the vessel of the wyrm's strength, and he warns that Nidhogg means to hurl his Horde against the wards of Daniffen's Collar.",
     ["M228d", "M228e", "M228f"], ["the Azure Dragoon"]),
   P(S(232), None, "main", "Estinien",
     "Ishgard's Azure Dragoon, who has become the vessel of Nidhogg's strength through the wyrm's Eye. He fought on the Steps of Faith, where one of Nidhogg's greatest champions was slain.",
     ["M228d", "M228e", "M232c"], ["the Azure Dragoon"]),
 ],
 "char-iceheart": [
   P(S(202), None, "main", "Iceheart",
     "The leader of a band of heretics in Coerthas. She and her followers waylaid a House Fortemps aid shipment bound for Revenant's Toll.",
     ["M202e"]),
   P(S(203), None, "main", "Iceheart",
     "A silver-haired heretic leader in Coerthas. Disguised as pilgrims, she and her followers slaughtered a House Fortemps caravan's guards and seized its crystals, "
     "and Alphinaud believes they mean to summon Shiva, the heretics' patron saint, as a beast tribe would a primal.",
     ["M203h", "M203b", "M203e", "M203g"]),
   P(S(207), None, "main", "Iceheart",
     "A heretic leader in Coerthas who means to summon Shiva. She was given the name Ysayle but earned the name Iceheart, and vows to end the war between dragon and man at any cost. "
     "When you broke into her lair beneath Snowcloak she escaped by aetheryte.",
     ["M203e", "M207c", "M207d", "M207e"], ["Ysayle"]),
   P(S(213), None, "main", "Iceheart",
     "The heretic leader once known as Ysayle, who vows to end the war between dragon and man. In her sanctuary she offered her own body as a vessel for Shiva's soul. "
     "You defeated the primal, and she withdrew, telling you to seek the Keeper of the Lake and see with eyes unclouded.",
     ["M207c", "M207d", "M213b", "M213c", "M213d"], ["Ysayle"]),
   P(S(215), None, "main", "Iceheart",
     "The heretic leader once known as Ysayle, who vows to end the war between dragon and man. She summoned Shiva into her own body, and when you defeated the primal she escaped. "
     "Minfilia wonders whether she has the Echo.",
     ["M207c", "M207d", "M213b", "M214f", "M215c"], ["Ysayle"]),
   P(S(227), None, "main", "Iceheart",
     "The heretic leader once known as Ysayle, who summoned Shiva into her own body. Lady Iceheart and her followers attacked the knights at the Gates of Judgement and dispelled the first of Ishgard's wards; "
     "she says the sons must answer for their fathers' misdeeds.",
     ["M207c", "M213b", "M227g", "M227f", "M227h"], ["Ysayle", "Lady Iceheart"]),
   P(S(228), None, "main", "Iceheart",
     "The heretic leader once known as Ysayle, who summoned Shiva into her own body and has dispelled one of Ishgard's wards. Ser Aymeric says she shares the Dravanians' aim of reclaiming Nidhogg's stolen Eye.",
     ["M207c", "M213b", "M227f", "M228a"], ["Ysayle", "Lady Iceheart"]),
   P(S(232), None, "main", "Iceheart",
     "The heretic leader once known as Ysayle, who summoned Shiva into her own body and seeks Nidhogg's stolen Eye. The damage she did to Ishgard's barrier let the dragons land on the Steps of Faith, where the Horde was driven back.",
     ["M207c", "M213b", "M228a", "M232a", "M232d"], ["Ysayle", "Lady Iceheart"]),
 ],
 "char-shiva": [
   P(S(203), None, "main", "Shiva",
     "The heretics' patron saint, whom Ishgard calls a traitor to kith and kin who lay down with dragons. Alphinaud believes Iceheart means to summon her as a beast tribe would a primal.",
     ["M203d", "M203g", "M203e"]),
   P(S(208), None, "main", "Shiva",
     "The heretics' patron saint, whom Ishgard calls a traitor who lay down with dragons. Minfilia is certain she was a real, living woman, and Iceheart means to summon her as a primal.",
     ["M203d", "M203e", "M208a"]),
   P(S(212), None, "main", "Shiva",
     "The heretics' patron saint, once a living woman. Iceheart means to summon her with crystals stolen from House Fortemps, and Minfilia expects the result to be more akin to a primal than a saint.",
     ["M203g", "M208a", "M212a", "M212b"]),
   P(S(213), None, "main", "Shiva",
     "The heretics' patron saint, once a living woman. Iceheart offered her own body as a vessel for Shiva's soul, and you defeated her.",
     ["M203g", "M208a", "M213b", "M213c"]),
   P(S(215), None, "main", "Shiva",
     "The heretics' patron saint, once a living woman. Iceheart summoned her into her own body, and you defeated her; Moenbryda confirms that what Iceheart summoned was a primal.",
     ["M203g", "M208a", "M213b", "M215d"], ["Saint Shiva"]),
 ],
 "char-ivy": [
   P(S(200), None, "main", "The Ivy",
     "The codename of a Garlean spy who has infiltrated one of the Grand Companies. A suspect in the Immortal Flames proved to be only one of many in the spy's employ: the vines by which the Ivy learns secrets without being exposed.",
     ["M200b", "M200c", "M200d"]),
   P(S(208), None, "main", "The Ivy",
     "The codename of a Garlean spy in the Immortal Flames, who works through many conspirators. A merchant caught helping the heretics links the Ivy to Iceheart.",
     ["M200b", "M200d", "M208c", "M208d"]),
   P(S(209), None, "main", "The Ivy",
     "The codename of a Garlean spy in the Immortal Flames, whose network fed caravan routes to Iceheart's heretics. Covering the trail took powers held only by high-ranking Flames, and Captain Ilberd says the Ivy is unmasked.",
     ["M200b", "M209a", "M209b", "M209f"]),
   P(S(210), None, "main", "The Ivy",
     "The codename of the Garlean spy in the Immortal Flames. Captain Ilberd has named the Ivy as Flame Marshal Eline.",
     ["M200b", "M210a"]),
 ],
 "char-eline": [
   P(S(210), None, "main", "Eline",
     "Flame Marshal of the Immortal Flames and Raubahn's second-in-command, of Ishgardian birth and the highest-ranked foreigner in the company. Captain Ilberd has named her as the Ivy, the Garlean spy. "
     "She slipped out of Gridania disguised as a merchant.",
     ["M210a", "M210b", "M210e"], ["Flame Marshal Eline", "The Ivy"]),
   P(S(211), None, "main", "Eline",
     "Flame Marshal of the Immortal Flames and Raubahn's second-in-command, named by Captain Ilberd as the Ivy, the Garlean spy. Ilberd arrested her for treason and espionage as she met an imperial intermediary. "
     "She offered no struggle, saying she has nothing to hide.",
     ["M210a", "M210b", "M211c", "M211d"], ["Flame Marshal Eline", "The Ivy"]),
   P(S(216), None, "main", "Eline",
     "A Flame Marshal unmasked as the Ivy, the Garlean spy in the Immortal Flames. She escaped her cell in Ul'dah with inside help, leaving the turnkey and two guards dead, and fled for Castrum Meridianum, "
     "but was run down and sent back for trial. She speaks of the injustice lowborn Ishgardians endure.",
     ["M210a", "M216a", "M216b", "M216c", "M216g", "M216e"], ["Flame Marshal Eline", "The Ivy"]),
   P(S(217), None, "main", "Eline",
     "A Flame Marshal unmasked as the Ivy, the Garlean spy in the Immortal Flames, and held for trial in Ul'dah. She once aided the Scions at their founding. Even as she served the Empire she sold imperial secrets to a faction in Eorzea, "
     "and Raubahn concludes that her true master was Emperor Varis.",
     ["M210a", "M216g", "M217a", "M217e", "M217f", "M217g"], ["Flame Marshal Eline", "The Ivy"]),
 ],
 "char-varis": [
   P(S(209), None, "main", "Varis",
     "The new emperor of Garlemald, grandson of the late emperor, who tore the crown from his uncle's grasp to end the war of succession. The Alliance fears the Empire will now resume its march on Eorzea.",
     ["M209c", "M209d"], ["Emperor Varis"]),
   P(S(217), None, "main", "Varis",
     "The emperor of Garlemald, grandson of the late emperor, who tore the crown from his uncle's grasp. Raubahn concludes that he was the true master of Eline, the spy in the Immortal Flames.",
     ["M209c", "M209d", "M217f"], ["Emperor Varis"]),
 ],
 "char-moenbryda": [
   P(S(212), None, "main", "Moenbryda",
     "An accomplished Sharlayan scholar and an authority on aetheryte technologies, whom Minfilia called in. She has been researching white auracite to capture Ascian souls, "
     "and proposes recreating the beacon to Iceheart's sanctuary, though everyone who has teleported that way has died.",
     ["M212c", "M212d", "M212e", "M212f"]),
   P(S(215), None, "main", "Moenbryda",
     "An accomplished Sharlayan scholar and an authority on aetheryte technologies, who researches white auracite to capture Ascian souls. Her beacon opened the way to Iceheart's sanctuary, and she confirms that what Iceheart summoned was a primal.",
     ["M212c", "M212d", "M213a", "M215d"]),
   P(S(217), None, "main", "Moenbryda",
     "A Sharlayan scholar and authority on aetheryte technologies who works with the Scions. With Urianger she believes an Ascian soul can be undone by a concentrated burst of pure aether, "
     "but white auracite holds aether only briefly.",
     ["M212c", "M217c", "M217b"]),
   P(S(222), None, "main", "Moenbryda",
     "A Sharlayan scholar working with the Scions on a blade to destroy an Ascian's soul, which does not return to the aetherial realm when its host falls. Her plan is to siphon aether from corrupted crystals across Eorzea.",
     ["M212c", "M222a", "M222b"]),
   P(S(224), None, "main", "Moenbryda",
     "A Sharlayan scholar who, like Urianger, studied under Louisoix. When the Ascian Nabriales attacked, Minfilia trapped his soul in white auracite, and Moenbryda spent her own life energy in a burst of aether "
     "so that your blade could pierce him. She died.",
     ["C54", "M224g", "M224h"]),
 ],
 "char-midgardsormr": [
   P(S(202), None, "main", "Midgardsormr",
     "A great wyrm, the fallen guardian of Silvertear Falls. The dragon star waxes bright, Ishgard's astrologians foretell his return, and Ser Aymeric has asked the Scions to help watch over his remains.",
     ["M202c", "M202h"]),
   P(S(215), None, "main", "Midgardsormr",
     "A great wyrm, the fallen guardian of Silvertear Falls: a king amongst kings who reigned for centuries. Ishgard's astrologians fear he may soon rise from the dead, and the Scions are watching the Keeper of the Lake.",
     ["M202c", "M215e", "M215f", "M215g"]),
   P(S(221), None, "main", "Midgardsormr",
     "A great wyrm, the fallen guardian of Silvertear Falls, who died in the explosion after Eorzea's victory there. Atop the wreck you fought him; when Hydaelyn marked you as Her chosen he relented, "
     "but stripped you of the Mothercrystal's blessing. A covenant binds him to you, and he says his children sing of Ishgard's destruction.",
     ["M221c", "M221d", "M221e", "M221f", "M221g"]),
   P(S(225), None, "main", "Midgardsormr",
     "A great wyrm who stripped you of the Mothercrystal's blessing and is bound to you by a covenant. At the memorial for Moenbryda his voice called her death life for death, a fair exchange, and promised other bargains.",
     ["M221e", "M221f", "M225b"]),
   P(B, None, "main", "Midgardsormr",
     "A great wyrm who stripped you of the Mothercrystal's blessing and is bound to you by a covenant. At the gates of Ishgard he told you that you will find naught there but delusion, despair and death.",
     ["M221e", "M221f", "M241i"]),
 ],
 "char-nidhogg": [
   P(S(228), None, "main", "Nidhogg",
     "A great wyrm who has terrorized Coerthas since Ishgard's founding. The hero Haldrath defeated him and took his Eye, now a treasured relic of Ishgard. Nidhogg means to hurl his Horde against the city's wards, "
     "and Estinien has become the vessel of his strength.",
     ["M228c", "M228b", "M228f", "M228e"]),
   P(S(232), None, "main", "Nidhogg",
     "A great wyrm who has terrorized Coerthas since Ishgard's founding, and whose Eye Haldrath took. His Horde struck Ishgard's wards, but one of his greatest champions fell on the Steps of Faith and the Horde was driven off.",
     ["M228c", "M228b", "M232c", "M232d"]),
 ],
 "char-nabriales": [
   P(S(224), None, "main", "Nabriales",
     "An Ascian. Your lost blessing of Light had kept his kind out of the Scions' domain. He came for Tupsimati, Louisoix's staff, meaning to use its power for a new Rejoining, and Minfilia saw that the vanishing of the Isle of Val was his doing. "
     "He carried her off through a rift; you defeated him, Minfilia trapped his soul in white auracite, and Moenbryda gave her life so that your blade could pierce him.",
     ["M224a", "M224b", "M224c", "M224i", "M224e", "M224d", "M224g", "M224h"]),
   P(B, None, "main", "Nabriales",
     "An Ascian who came for Louisoix's staff, Tupsimati, and was destroyed when Moenbryda gave her life to empower your blade. Elidibus says he is no more, and Lahabrea says the Ardor was not his to invoke.",
     ["M224c", "M224h", "M241f", "M241g"]),
 ],
 "char-elidibus": [
   P(B, None, "main", "Elidibus",
     "An Ascian. With Lahabrea he spoke of the end of Nabriales, saying he is no more, and the two turned their thoughts to the northern lands.",
     ["M241f", "M241g", "M241h"]),
 ],
 "char-yuyuhase": [
   P(S(208), None, "main", "Yuyuhase",
     "An officer of the Crystal Braves' 3rd Unit, who led its pursuit of the heretics past Daniffen Pass. You found him on a lone trail, with a plan for the heretics to withdraw to the Observatorium.",
     ["M208h", "M208i"]),
   P(S(220), None, "main", "Yuyuhase",
     "An officer of the Crystal Braves' 3rd Unit. When Captain Ilberd's raid on a black marketeer yielded only one crate of weapons, he blamed Riol's intelligence.",
     ["M208h", "M219d", "M220a"]),
   P(S(229), None, "main", "Yuyuhase",
     "An officer of the Crystal Braves' 3rd Unit, who fought beside you at the Ceruleum Processing Plant. Riol is uneasy about the private words passing between him and Captain Ilberd.",
     ["M208h", "M223d", "M229e"]),
   P(S(240), None, "main", "Yuyuhase",
     "An officer of the Crystal Braves' 3rd Unit. At the royal banquet in Ul'dah, as the Braves turned on Alphinaud, he told his commander they strive for the salvation of Eorzea.",
     ["M208h", "M240f"]),
 ],
 "char-alianne": [
   P(S(201), None, "main", "Alianne",
     "A Crystal Brave of the 4th Unit. When Garleans captured one of her comrades, you helped her unit free the wounded Brave from Castrum Centri with no further losses.",
     ["M201e", "M201f", "M201b"]),
   P(S(239), None, "main", "Alianne",
     "A lieutenant of the Crystal Braves' 4th Unit. Before the royal banquet in Ul'dah she asked to meet you privately to show you something, but she never came; a vial lay at your feet, and another Brave has seen no sign of her.",
     ["M201e", "M239a", "M239b", "M239c", "M239e"], ["Lieutenant Alianne"]),
 ],
 "char-wilred": [
   P(S(230), None, "main", "Wilred",
     "A youth from Little Ala Mhigo serving in the Crystal Braves. He reported that the Braves' numbers did not add up, then vanished after a skirmish, around the time black-market weapons went missing from the Braves' vault.",
     ["M230c", "M230f", "M230d"]),
   P(S235B, None, "main", "Wilred",
     "A young Ala Mhigan you recruited to the Crystal Braves. He vanished after reporting that the Braves' numbers did not add up, and was found murdered at Urth's Fount, where no Brave operation was known.",
     ["M235ba", "M230f", "M235bb", "M235bc"]),
   P(S(238), None, "main", "Wilred",
     "A young Ala Mhigan you recruited to the Crystal Braves, found murdered after he began asking pointed questions about the Braves' numbers. Riol believes Braves bribed by Teledji killed him.",
     ["M235ba", "M235bb", "M238b", "M238d"]),
 ],
 "char-pipin": [
   P(S(240), None, "main", "Pipin",
     "Vice Marshal of the Immortal Flames and Raubahn's adopted son. After the royal banquet he helped you and Alphinaud flee Ul'dah, then stayed behind, swearing to do what he can to clear your names.",
     ["M240l", "M240s", "M240o"], ["Vice Marshal Pipin"]),
 ],

 # ---- Existing characters ----
 "char-alphinaud": [
   P(S(200), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother. He commands the newly formed Crystal Braves, with Captain Ilberd as his second-in-command, and Minfilia has asked you to help him.",
     ["C10", "C16", "M200a"]),
   P(S(202), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who commands the Crystal Braves. He met Ser Aymeric of Ishgard, who would not rejoin the Alliance but agreed to protect aid shipments to Revenant's Toll "
     "in return for the Scions' watch over Midgardsormr's remains.",
     ["C10", "C16", "M202b", "M202d", "M202c"]),
   P(S(203), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who commands the Crystal Braves. He realized that Iceheart's heretics mean to summon Shiva as a primal, and turned the whole order to preventing it.",
     ["C10", "C16", "M203e", "M203f"]),
   P(S(214), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who commands the Crystal Braves. After Shiva's defeat he suspects Ishgard of manipulating Revenant's Toll and its other neighbors for its own ends.",
     ["C10", "C16", "M213c", "M214g"]),
   P(S(215), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who commands the Crystal Braves. He warns that if civilized peoples can summon primals as the beast tribes do, the Alliance could face the combined might of all Garlemald.",
     ["C10", "C16", "M215a", "M215b"]),
   P(S(218), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who commands the Crystal Braves. He is staying in Ul'dah with the Braves to support the Immortal Flames, shaken by the spy found among their officers.",
     ["C10", "C16", "M218a", "M218e"]),
   P(S(228), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who commands the Crystal Braves. He has pledged that Eorzea will not leave Ishgard to face Nidhogg's Horde alone.",
     ["C10", "C16", "M228h"]),
   P(S(231), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother. The Alliance leaders refused him meaningful aid for Ishgard, but Admiral Merlwyb gave him the Crystal Braves to command, and he sent them to the Steel Vigil.",
     ["C10", "M231a", "M231d", "M231f"]),
   P(S(232), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who commands the Crystal Braves. After the Dravanian Horde was driven from the Steps of Faith he declared the stage set for Ishgard's return to the Alliance.",
     ["C10", "M231d", "M232d", "M232e"]),
   P(S(240), None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who commanded the Crystal Braves. At the royal banquet in Ul'dah the Braves turned on him, Yuyuhase claiming they strive for the salvation of Eorzea. "
     "He escaped with you, and Cid flew you both to Camp Dragonhead aboard the Enterprise.",
     ["C10", "C52", "M240f", "M240m", "M240n"]),
 ],
 "char-minfilia": [
   P(S(224), None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. The Ascian Nabriales seized her and the broken Tupsimati and carried her off through a rift. You rescued her, she trapped his soul in white auracite, "
     "and Moenbryda gave her life to finish him. Minfilia keeps the device Moenbryda left behind.",
     ["C01", "C33", "M224d", "M224f", "M224g", "M224h", "M224j"]),
   P(S(225), None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. Mourning Louisoix, Moenbryda and the Scions who fell at the Waking Sands, she leans on you as her pillar of strength.",
     ["C01", "C33", "M225c", "M225d"]),
   P(S(229), None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. She agreed that the Scions, with the Crystal Braves, will directly intervene in Ishgard's war against the Dravanians.",
     ["C01", "C33", "M229d", "M229c"]),
   P(S(233), None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. In no mood to celebrate so soon after Moenbryda's death, she suspects the royal feast in Ul'dah is a chance to press Ishgard to rejoin the Alliance.",
     ["C01", "C33", "M233a", "M233f", "M233c"]),
   P(S(240), None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. When the Scions were accused of plotting the sultana's death at the royal banquet in Ul'dah and fled, she stayed behind, saying that Hydaelyn was speaking to her.",
     ["C01", "C33", "C50", "C17"]),
 ],
 "char-thancred": [
   P(S(240), None, "main", "Thancred",
     "A Scion and bard. At the royal banquet in Ul'dah he was accused of spying for the Garlean Empire. He led the escape through a hidden passage in the palace, then stayed behind with Y'shtola to stop the pursuit.",
     ["C51", "C18"]),
 ],
 "char-yshtola": [
   P(S(240), None, "main", "Y'shtola",
     "A Sharlayan Scion. When the Scions fled the royal banquet in Ul'dah through a hidden tunnel, she and Thancred stayed behind, and she meant to bring the tunnel down on their pursuers.",
     ["C18", "M240v"]),
 ],
 "char-urianger": [
   P(S(217), None, "main", "Urianger",
     "A learned Sharlayan Scion, in whose care the Waking Sands was left. With Moenbryda he believes an Ascian soul can be undone by a concentrated burst of pure aether.",
     ["C45", "M217c"]),
   P(S(224), None, "main", "Urianger",
     "A learned Sharlayan Scion, in whose care the Waking Sands was left. He and Moenbryda studied under Louisoix, who was branded a pariah in his own land, and Moenbryda gave her life to destroy the Ascian Nabriales.",
     ["C45", "C54", "M224l", "M224h"]),
 ],
 "char-tataru": [
   P(S(233), None, "main", "Tataru",
     "The Scions' receptionist at the Rising Stones. Troubled, she has taken leave to learn to fight, so that she can defend herself.",
     ["C15", "M233e", "M233d"]),
   P(S(234), None, "main", "Tataru",
     "The Scions' receptionist. She took up arcanima to learn to defend herself, but when her Carbuncle abandoned her to wild beasts she renounced it, admitting she will never be a warrior.",
     ["C15", "M234a", "M234b", "C47b", "M234c"]),
   P(S(235), None, "main", "Tataru",
     "The Scions' receptionist, who briefly trained as an arcanist and gave it up. Instead she harvested blood pearls to make charms for the Scions, so that wherever they go they will always come home.",
     ["C15", "C47", "C47b", "M235a", "M235b"]),
 ],
 "char-yda": [
   P(S(226), None, "main", "Yda",
     "A Scion grieving for Moenbryda. She ordered a rare flower in her friend's memory and laid it at the mark of the Scholar at Rathefrost, just as Dravanian wings darkened the sky.",
     ["C31", "M226a", "M226b", "M226c"]),
   P(B, None, "main", "Yda",
     "A Scion who grieved for Moenbryda. When the Scions fled the royal banquet in Ul'dah, she stayed behind with Papalymo to hold off the pursuers, and she is unaccounted for.",
     ["M226a", "M240t", "M240u", "C22"]),
 ],
 "char-papalymo": [
   P(S(232), None, "main", "Papalymo",
     "A Scion who fought beside Yda in the rearguard on the Steps of Faith, where the Dravanian Horde was driven back.",
     ["C31", "M232h", "M232d"]),
   P(B, None, "main", "Papalymo",
     "A Scion. When the Scions fled the royal banquet in Ul'dah, he stayed behind with Yda to hold off the pursuers, and he is unaccounted for.",
     ["C31", "M240u", "C22"]),
 ],
 "char-haurchefant": [
   P(S(214), None, "main", "Haurchefant",
     "A lord of House Fortemps who commands the garrison at Camp Dragonhead. He is more than a little distressed that you took on Iceheart and Shiva without involving him.",
     ["E116c", "M214e"]),
   P(S(240), None, "main", "Haurchefant",
     "A lord of House Fortemps who commands the garrison at Camp Dragonhead. When you and Alphinaud fled Ul'dah as fugitives, Alphinaud proposed seeking his counsel there.",
     ["E116c", "M240n"]),
   P(B, None, "main", "Haurchefant",
     "A lord of House Fortemps who commands the garrison at Camp Dragonhead. He shelters you and Alphinaud; your petition for asylum in Ishgard must wait until the threat to the city diminishes, "
     "and House Fortemps will give no aid to anyone who comes looking for you.",
     ["E116c", "M241b", "M241d"]),
 ],
 "char-drillemont": [
   P(S(204), None, "main", "Drillemont",
     "Lord of Whitebrim Front, who once opened the way to the Stone Vigil for you. His scouts lost a band of heretic pilgrims at Snowcloak, and he welcomes the Scions' help in the hunt for Iceheart.",
     ["E128e", "M204a", "M204d"]),
   P(S(206), None, "main", "Drillemont",
     "Lord of Whitebrim Front, who is hunting Iceheart's heretics. A covert check of his garrison exposed a knight passing word to them, and a timetable of the watches at Snowcloak, found on a slain heretic, "
     "shows they may already be poised to strike.",
     ["E128e", "M205a", "M205c", "M206b", "M206d"]),
 ],
 "char-cid": [
   P(S(240), None, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. When you and Alphinaud fled Ul'dah as fugitives, he flew you to Coerthas aboard his airship, the Enterprise.",
     ["K07", "M240m", "M240n"]),
 ],
 "char-louisoix": [
   P(S(224), None, "main", "Louisoix",
     "A revered Archon and Sharlayan sage who never returned from the Battle of Carteneau. Urianger and Moenbryda studied under him, and he was branded a pariah in his own land. "
     "His staff, Tupsimati, was the relic the Ascian Nabriales came to seize.",
     ["C44", "C54", "M224l", "M224c"], ["Archon Louisoix", "Master Louisoix"]),
 ],
 "char-lahabrea": [
   P(B, None, "main", "Lahabrea",
     "An Ascian who possessed Thancred until you freed him. With Elidibus he spoke of Nabriales's demise, saying the Ardor was not his to invoke, and the two turned their thoughts to the northern lands.",
     ["C09", "M241g", "M241h"]),
 ],

 # ---- Groups and places ----
 "org-crystal-braves": [
   P(S(200), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, bound to no single nation, which he commands with Captain Ilberd as his second-in-command. It is hunting the Ivy, a Garlean spy in the Immortal Flames.",
     ["C48", "C16", "M200b"]),
   P(S(204), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, bound to no single nation, which he commands with Captain Ilberd as his second-in-command. Besides hunting the Ivy, a Garlean spy, a unit has joined the hunt for Iceheart in Coerthas.",
     ["C48", "C16", "M200b", "M204c"]),
   P(S(211), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, bound to no single nation, which he commands with Captain Ilberd as his second-in-command. Ilberd unmasked the Ivy, Flame Marshal Eline, and arrested her for treason and espionage.",
     ["C48", "C16", "M210a", "M211c"]),
   P(S(218), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, bound to no single nation, which he commands with Captain Ilberd as his second-in-command. Alphinaud keeps it in Ul'dah to support the Immortal Flames, shaken by the spy among their officers.",
     ["C48", "C16", "M218a"]),
   P(S(220), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, which he commands with Captain Ilberd as his second-in-command. It is stationed in Ul'dah to support the Immortal Flames. Riol notes that its 1st and 3rd Units now spend freely.",
     ["C48", "C16", "M218a", "M220c"]),
   P(S(229), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, which he commands with Captain Ilberd as his second-in-command. With the Scions it has committed to the defense of Ishgard against the Dravanians.",
     ["C48", "C16", "M229c"]),
   P(S(230), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, committed with them to the defense of Ishgard. Black-market weapons went missing from its vault in Ul'dah around the time a young Brave, Wilred, vanished.",
     ["C48", "M229c", "M230d", "M230c"]),
   P(S(231), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, committed with them to the defense of Ishgard. Admiral Merlwyb gave Alphinaud the Braves to command, and he sent them to the Steel Vigil to join House Durendaire.",
     ["C48", "M229c", "M231d", "M231f"]),
   P(S(238), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions and commands, with Captain Ilberd as his second-in-command. Riol has evidence that Teledji bribed members of its 1st and 3rd Units, and believes they killed a young Brave, Wilred.",
     ["C48", "C16", "M238b", "M238d"]),
   P(S(240), None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, with Captain Ilberd as his second-in-command. At the royal banquet in Ul'dah, Ilberd delivered you bound on a charge of regicide, and the Braves turned on Alphinaud, "
     "Yuyuhase claiming they strive for the salvation of Eorzea.",
     ["C48", "C16", "M240e", "C52", "M240f"]),
 ],
 "org-scions": [
   P(S(203), None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. Alphinaud has turned it to preventing the heretic Iceheart from summoning Shiva as a primal.",
     ["C34", "C01", "M203e", "M203f"]),
   P(S(224), None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. With your blessing of Light gone, the Ascian Nabriales broke into its domain; he was destroyed, but the Sharlayan scholar Moenbryda died to do it.",
     ["C34", "C01", "M224b", "M224h"]),
   P(S(229), None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. With the Crystal Braves it has committed to the defense of Ishgard, a direct intervention in the war.",
     ["C34", "C01", "M229c", "M229d"]),
   P(S(240), None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. At the royal banquet in Ul'dah its members were accused of conspiring to poison the sultana, detained and branded fugitives; "
     "they fled, comrades staying behind one by one to hold back the pursuit.",
     ["C34", "C01", "C50", "M240r"]),
 ],
 "org-immortal-flames": [
   P(S(200), None, "main", "The Immortal Flames",
     "Ul'dah's Grand Company, in which Raubahn is a Flame General. A Garlean spy known as the Ivy has planted conspirators in its ranks.",
     ["M200f", "M200b", "M200c"]),
   P(S(210), None, "main", "The Immortal Flames",
     "Ul'dah's Grand Company, in which Raubahn is a Flame General. Captain Ilberd has named its Flame Marshal Eline, Raubahn's second-in-command, as the Ivy, the Garlean spy.",
     ["M200f", "M210a", "M210b"]),
   P(S(218), None, "main", "The Immortal Flames",
     "Ul'dah's Grand Company, in which Raubahn is a Flame General. It is struggling to cope with the revelation that one of its highest-ranking officers was a Garlean agent, and the Crystal Braves are supporting it.",
     ["M200f", "M210a", "M218a"]),
   P(S(240), None, "main", "The Immortal Flames",
     "Ul'dah's Grand Company. After the royal banquet its Vice Marshal, Pipin, Raubahn's adopted son, helped you and Alphinaud flee the city.",
     ["M200f", "M240l"]),
 ],
 "org-monetarists": [
   P(S(200), None, "main", "The Monetarists",
     "A faction in Ul'dah. Raubahn wonders whether it has been in league with the Empire from the first.",
     ["M200g"]),
   P(S(210), None, "main", "The Monetarists",
     "A faction in Ul'dah that Raubahn suspects of long dealings with the Empire. Captain Ilberd wonders whether the Ivy has some hold over it.",
     ["M200g", "M210c"]),
   P(S(217), None, "main", "The Monetarists",
     "A faction in Ul'dah that Raubahn suspects of long dealings with the Empire. Sultana Nanamo means to make Ul'dah a republic in which neither Royalists nor Monetarists remain, and Raubahn has sworn to purge them.",
     ["M200g", "M217h", "M217j"]),
 ],
 "org-heretics": [
   P(S(202), None, "main", "The heretics",
     "Heretics in Coerthas led by Iceheart. They waylaid a House Fortemps aid shipment bound for Revenant's Toll.",
     ["M202e"]),
   P(S(203), None, "main", "The heretics",
     "Heretics in Coerthas led by Iceheart, who revere Shiva as their patron saint. Disguised as pilgrims, they slaughtered a House Fortemps caravan's guards and seized its crystals, meaning to summon her.",
     ["M202e", "M203g", "M203b", "M203e"]),
   P(S(207), None, "main", "The heretics",
     "Heretics in Coerthas led by Iceheart, who mean to summon their patron saint, Shiva. They knew the movements of the Temple Knights and the Crystal Braves, but you drove them from their lair beneath Snowcloak.",
     ["M203g", "M203e", "M205b", "M207e"]),
   P(S(227), None, "main", "The heretics",
     "Heretics led by Iceheart, who summoned Shiva into her own body. They attacked the knights at the Gates of Judgement and dispelled the first of Ishgard's wards.",
     ["M213b", "M227g", "M227f"]),
 ],
 "org-temple-knights": [
   P(S(202), None, "main", "The Temple Knights",
     "Ishgard's knights, led by Lord Commander Ser Aymeric. Ishgard's forces are wholly committed to the conflict with the Dravanians.",
     ["M202a", "M202f"]),
   P(S(204), None, "main", "The Temple Knights",
     "Ishgard's knights, led by Lord Commander Ser Aymeric. They have joined the hunt for Iceheart's heretics in Coerthas.",
     ["M202a", "M204b", "M204a"]),
   P(S(232), None, "main", "The Temple Knights",
     "Ishgard's knights, led by Lord Commander Ser Aymeric. With your help they defended the Steps of Faith and drove the Dravanian Horde back.",
     ["M202a", "M232i", "M232d"]),
 ],
 "org-dravanian-horde": [
   P(S(221), None, "main", "The Dravanian Horde",
     "The Dravanians, children of Midgardsormr, who he says now sing of Ishgard's destruction. Lucia confirms an attack is coming.",
     ["M221g", "M221i"]),
   P(S(227), None, "main", "The Dravanian Horde",
     "The Dravanians, who Midgardsormr says sing of Ishgard's destruction. A first wave struck Ishgard and was beaten back at a heavy cost.",
     ["M221g", "M227b"]),
   P(S(228), None, "main", "The Dravanian Horde",
     "The Horde of Nidhogg, a great wyrm, who means to hurl it against Ishgard's remaining wards. A first wave was beaten back at a heavy cost.",
     ["M228f", "M227b"], ["the Horde"]),
   P(S(232), None, "main", "The Dravanian Horde",
     "The Horde of Nidhogg, a great wyrm. It struck Ishgard's wards, but on the Steps of Faith one of Nidhogg's greatest champions fell and the Horde was driven off.",
     ["M228f", "M232c", "M232d"], ["the Horde"]),
   P(B, None, "main", "The Dravanian Horde",
     "The Horde of Nidhogg, a great wyrm. Driven from the Steps of Faith, it has renewed its assault on Ishgard, and several wyverns broke into the city before the Temple Knights slew them.",
     ["M228f", "M232d", "M241a", "M241j"], ["the Horde"]),
 ],
 "org-holy-see": [
   P(S(202), None, "main", "The Holy See",
     "The authority that speaks for Ishgard, a city-state that has kept its neighbors at arm's length since the Battle of Silvertear Skies. Ser Aymeric represents it. "
     "It will not rejoin the Eorzean Alliance, and Ishgard's forces are committed to the conflict with the Dravanians.",
     ["M202i", "M202a", "M202b", "M202f"], ["the Holy See of Ishgard"]),
   P(S(214), None, "main", "The Holy See",
     "The authority that speaks for Ishgard, which keeps its neighbors at arm's length. It ordered its knights to observe and act only in self-defense, "
     "and Ishgard wants Revenant's Toll to flourish as an obstacle to its enemies from the south.",
     ["M202i", "M214a", "M214b"], ["the Holy See of Ishgard"]),
   P(S(227), None, "main", "The Holy See",
     "The authority that speaks for Ishgard, long apart from the Eorzean Alliance. A first Dravanian wave was beaten back at a heavy cost, a heretic force led by Iceheart has dispelled the first of the city's wards, "
     "and its envoy, Lucia, has come to Eorzea for help.",
     ["M202b", "M227b", "M227f", "M227g", "M227a"], ["the Holy See of Ishgard"]),
   P(S(229), None, "main", "The Holy See",
     "The authority that speaks for Ishgard, long apart from the Eorzean Alliance. The city's wards have been nullified and the Dravanian host advances on it; the Scions and the Crystal Braves have committed to its defense.",
     ["M202b", "M229a", "M229b", "M229c"], ["the Holy See of Ishgard"]),
   P(S(232), None, "main", "The Holy See",
     "The authority that speaks for Ishgard. Dragons landed on the Steps of Faith through the city's damaged wards, but its defenders drove the Horde off and the siege is ended. "
     "Ser Aymeric thanked the Scions in its name, and Alphinaud believes Ishgard may now rejoin the Alliance.",
     ["M232a", "M232d", "M232g", "M232f", "M232e"], ["the Holy See of Ishgard"]),
   P(B, None, "main", "The Holy See",
     "The authority that speaks for Ishgard, which withstood the Dravanian siege. The Horde has renewed its assault and wyverns broke into the city, so your petition for asylum will wait until the threat diminishes.",
     ["M232g", "M241a", "M241b"], ["the Holy See of Ishgard"]),
 ],
 "loc-rising-stones": [
   P(S(224), None, "main", "The Rising Stones",
     "The Scions' headquarters in Revenant's Toll, Mor Dhona, entered through the Seventh Heaven. With your blessing of Light gone, the Ascian Nabriales reached its solar and seized Minfilia and the broken Tupsimati.",
     ["C14", "C15", "M224b", "M224k", "M224d"]),
   P(S(240), None, "main", "The Rising Stones",
     "The Scions' headquarters in Revenant's Toll, Mor Dhona, entered through the Seventh Heaven. After the royal banquet in Ul'dah, the Crystal Braves seized it and detained the Scions' allies.",
     ["C14", "C15", "C19"]),
 ],
 "org-eorzean-alliance": [
   P(S(209), None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. At an emergency council in Old Gridania its leaders learned that Varis has taken the Garlean throne, and resolved that the Alliance must regain its unity and coax Ishgard back.",
     ["M209i", "M209c", "M209g"]),
   P(S(231), None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states, which Ishgard left long ago. When Ishgard asked for help against the Dravanians, its leaders refused meaningful aid and suggested hiring adventurers instead.",
     ["M202b", "M231a"]),
   P(S(233), None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. Its leaders sent only sellswords to Ishgard's defense, many of whom died before the siege began, and a royal feast in Ul'dah may be a chance to press Ishgard to rejoin.",
     ["M231a", "M233b", "M233c"]),
 ],
 "org-garlean-empire": [
   P(S(209), None, "main", "The Garlean Empire",
     "An empire that has tried to conquer Eorzea. Its war of succession ended when Varis, the late emperor's grandson, tore the crown from his uncle's grasp, and the Alliance fears it will soon resume its march.",
     ["E100a", "M209c", "M209d"], ["the Empire"]),
 ],
}

# ---- Relationship types and relationships -------------------------------------------------------------------------
TYPES = [
 ("bribes", "bribes", "bribed by", False),
 ("child-of", "child of", "parent of", False),
]

RELS = [
 ("rel-ilberd-serves-alphinaud", "char-ilberd", "serves", "char-alphinaud", S(200), S(240), "main", ["C16"], ["M240e", "C52"]),
 ("rel-ilberd-allied-raubahn", "char-ilberd", "allied-with", "char-raubahn", S(200), S(240), "main", ["M200e"], ["M240i"]),
 ("rel-ilberd-opposes-raubahn", "char-ilberd", "opposes", "char-raubahn", S(240), None, "main", ["M240i", "M240j"]),
 ("rel-raubahn-leads-immortal-flames", "char-raubahn", "leads", "org-immortal-flames", S(200), None, "main", ["M200f"]),
 ("rel-raubahn-serves-nanamo", "char-raubahn", "serves", "char-nanamo", S(217), None, "main", ["M217i", "M217k"]),
 ("rel-ivy-serves-garlean-empire", "char-ivy", "serves", "org-garlean-empire", S(200), None, "main", ["M200b"]),
 ("rel-ivy-revealed-eline", "char-ivy", "revealed-as", "char-eline", S(210), None, "main", ["M210a"]),
 ("rel-eline-member-immortal-flames", "char-eline", "member-of", "org-immortal-flames", S(210), S(211), "main", ["M210a", "M210b"], ["M211c"]),
 ("rel-eline-serves-garlean-empire", "char-eline", "serves", "org-garlean-empire", S(210), None, "main", ["M210a"]),
 ("rel-eline-prisoner-ilberd", "char-eline", "prisoner-of", "char-ilberd", S(211), None, "main", ["M211c"]),
 ("rel-eline-serves-varis", "char-eline", "serves", "char-varis", S(217), None, "main", ["M217f", "M217g"]),
 ("rel-varis-leads-garlean-empire", "char-varis", "leads", "org-garlean-empire", S(209), None, "main", ["M209c", "M209d"]),
 ("rel-aymeric-leads-temple-knights", "char-aymeric", "leads", "org-temple-knights", S(202), None, "main", ["M202a"]),
 ("rel-aymeric-aids-scions", "char-aymeric", "aids", "org-scions", S(202), None, "main", ["M202c", "M202d"]),
 ("rel-lucia-serves-aymeric", "char-lucia", "serves", "char-aymeric", S(214), None, "main", ["M214c"]),
 ("rel-iceheart-leads-heretics", "char-iceheart", "leads", "org-heretics", S(202), None, "main", ["M202e"]),
 ("rel-heretics-opposes-temple-knights", "org-heretics", "opposes", "org-temple-knights", S(205), None, "main", ["M205b"]),
 ("rel-iceheart-opposes-holy-see", "char-iceheart", "opposes", "org-holy-see", S(227), None, "main", ["M227g", "M227h"]),
 ("rel-shiva-summoned-iceheart", "char-shiva", "summoned-by", "char-iceheart", S(213), None, "main", ["M213b"]),
 ("rel-drillemont-aids-scions", "char-drillemont", "aids", "org-scions", S(204), None, "main", ["M204d"]),
 ("rel-yuyuhase-member-crystal-braves", "char-yuyuhase", "member-of", "org-crystal-braves", S(208), None, "main", ["M208h"]),
 ("rel-alianne-member-crystal-braves", "char-alianne", "member-of", "org-crystal-braves", S(201), None, "main", ["M201e", "M201a"]),
 ("rel-moenbryda-aids-scions", "char-moenbryda", "aids", "org-scions", S(212), S(224), "main", ["M212c"], ["M224h"]),
 ("rel-crystal-braves-aids-immortal-flames", "org-crystal-braves", "aids", "org-immortal-flames", S(218), S(240), "main", ["M218a"], ["M240e"]),
 ("rel-nidhogg-leads-dravanian-horde", "char-nidhogg", "leads", "org-dravanian-horde", S(228), None, "main", ["M228f"]),
 ("rel-dravanian-horde-opposes-holy-see", "org-dravanian-horde", "opposes", "org-holy-see", S(227), None, "main", ["M227b"]),
 ("rel-scions-aids-holy-see", "org-scions", "aids", "org-holy-see", S(229), None, "main", ["M229c", "M229d"]),
 ("rel-crystal-braves-aids-holy-see", "org-crystal-braves", "aids", "org-holy-see", S(229), None, "main", ["M229c"]),
 ("rel-teledji-member-monetarists", "char-teledji", "member-of", "org-monetarists", S(218), S(240), "main", ["M218f"], ["M240h"]),
 ("rel-teledji-opposes-raubahn", "char-teledji", "opposes", "char-raubahn", S(216), S(240), "main", ["M216h"], ["M240h"]),
 ("rel-teledji-bribes-crystal-braves", "char-teledji", "bribes", "org-crystal-braves", S(238), S(240), "main", ["M238b", "M238c"], ["M240h"]),
 ("rel-wilred-member-crystal-braves", "char-wilred", "member-of", "org-crystal-braves", S(230), S235B, "main", ["M230d"], ["M235ba", "M235bb"]),
  ("rel-crystal-braves-turned-against-alphinaud", "org-crystal-braves", "turned-against", "char-alphinaud", S(240), None, "main", ["C52", "M240f"]),
 ("rel-pipin-member-immortal-flames", "char-pipin", "member-of", "org-immortal-flames", S(240), None, "main", ["M240l"]),
 ("rel-pipin-child-raubahn", "char-pipin", "child-of", "char-raubahn", S(240), None, "main", ["M240s", "M240l"]),
 ("rel-cid-aids-alphinaud", "char-cid", "aids", "char-alphinaud", S(240), None, "main", ["M240m"]),
 ("rel-yugiri-aids-tataru", "char-yugiri", "aids", "char-tataru", B, None, "main", ["C53"]),
 ("rel-elidibus-allied-lahabrea", "char-elidibus", "allied-with", "char-lahabrea", B, None, "main", ["M241g", "M241h"]),
]

# Relationships the 2.1–2.3 module defines (same IDs as the contract gives them): end Alphinaud's command of the
# Braves at #240, where they turn on him. (Reported as unknown when this module is linted alone.)
ADJUST = {"rel-alphinaud-leads-crystal-braves": {"until": S(240), "end": ["C52", "M240f"]}}

# ---- Arcs -----------------------------------------------------------------------------------------------------------
ARCS = [
 ("arc-d1-spies-and-heretics", ARC1, S(200), S(211)),
 ("arc-d2-saint-of-the-heretics", ARC2, S(212), S(217)),
 ("arc-d3-blade-for-the-ascians", ARC3, S(218), S(225)),
 ("arc-d4-horde-at-the-gates", ARC4, S(226), S(233)),
 ("arc-d5-royal-banquet", ARC5, S(234), B),
]

CASTS = {
 ARC1: [("char-alphinaud", S(200), ["C16"]), ("org-crystal-braves", S(200), ["C16"]), ("char-ilberd", S(200), ["C16"]),
        ("char-raubahn", S(200), ["M200e"]), ("char-ivy", S(200), ["M200b"]), ("char-aymeric", S(202), ["M202a"]),
        ("char-iceheart", S(202), ["M202e"]), ("char-shiva", S(203), ["M203e"]), ("char-yugiri", S(208), ["M208f"]),
        ("char-eline", S(210), ["M210a"])],
 ARC2: [("char-minfilia", S(212), ["M212c"]), ("char-moenbryda", S(212), ["M212c"]), ("char-iceheart", S(212), ["M212a"]),
        ("char-shiva", S(212), ["M212a"]), ("char-aymeric", S(214), ["M214c"]), ("char-lucia", S(214), ["M214c"]),
        ("char-eline", S(216), ["M216a"]), ("char-ilberd", S(216), ["M216d"]), ("char-raubahn", S(217), ["M217f"]),
        ("char-nanamo", S(217), ["M217h"])],
 ARC3: [("char-moenbryda", S(218), ["M218c"]), ("char-urianger", S(218), ["M218c"]), ("char-alphinaud", S(218), ["M218e"]),
        ("org-crystal-braves", S(218), ["M218a"]), ("char-ilberd", S(218), ["M218e"]),
        ("char-lucia", S(221), ["M221a"]), ("char-midgardsormr", S(221), ["M221d"]), ("char-nabriales", S(224), ["M224a"]),
        ("char-minfilia", S(224), ["M224d"])],
 ARC4: [("char-yda", S(226), ["M226b"]), ("char-lucia", S(227), ["M227a"]), ("char-iceheart", S(227), ["M227g"]),
        ("org-holy-see", S(227), ["M227c"]), ("char-aymeric", S(228), ["M228a"]), ("char-estinien", S(228), ["M228d"]),
        ("char-nidhogg", S(228), ["M228f"]), ("org-dravanian-horde", S(228), ["M228f"]), ("char-alphinaud", S(228), ["M228h"]),
        ("org-eorzean-alliance", S(231), ["M231a"])],
 ARC5: [("char-tataru", S(234), ["M234a"]), ("char-wilred", S235B, ["M235ba"]), ("char-haurchefant", S(240), ["M240n"]),
        ("char-teledji", S(238), ["M238b"]), ("char-alianne", S(239), ["M239a"]), ("char-nanamo", S(240), ["M240a"]),
        ("char-raubahn", S(240), ["M240h"]), ("char-ilberd", S(240), ["M240e"]), ("org-crystal-braves", S(240), ["M240e"]),
        ("char-alphinaud", S(240), ["C52"])],
}

ARC_NOTES = {
 "arc-d1-spies-and-heretics": "MSQ #200 *Traitor in the Midst* to #211 *In Flagrante Delicto* (12 steps). The Crystal Braves' first months: the hunt for the Ivy (M200b) "
   "runs alongside the hunt for Iceheart in Coerthas (M202e–M208b), and the two threads meet in the merchant who served both (M208c, M209a). "
   "It ends when Ilberd arrests Eline and Minfilia reports progress toward Iceheart's sanctum (M211c, M211f), the hand-off to the Shiva fight.",
 "arc-d2-saint-of-the-heretics": "MSQ #212 *A Simple Plan* to #217 *Let Us Cling Together* (6 steps): Moenbryda's beacon, Shiva's summoning and defeat (M213b), "
   "its aftermath in Ishgard and at the Rising Stones, and Eline's escape, recapture and unmasking as Varis's agent (M216a, M217f). "
   "It ends on Nanamo's republic announcement (M217h), which sets up the 2.5 and 2.55 story in Ul'dah.",
 "arc-d3-blade-for-the-ascians": "MSQ #218 *Good Intentions* to #225 *In Memory of Moenbryda* (8 steps). The Scions' search for a blade that can destroy an Ascian (M218c) "
   "frames the Braves' black-market trail, Midgardsormr stripping the blessing of Light (M221e) and Moenbryda's siphon, and ends with Nabriales destroyed, "
   "Moenbryda dead and her memorial (M224h, M225b).",
 "arc-d4-horde-at-the-gates": "MSQ #226 *Mask of Grief* to #233 *Administrative Decision* (8 steps): Ishgard's call for help, Nidhogg's Horde, the Alliance's refusal and "
   "the defense of the Steps of Faith (M232d), ending on the royal invitation (M233a). Riol's Wilred thread starts here (M230c) but stays out of the cast to keep it at 10.",
 "arc-d5-royal-banquet": "MSQ #234 to #240 and the 2.55 milestone (both parallel pairs, #234–235 and #234b–235b), 8 checkpoints. Tataru's training, the survey and "
   "Wilred's murder, Riol's bribery evidence, Alianne's disappearance and the banquet itself (M240a–M240r), ending at cp-arr-2-55 with the fugitives in Coerthas. "
   "It ends on the milestone, as the contract allows for an era's last arc.",
}

DECISIONS = [
 "**The Ivy is its own entry** (`char-ivy`, #200–#210), `revealed-as` Eline from #210, the Marques → Cid pattern. Eline carries “the Ivy” as an alias from #210.",
 "**Eline, never her surname.** The wiki and the quest title use “Roaille”; displayed text uses “Eline” and “Flame Marshal Eline”.",
 "**Iceheart keeps one entry** with “Ysayle” as an alias from #207, where she gives the name herself. Not a reveal of a known person, so no second entity. Later eras may prefer `char-ysayle`; the lead should pick one ID.",
 "**Nanamo is never stated dead.** She collapses, Teledji proclaims her murdered and Ilberd claims credit (M240c, M240d, M240j); no relationship of hers ends.",
 "**Nabriales is named only from #224** (ALLOW proposed). At #213 his line is “an unseen figure remarked that Lahabrea will be pleased”.",
 "**Estinien without his epithet** (“Wyrmblood” is banned); “the Azure Dragoon” is his alias.",
 "**The accepted cp-arr-2-55 relationships stay where they are.** Each cites Before the Dawn claims (C19b, C20, C21), so an ADJUST to #240 would cite a later quest. "
 "The Braves' turn is shown at #240 instead by `rel-crystal-braves-turned-against-alphinaud` and the presentations.",
 "**Momodi, Krile, Edelstein, Marcelain, Slafborn, Thubyrgeim and Laurentius are left unnamed** in displayed text (incidental here).",
 "**No entries for Riol, House Fortemps or Ishgard the place.** Their names already appear in accepted 2.0 text (#104, #116, #112), so an entry first visible "
 "in this era would fail the visibility rule there. Riol and House Fortemps are named in text only; Ishgard is the `org-holy-see` entry (“The Holy See”), "
 "matching the 3.0 modules. If the lead backfills `char-riol` from #104, his 2.5 presentations and his place in the d3 and d5 casts can come back.",
 "**`char-raubahn` breaks the A4 recap at #159** (“General Raubahn”, accepted). Every era that creates him hits it, the 2.1–2.3 module included; the fix belongs in the accepted content.",
]

ALLOW = {"Nabriales": S(224)}  # he names himself in #224 and dies there; proposed for the lead's acceptance
