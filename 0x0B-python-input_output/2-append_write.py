#!/usr/bin/python3

""" Definees Append function"""


def append_write(filename="", text=""):
    """ appends a sring to the end of a file
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, 'a', encoding="utf-8") as fd:
        return fd.write(text)
