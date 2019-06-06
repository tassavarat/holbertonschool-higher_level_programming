#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited \
from the specified class; otherwise False
    """
    return not type(obj) is a_class and isinstance(obj, a_class)
