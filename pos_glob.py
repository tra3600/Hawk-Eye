import numpy as np

def pos_glo(pos1i, T1, Rx1, Ry1):
    """
    Calcule les coordonnées de la balle dans le repère global à l'instant i.

    Args:
    pos1i (list of float): Coordonnées de la balle dans le repère local de la caméra 1 [x1i, y1i, z1i]
    T1 (numpy array): Matrice de translation de la caméra 1
    Rx1 (numpy array): Matrice de rotation suivant x de la caméra 1
    Ry1 (numpy array): Matrice de rotation suivant y de la caméra 1

    Returns:
    list of float: Coordonnées [xgi, ygi, zgi] de la balle dans le repère global
    """
    pos1i_vector = np.array(pos1i)
    
    # Appliquer les rotations
    pos_rotated = np.dot(Rx1, pos1i_vector)
    pos_rotated = np.dot(Ry1, pos_rotated)
    
    # Appliquer la translation
    pos_global = pos_rotated + T1
    
    return pos_global.tolist()

# Exemple d'utilisation
pos1i = [100.0, 75.0, 25.0]
T1 = np.array([50.0, 50.0, 50.0])
theta1 = np.radians(30)  # Angle de rotation suivant x
gamma1 = np.radians(45)  # Angle de rotation suivant y

Rx1 = np.array([
    [1, 0, 0],
    [0, np.cos(theta1), -np.sin(theta1)],
    [0, np.sin(theta1), np.cos(theta1)]
])

Ry1 = np.array([
    [np.cos(gamma1), 0, np.sin(gamma1)],
    [0, 1, 0],
    [-np.sin(gamma1), 0, np.cos(gamma1)]
])

posgi ▋