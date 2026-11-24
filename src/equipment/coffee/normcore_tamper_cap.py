"""External locating envelope for the cap of the 58.5 mm Normcore V4 tamper."""

import build123d as bd
from cad import model


OUTSIDE_DIAMETER = 64.0
CAP_HEIGHT = 13.0


@model
def normcore_tamper_cap():
    """Full exterior envelope; unmeasured recess and edge details are omitted."""
    cap = bd.Cylinder(
        radius=OUTSIDE_DIAMETER / 2,
        height=CAP_HEIGHT,
        align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN),
    )
    cap.label = "Normcore V4 tamper cap (outer envelope)"
    cap.color = "#56585c"
    return cap


if __name__ == "__main__":
    normcore_tamper_cap()
