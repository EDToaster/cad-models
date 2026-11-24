"""Measured straight-sided espresso dosing ring. All dimensions in millimetres."""

import build123d as bd
from cad import model


OUTSIDE_DIAMETER = 62.0
INSIDE_DIAMETER = 53.0
HEIGHT = 28.0


@model
def dosing_ring():
    """Annular section with a through bore; the bottom face lies on Z=0."""
    section = bd.Circle(OUTSIDE_DIAMETER / 2) - bd.Circle(INSIDE_DIAMETER / 2)
    ring = bd.extrude(section, amount=HEIGHT)
    ring.label = "Espresso dosing ring"
    ring.color = "#767b80"
    return ring


if __name__ == "__main__":
    dosing_ring()
