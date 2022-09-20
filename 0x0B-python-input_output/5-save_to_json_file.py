#!/usr/bin/python3
"""writes a python object to a json file"""


def save_to_json_file(my_obj, filename):
    """writes a python object to a json file"""

    import json
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
