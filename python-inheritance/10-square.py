#!/usr/bin/python3
""" Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square inheriting from Rectangle """
    def __init__(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be greater than 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
