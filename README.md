# CAD models

Parametric CAD for measured objects and the things that fit them. The first project is a [coffee gear tray](src/coffee_tray/README.md).

## Layout

- `src/equipment/`: reusable reference models, grouped by purpose. [Coffee gear](src/equipment/coffee/) lives here, independent of any tray.
- `src/common/`: geometry helpers shared by multiple models. Keep a helper with its first model until a second model needs it.
- `src/coffee_tray/`: the printable parts and the assembly that places the reference models. Fit allowances belong here, not in the equipment dimensions.

## CAD workflow

Use the [text-to-cad CAD skill](https://github.com/earthtojake/text-to-cad/blob/b61fb3a974737e27d7b87a2b518a846d11861bc9/skills/cad/SKILL.md) and its [project layout guide](https://github.com/earthtojake/text-to-cad/blob/b61fb3a974737e27d7b87a2b518a846d11861bc9/skills/cad/references/project-layout.md). The links pin the workflow to the revision used to start this repository.

```sh
uv tool install 'cad==0.11.17'
cad --version
cad server start
```

Run models as Python modules from `src/` with `cad run -m <module>`. Use millimetres with +Z up. Store the as-measured dimensions beside each model; distinguish direct measurements, manufacturer specifications and estimates. Never encode an unknown dimension as zero or silently substitute a catalogue size.

For each iteration, commit the source and measurement notes together. Compare the built geometry to the supplied measurements and inspect a preview before accepting the model. During tray design, check the assembled clearances separately. Generated exports are reproducible; release print files deliberately rather than checking them in on every run.

## Download STEP and STL

Open [Export tray CAD](https://github.com/EDToaster/cad-models/actions/workflows/export-cad.yml), select a successful run, and download the `compact-four-tool-tray-<commit>` artifact. It contains the STEP solid and the millimetre STL of the same bed-oriented tray, without equipment. Artifacts are retained for 30 days; use **Run workflow** to regenerate them. CAD-source or workflow changes on pushes to `main` and pull requests targeting `main` trigger a fresh build. Generated binaries are not committed.

To reproduce locally, install the CAD CLI above and the PrusaSlicer CLI (`prusa-slicer`), start the CAD server and run:

```sh
cd src
cad run -m coffee_tray.check_compact
cad run -m coffee_tray.exports
```

The files appear in `dist/coffee-tray/` at the repository root. The exporter reopens the STEP to check that it is a valid single solid with matching volume, and checks that the normalized STL is one manifold part at Z=0. These checks do not replace slicing or a physical fit check.
