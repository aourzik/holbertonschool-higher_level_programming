#!/usr/bin/python3
"""This module defines SwimMixin and FlyMixin and a Dragon class
that demonstrate mixin-based inheritance"""


class SwimMixin:
    """Provides swimming behavior"""

    def swim(self):
        """Defines the swim method"""
        print("The creature swims!")


class FlyMixin:
    """Provides flying behavior"""

    def fly(self):
        """Defines fly method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class that inherits from SwimMixin and FlyMixin classes"""

    def roar(self):
        """Additional methods for Dragon"""
        print("The dragon roars!")
