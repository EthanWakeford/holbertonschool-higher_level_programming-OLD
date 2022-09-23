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
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]), \
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

    def test_save_to_file(self):
        from models.rectangle import Rectangle
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), \
                '[{"x": 2, "y": 8, "id": 3, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 4, "height": 4, "width": 2}]')
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string('[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]')\
            , [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])

if __name__ == "__main__":
    unittest.main()
