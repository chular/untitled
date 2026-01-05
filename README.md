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

### 1. Player Guesses the Number
The computer selects a random number within a chosen range.

You attempt to guess the number.

Feedback is provided after each guess:

Too high

Too low

Correct

The game tracks the number of attempts taken.

### 2. Computer Guesses the Number

You think of a number within a chosen range.

The computer attempts to guess your number using binary search logic.

You respond with:

H → Too high

L → Too low

C → Correct

The computer minimizes the number of attempts efficiently

## Scoring System

| Attempts     | Score     |
| ------------ | --------- |
| 5 or fewer   | 10 points |
| 6–10         | 5 points  |
| More than 10 | 0 points  |


## Project Structure

Clear separation of concerns using functions

Central `main()` function to manage program flow

Reusable input validation utility

Algorithm-focused logic for computer guessing


## Skills Demonstrated

Python programming

Control flow and loops

Functions and modular design

Input validation and error handling

Binary search algorithm

Refactoring and code maintainability


## Future Improvements

Object-Oriented Programming (OOP) version

Unit tests

Difficulty levels

Graphical User Interface (GUI)

Persistent score tracking

## License

This project is currently unlicensed and intended for learning and portfolio purposes.
You are free to use, modify, and distribute it





