# Numero random da 1 a 100
# Difficolta easy 10 tentativi, hard 5 tentativi

import random
import art

def randomNumber():
    return random.randint(1, 101)


print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

number = randomNumber()

# print(f"Psss {number}")

while attempts > 0:
    guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess:"))
    attempts -= 1
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {number}.")
        break

if attempts == 0:
    print("You're run out of guesses, you lose.")