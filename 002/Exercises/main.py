"""
Exercise 1
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
"""

# Solution 1
twoDigitNumber = input("Type a two digit number: ")
print((int(twoDigitNumber[0]) + int(twoDigitNumber[1])))

"""
Exercise 2
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
"""

# Solution 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
print(int(float(weight) / (float(height) ** 2)))

"""
Exercise 3
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
https://waitbutwhy.com/2014/05/life-weeks.html
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
"""

# Solution 3
age = int(input("What is your current age?"))
yearsLive = (90 - age)
days = (yearsLive * 365)
weeks = (yearsLive * 52)
months = (yearsLive * 12)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")