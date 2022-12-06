#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: November 30, 2022
# This program asks the user for two numbers and
# what operation they would like to do to them.
# The program will then calculate it and display it to the user


# This function calculate the value of two numbers given the operator
def calculate(sign, first_number, second_number):
    # Declared Variable
    calculation = 0

    # Calculates the addition if user wanted addition
    if sign == "+":
        calculation = first_number + second_number
    # Calculates the subtraction if user wanted subtraction
    elif sign == "-":
        calculation = first_number - second_number
    # Calculates the multiplication if user wanted multiplication
    elif sign == "*":
        calculation = first_number * second_number
    # Calculates the division if user wanted division
    elif sign == "/":
        calculation = first_number / second_number
    # Calculates the modulus if user wanted modulus
    elif sign == "%":
        calculation = first_number % second_number

    # Returns calculation to main()
    return calculation


def main():
    # Checks for exceptions
    try:
        # Asks user for what operation they want to do
        user_operation = input(
            "Enter which operation you'd like to perform (+, -, *, /, %): "
        )

        # Asks user for their two numbers
        user_first_num = float(input("Enter your first number: "))
        user_second_num = float(input("Enter your second number: "))

    # In the event of an exception
    except Exception:
        print("You must enter valid numbers!")

    # Valid Input for numbers
    else:
        # Ensures that user entered a valid operation
        if (
            user_operation != "+"
            and user_operation != "-"
            and user_operation != "*"
            and user_operation != "/"
            and user_operation != "%"
        ):
            print("You must enter a valid operation symbol!")
        # User entered a valid operation
        else:
            # Calls function to do the calculation for the user
            user_result = calculate(user_operation, user_first_num, user_second_num)

            # Displays the calculation to the user
            print(
                f"The calculation: {user_first_num} {user_operation} {user_second_num} = {user_result}"
            )


if __name__ == "__main__":
    main()
