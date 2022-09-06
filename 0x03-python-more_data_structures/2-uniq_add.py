#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    nums = set(my_list)
    for i in nums:
        sum += i
    return (sum)
