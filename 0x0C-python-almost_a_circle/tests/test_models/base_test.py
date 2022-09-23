#!/usr/bin/python3
"""test file for base.py"""
from models.base import Base
#Base = __import__('base').Base
import unittest


class TestBase(unittest.TestCase):
    """base class testing"""

    def test_init(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

if __name__ == "__main__":
    unittest.main()
