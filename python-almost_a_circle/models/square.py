#!/usr/bin/python3
"""class Square"""
from models.rectangle import Rectangle


"""class Square"""


class Square(Rectangle):
    """class Square that imports from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """new init"""
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """ overloading of str method """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
