#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return
    else:
        reverse = len(my_list)
        for x in reversed(range(0, reverse)):
            print("{:d}".format(my_list[x]))
