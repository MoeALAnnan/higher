#!/usr/bin/python3
""" a function that check if an object is an instance of a class """


def inherits_from(obj, a_class):
    """ a function that check if an object is an instance of a class """
    if type(obj) != (a_class):
        return (issubclass(type(obj), a_class))
