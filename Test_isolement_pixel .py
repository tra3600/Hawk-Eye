if image[p][c] == 1:
    nb_pixel = -1
    for k in [p-1, p, p+1]:
        for j in [c-1, c, c+1]:
            nb_pixel += image[k][j]
    if nb_pixel == 0:
        image[p][c] = 0