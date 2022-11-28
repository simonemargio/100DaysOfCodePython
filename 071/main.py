#  Created by Simone Margio
#  www.simonemargio.im

# Problem: follow the steps below and develop the solutions in the fewest lines
# Create a class Smoothie and do:
# 1 Create an instance attribute called ingredients
# 2 Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie
# 3 Create a get_price method which returns the number from get_cost plus the  number from get_cost multiplied by 1.5.
#   Round to two decimal places.
# 4 Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive
#   sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie".
#   Remember to change "-berries" to "-berry".
#
# Ingredient	Price
# Strawberries	$1.50
# Banana	    $0.50
# Mango	        $2.50
# Blueberries	$1.00
# Raspberries	$1.00
# Apple	        $1.75
# Pineapple	    $3.50
#
# Es: s1 = Smoothie(["Banana"]), s1.get_ingredients ➞ ["Banana"], s1.get_cost() ➞ "$0.50", s1.get_price() ➞ "$1.25", s1.get_name() ➞ "Banana Smoothie"
# Es: s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"]), s2.get_ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]
#     s2.get_cost() ➞ "$3.50", s2.get_price() ➞ "$8.75", s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"


prices = {
    "Strawberries": "$1.50",
    "Banana": "$0.50",
    "Mango": "$2.50",
    "Blueberries": "$1.00",
    "Raspberries": "$1.00",
    "Apple": "$1.75",
    "Pineapple": "$3.50"
}


class Smoothie:

    def __init__(self, lst_items):
        self.ingredients = lst_items[:]

    def __get_cost__(self):
        return sum(float(prices[item][1:]) for item in self.ingredients)

    def get_ingredients(self):
        return self.ingredients

    def get_cost(self):
        return '${:.2f}'.format(self.__get_cost__())

    def get_price(self):
        return '${:.2f}'.format(round(self.__get_cost__() * 2.5, 2))

    def get_name(self):
        return (' '.join(sorted(self.ingredients)).replace('berries', 'berry') +
                (' Smoothie' if len(self.ingredients) == 1 else ' Fusion'))


s1 = Smoothie(["Banana"])

print(s1.get_ingredients())
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())

s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])

print(s2.get_ingredients())
print(s2.get_cost())
print(s2.get_price())
print(s2.get_name())
