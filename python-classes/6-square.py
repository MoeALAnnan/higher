#!/usr/bin/python3
class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): size of the square
        __position (tuple): position of the square

    Methods:
        area(): calculates the area of the square
        my_print(): prints the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): size of the square (default 0)
            position (tuple): position of the square (default (0, 0))

        Raises:
            TypeError: if sizep is not an integer or
            position is not tuple of 2 positive integers
            ValueError: if size is less than 0
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) != tuple or len(position) != 2\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("size must be an integer")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for size

        Args:
            value (int): size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method for position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter method for position

        Args:
            value (tuple): position of the square

        Raises:
            TypeError: if value is not a tuple or has length not equal to 2
            ValueError: if either element of the tuple is less than 0
        """
        if type(value) != tuple or len(value) != 2\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        if self.__size == 0:
            print("")
        y = 0

        for y in range(self.__position[1]):
            print("")

        x = 0
        z = 0

        for x in range(self.__size):
            for z in range(self.__position[0]):
                print("_", end="")
            for x in range(self.__size):
                print("#", end="")
            print("")

