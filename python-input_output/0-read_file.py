#!/usr/bin/python3
""" opening files """


def read_file(filename=""):
    """ a function that reads file and print it to the terminal """
    with open(filename, 'r', encoding="utf-8") as f:
        for x in f:
            print("{}".format(x), end="")
