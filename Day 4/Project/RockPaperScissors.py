import random

"""
Rock Paper Scissors
Make a rock, paper, scissors game
Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
"""
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Solution
playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n->"))

if playerChoice == 0:
    print(rock + "Rock")
elif playerChoice == 1:
    print(paper + "Paper")
else:
    print(scissors + "Scissors")

pcChoice = random.randint(0,2)

if pcChoice == 0:
    print(rock + "Rock")
elif pcChoice == 1:
    print(paper + "Paper")
else:
    print(scissors + "Scissors")

if (playerChoice == 0 and pcChoice == 2) or (playerChoice == 1 and pcChoice == 0) or (playerChoice == 2 and pcChoice == 1):
    print("You win!")
elif playerChoice == pcChoice:
    print("Tie")
else:
    print("You lose!")
