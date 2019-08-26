#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests package"""
import requests

r = requests.get("https://intranet.hbtn.io/status")
print("Body response:\n"
      "\t- type: {}\n"
      "\t- content: {}".format(type(r.text), r.text))
