# Four-tool coffee tray: flat-bed print prototype

The included STL is the tray only, not the equipment. Import in millimetres, at 100%, with the flat bottom on the plate as supplied. The envelope is **127.0 × 228.6 × 109.0 mm**; allow additional usable bed area if your profile adds a brim, purge line or keep-out. No machine-specific G-code is included.

## WDT fit and strength

The open cape keeps the old conical handle seat but replaces the unsupported ring with curved shoulders, a gathered waist and a flared foot. The foot blends into the deck with a 2 mm radius. The needle tips sit nominally 5 mm above deck level; the central dimple is below that datum. The checked release lifts the grip 26 mm and then draws it toward the tray front. A 16 mm diameter rigid gauge clears the exit. Measure the actual bundle without squeezing the needles; allow clearance for print variation. A wider splay needs a different opening.

The geometry is intended to spread bending loads into the deck. No physical print, load test or strength rating has been performed. Do not tamp using the WDT holder. Check the portafilter bearing, stability and grip clearance on a real print before applying tamping force.

## Digital checks

- The CAD export is one solid. After STL normalization, PrusaSlicer reported one manifold part; CGAL found a closed triangle mesh with no self-intersections. This independent mesh check supplements a bounded CAD face self-intersection check on the freeform cape.
- The FDM geometry check, deck down, reported no downward-facing area below its 45° threshold and zero estimated support volume. Sampled minimum tray wall thickness was 2.4 mm; this is not a load rating.
- The supplied STL was sliced in **PrusaSlicer 2.9.4**, using a generic 256 × 256 mm bed, 0.4 mm nozzle, 0.2 mm layers, four perimeters and 20% infill. Automatic support generation was **enabled at 45°**, with bridges not exempted. The slice emitted **no support-material toolpaths**. Ordinary bridge infill within the part is not removable support. Re-slice with your actual printer and material profile, and inspect the layer preview before printing.

## Rebuild from source

From the repository's `src/` directory, run `cad run -m coffee_tray.compact` and `cad run -m coffee_tray.check_compact`. Export `bed_ready`, not `parked` or `tamp`: `cad model export <bed_ready_id> tray-raw.stl --tolerance 0.06 --angle 7`. The packaged STL was normalized with `prusa-slicer --export-stl --output compact-four-tool-tray.stl tray-raw.stl`. Geometry, fit checks, and store/tamp poses are in the same repository.
