import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco

# 1.

# A l'origine des temps : 0 = Acos(phi)
# D'où phi = pi/2 ou -pi/2
# On choisi -pi/2 pour la suite

# 2.

# 3.

# Constante :
m = 1
k = 1
L = 10
mu = 0.1
c = np.sqrt(k*L/mu)
meff = mu*L/3


def cotan(x):
    return np.cos(x)/np.sin(x)


X = np.linspace(0, 20, 1536)
Y = [(k*L)/(m*c)*1/np.tan(w*L/c) for w in X]
plt.plot(X, Y, label='w avec cotan')
plt.plot(X, X, label='w = w')
plt.legend()
plt.show()

# 4.


def f(w):
    return (k*L)/(m*c)*1/np.tan(w*L/c) - w


for i in range(5):
    print(sco.newton(f, i*np.pi+0.001))

# 5.

print('\n', "Q.5 : ", np.sqrt(k/(m + meff)), sep='')

# On trouve pareil c'est bon.
