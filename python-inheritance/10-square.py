#!/usr/bin/python3
"""This module defines the square class"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle class"""

    def __init__(self, size):
        """Initialize the Square class"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Defines the area of Square"""
        return self.__size ** 2
