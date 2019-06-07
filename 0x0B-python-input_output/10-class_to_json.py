#!/usr/bin/python3
"""10-class_to_json
"""


def class_to_json(obj):
    """Returns dictionary with simple data structure
    (list, dictionary, string, integer, and boolean)
    for JSON serialisation of an object
    """
    return obj.__dict__
