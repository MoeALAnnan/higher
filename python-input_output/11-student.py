#!/usr/bin/python3
"""class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """to json method"""
        new_dic = {}
        dictionary = {'first_name': self.first_name,
                      'last_name': self.last_name,
                      'age': self.age}
        if type(attr) == list:
            new_dictionary = {}
            for i in attr:
                for k, v in dictionary.items():
                    if i == k:
                        new_dictionary[k] = v
            return (new_dictionary)
        else:
            return (dictionary)

    def reload_from_json(self, json):
        for k, v in json.items():
            if k == "first_name":
                self.first_name = v
            elif k == "last_name":
                self.last_name = v
            elif k == "age":
                self.age = v
