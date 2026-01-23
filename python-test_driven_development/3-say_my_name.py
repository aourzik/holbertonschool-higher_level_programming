#!/usr/bin/python3
"""
This module prints a sentence with the first name
and last name of the user.
"""


def say_my_name(first_name, last_name=""):
    """
    Docstring for say_my_name

    First_name: takes the user's first name.
    Last_name: takes the user's last name.

    The function print the two variables first and last name.
    It has to be a string or raises TypeError message.

    Return the user's name string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
