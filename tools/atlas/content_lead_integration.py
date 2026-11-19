"""The lead's integration module for the Atlas after 2.0, merged after the five era modules (data only).

Two jobs no single era could do while the eras were written in parallel:
  - earlier entries for entities whose names accepted or earlier-era text already uses, so nothing is named before it
    is visible: Revenant's Toll (accepted 2.0 text from #148), Raubahn (the accepted A4 recap at #159) and Omega
    (2.3 text from #190);
  - adopting records an era drafted for an entity it could not create itself (Omega's 3.56 records).
Every locator is checked against the saved Console Games Wiki pages (--verify-locators).
"""
import content_3_1_to_3_56 as HW3X

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

CLAIMS = {
 "L148a": ("Cid sends you to Revenant's Toll in Mor Dhona to gather information on the captive Scions.", "Come-Into-My-Castrum",
           "Cid bids you make your way to [[Revenant's Toll]] in [[Mor Dhona]], and solicit the local [[adventurer]]s for information."),
}

ENTITIES = {"char-omega": "character"}

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
}

DECISIONS = [
 "**Earlier entries from the lead:** Revenant's Toll from #148, Raubahn from #159 and Omega from #190, because text there already names them. Omega's 3.56 records were drafted by the 3.1–3.56 era and adopted here.",
]
