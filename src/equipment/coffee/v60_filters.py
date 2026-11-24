"""Nominal envelope of a folded V60 filter stack, laid flat, in millimetres."""

import build123d as bd
from cad import model


FILTER_RADIUS = 128.0
STACK_THICKNESS = 20.0


@model
def v60_filter_stack():
    """Place the fold's right-angle corner at the origin, straight edges on +X/+Y."""
    stack = bd.Cylinder(
        radius=FILTER_RADIUS,
        height=STACK_THICKNESS,
        arc_size=90,
        align=(bd.Align.MIN, bd.Align.MIN, bd.Align.MIN),
    )
    stack.label = "Folded V60 filter stack"
    stack.color = "#dfcfae"
    return stack


if __name__ == "__main__":
    v60_filter_stack()
