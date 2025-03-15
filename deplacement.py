def deplacement(pos1, pos2):
    """
    Calcule le vecteur déplacement entre deux positions.

    Args:
    pos1 (list of int): Position initiale [x1, y1]
    pos2 (list of int): Position finale [x2, y2]

    Returns:
    list of int: Vecteur déplacement [dx, dy]
    """
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    return [dx, dy]

# Exemple d'utilisation
pos1 = [3, 4]
pos2 = [7, 9]
dep = deplacement(pos1, pos2)
print(dep)  # Output: [4, 5]

dx, dy = abs(dep[0]), abs(dep[1])
Lx = max(2 * dx + 1, 3)
Ly = max(2 * dy + 1, 3)