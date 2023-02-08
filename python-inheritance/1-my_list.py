#!/usr/bin/python3
""" a class """


class MyList(list):
    """print sorted list """
    def print_sorted(self):
        print(sorted(self))
