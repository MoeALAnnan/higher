#!/usr/bin/python3
""" a function that read a file """


def read_file(filename=""):
    """read and print it to std out """
    with open(filename, 'r', encoding="utf-8") as f:
        read = f.read()
        print(read, end="")
