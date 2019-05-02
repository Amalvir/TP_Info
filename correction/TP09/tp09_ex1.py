fichier = open("donnees.csv","r")

lesT = []
lesA = []
lesW = []
for ligne in fichier:
    L = ligne.split(";")
    lesT.append(L[0])
    lesA.append(L[1])
    lesW.append(L[2])
    
fichier.close()
    
lesT = [float(t)*10**(-3) for t in lesT[1:]]    
lesA = [float(a) for a in lesA[1:]]    
lesW = [float(w) for w in lesW[1:]]

lesA2 = [lesA[0]]
for i in range(1, len(lesA)):
    lesA2.append(lesA2[i-1]+lesW[i-1]*(lesT[i]-lesT[i-1]))

lesA3 = [lesA[0]]
for i in range(1, len(lesA)):
    lesA3.append(lesA3[i-1]+lesW[i]*(lesT[i]-lesT[i-1]))

lesA4 = [lesA[0]]
for i in range(1, len(lesA)):
    lesA4.append(lesA4[i-1]+(lesW[i-1]+lesW[i])/2*(lesT[i]-lesT[i-1]))

import matplotlib.pyplot as plt
ecart2 = [lesA2[i] - lesA[i] for i in range(len(lesA2))]
ecart3 = [lesA3[i] - lesA[i] for i in range(len(lesA3))]
ecart4 = [lesA4[i] - lesA[i] for i in range(len(lesA4))]
plt.plot(lesT, ecart2, label="Rectangles à gauche")
plt.plot(lesT, ecart3, label="Rectangles à droite")
plt.plot(lesT, ecart4, label="Trapèzes")
plt.legend(loc="best")
plt.show()