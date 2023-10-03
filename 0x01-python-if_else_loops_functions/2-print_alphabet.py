#!/usr/bin/python3
""" Prints ASCII Alphabets in lowercase, not followed by a new line """

for i in range(97, 123):
    print('{}'.format(chr(i)), end='')
