#  Created by Simone Margio
#  www.simonemargio.im

# Problem: create a function that takes a number that represents a person's programming language score, and returns
# an alphabetised list of programming languages they are proficient in. Arbitrarily assigned points for each language
# are listed below:
# Language	Points
# C#	        1
# C++	        2
# Java      	4
# JavaScript	8
# PHP	        16
# Python	    32
# Ruby	        64
# Swift         128
# Input: number
# Output: list
# Es: 25 -> C# JavaScript PHP
# Es: 100 -> Java Python Ruby

languages = ["C#", "C++", "Java", "JavaScript", "PHP", "Python", "Ruby", "Swift"]


def get_languages(num):
    out = ""
    for i in range(len(languages)):
        if num & (1 << i):
            out += languages[i] + " "

    return out


print(get_languages(53))