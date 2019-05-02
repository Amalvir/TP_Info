from cesar import *

## 1
def codage(cle, texte):
    code = ''
    for c in texte:
        b = crypte(cle, c)
        code = code+b
    return code

## 2
def decodage(cle, texte):
    code = ''
    for c in texte:
        code += clair(cle, c)
    return code
