#!/usr/bin/python3
"""Takes a letter and sends POST request to http://0.0.0.0:5000/search_user
with letter as parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}

    r = requests.post("http://0.0.0.0:5000/search_user", data=data).json()
    try:
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r["id"], r["name"]))
    except Exception:
        print("Not a valid JSON")
