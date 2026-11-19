"""The lead's integration module for the Atlas after 2.0, merged after the five era modules (data only).

Two jobs no single era could do while the eras were written in parallel:
  - earlier entries for entities whose names accepted or earlier-era text already uses, so nothing is named before it
    is visible: Revenant's Toll (accepted 2.0 text from #148), Raubahn (the accepted A4 recap at #159) and Omega
    (2.3 text from #190);
  - adopting records an era drafted for an entity it could not create itself (Omega's 3.56 records).
Every locator is checked against the saved Console Games Wiki pages (--verify-locators).
"""
import content_3_1_to_3_56 as HW3X
import content_4_0_part3 as SB3
import content_4_1_to_4_56 as SB4X

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

CLAIMS = {
 "L148a": ("Cid sends you to Revenant's Toll in Mor Dhona to gather information on the captive Scions.", "Come-Into-My-Castrum",
           "Cid bids you make your way to [[Revenant's Toll]] in [[Mor Dhona]], and solicit the local [[adventurer]]s for information."),
}

ENTITIES = {"char-omega": "character", "loc-ala-mhigo": "location"}

PRES = {
 "loc-revenants-toll": [
   P("cp-msq-148", None, "main", "Revenant's Toll",
     "A settlement in Mor Dhona where Cid gathered his allies to prepare the rescue of the Scions held at Castrum Centri.",
     ["L148a", "K04"]),
 ],
 "char-raubahn": [
   P("cp-msq-159", None, "main", "Raubahn",
     "An Eorzean general. On the eve of the assault on the imperial castrum, you helped him rally the wavering garrison at the Ceruleum Processing Plant.",
     ["K55"], ["General Raubahn"]),
 ],
 "char-omega": [
   P("cp-msq-190", None, "main", "Omega",
     "A weapon that Raubahn believes Teledji wants, with power enough to subjugate Ul'dah and the rest of Eorzea. It is more akin to a fossil than a tool of war, having long since ceased to function.",
     ["M190g", "M190h"]),
   *HW3X.OMEGA_DRAFT["char-omega"],
 ],
 # Stormblood: text names Ala Mhigo from #200, long before the 4.1 era could create it; its 4.x records were drafted there.
 "loc-ala-mhigo": [
   P("cp-msq-200", None, "main", "Ala Mhigo",
     "A fallen nation. Raubahn and Ilberd were friends and rivals there before it fell.",
     ["M200e"]),
   *SB4X.ALA_MHIGO_DRAFT["loc-ala-mhigo"],
 ],
 # Part 1 creates these two places; part 3 drafted their later records.
 "loc-castellum-velodyna": SB3.LOC_DRAFTS["loc-castellum-velodyna"],
 "loc-specula-imperatoris": SB3.LOC_DRAFTS["loc-specula-imperatoris"],
}

DECISIONS = [
 "**Ala Mhigo from #200:** text there already names it, so the lead starts its entry with Raubahn and Ilberd's shared past, then adopts the 4.1–4.56 era's drafted records. Part 3's later records for Castellum Velodyna and Specula Imperatoris, which part 1 creates, are adopted the same way.",
 "**Earlier entries from the lead:** Revenant's Toll from #148, Raubahn from #159 and Omega from #190, because text there already names them. Omega's 3.56 records were drafted by the 3.1–3.56 era and adopted here.",
]
