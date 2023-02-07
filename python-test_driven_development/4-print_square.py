#!/usr/bin/python3
""" function that prints a square """


def print_square(size):
    """ this function prints a square """
    if type(size) is int and size > 0:
        for i in range(0, size):
            for j in range(size):
                print("#", end="")
            print("")
    elif size == 0:
        print("")
    elif size < 0:
        raise TypeError("size must be >= 0")

    else:
        raise TypeError("size must be an integer")
