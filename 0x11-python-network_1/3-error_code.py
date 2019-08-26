#!/usr/bin/python3
"""Takes URL, sends request to URL, displays body of response decoded in utf-8
"""
if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
