#!/usr/bin/python3
"""Takes in URL and email, sends POST request using given parameters, displays
body of response decoded in utf-8"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    email = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], email)
    with request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
