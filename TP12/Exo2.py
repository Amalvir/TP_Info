## Mouvement d'une particule dans un champ magnetique
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def Euler(F, a, b, y0, h):
    """Valeur approché de la solution de y' = F(t,y)"""
    t = a
    y = y0
    les_t = [a]
    les_y = [y0]
    while t + h <= b:
        y = y + h*F(t,y)
        t = t + h
        les_t.append(t)
        les_y.append(list(y))
    return les_t, np.array(les_y)

def F(t, y):
    A = np.array([[0, B[2], -B[1]], [-B[2], 0, B[0]], [B[1], -B[0], 0]])
    return A.dot(y)+np.array([V0, 0, 0])
    

def trajectoire(B, V0, pas, n, qm = 1):
    les_X = np.empty((n+1)) #n+1 elements
    les_Y = np.empty((n+1))
    les_Z = np.empty((n+1))
    les_t, les_y = Euler(F, 0, n*pas, y0, pas)
    les_X = les_y[:,0]
    les_Y = les_y[:,1]
    les_Z = les_y[:,2]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(les_X, les_Y, les_Z)
    ax.legend()
    plt.show()
    return les_X, les_Y, les_Z

B = np.array([0, 0, 1])
y0 = np.array([0, 0, 0])
V0 = 1
pas = 0,1
n = 1000
trajectoire(B, V0, pas, n, qm = 1)