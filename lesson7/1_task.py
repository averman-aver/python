class Matrix:
    def __init__(self, list1):
        self.list1 = list1
        self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # пример, тут тоже нужно формировать в цикле размерности list1

    def __add__(self, other):
        for i in range(len(self.list1)):
            for j in range(len(self.list1[i])):
                self.matrix[i][j] = self.list1[i][j]  + other[i][j]
        return Matrix((self.matrix))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list1]))


matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

matrix_10 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]

my_matrix1 = Matrix(matrix_1)
my_matrix2 = Matrix(matrix_2)

print(my_matrix1)
print(my_matrix2)

my_matrix3 = my_matrix1 + matrix_10
print(type(my_matrix3))
print(my_matrix3)

my_matrix4 = my_matrix1 + matrix_2
print(type(my_matrix4))
print(my_matrix4)

