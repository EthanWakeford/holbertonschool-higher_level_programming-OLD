#!/usr/bin/python3
"""module to check if object inherits from class"""


def inherits_from(obj, a_class):
    """checks if object inherits from class"""

    return (issubclass(type(obj), a_class))
