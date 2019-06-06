#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class BaseGeometry:
    """BaseGeometry class
    """
    def area(self):
        """Raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Square(Rectangle):
    """Square class
    """
    def __init__(self, size):
        """Instantiation
        """
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)

    def area(self):
        """Returns area
        """
        return self.__size ** 2
