#!/usr/bin/python3
"""this module creates a class square"""


class Square:
    """this class is used to create a square with a size attribute"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """creates a size attribute >= 0"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints a square defined by size"""
        if self.__size == 0:
            print()
            return
        for i in range(1, self.__size + 1):
            print('#' * self.__size)
