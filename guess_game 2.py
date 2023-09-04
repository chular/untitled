import random

def guess_the_number(x):
    random_number = random.randint(1, x)
    attempts = 0
    correct_guesses = 0

    while True:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        attempts += 1

        if guess > random_number:
            print("Too high! Try again.")
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            correct_guesses += 1
            print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")
            break

    return attempts, correct_guesses

def computer_guess_the_number(x):
    low = 1
    high = x
    attempts = 0

    print(f"Think of a number between 1 and {x} and let the computer guess it.")

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").strip().lower()

        if feedback == 'c':
            print(f"The computer guessed your number {guess} correctly in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'H' for too high, 'L' for too low, or 'C' for correct.")

    return attempts

def calculate_score(attempts, correct_guesses):
    if attempts <= 10 and correct_guesses / attempts >= 0.7:
        return 10
    return 0

if __name__ == "__main__":
    print("Welcome to the Number Guessing Games!")
    game_choice = input("Choose a game: '1' for you guessing, '2' for computer guessing: ")

    if game_choice == '1':
        max_range = int(input("Enter the maximum number for the guessing range: "))
        attempts, correct_guesses = guess_the_number(max_range)
    elif game_choice == '2':
        max_range = int(input("Enter the maximum number for the guessing range: "))
        attempts = computer_guess_the_number(max_range)
    else:
        print("Invalid choice. Please enter '1' or '2' for the game you want to play.")

    user_score = calculate_score(attempts, correct_guesses)
    print(f"Your score: {user_score} credits")
