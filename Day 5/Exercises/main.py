"""
Exercise 1
You are going to write a program that calculates the average student height from a List of heights.
"""
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Solution 1
i = 0
total = 0

for student in student_heights:
    i += 1
    total += student

total = round(total/i)
print(total)


"""
Exercise 2
You are going to write a program that calculates the highest score from a List of scores.
"""
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Solution 2
max = 0
for i in student_scores:
    if max < i:
        max = i

print(f"The highest score in the class is: {max}")


"""
Exercise 3
You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
"""

# Solution 3
total = 0

for i in range(2,101):
    if i % 2 == 0:
        total += i

print(total)


"""
Exercise 4
You are going to write a program that automatically prints the solution to the FizzBuzz game.
Your program should print each number from 1 to 100 in turn.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
"""

# Solution 4
for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
