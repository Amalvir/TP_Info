## Exercice 1
v0 = 0
z0 = 39068

rho0 = 1.2 #en kg.m^(-1)
S = .4
Cx = 1.5
m = 110 #en kg
g = 9.8

H = 7.7e3 #en m

#Q1
import numpy as np
def rho_alt(z):
    return rho0*np.exp(-z/H)
    
    
#Q2
from scipy.integrate import odeint

def F(u,t):
    """ Prend en paramètre u = [z(t), v(t)] et t et 
    renvoie la liste u' = [z'(t), v'(t)]"""
    # u est la liste [z(t), v(t)]
    z = u[0]
    v = u[1]
    # On doit renvoyer [z'(t), v'(t)]
    zprime = v
    vprime = -g+1/(2*m)*rho_alt(z)*S*Cx*v**2
    return [zprime, vprime]

u0 = [z0, v0]
les_t = np.linspace(0, 300, 1000)
les_u = odeint(F, u0, les_t)

les_z = [u[0] for u in les_u]
les_v = [u[1] for u in les_u]

# Q3
import matplotlib.pyplot as plt
def trace(X, Y, titre):
    plt.plot(X, Y)
    plt.title(titre)
    plt.show()
#     
# trace(les_t, les_v, "Vitesse en fonction du temps")
# trace(les_t, les_z, "Altitude en fonction du temps") 
# trace(les_z, les_v, "Vitesse en fonction de l'altitude")


# Q4
gamma = 5/3
R = 8.314
M=29e-3
T0 = 263

c = np.sqrt(gamma*R*T0/M)
plt.plot([0, 300], [-c, -c])
trace(les_t, les_v, "Vitesse en fonction du temps")

# Q5
les_t_exp = [0, 34, 50, 64, 180, 260]
les_z_exp = [38969, 33446, 27833, 22961, 7619, 2567]
# Vitesses à convertir !!
les_v_exp = [ -v/3.6 for v in [0, 1115, 1358, 1043, 285, 192] ]

def trace(X, Y, X_exp, Y_exp, titre):
    plt.plot(X, Y, label="Par résolution")
    plt.plot(X_exp, Y_exp, label="Données expérimentales")
    plt.title(titre)
    plt.legend(loc="best")
    plt.show()

# trace(les_t, les_v, les_t_exp, les_v_exp, "Vitesse en fonction du temps")
# plt.figure()
# trace(les_t, les_z, les_t_exp, les_z_exp, "Altitude en fonction du temps") 
# plt.figure()
# trace(les_z, les_v, les_z_exp, les_v_exp, "Vitesse en fonction de l'altitude")

plt.close()
## Exercice 2
m = 1 
l = 1
g = 10
J = 1/3*m*l**2
omega0 = np.sqrt(m*g*l/(2*J))

# Q1
def Fpendule1(u, t):
    theta = u[0]
    theta_point = u[1]
    #On doit renvoyer theta_point et theta_point_point
    theta_point_point = -omega0**2 * np.sin(theta)
    return [theta_point, theta_point_point]

# Q2
def trace(les_theta_0):
    les_t = np.linspace(0, 1, 100)
    for theta_0 in les_theta_0:
        u0 = [theta_0, 0]
        les_u = odeint(Fpendule1, u0, les_t)
        les_theta = [u[0] for u in les_u]
        plt.plot(les_t, les_theta, label="theta(0)="+str(theta_0))
    plt.legend(loc="best")
    plt.show()
    
trace([0.1, 0.5, 2, 3.1, 3.14159])
        
    