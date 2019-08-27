#!/usr/bin/python3
"""Takes in a string and sends a search request to Star Wars API"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get("https://swapi.co/api/people/?search={}".
                     format(argv[1])).json()
    print("Number of results:", r["count"])
    for k in r["results"]:
        print(k["name"])
