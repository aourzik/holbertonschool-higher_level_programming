#!/usr/bin/env python3
"""
This module defines a CustomObject class and provides methods
to serialize and deserialize instances using the pickle module.
"""

import pickle


class CustomObject:
    """
    A custom class representing a person.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a new CustomObject instance.

        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file into an instance of CustomObject.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except (OSError, pickle.PickleError, EOFError):
            return None

        return None
