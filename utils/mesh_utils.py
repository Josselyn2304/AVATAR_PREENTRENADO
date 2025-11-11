import numpy as np

def save_obj(filename, vertices, faces):
    """Saves a 3D mesh in the OBJ file format."""
    with open(filename, 'w') as file:
        for vertex in vertices:
            file.write(f"v {' '.join(map(str, vertex))}\n")
        for face in faces:
            file.write(f"f {' '.join(map(str, [v + 1 for v in face]))}\n")
            
def save_ply(filename, vertices, faces):
    """Saves a 3D mesh in the PLY file format."""
    with open(filename, 'w') as file:
        file.write("ply\n")
        file.write("format ascii 1.0\n")
        file.write(f"element vertex {len(vertices)}\n")
        file.write("property float x\nproperty float y\nproperty float z\n")
        file.write(f"element face {len(faces)}\n")
        file.write("property list uchar int vertex_index\n")
        file.write("end_header\n")
        for vertex in vertices:
            file.write(f"{' '.join(map(str, vertex))}\n")
        for face in faces:
            file.write(f"{len(face)} {' '.join(map(str, face))}\n")
            
def compute_normals(vertices, faces):
    """Computes normals for the mesh."""
    normals = np.zeros(vertices.shape, dtype=vertices.dtype)
    for face in faces:
        v0, v1, v2 = vertices[face]
        normal = np.cross(v1 - v0, v2 - v0)
        normal /= np.linalg.norm(normal)  # Normalize
        for vertex in face:
            normals[vertex] += normal
    return normals / np.linalg.norm(normals, axis=1)[:, np.newaxis]

def export_avatar(filename, vertices, faces):
    """Exports 3D mesh to both OBJ and PLY formats."""
    save_obj(filename.replace('.ply', '.obj'), vertices, faces)
    save_ply(filename, vertices, faces)