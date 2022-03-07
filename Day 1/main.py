"""
Exercise 1
Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.
Notes to print:
    Day 1 - Python Print Function
    The function is declared like this:
    print('what to print')
"""

# Solution 1
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

"""
Exercise 2
Look at the code below. There are errors in all of the lines of code. Fix the code so that it runs without errors.
Code to fix: 
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")

When you run your program, it should print the following:
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n.
"""

# Solution 2
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print("e.g. print(\"Hello \" + \"world\")")
print("New lines can be created with a backslash and n.")

"""
Exercise 3
Write a program that prints the number of characters in a user's name. 
"""

# Solution 3
print( len( input("Print your name?")))

"""
Exercise 4
Write a program that switches the values stored in the variables a and b.
"""
a = input("a: ")
b = input("b: ")

# Solution 4
tmp = a
a = b
b = tmp
print("a: " + a)
print("b: " + b)

"""
Exercise 5 
Write the appropriate instructions based on the comments.
"""
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.

# Solution 5
print("Hello " + input("Hey, what's your name?\n") + " nice to meet u.")
cityName = input("So, what are the city that u gre up in?\n")
petName = input("And the name of your pet?\n")
print("Wow, I think that this name is awesome for your band: " + petName + " " + cityName + "\nCool bro, true?")