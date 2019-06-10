#!/usr/bin/python3
"""base"""


class Base:
    """Manage id attributes for future classes and avoid code duplication
    Attributes:
        __nb_objects (int): Number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        Args:
            id (int): id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
