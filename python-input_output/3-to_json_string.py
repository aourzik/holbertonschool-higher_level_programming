#!/usr/bin/python3
"""Module that defines a function that returns
the JSON representation of an object"""

import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object"""
    return json.dump(my_obj)
