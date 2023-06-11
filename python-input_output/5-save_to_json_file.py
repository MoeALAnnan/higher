#!/usr/bin/python3
""" import """
import json
""" a function that deserialize """


def save_to_json_file(my_obj, filename):
    """ save to file """
    with open(filename, 'w', encoding='utf-8') as f:
        serializing = json.dumps(my_obj)
        f.write(serializing)
