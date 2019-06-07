#!/usr/bin/python3
"""3-write_file module
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns number of characters
    written
    """
    with open(filename, mode='w', encoding="utf8") as f:
        return f.write(text)
