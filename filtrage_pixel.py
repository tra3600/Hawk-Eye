def filtre_pixel(image):
    n, m = len(image), len(image[0])
    for p in range(1, n-1):
        for c in range(1, m-1):
            if image[p][c] == 1:
                nb_pixel = -1
                for k in [p-1, p, p+1]:
                    for j in [c-1, c, c+1]:
                        nb_pixel += image[k][j]
                if nb_pixel == 0:
                    image[p][c] = 0
    return image