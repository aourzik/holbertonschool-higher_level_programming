#!/usr/bin/python3
"""This module prints a text with 2 new lines after specials characters."""


def text_indentation(text):
    """
    Docstring for text_indentation function.

    Text: string variable.

    Text must be a string otherwise raises TypeError with an
    explicit message. There should be no space between or at
    the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    len = len(text)

    while i < len:
        print(text[i], end="")

        if text[i] in ".?:":
            print('\n')
            i += 1

            while i + 1 < len and text[i] == ' ':
                i += 1

            continue

        i += 1
