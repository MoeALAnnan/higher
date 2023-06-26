#!/usr/bin/python3
"""class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {}
        if type(attrs) == list:
            for i in range(len(attrs)):
                if attrs[i] == "first_name":
                    my_dict['first_name'] = self.first_name
                elif attrs[i] == "last_name":
                    my_dict['last_name'] = self.last_name
                elif attrs[i] == "age":
                    my_dict['age'] = self.age
            return (my_dict)
        else:
            return (vars(self))
