#!/usr/bin/python3
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


class Rectangle(BaseGeometry):
    """Rectangle class
    """
    def __init__(self, width, height):
        """Instantiation
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """Returns area
        """
        return self.__width * self.__height

    def __str__(self):
        """Creates a new string object from the given object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
