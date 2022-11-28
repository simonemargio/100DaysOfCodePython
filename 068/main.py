#  Created by Simone Margio
#  www.simonemargio.im

# Problem: generate a random password that meets specific conditions
# Condition: password length must be 15 characters long.
#            It must contain at least 4 upper case letters,
#            2 digit
#            3 special symbol
# Input: nil
# Output: random password


import random
import string


def random_password():
    randomElements = string.ascii_letters + string.digits

    password = random.sample(randomElements, 8)
    password += random.sample(string.ascii_uppercase, 4)
    password += random.sample(string.digits, 2)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password


password = random_password()
print(f"Password generated: {password}\nLen: {len(password)}")
