"""Run with cad run -m coffee_tray.check_compact from src/."""

from coffee_tray.check_layout import check_groups
from coffee_tray.compact import DEPTH, THICKNESS, WIDTH, groups


if __name__ == "__main__":
    for tamping in (False, True):
        check_groups(groups(tamping), WIDTH, DEPTH, THICKNESS, tamping)
