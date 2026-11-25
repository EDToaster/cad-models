# Four-tool coffee tray: flat-bed print prototype

The included STL is the tray only, not the equipment. Import in millimetres, at 100%, with the flat bottom on the plate as supplied. The envelope is **127.0 × 228.6 × 109.0 mm**; allow additional usable bed area if your profile adds a brim, purge line or keep-out. No machine-specific G-code is included.

## WDT fit and strength

The open cape keeps the old conical handle seat but replaces the unsupported ring with curved shoulders, a gathered waist and a flared foot. The foot blends into the deck with a 2 mm radius. The needle tips sit nominally 5 mm above deck level; the central dimple is below that datum. The checked release lifts the grip 26 mm and then draws it toward the tray front. A 16 mm diameter rigid gauge clears the exit. Measure the actual bundle without squeezing the needles; allow clearance for print variation. A wider splay needs a different opening.

The geometry is intended to spread bending loads into the deck. No physical print, load test or strength rating has been performed. Do not tamp using the WDT holder. Check the portafilter bearing, stability and grip clearance on a real print before applying tamping force.

## Underside foot pockets

Four flat-ended cylindrical openings face the build plate. Their CAD diameter is exactly 11 mm, depth 3 mm, with no fit allowance or edge treatment. Each center is 10 mm from its two neighboring edges. At the rear-right pocket, the 4.5 mm scale slot above leaves 2.5 mm of deck at the overlap; elsewhere an uncut 10 mm deck leaves 7 mm above the pocket. Supports may be used beneath the pocket roofs; no feet or supports are included in the model.

## Portafilter, paper and scale fit

The 20 mm pedestal has a 6 mm central recess instead of a through-opening; 14 mm of pedestal height remains below the pocket, above the 10 mm deck. The center is part of the print body, not a request for 100% infill. The pedestal has a 3 mm radius at its base, a 2.3 mm radius at the pocket floor and rounded lips and neck cutouts. Two flat lands under the rigid metal head total 476.5 mm² in CAD. With either handle orientation the nearest modeled basket surface clears by 4.29 mm, the basket center by 6 mm vertically and the neck by 2.00 mm. Grip clearance is 2.00 mm in storage and 15.19 mm pointing forward.

The model assumes that the installed basket bottom sits flush with the underside of the metal head; the real projection and contact band are unmeasured. With the portafilter unloaded, check that both sides of the metal head sit flat without rocking and that the basket, neck and grip do not touch the tray. Check counter grip and stability before applying force.

The paper walls and shared divider are 3.2 mm thick; the low outer scale fin is 3.0 mm. The outer paper wall, divider and outer scale fin respectively have 3, 1.25 and 1.5 mm fillets where they meet the deck. The 21 mm paper slot and 24.5 mm scale slot retain their full lift corridors. Confirm easy removal on the physical print, especially around the scale feet.

## Digital checks

- The exporter checks that the STEP reopens as one valid solid and the normalized STL is one closed manifold at Z=0. The geometry check inspects all four cylindrical walls and flat roofs on the final body and verifies the material above them.
- The previous tray without foot pockets was test-sliced. That support result does not apply to the new downward-facing recesses; support settings are left to the printer operator.

## Rebuild from source

From the repository's `src/` directory, run `cad run -m coffee_tray.check_compact` and `cad run -m coffee_tray.exports`. The latter exports `bed_ready`, not the equipped assembly, into `dist/coffee-tray/` at the repository root. GitHub Actions uses the same commands for its STEP and STL downloads.
