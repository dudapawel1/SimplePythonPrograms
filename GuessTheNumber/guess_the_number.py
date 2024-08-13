import random


def guess_number():

    number_to_guess = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    user_number = 0

    while user_number != number_to_guess:
        try:
            user_number = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_number < number_to_guess:
            print("Too low!")
        elif user_number > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the correct number.")


if __name__ == "__main__":
    guess_number()
