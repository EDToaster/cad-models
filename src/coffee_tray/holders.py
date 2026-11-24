"""Shared provisional holder geometry, in local coordinates with deck at Z=0."""

from math import sqrt

import build123d as bd

from equipment.coffee import wdt

BASE_ALIGN = (bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN)
NEEDLE_GAP = 5.0


def two_way_riser():
    """Outer head annulus with front and back neck clearance."""
    seat = bd.extrude(bd.Circle(34.5) - bd.Circle(31), amount=20)
    return seat - bd.Pos(Z=19) * bd.Box(22, 80, 12)


def open_wdt_hanger(post_radius=0):
    """Matched conic seat on a straight post. Mouth opens toward negative Y."""
    r = wdt.BOTTOM_DIAMETER / 2
    dr = wdt.MAX_DIAMETER / 2 - r
    slope = dr / sqrt(wdt.TAPER_SLANT**2 - dr**2)
    z0, z1 = 16.0, 24.0  # axial distances above the handle's needle face
    needle_face = NEEDLE_GAP + wdt.NEEDLE_REACH
    h = z1 - z0
    collar = bd.Cylinder(18.75, h, align=BASE_ALIGN) - bd.Cone(
        r + z0 * slope, r + z1 * slope, h, align=BASE_ALIGN
    )
    collar -= bd.Pos(0, -11, -1) * bd.Box(14, 22, h + 2, align=BASE_ALIGN)
    profile = bd.RectangleRounded(6, 6, post_radius) if post_radius else bd.Rectangle(6, 6)
    post = bd.Pos(Y=18.5) * bd.extrude(profile, amount=needle_face + z1)
    return post + bd.Pos(Z=needle_face + z0) * collar
