#!/usr/bin/python3
"""1-number_of_lines module
"""


def number_of_lines(filename=""):
    """Returns number of lines in text file
    """
    line_num = 0
    with open(filename, encoding="utf8") as f:
        for line in f:
            line_num += 1
    return line_num
