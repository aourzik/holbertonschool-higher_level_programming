#!/usr/bin/python3
import sys, json

def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    with open(filename, "r") as f:
        return json.load(f)

filename = "add_item.json"

args = sys.argv[1:]

items = load_from_json_file(filename)

items.extend(args)
save_to_json_file(items, filename)
