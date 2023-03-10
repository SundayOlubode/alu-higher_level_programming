#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    counter = 0
    for item in my_list:
        try:
            print(item, end='')
        except IndexError:
            return
        else:
            counter += 1
    print('\n')
    return counter
