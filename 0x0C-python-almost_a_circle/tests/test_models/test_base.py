#!/usr/bin/python3
"""Unittest for Base"""
import unittest
from models.base import Base


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
        with self.assertRaises(NameError):
            Base(a)


if __name__ == '__main__':
    unittest.main()
