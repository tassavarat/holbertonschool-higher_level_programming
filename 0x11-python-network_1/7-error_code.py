#!/usr/bin/python3
"""Takes URL, sends request to URL, displays body of response"""
if __name__ == "__main__":
    import requests
    from sys import argv

    print("Error code:", requests.get(argv[1]).status_code)
