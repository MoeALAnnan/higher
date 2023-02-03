#!/usr/bin/python3
""" this is a class the defines a square """


class Square:
    """ declaring a private instance attribute """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.size = size
        self.position = position

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

    @property
    def position(self):

        """ retrieving position """
        return self.__position

    @position.setter
    def position(self, value):

        """ setting position """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """a method that prints squares
        using hashtaghs depending on the size"""
        for k in range(self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for z in range(self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
            if self.__size == 0:
                print("")
