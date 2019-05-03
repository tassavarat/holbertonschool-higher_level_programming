#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    i = 1
    for i, args in enumerate(argv[i:], 1):
        sum += int(argv[i])
    print("{:d}".format(sum))
