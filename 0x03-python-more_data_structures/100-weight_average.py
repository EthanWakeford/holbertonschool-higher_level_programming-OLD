#!/usr/bin/python3
def weight_average(my_list=[]):
    products = [(x * y) for x, y in my_list]
    divides = [(y) for x, y in my_list]
    return (sum(products) / sum(divides))
