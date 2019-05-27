#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after ., ?, and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    delimiter = ['.', '?', ':']
    s = ""

    for c in text:
        s += c
        if c in delimiter:
            print(s.strip())
            print()
            s = ""
    print(s.strip(), end='')
    if text is "\n":
        print()
