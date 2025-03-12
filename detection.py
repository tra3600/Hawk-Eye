def detection(image1, image2):
    n, m = len(image1), len(image1[0])
    image_gray = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            r1, g1, b1 = image1[i][j]
            r2, g2, b2 = image2[i][j]
            delta = (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2
            image_gray[i][j] = min(delta, 255)
    return image_gray

# Instruction pour appliquer la fonction à deux images im1 et im2
image_gray = detection(im1, im2)