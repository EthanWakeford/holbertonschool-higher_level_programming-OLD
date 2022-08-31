#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) == 1:
        print("0 arguments.")
        exit()
    count = 1
    print("{} argument".format(len(argv)-1),  end="")
    print("s:" if len(argv) > 2 else ":")
    for i in argv[1:]:
        print("{}: {}".format(count, argv[count]))
        count += 1
if __name__ == "__main__":
    main()
