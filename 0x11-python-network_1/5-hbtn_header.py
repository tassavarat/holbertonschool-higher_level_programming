#!/usr/bin/python3
"""Takes URL, sends request to URL, displays value of X-Request-Id in header"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    print(get(argv[1]).headers.get("X-Request-Id"))
