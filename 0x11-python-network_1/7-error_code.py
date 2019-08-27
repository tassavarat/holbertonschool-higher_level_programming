#!/usr/bin/python3
"""Takes URL, sends request to URL, displays body of response"""
if __name__ == "__main__":
    import requests
    from sys import argv

    status = requests.get(argv[1]).status_code
    if status >= 400:
        print("Error code:", status)
    else:
        print(requests.get(argv[1]).text)
