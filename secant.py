def secant(f, x_a, x_b, e=10**(-12)):
    while True:
        x = x_b - f(x_b) * ((x_b - x_a) / (f(x_b) - f(x_a)))
        t_e = abs(x - x_b)
        if t_e < e:
            return x
        x_a = x_b
        x_b = x


if __name__ == "__main__":
    f = lambda x: x**2 - 10
    x_a = 3
    x_b = 4
    print('Secante Propio:', secant(f, x_a, x_b))
    print('Raíz Exacta:', 10**(1/2))
