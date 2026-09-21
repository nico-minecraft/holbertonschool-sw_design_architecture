#!/usr/bin/env python3
"""Module that defines a function to append a string to a UTF8 text file."""


def append_write(filename="", text=""):
    """Append text to a UTF8 file, creating it if it doesn't exist.

    Returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
