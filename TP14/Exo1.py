# A.1


def newton(f, fprime, u0, eps):
    """Méthode de Newton vu en cours"""
    u = u0  # u = u0
    v = u - f(u)/fprime(u)  # u = u1
    count = 1

    while abs(v - u) > eps:
        u = v
        v = v - f(v)/fprime(v)
        count += 1
    return v


def f(x):
    return x**2 - 2


def fprime(x):
    """Dérivée de f"""
    return 2*x


# 1 test:
print(newton(f, fprime, 2, 0.01), '\n')

# A.2


def g(x):
    return x**3 - x


def gprime(x):
    return 3*x**2 - 1


u0 = 3**-1/3
print(newton(g, gprime, u0, 0.001))

u0 = u0 + 0.001
print(newton(g, gprime, u0, 0.001))

u0 = u0 - 0.002
print(newton(g, gprime, u0, 0.001))

u0 = 3**-1/3 - 0.3
print(newton(g, gprime, u0, 0.001), '\n')
# On est proche du point ou la derivée s'annule donc Newton merde.

# A.3


def newton_compteur(f, fprime, u0, it_max, epsilon):
    """Méthode de Newton vu en cours"""
    u = u0  # u = u0
    v = u - f(u)/fprime(u)  # u = u1
    count = 1

    while abs(v - u) > epsilon and count < it_max:
        u = v
        v = v - f(v)/fprime(v)
        count += 1
    return v, count


def h(x):
    return x/(1 + x**2)


def hprime(x):
    return (1 - x**2)/((1 + x**2)**2)


print("u0 = 0.5 :", newton_compteur(h, hprime, 0.5, 100, 0.01))
print("u0 = 1.5 :", newton_compteur(h, hprime, 1.5, 100, 0.01), '\n')
# On atteint le maximum d'itération

# B.1


def derivee(f, x, h):
    """Retourne une approx de la dérivee"""
    return (f(x) - f(x - h))/h

# B.2


def newton_derivee(f, u0, it_max, epsilon, h):
    """Newton qui calcule la dérivée"""
    u = u0  # u = u0
    v = u - f(u)/derivee(f, u, h)  # u = u1
    count = 1

    while abs(v - u) > epsilon and count < it_max:
        u = v
        v = v - f(v)/derivee(f, v, h)
        count += 1
    return v, count


print(newton_compteur(f, fprime, 2, 10, 0.01), newton_derivee(f, 2, 10, 0.01, 0.01), '\n')

# C.1


import scipy.optimize as sco

# x0 doit être proche du 0 qu'on cherche
# Si fprime pas précisée, méthode des sécantes est utiliser
# maxiter = 50

# C.2


print(sco.newton(f, 2, fprime=fprime, tol=0.001, maxiter=10))

