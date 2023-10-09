#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisible = []

    for d in range(len(my_list)):
        if my_list[d] % 2 == 0:
            divisible.append(True)
        else:
            divisible.append(False)
    return divisible
