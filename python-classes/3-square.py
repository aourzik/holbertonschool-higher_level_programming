#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """ Square defines a square with private instance named size."""

    def __init__(self, size=0):
        """Initialize the square with a size argument."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size
