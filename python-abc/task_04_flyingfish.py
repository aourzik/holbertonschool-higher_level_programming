#!/usr/bin/python3
"""This module defines a flying fish that inherits a fish
and a bird class"""


class Fish:
    """Defines the Fish class"""

    def swim(self):
        """Method that makes the fish swim"""
        print("The fish is swimming")

    def habitat(self):
        """Defines the habitat of the fish"""
        print("The fish lives in water")


class Bird:
    """Defines the Bird class"""

    def fly(self):
        """Defines the bird flying"""
        print("The bird is flying")

    def habitat(self):
        """Defines the habitat of the bird"""
        print("The bird lives in the sky")


class FLyingFish(Fish, Bird):
    """Class that inherits of Fish and Bird classes"""

    def fly(self):
        """Override the fly method from bird"""
        print("The flying fish is soaring!")

    def swim(self):
        """Override the method from fish"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat method from both of parents"""
        print("The flying fish lives both in water and the sky!")
