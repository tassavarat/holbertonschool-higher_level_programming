#!/usr/bin/python3
"""0-read_file module
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints to stdout
    """
    with open(filename, encoding="utf8") as f:
        print(f.read(), end='')
