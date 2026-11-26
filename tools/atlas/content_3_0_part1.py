"""Atlas content for patch 3.0, part 1: MSQ #242 *Coming to Ishgard* to #291 *New Winds, Old Friends* (arc tag e).

Data only, merged by build_pilot_content.py (see docs/atlas/era-modules.md). Researched 2026-11-19 from the saved Console
Games Wiki wikitext (lanes L11–L15); every locator is copied from those pages.

Parallel chains. After #244 the story splits into Artoirel's chain (#245–#251, Falcon's Nest) and Emmanellain's chain
(#245b–#251b, Camp Cloudtop); both rejoin at #259. The timeline orders Artoirel's chain first, but a player may do either
first, so records follow one rule: nothing visible on an Emmanellain step depends on an Artoirel-only event.
  - Arc e1 (Artoirel's chain) and arc e2 (Emmanellain's chain) are separate arcs. Arc e1's entry and Artoirel get a
    chain-neutral presentation at #245b (the story as of #244) and a full one at #259, once both chains are done.
  - Artoirel-chain facts about other entities (Haurchefant's parentage, the meeting with Iceheart) reach those entities
    only at #259. Midgardsormr and Hraesvelgr, who first come up in Artoirel's chain, become entries at #270, and the
    #250 recap does not name them. Iceheart's #245 presentation (a heretic leader, named by Artoirel) does show on
    Emmanellain steps; it holds nothing more than her name and the Holy See's campaign against her.
  - Emmanellain's chain comes later in the timeline, so nothing of it is visible on Artoirel steps.
Spoiler rules this module follows: no surnames ("Garlond" is never shown, so Cid is only Cid), no "Heavensward",
no "new primal", no "The First" (so no claim cites #247 *The First and Foremost*, whose title and URL contain it: #247
is covered by the arc recap alone), and no name from the 3.0 voice that speaks after Ravana (a banned Ascian name).
"""

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

S = {n: f"cp-msq-{n}" for n in ["242", "243", "244", "245", "246", "247", "248", "249", "250", "251",
                                 "245b", "246b", "247b", "248b", "249b", "250b", "251b",
                                 "259", "260", "261", "262", "263", "264", "265", "266", "267", "268", "269", "270",
                                 "271", "272", "273", "274", "275", "276", "277", "278", "279", "280",
                                 "281", "282", "282b", "282c", "285", "286", "287", "288", "289", "290", "291"]}

# ---- Claims: id -> (own-words claim, source quest, verbatim locator) ----------------------------------------------
CLAIMS = {
 # #242 Coming to Ishgard
 "M242a": ("Count Edmont has made you, Alphinaud and Tataru wards of House Fortemps.", "Coming to Ishgard", "Count Edmont has decreed that the three of you be taken in as wards of House Fortemps."),
 "M242b": ("Haurchefant offers the family manor as the Scions' new headquarters.", "Coming to Ishgard", "Pray consider our manor your new headquarters"),
 "M242c": ("Ishgard is devoted to Halone and ruled by Archbishop Thordan VII of the Ishgardian Orthodox Church.", "Coming to Ishgard", "A great and proud nation devoted to Halone, the Fury, ruled by Thordan VII, Archbishop of the Ishgardian Orthodox Church..."),
 "M242d": ("After a thousand years of war, Ishgard had forgotten peace.", "Coming to Ishgard", "A land that after a thousand years of war had forgotten what it was to be at peace."),
 "M242e": ("The Scions, betrayed by the Crystal Braves, fled the victory banquet and are condemned as murderers.", "Coming to Ishgard", "are now condemned as murderers─betrayed by the [[Crystal Braves]] and forced to flee the banquet held to celebrate the very victory"),
 "M242f": ("Your comrades stayed behind one by one, and you alone escaped to rejoin Alphinaud and take refuge in Coerthas.", "Coming to Ishgard", "until you alone emerged from the tunnels beneath [[Ul'dah]] to be reunited with Alphinaud and seek refuge in [[Coerthas]]"),
 "M242g": ("Haurchefant says any missing allies who are found will be welcome at the manor.", "Coming to Ishgard", "should any of your missing allies be found─as I am certain they shall─they will of course be welcome to join you there."),
 "M242h": ("Fortemps Manor is Haurchefant's family home.", "Coming to Ishgard", "Allow me to present to you my family home: Fortemps Manor!"),
 "M242i": ("Ishgard has closed its borders for the war, and Edmont's decision will raise eyebrows among the other High Houses.", "Coming to Ishgard", "'Tis true that Ishgard's first thought has ever been the war effort, hence the closing of our borders... … Granted, my decision will have raised eyebrows in the Vault and in the halls of the other High Houses."),
 "M242j": ("Wyverns recently wrought destruction in Ishgard's Foundation.", "Coming to Ishgard", "As you arrive in [[Foundation]], you find that the destruction wrought by the [[wyvern]]s is still fresh."),
 # #243 Taking in the Sights
 "M243a": ("Ishgard's borders have been closed for decades, so many of its people are unused to foreigners.", "Taking in the Sights", "Given that our borders have remained closed for decades, many of my countrymen are unaccustomed to treating with foreigners."),
 "M243b": ("Archbishop Thordan VII lives in and rules from the Holy Vault.", "Taking in the Sights", "wherein [[Thordan VII]], Archbishop of the [[Ishgardian Orthodox Church]], resides and rules."),
 "M243c": ("Alphinaud and Tataru resolve to learn more of Ishgard.", "Taking in the Sights", "Alphinaud and [[Tataru]] resolve to learn more of Ishgard."),
 # #244 The Better Half
 "M244a": ("The Brume suffered worst in the wyvern attack, while the Pillars had the High Houses and Temple Knights to protect them.", "The Better Half", "it was the Brume that got the worst of it, while the Pillars enjoyed the protection of the High Houses and the Temple Knights."),
 "M244b": ("Ser Aymeric has ordered his knights to strengthen Ishgard's defenses, and every house is asked to help.", "The Better Half", "Ser Aymeric has ordered his knights to strengthen our defenses, and each house has been called upon to lend what support it can."),
 "M244c": ("Edmont accepts the Scions' help, hoping to secure provisions from abroad.", "The Better Half", "Such qualities may prove most useful to us in our efforts to secure provisions from foreign sources"),
 "M244d": ("Edmont asks you to help his sons, Artoirel and Emmanellain, with their duties.", "The Better Half", "to aid Artoirel and Emmanellain in their duties."),
 "M244e": ("Edmont's two sons greet the offer with indignation and mirth.", "The Better Half", "unlike his two sons, who greet your proposal with a mixture of indignation and mirth."),
 "M244f": ("By granting the Scions patronage, House Fortemps has taken a great risk.", "The Better Half", "By granting us patronage, House Fortemps has taken a tremendous risk."),
 "M244g": ("Tataru stays at the Forgotten Knight tavern to gather news, perhaps of the missing Scions.", "The Better Half", "[[Tataru]] proposes that she stay behind and ingratiate herself with the regulars."),
 # #245 Over the Wall (Artoirel)
 "M245a": ("Artoirel, Edmont's eldest son, is sent to aid Houses Durendaire and Dzemael, despite the old rivalries between Ishgard's noble families.", "Over the Wall", "Ser Artoirel de Fortemps, eldest son of [[Count Edmont de Fortemps]], did not expect to have company on his mission to aid houses [[House Durendaire|Durendaire]] and [[House Dzemael|Dzemael]] … given the ancient rivalries between [[Ishgard]]'s noble families"),
 "M245b": ("Artoirel takes your company as a sign his father does not trust him to work alone.", "Over the Wall", "the count has given Artoirel cause to believe that his father does not trust him to carry out his duties alone."),
 "M245c": ("The Holy See wills that the houses set aside their differences.", "Over the Wall", "it is the will of the Holy See that we set aside our differences at this crucial juncture."),
 "M245d": ("Falcon's Nest was abandoned in the Ishgardian withdrawal after the Calamity.", "Over the Wall", "which was abandoned during the Ishgardian withdrawal shortly after [[the Calamity]]."),
 "M245e": ("The Holy See has ordered the western highlands reclaimed and the heretics expelled.", "Over the Wall", "The Holy See has commanded the reclamation of the western highlands and the expulsion of heretical elements."),
 "M245f": ("Lady Iceheart and her kind have roamed the western highlands unchecked since then.", "Over the Wall", "Lady Iceheart and her kind have walked these lands with impunity ever since."),
 "M245g": ("Artoirel pledges House Fortemps to the Durendaire knight commanding Falcon's Nest.", "Over the Wall", "As promised, we of House Fortemps are at your disposal, Ser Redwald."),
 # #246 Work in Progress
 "M246a": ("House Dzemael's craftsmen are rebuilding Falcon's Nest.", "Work in Progress", "Several craftsmen in service to House Dzemael are contributing to the restoration of Falcon's Nest."),
 "M246b": ("You slay the icicle sprites sabotaging the work.", "Work in Progress", "It would seem that Rothe was correct, as you discover and slay numerous icicle sprites within the walls of Falcon's Nest."),
 # #248 From on High
 "M248a": ("A mason at the Pike and a knight at the Anvil look out for each other, though decorum keeps the knight from showing it.", "From on High", "Torn between decorum and her desire to do right by the hardworking mason"),
 "M248b": ("A sudden development has the commander of Falcon's Nest calling on everyone, you and Artoirel included.", "From on High", "I have a task to which I would commit all able-bodied men and women─you and Lord Artoirel included."),
 # #249 Reconnaissance Lost
 "M249a": ("A reconnaissance party sent north to find the heretics' hideaway has gone silent.", "Reconnaissance Lost", "We have lost contact with a reconnaissance party sent north to Riversmeet in search of the heretics' hideaway."),
 "M249b": ("The sole survivor says heretics ambushed the party in a blizzard.", "Reconnaissance Lost", "ambushed by the heretics in the midst of a furious blizzard"),
 "M249c": ("The survivor says the heretics' hideaway lies to the north.", "Reconnaissance Lost", "the heretics' hideaway lies somewhere to the north."),
 "M249d": ("You and Artoirel save the knight.", "Reconnaissance Lost", "Three heretics slain and one knight saved, just like that."),
 # #250 At the End of Our Hope
 "M250a": ("Artoirel sends you to follow the heretics' trail alone.", "At the End of Our Hope", "Accordingly, Lord Artoirel assigns you the unenviable task of following the trail alone"),
 "M250b": ("In a lair below Gorgagne Mills you meet an old foe, Lady Iceheart.", "At the End of Our Hope", "Within the secret lair hidden below [[Gorgagne Mills]], you are reunited with an old foe: the Lady [[Iceheart]]."),
 "M250c": ("An ancient wyrm in your company reveals himself to Iceheart, to her shock.", "At the End of Our Hope", "reveals himself to the heretic leader, who is shocked to see the ancient wyrm in your company."),
 "M250d": ("Iceheart has the Echo, which showed her the truth of the Dragonsong War through a great wyrm's eyes.", "At the End of Our Hope", "she too is blessed with [[the Echo]], and that it allowed her to see the truth of the [[Dragonsong War]] through the eyes of [[Hraesvelgr]]"),
 "M250e": ("Iceheart says she was chosen to bring dragon and man together again.", "At the End of Our Hope", "I was chosen to deliver this revelation to the people─to bring dragon and man together, as they once were, and should ever be!"),
 "M250f": ("Iceheart helped the Dravanians breach Ishgard's wards, and their slaughter leaves her doubting.", "At the End of Our Hope", "the indiscriminate slaughter committed by the [[Dravanian Horde|Dravanians]] whom she helped to breach the wards, her doubts soon resurface"),
 "M250g": ("Iceheart swears to break the cycle and restore peace.", "At the End of Our Hope", "I will see this cycle broken and peace restored."),
 "M250h": ("You let Iceheart escape.", "At the End of Our Hope", "nor of the Lady Iceheart, whom you allowed to escape."),
 # #251 Knights Be Not Proud
 "M251a": ("Falcon's Nest's commander releases you and Artoirel, and will report your deeds to the Holy See.", "Knights Be Not Proud", "affirms his intent to deliver a glowing report to the [[Holy See]]"),
 "M251b": ("Haurchefant is Artoirel's bastard half-brother.", "Knights Be Not Proud", "Lord [[Haurchefant]]─his bastard half-brother─holds you in such high esteem."),
 "M251c": ("Artoirel calls Haurchefant the legacy of their father's only indiscretion, whom his mother never acknowledged.", "Knights Be Not Proud", "the legacy of my father's sole indiscretion. … Even on her deathbed, she refused to acknowledge him."),
 "M251d": ("Artoirel admits he half hoped you would fail.", "Knights Be Not Proud", "I told myself it was to be a test, but part of me...part of me hoped that you would fail."),
 "M251e": ("Artoirel swears never to doubt you again.", "Knights Be Not Proud", "swears never to doubt you again."),
 # #245b Onwards and Upwards (Emmanellain)
 "M245ba": ("Emmanellain, Edmont's second son, longs to escape his elder brother's shadow.", "Onwards and Upwards", "has long dreamed of emerging from beneath his elder brother's shadow"),
 "M245bb": ("Emmanellain hopes his deeds will raise him above Artoirel in the people's eyes.", "Onwards and Upwards", "so that the tales of my great deeds can win me a place in the people's hearts─or better yet, raise me higher in their estimations than Artoirel!"),
 "M245bc": ("Emmanellain's mission is to aid House Haillenarte.", "Onwards and Upwards", "we are to aid the good men and women of House Haillenarte."),
 "M245bd": ("Camp Cloudtop was built to warn of Dravanian incursions.", "Onwards and Upwards", "Camp Cloudtop was established to provide early warning of impending Dravanian incursions."),
 "M245be": ("Ser Laniaitte of House Haillenarte commands Camp Cloudtop.", "Onwards and Upwards", "I am Ser Laniaitte de Haillenarte, commander of the forces stationed here at Camp Cloudtop."),
 "M245bf": ("The camp's great airship, the Protector, is under repair, hampered by skirmishes with the Vanu Vanu.", "Onwards and Upwards", "our efforts have been hampered by an indigenous beast tribe known as the Vanu Vanu, with whom we have had several skirmishes already."),
 "M245bg": ("Laniaitte is the elder sister of Francel, whose unjust execution you prevented.", "Onwards and Upwards", "Lady Laniaitte explains that she is the elder sister of Lord [[Francel]], whose unjust execution you prevented during your search for the ''Enterprise'' long ago."),
 "M245bh": ("Laniaitte thinks little of Emmanellain, who does not notice.", "Onwards and Upwards", "though the young lord seems oblivious to her low opinion of him."),
 "M245bi": ("Emmanellain resents being born second in a society where the eldest inherits all.", "Onwards and Upwards", "What ill fortune to be born second in a society where the eldest inherits all."),
 # #246b An Indispensable Ally
 "M246ba": ("Laniaitte keeps Emmanellain out of trouble with a watch for Dravanian outflyers.", "An Indispensable Ally", "Tell him...tell him that I would like him to keep watch for...Dravanian outflyers."),
 "M246bb": ("Laniaitte spares Emmanellain's feelings only for the close ties between Houses Haillenarte and Fortemps.", "An Indispensable Ally", "Were it not for the close relationship between [[House Haillenarte]] and [[House Fortemps]], Lady Laniaitte would not feel obligated to spare Lord Emmanellain's feelings."),
 # #247b Meeting the Neighbors
 "M247ba": ("After half a year of peace, the Vanu turned hostile for no known reason.", "Meeting the Neighbors", "There was peace between our peoples for half a year, until suddenly, for reasons unknown, their attitudes towards us changed."),
 "M247bb": ("The Vanu attack the camp's foragers unprovoked.", "Meeting the Neighbors", "They began to attack our foraging parties without provocation, forcing us to rely more heavily on supplies flown in from Ishgard."),
 "M247bc": ("You drive off Vanu on patrol.", "Meeting the Neighbors", "As expected, you spy several Vanu during your patrol and are forced to drive them off."),
 # #248b Sense of Urgency
 "M248ba": ("Camp Cloudtop has never recorded a Dravanian intrusion.", "Sense of Urgency", "Despite being built as an observation post, we have yet to record a single intrusion by the Horde."),
 "M248bb": ("Emmanellain demands a grand mission befitting his station.", "Sense of Urgency", "Lady Laniaitte ''will'' give me a grand mission as befits my station!"),
 # #249b Hope Springs Eternal
 "M249ba": ("Laniaitte sends you and Emmanellain to fetch a spring crystal for water.", "Hope Springs Eternal", "I would have you and Emmanellain bring one back to us."),
 "M249bb": ("Emmanellain runs off, and does not come back.", "Hope Springs Eternal", "It would seem you were the first to return and present him with an entry, for Lord Emmanellain is nowhere to be seen..."),
 # #250b A Series of Unfortunate Events
 "M250ba": ("The Vanu Vanu capture Emmanellain.", "A Series of Unfortunate Events", "Honoroit screams that Lord Emmanellain has been captured by the [[Vanu Vanu]]."),
 "M250bb": ("Haurchefant arrives with knights to help free him, but the Vanu surround you.", "A Series of Unfortunate Events", "who arrives in the nick of time with a party of knights … However, the Vanu are too numerous, and you soon find yourselves surrounded with no means of escape."),
 "M250bc": ("The Vanu chieftain calls forth Bismarck, Lord of the Mists, a primal.", "A Series of Unfortunate Events", "[[Bismarck]], Lord of the Mists, the chieftain names it, and Haurchefant realizes with horror that the creature is a [[primal]]."),
 "M250bd": ("Cid swoops in aboard the Enterprise and carries you away.", "A Series of Unfortunate Events", "swoops down aboard the ''Enterprise'' and spirits you away."),
 "M250be": ("The Holy See has asked the Ironworks for help with its airship, the Protector.", "A Series of Unfortunate Events", "The Holy See has petitioned the Ironworks for assistance with this creation of theirs, the ''Protector''."),
 "M250bf": ("Cid promises to speak with you again soon.", "A Series of Unfortunate Events", "Don't worry, old friend─we'll speak again soon, I promise."),
 # #251b A Reward Long in Coming
 "M251ba": ("The Vanu have summoned a primal, which must lie behind their hostility.", "A Reward Long in Coming", "Lady Laniaitte is shocked to hear that the Vanu have summoned a primal, and all agree that its presence must be behind the recent rise in Vanu hostility."),
 "M251bb": ("Laniaitte praises you for rescuing Emmanellain from a doom of his own making.", "A Reward Long in Coming", "praises you for rescuing the young lord from a doom of his own making."),
 "M251bc": ("Haurchefant goes to tell Ser Aymeric of the Congregation what happened.", "A Reward Long in Coming", "I must make for the Congregation and inform Ser Aymeric of all that has occurred."),
 "M251bd": ("Edmont scolds Emmanellain for his recklessness.", "A Reward Long in Coming", "having received a dressing down from his father for his recklessness."),
 # #259 Divine Intervention
 "M259a": ("Ser Grinnaux of the Heavens' Ward has arrested Alphinaud and Tataru for fomenting heresy.", "Divine Intervention", "have been arrested by a knight of the [[Heavens' Ward]]—one “[[Ser Grinnaux]]”—on the charge of fomenting heresy."),
 "M259b": ("The Heavens' Ward is the archbishop's personal guard: twelve knights who answer only to him.", "Divine Intervention", "the personal guard of the [[Thordan VII|archbishop]]. These twelve chosen sers answer to none save the archbishop himself, and their testimony is unimpeachable."),
 "M259c": ("Only a trial by combat can disprove the charge.", "Divine Intervention", "by granting victory in a trial by combat between the accuser and the accused."),
 "M259d": ("Grinnaux is a son of House Dzemael.", "Divine Intervention", "Alas, he is also a son of House Dzemael."),
 "M259e": ("Edmont suspects another member of House Dzemael is manipulating Grinnaux.", "Divine Intervention", "'Tis like that one such member of House Dzemael is manipulating Ser Grinnaux, for he is not a man to dabble in politics of his own volition."),
 "M259f": ("Edmont believes the charges are a political ploy against House Fortemps.", "Divine Intervention", "The count believes the charges leveled against your friends to be nothing more than a political ploy to defame [[House Fortemps]]."),
 "M259g": ("Aymeric, the lord commander, believes them innocent but cannot overrule the Heavens' Ward.", "Divine Intervention", "Though Ser Aymeric believes your friends to be innocent, he is powerless to intervene as the knight who accused them is a member of the Heavens' Ward"),
 "M259h": ("Edmont sends you to the lord commander, Ser Aymeric.", "Divine Intervention", "pay the lord commander a visit at the [[Congregation of Our Knights Most Heavenly]]"),
 "M259i": ("You defeat Grinnaux and his second in the trial, and your friends go free.", "Divine Intervention", "you defeat Ser Grinnaux and [[Ser Paulecrain]], thus earning your comrades their freedom."),
 "M259j": ("Haurchefant gives you a black chocobo that can fly.", "Divine Intervention", "a fully trained [[Black Chocobo|black chocobo]]"),
 "M259k": ("Edmont has heard of all you did at Falcon's Nest and Camp Cloudtop.", "Divine Intervention", "Having been informed of all you accomplished during your time in [[Falcon's Nest]] and [[Camp Cloudtop]], Count [[Edmont]] wishes to express his heartfelt gratitude."),
 # #260 Disclosure
 "M260a": ("Thordan VII apologizes for your friends' wrongful arrest.", "Disclosure", "Thordan VII warmly welcomes you and apologizes for the misunderstanding that led to Alphinaud and Tataru's incarceration."),
 "M260b": ("Ser Zephirin, of the Heavens' Ward, admits the Ward acted on false information.", "Disclosure", "Regrettably, it would appear that we of the Heavens' Ward were in receipt of erroneous information."),
 "M260c": ("Thordan says the Ascians offered Ishgard power to keep fighting the dragons.", "Disclosure", "Those harbingers of chaos and strife offered us power, that we might continue our war against the dragons."),
 "M260d": ("Thordan says he pays the Ascians lip service while plotting against them, and asks your help.", "Disclosure", "he is paying lip service to their wishes while plotting to move against them. He asks for your help in this endeavor"),
 "M260e": ("Alphinaud is shocked that the Ascians' influence reaches Ishgard.", "Disclosure", "Alphinaud is shocked to learn that the Ascians' influence has also spread to [[Ishgard]]."),
 "M260f": ("Raubahn, the deposed Flame General, is to be executed, and Alphinaud resolves to rescue him.", "Disclosure", "It would seem that [[Raubahn]] is to be executed for crimes against the sultanate. Determined not to lose yet another ally, Alphinaud resolves to do everything in his power to rescue the deposed Flame General."),
 # #261 Flame General Affairs
 "M261a": ("Merlwyb remains a stout ally of the Scions.", "Flame General Affairs", "who remains a stout ally to the [[Scions]]"),
 "M261b": ("The Crystal Braves have moved Raubahn somewhere unknown ahead of his execution.", "Flame General Affairs", "[[Raubahn]] has been moved to an unknown location ahead of his impending execution—by none other than the [[Crystal Braves]]."),
 "M261c": ("Merlwyb and the Elder Seedseer made the Syndicate keep the Scions' alleged crimes quiet until proof is found.", "Flame General Affairs", "On Marshal Tarupin's urging, the Elder Seedseer and I demanded that the Syndicate suppress news of the Scions' alleged crimes until such time as irrefutable evidence could be found."),
 "M261d": ("The sultana meant to abdicate and make way for an Ul'dahn republic.", "Flame General Affairs", "There, she revealed her intent to announce her abdication, that she might pave the way for the establishment of an Ul'dahn republic."),
 "M261e": ("Alphinaud suspects Lolorito and Teledji plotted the sultana's assassination.", "Flame General Affairs", "Lolorito and Teledji plotted the sultana's assassination in the hope of maintaining the constitutional status quo...?"),
 "M261f": ("Ul'dah claims the sultana is convalescing from illness.", "Flame General Affairs", "To allay any suspicion that may arise from Her Grace's absence, they have issued a statement to the effect that she is presently convalescing from illness."),
 "M261g": ("Merlwyb cannot send troops into Ul'dah without ending the Alliance.", "Flame General Affairs", "But I cannot send troops into Ul'dah. 'Twould spell the end of the Alliance, and war, like as not."),
 "M261h": ("Alphinaud takes responsibility for the Crystal Braves he founded.", "Flame General Affairs", "It was I who founded the Crystal Braves, and I who must take responsibility for their actions."),
 "M261i": ("The Crystal Braves turned on the Domans at the victory feast and took the Rising Stones by force.", "Flame General Affairs", "Even as the victory feast was taking place, the Crystal Braves turned upon us and took the Rising Stones by force."),
 "M261j": ("The shinobi of Doma are gathering intelligence on Raubahn's whereabouts.", "Flame General Affairs", "the shinobi of [[Doma]] have been frantically gathering intelligence on the Flame General's whereabouts"),
 # #262 In Search of Raubahn
 "M262a": ("A unit of Crystal Braves has left the Rising Stones to escort Raubahn to his execution.", "In Search of Raubahn", "Their purpose: to escort [[Raubahn]] to his execution."),
 "M262b": ("The Domans are shadowing the Braves.", "In Search of Raubahn", "This can be no simple coincidence. Their purpose, we believe, is to escort the Flame General to the scene of his execution."),
 "M262c": ("Ilberd, the traitor, has entered Halatali.", "In Search of Raubahn", "But moments ago, the traitor Ilberd arrived and entered Halatali."),
 # #263 Keeping the Flame Alive
 "M263a": ("With Alphinaud and Yugiri you rescue Raubahn from the Crystal Braves.", "Keeping the Flame Alive", "With the aid of [[Alphinaud]] and [[Yugiri]], you have succeeded in rescuing Raubahn from the clutches of the traitorous [[Crystal Braves]]."),
 "M263b": ("Ilberd denies killing the sultana.", "Keeping the Flame Alive", "'Twas not I who assassinated the sultana, boy!"),
 "M263c": ("Ilberd says all he wanted was to free his homeland.", "Keeping the Flame Alive", "All I ever wanted was to liberate my homeland, and I ate dirt to make it happen."),
 "M263d": ("Dewlala, head of the Order of Nald'thal, is a member of the Syndicate.", "Keeping the Flame Alive", "I am Dewlala, head of the Order of Nald'thal, and member of the Syndicate."),
 "M263e": ("Dewlala confirms Nanamo is still alive, perhaps held in an induced slumber.", "Keeping the Flame Alive", "she confirms Alphinaud's suspicion that [[Nanamo]] is still alive, and goes on to speculate that the sultana may be confined somewhere in a state of induced slumber."),
 "M263f": ("Dewlala says Nanamo lives because Lolorito willed it.", "Keeping the Flame Alive", "She lives because Lolorito willed it."),
 "M263g": ("Dewlala believes Teledji plotted the assassination alone and Lolorito exploited it.", "Keeping the Flame Alive", "'Tis my belief that Teledji plotted the sultana's assassination alone, but that Lolorito caught wind of his plot, and exploited it to his own ends."),
 "M263h": ("Raubahn is brought to the Waking Sands.", "Keeping the Flame Alive", "Upon arriving at the Waking Sands, you are greeted by a number of familiar faces"),
 # #264 To Siege or Not to Siege
 "M264a": ("The Dravanian Horde gathers to renew its assault on Ishgard.", "To Siege or Not to Siege", "It would seem the [[Dravanian Horde|Horde]] gathers once more to renew its assault upon the city."),
 "M264b": ("Raubahn is in safe hands.", "To Siege or Not to Siege", "Tataru? ...Yes, General Raubahn is now in safe hands."),
 "M264c": ("The Scions lack the evidence to act on Dewlala's claims.", "To Siege or Not to Siege", "we lack the necessary evidence to act upon Dewlala's claims."),
 "M264d": ("Trappers saw a cloud of dragons big enough to dim the sky.", "To Siege or Not to Siege", "a band of trappers returning from the west claim they saw a cloud of dragons big enough to dim the midday sky!"),
 "M264e": ("Nidhogg's minions are gathering for war.", "To Siege or Not to Siege", "Nidhogg's minions gather once more for war..."),
 "M264f": ("Edmont offers the Scions the choice of staying in a besieged Ishgard or seeking refuge elsewhere.", "To Siege or Not to Siege", "Scions of the Seventh Dawn, you are faced with a choice: to remain in a besieged Ishgard, or seek sanctuary elsewhere."),
 "M264g": ("Alphinaud is tired of running.", "To Siege or Not to Siege", "The count would have us seek shelter from this storm, but I, for one, grow tired of running."),
 # #265 Alphinaud's Way
 "M265a": ("Alphinaud hopes Iceheart can persuade Nidhogg to abandon his course.", "Alphinaud's Way", "If we can persuade Iceheart to act as our intermediary, we may yet be able to convince Nidhogg to abandon his bloody course."),
 "M265b": ("Estinien, Ishgard's Azure Dragoon, insists on joining the parley with Nidhogg.", "Alphinaud's Way", "you are approached by [[Estinien]], [[Ishgard]]'s famed [[Azure Dragoon]]. He insists on accompanying you to the proposed parley with [[Nidhogg]]"),
 "M265c": ("Alphinaud agrees on condition that Estinien uses his lance only if words fail.", "Alphinaud's Way", "I should only turn to your lance if my words failed to find their mark."),
 "M265d": ("Estinien carries the power of the Eye.", "Alphinaud's Way", "With the power of the Eye at my disposal, and the vaunted strength of the Warrior of Light, we could conceivably slay the beast outright..."),
 "M265e": ("Aymeric will support any effort that could spare his countrymen's blood.", "Alphinaud's Way", "I will gladly lend my support to any endeavor that could spare the blood of my countrymen"),
 "M265f": ("Thordan tells Zephirin they will reward their Ascian allies once the dragons are gone.", "Alphinaud's Way", "And when we have rid the world of their pestilence, we shall turn our attention to our Ascian allies─see that they are suitably rewarded for their invaluable assistance."),
 "M265g": ("Zephirin worries the Paragons may see through their deception.", "Alphinaud's Way", "The Paragons wield powers strange and unknowable. Can we be certain that they will not see through our deception?"),
 "M265h": ("Zephirin, in a changed voice, swears by the glory of King Thordan.", "Alphinaud's Way", "For the glory of King Thordan..."),
 # #266 In Search of Iceheart
 "M266a": ("Alphinaud begins the search for Iceheart in the western highlands, where you last met her.", "In Search of Iceheart", "Alphinaud proposes that you begin the search for Lady [[Iceheart]] in the last place you encountered her"),
 "M266b": ("Tataru keeps searching for the missing Scions.", "In Search of Iceheart", "promises to continue her search for the missing [[Scions]] in your absence."),
 "M266c": ("Knights are picking over the heretics' abandoned hideaway at Gorgagne Mills.", "In Search of Iceheart", "an expedition sent to pick over the remnants of the heretic hideaway you discovered at [[Gorgagne Mills]]."),
 # #267 From One Heretic to Another
 "M267a": ("The heretics' letters show Iceheart's followers still use the Akh Afah Amphitheatre as a base.", "From One Heretic to Another", "it would seem the amphitheatre is still being used as a base by Iceheart's minions..."),
 # #268 Sounding Out the Amphitheatre
 "M268a": ("The heretics at the amphitheatre refuse to parley and attack.", "Sounding Out the Amphitheatre", "the heretics are not inclined to trust his word, and the encounter quickly devolves into violence"),
 "M268b": ("The heretics drink the blood of dragons.", "Sounding Out the Amphitheatre", "They partake of the blood of dragons!"),
 "M268c": ("Iceheart is not at the amphitheatre.", "Sounding Out the Amphitheatre", "I see no sign of Lady Iceheart."),
 "M268d": ("Estinien sends you to the Convictors at Twinpools.", "Sounding Out the Amphitheatre", "I am told the Convictors have set up camp in Twinpools."),
 # #269 Camp of the Convictors
 "M269a": ("Heretics win lowborn conscripts with the promise of freedom.", "Camp of the Convictors", "From what I hear, the simple promise of freedom tends to do it."),
 "M269b": ("Purple smoke in the highlands summons the heretics.", "Camp of the Convictors", "Send up some purple smoke, and the bastards come to you."),
 "M269c": ("Alphinaud thinks that promise explains how fast Iceheart's following grew.", "Camp of the Convictors", "That may explain how Lady Iceheart was able to expand her following so swiftly."),
 # #270 Purple Flame, Purple Flame
 "M270a": ("Iceheart tells how an Elezen tribe came to claim Coerthas over a millennium ago.", "Purple Flame, Purple Flame", "'Twas more than a millennium past when an Elezen tribe first sought to claim the lands of Coerthas as its home."),
 "M270b": ("In her tale, the maid Shiva asked the wyrm Hraesvelgr to consume her so their spirits would be joined forever.", "Purple Flame, Purple Flame", "Unable to bear the thought of their separation, the maid bid the wyrm consume her, that their spirits might be entwined for eternity."),
 "M270c": ("Iceheart says Nidhogg lost an eye to Elezen treachery.", "Purple Flame, Purple Flame", "Nidhogg─he who now stands poised to unleash his wyrmlings upon Ishgard─was the great dragon who lost an eye to Elezen treachery."),
 "M270d": ("Estinien kept the Eye with him to draw Nidhogg away from Ishgard.", "Purple Flame, Purple Flame", "Indeed, it was for that very reason that I kept it with me as I roamed the land, attempting to draw him away from the city."),
 "M270e": ("Iceheart agrees to take you to Hraesvelgr.", "Purple Flame, Purple Flame", "You ''still'' believe that a peaceable solution can be found? Very well. I will take you to him."),
 "M270f": ("Midgardsormr notes that his mistress's blessing on you is stronger than it was.", "Purple Flame, Purple Flame", "Curious... The vestiges of thy mistress's blessing are not as faint as once they were..."),
 "M270g": ("Your Crystal of Ice flares as you set out for the dragons' homeland.", "Purple Flame, Purple Flame", "As you resolve to depart for the dragons' homeland, the light of your Crystal of Ice suddenly flares once more..."),
 # #271 Where the Chocobos Roam
 "M271a": ("Iceheart asks you to use her true name, Ysayle.", "Where the Chocobos Roam", "Lady [[Iceheart]] invites you to use her true name, [[Ysayle]],"),
 "M271b": ("Sohm Al is the ancient home of dragonkind.", "Where the Chocobos Roam", "Into the deepening shadows of Sohm Al, where lies the ancient home of dragonkind..."),
 "M271c": ("The path to Sohm Al lies far to the west through Dravania.", "Where the Chocobos Roam", "We now stand on the threshold of Dravania. The path to Sohm Al will take us far to the west"),
 "M271d": ("The dragons have been murderous of late.", "Where the Chocobos Roam", "The dragons've been absolutely bleedin' ''murderous'' of late."),
 # #272 Worse than Dragons
 "M272a": ("The Gnath, a beast tribe, have turned to unprovoked hostility.", "Worse than Dragons", "tells you of the [[beast tribe]] known as the [[Gnath]], and of their recent acts of unprovoked hostility."),
 "M272b": ("Ysayle fled into Dravania after the Calamity, her family dead and her home gone.", "Worse than Dragons", "My family was dead, my home was gone, and I had fled from the bitter cold into these lands."),
 "M272c": ("Ysayle says the ruins date from an age when her ancestors and dragonkind lived in peace.", "Worse than Dragons", "It is a remnant of the age when our ancestors and dragonkind lived together in peace."),
 "M272d": ("Estinien was taught the ruins were built by heretics.", "Worse than Dragons", "I was taught that these buildings were constructed by heretics, in honor of your Dravanian masters."),
 "M272e": ("Alphinaud says the Echo's visions will settle their dispute.", "Worse than Dragons", "he declares that their debate will presently be settled by the indisputable visions granted you by the Echo."),
 # #273 The Trine Towers
 "M273a": ("Without the help of the dragons at Anyx Trine, the way to Sohm Al's summit stays closed.", "The Trine Towers", "Without their cooperation, she claims, the way to [[Sohm Al]]'s summit will remain closed."),
 "M273b": ("Vidofnir must stay to protect her kin from the Gnath's god.", "The Trine Towers", "I am bound to remain here, and protect my kin from the Gnath's god."),
 "M273c": ("The Gnath act under the influence of a primal.", "The Trine Towers", "Suddenly, the [[beastmen]]'s aggression begins to make sense—they act under the influence of a [[primal]]."),
 "M273d": ("Vidofnir knows Estinien carries Nidhogg's stolen eye.", "The Trine Towers", "when thine own companion beareth Nidhogg's stolen eye!?"),
 "M273e": ("Alphinaud offers to remove the threat in return for Vidofnir's help.", "The Trine Towers", "if we were to eliminate the threat to your territory, would you consent to Lady Ysayle's request?"),
 # #274 Gifts for the Outcasts
 "M274a": ("Ysayle says the Gnath have summoned their god.", "Gifts for the Outcasts", "So, the Gnath have summoned their god... And thus is the mystery of their newfound belligerence laid to rest."),
 "M274b": ("Ysayle insists she called on Saint Shiva for peace, not for her own ends.", "Gifts for the Outcasts", "I did ''not'' reach out to Saint Shiva to further mine own ends!"),
 "M274c": ("Outcast Gnath to the northwest trade with Tailfeather's hunters.", "Gifts for the Outcasts", "From time to time, we barter with a small hive to the north and west of here─outcasts from the main tribe, from what I understand."),
 # #275 The Nonmind
 "M275a": ("The Vath are the Nonmind, outside the Onemind of the Gnath.", "The Nonmind", "You must speak to our chosen leader in words, for we are Vath. We are the Nonmind."),
 "M275b": ("The Overmind heeded black-robed men and summoned the god against the dragons.", "The Nonmind", "Thus did the Overmind decide to heed the words of the black-robed men."),
 "M275c": ("The Gnath mean to make Dravanian lands their own.", "The Nonmind", "Dravanian lands would become Gnath lands, and ever larger would grow our domain."),
 "M275d": ("The god demands more crystals than the war yields.", "The Nonmind", "The price He demands in crystals far exceeds the rewards for this war."),
 # #276 A Gnathic Deity
 "M276a": ("The Overmind binds the senses of every Gnath of the Onemind.", "A Gnathic Deity", "The senses of the Onemind are enmeshed by the Overmind─what one sees, all see; what one feels, all feel."),
 "M276b": ("Captives taken near the colony are brought before the Gnath's god.", "A Gnathic Deity", "Should we allow ourselves to be captured in the environs of the colony, the Gnath will bring us before their deity to make an offering of our souls..."),
 # #277 Breaking into Hives
 "M277a": ("Alphinaud and Estinien stay behind, unprotected from the primal, while you and Ysayle stage an assault.", "Breaking into Hives", "Lacking any protection from the primal's influence, Alphinaud and [[Estinien]] will remain behind while you and Ysayle mount a mock assault upon the hive."),
 # #278 Lord of the Hive
 "M278a": ("Ravana, Master of the Sacred Blades and Wrath of the Colony, comes to claim his sacrifices.", "Lord of the Hive", "Lord [[Ravana]], Master of the Sacred Blades and Wrath of the Colony, arrives to claim his sacrifices."),
 "M278b": ("The Gnath's prayers for the Dravanians' death gave Ravana form.", "Lord of the Hive", "The Gnath would see the Dravanians slain, and their territory secured─and by such fervent prayers am I now given form and purpose."),
 "M278c": ("Ysayle challenges Ravana to withdraw his soldiers from Dravanian soil if she wins.", "Lord of the Hive", "And should we emerge the victors, I would have you swear to withdraw your soldiers from Dravanian soil!"),
 "M278d": ("Ysayle draws on the Gnath's crystals to become Saint Shiva.", "Lord of the Hive", "Ysayle draws upon the energy of the Gnath's hoarded crystals to transform herself into Saint [[Shiva]], and battle is joined."),
 "M278e": ("Ravana, defeated, vows to call his followers back from the dragons' domain.", "Lord of the Hive", "vows to call his followers back from the dragons' domain."),
 "M278f": ("A voice warns that warring gods will shake the world into chaos.", "Lord of the Hive", "At their bidding, warring gods will shake the firmament, and your world will be consumed in the swelling storm of chaos..."),
 # #279 Mourn in Passing
 "M279a": ("Vidofnir opens the way through Mourn to Sohm Al's summit.", "Mourn in Passing", "hie you unto the deepest reaches of Mourn, and there shall you find Halo─the altar from which you may begin your ascent to the summit of Sohm Al."),
 "M279b": ("You defeat Tioman, Nidhogg's consort.", "Mourn in Passing", "You have defeated [[Tioman]], the consort of Nidhogg"),
 "M279c": ("Nidhogg's fury bleeds through the Eye into Estinien.", "Mourn in Passing", "His fury... <gasp> It bleeds through the Eye."),
 "M279d": ("Vidofnir warns Estinien to keep his stolen power in check.", "Mourn in Passing", "have care to keep the stolen power thou wieldest in check, lest it breed further despair."),
 "M279e": ("You reach the summit of Sohm Al.", "Mourn in Passing", "You have arrived at the summit of Sohm Al."),
 # #280 Beyond the Clouds
 "M280a": ("You still must find Hraesvelgr.", "Beyond the Clouds", "Now that we have scaled the mountain, there remains the problem of finding Hraesvelgr himself..."),
 "M280b": ("A moogle on the summit may know where Hraesvelgr lairs.", "Beyond the Clouds", "If the moogle ''does'' live here, however, he may know where Hraesvelgr makes his lair."),
 "M280c": ("The moogle vanishes, perhaps hidden by magic.", "Beyond the Clouds", "Could he be concealing himself with magic...?"),
 # #281 Mountaintop Diplomacy
 "M281a": ("Kan-E-Senna, the Elder Seedseer, joins you as Gridania's ambassador.", "Mountaintop Diplomacy", "If you will have me, I too will accompany you on this venture, and lend my voice to your cause as an ambassador of Gridania."),
 "M281b": ("Estinien watches Nidhogg, who senses the loss of his consort and the coming of the Eye.", "Mountaintop Diplomacy", "Nidhogg senses both the loss of his consort and the coming of the Eye, and his attention is firmly fixed in this direction."),
 "M281c": ("Hraesvelgr is Nidhogg's brood-brother.", "Mountaintop Diplomacy", "I can only identify Nidhogg's with any certainty. We could wander the Mists for days, and not know if we were any closer to his brood-brother..."),
 "M281d": ("Moglin is chieftain of the moogles of the Churning Mists.", "Mountaintop Diplomacy", "I am Moglin, the chieftain of this moogle clan."),
 "M281e": ("The moogles hid because they smelled dragon blood.", "Mountaintop Diplomacy", "We hid because we smelled dragon blood."),
 "M281f": ("Moglin says some dragons, like Hraesvelgr, crave peace, and others, like Nidhogg, the opposite.", "Mountaintop Diplomacy", "While some crave peace, such as Hraesvelgr, many others crave the opposite...such as Nidhogg."),
 "M281g": ("Moglin sets trials to judge you worthy of his help.", "Mountaintop Diplomacy", "It seems that Moglin has devised a number of trials by which he shall judge you worthy of his assistance."),
 # #282 Moghan's Trial / #282b Mogmug's Trial / #282c Mogwin's Trial
 "M282a": ("For Moghan, an alchemist, you gather cloudsbreath for a pom tonic.", "Moghan's Trial", "Oh, yes, these are perfect, kupo! Now I have the main ingredient for my pom tonic."),
 "M282ba": ("For Mogmug you humble the archaeosaurs pursuing him.", "Mogmug's Trial", "You were able to humble my Dravanian devotees? Wonderful!"),
 "M282ca": ("For Mogwin you find his painted pebble on Sohm Al's summit.", "Mogwin's Trial", "You search Sohm Al's summit and find Mogwin's painted pebble."),
 # #285 Moglin's Judgment
 "M285a": ("The trials only kept you busy while the moogles repaired the horn that summons Hraesvelgr.", "Moglin's Judgment", "a means to keep you and your companions occupied while the moogles repaired the horn required to summon [[Hraesvelgr]]."),
 "M285b": ("The horn must be blown at Zenith, the wyrm's dwelling to the west.", "Moglin's Judgment", "Now, you need simply head to Zenith─the wyrm's dwelling to the west─and give the horn a good toot."),
 "M285c": ("Your friendship with a Twelveswood moogle earned the moogles' trust.", "Moglin's Judgment", "You were, after all, already friends with a fellow moogle."),
 # #286 Leaving Moghome
 "M286a": ("Kan-E-Senna warns that a storm of anguish seethes beneath Estinien's calm.", "Leaving Moghome", "Pray attend closely to your companion, Ser Estinien─beneath that stoical facade, a storm of anguish seethes unseen."),
 "M286b": ("You bid farewell to Kan-E-Senna and her moogle companion as they leave.", "Leaving Moghome", "before bidding them both a fond farewell. As the Elder Seedseer turns to leave"),
 # #287 The Road to Zenith
 "M287a": ("Moghan guides you toward Zenith, warning the road will be fought over.", "The Road to Zenith", "but he warns that the road will not be traveled without conflict."),
 "M287b": ("Moghan is unsettled by the dragons' unusual aggression.", "The Road to Zenith", "Though Moghan seems unsettled by the dragons' unusual aggression, your journey to Zenith is all but at an end."),
 # #288 Waiting for the Wind to Change
 "M288a": ("High winds force you to camp and wait.", "Waiting for the Wind to Change", "It would seem you have no choice but to make yourself comfortable, and wait for the weather to turn."),
 "M288b": ("Ysayle vowed to tear down the Holy See and its falsehoods after meeting Hraesvelgr.", "Waiting for the Wind to Change", "I would never have vowed to tear down the Holy See, and expunge the falsehoods with which it fans the flames of conflict."),
 "M288c": ("Alphinaud says his hubris invited the betrayal that brought down the Scions.", "Waiting for the Wind to Change", "That hubris invited manipulation and betrayal...and led to the downfall of the Scions."),
 "M288d": ("Nidhogg killed Estinien's family.", "Waiting for the Wind to Change", "Nidhogg killed my family, and no quirk of history will exonerate him."),
 "M288e": ("Estinien's word holds only if the parley succeeds.", "Waiting for the Wind to Change", "My word is contingent upon the success of our parley."),
 # #289 Heart of Ice
 "M289a": ("Hraesvelgr says the spirit Ysayle summons is only a shade of her own fancy, not Shiva.", "Heart of Ice", "The spirit thou hast summoned belongeth not to Shiva─'tis but a shade conjured by thine own fancy."),
 "M289b": ("King Thordan and his knights ambushed Hraesvelgr's brood-sister Ratatoskr and took what he craved from her.", "Heart of Ice", "With the aid of his leal knights, that most noble of Elezen lured my brood-sister Ratatoskr into an ambush, and took from her that which he craved."),
 "M289c": ("Nidhogg slew Thordan and some of his knights in vengeance.", "Heart of Ice", "But though he slew Thordan and some few of his knights, their fellow butchers knew only too well where to aim their spears"),
 "M289d": ("That, says Hraesvelgr, began the Dragonsong War, and the Holy See hides it.", "Heart of Ice", "Such is the truth the Holy See would keep hidden. Such was the beginning of the Dragonsong War."),
 "M289e": ("Heretics who drink dragon blood become dragons in Nidhogg's army.", "Heart of Ice", "those who abandon their loyalties are rewarded with a drink. And thus are they transformed, to join the ranks of Nidhogg's ever-growing army as newborn dragons."),
 "M289f": ("Alphinaud concludes nothing will deter Nidhogg.", "Heart of Ice", "Nothing will deter Nidhogg from his course."),
 # #290 The Wyrm's Lair
 "M290a": ("Nidhogg's lair, the Aery, lies to the east.", "The Wyrm's Lair", "Nidhogg's lair─the Aery─is said to lie in that direction."),
 "M290b": ("With the parley failed, Estinien means to kill Nidhogg to save Ishgard.", "The Wyrm's Lair", "But your efforts at parley have come to naught, Lady Iceheart. I would see Ishgard saved, and for that, Nidhogg must die."),
 "M290c": ("Ysayle is beyond reach, and Estinien leaves her behind.", "The Wyrm's Lair", "Leave her. Your words will not reach her now."),
 "M290d": ("Nidhogg has walled the Aery behind impenetrable winds.", "The Wyrm's Lair", "You have at last discovered the Aery, but Nidhogg has surrounded his lair with a barrier of impenetrable winds."),
 "M290e": ("Alphinaud proposes calling on Cid.", "The Wyrm's Lair", "Mayhap it is time we called upon Master Garlond."),
 # #291 New Winds, Old Friends
 "M291a": ("Estinien keeps watch on the Aery until you are ready to set out together.", "New Winds, Old Friends", "Contact me by linkpearl when your preparations are complete, and we shall set forth from Ishgard together."),
 "M291b": ("Cid is in Ishgard, working on the Holy See's ill-fated airship.", "New Winds, Old Friends", "the latest gossip surrounding Cid and the Holy See's ill-fated [[airship]]."),
 "M291c": ("The Enterprise is too big to dodge dragons.", "New Winds, Old Friends", "The Dravanians would fly rings around her."),
 "M291d": ("Biggs and Wedge show off a small airship, the manacutter.", "New Winds, Old Friends", "Biggs and [[Wedge]] proudly display their newest invention—a diminutive airship known as a “[[manacutter]].”"),
 "M291e": ("Tataru brings news of the sultana, and Cid sends you to Ul'dah while the manacutter is finished.", "New Winds, Old Friends", "The receptionist has news of the [[Nanamo Ul Namo|sultana]]! Noting the urgency of the situation, Cid bids you concentrate on matters in [[Ul'dah]] while he and his engineers continue work on the manacutter."),
}

# ---- New entities --------------------------------------------------------------------------------------------------
ARC1, ARC2, ARC3, ARC4, ARC5, ARC6 = ("evt-wards-of-house-fortemps", "evt-the-sea-of-clouds", "evt-friends-in-chains",
                                      "evt-hunt-for-lady-iceheart", "evt-road-to-sohm-al", "evt-great-wyrms-answer")
ENTITIES = {
 ARC1: "event", ARC2: "event", ARC3: "event", ARC4: "event", ARC5: "event", ARC6: "event",
 "char-edmont": "character", "char-artoirel": "character", "char-emmanellain": "character", "char-laniaitte": "character",
 "char-aymeric": "character", "char-thordan": "character", "char-grinnaux": "character", "char-zephirin": "character",
 "char-estinien": "character", "char-iceheart": "character", "char-ysayle": "character", "char-midgardsormr": "character",
 "char-hraesvelgr": "character", "char-nidhogg": "character", "char-vidofnir": "character", "char-shiva": "character",
 "char-ravana": "character", "char-bismarck": "character", "char-merlwyb": "character", "char-kan-e-senna": "character",
 "char-nanamo": "character", "char-lolorito": "character", "char-teledji": "character", "char-dewlala": "character",
 "char-moglin": "character",
 "org-holy-see": "organization", "org-heavens-ward": "organization", "org-house-dzemael": "organization",
 "org-dravanian-horde": "organization", "org-vanu-vanu": "organization", "org-gnath": "organization",
 "org-moogles": "organization", "org-doman-refugees": "organization", "org-syndicate": "organization",
 "loc-fortemps-manor": "location", "loc-camp-cloudtop": "location", "loc-sohm-al": "location", "loc-aery": "location",
}

N1, N2, N3, N4, N5, N6 = ("Wards of House Fortemps", "The Sea of Clouds", "Friends in Chains", "The Hunt for Lady Iceheart",
                          "The Road to Sohm Al", "The Great Wyrm's Answer")

# Shared openings, so each step's recap reads on its own.
L1 = ("Branded murderers after the Crystal Braves' betrayal, you, Alphinaud and Tataru have been taken into Ishgard as wards of House Fortemps, "
      "and Count Edmont has set you to help his sons. ")
L1A = L1 + "With his eldest, Artoirel, you are helping reclaim Falcon's Nest in the western highlands for the Holy See. "
L2 = ("You, Alphinaud and Tataru are wards of House Fortemps in Ishgard. With Count Edmont's second son, Emmanellain, you have come to Camp Cloudtop, "
      "the Sea of Clouds outpost that Ser Laniaitte of House Haillenarte commands. ")
L3 = "Alphinaud means to rescue Raubahn, the deposed Flame General, whom the Crystal Braves hold for execution. "
L4 = ("Nidhogg's Dravanian Horde gathers to renew its assault on Ishgard. Rather than run, Alphinaud hopes Lady Iceheart can persuade Nidhogg to stand down, "
      "and Estinien, the Azure Dragoon, has joined you. ")
L5 = "Ysayle, once Lady Iceheart, is guiding you, Alphinaud and Estinien west through Dravania to Sohm Al, to seek an audience with the great wyrm Hraesvelgr. "
L6 = "On Sohm Al's summit you are seeking Hraesvelgr, the great wyrm who may yet talk Nidhogg out of his war on Ishgard. "

PRES = {
 # ---- Arc entries ----
 ARC1: [
   P(S["242"], None, "main", N1,
     "Branded murderers after the Crystal Braves turned on you at the victory banquet, you escaped Ul'dah alone while your comrades stayed behind, and rejoined Alphinaud in Coerthas. "
     "Now Count Edmont has made you, Alphinaud and Tataru wards of House Fortemps, which opens Ishgard's gates. "
     "Haurchefant offers Fortemps Manor as your new headquarters, where any missing allies will be welcome. "
     "Ishgard, ruled by Archbishop Thordan VII, has been at war for a thousand years and keeps its borders closed.",
     ["M242e", "M242f", "M242a", "M242b", "M242g", "M242c", "M242d"]),
   P(S["243"], None, "main", N1,
     "Branded murderers after the Crystal Braves' betrayal, you, Alphinaud and Tataru have been taken into Ishgard as wards of House Fortemps, and Haurchefant has offered Fortemps Manor as your headquarters. "
     "Count Edmont's guide showed you the city, where Archbishop Thordan VII rules from the Holy Vault, "
     "and warned that after decades of closed borders many Ishgardians are wary of foreigners. Alphinaud and Tataru mean to learn more of Ishgard.",
     ["M242e", "M242a", "M242b", "M243b", "M243a", "M243c"]),
   P(S["244"], None, "main", N1,
     "Branded murderers after the Crystal Braves' betrayal, you, Alphinaud and Tataru are wards of House Fortemps, which has taken a great risk in sheltering you. "
     "The lowborn Brume bore the worst of a wyvern attack, and Ser Aymeric's knights are strengthening the defenses. "
     "Count Edmont accepted the Scions' help and set you to aid his sons, Artoirel and Emmanellain, who greeted the offer with indignation and mirth. "
     "Tataru stays at a tavern to gather news of the missing Scions.",
     ["M242e", "M244f", "M244a", "M244b", "M244c", "M244d", "M244e", "M244g"]),
   P(S["245"], None, "main", N1,
     "Branded murderers after the Crystal Braves' betrayal, you, Alphinaud and Tataru are wards of House Fortemps in Ishgard, and Count Edmont has set you to help his sons. "
     "His eldest, Artoirel, sent to aid Houses Durendaire and Dzemael, resents your company as a sign his father doubts him. "
     "He took you to Falcon's Nest, abandoned after the Calamity, which the Holy See has ordered reclaimed and cleared of heretics: "
     "Lady Iceheart and her kind roam there unchecked.",
     ["M242e", "M242a", "M244d", "M245a", "M245b", "M245d", "M245e", "M245f"]),
   P(S["246"], None, "main", N1,
     L1A + "House Dzemael's craftsmen are rebuilding the hamlet, and you cleared out the icicle sprites sabotaging their work. "
     "Lady Iceheart's heretics still roam the highlands.",
     ["M242e", "M242a", "M245a", "M245e", "M246a", "M246b", "M245f"]),
   P(S["247"], None, "main", N1,
     L1A + "House Dzemael's craftsmen are rebuilding the hamlet, and you are lending a hand wherever the work needs it, while Lady Iceheart's heretics still roam the highlands.",
     ["M242e", "M242a", "M245a", "M245e", "M246a", "M245f"]),
   P(S["248"], None, "main", N1,
     L1A + "You have been helping its craftsmen and the people of the outposts nearby; now the hamlet's commander has a sudden task for every able body, you and Artoirel included.",
     ["M242e", "M242a", "M245a", "M245e", "M246a", "M248a", "M248b"]),
   P(S["249"], None, "main", N1,
     L1A + "Scouts sent to find the heretics' hideaway went silent; with Artoirel you saved the sole survivor, "
     "who says heretics ambushed them in a blizzard and the hideaway lies north.",
     ["M242e", "M242a", "M245a", "M245e", "M249a", "M249b", "M249c", "M249d"]),
   P(S["250"], None, "main", N1,
     "Branded murderers, you, Alphinaud and Tataru are wards of House Fortemps, and you are helping Count Edmont's eldest, Artoirel, reclaim Falcon's Nest. "
     "Sent alone along the heretics' trail, you met an old foe, Lady Iceheart, below Gorgagne Mills. "
     "She told you her own Echo showed her the truth of the Dragonsong War through a great wyrm's eyes, and that she was chosen to bring dragon and man together; "
     "she helped the Dravanians breach Ishgard's wards, yet you let her go.",
     ["M242e", "M245a", "M250a", "M250b", "M250d", "M250e", "M250f"]),
   P(S["251"], None, "main", N1,
     "Branded murderers after the Crystal Braves' betrayal, you, Alphinaud and Tataru are wards of House Fortemps. "
     "With Count Edmont's eldest son, Artoirel, you helped reclaim Falcon's Nest and found Lady Iceheart's lair, but let her escape, and the hamlet's commander will praise you both to the Holy See. "
     "Back at the manor, Artoirel admitted he half hoped you would fail, revealed that Haurchefant is his bastard half-brother, and swore never to doubt you again.",
     ["M242e", "M242a", "M245a", "M250b", "M250h", "M251a", "M251d", "M251b"]),
   # The story as of #244, for Emmanellain's chain (a player may do it first); the full story returns at #259.
   P(S["245b"], None, "main", N1,
     "Branded murderers after the Crystal Braves' betrayal, you, Alphinaud and Tataru are wards of House Fortemps, which has taken a great risk in sheltering you. "
     "Count Edmont accepted the Scions' help and set you to aid his sons, Artoirel and Emmanellain, in their duties, while Alphinaud and Tataru seek word of the missing Scions.",
     ["M242e", "M242a", "M244f", "M244d", "M244g"]),
   P(S["259"], None, "main", N1,
     "As wards of House Fortemps, you, Alphinaud and Tataru found refuge in Ishgard. With Count Edmont's eldest son, Artoirel, you helped reclaim Falcon's Nest and found Lady Iceheart's lair, "
     "where she told you the Echo had shown her the truth of the Dragonsong War; you let her escape. Artoirel admitted he had hoped you would fail, revealed that Haurchefant is his bastard half-brother, "
     "and swore never to doubt you again.",
     ["M242a", "M245a", "M250b", "M250d", "M250h", "M251d", "M251b", "M251e"]),
 ],
 ARC2: [
   P(S["245b"], None, "main", N2,
     "You, Alphinaud and Tataru are wards of House Fortemps in Ishgard, and Count Edmont has set you to help his sons. His second son, Emmanellain, who longs to escape his brother's shadow, "
     "took you to Camp Cloudtop in the Sea of Clouds to aid House Haillenarte. Its commander, Ser Laniaitte, is the elder sister of Francel, whom you once saved, and thinks little of Emmanellain. "
     "Her airship, the Protector, is under repair, hampered by clashes with the Vanu Vanu.",
     ["M242a", "M244d", "M245ba", "M245bc", "M245bd", "M245be", "M245bg", "M245bh", "M245bf"]),
   P(S["246b"], None, "main", N2,
     L2 + "To keep Emmanellain out of trouble, she had you set him to watch for Dravanian outflyers. She spares his feelings only for the close ties between her house and his.",
     ["M242a", "M245ba", "M245be", "M246ba", "M246bb"]),
   P(S["247b"], None, "main", N2,
     L2 + "The Vanu Vanu, a beast tribe of the floating isles, were at peace with the camp for half a year, then turned on its foragers for no known reason. "
     "On patrol, you drove several of them off.",
     ["M242a", "M245ba", "M245be", "M247ba", "M247bb", "M247bc"]),
   P(S["248b"], None, "main", N2,
     L2 + "The Vanu Vanu have turned hostile for no known reason, but the camp has never recorded a single Dravanian intrusion and has grown complacent. "
     "You roused its sentries, and Emmanellain now demands a grand mission befitting his station.",
     ["M242a", "M245ba", "M245be", "M247ba", "M248ba", "M248bb"]),
   P(S["249b"], None, "main", N2,
     L2 + "The Vanu Vanu have turned hostile for no known reason. Laniaitte sent you and Emmanellain to the floating lakes for a spring crystal to supply the camp with water; "
     "he ran off to make a contest of it, and has not come back.",
     ["M242a", "M245ba", "M245be", "M247ba", "M249ba", "M249bb"]),
   P(S["250b"], None, "main", N2,
     L2 + "When the Vanu Vanu captured Emmanellain, you freed him with Haurchefant and his knights, but the Vanu surrounded you and their chieftain called forth the primal Bismarck. "
     "Cid, come to inspect the Holy See's airship, swooped in aboard the Enterprise and carried you away.",
     ["M242a", "M245ba", "M245be", "M250ba", "M250bb", "M250bc", "M250bd", "M250be"]),
   P(S["251b"], None, "main", N2,
     "You, Alphinaud and Tataru are wards of House Fortemps in Ishgard. At Camp Cloudtop, Count Edmont's second son, Emmanellain, was captured by the Vanu Vanu, and while you rescued him their chieftain called forth the primal Bismarck. "
     "Ser Laniaitte agrees the primal must lie behind the Vanu's hostility, and praised you for saving Emmanellain from a doom of his own making. "
     "Haurchefant has gone to tell Ser Aymeric, and Count Edmont has scolded his son for his recklessness.",
     ["M242a", "M245ba", "M250ba", "M250bc", "M251ba", "M251bb", "M251bc", "M251bd"]),
 ],
 ARC3: [
   P(S["259"], None, "main", N3,
     "Count Edmont had only begun to thank you for your work at Falcon's Nest and Camp Cloudtop when word came that Ser Grinnaux of the Heavens' Ward, the archbishop's personal guard, had arrested Alphinaud and Tataru for heresy. "
     "The lord commander, Ser Aymeric, believed them innocent but could not overrule the Ward, and Edmont suspects a plot by House Dzemael against House Fortemps. "
     "You won the trial by combat that the law demanded, and your friends went free.",
     ["M259k", "M259a", "M259b", "M259g", "M259f", "M259e", "M259c", "M259i"]),
   P(S["260"], None, "main", N3,
     "Alphinaud and Tataru have been cleared of heresy, and Archbishop Thordan VII apologized for their arrest. In private, he told you the Ascians offered Ishgard power to keep fighting the dragons, "
     "and that he pays them lip service while plotting against them; he asks your help. Then Tataru heard that Raubahn, the deposed Flame General, is to be executed, and Alphinaud resolved to rescue him.",
     ["M259i", "M260a", "M260c", "M260d", "M260e", "M260f"]),
   P(S["261"], None, "main", N3,
     L3 + "In Limsa Lominsa, Merlwyb, still a stout ally, said the Braves have moved him somewhere unknown, but she cannot send troops into Ul'dah without ending the Alliance. "
     "She revealed the sultana meant to abdicate for a republic, and Alphinaud suspects Lolorito and Teledji plotted her death. "
     "The Domans, whom the Braves also turned on, are hunting for Raubahn.",
     ["M260f", "M261b", "M261a", "M261g", "M261d", "M261e", "M261i", "M261j"]),
   P(S["262"], None, "main", N3,
     L3 + "Doman scouts tracked a unit of Braves escorting him from the Rising Stones toward his execution at Halatali, and Ilberd, the traitor, has gone in after them.",
     ["M260f", "M261b", "M262a", "M262b", "M262c"]),
   P(S["263"], None, "main", N3,
     "With Alphinaud and Yugiri you stormed Halatali and rescued Raubahn from the Crystal Braves. Ilberd, defeated, denied killing the sultana and said all he wanted was to free his homeland. "
     "At the Waking Sands, Dewlala of the Syndicate revealed that Nanamo is alive because Lolorito willed it, perhaps held somewhere in an induced slumber, "
     "and she believes Teledji plotted the assassination alone.",
     ["M263a", "M263b", "M263c", "M263h", "M263d", "M263e", "M263f", "M263g"]),
 ],
 ARC4: [
   P(S["264"], None, "main", N4,
     "With Raubahn safe but no proof of Dewlala's claims, you returned to Ishgard to find Nidhogg's Dravanian Horde gathering to renew its assault: trappers saw a cloud of dragons that dimmed the sky. "
     "Count Edmont offered the Scions the chance to seek refuge elsewhere, but Alphinaud is tired of running.",
     ["M264b", "M264c", "M264a", "M264d", "M264e", "M264f", "M264g"]),
   P(S["265"], None, "main", N4,
     "Nidhogg's Dravanian Horde gathers to renew its assault on Ishgard. Alphinaud hopes Lady Iceheart can persuade Nidhogg to stand down, and Estinien, the Azure Dragoon, has joined you, "
     "promising to hold his lance until words fail. Ser Aymeric will hold back the Holy See's knights. In private, Thordan VII told Ser Zephirin they will reward their Ascian allies, "
     "and Zephirin, in a changed voice, swore by the glory of King Thordan.",
     ["M264a", "M265a", "M265b", "M265c", "M265e", "M265f", "M265h"]),
   P(S["266"], None, "main", N4,
     L4 + "You began the search in the western highlands, where you last met her, while Tataru keeps looking for the missing Scions. "
     "Knights picking over her abandoned hideaway at Gorgagne Mills found her followers' letters.",
     ["M264a", "M265a", "M265b", "M266a", "M266b", "M266c"]),
   P(S["267"], None, "main", N4,
     L4 + "Letters from her abandoned hideaway show her followers still use the Akh Afah Amphitheatre as a base.",
     ["M264a", "M265a", "M265b", "M267a"]),
   P(S["268"], None, "main", N4,
     L4 + "At the Akh Afah Amphitheatre her followers refused to parley and attacked, and some had drunk the blood of dragons. She was not there, so Estinien has sent you to the Convictors at Twinpools.",
     ["M264a", "M265a", "M265b", "M268a", "M268b", "M268c", "M268d"]),
   P(S["269"], None, "main", N4,
     L4 + "Her followers proved hostile, and the Convictors knew nothing of her, but a lowborn soldier told you the heretics win conscripts with the promise of freedom, "
     "and answer purple smoke sent up in the highlands.",
     ["M264a", "M265a", "M265b", "M269a", "M269b", "M269c"]),
   P(S["270"], None, "main", N4,
     "As Nidhogg's Dravanian Horde gathers to renew its assault on Ishgard, purple smoke drew Lady Iceheart to you. She told of the maid Shiva, who asked the wyrm Hraesvelgr to consume her so their spirits would be joined, "
     "and how Nidhogg lost an eye to Elezen treachery; Estinien admitted he carries it to draw Nidhogg away. Iceheart agreed to take you to Hraesvelgr instead. "
     "Midgardsormr noted that his mistress's blessing on you has strengthened, and your Crystal of Ice flared.",
     ["M264a", "M269b", "M270b", "M270c", "M270d", "M270e", "M270f", "M270g"]),
 ],
 ARC5: [
   P(S["271"], None, "main", N5,
     "Lady Iceheart has asked you to call her by her true name, Ysayle, as she leads you, Alphinaud and Estinien into Dravania toward Sohm Al, the ancient home of dragonkind, "
     "to seek the great wyrm Hraesvelgr. The road lies far to the west, and the dragons have been murderous of late.",
     ["M271a", "M270e", "M271b", "M271c", "M271d"]),
   P(S["272"], None, "main", N5,
     L5 + "The Gnath, a beast tribe, have turned to unprovoked attacks. Ysayle told how she fled here after the Calamity, her family dead and her home gone. "
     "At ancient ruins she and Estinien quarreled over whether they were built in peace with dragons or by heretics, and Alphinaud says the Echo's visions will settle it.",
     ["M271a", "M270e", "M272a", "M272b", "M272c", "M272d", "M272e"]),
   P(S["273"], None, "main", N5,
     L5 + "The way to Sohm Al's summit stays closed without the dragons of Anyx Trine. Their guardian, Vidofnir, will not leave her post while the Gnath's god threatens her kin, "
     "and she resents that Estinien carries Nidhogg's stolen eye. Alphinaud offered to remove the threat in return for her help.",
     ["M271a", "M270e", "M273a", "M273b", "M273c", "M273d", "M273e"]),
   P(S["274"], None, "main", N5,
     L5 + "To open the way, you must defeat the god the Gnath have summoned. Estinien accused Ysayle of summoning a primal herself; she insists she called on Saint Shiva only for peace. "
     "The hunters of Tailfeather pointed you to an outcast hive that trades with them, and you gathered gifts.",
     ["M271a", "M273b", "M273e", "M274a", "M274b", "M274c"]),
   P(S["275"], None, "main", N5,
     L5 + "The dragon guarding the way will help only if the Gnath's god falls. The outcast Vath, who stand outside the Gnath's Onemind, told how its Overmind heeded black-robed men and summoned the god "
     "to seize Dravanian lands, though its hunger for crystals outweighs what the war yields.",
     ["M271a", "M273e", "M275a", "M275b", "M275c", "M275d"]),
   P(S["276"], None, "main", N5,
     L5 + "The way is barred until the Gnath's god falls. The Overmind binds the senses of every Gnath of the colony, and captives taken there are brought before the god. "
     "Ysayle means to be taken captive with you to reach it.",
     ["M271a", "M273e", "M276a", "M276b"]),
   P(S["277"], None, "main", N5,
     L5 + "The way is barred until the Gnath's god falls. Unprotected from the primal's influence, Alphinaud and Estinien stayed behind while you and Ysayle staged an assault on the Gnath colony, "
     "meaning to be captured and brought before the god.",
     ["M271a", "M273e", "M276b", "M277a"]),
   P(S["278"], None, "main", N5,
     L5 + "Taken captive, you and Ysayle faced the Gnath's god, Ravana. Ysayle challenged him to withdraw his soldiers and became Saint Shiva on the Gnath's crystals, "
     "but he defeated her; you then beat him, and he vowed to call his followers back. A voice warned that warring gods will plunge the world into chaos.",
     ["M271a", "M278a", "M278c", "M278d", "M278e", "M278f"]),
   P(S["279"], None, "main", N5,
     L5 + "With Ravana beaten, Vidofnir opened the way through Mourn. On the climb, Nidhogg's fury bled through the Eye into Estinien, and Vidofnir warned him to keep that stolen power in check. "
     "You defeated Tioman, Nidhogg's consort, and reached the summit.",
     ["M271a", "M278e", "M279a", "M279c", "M279d", "M279b", "M279e"]),
   P(S["280"], None, "main", N5,
     "Ysayle, once Lady Iceheart, led you, Alphinaud and Estinien through Dravania to the summit of Sohm Al. Now you must find the great wyrm Hraesvelgr. "
     "A moogle that might know his lair appeared in the mists and vanished, perhaps hidden by magic.",
     ["M271a", "M279e", "M280a", "M280b", "M280c"]),
 ],
 ARC6: [
   P(S["281"], None, "main", N6,
     L6 + "To reach the moogles of the Churning Mists, you brought the Elder Seedseer, Kan-E-Senna, and a Twelveswood moogle from Gridania, while Estinien watches Nidhogg, "
     "who senses his consort's loss. The moogles' chieftain, Moglin, hid from the smell of dragon blood, says Hraesvelgr craves peace and Nidhogg its opposite, and sets you trials first.",
     ["M280a", "M281a", "M281b", "M281d", "M281e", "M281f", "M281g"]),
   P(S["282"], None, "main", N6,
     L6 + "The moogles' chieftain, Moglin, will help only after his trials. For Moghan, an alchemist, you gathered cloudsbreath for a pom tonic.",
     ["M280a", "M281d", "M281g", "M282a"]),
   P(S["282b"], None, "main", N6,
     L6 + "The moogles' chieftain, Moglin, will help only after his trials. For Mogmug, you taught the archaeosaurs chasing him some manners.",
     ["M280a", "M281d", "M281g", "M282ba"]),
   P(S["282c"], None, "main", N6,
     L6 + "The moogles' chieftain, Moglin, will help only after his trials. For Mogwin, you found his painted pebble on the summit.",
     ["M280a", "M281d", "M281g", "M282ca"]),
   P(S["285"], None, "main", N6,
     L6 + "Moglin's trials only kept you busy while the moogles repaired the horn that summons Hraesvelgr; your friendship with a Twelveswood moogle won their trust. "
     "The horn must be blown at Zenith, the wyrm's palace to the west.",
     ["M280a", "M285a", "M285c", "M285b"]),
   P(S["286"], None, "main", N6,
     L6 + "The moogles gave you the horn that summons him, to be blown at Zenith. Kan-E-Senna took her leave, warning you that a storm of anguish seethes beneath Estinien's calm.",
     ["M280a", "M285a", "M285b", "M286b", "M286a"]),
   P(S["287"], None, "main", N6,
     L6 + "With the moogles' horn, the alchemist Moghan is guiding you to Zenith, Hraesvelgr's palace, through dragons unusually aggressive even for Dravania.",
     ["M280a", "M285b", "M287a", "M287b"]),
   P(S["288"], None, "main", N6,
     L6 + "High winds forced you to camp near Zenith. By the fire, Ysayle told how meeting Hraesvelgr made her vow to tear down the Holy See's falsehoods, Alphinaud blamed his hubris for the Scions' downfall, "
     "and Estinien, whose family Nidhogg killed, said his word holds only if the parley succeeds.",
     ["M280a", "M288a", "M288b", "M288c", "M288d", "M288e"]),
   P(S["289"], None, "main", N6,
     "At Zenith, Hraesvelgr answered the horn, and refused peace. He told Ysayle the spirit she summons is a shade of her own fancy, not Shiva. "
     "He said King Thordan and his knights ambushed his brood-sister Ratatoskr, and that Nidhogg's vengeance began the Dragonsong War, a truth the Holy See hides; "
     "heretics who drink dragon blood now become dragons in Nidhogg's army. Alphinaud believes nothing will stop Nidhogg now.",
     ["M289a", "M289b", "M289c", "M289d", "M289e", "M289f"]),
   P(S["290"], None, "main", N6,
     "Hraesvelgr refused your plea for peace. Estinien now means to kill Nidhogg to save Ishgard, and leaving the shattered Ysayle behind, you followed him east to Nidhogg's lair, the Aery, "
     "which Nidhogg has walled behind impenetrable winds. Alphinaud proposes calling on Cid.",
     ["M289f", "M290b", "M290c", "M290a", "M290d", "M290e"]),
   P(S["291"], None, "main", N6,
     "Hraesvelgr refused peace, and Estinien means to kill Nidhogg in his lair, the Aery, which is walled behind impenetrable winds; he keeps watch until you are ready. "
     "In Ishgard you found Cid working on the Holy See's airship. The Enterprise can't dodge dragons, so Biggs and Wedge are finishing a small one, the manacutter. "
     "Then Tataru arrived with news of the sultana, and Cid sent you to Ul'dah.",
     ["M289f", "M290b", "M290d", "M291a", "M291b", "M291c", "M291d", "M291e"]),
 ],
 # ---- House Fortemps and Ishgard ----
 "char-edmont": [
   P(S["242"], None, "main", "Edmont",
     "Count of House Fortemps, one of Ishgard's High Houses. He has taken you, Alphinaud and Tataru in as wards of his house, opening Ishgard's gates to you, "
     "and knows his decision will raise eyebrows among the other High Houses.",
     ["M242a", "M242i"], ["Count Edmont"]),
   P(S["244"], None, "main", "Edmont",
     "Count of House Fortemps, who has taken you, Alphinaud and Tataru in as wards of his house, a great risk. He accepted the Scions' help in securing provisions from abroad, "
     "and set you to aid his sons, Artoirel and Emmanellain.",
     ["M242a", "M244f", "M244c", "M244d"], ["Count Edmont"]),
   P(S["259"], None, "main", "Edmont",
     "Count of House Fortemps and father of Artoirel, Emmanellain and Haurchefant, who shelters you, Alphinaud and Tataru as wards of his house. "
     "When the Heavens' Ward arrested your friends for heresy, he called it a ploy against his house, and suspects a member of House Dzemael was behind it.",
     ["M242a", "M244d", "M251c", "M259f", "M259e"], ["Count Edmont"]),
   P(S["264"], None, "main", "Edmont",
     "Count of House Fortemps and father of Artoirel, Emmanellain and Haurchefant, who shelters you, Alphinaud and Tataru as wards of his house. "
     "With Nidhogg's minions gathering for war, he offered the Scions the chance to seek refuge outside a besieged Ishgard.",
     ["M242a", "M244d", "M251c", "M264e", "M264f"], ["Count Edmont"]),
 ],
 "char-artoirel": [
   P(S["244"], None, "main", "Artoirel",
     "A son of Count Edmont of House Fortemps. He greeted the Scions' offer of help with indignation, but his father has set you to aid him in his duties.",
     ["M244d", "M244e"], ["Lord Artoirel"]),
   P(S["245"], None, "main", "Artoirel",
     "Count Edmont's eldest son, a knight of House Fortemps, sent to aid Houses Durendaire and Dzemael in reclaiming Falcon's Nest for the Holy See. "
     "He takes your company as a sign his father doubts him, but means to respect his father's wishes.",
     ["M245a", "M245b", "M245e", "M245g"], ["Lord Artoirel"]),
   P(S["249"], None, "main", "Artoirel",
     "Count Edmont's eldest son, a knight of House Fortemps helping to reclaim Falcon's Nest. With you he saved the sole survivor of a reconnaissance party ambushed by heretics.",
     ["M245a", "M249a", "M249d"], ["Lord Artoirel"]),
   P(S["250"], None, "main", "Artoirel",
     "Count Edmont's eldest son, a knight of House Fortemps helping to reclaim Falcon's Nest. He sent you alone along the heretics' trail, to the lair where you met Lady Iceheart.",
     ["M245a", "M250a", "M250b"], ["Lord Artoirel"]),
   P(S["251"], None, "main", "Artoirel",
     "Count Edmont's eldest son, a knight of House Fortemps. After you reclaimed Falcon's Nest together, he admitted he had half hoped you would fail, "
     "partly because his bastard half-brother, Haurchefant, holds you in such esteem. He has sworn never to doubt you again.",
     ["M245a", "M251a", "M251d", "M251b", "M251e"], ["Lord Artoirel"]),
   # As of #244 for Emmanellain's chain; Artoirel's own chain returns at #259.
   P(S["245b"], None, "main", "Artoirel",
     "Count Edmont's elder son, of House Fortemps. He greeted the Scions' offer of help with indignation, but his father has set you to aid him in his duties.",
     ["M244d", "M244e", "M245ba"], ["Lord Artoirel"]),
   P(S["259"], None, "main", "Artoirel",
     "Count Edmont's eldest son, a knight of House Fortemps. With you he helped reclaim Falcon's Nest, admitting afterward that he had half hoped you would fail; "
     "his bastard half-brother, Haurchefant, holds you in high esteem. He has sworn never to doubt you again.",
     ["M245a", "M251d", "M251b", "M251e"], ["Lord Artoirel"]),
 ],
 "char-emmanellain": [
   P(S["244"], None, "main", "Emmanellain",
     "A son of Count Edmont of House Fortemps. He greeted the Scions' offer of help with mirth, but his father has set you to aid him in his duties.",
     ["M244d", "M244e"], ["Lord Emmanellain"]),
   P(S["245b"], None, "main", "Emmanellain",
     "Count Edmont's second son, of House Fortemps, who resents that the eldest inherits all and longs to outshine his brother, Artoirel. "
     "He brought you to Camp Cloudtop to aid House Haillenarte, where its commander, Ser Laniaitte, thinks little of him.",
     ["M245ba", "M245bi", "M245bb", "M245bc", "M245bh"], ["Lord Emmanellain"]),
   P(S["248b"], None, "main", "Emmanellain",
     "Count Edmont's second son, who longs to outshine his elder brother. At Camp Cloudtop, Ser Laniaitte set him to harmless watch duty to keep him out of trouble, "
     "but he demands a grand mission befitting his station.",
     ["M245ba", "M246ba", "M248bb"], ["Lord Emmanellain"]),
   P(S["249b"], None, "main", "Emmanellain",
     "Count Edmont's second son, who longs to outshine his elder brother. Sent with you to fetch a spring crystal for Camp Cloudtop, he ran off to make a contest of it, and has not come back.",
     ["M245ba", "M249ba", "M249bb"], ["Lord Emmanellain"]),
   P(S["250b"], None, "main", "Emmanellain",
     "Count Edmont's second son, who longs to outshine his elder brother. The Vanu Vanu captured him near Camp Cloudtop; you and Haurchefant freed him, and Cid carried you all away from the primal Bismarck.",
     ["M245ba", "M250ba", "M250bb", "M250bd"], ["Lord Emmanellain"]),
   P(S["251b"], None, "main", "Emmanellain",
     "Count Edmont's second son, who longs to outshine his elder brother. Captured by the Vanu Vanu and rescued by you, he claims credit for uncovering their primal, "
     "but Ser Laniaitte credits you, and his father has scolded him for his recklessness.",
     ["M245ba", "M250ba", "M251ba", "M251bb", "M251bd"], ["Lord Emmanellain"]),
 ],
 "char-haurchefant": [
   P(S["242"], None, "main", "Haurchefant",
     "A lord of House Fortemps who commands the garrison at Camp Dragonhead. After the Scions were branded murderers, he had you, Alphinaud and Tataru made wards of his house so you could enter Ishgard, "
     "and offers its manor, his family home, as your headquarters.",
     ["E116c", "M242e", "M242a", "M242h", "M242b"]),
   P(S["250b"], None, "main", "Haurchefant",
     "A lord of House Fortemps who had you, Alphinaud and Tataru made wards of his house. He arrived with knights to help you free Emmanellain from the Vanu Vanu, "
     "and was first to see that the Vanu's whale, Bismarck, is a primal.",
     ["M242a", "M250bb", "M250bc"]),
   P(S["251b"], None, "main", "Haurchefant",
     "A lord of House Fortemps who had you, Alphinaud and Tataru made wards of his house. He helped you free Emmanellain from the Vanu Vanu, and has gone to report their primal, Bismarck, to Ser Aymeric.",
     ["M242a", "M250bb", "M250bc", "M251bc"]),
   P(S["259"], None, "main", "Haurchefant",
     "A lord of House Fortemps, Count Edmont's son and Artoirel's bastard half-brother, who had you, Alphinaud and Tataru made wards of his house. "
     "He helped you rescue Emmanellain from the Vanu Vanu, and after you won the trial by combat that freed Alphinaud and Tataru, he gave you a black chocobo that can fly.",
     ["M242a", "M251b", "M251c", "M250bb", "M259i", "M259j"]),
 ],
 "loc-fortemps-manor": [
   P(S["242"], None, "main", "Fortemps Manor",
     "The family home of House Fortemps in Ishgard's Pillars. Haurchefant has offered it to you, Alphinaud and Tataru as your new headquarters, and any missing allies who are found will be welcome there.",
     ["M242h", "M242b", "M242g"]),
 ],
 "char-thordan": [
   P(S["242"], None, "main", "Thordan VII",
     "Archbishop of the Ishgardian Orthodox Church, who rules Ishgard, a nation devoted to the goddess Halone.",
     ["M242c"], ["Archbishop Thordan VII"]),
   P(S["243"], None, "main", "Thordan VII",
     "Archbishop of the Ishgardian Orthodox Church, who rules Ishgard, a nation devoted to the goddess Halone, from his seat in the Holy Vault.",
     ["M242c", "M243b"], ["Archbishop Thordan VII"]),
   P(S["260"], None, "main", "Thordan VII",
     "Archbishop of the Ishgardian Orthodox Church, who rules Ishgard from the Holy Vault. He apologized for your friends' wrongful arrest, then told you in private that the Ascians offered Ishgard power "
     "to keep fighting the dragons, and that he pays them lip service while plotting against them. He asks your help.",
     ["M242c", "M260a", "M260c", "M260d"], ["Archbishop Thordan VII"]),
   P(S["265"], None, "main", "Thordan VII",
     "Archbishop of the Ishgardian Orthodox Church, who rules Ishgard from the Holy Vault. He told you he pays the Ascians lip service while plotting against them, "
     "yet in private he told Ser Zephirin that once the dragons are gone they will reward their Ascian allies.",
     ["M242c", "M260d", "M265f"], ["Archbishop Thordan VII"]),
 ],
 "org-holy-see": [
   P(S["245"], None, "main", "The Holy See",
     "Ishgard's ruling authority, under Archbishop Thordan VII. It wants the High Houses to set aside their rivalries, and has ordered the western highlands reclaimed and their heretics expelled.",
     ["M242c", "M245c", "M245e"]),
   P(S["264"], None, "main", "The Holy See",
     "Ishgard's ruling authority, under Archbishop Thordan VII, whose personal guard is the Heavens' Ward. It has asked the Ironworks for help with its airship, the Protector, "
     "and now readies for battle as Nidhogg's Dravanian Horde gathers.",
     ["M242c", "M259b", "M250be", "M264a"]),
   P(S["289"], None, "main", "The Holy See",
     "Ishgard's ruling authority, under Archbishop Thordan VII. Hraesvelgr says it hides how the Dragonsong War began: King Thordan and his knights ambushed the dragon Ratatoskr, and Nidhogg took vengeance.",
     ["M242c", "M289b", "M289c", "M289d"]),
 ],
 "char-aymeric": [
   P(S["244"], None, "main", "Aymeric",
     "An Ishgardian knight whose knights are strengthening the city's defenses after a wyvern attack, with each High House asked to help.",
     ["M244b"], ["Ser Aymeric"]),
   P(S["259"], None, "main", "Aymeric",
     "The lord commander of Ishgard's knights, who sit at the Congregation. He believed Alphinaud and Tataru innocent of heresy, but could not overrule the Heavens' Ward.",
     ["M259h", "M259g", "M251bc"], ["Ser Aymeric"]),
   P(S["265"], None, "main", "Aymeric",
     "The lord commander of Ishgard's knights. He believed Alphinaud and Tataru innocent of heresy, and will support any effort that could spare his countrymen's blood, holding back the Holy See while you seek peace.",
     ["M259h", "M259g", "M265e"], ["Ser Aymeric"]),
 ],
 "org-heavens-ward": [
   P(S["259"], None, "main", "The Heavens' Ward",
     "The personal guard of Archbishop Thordan VII: twelve chosen knights who answer only to him, and whose testimony cannot be challenged. "
     "One of them, Ser Grinnaux, had Alphinaud and Tataru arrested for heresy, and you defeated him in a trial by combat.",
     ["M259b", "M259a", "M259i"]),
   P(S["260"], None, "main", "The Heavens' Ward",
     "The personal guard of Archbishop Thordan VII: twelve chosen knights who answer only to him. Ser Zephirin admitted they acted on false information when Ser Grinnaux had Alphinaud and Tataru arrested.",
     ["M259b", "M259a", "M260b"]),
 ],
 "char-grinnaux": [
   P(S["259"], None, "main", "Grinnaux",
     "A knight of the Heavens' Ward and a son of House Dzemael. He had Alphinaud and Tataru arrested for heresy, and you defeated him in the trial by combat that freed them. "
     "Count Edmont suspects another member of his house was manipulating him.",
     ["M259a", "M259d", "M259i", "M259e"], ["Ser Grinnaux"]),
 ],
 "org-house-dzemael": [
   P(S["245"], None, "main", "House Dzemael",
     "One of Ishgard's High Houses, long a rival of the other noble families. Its craftsmen work to reclaim Falcon's Nest in the western highlands.",
     ["M245a"]),
   P(S["259"], None, "main", "House Dzemael",
     "One of Ishgard's High Houses. Ser Grinnaux, the knight who had Alphinaud and Tataru arrested for heresy, is one of its sons, and Count Edmont suspects another of its members was manipulating him.",
     ["M245a", "M259d", "M259e"]),
 ],
 "char-zephirin": [
   P(S["260"], None, "main", "Zephirin",
     "A knight of the Heavens' Ward, the archbishop's personal guard. He admitted the Ward acted on false information when Alphinaud and Tataru were arrested, and apologized.",
     ["M260b"], ["Ser Zephirin"]),
   P(S["265"], None, "main", "Zephirin",
     "A knight of the Heavens' Ward. In private, Archbishop Thordan VII told him they will reward their Ascian allies; Zephirin worried that the Paragons might see through their deception, "
     "then, in a changed voice, swore by the glory of King Thordan.",
     ["M260b", "M265f", "M265g", "M265h"], ["Ser Zephirin"]),
 ],
 # ---- Camp Cloudtop ----
 "char-laniaitte": [
   P(S["245b"], None, "main", "Laniaitte",
     "A knight of House Haillenarte who commands Camp Cloudtop in the Sea of Clouds. She is the elder sister of Francel, whom you once saved from an unjust execution, and thinks little of Emmanellain.",
     ["M245be", "M245bg", "M245bh"], ["Ser Laniaitte"]),
   P(S["246b"], None, "main", "Laniaitte",
     "A knight of House Haillenarte who commands Camp Cloudtop, and the elder sister of Francel, whom you once saved. She keeps Emmanellain out of trouble, sparing his feelings only for the close ties between their houses.",
     ["M245be", "M245bg", "M246ba", "M246bb"], ["Ser Laniaitte"]),
   P(S["251b"], None, "main", "Laniaitte",
     "A knight of House Haillenarte who commands Camp Cloudtop, and the elder sister of Francel, whom you once saved. She agrees the Vanu Vanu's primal must lie behind their hostility, "
     "and praised you for rescuing Emmanellain from a doom of his own making.",
     ["M245be", "M245bg", "M251ba", "M251bb"], ["Ser Laniaitte"]),
 ],
 "loc-camp-cloudtop": [
   P(S["245b"], None, "main", "Camp Cloudtop",
     "An Ishgardian outpost in the Sea of Clouds, built to warn of Dravanian incursions and commanded by Ser Laniaitte of House Haillenarte. Its great airship, the Protector, is under repair, "
     "hampered by clashes with the Vanu Vanu.",
     ["M245bd", "M245be", "M245bf"]),
   P(S["248b"], None, "main", "Camp Cloudtop",
     "An Ishgardian outpost in the Sea of Clouds, built to warn of Dravanian incursions, but it has never recorded one and has grown complacent. The Vanu Vanu now attack its foragers, "
     "so it relies more on supplies flown in from Ishgard.",
     ["M245bd", "M248ba", "M247bb"]),
 ],
 "char-francel": [
   P(S["245b"], None, "main", "Francel",
     "A lord of House Haillenarte whom you saved from an unjust execution when he was tried for heresy. His elder sister, Ser Laniaitte, commands Camp Cloudtop and is grateful to you.",
     ["E120d", "M245bg"]),
 ],
 "org-house-haillenarte": [
   P(S["245b"], None, "main", "House Haillenarte",
     "One of Ishgard's High Houses, once accused of harboring heretics; its Lord Francel was cleared at his trial. Its knights hold Camp Cloudtop in the Sea of Clouds under Ser Laniaitte, "
     "and House Fortemps has sent Emmanellain to aid them.",
     ["E115b", "E120d", "M245be", "M245bc"]),
   P(S["246b"], None, "main", "House Haillenarte",
     "One of Ishgard's High Houses, once accused of harboring heretics; its Lord Francel was cleared at his trial. Its knights hold Camp Cloudtop under Ser Laniaitte, and it has close ties to House Fortemps.",
     ["E115b", "E120d", "M245be", "M246bb"]),
 ],
 "org-vanu-vanu": [
   P(S["245b"], None, "main", "The Vanu Vanu",
     "A beast tribe of the Sea of Clouds whose skirmishes with Camp Cloudtop have hampered repairs to its airship.",
     ["M245bf"]),
   P(S["247b"], None, "main", "The Vanu Vanu",
     "A beast tribe of the floating isles of the Sea of Clouds. After half a year of peace with Camp Cloudtop, they turned on its foragers for no known reason.",
     ["M245bf", "M247ba", "M247bb"]),
   P(S["250b"], None, "main", "The Vanu Vanu",
     "A beast tribe of the floating isles that turned on Camp Cloudtop. They captured Emmanellain, and their chieftain called forth Bismarck, Lord of the Mists, a primal.",
     ["M247ba", "M250ba", "M250bc"]),
   P(S["251b"], None, "main", "The Vanu Vanu",
     "A beast tribe of the floating isles that has summoned a primal, Bismarck, which Camp Cloudtop believes lies behind the tribe's sudden hostility.",
     ["M250bc", "M251ba"]),
 ],
 "char-bismarck": [
   P(S["250b"], None, "main", "Bismarck",
     "A primal summoned by the Vanu Vanu: a gargantuan flying whale that their chieftain named Lord of the Mists. Cid carried you away before it could swallow you.",
     ["M250bc", "M250bd"], ["Lord of the Mists"]),
   P(S["251b"], None, "main", "Bismarck",
     "A primal summoned by the Vanu Vanu: a gargantuan flying whale, Lord of the Mists. Camp Cloudtop believes it lies behind the Vanu's sudden hostility.",
     ["M250bc", "M251ba"], ["Lord of the Mists"]),
 ],
 # ---- The Scions and their allies ----
 "org-scions": [
   P(S["242"], None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future. Betrayed by the Crystal Braves, its members were condemned as murderers and scattered; you alone escaped Ul'dah to rejoin Alphinaud. "
     "Now you, Alphinaud and Tataru are wards of House Fortemps in Ishgard, with Fortemps Manor as your headquarters.",
     ["C34", "M242e", "M242f", "M242a", "M242b"]),
   P(S["244"], None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, condemned as murderers after the Crystal Braves betrayed it. The few left, you, Alphinaud and Tataru, are wards of House Fortemps in Ishgard, "
     "and serve the city to repay that risk while seeking word of the missing Scions.",
     ["C34", "M242e", "M242a", "M244f", "M244g"]),
   P(S["264"], None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, condemned as murderers after the Crystal Braves betrayed it. From their refuge with House Fortemps in Ishgard, Alphinaud and Tataru were cleared of heresy, "
     "and you rescued Raubahn. With Nidhogg's Horde gathering, Count Edmont offered them refuge elsewhere, but Alphinaud is tired of running.",
     ["C34", "M242e", "M242a", "M259i", "M263a", "M264f", "M264g"]),
   P(S["288"], None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, condemned as murderers after the Crystal Braves betrayed it, with most of its members still missing. Alphinaud blames his own hubris for the downfall. "
     "From Ishgard, its few remaining members are seeking peace with the dragons, while Tataru keeps searching for the rest.",
     ["C34", "M242e", "M266b", "M288c", "M265a"]),
 ],
 "char-alphinaud": [
   P(S["242"], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who founded the Crystal Braves, only for them to betray the Scions. Branded a murderer, he took refuge in Coerthas, "
     "and he, you and Tataru are now wards of House Fortemps in Ishgard.",
     ["C10", "C48", "M242e", "M242a"]),
   P(S["244"], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who founded the Crystal Braves, only for them to betray the Scions. A ward of House Fortemps in Ishgard, he offered the Scions' help to Count Edmont, "
     "hoping their work will also bring word of the missing Scions.",
     ["C10", "C48", "M242a", "M244c", "M244f"]),
   P(S["260"], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, sheltered by House Fortemps in Ishgard. Arrested for heresy by the Heavens' Ward, he was freed when you won his trial by combat. "
     "He is shocked that the Ascians' influence reaches Ishgard, and has resolved to rescue Raubahn from execution.",
     ["C10", "M242a", "M259a", "M259i", "M260e", "M260f"]),
   P(S["263"], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, sheltered by House Fortemps in Ishgard. Taking responsibility for the Crystal Braves he founded, he helped you and Yugiri rescue Raubahn from them at Halatali.",
     ["C10", "M242a", "M261h", "M263a"]),
   P(S["265"], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, sheltered by House Fortemps. Tired of running, he hopes to end the dragons' war on Ishgard by peace: Lady Iceheart might persuade Nidhogg to stand down, "
     "and Estinien has joined you on condition that he holds his lance until words fail.",
     ["C10", "M242a", "M264g", "M265a", "M265c"]),
   P(S["288"], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother. He blames his own hubris, which invited manipulation and betrayal, for the Scions' downfall. "
     "He has led you, Ysayle and Estinien through Dravania to seek peace from the great wyrm Hraesvelgr.",
     ["C10", "M288c", "M271a", "M280a"]),
   P(S["290"], None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother, who blames his own hubris for the Scions' downfall. His mission of peace failed when Hraesvelgr refused it, and he believes nothing will deter Nidhogg now. "
     "He has turned to Cid to breach the winds around Nidhogg's lair.",
     ["C10", "M288c", "M289f", "M290d", "M290e"]),
 ],
 "char-tataru": [
   P(S["242"], None, "main", "Tataru",
     "The Scions' receptionist. Branded a fugitive with the others, she is now, with you and Alphinaud, a ward of House Fortemps in Ishgard.",
     ["C15", "M242e", "M242a"]),
   P(S["244"], None, "main", "Tataru",
     "The Scions' receptionist, and with you and Alphinaud a ward of House Fortemps in Ishgard. She is gathering news at a local tavern, perhaps of the missing Scions.",
     ["C15", "M242a", "M244g"]),
   P(S["259"], None, "main", "Tataru",
     "The Scions' receptionist, a ward of House Fortemps in Ishgard. Arrested with Alphinaud for heresy by the Heavens' Ward, she named you her champion, and your victory set them free.",
     ["C15", "M242a", "M259a", "M259i"]),
   P(S["266"], None, "main", "Tataru",
     "The Scions' receptionist, a ward of House Fortemps in Ishgard. Once freed from a heresy charge, she brought word that Raubahn was to be executed, and she keeps searching for the missing Scions.",
     ["C15", "M259i", "M260f", "M266b"]),
   P(S["291"], None, "main", "Tataru",
     "The Scions' receptionist, a ward of House Fortemps in Ishgard, who keeps searching for the missing Scions. She has brought urgent news of the sultana from Ul'dah.",
     ["C15", "M242a", "M266b", "M291e"]),
 ],
 # ---- Ul'dah and the rescue of Raubahn ----
 "char-merlwyb": [
   P(S["261"], None, "main", "Merlwyb",
     "Admiral of Limsa Lominsa and a stout ally of the Scions. With the Elder Seedseer she made the Syndicate keep the Scions' alleged crimes quiet until proof is found. "
     "She helps Alphinaud seek Raubahn, but cannot send troops into Ul'dah without ending the Alliance.",
     ["M261a", "M261c", "M261b", "M261g"]),
 ],
 "char-kan-e-senna": [
   P(S["261"], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania. With Merlwyb she made the Syndicate keep the Scions' alleged crimes quiet until proof is found.",
     ["M261c"], ["the Elder Seedseer"]),
   P(S["281"], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania, who kept the Scions' alleged crimes quiet. She has joined your journey to the moogles of the Churning Mists as Gridania's ambassador.",
     ["M261c", "M281a"], ["the Elder Seedseer"]),
   P(S["286"], None, "main", "Kan-E-Senna",
     "The Elder Seedseer of Gridania, who kept the Scions' alleged crimes quiet. She helped you reach the moogles of the Churning Mists as Gridania's ambassador, "
     "and as she took her leave she warned you of the anguish hidden beneath Estinien's calm.",
     ["M261c", "M281a", "M286b", "M286a"], ["the Elder Seedseer"]),
 ],
 "char-nanamo": [
   P(S["261"], None, "main", "Nanamo",
     "The sultana of Ul'dah, whose death the Scions were accused of plotting. Merlwyb says she meant to abdicate and make way for a republic; Ul'dah says only that she is convalescing from illness.",
     ["M261d", "M261f", "M261e"]),
   P(S["263"], None, "main", "Nanamo",
     "The sultana of Ul'dah, who meant to abdicate for a republic. Dewlala confirms she is still alive, perhaps held somewhere in an induced slumber, and says she lives because Lolorito willed it.",
     ["M261d", "M263e", "M263f"]),
   P(S["291"], None, "main", "Nanamo",
     "The sultana of Ul'dah, who meant to abdicate for a republic. Dewlala believes she is alive and held in an induced slumber, and now Tataru has brought urgent news of her.",
     ["M261d", "M263e", "M291e"]),
 ],
 "char-lolorito": [
   P(S["261"], None, "main", "Lolorito",
     "A powerful man of Ul'dah. Alphinaud suspects he and Teledji plotted the sultana's assassination to keep the sultanate as it is.",
     ["M261e"]),
   P(S["263"], None, "main", "Lolorito",
     "A powerful man of Ul'dah. Dewlala says the sultana lives because he willed it, and believes he learned of Teledji's plot against her and exploited it.",
     ["M261e", "M263f", "M263g"]),
 ],
 "char-teledji": [
   P(S["261"], None, "main", "Teledji",
     "A powerful man of Ul'dah. Alphinaud suspects he and Lolorito plotted the sultana's assassination to keep the sultanate as it is.",
     ["M261e"]),
   P(S["263"], None, "main", "Teledji",
     "A powerful man of Ul'dah. Dewlala believes he plotted the sultana's assassination alone, and that Lolorito exploited it.",
     ["M261e", "M263g"]),
 ],
 "org-syndicate": [
   P(S["261"], None, "main", "The Syndicate",
     "Ul'dah's ruling council. At Merlwyb's and the Elder Seedseer's demand, it has kept the Scions' alleged crimes quiet until proof is found.",
     ["M261c"]),
   P(S["263"], None, "main", "The Syndicate",
     "Ul'dah's ruling council, which has kept the Scions' alleged crimes quiet. One of its members, Dewlala, says the sultana lives and that Lolorito exploited Teledji's plot against her.",
     ["M261c", "M263d", "M263e", "M263g"]),
 ],
 "char-dewlala": [
   P(S["263"], None, "main", "Dewlala",
     "Head of the Order of Nald'thal and a member of Ul'dah's Syndicate. At the Waking Sands she revealed that Nanamo is alive because Lolorito willed it, and believes Teledji plotted the assassination alone.",
     ["M263d", "M263e", "M263f", "M263g"]),
 ],
 "org-doman-refugees": [
   P(S["261"], None, "main", "The Doman refugees",
     "Refugees from Doma. The Crystal Braves turned on them too at the victory feast and took the Rising Stones by force. Their shinobi are hunting for Raubahn.",
     ["M261i", "M261j"]),
   P(S["263"], None, "main", "The Doman refugees",
     "Refugees from Doma whom the Crystal Braves turned on at the victory feast. Their scouts tracked Raubahn to Halatali, and Yugiri helped you rescue him.",
     ["M261i", "M262b", "M263a"]),
 ],
 "org-crystal-braves": [
   P(S["261"], None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, which turned on the Scions and the Domans at the victory feast and took the Rising Stones by force. "
     "They have moved the deposed Flame General, Raubahn, somewhere unknown ahead of his execution.",
     ["C48", "M261i", "M261b", "M261h"]),
   P(S["263"], None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, which turned on the Scions and the Domans and took the Rising Stones. You rescued Raubahn from them at Halatali, "
     "where Ilberd denied killing the sultana and said all he wanted was to free his homeland.",
     ["C48", "M261i", "M263a", "M263b", "M263c"]),
 ],
 # ---- The dragons and the heretics ----
 "char-iceheart": [
   P(S["245"], None, "main", "Iceheart",
     "A heretic leader. The Holy See has ordered the western highlands reclaimed and their heretics expelled; Lady Iceheart and her kind have roamed those lands ever since they were abandoned after the Calamity.",
     ["M245e", "M245f", "M245d"], ["Lady Iceheart"]),
   P(S["259"], None, "main", "Iceheart",
     "A heretic leader, an old foe of yours. In her lair below Gorgagne Mills she told you she too has the Echo, which showed her the truth of the Dragonsong War through a great wyrm's eyes, "
     "and that she was chosen to bring dragon and man together. She helped the Dravanians breach Ishgard's wards, but swore to break the cycle of bloodshed, and you let her escape.",
     ["M250b", "M250d", "M250e", "M250f", "M250g", "M250h"], ["Lady Iceheart"]),
   P(S["265"], None, "main", "Iceheart",
     "A heretic leader with the Echo, who swore to bring dragon and man together and end the bloodshed. Alphinaud hopes she will persuade Nidhogg to call off his assault on Ishgard.",
     ["M250d", "M250g", "M265a"], ["Lady Iceheart"]),
   P(S["269"], None, "main", "Iceheart",
     "A heretic leader with the Echo, who swore to bring dragon and man together. Alphinaud is searching for her, hoping she will persuade Nidhogg to call off his assault on Ishgard. "
     "Her followers, some of whom drink dragon blood, win lowborn conscripts with the promise of freedom.",
     ["M250d", "M265a", "M266a", "M268b", "M269a", "M269c"], ["Lady Iceheart"]),
   P(S["270"], None, "main", "Iceheart",
     "A heretic leader with the Echo. Drawn by purple smoke, she told you of the maid Shiva and the wyrm Hraesvelgr, and how Nidhogg lost an eye to Elezen treachery. "
     "She has agreed to take you to Hraesvelgr to seek peace.",
     ["M250d", "M269b", "M270b", "M270c", "M270e"], ["Lady Iceheart"]),
   P(S["271"], None, "main", "Iceheart",
     "The name the heretic leader went by until she asked you to call her by her true name, Ysayle.",
     ["M245f", "M271a"], ["Lady Iceheart"]),
 ],
 "char-ysayle": [
   P(S["271"], None, "main", "Ysayle",
     "The true name of Lady Iceheart, the heretic leader with the Echo who swore to bring dragon and man together. She is guiding you, Alphinaud and Estinien through Dravania to Sohm Al, "
     "to seek peace from the great wyrm Hraesvelgr.",
     ["M271a", "M250d", "M250e", "M270e", "M271c"], ["Iceheart", "Lady Iceheart"]),
   P(S["272"], None, "main", "Ysayle",
     "The true name of Lady Iceheart, a heretic leader with the Echo. After the Calamity, with her family dead and her home gone, she fled into Dravania. "
     "She is guiding you to Sohm Al to seek peace from Hraesvelgr, and quarrels with Estinien over the true history of man and dragon.",
     ["M271a", "M272b", "M270e", "M272c", "M272d"], ["Iceheart", "Lady Iceheart"]),
   P(S["274"], None, "main", "Ysayle",
     "The true name of Lady Iceheart, a heretic leader with the Echo, guiding you to Sohm Al to seek peace from Hraesvelgr. Estinien accuses her of summoning a primal for her own ends; "
     "she insists she called on Saint Shiva only for peace.",
     ["M271a", "M270e", "M274b"], ["Iceheart", "Lady Iceheart"]),
   P(S["278"], None, "main", "Ysayle",
     "The true name of Lady Iceheart, a heretic leader with the Echo, guiding you to Sohm Al to seek peace from Hraesvelgr. Brought before Ravana, she challenged him and, drawing on the Gnath's crystals, "
     "became Saint Shiva, but he defeated her before you won the fight.",
     ["M271a", "M270e", "M278c", "M278d", "M278e"], ["Iceheart", "Lady Iceheart"]),
   P(S["288"], None, "main", "Ysayle",
     "The true name of Lady Iceheart, a heretic leader with the Echo who calls on Saint Shiva. Meeting Hraesvelgr made her vow to tear down the Holy See and its falsehoods, "
     "and now she has come with you to the edge of his palace, Zenith, to plead for peace.",
     ["M271a", "M278d", "M288b", "M285b", "M288a"], ["Iceheart", "Lady Iceheart"]),
   P(S["289"], None, "main", "Ysayle",
     "The true name of Lady Iceheart, a heretic leader with the Echo who called on Saint Shiva for peace. Hraesvelgr told her the spirit she summons is only a shade of her own fancy, "
     "and refused her plea for peace.",
     ["M271a", "M274b", "M289a", "M289f"], ["Iceheart", "Lady Iceheart"]),
   P(S["290"], None, "main", "Ysayle",
     "The true name of Lady Iceheart, a heretic leader with the Echo who called on Saint Shiva for peace. When Hraesvelgr rejected her and her plea, she was left shattered, "
     "and Estinien left her behind as he set out to kill Nidhogg.",
     ["M271a", "M274b", "M289a", "M290c"], ["Iceheart", "Lady Iceheart"]),
 ],
 "char-shiva": [
   P(S["270"], None, "main", "Shiva",
     "In Lady Iceheart's tale, a maid who loved the wyrm Hraesvelgr and asked him to consume her, so that their spirits would be joined for eternity.",
     ["M270b"], ["Saint Shiva"]),
   P(S["274"], None, "main", "Shiva",
     "In Ysayle's tale, a maid who loved the wyrm Hraesvelgr and asked him to consume her, so their spirits would be joined. Ysayle calls on Saint Shiva, she insists, only for peace.",
     ["M270b", "M274b"], ["Saint Shiva"]),
   P(S["278"], None, "main", "Shiva",
     "A maid of legend who asked the wyrm Hraesvelgr to consume her. Ysayle calls on her as Saint Shiva, and drew on the Gnath's crystals to become her in battle against Ravana.",
     ["M270b", "M274b", "M278d"], ["Saint Shiva"]),
   P(S["289"], None, "main", "Shiva",
     "A maid of legend who asked the wyrm Hraesvelgr to consume her. Ysayle calls on her as Saint Shiva, but Hraesvelgr says the spirit Ysayle summons is not Shiva, only a shade of her own fancy.",
     ["M270b", "M278d", "M289a"], ["Saint Shiva"]),
 ],
 "char-midgardsormr": [
   P(S["270"], None, "main", "Midgardsormr",
     "An ancient wyrm who travels in your company. He revealed himself to Lady Iceheart when you met her below Gorgagne Mills, to her shock, "
     "and has remarked that his mistress's blessing on you is not as faint as it was.",
     ["M250c", "M270f"]),
 ],
 "char-hraesvelgr": [
   P(S["270"], None, "main", "Hraesvelgr",
     "A great wyrm. Lady Iceheart says the Echo showed her the truth of the Dragonsong War through his eyes, and in her tale the maid Shiva asked him to consume her so their spirits would be joined. "
     "She has agreed to take you to him to seek peace.",
     ["M250d", "M270b", "M270e"], ["the great wyrm"]),
   P(S["281"], None, "main", "Hraesvelgr",
     "A great wyrm and Nidhogg's brood-brother, who, the moogles say, craves peace where Nidhogg craves the opposite. You are seeking him to plead for peace for Ishgard.",
     ["M281c", "M281f", "M280a"], ["the great wyrm"]),
   P(S["289"], None, "main", "Hraesvelgr",
     "A great wyrm and Nidhogg's brood-brother. Summoned by the moogles' horn to Zenith, he refused your plea for peace. He told of King Thordan's ambush of his brood-sister Ratatoskr, "
     "which began the Dragonsong War, and rejected Ysayle's Shiva as a shade of her own fancy.",
     ["M281c", "M285a", "M289b", "M289d", "M289a", "M289f"], ["the great wyrm"]),
 ],
 "char-nidhogg": [
   P(S["264"], None, "main", "Nidhogg",
     "A dragon whose minions, the Dravanian Horde, are gathering once more for war on Ishgard.",
     ["M264e", "M264a"]),
   P(S["265"], None, "main", "Nidhogg",
     "A dreaded wyrm whose Dravanian Horde gathers once more for war on Ishgard. Alphinaud hopes Lady Iceheart can persuade him to stand down.",
     ["M264e", "M264a", "M265a"]),
   P(S["270"], None, "main", "Nidhogg",
     "A dreaded wyrm whose Dravanian Horde gathers for war on Ishgard. Lady Iceheart says he lost an eye to Elezen treachery, and Estinien carries that Eye to draw him away from the city.",
     ["M264e", "M270c", "M270d"]),
   P(S["279"], None, "main", "Nidhogg",
     "A dreaded wyrm whose Horde gathers for war on Ishgard. Estinien carries his stolen eye, and his fury bleeds through it. You defeated his consort, Tioman, on Sohm Al.",
     ["M264e", "M273d", "M279c", "M279b"]),
   P(S["288"], None, "main", "Nidhogg",
     "A dreaded wyrm whose Horde gathers for war on Ishgard, and Hraesvelgr's brood-brother. Estinien carries his stolen eye, and means to kill him himself: Nidhogg killed Estinien's family.",
     ["M264e", "M281c", "M273d", "M288d"]),
   P(S["289"], None, "main", "Nidhogg",
     "A dreaded wyrm, Hraesvelgr's brood-brother. Hraesvelgr says Nidhogg slew King Thordan and some of his knights in vengeance for their ambush of Ratatoskr, beginning the Dragonsong War, "
     "and that heretics who drink dragon blood now become dragons in his army.",
     ["M281c", "M289b", "M289c", "M289d", "M289e"]),
   P(S["290"], None, "main", "Nidhogg",
     "A dreaded wyrm whose vengeance began the Dragonsong War, and whose Horde gathers for war on Ishgard. He has walled his lair, the Aery, behind impenetrable winds, and Estinien means to kill him there.",
     ["M289c", "M289d", "M264a", "M290a", "M290d", "M290b"]),
 ],
 "org-dravanian-horde": [
   P(S["264"], None, "main", "The Dravanian Horde",
     "The dragons and their kin who war on Ishgard as Nidhogg's minions. They gather once more to renew their assault on the city; trappers saw a cloud of dragons that dimmed the midday sky.",
     ["M264e", "M264a", "M264d"], ["the Horde"]),
   P(S["289"], None, "main", "The Dravanian Horde",
     "The dragons and their kin who war on Ishgard as Nidhogg's minions, gathering to renew their assault. Heretics who drink dragon blood become dragons and join Nidhogg's army.",
     ["M264e", "M264a", "M289e"], ["the Horde"]),
 ],
 "char-estinien": [
   P(S["265"], None, "main", "Estinien",
     "Ishgard's Azure Dragoon, who wields the power of the Eye. He insisted on joining the parley with Nidhogg, and Alphinaud agreed on condition that he holds his lance until words fail.",
     ["M265b", "M265d", "M265c"]),
   P(S["270"], None, "main", "Estinien",
     "Ishgard's Azure Dragoon. The Eye he carries is the one Nidhogg lost to Elezen treachery; he kept it to draw Nidhogg away from the city. He travels with you to seek peace.",
     ["M265b", "M270c", "M270d", "M270e"]),
   P(S["272"], None, "main", "Estinien",
     "Ishgard's Azure Dragoon, who carries Nidhogg's lost eye. Travelling through Dravania with you to seek peace, he quarrels with Ysayle, holding to the Holy See's teaching that the ancient ruins are heretics' work.",
     ["M265b", "M270d", "M272d"]),
   P(S["279"], None, "main", "Estinien",
     "Ishgard's Azure Dragoon, who carries Nidhogg's stolen eye. On Sohm Al, Nidhogg's fury bled through it into him, and Vidofnir warned him to keep that stolen power in check.",
     ["M265b", "M273d", "M279c", "M279d"]),
   P(S["286"], None, "main", "Estinien",
     "Ishgard's Azure Dragoon, who carries Nidhogg's stolen eye and watches the wyrm through it. Kan-E-Senna warns that a storm of anguish seethes beneath his calm.",
     ["M265b", "M273d", "M281b", "M286a"]),
   P(S["288"], None, "main", "Estinien",
     "Ishgard's Azure Dragoon, who carries Nidhogg's stolen eye. Nidhogg killed his family, and he means to kill the wyrm himself if Ishgard's survival demands it: his word holds only if the parley succeeds.",
     ["M265b", "M273d", "M288d", "M288e"]),
   P(S["290"], None, "main", "Estinien",
     "Ishgard's Azure Dragoon, who carries Nidhogg's stolen eye. With the parley failed, he means to kill Nidhogg to save Ishgard, and has led you to Nidhogg's lair, the Aery, walled behind impenetrable winds.",
     ["M265b", "M273d", "M290b", "M290a", "M290d"]),
   P(S["291"], None, "main", "Estinien",
     "Ishgard's Azure Dragoon, who carries Nidhogg's stolen eye and means to kill the wyrm to save Ishgard. He keeps watch over Nidhogg's walled lair, the Aery, until you are ready to set out from Ishgard together.",
     ["M265b", "M273d", "M290b", "M290d", "M291a"]),
 ],
 # ---- Dravania ----
 "loc-sohm-al": [
   P(S["271"], None, "main", "Sohm Al",
     "A mountain far to the west in Dravania, the ancient home of dragonkind, where you hope to find the great wyrm Hraesvelgr.",
     ["M271b", "M271c"]),
   P(S["273"], None, "main", "Sohm Al",
     "A mountain in Dravania, the ancient home of dragonkind. The way to its summit stays closed without the help of the dragons of Anyx Trine.",
     ["M271b", "M273a"]),
   P(S["279"], None, "main", "Sohm Al",
     "A mountain in Dravania, the ancient home of dragonkind. Vidofnir opened the way through Mourn, and you fought past Nidhogg's consort, Tioman, to its summit.",
     ["M271b", "M279a", "M279b", "M279e"]),
 ],
 "org-gnath": [
   P(S["272"], None, "main", "The Gnath",
     "A beast tribe of Dravania that has turned to unprovoked attacks.",
     ["M272a"]),
   P(S["273"], None, "main", "The Gnath",
     "A beast tribe of Dravania that has turned to unprovoked attacks under the influence of a primal, their god, which Vidofnir must guard her kin against.",
     ["M272a", "M273b", "M273c"]),
   P(S["275"], None, "main", "The Gnath",
     "A beast tribe of Dravania bound together as the Onemind, whose Overmind heeded black-robed men and summoned a god to seize Dravanian lands. "
     "Outcasts outside that bond, the Vath, say the god's hunger for crystals outweighs what the war yields.",
     ["M275a", "M275b", "M275c", "M275d"]),
   P(S["276"], None, "main", "The Gnath",
     "A beast tribe of Dravania whose Overmind binds the senses of every member of the colony. Heeding black-robed men, it summoned a god to seize Dravanian lands, and captives are brought before that god.",
     ["M276a", "M275b", "M275c", "M276b"]),
   P(S["278"], None, "main", "The Gnath",
     "A beast tribe of Dravania whose prayers for the Dravanians' death gave form to their god, Ravana. You defeated him, and he vowed to call his followers back from the dragons' domain.",
     ["M276a", "M275b", "M278b", "M278e"]),
 ],
 "char-vidofnir": [
   P(S["273"], None, "main", "Vidofnir",
     "A dragon of Anyx Trine and Ysayle's friend, without whose help the way to Sohm Al's summit stays closed. She will not leave her post while the Gnath's god threatens her kin, "
     "and resents that Estinien carries Nidhogg's stolen eye.",
     ["M273a", "M273b", "M273d", "M273e"]),
   P(S["279"], None, "main", "Vidofnir",
     "A dragon of Anyx Trine and Ysayle's friend. With the Gnath's god defeated, she kept her word and opened the way through Mourn to Sohm Al's summit, warning Estinien to keep his stolen power in check.",
     ["M273e", "M279a", "M279d"]),
 ],
 "char-ravana": [
   P(S["278"], None, "main", "Ravana",
     "The primal of the Gnath, Master of the Sacred Blades and Wrath of the Colony, given form by their prayers for the Dravanians' death. He defeated Ysayle as Saint Shiva, "
     "but you beat him, and he vowed to call his followers back from the dragons' domain.",
     ["M278a", "M278b", "M278d", "M278e"], ["Master of the Sacred Blades", "Wrath of the Colony"]),
 ],
 "org-moogles": [
   P(S["281"], None, "main", "The Moogles",
     "Moogles live in the Twelveswood and, it turns out, in the Churning Mists atop Sohm Al. Those of the Mists, led by their chieftain, Moglin, hid from the smell of dragon blood, "
     "and set you trials before they will help you find Hraesvelgr.",
     ["M280b", "M281d", "M281e", "M281g"]),
   P(S["285"], None, "main", "The Moogles",
     "Moogles live in the Twelveswood and in the Churning Mists atop Sohm Al. Those of the Mists, led by Moglin, repaired the horn that summons Hraesvelgr and trust you now, "
     "thanks to your friendship with a Twelveswood moogle.",
     ["M281d", "M285a", "M285c"]),
 ],
 "char-moglin": [
   P(S["281"], None, "main", "Moglin",
     "Chieftain of the moogles of the Churning Mists, wary of the dragon blood he smells on you. He says some dragons, like Hraesvelgr, crave peace and others, like Nidhogg, the opposite, "
     "and has set you trials before he will help.",
     ["M281d", "M281e", "M281f", "M281g"]),
   P(S["285"], None, "main", "Moglin",
     "Chieftain of the moogles of the Churning Mists. His trials only kept you busy while his moogles repaired the horn that summons Hraesvelgr, and he has sent you to blow it at Zenith.",
     ["M281d", "M285a", "M285b"]),
 ],
 "loc-aery": [
   P(S["290"], None, "main", "The Aery",
     "Nidhogg's lair in Dravania, which he has walled behind a barrier of impenetrable winds.",
     ["M290a", "M290d"]),
   P(S["291"], None, "main", "The Aery",
     "Nidhogg's lair in Dravania, walled behind a barrier of impenetrable winds. Estinien keeps watch over it, and Cid's crew is finishing a small airship, the manacutter, to get you in.",
     ["M290a", "M290d", "M291a", "M291d"]),
 ],
 # ---- The Ironworks ----
 "char-cid": [
   P(S["250b"], None, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. The Holy See has asked his help with its airship, the Protector, and at Camp Cloudtop he swooped in aboard the Enterprise "
     "to carry you away from the primal Bismarck.",
     ["K07", "M250be", "M250bd", "M250bf"]),
   P(S["291"], None, "main", "Cid",
     "A brilliant engineer from Garlemald who built the Ironworks, now in Ishgard working on the Holy See's airship. The Enterprise can't dodge dragons, so his crew is finishing a small airship, "
     "the manacutter, to breach the winds around Nidhogg's lair, and he has sent you to Ul'dah meanwhile.",
     ["K07", "M291b", "M291c", "M291d", "M290e", "M291e"]),
 ],
 "char-biggs": [
   P(S["291"], None, "main", "Biggs",
     "A member of Cid's Ironworks crew. With Wedge he built a small new airship, the manacutter, which Cid is finishing to reach Nidhogg's lair.",
     ["E147e", "M291d", "M291e"]),
 ],
 "char-wedge": [
   P(S["291"], None, "main", "Wedge",
     "A member of Cid's Ironworks crew. With Biggs he built a small new airship, the manacutter, which Cid is finishing to reach Nidhogg's lair.",
     ["E147e", "M291d", "M291e"]),
 ],
}

# ---- Relationship types and relationships -------------------------------------------------------------------------
TYPES = [
 ("child-of", "child of", "parent of", False),
 ("sibling-of", "sibling of", "sibling of", True),
]

# (id, source, type, target, from, until, scope, claims[, end claims])
RELS = [
 ("rel-scions-headquartered-at-fortemps-manor", "org-scions", "headquartered-at", "loc-fortemps-manor", S["242"], None, "main", ["M242b", "M242a"]),
 ("rel-edmont-aids-scions", "char-edmont", "aids", "org-scions", S["242"], None, "main", ["M242a", "M242i"]),
 ("rel-artoirel-child-of-edmont", "char-artoirel", "child-of", "char-edmont", S["244"], None, "main", ["M244d", "M244e"]),
 ("rel-emmanellain-child-of-edmont", "char-emmanellain", "child-of", "char-edmont", S["244"], None, "main", ["M244d", "M244e"]),
 ("rel-artoirel-sibling-of-emmanellain", "char-artoirel", "sibling-of", "char-emmanellain", S["244"], None, "main", ["M244e"]),
 ("rel-thordan-leads-holy-see", "char-thordan", "leads", "org-holy-see", S["245"], None, "main", ["M242c", "M243b"]),
 ("rel-holy-see-opposes-iceheart", "org-holy-see", "opposes", "char-iceheart", S["245"], S["271"], "main", ["M245e", "M245f"]),
 ("rel-laniaitte-member-of-house-haillenarte", "char-laniaitte", "member-of", "org-house-haillenarte", S["245b"], None, "main", ["M245be"]),
 ("rel-laniaitte-leads-camp-cloudtop", "char-laniaitte", "leads", "loc-camp-cloudtop", S["245b"], None, "main", ["M245be"]),
 ("rel-laniaitte-sibling-of-francel", "char-laniaitte", "sibling-of", "char-francel", S["245b"], None, "main", ["M245bg"]),
 ("rel-vanu-vanu-opposes-camp-cloudtop", "org-vanu-vanu", "opposes", "loc-camp-cloudtop", S["247b"], None, "main", ["M247ba", "M247bb"]),
 ("rel-bismarck-summoned-by-vanu-vanu", "char-bismarck", "summoned-by", "org-vanu-vanu", S["250b"], None, "main", ["M250bc"]),
 ("rel-cid-aids-holy-see", "char-cid", "aids", "org-holy-see", S["250b"], None, "main", ["M250be"]),
 # Artoirel's chain (#251) reveals Haurchefant's parentage; these start at #259 so Emmanellain's steps don't show it.
 ("rel-haurchefant-child-of-edmont", "char-haurchefant", "child-of", "char-edmont", S["259"], None, "main", ["M251c"]),
 ("rel-haurchefant-sibling-of-artoirel", "char-haurchefant", "sibling-of", "char-artoirel", S["259"], None, "main", ["M251b"]),
 ("rel-heavens-ward-serves-thordan", "org-heavens-ward", "serves", "char-thordan", S["259"], None, "main", ["M259b"]),
 ("rel-grinnaux-member-of-heavens-ward", "char-grinnaux", "member-of", "org-heavens-ward", S["259"], None, "main", ["M259a"]),
 ("rel-grinnaux-member-of-house-dzemael", "char-grinnaux", "member-of", "org-house-dzemael", S["259"], None, "main", ["M259d"]),
 ("rel-zephirin-member-of-heavens-ward", "char-zephirin", "member-of", "org-heavens-ward", S["260"], None, "main", ["M260b"]),
 ("rel-merlwyb-aids-scions", "char-merlwyb", "aids", "org-scions", S["261"], None, "main", ["M261a", "M261c"]),
 ("rel-crystal-braves-turned-against-doman-refugees", "org-crystal-braves", "turned-against", "org-doman-refugees", S["261"], None, "main", ["M261i"]),
 ("rel-doman-refugees-aids-scions", "org-doman-refugees", "aids", "org-scions", S["261"], None, "main", ["M261j"]),
 ("rel-dewlala-member-of-syndicate", "char-dewlala", "member-of", "org-syndicate", S["263"], None, "main", ["M263d"]),
 ("rel-nidhogg-leads-dravanian-horde", "char-nidhogg", "leads", "org-dravanian-horde", S["264"], None, "main", ["M264e"]),
 ("rel-dravanian-horde-opposes-holy-see", "org-dravanian-horde", "opposes", "org-holy-see", S["264"], None, "main", ["M264a", "M264e"]),
 ("rel-estinien-aids-scions", "char-estinien", "aids", "org-scions", S["265"], None, "main", ["M265b", "M265c"]),
 ("rel-aymeric-aids-scions", "char-aymeric", "aids", "org-scions", S["265"], None, "main", ["M265e", "M259g"]),
 ("rel-zephirin-serves-thordan", "char-zephirin", "serves", "char-thordan", S["265"], None, "main", ["M265f", "M265g"]),
 ("rel-iceheart-revealed-as-ysayle", "char-iceheart", "revealed-as", "char-ysayle", S["271"], None, "main", ["M271a"]),
 ("rel-ysayle-aids-scions", "char-ysayle", "aids", "org-scions", S["271"], None, "main", ["M270e", "M271a"]),
 ("rel-holy-see-opposes-ysayle", "org-holy-see", "opposes", "char-ysayle", S["271"], None, "main", ["M245e", "M245f", "M271a"]),
 ("rel-gnath-opposes-vidofnir", "org-gnath", "opposes", "char-vidofnir", S["273"], S["278"], "main", ["M273b", "M273c"], ["M278e"]),
 ("rel-ravana-summoned-by-gnath", "char-ravana", "summoned-by", "org-gnath", S["278"], None, "main", ["M274a", "M278b"]),
 ("rel-vidofnir-aids-scions", "char-vidofnir", "aids", "org-scions", S["279"], None, "main", ["M279a"]),
 ("rel-hraesvelgr-sibling-of-nidhogg", "char-hraesvelgr", "sibling-of", "char-nidhogg", S["281"], None, "main", ["M281c"]),
 ("rel-moglin-leads-moogles", "char-moglin", "leads", "org-moogles", S["281"], None, "main", ["M281d"]),
 ("rel-moogles-aids-scions", "org-moogles", "aids", "org-scions", S["285"], None, "main", ["M285a", "M285c"]),
 ("rel-estinien-opposes-nidhogg", "char-estinien", "opposes", "char-nidhogg", S["288"], None, "main", ["M288d", "M288e"]),
 ("rel-nidhogg-headquartered-at-aery", "char-nidhogg", "headquartered-at", "loc-aery", S["290"], None, "main", ["M290a", "M290d"]),
 ("rel-cid-aids-scions", "char-cid", "aids", "org-scions", S["291"], None, "main", ["M291d", "M291e", "M290e"]),
]

# Arc casts: (member, from step, claims). At most 10 per arc, counted over the whole arc.
CASTS = {
 ARC1: [("char-alphinaud", S["242"], ["M242a"]), ("char-tataru", S["242"], ["M242a"]), ("char-haurchefant", S["242"], ["M242b"]),
        ("char-edmont", S["242"], ["M242a"]), ("org-scions", S["242"], ["M242e"]), ("loc-fortemps-manor", S["242"], ["M242b"]),
        ("char-artoirel", S["244"], ["M244d"]), ("char-emmanellain", S["244"], ["M244d"]), ("org-holy-see", S["245"], ["M245e"]),
        ("char-iceheart", S["245"], ["M245f"])],
 ARC2: [("char-emmanellain", S["245b"], ["M245bc"]), ("char-laniaitte", S["245b"], ["M245be"]), ("org-house-haillenarte", S["245b"], ["M245bc"]),
        ("loc-camp-cloudtop", S["245b"], ["M245bd"]), ("char-francel", S["245b"], ["M245bg"]), ("org-vanu-vanu", S["245b"], ["M245bf"]),
        ("char-haurchefant", S["250b"], ["M250bb"]), ("char-bismarck", S["250b"], ["M250bc"]), ("char-cid", S["250b"], ["M250bd"])],
 ARC3: [("char-alphinaud", S["259"], ["M259a"]), ("char-tataru", S["259"], ["M259a"]), ("org-heavens-ward", S["259"], ["M259a"]),
        ("char-grinnaux", S["259"], ["M259a"]), ("char-aymeric", S["259"], ["M259g"]), ("char-thordan", S["260"], ["M260a"]),
        ("char-merlwyb", S["261"], ["M261a"]), ("org-crystal-braves", S["261"], ["M261b"]), ("org-doman-refugees", S["261"], ["M261j"]),
        ("char-dewlala", S["263"], ["M263d"])],
 ARC4: [("char-alphinaud", S["264"], ["M264g"]), ("char-edmont", S["264"], ["M264f"]), ("org-dravanian-horde", S["264"], ["M264a"]),
        ("char-nidhogg", S["264"], ["M264e"]), ("char-estinien", S["265"], ["M265b"]), ("char-aymeric", S["265"], ["M265e"]),
        ("char-thordan", S["265"], ["M265f"]), ("char-zephirin", S["265"], ["M265h"]), ("char-iceheart", S["265"], ["M265a"]),
        ("char-hraesvelgr", S["270"], ["M270e"])],
 ARC5: [("char-ysayle", S["271"], ["M271a"]), ("char-alphinaud", S["271"], ["M271a"]), ("char-estinien", S["271"], ["M270d"]),
        ("loc-sohm-al", S["271"], ["M271b"]), ("char-hraesvelgr", S["271"], ["M270e"]), ("org-gnath", S["272"], ["M272a"]),
        ("char-vidofnir", S["273"], ["M273b"]), ("char-shiva", S["274"], ["M274b"]), ("char-ravana", S["278"], ["M278a"]),
        ("char-nidhogg", S["279"], ["M279b"])],
 ARC6: [("char-alphinaud", S["281"], ["M280a"]), ("char-ysayle", S["281"], ["M271a"]), ("char-estinien", S["281"], ["M281b"]),
        ("char-hraesvelgr", S["281"], ["M281c"]), ("char-kan-e-senna", S["281"], ["M281a"]), ("org-moogles", S["281"], ["M281e"]),
        ("char-moglin", S["281"], ["M281d"]), ("char-nidhogg", S["281"], ["M281b"]), ("loc-aery", S["290"], ["M290a"]),
        ("char-cid", S["291"], ["M291b"])],
}

ARCS = [
 ("arc-e1-wards-of-house-fortemps", ARC1, S["242"], S["251"]),
 ("arc-e2-the-sea-of-clouds", ARC2, S["245b"], S["251b"]),
 ("arc-e3-friends-in-chains", ARC3, S["259"], S["263"]),
 ("arc-e4-hunt-for-lady-iceheart", ARC4, S["264"], S["270"]),
 ("arc-e5-road-to-sohm-al", ARC5, S["271"], S["280"]),
 ("arc-e6-great-wyrms-answer", ARC6, S["281"], S["291"]),
]
ARC_NOTES = {
 "arc-e1-wards-of-house-fortemps": "MSQ #242 *Coming to Ishgard* to #251 *Knights Be Not Proud*: arrival in Ishgard as wards of House Fortemps (M242a), then Artoirel's chain at Falcon's Nest, "
   "ending with Artoirel's confession and the half-brother reveal (M251b). #247 *The First and Foremost* cites nothing: its title and URL contain the banned \"The First\". "
   "The entry gets a chain-neutral presentation at #245b (the story as of #244) and a full one at #259.",
 "arc-e2-the-sea-of-clouds": "MSQ #245b *Onwards and Upwards* to #251b *A Reward Long in Coming*: Emmanellain's chain at Camp Cloudtop, from the mission to aid House Haillenarte (M245bc) to "
   "Bismarck and the scolding (M251bd). A separate arc because the chain is parallel to e1; no recap here depends on Artoirel's chain.",
 "arc-e3-friends-in-chains": "MSQ #259 *Divine Intervention* to #263 *Keeping the Flame Alive*: the chains rejoin; Alphinaud and Tataru's heresy arrest and trial (M259a), the archbishop's "
   "confession (M260d), and the rescue of Raubahn (M263a). Ends when Dewlala reveals the sultana lives (M263e).",
 "arc-e4-hunt-for-lady-iceheart": "MSQ #264 *To Siege or Not to Siege* to #270 *Purple Flame, Purple Flame*: the Horde gathers (M264a), Alphinaud chooses peace over flight, and the search "
   "for Iceheart ends when she agrees to guide you to Hraesvelgr (M270e).",
 "arc-e5-road-to-sohm-al": "MSQ #271 *Where the Chocobos Roam* to #280 *Beyond the Clouds*: Iceheart becomes Ysayle (M271a), Ravana falls (M278e), and the party reaches Sohm Al's summit "
   "(M279e). Ends on the vanished moogle, which opens the next arc.",
 "arc-e6-great-wyrms-answer": "MSQ #281 *Mountaintop Diplomacy* to #291 *New Winds, Old Friends*, with all three moogle trials: Moghome, the horn, Hraesvelgr's refusal (M289f) and the walled "
   "Aery, ending when Cid's manacutter is under way and Tataru's news sends you to Ul'dah (M291e), where 3.0 part 2 picks up.",
}

DECISIONS = [
 "Parallel chains: arc e1 (Artoirel, #245–#251) and arc e2 (Emmanellain, #245b–#251b) are separate arcs. Arc e1's entry and Artoirel get a chain-neutral presentation at #245b and a full one at #259, so Emmanellain-first players don't see Artoirel's chain; this means an Artoirel-first player sees those two entries step back to the #244 story during #245b–#251b.",
 "Artoirel-chain facts about other entities (Haurchefant's parentage, Iceheart's encounter, Midgardsormr, Hraesvelgr) appear on those entities only from #259 or #270; the #250 recap describes Midgardsormr as \"the ancient wyrm who travels with you\" and Hraesvelgr as \"a great wyrm\". Iceheart's #245 presentation (named by Artoirel as a heretic leader) is the one Artoirel-chain record visible on Emmanellain steps.",
 "No claim cites #247 *The First and Foremost*: its citation title and URL contain \"The First\" (a banned name and a NeverLink page fragment). #247's recap carries the #246 state forward.",
 "Not made entries: Raubahn, Yugiri, Ilberd, Ishgard and House Fortemps. Their names already appear in accepted text before any era module can make them visible (Raubahn at #159, Yugiri and Ilberd at 2.55, Ishgard from #112, House Fortemps from #116), so an entry would fail the visibility lint on accepted records. They are named in text only; Fortemps Manor and Count Edmont stand in for the house.",
 "Iceheart becomes Ysayle at #271 as a reveal (rule 5): char-iceheart keeps a final presentation explaining the name, a revealed-as edge to char-ysayle, and Ysayle carries \"Iceheart\" and \"Lady Iceheart\" as aliases.",
 "Ravana is unnamed (\"the Gnath's god\") until #278, where the page first names him; his entry and summoned-by edge start there.",
 "The voice after Ravana's fall (#278) is a banned Ascian name, so the recap says \"a mysterious voice\". Moogle trial-givers, Tioman, Marcechamp, Honoroit, Redwald and other incidental NPCs are named in recaps at most, with no entries.",
 "Thordan VII's double game is shown as both pages state it: he tells you he pays the Ascians lip service (#260), and tells Zephirin they will reward their Ascian allies (#265). The Atlas draws no conclusion.",
]
