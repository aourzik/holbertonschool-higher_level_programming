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

    while (
        i < length
        and text[i] == " "
        and (i == 0 or text[i - 1] in ".?:")
    ):
        i += 1

    if i >= length:
        break

    print(text[i], end="")

    if text[i] in ".?:":
        print()
        print()
        i += 1

        while i < length and text[i] == " ":
            i += 1

        continue

    i += 1
