from art import logo
print(logo)
from random import randint
EASY = 10
HARD = 5
turn = 0

def set_level():
    level = input("Chosse a difficulty. Type 'easy' or 'hard' ")
    if level == 'easy':
        return  EASY
    else:
        return HARD

def check_answer(guess,answer,turn):
    if guess > answer:
        print("Too High")
        return turn - 1
    elif guess < answer:
        print("Too Low")
        return turn - 1
    else:
        print(f"You got it right {answer}")


def game():
    print("Welcome to the number guessing game")
    print("I'm thinking of number between 1 to 100")
    answer = randint(1,100)

    turn = set_level()

    guess = 0
    while guess != answer:
        print(f"You have only {turn} left")

        guess = int(input("Make a guess "))

        turn = check_answer(guess,answer,turn)

        if turn == 0:
            print("You are out of moves")
        else:
            print("Guess again")

game()