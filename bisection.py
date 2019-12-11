from scipy import sign
from scipy.optimize import bisect


def bisection(f, a, b, e=10**(-12)):
    while (b - a) > e:
        m = a + (b - a) / 2
        if sign(f(a)) == sign(f(m)):
            a = m
        else:
            b = m
    m = a + (b - a) / 2
    return m


if __name__ == "__main__":
    f = lambda x: x**2 - 10
    a = 0
    b = 10
    print('Bisección Propio:', bisection(f, a, b))
    print('Bisección Scipy:', bisect(f, a, b))
    print('Raíz Exacta:', 10**(1/2))
