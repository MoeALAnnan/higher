#!/usr/bin/python3
"""class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to json method"""
        dictionary = {'first_name': self.first_name,
                      'last_name': self.last_name,
                      'age': self.age}
        return (dictionary)