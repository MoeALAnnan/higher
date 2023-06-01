#!/usr/bin/python3
""" Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inheriting from BaseGeometry """
    def __init__(self, width, height):
        if width <= 0:
            raise TypeError("width must be greater than 0")
        elif height <= 0:
            raise TypeError("height must be greater than 0")
        elif type(width) is not int:
            raise ValueError("width must be an integer")
        elif type(height) is not int:
            raise ValueError("height must be an integer")
        else:
            self.__width = width
            self.__height = height
