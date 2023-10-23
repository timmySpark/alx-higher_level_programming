#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """print the first x element of a list and only integers

    Args:
        my_list (list): lists of elements
        x (int): elements to be accessed in my_list

    Returns:
        The real number of integers printed
    """

    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print("")
    return(count)
