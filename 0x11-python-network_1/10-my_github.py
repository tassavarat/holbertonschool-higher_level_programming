#!/usr/bin/python3
"""Takes Github credentials and uses Github API to display id"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get("https://api.github.com/user",
                     auth=(argv[1], argv[2])).json()
    if "id" not in r:
        print("None")
    else:
        print(r["id"])
