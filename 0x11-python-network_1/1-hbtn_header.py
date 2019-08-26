#!/usr/bin/python3
"""Takes in URL, sends request, displays value of X-Request-Id found in header
"""
from urllib import request
from sys import argv

print(argv[1])
with request.urlopen(argv[1]) as f:
    print(f.info().get("X-Request-Id"))
