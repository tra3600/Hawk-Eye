point = input("Rentrer le numéro du point litigieux à analyser")
dirs = listdir("sequence_" + point)  # Récupère la liste des fichiers dans le dossier correspondant au point litigieux

# Première boucle for : Recherche de l'index maximum des images
for image in dirs:
    index_max = 0
    index = int(image[6:11])  # Extrait l'index de l'image à partir de son nom
    if index >= index_max:
        index_max = index

# Initialisation de la séquence de la balle avec la position initiale
seq_balle = [[x0, y0]]  # [x0, y0] position initiale de la balle donnée par un autre traitement

# Deuxième boucle for : Traitement des images pour détecter la balle
for image in dirs:
    index_init = index_max - 3000  # Détermine l'indice de la première image de la séquence analysée
    if int(image[6:11]) == index_init:
        image2 = imread("sequence_" + point + "/" + image)
    elif int(image[6:11]) > index_init:
        image1 = deepcopy(image2)
        image2 = imread("sequence_" + point + "/" + image)
        liste_balles = traitement(image1, image2)
        seq_balle.append(liste_balles)