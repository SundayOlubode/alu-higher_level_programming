#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    if len(tuple_a) == 0:
        tuple_a += (0, 0)
    elif len(tuple_a) < 2:
        tuple_a += (0,)
    if len(tuple_b) == 0:
        tuple_b += (0, 0)
    elif len(tuple_b) < 2:
        tuple_b += (0,)
    for i in range(2):
        new_tuple += (tuple_a[i] + tuple_b[i],)
            
