#  Created by Simone Margio
#  www.simonemargio.im

# Problem: use pandas for merge two data frames using the following condition
# Condition:  1 create two data frames using the following two Dicts
#             2 merge two data frames
#             3 append the second data frame as a new column to the first data frame
# Input: Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
#        car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
# Output:
# Company   Price  horsepower
# 0  Toyota   23845         141
# 1   Honda   17995          80
# 2     BMV  135925         182
# 3    Audi   71400         160

import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
print(carsDf)