#!/usr/bin/python3

def no_c(my_string):
    my_string = my_string.translate({ord('C'): ''})
    my_string = my_string.translate({ord('c'): ''})
    return my_string
