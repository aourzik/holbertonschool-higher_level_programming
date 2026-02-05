#!/usr/bin/python3
from builtins import list

class VerboseList(list):
    def append(self, i):
        super().append(i)
        print(f"Added [{i}] to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, i):
        super().remove(i)
        print(f"Removed [{i}] from the list.")

    def pop(self, index=0):
        super().pop(index)
        print(f"Popped [{index}] from the list.")
