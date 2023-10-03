#!/usr/bin/python3

def fizzbuzz():
    """In a range of numbers from 1 - 100,
    function prints Fizz if number is a multiple of 3,
    Buzz if number is a multiple of 5, and
    FizzBuzz if number is a multiple of 3 and 5."""

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
