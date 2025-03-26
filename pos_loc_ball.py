def pos_loc(e, f, x1, x2, y1, y2):
    """
    Calcule les coordonnées de la balle dans le repère local de la caméra 1 à un instant i.

    Args:
    e (float): Longueur de la ligne de base stéréo des caméras
    f (float): Distance focale des caméras
    x1 (float): Coordonnée x de la balle dans l'image de la caméra 1
    x2 (float): Coordonnée x de la balle dans l'image de la caméra 2
    y1 (float): Coordonnée y de la balle dans l'image de la caméra 1
    y2 (float): Coordonnée y de la balle dans l'image de la caméra 2

    Returns:
    list of float: Coordonnées [x1i, y1i, z1i] de la balle dans le repère local de la caméra 1
    """
    d = x1 - x2
    if d == 0:
        raise ValueError("Les coordonnées x1 et x2 ne doivent pas être égales pour éviter une division par zéro.")
    
    x1i = (e / d) * x1
    y1i = (e / d) * y1
    z1i = (e / d) * f
    
    return [x1i, y1i, z1i]

# Exemple d'utilisation
e = 10.0  # Longueur de la ligne de base stéréo des caméras (en unités quelconques)
f = 50.0  # Distance focale des caméras (en unités quelconques)
x1 = 200.0
x2 = 180.0
y1 = 150.0
y2 = 140.0

pos1i = pos_loc(e, f, x1, x2, y1, y2)
print(pos1i)  # Output: [100.0, 75.0, 25.0]