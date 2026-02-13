#!/usr/bin/env python3
"""
Module: task_00_basic_serialization

This module provides basic JSON serialization and deserialization
functionalities for Python dictionaries.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    This function takes a Python dictionary and writes it to a file
    in JSON format. If the specified file already exists, it will
    be overwritten.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the JSON file where data will be saved.

    Raises:
        TypeError: If data is not serializable to JSON.
        OSError: If there is an issue writing to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
