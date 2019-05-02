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
    b = j
    return a

for i in range(0, 9):
    print(num_carre(i, 0))