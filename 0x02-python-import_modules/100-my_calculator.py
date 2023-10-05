#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv[1:]
    no_of_args = len(args)

    if no_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    op = args[1]
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(args[0])
    b = int(args[2])
    res = operators[op](a, b)
    print(f"{a} {op} {b} = {res}")
