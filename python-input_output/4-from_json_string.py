#!/usr/bin/python3
""" import """
import json
""" a function that deserialize """


def from_json_string(my_str):
    """ from json string """
    deserializing = json.loads(my_str)
    return (deserializing)
