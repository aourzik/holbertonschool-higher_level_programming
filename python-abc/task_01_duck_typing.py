#!/usr/bin/python3
"""This module defines an abstract class Shape and two concrete classes
Circle an Rectangle"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Defines area abstract method and perimeter method"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Defines a Circle, subclass of Shape"""

    def __init__(self, radius):
        """Initialise the circle radius argument"""
        self.radius = radius

    def area(self):
        """Defines the area of the Circle"""
        return (3.14 * (self.radius ** 2))

    def perimeter(self):
        """Defines the perimeter of the Circle"""
        return (2 * 3.14 * self.radius)


class Rectangle(Shape):
    """Defines a Rectangle, subclass of Shape"""

    def __init__(self, width, height):
        """Initialise the width and height arguments"""
        self.width = width
        self. height = height

    def area(self):
        """Defines the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Defines the perimeter of the rectangle"""
        return (self.width + self.height) * 2
