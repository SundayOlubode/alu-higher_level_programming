#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        if len(sublist) > 0:
            for item in sublist:
                if item == sublist[-1]:
                    print('{:d}'.format(item))
                else:
                    print('{:d}'.format(item), end=" ")
        else:
            print()
