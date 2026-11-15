"""Authoring source for the Atlas content: the pilot (NDL-003) and arc A4 (NDL-009).

Builds, from the claims and text below:
  - NpcDialogueLinks/atlas.json       the data the plugin and the local viewer load
  - docs/atlas/content-review.md      the human review sheet
  - docs/atlas/content-claims.md      the claim-by-claim evidence table

Edit this file, never the generated outputs, then run from the repository root:
    python3 tools/atlas/build_pilot_content.py
and rerun `dotnet test NpcDialogueLinks.Tests`. See docs/atlas/content-evidence.md.

Review status is per record and bound to content (schema v2, NDL-006). ACCEPTED maps each accepted record's key to a
fingerprint of its emitted content; a record is "reviewed" only when its current fingerprint matches. A new record, or
any change to an accepted one, is emitted "pending" until the user accepts it and its fingerprint is recorded. The
fingerprint covers the emitted record (text, interval, endpoints, scope, citations) and the reviewed context it is
shown with: the entity's category for a presentation, the type's labels and symmetry for a relationship, and the
claims (wording, source and locator) behind either. The only exempt field is a citation's availableAt, which the v2
plan allows to move earlier mechanically.

    --self-test       checks these rules without writing anything
    --print-pending   prints the key and fingerprint of each pending record, to copy into ACCEPTED after acceptance
"""
import copy, hashlib, json, sys, pathlib, urllib.parse

REPO = pathlib.Path(__file__).resolve().parents[2]
SELF_TEST = sys.argv[1:] == ["--self-test"]
PRINT_PENDING = sys.argv[1:] == ["--print-pending"]
if sys.argv[1:] and not (SELF_TEST or PRINT_PENDING):
    sys.exit("Usage: build_pilot_content.py [--self-test | --print-pending]. Review status is per record (see ACCEPTED).")
A, B = "cp-arr-2-0", "cp-arr-2-55"

# ---- Timeline (schema v2) ---------------------------------------------------------------------------------------
# The A4 slice (NDL-009): the baseline step after MSQ #154, then one step after each of #155–160. Each step means
# "after this quest". The milestone A (cp-arr-2-0) is the step after #161, The Ultimate Weapon, so it is contiguous
# with the slice. Every step carries its quest's game id (wiki id-gt) for Follow (deferred; NDL-007 verifies them).
SLICE = [  # (checkpoint id, MSQ index, quest title, game quest id)
    ("cp-msq-154", 154, "Every Little Thing She Does Is Magitek", 66541),
    ("cp-msq-155", 155, "Escape from Castrum Centri", 66057),
    ("cp-msq-156", 156, "The Black Wolf's Ultimatum", 66058),
    ("cp-msq-157", 157, "Operation Archon", 70057),
    ("cp-msq-158", 158, "A Hero in Need", 66573),
    ("cp-msq-159", 159, "Hearts on Fire", 69408),
    ("cp-msq-160", 160, "Rock the Castrum", 69409),
]
BASE = SLICE[0][0]
STEP_OF = {title: cid for cid, _, title, _ in SLICE}
CP_LABEL = {A: "A Realm Reborn — Patch 2.0 complete", B: "A Realm Reborn — Patch 2.55 complete",
            **{cid: f"After {title}" for cid, _, title, _ in SLICE}}
CP_SHORT = {A: "2.0", B: "2.55", **{cid: f"#{n}" for cid, n, _, _ in SLICE}}
ORDER = [cid for cid, _, _, _ in SLICE] + [A, B]

# ---- Sources: wiki page title -> (display title, patch, availableAt, scope) -------------------------------
# availableAt is the earliest timeline step at or after the quest: a 2.0 main quest before #154 counts from the
# baseline, a slice quest from its own step, The Ultimate Weapon from cp-arr-2-0; later patches from cp-arr-2-55, and
# optional quests from the milestone of their patch. Moving an accepted citation's availableAt earlier this way is the
# v2 plan's permitted mechanical change (it is never displayed, and the fingerprint ignores it).
SRC = {}
def src(key, page, patch, scope="main", kind=None):
    if scope == "optional" or patch != "2.0":
        avail = A if patch == "2.0" else B
    else:
        avail = A if key == "The Ultimate Weapon" else STEP_OF.get(key, BASE)
    label = kind or ("main scenario quest" if scope == "main" else "optional Binding Coil quest")
    SRC[key] = dict(page=page, patch=patch, avail=avail, scope=scope,
                    title=f"{key} — {label} ({patch})")

for k, p in [("The Scions of the Seventh Dawn", "The Scions of the Seventh Dawn (Quest)"),
             ("A Wild Rose by Any Other Name", None), ("Casing the Castrum", None), ("Escape from Castrum Centri", None),
             ("All Good Things", None), ("Reclamation", None), ("A Hero in the Making", None),
             ("Back from the Wood", "Back from the Wood (Quest)"), ("Eyes on Me", None), ("The Ultimate Weapon", None),
             ("The Lominsan Envoy", None), ("The Gridanian Envoy", None)]:
    src(k, p or k, "2.0")
src("Alisaie's Pledge", "Alisaie's Pledge", "2.0", "optional")
for k, patch in [("The Gifted", "2.1"), ("Laying the Foundation", "2.1"), ("Build on the Stone", "2.1"),
                 ("Brave New Companions", "2.3"), ("Traitor in the Midst", "2.4"), ("An Uninvited Ascian", "2.5"),
                 ("Administrative Decision", "2.55"), ("An Unexpected Ambition", "2.55"), ("The Steps of Faith", "2.55"),
                 ("The Parting Glass", "2.55"), ("Before the Dawn", "2.55")]:
    src(k, k, patch)
for k, patch in [("Another Turn in the Coil", "2.2"), ("Alisaie's Resolve", "2.2"), ("Alisaie's Path", "2.4")]:
    src(k, k, patch, "optional")

# ---- Claims: id -> (own-words claim, source key, locator quote) ------------------------------------------------
C = {
 "C01": ("Minfilia leads the Scions.", "The Scions of the Seventh Dawn", "My name is Minfilia, and I lead the Scions of the Seventh Dawn."),
 "C02": ("The Scions are headquartered at the Waking Sands in Vesper Bay, western Thanalan.", "The Scions of the Seventh Dawn", "the Waking Sands, located in Vesper Bay, out in western Thanalan"),
 "C33": ("Minfilia has the Echo.", "The Scions of the Seventh Dawn", "That's right. I too possess the Echo."),
 "C34": ("The Scions stand above politics; their aim is preserving Eorzea's future.", "The Scions of the Seventh Dawn", "an order that transcends political boundaries. Our single objective is the preservation of the future of Eorzea."),
 "C31": ("Minfilia introduces Yda, Papalymo, Thancred, Y'shtola and Urianger as the player's friends in the order: Sharlayans who stayed in Eorzea when their countrymen fled.", "A Wild Rose by Any Other Name", "I would introduce you to your friends in the order. … Those same brave souls stand before you now."),
 "C32": ("Tataru is the Scions' clerk.", "A Wild Rose by Any Other Name", "Oh, I should also introduce you to Tataru, our clerk. She ensures that everything runs smoothly."),
 "C39": ("Thancred is the Scions' man in Ul'dah and briefs the player's first investigation.", "A Wild Rose by Any Other Name", "He is our man here in Ul'dah, jewel of the desert. … Thancred, would you do the honors?"),
 "C40": ("Y'shtola looks after Limsa Lominsa for the order and tells how the Scions were founded.", "A Wild Rose by Any Other Name", "Limsa Lominsa has the pleasure of being under her care. … together established the Scions of the Seventh Dawn."),
 "C41": ("Urianger presides over the affairs of the Waking Sands.", "A Wild Rose by Any Other Name", "Last but not least is Urianger, who presides over all affairs within these halls."),
 "C06": ("Imperial forces raid the Waking Sands and take prisoners.", "All Good Things", "the Waking Sands was raided by imperial forces"),
 "C36": ("The prisoners are Minfilia, Urianger, Papalymo and Tataru, whom Y'shtola calls \"our fellow Scions\".", "Casing the Castrum", "Minfilia, Urianger, Papalymo, and Tataru! … the Garleans took our fellow Scions prisoner"),
 "C37": ("The rescue from Castrum Centri succeeds, and Thancred is revealed to have been possessed by Lahabrea.", "Escape from Castrum Centri", "Though the rescue mission was a success, the shocking revelation that Thancred has been possessed by Lahabrea"),
 "C38": ("The Scions restore their damaged headquarters.", "Reclamation", "To leave our headquarters in disrepair any longer would be to dishonor the memory of those who fell there."),
 "C10": ("Alphinaud and Alisaie are twins.", "A Hero in the Making", "the traveling twins, Alphinaud and Alisaie … And my sister, Alisaie, at your service."),
 "C42": ("The twins call themselves students of history; Alisaie means to find another way to heal the realm.", "A Hero in the Making", "You might call us students of history … There must be another way to cure what ails this world─and I mean to find it!"),
 "C11": ("Alisaie walks her own path, but shares her brother's goal.", "Back from the Wood", "Alisaie has chosen to walk her own path─stubborn girl─but you may be assured that our destination remains the same."),
 "C25": ("Alphinaud is a Scion.", "Eyes on Me", "As a Scion of the Seventh Dawn, I stand against our primal and imperial foes─as my grandfather once did."),
 "C43": ("Alphinaud's grandfather gave his life for a dream Alphinaud carries on.", "The Ultimate Weapon", "Do you see, Grandfather? Our first step towards realizing the dream for which you gave your life."),
 "C09": ("The player frees Thancred from Lahabrea's enthrallment, and he returns with them.", "The Ultimate Weapon", "free your comrade Thancred from his enthrallment … Look! Thancred is with him/her!"),
 "C44": ("Archon Louisoix never returned from Carteneau, and the realm's leaders miss his wisdom.", "The Lominsan Envoy", "Archon Louisoix may well have been able to shed light upon these mysteries, but he, like so many, never returned from Carteneau."),
 "C44b": ("The Admiral wishes Archon Louisoix were still with them.", "The Gridanian Envoy", "Were Archon Louisoix still with us, he would doubtless shed some light on these unfathomable happenings. Alas, he is not"),
 "C44c": ("The Scions feel Master Louisoix's guidance still.", "Reclamation", "It is as if the benevolent hand of Master Louisoix guides us still."),
 "C13": ("Louisoix was Alisaie's grandfather.", "Alisaie's Pledge", "Master Louisoix was my lady's grandsire."),
 "C27": ("Bahamut was sealed beneath Carteneau, seemingly by Louisoix, who is presumed dead.", "Alisaie's Pledge", "Bahamut was sealed deep beneath the Carteneau Flats seemingly by Louisoix, who was presumed dead."),
 "C58": ("Alisaie believes she saw her grandfather alive in the Binding Coil.", "Alisaie's Pledge", "I saw him with my own two eyes—as did [Forename]."),
 "C30": ("The journal calls Alisaie \"the young Scion\".", "Alisaie's Pledge", "Urianger bids you join the young Scion in reflecting upon all that you witnessed within the Binding Coil."),
 "C45": ("The Waking Sands stops being the headquarters and passes to Urianger; Alisaie keeps working with him.", "The Gifted", "the Waking Sands will formally cease to be our headquarters, and the premises will be given into the care of Urianger. … Alisaie shall continue to work closely with him"),
 "C14": ("The Scions find a new home in Revenant's Toll, Mor Dhona.", "Laying the Foundation", "we have found ourselves a new home in Revenant's Toll"),
 "C15": ("The Rising Stones, entered through the Seventh Heaven, is inaugurated as the new headquarters; Tataru is its receptionist.", "Build on the Stone", "celebrate the inauguration of their new headquarters … speak with Tataru inside the Seventh Heaven … your restive receptionist"),
 "C48": ("Alphinaud names his company the Crystal Braves: pledged to the Scions, bound to no single nation, fighting for a united Eorzea.", "Brave New Companions", "the name he has chosen for the trial company: the Crystal Braves … beholden to no single nation. You stand as the vanguard for a united Eorzea!"),
 "C16": ("Alphinaud commands the Crystal Braves, with Captain Ilberd as his second-in-command.", "Traitor in the Midst", "his new station as commander of the Crystal Braves … Captain Ilberd, his second-in-command"),
 "C54": ("Louisoix founded the Circle of Knowing, came to Eorzea, and spared the realm through his sacrifice; Urianger and Moenbryda studied under him.", "An Uninvited Ascian", "Moenbryda and I did study under the sage tutelage of Master Louisoix. … he founded the Circle of Knowing … Through his noble sacrifice was the realm spared its doom."),
 "C55": ("The Scions still hold to Louisoix's teachings.", "The Steps of Faith", "To do otherwise would go against all that Master Louisoix has taught us."),
 "C47": ("Tataru leaves to train as an arcanist so she can protect others, then gives it up.", "Administrative Decision", "When I return, I shall be both your receptionist and your bodyguard!"),
 "C47b": ("Tataru renounces arcanima.", "An Unexpected Ambition", "Crestfallen, she renounces arcanima and returns to the city."),
 "C50": ("At the banquet the Scions are accused of conspiring to poison the sultana, detained, and branded fugitives.", "The Parting Glass", "I hereby accuse you of regicide! … all members of the Scions of the Seventh Dawn will be detained for questioning … branded fugitives"),
 "C51": ("Thancred is accused of spying for the Empire, and leads the escape through a hidden passage.", "The Parting Glass", "You stand accused of committing acts of espionage in service to the Garlean Empire. … the passages hidden in the walls of the palace"),
 "C17": ("Minfilia stays behind, saying Hydaelyn speaks to her.", "The Parting Glass", "Hydaelyn... She speaks to me. … I must remain behind...but you cannot stay with me."),
 "C18": ("Y'shtola and Thancred stay behind to stop the pursuit.", "The Parting Glass", "You two go on ahead. Thancred and I will deal with this."),
 "C19": ("The Crystal Braves seize the Rising Stones and detain the Scions' allies.", "The Parting Glass", "we have detained all those with allegiance to the Scions. The Rising Stones is also under our control."),
 "C52": ("The Braves turn on Alphinaud, who later blames himself for using the Braves and Scions as pawns.", "The Parting Glass", "I thought the Crystal Braves mine till the very moment I felt the blade at my back"),
 "C52b": ("Alphinaud blames himself.", "Before the Dawn", "I treated the Crystal Braves, and even the Scions themselves, as pawns in my great scheme to save the realm."),
 "C23": ("Alphinaud believes Alisaie was watching over him.", "The Parting Glass", "I had thought to look out for Alisaie, but 'twould appear she was the one watching over me."),
 "C20": ("Crystal Braves turn on the Scions' people in the marketplace.", "Before the Dawn", "And then Crystal Braves─our own people!─turned on us in the marketplace."),
 "C19b": ("Only Crystal Braves remain at the Rising Stones.", "Before the Dawn", "Only Crystal Braves await you there."),
 "C21": ("Urianger hides the Waking Sands behind a glamour that makes it look abandoned, sheltering refugees.", "Before the Dawn", "he used his magicks to weave a glamour around the Waking Sands … our old headquarters now looks like an abandoned storehouse!"),
 "C53": ("Yugiri rescued Tataru from the Crystal Braves.", "Before the Dawn", "the refugee leader having rescued the young receptionist from Crystal Braves"),
 "C22": ("Every other Scion at the banquet is unaccounted for; Minfilia and the others do not respond.", "Before the Dawn", "every other Scion who attended the banquet remains unaccounted for … I tried contacting Minfilia and the others, but no one would respond"),
 "C24": ("The survivors regroup in an intercessory in Coerthas.", "Before the Dawn", "join your companions in the intercessory"),
 "C26": ("Alphinaud speaks of \"our grandsire\", shared with his sister.", "Another Turn in the Coil", "my sister's admiration and affection for our grandsire exceeds even mine own."),
 "C56": ("What Alisaie saw was an aetherial shadow of Louisoix bound by Bahamut.", "Alisaie's Resolve", "'twas but the aetherial shadow of Master Louisoix that Lady Alisaie beheld"),
 "C28": ("The player freed Louisoix's soul from Bahamut.", "Alisaie's Path", "You are the one who freed Grandfather's soul and saved Eorzea from Bahamut's wrath."),
 "C57": ("Alisaie now means to find her own reason to fight for Eorzea.", "Alisaie's Path", "I mean to find my own reason to fight for Eorzea."),
}

def cites(claims):
    seen = []
    for c in claims:
        k = C[c][1]
        if k not in seen:
            seen.append(k)
    return seen

# ---- Entities -------------------------------------------------------------------------------------------------
def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

CHECKPOINTS = [
    {"id": cid, "label": CP_LABEL[cid], "questTitle": title, **({"contiguousWithPrevious": True} if i else {}), "gameQuestIds": [gid]}
    for i, (cid, _, title, gid) in enumerate(SLICE)
] + [
    {"id": A, "label": CP_LABEL[A], "milestone": True, "contiguousWithPrevious": True, "gameQuestIds": [70058]},  # The Ultimate Weapon (#161)
    {"id": B, "label": CP_LABEL[B], "milestone": True, "gameQuestIds": [65964]},  # Before the Dawn
]

ENT = [
 ("char-minfilia", "character", [
   P(A, B, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who welcomes you at the Waking Sands. Like you, she has the Echo. "
     "She was taken prisoner when imperial forces raided the Waking Sands, and after her rescue from Castrum Centri she leads the Scions again.",
     ["C01", "C33", "C36", "C37"], ["the Antecedent"]),
   P(B, None, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. She led the Scions' move from the Waking Sands to the Rising Stones in Mor Dhona. "
     "When the Scions were accused of plotting the sultana's death at a royal banquet in Ul'dah, she stayed behind during the escape, saying that Hydaelyn was speaking to her. "
     "No one has heard from her since.",
     ["C45", "C14", "C50", "C17", "C22"], ["the Antecedent"]),
 ]),
 ("char-thancred", "character", [
   P(A, B, "main", "Thancred",
     "A Scion and bard who serves as the order's man in Ul'dah and briefed your first investigation. "
     "During the rescue at Castrum Centri, the Scions learned that the Ascian Lahabrea had possessed him. You freed him from that enthrallment, and he came home with you.",
     ["C31", "C39", "C37", "C09"]),
   P(B, None, "main", "Thancred",
     "A Scion and bard. At the royal banquet in Ul'dah he was arrested and accused of spying for the Garlean Empire. "
     "He led the escape through a hidden passage in the palace, then stayed behind with Y'shtola to stop the pursuit so the others could get away. He is unaccounted for.",
     ["C51", "C18", "C22"]),
 ]),
 ("char-yshtola", "character", [
   P(A, B, "main", "Y'shtola",
     "A Sharlayan Scion who looks after the order's affairs in Limsa Lominsa. She explains how the Scions came to be: after their leader was lost at Carteneau, they sought out Minfilia and others with the Echo. "
     "She helped plan the rescue of the Scions captured in the imperial raid.",
     ["C31", "C40", "C36"]),
   P(B, None, "main", "Y'shtola",
     "A Sharlayan Scion. When the Scions fled the royal banquet in Ul'dah through a hidden tunnel, she and Thancred stayed behind, and she brought the tunnel down to stop their pursuers. She is unaccounted for.",
     ["C18", "C22"]),
 ]),
 ("char-urianger", "character", [
   P(A, B, "main", "Urianger",
     "A learned Sharlayan Scion who presides over the affairs of the Waking Sands. "
     "He was among the Scions taken prisoner in the imperial raid, and was freed in the rescue at Castrum Centri.",
     ["C31", "C41", "C36", "C37"]),
   P(B, None, "main", "Urianger",
     "A learned Sharlayan Scion who once studied under Louisoix. When the Scions moved to the Rising Stones, the Waking Sands was left in his care. "
     "After the royal banquet he hid it behind a glamour, so that it now looks like an abandoned storehouse and shelters those fleeing the Crystal Braves.",
     ["C54", "C45", "C21"]),
 ]),
 ("char-alphinaud", "character", [
   P(A, B, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother. The twins first appear as self-described students of history, touring the city-states' remembrance services. "
     "After the raid on the Waking Sands he worked to rebuild the Scions, and he sees their cause as the dream of his grandfather, who gave his life for the realm.",
     ["C10", "C42", "C25", "C38", "C43"]),
   P(B, None, "main", "Alphinaud",
     "A young Scion and Alisaie's twin brother. He founded the Crystal Braves to serve all of Eorzea rather than any one nation, and commanded them. "
     "At the royal banquet in Ul'dah the Braves turned on him. He escaped, and now blames himself for treating the Braves and even the Scions as pawns in his plans.",
     ["C10", "C48", "C16", "C52", "C52b"]),
 ]),
 ("char-alisaie", "character", [
   P(A, B, "main", "Alisaie",
     "Alphinaud's twin sister. She doubts her brother's approach and has set out to find her own way to heal the realm's troubles. "
     "Alphinaud says that although she walks her own path, the twins share the same goal.",
     ["C10", "C42", "C11"]),
   P(A, B, "optional", "Alisaie",
     "Alphinaud's twin sister, a young Scion who walks her own path apart from her brother. "
     "She is investigating the Binding Coil of Bahamut, where she believes she saw her grandfather, Louisoix, who is presumed to have died sealing the primal away.",
     ["C10", "C11", "C30", "C13", "C58"]),
   P(B, None, "main", "Alisaie",
     "Alphinaud's twin sister, who walks her own path. She stayed on at the Waking Sands to work with Urianger when the Scions moved to Mor Dhona, and she was not among them at the royal banquet in Ul'dah. "
     "Alphinaud believes she was watching over him during his escape.",
     ["C10", "C11", "C45", "C23"]),
   P(B, None, "optional", "Alisaie",
     "Alphinaud's twin sister, a young Scion who walks her own path. She learned that the figure she saw in the Binding Coil was only an aetherial shadow of her grandfather, Louisoix, bound to Bahamut. "
     "With your help his soul was freed, and she now means to find her own reason to fight for Eorzea. "
     "She was not among the Scions at the royal banquet in Ul'dah, and Alphinaud believes she was watching over him during his escape.",
     ["C10", "C30", "C56", "C28", "C57", "C23"]),
 ]),
 ("char-louisoix", "character", [
   P(A, B, "main", "Louisoix",
     "A revered Archon and man of learning. He never returned from the Battle of Carteneau, and the realm's leaders lament the loss of his wisdom. "
     "The Scions still speak of his guidance.",
     ["C44", "C44b", "C44c"], ["Archon Louisoix", "Master Louisoix"]),
   P(A, B, "optional", "Louisoix",
     "A revered Archon and man of learning, and Alisaie's grandfather. He never returned from the Battle of Carteneau and is presumed dead, having apparently sealed the primal Bahamut away there. "
     "Alisaie believes she has seen him alive within the Binding Coil.",
     ["C44", "C13", "C27", "C58"], ["Archon Louisoix", "Master Louisoix"]),
   P(B, None, "main", "Louisoix",
     "A Sharlayan sage who founded the Circle of Knowing in the face of fierce opposition and came to Eorzea. Urianger studied under him. "
     "His sacrifice during the Calamity spared the realm, and the Scions still hold to his teachings.",
     ["C54", "C55"], ["Archon Louisoix", "Master Louisoix"]),
   P(B, None, "optional", "Louisoix",
     "A Sharlayan sage, the twins' grandfather, who founded the Circle of Knowing and came to Eorzea. His sacrifice during the Calamity spared the realm, apparently sealing Bahamut away. "
     "The figure Alisaie saw in the Binding Coil was an aetherial shadow of him bound to the primal, and you freed his soul.",
     ["C54", "C26", "C13", "C27", "C56", "C28"], ["Archon Louisoix", "Master Louisoix"]),
 ]),
 ("char-tataru", "character", [
   P(A, B, "main", "Tataru",
     "The Scions' clerk, who greets visitors at the Waking Sands and keeps the order running smoothly. "
     "She was among those taken prisoner in the imperial raid, and was freed in the rescue at Castrum Centri.",
     ["C32", "C36", "C37"]),
   P(B, None, "main", "Tataru",
     "The Scions' receptionist, who followed them to their new headquarters at the Rising Stones. She briefly left to train as an arcanist so that she could protect others, but gave it up. "
     "After the royal banquet in Ul'dah, Crystal Braves turned on her; Yugiri rescued her, and she sheltered at the glamoured Waking Sands before rejoining you.",
     ["C15", "C47", "C47b", "C20", "C53", "C21"]),
 ]),
 ("org-scions", "organization", [
   P(A, B, "main", "The Scions of the Seventh Dawn",
     "An order that stands apart from the city-states' politics, devoted to preserving Eorzea's future. Minfilia leads it from the Waking Sands in Vesper Bay, and its members include Sharlayans who stayed in Eorzea when their countrymen fled. "
     "An imperial raid devastated the order and took several members prisoner, but the Scions rescued them and rebuilt.",
     ["C34", "C01", "C02", "C31", "C06", "C36", "C38"]),
   P(B, None, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. It moved its headquarters to the Rising Stones in Mor Dhona. "
     "At a royal banquet in Ul'dah, its members were accused of plotting to poison the sultana and branded fugitives, and its own Crystal Braves turned on it. "
     "Most of those who attended are unaccounted for, and the few who escaped regroup in Coerthas.",
     ["C14", "C15", "C50", "C19", "C20", "C22", "C24"]),
 ]),
 ("org-crystal-braves", "organization", [
   P(B, None, "main", "The Crystal Braves",
     "A company Alphinaud founded under the Scions, recruiting fighters who serve no single nation, for the sake of a united Eorzea. "
     "Alphinaud commanded it, with Captain Ilberd as his second-in-command. At the royal banquet in Ul'dah the Braves turned on the Scions: they detained the Scions' allies, seized the Rising Stones and hunted the fugitives.",
     ["C48", "C16", "C19", "C20"]),
 ]),
 ("loc-waking-sands", "location", [
   P(A, B, "main", "The Waking Sands",
     "The Scions' headquarters in Vesper Bay, in western Thanalan, where Minfilia receives visitors. "
     "Imperial forces raided it and took prisoners, and the Scions later restored it.",
     ["C02", "C06", "C38"]),
   P(B, None, "main", "The Waking Sands",
     "The Scions' former headquarters in Vesper Bay. When they moved to the Rising Stones it passed into Urianger's care. "
     "After the royal banquet in Ul'dah, Urianger hid it behind a glamour that makes it look like an abandoned storehouse, and it now shelters those fleeing the Crystal Braves.",
     ["C45", "C21", "C53"]),
 ]),
 ("loc-rising-stones", "location", [
   P(B, None, "main", "The Rising Stones",
     "The Scions' headquarters in Revenant's Toll, Mor Dhona, entered through the Seventh Heaven. They moved there from the Waking Sands. "
     "After the royal banquet in Ul'dah, the Crystal Braves took control of it, and now only Braves remain there.",
     ["C14", "C15", "C19", "C19b"]),
 ]),
]

TYPES = [
 ("leads", "leads", "led by", False),
 ("member-of", "member of", "has member", False),
 ("twin-of", "twin of", "twin of", True),
 ("grandchild-of", "grandchild of", "grandparent of", False),
 ("headquartered-at", "headquartered at", "headquarters of", False),
 ("controls", "controls", "controlled by", False),
 ("turned-against", "turned against", "betrayed by", False),
 ("conceals", "conceals", "concealed by", False),
]

RELS = [
 ("rel-minfilia-leads-scions", "char-minfilia", "leads", "org-scions", A, None, "main", ["C01"], "R01"),
 ("rel-thancred-member-scions", "char-thancred", "member-of", "org-scions", A, None, "main", ["C31"], "R02"),
 ("rel-yshtola-member-scions", "char-yshtola", "member-of", "org-scions", A, None, "main", ["C31", "C40"], "R03"),
 ("rel-urianger-member-scions", "char-urianger", "member-of", "org-scions", A, None, "main", ["C31", "C36"], "R04"),
 ("rel-alphinaud-member-scions", "char-alphinaud", "member-of", "org-scions", A, None, "main", ["C25"], "R05"),
 ("rel-tataru-member-scions", "char-tataru", "member-of", "org-scions", A, None, "main", ["C32", "C36"], "R06"),
 ("rel-alphinaud-twin-alisaie", "char-alphinaud", "twin-of", "char-alisaie", A, None, "main", ["C10"], "R07"),
 ("rel-scions-hq-waking-sands", "org-scions", "headquartered-at", "loc-waking-sands", A, B, "main", ["C02"], "R08"),
 ("rel-braves-control-rising-stones", "org-crystal-braves", "controls", "loc-rising-stones", B, None, "main", ["C19", "C19b"], "R09"),
 ("rel-braves-turned-against-scions", "org-crystal-braves", "turned-against", "org-scions", B, None, "main", ["C19", "C20"], "R10"),
 ("rel-urianger-conceals-waking-sands", "char-urianger", "conceals", "loc-waking-sands", B, None, "main", ["C21"], "R11"),
 ("rel-alisaie-grandchild-louisoix", "char-alisaie", "grandchild-of", "char-louisoix", A, None, "optional", ["C13"], "R12"),
 ("rel-alphinaud-grandchild-louisoix", "char-alphinaud", "grandchild-of", "char-louisoix", B, None, "optional", ["C26", "C13"], "R13"),
 ("rel-alisaie-member-scions", "char-alisaie", "member-of", "org-scions", A, None, "optional", ["C30"], "R14"),
]

# ==== Arc A4: The Black Wolf's Challenge (NDL-009) ===============================================================
# MSQ #155–161, baseline #154. Researched 2026-11-14 from raw Console Games Wiki wikitext (lanes A–C); every locator is
# checked verbatim against the saved pages. Cast (user decision, 2026-11-14): Minfilia, Thancred, Alphinaud and the
# Scions, plus Cid, Gaius, Livia, Lahabrea and the Eorzean Alliance, plus the Operation Archon event; the caps were
# raised by one each (5 new entities, 4 new relationship types). First names only; "Garlond Ironworks" is shown as
# "the Ironworks". Q1..Q7 below are the slice steps.
Q154, Q155, Q156, Q157, Q158, Q159, Q160 = (cid for cid, _, _, _ in SLICE)
for k, p in [("Come-Into-My-Castrum", None), ("Lady of the Vortex", None), ("In Pursuit of the Past", None), ("Lord of Crags", None),
             ("Every Little Thing She Does Is Magitek", None), ("The Black Wolf's Ultimatum", None), ("Operation Archon", None),
             ("A Hero in Need", None), ("Hearts on Fire", None), ("Rock the Castrum", None)]:
    src(k, p or k, "2.0")

C.update({
 # ---- Before the arc (known by #154) ----
 "K01": ("Imperial forces led by Livia raid the Waking Sands, refuse Minfilia's surrender and take her prisoner.", "All Good Things", "Conditions of surrender...denied. … We leave! Bring the prisoners."),
 "K02": ("Livia wants Minfilia for the Echo.", "All Good Things", "They say she also possesses the Echo. I cannot wait to hear her scream."),
 "K03": ("Minfilia and the other captured Scions are held at Castrum Centri.", "Come-Into-My-Castrum", "All evidence suggests that Minfilia and the others are being held captive at [[Castrum Centri]]."),
 "K04": ("Cid prepares a plan to rescue the captive Scions.", "Come-Into-My-Castrum", "wants to prepare a strategy to rescue"),
 "K05": ("Alphinaud seeks out Cid as the greatest engineer of the age.", "Eyes on Me", "I have come in search of a legend─the greatest engineer of our time."),
 "K06": ("Cid has an airship of his own.", "Eyes on Me", "Yes, Cid, you do. Your very own airship."),
 "K07": ("Cid was born in Garlemald, left the Empire and came to Eorzea, where he built the Ironworks.", "Lady of the Vortex", "Born and raised in Garlemald... … left the Empire behind and came to Eorzea, where I built the Ironworks."),
 "K08": ("Gaius knows Cid, and reproaches him for forsaking kin and country.", "Lady of the Vortex", "Ah, Cid, my boy. You look well─for one who has forsaken ''kin'' and country."),
 "K09": ("Cid's crew restores a suit of magitek armor, and the time comes to infiltrate Castrum Centri and rescue the Scions.", "Every Little Thing She Does Is Magitek", "you are now the proud owner of a fully functional suit of magitek armor. … At long last, the time is come to infiltrate [[Castrum Centri]] and rescue the imprisoned [[Scions]]."),
 "K10": ("Gaius, the Black Wolf, is legatus of the XIVth Imperial Legion and commands the Garlean invasion of Eorzea.", "Lady of the Vortex", "legatus of the XIVth Imperial Legion, and supreme commander of the Garlean invasion force in Eorzea. … Of course, the Black Wolf─how could I not realize?"),
 "K11": ("The Black Wolf calls forth an imperial weapon that overpowers and seemingly absorbs three primals.", "Lady of the Vortex", "the Black Wolf calls forth an unknown imperial weapon which summarily dispatches and seemingly absorbs all three primals."),
 "K12": ("Gaius means to purge Eorzea of its gods.", "Casing the Castrum", "At last, we have the power to purge this land of its false gods."),
 "K13": ("Lahabrea is an Ascian.", "In Pursuit of the Past", "the [[Ascian]] uses his magicks to awaken the dragon"),
 "K14": ("The Ascians are elusive, and Y'shtola is troubled that they would consort with the Empire.", "Lord of Crags", "Well, the Ascians are nothing if not elusive. … But that they would choose to consort with the ''Empire''..."),
 "K15": ("Lahabrea marvels as the weapon grows stronger with each primal it consumes.", "Lady of the Vortex", "With each primal it consumes, it grows more powerful. A marvel, is it not?"),
 "K16": ("Alphinaud means to rebuild the Scions.", "Reclamation", "It is up to us to rebuild the Scions and save Eorzea."),
 "K17": ("The Scions were taken prisoner by the Empire, and the order must be reborn.", "Reclamation", "[[the Scions]] taken prisoner by the Empire. … [[the Scions of the Seventh Dawn]] must be reborn."),
 # ---- #155 Escape from Castrum Centri ----
 "K20": ("The rescue party frees the captives held in Castrum Centri's storage tower.", "Escape from Castrum Centri", "and the others are being held within the storage tower. … Though the rescue mission was a success"),
 "K21": ("Cid and Alphinaud create a diversion outside the castrum.", "Escape from Castrum Centri", "Alphinaud and I will create a diversion out here and keep them occupied for as long as we are able."),
 "K22": ("Livia, the tribunus, captured the Scions and means to study Minfilia's Echo.", "Escape from Castrum Centri", "captured by the tribunus herself! … This “Echo” of yours intrigues us."),
 "K23": ("The Empire has finished the Ultima Weapon, an Allagan relic excavated beneath Ala Mhigo.", "Escape from Castrum Centri", "They finished it. Ultima Weapon... … It is a relic of ancient Allag, excavated from its resting place deep beneath Ala Mhigo."),
 "K24": ("Lahabrea stands beside the Black Wolf.", "Escape from Castrum Centri", "Look! There, beside the Black Wolf!"),
 "K25": ("Gaius demands the realm submit to his power; resistance means sharing the primals' fate.", "Escape from Castrum Centri", "This realm founders for want of a ruler with true power─the power to cast down eikons. … Yet offer resistance, and he swears that we shall share the primals' fate."),
 "K26": ("The Alliance leaders had believed the Scions dead or missing, and now weigh the Black Wolf's ultimatum.", "Escape from Castrum Centri", "The Alliance leaders staked their hopes on the Scions, but now they believe us all dead or missing. … I believe we are all acquainted with the terms of the Black Wolf's ultimatum."),
 # ---- #156 The Black Wolf's Ultimatum ----
 "K30": ("Eorzea's leaders resolve to fight, and burn the ultimatum.", "The Black Wolf's Ultimatum", "Eorzea's leaders have resolved to fight … The city-state leaders burn the ultimatum."),
 "K31": ("Minfilia argues that the Black Wolf's offer would doom Eorzea.", "The Black Wolf's Ultimatum", "That which the Black Wolf offers will doom Eorzea, not deliver it"),
 "K32": ("Ascians are immortal beings without physical form who possess mortals through Crystals of Darkness.", "The Black Wolf's Ultimatum", "the Ascians are immortal beings without physical form. … malign artifacts known as Crystals of Darkness."),
 "K33": ("Destroying the Crystal that binds Thancred, somewhere on his person, may save him.", "The Black Wolf's Ultimatum", "The Crystal that binds Thancred must be somewhere on his person. … One such Crystal may yet be the key to saving Thancred."),
 "K34": ("Cid is asked to be the Alliance's man in Ul'dah.", "The Black Wolf's Ultimatum", "Cid, would you be our man in Ul'dah?"),
 "K35": ("The Scions vow to keep fighting.", "The Black Wolf's Ultimatum", "Come what may, we Scions will never give up the fight."),
 "K36": ("Gridania goes to war, and the Maelstrom will secure the Lominsan coast.", "The Black Wolf's Ultimatum", "Gridania will go to war. … The Maelstrom will secure strategic points along the coastline."),
 # ---- #157 Operation Archon ----
 "K40": ("Operation Archon is the Eorzean Alliance's eleventh-hour bid to drive out the Empire.", "Operation Archon", "So begins Operation Archon, the Eorzean Alliance's eleventh-hour bid to purge the realm of the imperial menace."),
 "K41": ("It is the largest counteroffensive in the realm's history; its last phase is to destroy the Ultima Weapon in the Praetorium.", "Operation Archon", "the largest single counteroffensive in the realm's troubled history … where they will locate and destroy the Ultima Weapon."),
 "K42": ("You lead the first phase and slay Rhitahtyn, one of the Black Wolf's most trusted lieutenants.", "Operation Archon", "The first shall see us eliminate one of the Black Wolf's most trusted lieutenants … you deal Rhitahtyn his death-blow"),
 "K43": ("Minfilia, Cid and Alphinaud advise the main host, and the other Scions go with their Grand Companies.", "Operation Archon", "Minfilia, Cid, and I shall accompany the main host in an advisory capacity. … pray accompany your respective organizations on their missions."),
 "K44": ("The Maelstrom and the Order of the Twin Adder move against imperial castra.", "Operation Archon", "the Maelstrom moves to blockade Castrum Occidens and Castrum Marinum. … the Order of the Twin Adder advances upon Castrum Oriens."),
 "K45": ("In Gaius's war council, Livia mourns Rhitahtyn, and Gaius orders his tribuni to crush the resistance.", "Operation Archon", "Rhitahtyn... … We shall crush them as we crushed the eikons! … Yes, my lord!"),
 # ---- #158 A Hero in Need ----
 "K50": ("Phase two is under way: the Immortal Flames will strike Castrum Meridianum as a diversion while you bring down the magitek field around the Praetorium.", "A Hero in Need", "Phase two of the operation is presently in motion. … The Immortal Flames shall strike at Castrum Meridianum by way of a diversionary maneuver. … you are to infiltrate the stronghold and bring down the magitek field that surrounds the Praetorium."),
 "K51": ("The Alliance troops at Camp Bluefog are in low spirits before what may be the bloodiest battle in history.", "A Hero in Need", "the Alliance garrison at [[Camp Bluefog]] is in low spirits and would be better for a hero's visit. … the bloodiest battle in history"),
 # ---- #159 Hearts on Fire ----
 "K55": ("You help General Raubahn rally the garrison at the Ceruleum Processing Plant.", "Hearts on Fire", "Raubahn bids you rally the garrison at the Ceruleum Processing Plant. … the entire garrison is fairly ablaze with determination."),
 # ---- #160 Rock the Castrum ----
 "K60": ("Phase two succeeds: Castrum Occidens and Castrum Marinum are under blockade.", "Rock the Castrum", "Phase two of Operation Archon is a success! … Castrum Occidens and Castrum Marinum are now under blockade!"),
 "K61": ("While you create a diversion, Cid finds the generator, and the magitek field comes down.", "Rock the Castrum", "If you could create a diversion─that's to say, wreak lots of havoc─I'll search for the field generator. … we've succeeded in bringing down the generator tower─and with it, the magitek field!"),
 "K62": ("Livia, devoted to Gaius, fights you and dies.", "Rock the Castrum", "My minions, my comrades...even my lord Gaius! … Another poor fool who craved Gaius's affection over all else... May her soul know rest."),
 "K63": ("Only the Enterprise can reach the Praetorium, and all that remains is to destroy the Ultima Weapon.", "Rock the Castrum", "Nay, we'll need to take the ''Enterprise''. … All that remains is the small matter of finding and destroying the Ultima Weapon."),
 # ---- #161 The Ultimate Weapon (milestone cp-arr-2-0) ----
 "K70": ("Gaius asks Cid to take up his father's mantle as the Empire's lead engineer, and Cid refuses.", "The Ultimate Weapon", "Take up your father's mantle, and become the Empire's lead engineer. … I have long known my destiny, and I assure you, it lies ''not'' with the Empire!"),
 "K71": ("The Black Wolf turns the Ultima Weapon on you, and you lay it low.", "The Ultimate Weapon", "Taking control of the fearsome weapon, the Black Wolf sets upon you once more. … you weather the Ultima Weapon's relentless onslaught and succeed in laying it low."),
 "K72": ("Lahabrea quickened the weapon's core with the primals' life force, then comes to eliminate you himself.", "The Ultimate Weapon", "I sought the life force of the primals for no other reason but to quicken the core. … now intends to eliminate you himself,"),
 "K73": ("Gaius is slain and the Ultima Weapon destroyed.", "The Ultimate Weapon", "slain, and the Ultima Weapon destroyed,"),
 "K74": ("The Crystal that bound Thancred is no more.", "The Ultimate Weapon", "Though the Crystal that bound Thancred is no more"),
 "K75": ("Eorzea's leaders proclaim the Seventh Astral Era and announce that their Grand Companies will be joined.", "The Ultimate Weapon", "The Seventh Astral Era is come! … So too shall our Grand Companies be joined henceforth,"),
})

ARC = "evt-black-wolfs-challenge"
ARCHON = "evt-operation-archon"

# Slice-era presentations for entities the pilot already covers from cp-arr-2-0. Fresh research; the accepted 2.0
# summaries narrate the whole arc, so none is reused (v2 plan, "Fresh research").
ARC_PRES = {
 "char-minfilia": [
   P(Q154, Q155, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. When imperial forces under Livia raided the Waking Sands, they refused her surrender and took her prisoner. "
     "She and other captured Scions are held at Castrum Centri, and the Empire wants her for the Echo. Cid's crew is ready to break in and rescue them.",
     ["C01", "C33", "K01", "K02", "K03", "K09"]),
   P(Q155, Q156, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn, who has the Echo. She was freed from Castrum Centri's storage tower in the rescue, but during the escape the Scions learned that Thancred has been possessed by the Ascian Lahabrea.",
     ["C01", "C33", "K20", "C37"]),
   P(Q156, A, "main", "Minfilia",
     "Leader of the Scions of the Seventh Dawn. She urged Eorzea's leaders to reject the Black Wolf's ultimatum, warning that his offer would doom the realm rather than deliver it, and they resolved to fight. "
     "She believes destroying the Crystal of Darkness on Thancred's person may free him from the Ascian who possesses him.",
     ["C01", "K31", "K30", "K33"]),
 ],
 "char-thancred": [
   P(Q154, Q155, "main", "Thancred",
     "A Scion who serves as the order's man in Ul'dah, and who briefed your first investigation.",
     ["C31", "C39"]),
   P(Q155, Q156, "main", "Thancred",
     "A Scion who serves as the order's man in Ul'dah. During the rescue at Castrum Centri, the Scions discovered that the Ascian Lahabrea has possessed him.",
     ["C31", "C39", "C37"]),
   P(Q156, A, "main", "Thancred",
     "A Scion who serves as the order's man in Ul'dah, now in the thrall of the Ascian Lahabrea. Ascians possess mortals through Crystals of Darkness, and Minfilia believes destroying the Crystal on his person may save him.",
     ["C31", "C37", "K32", "K33"]),
 ],
 "char-alphinaud": [
   P(Q154, Q157, "main", "Alphinaud",
     "A young Scion who stands against the primals and the Empire, as his grandfather once did. Since the raid on the Waking Sands he has worked to rebuild the Scions, and he sought out Cid, the greatest engineer of the age, to help.",
     ["C25", "K16", "K05"]),
   P(Q157, A, "main", "Alphinaud",
     "A young Scion who stands against the primals and the Empire, as his grandfather once did. He briefed you on Operation Archon, the Alliance's great counteroffensive, and advises its main host alongside Minfilia and Cid.",
     ["C25", "K41", "K43"]),
 ],
 "org-scions": [
   P(Q154, Q155, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. Imperial forces raided its headquarters at the Waking Sands and took members prisoner, Minfilia among them. "
     "Alphinaud means to rebuild the order, and its free members are working with Cid to rescue the captives from Castrum Centri.",
     ["C34", "C01", "C06", "K17", "K16", "K04"]),
   P(Q155, Q157, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. Its captured members were freed from Castrum Centri, though Thancred was found to be possessed by the Ascian Lahabrea. "
     "Eorzea's leaders had believed the Scions dead or missing.",
     ["C34", "C01", "K20", "C37", "K26"]),
   P(Q157, A, "main", "The Scions of the Seventh Dawn",
     "An order devoted to preserving Eorzea's future, led by Minfilia. It stands with the Eorzean Alliance in Operation Archon: Minfilia and Alphinaud advise the main host, and the other Scions go with their Grand Companies.",
     ["C34", "C01", "K40", "K43"]),
 ],
}
ENT = [(eid, cat, ARC_PRES.get(eid, []) + pres) for eid, cat, pres in ENT]

ENT += [
 (ARC, "event", [
   P(Q155, Q156, "main", "The Black Wolf's Challenge",
     "You and Cid's crew broke into Castrum Centri and freed Minfilia and the captive Scions, but the escape revealed that the Ascian Lahabrea has possessed Thancred. "
     "The Empire has finished the Ultima Weapon, an ancient Allagan relic, and Gaius, the Black Wolf, has given Eorzea's leaders an ultimatum: submit to his power, or share the primals' fate.",
     ["K20", "K21", "C37", "K23", "K25", "K26"]),
   P(Q156, Q157, "main", "The Black Wolf's Challenge",
     "Eorzea's leaders refused the Black Wolf's ultimatum and resolved to fight, with the Scions beside them. "
     "Thancred remains in the thrall of the Ascian Lahabrea; Minfilia believes destroying the Crystal of Darkness on his person may free him. "
     "The Empire still holds the Ultima Weapon, and Cid now serves as the Alliance's man in Ul'dah.",
     ["K30", "K31", "K33", "K23", "K34"]),
   P(Q157, Q158, "main", "The Black Wolf's Challenge",
     "The Eorzean Alliance has launched Operation Archon, the largest counteroffensive in the realm's history. "
     "You led its first phase and slew Rhitahtyn, one of the Black Wolf's most trusted lieutenants, and the Maelstrom and the Order of the Twin Adder now move on imperial castra. "
     "The final aim is the Praetorium, where the Ultima Weapon is believed to be housed. Thancred is still possessed.",
     ["K40", "K41", "K42", "K44", "C37"]),
   P(Q158, Q159, "main", "The Black Wolf's Challenge",
     "Operation Archon's second phase is under way. While the Immortal Flames strike Castrum Meridianum as a diversion, your task is to slip inside and bring down the magitek field around the Praetorium, where the Ultima Weapon waits. "
     "First you raised the spirits of the Alliance troops at Camp Bluefog, who dread what may be the bloodiest battle in history.",
     ["K50", "K41", "K51"]),
   P(Q159, Q160, "main", "The Black Wolf's Challenge",
     "With the assault on Castrum Meridianum close, you helped General Raubahn rally the wavering garrison at the Ceruleum Processing Plant. "
     "The plan holds: while the Alliance strikes outside, you are to infiltrate the castrum and bring down the magitek field that shields the Praetorium and the Ultima Weapon. "
     "Thancred remains in the Ascian Lahabrea's thrall.",
     ["K55", "K50", "K41", "C37"]),
   P(Q160, A, "main", "The Black Wolf's Challenge",
     "You broke into Castrum Meridianum and, with Cid guiding you, brought down the magitek field around the Praetorium. "
     "Livia, the tribunus who captured the Scions, fought you and fell. "
     "The Praetorium can now be reached only aboard Cid's airship, the Enterprise, and what remains is to find and destroy the Ultima Weapon. Thancred is still possessed.",
     ["K61", "K22", "K62", "K63", "C37"]),
   P(A, None, "main", "The Black Wolf's Challenge",
     "Aboard the Enterprise you stormed the Praetorium. Gaius urged Cid to take up his father's mantle in the Empire, and Cid refused. "
     "The Black Wolf turned the Ultima Weapon on you and you laid it low; then the Ascian Lahabrea, who had quickened the weapon with the primals' life force, came for you himself, and you freed Thancred from his enthrallment. "
     "Gaius is slain and the Ultima Weapon destroyed.",
     ["K70", "K71", "K72", "C09", "K73"]),
 ]),
 (ARCHON, "event", [
   P(Q157, Q160, "main", "Operation Archon",
     "The Eorzean Alliance's eleventh-hour bid to drive the Empire from the realm: the largest counteroffensive in its history, in four phases, ending with the destruction of the Ultima Weapon in the Praetorium of Castrum Meridianum. "
     "You led the first phase and slew Rhitahtyn, and the Maelstrom and the Order of the Twin Adder move against imperial castra. The Scions and Cid stand with the Alliance.",
     ["K40", "K41", "K42", "K44", "K43"]),
   P(Q160, A, "main", "Operation Archon",
     "The Eorzean Alliance's eleventh-hour bid to drive the Empire from the realm, in four phases. You slew Rhitahtyn in the first, the Maelstrom blockaded Castrum Occidens and Castrum Marinum in the second, "
     "and in the third you and Cid brought down the magitek field around the Praetorium. The last phase is to destroy the Ultima Weapon within.",
     ["K40", "K42", "K60", "K61", "K63"]),
   P(A, None, "main", "Operation Archon",
     "The Eorzean Alliance's eleventh-hour counteroffensive against the Empire, the largest in the realm's history. "
     "It ran from the death of Rhitahtyn at Cape Westwind to the Praetorium of Castrum Meridianum, where Gaius was slain and the Ultima Weapon destroyed.",
     ["K40", "K41", "K42", "K73"]),
 ]),
 ("char-cid", "character", [
   P(Q154, Q155, "main", "Cid",
     "A brilliant engineer, born and raised in Garlemald, who left the Empire for Eorzea and built the Ironworks. He has an airship of his own. "
     "Gaius knows him and scorns him for forsaking kin and country. With his crew he restored a suit of magitek armor to break into Castrum Centri and rescue the captive Scions.",
     ["K05", "K06", "K07", "K08", "K04", "K09"]),
   P(Q155, Q156, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. He planned the rescue at Castrum Centri, and he and Alphinaud drew off the guards while the captive Scions were freed.",
     ["K05", "K07", "K21", "K20"]),
   P(Q156, Q157, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. After the rescue at Castrum Centri, the Alliance asked him to be its man in Ul'dah.",
     ["K05", "K07", "K34"]),
   P(Q157, Q160, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. The Alliance asked him to be its man in Ul'dah, and he advises the main host of Operation Archon alongside Minfilia and Alphinaud.",
     ["K05", "K07", "K34", "K43"]),
   P(Q160, A, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. In the assault on Castrum Meridianum he found the field generator and brought down the magitek field while you created a diversion, "
     "and only his airship, the Enterprise, can now reach the Praetorium.",
     ["K05", "K07", "K61", "K63"]),
   P(A, None, "main", "Cid",
     "A brilliant engineer from Garlemald who left the Empire and built the Ironworks. He flew you into the Praetorium aboard his airship, the Enterprise, "
     "where Gaius urged him to take up his father's mantle as the Empire's lead engineer, and he refused.",
     ["K05", "K07", "K63", "K70"]),
 ]),
 ("char-gaius", "character", [
   P(Q154, Q155, "main", "Gaius",
     "The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. "
     "He called forth an imperial weapon that overpowered and seemingly absorbed three primals, and he means to purge the land of its false gods.",
     ["K10", "K11", "K12"], ["the Black Wolf"]),
   P(Q155, Q157, "main", "Gaius",
     "The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. "
     "The Empire has finished the Ultima Weapon, an ancient Allagan relic, and he demands that the realm submit to his power or share the primals' fate. The Ascian Lahabrea stands beside him.",
     ["K10", "K23", "K25", "K24"], ["the Black Wolf"]),
   P(Q157, A, "main", "Gaius",
     "The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. Eorzea's leaders rejected his ultimatum, "
     "and when Operation Archon claimed his trusted lieutenant Rhitahtyn, he ordered his tribuni to crush the resistance. He holds the Ultima Weapon.",
     ["K10", "K30", "K42", "K45", "K23"], ["the Black Wolf"]),
   P(A, None, "main", "Gaius",
     "The Black Wolf: legatus of the XIVth Imperial Legion and supreme commander of the Garlean invasion of Eorzea. "
     "In the Praetorium he urged Cid to join the Empire and turned the Ultima Weapon on you. He was slain, and the weapon destroyed.",
     ["K10", "K70", "K71", "K73"], ["the Black Wolf"]),
 ]),
 ("char-livia", "character", [
   P(Q154, Q155, "main", "Livia",
     "An imperial officer who led the raid on the Waking Sands. She refused Minfilia's surrender, took her prisoner, and is eager to learn about the Echo.",
     ["K01", "K02"]),
   P(Q155, Q157, "main", "Livia",
     "An imperial tribunus who captured the Scions in the raid on the Waking Sands and means to study Minfilia's Echo. The captives escaped her at Castrum Centri.",
     ["K22", "K01", "K20"]),
   P(Q157, Q160, "main", "Livia",
     "An imperial tribunus who captured the Scions in the raid on the Waking Sands. She stands in Gaius's war council, and mourned Rhitahtyn when Operation Archon claimed him.",
     ["K22", "K01", "K45"]),
   P(Q160, None, "main", "Livia",
     "An imperial tribunus who captured the Scions in the raid on the Waking Sands. Utterly devoted to Gaius, she fought you in Castrum Meridianum and died.",
     ["K22", "K01", "K62"]),
 ]),
 ("char-lahabrea", "character", [
   P(Q154, Q155, "main", "Lahabrea",
     "An Ascian, one of an elusive kind that the Scions are troubled to find consorting with the Empire. He marveled as the Empire's weapon grew stronger with each primal it consumed.",
     ["K13", "K14", "K15"]),
   P(Q155, Q156, "main", "Lahabrea",
     "An Ascian who stands beside the Black Wolf. During the rescue at Castrum Centri, the Scions discovered that he has possessed Thancred.",
     ["K13", "K24", "C37"]),
   P(Q156, A, "main", "Lahabrea",
     "An Ascian who stands beside the Black Wolf and has possessed Thancred. Ascians are immortal beings without physical form who possess mortals through Crystals of Darkness.",
     ["K24", "C37", "K32"]),
   P(A, None, "main", "Lahabrea",
     "An Ascian. He quickened the Ultima Weapon's core with the life force of the primals it absorbed, and when the weapon fell he came for you himself. You freed Thancred, whom he had possessed.",
     ["K72", "C09", "K74"]),
 ]),
 ("org-eorzean-alliance", "organization", [
   P(Q155, Q156, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. Its leaders had staked their hopes on the Scions and believed them dead or missing, and they are weighing the Black Wolf's ultimatum.",
     ["K26"]),
   P(Q156, Q157, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. Its leaders rejected the Black Wolf's ultimatum and resolved to fight: Gridania goes to war, and the Maelstrom will secure the Lominsan coast. "
     "They asked Cid to be the Alliance's man in Ul'dah.",
     ["K30", "K36", "K34"]),
   P(Q157, A, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states, now waging Operation Archon, its eleventh-hour counteroffensive to drive the Empire from the realm.",
     ["K40", "K41"]),
   P(A, None, "main", "The Eorzean Alliance",
     "The alliance of Eorzea's city-states. Its Operation Archon carried the fight to the Praetorium, where Gaius was slain and the Ultima Weapon destroyed. "
     "Its leaders proclaimed the Seventh Astral Era and announced that their Grand Companies will be joined.",
     ["K40", "K73", "K75"]),
 ]),
]

TYPES += [
 ("participant-in", "part of", "involves", False),
 ("prisoner-of", "prisoner of", "holds prisoner", False),
 ("possessed-by", "possessed by", "possesses", False),
 ("serves", "serves", "served by", False),
]

RELS += [
 # Baseline backfill (v2 plan, "Baseline rule"): the same triples as accepted R01, R02 and R05, before cp-arr-2-0.
 ("rel-minfilia-leads-scions-a4", "char-minfilia", "leads", "org-scions", Q154, A, "main", ["C01"], "R15"),
 ("rel-thancred-member-scions-a4", "char-thancred", "member-of", "org-scions", Q154, A, "main", ["C31"], "R16"),
 ("rel-alphinaud-member-scions-a4", "char-alphinaud", "member-of", "org-scions", Q154, A, "main", ["C25"], "R17"),
 # Arc relationships.
 ("rel-minfilia-prisoner-livia", "char-minfilia", "prisoner-of", "char-livia", Q154, Q155, "main", ["K01", "K03"], "R18", ["K20"]),
 ("rel-thancred-possessed-lahabrea", "char-thancred", "possessed-by", "char-lahabrea", Q155, A, "main", ["C37"], "R19"),
 ("rel-livia-serves-gaius", "char-livia", "serves", "char-gaius", Q157, Q160, "main", ["K45"], "R20", ["K62"]),
 ("rel-alliance-in-archon", "org-eorzean-alliance", "participant-in", ARCHON, Q157, None, "main", ["K40"], "R21"),
 ("rel-scions-in-archon", "org-scions", "participant-in", ARCHON, Q157, None, "main", ["K43"], "R22"),
 ("rel-cid-in-archon", "char-cid", "participant-in", ARCHON, Q157, None, "main", ["K43"], "R23"),
 # The arc's cast: each member's participant-in edge to the arc entry, from the step they enter it.
 ("p-minfilia-a4", "char-minfilia", "participant-in", ARC, Q155, None, "main", ["K20"], "P1"),
 ("p-thancred-a4", "char-thancred", "participant-in", ARC, Q155, None, "main", ["C37"], "P2"),
 ("p-alphinaud-a4", "char-alphinaud", "participant-in", ARC, Q155, None, "main", ["K21"], "P3"),
 ("p-scions-a4", "org-scions", "participant-in", ARC, Q155, None, "main", ["K20"], "P4"),
 ("p-cid-a4", "char-cid", "participant-in", ARC, Q155, None, "main", ["K21"], "P5"),
 ("p-gaius-a4", "char-gaius", "participant-in", ARC, Q155, None, "main", ["K25"], "P6"),
 ("p-livia-a4", "char-livia", "participant-in", ARC, Q155, None, "main", ["K22"], "P7"),
 ("p-lahabrea-a4", "char-lahabrea", "participant-in", ARC, Q155, None, "main", ["C37"], "P8"),
 ("p-alliance-a4", "org-eorzean-alliance", "participant-in", ARC, Q155, None, "main", ["K26"], "P9"),
 ("p-archon-a4", ARCHON, "participant-in", ARC, Q157, None, "main", ["K40"], "P10"),
]

# Arcs (schema v2): (arc id, arc entry event id, first step, last step), in authored order.
ARCS = [("arc-a4-black-wolf", ARC, Q155, A)]
ARC_NOTES = {"arc-a4-black-wolf": "MSQ #155 *Escape from Castrum Centri* to #161 *The Ultimate Weapon* (the `cp-arr-2-0` milestone), with #154 as the baseline. "
             "It opens with the rescue that frees the Scions and reveals Thancred's possession (K20, C37), and runs through Operation Archon to the Praetorium, where Gaius is slain, the Ultima Weapon destroyed and Thancred freed (K73, C09). "
             "Boundaries per [v2-discovery.md](v2-discovery.md#proposed-arc-map)."}

# Records the user explicitly accepted (NDL-003, 2026-11-14), each bound to a fingerprint of its accepted content and
# context. Re-recorded mechanically in NDL-006 when the fingerprint gained the context, and in NDL-009 when it dropped
# the sources' mechanical availability; each time only fingerprint inputs moved, and RealDataTests' v1 pin proves the
# content itself did not change.
# Only an exact content match is emitted "reviewed"; see fingerprint() and the module docstring.
ACCEPTED = {
    ('presentation', 'char-minfilia', 'cp-arr-2-0', 'main'): 'bfc89614a1861a0ced86e6dc',
    ('presentation', 'char-minfilia', 'cp-arr-2-55', 'main'): '54bd6ce1624348d24caf5841',
    ('presentation', 'char-thancred', 'cp-arr-2-0', 'main'): '2094032d324714afdadba967',
    ('presentation', 'char-thancred', 'cp-arr-2-55', 'main'): '31ef5a5836c6ffebe9261f80',
    ('presentation', 'char-yshtola', 'cp-arr-2-0', 'main'): '56985d6f9d0dc0b9a534c60e',
    ('presentation', 'char-yshtola', 'cp-arr-2-55', 'main'): '99945ac958a6a86cacdfe2ef',
    ('presentation', 'char-urianger', 'cp-arr-2-0', 'main'): '5fb92be56b707e2cc005d6f2',
    ('presentation', 'char-urianger', 'cp-arr-2-55', 'main'): '73fbf8adcb6bcd100fe5c5fc',
    ('presentation', 'char-alphinaud', 'cp-arr-2-0', 'main'): '035ce3f714d759e8041b3c00',
    ('presentation', 'char-alphinaud', 'cp-arr-2-55', 'main'): '87fc6b363949382022d65bf8',
    ('presentation', 'char-alisaie', 'cp-arr-2-0', 'main'): '0ac538cac4294a9472e53cf4',
    ('presentation', 'char-alisaie', 'cp-arr-2-0', 'optional'): '1c1135fb1fd217896cdd1a02',
    ('presentation', 'char-alisaie', 'cp-arr-2-55', 'main'): '7dc53e74beb0010764b446b1',
    ('presentation', 'char-alisaie', 'cp-arr-2-55', 'optional'): '091a16a246558de3708c8e49',
    ('presentation', 'char-louisoix', 'cp-arr-2-0', 'main'): '967fcc43a76eeb49777f6a7a',
    ('presentation', 'char-louisoix', 'cp-arr-2-0', 'optional'): 'aaf5f08634e8b1925f651962',
    ('presentation', 'char-louisoix', 'cp-arr-2-55', 'main'): '63b81514561793b28152105f',
    ('presentation', 'char-louisoix', 'cp-arr-2-55', 'optional'): '5b5f18f63ea33c70fa4fdd8b',
    ('presentation', 'char-tataru', 'cp-arr-2-0', 'main'): '490f82c1573e07f83b19b5f9',
    ('presentation', 'char-tataru', 'cp-arr-2-55', 'main'): '9b4bab84c0557fe329d34611',
    ('presentation', 'org-scions', 'cp-arr-2-0', 'main'): '7b33c9e8e006ec54a13bfc1a',
    ('presentation', 'org-scions', 'cp-arr-2-55', 'main'): '7c4e9f62567c24170da32c0c',
    ('presentation', 'org-crystal-braves', 'cp-arr-2-55', 'main'): 'a8c8e111edd7eda1a1e8a107',
    ('presentation', 'loc-waking-sands', 'cp-arr-2-0', 'main'): '0db3feac0806311b706fa5b3',
    ('presentation', 'loc-waking-sands', 'cp-arr-2-55', 'main'): '1a055d80873713f68c88055a',
    ('presentation', 'loc-rising-stones', 'cp-arr-2-55', 'main'): '6578619646fc193958c8e930',
    ('relationship', 'rel-minfilia-leads-scions'): 'b8132fbcc20efdf161e54e11',
    ('relationship', 'rel-thancred-member-scions'): 'a811de0a14892ad6f1258496',
    ('relationship', 'rel-yshtola-member-scions'): '74b54427aa328e15c4bde01e',
    ('relationship', 'rel-urianger-member-scions'): 'a05362ba743578b5e76afe98',
    ('relationship', 'rel-alphinaud-member-scions'): '67bc179a99ae72883a7c456c',
    ('relationship', 'rel-tataru-member-scions'): '9a9a5c8eb4d7c6a0e5aeb09e',
    ('relationship', 'rel-alphinaud-twin-alisaie'): 'f58f7f36d201b1a4c759fd17',
    ('relationship', 'rel-scions-hq-waking-sands'): '7b68b5a2f4867c58652e7e4b',
    ('relationship', 'rel-braves-control-rising-stones'): 'b4a77f73ae9a8c40c932e5d0',
    ('relationship', 'rel-braves-turned-against-scions'): '2184c0fa4cad67c5e10fcdea',
    ('relationship', 'rel-urianger-conceals-waking-sands'): '7cb94d05b001cca73bfc4ab0',
    ('relationship', 'rel-alisaie-grandchild-louisoix'): '800de2048776ba880a364001',
    ('relationship', 'rel-alphinaud-grandchild-louisoix'): '47f4e9a585e113c723d7835e',
    ('relationship', 'rel-alisaie-member-scions'): '8f163e268ab8d05aed8a811b',
    # Arc A4 (NDL-009), accepted by the user on 2026-11-14.
    ('presentation', 'char-minfilia', 'cp-msq-154', 'main'): 'bd819b7ec3a838011d7bdbf5',
    ('presentation', 'char-minfilia', 'cp-msq-155', 'main'): '0f30ddb4e04a932825e8390c',
    ('presentation', 'char-minfilia', 'cp-msq-156', 'main'): 'b4db021395b9318160d9184a',
    ('presentation', 'char-thancred', 'cp-msq-154', 'main'): 'cfc3d5108895311badc6a3a9',
    ('presentation', 'char-thancred', 'cp-msq-155', 'main'): '338e17c45a3e5a0360447b20',
    ('presentation', 'char-thancred', 'cp-msq-156', 'main'): '22ae2dd47df31840c318ff39',
    ('presentation', 'char-alphinaud', 'cp-msq-154', 'main'): '186dfb4852b8872db5d8c7be',
    ('presentation', 'char-alphinaud', 'cp-msq-157', 'main'): 'b6c8120f598f21890ee394e0',
    ('presentation', 'org-scions', 'cp-msq-154', 'main'): 'd623120780ee081cfc257364',
    ('presentation', 'org-scions', 'cp-msq-155', 'main'): '000283b79c4476e8f8b8ea8f',
    ('presentation', 'org-scions', 'cp-msq-157', 'main'): 'e08b50a62a65a343009020ab',
    ('presentation', 'evt-black-wolfs-challenge', 'cp-msq-155', 'main'): 'c98569fc938a361e0e5f4a8e',
    ('presentation', 'evt-black-wolfs-challenge', 'cp-msq-156', 'main'): 'e33d6b4737d89f2bff5f6be8',
    ('presentation', 'evt-black-wolfs-challenge', 'cp-msq-157', 'main'): '627a1c79455136b75e91a0bd',
    ('presentation', 'evt-black-wolfs-challenge', 'cp-msq-158', 'main'): '45b9b9d05e02d9d867814c00',
    ('presentation', 'evt-black-wolfs-challenge', 'cp-msq-159', 'main'): '05b809d51bf5e6a3835d78a2',
    ('presentation', 'evt-black-wolfs-challenge', 'cp-msq-160', 'main'): 'b2a29f39aa50d547f5cad867',
    ('presentation', 'evt-black-wolfs-challenge', 'cp-arr-2-0', 'main'): '68361b8c7b1e70619ae3120e',
    ('presentation', 'evt-operation-archon', 'cp-msq-157', 'main'): '6cfa61228e157033bcf22b7e',
    ('presentation', 'evt-operation-archon', 'cp-msq-160', 'main'): '2efcd7c84e660f9434b3ecca',
    ('presentation', 'evt-operation-archon', 'cp-arr-2-0', 'main'): 'e980d93cc1effba80465d881',
    ('presentation', 'char-cid', 'cp-msq-154', 'main'): '413f534fe6f5ef5c8af2564e',
    ('presentation', 'char-cid', 'cp-msq-155', 'main'): 'a88294682c20998f54324091',
    ('presentation', 'char-cid', 'cp-msq-156', 'main'): '7531cdef86f95bdf3f6cc4e5',
    ('presentation', 'char-cid', 'cp-msq-157', 'main'): '8d89673858f8a57885265c0a',
    ('presentation', 'char-cid', 'cp-msq-160', 'main'): '3653ecf028bd8d3367cfd545',
    ('presentation', 'char-cid', 'cp-arr-2-0', 'main'): '63d531e8acf0e73aaa91823c',
    ('presentation', 'char-gaius', 'cp-msq-154', 'main'): '898f21e29b228cf311ce3b93',
    ('presentation', 'char-gaius', 'cp-msq-155', 'main'): 'e4793830e6900e4a30c768b1',
    ('presentation', 'char-gaius', 'cp-msq-157', 'main'): 'bd48ca9f921f6ddf12afa669',
    ('presentation', 'char-gaius', 'cp-arr-2-0', 'main'): 'bde5d6263fcc7b39f9eec01d',
    ('presentation', 'char-livia', 'cp-msq-154', 'main'): '353af7c1f78790e0fa04c68b',
    ('presentation', 'char-livia', 'cp-msq-155', 'main'): 'f7f6defd62feb235402c06c4',
    ('presentation', 'char-livia', 'cp-msq-157', 'main'): 'e960199e3ef69876500a06a2',
    ('presentation', 'char-livia', 'cp-msq-160', 'main'): 'd893b1312ef6d950fc698c94',
    ('presentation', 'char-lahabrea', 'cp-msq-154', 'main'): '487348a99a51304cef72eb5b',
    ('presentation', 'char-lahabrea', 'cp-msq-155', 'main'): '82ce39a48d97e9ae92309c70',
    ('presentation', 'char-lahabrea', 'cp-msq-156', 'main'): '3c42285a7e7af9d721a0d1e7',
    ('presentation', 'char-lahabrea', 'cp-arr-2-0', 'main'): '923ed6b32fc21bffa0db1f7d',
    ('presentation', 'org-eorzean-alliance', 'cp-msq-155', 'main'): 'ff46c91ec736a3098be671f6',
    ('presentation', 'org-eorzean-alliance', 'cp-msq-156', 'main'): 'ccbe1c03096ceb35ccb4a120',
    ('presentation', 'org-eorzean-alliance', 'cp-msq-157', 'main'): 'be27e8ad6c6e1397ddad1956',
    ('presentation', 'org-eorzean-alliance', 'cp-arr-2-0', 'main'): '446a0a7244676be252e6d799',
    ('relationship', 'rel-minfilia-leads-scions-a4'): '995a4f96d324c0188c55e7c5',
    ('relationship', 'rel-thancred-member-scions-a4'): 'c0e9ca996202332d4bdccc89',
    ('relationship', 'rel-alphinaud-member-scions-a4'): 'dd6751e959a613989896525f',
    ('relationship', 'rel-minfilia-prisoner-livia'): 'bd438da9e7ee4908b19c34db',
    ('relationship', 'rel-thancred-possessed-lahabrea'): 'fe472dacf75dc17b941e9e50',
    ('relationship', 'rel-livia-serves-gaius'): 'fb8b80672671a40c23ebf39c',
    ('relationship', 'rel-alliance-in-archon'): '2b760737727b949ad501f8e0',
    ('relationship', 'rel-scions-in-archon'): '37d829bd1f7c1a2cb657661c',
    ('relationship', 'rel-cid-in-archon'): 'b590755d1505fc28c257259a',
    ('relationship', 'p-minfilia-a4'): 'd3ee2514b5d2c071ca8c4c96',
    ('relationship', 'p-thancred-a4'): '6a559d582ce1fcbb5ec84d0f',
    ('relationship', 'p-alphinaud-a4'): '3fdddcf23f4bdae67c4b22ec',
    ('relationship', 'p-scions-a4'): 'deb5f5ef8cf06b540b8b06d4',
    ('relationship', 'p-cid-a4'): '89af62baadee9ef810d2e04d',
    ('relationship', 'p-gaius-a4'): 'cd1ae2851eea3956b8f676a4',
    ('relationship', 'p-livia-a4'): '9d35dd1d1d53f2a3f690ffed',
    ('relationship', 'p-lahabrea-a4'): 'cf6f681dd76641d6f6e37b89',
    ('relationship', 'p-alliance-a4'): 'ed529c7075fbd6b67095741b',
    ('relationship', 'p-archon-a4'): '3b0d6fc80731cff94accbcc5',
}

def fingerprint(record, context=None):
    """Content fingerprint of an emitted record plus the reviewed context it is shown with (never emitted), ignoring
    `review` and each citation's mechanical `availableAt`."""
    body = copy.deepcopy(record)
    body.pop("review", None)
    for field in ("citations", "endCitations"):
        for cite in body.get(field, []):
            cite.pop("availableAt", None)
    body["_context"] = context
    return hashlib.sha256(json.dumps(body, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:24]

def with_review(key, record, context=None, accepted=None):
    """Attach `review`: "reviewed" only if the key was accepted with exactly this content and context."""
    accepted = ACCEPTED if accepted is None else accepted
    fp = fingerprint(record, context)
    record["review"] = "reviewed" if accepted.get(key) == fp else "pending"
    FINGERPRINTS[key] = fp
    return record

FINGERPRINTS = {}

def evidence(claims):
    """The reviewed evidence behind a record: each claim's id, wording, source entry and locator. The source's
    availability is left out, like a citation's availableAt: it may move earlier mechanically (v2 plan)."""
    return [[c, C[c][0], C[c][2], {k: v for k, v in SRC[C[c][1]].items() if k != "avail"}] for c in claims]

TYPE_ROW = {i: [o, n, sym] for i, o, n, sym in TYPES}

def rel_parts(r):
    """A RELS row: (id, source, type, target, from, until, scope, claims, review-sheet label[, end claims])."""
    rid, s, t, g, f, u, sc, cl, rn, *rest = r
    return rid, s, t, g, f, u, sc, cl, rn, (rest[0] if rest else [])

def rel_record(r):
    rid, s, t, g, f, u, sc, cl, _, end = rel_parts(r)
    record = {"id": rid, "source": s, "type": t, "target": g, "validFrom": f, "validUntil": u, "scope": sc,
              "citations": [citation(k) for k in cites(cl)]}
    context = {"type": TYPE_ROW[t], "evidence": evidence(cl)}
    if end:  # end evidence, shown only on the Changes "ended" row (v2 spoiler rule 2)
        record["endCitations"] = [citation(k) for k in cites(end)]
        context["endEvidence"] = evidence(end)
    return with_review(("relationship", rid), record, context)

def missing_accepted(accepted, emitted):
    return sorted(set(accepted) - emitted)

def citation(k):
    s = SRC[k]
    return {"title": s["title"], "url": url(k), "availableAt": s["avail"], "scope": s["scope"]}

def url(k):
    # Quest article pages only (user decision, 2026-11-14): links are shown behind the Atlas's external-page
    # spoiler warning. The URL itself names only the quest; see docs/atlas/content-evidence.md#citation-safety.
    return "https://ffxiv.consolegameswiki.com/wiki/" + urllib.parse.quote(SRC[k]["page"].replace(" ", "_"), safe="()'_-.")

doc = {
  "schemaVersion": 2,
  "checkpoints": CHECKPOINTS,
  "relationshipTypes": [{"id": i, "outgoingLabel": o, "incomingLabel": n, "symmetric": s} for i, o, n, s in TYPES],
  "entities": [
    {"id": eid, "category": cat, "presentations": [
      with_review(("presentation", eid, p["frm"], p["scope"]),
        {"validFrom": p["frm"], "validUntil": p["until"], "scope": p["scope"], "name": p["name"], "aliases": p["aliases"],
         "summary": p["summary"], "citations": [citation(k) for k in cites(p["claims"])]},
        {"category": cat, "evidence": evidence(p["claims"])})
      for p in pres]}
    for eid, cat, pres in ENT],
  "relationships": [rel_record(r) for r in RELS],
  **({"arcs": [{"id": aid, "entityId": eid, "firstStep": f, "lastStep": l} for aid, eid, f, l in ARCS]} if ARCS else {}),
}

# An accepted key that no longer exists means a record was renamed or deleted: fail loudly instead of drifting.
EMITTED_KEYS = {("presentation", e["id"], pr["validFrom"], pr["scope"]) for e in doc["entities"] for pr in e["presentations"]} | {("relationship", r["id"]) for r in doc["relationships"]}
MISSING = missing_accepted(ACCEPTED, EMITTED_KEYS)
if MISSING:
    sys.exit(f"ACCEPTED lists records that no longer exist: {MISSING}")

if PRINT_PENDING:
    for e in doc["entities"]:
        for pr in e["presentations"]:
            if pr["review"] == "pending":
                k = ("presentation", e["id"], pr["validFrom"], pr["scope"]); print(f"    {k!r}: {FINGERPRINTS[k]!r},")
    for r in doc["relationships"]:
        if r["review"] == "pending":
            k = ("relationship", r["id"]); print(f"    {k!r}: {FINGERPRINTS[k]!r},")
    sys.exit(0)

if SELF_TEST:
    def check(label, cond):
        print(("ok   " if cond else "FAIL ") + label)
        if not cond:
            sys.exit(1)
    rid, _, rtype, _, _, _, _, rclaims, _, _ = rel_parts(RELS[0])
    sample = copy.deepcopy(doc["relationships"][0]); sample.pop("review")
    key = ("relationship", sample["id"])
    ctx = {"type": TYPE_ROW[rtype], "evidence": evidence(rclaims)}
    accepted = {key: fingerprint(sample, ctx)}
    def status(record, context=ctx, k=key, acc=accepted): return with_review(k, copy.deepcopy(record), context, acc)["review"]
    check("unchanged accepted record stays reviewed", status(sample) == "reviewed")
    check("new record is pending", status(sample, k=("relationship", "rel-new")) == "pending")
    moved = copy.deepcopy(sample); moved["validFrom"] = "cp-earlier"
    check("an earlier validFrom under the same id is pending", status(moved) == "pending")
    retargeted = copy.deepcopy(sample); retargeted["target"] = "org-elsewhere"
    check("a changed endpoint is pending", status(retargeted) == "pending")
    cited = copy.deepcopy(sample); cited["citations"] = cited["citations"] + [{"title": "Extra", "url": None, "availableAt": "cp-arr-2-0", "scope": "main"}]
    check("an added citation is pending", status(cited) == "pending")
    shifted = copy.deepcopy(sample); shifted["citations"][0]["availableAt"] = "cp-earlier"
    check("only a citation's availableAt moved: still reviewed", status(shifted) == "reviewed")
    relabelled = copy.deepcopy(ctx); relabelled["type"] = ["betrays", "betrayed by", False]
    check("a changed type label is pending", status(sample, relabelled) == "pending")
    swapped = {**ctx, "evidence": evidence(["C33"])}
    check("a swapped claim is pending", status(sample, swapped) == "pending")
    requoted = copy.deepcopy(ctx); requoted["evidence"][0][2] += " (edited)"
    check("a reworded locator is pending", status(sample, requoted) == "pending")
    eid, ecat, epres = ENT[0]
    pres = copy.deepcopy(doc["entities"][0]["presentations"][0]); pres.pop("review")
    pkey = ("presentation", eid, pres["validFrom"], pres["scope"])
    pctx = {"category": ecat, "evidence": evidence(epres[0]["claims"])}
    paccepted = {pkey: fingerprint(pres, pctx)}
    reworded = copy.deepcopy(pres); reworded["summary"] = pres["summary"] + " Changed."
    check("changed presentation text is pending", status(reworded, pctx, pkey, paccepted) == "pending")
    check("a changed category is pending", status(pres, {**pctx, "category": "location"}, pkey, paccepted) == "pending")
    check("an accepted key that no longer exists is reported", missing_accepted({**ACCEPTED, ("relationship", "rel-gone"): "x"}, EMITTED_KEYS) == [("relationship", "rel-gone")])
    ended = copy.deepcopy(sample); ended["endCitations"] = [{"title": "Why it ended", "url": None, "availableAt": "cp-arr-2-0", "scope": "main"}]
    check("added end evidence is pending", status(ended) == "pending")
    check("every accepted record is currently reviewed", all(pr["review"] == "reviewed" for e in doc["entities"] for pr in e["presentations"] if ("presentation", e["id"], pr["validFrom"], pr["scope"]) in ACCEPTED)
          and all(r["review"] == "reviewed" for r in doc["relationships"] if ("relationship", r["id"]) in ACCEPTED))
    sys.exit(0)
for c in C.values():
    assert c[1] in SRC, c
(REPO / "NpcDialogueLinks/atlas.json").write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n")

# ---- Review sheet ---------------------------------------------------------------------------------------------
NAME = {eid: pres[0]["name"] for eid, _, pres in ENT}
TLAB = {i: (o, n) for i, o, n, _ in TYPES}
def interval(f, u):
    if u is None:
        return f"{CP_SHORT[f]} onward"
    last = ORDER[ORDER.index(u) - 1]
    return f"{CP_SHORT[f]} only" if last == f else f"{CP_SHORT[f]}–{CP_SHORT[last]}"

def covers(f, u, cid):
    return ORDER.index(f) <= ORDER.index(cid) and (u is None or ORDER.index(cid) < ORDER.index(u))

def visible_counts(cid, view):
    scopes = ("main",) if view == "main" else ("main", "optional")
    ents = sum(1 for _, _, pres in ENT if any(p["scope"] in scopes and covers(p["frm"], p["until"], cid) for p in pres))
    rels = sum(1 for r in RELS if (lambda x: x[6] in scopes and covers(x[4], x[5], cid))(rel_parts(r)))
    return ents, rels
def claimrows(claims):
    return "\n".join(f"  - **{c}** {C[c][0]} *{C[c][1]}* ({SRC[C[c][1]]['patch']}, {SRC[C[c][1]]['scope']}): \"{C[c][2]}\"" for c in claims)

out = []
w = out.append
w("# Atlas content review sheet\n")
PENDING = sum(1 for e in doc["entities"] for pr in e["presentations"] if pr["review"] == "pending") + sum(1 for r in doc["relationships"] if r["review"] == "pending")
w(f"> **Status: {'REVIEWED' if PENDING == 0 else f'AWAITING HUMAN REVIEW ({PENDING} pending)'}.** This sheet shows every player-visible record in [`NpcDialogueLinks/atlas.json`](../../NpcDialogueLinks/atlas.json), "
  "exactly as written there, with the evidence behind it. Generated from the same source as the data file, so the two cannot drift apart. "
  "AI research and AI review are not canon acceptance: only your explicit approval marks these records `reviewed`.\n")
w("How to read it:\n")
w("- **Main** text is what the main-story view shows. **Optional** text replaces it in the default *main + optional* view, because it includes optional Binding Coil quests that are doable and released by that patch (the [available-content rule](../lore-relationship-atlas.md#research-and-content-rules)).")
w("- Each claim quotes a short locator from the Console Games Wiki transcription of that quest, so you can find it. Patch numbers are when the quest was released, which sets the earliest checkpoint where the claim counts.")
w("- Every source links to its quest page on the Console Games Wiki. The Atlas warns before opening it, because those pages list NPCs by full name and can mention later patches.\n")
w("## Decisions recorded\n")
w("The user decided these on 2026-11-14:\n")
w("1. **Source links: on.** Every citation links to its quest page. The [citation audit](content-evidence.md#citation-safety) found that most quest pages list NPCs by full name (\"Warde\", and \"Leveilleur\" from 2.2), so the link opens only behind the Atlas's external-page spoiler warning. Each URL names only the quest itself.")
w("2. **Alisaie as a Scion (R14, optional only): keep.** Its only direct support is the optional *Alisaie's Pledge* journal calling her \"the young Scion\" (C30).")
w("3. **Alphinaud as Louisoix's grandchild (R13, optional, from 2.55): keep.** It rests on two optional lines read together: Louisoix was Alisaie's grandsire (C13, 2.0), and Alphinaud speaks of \"our grandsire\" shared with his sister (C26, 2.2).\n")
w("For arc A4 (`NDL-009`), the user decided on 2026-11-14:\n")
w("4. **The arc:** A4, MSQ #155 *Escape from Castrum Centri* to #161 *The Ultimate Weapon*, with #154 as the baseline ([v2-discovery.md](v2-discovery.md)).")
w("5. **The cast of 10:** Minfilia, Thancred, Alphinaud and the Scions (already in the Atlas); Cid, Gaius, Livia, Lahabrea and the Eorzean Alliance (new); and the Operation Archon event. The plan's caps were raised by one each: five new entities instead of four, and four new relationship types instead of three (*part of*, *prisoner of*, *possessed by*, *serves*).\n")
w("Lead decisions, confirmed by the user with the content on 2026-11-14:\n")
w("6. **First names only**, as in the pilot: Gaius, Livia, Cid. Cid's company is \"the Ironworks\", never its full name.")
w("7. **Slice steps name only the cast.** Text at #154–160 never names a character the slice doesn't cover (such as Tataru or Y'shtola), because the leak sweep can't tell \"met before #154\" from \"not met yet\". Raubahn and Rhitahtyn, who are not Atlas entries, are named only from the quest where they appear.")
w("8. **Current quest versions.** Patch 6.1 reworked *Operation Archon* and *The Ultimate Weapon* (the Lahabrea fight became a solo duty). The wiki transcribes the current versions, which is what a player sees today, so the evidence follows them.")
w("9. **Lahabrea is never written as dead,** and Nero is left out: the 2.0 finale shows neither's end. Livia is written as dead, from Cid's \"May her soul know rest\" (K62).")
w("10. **The arc's name, *The Black Wolf's Challenge*.** It reveals nothing past its first step: by the end of #155 the Black Wolf's ultimatum is already being debated (K26). It avoids reusing #156's quest title, *The Black Wolf's Ultimatum*.\n")
w("## Snapshot overview\n")
w("Visible records at each step, in the main-story view and the main + optional view. Slice steps (#…) cover only the arc's cast.\n")
w("| Step | Entities (main) | Entities (+ optional) | Relationships (main) | Relationships (+ optional) |\n|---|---|---|---|---|")
for cid in ORDER:
    em, rm = visible_counts(cid, "main"); eo, ro = visible_counts(cid, "full")
    w(f"| {CP_SHORT[cid]} {CP_LABEL[cid]} | {em} | {eo} | {rm} | {ro} |")
w("")
if ARCS:
    w("## Arcs\n")
    for aid, entry, first, last in ARCS:
        pres = next(p for e, _, p in ENT if e == entry)
        w(f"### {pres[0]['name']} (`{aid}`)\n")
        w(f"From {CP_SHORT[first]} *{CP_LABEL[first]}* to {CP_SHORT[last]} *{CP_LABEL[last]}*. {ARC_NOTES[aid]}\n")
        w("| Step | Arc name | Recap | Recap status | Cast at this step |\n|---|---|---|---|---|")
        cast = []
        for cid in ORDER[ORDER.index(first):ORDER.index(last) + 1]:
            p = next(x for x in pres if covers(x["frm"], x["until"], cid))
            status = "new recap" if p["frm"] == cid else "unchanged, still accurate"
            members = [NAME[s] for r in RELS for (rid, s, t, g, f, u, sc, cl, rn, end) in [rel_parts(r)] if t == "participant-in" and g == entry and covers(f, u, cid)]
            w(f"| {CP_SHORT[cid]} | {p['name']} | {p['summary']} | {status} | {', '.join(members)} ({len(members)}) |")
        w("")
w("## Entities\n")
for eid, cat, pres in ENT:
    w(f"### {NAME[eid]} (`{eid}`, {cat})\n")
    for p in pres:
        al = f" · Also searchable as: {', '.join(p['aliases'])}" if p["aliases"] else ""
        w(f"**{interval(p['frm'], p['until'])} · {p['scope']}**{al}\n")
        w(f"> {p['summary']}\n")
        w("Sources shown: " + "; ".join(SRC[k]["title"] for k in cites(p["claims"])) + "\n")
        w("<details><summary>Evidence</summary>\n\n" + claimrows(p["claims"]) + "\n\n</details>\n")
w("## Relationships\n")
w("| ID | Edge | Visible | Scope | Claims |\n|---|---|---|---|---|")
w("| ID | Edge | Visible | Scope | Claims | End evidence |\n|---|---|---|---|---|---|") if False else None
for r in RELS:
    rid, s, t, g, f, u, sc, cl, rn, end = rel_parts(r)
    w(f"| {rn} | {NAME[s]} → *{TLAB[t][0]}* → {NAME[g]} | {interval(f, u)} | {sc} | {', '.join(cl)}{(' · ends: ' + ', '.join(end)) if end else ''} |")
w("\nEvidence for each claim is listed under the entities above and in full in the [claims table](content-claims.md).\n")
(REPO / "docs/atlas/content-review.md").write_text("\n".join(out))

# ---- Claims table for the evidence matrix ---------------------------------------------------------------------
rows = ["| ID | Claim (own words) | Source · patch · scope | Locator | Counts from |", "|---|---|---|---|---|"]
for cid in sorted(C, key=lambda x: (int(''.join(ch for ch in x[1:] if ch.isdigit())), x)):
    t, k, q = C[cid]
    rows.append(f"| {cid} | {t} | *{SRC[k]['page']}* · {SRC[k]['patch']} · {SRC[k]['scope']} | \"{q}\" | {CP_SHORT[SRC[k]['avail']]} |")
head = ("# Atlas claims\n\nGenerated by `tools/atlas/build_pilot_content.py`; do not edit by hand. "
        "Method, decisions and citation safety: [content-evidence.md](content-evidence.md). "
        "Locators quote Console Games Wiki transcriptions of in-game text; \"Counts from\" is the earliest checkpoint where the quest is player knowledge.\n\n")
(REPO / "docs/atlas/content-claims.md").write_text(head + "\n".join(rows) + "\n")
print("ok", len(C), "claims", sum(len(p) for _, _, p in ENT), "presentations", len(RELS), "relationships")
