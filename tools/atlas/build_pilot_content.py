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

# Arcs (schema v2): (arc id, arc entry event id, first step, last step), in authored order.
ARCS = []

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
