#!/usr/bin/python3
""" this is a class the defines a Rectangle"""


class Rectangle:
    """initializing width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieving width"""
        return self.__width

    @width.setter
    def width(self, value):
        """managing the width"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieving Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """managing the Height"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ retrieving area """
        return self.__height * self.__width

    def perimeter(self):
        """ retrieving perimeter """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """ printing rectangle """
        z = ""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        for i in range(0, self.__height):
            for k in range(0, self.__width):
                z = z + str(self.print_symbol)
            if (i != self.__height - 1):
                z = z + """
"""
        return z

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances += -1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
                return (rect_1)
            else:
                return (rect_2)
