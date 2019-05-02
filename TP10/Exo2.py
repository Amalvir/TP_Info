from Exo1 import Euler
import matplotlib.pyplot as plt
import scipy.integrate as int

# Constante
G = 9.8
m = 110
C = 1.5
S = 0.4
p0 = 1.2
h = 0.01

def dv(t,v):
    return -G + 1/(2*m)*p0*S*C*v**2


def main():
    X, Y = Euler(dv, 0, 40, 0, h)
    plt.subplot(221)
    plt.plot(X, Y, label="Vitesse")
    plt.legend()
    z = 0
    les_z = []
    for v in Y:
        z += v*h
        les_z.append(z)
    plt.subplot(222)
    plt.plot(X, les_z, label="Altitude")
    plt.legend()
    plt.subplot(223)
    plt.plot(les_z, Y, label = "phase")
    plt.legend()
    plt.show()

main()