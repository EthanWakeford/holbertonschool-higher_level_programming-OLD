#!/usr/bin/python3
"""this module has a class Rectangle"""


class Rectangle():
    """class rectangle with height and width properties"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        """height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.width * 2))

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        str = ("{}\n".format('#' * self.__width) * self.__height)
        return (str)
