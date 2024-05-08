# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import math
import random

# Get the user input
lower = int(input("Enter the lower range"))
upper = int(input("Enter the upper range"))

# Generating random number
rndmNum = random.randint(lower, upper)
print(rndmNum)

guess = int(input("Guess a number: "))

if rndmNum == guess:
    print("Congratulations you did it.")
elif rndmNum > guess:
    print("You guessed too small!")
elif rndmNum < guess:
    print("You Guessed too high!")
