"""First full tray mockup. X across; Y toward wall; deck top is Z=0. All mm."""

import build123d as bd
from cad import model

from coffee_tray.k6_handle_docks import deck_rack, upright_position
from coffee_tray.holders import open_wdt_hanger, two_way_riser
from coffee_tray.portafilter_poses import storage_pose, tamping_pose
from equipment.coffee import dosing_ring, muji_spray_bottle, normcore_tamper_cap
from equipment.coffee import scale, v60_filters, wdt
from equipment.coffee.kingrinder_k6 import crank_and_lid, grinder_body

WIDTH, DEPTH, THICKNESS = 203.2, 241.3, 10.0
PF = (39.0, 49.0)
CAP = (106.0, 55.0)
FUNNEL = (168.5, 34.0)
SPRAY = (82.0, 111.0)
GRINDER = (105.5, 210.5)
WDT = (148.5, 83.0)
SCALE = (187.5, 152.0)
PAPER = (151.5, 107.0)  # near corner; stack runs +X, straight edge runs +Y
CRANK = (106.0, 167.0)  # crank datum, using the compact version of option B
ROUND_DEPTH, SLOT_DEPTH, SIDE_GAP = 2.5, 4.5, 0.5
BASE_ALIGN = (bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN)
HOLDER_COLOR = "#72a29a"


def _at(xy, z=0):
    return bd.Pos(*xy, z)


def _round(xy, r, z, height):
    return _at(xy, z) * bd.Cylinder(r, height, align=BASE_ALIGN)


def _block(x, y, z, dx, dy, dz):
    return bd.Pos(x, y, z) * bd.Box(
        dx, dy, dz, align=(bd.Align.MIN, bd.Align.MIN, bd.Align.MIN)
    )


def _styled(part, label, color=HOLDER_COLOR):
    part.label, part.color = label, color
    return part


@model
def tray_blank():
    """10 mm stock; shallow pockets and edge slots retain an unbroken floor."""
    part = bd.Pos(WIDTH/2, DEPTH/2, -THICKNESS) * bd.extrude(
        bd.RectangleRounded(WIDTH, DEPTH, 4), amount=THICKNESS
    )
    for xy, diameter in (
        (CAP, normcore_tamper_cap.OUTSIDE_DIAMETER),
        (FUNNEL, dosing_ring.OUTSIDE_DIAMETER),
        (SPRAY, muji_spray_bottle.OUTSIDE_DIAMETER),
        (GRINDER, 52.0),  # K6 lower body OD, not its shoulder
    ):
        part -= _round(xy, diameter/2 + SIDE_GAP, -ROUND_DEPTH, ROUND_DEPTH + 1)
    for xy, dx, dy in (
        (SCALE, scale.THICKNESS, scale.LENGTH),
        ((PAPER[0]+v60_filters.STACK_THICKNESS/2, PAPER[1]+v60_filters.FILTER_RADIUS/2),
         v60_filters.STACK_THICKNESS, v60_filters.FILTER_RADIUS),
    ):
        part -= _at(xy, -SLOT_DEPTH) * bd.Box(
            dx+2*SIDE_GAP, dy+2*SIDE_GAP, SLOT_DEPTH+1, align=BASE_ALIGN
        )
    return _styled(part, "10 mm deck", "#c2c3ad")


@model
def file_guides():
    # One common divider and two outside cheeks. Leave ends open for fingers.
    guides = [_block(x, 119, 0, 2, 99, height) for x, height in
              ((148.5, 22), (172.5, 27), (200.0, 22))]
    return _styled(bd.Compound(children=guides), "Scale and paper guides")


@model
def pf_riser():
    return _styled(_at(PF) * two_way_riser(), "Provisional two-way head support")


@model
def wdt_hanger():
    return _styled(_at(WDT) * open_wdt_hanger(), "WDT hanger")


def groups(tamping=False):
    """Top-level groups for exact inter-item checks; exclude internal STEP mates."""
    return {
        "deck": tray_blank().shape,
        "file guides": file_guides().shape,
        "head support": pf_riser().shape,
        "hanger": wdt_hanger().shape,
        "portafilter": _at(PF) * (tamping_pose() if tamping else storage_pose()).shape,
        "cap": _at(CAP, -ROUND_DEPTH) * normcore_tamper_cap.normcore_tamper_cap().shape,
        "funnel": _at(FUNNEL, -ROUND_DEPTH) * dosing_ring.dosing_ring().shape,
        "bottle": _at(SPRAY, -ROUND_DEPTH) * muji_spray_bottle.muji_spray_bottle().shape,
        "grinder": _at(GRINDER, -ROUND_DEPTH) * grinder_body().shape,
        "crank dock": _at(CRANK) * bd.Rot(Z=90) * deck_rack().shape,
        "crank": _at(CRANK) * bd.Rot(Z=90) * upright_position() * crank_and_lid().shape,
        "WDT": _at(WDT, 5) * wdt.wdt_tool().shape,
        "scale": _at(SCALE, -SLOT_DEPTH) * bd.Rot(Z=90) * scale.scale_on_long_edge().shape,
        "papers": _at(PAPER, -SLOT_DEPTH) * bd.Rot(Z=90) * bd.Rot(X=90)
                  * v60_filters.v60_filter_stack().shape,
    }


@model
def stored():
    return bd.Compound(label="Stored layout", children=list(groups().values()))


@model
def tamping():
    return bd.Compound(label="Tamping layout", children=list(groups(tamping=True).values()))


if __name__ == "__main__":
    stored()
    tamping()
