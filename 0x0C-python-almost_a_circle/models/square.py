#!/usr/bin/python3
"""holds a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the size property"""
        return self.width

    @size.setter
    def size(self, size):
        """sets the size property"""
        self.width = size
        self.height = size

    def __str__(self):
        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}')
