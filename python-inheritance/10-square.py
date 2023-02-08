#!/usr/bin/python3
""" base geometry """


class BaseGeometry:
    """base gemoetry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """sub class """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        obj = BaseGeometry()
        obj.integer_validator("height", height)
        obj2 = BaseGeometry()
        obj2.integer_validator("width", width)

    def area(self):
        return (self.__height * self.___width)

    def __str__(self):

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """sub class: Square """
    def __init__(self, size):
        self.__size = size
        print("[Rectangle] {}/{}".format(self.__size, self.__size))
