"""Measured upright storage envelope for the small MUJI spray bottle (mm)."""

import build123d as bd
from cad import model


OUTSIDE_DIAMETER = 24.40
OVERALL_HEIGHT = 86.0


@model
def muji_spray_bottle():
    """Model the space occupied, without inventing a cap or sprayer profile."""
    bottle = bd.Cylinder(
        radius=OUTSIDE_DIAMETER / 2,
        height=OVERALL_HEIGHT,
        align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN),
    )
    bottle.label = "MUJI spray bottle (storage envelope)"
    bottle.color = "#90afaf"
    return bottle


if __name__ == "__main__":
    muji_spray_bottle()
