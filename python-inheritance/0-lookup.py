#!/usr/bin/python3
""" Create a function that returns defined names in an object """


def lookup(obj):
    """ return a list of defined names """
    return dir(obj)
