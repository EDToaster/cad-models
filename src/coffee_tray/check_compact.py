"""Run with cad run -m coffee_tray.check_compact from src/."""

import build123d as bd

from coffee_tray.check_layout import check_groups
from coffee_tray.compact import (
    DEPTH, THICKNESS, WIDTH, PAPER_X, REAR_LINE, SIDE_GAP, SLOT_DEPTH,
    groups, thin_packet,
)
from equipment.coffee.v60_filters import FILTER_RADIUS, STACK_THICKNESS


def check_paper_pocket():
    parts = groups()
    full = parts.pop("papers")
    # A rectangular keep-out conservatively contains every upright stack,
    # including a single thin packet resting on either wall, throughout lift-out.
    sweep = bd.Pos(PAPER_X - SIDE_GAP, REAR_LINE - FILTER_RADIUS, -SLOT_DEPTH) * bd.Box(
        STACK_THICKNESS + 2 * SIDE_GAP, FILTER_RADIUS, 2 * FILTER_RADIUS,
        align=(bd.Align.MIN,) * 3,
    )
    for name, part in parts.items():
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


if __name__ == "__main__":
    for tamping in (False, True):
        check_groups(groups(tamping), WIDTH, DEPTH, THICKNESS, tamping)
    check_paper_pocket()
