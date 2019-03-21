import matplotlib.pyplot as plt

## 1.
def moyenne(L):
    """Renvoie la moyenne des termes de L"""
    somme = 0
    for i in L:
        somme += i
    return somme/len(L)

## 2.
def moyenne_par_paquet(L, N):
    """Renvoie la moyenne par paquets de N des termes de L"""
    Lmoy = []
    Linter = []
    for i in range(0, len(L), N):
        Linter = L[i:i + N]
        Lmoy.append(moyenne(Linter))
    return Lmoy

## 3.
def notes_aleatoires(n):
    """Renvoie une liste aléatoire de n notes comprises entre 0 et 20."""
    import random
    L = [0]*n
    for i in range(n):
        L[i] = random.randint(0, 20)
    return L

## 4.
def frequence(N):
    """Renvoie l'hist..."""
    L = notes_aleatoires(N)
    #Lmoy = moyenne_par_paquet(L, 2)
    plt.hist(L, 10)
    plt.show()