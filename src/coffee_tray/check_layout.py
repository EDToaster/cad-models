"""Check both seated layouts, not removal sweeps, hand access or loaded strength.

Run from src/: cad run -m coffee_tray.check_layout
"""

from itertools import combinations
from math import isclose

def _positive_box_overlap(a, b):
    return all(
        min(hi_a, hi_b) > max(lo_a, lo_b) + 1e-6
        for lo_a, hi_a, lo_b, hi_b in zip(a.min, a.max, b.min, b.max)
    )


def check_groups(parts, width, depth, thickness, tamping):
    boxes = {key: obj.bounding_box() for key, obj in parts.items()}
    deck_size = boxes["deck"].size
    assert all(isclose(a, b, abs_tol=1e-5)
               for a, b in zip(deck_size, (width, depth, thickness)))
    assert all(s.is_valid for s in parts.values())
    for name, box in boxes.items():
        assert box.min.X >= -1e-5 and box.max.X <= width+1e-5, name
        assert box.max.Y <= depth+1e-5, name
        if not (tamping and name == "portafilter"):
            assert box.min.Y >= -1e-5, name
    collisions = []
    for a, b in combinations(parts, 2):
        if not _positive_box_overlap(boxes[a], boxes[b]):
            continue
        for sa in parts[a].solids():
            for sb in parts[b].solids():
                if not _positive_box_overlap(sa.bounding_box(), sb.bounding_box()):
                    continue
                common = sa.intersect(sb)
                overlap = sum(s.volume for s in common.solids()) if common else 0
                if overlap >= 0.001:
                    collisions.append(f"{a} / {b}: {overlap:.4f} mm³")
    assert not collisions, collisions
    pf = boxes["portafilter"]
    overhang = max(0, -pf.min.Y)
    assert (overhang > 0) == tamping
    print(f"{'tamping' if tamping else 'parked'}: {len(parts)} valid groups; no positive "
          f"inter-item overlap; front overhang {overhang:.1f} mm; "
          f"PF rear edge Y={pf.max.Y:.1f} mm; highest Z={max(b.max.Z for b in boxes.values()):.1f} mm above deck")


if __name__ == "__main__":
    from coffee_tray.layout import DEPTH, THICKNESS, WIDTH, groups

    for tamping in (False, True):
        check_groups(groups(tamping), WIDTH, DEPTH, THICKNESS, tamping)
