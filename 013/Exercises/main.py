# Exercise 1: Describe Problem
def my_function():
   for i in range(1, 20):
     if i == 20:
       print("You got it")
my_function()
# Solution 1: "You got it" is never printed as the range goes from 1 to 19. To solve it, just set range (1, 21)

# Exercise 2:Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
# Solution 2: The randint function generates a random number between 1 and 6. The elements of the list start at index 0. So they will have indexes from 0 to 5.
# If random number 6 is generated it will result in an error. The solution is randint(0, 5)

# Exercise 3: Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
   print("You are a millenial.")
elif year > 1994:
   print("You are a Gen Z.")
# Solution 3: The problem is when inserting the date 1994. To solve it, just elif year >= 1994:

# Exercise 4: Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")
# Solution 4: input returns a string that you can compare against an integer. To solve, just set age = int(input (....))
# Also the print must be an f string, print(f"...")

# Exercise 5: Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
# Sulution 5: The word_per_page line has == which is a comparison not an assignment. Just put an =. Furthermore, the print must be done with f string

# Exercise 6: Use a Debugger
def mutate(a_list):
   b_list = []
   for item in a_list:
     new_item = item * 2
   b_list.append(new_item)
   print(b_list)

mutate([1,2,3,5,8,13])
# Solution 6: b_list.append is outside the for loop

# Exercise 7: Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# The code needs to print the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
""""
Solution 7: 
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
"""
# Exercise 8: Read this the code in main.py
# Spot the problems.
# Modify the code to fix the program.

year = input("Which year do you want to check?")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
# Solution 8: input returns a string that you can compare against an integer. To solve, just set age = int(input (....))

# Exercise 9: Read this the code in main.py
# Spot the problems.
# Modify the code to fix the program.
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
# Solutzion 9: number% 2 = 0 is a wrong assignment. You have to put ==