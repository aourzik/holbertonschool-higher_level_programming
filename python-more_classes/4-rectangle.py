#!/usr/bin/python3
"""This module defines a class named Rectangle."""


class Rectangle:
    """Rectangle defines a rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of Rectangle."""
        return self.__width

    @property
    def height(self):
        """Return the height of Rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for the width of Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for the height of Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Prints the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            line = []
            for _ in range(self.height):
                line.append(self.width * "#")
            return "\n".join(line)

    def __repr__(self):
        """String representation of Rectangle."""
        return f"Rectangle{self.width}, {self.height}"
