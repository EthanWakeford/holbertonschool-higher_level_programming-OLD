#!/usr/bin/python3
"""has a base class"""


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if not list_dictionaries:
            return "[]"
        import json
        return (json.dumps(list_dictionaries))
