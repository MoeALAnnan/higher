#!/usr/bin/python3
""" load object from json file"""
import json


def load_from_json_file(filename):
    """ a function that loads  object from json file """
    with open(filename, encoding="utf-8") as f:
        y = ""
        for k in f:
            y = y + k
        return (json.loads(y))
