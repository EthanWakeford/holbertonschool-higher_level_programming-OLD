#!/usr/bin/python3
'''this module is to practice doctests in python'''


def text_indentation(text):
    '''function prints text with 2 newlines inserted
    after every . ? and :'''
    if type(text) != str:
        raise TypeError('text must be a string')

    for i in text:
        print(i, end='')
        if i in ['.', '?', ':']:
            print("\n\n", end='')
