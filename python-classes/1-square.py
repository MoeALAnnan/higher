#!/usr/bin/python3
""" this is a class the defines a square """


class Square:
    """ declaring a private instance attribute """

    __size = None

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
