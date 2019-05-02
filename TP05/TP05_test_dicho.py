    def dichotomie(x, L):
    '''Recherche par dichotomie de x dans la liste L triée par ordre croissant'''
    n = len(L)
    g = 0 # indice de début de recherche
    d = n-1 # indice de fin de recherche
    # Tant qu'il y a des éléments dans la 
    # portion de liste considérée
    while d >= g:
        m = (g+d)//2
        Lm = L[m]
        if x == Lm:
            return True
        elif x < Lm:
            d = m-1
        else:
            g = m+1
    # Si on sort de la boucle while,
    # on n'a pas trouvé
    return False
           
L1 = [2, 4, 6, 8]
L2 = [2, 4, 6]

print(dichotomie(0, L1))
print(dichotomie(0, L2))

print(dichotomie(2, L1))
print(dichotomie(2, L2))

print(dichotomie(4, L1))
print(dichotomie(4, L2))

print(dichotomie(5, L1))
print(dichotomie(5, L2))
    
L3 = [1]

print(dichotomie(1, L3))
print(dichotomie(0, L3))
print(dichotomie(2, L3))



