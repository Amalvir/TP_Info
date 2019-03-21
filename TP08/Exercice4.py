def mystere():
    x = 1.0
    y = x + 1.0
    i = 0
    while (y - x == 1.0):
        i = i + 1
        x = x*2.0
        y = x + 1.0
        print(i, x, y)
    return y - x