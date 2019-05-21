#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ee:
        print("Exception:", ee, file=stderr)
