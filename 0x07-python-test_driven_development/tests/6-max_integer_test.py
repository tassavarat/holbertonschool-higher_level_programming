#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_string(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_diff_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'c'])

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, None])

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
