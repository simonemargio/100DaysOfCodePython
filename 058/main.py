#  Created by Simone Margio
#  www.simonemargio.im

# Problem: create a function that is a Hashtag Generator by using the following rules:
# 1 The output must start with a hashtag (#)
# 2 Each word in the output must have its first letter capitalized
# 3 If the final result, a single string, is longer than 140 characters, the function should return false
# 4 If either the input (str) or the result is an empty string, the function should return false
# Input: String
# Output: #String
# Es: "    Hello     World   " -> #HelloWorld
# Es: "" -> False
# Es: "a cute    Doge" -> #ACuteDoge

def generate_hashtag(txt):
    return '#' + txt.title().replace(" ", "") if 0 < len(txt) < 140 else False


print(generate_hashtag("  Hello     World         "))
print(generate_hashtag(""))
print(generate_hashtag("a cute    Doge"))

