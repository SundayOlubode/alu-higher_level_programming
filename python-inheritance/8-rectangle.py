#!/usr/bin/python3
""" An empty class """


class BaseGeometry:
    """ BaseGeometry """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):
    """ Rectangle """
    def __init__(self, width, height):
        self.__height = height
        self.__width = width

    super().integer_validator('width', self.__width)
    super().integer_validator('height', self.__height)
