#!/usr/bin/python3
"""Takes URL, sends request to URL, displays value of X-Request-Id in header"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    r = get(argv[1])
    print(r.headers["X-Request-Id"])
