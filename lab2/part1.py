from math import cos, tan, log10, sqrt

h = 0.02
a = 2
b = 5

while a < b:
    if a < 3:
        print(cos(a ** 0.3))
    elif 3 <= a < 4:
        print(sqrt(a ** 3 + log10(a)))
    elif a >= 4:
        print(1 / tan(a ** 2))
    a += h
    a = round(a, 3)
    print(a)

