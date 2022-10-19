#  Created by Simone Margio
#  www.simonemargio.im

# Problem: get all values from the dictionary and add them to a list without duplicates
# Input: dictionary = {'jan': 66, 'feb': 52, 'march': 66, 'April': 87, 'May': 52, 'June': 35,'july': 54, 'Aug': 87, 'Sept': 54}
# Output: [66, 52, 87, 35, 54]


dictionary = {'jan': 66, 'feb': 52, 'march': 66, 'April': 87, 'May': 52, 'June': 35, 'july': 54, 'Aug': 87, 'Sept': 54}

# Output list
numbers = list()

# Iterate every dictionry's values
for val in dictionary.values():
    # Check if value isn't present in the list
    if val not in numbers:
        numbers.append(val)

print("Input:", dictionary.values())
print("Output:", numbers)
