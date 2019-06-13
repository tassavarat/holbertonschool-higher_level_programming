#!/usr/bin/python3
"""Unittest for Base"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Base class test"""
    def test_id(self):
        """Prints out the id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_id_string(self):
        """Passing string"""
        b1 = Base("string")
        self.assertEqual(b1.id, "string")

    def test_id_None(self):
        """Passing None"""
        b1 = Base(None)
        self.assertEqual(b1.id, 5)

    def test_id_float(self):
        """Passing float"""
        b1 = Base(1.2)
        self.assertEqual(b1.id, 1.2)

    def test_id_NaN(self):
        """Passing float"""
        b1 = Base(float("nan"))
        self.assertEqual(b1.id is float("nan"), False)

    def test_id_inf(self):
        """Passing inf"""
        b1 = Base(float("inf"))
        self.assertEqual(b1.id is float("inf"), False)

    def test_unknown(self):
        """Testing name error"""
        with self.assertRaises(NameError):
            Base(a)

    def test_to_json_string_len(self):
        """Testing to_json_string len"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(len(json_dictionary), len(str([{
            "x": 2, "width": 10, "id": 6, "height": 7, "y": 8}])))

    def test_to_json_string_type(self):
        """Testing to_json_string type"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)

    def test_to_json_string_None(self):
        """Testing to_json_string type"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_empty(self):
        """Testing to_json_string empty"""
        json_dictionary = Base.to_json_string('')
        self.assertEqual(json_dictionary, "[]")

    def test_save_to_file_len(self):
        """Testing JSON string rep len"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as file:
            self.assertEqual(
                    len(file.read()), len(str(
                        [{"x": 2, "id": 6, "width": 10, "y": 8, "height": 7}, {
                            "x": 0, "id": 7, "width": 2, "y": 0, "height": 4}]
                        )))

    def test_save_to_file_None(self):
        """Testing JSON string rep len"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string(self):
        """Testing JSON string rep"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{
            'id': 89, 'width': 10, 'height': 4}, {
                'id': 7, 'width': 1, 'height': 7}])

    def test_from_json_string_None(self):
        """Testing JSON string rep with None param"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty(self):
        """Testing JSON string rep with None param"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string('')
        self.assertEqual(list_output, [])

    def test_create(self):
        """Testing instance with set attributes"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        sys.stdout = sys.__stdout__
        self.assertEqual(r1, "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r2, "[Rectangle] (1) 1/0 - 3/5")


if __name__ == '__main__':
    unittest.main()
