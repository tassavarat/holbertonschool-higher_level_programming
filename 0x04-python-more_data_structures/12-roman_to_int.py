#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if type(roman_string) == str:
        largest = 1
        rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for s in roman_string[::-1]:
            if s in rn:
                if rn[s] >= largest:
                    res = res + rn[s]
                    largest = rn[s]
                else:
                    res -= rn[s]
    return res
