#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''class to test max_integer function'''


    def test_valid(self):
        '''tests valid inputs'''
        self.assertEqual(max_integer([1, 5, 3]), 5)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer(), None)


    def test_invalid(self):
        '''tests invalid inputs'''
        self.assertRaises(TypeError, max_integer, [1, 2, 'hello'])
