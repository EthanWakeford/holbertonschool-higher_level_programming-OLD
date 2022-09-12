#!/usr/bin/python3
'''this module is to practice doctests with'''


def say_my_name(first_name, last_name=""):
    '''this function prints a string that uses arguments
     for first name and last name'''
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
