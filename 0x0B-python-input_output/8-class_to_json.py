#!/usr/bin/python3
"""Puts all attributes of an object into a dictionary"""


def class_to_json(obj):
    """Puts all attributes of an object into a dictionary"""

    att_dict = {}
    valid_types = ['list', 'dict', 'str', 'int', 'bool']
    obj_attributes = dir(obj)
    for i in obj_attributes:
        if type(i) in valid_types:
            att_dict[type[i]] = i

    return (att_dict)
