#!/usr/bin/python3
""" a function that prints 2 strings """


def say_my_name(first_name, last_name=""):
    """ a function that prints 2 strings """
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except:
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        else:
            raise TypeError("last_name must be a string")
