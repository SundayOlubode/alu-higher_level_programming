#!/usr/bin/python3
""" base.py """

import json

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
    def id(self, val):
        if val is None:
            Base.__nb_objects += 1
            self.__id = self.__nb_objects
        else:
            self.__id = val

    @staticmethod
    def to_json_string(list_dictionaries):
        """Doc"""
        if list_dictionaries is None or \
                len(list_dictionaries) == 0:
            return "[]"
    return json.dumps(list_dictionaries)
