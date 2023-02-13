#!/usr/bin/python3
"""class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """retrieving width"""
        return self.__width

    @width.setter
    def width(self, value):
        """managing width"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """retrieving Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """managing the Height"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    @property
    def position_x(self):
        """setting position_x"""
        return self.__x

    @position_x.setter
    def position_x(self, value):
        """managing position_x"""
        if type(value) is not int:
            raise TypeError(" position x must be an integer")
        else:
            self.__x = value

    @property
    def position_y(self):
        """retrieving position_y"""
        return self.__y

    @position_y.setter
    def position_y(self, value):
        """managing position y"""
        if type(value) is not int:
            raise TypeError(" position y must be an integer")
