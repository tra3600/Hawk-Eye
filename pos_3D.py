import numpy as np

def transform_local_to_global(coord, T1, Rx1, Ry1):
    # Appliquer les rotations et la translation aux coordonnées locales
    r_matrix = np.dot(Ry1, Rx1)
    coord_global = np.dot(r_matrix, coord) + T1
    return coord_global

def traj3D(coord_loc, T1, Rx1, Ry1):
    coord_glo = []
    for coord in coord_loc:
        coord = np.array(coord).reshape(3, 1)  # Convertir en vecteur colonne
        coord_global = transform_local_to_global(coord, T1, Rx1, Ry1)
        coord_glo.append(coord_global.flatten().tolist())
    return coord_glo

# Exemple d'utilisation:
# coord_loc = [[x10, y10, z10], [x11, y11, z11], ..., [x1N, y1N, z1N]]
# T1 = np.array([Tx, Ty, Tz])
# Rx1 = np.array([[...], [...], [...]])  # Matrice de rotation autour de l'axe x
# Ry1 = np.array([[...], [...], [...]])  # Matrice de rotation autour de l'axe y

# coord_glo = traj3D(coord_loc, T1, Rx1, Ry1)
# print(coord_glo)