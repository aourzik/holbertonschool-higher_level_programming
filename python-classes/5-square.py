#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """ Square defines a square with private instance named size."""

    def __init__(self, size=0):
        """Initialize the square with a size argument."""
        self.__size = size

    @property
    def size(self):
        """Return the size of Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of Square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
    
    def my_print(self):
        """Print the square using '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print(self.__size * "#")
