#!/usr/bin/python3
""" base geometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
# class BaseGeometry:
#   """base gemoetry """
# def area(self):
#   raise Exception("area() is not implemented")

#   def integer_validator(self, name, value):
#   if type(value) is not int:
#      raise TypeError("{} must be an integer".format(name))
# if value <= 0:

# raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """sub class """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
