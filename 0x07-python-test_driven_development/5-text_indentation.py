#!/usr/bin/python3
'''this module is to practice doctests in python'''


def text_indentation(text):
    '''function prints text with 2 newlines inserted
    after every . ? and :'''
    if type(text) != str:
        raise TypeError('text must be a string')

    newline = False
    for i in text:
        if not newline or i != ' ':
            print(i, end='')
        if i in ['.', '?', ':']:
            print("\n\n", end='')
            newline = True
        else:
            newline = False
