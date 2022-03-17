
import random

"""
Exercise 1
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
"""
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Solution 1

num = random.randint(0,1)

if num == 0:
    print("Heads")
else:
    print("Tails")


"""
Exercise 2
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
"""
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Solution 2
print( names[random.randint(0, len(names)-1)] + " is going to buy the meal today!")


"""
Exercise 3
Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
The first digit is the vertical column number and the second digit is the horizontal row number.
"""
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Solution 3
map[int(position[1])-1][int(position[0])-1] = "X"

print(f"{row1}\n{row2}\n{row3}")