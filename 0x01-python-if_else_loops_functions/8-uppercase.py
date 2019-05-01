#!/usr/bin/python3
def islower(c):
    return ord(c) in range(ord('a'), ord('z') + 1)


def uppercase(str):
    s = ""
    for i in str:
        if islower(i):
            s += chr(ord(i) - ord(' '))
        else:
            s += i
    print("{}".format(s))
