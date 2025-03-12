def filtre(image, seuil):
    n, m = len(image), len(image[0])
    filtered_image = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if image[i][j] >= seuil:
                filtered_image[i][j] = 1
            else:
                filtered_image[i][j] = 0
    return filtered_image