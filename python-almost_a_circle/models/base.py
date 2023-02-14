#!/usr/bin/python3
import json
"""class Base"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    """static method"""
    def to_json_string(list_dictionaries):
        """converting json object to string"""
        return (json.dumps(list_dictionaries))
