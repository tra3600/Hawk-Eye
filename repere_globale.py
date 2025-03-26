def det_impact(coord_glo, eps):
    y_ground = 0  # La coordonnée y du sol est 0 (hypothèse du terrain plat)
    impact = None

    for i in range(1, len(coord_glo)):
        x_prev, y_prev, z_prev = coord_glo[i-1]
        x_curr, y_curr, z_curr = coord_glo[i]

        # Vérifier si la balle descendait et maintenant elle remonte
        if y_prev > y_ground >= y_curr:
            # Moyenne des positions x et z lorsque y est proche de y_ground
            x_imp = (x_prev + x_curr) / 2
            z_imp = (z_prev + z_curr) / 2
            impact = [x_imp, z_imp]
            break
        # Si la coordonnée y est très proche de y_ground
        elif y_ground <= y_curr <= y_ground + eps:
            impact = [x_curr, z_curr]
            break

    return impact

def res_final(impact, L, l):
    x_imp, z_imp = impact
    if 0 <= x_imp <= L and 0 <= z_imp <= l:
        return "IN"
    else:
        return "OUT"

# Exemple d'utilisation:
# coord_glo = [[xg0, yg0, zg0], [xg1, yg1, zg1], ..., [xgN, ygN, zgN]]
# eps = 0.1  # Par exemple
# impact = det_impact(coord_glo, eps)
# result = res_final(impact, 24, 11)
# print(impact, result)