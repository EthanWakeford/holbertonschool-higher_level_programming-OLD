#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print("0 arguments")
    exit()
count = 1
print("{} argument".format(len(argv)-1), "s"if len(argv) > 1 else None, sep="")
for i in argv[1:]:
    print("{}: {}".format(count, argv[count]))
    count += 1
