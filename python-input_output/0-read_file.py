#!/usr/bin/python3
"""This module defines a function that reads a text file
and prints it to stdout."""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout"""
    with open(filename, "r") as f:
        file = f.read()
        print(file)
