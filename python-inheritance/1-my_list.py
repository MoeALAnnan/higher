#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """ print sorted """
        new = self[:]
        new.sort()
        print(new)
