# Four-tool coffee tray: flat-bed print prototype

The included STL is the tray only, not the equipment. Import in millimetres, at 100%, with the flat bottom on the plate as supplied. The envelope is **127.0 × 228.6 × 109.0 mm**; allow additional usable bed area if your profile adds a brim, purge line or keep-out. No machine-specific G-code is included.

## WDT fit and strength

The open cape keeps the old conical handle seat but replaces the unsupported ring with curved shoulders, a gathered waist and a flared foot. The foot blends into the deck with a 2 mm radius. The needle tips sit nominally 5 mm above deck level; the central dimple is below that datum. The checked release lifts the grip 26 mm and then draws it toward the tray front. A 16 mm diameter rigid gauge clears the exit. Measure the actual bundle without squeezing the needles; allow clearance for print variation. A wider splay needs a different opening.

The geometry is intended to spread bending loads into the deck. No physical print, load test or strength rating has been performed. Do not tamp using the WDT holder. Check the portafilter bearing, stability and grip clearance on a real print before applying tamping force.

## Portafilter, paper and scale fit

The 20 mm pedestal has a 6 mm central recess instead of a through-opening; 14 mm of pedestal height remains below the pocket, above the 10 mm deck. The center is part of the print body, not a request for 100% infill. The pedestal has a 3 mm radius at its base, a 2.3 mm radius at the pocket floor and rounded lips and neck cutouts. Two flat lands under the rigid metal head total 476.5 mm² in CAD. With either handle orientation the nearest modeled basket surface clears by 4.29 mm, the basket center by 6 mm vertically and the neck by 2.00 mm. Grip clearance is 2.00 mm in storage and 15.19 mm pointing forward.

The model assumes that the installed basket bottom sits flush with the underside of the metal head; the real projection and contact band are unmeasured. With the portafilter unloaded, check that both sides of the metal head sit flat without rocking and that the basket, neck and grip do not touch the tray. Check counter grip and stability before applying force.

The paper walls and shared divider are 3.2 mm thick; the low outer scale fin is 3.0 mm. The outer paper wall, divider and outer scale fin respectively have 3, 1.25 and 1.5 mm fillets where they meet the deck. The 21 mm paper slot and 24.5 mm scale slot retain their full lift corridors. Confirm easy removal on the physical print, especially around the scale feet.

## Digital checks

- The CAD export is one solid. After STL normalization, PrusaSlicer reported one manifold part; CGAL found a closed triangle mesh with no self-intersections. This independent mesh check supplements a bounded CAD face self-intersection check on the freeform cape.
- The FDM geometry check, deck down, reported no downward-facing area below its 45° threshold and zero estimated support volume. Sampled minimum wall thickness was 3.0 mm; this is not a load rating.
- The supplied STL was sliced in **PrusaSlicer 2.9.4**, using a generic 256 × 256 mm bed, 0.4 mm nozzle, 0.2 mm layers, four perimeters and 20% infill. Automatic support generation was **enabled at 45°**, with bridges not exempted. The slice emitted **no support-material toolpaths**. Ordinary bridge infill within the part is not removable support. Re-slice with your actual printer and material profile, and inspect the layer preview before printing.

## Rebuild from source

From the repository's `src/` directory, run `cad run -m coffee_tray.compact` and `cad run -m coffee_tray.check_compact`. Export `bed_ready`, not `parked` or `tamp`: `cad model export <bed_ready_id> tray-raw.stl --tolerance 0.06 --angle 7`. The packaged STL was normalized with `prusa-slicer --export-stl --output compact-four-tool-tray.stl tray-raw.stl`. Geometry, fit checks, and store/tamp poses are in the same repository.
