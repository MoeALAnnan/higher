#!/usr/bin/python3
""" opening files """


def read_file(filename=""):
    f = open(filename, 'r', encoding="utf-8")
    for x in f:
        print("{}".format(x), end="")
