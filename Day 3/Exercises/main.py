"""
Exercise 1
Write a program that works out whether if a given number is an odd or even number.
"""

# Solution 1
number = int(input("Which number do you want to check?\n->"))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

"""
Exercise 2
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""

# Solution 2
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

"""
Exercise 3
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.
"""

# Solution 3
year = int(input("Which year do you want to check? "))
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

"""
Exercise 4
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""

# Solution 4
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

"""
Exercise 5
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
"""

# Solution 5
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower() + name2.lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")

sumTrue = str(t + r + u + e)
sumLove = str(l + o + v + e)
sum = int(sumTrue + sumLove)

if sum <= 10 or sum >= 90:
    print(f"Your score is {sum}, you go together like coke and mentos.")
elif 40 <= sum <= 50:
    print(f"Your score is {sum}, you are alright together.")
else:
    print(f"Your score is {sum}.")