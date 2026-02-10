#/usr/bin/python3
import json

def from_json_string(my_str):
    with open(my_str) as f:
        return json.load(f)
