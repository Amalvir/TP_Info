##Exercice 1
# def recherche(x, L):
#     """Retourne l'indice de x si x est dans L. False sinon."""
#     for i in range(len(L)) :
#         if x == L[i]:
#             return i
#     return False

##Exercice 2
import math as m
def recherche(x, L):
    """Retourne l'indice de x si x est dans L. False sinon."""
    i = 0
    while x >= L[i]:
        if x == L[i]:
            return i
        i = i + 1
    return False

def dicho(x, L):
    g = 0
    d = len(L) - 1
    m = 0
    acces = 1 
    while d-  g >= 0:
        m = (g + d)//2
        if L[m] == x:
            acces += 1
            return True
        elif x < L[m]:
            acces += 1
            d = m - 1
        else:
            acces += 1
            g = m + 1
    return False

def chrono_recherche():
    from time import clock
    L = [2*k for k in range(10**7)]
    x = 10**7
    t0 = clock()
    reponse = recherche(x, L)
    t1 = clock()
    return reponse, t1 - t0

def chrono_dicho():
    from time import clock
    L = [2*k for k in range(10**7)]
    x = 10**7
    t0 = clock()
    reponse = dicho(x, L)
    t1 = clock()
    return reponse, t1 - t0

##Exercice 3
def interpolation(x, L, e = 450):
    i = m.floor((e-L[0])*(len(L)-1)/(L[len(L)-1]-L[0]))
    return i