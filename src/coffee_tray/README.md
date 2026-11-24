# Coffee gear tray

Model each object as it sits in storage, one at a time. The equipment models represent the real objects. Tray pockets, finger access and room to lift pieces out come later.

| Order | Reference item | Status |
| --- | --- | --- |
| 1 | [Small scale](../equipment/coffee/scale.md) | Simplified reference built; stores on 148.4 mm body edge |
| 2 | [Stack of V60 filter papers](../equipment/coffee/v60_filters.md) | Measured quarter-circle stack modeled; holder orientation open |
| 3 | [Manual WDT tool](../equipment/coffee/wdt.md) | Grip and needle reach modeled; [open-collar hanger](concepts/wdt_open_collar.svg) selected; relaxed needle spread unmeasured |
| 4 | [Normcore V4 tamper cap](../equipment/coffee/normcore_tamper_cap.md) | Cap exterior modeled; the cap, not the 58.5 mm tamper base, locates in the tray |
| 5 | [Dosing ring](../equipment/coffee/dosing_ring.md) | Straight ring modeled, including its through bore |
| 6 | Portafilter with basket and handle | Queued |
| 7 | KINGrinder K6 with crank and knob | Queued |

The scale stands on its long edge. Start a width test coupon at **24.5 mm** (23.5 mm measured thickness + 0.5 mm clearance per face), not a press fit. This is a trial CAD opening, not a guaranteed as-printed size. Print the coupon with the tray's material, orientation and settings; check that the scale drops in and lifts out without dragging its four load-cell feet. Adjust the tray allowance from the coupon, not the scale model.

## WDT hanger decision

Use a single straight post rising from the tray and a rigid C-shaped conical collar, open opposite the post. The seat is wider at the top: the tapered handle hangs by gravity and is intended to self-align. Store the tool needles down without loading the tips. For removal, lift the grip clear of the rim and slide the needles sideways through the opening. This replaces the earlier [cup sketch](concepts/wdt_dock.svg).

**Defer holder refinement until the full equipment mockup exists.** At that point measure the relaxed needle spread, size the slot to pass it without flexing the needles while retaining the grip, and verify that the handle releases without wedging. Set the post height, tip clearance, edge rounding and exit direction against the tray and neighboring gear. The open sides do not shield the needles, so keep them inside the tray perimeter and out of normal hand paths. The sketch is not a dimensioned or print-ready part.
