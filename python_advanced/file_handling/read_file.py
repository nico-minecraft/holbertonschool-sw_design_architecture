#!/usr/bin/env python3
"""Module that defines a function to read and print a UTF8 text file."""


def read_file(filename=""):
    """Read a text file (UTF8) and print its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
