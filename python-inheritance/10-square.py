#!/usr/bin/python3
""" base geometry """
Rectangle = __import__("9-rectangle").BaseGeometry


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        Rectangle.integer_validator(self, "size", size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
