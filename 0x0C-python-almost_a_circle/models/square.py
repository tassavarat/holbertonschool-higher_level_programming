#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
        Args:
            size (int): Square parameter
            x (int): Horizontal offset
            y (int): Vertical offset
            id (int): id attribute
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Creates a new string object from the given object
        Returns: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """int: Assigns value to size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], e)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns: Dictionary representation of Square"""
        my_dict = super().to_dictionary()
        my_dict["size"] = my_dict["width"]
        del my_dict["width"], my_dict["height"]
        return my_dict
