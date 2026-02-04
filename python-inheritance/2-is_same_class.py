#!/usr/bin/python3
"""This module defines is_the_same function"""


def is_same_class(obj, a_class):
    """Returns true if object is exactly an instance of the specific class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
