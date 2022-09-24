#!/usr/bin/python3
"""test file for rectangle.py"""
from models.rectangle import Rectangle
import unittest
unittest.TestLoader.sortTestMethodsUsing = None


class TestRectangle(unittest.TestCase):
    """rectangle class testing"""

    def test_docstrings(self):
        """Checks module and function docstrings"""
        modDocstring = __import__('models').rectangle.__doc__
        self.assertIsNotNone(modDocstring)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test__str__(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r1.__str__(), 'sdf')
        r1 = Rectangle(5, 3, 1, 6, 100)
        self.assertEqual(r1.__str__(), 'sdf')

    def test_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_errors(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 'f')
        with self.assertRaises(TypeError):
            r1 = Rectangle('d', 3)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 'sadf', 5)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 'dsf')
        with self.assertRaises(TypeError):
            r1 = Rectangle(None)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -5)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 3)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -2, 45)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 4, -6)
        