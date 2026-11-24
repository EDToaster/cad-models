"""Nominal envelope of a folded V60 filter stack, laid flat, in millimetres."""

import build123d as bd
from cad import model


FILTER_RADIUS = 128.0
STACK_THICKNESS = 20.0


def stack_envelope(thickness):
    """Quarter-circle stack with a given thickness, straight edges on +X and +Y."""
    if thickness <= 0:
        raise ValueError("Stack thickness must be positive")
    stack = bd.Cylinder(
        radius=FILTER_RADIUS,
        height=thickness,
        arc_size=90,
        align=(bd.Align.MIN, bd.Align.MIN, bd.Align.MIN),
    )
    stack.label = "Folded V60 filter stack"
    stack.color = "#dfcfae"
    return stack


@model
def v60_filter_stack():
    """Owner-measured full stack, independent of the tray's fit allowance."""
    return stack_envelope(STACK_THICKNESS)


if __name__ == "__main__":
    v60_filter_stack()
