a = 1
b = 1.2
h = 0.02
d = 1e-6


def series_sum(x, d):
    sum_value = 0
    n = 1
    while True:
        term = (x - 1) ** (2 * n + 1) / ((2 * n + 1) * (x + 1) ** (2 * n + 1))
        sum_value += term

        if abs(term) < d:
            break

        n += 1

    return 2 * sum_value


x = a
while x <= b:
    result = series_sum(x, d)
    print(f"x = {x}, f(x) = {result}")
    x += h
    a = round(x, 2)
