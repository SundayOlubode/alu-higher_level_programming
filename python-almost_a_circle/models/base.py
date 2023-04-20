#!/usr/bin/python3
""" base.py """


class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init """
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if id is None:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
        else:
            self.__id = id

b1 = Base()
b2 = Base()
