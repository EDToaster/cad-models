"""Alternative placements of one tool in one future seat, never simultaneous."""

import build123d as bd
from cad import model
from equipment.coffee.gaggia_portafilter import gaggia_portafilter


@model
def tamping_pose():
    """Handle toward the user (-Y); basket opening up."""
    return bd.Rot(Z=-90) * gaggia_portafilter().shape


@model
def storage_pose():
    """Handle toward the rear wall (+Y), about the same vertical basket axis."""
    return bd.Rot(Z=90) * gaggia_portafilter().shape


if __name__ == "__main__":
    tamping_pose()
    storage_pose()
