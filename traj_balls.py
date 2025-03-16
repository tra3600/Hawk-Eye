def traj_balle(seq_balle, vit_init):
    """
    Calcule la trajectoire des balles bonnes en fonction de la séquence de balles et de la vitesse initiale.

    Args:
    seq_balle (list of list of int): Séquence des balles détectées
    vit_init (list of int): Vitesse initiale [vx, vy]

    Returns:
    list of int: Liste des coordonnées des balles bonnes [x0, y0, x1, y1, ..., xi, yi]
    """
    trajectoire = [seq_balle[0]]
    dep_i = vit_init

    for i in range(1, len(seq_balle)):
        xi_1, yi_1 = trajectoire[-1]
        dx, dy = dep_i
        xc = xi_1 + dx
        yc = yi_1 + dy
        Lx = max(2 * abs(dx) + 1, 3)
        Ly = max(2 * abs(dy) + 1, 3)

        balle_detectee = cherche_balle(xc, yc, Lx, Ly, seq_balle[i])
        if balle_detectee == [None, None]:
            dep_i = [2 * dx, 2 * dy]
        else:
            trajectoire.append(balle_detectee)
            dep_i = deplacement([xi_1, yi_1], balle_detectee)
    
    return trajectoire

# Exemple d'utilisation
seq_balle = [[0, 0], [1, 1, 2, 2], [2, 2, 3, 3]]
vit_init = [1, 1]
trajectoire = traj_balle(seq_balle, vit_init)
print(trajectoire)  # Output: [[0, 0], [1, 1], [2, 2]]