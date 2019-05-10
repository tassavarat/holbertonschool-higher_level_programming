#!/usr/bin/python3
def roman(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return 0


def roman_to_int(roman_string):
    i = 0
    d = 0
    if isinstance(roman_string, str):
        while i < len(roman_string):
            s1 = roman(roman_string[i])
            if i + 1 < len(roman_string):
                s2 = roman(roman_string[i + 1])
                if s1 >= s2:
                    d += s1
                    i += 1
                else:
                    d = d + s2 - s1
                    i += 2
            else:
                d += s1
                i += 1
    return d
