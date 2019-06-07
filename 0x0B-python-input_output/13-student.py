#!/usr/bin/python3
"""12-student module
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

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of Student instance
        """
        if attrs is not None:
            my_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance
        """
        self.__dict__ = json
