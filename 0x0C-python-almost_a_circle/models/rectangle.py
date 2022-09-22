#!/usr/bin/python3
"""Has a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class for a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width attribute"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """sets the width attribute"""
        self.__width = width

    @property
    def height(self):
        """gets the height attribute"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """sets the height attribute"""
        self.__height = height

    @property
    def x(self):
        """gets the x attribute"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """sets the x attribute"""
        self.__x = x

    @property
    def y(self):
        """gets the y attribute"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """sets the y attribute"""
        self.__y = y
