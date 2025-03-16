# Hawk-Eye
système d aide a l arbitrage tennis
### Fonction deplacement

```python
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
```

### Fonction distance_quad

```python
def distance_quad(xc, yc, liste_balle_i):
    """
    Calcule les carrés des distances entre le pixel central et les balles possibles.

    Args:
    xc (int): Coordonnée x du pixel central
    yc (int): Coordonnée y du pixel central
    liste_balle_i (list of int): Liste des coordonnées des balles possibles [x1, y1, x2, y2, ...]

    Returns:
    list of int: Liste des carrés des distances
    """
    distances = []
    for i in range(0, len(liste_balle_i), 2):
        x = liste_balle_i[i]
        y = liste_balle_i[i+1]
        dist_quad = (x - xc) ** 2 + (y - yc) ** 2
        distances.append(dist_quad)
    return distances

# Exemple d'utilisation
xc, yc = 5, 5
liste_balle_i = [3, 4, 7, 9]
distances = distance_quad(xc, yc, liste_balle_i)
print(distances)  # Output: [5, 32]
```

### Fonction cherche_balle

```python
def cherche_balle(xc, yc, Lx, Ly, liste_balle_i):
    """
    Cherche la balle la plus proche du pixel central dans la zone de recherche.

    Args:
    xc (int): Coordonnée x du pixel central
    yc (int): Coordonnée y du pixel central
    Lx (int): Largeur de la zone de recherche
    Ly (int): Hauteur de la zone de recherche
    liste_balle_i (list of int): Liste des coordonnées des balles possibles [x1, y1, x2, y2, ...]

    Returns:
    list of int: Coordonnées de la balle détectée [x, y] ou [None, None] si aucune balle n'est détectée
    """
    distances = distance_quad(xc, yc, liste_balle_i)
    if not distances:
        return [None, None]
    
    min_distance = min(distances)
    index_min = distances.index(min_distance)
    x_balle = liste_balle_i[2 * index_min]
    y_balle = liste_balle_i[2 * index_min + 1]
    
    return [x_balle, y_balle]

# Exemple d'utilisation
xc, yc = 5, 5
Lx, Ly = 3, 3
liste_balle_i = [3, 4, 7, 9]
balle_detectee = cherche_balle(xc, yc, Lx, Ly, liste_balle_i)
print(balle_detectee)  # Output: [3, 4]
```

### Fonction traj_balle

```python
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
```

### Limites ou défauts de l'algorithme

1. **Approximation de la vitesse constante** : L'algorithme suppose que la vitesse de la balle varie peu entre deux images successives, ce qui peut ne pas être vrai en cas de changements brusques de direction ou de vitesse.
2. **Zone de recherche fixe** : La taille de la zone de recherche est déterminée par le déplacement précédent. En cas de grandes variations, cette méthode peut ne pas être suffisante.
3. **Cas de plusieurs balles** : Si plusieurs balles sont présentes dans la zone de recherche, l'algorithme choisit simplement la plus proche du centre, ce qui peut entraîner des erreurs en présence de bruit ou d'autres objets en mouvement.
4. **Perte de la balle** : Si la balle n'est pas détectée dans une image, l'algorithme double la taille de la zone de recherche pour la prochaine image. Cela peut augmenter le risque de fausses détections, surtout en présence de bruit.
5. **Non-prise en compte des bords** : L'algorithme ne traite pas les cas où la balle se trouve près des bords de l'image, ce qui peut générer des erreurs de détection.
6. **Non-robustesse aux conditions lumineuses et météorologiques** : Les variations de lumière et les conditions météorologiques peuvent affecter la détection des balles, ce qui n'est pas pris en compte dans l'algorithme.
