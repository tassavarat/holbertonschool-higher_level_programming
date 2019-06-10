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
            x (int):
            y (int):
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    """int: Assigns value to width"""
    def width(self):
        return self.__width

    @property
    """int: Assigns value to height"""
    def height(self):
        return self.__height

    @property
    """int: Assigns value to x"""
    def x(self):
        return self.__x

    @property
    """int: Assigns value to y"""
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
