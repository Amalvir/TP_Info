## 1
#for i in range(97,123):
#    print(chr(i))
## 2
def ordre(car):
    return ord(car) - 97
## 3    
def lettre(nb):
    return chr(nb + 97)

## 4
# y = x + z   <=>   x = y - z

## 5
def crypte(cle, car):
    z = ordre(cle)
    x = ordre(car)
    y = (x + z)%26
    return lettre(y)

## 6
def clair(cle, car):
    z = ordre(cle)
    y = ordre(car)
    x = (y - z)%26
    return lettre(x)