#/usr/bin/python3
"""Module that defines a function that returns a Python
object from JSON"""

import json


def from_json_string(my_str):
    """Function that returns a Python object from a JSON
    string"""
    with open(my_str) as f:
        return json.loads(f)
