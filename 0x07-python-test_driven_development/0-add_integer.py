#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers
    """
    if type(a) is float:
        a = int(a)
    elif type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is float:
        b = int(b)
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
