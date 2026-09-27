import random

def number_guessing_game():
    print("=== Number Guessing Game ===")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("\nCongratulations! You guessed the number!")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")


number_guessing_game()
