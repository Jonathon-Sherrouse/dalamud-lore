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
import content_5_0_part2 as SHB2
import content_5_0_part3 as SHB3

def P(frm, until, scope, name, summary, claims, aliases=()):
    return dict(frm=frm, until=until, scope=scope, name=name, aliases=list(aliases), summary=summary, claims=claims)

CLAIMS = {
 "L148a": ("Cid sends you to Revenant's Toll in Mor Dhona to gather information on the captive Scions.", "Come-Into-My-Castrum",
           "Cid bids you make your way to [[Revenant's Toll]] in [[Mor Dhona]], and solicit the local [[adventurer]]s for information."),
}

ENTITIES = {"char-omega": "character", "loc-ala-mhigo": "location", "org-lightwardens": "organization", "char-halric": "character"}

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
 # Shadowbringers: the Lightwardens share a quest's name (#563), so they are visible from that quest; Halric is named
 # from #551b on the Amh Araeng chain, before the 5.1 era creates him.
 "org-lightwardens": [
   P("cp-msq-563", None, "main", "The Lightwardens",
     "The strongest of the sin eaters, which the lesser ones serve. The Crystarium believes that a Lightwarden's death will scatter the lesser sin eaters around it.",
     ["M563a", "M563b"]),
 ],
 "char-halric": [
   P("cp-msq-551b", None, "main", "Halric",
     "A resident of the Inn at Journey's Head, cared for by its carers. The nectarine you bought there is his favorite fruit.",
     ["M551bd"]),
 ],
 # Shadowbringers: what the First learns of Hydaelyn, drafted by 5.0 parts 2 and 3 (her entity is from 2.1).
 "char-hydaelyn": [*SHB2.HYDAELYN_DRAFT["char-hydaelyn"], *SHB3.HYDAELYN_DRAFT["PRES"]["char-hydaelyn"]],
 # Endwalker: two names the 6.0 text uses before the era that makes them entries (Galuf from 6.55, Khalzahl from #752).
 "char-galuf": [
   P("cp-msq-700", None, "main", "Galuf",
     "Krile's grandfather, who sat in Sharlayan's Forum and, like Archon Louisoix, argued for direct intervention abroad.",
     ["M700d"]),
 ],
 "char-khalzahl": [
   P("cp-msq-702b", None, "main", "Khalzahl",
     "A merchant of Thavnair who buys the fisherman Matsya's catch to sell on to foreign traders, though he has bought nothing for a while.",
     ["M702be"]),
 ],
 # Part 1 creates these two places; part 3 drafted their later records.
 "loc-castellum-velodyna": SB3.LOC_DRAFTS["loc-castellum-velodyna"],
 "loc-specula-imperatoris": SB3.LOC_DRAFTS["loc-specula-imperatoris"],
}

DECISIONS = [
 "**Endwalker, earlier entries from the lead:** Galuf from #700 and Khalzahl from #702b, because 6.0 text names them there, before the eras that make them entries (6.55 and #752).",
 "**Endwalker, cross-era endings:** Hydaelyn's opposition to Zodiark, Zenos's lead of the Telophoroi and Fandaniel's Ascian membership end at #740; Elidibus's hold in the Crystal Tower and his opposition to the Scions end at #762; Azdaja's captivity under Golbez ends at #842 and his opposition to Zero at #848. The edges opposing Zenos close on the step after the 6.0 milestone, where his Journal says he breathes his last.",
 "**Ala Mhigo from #200:** text there already names it, so the lead starts its entry with Raubahn and Ilberd's shared past, then adopts the 4.1–4.56 era's drafted records. Part 3's later records for Castellum Velodyna and Specula Imperatoris, which part 1 creates, are adopted the same way.",
 "**Earlier entries from the lead:** Revenant's Toll from #148, Raubahn from #159 and Omega from #190, because text there already names them. Omega's 3.56 records were drafted by the 3.1–3.56 era and adopted here.",
]

RELS = [*SHB3.HYDAELYN_DRAFT["RELS"]]

# Cross-era endings no single era could write: Eline (2.4) served Varis, who is murdered in 5.2.
ADJUST = {"rel-eline-serves-varis": {"until": "cp-msq-657", "end": ["M657f"]},
          # Endwalker endings across eras: Zodiark falls and Fandaniel dies (#740); Elidibus's essence is consumed (#762);
          # Golbez releases Azdaja (#842) and is unmasked and repentant (#848). Zenos breathes his last at the 6.0
          # milestone, so the edges against him close on the next step, with no end claims (none may sit there).
          "rel-hydaelyn-opposes-zodiark": {"until": "cp-msq-740", "end": ["M740f", "M740h"]},
          "rel-zenos-leads-telophoroi": {"until": "cp-msq-740", "end": ["M740h"]},
          "rel-fandaniel-member-of-ascians": {"until": "cp-msq-740", "end": ["M740h"]},
          "rel-elidibus-held-at-crystal-tower": {"until": "cp-msq-762", "end": ["M762i"]},
          "rel-elidibus-opposes-scions": {"until": "cp-msq-762", "end": ["M762i"]},
          "rel-azdaja-prisoner-of-golbez": {"until": "cp-msq-842", "end": ["M842f"]},
          "rel-golbez-opposes-zero": {"until": "cp-msq-848", "end": ["M848h"]},
          "rel-jullus-opposes-zenos": {"until": "cp-msq-807"},
          "rel-xth-legion-opposes-zenos": {"until": "cp-msq-807"},
          "rel-gaius-opposes-zenos": {"until": "cp-msq-807"}}

