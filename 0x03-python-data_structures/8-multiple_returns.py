#!/usr/bin/python3

def multiple_returns(sentence):
    char_tuple = ()
    if sentence == "":
        return (0, None)
    char_tuple = (len(sentence), sentence[0])
    return char_tuple
