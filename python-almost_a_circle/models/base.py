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
    def to_json_string(list_dictionaries):
        """converting json object to string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return (json.dumps([]))
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """classmethod"""
        list_dict = []
        for obj in list_objs:
            x = obj.to_dictionary()
            list_dict.append(x)

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            y = cls.to_json_string(list_dict)
            f.write(y)
        f.close()

    @staticmethod
    def from_json_string(json_string):
        """method to convert json string"""
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """a class method that returns an instance with all attributes """
        # create instance with dummy value
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4, 0, 0)
        elif cls.__name__ == "Square":
            dummy = cls(2, 4, 1)
        dummy.update(**dictionary)
        return (dummy)
