# Folded V60 filter stack

The folded papers form a 90° circular sector, measured from the right-angle corner to the rim at **128 mm radius**. The stack as stored is **20 mm thick**. It is modeled as one solid envelope, not as individual sheets; there is no assumption about paper count or single-sheet thickness.

The reference lies flat on Z=0 with its straight sides on +X and +Y. Its axis-aligned bounds are 128 × 128 × 20 mm; the direct distance between the two rim ends is 128√2 ≈ 181.0 mm. Those dimensions describe different directions, which matters if the holder presents the stack with the tip pointing down.

Build from `src/` with `cad run -m equipment.coffee.v60_filters`. Rotate the reference in the tray assembly as needed. Leave room for stack variation and for picking up one sheet in the holder design rather than inflating this model; no holder orientation or clearance has been fixed.
