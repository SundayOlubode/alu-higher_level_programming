#!/usr/bin/python3
""" square.py """

from models.rectangle import Rectangle

class square(Rectangle):
    """ square """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize instances """
        super().__init__(id, x, y, width=size, height=size)


    def __str__(self):
        """ info """
        return '[Square] ({}) {}/{} - {}'\
                .format(self.id, self.x, self.y, self.width)

