#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    products = [(x * y) for x, y in my_list]
    divides = [(y) for x, y in my_list]
    return (sum(products) / sum(divides))
