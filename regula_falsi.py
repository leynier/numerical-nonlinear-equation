from scipy import sign


def regula_falsi(f, a, b, e=10**(-12)):
    x_a = 10**6
    while True:
        x = a - ((b - a) / (f(b) - f(a))) * f(a)
        t_e = abs(x - x_a)
        if f(x) == 0:
            return x
        elif sign(f(a)) == sign(f(x)):
            b = x
        else:
            a = x
        x_a = x
        if t_e <= e:
            return x


if __name__ == "__main__":
    f = lambda x: x**2 - 10
    a = 0
    b = 10
    print('Regula Falsi Propio:', regula_falsi(f, a, b))
    print('Raíz Exacta:', 10**(1/2))
