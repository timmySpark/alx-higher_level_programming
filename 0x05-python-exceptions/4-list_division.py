#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divide elements by elements 2 lists

    Args:
        my_list_1 (list): first list (divisible)
        my_list_2 (list) : second list (divisor)
        list_length (int): number of elements to be divided

    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i]/my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
