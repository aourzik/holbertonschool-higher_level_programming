#!/usr/bin/python3
"""
This module provides a function that adds two integers.

It validates input values before performing
the calculation and raises errors if the argument
provided are not valid numbers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    The function accepts integers or float.
    Floats values are converted into integers before addition.

    Arguments : a and b, the two numbers to add.

    Return : the sum of a and b, an int.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (a != a or a in (float("inf"), float("-inf"))):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b in (float("inf"), float("-inf"))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
