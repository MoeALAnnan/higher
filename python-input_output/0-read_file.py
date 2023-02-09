#!/usr/bin/python3
""" opening files """


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        for x in f:
            print("{}".format(x), end="")
