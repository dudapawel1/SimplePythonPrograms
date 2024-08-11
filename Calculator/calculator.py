from functions import *

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    print("S. to Stop")

    choice = input("Enter your choice: ").upper()

    if choice == "S":
        break

    first_number = int(input("Type 1st number: "))
    second_number = int(input("Type 2nd number: "))

    if choice == '1':
        add(first_number, second_number)
    elif choice == '2':
        subtract(first_number, second_number)
    elif choice == '3':
        multiply(first_number, second_number)
    elif choice == '4':
        divide(first_number, second_number)
    else:
        print("Wrong choice!")
