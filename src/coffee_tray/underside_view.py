"""Presentation pose only. The print export still uses compact.bed_ready."""

import build123d as bd
from cad import model

from coffee_tray.compact import STONE, bed_ready


@model
def underside():
    """Turn the actual print body over so studio lighting reaches the pockets."""
    shape = bd.Rot(Z=90) * bd.Rot(X=180) * bed_ready().shape
    shape.label, shape.color = "Four-tool tray, underside", STONE
    return shape


if __name__ == "__main__":
    underside()
