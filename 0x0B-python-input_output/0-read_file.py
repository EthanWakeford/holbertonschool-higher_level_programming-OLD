#!/usr/bin/python3
"""reads a text file and prints it out"""


def read_file(filename=""):
    """reads a text file and prints it out"""

    with open(filename, encoding="utf-8") as f:
        print(f.read())
