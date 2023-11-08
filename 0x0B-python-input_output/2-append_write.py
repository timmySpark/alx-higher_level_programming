#!/usr/bin/python3

""" Definees Append function"""


def append_write(filename="", text=""):
    """ appends a sring to the end of a file
    """
    with open(filename, 'a', encoding="utf-8") as fd:
        return fd.write(filename, text)
