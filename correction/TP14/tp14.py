## Exercice 1

# Question A1
def newton(f, fprime, u0, eps):
    u = u0 #u_n
    v = u - f(u)/fprime(u) #u_{n+1}
    while abs(v-u)>eps:
        u = v
        v = v - f(v)/fprime(v)
    return v
    
    
def f(x):
    return x**2 - 2
    
def fprime(x):
    return 2*x # Expression de la dérivée de f

print(newton(f, fprime, 2, 0.01))
    
# Question A2

def g(x):
    return x**3-x

def gprime(x):
    return 3*x**2 - 1

#u0 = 3**(1/2)/3
#print(newton(g, gprime, u0, 0.001))
# gprime(u0) = 0 donc erreur


u0 = 3**(1/2)/3 + 0.001
print(newton(g, gprime, u0, 0.001))

u0 = 3**(1/2)/3 - 0.001
print(newton(g, gprime, u0, 0.001))

u0 = 3**(1/2)/3 - 0.3
print(newton(g, gprime, u0, 0.001))


# Question A1
def newton_compteur(f, fprime, u0, it_max, eps):
    u = u0 #u_n
    v = u - f(u)/fprime(u) #u_{n+1}
    it = 1
    while abs(v-u)>eps and it < it_max:
        u = v
        v = v - f(v)/fprime(v)
        it = it + 1
    return v, it
    
def h(x):
    return x/(1+x**2)
    
def hprime(x):
    return (1-x**2)/(1+x**2)**2

print(newton_compteur(h, hprime, 1.5, 100, 0.01))
# On atteint le nombre total d'itérations :
# cela sent mauvais...

# Question B1
def derivee(f, x, h):
    return (f(x)-f(x-h))/h

# Question B2
def newton_derivee(f, u0, it_max, eps, h):
    u = u0 #u_n
    v = u - f(u)/derivee(f, u, h) #u_{n+1}
    it = 1
    while abs(v-u)>eps and it < it_max:
        u = v
        v = v - f(v)/derivee(f, u, h)
        it = it + 1
    return v, it
    
print(newton_compteur(f, fprime, 2, 10, 0.01), newton_derivee(f, 2, 10, 0.01, 0.01))

# Question C1
import scipy.optimize as sco

print(sco.newton(f, 2, fprime=fprime, tol=0.001, maxiter=10))

## Exercice 2
import numpy as np

def cotan(x):
    return np.cos(x)/np.sin(x)
    
X = np.linspace(np.pi/2, 50*np.pi, 1001)
Y = [cotan(x)  for x in X]

import matplotlib.pyplot as plt
plt.plot(X, Y)

plt.show()

