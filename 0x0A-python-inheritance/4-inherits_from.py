#!/usr/bin/python3
"""Returns True if obj is an instance of a class that inherited \
from the specified class; otherwise False
"""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is not a_class
