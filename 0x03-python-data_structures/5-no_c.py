#!/usr/bin/python3

def no_c(my_string):
    new_strings = []

    for str in my_string:
        if str != 'c' and str != 'C':
            new_strings.append(str)
    return "".join(new_strings)
