#!/usr/bin/env python3
"""Module that defines a function to write a string to a UTF8 text file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file, creating or overwriting it.

    Returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
