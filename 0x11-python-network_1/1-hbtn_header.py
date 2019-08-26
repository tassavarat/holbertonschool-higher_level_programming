#!/usr/bin/python3
"""Takes in URL, sends request, displays value of X-Request-Id found in header
"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as f:
        print(f.info().get("X-Request-Id"))
