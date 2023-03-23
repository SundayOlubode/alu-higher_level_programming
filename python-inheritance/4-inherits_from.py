#!/usr/bin/python3
"""Check if only a subclass"""


def inherits_from(obj, a_class):
    """check inheritance"""
    return isinstance(obj, a_class) and type(obj) not a_class
