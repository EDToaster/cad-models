"""Export and verify the current printable tray. Run from src/ via cad run."""

from math import isclose
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

import build123d as bd
from cad import model

from coffee_tray.compact import bed_ready

OUTPUT = Path(__file__).resolve().parents[2] / "dist" / "coffee-tray"
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

        subprocess.run(["prusa-slicer", "--export-stl", "--output", stl, raw], check=True)
        info = subprocess.check_output(["prusa-slicer", "--info", stl], text=True)
        print(info, flush=True)
        fields = {key.strip(): value.strip() for line in info.splitlines() if "=" in line
                  for key, value in [line.split("=", 1)]}
        if fields.get("manifold") != "yes" or fields.get("number_of_parts") != "1":
            raise ValueError("STL did not round-trip as one manifold part")
        if not isclose(float(fields["min_z"]), 0.0, abs_tol=0.001):
            raise ValueError("STL no longer sits flat on the build plate at Z=0")
        for path in (step, stl):
            print(path.replace(OUTPUT / path.name))


if __name__ == "__main__":
    export_tray()
