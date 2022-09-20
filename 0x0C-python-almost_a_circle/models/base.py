#!/usr/bin/python3
"""has a base class"""


class Base:
    """class base"""

    self.__nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        """gets the id"""
        return (self.id)

    @id.setter
    def id(self, id):
        """sets the id"""
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
