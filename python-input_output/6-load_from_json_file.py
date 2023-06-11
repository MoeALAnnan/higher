#!/usr/bin/python3
""" import """
import json
""" a function that deserialize """


def load_from_json_file(filename):
    """ load from file """
    with open(filename, 'r', encoding='utf-8') as f:
        deserializing = json.load(f)
        return (deserializing)
