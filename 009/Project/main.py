"""
Project Secret Auction
"""

import art


print(art.logo)
participants = {}
print("Welcome to the secret auction program.")
while True:
    name = input("What is your name?\n->")
    bid = input("What's your bid?\n-$")
    participants[name] = bid
    cont = input("Are there any other bidders? Type 'yes' or 'no'.\n->")
    if cont != "yes":
        break

print(participants)

winner = [0,""]
for key in participants:
     value = int(participants[key])
     if value > winner[0]:
         winner[0] = value
         winner[1] = key

print(f"The winner is {winner[1]} with a bit of ${winner[0]}.")