#!/usr/bin/python3
import json
""" a function that serialize """


def to_json_string(my_obj):
    """ to json string """
    serializing = json.dumps(my_obj)
    return (serializing)
