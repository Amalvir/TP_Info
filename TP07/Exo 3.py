from Exo2 import *
# Executer le fichier avec ctrl+maj+E
## 2.
def mesures():
    L = []
    fichier = open("tensions.txt", 'r')
    for ligne in fichier:
        L.append(float(fichier.readline()))
    fichier.close()
    return L

## 3.
def frequenceU():
    L = mesures()
    plt.hist(L, 50)
    plt.title("Un bel histogramme bien titré")
    plt.show()

## 4.
def distribution(N):
    L = mesures()
    Lmoy = moyenne_par_paquet(L, N)
    plt.hist(Lmoy, 50)
    plt.show()