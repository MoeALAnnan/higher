#!/usr/bin/python3
""" a function that append a file """


def append_write(filename="", text=""):
    """ append text to file """
    with open(filename, 'a', encoding="utf-8") as f:
        append = f.write(text)
        return (append)
