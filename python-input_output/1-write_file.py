#!/usr/bin/python3
""" Write into a file """


def write_file(filename="", text=""):
    """ Write """
    with open(filename, 'w+') as f:
        return f.write(text)
