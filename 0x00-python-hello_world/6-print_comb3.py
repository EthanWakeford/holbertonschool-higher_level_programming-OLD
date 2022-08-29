#!/usr/bin/python3
for i in range(8):
    for j in range(10):
        if j > i:
            print("{}".format(i, j), sep="", end=", ")
print("{}".format(89))
