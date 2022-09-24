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
        """str doc"""
        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}')

    def update(self, *args, **kwargs):
        """updates the attributes for square, args order goes:
        id, size, x, y"""
        attr_list = ['id', 'size', 'x', 'y']
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for arg, attr in zip(args, attr_list):
            setattr(self, attr, arg)

    def to_dictionary(self):
        """returns all attributes in dictionary format"""
        return ({'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.size})
