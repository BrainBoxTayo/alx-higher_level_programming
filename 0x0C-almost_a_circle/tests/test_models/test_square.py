#!/usr/bin/python3
"""Defines unittests for models/square.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        """ Test instantiation of a Square object."""
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        """ Test instantiation of a Square object."""
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        """ Test instantiation with no arguments."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """ Test instantiation with one argument."""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """ Test instantiation with two arguments."""
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        """ Test instantiation with three arguments."""
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """  Test instantiation with four arguments."""
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        """ Test instantiation with more than four arguments."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        """ Test that __size is private."""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """ Test instantiation with size."""
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        """ Test instantiation with size."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        """ Test instantiation with width."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        """ Test instantiation with height."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        """ Test instantiation with x coordinate."""
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        """ Test instantiation with y coordinate."""
        self.assertEqual(0, Square(10).y)


if __name__ == "__main__":
    unittest.main()
