from cmath import sqrt


def muller(f, x_1, x_2, x_3, e=10**-12):
    while abs(f(x_1)) > e:
        q = (x_1 - x_2) / (x_2 - x_3)
        a = q * f(x_1) - q * (1 + q) * f(x_2) + q**2 * f(x_3)
        b = (2 * q + 1) * f(x_1) - (1 + q)**2 * f(x_2) + q**2 * f(x_3)
        c = (1 + q) * f(x_1)
        r = x_1 - (x_1 - x_2) * ((2 * c) / (b + sqrt(b**2 - 4 * a * c)))
        s = x_1 - (x_1 - x_2) * ((2 * c) / (b - sqrt(b**2 - 4 * a * c)))
        if abs(f(r)) < abs(f(s)):
            x = r
        else:
            x = s
        if x.imag == 0j:
            x = x.real
            return x
        else:
            return x
        x_3 = x_2
        x_2 = x_1
        x_1 = x


if __name__ == "__main__":
    f = lambda x: x**2 - 10
    x_1 = 3
    x_2 = 3.5
    x_3 = 4
    print('Muller Propio:', muller(f, x_1, x_2, x_3))
    print('Raíz Exacta:', 10**(1/2))
