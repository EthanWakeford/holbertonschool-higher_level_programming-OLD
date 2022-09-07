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
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError(size must be an integer)
        if size < 0:
            raise ValueError(size must be >= 0)
