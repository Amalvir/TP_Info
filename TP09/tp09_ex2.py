Um = 6
U0 = 4
f = 50
T=1/f

import numpy as np
lesT = np.linspace(-2*T,2*T, 180)
lesU = Um*np.cos(2*np.pi*f*lesT)+U0

import matplotlib.pyplot as plt
plt.plot(lesT, lesU)
plt.xlabel("Temps")
plt.ylabel("Tension")
plt.show()

def U(t):
    return U0+Um*np.cos(2*np.pi*f*t)
    
from scipy.integrate import quad

L = quad(U, 0, T)
print(1/T*L[0])