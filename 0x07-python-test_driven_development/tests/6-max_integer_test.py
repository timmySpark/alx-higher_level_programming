#!/usr/bin/python3

"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def setUp(self):
        self.empty_list = []
        self.order_list = [1, 2, 3, 4]
        self.unordered_list = [4, 3, 2, 1]
        self.negative = [-2, -6, -4, -8]
        self.max_beginning = [9, 7, 5, 1]
        self.max_end = [1, 5, 7, 9]
        self.one_man = [7]
        self.floats = [2.3, 4.5, 5.5, 6.7]
        self.mixup = [1, 3.3, 5.5, 6, 10]
        self.string = "Dylan"
        self.list_strings = ["Tyler", "is", "a", "dude"]

    def test_empty_list(self):
        """Test an Empty list"""
        self.assertEqual(max_integer(self.empty_list), None)

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer(self.order_list), 4)

    def test_unordered_list(self):
        """Test an Unordered list of integers"""
        self.assertEqual(max_integer(self.unordered_list), 4)

    def test_negative(self):
        """Test a Negative list of integers"""
        self.assertEqual(max_integer(self.negative), -2)

    def test_max_begin(self):
        """Test when max is at the beginning of integers"""
        self.assertEqual(max_integer(self.max_beginning), 9)

    def test_max_begin(self):
        """Test when max is at the end of integers"""
        self.assertEqual(max_integer(self.max_end), 9)

    def test_one_element(self):
        """Test when list has one element"""
        self.assertEqual(max_integer(self.one_man), 7)

    def test_floats(self):
        """Test when lists has a lot of floated integers"""
        self.assertEqual(max_integer(self.floats), 6.7)

    def test_mixup(self):
        """Test when lists has a mixture of floats and integers"""
        self.assertEqual(max_integer(self.mixup), 10)

    def test_max_lett(self):
        """Test for the highest letter (max)"""
        self.assertEqual(max_integer(self.string), 'y')

    def test_strings(self):
        """Test for the highest string (max)"""
        self.assertEqual(max_integer(self.list_strings), "is")

if __name__ == "__main__":
    unittest.main()
