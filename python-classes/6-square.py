#!/usr/bin/python3
""" Define a class of Square """


class Square():
    ' Define with optionla args and setters '
    def __init__(self, size=0):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            return print()
        for i in range(self.__size):
            print('#' * self.__size)

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
