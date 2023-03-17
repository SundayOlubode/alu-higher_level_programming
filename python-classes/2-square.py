#!/usr/bin/python3
""" Define a class of Square """


class Square():
    ' Define with optionla args and setters '
    def __init__(self, size=0):
        self.ourAtt = size

    @property
    def ourAtt(self):
        return self.__size
    
    @ourAtt.setter
    def ourAtt(self, size):
        if (not int(size)):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
