"""Black plastic-handled Gaggia bottomless portafilter: layout proxy, not fit CAD."""

import build123d as bd
from cad import model

# One reference configuration from Shades of Coffee; see gaggia_portafilter.md.
LENGTH = 215.0
EAR_SPAN = 78.0
GRIP_WIDTH, GRIP_HEIGHT = 35.0, 22.0
BASKET_DEPTH = 28.0

# Unverified geometry; not dimensions for a load-bearing fixture.
HEAD_RADIUS = 35.0
BORE_RADIUS = 30.5
HEAD_BASE_Z = 6.0
HEAD_TOP_Z = BASKET_DEPTH - 1.0


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
    # The oval section is sourced; neck, contour and handle inclination are estimates.
    neck = bd.loft([_oval_at(34.5, 17, 15, 13), _oval_at(49, 17, 16, 14)], ruled=True)
    neck.label, neck.color = "Metal neck", "#868f94"
    grip = bd.loft([
        _oval_at(49, 17, 26, 18),
        _oval_at(55, 17, GRIP_WIDTH, GRIP_HEIGHT),
        _oval_at(65, 16.5, 30, 20),
        _oval_at(tip_x - 3, 14, GRIP_WIDTH, GRIP_HEIGHT),
        _oval_at(tip_x, 14, 33, 20),
    ], ruled=True)
    grip.label, grip.color = "Black plastic grip", "#363b41"
    return neck, grip


@model
def gaggia_portafilter():
    """Basket axis at X=Y=0, lowest basket point at Z=0, handle along +X."""
    neck, grip = _handle()
    head = _head() + neck
    head.label, head.color = "Bottomless metal head and neck", "#929b9f"
    return bd.Compound(
        label="Gaggia bottomless portafilter reference",
        children=[head, _basket(), grip],
    )


if __name__ == "__main__":
    gaggia_portafilter()
