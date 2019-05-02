A = [[1, -2, 4, 5], [0, -1, -3, 8]]

# Mathématiquement, 
# 1 est le terme (1,1), 
#-2 le terme (1,2),
# 8 le terme (2,4)

# En Python
# 1 est le terme A[0][0], 
#-2 le terme A[0][1],
# 8 le terme A[1][3]

def init_matrice(n, p):
    return [[0]*p for i in range(n)]
    
def init_matrice(n, p):
    m = [0]*n
    for i in range(n):
        m[i] = [0]*p
    return m
    
def matrice_somme(n, p):
    m = init_matrice(n, p)
    for i in range(1, n+1):
        for j in range(1, p+1):
            m[i-1][j-1] = i+j
    return m
    
def matrice_somme(n, p):
    return [[i+j for j in range(1,p+1)] for i in range(1,n+1)]


## C - Module Numpy
import numpy as np

A = np.zeros((3,4))
A[1,2] = 5

B = np.ones((3,4))
print("A+2B=",A+2*B)

C = np.array([[1, 2, 3], [4, 5, 6]])
print("Taille de C")
print(C.shape)

print("Produit matriciel CA")
print(C.dot(A))

print("Produit coeff par coeff :")
print("matrice des a(i,j)b(i,j)")
print(A*B)

## Mouvement d'une particule
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# B vecteur
# V0 scalaire tq v(0) = V0 e_x
def trajectoire(B, V0, pas, n, qm = 1):
    les_X = np.empty((n+1))
    les_Y = np.empty((n+1))
    les_Z = np.empty((n+1))
    les_X[0] = 0
    les_Y[0] = 0
    les_Z[0] = 0
    Bx, By, Bz = B[0], B[1], B[2]
    MB = np.array(
        [[0, Bz, -By],
        [-Bz, 0, Bx],
        [By, -Bx, 0]])
    for i in range(n):
        VecPos = np.array([les_X[i], les_Y[i], les_Z[i]])
        VecVit = qm*MB.dot(VecPos)+np.array([V0,0,0])
        VecPosNew = VecPos + pas*VecVit
        les_X[i+1] = VecPosNew[0]
        les_Y[i+1] = VecPosNew[1]
        les_Z[i+1] = VecPosNew[2]
    return les_X, les_Y, les_Z

B0 = 1
V0 = 1

B = np.array([0,0,B0])
les_X, les_Y, les_Z  = trajectoire(B, V0, 0.001, 10000)
fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot(les_X, les_Y, les_Z)
ax.legend()
plt.show() 

    
    
    
    
    
    