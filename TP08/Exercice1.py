def somme1(n):
    """Somme pour i allant de 1 à n de 1/i**4"""
    s = 0
    for i in range(1, n + 1):
        s = s + 1/i**4
    return s

def somme2(n):
    """Pareil que somme1 mais à l'nevers"""
    s = 0
    i = n
    while i != 0:
        s = s + 1/i**4
        i = i - 1
    return s