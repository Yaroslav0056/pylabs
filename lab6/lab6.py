matrix = [
    [3, 5, 9, 24, 2],
    [-23, 0, 37, 29, 10],
    [0, 1, 4, -2, -5],
    [-5, -83, -74, 82, -1],
    [11, 88, -5, 81, -39]
]

def sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x

for row in matrix:
    sort(row)
    print(row)

sum_under_diagonal = 0

for row in range(1, len(matrix)):
    for col in range(row):
        sum_under_diagonal += matrix[row][col]

print("\nСума елементів під головною діагоналлю:", sum_under_diagonal)