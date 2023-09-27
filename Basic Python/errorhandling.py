try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    opp = input("Enter Operator: ")

    if opp == "+":
        print(num1 + num2)

    elif opp == "-":
        print(num1 - num2)

    elif opp == "/":
        print(num1 / num2)

    elif opp == "*":
        print(num1 * num2)

    else:
        print("Invalid, Enter opp: * or + or / or -")

except ValueError:
    print('please enter a number')
except:
    print('please enter a number')
