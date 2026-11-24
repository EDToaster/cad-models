"""Export and verify the current printable tray. Run from src/ via cad run."""

from math import isclose
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

import build123d as bd
from cad import model

from coffee_tray.compact import bed_ready

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "dist" / "coffee-tray"
STEM = "compact-four-tool-tray"


def export_tray():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    tray = bed_ready()
    # Validate fresh outputs before replacing either deliverable on a local rerun.
    with TemporaryDirectory(dir=OUTPUT) as staging:
        work = Path(staging)
        step, stl = work / f"{STEM}.step", work / f"{STEM}.stl"
        raw = work / "raw.stl"
        model.export(tray, step)
        model.export(tray, raw, tolerance=0.06, angle=7)
        solid = bd.import_step(step)
        if not (solid.is_valid and len(solid.solids()) == 1
                and isclose(solid.volume, tray.shape.volume, rel_tol=1e-5)):
            raise ValueError("STEP did not round-trip as the same single solid")

        subprocess.run(["uv", "run", "--script", ROOT / "scripts/normalize_stl.py", raw, stl],
                       check=True)
        for path in (step, stl):
            print(path.replace(OUTPUT / path.name))


if __name__ == "__main__":
    export_tray()
