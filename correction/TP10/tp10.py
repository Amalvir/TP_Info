#### Exercice 1  ####
## Partie A
C = 220e-9
R = 10e3
r = 50
E = 10

# Q1
tau = (r+R)*C

# Q2
def e(t):
    if t >= 0:
        return E
    else:
        return 0
        
def F(uc, t):
    return (e(t)-uc)/tau
    
def Euler(F, a, b, y0, h):
    t = a
    y = y0
    les_t = [t]
    les_y = [y]
    while t+h <= b:
        y = y + h*F(y, t)
        t = t + h
        les_t.append(t)
        les_y.append(y)
    return les_t, les_y
    
import matplotlib.pyplot as plt
import numpy as np

les_t, les_uc = Euler(F, 0, 5*tau, 0, 0.001)
#plt.plot(les_t, les_uc, label="Euler")

# Q3
les_t2 = np.linspace(0, 5*tau)

def uc(t):
    return E*(1-np.exp(-t/tau))
#plt.plot(les_t2, uc(les_t2), "*-.", label='Solution analytique', markersize = 10)
#plt.legend(loc="best")
#plt.show()

# Q4
for k in [1, 0.1, 0.01, 0.001]:
    les_t, les_uc = Euler(F, 0, 5*tau, 0, k*tau)
    plt.plot(les_t, les_uc, label="Euler pour h ="+str(k)+"tau")
#plt.plot(les_t2, uc(les_t2), "-.", label='Solution analytique')
#plt.legend(loc="best")
#plt.show()

# Q5
from time import process_time

def chrono(h):
    t0 = process_time()
    response = Euler(F, 0, 5*tau, 0, h)
    t1 = process_time()
    return t1-t0

for k in [1, 0.1, 0.01, 0.001]:
    print("Temps d'exécution pour h="+str(k)+"tau :")
    print(chrono(k*tau))
    
## Partie B
# Q1
from scipy.integrate import odeint

# Q2
les_t, les_uc = Euler(F, 0, 5*tau, 0, 0.01*tau)
les_uc2 = odeint(F, 0, les_t)

# plt.plot(les_t, les_uc, label = "Méthode d'Euler")
# plt.plot(les_t, les_uc2, label = "odeint")
# plt.legend(loc="best")
# plt.show()


#### Exercice 2 ####
v0 = 0
z0 = 39068

rho0 = 1.2 #en kg.m^(-1)
S = .4
Cx = 1.5
m = 110 #en kg
g = 9.8

def F_felix(v, t):
    return -g + 1/(2*m)*rho0*S*Cx*v**2

h = 1
les_t, les_v = Euler(F_felix, 0, 40, v0, h)
plt.plot(les_t, les_v)
plt.show()


def altitude(les_t, les_v):
    s = 0
    z = z0
    les_z = [z0]
    for k in range(0, len(les_t)-1):
        z = z + (les_t[k+1]-les_t[k])*(les_v[k]+les_v[k+1])/2
        les_z.append(z)
    return les_z

plt.figure()
les_z = altitude(les_t, les_v)
plt.plot(les_t, les_z)
plt.show()