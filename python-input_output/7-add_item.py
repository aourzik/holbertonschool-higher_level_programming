#!/usr/bin/python3
"""This module defines a script that adds all arguments
to a Python list and saves them to a file"""

import sys, json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file
    using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Function that creates an object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    item = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
