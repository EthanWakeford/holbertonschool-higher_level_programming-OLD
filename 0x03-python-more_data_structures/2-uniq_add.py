#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    nums = []
    for i in my_list:
        if i not in nums:
            sum += i
            nums.append(i)
    return (sum)
