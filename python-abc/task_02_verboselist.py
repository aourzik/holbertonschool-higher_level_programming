#!/usr/bin/python3
"""This module defines a class named VerboseList that
extends the Python class list."""

from builtins import list


class VerboseList(list):
    """Defines a class that inherits the builtins list."""

    def append(self, i):
        """Defines a class that added an item to a list."""
        super().append(i)
        print(f"Added [{i}] to the list.")

    def extend(self, iterable):
        """Defines a class that extends a list."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, i):
        """Defines a class that remove an item from a list."""
        print(f"Removed [{i}] from the list.")
        super().remove(i)

    def pop(self, index=-1):
        """Defines a class that pops an item in a list."""
        i = self[index]
        print(f"Popped [{i}] from the list.")
        return super().pop(index)
