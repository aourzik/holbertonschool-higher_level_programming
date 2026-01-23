#!/usr/bin/python3
"""This module prints a square with #."""


def print_square(size):
    """
    Docstring for print_square

    Size: size of the square, both row and column.

    The function prints a square with the size parameter,
    size must be an integer otherwise raises a TypeError,
    it has to be more than 0 otherwise raises a ValueError,
    and if it's a float and less than 0 it raises a
    TypeError.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
