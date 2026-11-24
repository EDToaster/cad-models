"""Four-tool layout. X across, +Y toward the wall, Z=0 at the deck surface."""

import build123d as bd
from cad import model

from coffee_tray.holders import BASE_ALIGN, NEEDLE_GAP, open_wdt_hanger, two_way_riser
from coffee_tray.portafilter_poses import storage_pose, tamping_pose
from equipment.coffee import scale, v60_filters, wdt

WIDTH, DEPTH, THICKNESS = 127.0, 228.6, 10.0
STONE = "#cab8a0"  # Presentation color; no material or finish is specified.
PF, WDT = (41, 43), (102, 43)
REAR_LINE = 216.0  # common back line for scale and filter stack
SCALE_X, PAPER_X = 110.5, 74.5  # scale center and paper stack left edge
SIDE_GAP, SLOT_DEPTH = 0.5, 4.5


def _finish(part, name):
    part.label, part.color = name, STONE
    return part


def _slot(center_x, width, length):
    return bd.Pos(center_x, REAR_LINE - length / 2, -SLOT_DEPTH) * bd.Box(
        width + 2 * SIDE_GAP, length + 2 * SIDE_GAP, SLOT_DEPTH + 1, align=BASE_ALIGN
    )


@model
def deck():
    plate = bd.Pos(WIDTH / 2, DEPTH / 2, -THICKNESS) * bd.extrude(
        bd.RectangleRounded(WIDTH, DEPTH, 9), amount=THICKNESS
    )
    # A small round-over softens the silhouette; maximum thickness stays 10 mm.
    plate = bd.fillet(plate.edges().group_by(bd.Axis.Z)[-1], radius=1.6)
    plate -= _slot(SCALE_X, scale.THICKNESS, scale.LENGTH)
    plate -= _slot(PAPER_X + v60_filters.STACK_THICKNESS / 2,
                   v60_filters.STACK_THICKNESS, v60_filters.FILTER_RADIUS)
    # Shallow, wipeable depression directly below the suspended needle tips.
    plate -= bd.Pos(*WDT, 70 - 1.2) * bd.Sphere(70)
    return _finish(plate, "Soft-edge deck")


def _cheek(x, height):
    """Open ends and a scooped upper edge. The middle divider serves both slots."""
    start, end = 92, 212
    mid = (start + end) / 2
    with bd.BuildLine() as outline:
        bd.Line((start, 0), (end, 0))
        bd.Bezier((end, 0), (end - 2, 3), (end - 1, height), (end - 16, height))
        bd.Bezier((end - 16, height), (end - 30, height),
                  (mid + 13, height * 0.60), (mid, height * 0.60))
        bd.Bezier((mid, height * 0.60), (mid - 13, height * 0.60),
                  (start + 30, height), (start + 16, height))
        bd.Bezier((start + 16, height), (start + 1, height), (start + 2, 3), (start, 0))
    return bd.Pos(X=x) * (bd.Plane.YZ * bd.extrude(bd.Face(outline.wire()), amount=2.4))


@model
def files():
    rails = [_cheek(x, h) for x, h in ((71.2, 16), (95.5, 25), (123.0, 20))]
    return _finish(bd.Compound(children=rails), "Shared file rack")


@model
def station():
    # A narrow flared foot meets the deck; bearing surfaces stay unchanged.
    foot = bd.Cone(36.5, 34.5, 3.5, align=BASE_ALIGN)
    foot -= bd.Cylinder(31, 3.5, align=BASE_ALIGN)
    return _finish(bd.Pos(*PF, 0) * (two_way_riser() + foot), "Reversible head seat")


@model
def hanger():
    return _finish(bd.Pos(*WDT, 0) * open_wdt_hanger(post_radius=1.8), "Open WDT hanger")


def fixtures():
    return {"deck": deck().shape, "files": files().shape,
            "seat": station().shape, "hanger": hanger().shape}


def groups(tamping=False):
    return {
        **fixtures(),
        "portafilter": bd.Pos(*PF, 0) * (tamping_pose() if tamping else storage_pose()).shape,
        "WDT": bd.Pos(*WDT, NEEDLE_GAP) * wdt.wdt_tool().shape,
        "scale": bd.Pos(SCALE_X, REAR_LINE - scale.LENGTH / 2, -SLOT_DEPTH)
                 * bd.Rot(Z=90) * scale.scale_on_long_edge().shape,
        "papers": bd.Pos(PAPER_X, REAR_LINE - v60_filters.FILTER_RADIUS, -SLOT_DEPTH)
                  * bd.Rot(Z=90) * bd.Rot(X=90) * v60_filters.v60_filter_stack().shape,
    }


@model
def empty():
    return bd.Compound(label="Compact tray, empty", children=list(fixtures().values()))


@model
def parked():
    return bd.Compound(label="Compact tray, parked", children=list(groups().values()))


@model
def tamp():
    return bd.Compound(label="Compact tray, tamping", children=list(groups(True).values()))


if __name__ == "__main__":
    empty()
    parked()
    tamp()
