#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        if len(sublist) > 0:
            for item in sublist:
                print('{:d}'.format(item))
        else:
            print()
