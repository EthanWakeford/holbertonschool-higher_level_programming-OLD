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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation to a file"""
        if not list_objs:
            list_objs = []
        dicts = [cls.to_dictionary(obj) for obj in list_objs]
        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        pass

    @classmethod
    def create(cls, **dictionary):
        """creates a new object"""
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        if cls.__name__ == 'Square':
            obj = cls(1)
        obj.update(**dictionary)
        return (obj)
