"""Use the owner's exact STEP bodies, with one explicitly inferred attached pose."""

from pathlib import Path

import build123d as bd
from cad import model, step


INPUTS = Path(__file__).resolve().parents[3] / "vendor" / "kingrinder_k6"

# Imported local-Z datums in millimetres: body top and lid's outer seating face.
BODY_TOP_Z = 170.5
LID_SEAT_Z = 10.25


@model
def grinder_body():
    part = step.read(INPUTS / "Grinder.step")
    part.label, part.color = "Grinder body", "#555b61"
    return part


@model
def crank_and_lid():
    part = step.read(INPUTS / "Handle.step")
    part.label, part.color = "Lid crank and knob", "#9b8066"
    return part


@model
def attached_layout():
    """Outer storage envelope, not a verified joint: see the measured overlap."""
    body = grinder_body().shape
    handle = bd.Pos(Z=BODY_TOP_Z - LID_SEAT_Z) * crank_and_lid().shape
    return bd.Compound(label="K6 provisional attached pose", children=[body, handle])


if __name__ == "__main__":
    grinder_body()
    crank_and_lid()
    attached_layout()
