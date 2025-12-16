import random

def guessing_game():
    """Simple number guessing game between 1 and 50."""
    target = random.randint(1, 50)
    attempts = 0

    print("Guess the number (between 1 and 50)")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target:
                print("Too low! Try again.")
            elif guess > target:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    guessing_game()
