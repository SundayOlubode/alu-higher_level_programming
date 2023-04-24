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

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json rep to a file """
        objs_dict_rep = []

        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None or len(list_objs) < 1:
                f.write("[]")
                return

            for obj in list_objs:
                objs_dict_rep.append(obj.to_dictionary())
            f.write(cls.to_json_string(objs_dict_rep))

    @staticmethod
    def from_json_string(json_string):
        """ return list of json string """
        if json_string is None or len(json_string) < 1:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an updated instance with all attributes """
        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 6)
        elif cls.__name__ == 'Square':
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy
