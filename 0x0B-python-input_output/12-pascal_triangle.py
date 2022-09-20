#!/usr/bin/python3
"""pascals triangle"""


def pascal_triangle(n):
    """creates a pascals triangle"""

    if n <= 0:
        return ([])
    big_list = [[1]]
    l1 = [1]
    for i in range(1, n):
        l2 = [1]
        for j in range(len(l1)):
            if j < len(l1) - 1:
                l2.append(l1[j] + l1[j + 1])
        l2.append(1)
        big_list.append(l2)
        l1 = l2
    return (big_list)
