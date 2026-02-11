#!/usr/bin/python3
"""Module that defines a class that defines a student"""


class Student:
    """Defines a student by public instances"""

    def __init__(self, first_name, last_name, age):
        """Defines the instances of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retreives a dictionary
        representation of a student instance"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__

        filtered = {}
        for key in attrs:
            if key in self.__dict__:
                filtered[key] = self.__dict__[key]
        return filtered

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        self.__dict__ = json
