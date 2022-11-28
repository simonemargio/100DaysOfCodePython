#  Created by Simone Margio
#  www.simonemargio.im

# Problem: generate a random date between given start and end dates
# Input: start date: 1/1/2018 end date: 4/6/2022
# Output: random date between 1/1/2018 and 4/6/2022

import random
import time

START_DATE = "1/1/2018"
END_DATE = "4/6/2022"


def random_date(start_date, end_date):
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(start_date, dateFormat))
    endTime = time.mktime(time.strptime(end_date, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate


print("Random date between:", START_DATE, " and ", END_DATE)
print("New random date = ", random_date(START_DATE, END_DATE))
