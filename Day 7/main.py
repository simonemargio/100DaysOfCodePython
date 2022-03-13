import random

""""
# Hangman project
Create the hangman game
"""

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def checkWin():
    for i in display:
        if i == "_":
            return True
    return False

word_list = ["asd", "bitcoin", "telegram", "apple", "wow", "dogecoin", "simone"]
lives = 6
display = []

chosenWord = random.choice(word_list)
for i in chosenWord:
    display += "_"

while checkWin():
    find = False
    guess = (input("Guess a letter\n->").lower())

    for i in range(len(chosenWord)):
        if chosenWord[i] == guess:
            display[i] = guess
            find = True
    if not find:
        print(stages[lives])
        lives -= 1
    if lives < 0:
        break
    print(display)

if lives > 0:
    print("You Win!")
else:
    print("You Lose!")




