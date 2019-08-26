#!/usr/bin/python3
"""Takes a URL and email, sends POST request using parameters, displays body
of response
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    print(requests.post(argv[1], data={"email": argv[2]}).text)
