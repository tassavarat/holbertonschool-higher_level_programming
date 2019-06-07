#!/usr/bin/python3
"""5-to_json_tring module
"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object string
    """
    return json.dumps(my_obj, ensure_ascii=False)
