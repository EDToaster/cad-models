# Coffee gear tray

The current tray holds four items: portafilter, WDT, scale and V60 filters. The earlier eight-item layout and all equipment references are retained for comparison.

**Footprint rule for all holders:** minimize the tray area each holder adds beyond the parked item. Compare layouts with the gear in place, including overhangs. Preserve stable support and a clear path for fingers and removal; a smaller printed base is not a saving if the same space must stay empty.

## Compact four-tool tray

The [compact study](compact.py) measures **5 in across × 9 in front to back** (127 × 228.6 mm) and retains the **10 mm base**. It is 3 in narrower and 0.5 in shallower than the eight-item tray, about 41% less counter area. The grinder, crank, bottle, dosing ring and tamper cap have no holders or pockets in this version.

![Compact tray with its four tools, empty fixtures, and storage plan](concepts/compact-four-tool-tray.png)

The portafilter seat and open WDT collar share one front centerline. The handle parks along the open left side. On the right, the papers and scale stand on edge against one shared divider, with their rear edges aligned. The longer scale extends 20.4 mm farther forward than the paper stack, leaving its end exposed. Three low, curved guides, a rounded deck edge and a single warm-stone preview color keep the parts visually related. The color is illustrative.

The nominal holder allowances are 0.5 mm per face and the file slots are 4.5 mm deep, leaving 5.5 mm of deck below. The WDT hangs needles down, with the collar open toward the user. The portafilter keeps its two-way 20 mm head support. Its parked tip is 5.6 mm inside the rear edge; in the tamping pose it extends 137 mm (5.39 in) beyond the front. The deck itself never moves or changes size.

Build from `src/` with `cad run -m coffee_tray.compact` (empty, parked and tamping views) and check with `cad run -m coffee_tray.check_compact`. Both seated poses were checked for inter-item intersections using the modeled solids. Actual needle spread, hand access, print fit and stability under tamping load are unverified. The deck and fixtures remain separate CAD bodies for iteration; this is not a production print file.

## Earlier eight-item layout

The [working mockup](layout.py) uses a **9.5 × 8 in (241.3 × 203.2 mm) footprint and a 10 mm deck**. In this version the long side runs toward the wall. The 10 mm is the base thickness before pockets, not a height limit on holders or gear.

![Plan and oblique view with equipment key](concepts/tray-layout-v1.png)

The raised, reversible portafilter seat is at the front left. The tamper cap and dosing ring sit at the front; scale and papers stand on edge along the right side, sharing a divider. The grinder and detached crank park separately. A **46 × 46 mm base and 102 mm guide** replace Option B's original 85 × 62 mm base and 116 mm guide; the knob still sets the assembly height at 185.5 mm above the deck (195.5 mm above the counter). The bottle sits between the portafilter and crank, clear of both in the parked model.

![Portafilter storage and tamping compared at the same scale](concepts/tray-portafilter-clearance.png)

**The footprint is met in storage, not while tamping.** The basket center is 49 mm behind the front edge. Its modeled 180 mm handle reach puts the parked tip 12.3 mm inside the rear edge and the forward tip 131 mm (5.16 in) past the front edge. This is a temporary equipment overhang, not extra tray material. Both opposite tips cannot fit inside this rectangle with a single fixed seat, even diagonally: their separation is 360 mm versus a 315.5 mm deck diagonal. If no overhang is acceptable, revisit the one-seat requirement before refining the layout.

Round pockets are 2.5 mm deep; file slots are 4.5 mm deep, leaving at least 5.5 mm of floor. The starting allowance is 0.5 mm per side, not a validated print fit. The WDT hangs with 5 mm nominal tip clearance. Nozzle settings, printed tolerances, needle spread, one-handed access, tall-item stability and the metal bearing surface under tamping force still need verification. Only the measured tamper **cap** is modeled: the tamper above it must be checked for overhang and hand access.

Build from `src/` with `cad run -m coffee_tray.layout`, then run `cad run -m coffee_tray.check_layout`. The checker compares solids between the equipment, supports and deck and tests the footprint in both seated poses, not the swing from one to the other. Lift and reseat the portafilter. The compact crank rack's 8 mm lift followed by a 45 mm forward slide was sampled every 1 mm against its holder alone (`coffee_tray.check_k6_handle_docks`). These are layout studies, not a load-rated or print-ready assembly.

## Equipment references

| Order | Reference item | Status |
| --- | --- | --- |
| 1 | [Small scale](../equipment/coffee/scale.md) | Simplified reference built; stores on 148.4 mm body edge |
| 2 | [Stack of V60 filter papers](../equipment/coffee/v60_filters.md) | Measured quarter-circle stack modeled; holder orientation open |
| 3 | [Manual WDT tool](../equipment/coffee/wdt.md) | Grip and needle reach modeled; [open-collar hanger](concepts/wdt_open_collar.svg) selected; relaxed needle spread unmeasured |
| 4 | [Normcore V4 tamper cap](../equipment/coffee/normcore_tamper_cap.md) | Cap exterior modeled; the cap, not the 58.5 mm tamper base, locates in the tray |
| 5 | [Dosing ring](../equipment/coffee/dosing_ring.md) | Straight ring modeled, including its through bore |
| 6 | [Gaggia bottomless portafilter](../equipment/coffee/gaggia_portafilter.md) | Measured drop at neck and grip; raised handle-forward and handle-rearward poses |
| 7 | [KINGrinder K6, lid/crank and knob](../equipment/coffee/kingrinder_k6.md) | Separate upright parking fits in the first layout; compact version of [Option B](#detached-k6-handle-parking) |
| 8 | [Small MUJI spray bottle](../equipment/coffee/muji_spray_bottle.md) | Upright cylindrical reference, Ø24.40 × 86 mm; holder depth and clearance deferred |

The scale stands on its long edge. Start a width test coupon at **24.5 mm** (23.5 mm measured thickness + 0.5 mm clearance per face), not a press fit. This is a trial CAD opening, not a guaranteed as-printed size. Print the coupon with the tray's material, orientation and settings; check that the scale drops in and lifts out without dragging its four load-cell feet. Adjust the tray allowance from the coupon, not the scale model.

## WDT hanger decision

Use a single straight post rising from the tray and a rigid C-shaped conical collar, open opposite the post. The seat is wider at the top: the tapered handle hangs by gravity and is intended to self-align. Store the tool needles down without loading the tips. For removal, lift the grip clear of the rim and slide the needles sideways through the opening. This replaces the earlier [cup sketch](concepts/wdt_dock.svg).

**Defer holder refinement until the full equipment mockup exists.** At that point measure the relaxed needle spread, size the slot to pass it without flexing the needles while retaining the grip, and verify that the handle releases without wedging. Set the post height, tip clearance, edge rounding and exit direction against the tray and neighboring gear. The open sides do not shield the needles, so keep them inside the tray perimeter and out of normal hand paths. The sketch is not a dimensioned or print-ready part.

## Reversible portafilter station

One seat, two placements: handle toward the user for tamping, toward the wall for storage. The basket stays upright and on the same centerline. Lift, turn 180° and reseat; this does not require clearance for a horizontal sweep while seated. Run `cad run -m coffee_tray.portafilter_poses` from `src/` to inspect the two alternatives.

The black grip hangs 18 mm below the portafilter head. For both mockup poses, the **head underside is 20 mm above the local tray deck**: 18 mm measured drop plus a provisional 2 mm air gap. At 18 mm it would just touch. This is a placement requirement over a flat deck, not a finished holder height. The metal neck also passes below the basket, so relieve its path on both sides. Recheck against any raised lip or adjacent item and under tamping load when refining the station.

Reserve opposing handle/neck openings and clear the ears in both poses. The design intent is to keep the basket rim level under tamping force and support the rigid metal head directly over the base, not the plastic grip or perforated basket floor. Confirm a usable metal contact surface on the real part. Reserve center-to-wall reach plus hand/placement clearance for storage; the present model reaches 180 mm behind center. Check rear wall, front overhang, adjacent gear, basket underside clearance, skid/tip resistance and loaded stability at refinement. No station geometry or load rating has been set.

## Detached K6 handle parking

**Decision for the eight-item layout: Option B, with a lower-profile holder.** Keep the lid on edge and the crank upright. The [eight-item layout](#earlier-eight-item-layout) trials a shorter arm guide and smaller base. Lowering the guide alone does not lower the parked knob. The image and measurements below document the original comparison, not the revised rack.

![Low cradle and upright rack, with the actual crank parked and removed](concepts/k6-handle-docks.png)

Both concepts use the unmodified handle STEP, including the lid and knob. The bounds below are axis-aligned (length × width × height in mm); they exclude the grinder, fingers and the removal path.

| Concept | Empty holder | With handle parked | How it works |
| --- | --- | --- | --- |
| Low cradle | 150 × 64 × 25.52 | 180 × 64 × 74.95 | The lid flange rests on an annular ledge above its center pin. A shallow V under the far end of the arm keeps the knob aligned. Lift straight up. The knob reaches 30 mm beyond the base. |
| Upright rack | 85 × 62 × 116 | 85 × 62 × 185.50 | The lid stands on edge in a shallow V between guide cheeks. An open fork steadies the arm; lift the lid, then draw the crank forward out of the fork. No snap fit. |

The original upright rack's occupied bounding rectangle is 54% smaller than the low cradle's. Its modeled 20 mm lift needs 205.5 mm above the deck, plus hand clearance and an unobstructed front exit. Recheck stability and removal with the shorter guide once all equipment is placed. Keep separate parking conditional on that layout; the low cradle is a fallback if headroom or access rules out the upright pose.

Build from `src/` with `cad run -m coffee_tray.k6_handle_docks`. With the local reference STEP present, run `cad run -m coffee_tray.check_k6_handle_docks` for the geometry checks. Both parked assemblies touch their holders without solid overlap. The low lift (35 mm) and the upright lift (20 mm) followed by a forward pull (80 mm) were checked at 1 mm increments against each holder alone. These are example release paths, not minimum necessary travel or a continuous sweep proof.

Where the lid is guided, the nominal side allowance is 0.8 mm per side. The upright fork has a 7.6 mm clear opening for the 6 mm shaft. The first-pass FDM check (base down, PETG, 0.4 mm nozzle, 0.2 mm layers) flagged neither holder for supports; this is not a slicer or stability test. Tune allowance and edge treatment with a coupon and check knock-over risk, comfort and nearby gear after the complete layout is available.
