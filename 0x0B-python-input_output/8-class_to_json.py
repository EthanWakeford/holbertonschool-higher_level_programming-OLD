#!/usr/bin/python3
"""Puts all attributes of an object into a dictionary"""


def class_to_json(obj):
    """Puts all attributes of an object into a dictionary"""

    return (vars(obj))
