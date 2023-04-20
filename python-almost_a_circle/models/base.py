#!/usr/bin/python3
""" base.py """

class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init """
        if id not None:
            self.id = id
        else:
            __nb_objects =+ 1
            self.id = __nb_objects
