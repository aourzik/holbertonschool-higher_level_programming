#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """ Square defines a square with private instance named size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a size argument."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of Square."""
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """Setter for the size of Square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("posiotion must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("posiotion must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("posiotion must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#'."""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(self.position[0] * " ", end="")
                print(self.size * "#")
