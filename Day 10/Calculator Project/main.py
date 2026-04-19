from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# n1 = 0
# n2 = 0

# add_it = add
# subtract_it = subtract
# multiply_it = multiply
#                # (n1, n2))
# divide_it = divide

calc = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(calc)
def calculator():
    print(logo)
    should_continue = True
    n1 = int(input("What is the first number?\n"))

    while should_continue:

        # def calc_input():

        op = input("Which mathematical operator do you want?\n"
                   "+\n"
                   "-\n"
                   "*\n"
                   "/\n")
        n2 = int(input("What is the second number?\n"))

        # if op == "+":
        #     # multiply_it(n1, n2)
        #     # print(calc["*"])
        #     output = calc["+"](n1, n2)
        #     print(f"{output}")
        # if op == "-":
        #     # multiply_it(n1, n2)
        #     # print(calc["*"])
        #     output = calc["-"](n1, n2)
        #     print(f"{output}")
        # if op == "*":
        #     # multiply_it(n1, n2)
        #     # print(calc["*"])
        #     output = calc["*"](n1, n2)
        #     print(f"{output}")
        # if op == "/":
        #     # multiply_it(n1, n2)
        #     # print(calc["*"])
        #     output = calc["/"](n1, n2)
        #     print(f"{output}")
        output = calc[op](n1, n2)
        print(f"{n1} {op} {n2} = {output}")
        choice = input("Do you want to continue with another number? Type 'yes' or 'no'.\n")
        if choice == "yes":
            n1 = output
            # calc_input()
        else:
            # should_continue = False
            # n1 = 0
            # n2 = 0
            calculator()
calculator()