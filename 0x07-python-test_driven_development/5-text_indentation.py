#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    tokens = ".?:"
    count = 1
    for i in range(0, len(text)):
        if text[i] in tokens:
            print(text[count:i + 1].strip())
            print()
            count += 1
    print(text[count:].strip())
