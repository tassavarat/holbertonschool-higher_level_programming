#!/usr/bin/python3
class Rectangle:
    """Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """"Setter method
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """Creates a new string object from the given object
        """
        s = ''
        if self.__width > 0 and self.__height > 0:
            for _ in range(self.__height):
                for _ in range(self.__width):
                    s += str(self.print_symbol)
                s += '\n'
        return s[: -1]

    def __repr__(self):
        """Canonical string representation of the object
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Prints on instance delete
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
