# Coffee gear tray

Model each object as it sits in storage, one at a time. The equipment models represent the real objects. Tray pockets, finger access and room to lift pieces out come later.

| Order | Reference item | Status |
| --- | --- | --- |
| 1 | [Small scale](../equipment/coffee/scale.md) | Simplified reference built; stores on 148.4 mm body edge |
| 2 | [Stack of V60 filter papers](../equipment/coffee/v60_filters.md) | Measured quarter-circle stack modeled; holder orientation open |
| 3 | Manual WDT tool | Needles down in an [open collar on a straight post](concepts/wdt_open_collar.svg); measurements pending |
| 4 | Normcore tamper | Queued |
| 5 | Dosing ring / funnel | Queued |
| 6 | Portafilter with basket and handle | Queued |
| 7 | KINGrinder K6 with crank and knob | Queued |

The scale stands on its long edge. Start a width test coupon at **24.5 mm** (23.5 mm measured thickness + 0.5 mm clearance per face), not a press fit. This is a trial CAD opening, not a guaranteed as-printed size. Print the coupon with the tray's material, orientation and settings; check that the scale drops in and lifts out without dragging its four load-cell feet. Adjust the tray allowance from the coupon, not the scale model.

The current WDT hanger concept is a single straight post supporting a rigid C-shaped collar, open opposite the post. The short conical seat is wider at the top and cradles the tapered grip by gravity. Lift until the bottom of the handle clears the rim, then withdraw laterally; only the needles pass through the slot. Round the slot ends. The minimum finished gap must clear the relaxed needle spread with allowance to both sides, while retaining the seated grip. If that width window does not exist, change the support geometry rather than requiring needle flex or a snap fit. Leave tip clearance above the tray and check the lateral exit path against neighboring gear. Unlike the earlier [cup sketch](concepts/wdt_dock.svg), this hanger does not shield the needles from the side. Neither sketch is a dimensioned part.
