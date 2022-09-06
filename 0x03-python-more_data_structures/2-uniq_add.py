#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    nums = [ x for x in range(0, 10)]
    for i in my_list:
        if i in nums:
            sum += i
            nums.remove(i)
    return (sum)
