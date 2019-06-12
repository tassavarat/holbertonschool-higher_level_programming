#!/usr/bin/python3
"""base module"""
import json
from os import path


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        my_list = []
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            for i in list_objs:
                my_list.append(i.to_dictionary())
        with open(filename, mode='w') as f:
            f.write(cls.to_json_string(my_list))

    @classmethod
    def create(cls, **dictionary):
        """Returns: Instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            r = cls(1, 1)
        else:
            r = cls(1)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """Returns: List of instances"""
        filename = cls.__name__ + ".json"
        my_list = []

        if path.isfile(filename):
            with open(filename) as f:
                list_output = cls.from_json_string(f.read())
            for e in list_output:
                my_list.append(cls.create(**e))
        return my_list

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns: JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns: List of the JSON string representation"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)
