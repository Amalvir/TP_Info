# -*- coding: utf-8 -*-
from __future__ import division # si Python 2

# Fichier initial pour le TP 17 : Pivot de Gauss

def transvection(A,j,i,mu):
    """ transforme sur place la matrice A avec Lj <- Lj + mu Li
        Les indices commencent à zéro """
    n=len(A[0]) # le nombre de colonne qui seront parcourues avec l'indice k
    for k in range(n):
        A[j][k] += mu * A[i][k]
    return(None)


def permutation(A,i,j):
    """ transforme sur place la matrice A avec Li <-> Lj
        Les indices commencent à zéro """
    A[i] , A[j] = A[j] , A[i]
    return(None)


A0=[ [2,2,-3] , [-2,-1,-3] , [6,4,4] ] 
print('A0 = ', A0)
print('\nTransvection...')
transvection(A0,0,1,4) 

print('A0 = ', A0) # A0 est modifiée sur place
print('\n... puis permutation')
permutation(A0,1,2) 
print('A0 = ', A0) # A0 est modifiée sur place successivement

# Ceci ne donnera "rien"
B=permutation(A0,1,2)
print('B = ', B)



def copie_matrice(A):
    """ renvoie une copie de la matrice A """
    return( [ A[i][:] for i in range(len(A)) ] )

#On reprend la matrice A0 initiale. 

A0=[ [2,2,-3] , [-2,-1,-3] , [6,4,4] ] 
print('\nRetour à la matrice initiale')
print('A0 = ', A0)

print('\nUne copie : ')
B=copie_matrice(A0) 
print('B = ', B)

print('\nModification du premier coefficient ')
B[0][0]=19
print('A0 = ', A0) 
print('B = ', B)
# Seule B est modifiée, A0 est conservée.


#Pour le pivot de Gauss en général

def recherche_pivot(A,i):
    """ retourne le plus grand pivot en valeur absolue
        sous A[i][i]"""
    n=len(A)
    indice_piv=i # la ligne du maximum provisoire
    for k in range(i+1,n):
        if abs(A[k][i])>abs(A[indice_piv][i]):
            indice_piv=k #un nouveau maximum provisoire
    return(indice_piv)


########################################################
#A vous de travailler maintenant !
########################################################



    
    


