import matplotlib.pyplot as plt
import numpy as np
import math as m

# x=np.linspace (-5,5,100)
# plt.plot(x,np.sin(x),marker='o', linestyle='--',label="Sinus")
# plt.plot(x,np.cos(x), marker='v', label='Cosinus')
# plt.title("Fonctions trigonométriques")
# plt.axis([-5,5,-1,1])
# plt.legend()
# plt.show()

def transitoire(A):
    x=np.linspace(0,10,100)
    plt.plot(x,A*(1-np.exp(-(x/2))))
    plt.plot(x,A*x/2)
    plt.plot(x,A*x/x)
    plt.show()

def somme(f1):
    f2=100*f1
    t=np.linspace(0,10,1000)
    plt.plot(t,np.cos(2*m.pi*f1*t)+np.cos(2*m.pi*f2*t))
    plt.show()

def battement(f1,f2):
    x=np.linspace(0,10,1000)
    y1=np.sin(2*m.pi*f1*x)
    y2=np.sin(2*m.pi*f2*x)
    plt.plot(x,y1 + y2)
    plt.show()

def fourrier(f):
    for i in range(i)
    
    