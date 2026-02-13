#!/usr/bin/env python3
"""
This module provides functionality to convert data from a CSV file
into a JSON file using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into a JSON file named 'data.json'.
    """
    try:
        data = []

        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError):
        return False
