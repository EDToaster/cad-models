"""Needles-down WDT reference. Only the handle profile and reach are measured."""

from math import sqrt

import build123d as bd
from cad import model


HANDLE_HEIGHT = 40.5
BOTTOM_DIAMETER = 24.0
MAX_DIAMETER = 31.5
TAPER_SLANT = 34.22
NEEDLE_REACH = 70.0

# Layout witnesses only, not a measured needle pattern or a keep-out volume.
ILLUSTRATIVE_PITCH_RADIUS = 7.0
ILLUSTRATIVE_WIRE_RADIUS = 0.25


@model
def wdt_handle():
    """Needle attachment face at local Z=0; widest upper band bounds the crown."""
    radial_change = (MAX_DIAMETER - BOTTOM_DIAMETER) / 2
    taper_rise = sqrt(TAPER_SLANT**2 - radial_change**2)
    remaining_height = HANDLE_HEIGHT - taper_rise
    if remaining_height < 0:
        raise ValueError("The taper rise exceeds the overall handle height.")
    base = (bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN)
    handle = bd.Cone(BOTTOM_DIAMETER / 2, MAX_DIAMETER / 2, taper_rise, align=base)
    if remaining_height > 0:
        handle += bd.Pos(Z=taper_rise) * bd.Cylinder(
            MAX_DIAMETER / 2, remaining_height, align=base
        )
    handle.label, handle.color = "Tapered grip envelope", "#594641"
    return handle


@model
def wdt_tool():
    """Stored orientation: the lowest tips are at Z=0; no hanger or tray included."""
    handle = bd.Pos(Z=NEEDLE_REACH) * wdt_handle().shape
    pitch = ILLUSTRATIVE_PITCH_RADIUS
    markers = []
    for i, (x, y) in enumerate(((pitch, 0), (0, pitch), (-pitch, 0), (0, -pitch))):
        wire = bd.Pos(x, y, NEEDLE_REACH / 2) * bd.Cylinder(
            ILLUSTRATIVE_WIRE_RADIUS, NEEDLE_REACH
        )
        wire.label, wire.color = f"Illustrative needle {i + 1}", "#776e67"
        markers.append(wire)
    return bd.Compound(label="WDT tool reference", children=[handle, *markers])


if __name__ == "__main__":
    wdt_handle()
    wdt_tool()
