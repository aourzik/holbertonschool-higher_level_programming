#!/usr/bin/python3
"""This module defines an abstract class Animal"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Defines an abstract methods sound"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Defines the method sound for class Dog"""
    def sound(self):
        return "Bark"


class Cat(ABC):
    """Defines the method sound for class Cat"""
    def sound(self):
        return "Meow"
