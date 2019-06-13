#!/usr/bin/python3
"""Unittest for Rectangle"""
import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Rectangle class test"""
    def setUp(self):
        """Resets nb_objects"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Prints out the id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertTrue(type(r3), Rectangle)

    def test_one_param(self):
        """Passing one parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_all_param(self):
        """Passing all parameters"""
        r1 = Rectangle(1, 1, 1, 1, 1)

    def test_string(self):
        """Passing string"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "string")
        with self.assertRaises(TypeError):
            r1 = Rectangle("string", 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")

    def test_no_param(self):
        """Passing nothing"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_excess_param(self):
        """Excess parameters"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1, 1, 1)

    def test_float(self):
        """Float parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1.2, 1, 1, 3)

    def test_NaN(self):
        """NaN parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, float("nan"), 1, 1)

    def test_inf(self):
        """inf parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, float("inf"), 1, 1)

    def test_unknown(self):
        """unknown parameter"""
        with self.assertRaises(NameError):
            r1 = Rectangle(a)

    def test_None(self):
        """None parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, None, 1, 1)

    def test_neg(self):
        """Neg parameter"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2, 1, 1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, -4)

    def test_zero(self):
        """Neg parameter"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

    def test_area(self):
        """Prints out area"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

    def test_display(self):
        """Tests rectangle output"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "##\n##\n"

    def test_str(self):
        """Tests __str__"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (12) 2/1 - 4/6\n"

    def test_display_x_y(self):
        """Tests rectangle output with x and y"""
        output = StringIO()
        sys.stdout = output
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == " ###\n ###\n"

    def test_update(self):
        """Test update"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        r1.update(89, 2, 3, 4, 5)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_extra(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 6, 7)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_no_param(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 10/10 - 10/10\n"

    def test_kwargs(self):
        """Test kwargs normal behavior"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 1/3 - 4/2\n"

    def test_kwargs_extra_keys(self):
        """Test kwargs normal behavior"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4, betty=88)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 1/3 - 4/2\n"

    def test_to_dict_rep(self):
        """Test dictionary representation"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {
            'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

    def test_to_dict_rep_update(self):
        """Testing dictionary representation update"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/9 - 10/2\n")


if __name__ == '__main__':
    unittest.main()
