import math

"""
Exercise 1
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
"""
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Solution 1
def paint_calc(height,width,cover):
    res = int(math.ceil((height*width)/cover))
    print(f"You'll need {res} cans of paint.")


"""
Exercise 2
You need to write a function that checks whether if the number passed into it is a prime number or not.
"""

n = int(input("Check this number: "))
prime_checker(number=n)

# Solution 2
def prime_checker(number):
    checkPrime = True
    for i in range(2,number):
        if number % i == 0:
            checkPrime = False

    if checkPrime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")