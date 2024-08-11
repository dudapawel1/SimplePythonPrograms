def add(first_number, second_number):
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")


def subtract(first_number, second_number):
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")


def multiply(first_number, second_number):
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")


def divide(first_number, second_number):
    if second_number != 0:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
    else:
        print("You can't divide by 0")
