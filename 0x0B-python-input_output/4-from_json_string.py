#!/usr/bin/python3
"""returns a python object from json string"""


def from_json_string(my_str):
    """returns a python object from json string"""

    import json
    return (json.loads(my_str))
