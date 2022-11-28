"""
Project: coffee machine
"""
import data

def printReport():
    print(f"Water: {data.resources['water']}\nMilk: {data.resources['milk']}\nCoffee: {data.resources['coffee']}\nMoney: ${data.resources['money']}")

def checkResources(drink):
    res = ""
    for ingredient in data.MENU[drink]["ingredients"]:
        if data.resources[ingredient] < data.MENU[drink]["ingredients"][ingredient]:
            res += ingredient + ","
    return res

def updateData(drink):
    for ingredient in data.MENU[drink]["ingredients"]:
        data.resources[ingredient] -= data.MENU[drink]["ingredients"][ingredient]


def makeDrink(coins, drink):
    change = round(coins - data.MENU[drink]["cost"],2)
    if change != 0:
        print(f"Here is ${change} in change.")
    data.resources["money"] += data.MENU[drink]["cost"]
    print(f"Here is you {drink} ☕️, enjoy!\n")

def checkCoins(drink):
    sum = int(input("How many quarters?:")) * 0.25
    sum += int(input("How many dimes?:")) * 0.10
    sum += int(input("How many nickles?:")) * 0.05
    sum += int(input("How many pennies?:")) * 0.01

    if sum < data.MENU[drink]["cost"]:
        print(f"Sorry that's not enough money (insert: {sum}, cost of {drink}: ${data.MENU[drink]['cost']}. Money refounded.")
    else:
        makeDrink(sum, drink)
        updateData(drink)

def engine():
    choise = input("What would you like? (espresso, latte, cappuccino):")

    if choise != "off":
        if choise == "report":
            printReport()
        else:
            resource = checkResources(choise)
            if resource != "":
                print(f"There is not enough: {resource} sorry!")
            else:
                checkCoins(choise)
        engine()
    else:
        print("Shutdown, bye 👋")

engine()