#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for m, l in a_dictionary.items():
            if l == value:
                del a_dictionary[m]
                break

    return (a_dictionary)
