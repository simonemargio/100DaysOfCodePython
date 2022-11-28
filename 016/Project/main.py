from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def engine(menu, maker, money):
    choise = input("What would you like (" + menu.get_items() + "):")

    if choise != "off":
        if choise == "report":
            maker.report()
            money.report()
        else:
            drink = menu.find_drink(choise)
            if drink is not None:
                if maker.is_resource_sufficient(drink):
                    if money.make_payment(drink.cost):
                        maker.make_coffee(drink)
        engine(menu,maker,money)
    else:
        print("Shutdown, bye 👋")

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
engine(menu, maker, money)