#!/usr/bin/pyhton3
""" This is my calculation module """
def add_integer(a, b=98):
    """ This function adds two integers a and b """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
