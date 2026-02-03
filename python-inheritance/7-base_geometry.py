#!/usr/bin/python3


"""This module defines an empty class"""


class BaseGeometry:
    """Defines the area() methods"""
    def area(self):
        """Raises an exception because it's not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be an integer")
