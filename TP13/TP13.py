liste1 = [[0]*9]*9  # 9 fois la meme liste
# print(liste1)
liste2 = [[1 for i in range(9)] for j in range(9)]  # Utiliser elle
# print(liste2)


def affiche_grille(grille):
    ligne = ""
    count1 = 0
    count2 = 0
    for i in grille:
        for j in i:
            count1 += 1
            if j == 0:
                ligne += " "
            else:
                ligne += str(j)
            if count1 == 3:
                ligne += "|"
                count1 = 0
        count2 += 1
        print(ligne)
        ligne = ""
        if count2 == 3:
            print("-"*12)
            count2 = 0


def num_carre(i, j):
    a = i // 3
    b = j // 3
    t = 3*a + b
    return t


def case_carre(n, k):
    return 3*n//3 + k//3, 3*(n % 3) + k % 3


def est_complete(grille):
    # Correction d'Izi incomplète :
    n = len(grille)
    lcl = [[0]*9 for i in range(9)]     # Liste 9 entiers compteur ligne i
    lcc = [[0]*9 for i in range(9)]     # Liste 9 entiers compteur colonne j
    lcpc = [[0]*9 for i in range(9)]    # Liste 9 entiers compteur petit carré

    for i in range(n):
        for j in range(n):
            x = grille[i][j] - 1
            if x == -1:
                return False
            lcl[i][x] += 1
            lcc[j][x] += 1
            k = num_carre(i, j)
            lcpc[k][x] += 1
