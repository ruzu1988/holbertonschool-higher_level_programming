#!/usr/bin/pyrhon3
def square_matrix_simple(matrix=[]):
    return [[element ** 2 for element in row] for row in matrix]
matrix = [[1, 2, 3], [4, 5, 6]]
square_matrix = square_matrix_simple(matrix)
print(square_matrix)
