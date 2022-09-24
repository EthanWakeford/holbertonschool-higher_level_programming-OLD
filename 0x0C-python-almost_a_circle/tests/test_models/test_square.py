#!/usr/bin/python3
"""test file for Square.py"""
from models.square import Square
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from io import StringIO
from unittest.mock import patch

class TestSquare(unittest.TestCase):
    """Square class testing"""

    def test_docstrings(self):
        """Checks module and function docstrings"""
        modDocstring = __import__('models').square.__doc__
        self.assertIsNotNone(modDocstring)
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.area.__doc__)
        self.assertIsNotNone(Square.display.__doc__)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test__str__(self):
        s1 = Square(1, 1, 1, 1)
        self.assertEqual(s1.__str__(), '[Square] (1) 1/1 - 1')
        s1 = Square(5, 1, 6, 100)
        self.assertEqual(s1.__str__(), '[Square] (100) 1/6 - 5')

    def a_test_init(self):
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        r2 = Square(2)
        self.assertEqual(r2.id, 2)
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_errors(self):
        with self.assertRaises(TypeError):
            s1 = Square('d')
        with self.assertRaises(TypeError):
            s1 = Square(1, 'sadf', 5)
        with self.assertRaises(TypeError):
            s1 = Square(1, 3, 'dsf')
        with self.assertRaises(TypeError):
            s1 = Square(None)
        with self.assertRaises(ValueError):
            s1 = Square(0, 3)
        with self.assertRaises(ValueError):
            s1 = Square(1, -2, 45)
        with self.assertRaises(ValueError):
            s1 = Square(1, 4, -6)

    def test_area(self):
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)
        s1 = Square(8, 0, 0, 12)
        self.assertEqual(s1.area(), 64)

    def test_display(self):
        s1 = Square(2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")
        s1 = Square(3, 1, 1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), "\n ###\n ###\n ###\n")

    def test_update(self):
        s1 = Square(10, 10, 10)
        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), '[Square] (89) 3/10 - 2')
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), '[Square] (89) 3/4 - 2')
        s1 = Square(10, 10, 10, 10)
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s1.__str__(), '[Square] (89) 3/1 - 2')
        s1.update(x=1, size=2, y=3)
        self.assertEqual(s1.__str__(), '[Square] (89) 1/3 - 2')

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 9)
        self.assertEqual(s1.to_dictionary(), {'x': 2, 'y': 1, 'id': 9, 'size': 10})
        r2 = Square(1)
        r2.update(**(s1.to_dictionary()))
        self.assertEqual(r2.__str__(), '[Square] (9) 2/1 - 10')
        self.assertIsNot(s1, r2)
