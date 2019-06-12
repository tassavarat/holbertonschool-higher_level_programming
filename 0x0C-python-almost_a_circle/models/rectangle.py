#!/usr/bin/python3
"""rectangle"""
from models.base import Base


class Rectangle(Base):
    """Inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        Args:
            width (int): Dimension of Rectangle
            height (int): Dimension of Rectangle
            x (int): Horizontal offset
            y (int): Vertical offset
            id (int): id attribute
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Assigns value to width"""
        return self.__width

    @property
    def height(self):
        """int: Assigns value to height"""
        return self.__height

    @property
    def x(self):
        """int: Assigns value to x"""
        return self.__x

    @property
    def y(self):
        """int: Assigns value to y"""
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns: Area value of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the character #
        offset by specified amount
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end='')
            for _ in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Creates a new string object from the given object
        Returns: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, e in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], e)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns: Dictionary representation of Rectangle"""
        my_dict = {}

        for k, v in self.__dict__.items():
            keys = k.split("__")[-1]
            my_dict[keys] = v
        return my_dict
