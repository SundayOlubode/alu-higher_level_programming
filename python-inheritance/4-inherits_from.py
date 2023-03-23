#!/usr/bin/python3
""" Check if an instance """


def inherits_from(obj, a_class):
    """ Subclass """
    return isinstance(obj, a_class) and type(obj) not a_class
