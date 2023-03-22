#!/usr/bin/python3
""" Write a class MyList that inherits from list: """


class MyList(list):
    """ Sorts lists object """

    def print_sorted(self):
        self.sort()
        print(self)
