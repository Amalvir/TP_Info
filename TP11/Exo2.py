import numpy as np
from scipy.integrate import odeint

m = 1
l = 1
g = 10
J = 1/3*m*l**2
w0 = ((m*g*l)/2*J)**0.5

u0 = 

def Fpendule(u,t):
    """De u renvoie u'"""
    o = u[0]
    w = u[1]
    
    oprime = w
    wprime = -w0**2*np.sin(0)
    return [oprime, wprime]


les_t = np.linspace(0, 1, 1000)