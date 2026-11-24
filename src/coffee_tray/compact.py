"""Four-tool layout. X across, +Y toward the wall, Z=0 at the deck surface."""

import build123d as bd
from cad import model

from coffee_tray.holders import BASE_ALIGN, NEEDLE_GAP
from coffee_tray.portafilter_station import filled_station
from coffee_tray.portafilter_poses import storage_pose, tamping_pose
from coffee_tray.wdt_cape import ROOT_FILLET, cape
from equipment.coffee import scale, v60_filters, wdt

WIDTH, DEPTH, THICKNESS = 127.0, 228.6, 10.0
STONE = "#cab8a0"  # Presentation color; no material or finish is specified.
PF, WDT = (41, 43), (102, 43)
REAR_LINE = 216.0  # common back line for scale and filter stack
SCALE_X, PAPER_X = 108.0, 70.5  # scale center and paper stack left edge
SIDE_GAP, SLOT_DEPTH = 0.5, 4.5
WALL = 3.2
SCALE_WALL = 3.0
OUTER_SCALE_X = 120.6
PAPER_GUIDE_HEIGHTS = (80.0, 86.0)  # outer wall and shared divider, above deck
PAPER_SCOOP = 46.0


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
    plate = bd.chamfer(plate.edges().group_by(bd.Axis.Z)[0], length=0.6)
    plate -= _slot(SCALE_X, scale.THICKNESS, scale.LENGTH)
    plate -= _slot(PAPER_X + v60_filters.STACK_THICKNESS / 2,
                   v60_filters.STACK_THICKNESS, v60_filters.FILTER_RADIUS)
    # Shallow, wipeable depression directly below the suspended needle tips.
    plate -= bd.Pos(*WDT, 70 - 1.2) * bd.Sphere(70)
    return _finish(plate, "Soft-edge deck")


def _cheek(x, height):
    """Original low outer guide for the scale."""
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
    fin = bd.Pos(X=x) * (bd.Plane.YZ * bd.extrude(bd.Face(outline.wire()), amount=SCALE_WALL))
    return bd.fillet([e for e in fin.edges() if e.geom_type in
                      (bd.GeomType.BEZIER, bd.GeomType.BSPLINE)], radius=0.65)


def _paper_wall(x, crown, scoop):
    """A high front shoulder, a finger scoop, then a lower shoulder under the arc."""
    front = REAR_LINE - v60_filters.FILTER_RADIUS - SIDE_GAP
    rear = REAR_LINE + SIDE_GAP
    mid = front + 58
    with bd.BuildLine() as outline:
        bd.Polyline((front, 0), (rear, 0), (rear, 15))
        bd.Bezier((rear, 15), (rear - 9, 17), (rear - 15, crown - 13),
                  (rear - 34, crown - 13))
        bd.Bezier((rear - 34, crown - 13), (rear - 48, crown - 13),
                  (mid + 13, scoop), (mid, scoop))
        bd.Bezier((mid, scoop), (mid - 16, scoop),
                  (front + 33, crown), (front + 21, crown))
        bd.Bezier((front + 21, crown), (front + 6, crown),
                  (front + 4, 23), (front, 19))
        bd.Line((front, 19), (front, 0))
    side = bd.Pos(X=x) * (bd.Plane.YZ * bd.extrude(bd.Face(outline.wire()), amount=WALL))
    curved_lips = [e for e in side.edges() if e.geom_type in (bd.GeomType.BEZIER, bd.GeomType.BSPLINE)]
    return bd.fillet(curved_lips, radius=0.55)


def _paper_pocket():
    left = PAPER_X - SIDE_GAP
    clear_width = v60_filters.STACK_THICKNESS + 2 * SIDE_GAP
    front = REAR_LINE - v60_filters.FILTER_RADIUS - SIDE_GAP
    rear = REAR_LINE + SIDE_GAP
    outer, divider = PAPER_GUIDE_HEIGHTS
    sides = _paper_wall(left - WALL, outer, PAPER_SCOOP)
    sides += _paper_wall(left + clear_width, divider, PAPER_SCOOP + 9)
    # End stops connect both walls outside the clear opening; the deck is the floor.
    for y, h in ((front - WALL, 19), (rear, 15)):
        sides += bd.Pos(left - WALL, y, 0) * bd.Box(
            clear_width + 2 * WALL, WALL, h, align=(bd.Align.MIN,) * 3
        )
    return sides


@model
def files():
    return _finish(bd.Compound(children=[_paper_pocket(), _cheek(OUTER_SCALE_X, 20)]),
                   "Deep V60 pocket and scale guide")


@model
def station():
    return _finish(bd.Pos(*PF, 0) * filled_station(), "Filled reversible head seat")


@model
def hanger():
    return _finish(bd.Pos(*WDT, 0) * cape().shape, "Open WDT cape")


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
    parts = fixtures()
    support = parts["hanger"]
    foot_edges = [e for e in support.edges() if e.bounding_box().max.Z < 1e-5]
    joined = parts["deck"].fuse(support)
    # Find the actual re-entrant seam after union, not the edge of a loose post.
    root_edges = [e for e in joined.edges()
                  if abs(e.bounding_box().min.Z) < 1e-5 and abs(e.bounding_box().max.Z) < 1e-5
                  and any(f.distance_to(e.position_at(0.5)) < 1e-5 for f in foot_edges)]
    joined = bd.fillet(root_edges, radius=ROOT_FILLET)
    tray = joined.fuse(parts["seat"], *parts["files"].solids())
    # Round the actual re-entrant fin/deck junctions, away from the openings.
    for x, radius in ((PAPER_X - SIDE_GAP - WALL, 3.0),
                      (PAPER_X + v60_filters.STACK_THICKNESS + SIDE_GAP + WALL, 1.25),
                      (OUTER_SCALE_X + SCALE_WALL, 1.5)):
        seam = []
        for e in tray.edges():
            box = e.bounding_box()
            if (abs(box.min.Z) < 1e-5 and abs(box.max.Z) < 1e-5
                    and abs(box.min.X-x) < 1e-5 and abs(box.max.X-x) < 1e-5
                    and box.size.Y > 90):
                seam.append(e)
        assert len(seam) == 1, f"Expected one structural fin seam at X={x}, found {len(seam)}"
        tray = bd.fillet(seam, radius=radius)
    assert tray.is_valid and len(tray.solids()) == 1, "tray must be one watertight solid"
    return _finish(tray, "Compact tray with integrated cape")


@model
def bed_ready():
    return _finish(bd.Pos(Z=THICKNESS) * empty().shape, "Compact four-tool tray")


def assembled(tamping=False):
    parts = groups(tamping)
    return {"tray": empty().shape, **{k: parts[k] for k in ("portafilter", "WDT", "scale", "papers")}}


@model
def parked():
    return bd.Compound(label="Compact tray, parked", children=list(assembled().values()))


def thin_packet(right=False):
    """Illustrative 1 mm remaining stack, against either wall; not sheet thickness."""
    thin = v60_filters.stack_envelope(1.0)
    x = (PAPER_X + v60_filters.STACK_THICKNESS + SIDE_GAP - 1.0
         if right else PAPER_X - SIDE_GAP)
    return (bd.Pos(x, REAR_LINE - v60_filters.FILTER_RADIUS, -SLOT_DEPTH)
            * bd.Rot(Z=90) * bd.Rot(X=90) * thin)


@model
def nearly_empty():
    pieces = assembled()
    pieces["papers"] = thin_packet(right=True)
    return bd.Compound(label="Compact tray, nearly empty filter pocket", children=list(pieces.values()))


@model
def tamp():
    return bd.Compound(label="Compact tray, tamping", children=list(assembled(True).values()))


if __name__ == "__main__":
    empty()
    bed_ready()
    parked()
    nearly_empty()
    tamp()
