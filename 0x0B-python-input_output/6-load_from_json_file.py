#!/usr/bin/python3

"""Defines a JSON file-reading function."""
import json


def load_from_json_file(my_obj, filename):
    """Create a Python object from a JSON file."""
    with open(filename, "w") as fd:
        return json.loads(fd)
