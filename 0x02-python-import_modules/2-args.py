#!/usr/bin/python3


if __name__ == "__main__":

    import sys
 
    args = sys.argv[1:]
    no_of_args = len(args)

    if no_of_args == 0:
        print(f'{no_of_args} arguments.')
    elif no_of_args == 1:
        print(f'{no_of_args} argument:')
    else:
        print(f'{no_of_args} arguments:')

    for count, arg in enumerate(args, start=1):
        print(f'{count}: {arg}')
