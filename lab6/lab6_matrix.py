class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            x = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < x:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = x
        return arr

    @staticmethod
    def sort_desc(func):
        def wrapper(self, *args, **kwargs):
            for matrix_row in self.matrix:
                self.insertion_sort(matrix_row)
            return func(self, *args, **kwargs)
        return wrapper

    @sort_desc
    def sort_matrix_rows(self):
        for sorted_row in self.matrix:
            print(sorted_row)

    def column_sums(self):
        sums = [0] * len(self.matrix[0])
        for row_index in range(1, len(self.matrix)):
            for col_index in range(row_index):
                sums[col_index] += self.matrix[row_index][col_index]
                if sums[col_index] == 0:
                    del sums[col_index]
        return sums

    @staticmethod
    def geometric_mean(sums):
        product = 1
        for s in sums:
            product *= abs(s)
        geometric_means = product ** (1 / len(sums))
        return geometric_means

    def __add__(self, other):
        return Matrix([
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ])

    def process_all(self):
        print("Початкова матриця:")
        for initial_row in unsorted_matrix:
            print(initial_row)

        print("\nВідсортована матриця:")
        self.sort_matrix_rows()

        column_sums = self.column_sums()
        print("\nСуми елементів стовпців під головною діагоналлю:\n", column_sums)

        geom_mean = self.geometric_mean(column_sums)
        print("\nСереднє геометричне значення:\n", geom_mean)

unsorted_matrix = [
    [3, 5, 9, 24, 2],
    [-23, 0, 37, 29, 10],
    [0, 1, 4, -2, -5],
    [-5, -83, -74, 82, -1],
    [11, 88, -5, 81, -39]
]
other_matrix = [
    [3, 5, 9, 24, 2],
    [-23, 4, 37, 29, 10],
    [0, 1, 4, -2, -5],
    [-5, -83, -7, 82, 8],
    [11, 88, -5, 6, -39]
]

matrix_sort = Matrix(unsorted_matrix)
matrix_sort.process_all()

matrix1 = Matrix(unsorted_matrix)
matrix2 = Matrix(other_matrix)
result = matrix1 + matrix2

print("\nРезультат додавання двох матриць:")
for result_row in result.matrix:
    print(result_row)
