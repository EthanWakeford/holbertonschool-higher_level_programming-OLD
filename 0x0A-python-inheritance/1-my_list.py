#!/usr/bin/python3
"""has class MyList which inherits from list"""


class MyList(list):
    """has personal methods for list"""

    def print_sorted(self):
        """prints a sorted list"""
        if not self:
            print(self)
        else:
            lst = self[:]
            lst.sort()
            print(lst)
