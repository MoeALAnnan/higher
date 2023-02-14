#!/usr/bin/python3
"""class Square"""
from models.rectangle import Rectangle


"""class Square"""


class Square(Rectangle):
    """class Square that imports from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """new init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overloading of str method """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))
