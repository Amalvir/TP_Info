def nbsol(a, b, c):
    a = a*100
    b = b*100
    c = c*100
    delta = b**2 - 4*a*c
    if delta == 0:
        return 1
    elif delta > 0:
        return 2
    else:
        return 0
    