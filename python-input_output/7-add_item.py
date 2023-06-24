#!/usr/bin/python3
""" import """
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
""" writing and appending to file  """
add_args = []
try:
    add_args = load_from_json_file("add_item.json")

except (NameError, FileNotFoundError):
    pass
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        add_args.append(sys.argv[i])
save_to_json_file(add_args, "add_item.json")
