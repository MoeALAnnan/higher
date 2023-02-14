#!/usr/bin/python3
"""this is the documentation"""
import json


class Base:
    """ This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
             to avoid duplicating the same code (by extension, same bugs) """
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    """
    method to convert json object to stringsi
    """
    def to_json_string(list_dictionaries):
        """converting json object to string"""
        return (json.dumps(list_dictionaries))
