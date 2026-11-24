"""Open, self-supporting WDT cape. Coordinates local to the needle axis; mm."""

from math import cos, pi, radians, sin, sqrt

import build123d as bd
from cad import model

from coffee_tray.holders import NEEDLE_GAP
from equipment.coffee import wdt

SEAT_BOTTOM = NEEDLE_GAP + wdt.NEEDLE_REACH + 16
SEAT_TOP = SEAT_BOTTOM + 8
ROOT_FILLET = 2.0


def seat_radius(z):
    dr = (wdt.MAX_DIAMETER - wdt.BOTTOM_DIAMETER) / 2
    rise = sqrt(wdt.TAPER_SLANT**2 - dr**2)
    return wdt.BOTTOM_DIAMETER / 2 + (z - NEEDLE_GAP - wdt.NEEDLE_REACH) * dr / rise


def _section(z, inner, outer, angle, fold):
    """One horseshoe section. Rounded hems have no sharp corners at the mouth."""
    half = radians(angle)

    def p(r, a):
        return bd.Vector(r * sin(a), r * cos(a), z)

    pts = []
    for i in range(25):
        t = (i - 12) / 12
        # Three soft longitudinal folds on the back; vanish at mouth and collar.
        r = outer + fold * cos(pi*t/2)**2 * (0.5 + 0.5*cos(3*pi*t))
        pts.append(p(r, t * half))
    exterior = bd.Edge.make_spline(pts)
    arc = bd.Edge.make_three_point_arc
    mid, cap_r = (inner + outer) / 2, (outer - inner) / 2
    right = p(mid, half) + bd.Vector(cap_r*cos(half), -cap_r*sin(half), 0)
    left = p(mid, -half) + bd.Vector(-cap_r*cos(half), -cap_r*sin(half), 0)
    return bd.Wire([exterior,
                    arc(pts[-1], right, p(inner, half)),
                    arc(p(inner, half), p(inner, 0), p(inner, -half)),
                    arc(p(inner, -half), left, pts[0])])


@model
def cape():
    # Flared hem, gathered waist, then two shoulders rising into the seat.
    # A separate ruled final band preserves the measured straight conical taper.
    stations = [
        (0, 15.6, 21.0, 94, 0.7), (4, 15.9, 20.5, 88, 0.9),
        (16, 16.3, 20.1, 66, 1.6), (33, 16.5, 20.4, 48, 2.0),
        (46, 16.5, 20.6, 51, 2.1), (61, 16.2, 20.5, 73, 1.8),
        (76, 15.4, 20.0, 105, 1.2), (85, 14.6, 19.2, 126, 0.5),
        (SEAT_BOTTOM, seat_radius(SEAT_BOTTOM), 18.8, 138, 0),
    ]
    profiles = [_section(*s) for s in stations]
    body = bd.Solid.make_loft(profiles)
    band = bd.Solid.make_loft([profiles[-1], _section(SEAT_TOP, seat_radius(SEAT_TOP),
                                                       18.8, 138, 0)], ruled=True)
    part = body.fuse(band)
    # Round the touch edge at the mouth but retain the conical bearing band.
    rim = part.edges().group_by(bd.Axis.Z)[-1]
    part = bd.fillet(rim, radius=0.6)
    part.label, part.color = "Open cape WDT holder", "#cab8a0"
    return part


if __name__ == "__main__":
    cape()
