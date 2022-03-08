"""
Project Tip calculator
Calculate the tip based on the bill, percentage and number of people who have to pay
"""

# Solution
bill = float(input("What was the total bill?\n->$"))
percentageTip = (int(input("What percentage tip would you like to give? 10, 12 or 15?\n->")) / 100)
peopleSplit = int(input("How many people to slip the bill?\n->"))
totalBill = bill + (bill * percentageTip)
billForPerson = round((totalBill / peopleSplit), 2)

print(f"Each person should pay ${billForPerson}")