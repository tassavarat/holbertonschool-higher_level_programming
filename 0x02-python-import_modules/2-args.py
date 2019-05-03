#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = len(argv) - 1
    if arguments is 0:
        print("{:d} arguments.".format(arguments))
    elif arguments is 1:
        print("{:d} argument:".format(arguments))
        print("{:d}: {}".format(1, argv[1]))
    else:
        print("{:d} arguments:".format(arguments))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
