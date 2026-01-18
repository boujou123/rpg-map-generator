import random

largeur = int(input("Entrez la largeur de la carte : "))
hauteur = int(input("Entrez la hauteur de la carte : "))


def creer_map(largeur, hauteur):
    l_map = [['.'] * largeur for i in range(hauteur)]
    pourcentage_cailloux = round(0.15 * ((largeur-2) * (hauteur-2)))

    for h in range(hauteur):
        for l in range(largeur):
            if h == 0 or h == hauteur - 1:
                l_map[h][l] = '#'
            elif l == 0 or l == largeur - 1:
                l_map[h][l] = '#'

    for i in range(pourcentage_cailloux):
        x = random.randint(1, largeur - 2)
        y = random.randint(1, hauteur - 2)
        l_map[y][x] = 'o'

    chemin_centre = largeur // 2
    for h in range(1, hauteur - 1):
        l_map[h][chemin_centre] = '|'

    chemin_hor = random.randint(1, hauteur - 2)
    for l in range(1, largeur - 1):
        l_map[chemin_hor][l] = '-'

    salle_centrale_largeur = 2 *round(0.1 * (largeur - 2) ) + 1
    salle_centrale_hauteur = 2 *round(0.1 * (hauteur - 2) ) + 1
    debut_x = (largeur - salle_centrale_largeur) // 2
    debut_y = (hauteur - salle_centrale_hauteur) // 2
    for h in range(debut_y, debut_y + salle_centrale_hauteur):
        for l in range(debut_x, debut_x + salle_centrale_largeur):
            l_map[h][l] = 'S'

    return l_map

def afficher_map(l_map):
    for col in l_map:
        for element in col:
            if element == '.':
                element = ' '
            elif element == '#':
                element = '█'
            elif element == 'o':
                element = '●'
            elif element == '|':
                element = '│'
            elif element == '-':
                element = '─'
            print (element, end='')
        print()



l_map = creer_map(largeur, hauteur)

afficher_map(l_map)