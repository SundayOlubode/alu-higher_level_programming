#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    set_items = list(set_1) + list(set_2)
    diff_elems = set(set_items)
    return diff_elems
