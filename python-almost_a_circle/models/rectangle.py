#!/usr/bin/python3
""" rectangle.py """


from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize every instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def setter(self, val):
        self.__width = self.width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, val):
        self.__height = self.height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = self.x
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = self.y
