import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("-" * 40)

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too Low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too High! Try a lower number.\n")
        else:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt(s)!")
            break

guessing_game()