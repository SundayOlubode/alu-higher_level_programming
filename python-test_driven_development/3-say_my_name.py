#!/usr/bin/python3
""" Say my name """


def say_my_name(first_name, last_name=""):
    """ Say """

    if not isinstance(str, last_name):
        raise TypeError('last_name must be a string')
    if not isinstance(str, first_name):
        raise TypeError('first_name must be a string')

    return "My name is {} {}".format(first_name, last_name)
