#!/usr/bin/python3
""" square.py """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ square """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize instances """
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """ info """
        return '[Square] ({}) {}/{} - {}'\
                .format(self.id, self.x, self.y, self.width)

