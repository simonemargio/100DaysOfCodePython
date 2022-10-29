#  Created by Simone Margio
#  www.simonemargio.im

# Problem: solve the Fibonacci sequence using recursion
# Input: any number (ex: 15)
# Output: fibonacci sequence (ex: 610 for 15)


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fibonacci(n - 1) + (fibonacci(n - 2)))


num = int(input("Enter the number:"))
print(f"Output: {fibonacci(num)}")
