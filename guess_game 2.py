import random


def get_int_input(prompt, min_value=1):
    """
    Safely get an integer input from the user.
    Keeps asking until a valid number is entered.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Please enter a number greater than or equal to {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def user_guesses_number(max_range):
    """
    User tries to guess a randomly generated number.
    Returns the number of attempts.
    """
    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_range}.")

    while True:
        guess = get_int_input("Your guess: ")
        attempts += 1

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            return attempts


def computer_guesses_number(max_range):
    """
    Computer guesses the user's number using binary search logic.
    Returns the number of attempts.
    """
    low = 1
    high = max_range
    attempts = 0

    print(f"\nThink of a number between 1 and {max_range}.")
    print("Respond with:")
    print("  H = too high, L = too low, C = correct")

    while low <= high:
        guess = (low + high) // 2  # Binary search
        attempts += 1

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").strip().lower()

        if feedback == "c":
            print(f"🤖 I guessed your number in {attempts} attempts!")
            return attempts
        elif feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else:
            print("Invalid input. Please enter H, L, or C.")

    print("Something went wrong. Please ensure consistent answers.")
    return attempts


def calculate_score(attempts):
    """
    Simple scoring system based on efficiency.
    """
    if attempts <= 5:
        return 10
    elif attempts <= 10:
        return 5
    return 0


def main():
    print("🎮 Welcome to the Number Guessing Game!")

    while True:
        print("\nChoose a game mode:")
        print("1 - You guess the number")
        print("2 - Computer guesses your number")
        print("3 - Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            max_range = get_int_input("Enter the maximum number: ")
            attempts = user_guesses_number(max_range)

        elif choice == "2":
            max_range = get_int_input("Enter the maximum number: ")
            attempts = computer_guesses_number(max_range)

        elif choice == "3":
            print("Thanks for playing! 👋")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        score = calculate_score(attempts)
        print(f"Your score: {score} points")


if __name__ == "__main__":
    main()
