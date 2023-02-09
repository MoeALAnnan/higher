#!/usr/bin/python3
""" write files"""


def append_write(filename="", text=""):
    """ a function that reads file and print it to the terminal """
    # we used a+ to create a file that if it does not exist
    with open(filename, 'a+', encoding="utf-8") as f:
        return (f.write(text))
