#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for i, c in enumerate(str):
        if i is n:
            s += ''
        else:
            s += c
    return s
