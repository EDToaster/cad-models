"""Filled, reversible tamping pedestal. Local origin is the head axis at deck level."""

from math import sqrt

import build123d as bd

HEIGHT = 20.0
RELIEF = 6.0
FLOOR_Z = HEIGHT - RELIEF
LAND_IN, LAND_OUT = 31.5, 34.55
OUTSIDE_R = 35.8
BASE_BLEND = 3.0
WELL_BLEND = 2.3
ROOT2 = sqrt(2)


def _pedestal():
    # Revolve the load path, including real tangent fillets, not a hollow ring.
    floor_r = 30.4 - WELL_BLEND
    toe = OUTSIDE_R + BASE_BLEND
    top_blend = OUTSIDE_R - LAND_OUT
    lip = LAND_IN - 30.4
    with bd.BuildLine() as profile:
        bd.Line((0, 0), (toe, 0))
        bd.ThreePointArc((toe, 0), (toe - BASE_BLEND/ROOT2, BASE_BLEND - BASE_BLEND/ROOT2),
                         (OUTSIDE_R, BASE_BLEND))
        bd.Line((OUTSIDE_R, BASE_BLEND), (OUTSIDE_R, HEIGHT-top_blend))
        bd.ThreePointArc((OUTSIDE_R, HEIGHT-top_blend),
                         (LAND_OUT + top_blend/ROOT2, HEIGHT-top_blend + top_blend/ROOT2),
                         (LAND_OUT, HEIGHT))
        bd.Line((LAND_OUT, HEIGHT), (LAND_IN, HEIGHT))
        bd.ThreePointArc((LAND_IN, HEIGHT),
                         (LAND_IN-lip/ROOT2, HEIGHT-lip+lip/ROOT2), (30.4, HEIGHT-lip))
        bd.Line((30.4, HEIGHT-lip), (30.4, FLOOR_Z+WELL_BLEND))
        bd.ThreePointArc((30.4, FLOOR_Z+WELL_BLEND),
                         (floor_r + WELL_BLEND/ROOT2, FLOOR_Z + WELL_BLEND-WELL_BLEND/ROOT2),
                         (floor_r, FLOOR_Z))
        bd.Polyline((floor_r, FLOOR_Z), (0, FLOOR_Z), (0, 0))
    return bd.revolve(bd.Plane.XZ * bd.Face(profile.wire()), axis=bd.Axis.Z)


def _neck_relief():
    # Cut both opposite approaches in one pass. A rounded trough, not a sharp
    # rectangular notch; the neck stays unloaded even where it drops below the head.
    r, lip = 3.5, 1.5
    w = 11.0
    flat = w - r
    with bd.BuildLine() as outline:
        bd.Line((-flat, FLOOR_Z), (flat, FLOOR_Z))
        bd.ThreePointArc((flat, FLOOR_Z),
                         (flat+r/ROOT2, FLOOR_Z+r-r/ROOT2), (w, FLOOR_Z+r))
        bd.Line((w, FLOOR_Z+r), (w, HEIGHT-lip))
        bd.ThreePointArc((w, HEIGHT-lip), (w+lip-lip/ROOT2, HEIGHT-lip+lip/ROOT2),
                         (w+lip, HEIGHT))
        bd.Polyline((w+lip, HEIGHT), (w+lip, HEIGHT+3), (-w-lip, HEIGHT+3), (-w-lip, HEIGHT))
        bd.ThreePointArc((-w-lip, HEIGHT), (-w-lip+lip/ROOT2, HEIGHT-lip+lip/ROOT2),
                         (-w, HEIGHT-lip))
        bd.Line((-w, HEIGHT-lip), (-w, FLOOR_Z+r))
        bd.ThreePointArc((-w, FLOOR_Z+r),
                         (-flat-r/ROOT2, FLOOR_Z+r-r/ROOT2), (-flat, FLOOR_Z))
    return bd.extrude(bd.Plane.XZ * bd.Face(outline.wire()), amount=50, both=True, dir=(0, 1, 0))


def filled_station():
    return _pedestal() - _neck_relief()
