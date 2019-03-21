import matplotlib.pyplot as plt

def suite_u(n):
    u0 = 2 
    u1 = -4
    u = 0
    for i in range(2, n + 1):
        u = 111 - 1130/u1 + 3000/(u0*u1)  
        u0 = u1
        u1 = u
    return u

def suite_f(n):
    return (4*5**(n + 1) - 3*6**(n + 1))/(4*5**n - 3*6**n)

def trace():
    X = [k for k in range(0, 31)]
    Yf = [suite_f(k) for k in X]
    Yu = [suite_u(k) for k in X]
    plt.plot(X, Yf, label = 'f')
    plt.plot(X, Yu, label = 'u')
    plt.legend()
    plt.show()