#!/usr/bin/python3
""" this is a class the defines a Rectangle """


class Rectangle:
     """Initializes the data."""
    def __init__(self, width=0, height=0):
         """Initializes the data."""
        self.width = width
        self.height = height
    
    @property
        def width(self)
        """retrieving width"""
            return self.__width
    @width.setter
        def width(self, value)
        """managing the width"""
            if isinstance(value, int) is False:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

