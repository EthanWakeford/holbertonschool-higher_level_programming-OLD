#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = []
    for i in range(2):
        int_a = 0
        int_b = 0
        if len(tuple_a) > i:
            int_a = tuple_a[i]
        if len(tuple_b) > i:
            int_b = tuple_b[i]
        sum.append(int_a + int_b)
    new_tup = (sum[0], sum[1])
    return (new_tup)
