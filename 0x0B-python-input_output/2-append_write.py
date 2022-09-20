#!/usr/bin/python3
"""contains a function to append a string to a text file"""


def write_file(filename="", text=""):
    """appends a string to a text file"""

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)

    return (len(text))
