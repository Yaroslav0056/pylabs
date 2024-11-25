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
            for row in self.matrix:
                self.insertion_sort(row)
            return func(self, *args, **kwargs)
        return wrapper

    @sort_desc
    def sort_matrix_rows(self):
        for row in self.matrix:
            print(row)

    def column_sums(self):
        sums = [0] * len(self.matrix[0])
        for row in range(1, len(self.matrix)):
            for col in range(row):
                sums[col] += self.matrix[row][col]
                if sums[col] == 0:
                    del sums[col]
        return sums

    @staticmethod
    def geometric_mean(sums):
        sum_under_diagonal = 1
        for s in sums:
            sum_under_diagonal *= abs(s)
        geometric_means = sum_under_diagonal ** (1 / len(sums))
        return geometric_means

    def process_all(self):
        print("Початкова матриця:")
        for row in unsorted_matrix:
            print(row)

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

matrix_sort = Matrix(unsorted_matrix)
matrix_sort.process_all()