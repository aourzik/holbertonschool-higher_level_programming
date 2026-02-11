#!/usr/bin/python3
"""This module defines a function that writes an object
to a text file using JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file
    using JSON representation"""
    with open(filename, "w") as f:
        json.dumps(my_obj, f)
