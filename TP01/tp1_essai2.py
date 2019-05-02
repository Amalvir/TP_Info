import math as m
def inconnu(n):
        """ Factoriel de n """
        p=1
        for i in range(2,n+1):
            p=p*i
        return(p)

def coefbinm(n,k):
    """ Coefficients binomiaux de k parmi n """
    a = m.factorial(n)
    b = m.factorial(n-k)
    c = m.factorial(k)
    d = m.factorial(n)/(m.factorial(n-k)*m.factorial(k))
    return int(d)

def carre(n):
    """ Renvoie n au carré """
    n = n**2
    return(n)

def aire_disque(r):
    """ Renvoie l'aire d'un disque de rayon r """
    A = m.pi*carre(r)
    return(A)

def affichage(n):
    """ Affiche les carrés inférieur à n """
    i=1
    c=0
    while c < n :
        print(c)
        c = carre(i)
        i+=1

## Exo 1:
def racine(x):
    """Renvoie racine²(x)"""
    if x<0:
        return False
    else:
        return m.sqrt(x)

## Exo 2:
def valeur_de_u(n):
    a=1
    for i in range(1, n+1):
        a=a**2 + 1
    return a

def somme(n):
    s=0
    for i in range(0,n+1):
        s += valeur_de_u(i)
    return s

## Exo 3:
def depasse(p):
    u=-1
    n=-1
    while p > u :
        n+=1
        u=somme(n)
    return n

## Exo 5:
def echange(L, a, b):
    if a >= len(L) or b >= len(L):
        return "Out of range"
    else:
        (L[a], L[b]) = (L[b], L[a])

## Exo 7
def