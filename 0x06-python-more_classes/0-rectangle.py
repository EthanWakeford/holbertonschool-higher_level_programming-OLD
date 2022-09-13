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
        if type(value) != int:
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
        elif height <0 :
            raise ValueError('height must be >= 0')
        else:
            self.__height = height
