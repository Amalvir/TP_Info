from cesar import *

def ordre(car):
    return ord(car)-97
    
def lettre(c):
    return chr(c+97)
    
def crypte(cle, car):
    z = ordre(cle)
    x = ordre(car)
    y = (x+z) % 26
    return lettre(y)
    
def clair(cle, car):
    z = ordre(cle)
    y = ordre(car)
    x = (y-z) % 26
    return lettre(x)
    
def est_une_lettre(car):
    c = ordre(car)
    return c >= 0 and c <= 25
    
def codage(cle, texte):
    texte_code = ""
    for car in texte:
        if est_une_lettre(car):
            # On code la lettre
            texte_code = texte_code + crypte(cle, car)
        else:
            texte_code = texte_code + car
            # On laisse en clair
    return texte_code
    
def decodage(cle, texte):
    texte_clair = ""
    for car in texte:
        if est_une_lettre(car):
            # On décode la lettre
            texte_clair = texte_clair + clair(cle, car)
        else:
            texte_clair = texte_clair + car
            # On laisse en clair
    return texte_clair
    
def frequence(texte):
    L_nb = [0]*26
    for car in texte:
        if est_une_lettre(car):
            x = ordre(car)
            L_nb[x] = L_nb[x] + 1
    return [nb/len(texte) for nb in L_nb]
    
    
    



