#!/usr/bin/python3
def uppercase(str):
    word = []
    for i in range(len(str)):
        word.append(str[i])
        if 97 <= ord(word[i]) <= 122:
            word[i] = chr(ord(word[i]) - 32)
    str = "".join(word)
    print("{}".format(str))
