#!/usr/bin/python3
""" base.py """


class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init """
        if id is None:
            __nb_objects = __nb_objects + 1
            self.id = __nb_objects
        else:
            self.id = id

b1 = Base()
