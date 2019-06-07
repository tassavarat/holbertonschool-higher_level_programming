#!/usr/bin/python3
"""11-student module
"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of Student instance
        """
        return self.__dict__
