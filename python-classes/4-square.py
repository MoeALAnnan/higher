#!/usr/bin/python3
""" this is a class the defines a square """


class Square:
    """ declaring a private instance attribute """

    __size = None

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size
        x = isinstance(self.__size, int)
        if x is False:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            pass

    def area(self):
        """method to return area"""
        return self.__size**2

    @property
    def size(self):

        """retrieving size"""
        return self.__size

    @size.setter
    def size(self, value):

        """managing values"""

        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
