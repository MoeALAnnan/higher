#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k in a_dictionary.keys():
        if k == key:
            a_dictionary[key] = value
    a_dictionary[key] = value
    return (a_dictionary)
