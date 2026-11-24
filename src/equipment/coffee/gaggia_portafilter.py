"""Gaggia bottomless portafilter: owner-measured side datums and layout proxies."""

import build123d as bd
from cad import model

# One reference configuration from Shades of Coffee; see gaggia_portafilter.md.
LENGTH = 215.0
EAR_SPAN = 78.0
GRIP_WIDTH, GRIP_HEIGHT = 35.0, 22.0

# Owner's measurements. Local Z=0 is the basket underside, not the tray deck.
BASKET_DEPTH = 26.30
NECK_EXPOSED_LENGTH = 22.8
NECK_THICKNESS = 10.0
NECK_DROP_BELOW_BASKET = 4.0
GRIP_DROP_BELOW_HEAD = 18.0

# Unverified geometry; not dimensions for a load-bearing fixture.
HEAD_RADIUS = 35.0
BORE_RADIUS = 30.5
# Basket bottom and metal head underside are separate physical datums. No offset
# between them was supplied; assume flush in this reference, not for seat sizing.
HEAD_BASE_Z = 0.0
HEAD_TOP_Z = BASKET_DEPTH - 1.0
FLARE_HEIGHT = 32.0  # shape estimate from the side photo


def _head():
    height = HEAD_TOP_Z - HEAD_BASE_Z
    section = bd.Circle(HEAD_RADIUS) - bd.Circle(BORE_RADIUS)
    body = bd.Pos(Z=HEAD_BASE_Z) * bd.extrude(section, amount=height)
    # Opposite curved ears with a 78 mm tip circle, not a 78 mm round head.
    outer = bd.Solid.make_cylinder(EAR_SPAN / 2, 7.0, angle=30.0)
    ear = outer - bd.Solid.make_cylinder(HEAD_RADIUS - 0.5, 7.0)
    for angle in (30.0, 210.0):
        body += bd.Pos(Z=16) * bd.Rot(Z=angle) * ear
    body.label, body.color = "Bottomless metal head", "#929b9f"
    return body


def _basket():
    # Closed thin-wall cup with rim; the perforated area is represented unpierced.
    profile = bd.Plane.XZ * bd.Polygon(
        (0, 0), (24.5, 0), (28, 3), (29.8, HEAD_TOP_Z),
        (34.5, HEAD_TOP_Z), (34.5, BASKET_DEPTH), (29, BASKET_DEPTH),
        (27.3, 3.4), (24.3, 0.8), (0, 0.8), align=None,
    )
    basket = bd.revolve(profile, axis=bd.Axis.Z)
    basket.label, basket.color = "Installed basket proxy", "#b5bec2"
    return basket


def _oval_at(x, z, width, height):
    return bd.Pos(x, 0, z) * (bd.Plane.YZ * bd.Ellipse(width / 2, height / 2))


def _handle():
    tip_x = LENGTH - HEAD_RADIUS
    grip_start = HEAD_RADIUS + NECK_EXPOSED_LENGTH
    neck_center_z = NECK_THICKNESS / 2 - NECK_DROP_BELOW_BASKET
    # A short buried tenon joins the curved head; it is not part of the exposed length.
    neck_start = HEAD_RADIUS - 1.5
    neck_section = bd.Plane.YZ * bd.RectangleRounded(15.0, NECK_THICKNESS, 1.5)
    neck = bd.Pos(neck_start, 0, neck_center_z) * bd.extrude(
        neck_section, amount=grip_start - neck_start
    )
    neck.label, neck.color = "Metal neck", "#868f94"
    grip_low = HEAD_BASE_Z - GRIP_DROP_BELOW_HEAD
    # Photo: the low point is at the flared ring by the neck, not the distal tip.
    # These ruling stations approximate the contour; the first anchors the measured low.
    grip = bd.loft([
        _oval_at(grip_start, grip_low + FLARE_HEIGHT / 2, GRIP_WIDTH, FLARE_HEIGHT),
        _oval_at(grip_start + 3, grip_low + 16, 33, 28),
        _oval_at(grip_start + 9, grip_low + 16.5, 30, 23),
        _oval_at(grip_start + 15, grip_low + 17, 29, GRIP_HEIGHT),
        _oval_at(tip_x - 5, grip_low + 18.5, 32, 20),
        _oval_at(tip_x - 1, grip_low + 18.5, 30, 18),
        _oval_at(tip_x, grip_low + 18.5, 28, 16),
    ], ruled=True)
    grip.label, grip.color = "Black plastic grip", "#363b41"
    return neck, grip


def components():
    """Separate reference solids for checking metal bearing, basket and grip clearance."""
    neck, grip = _handle()
    return _head(), _basket(), neck, grip


@model
def gaggia_portafilter():
    """Basket axis at X=Y=0, lowest basket point at Z=0, handle along +X."""
    body, basket, neck, grip = components()
    head = body + neck
    head.label, head.color = "Bottomless metal head and neck", "#929b9f"
    return bd.Compound(
        label="Gaggia bottomless portafilter reference",
        children=[head, basket, grip],
    )


if __name__ == "__main__":
    gaggia_portafilter()
