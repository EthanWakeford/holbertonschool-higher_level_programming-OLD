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
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """gets the height attribute"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """sets the height attribute"""
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """gets the x attribute"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """sets the x attribute"""
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """gets the y attribute"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """sets the y attribute"""
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """displays the rectangle visually"""
        print('\n' * self.__y, sep='', end='')
        disp = '{}{}\n'.format(' ' * self.__x, '#' * self.__width)
        print(disp * self.__height, end='')

    def __str__(self):
        return (f'[Rectangle] ({self.id}) '
                f'{self.__x}/{self.__y} - '
                f'{self.__width}/{self.__height}')

    def update(self, *args):
        attr_list = ['id', 'width', 'height', 'x', 'y']
        for arg, attr in zip(args, attr_list):
            setattr(self, attr, arg)
