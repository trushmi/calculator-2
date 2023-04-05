"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )




while True:
    user_input = input("Enter your equation > ")
    tokens = user_input.split(' ')
    operator = tokens[0]

    if operator == "q":
        break

    num1 = int(tokens[1])
    if len(tokens) > 2:
        num2 = int(tokens[2])
    else:
        num2 = None


    if operator == '+':
        print(float(add(num1, num2)))
        continue
    elif operator == '-':
        print(float(subtract(num1, num2)))
    elif operator == '*':
        print(float(multiply(num1, num2)))
    elif operator == '/':
        print(float(divide(num1, num2)))
    elif operator == 'square':
        print(float(square(num1)))
    elif operator == 'cube':
        print(float(cube(num1)))
    elif operator == 'pow': #pow
        print(float(power(num1, num2)))
    elif operator == 'mod':
        print(float(mod(num1, num2)))

