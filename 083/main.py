#  Created by Simone Margio
#  www.simonemargio.im

# Problem: you will be given a list of 32-bit unsigned integers. Flip all the bits 1 -> 0 and 0 -> 1 and return the result as an integer.
# Input: unsigned integer
# Output: inverted unsigned integer
# Es: input-> 1 , output -> 4294967294
# Es: input-> 4 , output -> 4294967291

def int_to_binary(n):
    return '{:032b}'.format(int(n))


def inverted_number(n):
    new_binary_sequence = ""
    for bit in n:
        if bit == "0":
            new_binary_sequence += "1"
        else:
            new_binary_sequence += "0"

    return new_binary_sequence


def binary_to_int(n):
    return int(n, 2)


n = input("Enter the number:")

n = int_to_binary(n)
print(f"Binary 32: {n}")

n = inverted_number(n)
print(f"Inverted: {n}")

n = binary_to_int(n)
print(f"Inverted new number: {n}")
