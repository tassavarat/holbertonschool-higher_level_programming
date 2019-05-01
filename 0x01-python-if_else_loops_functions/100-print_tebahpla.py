#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 is 1:
        c -= ord(' ')
    print("{}".format(chr(c)), end="")
