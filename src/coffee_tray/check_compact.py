"""Run with cad run -m coffee_tray.check_compact from src/."""

import build123d as bd

from coffee_tray.check_layout import check_groups
from coffee_tray.compact import (
    DEPTH, THICKNESS, WIDTH, PAPER_X, REAR_LINE, SIDE_GAP, SLOT_DEPTH,
    PF, WDT, SCALE_X, assembled, empty, groups, station, thin_packet,
)
from coffee_tray.holders import BASE_ALIGN
from equipment.coffee.v60_filters import FILTER_RADIUS, STACK_THICKNESS
from coffee_tray.portafilter_station import FLOOR_Z, HEIGHT
from equipment.coffee import gaggia_portafilter, scale


def check_station_and_fins():
    # Keep the basket and plastic grip out of the load path. Check actual
    # closest surfaces, not just the vertical offset between two datum planes.
    tray = empty().shape
    seat = station().shape
    assert seat.is_inside((*PF, FLOOR_Z-0.05)) and not seat.is_inside((*PF, FLOOR_Z+0.05))
    pads = [f for f in seat.faces() if f.bounding_box().min.Z > HEIGHT-1e-5]
    assert len(pads) == 2 and all(f.area > 200 for f in pads)
    body, basket, neck, grip = gaggia_portafilter.components()
    for angle in (90, -90):
        pose = bd.Pos(*PF, HEIGHT) * bd.Rot(Z=angle)
        assert tray.distance_to(pose * body) < 1e-4, "metal head not seated"
        gaps = [tray.distance_to(pose * s) for s in (basket, neck, grip)]
        assert all(g > min_g for g, min_g in zip(gaps, (4.0, 1.99, 1.99))), gaps
        print(f"{angle:+}° seat: nearest basket {gaps[0]:.2f}, neck {gaps[1]:.2f}, "
              f"grip {gaps[2]:.2f} mm; nominal center-floor clearance {HEIGHT-FLOOR_Z:g} mm")
    # Protect the entire original scale-slot envelope, including nominal side
    # allowance, through a straight lift. No strength fillet may intrude.
    corridor = bd.Pos(SCALE_X, REAR_LINE-scale.LENGTH/2, -SLOT_DEPTH) * bd.Box(
        scale.THICKNESS + 2*SIDE_GAP, scale.LENGTH, 2*scale.WIDTH,
        align=BASE_ALIGN,
    )
    for name, obj in assembled().items():
        if name != "scale":
            assert _overlap(corridor, obj) < 1e-4, f"scale lift blocked by {name}"
    print(f"Two metal bearing lands, total {sum(f.area for f in pads):.1f} mm²; scale lift clear")


def check_paper_pocket():
    parts = groups()
    full = parts.pop("papers")
    # A rectangular keep-out conservatively contains every upright stack,
    # including a single thin packet resting on either wall, throughout lift-out.
    sweep = bd.Pos(PAPER_X - SIDE_GAP, REAR_LINE - FILTER_RADIUS, -SLOT_DEPTH) * bd.Box(
        STACK_THICKNESS + 2 * SIDE_GAP, FILTER_RADIUS, 2 * FILTER_RADIUS,
        align=(bd.Align.MIN,) * 3,
    )
    fused = assembled()
    for name, part in fused.items():
        if name == "papers":
            continue
        for solid in part.solids():
            common = sweep.intersect(solid)
            assert not common or sum(s.volume for s in common.solids()) < 1e-4, name
    assert len(parts["files"].solids()) == 2, "expect one joined paper pocket and one scale guide"
    for stack in (thin_packet(), full, thin_packet(right=True)):
        box, limits = stack.bounding_box(), sweep.bounding_box()
        assert box.min.X >= limits.min.X - 1e-5 and box.max.X <= limits.max.X + 1e-5
        assert stack.distance_to(parts["deck"]) < 1e-4
    for side in (False, True):
        assert thin_packet(side).distance_to(parts["files"]) < 1e-4
    print("Filter pocket: full and 1 mm envelopes fit; thin packet reaches either wall; "
          "straight lift clear with adjacent tools parked")


def _overlap(part, other):
    volume = 0
    for a in part.solids():
        for b in other.solids():
            common = a.intersect(b)
            if common:
                volume += sum(s.volume for s in common.solids())
    return volume


def check_cape():
    tray = empty().shape
    parked = assembled()
    tool = parked["WDT"]
    assert len(tray.solids()) == 1 and tray.is_valid
    for pose in (parked, assembled(tamping=True)):
        for k in ("portafilter", "WDT", "scale", "papers"):
            assert _overlap(tray, pose[k]) < 1e-3, k
    assert tool.distance_to(tray) < 1e-4, "taper is not seated"
    assert _overlap(tray, bd.Pos(Z=-1) * tool) > 0.1, "seat must carry the tapered grip"
    # Move the handle 26 mm up before sliding toward the front. Below the
    # grip a 16 mm gauge conservatively represents the whole round bundle,
    # rather than claiming the handful of visual needle markers is the actual spread.
    x, y = WDT
    gauge = bd.Pos(x, y, 5) * bd.Cylinder(8, 96, align=BASE_ALIGN)
    gauge += bd.Pos(x, y-25, 5) * bd.Box(16, 50, 96, align=BASE_ALIGN)
    for k in ("tray", "portafilter", "scale", "papers"):
        assert _overlap(parked[k], gauge) < 1e-3, f"bundle exit blocked by {k}"
    for lift in (1, 8, 16, 24, 26):
        assert _overlap(tray, bd.Pos(Z=lift) * tool) < 1e-3, f"handle caught at lift {lift}"
    # After the lift, the grip's bottom is above the collar. Check its entire
    # forward path with a bounding capsule based on the maximum handle diameter.
    from equipment.coffee.wdt import HANDLE_HEIGHT, MAX_DIAMETER
    grip = bd.Pos(x, y, 101) * bd.Cylinder(MAX_DIAMETER/2, HANDLE_HEIGHT, align=BASE_ALIGN)
    grip += bd.Pos(x, y-25, 101) * bd.Box(MAX_DIAMETER, 50, HANDLE_HEIGHT, align=BASE_ALIGN)
    grip += bd.Pos(x, y-50, 101) * bd.Cylinder(MAX_DIAMETER/2, HANDLE_HEIGHT, align=BASE_ALIGN)
    for k in ("tray", "portafilter", "scale", "papers"):
        assert _overlap(parked[k], grip) < 1e-3, f"lifted handle exit blocked by {k}"
    print("One fused body; tapered grip seats; 16 mm gauge clears front; "
          "26 mm lift and 50 mm forward withdrawal checked")


if __name__ == "__main__":
    check_station_and_fins()
    for tamping in (False, True):
        check_groups(groups(tamping), WIDTH, DEPTH, THICKNESS, tamping)
    check_paper_pocket()
    check_cape()
