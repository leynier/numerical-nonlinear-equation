def newton_raphson(f, df, x_a, e=10**(-12)):
    while True:
        x = x_a - f(x_a) / df(x_a)
        if abs(x - x_a) <= e:
            return x
        x_a = x


if __name__ == "__main__":
    f = lambda x: x**2 - 10
    df = lambda x: 2 * x
    x_a = 3
    print('Newton Raphson Propio:', newton_raphson(f, df, x_a))
    print('Raíz Exacta:', 10**(1/2))
