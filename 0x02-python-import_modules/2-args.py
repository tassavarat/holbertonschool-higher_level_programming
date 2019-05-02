#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = len(argv) - 1
    i = 1
    if arguments is 0:
        print("{:d} arguments.".format(arguments))
    elif arguments is 1:
        print("{:d} argument:".format(arguments))
    else:
        print("{:d} arguments:".format(arguments))
        for i, args in enumerate(argv[i:], 1):
            print("{:d}: {}".format(i, argv[i]))
