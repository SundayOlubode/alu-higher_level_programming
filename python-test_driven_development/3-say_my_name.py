#!/usr/bin/python3
""" Say my name """


def say_my_name(first_name, last_name=""):
    """ Say """

    if type(last_name) not str:
        raise TypeError('last_name must be a string')
    if type(first_name) not str:
        raise TypeError('first_name must be a string')

    return "My name is {} {}".format(first_name, last_name)
