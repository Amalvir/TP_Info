import math as m

def trinome(a, b, c):
    delta = b**2 - 4*a*c
    L = []
    if delta == 0:
        L.append(-b/2*a)
    elif delta > 0:
        x1 = (-b - m.sqrt(delta))/2*a
        x2 = (-b + m.sqrt(delta))/2*a
        if x2>x1:
            L.append(x1)
            L.append(x2)
    return L

def p(x):
    return x**2 -160*x + 1