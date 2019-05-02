from cesar import *
from Exercice1 import *
import math as m
fr =[9.42,1.02,2.64,3.39,15.87,0.95,1.04,0.77,8.41,0.89,0.00,5.34,3.24,7.15,5.14,2.86,1.06,6.46,7.90,7.26,6.24,2.15,0.00,0.30,0.24,0.32]

def frequence(texte):
    L = [0]*26
    for c in texte:
        L[ordre(c)] += 1
    return [x*100/len(texte) for x in L]

def distance(texte):
    fc = frequence(texte)
    d = []
    
    for i in range(26):
        u = 0
        for j in range(26):
            u += m.fabs(fr[j] - fc[(j + i)%26])
        d.append(u)
    return d

def minimum_distance(texte):
    di = distance(texte)
    for i in range(26):
        if di[i] == min(di):
            return i