#!/usr/bin/python3
"""Module that defines a class that defines a student"""

class student:
    """Defines a student by public instances"""

    def __init__(self, first_name, last_name, age):
        """Defines the instances of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retreives a dictionary
        representation of a student instance"""
        return self.__dict__
