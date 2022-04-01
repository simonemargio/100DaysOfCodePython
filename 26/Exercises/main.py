"""
Exercise 1
You are going to write a List Comprehension to create a new list called squared_numbers.
This new list should contain every number in the list numbers but each number should be squared.
"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Solution 1
squared_numbers = [number * number for number in numbers]
print(squared_numbers)


"""
Exercise 2
You are going to write a List Comprehension to create a new list called result. 
This new list should only contain the even numbers from the list numbers.
"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Solution 2
result = [n for n in numbers if n%2==0]
print(result)


"""
Exercise 3
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result which contains the numbers that are common in both files.
"""

# Solution 3
with open("file1.txt", mode="r") as file_1:
    list_1 = file_1.read().splitlines()

with open("file2.txt", mode="r") as file_2:
    list_2 = file_2.read().splitlines()

result = [int(n) for n in list_1 if n in list_2]

print(result)

"""
Exercise 4
You are going to use Dictionary Comprehension to create a dictionary called result that takes 
each word in the given sentence and calculates the number of letters in each word.
Try Googling to find out how to convert a sentence into a list of words.
Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Solution 4
result = {word:len(word) for word in sentence.split()}
print(result)
