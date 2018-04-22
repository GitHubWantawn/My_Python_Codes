# CTI-110 P5HW2
# Random Number Guessing Game
# Juan Hernaez
# 04/21/2018

# This is a guess the "secret number" game.

import random
import sys

def guessNumber():
    number = random.randint(1,100)
    count = 1
    guess = int(input("Enter your guess between 1 and 100: "))

    while guess !=number:
        count+=1
        if guess > (number + 10):
            print("Too high!")
        elif guess < (number - 10):
            print("Too low!")
        elif guess > number:
            print("Getting warm but still high!")
        elif guess < number:
            print("Getting warm but still Low!")

        guess = int(input("Try again "))

    if guess == number:
        print("You rock! You guessed the secret number in ", count, " tries!")
        return

guessNumber()

again = str(input("Do you want to play again? (type 'y' for yes or any other key for no): "))
if again == "y":
    guessNumber()
else:
    sys.exit(0)
