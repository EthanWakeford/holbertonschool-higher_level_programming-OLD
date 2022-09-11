#!/usr/bin/python3
'''this module divides each element of a matrix by the div variable'''


def matrix_divided(matrix, div):
    '''function to divide each element of a matrix'''

    error = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(error)

    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append([])
        for elem in matrix[row]:
            new_matrix[row].append(round((elem / div), 2))
    return (new_matrix)
