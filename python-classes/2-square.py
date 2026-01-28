#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """ Square defines a square with private instance named size."""

    def __init__(self, size=0):
        """Initialize the square with a size argument."""
        self.__size = size

        if self.__size is not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
