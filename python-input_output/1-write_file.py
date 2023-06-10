#!/usr/bin/python3
""" a function that write a file """


def write_file(filename="", text=""):
    """write and return number of charachters """
    with open(filename, 'w', encoding="utf-8") as f:
        write = f.write(text)
        return (write)
