#!/usr/bin/python3
"""This module defines the Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Initialize the Rectangle class with width and height arguments"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

        self.area(self.__width * self.__height)

    def str(self):
        """Return the rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
