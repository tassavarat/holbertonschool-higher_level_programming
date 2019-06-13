#!/usr/bin/python3
"""Unittest for Base"""
import os
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Base class test"""
    def setUp(self):
        """Resets nb_objects"""
        Base._Base__nb_objects = 0

    def test_type(self):
        """Testing for instance type"""
        b = Base()
        self.assertTrue(type(b) == Base)

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
        self.assertEqual(b1.id, 1)

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
        self.assertTrue(type(json_dictionary), dict)

    def test_to_json_string_len_square(self):
        """Testing to_json_string len"""
        r1 = Square(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(len(json_dictionary), len(str([{
            "x": 7, "size": 10, "id": 8, "y": 2}])))
        self.assertTrue(type(json_dictionary), dict)

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

    def test_save_to_file_rec(self):
        """Testing JSON string rep rec"""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_square(self):
        """Testing JSON string rep square"""
        Square.save_to_file([])
        with open("Square.json") as file:
            self.assertEqual(file.read(), "[]")
            os.remove("Square.json")

    def test_save_to_file_None(self):
        """Testing JSON string rep None"""
        Square.save_to_file(None)
        with open("Square.json") as file:
            self.assertEqual(file.read(), "[]")
            os.remove("Square.json")

    def test_save_to_file_len_Square(self):
        """Testing JSON string rep len"""
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json") as file:
            self.assertEqual(
                    len(file.read()), len(str(
                        [{"x": 7, "id": 8, "size": 10, "y": 2}, {
                            "x": 4, "id": 7, "size": 2, "y": 0}]
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
        self.assertTrue(type(list_output), list)

    def test_from_json_string_rec(self):
        """Testing JSON string rep"""
        list_input = [
            {'id': 89, 'size': 10},
            {'id': 7, 'size': 1}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output, [{
            'id': 89, 'size': 10}, {
                'id': 7, 'size': 1}])
        self.assertTrue(type(list_output), list)

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

    def test_from_json_string_empty(self):
        """Testing JSON string rep with None param"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string('')
        self.assertTrue(type(list_output), list)

    def test_create(self):
        """Testing instance with set attributes"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/0 - 3/5\n")
        self.assertTrue(type(r1) == Rectangle)

        output = StringIO()
        sys.stdout = output
        r1 = Square(3)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (3) 0/0 - 3\n")
        self.assertTrue(type(r1) == Square)

    def test_create2(self):
        """Testing instance with set attributes 2"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/0 - 3/5\n")

    def test_create2(self):
        """Testing instance with set attributes 2"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_create_TypeError(self):
        """Testing instance with set attributes TypeError"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(None)

    def test_create_TypeError_int(self):
        """Testing instance with set attributes TypeError int"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(1, 2, 3)

    def test_create_TypeError_string(self):
        """Testing instance with set attributes TypeError string"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create("string")

    def test_create_TypeError_string(self):
        """Testing instance with set attributes TypeError string"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(NameError):
            r2 = Rectangle.create(**betty)

    def test_load_from_file(self):
        """Testing list of instances"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        print(list_rectangles_output[0])
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 2/8 - 10/7\n")

        output = StringIO()
        sys.stdout = output
        print(list_rectangles_output[1])
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (2) 0/0 - 2/4\n")
        self.assertTrue(type(list_rectangles_output), list)

        output = StringIO()
        sys.stdout = output
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        print(list_squares_output[0])
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (5) 0/0 - 5\n")

        output = StringIO()
        sys.stdout = output
        print(list_squares_output[1])
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (6) 9/1 - 7\n")
        self.assertTrue(type(list_squares_output), list)


if __name__ == '__main__':
    unittest.main()
