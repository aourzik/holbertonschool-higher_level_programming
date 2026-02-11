#!/usr/bin/python3
"""Module that defines a function that writes a string to
a text file and returns the number of characters"""


def write_file(filename="", text=""):
    """Function that writes a string to UTF-8 text file and
    returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
