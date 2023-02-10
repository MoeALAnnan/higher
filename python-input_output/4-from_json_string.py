#!/usr/bin/python3
""" jason convert """
import json


def from_json_string(my_str):
    """ from jason to object """
    return (json.loads(my_str))
