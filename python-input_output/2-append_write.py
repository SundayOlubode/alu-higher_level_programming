#!/usr/bin/python3
"""Input and output"""


def append_write(filename="", text=""):
    """ append """
    with open(filename, 'a+') as f:
        return f.write(text)
