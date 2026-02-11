#!/usr/bin/python3
"""This module defines a script that adds all arguments
to a Python list and saves them to a file"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    item = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
