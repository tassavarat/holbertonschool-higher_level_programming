#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as f:
    status = f.read()
    print("Body response:\n"
          "\t- type: {}\n"
          "\t- content: {}\n"
          "\t- utf8 content: {}".format(type(status), status,
                                        status.decode("utf-8")))
