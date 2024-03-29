#!/usr/bin/python3
"""
    This module create a function that adds two integers
"""


def add_integer(a, b=98):
    """This function adds two integers"""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
