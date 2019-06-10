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
        self.size = size

    def __str__(self):
        """Creates a new string object from the given object
        Returns: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """int: Assigns value to size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns: Dictionary representation of Square"""
        my_dict = {}

        for k, v in self.__dict__.items():
            keys = k.split("__")[-1]
            if "width" not in keys and "height" not in keys:
                my_dict[keys] = v
        return my_dict
