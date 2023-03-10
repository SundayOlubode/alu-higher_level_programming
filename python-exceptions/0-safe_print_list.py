#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    counter = 0
    if x == 0:
        return counter

    for i in range(x):
        try:
            print(my_list[i], end='')
        except IndexError:
            return
        else:
            counter += 1
    print()
    return counter
