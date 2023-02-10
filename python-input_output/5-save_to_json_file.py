#!/usr/bin/
""" write an object to text file using json reoresentation"""
import json


def save_to_json_file(my_obj, filename):
    """ a function that reads file and print it to the terminal """
    with open(filename, 'a+', encoding="utf-8") as f:
        x = json.dumps(my_obj)
        return (f.write(x))
