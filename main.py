# Calculator operations.
operations = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y,
              '^': lambda x, y: x ** y,
              '%': lambda x, y: x % y}


def handle_operation(num1, num2, operator):
    if operator not in operations:
        print('Invalid operator!')
        return None

    # Call the function from the dictionary.
    return operations[operator](num1, num2)


# This function runs the calculator app.
def calculator():
    # Print welcome message.
    print('Welcome to the calculator app by Mariusz Matyszczak!')

    while True:
        # Get the numbers and the operator from the user.
        num1 = float(input('Enter the first number: '))
        operator = input('Enter the operator (+, -, *, /, ^, %): ')
        num2 = float(input('Enter the second number: '))

        # Calculate the result.
        result = handle_operation(num1, num2, operator)
        if result is None:
            continue

        print('The result is: ' + str(result))
        # Ask the user if they want to continue.
        answer = input('Do you want to continue? (y/n): ')
        # If the user doesn't want to continue, exit the program.
        if answer == 'n':
            break

    # Cya!
    print('Thank you for using the calculator!')


# Main function.
if __name__ == '__main__':
    calculator()
