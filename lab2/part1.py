from math import cos, tan, log10, sqrt

h = 0.02
a = 2
b = 5

while a < b:
    if a < 3:
        result_1 = cos(a ** 0.3)
        print(round(result_1, 3))
    elif 3 <= a < 4:
        result_2 = sqrt(a ** 3 + log10(a))
        print(round(result_2, 3))
    elif a >= 4:
        result_3 = 1 / tan(a ** 2)
        print(round(result_3, 3))
    a += h
    a = round(a, 3)
    print(a)

