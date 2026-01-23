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
    length = len(text)
    new_line = True

    while i < length:
        if new_line and text[i] == ' ':
            i += 1
            continue

        print(text[i], end='')
        new_line = False

        if text[i] in ['.', '?', ':']:
            print('\n')
            new_line = True
            while i + 1 < length and text[i + 1] == ' ':
                i += 1

        i += 1

