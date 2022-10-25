#  Created by Simone Margio
#  www.simonemargio.im

# Problem: check if two sets have any elements in common. If yes, display the common elements
# Input: set_1 = {10, 20, 80, 40, 55, 32, 0}
#        set_2 = {60, 70, 80, 91, 12, 0, 45, 8}
# Output: {0, 10, 80}


set_1 = {10, 20, 80, 40, 55, 32, 0}
set_2 = {60, 70, 80, 91, 12, 0, 45, 10, 8}

if set_1.isdisjoint(set_2):
    print("Two sets don't have items in common")
else:
    print(f"Two sets have items in common: {set_1.intersection(set_2)}")
