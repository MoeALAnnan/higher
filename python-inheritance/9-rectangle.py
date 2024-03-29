#!/usr/bin/python3
""" Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inheriting from BaseGeometry """
    def __init__(self, width, height):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif width <= 0:
            raise ValueError("width must be greater than 0")
        elif height <= 0:
            raise ValueError("height must be greater than 0")
        else:
            self.__width = width
            self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
