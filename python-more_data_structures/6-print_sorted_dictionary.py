#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)
    for k, v in sorted_dict:
        print('{}: {}'.format(k, v))
