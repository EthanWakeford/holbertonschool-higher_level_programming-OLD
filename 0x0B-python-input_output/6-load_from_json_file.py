#!/usr/bin/python3
"""creates a python object from a json file"""


def load_from_json_file(filename):
    """creates a python object from a json file"""

    import json
    with open(filename, encoding='utf-8') as f:
        return (json.loads(f.read()))
