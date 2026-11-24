# Manual WDT tool

The tool hangs needles-down. The grip and complete tool are independently rebuildable from `src/` with `cad run -m equipment.coffee.wdt`. The reference has no holder allowances.

| Owner-supplied measurement | mm |
| --- | ---: |
| Handle height, parallel to axis | 40.5 |
| Handle diameter at needle end | 24 |
| Maximum handle diameter | 31.5 |
| Straight taper length, along the sloping surface | 34.22 |
| Exposed needle reach from the handle | 70 |

Assuming the main taper starts at the bottom face and runs to the widest point, the radius increases by 3.75 mm. Its **axial rise is 34.014 mm**: `sqrt(34.22² − 3.75²)`, not 34.22 mm. The half-angle is about 6.29° to the axis. The remaining 6.486 mm of handle height is bounded at the maximum diameter; the crown and decorative flutes are not measured.

In the complete model, the tip datum is Z=0, the needle-end face is at Z=70, and the grip top is at Z=110.5 mm. Only the reach of the needle bundle is measured. The displayed wires are visual stand-ins: count, diameter, pitch and relaxed spread are not fit evidence. The measured maximum grip diameter alone does not establish the complete tool's lateral envelope. Do not use the visual wires for collision checks or collar-gap sizing.
