#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints X elements of a list

    Args:
        My_list (list) : The list to prints elements from
        x (int) : Numbers of elements of my_list to be printed

    Returns:
        Numbers of element printed
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
