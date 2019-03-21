import math as ma
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constante
p0 = 1.2
H = 7.7e3
g = 9.8
S = .4
Cx = 1.5
m = 110

z0 = 39068
v0 = 0

#Q1
def rho_alt(z):
    """Retorune la masse volumique de l'air à l'altitude z"""
    return p0*np.exp(-z/H)


#Q2
def F(u,t):
    """De u=[z(t), v(t)] renvoie u'"""
    z = u[0]
    v = u[1]
    zprime = v
    vprime = -g + (rho_alt(z)*S*Cx*v**2)/(2*m)
    return [zprime, vprime]

u0 = [z0, v0]
les_t = np.linspace(0, 300, 1000)
les_u = odeint(F, u0, les_t)

les_z = [u[0] for u in les_u]
les_v = [u[1] for u in les_u]

#Q3
def trace(X, Y, X_exp, Y_exp, titre):
    plt.plot(X, Y)
    plt.plot(X_exp, Y_exp, )
    plt.title(str(titre))
    plt.show()
    return none

#trace(les_t, les_z, "Altitude")
#trace(les_t, les_v, "Vitesse")
#trace(les_z, les_v, "Altitude Vitesse")

#Q4
def son(les_v):
    c = -((5/3*8.314*263)/29e-3)**0.5
    for i in les_v:
        if i<=c:
            return True
    return False

#False

 