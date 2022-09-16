#!/usr/bin/python3
"""Has a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class for a square"""

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """returns area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """prints info about the square object"""
        return ('[Square] {}/{}'.format(self.__size, self.__size))
