#!/usr/bin/python3
"""This module defines is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns true if object is exactly an instance of the specific class
    or parent class."""
    return isinstance(obj, a_class)
