#!/usr/bin/python3


"""This module defines an empty class"""


class BaseGeometry:
    """Defines the area() methods"""
    def area(self):
        """Raises an exception because it's not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
