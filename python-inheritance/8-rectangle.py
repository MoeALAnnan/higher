#!/usr/bin/python3
""" Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inheriting from BaseGeometry """
    def __init__(self, width, height):
        if width > 0 and height > 0\
                and type(width) is int and type(height) is int:
            self.__width = width
            self.__height = height
        else:
            raise TypeError("height must be an integer")
