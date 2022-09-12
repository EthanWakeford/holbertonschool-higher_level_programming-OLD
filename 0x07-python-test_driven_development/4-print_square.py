#!/usr/bin/python3
'''this module is used to practice doctests in python'''


def print_square(size):
    '''function prints a square with sides of size ~size~'''
    if type(size) == float:
        size = int(size)
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print("#" * size)
