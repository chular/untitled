# Number Guessing Game

A console-based Python number guessing game featuring two interactive modes:

the player guesses a randomly generated number, or

the computer guesses a number the player is thinking of using an efficient binary search strategy.

This project demonstrates Python fundamentals, algorithmic thinking, input validation, and clean code structure.

## Features

Two game modes:

Player Guessing Mode

Computer Guessing Mode

Binary search algorithm for optimized computer guesses

Safe input handling (prevents crashes on invalid input)

Scoring system based on efficiency

Replayable game loop

Modular and well-documented code
   

## How to Play

Ensure you have Python 3.x installed.

Clone this repository or download the source code.

Open a terminal in the project directory.

Run the game using:

`python number_guessing_game.py`


## Game Modes

### 1. Player Guesses the Numbe
The computer selects a random number within a chosen range.

You attempt to guess the number.

Feedback is provided after each guess:

Too high

Too low

Correct

The game tracks the number of attempts taken.

### Let the Computer Guess Your Number

In this game mode, you think of a number between 1 and the specified maximum range. The computer will make guesses and you provide feedback on whether its guess is too high, too low, or correct. The computer will try to guess your number with the fewest attempts possible.

## Scoring

Your score is calculated based on the number of attempts and correct guesses:
- If you guess the number yourself, you earn credits based on how quickly and accurately you guess.
- If you let the computer guess your number, your score is based on the number of attempts the computer takes.

## License

This project is currently not licensed under any specific license. It is for personal use and may be used and distributed without the owner's permission.



