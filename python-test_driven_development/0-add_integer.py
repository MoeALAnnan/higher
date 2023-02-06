#!/usr/bin/python3
""" a function that adds two intgers """


def add_integer(a, b=98):
    """ a function that adds two intgers """
    if isinstance(a, int) or isinstance(a, float):
        if type(a) is float:
            a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, int) or isinstance(b, float):
        if type(b) is float:
            b = int(b)
    else:
        raise TypeError("b must be an integer")
    return (a + b)
