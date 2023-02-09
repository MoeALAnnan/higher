#!/usr/bin/python3
""" write files"""


def write_file(filename="", text=""):
    """ a function that reads file and print it to the terminal """
    with open(filename, 'a+', encoding="utf-8") as f:
        return (f.write(text))
