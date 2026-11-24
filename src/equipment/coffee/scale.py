"""Storage reference for a small coffee scale; see scale.md for dimension sources."""

import build123d as bd
from cad import model


# Caliper envelope, millimetres, normal weighing position.
WIDTH = 128.2
LENGTH = 148.4
THICKNESS = 23.5  # overall, feet included

# Underside plan estimated from a perspective photo; not fit datums.
CORNER_RADIUS = 8.0
FOOT_DIAMETER = 11.0
FOOT_INSET_X = 20.5
FOOT_INSET_Y = 20.5
FOOT_PROJECTION = 2.0  # illustrative until the side profile is measured


def _scale_body():
    outline = bd.RectangleRounded(WIDTH, LENGTH, CORNER_RADIUS)
    shell = bd.Pos(Z=FOOT_PROJECTION) * bd.extrude(
        outline, amount=THICKNESS - FOOT_PROJECTION
    )
    shell.label, shell.color = "Weighing body", "#555a60"
    parts = [shell]
    for ix in (-1, 1):
        for iy in (-1, 1):
            foot = bd.Pos(
                ix * (WIDTH / 2 - FOOT_INSET_X),
                iy * (LENGTH / 2 - FOOT_INSET_Y),
                FOOT_PROJECTION / 2,
            ) * bd.Cylinder(FOOT_DIAMETER / 2, FOOT_PROJECTION)
            foot.label, foot.color = f"Foot {ix:+d} {iy:+d}", "#27292c"
            parts.append(foot)
    return bd.Compound(label="Scale reference", children=parts)


@model
def scale_flat():
    """Feet down: width along X, long axis along Y, bottom at Z=0."""
    return _scale_body()


@model
def scale_on_long_edge():
    """Storage pose: length along X, thickness along Y, edge tangent to Z=0."""
    # The two rotations keep the physical long side horizontal, and map the
    # underside toward -Y so all four feet can be inspected in the front view.
    return (
        bd.Pos(Y=-THICKNESS / 2, Z=WIDTH / 2)
        * bd.Rot(X=-90)
        * bd.Rot(Z=90)
        * scale_flat().shape
    )


if __name__ == "__main__":
    scale_flat()
    scale_on_long_edge()
