#!/usr/bin/python3
"""has a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class for a rectangle"""

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))

    def area(self):
        """returns area of the rectangle"""
        return (self.__width * self.__height)
