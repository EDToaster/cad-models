"""Detached K6 handle parking studies. Millimetres; deck is Z=0.

Build: cd src && cad run -m coffee_tray.k6_handle_docks
Check each empty holder: cad model dfm ID --process printing --technology fdm
"""

from math import hypot

import build123d as bd
from bd_materials import plastics
from bd_materials.processes import fdm
from cad import model
from equipment.coffee.kingrinder_k6 import LID_SEAT_Z, crank_and_lid


# Datums from the handle STEP, no added clearance in the reference tool.
LID_R = 27.25
LID_TOP = 13.75
ARM_R = 3.0
ARM_CENTER_Z = 17.5

DECK = 4.0
SIDE_PLAY = 0.8  # each side, provisional loose lift-out fit
V_SLOPE = 0.65
LOW_SEAT = 16.0
EDGE_V_APEX = 5.0
EDGE_LID_CENTER = EDGE_V_APEX + LID_R * hypot(1, V_SLOPE)
MIN_ALIGN = (bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN)


def _plate(x0, x1, width, radius):
    return bd.Pos((x0 + x1) / 2, 0, 0) * bd.extrude(
        bd.RectangleRounded(x1 - x0, width, radius), amount=DECK
    )


def _v_pad(x0, x1, half_width, apex):
    """Two planar tangencies with a round part, open at the top."""
    side_z = apex + half_width * V_SLOPE
    section = bd.Plane.YZ * bd.Polygon(
        (-half_width, DECK - 1), (half_width, DECK - 1),
        (half_width, side_z), (0, apex), (-half_width, side_z), align=None,
    )
    return bd.Pos(X=x0) * bd.extrude(section, amount=x1 - x0)


def _holder(part, label):
    part.label = label
    part.material = plastics.petg(process=fdm(layer_height_mm=0.2))
    part.color = "#679f98"
    return part


def low_position():
    return bd.Pos(Z=LOW_SEAT - LID_SEAT_Z)


def upright_position():
    # Lid on edge and crank pointing up; knob faces the open/front (-X) side.
    return bd.Pos(Z=EDGE_LID_CENTER) * bd.Rot(Y=-90)


@model
def low_cradle():
    """Seat only the lid's outer flange; the far V prevents the arm rotating."""
    base = bd.Cylinder(32, DECK, align=MIN_ALIGN) + _plate(-2, 118, 28, 8)
    seat = bd.Circle(30.8) - bd.Circle(23.6)  # clears underside lip R22.675
    lip = bd.Circle(30.8) - bd.Circle(LID_R + SIDE_PLAY)
    seat_wall = bd.Pos(Z=DECK) * bd.extrude(seat, amount=LOW_SEAT - DECK)
    fence = bd.Pos(Z=LOW_SEAT) * bd.extrude(lip, amount=2.5)
    arm_z = LOW_SEAT - LID_SEAT_Z + ARM_CENTER_Z
    arm_pad = _v_pad(96, 108, 9, arm_z - ARM_R * hypot(1, V_SLOPE))
    return _holder(base + seat_wall + fence + arm_pad, "Low lid-and-arm cradle")


def _upright_rack(front_edge, width, corner, guide_top):
    base = _plate(front_edge, 12, width, corner)
    # The lid spans X=[-13.75,-10.25]. Low cheeks flank it without hitting its
    # underside lip. A circular lid is free to roll without the higher arm guide.
    front = -LID_TOP - SIDE_PLAY
    back = -LID_SEAT_Z + SIDE_PLAY
    pad = _v_pad(front, back, 20, EDGE_V_APEX)
    pad += _v_pad(front - 4, front, 20, EDGE_V_APEX + 3)
    pad += _v_pad(back, back + 4, 20, EDGE_V_APEX + 3)
    # Sloped underside carries both fork tips back into the spine. No overhead
    # loop: after lifting the lid above the cheeks the arm exits toward -X.
    side = bd.Plane.XZ * bd.Polygon(
        (1.5, DECK - 1), (10.5, DECK - 1), (10.5, guide_top),
        (-26, guide_top), (-26, guide_top-11), (1.5, guide_top-38.5), align=None,
    )
    post = bd.Pos(Y=8) * bd.extrude(side, amount=16)
    throat = ARM_R + SIDE_PLAY
    slot_back = -ARM_CENTER_Z + throat
    slot = bd.Pos((slot_back - 40) / 2, 0, guide_top-7) * bd.Box(
        slot_back + 40, 2 * throat, 65
    )
    return _holder(base + pad + (post - slot), "Upright lid-edge rack")


@model
def upright_rack():
    """Original freestanding-footprint study, retained for comparison."""
    return _upright_rack(-73, 62, 10, 116)


@model
def deck_rack():
    """Compact Option B for the shared tray, not a freestanding stand."""
    return _upright_rack(-34, 46, 6, 102)


@model
def low_parked():
    return bd.Compound(label="Low crank parking", children=[
        low_cradle().shape, low_position() * crank_and_lid().shape,
    ])


@model
def upright_parked():
    return bd.Compound(label="Upright crank parking", children=[
        upright_rack().shape, upright_position() * crank_and_lid().shape,
    ])


if __name__ == "__main__":
    low_cradle()
    upright_rack()
    low_parked()
    upright_parked()
