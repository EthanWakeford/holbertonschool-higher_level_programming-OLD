#!/usr/bin/python3
"""Has a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class for a square"""

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
