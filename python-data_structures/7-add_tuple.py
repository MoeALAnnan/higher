#!/usr/bin/python2
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is not None and tuple_b is not None:
        if len(tuple_a) == 1:
            x = tuple_a[0] + tuple_b[0]
            y = tuple_b[1]
        elif len(tuple_a) == 0:
            x = tuple_b[0]
            y = tuple_b[1]
        elif len(tuple_b) == 1:
            x = tuple_a[0] + tuple_b[0]
            y = tuple_a[1]
        elif len(tuple_b) == 0:
            x = tuple_a[0]
            y = tuple_a[1]
        else:
            x = tuple_a[0] + tuple_b[0]
            y = tuple_a[1] + tuple_b[1]
        tuple_c = x, y,
        return (tuple_c)
