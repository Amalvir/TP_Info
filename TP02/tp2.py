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
def carre(L):
    for i in range(len(L)):
        L[i]=L[i]**2
    return L

## Exo 10

