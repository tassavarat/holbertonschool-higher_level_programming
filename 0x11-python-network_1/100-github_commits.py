#!/usr/bin/python3
"""Users github api to list out 10 most recent commits from specified repo
and user
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get("https://api.github.com/repos/{}/{}/commits".
                     format(argv[2], argv[1])).json()
    length = len(r)

    if length > 10:
        for i in range(10):
            print("{}: {}".format(r[i].get("sha"), r[i].get("commit").
                                  get("author").get("name")))
    else:
        for i in range(length):
            print("{}: {}".format(r[i].get("sha"), r[i].get("commit").
                                  get("author").get("name")))
