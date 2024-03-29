#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        """Test that Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Test instantiation with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test instantiation with one argument."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test instantiation with two arguments."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Test instantiation with three arguments."""
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Test instantiation with four arguments."""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """ Test instantiation with five arguments."""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """ Test instantiation with more than five arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """ Test that width is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """ Test that height is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """ Test that x is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """ Test that y is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """ Test instantiation with width."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        """ Test instantiation with width."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        """ Test instantiation with height."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        """ Test instantiation with height."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        """ Test instantiation with x."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        """ Test instantiation with x."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        """ Test instantiation with y."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        """ Test instantiation with y."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


if __name__ == "__main__":
    unittest.main()
