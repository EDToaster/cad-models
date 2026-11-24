# /// script
# requires-python = ">=3.11"
# dependencies = ["manifold3d==3.5.5", "trimesh==5.2.2", "numpy>=2,<3"]
# ///
"""Normalize STL seams without filling holes, then check the file a slicer will read."""

from pathlib import Path
import sys

import manifold3d as m3d
import numpy as np
import trimesh


def normalize(raw_path: Path, output: Path):
    raw = trimesh.load_mesh(raw_path, process=False)
    # Binary STL repeats vertices for every triangle. Sew coincident vertices,
    # allowing only sub-micron discrepancies, without remeshing the surface.
    mesh = m3d.Mesh(raw.vertices.astype("float32"), raw.faces.astype("uint32"), tolerance=0.0001)
    mesh.merge()
    solid = m3d.Manifold(mesh)
    if solid.status() != m3d.Error.NoError or len(solid.decompose()) != 1:
        raise ValueError(f"Expected one closed manifold, got {solid.status()}")
    clean = solid.to_mesh()
    trimesh.Trimesh(clean.vert_properties[:, :3], clean.tri_verts, process=False).export(output)

    result = trimesh.load_mesh(output)
    if not result.is_volume or not np.isclose(result.bounds[0, 2], 0, atol=0.001):
        raise ValueError("STL is not a closed, consistently oriented volume at Z=0")
    if not (np.allclose(result.bounds, raw.bounds, rtol=0, atol=0.001)
            and np.isclose(result.volume, raw.volume, rtol=1e-5)):
        raise ValueError("STL normalization changed model bounds or volume")
    print(f"STL verified: one manifold part, {len(result.faces):,} triangles, "
          f"bounds {result.extents.round(3)} mm")


if __name__ == "__main__":
    normalize(Path(sys.argv[1]), Path(sys.argv[2]))
