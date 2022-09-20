#!/usr/bin/python3
"""Has a class student"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of class"""

        if attrs is None:
            return (vars(self))
        attributes = {}
        for key, value in vars(self).items:
            if key in attrs:
                attributes[key] = value
        return (attributes)
