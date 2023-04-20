#!/usr/bin/python3
""" base.py """


class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

b1 = Base()
