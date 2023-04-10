#!/usr/bin/bash
""" Divide a matrix """


def matrix_divided(matrix, div):
    """ Divide a matrix """
    
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    row_len = len(matrix[0])

    for row in matrix:
        if len(row) =! row_len:
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    return [[round(elem/div, 2) for elem in row] for row in matrix]
