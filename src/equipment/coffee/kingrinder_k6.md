# KINGrinder K6: owner-supplied STEP references

Each input is one valid solid from an Onshape part export. The STEP unit is metre; the CAD kernel converts to millimetres. These measurements describe the supplied geometry, not a separately measured production grinder. There is no saved assembly mate. See [input placement and provenance](../../../vendor/kingrinder_k6/README.md).

| Feature | CAD measurement (mm) |
| --- | ---: |
| Grinder body height | 170.50 |
| Bottom diameter, Z=0 to 140 | 52.00 |
| Upper body diameter, Z=142 to 170.50 | 54.50 |
| Detached lid, crank and knob, box with crank along +X | 175.25 × 54.50 × 69.20 |
| Lid OD / crank arm diameter / spherical knob diameter | 54.50 / 6.00 / 40.00 |
| Crank axis to knob center / outermost knob edge | 128.00 / 148.00 |

The grinder stands on Z=0. The lower 140 mm is cylindrical; the shoulder transitions to the upper diameter by Z=142. Use the 52 mm nominal body for a shallow pocket; add any print allowance in the tray, not to this part. The handle export includes its own lid and knob as one solid.

## Attached storage hypothesis

The local handle model begins at its center pin's tip. Its outer lid underside is at Z=10.25. Putting that annular face on the body's flat top puts the handle origin at Z=160.25 and its highest point at **229.45 mm** above the grinder base. At the shown fixed angle, the assembly box is **175.25 × 54.50 × 229.45 mm**. If the handle can rotate freely, the knob sweeps a **296 mm diameter**; a keyed parking direction needs a single clear path, not that full circle.

The grinder export has a solid, closed top. In this inferred pose the handle's underside boss and annular lip intersect that solid by approximately **3,106.45 mm³**. These two bodies are suitable for external layout, not evidence of a verified mechanical fit. Do not union them, alter the supplied solids to remove the interference, or double count the mating plug by simply adding the separate heights. A different actual seating depth would change the assembled height. If the crank is parked separately, use the two independent models and validate whichever orientation is chosen.

Build all three references from `src/`: `cad run -m equipment.coffee.kingrinder_k6`. Tool colors are for legibility only. No tray orientation, pocket clearance or cradle for the handle is chosen here.
