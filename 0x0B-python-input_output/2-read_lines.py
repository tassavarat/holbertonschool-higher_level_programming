#!/usr/bin/python3
"""2-read_lines module
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints to stdout
    """
    with open(filename, encoding="utf8") as f:
        if not nb_lines:
            print(f.read(), end='')
        else:
            for line in range(nb_lines):
                print(f.readline(), end='')
