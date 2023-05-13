#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(position) != tuple or len(tuple) != 2\
                or poistion[0] < 0 or poistion[1] < 0:
            raise TypeError("size must be an integer")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
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
