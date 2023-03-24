#!/usr/bin/python3
"""Object - json"""


import json


def load_from_json_file(filename):
    """Object - json"""
    with open(filename, "r") as f:
        return json.load(f)
