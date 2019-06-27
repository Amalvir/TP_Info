# -*- coding: utf-8 -*-
from __future__ import division # si Python 2

# Fichier initial pour le TP 14 : Pivot de Gauss

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


def triangu2(A, B):
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            mu = A[j][i]/A[i][i]
            transvection(A, j, i, -mu)
            transvection(B, j, i, -mu)
            

def Gauss_etoile(A0, B0):
    A, B = copie_matrice(A0), copie_matrice(B0)
    triangu2(A, B)
    n = len(A)
    X= [0]*n
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s = s + A[i][j]*X[j]
        X[i] = (B[i][0] - s)/A[i][i]
    return X

def Gauss(A0, B0):
    A, B = copie_matrice(A0), copie_matrice(B0)
    n = len(A)
    for i in range(n-1):
        k = recherche_pivot(A, i)
        if k > i:
            permutation(A, i, k) 
            permutation(B, i, k) 
        for j in range(i+1, n):
            mu = A[j][i]/A[i][i]
            transvection(A, j, i, -mu)
            transvection(B, j, i, -mu)
    X= [0]*n
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s = s + A[i][j]*X[j]
        X[i] = (B[i][0] - s)/A[i][i]
    return X

def matrice_A(n):
    A = [[0 for j in range(n)] for i in range(n)]
    # Surtout pas A = [[0]*n]*n
    for i in range(n):
        A[i][i] = -2
    for i in range(n-1):
        A[i][i+1] = 1
        A[i+1][i] = 1
    return A
    
T_ext = 300
L = 1
alpha = 40
n = 10

def matrice_B(n):
    h = L/(n+1)
    B = [[-h**2 * alpha] for i in range(n)]
    B[0][0] = B[0][0] - T_ext
    B[n-1][0] = B[n-1][0] - T_ext
    return B
    
les_T = Gauss(matrice_A(n), matrice_B(n))
les_T = [T_ext] + les_T
les_T.append(300)

import numpy as np

les_X = np.linspace(0, L, n+2)

import matplotlib.pyplot as plt
plt.plot(les_X, les_T)
plt.show()
        
        
        
        
    