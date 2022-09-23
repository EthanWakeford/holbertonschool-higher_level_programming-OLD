#!/usr/bin/python3
"""test file for base.py"""
from models.base import Base
#Base = __import__('base').Base
import unittest


class TestBase(unittest.TestCase):
    """base class testing"""

    def test_docs(self):
        modDocstring = __import__('models').base.__doc__
        self.assertIsNotNone(modDocstring)
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)


    def test_init(self):
        """tests init method"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base(-2)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, -2)

    
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]), \
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')


if __name__ == "__main__":
    unittest.main()
