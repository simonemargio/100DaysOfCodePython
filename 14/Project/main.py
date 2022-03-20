import art
import data
import random

print(art.logo)
score = 0

def initGame():
    indexA = random.randint(0, len(data.product) - 1)
    return indexA

def randomProduct(indexA):
    indexB = random.randint(0, len(data.product) - 1)
    while indexA == indexB:
        indexB = random.randint(0, len(data.product)-1)
    return indexB

def winner(compareA, compareB):
    if compareA['date'] < compareB['date']:
        return 'A'
    else:
        return 'B'

def engine(indexA):
    global score
    indexB = randomProduct(indexA)
    compareA = data.product[indexA]
    compareB = data.product[indexB]
    print(f"Compare A: {compareA['name']}, {compareA['company']} product.")
    print(art.vs)
    print(f"Against B: {compareB['name']}, {compareB['company']} product.")
    choise = input("Who was introduced first? Type 'A' or 'B':")

    if choise.lower() == winner(compareA, compareB).lower():
        score += 1
        print(f"You're right! Current score: {score}")
        engine(indexB)
    else:
        print(f"Sorry, that's wrong. The {compareA['name']} product came out in {compareA['date']} and {compareB['name']} in {compareB['date']} Final score: {score}")


indexA = initGame()
engine(indexA)


