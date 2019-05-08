#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        else:
            s += c
    return s
