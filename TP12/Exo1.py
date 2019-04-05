## Partie A
A = [[1, -2, 4, 5], [0, -1, -3, 8]]

print("Indice de", A[0][0],":", "A[0][0]")
print("Indice de", A[0][1],":", "A[0][1]")
print("Indice de", A[1][3],":", "A[1][3]", )

A[1][2] = 42
print("\nOn a remplacé -3 par 42 :", A)

a = A[1][0]   #a est le coeff 0 de la matrice A

## Partie B
#On constate que l'instruction m[1][1] = 2 change toutes les lignes de la matrice
#C'est parce qu'on change la valeur de la liste L.

def init_matrice(n, p):
    #Le init donné marche pas, y'a un 0 en trop
    """Crée une matrice nulle n*p"""
    return [[0]*p for i in range(n)]

# Problème résolu.

def matrice_somme(n,p):
    m = init_matrice(n, p)
    for i in range(1, n+1):
        for j in range(1, p+1):
            m[i-1][j-1] = j + i
    return m

## Partie C
# A*B : Produit scalaire
# A.dot(B) : Produite vectoriel