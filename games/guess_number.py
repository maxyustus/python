import random

EASY_LEVEL_ATTEMPTS = 5
HARD_LEVEL_ATTEMPTS = 10


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def check_answer(guess, answer, attempts):
    """check q_answer against guess, returns the number or attempts remained"""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The q_answer was {guess}.")


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)

    attempts = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts  remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


play_game()