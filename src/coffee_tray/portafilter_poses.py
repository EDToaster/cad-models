"""Alternative placements of one tool in one future seat, never simultaneous."""

import build123d as bd
from cad import model
from equipment.coffee.gaggia_portafilter import (
    GRIP_DROP_BELOW_HEAD,
    HEAD_BASE_Z,
    gaggia_portafilter,
)

# Positive air gap for layout only, not a validated loaded/printed fit tolerance.
MOCKUP_GRIP_GAP = 2.0


def _on_raised_seat(angle):
    head_underside_above_deck = GRIP_DROP_BELOW_HEAD + MOCKUP_GRIP_GAP
    lift = head_underside_above_deck - HEAD_BASE_Z
    return bd.Pos(Z=lift) * bd.Rot(Z=angle) * gaggia_portafilter().shape


@model
def tamping_pose():
    """Handle toward the user (-Y); basket opening up."""
    return _on_raised_seat(-90)


@model
def storage_pose():
    """Handle toward the rear wall (+Y), about the same vertical basket axis."""
    return _on_raised_seat(90)


if __name__ == "__main__":
    tamping_pose()
    storage_pose()
