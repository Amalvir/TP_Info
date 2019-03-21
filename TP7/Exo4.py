from Exo2 import moyenne
import numpy as np
## 2.
def moyenne_eleve(ligne):
    splitee = ligne.split(',')
    L = [float(s) for s in splitee[2:]]
    car = splitee[0] + ' : ' +  str(moyenne(L))
    return car