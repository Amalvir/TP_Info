## Question 1
liste1 = [[0]*9]*9
liste1[0][0] = 1
# Les 9 lignes sont en fait une seule liste...

liste2 = [[0 for i in range(9)] for j in range(9)]
liste2[0][0] = 1 

# Il faut utiliser la deuxième instruction.

## Question 2
grille1 = [
[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]

def affiche_grille(grille):
    for i in range(9):
        for j in range(9):
            if grille[i][j] != 0:
                print(grille[i][j],end="")
            else:
                print(" ",end="")
            if j == 2 or j == 5:
                print("|", end="")
        print("")
        if i == 2 or i == 5:
            print("-----------")

## Question 3

def num_carre(i,j):
    return 3*(i//3)+j//3
    
def num_carre(i, j):
    if i < 3:
        if j < 3:
            return 0
        elif j <6:
            return 1
        else:
            return 2
    elif i < 6:
        if j < 3:
            return 3
        elif j <6:
            return 4
        else:
            return 5
    else:
        if j < 3:
            return 6
        elif j <6:
            return 7
        else:
            return 8
            
## Question 4

def case_carre(n, k):
    return (3*(n//3) + k//3, 3*(n%3)+ (k%3))
    
def case_carre(n, k):
    #Coordonnées de la première case:
    if n == 0:
        (i0, j0) = (0,0)
    elif n == 1:
        (i0, j0) = (0,3)
    elif n == 2:
        (i0, j0) = (0,6)
    elif n == 3:
        (i0, j0) = (3,0)
    elif n == 4:
        (i0, j0) = (3,3)
    elif n == 5:
        (i0, j0) = (3,6)
    elif n == 6:
        (i0, j0) = (6,0)
    elif n == 7:
        (i0, j0) = (6,3)
    elif n == 8:
        (i0, j0) = (6,6)
    if k < 3:
        return (i0, j0+k)
    elif k < 6:
        return (i0+1, j0+(k-3))
    else:
        return (i0+2, j0+(k-6))

## Question 5
def appartient(x, L):
    for e in L:
        if x == e:
            return True
    return False

def verifier_ligne(grille, i):
    ligne = grille[i]
    for valeur in range(1,10):
        if not appartient(valeur, ligne):
            return False
    return True

def verifier_colonne(grille, j):
    colonne = [grille[i][j] for i in range(9)]
    for valeur in range(1,10):
        if not appartient(valeur, colonne):
            return False
    return True

def valeur_case_carre(grille,n,k):
    (i, j) = case_carre(n, k)
    return grille[i][j]
    
def verifier_carre(grille, n):
    liste_carre = []
    for k in range(9):
        (i,j) = case_carre(n, k)
        liste_carre.append(grille[i][j])
    for valeur in range(1,10):
        if not appartient(valeur, liste_carre):
            return False
    return True

def est_complete(grille):
    for p in range(9):
        if not verifier_ligne(grille, p):
            return False
        if not verifier_colonne(grille, p):
            return False
        if not verifier_carre(grille, p):
            return False
    return True
    
## Question 6

def chiffres_possibles(grille, i, j):
    if grille[i][j] != 0:
        return [grille[i][j]]
    else:
        val_poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # On parcourt la ligne i
        for k in range(9):
            if appartient(grille[i][k], val_poss):
                val_poss.remove(grille[i][k])
        # On parcourt la colonne j
        for k in range(9):
            if appartient(grille[k][j], val_poss):
                val_poss.remove(grille[k][j])
        # On parcourt le carre de la case (i,j)
        n = num_carre(i, j)
        for k in range(9):
            ik, jk = case_carre(n, k)
            if appartient(grille[ik][jk], val_poss):
                val_poss.remove(grille[ik][jk])
        return val_poss

## Question 7

def completer(grille):
    """Renvoie la liste des coordonnées des cases vides pour lesquelles une seule valeur est possible"""
    y_a_du_chgt = True
    while y_a_du_chgt:
        # Avant de recommencer le parcours, rien n'a changé
        y_a_du_chgt = False
        for i in range(9):
            for j in range(9):
                if grille[i][j] == 0:
                    val_poss = chiffres_possibles(grille, i, j)
                    if len(val_poss) == 1:
                        grille[i][j] = val_poss[0]
                        y_a_du_chgt = True
    return grille

## Question 8
def str_to_grille(s):
    grille = [[0 for j in range(9)] for i in range(9)]
    for k in range(len(s)):
        grille[k//9][k%9] = int(s[k])
    return grille
        
    
## Question 10

def resout(nom_fichier):
    total = 0
    resolues = 0
    f = open(nom_fichier,"r")
    for ligne in f:
        total = total + 1
        grille = str_to_grille(ligne.strip())
        completer(grille)
        if est_complete(grille):
            resolues = resolues + 1
    f.close()
    return 100*resolues/total