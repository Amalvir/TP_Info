import matplotlib.pyplot as plt
from time import clock

def Euler(F, a, b, y0, h):
    """Valeur approché de la solution de y' = F(t,y)"""
    t = a
    y = y0
    les_t = [a]
    les_y = [y0]
    while t + h <= b:
        y = y + h*F(t,y)
        t = t + h
        les_t.append(t)
        les_y.append(y)
    return les_t, les_y

def F(t,y):
    return y

def main():
    for i in range(0, 7):
        t0 = clock()
        X, Y = Euler(F, 0, 5, 1, 10**-i)
        t1 = clock()
        print(str(10**-i), ":", str(t1 - t0), "s")
        plt.plot(X, Y, label="pas = 10^-"+str(i))
    plt.legend()
    plt.show()

# 3.b)
# 1  :  8.018343407911743e-06 s
# 0.1  :  3.3677042296176296e-05 s
# 0.01  :  0.00023702223101906839 s
# 0.001  :  0.002282662000212099 s
# 0.0001  :  0.022017408785728776 s
# 1e-05  :  0.2566209866988487 s
# 1e-06  :  2.548181744413071 s
#
# Meilleur compromis : 10**-2

#main()