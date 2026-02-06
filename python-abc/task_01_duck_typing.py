#!/usr/bin/python3
"""
This module defines an abstract class Shape and two concrete classes
Circle an Rectangle
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Defines area abstract method and perimeter method"""
    @abstractmethod
    def area(self):
        """Return the area of the class"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the area of the class"""
        pass


class Circle(Shape):
    """Defines a Circle, subclass of Shape"""

    def __init__(self, radius=0):
        """Initialize the circle radius argument"""
        self.radius = abs(radius)

    def area(self):
        """Defines the area of the Circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Defines the perimeter of the Circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Defines a Rectangle, subclass of Shape"""

    def __init__(self, width, height):
        """Initialize the width and height arguments"""
        self.width = width
        self. height = height

    def area(self):
        """Defines the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Defines the perimeter of the rectangle"""
        return (self.width + self.height) * 2


def shape_info(shape):
    """Prints the area and perimeter of shape"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
