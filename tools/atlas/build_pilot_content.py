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
import copy, hashlib, importlib, json, re, sys, pathlib, urllib.parse
import content_arr_2_0 as ARR  # NDL-012: MSQ #102–#154, five arcs before A4 (data only)
import timeline_2x_3x as TL  # one step per main-scenario quest of 2.1–3.56, plus the 2.55, 3.0 and 3.56 milestones
import timeline_4x as TL4  # the same for Stormblood, 4.0–4.56, plus the 4.0 and 4.56 milestones
import timeline_5x as TL5  # the same for Shadowbringers, 5.0–5.55, plus the 5.0 and 5.55 milestones

REPO = pathlib.Path(__file__).resolve().parents[2]
ARGS = sys.argv[1:]
SELF_TEST = ARGS == ["--self-test"]
PRINT_PENDING = ARGS == ["--print-pending"]
ACCEPT_PENDING = ARGS == ["--accept-pending"]
LINT = bool(ARGS) and ARGS[0] == "--lint" and len(ARGS) <= 2
VERIFY = len(ARGS) == 2 and ARGS[0] == "--verify-locators"
if ARGS and not (SELF_TEST or PRINT_PENDING or ACCEPT_PENDING or LINT or VERIFY):
    sys.exit("Usage: build_pilot_content.py [--self-test | --print-pending | --accept-pending | --lint [ERA_MODULE] | --verify-locators PAGES_DIR].")
A, B = "cp-arr-2-0", "cp-arr-2-55"
C3, D3 = TL.MILESTONE_3_0[0], TL.MILESTONE_3_56[0]
E4, F4 = TL4.MILESTONE_4_0[0], TL4.MILESTONE_4_56[0]
G5, H5 = TL5.MILESTONE_5_0[0], TL5.MILESTONE_5_55[0]

# The era modules after 2.0, in timeline order: (module, first step it may start a record on, last checkpoint).
ERAS = [
    ("content_2_1_to_2_3", "cp-msq-162", "cp-msq-199"),
    ("content_2_4_to_2_55", "cp-msq-200", B),
    ("content_3_0_part1", "cp-msq-242", "cp-msq-291"),
    ("content_3_0_part2", "cp-msq-292", C3),
    ("content_3_1_to_3_56", "cp-msq-336", D3),
    ("content_4_0_part1", "cp-msq-380", "cp-msq-418"),
    ("content_4_0_part2", "cp-msq-419", "cp-msq-464"),
    ("content_4_0_part3", "cp-msq-465", E4),
    ("content_4_1_to_4_56", "cp-msq-502", F4),
    ("content_5_0_part1", "cp-msq-542", "cp-msq-579"),
    ("content_5_0_part2", "cp-msq-580", "cp-msq-620"),
    ("content_5_0_part3", "cp-msq-621", G5),
    ("content_5_1_to_5_3", "cp-msq-648", "cp-msq-681"),
    ("content_5_4_to_5_55", "cp-msq-682", H5),
    # The lead's integration module, merged last: earlier entries for entities that accepted or earlier-era text already
    # names (so nothing is named before it is visible), and the cross-era endings no single era could write.
    ("content_lead_integration", "cp-msq-102", H5),
]
LINT_ONLY = ARGS[1] if LINT and len(ARGS) == 2 else None
if LINT_ONLY and LINT_ONLY not in {m for m, _, _ in ERAS}:
    sys.exit(f"--lint takes one of: {', '.join(m for m, _, _ in ERAS)}")

# ---- Timeline (schema v2) ---------------------------------------------------------------------------------------
# The A4 slice (NDL-009): the baseline step after MSQ #154, then one step after each of #155–160. Each step means
# "after this quest". The milestone A (cp-arr-2-0) is the step after #161, The Ultimate Weapon, so it is contiguous
# with the slice. Every step carries its quest's game id (wiki id-gt) for Follow (deferred; NDL-007 verifies them).
SLICE = ARR.EARLY_SLICE + [  # (checkpoint id, MSQ index, quest title, game quest id); NDL-012 prepends #102–#153
    ("cp-msq-154", 154, "Every Little Thing She Does Is Magitek", 66541),
    ("cp-msq-155", 155, "Escape from Castrum Centri", 66057),
    ("cp-msq-156", 156, "The Black Wolf's Ultimatum", 66058),
    ("cp-msq-157", 157, "Operation Archon", 70057),
    ("cp-msq-158", 158, "A Hero in Need", 66573),
    ("cp-msq-159", 159, "Hearts on Fire", 69408),
    ("cp-msq-160", 160, "Rock the Castrum", 69409),
]
BASE = SLICE[0][0]
LATER = TL.STEPS_2X + TL.STEPS_3_0 + TL.STEPS_3X + TL4.STEPS_4_0 + TL4.STEPS_4X + TL5.STEPS_5_0 + TL5.STEPS_5X  # (checkpoint id, MSQ index, quest title, game quest id, patch)
MILESTONES = {A: ("A Realm Reborn — Patch 2.0 complete", "The Ultimate Weapon", 70058), B: TL.MILESTONE_2_55[1:],
              C3: TL.MILESTONE_3_0[1:], D3: TL.MILESTONE_3_56[1:], E4: TL4.MILESTONE_4_0[1:], F4: TL4.MILESTONE_4_56[1:],
              G5: TL5.MILESTONE_5_0[1:], H5: TL5.MILESTONE_5_55[1:]}
STEP_OF = {title: cid for cid, _, title, _ in SLICE} | {title: cid for cid, _, title, _, _ in LATER}
MILESTONE_OF = {quest: cid for cid, (_, quest, _) in MILESTONES.items()}  # a milestone's own quest counts from it
CP_LABEL = {cid: label for cid, (label, _, _) in MILESTONES.items()} | {cid: f"After {title}" for cid, _, title, _ in SLICE} \
    | {cid: f"After {title}" for cid, _, title, _, _ in LATER}
CP_SHORT = {A: "2.0", B: "2.55", C3: "3.0", D3: "3.56", E4: "4.0", F4: "4.56", G5: "5.0", H5: "5.55", **{cid: f"#{n}" for cid, n, _, _ in SLICE}, **ARR.SHORT,
            **{cid: f"#{n}" for cid, n, _, _, _ in LATER}, **TL.SHORT, **TL4.SHORT, **TL5.SHORT}
ORDER = ([cid for cid, _, _, _ in SLICE] + [A] + [c for c, *_ in TL.STEPS_2X] + [B] + [c for c, *_ in TL.STEPS_3_0] + [C3]
         + [c for c, *_ in TL.STEPS_3X] + [D3] + [c for c, *_ in TL4.STEPS_4_0] + [E4] + [c for c, *_ in TL4.STEPS_4X] + [F4]
         + [c for c, *_ in TL5.STEPS_5_0] + [G5] + [c for c, *_ in TL5.STEPS_5X] + [H5])
IDX = {cid: i for i, cid in enumerate(ORDER)}

# ---- Sources: wiki page title -> (display title, patch, availableAt, scope) -------------------------------
# availableAt is the earliest timeline step at or after the quest: a 2.0 main quest before #154 counts from the
# baseline, a slice quest from its own step, The Ultimate Weapon from cp-arr-2-0; later patches from cp-arr-2-55, and
# optional quests from the milestone of their patch. Moving an accepted citation's availableAt earlier this way is the
# v2 plan's permitted mechanical change (it is never displayed, and the fingerprint ignores it).
SRC = {}
def src(key, page, patch, scope="main", kind=None):
    if scope == "optional":
        avail = A if patch == "2.0" else B
    elif key in MILESTONE_OF:
        avail = MILESTONE_OF[key]
    elif patch == "2.0":
        avail = STEP_OF.get(key, BASE)
    else:  # every later main-scenario quest has its own step (timeline_2x_3x)
        avail = STEP_OF[key]
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
# Every later main-scenario quest, and the quest each later milestone follows, so era modules can cite any of them.
PAGES_LATER = {**TL.PAGES, **TL4.PAGES, **TL5.PAGES}
for _, _, k, _, patch in LATER:
    if k not in SRC:
        src(k, PAGES_LATER.get(k, k), patch)
for k, patch in [("Heavensward", "3.0"), ("The Far Edge of Fate", "3.56"), ("Stormblood", "4.0"), ("A Requiem for Heroes", "4.56"),
                 ("Shadowbringers", "5.0"), ("Death Unto Dawn", "5.55")]:
    src(k, PAGES_LATER.get(k, k), patch)

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
    {"id": cid, "label": CP_LABEL[cid], "questTitle": title, **({"contiguousWithPrevious": True} if i and cid not in ARR.NOT_CONTIGUOUS else {}), "gameQuestIds": [gid]}
    for i, (cid, _, title, gid) in enumerate(SLICE)
]
# Each milestone is the step after its patch's last quest, so it is contiguous with the step before it; each later step
# is contiguous unless it follows another parallel path (timeline_2x_3x.NOT_CONTIGUOUS).
def _milestone(cid):
    label, _, gid = MILESTONES[cid]
    return {"id": cid, "label": label, "milestone": True, "contiguousWithPrevious": True, "gameQuestIds": [gid]}
def _later(steps):
    return [{"id": cid, "label": CP_LABEL[cid], "questTitle": title, **({} if cid in TL.NOT_CONTIGUOUS | TL4.NOT_CONTIGUOUS | TL5.NOT_CONTIGUOUS else {"contiguousWithPrevious": True}),
             "gameQuestIds": [gid]} for cid, _, title, gid, _ in steps]
CHECKPOINTS += [_milestone(A)] + _later(TL.STEPS_2X) + [_milestone(B)] + _later(TL.STEPS_3_0) + [_milestone(C3)] + _later(TL.STEPS_3X) + [_milestone(D3)] \
    + _later(TL4.STEPS_4_0) + [_milestone(E4)] + _later(TL4.STEPS_4X) + [_milestone(F4)] \
    + _later(TL5.STEPS_5_0) + [_milestone(G5)] + _later(TL5.STEPS_5X) + [_milestone(H5)]
assert [c["id"] for c in CHECKPOINTS] == ORDER

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
Q154, Q155, Q156, Q157, Q158, Q159, Q160 = (cid for cid, _, _, _ in SLICE[len(ARR.EARLY_SLICE):])
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

# ==== A Realm Reborn 2.0, MSQ #102–#154 (NDL-012) ================================================================
# Data lives in content_arr_2_0.py; merged here so review status, citations and generated files work as for A4.
for _, _, title, _ in ARR.EARLY_SLICE:
    src(title, ARR.PAGES.get(title, title), "2.0")
for title in ARR.EXTRA_SOURCES:
    src(title, title, "2.0")
assert not set(ARR.CLAIMS) & set(C), "claim id collision"
C.update(ARR.CLAIMS)
_known = {eid for eid, _, _ in ENT}
assert set(ARR.EARLY_PRES) <= _known and not {eid for eid, _, _ in ARR.NEW_ENT} & _known
ENT = [(eid, cat, ARR.EARLY_PRES.get(eid, []) + pres) for eid, cat, pres in ENT] + ARR.NEW_ENT
TYPES += ARR.TYPES
RELS += ARR.RELS
_n = 11
for entry, members in ARR.CASTS.items():
    arc_tag = next(aid for aid, e, _, _ in ARR.ARCS if e == entry).split("-")[1]
    for member, frm, claims in members:
        RELS.append((f"p-{member.split('-', 1)[1]}-{arc_tag}", member, "participant-in", entry, frm, None, "main", claims, f"P{_n}"))
        _n += 1
ARCS = ARR.ARCS + ARCS
ARC_NOTES.update(ARR.ARC_NOTES)

# ==== After 2.0: patches 2.1–3.56, one module per era (ERAS) =====================================================
# Each module holds only data (see docs/atlas/era-modules.md for the contract): CLAIMS, ENTITIES (new id -> category),
# PRES (entity id -> presentations, for new or existing entities), TYPES, RELS, ADJUST (interval changes to
# relationships an earlier module or the accepted content defined), ARCS, CASTS, ARC_NOTES and DECISIONS.
# Presentations are merged per entity and scope in timeline order; each one runs until the next one starts (so an
# earlier open or longer record is closed there), which keeps every entity continuously visible.
ERA_MODULES = []
ERA_OF = {}
_known_ids = {eid for eid, _, _ in ENT}
_ent_index = {eid: i for i, (eid, _, _) in enumerate(ENT)}
_rel_ids = {r[0] for r in RELS}
_type_rows = {i: (o, n, s) for i, o, n, s in TYPES}
LINT_ERRORS = []
DROPPED_DUPLICATES = []
def _lint(msg):
    LINT_ERRORS.append(msg)
for _mod, _first, _last in ERAS:
    if LINT_ONLY and _mod != LINT_ONLY:
        continue
    try:
        M = importlib.import_module(_mod)
    except ModuleNotFoundError:
        continue
    ERA_MODULES.append((_mod, M))
    _lo, _hi = IDX[_first], IDX[_last]
    def _in_era(step, what):
        if step not in IDX:
            _lint(f"{_mod}: {what}: unknown step {step!r}")
        elif not (_lo <= IDX[step] <= _hi):
            _lint(f"{_mod}: {what}: step {step} is outside this era ({_first}–{_last})")
    for k, v in getattr(M, "CLAIMS", {}).items():
        if k in C:
            _lint(f"{_mod}: claim id {k} already exists")
        elif v[1] not in SRC:
            _lint(f"{_mod}: claim {k} cites unknown source {v[1]!r} (use the quest title exactly)")
        else:
            C[k] = v
            ERA_OF[("claim", k)] = _mod
    for eid, cat in getattr(M, "ENTITIES", {}).items():
        if eid in _known_ids:
            known_cat = ENT[_ent_index[eid]][1]
            if known_cat != cat:
                _lint(f"{_mod}: entity {eid} already exists as {known_cat}, not {cat}")
            continue
        if cat not in ("character", "organization", "location", "event"):
            _lint(f"{_mod}: entity {eid}: unknown category {cat}")
        _ent_index[eid] = len(ENT); ENT.append((eid, cat, [])); _known_ids.add(eid)
        ERA_OF[("entity", eid)] = _mod
    for eid, plist in getattr(M, "PRES", {}).items():
        if eid not in _known_ids:
            _lint(f"{_mod}: presentations for unknown entity {eid} (add it to ENTITIES)")
            continue
        for pr in plist:
            _in_era(pr["frm"], f"presentation of {eid}")
            pr = dict(pr, _era=_mod)
            ENT[_ent_index[eid]][2].append(pr)
    for i, o, n, s in getattr(M, "TYPES", []):
        if i in _type_rows:
            if _type_rows[i] != (o, n, s):
                _lint(f"{_mod}: relationship type {i} already exists with different labels {_type_rows[i]}")
            continue
        _type_rows[i] = (o, n, s); TYPES.append((i, o, n, s))
    for r in getattr(M, "RELS", []):
        rid, s, ty, g, f, u, sc, cl, *rest = r
        if rid in _rel_ids:
            # Parallel eras sometimes wrote the same relationship under the conventional id: keep the earlier era's
            # record (it starts first) and drop this copy, unless the two disagree on what the relationship is.
            prior = next(x for x in RELS if x[0] == rid)
            if (prior[1], prior[2], prior[3], prior[6]) != (s, ty, g, sc):
                _lint(f"{_mod}: relationship id {rid} already exists as a different relationship")
            else:
                DROPPED_DUPLICATES.append((_mod, rid))
            continue
        _in_era(f, f"relationship {rid}")
        _rel_ids.add(rid); RELS.append((rid, s, ty, g, f, u, sc, cl, f"R{len(RELS) + 1}", *(rest[:1])))
        ERA_OF[("relationship", rid)] = _mod
    for rid, change in getattr(M, "ADJUST", {}).items():
        hit = [i for i, r in enumerate(RELS) if r[0] == rid]
        if not hit:
            _lint(f"{_mod}: ADJUST names unknown relationship {rid}"); continue
        _r = RELS[hit[0]]
        r = list(_r[:9]) + [(_r[9] if len(_r) > 9 else [])]
        if "frm" in change:
            r[4] = change["frm"]
        if "until" in change:
            r[5] = change["until"]
            if change["until"] is not None:
                _in_era(change["until"], f"ADJUST until of {rid}")
        if "end" in change:
            r[9] = change["end"]
        RELS[hit[0]] = tuple(r[:9]) + ((r[9],) if r[9] else ())
    for aid, entry, f, l in getattr(M, "ARCS", []):
        _in_era(f, f"arc {aid} first step"); _in_era(l, f"arc {aid} last step")
        ARCS.append((aid, entry, f, l))
    ARC_NOTES.update(getattr(M, "ARC_NOTES", {}))
    for entry, members in getattr(M, "CASTS", {}).items():
        arc = [a for a in getattr(M, "ARCS", []) if a[1] == entry]
        if not arc:
            _lint(f"{_mod}: CASTS names {entry}, which is no arc entry in this module"); continue
        tag = arc[0][0].split("-")[1]
        for member, frm, claims in members:
            _in_era(frm, f"cast member {member} of {arc[0][0]}")
            RELS.append((f"p-{member.split('-', 1)[1]}-{tag}", member, "participant-in", entry, frm, None, "main", claims, f"P{len(RELS) + 1}"))

# Merge each entity's presentations in timeline order, per scope; each runs until the next one of its scope starts.
for _eid, _cat, _pres in ENT:
    _pres.sort(key=lambda p: (IDX.get(p["frm"], -1), p["scope"] != "main"))
    for _scope in ("main", "optional"):
        _ps = [p for p in _pres if p["scope"] == _scope]
        for _p, _q in zip(_ps, _ps[1:]):
            if _p["until"] is None or IDX[_p["until"]] > IDX[_q["frm"]]:
                _p["until"] = _q["frm"]
            elif IDX[_p["until"]] < IDX[_q["frm"]]:
                _lint(f"{_eid}: {_scope} presentations leave a gap from {_p['until']} to {_q['frm']}")
            if _p["frm"] == _q["frm"]:
                _lint(f"{_eid}: two {_scope} presentations start at {_p['frm']}")
    # Optional follows main boundaries, and optional persists (schema v1): an optional record ends where a later main
    # record starts inside it, and from there the optional view carries each newer main record's text unchanged.
    _mains = [p for p in _pres if p["scope"] == "main" and p["frm"] in IDX]
    _extra = []
    for _p in [p for p in _pres if p["scope"] == "optional" and p["frm"] in IDX]:
        _end = len(ORDER) if _p["until"] is None else IDX[_p["until"]]
        _inside = [m for m in _mains if IDX[_p["frm"]] < IDX[m["frm"]] < _end]
        if not _inside:
            continue
        _p["until"] = _inside[0]["frm"]
        for _m in _inside:
            _mu = len(ORDER) if _m["until"] is None else IDX[_m["until"]]
            _u = min(_mu, _end)
            _extra.append(dict(_m, scope="optional", until=None if _u == len(ORDER) else ORDER[_u], _mirrors_main=True))
    _pres.extend(_extra)
    _pres.sort(key=lambda p: (IDX.get(p["frm"], -1), p["scope"] != "main"))
# Catch a record citing a quest that comes after its own start here, before the C# validator does (CitationTooNew).
for _eid, _, _pres in ENT:
    for _p in _pres:
        for _c in _p["claims"]:
            if _c not in C:
                _lint(f"{_eid} at {_p['frm']}: unknown claim {_c}")
            elif IDX[SRC[C[_c][1]]["avail"]] > IDX.get(_p["frm"], -1):
                _lint(f"{_eid} at {_p['frm']}: claim {_c} cites {C[_c][1]!r}, which comes later")
for _r in RELS:
    _rid, _, _, _, _f, _u, _, _cl, _, *_rest = _r
    for _c in _cl:
        if _c not in C:
            _lint(f"{_rid}: unknown claim {_c}")
        elif IDX[SRC[C[_c][1]]["avail"]] > IDX.get(_f, -1):
            _lint(f"{_rid} at {_f}: claim {_c} cites {C[_c][1]!r}, which comes later")
    for _c in (_rest[0] if _rest else []):
        if _c not in C:
            _lint(f"{_rid}: unknown end claim {_c}")
        elif _u is None or IDX[SRC[C[_c][1]]["avail"]] > IDX.get(_u, -1):
            _lint(f"{_rid}: end claim {_c} cites {C[_c][1]!r}, which is not available by the ending step {_u}")
if LINT_ERRORS and not LINT:
    sys.exit("Content errors (run --lint for the full report):\n  " + "\n  ".join(LINT_ERRORS[:40]))

# ---- Portraits (NDL-011) ---------------------------------------------------------------------------------------
# Each is a game icon from the player's own install (never an image file in the repository or the package), cropped
# to a square: (x, y) is the crop's centre as fractions of the image, and size a fraction of its shorter side. Found
# by searching the game's Triple Triad cards, quest illustrations and duty art. The user approved every pick on
# 2026-11-15 from a review page showing each crop beside its source image. An entity without a portrait keeps its
# category shape: the Waking Sands has no usable image in the game data.
PORTRAITS = {
    "char-tataru": (87019, 0.42, 0.36, 0.72, "Triple Triad card #19"),
    "char-livia": (87031, 0.45, 0.42, 0.75, "Triple Triad card #31"),
    "char-thancred": (87046, 0.52, 0.40, 0.75, "Triple Triad card #46"),
    "char-yshtola": (87049, 0.50, 0.45, 0.75, "Triple Triad card #49"),
    "char-urianger": (87050, 0.50, 0.42, 0.75, "Triple Triad card #50"),
    "char-minfilia": (87056, 0.52, 0.40, 0.75, "Triple Triad card #56"),
    "char-lahabrea": (87057, 0.50, 0.42, 0.75, "Triple Triad card #57 (the masked Ascian, as first seen)"),
    "char-cid": (87058, 0.48, 0.38, 0.75, "Triple Triad card #58"),
    "char-alphinaud": (87059, 0.30, 0.36, 0.55, "Triple Triad card #59 (shared with Alisaie), left half"),
    "char-alisaie": (87059, 0.66, 0.40, 0.55, "Triple Triad card #59 (shared with Alphinaud), right half"),
    "char-louisoix": (87060, 0.52, 0.38, 0.75, "Triple Triad card #60"),
    "char-gaius": (87064, 0.50, 0.38, 0.80, "Triple Triad card #64"),
    "org-scions": (100073, 0.50, 0.50, 1.00, "Quest illustration, The Scions of the Seventh Dawn (2.0)"),
    "org-eorzean-alliance": (100164, 0.50, 0.50, 1.00, "Quest illustration, The Black Wolf's Ultimatum (MSQ #156)"),
    "org-crystal-braves": (100316, 0.68, 0.55, 1.00, "Quest illustration, Traitor in the Midst (2.4)"),
    "loc-rising-stones": (100177, 0.62, 0.50, 1.00, "Quest illustration, Build on the Stone (2.1)"),
    "evt-operation-archon": (112016, 0.37, 0.45, 1.00, "Duty art, Castrum Meridianum"),
    "evt-black-wolfs-challenge": (100163, 0.17, 0.50, 1.00, "Quest illustration, Escape from Castrum Centri (MSQ #155)"),
}

import portraits_later
assert not set(portraits_later.PORTRAITS) & set(PORTRAITS), "portrait defined twice"
PORTRAITS.update(portraits_later.PORTRAITS)

def portrait_record(eid):
    icon, x, y, size, source = PORTRAITS[eid]
    record = {"gameIcon": icon, "crop": {"x": x, "y": y, "size": size}}
    return with_review(("portrait", eid), record, {"source": source})

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
    # NDL-011 portraits: the user approved all 18 picks ("all good!", 2026-11-15) from the candidate review page.
    ('portrait', 'char-minfilia'): '9cb488e506aa0c61d09890bd',
    ('portrait', 'char-thancred'): '49e143665e649e434f9845b0',
    ('portrait', 'char-yshtola'): 'bd90200535870aeec58746cc',
    ('portrait', 'char-urianger'): '999ef70275b3025e90a805b8',
    ('portrait', 'char-alphinaud'): '0f029343c44498998227462a',
    ('portrait', 'char-alisaie'): 'b899ad8b980ca1618d86a785',
    ('portrait', 'char-louisoix'): 'ef326a23ee9e3f11b35a9b34',
    ('portrait', 'char-tataru'): '9c1b41d4d4bb46b7c9ef16b8',
    ('portrait', 'org-scions'): '942fc3cc48bee2c6cd704e59',
    ('portrait', 'org-crystal-braves'): '779cde58a8de9e22653f6450',
    ('portrait', 'loc-rising-stones'): '331a57ebe003bc54f8c7e55d',
    ('portrait', 'evt-black-wolfs-challenge'): 'd7008477a8d90c07a08b12b4',
    ('portrait', 'evt-operation-archon'): 'fcbebcf61000a478070f0ad2',
    ('portrait', 'char-cid'): '3827b678df980b90f781caed',
    ('portrait', 'char-gaius'): '1e0891737c32d45e587b0f1d',
    ('portrait', 'char-livia'): '98b76b1692eb82f7499d793b',
    ('portrait', 'char-lahabrea'): '4464efc5029b3fbadc098364',
    ('portrait', 'org-eorzean-alliance'): 'c5f30fa37132d1290c6a490e',
    # NDL-012 (ARR 2.0, MSQ #102–#154): accepted by the user on 2026-11-17; recorded mechanically from --print-pending.
    ('presentation', 'char-minfilia', 'cp-msq-102', 'main'): '38092783d73727e7638c3fad',
    ('presentation', 'char-minfilia', 'cp-msq-106', 'main'): '94c3f152c3091e4c3a987fa8',
    ('presentation', 'char-minfilia', 'cp-msq-142', 'main'): '94e0cc54939c6261ffc06351',
    ('presentation', 'char-minfilia', 'cp-msq-149', 'main'): '9e2cd3f504e1d8936dbed4d6',
    ('presentation', 'char-thancred', 'cp-msq-102', 'main'): '179a03085fe291577377e010',
    ('presentation', 'char-yshtola', 'cp-msq-102', 'main'): 'd8d54d61621910c1b57b6947',
    ('presentation', 'char-yshtola', 'cp-msq-103', 'main'): '6248c2acb3bda09388c3c798',
    ('presentation', 'char-yshtola', 'cp-msq-105', 'main'): '9d2800a54bafb2a9ce7835f1',
    ('presentation', 'char-yshtola', 'cp-msq-142', 'main'): 'e059858875eca00ebc1a6818',
    ('presentation', 'char-yshtola', 'cp-msq-143', 'main'): '301d3602365239888179e8f8',
    ('presentation', 'char-yshtola', 'cp-msq-147', 'main'): '1e3e0940bb7d4209130698ab',
    ('presentation', 'char-yshtola', 'cp-msq-155', 'main'): 'c1cbfea1fba1a6c6ebe68135',
    ('presentation', 'char-urianger', 'cp-msq-102', 'main'): 'ea0287f214e9fb387aa2138d',
    ('presentation', 'char-urianger', 'cp-msq-143', 'main'): '5a1816c7cff24f42906587a2',
    ('presentation', 'char-urianger', 'cp-msq-155', 'main'): 'b4761649fd0af497c7e1ff46',
    ('presentation', 'char-alphinaud', 'cp-msq-102', 'main'): 'c15242eaad963c1290c9947a',
    ('presentation', 'char-alphinaud', 'cp-msq-110', 'main'): 'c26c70ac450e374f3aee4998',
    ('presentation', 'char-alphinaud', 'cp-msq-129', 'main'): 'c7d83f4d323485fe18e3873f',
    ('presentation', 'char-alphinaud', 'cp-msq-141', 'main'): '5fc1e2ffba57ee970e66c28d',
    ('presentation', 'char-alphinaud', 'cp-msq-142', 'main'): '67f4e50217c71c78d4df66fe',
    ('presentation', 'char-tataru', 'cp-msq-102', 'main'): '90c2ee239778b0358cdabf51',
    ('presentation', 'char-tataru', 'cp-msq-143', 'main'): '928435a2e2ca9233ea6fbb3c',
    ('presentation', 'char-tataru', 'cp-msq-155', 'main'): '80a0d5e72a2d8c670a20225a',
    ('presentation', 'org-scions', 'cp-msq-102', 'main'): '41e33c21f788f63f1da0b1c5',
    ('presentation', 'org-scions', 'cp-msq-106', 'main'): '6474790462121359029b1d06',
    ('presentation', 'org-scions', 'cp-msq-110', 'main'): 'c41cac5ccf4455ef12565dbc',
    ('presentation', 'org-scions', 'cp-msq-141', 'main'): 'b1b0d1c7ceb4ceb05b66d1cc',
    ('presentation', 'org-scions', 'cp-msq-142', 'main'): 'b3ebb4c1f0192bac5d87a031',
    ('presentation', 'loc-waking-sands', 'cp-msq-102', 'main'): 'd1718b71e3c5f44b6c5ac7d1',
    ('presentation', 'loc-waking-sands', 'cp-msq-106', 'main'): '677e97d1c6aa4a8adc129bce',
    ('presentation', 'loc-waking-sands', 'cp-msq-142', 'main'): '24bdafe49b4651a47dcded6d',
    ('presentation', 'char-cid', 'cp-msq-110', 'main'): '5c3d26363fc332b756b640c0',
    ('presentation', 'char-cid', 'cp-msq-129', 'main'): '29f05c0ed6a1de1907bc5c85',
    ('presentation', 'char-cid', 'cp-msq-130', 'main'): '8c22b92322af912c76fb914a',
    ('presentation', 'char-cid', 'cp-msq-141', 'main'): '16241a4fa36deda65ae0d608',
    ('presentation', 'char-cid', 'cp-msq-147', 'main'): 'e973a3968665a703d5be48d5',
    ('presentation', 'char-cid', 'cp-msq-148', 'main'): '5b2ea6d2863b00414635edab',
    ('presentation', 'char-gaius', 'cp-msq-141', 'main'): '27bcb11d5483d3a91ae6f676',
    ('presentation', 'char-gaius', 'cp-msq-143', 'main'): '369bd0c17378b6c7a3ae03c4',
    ('presentation', 'char-livia', 'cp-msq-106', 'main'): '6826cd112de684e18d837779',
    ('presentation', 'char-lahabrea', 'cp-msq-105', 'main'): 'f7d0542ded69f4a043e60c0f',
    ('presentation', 'char-lahabrea', 'cp-msq-129', 'main'): '620f5d39b1a87651f7895b7d',
    ('presentation', 'char-lahabrea', 'cp-msq-141', 'main'): '56d178c8581d71121676de8c',
    ('presentation', 'evt-road-to-titan', 'cp-msq-103', 'main'): 'c15b12cf09507bd7d3022764',
    ('presentation', 'evt-road-to-titan', 'cp-msq-104', 'main'): '98e2fe26a5dccc521c2a5afe',
    ('presentation', 'evt-road-to-titan', 'cp-msq-105', 'main'): '436c34cb7b55f77ff58408e5',
    ('presentation', 'evt-fall-of-the-waking-sands', 'cp-msq-106', 'main'): '5f1d1597d035a3f728c511aa',
    ('presentation', 'evt-fall-of-the-waking-sands', 'cp-msq-107', 'main'): '0167cd8169b06f041853b656',
    ('presentation', 'evt-fall-of-the-waking-sands', 'cp-msq-108', 'main'): '6afae35f6dc68c7869647245',
    ('presentation', 'evt-fall-of-the-waking-sands', 'cp-msq-109', 'main'): 'd70038b6569636e09e809ea4',
    ('presentation', 'evt-fall-of-the-waking-sands', 'cp-msq-110', 'main'): 'cf876dde5b6276f65eb93c85',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-110', 'main'): '2470f73e602f194ca6112ac3',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-111', 'main'): '863ea931806fda6997007555',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-112', 'main'): 'bfe4a965c40657309f25ffcf',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-113', 'main'): '7af5d4fee2f47fba3f6b9ea2',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-114', 'main'): 'f7d83b0fc79761cb8883ed0e',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-115', 'main'): '4fe283b871e6180a8b23bf17',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-116', 'main'): 'eda8d0715854162db984cb10',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-117', 'main'): '834d1e9c5d65199f2dbc94a7',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-118', 'main'): '42d011d6b18846c655fd1dc5',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-119', 'main'): 'dbdd0bd8049dbee78ec3c357',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-120', 'main'): '362b1aed8e930dbd2612ee1b',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-121', 'main'): '65dcd9d7f2f26fda6c2eea4c',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-122', 'main'): 'd9145f32ce952cd5a3d1cfce',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-123', 'main'): '68c4a1eb815eb19f15718f5a',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-124', 'main'): '18869d4a7bf0781d432a98d1',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-125', 'main'): '294aefe2bc8cb7008a46b5a9',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-126', 'main'): '064750b1b4f0d63130a19812',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-127', 'main'): 'b4eec2f33a072354ab0b3673',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-128', 'main'): '0a34ccb5aafa9b2ded319265',
    ('presentation', 'evt-search-for-the-enterprise', 'cp-msq-129', 'main'): 'ccc3a63be90e58d670b58ce0',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-130', 'main'): 'ca5e1c851e0bb7095d451583',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-131', 'main'): 'ebd2096ddb57d6dd0e933ebb',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-132', 'main'): '6f484792f09e190d6deaecf1',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-133', 'main'): '8a6347b670e82db1e785920d',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-134', 'main'): '2b2273f5cf4099d82efd4234',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-135', 'main'): 'edbf3af0a4863bc93b6dd213',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-136', 'main'): '7f413fa8fdd1ac8340d17bbc',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-137', 'main'): 'fd79524382ca21fffd1c93d2',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-138', 'main'): '56b916f58338d2fb515f7b2a',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-139', 'main'): 'cfe048665705482a8345da4b',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-140', 'main'): 'bac32d801ea374032a1d695e',
    ('presentation', 'evt-garudas-barrier', 'cp-msq-141', 'main'): '07fdbc41f3add8e69866c2d8',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-142', 'main'): '3f3af11b236acd73f5aa4f0a',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-143', 'main'): '45b852fe92ab0bb9d3b8c97d',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-144', 'main'): '33c5dcf9c34e607932734681',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-145', 'main'): '6dbac51f7efca9ea2aa31d1f',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-146', 'main'): 'ee9c68d08b6042ef3aa00999',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-147', 'main'): '601b3fc1cc4d210fc6152d2c',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-148', 'main'): 'b61bd97854267c05257c1222',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-149', 'main'): 'ade4a135460dc5491cf4db60',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-150', 'main'): 'ff447f6c6314c0e52f7355d0',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-150b', 'main'): 'ef527364520108e4440ca2eb',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-151', 'main'): '57dba2e08dffb4f74b7da797',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-153', 'main'): 'cecb306fb04b2ef5dc82a111',
    ('presentation', 'evt-road-to-castrum-centri', 'cp-msq-154', 'main'): '82d1b2fa0cea548778290f44',
    ('presentation', 'char-yda', 'cp-msq-102', 'main'): 'a107d073fc77c57faec66be5',
    ('presentation', 'char-yda', 'cp-msq-142', 'main'): '3440ae06ff3e066e3d81ad39',
    ('presentation', 'char-yda', 'cp-msq-147', 'main'): '58f52b362cb1cae1455c6a56',
    ('presentation', 'char-yda', 'cp-msq-155', 'main'): '8c71ae20c93ac137c09d1e35',
    ('presentation', 'char-papalymo', 'cp-msq-102', 'main'): 'c0cbde7c2f6ad66345ae863e',
    ('presentation', 'char-papalymo', 'cp-msq-142', 'main'): '62decbbfed99672782f58452',
    ('presentation', 'char-papalymo', 'cp-msq-143', 'main'): 'a60d1a8cdc1f628a198f6958',
    ('presentation', 'char-papalymo', 'cp-msq-155', 'main'): '88488f3183b397911655ed1a',
    ('presentation', 'char-titan', 'cp-msq-103', 'main'): '5a682f209706cfc9a5515a25',
    ('presentation', 'char-titan', 'cp-msq-105', 'main'): 'e793c02e8567fd0761887ae5',
    ('presentation', 'char-titan', 'cp-msq-141', 'main'): '7caad5f6c0f7a005d773e650',
    ('presentation', 'char-rhitahtyn', 'cp-msq-105', 'main'): 'f66ce0102945cc6c1d8cc5de',
    ('presentation', 'char-rhitahtyn', 'cp-msq-143', 'main'): '8b367f5bf1d5c256aa020d0a',
    ('presentation', 'char-rhitahtyn', 'cp-msq-157', 'main'): '3e72fc97de89e20a4ade8478',
    ('presentation', 'char-noraxia', 'cp-msq-106', 'main'): '3a4f0c7e3fc46f0ef3ef0311',
    ('presentation', 'char-noraxia', 'cp-msq-109', 'main'): 'fe967bf01b6f904d6d821e66',
    ('presentation', 'char-iliud', 'cp-msq-106', 'main'): 'dd29758be8ce7a72fe5f987b',
    ('presentation', 'char-iliud', 'cp-msq-110', 'main'): '0f6cf99a49cd72d6cf27375f',
    ('presentation', 'char-marques', 'cp-msq-106', 'main'): 'd65487b1d6b4c0783e87f4ff',
    ('presentation', 'char-marques', 'cp-msq-107', 'main'): '3b6fd68322d88a7857d7c376',
    ('presentation', 'char-marques', 'cp-msq-110', 'main'): '85247727388d6509ebf1748c',
    ('presentation', 'char-garuda', 'cp-msq-110', 'main'): 'b27dd164cb1ab86b59f339ba',
    ('presentation', 'char-garuda', 'cp-msq-129', 'main'): '1946ee4b7491eafd7f4222bc',
    ('presentation', 'char-garuda', 'cp-msq-130', 'main'): '5814eca06b46b6dde0f8b106',
    ('presentation', 'char-garuda', 'cp-msq-141', 'main'): 'a16f77fe8bcf938b11de3cbb',
    ('presentation', 'char-francel', 'cp-msq-115', 'main'): '90bb6aa5e8dd1f7286070e92',
    ('presentation', 'char-francel', 'cp-msq-116', 'main'): '301cc6c461d22c54648cdbd5',
    ('presentation', 'char-francel', 'cp-msq-118', 'main'): '9fc28bdb0920246387133395',
    ('presentation', 'char-francel', 'cp-msq-120', 'main'): 'ef08c8fe79d6d66418e6a755',
    ('presentation', 'char-haurchefant', 'cp-msq-116', 'main'): '31a7f6a215c37a3de62d2558',
    ('presentation', 'char-haurchefant', 'cp-msq-118', 'main'): '18b2079fe2e83ec5dd0e177a',
    ('presentation', 'char-haurchefant', 'cp-msq-120', 'main'): '16f75ca676548bf8b330160b',
    ('presentation', 'char-haurchefant', 'cp-msq-121', 'main'): 'dc5b850e78bd725f3936c981',
    ('presentation', 'char-guillaime', 'cp-msq-113', 'main'): '47d31539b37d8e720543965b',
    ('presentation', 'char-guillaime', 'cp-msq-117', 'main'): 'a7c2965dc91d0a4e1fe47106',
    ('presentation', 'char-guillaime', 'cp-msq-120', 'main'): 'b20a936d6a02e70bfa2300da',
    ('presentation', 'char-guillaime', 'cp-msq-122', 'main'): 'b0de4e292d9c2abc1e2b8e4f',
    ('presentation', 'char-guillaime', 'cp-msq-124', 'main'): 'e3f3c0c7ee1133a261dbbdc6',
    ('presentation', 'char-guillaime', 'cp-msq-126', 'main'): 'c3e19f4be486e37fb64f4373',
    ('presentation', 'char-guillaime', 'cp-msq-127', 'main'): 'ca3705d922a108eba4756d92',
    ('presentation', 'char-guillaime', 'cp-msq-128', 'main'): '98b16f02c56d9114a6d3a364',
    ('presentation', 'char-drillemont', 'cp-msq-121', 'main'): '78a563d70414446bb32a0dac',
    ('presentation', 'char-drillemont', 'cp-msq-122', 'main'): 'a147cb0154b5933c2e7d3326',
    ('presentation', 'char-drillemont', 'cp-msq-127', 'main'): '9c82fbda8800167d724b9124',
    ('presentation', 'char-drillemont', 'cp-msq-128', 'main'): 'a769274be17b43aea9717b5d',
    ('presentation', 'char-biggs', 'cp-msq-143', 'main'): 'b325f219cc4e9d2e8bb1771a',
    ('presentation', 'char-biggs', 'cp-msq-145', 'main'): '329baae9143419f1edeb592c',
    ('presentation', 'char-biggs', 'cp-msq-147', 'main'): '5670ccd565158a9c93e0a005',
    ('presentation', 'char-biggs', 'cp-msq-153', 'main'): 'dc0597b6aeafdc26a1a61a72',
    ('presentation', 'char-wedge', 'cp-msq-143', 'main'): '227ffb18df24e4bae506a62c',
    ('presentation', 'char-wedge', 'cp-msq-145', 'main'): '0d6b8760f32d39fda0bdb68b',
    ('presentation', 'char-wedge', 'cp-msq-147', 'main'): '39c73dba5aa33cb72dc63b50',
    ('presentation', 'char-wedge', 'cp-msq-153', 'main'): '692e3ef417faa54d41d71fd7',
    ('presentation', 'char-glaumunt', 'cp-msq-148', 'main'): '6f22a0e3a0f576a98ddad58d',
    ('presentation', 'char-glaumunt', 'cp-msq-149', 'main'): '9b8a60a1a941a1ceb278145c',
    ('presentation', 'char-glaumunt', 'cp-msq-153', 'main'): '03a26ec3f5f0863ef4df5158',
    ('presentation', 'org-company-of-heroes', 'cp-msq-103', 'main'): '82db772acc1a2fd663dbfb09',
    ('presentation', 'org-company-of-heroes', 'cp-msq-105', 'main'): '110acbce30f6dabaa287a961',
    ('presentation', 'org-garlean-empire', 'cp-msq-102', 'main'): '5094305d737f99b57e16a52d',
    ('presentation', 'org-garlean-empire', 'cp-msq-105', 'main'): 'f6ef053e4781daaddac0ac8e',
    ('presentation', 'org-garlean-empire', 'cp-msq-106', 'main'): 'feb7a1994807b325277eeb80',
    ('presentation', 'org-garlean-empire', 'cp-msq-141', 'main'): '888a691432c66a62231ae09e',
    ('presentation', 'org-house-haillenarte', 'cp-msq-115', 'main'): '869cbc9af1d1f07581c29ac0',
    ('presentation', 'org-house-haillenarte', 'cp-msq-117', 'main'): 'ac4e3df774dcbd32149f38b6',
    ('presentation', 'org-house-haillenarte', 'cp-msq-119', 'main'): 'b87eba7c4cf9659c83e55d8b',
    ('presentation', 'org-house-haillenarte', 'cp-msq-121', 'main'): '4f4c936969a8aed0e239d928',
    ('presentation', 'org-house-haillenarte', 'cp-msq-127', 'main'): '88d9687ad70ee5ed4805b013',
    ('presentation', 'org-ixal', 'cp-msq-110', 'main'): 'af224faae4a7c6be8409f169',
    ('presentation', 'org-ixal', 'cp-msq-141', 'main'): 'a424b8556381bb7c83dbb1c7',
    ('presentation', 'loc-castrum-centri', 'cp-msq-142', 'main'): 'ff2b00396e7cd9a7de37bc3c',
    ('presentation', 'loc-castrum-centri', 'cp-msq-143', 'main'): '6e32ccd2018dd04b81ca69eb',
    ('presentation', 'loc-castrum-centri', 'cp-msq-148', 'main'): '7cc37c3615c288ac09ded8f4',
    ('presentation', 'loc-castrum-centri', 'cp-msq-155', 'main'): '7391726da0a3722cc43b5c65',
    ('relationship', 'rel-minfilia-leads-scions-arr'): '15c1f25693de0dd3b303e230',
    ('relationship', 'rel-thancred-member-scions-arr'): '5f5b94a1dcb1a04ae86bcc7f',
    ('relationship', 'rel-yshtola-member-scions-arr'): '959dee04796cc239fd9f335d',
    ('relationship', 'rel-urianger-member-scions-arr'): 'e463bc6169d1808072789867',
    ('relationship', 'rel-tataru-member-scions-arr'): 'b34f2115961938ba024f0607',
    ('relationship', 'rel-alphinaud-member-scions-arr'): 'c7c5f1ada08781a3ee9bc33e',
    ('relationship', 'rel-scions-hq-waking-sands-arr'): '2a0db10b594e3484ed655426',
    ('relationship', 'rel-minfilia-prisoner-livia-arr'): '43fd6582e12536026291638e',
    ('relationship', 'rel-yda-member-scions'): 'edca0f6d09bdb524384e12a4',
    ('relationship', 'rel-papalymo-member-scions'): 'a589e10c929a92e1707a5355',
    ('relationship', 'rel-lahabrea-allied-empire'): 'd45e087388121aa89107d8d1',
    ('relationship', 'rel-livia-member-empire'): 'bbee8e250178e5e03153c8bf',
    ('relationship', 'rel-iliud-aids-scions'): '64d38c446680ca504f4d282a',
    ('relationship', 'rel-marques-revealed-cid'): '743004e94300294d4a33b34d',
    ('relationship', 'rel-garuda-summoned-ixal'): 'c153770f7701a4f89edd1525',
    ('relationship', 'rel-francel-member-haillenarte'): 'aa9a5e0773c718dd2feb4255',
    ('relationship', 'rel-haurchefant-aids-francel'): '13b790e4f81832a6d34787a7',
    ('relationship', 'rel-guillaime-opposes-alphinaud'): '9b00884ecc6142338b43f188',
    ('relationship', 'rel-drillemont-aids-alphinaud'): 'd530c3a2b433468a7ef641d8',
    ('relationship', 'rel-gaius-member-empire'): '9bf05bb0df55ed39bd07e915',
    ('relationship', 'rel-minfilia-held-castrum-centri'): 'eec3b9af1bf10df3b344cc73',
    ('relationship', 'rel-urianger-held-castrum-centri'): 'c4589510251717625395e332',
    ('relationship', 'rel-papalymo-held-castrum-centri'): 'e8c9f8f3f1210e48f980010f',
    ('relationship', 'rel-tataru-held-castrum-centri'): '5adfb9f955547f6fe5405d82',
    ('relationship', 'rel-rhitahtyn-serves-gaius'): '4b0e1a6dd22383709cb449fd',
    ('relationship', 'rel-biggs-serves-cid'): '8ec4f4ed8211cf5f556d8097',
    ('relationship', 'rel-wedge-serves-cid'): 'c49cc0aadc8ff78eb0dc5774',
    ('relationship', 'rel-glaumunt-aids-scions'): 'd29b24d42ccfa4dc094a7d23',
    ('relationship', 'p-yshtola-b1'): '1be99a85f7504d118abaca56',
    ('relationship', 'p-company-of-heroes-b1'): '5c6928c467578466d4806909',
    ('relationship', 'p-titan-b1'): '8aa1e59f4c19eb19da7e0194',
    ('relationship', 'p-rhitahtyn-b1'): 'd9f8e2b09e6f14f0980dfe68',
    ('relationship', 'p-lahabrea-b1'): '37d188c1172cef26aa9ec9cd',
    ('relationship', 'p-garlean-empire-b1'): '5f281a2d47a464ddaee51421',
    ('relationship', 'p-minfilia-b2'): '879b57a05d8372be9825e2e2',
    ('relationship', 'p-scions-b2'): 'bf22d6138c67df54d7d73afc',
    ('relationship', 'p-waking-sands-b2'): '6092147759731d9d9302701c',
    ('relationship', 'p-livia-b2'): '2afd1fc4cf9125b53eed214c',
    ('relationship', 'p-garlean-empire-b2'): 'a536e07885a9ea7afd228067',
    ('relationship', 'p-noraxia-b2'): 'b47f313cb6014ace4f51e0a9',
    ('relationship', 'p-iliud-b2'): '4ac30dc5d73803a83cd3daa9',
    ('relationship', 'p-marques-b2'): 'd25fc1080adcddd78db3090f',
    ('relationship', 'p-alphinaud-b2'): '9272c4f55af885219edce149',
    ('relationship', 'p-cid-b2'): '7dbdb28842895e91571f0af4',
    ('relationship', 'p-alphinaud-b3'): '3832b251978ecc8257d9b7bb',
    ('relationship', 'p-cid-b3'): '31a8d517db95033abf8cf30f',
    ('relationship', 'p-garuda-b3'): 'c087ced7c3a8db425f35f15f',
    ('relationship', 'p-ixal-b3'): '5aec8504e3626ff581bea82a',
    ('relationship', 'p-guillaime-b3'): 'ef0300503a8dbb50fda9e7b3',
    ('relationship', 'p-francel-b3'): 'e5f3f1cb766b3afdcb150e07',
    ('relationship', 'p-house-haillenarte-b3'): '1642a90d0beabe42c5453ff8',
    ('relationship', 'p-haurchefant-b3'): '3529f4c3123b58027901afd5',
    ('relationship', 'p-drillemont-b3'): 'a98ff0695ae4c27be9940aac',
    ('relationship', 'p-lahabrea-b3'): 'bb1af98485e8f31494c2bf9a',
    ('relationship', 'p-cid-b4'): '0f8cd439bcf91e905812a041',
    ('relationship', 'p-alphinaud-b4'): '1bd7ab839632b5e1022c7bd5',
    ('relationship', 'p-garuda-b4'): '61490782978d4b9ba10e2891',
    ('relationship', 'p-ixal-b4'): '766e9805fa2dfe0628a4f51b',
    ('relationship', 'p-titan-b4'): 'ac64aaf468088dd963a20628',
    ('relationship', 'p-gaius-b4'): '234a4066de7653adaec8b45f',
    ('relationship', 'p-garlean-empire-b4'): 'efe86096ec025f740ed0b4dd',
    ('relationship', 'p-scions-b4'): '859a0da58f4800cef602489a',
    ('relationship', 'p-alphinaud-b5'): '053b824ea194c6843f0b7278',
    ('relationship', 'p-cid-b5'): '1b6cec342f69b80ba9f31531',
    ('relationship', 'p-yda-b5'): '3057a54c0ffbc5dac0d414c6',
    ('relationship', 'p-yshtola-b5'): '1cf9ca6496a11e4f40c1688c',
    ('relationship', 'p-minfilia-b5'): '260d2cd2cb9910eaabd1b893',
    ('relationship', 'p-scions-b5'): '3c65601feb493ba66b3408c8',
    ('relationship', 'p-castrum-centri-b5'): '4e9689f6798343d728be244a',
    ('relationship', 'p-biggs-b5'): '989c6cfc251bd4a6083573fc',
    ('relationship', 'p-wedge-b5'): '5b97c47a2ade2032349c8c7d',
    ('relationship', 'p-glaumunt-b5'): '0d48d9eb0b33a44042af120a',
}

# Records accepted after NDL-012 (the post-2.0 eras): written by --accept-pending, keyed like ACCEPTED. The user waived
# the per-story acceptance gate for Atlas content on 2026-11-19 ("abandon the story approach"), so the lead records these
# after verification: every locator checked by script against the saved wiki pages, and the lint and host tests green.
ACCEPTED_LATER_FILE = pathlib.Path(__file__).with_name("accepted_later.json")
ACCEPTED_LATER = {tuple(k): v for k, v in json.loads(ACCEPTED_LATER_FILE.read_text())} if ACCEPTED_LATER_FILE.exists() else {}
ACCEPTED_CORE = dict(ACCEPTED)  # the records the user accepted story by story (NDL-003 to NDL-012)
ACCEPTED.update(ACCEPTED_LATER)

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
    {"id": eid, "category": cat, **({"portrait": portrait_record(eid)} if eid in PORTRAITS else {}), "presentations": [
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
EMITTED_KEYS = {("presentation", e["id"], pr["validFrom"], pr["scope"]) for e in doc["entities"] for pr in e["presentations"]} | {("relationship", r["id"]) for r in doc["relationships"]} | {("portrait", e["id"]) for e in doc["entities"] if "portrait" in e}
assert LINT_ONLY or set(PORTRAITS) <= {e["id"] for e in doc["entities"]}, "PORTRAITS names an unknown entity"
MISSING = missing_accepted(ACCEPTED_CORE, EMITTED_KEYS)  # stale ACCEPTED_LATER keys are dropped by --accept-pending
if MISSING:
    sys.exit(f"ACCEPTED lists records that no longer exist: {MISSING}")

# ---- Lint (--lint): the content rules the host tests enforce, checked fast in Python -------------------------------
BANNED_NAMES = [  # case-sensitive whole words (RealDataTests.BannedNames)
    "Warde", "Waters", "Rhul", "Augurelt", "Leveilleur", "Taru", "Totolymo", "Hext", "Ascilia", "Ascilla",
    "Lyse", "Ryne", "Exarch", "Emet-Selch", "Hythlodaeus", "Hades", "Lightwarden", "Wyrmblood", "The First",
    "Garlond", "Baelsar", "Junius", "Scaeva", "Arvina", "Midas", "Nero", "Zodiark", "Nabriales", "Igeyorhm", "Pashtarot",
]
BANNED_PHRASES = [  # case-insensitive (RealDataTests.BannedPhrases)
    "Oracle of Light", "Word of the Mother", "Warrior of Darkness", "Warriors of Darkness", "Heavensward",
    "Shadowbringers", "Stormblood", "Endwalker", "Bahamut stirs", "the Reckoning", "Dark One", "new primal",
]
# A banned term may appear from the step named here (mirrored in RealDataTests.AllowedFrom). Era modules may propose
# more in ALLOW; the lead copies the accepted ones here.
ALLOWED_FROM = {  # accepted by the lead on 2026-11-19, each from the step where the pages establish it
    "Nabriales": "cp-msq-224", "Warriors of Darkness": "cp-msq-340", "Warrior of Darkness": "cp-msq-340",
    "Word of the Mother": "cp-msq-345", "Nero": "cp-msq-376", "Lyse": D3, "Heavensward": C3,
    # Shadowbringers: each from the earliest step any era's pages establish it (the eras' ALLOW proposals, reconciled).
    "Exarch": "cp-msq-542", "The First": "cp-msq-542", "Oracle of Light": "cp-msq-543", "Lightwarden": "cp-msq-563",
    "Emet-Selch": "cp-msq-584", "Zodiark": "cp-msq-603", "Ryne": "cp-msq-620", "Hythlodaeus": "cp-msq-646", "Hades": G5,
}
for _mod, M in ERA_MODULES:
    for term, step in getattr(M, "ALLOW", {}).items():
        ALLOWED_FROM.setdefault(term, step)

def _texts_of_presentation(p):
    """(text, is_citation) pairs. A citation shows its quest's title, which is public and only appears once that quest
    is reached, so the banned-name lists don't apply to it (Still Waters, Shadows of the First, Heavensward)."""
    yield p["name"], False; yield p["summary"], False
    for a in p["aliases"]:
        yield a, False
    for k in cites(p["claims"]):
        yield SRC[k]["title"], True; yield urllib.parse.unquote(url(k)).replace("_", " "), True

def lint():
    errs = list(LINT_ERRORS)
    later_titles = {}  # step index -> quest titles of later steps
    titles = [(IDX[c["id"]], c["questTitle"]) for c in CHECKPOINTS if c.get("questTitle")]
    first_known = {}
    for eid, _, pres in ENT:
        for p in pres:
            for n in [p["name"], *p["aliases"]]:
                first_known[n] = min(first_known.get(n, 10**6), IDX[p["frm"]])
    def check_text(where, at, text, citation=False):
        for i, title in titles:
            if i > at and title in text:
                errs.append(f"{where}: names a later quest, {title!r} ({ORDER[i]}): {text[:140]}")
        for n, i in first_known.items():
            if i > at and n in text:
                errs.append(f"{where}: names {n!r} before it is visible (from {ORDER[i]}): {text[:140]}")
        for n in ([] if citation else BANNED_NAMES):
            if re.search(rf"(?<![\w-]){re.escape(n)}(?![\w-])", text) and not (n in ALLOWED_FROM and at >= IDX[ALLOWED_FROM[n]]):
                errs.append(f"{where}: banned name {n!r}: {text[:140]}")
        for n in ([] if citation else BANNED_PHRASES):
            if n.lower() in text.lower() and not (n in ALLOWED_FROM and at >= IDX[ALLOWED_FROM[n]]):
                errs.append(f"{where}: banned phrase {n!r}: {text[:140]}")
        for bad in ("[[", "]]", "''", "[Forename]", "<<", "Forename", "{{"):
            if bad in text and not text.startswith("https://"):
                errs.append(f"{where}: wiki markup or placeholder {bad!r}: {text[:140]}")
    type_ids = {i for i, *_ in TYPES}
    cat = {eid: c for eid, c, _ in ENT}
    vis = {}
    for eid, _, pres in ENT:
        if not pres:
            errs.append(f"{eid}: has no presentations"); continue
        if len(pres) > 512:
            errs.append(f"{eid}: {len(pres)} presentations (max 512)")
        if len(eid) > 64:
            errs.append(f"{eid}: id longer than 64")
        for p in pres:
            where = f"{eid} @{p['frm']} {p['scope']}"
            if p["frm"] not in IDX or (p["until"] is not None and p["until"] not in IDX):
                errs.append(f"{where}: unknown step"); continue
            if len(p["summary"]) > 1200: errs.append(f"{where}: summary longer than 1200")
            if len(p["name"]) > 80 or any(len(a) > 80 for a in p["aliases"]): errs.append(f"{where}: name or alias longer than 80")
            if len(p["aliases"]) > 8: errs.append(f"{where}: more than 8 aliases")
            if not 1 <= len(cites(p["claims"])) <= 8: errs.append(f"{where}: needs 1–8 distinct sources, has {len(cites(p['claims']))}")
            for text, citation in _texts_of_presentation(p):
                check_text(where, IDX[p["frm"]], text, citation)
            end = len(ORDER) if p["until"] is None else IDX[p["until"]]
            for i in range(IDX[p["frm"]], end):
                vis.setdefault((eid, p["scope"]), set()).add(i)
    def visible(eid, scope, i):
        return i in vis.get((eid, "main"), ()) or (scope == "optional" and i in vis.get((eid, "optional"), ()))
    triples = {}
    for r in RELS:
        rid, s, ty, g, f, u, sc, cl, _, end = rel_parts(r)
        where = f"{rid}"
        if len(rid) > 64: errs.append(f"{where}: id longer than 64")
        if ty not in type_ids: errs.append(f"{where}: unknown type {ty}")
        if s not in cat or g not in cat: errs.append(f"{where}: unknown endpoint"); continue
        if f not in IDX or (u is not None and u not in IDX): errs.append(f"{where}: unknown step"); continue
        hi = len(ORDER) if u is None else IDX[u]
        if hi <= IDX[f]: errs.append(f"{where}: empty interval")
        for i in range(IDX[f], hi):
            if not (visible(s, sc, i) and visible(g, sc, i)):
                errs.append(f"{where}: endpoint not visible at {ORDER[i]}"); break
        for i in range(IDX[f], hi):
            key = (s, ty, g, sc, i)
            if key in triples:
                errs.append(f"{where}: overlaps {triples[key]} (same source, type, target and scope) at {ORDER[i]}"); break
            triples[key] = rid
        if not 1 <= len(cites(cl)) <= 8: errs.append(f"{where}: needs 1–8 distinct sources")
        for k in cites(cl):
            check_text(where, IDX[f], SRC[k]["title"], citation=True)
        if end:
            if u is None:
                errs.append(f"{where}: end claims without validUntil")
            elif CHECKPOINTS[IDX[u] - 1].get("milestone", False) != CHECKPOINTS[IDX[u]].get("milestone", False):
                errs.append(f"{where}: end claims need an ending step where Changes is offered; {u} is next to a milestone boundary")
            if len(cites(end)) > 8: errs.append(f"{where}: more than 8 end sources")
    for aid, entry, f, l in ARCS:
        if cat.get(entry) != "event": errs.append(f"{aid}: entry {entry} is not an event entity")
        if f not in IDX or l not in IDX or IDX[f] > IDX[l]: errs.append(f"{aid}: bad interval"); continue
        if not visible(entry, "main", IDX[f]): errs.append(f"{aid}: entry not visible at its first step")
        members = [(rel_parts(r)[1], IDX[rel_parts(r)[4]]) for r in RELS if rel_parts(r)[2] == "participant-in" and rel_parts(r)[3] == entry]
        for i in range(IDX[f], IDX[l] + 1):
            n = len({m for m, frm in members if frm <= i})
            if n > 10: errs.append(f"{aid}: {n} cast members at {ORDER[i]} (max 10)"); break
    starts = sorted((IDX[f], IDX[l], aid) for aid, _, f, l in ARCS if f in IDX and l in IDX)
    for (f1, l1, a1), (f2, l2, a2) in zip(starts, starts[1:]):
        if f2 <= l1 and l1 - f2 >= 1:
            errs.append(f"{a1} and {a2} overlap on {l1 - f2 + 1} steps; arcs may share at most one step (the earlier one hides the later)")
    return errs

if LINT:
    errs = lint()
    scope = LINT_ONLY or "all eras"
    print(f"lint ({scope}): {len(ERA_MODULES)} era modules, {len(C)} claims, {sum(len(p) for _, _, p in ENT)} presentations, {len(RELS)} relationships, {len(ARCS)} arcs")
    for e in errs:
        print("  " + e)
    if LINT_ONLY:
        print("  (note: only this era is loaded, so ADJUST entries for another era's relationships report as unknown)")
    print("lint: " + ("OK" if not errs else f"{len(errs)} problems"))
    sys.exit(1 if errs else 0)

if VERIFY:
    pages = pathlib.Path(ARGS[1]); bad = []; missing = set(); n = 0
    for k, (_, source, loc) in C.items():
        if ("claim", k) not in ERA_OF:
            continue
        f = pages / (SRC[source]["page"].replace(" ", "_") + ".txt")
        if not f.exists():
            missing.add(f.name); continue
        text = f.read_text()
        for frag in loc.split(" … "):
            n += 1
            if frag not in text:
                bad.append((k, source, frag))
    print(f"verify: {n} locator fragments in {sum(1 for k in C if ('claim', k) in ERA_OF)} era claims; {len(bad)} not found; missing pages: {sorted(missing)}")
    for b in bad:
        print("  ", b)
    sys.exit(1 if bad or missing else 0)

if ACCEPT_PENDING:
    keys = [(("presentation", e["id"], pr["validFrom"], pr["scope"])) for e in doc["entities"] for pr in e["presentations"] if pr["review"] == "pending"]
    keys += [("relationship", r["id"]) for r in doc["relationships"] if r["review"] == "pending"]
    keys += [("portrait", e["id"]) for e in doc["entities"] if e.get("portrait", {}).get("review") == "pending"]
    later = json.loads(ACCEPTED_LATER_FILE.read_text()) if ACCEPTED_LATER_FILE.exists() else []
    # Replace, never duplicate: a record re-accepted after a change keeps only its new fingerprint.
    later = [kv for kv in later if tuple(kv[0]) in EMITTED_KEYS and tuple(kv[0]) not in set(keys)] + [[list(k), FINGERPRINTS[k]] for k in keys]
    ACCEPTED_LATER_FILE.write_text(json.dumps(sorted(later), ensure_ascii=False, indent=0) + "\n")
    print(f"accepted {len(keys)} pending records into {ACCEPTED_LATER_FILE.name}; rerun the build")
    sys.exit(0)

if PRINT_PENDING:
    for e in doc["entities"]:
        for pr in e["presentations"]:
            if pr["review"] == "pending":
                k = ("presentation", e["id"], pr["validFrom"], pr["scope"]); print(f"    {k!r}: {FINGERPRINTS[k]!r},")
    for r in doc["relationships"]:
        if r["review"] == "pending":
            k = ("relationship", r["id"]); print(f"    {k!r}: {FINGERPRINTS[k]!r},")
    for e in doc["entities"]:
        if e.get("portrait", {}).get("review") == "pending":
            k = ("portrait", e["id"]); print(f"    {k!r}: {FINGERPRINTS[k]!r},")
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
    por = copy.deepcopy(next(e["portrait"] for e in doc["entities"] if "portrait" in e)); por.pop("review")
    pokey = ("portrait", "x"); poctx = {"source": "s"}
    poacc = {pokey: fingerprint(por, poctx)}
    check("unchanged accepted portrait stays reviewed", with_review(pokey, copy.deepcopy(por), poctx, poacc)["review"] == "reviewed")
    moved = copy.deepcopy(por); moved["crop"]["x"] += 0.01
    check("a moved crop makes the portrait pending", with_review(pokey, moved, poctx, poacc)["review"] == "pending")
    swapped = copy.deepcopy(por); swapped["gameIcon"] += 1
    check("a different icon makes the portrait pending", with_review(pokey, swapped, poctx, poacc)["review"] == "pending")
    check("every accepted portrait is currently reviewed", all(e["portrait"]["review"] == "reviewed" for e in doc["entities"] if "portrait" in e))
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
PENDING = sum(1 for e in doc["entities"] for pr in e["presentations"] if pr["review"] == "pending") + sum(1 for r in doc["relationships"] if r["review"] == "pending") + sum(1 for e in doc["entities"] if e.get("portrait", {}).get("review") == "pending")
w(f"> **Status: {'REVIEWED' if PENDING == 0 else f'AWAITING HUMAN REVIEW ({PENDING} pending)'}.** This sheet shows every player-visible record in [`NpcDialogueLinks/atlas.json`](../../NpcDialogueLinks/atlas.json), "
  "exactly as written there, with the evidence behind it. Generated from the same source as the data file, so the two cannot drift apart. "
  "AI research and AI review are not canon acceptance: through NDL-012, only your explicit approval marked records `reviewed`. "
  "For the content after 2.0 (patches 2.1–3.56) you waived the per-story acceptance gate on 2026-11-19, so the lead marked it `reviewed` after "
  "checking every locator by script against the saved wiki pages and running the lint and host tests ([era-modules.md](era-modules.md)).\n")
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
w("For A Realm Reborn 2.0 before the Black Wolf (`NDL-012`), the user chose the scope on 2026-11-17 (MSQ #102–#154, with the step bound raised). "
  "The lead decided the rest, and it awaits your review; the reasoning is in [ndl-012-discovery.md](ndl-012-discovery.md#decisions-to-review):\n")
w("11. **Five arcs**: *The Road to Titan* (#103–105), *The Fall of the Waking Sands* (#106–110), *The Search for the Enterprise* (#110–129, sharing #110 with the arc before), *Garuda's Barrier* (#130–141) and *The Road to Castrum Centri* (#142–154, stopping before #155 so the Black Wolf's Challenge stays the default there).")
w("12. **The step bound rises from 16 to 128**: one step per main-scenario quest, both #150 paths included, ordered by MSQ index and then authored order.")
w("13. **Marques is his own entry, with no portrait**, because Cid's portrait shows his later look. From #110 he is *revealed as* Cid, and Cid is searchable as \"Marques\".")
w("14. **Rule 7 above is relaxed**: with #102–#160 covered, text names any entry that is already visible. The leak tests still forbid any name that isn't visible yet, and any later quest title (so the arcs are not named after #105's or #141's quests).")
w("15. **Left out**, as before: Nero, and surnames. The Company of Heroes holds a \"feast\", because \"banquet\" is reserved for the 2.55 story.\n")
w("For the content after 2.0 (patches 2.1–3.56, 2026-11-19), the era authors and the lead recorded these decisions; flag any you want changed:\n")
_n = 16
for _mod, _M in ERA_MODULES:
    for _d in getattr(_M, "DECISIONS", []):
        w(f"{_n}. *({_mod})* {_d}"); _n += 1
w("")
w("## Snapshot overview\n")
w("Visible records at each step, in the main-story view and the main + optional view. Slice steps (#…) cover only the characters involved in the story so far.\n")
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
w("## Portraits\n")
w("Each portrait is a game icon drawn from the player's own install at runtime; no image is stored in the repository or the package. "
  "The user approved NDL-011's picks on 2026-11-15 from a page showing each crop beside its source image; the lead picked the rest on 2026-11-19 (`tools/atlas/portraits_later.py`, which lists the entries left without one and why). Crop: centre x, y and size, as fractions of the image (size of its shorter side).\n")
w("| Entity | Source in the game | Icon | Crop (x, y, size) |\n|---|---|---|---|")
for eid, _, _ in ENT:
    if eid in PORTRAITS:
        icon, x, y, size, source = PORTRAITS[eid]
        w(f"| {NAME[eid]} | {source} | {icon} | {x}, {y}, {size} |")
    else:
        w(f"| {NAME[eid]} | none: keeps its category shape | – | – |")
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
