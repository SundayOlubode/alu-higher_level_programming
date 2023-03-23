#!/usr/bin/python3
""" Check if a subclass """


def inherits_from(obj, a_class):
    """ check subclass """
    return isinstance(obj, a_class) and type(obj) not a_class
