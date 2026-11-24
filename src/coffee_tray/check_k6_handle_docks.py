"""Check the seated crank and sample both lift-out paths, against the dock alone.

From src/: cad run -m coffee_tray.check_k6_handle_docks
"""

import build123d as bd

from coffee_tray.k6_handle_docks import (
    deck_rack,
    low_cradle,
    low_position,
    upright_position,
    upright_rack,
)
from equipment.coffee.kingrinder_k6 import crank_and_lid


def _shared_volume(a, b):
    common = a.intersect(b)
    return sum(solid.volume for solid in common.solids()) if common else 0.0


def _check(name, dock, parked, path):
    assert len(dock.solids()) == 1 and dock.is_valid, f"{name}: holder must be one valid solid"
    assert parked.distance_to(dock) < 1e-4, f"{name}: the crank does not touch its support"
    # Positive control: an exact check must catch a 1 mm intrusion into the rest.
    assert _shared_volume(dock, bd.Pos(Z=-1) * parked) > 0.1, f"{name}: contact check insensitive"
    for x, z in path:
        volume = _shared_volume(dock, bd.Pos(x, 0, z) * parked)
        assert volume < 1e-5, f"{name}: {volume:g} mm³ overlap at dx={x}, dz={z}"
    x, z = path[-1]
    assert (bd.Pos(x, 0, z) * parked).distance_to(dock) > 1.0, f"{name}: not fully released"
    print(f"{name}: seated contact, positive control, and {len(path)} overlap-free poses; released")


def main():
    crank = crank_and_lid().shape
    _check(
        "low", low_cradle().shape, low_position() * crank,
        [(0, z) for z in range(36)],
    )
    _check(
        "upright", upright_rack().shape, upright_position() * crank,
        [(0, z) for z in range(21)] + [(-x, 20) for x in range(1, 81)],
    )
    _check(
        "compact deck rack", deck_rack().shape, upright_position() * crank,
        [(0, z) for z in range(9)] + [(-x, 8) for x in range(1, 46)],
    )


if __name__ == "__main__":
    main()
