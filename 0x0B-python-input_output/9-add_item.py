#!/usr/bin/python3
"""9-add_item module
Adds all arguments to a Python list, then save them to a file
"""
from sys import argv
from os import path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
if path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
for x in range(1, len(argv)):
    my_list.append(argv[x])
save_to_json_file(my_list, filename)
